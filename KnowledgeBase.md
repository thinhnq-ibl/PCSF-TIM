# Research Knowledge Base (RKB): Master Scientific Operating System

> **Status:** Version 13.0+ — Master Frozen Scientific Operating System (Citation Verification Active)  
> **Feasibility State:** $\boxed{\text{FEASIBILITY PHASE = FROZEN}}$  
> **Proposal State:** $\boxed{\text{PROPOSAL FORMALIZATION = ACTIVE}}$  

$$\boxed{\text{Aggregate Observation } \neq \text{ Complete Information}}$$

$$\boxed{\text{Input Consistency } \neq \text{ Reconstruction Validity}}$$

$$\boxed{\text{Validity Requires Improvement on Unconstrained OD Properties}}$$

> **Core Scientific Master Statement (Frozen):**  
> *"This dissertation investigates the sufficiency of observable information for reconstructing urban spatial interaction under mobility data scarcity. It examines what information is retained or lost under aggregate mobility observation, how observation design affects recoverability, and how complementary open urban information improves OD reconstruction when the mobility observation alone is insufficient."*  
> *(Vietnamese: "Luận án này nghiên cứu tính đầy đủ của thông tin quan sát được để khôi phục tương tác không gian đô thị trong điều kiện khan hiếm dữ liệu di chuyển. Luận án phân tích thông tin nào được giữ lại hoặc mất đi dưới các quan sát di chuyển gộp, thiết kế quan sát ảnh hưởng thế nào đến khả năng khôi phục thông tin, và thông tin không gian đô thị mở bổ trợ cải thiện việc khôi phục OD ra sao khi bản thân quan sát di chuyển không đủ đơn độc.")*  

> **Evaluation Principle (Dissertation Directive):**  
> *"Matching the Meta input is merely in-sample consistency. It is not evidence of disaggregated OD recovery."*  

> **Condensed Core Narrative:**  
> *"Aggregate mobility observations are informative but non-identifying at the OD level. The remaining scientific problem is determining how complementary open spatial information reduces this ambiguity and improves OD recoverability."*

---

## 1. Refined Derivation Backbone & System Architecture

```text
OBSERVATION ──► RECOVERABLE ──► OBSERVATION ──► UNDERDETERMINATION ──► COMPLEMENTARY ──► OD RECONSTRUCTION ──► INDEPENDENT
                INFORMATION     SENSITIVITY                              CONTEXT                                VALIDATION
  (Meta MDM)     (Paper 1)       (T29-T30)       (TLD -> OD Non-ID)      (Paper 2)          (C3 Pipeline)        (HCMC Case Study)
```

The Knowledge Base structures scientific knowledge into the **Refined Derivation Backbone**, **Statistical Audit Results**, **Paper Scope**, and the **Master Scoped Claim Matrix**.

This architecture is grounded in foundational and modern spatial interaction literature:
* **Wilson (1971):** Establishes a family of spatial-interaction models whose formulations differ according to imposed system constraints, providing a classical foundation for treating observed interaction patterns as constraint-dependent rather than as a single universal gravity law.
* **Fotheringham (1981):** Provides empirical evidence that estimated distance-decay parameters depend on spatial structure, cautioning against interpreting them as context-free measures of travel behaviour.
* **Aoki et al. (2022):** Demonstrate that OD flow observations can reveal latent urban spatial structures, illustrating that mobility observations contain information about spatial organization.
* **DeepGravity (2021):** Demonstrates that geographic context and distance can be jointly incorporated in a supervised neural flow-generation model, and that rich geographic features improve mobility-flow prediction.
* **OD estimation from counts (incl. IIASA review):** Reports that OD reconstruction from partial traffic observations is underdetermined and requires additional prior information/regularization; page-level citation verification remains part of the active literature audit.

---

## 2. Statistical Significance & Reliability Audit Summary

* **T20 clean split gain:** $\Delta\text{CPC} = +0.0485$.
* **Dedicated paired reliability micro-audit:** Mean paired gain $+0.0417$ with $95\%\text{ bootstrap CI } [0.0308, 0.0527]$; Paired $t$-test $t = 6.9316, p < 0.001$; Wilcoxon $W = 0.0, p < 0.002$.
* **Clean LOOCV Performance (T21):** Leave-One-City-Out Cross-Validation on all 50 US metropolitan areas under completely clean zero-target-OD 3-bin beta MLE yields Mean CPC $= 0.6162$ (Median $= 0.6249$, $95\%\text{ Bootstrap CI } [0.5997, 0.6317]$).
* **Multi-Seed Protocol Reliability:** Multi-seed evaluation across 5 random seeds yields Mean $\text{CPC} = 0.5832 \pm 0.0006$ with Coefficient of Variation $\text{CV} = 0.0965\% (< 0.1\%)$, confirming high protocol stability.
* **Complexity-Controlled Failure Regression:** Multivariable regression $\text{CPC} = 0.9021 - 0.0611 \cdot \log(N) - 0.0034 \cdot \log(\text{Density})$ confirms spatial system scale $\log(N)$ maintains an independent negative difficulty association ($\beta = -0.0611$) after density control.

---

## 3. Paper Scope & Core Research Questions

### 3.1 Core Research Questions (RQs)
* **Gap 1 — Observation Sufficiency:** *What OD-relevant information survives highly compressed aggregate mobility observations?*
* **Gap 2 — Determinants of Observation Sufficiency:** *How do spatial support, bin resolution, bin geometry, and model complexity affect recoverability?*
* **Gap 3 — Complementary Reconstruction Value:** *How much marginal reconstruction improvement is obtained from adding open urban spatial information under the same mobility observation constraints?*
* **RQ4 — Empirical Defensibility:** *How can reconstructed OD patterns be empirically evaluated when complete target-city OD ground truth is unavailable?*

---

### 3.2 Paper Stream & Technical Scope
* **Paper 1 — Information Retention in Aggregate Mobility Observations**
  - *Research Question:* *How does the design of an aggregate mobility observation determine what spatial-interaction information remains recoverable?*
  - *Technical Scope:* Evaluates the observation transformation ($OD \to \text{Observation} \to \text{Information}$) across the axes of $\text{spatial support} \times \text{distance resolution} \times \text{bin geometry} \times \text{model complexity}$.
  - *Decay Probes:* Exponential primary probe (stable, interpretable), Power-law robustness check, and Tanner complexity stress test.
  - *Key Evidence:* T28, T29, T30, and T35.
* **Paper 2 — Complementary Information for OD Reconstruction**
  - *Research Question:* *How much complementary open urban information is needed to improve OD recoverability when aggregate mobility observations are insufficient?*
  - *Sub-Question:* *To what extent does open urban spatial context preserve incremental reconstruction value when distance-interaction information is uncertain?*
  - *Technical Scope:* Develops a zero-target-OD reconstruction methodology mapping open features ($X_U$) to complementary constraints, quantifying the incremental value along the information ladder ($\text{TLD} \to +P \to +\text{POI} \to \text{Full } X_U$).
  - *Key Evidence:* T20, T21, T22, T32, and T34.
* **Ho Chi Minh City Applied Case Study**
  - *Research Question:* *Can the resulting latent OD be empirically defended through independent partial manifestations when complete OD ground truth is unavailable?*
  - *Technical Scope:* Deploys the reconstruction pipeline under extreme data scarcity and evaluates OD patterns using unconstrained properties and available independent sources such as bus smart-card/tap data, traffic counts, and commuting statistics, subject to data availability.
  - *Supporting preliminary evidence:* T24, subject to clean no-oracle replication.

---

## 4. Master Scoped Dissertation Claim Status Matrix (v13.0+)

| Scientific Claim | Audited Evidence Status | Phrasing Constraint & Boundary |
| :--- | :--- | :--- |
| **Aggregate TLD retains distance-related interaction signal** | **Strongly Pre-validated** | 3-bin preserves non-trivial distance-related ordering and trend information. |
| **Compression reduces quantitative fidelity** | **Strongly Pre-validated** | Parameter magnitude error grows $0.77\% \to 44.42\% \to 100\%$ collapse at 1-bin. |
| **Bin geometry materially affects retained signal** | **Strongly Pre-validated** | T30: Shift $-20\% \to +20\%$ alters parameter error ($55.5\% \to 33.3\%$). |
| **Aggregate TLD does not identify OD uniquely** | **Demonstrated (Control)** | Empirically supported by Q5 ($\text{JSD} = 0.0000$, yet $\text{CPC} = 0.5373$). |
| **Open urban spatial information improves recovery** | **Demonstrated Feasibility** | Open spatial information yields positive reconstruction gains across the tested protocols; the dedicated paired reliability audit estimates a mean gain of $+0.0417$ with $95\%\text{ bootstrap CI } [0.0308, 0.0527]$. T20 clean split reports $\Delta\text{CPC} = +0.0485$. |
| **Multi-seed protocol reliability** | **High Reliability** | Multi-seed $\text{CPC} = 0.5832 \pm 0.0006$, $\text{CV} = 0.0965\%$. |
| **Pop + POI account for ~97.6% of spatial context gain** | **Strong Mechanism Evidence** | T32 Ablation: Pop + POI accounts for ~97.6% of observed full open spatial feature gain ($+0.0499$). |
| **Scale log(N) increases difficulty** | **Regression Associated** | $\text{CPC} \sim \log(N)$ yields $\beta = -0.0611$ after controlling for density and sparsity. |
| **Transferability follows simple feature similarity** | **NOT SUPPORTED** | T26–T27: $\rho = +0.0955$ ($p = 0.1681$). Raw structural similarity does not predict transfer. |
| **Incremental value of open urban spatial information is robust to distance-parameter misspecification** | **Preliminary robustness evidence** | T34: Incremental CPC gain remains stable ($+0.0411$ to $+0.0530$) across $\pm 60\%$ beta perturbation. |
| **Compression-induced parameter degradation is observed across alternative deterrence specifications** | **Preliminary functional-form robustness evidence** | Chicago case study only; Tanner results suggest greater information demand under higher parameterization. |
| **HCMC real-world applicability** | **Feasibility Justified** | US cities results provide sufficient feasibility evidence to justify testing in HCMC. |

---
*Status: Updated V13.0+ — Master Scientific Operating System (Frozen & Formalization Active).*
