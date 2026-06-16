"""
SHAP + Cross-City Feature Selection Protocol for OSM Variables
==============================================================

Implements robust, transferable feature selection pipeline for OSM-derived 
variables in PSF-CTF framework.

Core idea: 
  - Axis 1 (Predictive Power): Feature importance via SHAP
  - Axis 2 (Cross-City Stability): Consistency of importance across cities

Author: PSF-CTF Team
"""

from __future__ import annotations
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from dataclasses import dataclass, asdict
import logging

import shap
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from scipy.spatial.distance import pdist, squareform
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class FeatureImportance:
    """Per-city feature importance."""
    city: str
    feature_name: str
    mean_shap: float  # E[|SHAP|]
    std_shap: float
    n_samples: int


@dataclass
class FeatureStability:
    """Cross-city stability metrics for a single feature."""
    feature_name: str
    mu: float  # Mean importance across cities
    sigma: float  # Std of importance across cities
    stability_index: float  # μ / (σ + ε)
    mean_shap_values: np.ndarray  # Per-city importance values
    included_cities: List[str]


@dataclass
class FeatureSelectionResult:
    """Result of feature selection process."""
    selected_features: List[str]
    rejected_features: List[str]
    removed_count: int
    removal_ratio: float
    per_feature_stability: Dict[str, FeatureStability]
    feature_redundancy_groups: Dict[str, List[str]] = None


# ============================================================================
# CORE: SHAP COMPUTATION & STABILITY ANALYSIS
# ============================================================================

class SHAPFeatureAnalyzer:
    """
    Computes SHAP values per city and analyzes cross-city stability.
    """
    
    def __init__(self, model: Optional[Any] = None):
        """
        Args:
            model: Trained sklearn model (GradientBoostingRegressor recommended)
                   If None, will train internally
        """
        self.model = model
        self.explainers = {}  # {city: shap.TreeExplainer}
        self.shap_values_per_city = {}  # {city: np.ndarray}
        self.feature_names = None
    
    def train_model(
        self,
        X_train: np.ndarray,
        y_train: np.ndarray,
        feature_names: List[str],
        **model_kwargs
    ) -> Any:
        """
        Train a GradientBoostingRegressor if not provided.
        
        Args:
            X_train: Training features [n, p]
            y_train: Training targets [n]
            feature_names: Names of features
            **model_kwargs: Parameters for GradientBoostingRegressor
        
        Returns:
            Trained model
        """
        logger.info("Training base model...")
        
        default_params = {
            'n_estimators': 100,
            'max_depth': 5,
            'learning_rate': 0.1,
            'random_state': 42,
        }
        default_params.update(model_kwargs)
        
        self.model = GradientBoostingRegressor(**default_params)
        self.model.fit(X_train, y_train)
        self.feature_names = feature_names
        
        logger.info(f"✓ Model trained on {X_train.shape[0]} samples, {X_train.shape[1]} features")
        
        return self.model
    
    def compute_shap_per_city(
        self,
        X_per_city: Dict[str, np.ndarray],
        background_samples: Optional[np.ndarray] = None,
        n_background: int = 100,
    ) -> Dict[str, np.ndarray]:
        """
        Compute SHAP values for each city's test set.
        
        Args:
            X_per_city: {city_name: feature_matrix [n_zones, n_features]}
            background_samples: Background samples for SHAP baseline
                                If None, uses random subset from first city
            n_background: Number of background samples if not provided
        
        Returns:
            {city: shap_values_array [n_zones, n_features]}
        """
        logger.info("Computing SHAP values per city...")
        
        if self.model is None:
            raise ValueError("Model not trained. Call train_model() first.")
        
        if not self.feature_names:
            raise ValueError("Feature names not set. Call train_model() first.")
        
        # Select background samples
        if background_samples is None:
            first_city_X = list(X_per_city.values())[0]
            background_samples = first_city_X[
                np.random.choice(len(first_city_X), min(n_background, len(first_city_X)), replace=False)
            ]
            logger.info(f"  Using {len(background_samples)} background samples")
        
        # Create SHAP explainer (TreeExplainer for gradient boosting)
        explainer = shap.TreeExplainer(self.model)
        
        # Compute SHAP for each city
        self.shap_values_per_city = {}
        for city, X_city in X_per_city.items():
            logger.info(f"  Computing SHAP for {city} ({len(X_city)} zones)...")
            shap_vals = explainer.shap_values(X_city)
            self.shap_values_per_city[city] = shap_vals
        
        logger.info(f"✓ SHAP computed for {len(X_per_city)} cities")
        
        return self.shap_values_per_city
    
    def compute_feature_importance_per_city(self) -> Dict[str, List[FeatureImportance]]:
        """
        Compute mean absolute SHAP per feature per city.
        
        Returns:
            {city: [FeatureImportance, ...]}
        """
        logger.info("Computing feature importance per city...")
        
        if not self.shap_values_per_city:
            raise ValueError("SHAP values not computed. Call compute_shap_per_city() first.")
        
        importance_per_city = {}
        
        for city, shap_vals in self.shap_values_per_city.items():
            # Mean absolute SHAP per feature
            mean_abs_shap = np.mean(np.abs(shap_vals), axis=0)
            std_shap = np.std(np.abs(shap_vals), axis=0)
            n_samples = len(shap_vals)
            
            features = []
            for feat_idx, feat_name in enumerate(self.feature_names):
                features.append(FeatureImportance(
                    city=city,
                    feature_name=feat_name,
                    mean_shap=float(mean_abs_shap[feat_idx]),
                    std_shap=float(std_shap[feat_idx]),
                    n_samples=n_samples
                ))
            
            importance_per_city[city] = features
        
        return importance_per_city


# ============================================================================
# CROSS-CITY STABILITY ANALYSIS
# ============================================================================

class CrossCityStabilityAnalyzer:
    """
    Analyzes stability of features across cities.
    """
    
    def __init__(self, epsilon: float = 1e-10):
        self.epsilon = epsilon
    
    def compute_stability_metrics(
        self,
        importance_per_city: Dict[str, List[FeatureImportance]]
    ) -> Dict[str, FeatureStability]:
        """
        Compute cross-city stability for each feature.
        
        Args:
            importance_per_city: Output from SHAPFeatureAnalyzer
        
        Returns:
            {feature_name: FeatureStability}
        """
        logger.info("Computing cross-city stability metrics...")
        
        # Collect importance values per feature
        importance_by_feature = {}
        cities = list(importance_per_city.keys())
        
        for city in cities:
            for imp in importance_per_city[city]:
                if imp.feature_name not in importance_by_feature:
                    importance_by_feature[imp.feature_name] = []
                importance_by_feature[imp.feature_name].append(imp.mean_shap)
        
        # Compute stability metrics
        stability_results = {}
        
        for feature_name, shap_values in importance_by_feature.items():
            shap_array = np.array(shap_values)
            
            mu = np.mean(shap_array)
            sigma = np.std(shap_array)
            stability_index = mu / (sigma + self.epsilon)
            
            stability_results[feature_name] = FeatureStability(
                feature_name=feature_name,
                mu=float(mu),
                sigma=float(sigma),
                stability_index=float(stability_index),
                mean_shap_values=shap_array,
                included_cities=cities
            )
            
            logger.info(f"  {feature_name:20s}: μ={mu:.6f}, σ={sigma:.6f}, S={stability_index:.4f}")
        
        return stability_results


# ============================================================================
# FEATURE FILTERING & SELECTION
# ============================================================================

class FeatureFilter:
    """
    Applies filtering rules to select robust, transferable features.
    """
    
    def __init__(
        self,
        importance_threshold: float = 0.01,
        stability_threshold: float = 0.90,
        redundancy_threshold: float = 0.85,
    ):
        """
        Args:
            importance_threshold: μp ≥ τ_importance
            stability_threshold: Sp ≥ τ_stability
            redundancy_threshold: Correlation threshold for redundancy groups
        """
        self.importance_threshold = importance_threshold
        self.stability_threshold = stability_threshold
        self.redundancy_threshold = redundancy_threshold
    
    def filter_features(
        self,
        stability_metrics: Dict[str, FeatureStability],
        apply_redundancy_check: bool = False,
    ) -> FeatureSelectionResult:
        """
        Filter features based on importance, stability, and redundancy.
        
        Args:
            stability_metrics: From CrossCityStabilityAnalyzer
            apply_redundancy_check: Whether to check for redundant features
        
        Returns:
            FeatureSelectionResult with selected/rejected features
        """
        logger.info("Applying feature filtering rules...")
        
        selected = []
        rejected = []
        
        for feature_name, metrics in stability_metrics.items():
            # Rule 1: Minimum importance
            if metrics.mu < self.importance_threshold:
                logger.info(f"  ✗ {feature_name}: LOW IMPORTANCE (μ={metrics.mu:.6f} < {self.importance_threshold})")
                rejected.append(feature_name)
                continue
            
            # Rule 2: Minimum stability
            if metrics.stability_index < self.stability_threshold:
                logger.info(f"  ✗ {feature_name}: LOW STABILITY (S={metrics.stability_index:.4f} < {self.stability_threshold})")
                rejected.append(feature_name)
                continue
            
            # Passed all filters
            logger.info(f"  ✓ {feature_name}: SELECTED (μ={metrics.mu:.6f}, S={metrics.stability_index:.4f})")
            selected.append(feature_name)
        
        # Optional: Check for redundancy
        redundancy_groups = None
        if apply_redundancy_check:
            redundancy_groups = self._identify_redundancy_groups(
                selected, stability_metrics
            )
        
        removal_ratio = len(rejected) / (len(selected) + len(rejected))
        
        logger.info(f"\n✓ Filtering complete:")
        logger.info(f"  Selected: {len(selected)} features")
        logger.info(f"  Rejected: {len(rejected)} features")
        logger.info(f"  Removal ratio: {removal_ratio:.1%}")
        
        return FeatureSelectionResult(
            selected_features=selected,
            rejected_features=rejected,
            removed_count=len(rejected),
            removal_ratio=removal_ratio,
            per_feature_stability=stability_metrics,
            feature_redundancy_groups=redundancy_groups,
        )
    
    def _identify_redundancy_groups(
        self,
        feature_list: List[str],
        stability_metrics: Dict[str, FeatureStability],
    ) -> Dict[str, List[str]]:
        """
        Identify redundant feature groups via SHAP clustering.
        
        Args:
            feature_list: Features to analyze
            stability_metrics: Stability metrics with SHAP arrays
        
        Returns:
            {cluster_name: [feature_names, ...]}
        """
        logger.info("\nIdentifying redundancy groups via SHAP clustering...")
        
        if len(feature_list) < 2:
            return {}
        
        # Extract SHAP arrays for clustering
        shap_matrix = np.column_stack([
            stability_metrics[f].mean_shap_values for f in feature_list
        ])
        
        # Standardize for clustering
        shap_matrix_norm = (shap_matrix - shap_matrix.mean(axis=0)) / (shap_matrix.std(axis=0) + 1e-10)
        
        # Compute distance and linkage
        distances = pdist(shap_matrix_norm.T, metric='correlation')
        Z = linkage(distances, method='ward')
        
        # Cut dendrogram at threshold
        clusters = fcluster(Z, 1.0 - self.redundancy_threshold, criterion='distance')
        
        # Group features by cluster
        redundancy_groups = {}
        for cluster_id in np.unique(clusters):
            group_features = [f for f, c in zip(feature_list, clusters) if c == cluster_id]
            redundancy_groups[f"group_{cluster_id}"] = group_features
            logger.info(f"  Redundancy group {cluster_id}: {group_features}")
        
        return redundancy_groups


# ============================================================================
# VALIDATION FRAMEWORK
# ============================================================================

class FeatureSelectionValidator:
    """
    Validates feature selection via model retraining and performance comparison.
    """
    
    def __init__(self, model_class=None, **model_params):
        """
        Args:
            model_class: Model class to use for retraining (default: GradientBoostingRegressor)
            **model_params: Model parameters
        """
        self.model_class = model_class or GradientBoostingRegressor
        self.model_params = {
            'n_estimators': 100,
            'max_depth': 5,
            'learning_rate': 0.1,
            'random_state': 42,
            **model_params
        }
        self.models = {}  # {feature_set_name: trained_model}
    
    def train_models(
        self,
        X_train: np.ndarray,
        y_train: np.ndarray,
        feature_indices: Dict[str, List[int]],
        feature_names: List[str],
    ) -> Dict[str, Any]:
        """
        Train models with different feature sets.
        
        Args:
            X_train: Full training features [n, p]
            y_train: Training targets [n]
            feature_indices: {set_name: [feature_indices, ...]}
            feature_names: All feature names
        
        Returns:
            {set_name: trained_model}
        """
        logger.info("Training models with different feature sets...")
        
        for set_name, indices in feature_indices.items():
            logger.info(f"  Training model with feature set '{set_name}' ({len(indices)} features)")
            
            X_subset = X_train[:, indices]
            model = self.model_class(**self.model_params)
            model.fit(X_subset, y_train)
            
            self.models[set_name] = model
            
            # Log used features
            used_features = [feature_names[i] for i in indices]
            logger.info(f"    Features: {used_features}")
        
        return self.models
    
    def evaluate_models(
        self,
        X_test_per_city: Dict[str, np.ndarray],
        y_test_per_city: Dict[str, np.ndarray],
        feature_indices: Dict[str, List[int]],
        metric_fn: callable,
    ) -> pd.DataFrame:
        """
        Evaluate models on test sets across cities.
        
        Args:
            X_test_per_city: {city: test_features}
            y_test_per_city: {city: test_targets}
            feature_indices: {set_name: feature_indices}
            metric_fn: Function to compute metric (e.g., R2, MAE)
        
        Returns:
            DataFrame with results
        """
        logger.info("Evaluating models across cities...")
        
        results = []
        
        for set_name, model in self.models.items():
            indices = feature_indices[set_name]
            
            for city, X_city in X_test_per_city.items():
                if city not in y_test_per_city:
                    continue
                
                y_city = y_test_per_city[city]
                X_subset = X_city[:, indices]
                
                y_pred = model.predict(X_subset)
                metric_value = metric_fn(y_pred, y_city)
                
                results.append({
                    'feature_set': set_name,
                    'city': city,
                    'metric': metric_value,
                })
                
                logger.info(f"  {set_name:20s} | {city:15s}: {metric_value:.6f}")
        
        results_df = pd.DataFrame(results)
        return results_df
    
    def compute_summary_statistics(
        self,
        eval_results: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Compute summary statistics per feature set.
        
        Args:
            eval_results: DataFrame from evaluate_models()
        
        Returns:
            Summary DataFrame with mean, std, variance across cities
        """
        logger.info("Computing summary statistics...")
        
        summary = eval_results.groupby('feature_set')['metric'].agg([
            'mean', 'std', 'min', 'max', 'count'
        ]).reset_index()
        
        summary.columns = ['feature_set', 'mean_metric', 'std_metric', 'min_metric', 'max_metric', 'n_cities']
        
        logger.info("\nSummary Statistics:")
        for _, row in summary.iterrows():
            logger.info(
                f"  {row['feature_set']:20s}: "
                f"mean={row['mean_metric']:.6f}, std={row['std_metric']:.6f}, "
                f"cities={int(row['n_cities'])}"
            )
        
        return summary


# ============================================================================
# REPORTING
# ============================================================================

class FeatureSelectionReporter:
    """Generate comprehensive reports."""
    
    def __init__(self, output_dir: Path = None):
        self.output_dir = output_dir or Path("./feature_selection_results")
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def save_selection_result(
        self,
        result: FeatureSelectionResult,
        filename: str = "feature_selection.json"
    ):
        """Save feature selection result to JSON."""
        filepath = self.output_dir / filename
        
        data = {
            'selected_features': result.selected_features,
            'rejected_features': result.rejected_features,
            'removed_count': result.removed_count,
            'removal_ratio': result.removal_ratio,
            'per_feature_stability': {
                name: asdict(metric) for name, metric in result.per_feature_stability.items()
            },
            'redundancy_groups': result.feature_redundancy_groups,
        }
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        
        logger.info(f"✓ Selection result saved to {filepath}")
    
    def save_evaluation_results(
        self,
        eval_results: pd.DataFrame,
        summary_stats: pd.DataFrame,
        filename_eval: str = "evaluation_results.csv",
        filename_summary: str = "summary_statistics.csv"
    ):
        """Save evaluation results."""
        eval_results.to_csv(self.output_dir / filename_eval, index=False)
        summary_stats.to_csv(self.output_dir / filename_summary, index=False)
        logger.info(f"✓ Evaluation results saved to {self.output_dir}")
    
    def save_stability_report(
        self,
        stability_metrics: Dict[str, FeatureStability],
        filename: str = "stability_report.csv"
    ):
        """Save detailed stability metrics."""
        rows = []
        for feature_name, metrics in stability_metrics.items():
            rows.append({
                'feature': feature_name,
                'mean_importance': metrics.mu,
                'std_importance': metrics.sigma,
                'stability_index': metrics.stability_index,
                'n_cities': len(metrics.included_cities),
                'cities': ','.join(metrics.included_cities),
            })
        
        df = pd.DataFrame(rows).sort_values('stability_index', ascending=False)
        df.to_csv(self.output_dir / filename, index=False)
        logger.info(f"✓ Stability report saved to {self.output_dir / filename}")
    
    def generate_summary(
        self,
        result: FeatureSelectionResult,
        eval_summary: pd.DataFrame,
    ) -> str:
        """Generate text summary."""
        summary = "=" * 80 + "\n"
        summary += "SHAP + CROSS-CITY FEATURE SELECTION PROTOCOL SUMMARY\n"
        summary += "=" * 80 + "\n\n"
        
        summary += f"Selected Features ({len(result.selected_features)}):\n"
        for feat in sorted(result.selected_features):
            metrics = result.per_feature_stability[feat]
            summary += f"  • {feat:25s} | μ={metrics.mu:.6f}, S={metrics.stability_index:.4f}\n"
        
        summary += f"\nRejected Features ({len(result.rejected_features)}):\n"
        for feat in sorted(result.rejected_features):
            metrics = result.per_feature_stability[feat]
            summary += f"  • {feat:25s} | μ={metrics.mu:.6f}, S={metrics.stability_index:.4f}\n"
        
        summary += f"\nFeature Reduction:\n"
        summary += f"  • Removed: {result.removed_count} features ({result.removal_ratio:.1%})\n"
        summary += f"  • Kept: {len(result.selected_features)} features\n"
        
        if result.feature_redundancy_groups:
            summary += f"\nRedundancy Groups:\n"
            for group_name, features in result.feature_redundancy_groups.items():
                summary += f"  • {group_name}: {features}\n"
        
        summary += f"\nModel Performance Summary:\n"
        for _, row in eval_summary.iterrows():
            summary += (
                f"  • {row['feature_set']:20s}: "
                f"mean={row['mean_metric']:.6f}, std={row['std_metric']:.6f}\n"
            )
        
        return summary


# ============================================================================
# MAIN ORCHESTRATOR
# ============================================================================

class SHAPFeatureSelectionPipeline:
    """
    Complete pipeline: SHAP computation → Stability analysis → Filtering → Validation
    """
    
    def __init__(
        self,
        importance_threshold: float = 0.01,
        stability_threshold: float = 0.90,
        redundancy_threshold: float = 0.85,
    ):
        self.analyzer = SHAPFeatureAnalyzer()
        self.stability_analyzer = CrossCityStabilityAnalyzer()
        self.filter = FeatureFilter(
            importance_threshold=importance_threshold,
            stability_threshold=stability_threshold,
            redundancy_threshold=redundancy_threshold,
        )
        self.validator = FeatureSelectionValidator()
        self.reporter = FeatureSelectionReporter()
    
    def run_pipeline(
        self,
        X_train: np.ndarray,
        y_train: np.ndarray,
        X_test_per_city: Dict[str, np.ndarray],
        y_test_per_city: Dict[str, np.ndarray],
        feature_names: List[str],
        baseline_feature_indices: Dict[str, List[int]] = None,
        metric_fn: callable = None,
        output_dir: Path = None,
    ) -> Tuple[FeatureSelectionResult, pd.DataFrame, pd.DataFrame]:
        """
        Run complete feature selection pipeline.
        
        Args:
            X_train: Training features [n, p]
            y_train: Training targets [n]
            X_test_per_city: {city: test_features}
            y_test_per_city: {city: test_targets}
            feature_names: Names of all features
            baseline_feature_indices: {set_name: [indices, ...]} for comparison
            metric_fn: Metric function for evaluation
            output_dir: Output directory for results
        
        Returns:
            (FeatureSelectionResult, eval_results_df, summary_stats_df)
        """
        if output_dir:
            self.reporter.output_dir = output_dir
        
        logger.info("\n" + "=" * 80)
        logger.info("SHAP + CROSS-CITY FEATURE SELECTION PIPELINE")
        logger.info("=" * 80)
        
        # Step 1: Train base model
        self.analyzer.train_model(X_train, y_train, feature_names)
        
        # Step 2: Compute SHAP values per city
        self.analyzer.compute_shap_per_city(X_test_per_city)
        
        # Step 3: Compute feature importance per city
        importance_per_city = self.analyzer.compute_feature_importance_per_city()
        
        # Step 4: Compute cross-city stability
        stability_metrics = self.stability_analyzer.compute_stability_metrics(
            importance_per_city
        )
        
        # Step 5: Filter features
        selection_result = self.filter.filter_features(
            stability_metrics, apply_redundancy_check=True
        )
        
        # Save stability report
        self.reporter.save_stability_report(stability_metrics)
        self.reporter.save_selection_result(selection_result)
        
        # Step 6: Validate via model retraining
        if baseline_feature_indices is None:
            baseline_feature_indices = self._create_default_baselines(
                X_train.shape[1], selection_result, feature_names
            )
        
        feature_indices_combined = {
            **baseline_feature_indices,
            'SHAP_selected': [feature_names.index(f) for f in selection_result.selected_features],
        }
        
        self.validator.train_models(
            X_train, y_train,
            feature_indices_combined,
            feature_names
        )
        
        if metric_fn is None:
            metric_fn = self._default_metric_r2_log
        
        eval_results = self.validator.evaluate_models(
            X_test_per_city, y_test_per_city,
            feature_indices_combined,
            metric_fn
        )
        
        summary_stats = self.validator.compute_summary_statistics(eval_results)
        
        # Save results
        self.reporter.save_evaluation_results(eval_results, summary_stats)
        
        # Print summary
        summary_text = self.reporter.generate_summary(selection_result, summary_stats)
        print("\n" + summary_text)
        
        # Save summary to file
        with open(self.reporter.output_dir / "summary.txt", 'w') as f:
            f.write(summary_text)
        
        logger.info(f"\n✓ Pipeline complete. Results saved to {self.reporter.output_dir}")
        
        return selection_result, eval_results, summary_stats
    
    @staticmethod
    def _create_default_baselines(
        n_features: int,
        selection_result: FeatureSelectionResult,
        feature_names: List[str],
    ) -> Dict[str, List[int]]:
        """Create baseline feature sets for comparison."""
        all_indices = list(range(n_features))
        shap_indices = [feature_names.index(f) for f in selection_result.selected_features]
        
        # Random subset of same size as SHAP selection
        np.random.seed(42)
        random_indices = np.random.choice(
            all_indices, size=len(shap_indices), replace=False
        ).tolist()
        
        return {
            'Full_Features': all_indices,
            'Random_Subset': random_indices,
        }
    
    @staticmethod
    def _default_metric_r2_log(y_pred: np.ndarray, y_true: np.ndarray) -> float:
        """Compute R²_log as default metric."""
        y_pred_log = np.log1p(y_pred + 1e-10)
        y_true_log = np.log1p(y_true + 1e-10)
        
        ss_res = np.sum((y_pred_log - y_true_log) ** 2)
        ss_tot = np.sum((y_true_log - np.mean(y_true_log)) ** 2)
        
        r2_log = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
        return float(r2_log)


if __name__ == "__main__":
    logger.info("SHAP Feature Selection Module Loaded")
    logger.info("Use SHAPFeatureSelectionPipeline for complete pipeline execution")
