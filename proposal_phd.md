# PhD Dissertation Proposal: Learning Human Mobility from Aggregate Observations

## Title
**Learning Human Mobility from Aggregate Observations: Sufficiency of Observable Information and Complementary Urban Context for Origin-Destination Matrix Reconstruction**

### Subtitle
*Towards Mechanism-Based Human Mobility Science through Observability, Identifiability, and Empirical Defensibility*

---

## 7-Stage Scientific Backbone (Zero-Target-OD Baseline)

$$\boxed{\text{Observation} \longrightarrow \text{Recoverable Information} \longrightarrow \text{Observation Sensitivity} \longrightarrow \text{Complementary Context} \longrightarrow \text{OD Reconstruction} \longrightarrow \text{Independent Validation}}$$

---

## Core Scientific Premises

$$\boxed{\text{Aggregate Observation } \neq \text{ Complete Information}}$$

$$\boxed{\text{Input Consistency } \neq \text{ Reconstruction Validity}}$$

$$\boxed{\text{Validity Requires Improvement on Unconstrained OD Properties}}$$

> **Central Dissertation Master Statement (Frozen Key Sentence):**  
> **"This dissertation investigates the sufficiency of observable information for reconstructing urban spatial interaction under mobility data scarcity. It examines what information is retained or lost under aggregate mobility observation, how observation design affects recoverability, and how complementary open urban information improves OD reconstruction when the mobility observation alone is insufficient."**

---

# 1. Introduction & Problem Statement

Human mobility patterns shape critical urban planning decisions, transportation infrastructure investments, disaster response protocols, and public health interventions. Despite their importance, comprehensive Origin-Destination (OD) travel matrices remain severely unavailable in most cities of the Global South due to the prohibitive financial and administrative costs of disaggregated household travel surveys.

In recent years, aggregate mobility products—most prominently Meta's Movement Distribution Maps (MDM) \citep{MetaMovementDistributionMaps}—have become widely accessible across global urban regions. These products provide daily movement-range information in an aggregate map, serving as a real-world instance of highly compressed aggregate mobility observations. They reduce the granularity of disclosed movement information by removing individual-level and pairwise spatial identities, providing instead coarse, distance-binned Travel Length Distributions (TLDs). 

This dissertation addresses the fundamental scientific challenge of recovering disaggregated OD mobility matrices from aggregate mobility observations under extreme data scarcity. We reframe this challenge as an information sufficiency problem: *How much spatial-interaction information can be recovered from incomplete aggregate mobility observations, and what additional observable information is required for defensible OD reconstruction?*

---

# 2. Literature Baseline & Identified Scientific Limits

Reconstructing spatial interactions from partial data has a rich history in transportation planning. Traditional OD estimation from traffic link counts has long identified the underdetermined nature of the inverse problem, utilizing prior target surveys, Bayesian updates, and network regularization to constrain the unknowns (IIASA literature). Similarly, modern geographic flow generation (such as DeepGravity; Nature 2021) leverages deep learning and open spatial features ($X_U$) like land use, road networks, and POIs to generate commuting flows across different cities. Recent work like TransGM (2026) explores cross-city transfer but relies on limited target flow observations for adaptive calibration.

In spatial interaction modeling, foundational work by Fotheringham (1981, 1986) establishes that estimated distance-decay parameters ($\hat{\boldsymbol{\theta}}$) are systematically influenced by the spatial configuration of opportunity fields, demonstrating that observed decay rates are not pure behavioral parameters. Liang et al. (2013) confirm this by demonstrating that aggregate exponential travel-length distributions can emerge naturally from exponential urban population density decay. Gallotti et al. (2024) further demonstrate that observed mobility statistics and downstream urban conclusions vary systematically across measurement pipelines.

While these streams of literature are individually mature, their intersection has received limited systematic empirical attention. Specifically:
1. **Gap 1 — Observation Sufficiency:** What OD-relevant information survives highly compressed aggregate mobility observations (such as Meta MDM)? Existing work demonstrates that highly reduced mobility summaries such as median travel time can support single-parameter calibration when the spatial system is otherwise fully specified (Merlin 2020), but does not systematically characterize how observation resolution, bin geometry, and spatial support govern recoverability from compressed aggregate mobility representations under zero-target-OD constraints.
2. **Gap 2 — Observation Design:** How do spatial support, bin resolution, bin geometry, and model complexity affect recoverability? Existing studies evaluate data sparsity generally, but the joint effect of these observation design parameters on downstream parameter recoverability has received limited attention.
3. **Gap 3 — Complementary Reconstruction Value:** How much marginal reconstruction improvement ($\Delta\text{CPC}$) is obtained from adding open urban spatial information under the same mobility observation constraints? Although geographic variables improve flow prediction (e.g. DeepGravity, Imagery2Flow 2025), it remains less systematically quantified how much marginal OD reconstruction improvement each additional open data source contributes on top of incomplete aggregate observations.

When complete target-city OD ground truth is unavailable, reconstruction must be evaluated against independent partial observations and unconstrained OD properties rather than against the observations used to construct the model. This validation requirement is addressed as a methodological contribution (C4) in the HCMC case study.

---

# 3. Paper 1 Formulation — Information Retention in Aggregate Mobility Observations

* **Research Gap 1 (Observation Information & Compression Sensitivity - Gaps A & B):** Calibration models traditionally assume continuous distance observations or disaggregated flows. However, there is limited systematic understanding of what spatial-interaction information is retained by binned aggregate observations themselves, and how spatial support, distance resolution, and bin geometry control that information loss under varying model complexity.
* **Paper 1 Mission:** Parametric statistical inference of collective distance sensitivity from aggregate TLDs, utilizing $\beta$ as an interpretable measurement probe of information degradation across Exponential, Power-law, and Tanner models.
* **Claim P1-A (Information Retention):** Three-bin aggregation preserves non-trivial distance-related ordering and trend information.
* **Claim P1-B (Signal Retention vs. Parameter Fidelity):** Coarse aggregation can retain detectable distance-related signal while substantially degrading quantitative parameter fidelity ($R^2 = 0.9624$, Multi-start $\text{CV} = 0.00\%$ under 20-bins; $\text{Mean Error} \approx 36.94\%$ under 3-bins).

---

# 4. Paper 1 Methodology & Observability Analysis

Paper 1 formulates parametric statistical inference of collective distance sensitivity using a **3-Tier Information Probe Architecture** to evaluate how information sufficiency degrades under compression. 

Exponential deterrence is used as the primary one-parameter probe of information retention. Power-law provides a matched-complexity robustness specification, while Tanner is used as a higher-complexity stress test. Preliminary evidence from Chicago indicates that compression-induced parameter degradation is not unique to the exponential specification and becomes more severe for the two-parameter Tanner form.

| Probe Tier | Deterrence Formulation | Parameters | Role in Information Sufficiency Framework |
| :--- | :--- | :---: | :--- |
| **Primary Probe** | $f_{\exp}(d) = \exp(-\beta d)$ | 1 | Primary one-parameter probe of information retention (simple interpretation, numerically stable for short distances $d \to 0$, isolating compression loss from preprocessing choices). |
| **Robustness Check** | $f_{\text{power}}(d) = d^{-\alpha}$ | 1 | Matched-complexity robustness check to confirm compression findings are not specific function artifacts. |
| **Complexity Test** | $f_{\text{Tanner}}(d) = d^{-\alpha} \exp(-\beta d)$ | 2 | Higher-complexity stress test to evaluate parameter identifiability as representation complexity increases. |

The likelihood of observing aggregate binned trip counts $\boldsymbol{y} = (y_1, y_2, \dots, y_K)^T$ across distance bins $k \in \{1, \dots, K\}$ is maximized via a robust grid-start bounded optimization:

$$\boldsymbol{y} \sim \text{Multinomial}(N, \boldsymbol{p}(\boldsymbol{\theta}))$$

```text
Aggregate TLD (Meta 3-bin) ──► Grid-Start Bounded Likelihood ──► Parameter Optimizer ──► Primary Probe (β_3bin = 0.0989)
```

By scanning the likelihood profile, we avoid local minima traps caused by the clipping penalty ceiling when outer bins have near-zero trip counts.

---

# 5. Paper 2 Formulation — Complementary Information for OD Reconstruction

* **Research Gap 2 (Complementary Reconstruction Value - Gap 3):** Aggregate mobility observations are mathematically underdetermined. When the mobility observation itself is incomplete and quantitatively degraded, it remains less systematically quantified how much marginal OD reconstruction improvement is obtained by adding each open urban data source ($X_U$) under the same aggregate observation constraints.
* **Core Sub-Question (Spatial Context Robustness):** *To what extent can independent spatial context compensate for distance-decay parameter uncertainty in downstream OD reconstruction?*
* **Paper 2 Mission:** Spatial representation learning (Spatial GNNs) to map open spatial features $X_U$ (Population, POIs, Area, Roads, Accessibility, etc.) into operational production and attraction potentials $(O_i, A_j)$.
* **Spatial Complementarity Mechanism (T32):** Spatial variation in population and opportunities supplies complementary allocation information that is not directly captured by aggregate distance observations. Among the tested open spatial sources, population and POI density provide most of the observed incremental CPC improvement, accounting for approximately **97.6%** of the observed CPC gain provided by the full open spatial feature set under clean 3-bin TLD-MLE conditions.

---

# 6. Paper 2 Methodology & Spatial Context Integration

Paper 2 employs a Graph Neural Network architecture as a candidate mechanism to map open spatial features $X_U$ into operational structural quantities $(O_i, A_j)$ in spatial interaction models:

$$X_U \xrightarrow{\text{Spatial GNN}} (O_i, A_j)$$

$$\hat{T}_{ij} = O_i A_j f(d_{ij}; \hat{\boldsymbol{\theta}})$$

```text
Open Features X_U ──────► Spatial GNN ────► Potentials (O_i, A_j) ──┐
                                                                   ├──► Reconstructed Flows T_ij
Aggregate TLD D_agg ────► Robust MLE ─────► Deterrence Parameter θ ─┘
```

---

# 7. Operational Integration of Observable Information Sources

The reconstruction framework integrates two independently sourced information streams to constrain the underdetermined OD solution space:

$$\text{Aggregate Mobility Observation } (\hat{\boldsymbol{\theta}}) + \text{Open Urban Spatial Context } (O_i, A_j) \longrightarrow \hat{T}_{ij}$$

$$\hat{T}_{ij} = O_i A_j f(d_{ij}; \hat{\boldsymbol{\theta}})$$

The aggregate mobility observation (TLD) provides a compressed distance-sensitivity signal from which a decay parameter $\hat{\boldsymbol{\theta}}$ is inferred via robust MLE. Open urban spatial features ($X_U$) independently supply structural opportunity context — production and attraction potentials $(O_i, A_j)$ — that constrains the spatial allocation of flows. Local parameter inference of $\boldsymbol{\theta}$ is adopted as a modeling principle to respect city-specific distance-sensitivity profiles.

Because the aggregate observation alone is insufficient to uniquely determine the disaggregated OD matrix, complementary open urban information is required to narrow the solution space. The two information streams are combined operationally through the gravity integration model, rather than being assumed to represent empirically independent or uniquely separable components of mobility.

---

# 8. Ho Chi Minh City Case Study Strategy

Ho Chi Minh City (HCMC) represents a high-priority, extreme data-scarcity urban domain in Southeast Asia. Lacking complete disaggregated OD travel matrices, HCMC serves as the ultimate real-world application testbed. The framework is zero-target-OD: target-city reconstruction uses open spatial features ($X_U$) and the aggregate travel-distance distribution ($D_{\text{target}}$) to infer a local distance-interaction parameterization ($\hat{\boldsymbol{\theta}}$), while explicitly avoiding disaggregated target-city OD observations.

```text
HCMC Open Spatial Features (OSM, WorldPop, POI) ──► Potentials (O_i, A_j) ──┐
                                                                            ├──► Reconstructed HCMC OD Matrix
Meta MDM HCMC Aggregate TLD (3-bin) ──────────────► Deterrence Parameter θ ─┘
```

---

# 9. Evaluation Paradigm & Unconstrained Properties

In strict adherence to the Evaluation Principle (*"Matching the Meta input is merely in-sample consistency. It is not evidence of structural OD recovery"*), the framework is evaluated on **unconstrained properties of OD allocation**—spatial allocation characteristics that were *not* directly constrained by the input data:

```text
                      UNCONSTRAINED OD PROPERTIES
       ┌───────────────────────────┼───────────────────────────┐
       ▼                           ▼                           ▼
Fine-Resolution Distance      Directional Spatial         Inter-District Corridor
  Decay Curve Shape           Flow Asymmetry              Arterial Allocation
(Beyond input coarse bins)   (Origin-Destination ratio)   (Traffic flow consistency)
```

Validation follows a **3-Level Indirect Validation Hierarchy**:
1. **Level 1 — Model Diagnostics:** Conservation of origin production and destination attraction sums ($\sum_j T_{ij} = O_i, \sum_i T_{ij} = A_j$) and numerical consistency.
2. **Level 2 — Independent Partial Observations:** Auxiliary validation against bus smart card tap counts, arterial corridor volumes, and district commuting censuses.
3. **Level 3 — Falsification & Sensitivity Tests:** Shuffled opportunity fields, perturbed deterrence parameters, or incorrect spatial context must demonstrably degrade external alignment metrics.

---

# 10. Preliminary Feasibility Evidence (v13.0 Audited Evidence Base)

The pre-validation suite was executed across the **50 US Metropolitan Areas Dataset** under a controlled simulation paradigm ($\text{Full OD} \to \text{Meta 3-bin} \to \text{Hide OD} \to \text{Reconstruct} \to \text{Reveal OD}$):

### Master Experiment Registry & Quantitative Results

| Experiment | Dataset & Cities | Training Protocol | Available Inputs | Target OD Status | Key CPC Metric |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **T20 Leakage Audit** | 40 train / 10 test cities | RF on open spatial features $X_U$ | Aggregate TLD + Open $X_U$ | Hidden | **$0.5948$** (Transferred) vs **$0.5463$** (Uniform Baseline) [**Clean Gain $+0.0485$**] |
| **T21 50-City LOOCV** | 50 US cities (LOOCV) | 49 train / 1 test fold | Aggregate TLD + Open $X_U$ | Hidden | Mean **$0.6162$** (Median **$0.6249$**, $95\%\text{ CI } [0.5997, 0.6317]$ under clean beta) |
| **T22 Baseline Benchmark** | 10 unseen test cities | Common baseline protocol | Open spatial features | Hidden | **$0.5948$** (vs Gravity $0.5463$, Radiation $0.5257$, Uniform $0.4482$) |
| **Seed Reliability Audit** | 5 Random Seeds | Multi-seed RF protocol | Open spatial features $X_U$ | Hidden | **$0.5832 \pm 0.0006$** ($\text{CV} = 0.0965\% < 0.1\%$) |
| **T26–T27 Similarity Audit** | 15 cities (105 pairs) | Pairwise RF transfer | Raw spatial feature vectors | Hidden | $\rho = +0.0955$ ($p = 0.1681$). [**Simple structural similarity does NOT significantly predict transfer**] |
| **T28 Support Search** | Atlanta Case Study | Aggregated node clustering | $N/1 \to N/32$ | N/A | Support-robust (~3-5% error) down to $N/16$; breakdown at $N/32$ |
| **T29 Compression Grid** | Chicago Case Study | Binned MLE inference | 20, 10, 5, 3, 2, 1 bins | N/A | 20-bin ($0.77\%$) $\to$ 3-bin ($44.42\%$) $\to$ 1-bin ($100\%$ collapse) |
| **T30 Cut-Point Shift** | Chicago Case Study | Cut-point shift $-20\% \to +20\%$ | Shifted 3-bin cut-points | N/A | Error shifts $55.5\% \to 33.3\%$ (Jointly count & geometry dependent) |
| **T32 Structural Ablation** | 40 train / 10 test cities | Feature subset RF models | Subsets of $X_U$ | Hidden | Pop + POI: **$0.5950$** (~97.6% of full $R_S$ gain $+0.0499$) |
| **T33 Failure Taxonomy** | 50 US cities (LOOCV) | Multivariable OLS regression | City characteristics | Hidden | $\text{CPC} \sim \log(N)$ yields $\beta = -0.0611$ (scale increases difficulty) |
| **T34 Structural Compensation** | 40 train / 10 test cities | Perturbed beta RF models | Perturbed beta + Open $X_U$ | Hidden | CPC Gain stable ($+0.0411$ to $+0.0530$) across $\pm 60\%$ beta perturbation |
| **T35 Deterrence Robustness** | Chicago Case Study | Multinomial MLE (Exp, Pow, Tan) | 20, 10, 5, 3 bins | N/A | Exp ($0.77\% \to 44.4\%$), Power ($25.9\% \to 36.9\%$), Tanner ($65.3\% \to 96.2\%$ avg error) |

---

# 11. Summary of Scientific Contributions

1. **C1 — Aggregate Mobility Information Characterization:** An empirical and methodological characterization of the information retained and lost under aggregation/compression.
2. **C2 — Observation-Sensitivity Framework:** Quantifying the joint effects of spatial support, bin count, and bin geometry on parameter recoverability.
3. **C3 — Complementary-Information OD Reconstruction:** A zero-target-OD reconstruction methodology that integrates aggregate observations with open spatial context ($X_U$).
4. **C4 — Empirical Defensibility Framework:** Evaluating reconstruction quality using unconstrained properties and indirect validation, with HCMC acting as the applied case study.

---

# 12. Risks, Boundary Conditions & Phrasing Controls

To maintain scientific defensibility, all thesis claims are bounded by explicit empirical constraints:

* **US Pre-Validation Boundary:** Preliminary evidence is established on US metropolitan benchmarks; real-world applicability to HCMC remains a testable empirical hypothesis ($H_4$).
* **Scale & Dimensionality Bound (T33):** Several medium-scale systems (e.g. Arlington: $\text{CPC} \approx 0.6961$; Wichita: $\text{CPC} \approx 0.6947$) achieve higher reconstruction accuracy, whereas some large, high-dimensional metropolitan systems (e.g. New York: $\text{CPC} \approx 0.4329$; Chicago: $\text{CPC} \approx 0.5035$; Los Angeles: $\text{CPC} \approx 0.5121$) represent a substantially harder regime.
* **Negative Evidence on Feature Similarity (T26–T27):** Proper cross-city model transfer reveals that simple structural similarity in raw feature space does not significantly predict transfer performance directly ($\rho = 0.0955, p = 0.1681$).
* **Epistemic Boundary of Integration (RQ3):** Reconstructing flows evaluates the explanatory and predictive adequacy of the proposed operational integration framework under the specified model, not causal truth in reality.
* **Robustness of Spatial Context to Distance Misspecification (T34):** In downstream OD reconstruction, the incremental reconstruction gain provided by independent open spatial features is highly robust to parameter misspecification in the distance decay function. In T34, when the true decay parameter $\beta^*$ is deliberately perturbed by $\pm 60\%$, the incremental CPC gain provided by independent spatial features remains stable (ranging between $+0.0411$ and $+0.0530$). This controlled sensitivity experiment indicates that independent spatial context bounds the underdetermined solution space, maintaining reconstruction robustness even under moderate-to-large misspecification of the distance component.
* **Deterrence Function Robustness Boundary (T35):** Deterrence functions are employed as *information probes* rather than absolute ground-truth representations. In the Chicago case study, parameter fidelity deteriorates under increasing compression for both exponential and power-law specifications, while the two-parameter Tanner form exhibits substantially greater instability. This stress-test illustration supports the hypothesis that higher parameterization increases information demand, though multi-city replication would be required to claim this as a universal boundary.

---

# 13. Master Scoped Dissertation Claim Status Matrix (v13.0+)

| Scientific Claim | Audited Evidence Status | Phrasing Constraint & Boundary |
| :--- | :--- | :--- |
| **Aggregate TLD retains distance-related interaction signal** | **Strongly Pre-validated** | 3-bin preserves non-trivial distance-related ordering and trend information. |
| **Compression reduces quantitative fidelity** | **Strongly Pre-validated** | Parameter magnitude error grows $0.77\% \to 44.42\% \to 100\%$ collapse at 1-bin. |
| **Bin geometry materially affects retained signal** | **Strongly Pre-validated** | T30: Shift $-20\% \to +20\%$ alters parameter error ($55.5\% \to 33.3\%$). |
| **Aggregate TLD does not identify OD uniquely** | **Demonstrated (Control)** | Empirically supported by Q5 ($\text{JSD} = 0.0000$, yet $\text{CPC} = 0.5373$). |
| **Open urban spatial information improves recovery** | **Demonstrated Feasibility** | Clean 50-city LOOCV demonstrates end-to-end reconstruction feasibility ($\text{Mean CPC} = 0.6162, 95\%\text{ CI } [0.5997, 0.6317]$); net improvement over baseline ($\Delta\text{CPC} = +0.0485$, $95\%\text{ CI } [0.0308, 0.0527]$) is established via T20/T32. |
| **Multi-seed protocol reliability** | **High Reliability** | Multi-seed $\text{CPC} = 0.5832 \pm 0.0006$, $\text{CV} = 0.0965\%$. |
| **Pop + POI account for ~97.6% of spatial context gain** | **Strong Mechanism Evidence** | T32 Ablation: Pop + POI accounts for ~97.6% of observed full open spatial feature gain ($+0.0499$). |
| **Scale log(N) increases difficulty** | **Regression Associated** | $\text{CPC} \sim \log(N)$ yields $\beta = -0.0611$ after controlling for density and sparsity. |
| **Transferability follows simple feature similarity** | **NOT SUPPORTED** | T26–T27: $\rho = +0.0955$ ($p = 0.1681$). Raw structural similarity does not predict transfer. |
| **Incremental value of open urban spatial information is robust to distance-parameter misspecification** | **Preliminary robustness evidence** | T34: Incremental CPC gain remains stable ($+0.0411$ to $+0.0530$) across $\pm 60\%$ beta perturbation. |
| **Information loss and complexity bounds are robust to deterrence functional forms** | **Preliminary complexity evidence** | T35: Chicago case study shows parameter fidelity deteriorates for Exp/Power and Tanner. Higher parameterization increases information demand. |
| **HCMC real-world applicability** | **Feasibility Justified** | US cities results provide sufficient feasibility evidence to justify testing in HCMC. |

---

# 14. Research Timeline & Milestones

```text
2026 Q3: Proposal Defense & Paper 1 Submission (Aggregate Mobility Observability)
2026 Q4: Paper 2 Submission (Transferable Structural Complementarity for OD Recovery)
2027 Q1: HCMC Data Pipeline Integration & Multi-Level Indirect Validation
2027 Q2: Full Dissertation Writing & Pre-defense Review
2027 Q3: Final PhD Dissertation Defense
```

---
*Status: Updated V13.0+ — Master PhD Proposal Document (Clean Audited Evidence Base).*
