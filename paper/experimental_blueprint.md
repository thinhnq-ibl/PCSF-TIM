# EXPERIMENTAL BLUEPRINT V2.0

## Overall Strategy: Scientific Validation
The Experiment section (Section 5) must be titled **Experimental Validation**. The goal is not merely to prove that the proposed method beats a baseline, but to systematically test each component of the central scientific hypothesis.

### Narrative Flow
`Scientific Hypothesis $\to$ Evidence 1 (Can latent behavior be recovered?) $\to$ Evidence 2 (Is recovered behavior useful?) $\to$ Evidence 3 (Can recovered behavior enable transferable calibration?) $\to$ Evidence 4 (Methodological validation) $\to$ Scientific Conclusion`

---

## Section Guidelines

### 5.1 Experimental Protocol
**Objective**: Explicitly link the experimental setup to the scientific hypothesis.
**Logic**: 
`Scientific hypothesis $\to$ RQ1 $\to$ RQ2 $\to$ RQ3`

### 5.2 RQ1: Can aggregate mobility data preserve sufficient information to recover latent city-specific distance-decay?
**Objective**: Test the identifiability and validity of the behavioral parameter.
**Logic**: 
`Parameter identifiability $\to$ Behavioral validity $\to$ Real aggregate data $\to$ Robustness`
**Key Elements**:
- **Interpretation**: Focus on behavior, not parameters. The recovered parameters indicate that aggregate mobility data preserve the dominant behavioral signature governing interactions.
- **Section 5.2.3**: Title as `Behavioral Recovery from Real Aggregate Mobility Products`. Meta MDM should be framed as real-world evidence, not merely a dataset.
- **Conclusion for RQ1**: State that aggregate mobility contains sufficient behavioral information (scientific discovery).

### 5.3 RQ2: Is recovered behavior informative?
**Objective**: Quantify the contribution of the recovered distance-decay behavior relative to structural components.
**Logic**: 
`Recovered behavior $\to$ How important? $\to$ Ablation $\to$ Shapley $\to$ Behavior dominates`
**Key Elements**:
- **Ablation Interpretation**: Emphasize that the most predictive information originates from behavioral distance friction.
- **Shapley Interpretation**: Present the high attribution (e.g., 85.8%) as a core discovery proving that Behavior $\gg$ Production/Attraction.

### 5.4 RQ3: Can recovered behavior enable transferable gravity calibration?
**Objective**: Demonstrate practical utility as a downstream application of the scientific discovery.
**Logic**: 
`Behavior recovered $\to$ Gravity calibrated $\to$ OD generated $\to$ Deployment`

### Paradigm Comparison
**Objective**: Delineate PIGF's positioning against existing paradigms.
**Format**: Use a summary table for immediate clarity.
| Paradigm     | Learn Flow | Learn Behavior | Need OD | Transfer |
| ------------ | ---------- | -------------- | ------- | -------- |
| DeepGravity  | Yes        | No             | Yes     | Limited  |
| NeuroGravity | Yes        | Partial        | Yes     | Medium   |
| PIGF         | No         | Yes            | No      | Yes      |

### 5.5 Methodological Validation
**Objective**: Validate the structural necessity of the proposed components. *(Note: Formerly titled "Ablation").*

### 5.6 Robustness Analysis
**Objective**: Assess performance stability across varied conditions.

### 5.7 Scientific Findings
**Objective**: Conclude the section with three explicit scientific discoveries rather than a generic summary.

- **Finding 1 (Recoverability)**: Aggregate mobility preserves sufficient information to recover latent distance-decay.
- **Finding 2 (Behavioral Dominance)**: Recovered distance-decay constitutes the dominant behavioral component governing gravity-based OD prediction.
- **Finding 3 (Practical Utility)**: Zero-shot gravity calibration built upon recovered distance-decay enables competitive survey-free OD estimation.

---
## Final Blueprint Structure

- **Section 5: Experimental Validation**
  - 5.1 Experimental Protocol
  - 5.2 RQ1: Can latent behavior be recovered?
  - 5.3 RQ2: Is recovered behavior informative?
  - 5.4 RQ3: Can recovered behavior enable transferable gravity calibration?
  - 5.5 Methodological Validation
  - 5.6 Robustness Analysis
  - 5.7 Scientific Findings
