"""
5-Layer Evaluation Framework for PSF-CTF Paper
==============================================

This module implements a clean, causal, modular testing system that allows
reproduction and clear identification of component contributions.

Layers:
1. DECAY IDENTIFICATION TEST - whether distance decay parameters are identifiable
2. OUTFLOW (Oi) ESTIMATION TEST - whether Oi prediction is the main bottleneck
3. ATTRACTION MODEL (Aj) ABLATION TEST - whether OSM features are sufficient
4. FULL SYSTEM DECOMPOSITION TEST - causal contribution of each module
5. ZERO-SHOT GENERALIZATION TEST - robustness under domain shift

Author: PSF-CTF Team
"""

from __future__ import annotations
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Tuple, Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from scipy.optimize import minimize_scalar, minimize
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score
import json
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ============================================================================
# DATA STRUCTURES
# ============================================================================

@dataclass
class TestResult:
    """Atomic test result container."""
    layer: int
    test_name: str
    metric: str  # CPC, R2_log, variance, etc.
    value: float
    details: Dict[str, Any] = None
    
    def to_dict(self):
        return asdict(self)


@dataclass
class ComponentContribution:
    """Quantifies contribution of a single component."""
    component: str  # 'decay', 'outflow', 'attraction'
    baseline_cpc: float
    with_component_cpc: float
    delta_cpc: float
    variance_across_cities: float


# ============================================================================
# LAYER 1: DECAY IDENTIFICATION TEST
# ============================================================================

class Layer1_DecayIdentification:
    """
    Test whether distance decay parameters (α, β) are identifiable from 
    aggregated mobility histograms without OD data.
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.results = []
    
    def test_pure_decay_recovery(
        self,
        distance_bins: np.ndarray,
        bin_distribution: np.ndarray,
        ground_truth_alpha: float,
        ground_truth_beta: float
    ) -> TestResult:
        """
        T1.1: Pure Decay Recovery
        
        Recovers decay parameters (α, β) from aggregate distance distribution
        WITHOUT any OD data or Oi variation.
        
        Args:
            distance_bins: bin centers [K]
            bin_distribution: P(b_k) distribution [K]
            ground_truth_alpha, ground_truth_beta: reference values
        
        Returns:
            TestResult with recovered parameters and recovery error
        """
        logger.info("=== T1.1: Pure Decay Recovery ===")
        
        # Normalize distribution
        bin_dist_norm = bin_distribution / np.sum(bin_distribution)
        
        def loss_fn(params):
            alpha, beta = params
            # Evaluate decay function at bin centers
            decay_values = distance_bins ** (-alpha) * np.exp(-beta * distance_bins)
            decay_norm = decay_values / np.sum(decay_values)
            
            # KL divergence or L2 distance
            mse = np.sum((decay_norm - bin_dist_norm) ** 2)
            return mse
        
        # Optimize
        result = minimize(
            loss_fn,
            x0=[1.5, 0.1],
            bounds=[(0.5, 3.0), (0.001, 1.0)],
            method='L-BFGS-B'
        )
        
        estimated_alpha, estimated_beta = result.x
        error_alpha = abs(estimated_alpha - ground_truth_alpha) / ground_truth_alpha
        error_beta = abs(estimated_beta - ground_truth_beta) / ground_truth_beta
        total_error = (error_alpha + error_beta) / 2
        
        logger.info(f"  True:      α={ground_truth_alpha:.4f}, β={ground_truth_beta:.4f}")
        logger.info(f"  Estimated: α={estimated_alpha:.4f}, β={estimated_beta:.4f}")
        logger.info(f"  Error:     α={error_alpha:.4%}, β={error_beta:.4%}")
        
        return TestResult(
            layer=1,
            test_name="T1.1_Pure_Decay_Recovery",
            metric="Parameter_Recovery_Error",
            value=total_error,
            details={
                "true_alpha": float(ground_truth_alpha),
                "true_beta": float(ground_truth_beta),
                "estimated_alpha": float(estimated_alpha),
                "estimated_beta": float(estimated_beta),
                "error_alpha": float(error_alpha),
                "error_beta": float(error_beta),
            }
        )
    
    def test_bin_robustness(
        self,
        distance_bins_list: List[np.ndarray],
        bin_distributions_list: List[np.ndarray],
        n_bins_list: List[int]
    ) -> List[TestResult]:
        """
        T1.2: Bin Robustness Test
        
        Evaluate stability of (α, β) across different discretization levels.
        
        Args:
            distance_bins_list: List of bin center arrays
            bin_distributions_list: List of P(b_k) distributions
            n_bins_list: Corresponding bin counts K ∈ {3, 5, 10, 20}
        
        Returns:
            List of TestResults for each K
        """
        logger.info("=== T1.2: Bin Robustness Test ===")
        
        results = []
        estimated_params = []
        
        for k, dist_bins, bin_dist in zip(n_bins_list, distance_bins_list, bin_distributions_list):
            logger.info(f"  Testing K={k} bins...")
            
            bin_dist_norm = bin_dist / np.sum(bin_dist)
            
            def loss_fn(params):
                alpha, beta = params
                decay_values = dist_bins ** (-alpha) * np.exp(-beta * dist_bins)
                decay_norm = decay_values / np.sum(decay_values)
                return np.sum((decay_norm - bin_dist_norm) ** 2)
            
            result = minimize(
                loss_fn,
                x0=[1.5, 0.1],
                bounds=[(0.5, 3.0), (0.001, 1.0)],
                method='L-BFGS-B'
            )
            
            estimated_params.append(result.x)
            results.append(TestResult(
                layer=1,
                test_name=f"T1.2_Bin_Robustness_K{k}",
                metric="Convergence",
                value=result.fun,
                details={"n_bins": k, "alpha": float(result.x[0]), "beta": float(result.x[1])}
            ))
        
        # Compute variance of parameters across K values
        param_array = np.array(estimated_params)
        alpha_std = np.std(param_array[:, 0])
        beta_std = np.std(param_array[:, 1])
        
        logger.info(f"  Parameter stability: α_std={alpha_std:.6f}, β_std={beta_std:.6f}")
        
        results.append(TestResult(
            layer=1,
            test_name="T1.2_Bin_Robustness_Stability",
            metric="Parameter_Stability",
            value=(alpha_std + beta_std) / 2,
            details={"alpha_std": float(alpha_std), "beta_std": float(beta_std)}
        ))
        
        return results


# ============================================================================
# LAYER 2: OUTFLOW (Oi) ESTIMATION TEST
# ============================================================================

class Layer2_OutflowEstimation:
    """
    Test whether Oi prediction is the main bottleneck of system performance.
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.results = []
    
    def test_oracle_upper_bound(
        self,
        T_predicted_with_estimated_oi: np.ndarray,
        T_predicted_with_oracle_oi: np.ndarray,
        T_ground_truth: np.ndarray,
        cpc_metric_fn
    ) -> TestResult:
        """
        T2.1: Oracle Upper Bound
        
        Replace Oi with ground truth. Measure CPC gain.
        
        Args:
            T_predicted_with_estimated_oi: OD matrix with estimated Oi
            T_predicted_with_oracle_oi: OD matrix with ground truth Oi
            T_ground_truth: True OD matrix
            cpc_metric_fn: Function to compute CPC
        
        Returns:
            TestResult with oracle gap
        """
        logger.info("=== T2.1: Oracle Upper Bound ===")
        
        cpc_estimated = cpc_metric_fn(T_predicted_with_estimated_oi, T_ground_truth)
        cpc_oracle = cpc_metric_fn(T_predicted_with_oracle_oi, T_ground_truth)
        oracle_gap = cpc_oracle - cpc_estimated
        
        logger.info(f"  CPC with estimated Oi: {cpc_estimated:.6f}")
        logger.info(f"  CPC with oracle Oi:    {cpc_oracle:.6f}")
        logger.info(f"  Oracle gap:            {oracle_gap:.6f} ({oracle_gap/cpc_oracle*100:.2f}%)")
        
        return TestResult(
            layer=2,
            test_name="T2.1_Oracle_Upper_Bound",
            metric="Oracle_CPC_Gap",
            value=oracle_gap,
            details={
                "cpc_estimated_oi": float(cpc_estimated),
                "cpc_oracle_oi": float(cpc_oracle),
                "oracle_gap_pct": float(oracle_gap / cpc_oracle * 100)
            }
        )
    
    def test_noise_sensitivity(
        self,
        T_base: np.ndarray,
        T_ground_truth: np.ndarray,
        noise_levels: List[float],
        cpc_metric_fn
    ) -> List[TestResult]:
        """
        T2.2: Noise Sensitivity
        
        Add controlled noise to Oi. Measure degradation.
        
        Args:
            T_base: Base OD matrix
            T_ground_truth: True OD matrix
            noise_levels: List of noise percentages [0%, 10%, 20%, 40%]
            cpc_metric_fn: Function to compute CPC
        
        Returns:
            List of TestResults for each noise level
        """
        logger.info("=== T2.2: Noise Sensitivity ===")
        
        results = []
        cpc_baseline = cpc_metric_fn(T_base, T_ground_truth)
        logger.info(f"  Baseline CPC (0% noise): {cpc_baseline:.6f}")
        
        for noise_pct in noise_levels:
            # Add Gaussian noise to predicted flows
            noise_factor = noise_pct / 100.0
            T_noisy = T_base * (1 + np.random.normal(0, noise_factor, T_base.shape))
            T_noisy = np.maximum(T_noisy, 0)  # Clip to non-negative
            
            cpc_noisy = cpc_metric_fn(T_noisy, T_ground_truth)
            degradation = (cpc_baseline - cpc_noisy) / cpc_baseline
            
            logger.info(f"  CPC at {noise_pct}% noise: {cpc_noisy:.6f}, degradation: {degradation:.4%}")
            
            results.append(TestResult(
                layer=2,
                test_name=f"T2.2_Noise_Sensitivity_{noise_pct}pct",
                metric="CPC",
                value=cpc_noisy,
                details={
                    "noise_level_pct": float(noise_pct),
                    "degradation_pct": float(degradation * 100)
                }
            ))
        
        return results
    
    def test_cross_city_transfer(
        self,
        oi_predictions_per_city: Dict[str, np.ndarray],
        oi_ground_truth_per_city: Dict[str, np.ndarray],
        train_cities: List[str],
        test_cities: List[str]
    ) -> TestResult:
        """
        T2.3: Cross-City Transfer
        
        Train on M source cities, test on held-out cities.
        Report R²_log.
        
        Args:
            oi_predictions_per_city: {city: predicted_oi_vector}
            oi_ground_truth_per_city: {city: ground_truth_oi_vector}
            train_cities: List of source city names
            test_cities: List of target city names
        
        Returns:
            TestResult with R²_log on test cities
        """
        logger.info("=== T2.3: Cross-City Transfer ===")
        logger.info(f"  Train cities: {train_cities}")
        logger.info(f"  Test cities:  {test_cities}")
        
        # Aggregate predictions and ground truth
        pred_all = np.concatenate([oi_predictions_per_city[c] for c in test_cities])
        true_all = np.concatenate([oi_ground_truth_per_city[c] for c in test_cities])
        
        # Compute R²_log
        pred_log = np.log1p(pred_all)
        true_log = np.log1p(true_all)
        
        ss_res = np.sum((pred_log - true_log) ** 2)
        ss_tot = np.sum((true_log - np.mean(true_log)) ** 2)
        r2_log = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
        
        logger.info(f"  R²_log on {len(test_cities)} held-out cities: {r2_log:.6f}")
        
        return TestResult(
            layer=2,
            test_name="T2.3_Cross_City_Transfer",
            metric="R2_log",
            value=r2_log,
            details={
                "n_train_cities": len(train_cities),
                "n_test_cities": len(test_cities),
                "train_city_list": train_cities,
                "test_city_list": test_cities
            }
        )


# ============================================================================
# LAYER 3: ATTRACTION MODEL (Aj) ABLATION TEST
# ============================================================================

class Layer3_AttractionAblation:
    """
    Test whether OSM features are sufficient and stable for destination
    attractiveness modeling.
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.results = []
    
    def test_feature_knockout(
        self,
        features_dict: Dict[str, np.ndarray],
        T_ground_truth: np.ndarray,
        cpc_metric_fn
    ) -> List[TestResult]:
        """
        T3.1: Feature Knockout
        
        Remove features one-by-one:
        - POI only
        - POP only
        - ROAD only
        - AREA only
        
        Args:
            features_dict: {'POI': array, 'POP': array, 'ROAD': array, 'AREA': array}
            T_ground_truth: True OD matrix
            cpc_metric_fn: Function to compute CPC
        
        Returns:
            List of TestResults for each feature subset
        """
        logger.info("=== T3.1: Feature Knockout ===")
        
        results = []
        feature_names = list(features_dict.keys())
        
        # Baseline: all features
        all_features = np.column_stack([features_dict[f] for f in feature_names])
        cpc_all = cpc_metric_fn(all_features, T_ground_truth)
        logger.info(f"  CPC with all features: {cpc_all:.6f}")
        
        # Single feature ablation
        for feature_name in feature_names:
            other_features = [f for f in feature_names if f != feature_name]
            X_subset = np.column_stack([features_dict[f] for f in other_features])
            
            cpc_subset = cpc_metric_fn(X_subset, T_ground_truth)
            importance = (cpc_all - cpc_subset) / cpc_all
            
            logger.info(f"  CPC without {feature_name:4s}: {cpc_subset:.6f}, importance: {importance:.4%}")
            
            results.append(TestResult(
                layer=3,
                test_name=f"T3.1_Knockout_{feature_name}",
                metric="CPC",
                value=cpc_subset,
                details={
                    "removed_feature": feature_name,
                    "feature_importance": float(importance)
                }
            ))
        
        return results
    
    def test_normalization_study(
        self,
        features_raw: np.ndarray,
        T_ground_truth: np.ndarray,
        cpc_metric_fn
    ) -> List[TestResult]:
        """
        T3.2: Normalization Study
        
        Compare normalization schemes:
        - raw features
        - min-max normalization
        - Z-score normalization
        
        Args:
            features_raw: Raw feature matrix [n_zones x n_features]
            T_ground_truth: True OD matrix
            cpc_metric_fn: Function to compute CPC
        
        Returns:
            List of TestResults for each normalization scheme
        """
        logger.info("=== T3.2: Normalization Study ===")
        
        results = []
        
        # Raw
        cpc_raw = cpc_metric_fn(features_raw, T_ground_truth)
        logger.info(f"  CPC (raw):      {cpc_raw:.6f}")
        results.append(TestResult(
            layer=3,
            test_name="T3.2_Normalization_Raw",
            metric="CPC",
            value=cpc_raw,
            details={"normalization": "raw"}
        ))
        
        # Min-max
        features_minmax = (features_raw - features_raw.min(axis=0)) / (features_raw.max(axis=0) - features_raw.min(axis=0) + 1e-10)
        cpc_minmax = cpc_metric_fn(features_minmax, T_ground_truth)
        logger.info(f"  CPC (min-max):  {cpc_minmax:.6f}")
        results.append(TestResult(
            layer=3,
            test_name="T3.2_Normalization_MinMax",
            metric="CPC",
            value=cpc_minmax,
            details={"normalization": "min-max"}
        ))
        
        # Z-score
        features_zscore = (features_raw - features_raw.mean(axis=0)) / (features_raw.std(axis=0) + 1e-10)
        cpc_zscore = cpc_metric_fn(features_zscore, T_ground_truth)
        logger.info(f"  CPC (z-score):  {cpc_zscore:.6f}")
        results.append(TestResult(
            layer=3,
            test_name="T3.2_Normalization_ZScore",
            metric="CPC",
            value=cpc_zscore,
            details={"normalization": "z-score"}
        ))
        
        return results
    
    def test_cross_city_stability(
        self,
        Aj_predictions_per_city: Dict[str, np.ndarray],
        Aj_ground_truth_per_city: Dict[str, np.ndarray],
        train_cities: List[str],
        test_cities: List[str]
    ) -> TestResult:
        """
        T3.3: Cross-City Stability
        
        Train on source cities, test on held-out cities.
        
        Args:
            Aj_predictions_per_city: {city: predicted_aj_vector}
            Aj_ground_truth_per_city: {city: ground_truth_aj_vector}
            train_cities: List of source city names
            test_cities: List of target city names
        
        Returns:
            TestResult with R² on test cities
        """
        logger.info("=== T3.3: Cross-City Stability ===")
        logger.info(f"  Train cities: {train_cities}")
        logger.info(f"  Test cities:  {test_cities}")
        
        pred_all = np.concatenate([Aj_predictions_per_city[c] for c in test_cities])
        true_all = np.concatenate([Aj_ground_truth_per_city[c] for c in test_cities])
        
        ss_res = np.sum((pred_all - true_all) ** 2)
        ss_tot = np.sum((true_all - np.mean(true_all)) ** 2)
        r2 = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
        
        logger.info(f"  R² on {len(test_cities)} held-out cities: {r2:.6f}")
        
        return TestResult(
            layer=3,
            test_name="T3.3_Cross_City_Stability",
            metric="R2",
            value=r2,
            details={
                "n_train_cities": len(train_cities),
                "n_test_cities": len(test_cities)
            }
        )


# ============================================================================
# LAYER 4: FULL SYSTEM DECOMPOSITION TEST
# ============================================================================

class Layer4_FullSystemDecomposition:
    """
    Quantify causal contribution of each module to final performance.
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.results = []
    
    def test_full_factorial_ablation(
        self,
        predictions: Dict[str, np.ndarray],
        T_ground_truth: np.ndarray,
        cpc_metric_fn
    ) -> Tuple[List[TestResult], pd.DataFrame]:
        """
        T4.1: Full Factorial Ablation Table
        
        Generate 2^3 = 8 ablations across decay, Oi, Aj
        
        Args:
            predictions: {
                'full': T_full,
                'no_decay': T_no_decay,
                'no_oi': T_no_oi,
                'no_aj': T_no_aj,
                'decay_only': T_decay_only,
                'oi_only': T_oi_only,
                'aj_only': T_aj_only,
                'baseline': T_baseline
            }
            T_ground_truth: True OD matrix
            cpc_metric_fn: Function to compute CPC
        
        Returns:
            (List of TestResults, ablation table DataFrame)
        """
        logger.info("=== T4.1: Full Factorial Ablation ===")
        
        ablation_configs = [
            ('full', True, True, True),
            ('no_decay', False, True, True),
            ('no_oi', True, False, True),
            ('no_aj', True, True, False),
            ('decay_only', True, False, False),
            ('oi_only', False, True, False),
            ('aj_only', False, False, True),
            ('baseline', False, False, False),
        ]
        
        results_list = []
        rows = []
        
        for config_name, has_decay, has_oi, has_aj in ablation_configs:
            T_pred = predictions.get(config_name)
            if T_pred is None:
                logger.warning(f"  Missing prediction for {config_name}")
                continue
            
            cpc = cpc_metric_fn(T_pred, T_ground_truth)
            logger.info(f"  {config_name:20s} | Decay: {has_decay} | Oi: {has_oi} | Aj: {has_aj} | CPC: {cpc:.6f}")
            
            results_list.append(TestResult(
                layer=4,
                test_name=f"T4.1_Ablation_{config_name}",
                metric="CPC",
                value=cpc,
                details={
                    "has_decay": has_decay,
                    "has_oi": has_oi,
                    "has_aj": has_aj,
                }
            ))
            
            rows.append({
                'Configuration': config_name,
                'Decay': has_decay,
                'Oi': has_oi,
                'Aj': has_aj,
                'CPC': cpc
            })
        
        ablation_table = pd.DataFrame(rows)
        return results_list, ablation_table
    
    def test_contribution_decomposition(
        self,
        ablation_table: pd.DataFrame
    ) -> List[ComponentContribution]:
        """
        T4.2: Contribution Decomposition
        
        Compute marginal gains for each component.
        
        Args:
            ablation_table: DataFrame from T4.1 with columns:
                           [Configuration, Decay, Oi, Aj, CPC]
        
        Returns:
            List of ComponentContribution objects
        """
        logger.info("=== T4.2: Contribution Decomposition ===")
        
        # Extract reference points
        full_cpc = ablation_table[
            (ablation_table['Decay']) & 
            (ablation_table['Oi']) & 
            (ablation_table['Aj'])
        ]['CPC'].values[0]
        
        baseline_cpc = ablation_table[
            (~ablation_table['Decay']) & 
            (~ablation_table['Oi']) & 
            (~ablation_table['Aj'])
        ]['CPC'].values[0]
        
        contributions = []
        
        # Decay contribution
        no_decay_cpc = ablation_table[
            (~ablation_table['Decay']) & 
            (ablation_table['Oi']) & 
            (ablation_table['Aj'])
        ]['CPC'].values[0]
        decay_contrib = ComponentContribution(
            component='decay',
            baseline_cpc=no_decay_cpc,
            with_component_cpc=full_cpc,
            delta_cpc=full_cpc - no_decay_cpc,
            variance_across_cities=0.0  # Will be computed if per-city data available
        )
        contributions.append(decay_contrib)
        logger.info(f"  Decay:    ΔCPC = {decay_contrib.delta_cpc:+.6f} ({decay_contrib.delta_cpc/(full_cpc-baseline_cpc)*100:+.1f}% of total gain)")
        
        # Oi contribution
        no_oi_cpc = ablation_table[
            (ablation_table['Decay']) & 
            (~ablation_table['Oi']) & 
            (ablation_table['Aj'])
        ]['CPC'].values[0]
        oi_contrib = ComponentContribution(
            component='outflow',
            baseline_cpc=no_oi_cpc,
            with_component_cpc=full_cpc,
            delta_cpc=full_cpc - no_oi_cpc,
            variance_across_cities=0.0
        )
        contributions.append(oi_contrib)
        logger.info(f"  Outflow:  ΔCPC = {oi_contrib.delta_cpc:+.6f} ({oi_contrib.delta_cpc/(full_cpc-baseline_cpc)*100:+.1f}% of total gain)")
        
        # Aj contribution
        no_aj_cpc = ablation_table[
            (ablation_table['Decay']) & 
            (ablation_table['Oi']) & 
            (~ablation_table['Aj'])
        ]['CPC'].values[0]
        aj_contrib = ComponentContribution(
            component='attraction',
            baseline_cpc=no_aj_cpc,
            with_component_cpc=full_cpc,
            delta_cpc=full_cpc - no_aj_cpc,
            variance_across_cities=0.0
        )
        contributions.append(aj_contrib)
        logger.info(f"  Attraction: ΔCPC = {aj_contrib.delta_cpc:+.6f} ({aj_contrib.delta_cpc/(full_cpc-baseline_cpc)*100:+.1f}% of total gain)")
        
        return contributions


# ============================================================================
# LAYER 5: ZERO-SHOT GENERALIZATION TEST
# ============================================================================

class Layer5_ZeroShotGeneralization:
    """
    Test robustness under extreme domain shift and zero-shot transfer.
    
    **Architecture**:
    1. GBDT (23 SHAP features) → Predicts O_i (outflow)
    2. Proposed Framework (gravity model) → Uses GBDT's O_i to predict OD matrix
    3. DeepGravity (oracle O_i) → Upper bound for comparison
    
    **Main Evaluation**: 
    - Performance of GBDT + Proposed Framework on held-out cities
    - Degradation vs DeepGravity (oracle): Shows impact of imperfect O_i estimation
    
    **Key Metrics**:
    - CPC with GBDT O_i (survey-free E2E)
    - CPC with oracle O_i (DeepGravity upper bound)
    - Performance gap: indicates O_i bottleneck severity
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.results = []
    
    def test_e2e_gbdt_proposed_vs_deepgravity(
        self,
        cities_heldout: List[str],
        T_predicted_gbdt_proposed: Dict[str, np.ndarray],
        T_predicted_deepgravity_oracle: Dict[str, np.ndarray],
        T_ground_truth: Dict[str, np.ndarray],
        cpc_metric_fn
    ) -> List[TestResult]:
        """
        T5.0: Zero-Shot E2E System Comparison
        
        Compare two end-to-end approaches:
        1. **Proposed Framework** (Gravity Decomposed):
           - GBDT (23 SHAP features) → O_i prediction
           - Parametric decay function
           - Enforces: T_ij = O_i × A_j × decay(d)
           - Interpretable, domain-constrained
        
        2. **DeepGravity** (Neural E2E, No Decomposition):
           - MLP (38 features) → Direct T_ij prediction
           - NO gravity constraints
           - T_ij = f(38 features) learned directly
           - Flexible, unconstrained learning
        
        **Purpose**: Evaluate which paradigm generalizes better to held-out cities.
        - Question: Is gravity decomposition helpful or limiting?
        - If DeepGravity >> Proposed: Decomposition is too restrictive
        - If Proposed ≈ DeepGravity: Gravity structure is appropriate
        
        Args:
            cities_heldout: List of held-out city names
            T_predicted_gbdt_proposed: {city: OD from Proposed Framework}
            T_predicted_deepgravity_oracle: {city: OD from DeepGravity E2E}
            T_ground_truth: {city: ground truth OD matrix}
            cpc_metric_fn: Function to compute CPC
        
        Returns:
            List of TestResults with performance comparison
        """
        logger.info("=" * 80)
        logger.info("T5.0: ZERO-SHOT E2E SYSTEM COMPARISON")
        logger.info("Proposed (Gravity Decomposed) vs DeepGravity (Neural E2E, No Decomposition)")
        logger.info("=" * 80)
        
        results = []
        gaps_per_city = []
        degradations = []
        
        for city in cities_heldout:
            if city not in T_predicted_gbdt_proposed or city not in T_predicted_deepgravity_oracle:
                logger.warning(f"  Missing predictions for {city}")
                continue
            if city not in T_ground_truth:
                logger.warning(f"  Missing ground truth for {city}")
                continue
            
            T_proposed = T_predicted_gbdt_proposed[city]
            T_deepgravity = T_predicted_deepgravity_oracle[city]
            T_true = T_ground_truth[city]
            
            # Compute CPC for both
            cpc_proposed = cpc_metric_fn(T_proposed, T_true)
            cpc_deepgravity = cpc_metric_fn(T_deepgravity, T_true)
            
            # Difference: positive = DeepGravity better, negative = Proposed better
            advantage = cpc_deepgravity - cpc_proposed  # Negative = Proposed is better
            relative_advantage_pct = (advantage / cpc_proposed * 100) if cpc_proposed > 0 else 0
            
            gaps_per_city.append(advantage)
            degradations.append(relative_advantage_pct)
            
            logger.info(f"\n  {city:20s}:")
            logger.info(f"    CPC (Proposed Framework): {cpc_proposed:.6f}")
            logger.info(f"    CPC (DeepGravity E2E):   {cpc_deepgravity:.6f}")
            logger.info(f"    Advantage (DG - Prop):   {advantage:.6f}")
            logger.info(f"    Relative advantage:      {relative_advantage_pct:.2f}%")
            
            results.append(TestResult(
                layer=5,
                test_name=f"T5.0_E2E_ZeroShot_{city}",
                metric="DeepGravity_vs_Proposed",
                value=advantage,
                details={
                    "city": city,
                    "cpc_proposed": float(cpc_proposed),
                    "cpc_deepgravity": float(cpc_deepgravity),
                    "advantage": float(advantage),
                    "relative_advantage_pct": float(relative_advantage_pct),
                    "notes": "Positive advantage = DeepGravity E2E better. Negative = Proposed better."
                }
            ))
        
        # Summary statistics
        if gaps_per_city:
            mean_gap = np.mean(gaps_per_city)
            std_gap = np.std(gaps_per_city)
            mean_degradation = np.mean(degradations)
            
            logger.info("\n" + "=" * 80)
            logger.info("SUMMARY: E2E System Comparison (Proposed vs DeepGravity E2E)")
            logger.info("=" * 80)
            logger.info(f"  Mean CPC (Proposed):          {np.mean([d[0] for d in zip(list(T_predicted_gbdt_proposed.values()), list(T_predicted_deepgravity_oracle.values()))]):.6f}")
            logger.info(f"  Mean CPC (DeepGravity E2E):   {np.mean([d[1] for d in zip(list(T_predicted_gbdt_proposed.values()), list(T_predicted_deepgravity_oracle.values()))]):.6f}")
            logger.info(f"  Mean advantage (DeepGravity): {-np.mean(gaps_per_city):.6f} (±{std_gap:.6f})")
            logger.info(f"  Cities evaluated:             {len(gaps_per_city)}")
            
            dg_wins = sum(1 for g in gaps_per_city if g > 0)
            prop_wins = len(gaps_per_city) - dg_wins
            logger.info(f"  Win rate:")
            logger.info(f"    - DeepGravity E2E wins: {dg_wins}/{len(gaps_per_city)} cities ({dg_wins/len(gaps_per_city)*100:.1f}%)")
            logger.info(f"    - Proposed wins:        {prop_wins}/{len(gaps_per_city)} cities ({prop_wins/len(gaps_per_city)*100:.1f}%)")
            
            logger.info(f"\nInterpretation:")
            logger.info(f"  - DeepGravity advantage > 0: Neural E2E outperforms gravity decomposition")
            logger.info(f"  - DeepGravity advantage < 0: Gravity structure provides useful constraint")
            logger.info(f"  - Win rate ~50%: Both approaches are competitive")
            logger.info("=" * 80 + "\n")
            
            results.append(TestResult(
                layer=5,
                test_name="T5.0_E2E_Summary",
                metric="DeepGravity_Advantage",
                value=-np.mean(gaps_per_city),
                details={
                    "mean_cpc_proposed": float(np.mean([d[0] for d in zip(list(T_predicted_gbdt_proposed.values()), list(T_predicted_deepgravity_oracle.values()))])),
                    "mean_cpc_deepgravity": float(np.mean([d[1] for d in zip(list(T_predicted_gbdt_proposed.values()), list(T_predicted_deepgravity_oracle.values()))])),
                    "dg_wins": dg_wins,
                    "prop_wins": prop_wins,
                    "n_cities": len(gaps_per_city),
                    "interpretation": "Positive = DeepGravity better, Negative = Proposed better"
                }
            ))
        
        return results

    def test_morphology_split(
        self,
        city_morphology_dict: Dict[str, str],
        cpc_per_city: Dict[str, float],
        cpc_metric_fn
    ) -> List[TestResult]:
        """
        T5.1: Morphology-Based Split
        
        Evaluate performance across:
        - dense cities
        - suburban cities
        - polycentric cities
        - coastal cities
        
        Args:
            city_morphology_dict: {city: morphology_type}
            cpc_per_city: {city: cpc_value}
            cpc_metric_fn: (unused here, for API consistency)
        
        Returns:
            List of TestResults by morphology
        """
        logger.info("=== T5.1: Morphology-Based Split ===")
        
        morphology_cpcs = {}
        for city, morphology in city_morphology_dict.items():
            if city not in cpc_per_city:
                continue
            if morphology not in morphology_cpcs:
                morphology_cpcs[morphology] = []
            morphology_cpcs[morphology].append(cpc_per_city[city])
        
        results = []
        for morphology, cpcs in morphology_cpcs.items():
            mean_cpc = np.mean(cpcs)
            std_cpc = np.std(cpcs)
            logger.info(f"  {morphology:15s}: mean_CPC={mean_cpc:.6f}, std={std_cpc:.6f}, n={len(cpcs)}")
            
            results.append(TestResult(
                layer=5,
                test_name=f"T5.1_Morphology_{morphology}",
                metric="Mean_CPC",
                value=mean_cpc,
                details={
                    "morphology": morphology,
                    "mean_cpc": float(mean_cpc),
                    "std_cpc": float(std_cpc),
                    "n_cities": len(cpcs)
                }
            ))
        
        return results
    
    def test_extreme_transfer(
        self,
        transfer_pairs: List[Tuple[str, str]],
        T_predicted: Dict[Tuple[str, str], np.ndarray],
        T_ground_truth: Dict[str, np.ndarray],
        cpc_metric_fn
    ) -> List[TestResult]:
        """
        T5.2: Extreme Transfer
        
        Train → test on mismatched cities:
        - NYC → rural-like cities
        - LA → grid cities
        - Houston → dense cities
        
        Args:
            transfer_pairs: List of (source_city, target_city) tuples
            T_predicted: {(source, target): predicted_matrix}
            T_ground_truth: {city: ground_truth_matrix}
            cpc_metric_fn: Function to compute CPC
        
        Returns:
            List of TestResults for each transfer
        """
        logger.info("=== T5.2: Extreme Transfer ===")
        
        results = []
        for source, target in transfer_pairs:
            key = (source, target)
            if key not in T_predicted or target not in T_ground_truth:
                logger.warning(f"  Missing data for transfer {source} → {target}")
                continue
            
            T_pred = T_predicted[key]
            T_true = T_ground_truth[target]
            
            cpc = cpc_metric_fn(T_pred, T_true)
            logger.info(f"  {source:15s} → {target:15s}: CPC={cpc:.6f}")
            
            results.append(TestResult(
                layer=5,
                test_name=f"T5.2_Transfer_{source}_to_{target}",
                metric="CPC",
                value=cpc,
                details={
                    "source_city": source,
                    "target_city": target
                }
            ))
        
        return results
    
    def test_feature_perturbation_stress(
        self,
        features_base: Dict[str, np.ndarray],
        T_ground_truth: np.ndarray,
        perturbation_levels: Dict[str, Tuple[float, float]],
        cpc_metric_fn
    ) -> List[TestResult]:
        """
        T5.3: Feature Perturbation Stress Test
        
        Inject noise into:
        - POI ±10%
        - population ±10–20%
        - road density ±15%
        
        Args:
            features_base: {'POI': array, 'POP': array, 'ROAD': array, ...}
            T_ground_truth: True OD matrix
            perturbation_levels: {'POI': (min_pct, max_pct), ...}
            cpc_metric_fn: Function to compute CPC
        
        Returns:
            List of TestResults for each feature perturbation
        """
        logger.info("=== T5.3: Feature Perturbation Stress Test ===")
        
        results = []
        cpc_baseline = cpc_metric_fn(np.column_stack(list(features_base.values())), T_ground_truth)
        logger.info(f"  Baseline CPC (no perturbation): {cpc_baseline:.6f}")
        
        for feature_name, (min_pct, max_pct) in perturbation_levels.items():
            if feature_name not in features_base:
                continue
            
            # Random noise between min and max
            noise_pct = np.random.uniform(min_pct, max_pct)
            noise_factor = noise_pct / 100.0
            
            features_perturbed = features_base.copy()
            features_perturbed[feature_name] = features_base[feature_name] * (1 + np.random.normal(0, noise_factor, features_base[feature_name].shape))
            features_perturbed[feature_name] = np.maximum(features_perturbed[feature_name], 0)  # Clip
            
            X_perturbed = np.column_stack([features_perturbed[f] for f in features_base.keys()])
            cpc_perturbed = cpc_metric_fn(X_perturbed, T_ground_truth)
            degradation = (cpc_baseline - cpc_perturbed) / cpc_baseline if cpc_baseline > 0 else 0
            
            logger.info(f"  {feature_name:6s} ±{noise_pct:.1f}%: CPC={cpc_perturbed:.6f}, degradation={degradation:.4%}")
            
            results.append(TestResult(
                layer=5,
                test_name=f"T5.3_Perturbation_{feature_name}",
                metric="CPC",
                value=cpc_perturbed,
                details={
                    "perturbed_feature": feature_name,
                    "perturbation_pct": float(noise_pct),
                    "degradation_pct": float(degradation * 100)
                }
            ))
        
        return results


# ============================================================================
# REPORTING & UTILITIES
# ============================================================================

class EvaluationReporter:
    """Generate comprehensive evaluation reports."""
    
    def __init__(self, output_dir: Path = None):
        self.output_dir = output_dir or Path("./evaluation_results")
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def save_results(self, all_results: List[TestResult], filename: str = "results.json"):
        """Save all test results to JSON."""
        filepath = self.output_dir / filename
        results_dicts = [r.to_dict() for r in all_results]
        
        with open(filepath, 'w') as f:
            json.dump(results_dicts, f, indent=2)
        logger.info(f"Results saved to {filepath}")
    
    def save_ablation_table(self, table: pd.DataFrame, filename: str = "ablation_table.csv"):
        """Save ablation table to CSV."""
        filepath = self.output_dir / filename
        table.to_csv(filepath, index=False)
        logger.info(f"Ablation table saved to {filepath}")
    
    def generate_summary(self, all_results: List[TestResult]) -> str:
        """Generate text summary of evaluation."""
        summary = "=" * 80 + "\n"
        summary += "5-LAYER EVALUATION FRAMEWORK SUMMARY\n"
        summary += "=" * 80 + "\n\n"
        
        by_layer = {}
        for result in all_results:
            if result.layer not in by_layer:
                by_layer[result.layer] = []
            by_layer[result.layer].append(result)
        
        for layer in sorted(by_layer.keys()):
            summary += f"LAYER {layer}\n"
            summary += "-" * 80 + "\n"
            for result in by_layer[layer]:
                summary += f"  {result.test_name:50s} | {result.metric:20s} = {result.value:12.6f}\n"
            summary += "\n"
        
        return summary


# ============================================================================
# EXAMPLE USAGE / MAIN
# ============================================================================

if __name__ == "__main__":
    logger.info("5-Layer Evaluation Framework for PSF-CTF Paper")
    logger.info("This module provides modular testing for all evaluation components.")
    logger.info("\nImport and use the layer classes in your main evaluation script:")
    logger.info("  from evaluation_framework_5layer import Layer1_DecayIdentification, ...")
