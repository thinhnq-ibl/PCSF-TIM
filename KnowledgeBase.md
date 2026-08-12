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

> **Terminology Rule (Frozen):**  
> *"Meta Movement Distribution is an aggregate movement observation describing the distribution or range of daily movement relative to individuals' residential areas. It is not a directly observed trip-length distribution derived from an OD matrix. 'TLD' is reserved for distance distributions derived or simulated from OD flows, including OD-derived TLD and Meta-like aggregate movement observations generated from OD."*

---

## 1. Refined Derivation Backbone & System Architecture

```text
OBSERVATION ──► RECOVERABLE ──► OBSERVATION ──► UNDERDETERMINATION ──► COMPLEMENTARY ──► OD RECONSTRUCTION ──► INDEPENDENT
                INFORMATION     SENSITIVITY                              CONTEXT                                VALIDATION
  (Meta MDM Obs.) (Paper 1)      (T29-T30)       (Agg. Obs. -> OD Non-ID) (Paper 2)         (C3 Pipeline)        (HCMC Case Study)
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

### 3.1 3 Core Research Gaps & 3 Aligned RQs

* **Gap 1 — Information Retained / Lost:** Existing studies do not sufficiently characterize what reconstruction-relevant information is retained or lost when spatial interaction is observed only through aggregate mobility measurements.
* **Gap 2 — Observation Design & Resolution:** The effect of aggregate observation design and resolution on OD recoverability remains insufficiently understood, particularly beyond properties directly constrained by the observation.
* **Gap 3 — Complementary Urban Information:** When aggregate mobility observations are insufficient, it remains unclear how much complementary independently observable urban information can reduce the remaining reconstruction uncertainty.

---

* **RQ1 (Information Characterization):** *What reconstruction-relevant information is retained or lost under aggregate mobility observation?*
* **RQ2 (Observation Design):** *How does aggregate mobility observation design affect the recoverability of urban spatial interaction?*
* **RQ3 (Complementary Information Integration):** *To what extent can complementary open urban information improve OD reconstruction when aggregate mobility observation alone is insufficient?*
* **RQ4 (Empirical Defensibility):** *How can reconstructed OD patterns be empirically evaluated when complete target-city OD ground truth is unavailable?*

> **Structural Rule:** The progression $\text{RQ1} \to \text{RQ2} \to \text{RQ3}$ strictly operates on **information sufficiency for reconstruction** without assuming $S \perp B$ or requiring $S$ and $B$ to be independently observable.

---

### 3.2 Reframed 50-City Stage & Paper Stream

```text
                                  50 US METROPOLITAN AREAS (50 CITIES)
                                                   │
         ┌─────────────────────────────────────────┴─────────────────────────────────────────┐
         ▼                                                                                   ▼
PAPER 1: AGGREGATE OBSERVATION CHARACTERIZATION                    PAPER 2: COMPLEMENTARY URBAN INFORMATION INTEGRATION
Measure R(c, r, p):                                                Evaluate OD Reconstruction Performance:
  • c = City (50 MSAs)                                               • Baseline: Aggregate Mobility Observation
  • r = Resolution / Design (Meta 3-bin vs 20-bin vs OD)              • Proposed: Aggregate Obs + Open Urban Info (POIs/NLCD)
  • p = Evaluation Property (CPC, Q50, Q90, Distance Err, β)          • Benchmark: Aggregate Obs + Oracle Destination Info
Core Question: What is recoverable & what remains unconstrained?   Core Metric: RecoveryRatio_c = Gain_c(open) / Gain_c(oracle)
```

* **Paper 1 — Aggregate Observation Information Characterization**
  - *Objective:* Characterize what reconstruction-relevant information is retained or lost under aggregate mobility observation across 50 US metropolitan areas.
  - *Technical Scope:* Evaluates $R(c, r, p)$ across city $c$, observation design $r$, and evaluation property $p$ (distance-distribution error, Q50/Q90, CPC, network flow properties, and inferred deterrence parameter $\beta$ as a *diagnostic reconstruction property*).
  - *Core Question:* *"What is recoverable from this aggregate observation, and what remains unconstrained?"*
  - *Key Evidence:* Q1–Q4, T28, T29, T30, and T35.
* **Paper 2 — Complementary Open Information Integration**
  - *Research Question:* *When aggregate mobility observation is insufficient, how much can complementary open urban information improve OD reconstruction?*
  - *Technical Scope:* Evaluates the experimental triad (`Aggregate Obs` vs. `Aggregate Obs + Open Urban Info` vs. `Aggregate Obs + Oracle Destination Info`) across 50 cities.
  - *Core Metric:* $\text{RecoveryRatio}_c = \frac{\text{Gain}_c^{\text{open}}}{\text{Gain}_c^{\text{oracle}}} = \frac{\text{CPC}_c(\text{Agg}+\text{Open}) - \text{CPC}_c(\text{Agg})}{\text{CPC}_c(\text{Agg}+\text{Oracle}) - \text{CPC}_c(\text{Agg})}$.
  - *Key Evidence:* Q6b, T20, T21, T22, T32, and T34.
* **Ho Chi Minh City Applied Case Study**
  - *Research Question:* *Can the resulting latent OD be empirically defended through independent partial manifestations when complete OD ground truth is unavailable?*
  - *Technical Scope:* Deploys the zero-target-OD reconstruction pipeline under extreme data scarcity and evaluates OD patterns using unconstrained properties and available independent sources (bus tap counts, arterial traffic volumes, commuting censuses).

---

## 4. Pilot Diagnostic Battery (Q0–Q6b) & Reinterpretation Matrix

| Diagnostic Test | Measured Result | Aligned Narrative Interpretation |
| :--- | :--- | :--- |
| **Q1: TLD Information Retention** | $\Delta V_{\text{Q90}} > 0, \Delta V_{\text{CPC}} > 0$ <br> $NLL_{\text{shuffle}} < NLL_{\text{true}} < NLL_{\text{noTLD}}$ | **Coarse aggregate distance observation retains measurable information relevant to OD reconstruction**, though information recovered varies across properties ($\text{Information Sufficiency is Property-Dependent}$). |
| **Q2: Compression Discrepancy** | $\hat{\beta}_3 = 0.2499$ vs. OD ref ($10.64\%$ diff) | **The behavioural representation induced by coarse observation differs systematically from that obtained under fuller OD information.** (Coarsening observation changes inferred distance deterrence representation; $\beta$ is a diagnostic property, not "true behaviour"). |
| **Q3: Identification Stability** | Profile LR $\in [0.2498, 0.2500]$ | **The chosen distance-deterrence representation is statistically identifiable under this observation/model configuration.** (Shows precise optimum given assumed gravity model; does NOT prove "true travel behaviour identified"). |
| **Q5 / Q6a: Cross-City Diagnostic** | $5/6$ $\text{OWN\_CITY\_BETTER}$, $1/6$ $\text{CROSS\_CITY\_BETTER}$ | **Cross-city reuse of inferred mobility representations cannot be assumed to be universally valid.** (Acts as caution; parameterization from one city lacks uniform cross-city performance). |
| **Q6b: Complementary Information Bridge** | $\text{TLD} + A_j^{\text{uniform}} \to \text{TLD} + A_j^{\text{oracle}}$ ($\Delta \text{CPC} = +0.0636$) | **The aggregate mobility observation does not contain all information useful for OD reconstruction; complementary destination-side information has incremental value.** (Serves as upper-bound feasibility evidence for Paper 2). |

---

## 5. Master Scoped Dissertation Claim Status Matrix (v14.0+)

| Scientific Claim | Audited Evidence Status | Phrasing Constraint & Boundary |
| :--- | :--- | :--- |
| **OD-derived TLD retains distance-related interaction signal** | **Strongly Pre-validated** | 3-bin preserves non-trivial distance-related ordering and trend information under controlled OD-derived aggregation. |
| **Compression reduces quantitative fidelity** | **Strongly Pre-validated** | Parameter magnitude error grows $0.77\% \to 44.42\% \to 100\%$ collapse at 1-bin. |
| **Bin geometry materially affects retained signal** | **Strongly Pre-validated** | T30: Shift $-20\% \to +20\%$ alters parameter error ($55.5\% \to 33.3\%$). |
| **OD-derived TLD does not identify OD uniquely** | **Demonstrated (Control)** | Empirically supported by Q5 ($\text{JSD} = 0.0000$, yet $\text{CPC} = 0.5373$). |
| **Open urban spatial information improves recovery** | **Demonstrated Feasibility** | Open spatial information yields positive reconstruction gains across the tested protocols; the dedicated paired reliability audit estimates a mean gain of $+0.0417$ with $95\%\text{ bootstrap CI } [0.0308, 0.0527]$. T20 clean split reports $\Delta\text{CPC} = +0.0485$. |
| **Multi-seed protocol reliability** | **High Reliability** | Multi-seed $\text{CPC} = 0.5832 \pm 0.0006$, $\text{CV} = 0.0965\%$. |
| **Pop + POI account for ~97.6% of spatial context gain** | **Strong Mechanism Evidence** | T32 Ablation: Pop + POI accounts for ~97.6% of observed full open spatial feature gain ($+0.0499$). |
| **Scale log(N) increases difficulty** | **Regression Associated** | $\text{CPC} \sim \log(N)$ yields $\beta = -0.0611$ after controlling for density and sparsity. |
| **Transferability follows simple feature similarity** | **NOT SUPPORTED** | T26–T27: $\rho = +0.0955$ ($p = 0.1681$). Raw structural similarity does not predict transfer. |
| **Incremental value of open urban spatial information is robust to distance-parameter misspecification** | **Preliminary robustness evidence** | T34: Incremental CPC gain remains stable ($+0.0411$ to $+0.0530$) across $\pm 60\%$ beta perturbation. |
| **Compression-induced parameter degradation is observed across alternative deterrence specifications** | **Preliminary functional-form robustness evidence** | Chicago case study only; Tanner results suggest greater information demand under higher parameterization. |
| **HCMC real-world applicability** | **Feasibility Justified** | US cities results provide sufficient feasibility evidence to justify testing in HCMC. |

---
*Status: Updated V14.0+ — Master Scientific Operating System (Frozen & Formalization Active).*

