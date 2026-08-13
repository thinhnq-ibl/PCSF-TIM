# PhD Dissertation Proposal

## Title
**Learning Human Mobility from Aggregate Observations: Measurement Validity and Marginal Reconstructive Value of Privacy-Preserved Constraints**

## Subtitle
*Characterizing what mobility information survives observation processes and quantifying the non-redundant OD information it contributes beyond urban context*

---

## Scientific Backbone (Information-Centric Architecture)

$$\boxed{\text{Observation Operator } \mathcal{O}_{\psi} \longrightarrow \text{Validity Domain (RQ1)} \longrightarrow \text{Augmented Recovery} \longrightarrow \text{Marginal Value (RQ2)} \longrightarrow \text{Independent Validation}}$$

$$\text{Paper 1: Is the observation valid?} \quad \longrightarrow \quad \text{Paper 2: If valid, is it actually informative for OD?}$$

---

## Core Scientific Premises

$$\boxed{\text{Aggregate Observation } \neq \text{ Complete Information}}$$
$$\boxed{\text{Valid Measurement } \not\Rightarrow \text{ Useful OD Information}}$$
$$\boxed{\text{Validity Requires Improvement on Unconstrained OD Properties}}$$

> **Central Dissertation Master Statement (Frozen Key Sentence):**  
> *"This dissertation investigates not whether aggregate mobility data can simply be fitted to an OD model, but first whether the observed signal remains valid after information-reducing observation processes, and then how much destination-resolved OD information that validated signal contributes beyond independently observed urban context, using Meta Movement Distribution as the principal empirical testbed."*

---

# 1. Introduction & Problem Statement

Human mobility patterns shape critical urban planning decisions, transportation infrastructure investments, disaster response protocols, and public health interventions. Despite their importance, comprehensive Origin-Destination (OD) travel matrices remain severely unavailable in most cities of the Global South due to the prohibitive financial and administrative costs of disaggregated household travel surveys.

To solve this, the field increasingly relies on two distinct sources:
1. **Urban Spatial Structure ($X_{urban}$):** Utilizing Geographic Neural Networks to predict flows based on land use, points of interest, and road networks.
2. **Aggregate Mobility Observations ($Y$):** Using coarse, privacy-preserving mobility data (such as distance distributions) published by technology companies.

This dissertation focuses on the fundamental scientific challenge of integrating these sources. Conceptually, the problem is defined as: $M \rightarrow Y = \mathcal{O}_{\psi}(M)$, where $M$ is the underlying mobility, $Y$ is the aggregate observation, and $\mathcal{O}_{\psi}$ is an information-reducing observation operator. Meta's Movement Distribution Maps ($Y_{\text{Meta}}$) serves as the **principal empirical testbed** for this dissertation because it provides a stringent instantiation of this operator—explicitly incorporating single-ping sampling, 4-bin distance categorization, differential-privacy perturbation (Laplace noise), and minimum-count thresholding.

Rather than treating Meta data as absolute ground truth, this dissertation treats it as a mathematically distorted signal, asking what survives the distortion and what non-redundant information it adds to the OD recovery problem.

---

# 2. Literature Baseline & Identified Scientific Limits

Reconstructing spatial interactions from partial data has a rich history in transportation planning. Traditional OD estimation from traffic link counts has long identified the underdetermined nature of the inverse problem. Similarly, modern geographic flow generation leverages deep learning and open spatial features ($X_U$) to generate commuting flows across cities (e.g., DeepGravity).

In spatial interaction modeling, foundational work establishes that estimated distance-decay parameters are systematically influenced by the spatial configuration of opportunity fields (Fotheringham 1981). Furthermore, observed mobility statistics and downstream urban conclusions vary systematically across measurement pipelines (Gallotti et al., 2024).

While these streams of literature are individually mature, they have not adequately addressed the information-theoretic properties of modern privacy-preserved data releases:
1. **Major Gap 1 — Measurement Validity of Aggregate Mobility Observations:** Aggregate mobility products provide accessible but highly compressed representations of human movement, yet the conditions under which mobility information survives sampling, aggregation, privacy perturbation, and filtering sufficiently to constitute a valid quantitative measurement remain insufficiently understood. Meta Movement Distribution provides a well-defined empirical testbed for examining this problem.
2. **Major Gap 2 — Marginal Reconstructive Value for OD Recovery:** A measurement-valid aggregate mobility observation is not necessarily informative for destination-resolved OD reconstruction. It remains unclear how much such an observation reduces OD ambiguity beyond urban contextual information alone, and when its contribution is complementary, redundant, or insufficient.

---

# 3. Research Questions (RQs) & Scope

* **RQ1 (Measurement Validity):** *Under what conditions does a compressed, privacy-preserving aggregate mobility observation remain a valid quantitative representation of its intended mobility property?*
* **RQ2 (Information Value):** *Once established as valid, how much does an aggregate mobility observation improve destination-resolved OD recoverability beyond urban contextual information alone, and under what conditions is this marginal contribution substantial, redundant, or insufficient?*

> **Scope Boundaries (What the thesis does NOT claim):**
> * Establish universal validity for every aggregate mobility dataset.
> * Prove Meta is representative of the entire urban population.
> * Reconstruct individual trajectories from Meta or reverse differential privacy.
> * Claim four distance bins uniquely identify OD.
> * Claim empirical generalization to every city without assessing validity domains.

---

# 4. Paper 1 Formulation — Measurement Validity

* **Research Focus (Gap 1):** Characterize what mobility information survives the Meta observation operator ($T \to \text{1 ping} \to \text{4 bins} \to \text{Laplace DP} \to \text{Threshold}$).
* **Methodology:** 
  - **Distortion A (Information Compression):** Evaluate how much parameter information survives aggressive spatial binning using robust MLE.
  - **Distortion B (Privacy Perturbation):** A Monte Carlo simulation injecting $Laplace(0,1)$ noise into the reference observations (mimicking Meta's exact $\epsilon=1$ DP mechanism) to evaluate signal survivability.
* **Core Metric:** Establishing the **Validity Domain $\mathcal{V}(Y)$**—the specific sample sizes, spatial scales, and noise conditions under which the observation remains a faithful statistical representation of independent mobility benchmarks.
* **Contribution:** A measurement-validity framework for characterizing how much mobility signal survives information-reducing observation processes, empirically evaluated using Meta Movement Distribution as the principal open mobility-data testbed.

---

# 5. Paper 2 Formulation — Marginal Reconstructive Value

* **Research Focus (Gap 2):** Test how much destination-resolved OD information the validated observation adds beyond urban context. Based on the theoretical concept of Conditional Mutual Information $I(T; \tilde{p} \mid X_{\text{urban}})$.
* **Methodology:** A nested evaluation design across 50 US metropolitan areas to explicitly measure incremental value:
  - **Model A (Baseline):** Urban structure only ($\hat{T}_A = f(X_{\text{urban}})$)
  - **Model B (Observation):** Mobility observation only ($\hat{T}_B = f(\tilde{p})$)
  - **Model C (Combined):** Augmented model ($\hat{T}_C = f(X_{\text{urban}}, \tilde{p})$)
* **Core Metric:** Empirical Operationalization of Incremental Information: $\Delta R = R_C - R_A$. The research aims to find how $\Delta R$ fluctuates across urban morphological conditions ($f(U)$).
* **Dimensions of OD Ambiguity:** $\Delta R$ is measured across specific structural dimensions (Distance Profile, Flow Allocation, Topology, Marginal Flow, Scale).
* **Contribution:** A framework for quantifying the marginal reconstructive value of validated aggregate mobility observations beyond urban contextual information, demonstrated using Meta Movement Distribution for OD reconstruction.

---

# 6. Evaluation Paradigm & Kill-Tests

In strict adherence to the Evaluation Principle (*"Matching the Meta input is merely in-sample consistency. It is not evidence of structural OD recovery"*), the framework is evaluated on **unconstrained properties of OD allocation**.

### The 4 Scientific Kill-Tests (Defense Shields)
1. **Valid but redundant?** If $\Delta R \approx 0$, it means $X_{urban}$ already resolves the OD structure. This is a highly valuable scientific finding of information redundancy, not a failure.
2. **Aggregate fit $\neq$ OD recovery:** The augmented model must genuinely reduce *destination-level ambiguity* (improving metrics like CPC or JSD of the full matrix), not just curve-fit distance distributions better.
3. **Model-capacity artefact?** Models A and C must be architecturally capacity-matched to prove $\Delta R$ comes from *new information*, not *more parameters*.
4. **Is $\Delta R$ conditional on urban form?** Identifying the specific spatial regimes where complementarity occurs establishes the final mapping $f(U)$.

Validation follows a **3-Level Indirect Validation Hierarchy** in the Ho Chi Minh City case study:
1. **Level 1 — Model Diagnostics:** Conservation of origin production and destination attraction sums.
2. **Level 2 — Independent Partial Observations:** Auxiliary validation against bus smart card tap counts, arterial corridor volumes, and district commuting censuses.
3. **Level 3 — Falsification Tests:** Shuffled opportunity fields or perturbed distance constraints must demonstrably degrade external alignment metrics.

---

# 7. Preliminary Feasibility Evidence (v15.0+ Audited Evidence Base)

The pre-validation suite was executed across the **50 US Metropolitan Areas Dataset** under a controlled simulation paradigm.

| Scientific Claim | Audited Evidence Status | Phrasing Constraint & Boundary |
| :--- | :--- | :--- |
| **Observation operator degrades quantitative fidelity** | **Strongly Pre-validated** | Parameter magnitude error grows with bin compression. Tests now include Laplace DP Monte Carlo. |
| **Aggregate observation does not identify OD uniquely** | **Demonstrated (Control)** | Q5 ($\text{JSD} = 0$, yet $\text{CPC} = 0.537$). Shows observation can be valid but insufficient/redundant. |
| **Open urban spatial information provides independent recovery value** | **Demonstrated Feasibility** | Clean 50-city LOOCV demonstrates end-to-end reconstruction feasibility ($\text{Mean CPC} = 0.6162$). Model A baseline established. |
| **Multi-seed protocol reliability** | **High Reliability** | Multi-seed $\text{CPC} = 0.5832 \pm 0.0006$, $\text{CV} = 0.0965\%$. |
| **Pop + POI account for ~97.6% of spatial context gain** | **Strong Mechanism Evidence** | T32 Ablation: Pop + POI accounts for ~97.6% of observed full open spatial feature gain. |
| **Transferability follows simple feature similarity** | **NOT SUPPORTED** | T26–T27: $\rho = +0.0955$. Raw structural similarity does not predict transfer. |
| **Incremental value of open urban context is robust to distance misspecification** | **Preliminary robustness evidence** | T34: Incremental CPC gain remains stable across $\pm 60\%$ beta perturbation. |
| **HCMC real-world applicability** | **Feasibility Justified** | US cities results provide sufficient feasibility evidence to justify testing in HCMC. |

---

# 8. Research Timeline & Milestones

```text
2026 Q3: Proposal Defense & Paper 1 Submission (Measurement Validity & Observation Operator)
2026 Q4: Paper 2 Submission (Marginal Reconstructive Value of Privacy-Preserved Constraints)
2027 Q1: HCMC Data Pipeline Integration & Multi-Level Indirect Validation
2027 Q2: Full Dissertation Writing & Pre-defense Review
2027 Q3: Final PhD Dissertation Defense
```

---
*Status: Updated V15.0+ — Master PhD Proposal Document (Information Theory Architecture).*
