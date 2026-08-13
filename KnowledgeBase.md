# Research Knowledge Base (RKB): Master Scientific Operating System

> **Status:** Version 15.0+ — Master Frozen Scientific Operating System (Information Theory & Observation Operator)  
> **Feasibility State:** $\boxed{\text{FEASIBILITY PHASE = FROZEN}}$  
> **Proposal State:** $\boxed{\text{PROPOSAL FORMALIZATION = ACTIVE}}$  

$$\boxed{\text{Aggregate Observation } \neq \text{ Complete Information}}$$

$$\boxed{\text{Valid Measurement } \not\Rightarrow \text{ Useful OD Information}}$$

$$\boxed{\text{Validity Requires Improvement on Unconstrained OD Properties}}$$

> **Core Scientific Master Statement (Frozen):**  
> *"This dissertation investigates not whether aggregate mobility data can simply be fitted to an OD model, but first whether the observed signal remains valid after information-reducing observation processes, and then how much destination-resolved OD information that validated signal contributes beyond independently observed urban context, using Meta Movement Distribution as the principal empirical testbed."*  
> *(Vietnamese: "Luận án này không đơn thuần tìm cách khớp dữ liệu di chuyển gộp vào một mô hình OD, mà trước tiên điều tra xem tín hiệu quan sát có còn hợp lệ sau các quá trình quan sát làm giảm thông tin hay không, và sau đó lượng thông tin OD phân giải theo điểm đến mà tín hiệu đã được xác thực đó đóng góp vượt lên trên bối cảnh đô thị quan sát độc lập là bao nhiêu, sử dụng Phân phối Di chuyển của Meta như môi trường thử nghiệm thực nghiệm chính.")*  

> **Evaluation Principle (Dissertation Directive):**  
> *"Matching the Meta input is merely in-sample consistency. It is not evidence of disaggregated OD recovery. The augmented model must genuinely reduce destination-level ambiguity."*  

> **Terminology Rule (Frozen):**  
> *"Meta Movement Distribution ($Y_{\text{Meta}}$) serves as the principal empirical testbed representing a stringent empirical instantiation of learning mobility from aggregate observations. It explicitly incorporates single-ping sampling, coarse distance binning, differential-privacy perturbation (Laplace noise), and minimum-count filtering."*

---

## 1. Refined Derivation Backbone & System Architecture

```text
OBSERVATION ──► VALIDITY DOMAIN ──► COMPLEMENTARY ──► MARGINAL RECOVERABILITY ──► INDEPENDENT
OPERATOR        (Paper 1)           CONTEXT           (Paper 2)                   VALIDATION
(Meta MDM)      (MC DP Simulation)  (X_urban)         (ΔR Nested Models)          (HCMC Case Study)
```

The Knowledge Base structures scientific knowledge into the **Refined Derivation Backbone**, **Statistical Audit Results**, **Paper Scope**, and the **Master Scoped Claim Matrix**.

This architecture is grounded in foundational and modern spatial interaction literature:
* **Wilson (1971):** Establishes a family of spatial-interaction models whose formulations differ according to imposed system constraints.
* **Fotheringham (1981):** Provides empirical evidence that estimated distance-decay parameters depend on spatial structure.
* **Aoki et al. (2022):** Demonstrate that OD flow observations can reveal latent urban spatial structures.
* **DeepGravity (2021):** Demonstrates that geographic context and distance can be jointly incorporated in a supervised neural flow-generation model.
* **OD estimation from counts (incl. IIASA review):** Reports that OD reconstruction from partial traffic observations is underdetermined and requires additional prior information.

---

## 2. Statistical Significance & Reliability Audit Summary

* **T20 clean split gain:** $\Delta\text{CPC} = +0.0485$.
* **Dedicated paired reliability micro-audit:** Mean paired gain $+0.0417$ with $95\%\text{ bootstrap CI } [0.0308, 0.0527]$; Paired $t$-test $t = 6.9316, p < 0.001$; Wilcoxon $W = 0.0, p < 0.002$.
* **Clean LOOCV Performance (T21):** Leave-One-City-Out Cross-Validation on all 50 US metropolitan areas under completely clean zero-target-OD 3-bin beta MLE yields Mean CPC $= 0.6162$ (Median $= 0.6249$, $95\%\text{ Bootstrap CI } [0.5997, 0.6317]$).
* **Multi-Seed Protocol Reliability:** Multi-seed evaluation across 5 random seeds yields Mean $\text{CPC} = 0.5832 \pm 0.0006$ with Coefficient of Variation $\text{CV} = 0.0965\% (< 0.1\%)$, confirming high protocol stability.
* **Complexity-Controlled Failure Regression:** Multivariable regression $\text{CPC} = 0.9021 - 0.0611 \cdot \log(N) - 0.0034 \cdot \log(\text{Density})$ confirms spatial system scale $\log(N)$ maintains an independent negative difficulty association ($\beta = -0.0611$) after density control.

---

## 3. Paper Scope & Core Research Questions

### 3.1 Dimensions of OD Ambiguity (Empirical Metrics for $\Delta R$)

> **Operational Definition.** While the theoretical core of Paper 2 is Conditional Mutual Information $I(T; \tilde{p} \mid X_{\text{urban}})$, its empirical operationalization relies on measuring the reduction in specific **Dimensions of OD Ambiguity** ($U_m$):

$$U_{\text{ambiguity}}(T \mid Y_B) = \bigl( U_{\text{dist}},\ U_{\text{alloc}},\ U_{\text{topo}},\ U_{\text{margin}},\ U_{\text{scale}} \bigr)$$

| Dimension | Name | What it measures | Operational metric | Grounding evidence |
| :--- | :--- | :--- | :--- | :--- |
| $U_{\text{dist}}$ | Distance-profile ambiguity | How precisely does $Y_B$ constrain $\boldsymbol{\theta}$? | $\|\hat{\boldsymbol{\theta}}_{Y_B} - \hat{\boldsymbol{\theta}}_{\text{ref}}\| / \|\hat{\boldsymbol{\theta}}_{\text{ref}}\|$ | T29: $0.77\% \to 44.4\%$ |
| $U_{\text{alloc}}$ | Flow-allocation ambiguity | Pairwise OD flow accuracy | $1 - \text{CPC}(T_{\text{recon}}, T_{\text{ref}})$ | Q6b: CPC = 0.5463 baseline |
| $U_{\text{topo}}$ | Topological ambiguity | Can different ODs produce same $Y_B$? | Non-uniqueness: $\text{JSD} = 0$, $\text{CPC} \ll 1$ | Q5: CPC = 0.537 |
| $U_{\text{margin}}$ | Marginal-flow ambiguity | Zone-level outflow/inflow accuracy | $\text{SRMSE}(O_i^{\text{recon}}, O_i^{\text{ref}})$ | T24, QT15 |
| $U_{\text{scale}}$ | Scale-dependent ambiguity | Does ambiguity grow with system size? | Regression of $U_{\text{alloc}}$ on $\log(N)$ | T33: $\beta = -0.0611$ |

---

### 3.2 2 Major Gaps & 2 Aligned Research Questions

* **Major Gap 1 — Measurement validity under privacy-preserving aggregation:** Existing applications use Meta Movement Distribution as an aggregate mobility indicator, but it remains unclear how much mobility-distance information survives the complete observation process—single-ping sampling, coarse distance binning, differential-privacy perturbation, and minimum-count filtering—and under what conditions the released distribution remains consistent with independent mobility observations.
* **Major Gap 2 — Conditional Information Value for OD Recovery:** A mobility observation can be valid yet informationally redundant. It remains unknown whether a validated privacy-preserved distance distribution provides destination-resolved OD information beyond that already contained in urban structure, and under which urban configurations this marginal value is substantial, negligible, or absent.

---

* **RQ1 (Measurement Validity):** *Under what conditions does Meta's privacy-preserving, distance-binned distribution remain a valid measurement of mobility-distance behaviour?*
* **RQ2 (Information Value):** *Within the validity domain established in Paper 1, how much non-redundant OD information does the privacy-preserved, distance-binned mobility constraint contribute beyond urban structure alone, and under which urban configurations does this marginal information materially improve OD recoverability?*

> **Structural Rule:** The dependency is asymmetric: Paper 1 establishes the **Validity Domain $\mathcal{V}(Y)$**; Paper 2 takes observations where $Y \in \mathcal{V}$ and quantifies their **Marginal Reconstructive Value $\Delta R(Y \mid X)$**.

---

### 3.3 Reframed 50-City Stage & Paper Stream

```text
                                  50 US METROPOLITAN AREAS (50 CITIES)
                                                   │
                                    Paper 1: Is the observation valid?
                                     T ──► O_ψ ──► Validity Domain V(Y)
                                                   │
                                                   ▼
                                    Paper 2: Is it informative for OD?
                                     ΔR = R(T | X_urban, Ỹ) - R(T | X_urban)
```

* **Paper 1 — Measurement Validity & Observation Operator**
  - *Objective:* Characterize what mobility information survives the Meta observation operator ($T \to \text{1 ping} \to \text{4 bins} \to \text{Laplace DP} \to \text{Threshold}$).
  - *Core Question:* *"Under what conditions does the compressed, privacy-preserving observation remain a valid measurement constraint?"*
  - *Output:* The Validity Domain $\mathcal{V}(Y)$.
* **Paper 2 — Marginal Reconstructive Value**
  - *Objective:* Test how much destination-resolved OD information the validated observation adds beyond urban context.
  - *Core Metric:* $\Delta R = R_C - R_A$ via Nested Models (A: Urban only, B: Obs only, C: Combined).
  - *Key Evidence:* Q6b, T20, T21, T22, T32, T34. Focuses on identifying the urban conditions $f(U)$ where complementarity or redundancy occurs.
  - *Output:* Conditional Information Value and spatial regimes.
* **Ho Chi Minh City Applied Case Study**
  - *Research Question:* *Can the resulting reconstructed OD be empirically defended through independent partial manifestations when complete OD ground truth is unavailable?*
  - *Technical Scope:* Deploys the zero-target-OD reconstruction pipeline under extreme data scarcity.

---

## 4. Master Scoped Dissertation Claim Status Matrix (v15.0+)

| Scientific Claim | Audited Evidence Status | Phrasing Constraint & Boundary |
| :--- | :--- | :--- |
| **Observation operator degrades quantitative fidelity** | **Strongly Pre-validated** | Parameter magnitude error grows with bin compression. Must be tested alongside Laplace DP. |
| **Aggregate observation does not identify OD uniquely** | **Demonstrated (Control)** | Empirically supported by Q5 ($\text{JSD} = 0.0000$, yet $\text{CPC} = 0.5373$). It can be *valid* but *redundant/insufficient*. |
| **Open urban spatial information provides independent recovery value** | **Demonstrated Feasibility** | Clean 50-city LOOCV demonstrates end-to-end reconstruction feasibility ($\text{Mean CPC} = 0.6162$). |
| **Multi-seed protocol reliability** | **High Reliability** | Multi-seed $\text{CPC} = 0.5832 \pm 0.0006$, $\text{CV} = 0.0965\%$. |
| **Pop + POI account for ~97.6% of spatial context gain** | **Strong Mechanism Evidence** | T32 Ablation: Pop + POI accounts for ~97.6% of observed full open spatial feature gain. |
| **Transferability follows simple feature similarity** | **NOT SUPPORTED** | T26–T27: $\rho = +0.0955$. Raw structural similarity does not predict transfer. |
| **Incremental value of open urban context is robust to distance misspecification** | **Preliminary robustness evidence** | T34: Incremental CPC gain remains stable across $\pm 60\%$ beta perturbation. |
| **HCMC real-world applicability** | **Feasibility Justified** | US cities results provide sufficient feasibility evidence to justify testing in HCMC. |

---

## 5. Scope Boundaries (What the thesis does NOT claim)
> [!WARNING]
> * Establish universal validity for every aggregate mobility dataset.
> * Prove Meta is representative of the entire urban population.
> * Reconstruct individual trajectories from Meta.
> * Remove or reverse differential privacy.
> * Claim four distance bins uniquely identify OD.
> * Build a universal theory of urban morphology.
> * Claim empirical generalization to every city and every mobility product.

---
*Status: Updated V15.0+ — Master Scientific Operating System (Frozen).*
