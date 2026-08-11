# PhD Dissertation Proposal: Learning Human Mobility from Aggregate Observations

## Title
**Learning Human Mobility from Aggregate Observations: Identification of Spatial Interaction Behaviour and Transferable Urban Structure for OD Matrix Reconstruction**

### Subtitle
*Towards Mechanism-based Human Mobility Science through Observability, Identifiability, and Empirical Defensibility*

---

> **Master Opening Statement (Frozen Key Sentence):**  
> **"Human mobility can be reconstructed by independently inferring its structural and behavioural components from the maximum publicly available information."**  
> *(Phiên bản tiếng Việt: "Có thể phục hồi tương tác di chuyển đô thị bằng cách suy luận độc lập thành phần cấu trúc và thành phần hành vi từ lượng thông tin công khai tối đa.")*

> **Evaluation Principle (Dissertation Evaluation Directive):**  
> **"Matching the Meta input is merely in-sample consistency. It is not evidence of structural OD recovery."**  
> *(Phiên bản tiếng Việt: "Trùng khớp với dữ liệu đầu vào Meta chỉ là tính nhất quán nội mẫu. Đó không phải là bằng chứng của việc phục hồi cấu trúc OD.")*

---

# 1. Executive Summary & Scientific Core

## 1.1 The 3-Stage Scientific Backbone
This dissertation establishes a mechanism-based framework for learning human mobility under extreme data scarcity. Rather than treating mobility as a black-box machine learning prediction problem or arguing over model benchmarks, this research addresses three sequential scientific questions: **Observability $\longrightarrow$ Identifiability $\longrightarrow$ Empirical Defensibility**.

```text
       OBSERVABILITY                     IDENTIFIABILITY                 EMPIRICAL DEFENSIBILITY
         (Paper 1)                          (Paper 2)                       (HCMC Case Study)
┌──────────────────────────┐      ┌──────────────────────────┐      ┌──────────────────────────┐
│  Is the mobility signal  │      │ Can urban structure      │      │ Is the reconstructed OD  │
│  scientifically          │ ──►  │ reduce ambiguity         │ ──►  │ empirically defensible   │
│  observable from Meta    │      │ sufficiently for OD      │      │ on UNCONSTRAINED         │
│  compressed TLD?         │      │ identification?          │      │ properties?              │
└──────────────────────────┘      └──────────────────────────┘      └──────────────────────────┘
```

> **Condensed Thesis Core Narrative:**  
> **"Aggregate mobility appears informative but non-identifying."**  
> **"The remaining scientific problem is determining what independent structural information is sufficient to resolve that ambiguity."**

---

## 1.2 The Four Logical Pillars

1. **Slide 1 — Baseline (Locked Art):**  
   Calibrating distance decay functions from aggregate travel-distance distributions (TLDs) is a solved baseline in spatial interaction modelling. TLD calibration alone is not the primary scientific research gap.

2. **Slide 2 — Observability / Paper 1:**  
   The primary scientific question for aggregate mobility products (such as Meta's Movement Distribution Maps \citep{MetaMovementDistributionMaps}) is **which information survives spatial aggregation and bin compression**, and under which spatial-support conditions that signal remains statistically defensible.

3. **Slide 3 — Identifiability / Paper 2:**  
   Even when aggregate observation signals are reliable, aggregate constraints are underdetermined (non-identifiable)—infinitely many distinct OD matrices produce the exact same TLD ($TLD_{\text{3bin}} \to \hat{\boldsymbol{\theta}}$ stable, but $TLD_{\text{3bin}} \not\to \text{OD}$; Q5 empirical demonstration: $\text{JSD} = 0.0000$, yet $\text{CPC} = 0.5373$). **What independent structural information is sufficient to convert an observable but non-identifying mobility signal into defensible OD allocation?** Here, the Structure–Behaviour Decomposition Principle directly serves the **identification problem** by injecting structural opportunity fields ($R_S$) to constrain the solution space.

4. **Slide 4 — Empirical Defensibility / HCMC Case Study:**  
   Reconstruction is scientifically valid only if it correctly predicts **unconstrained properties of OD allocation**—spatial allocation characteristics that were *not* directly constrained by the input data—and explains independent urban patterns in Ho Chi Minh City under missing complete ground truth.

---

## 1.3 Pre-HCMC Simulation Paradigm & Test A Audit

A critical strategic insight of this dissertation is that **lack of initial target-city (HCMC) disaggregated OD data is NOT a research blocker**. Before deploying to HCMC, the framework is validated through a controlled experimental paradigm using multi-city datasets with complete OD ground truth (50 US Metropolitan Areas):

```text
Full OD Ground Truth ──► Artificial Aggregation (Meta 3-bin) ──► Hide Target OD ──► Reconstruct ──► Reveal OD (Evaluate)
```

> **Audit Test A Result (Zero Oracle Leakage):**  
> Evaluated on 10 unseen test cities, **Transferred Urban Structure ($R_S$, $\text{CPC} = 0.6462$)** learned strictly from open spatial features (without target OD marginals) reliably outperforms both **TLD-Only Baseline ($\text{CPC} = 0.5852$)** and **Shuffled Negative Control ($\text{CPC} = 0.5331$)**, while **Oracle OD Marginals ($\text{CPC} = 0.7159$)** serve strictly as the upper-bound ceiling.

---

# 2. Central Scientific Proposition & Refined Research Questions

> **Central Scientific Proposition:**  
> *"Although Spatial Interaction emerges from the interaction between Urban Structure Representation and Travel Behaviour Representation, treating these representations as analytically distinguishable enables different scientific questions to be formulated, different learning objectives to be defined, and different learning strategies to be developed. The Structure–Behaviour Decomposition Principle serves directly to resolve the identification problem by constraining underdetermined OD solution spaces."*

## Refined Research Questions (RQs)

```text
   RQ1: Observability ──► RQ2: Identifiability & ──► RQ3: Structural Transfer ──► RQ4: Empirical
 (Aggregate Mobility)      Unconstrained Properties     (Ambiguity Reduction)      Defensibility (HCMC)
```

* **RQ1 (Observability — Paper 1):**  
  *Which information survives aggregation in aggregate mobility data (such as Meta MDM), and under which spatial-support conditions is it statistically defensible?*  
  *(Quantifies information preservation and parameter stability $\hat{\boldsymbol{\theta}}$ across 20-bin OD-derived benchmark distributions and 3-bin Meta MDM open distributions).*

* **RQ2 (Identifiability & Unconstrained Properties — Paper 2):**  
  *Can support-aware aggregate mobility constraints, combined with a transferable representation of urban spatial structure, recover unconstrained properties of OD allocation without target-city OD calibration?*  
  *(Evaluates whether structural potential fields ($R_S$) provide sufficient information to narrow the underdetermined solution space and recover unobserved spatial allocation properties).*

* **RQ3 (Structural Transferability & Ambiguity Reduction — Paper 2):**  
  *To what extent can an Urban Structure Representation ($R_S$) learned from open spatial data reduce OD allocation ambiguity across heterogeneous urban domains?*  
  *(Tests the zero-shot cross-city transferability hypothesis $H_2$ under source-target structural similarity conditions).*

* **RQ4 (Empirical Defensibility — HCMC Case Study):**  
  *How can reconstructed latent OD matrices for Ho Chi Minh City be empirically defended using unconstrained spatial allocation properties and independent multi-level urban constraints under missing complete ground truth?*  
  *(Validates reconstructed flows against independent urban indicators and auxiliary mobility constraints).*

---

# 3. Paper Architecture & 3-Round Quick-Test Suite

```text
                        DISSERTATION FRAMEWORK
                                  │
         ┌────────────────────────┴────────────────────────┐
         ▼                                                 ▼
      PAPER 1                                           PAPER 2
   Observability Stream                           Identifiability Stream
 (Which info survives aggregation?)           (What structure resolves ambiguity?)
D_TLD ──► MLE ──► R_B(θ)                           X_S ──► GeoAI/GNN ──► R_S ──► (O_i, A_j)
         │                                                 │
         └────────────────────────┬────────────────────────┘
                                  ▼
                        HO CHI MINH CITY CASE STUDY
                        Empirical Defensibility Stream
               (Evaluating Unconstrained OD Allocation Properties)
```

## 3.1 Paper 1 Mission: Observability Stream
* **Core Task:** Parametric statistical inference of collective distance sensitivity ($\boldsymbol{\theta} = (\alpha, \beta)$ under Tanner deterrence) from aggregate travel-distance distributions (TLDs) given an independently specified structural representation ($R_S$).
* **Real-World Goal:** Scientifically and efficiently exploit open Meta TLD data (3-bin aggregate releases) to establish robust behavioural calibration as an input stream for Paper 2.
* **Empirical Findings:** Multi-start MLE optimization achieves $\text{CV} = 0.0000\%$, $R^2 = 0.9624$, and noise robustness error $<0.45\%$ under $20\%$ noise perturbation.

## 3.2 Paper 2 Mission: Identifiability Stream
* **Core Task:** Spatial representation learning (Spatial GNNs) to learn an explicit Urban Structure Representation ($R_S$) from open spatial features ($X_S$: population density, land use, POI density, accessibility, road network layout) and operationalize it into production and attraction potentials $(O_i, A_j)$.
* **Methodological Rationale for Spatial GNNs:** Non-spatial tabular models ceiling at $R^2 \approx 0.481$ (QT14). The observed tabular performance ceiling motivates explicitly spatial relational representations, such as graph-based models.
* **Core Identifiability Premise:** Aggregate TLD constraints are underdetermined. Integrating $R_S$ with aggregate TLD constraints reduces solution space ambiguity sufficiently to enable defensible OD recovery.

## 3.3 The 3-Round Feasibility Quick-Test Suite (Q1–Q10 & Audit Results)

```text
ROUND A: KILL THE IDEA CHEAPLY ──► ROUND B: MECHANISM TEST ──► ROUND C: FEASIBILITY TEST
    (Q1, Q2, Q4, Q5)                   (Q6, Q8, Q9 + Neg Controls)          (Q7, Q10)
```

1. **Round A — Kill the Idea Cheaply (Q1, Q2, Q4, Q5):**
   * *Q1 (Tidelity):* $R^2 = 0.9624$ between $\hat{\beta}_{\text{OD}}$ and $\hat{\beta}_{\text{TLD}}$.
   * *Q4 (Observability vs Identifiability):* Proving $TLD_{\text{3bin}} \to \hat{\boldsymbol{\theta}}$ is stable ($\text{CV} = 0.00\%$), but $TLD_{\text{3bin}} \not\to \text{OD}$.
   * *Q5 (Non-Identifiability Demonstration):* Empirical proof that **Same TLD $\to$ Radically Different ODs** ($\text{JSD} = 0.000000$, yet $\text{CPC} = 0.5373$).
2. **Round B — Scientific Mechanism Test & Test A Audit (Q6, Q8, Q9 & Negative Controls):**
   * *Q6 & Test A Audit (Zero Oracle Leakage):* Evaluating Transferred Structure ($R_S$, $\text{CPC} = 0.6462$) against TLD-Only ($\text{CPC} = 0.5852$), Shuffled Negative Control ($\text{CPC} = 0.5331$), and Oracle Upper Bound ($\text{CPC} = 0.7159$).
   * *Q9 (Information Ablation Ladder):* Evaluating progressive recovery gains across $\text{TLD (0.6925)} \to \text{TLD}+O_i \text{ (0.7772)} \to \text{TLD}+A_j \text{ (0.8181)} \to \text{TLD}+S \text{ (1.0000)}$.
   * *Negative Controls:* Real Structure ($\text{CPC} = 0.6462$) significantly outperforms Shuffled Negative Control ($\text{CPC} = 0.5331$).
3. **Round C — Dissertation Feasibility Test (Q7, Q10):**
   * *Q7 (Zero-Target-OD Test):* Leave-one-city-out cross-city reconstruction achieves mean $\text{CPC} = 0.6462$ across 10 unseen test cities.
   * *Q10 (Pseudo-HCMC Stress Test):* Stress-testing transferability as a function of source-target structural similarity ($Transferability = f(\text{structural similarity})$).

---

# 4. Ho Chi Minh City Case Study & Empirical Defensibility

## 4.1 Evaluation of Unconstrained OD Allocation Properties
In alignment with the Evaluation Principle (*"Matching the Meta input is merely in-sample consistency. It is not evidence of structural OD recovery"*), the HCMC Case Study evaluates OD recovery on **unconstrained properties**—spatial allocation attributes that are NOT directly forced by the aggregate input TLD:

```text
                      UNCONSTRAINED OD PROPERTIES
       ┌───────────────────────────┼───────────────────────────┐
       ▼                           ▼                           ▼
Fine-Resolution Distance      Directional Spatial         Inter-District Corridor
  Decay Curve Shape           Flow Asymmetry              Arterial Allocation
(Beyond input coarse bins)   (Origin-Destination ratio)   (Traffic flow consistency)
```

1. **Fine-Resolution Distance Decay Shape:** Reconstructing smooth, continuous trip length distributions across fine distance intervals beyond the 3 coarse Meta input bins.
2. **Directional Spatial Flow Asymmetry:** Recovering asymmetric commuting patterns between suburban residential areas (e.g., Binh Chanh, District 12) and central employment hubs (District 1, Thu Duc).
3. **Inter-District Corridor Allocation:** Reconstructing major traffic flow volumes along primary arterial road corridors without direct corridor flow inputs.

## 4.2 The 3-Level Indirect Validation Hierarchy
1. **Level 1 — Internal Consistency:** Conservation of origin production and destination attraction sums ($\sum_j T_{ij} = O_i, \sum_i T_{ij} = A_j$), flow symmetry, and spatial smoothness.
2. **Level 2 — External Plausibility:** Alignment of inferred attraction potentials ($A_j$) with known economic centers (CBD District 1, Thu Duc Financial City, Tan Binh industrial zones) and major highway capacities.
3. **Level 3 — Partial Validation:** Auxiliary validation against available partial transit proxies (bus smart card tap-in/tap-out matrices, population census commuting counts, LBS location proxies) used strictly as boundary constraints rather than complete ground truth.

---

# 5. Summary of Scientific Contributions

1. **Theoretical Contribution:** Establishes Spatial Interaction as the formal scientific object and reframes Structure–Behaviour Decomposition as a mechanism to resolve OD non-identifiability.
2. **Methodological Contribution:** Proposes an independent inference protocol: learning structural representations ($R_S$) from open spatial features via GeoAI and inferring behavioural representations ($R_B$) from aggregate TLDs via MLE.
3. **Empirical Contribution:** Provides systematic evidence of data observability and aggregation robustness when compressing 20-bin primary TLDs to 3-bin Meta MDM open TLDs.
4. **Applied Contribution:** Delivers a defensible OD matrix reconstruction protocol for Ho Chi Minh City tested on unconstrained spatial allocation properties under extreme data scarcity.
5. **Practical Contribution:** Shifts urban planning paradigm from "costly disaggregated OD survey collection" to "maximizing scientific signal extraction from publicly available open data and aggregate mobility products."

---

# 6. Methodological Rule Compliance & Terminology Mapping

| Scientific Dimension | Conventional Conflated Framing | Refined Decoupled Framing (This Dissertation) |
| :--- | :--- | :--- |
| **Scientific Core** | Model prediction benchmarks | **Observability $\rightarrow$ Identifiability $\rightarrow$ Empirical Defensibility** |
| **Thesis Core Narrative** | "Models reconstruct OD" | **"Aggregate mobility is informative but non-identifying; structure resolves ambiguity"** |
| **Evaluation Principle** | Good in-sample fit = good model | **"Matching Meta input is merely in-sample consistency, not OD recovery evidence"** |
| **Identifiability Goal** | Break non-identifiability completely | **Reduce solution space ambiguity sufficiently for defensible OD recovery** |
| **Evaluation Target** | In-sample TLD matching | **Unconstrained properties of OD allocation** |
| **Oracle Marginal Role** | Flagship feasibility evidence | **Upper-bound ceiling ONLY (Test A Audit: Oracle $\text{CPC}=0.7159$)** |
| **Transferred Structure Role** | Secondary evaluation | **Primary Feasibility Evidence (Test A Audit: Transferred $\text{CPC}=0.6462$)** |
| **Tabular $R^2 \le 0.481$** | Proves GNN is mandatory | **Motivates explicitly spatial relational representations (Graph GNNs)** |
| **Pre-HCMC Validation** | Wait for HCMC ground truth | **Controlled simulation: Artificial Aggregation $\to$ Hide OD $\to$ Reconstruct $\to$ Reveal OD** |
| **Quick Test Pipeline** | Exploratory trial & error | **3-Round Decision Pipeline (Q1–Q10) with Go/Revise/Stop matrix** |
| **Urban Structure** | Urban Structure = $(O_i, A_j)$ | $\text{Urban Structure} \longrightarrow R_S \longrightarrow (O_i, A_j)$ |
| **AI Learning Role** | GNN learns Urban Structure | GNN learns task-specific representation ($Z_{\text{task}}$) from $X_S$ |
| **Latent Embedding** | Latent vector $Z = R_S$ | $Z_{\text{task}} \neq R_S$ by default (requires structural validation) |
| **Travel Behaviour** | Deterrence function *is* Behaviour | Deterrence function operationalizes representation $R_B(\boldsymbol{\theta})$ |
| **Local Inference Rationale** | Intrinsic untransferable property | **Modelling principle & strategic design choice** |
| **Parameter Identification** | Mathematical proof of identifiability | **Multi-tiered evidence bundle** (QT12, QT18, $R^2 = 0.9624$) |
| **Structural Transferability** | Absolute assumption of transfer | **Testable empirical hypothesis ($H_2$)** |
| **ANOVA ($\eta^2_S = 81.3\%$)** | Absolute proof of natural law | Empirical support for decomposition's analytical usefulness |
| **Privacy Motivation** | Aggregate TLD is DP guaranteed | Aggregation reduces granularity; depends on release mechanism |
| **Paper Relationship** | Sequential dependency | **Decoupled complementary parallel inference pathways** |

---
*Status: Updated V7.0 — Full Test A Audit & Refined Scientific Core Narrative.*
