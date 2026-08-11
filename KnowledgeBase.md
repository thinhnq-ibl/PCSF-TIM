# Research Knowledge Base (RKB): Master Scientific Operating System

> **Status:** Version 7.0 — Full Test A Audit & Refined Scientific Core Narrative  
> **Core Scientific Master Statement (Frozen):**  
> *"Human mobility can be reconstructed by independently inferring its structural and behavioural components from the maximum publicly available information."*  
> *(Vietnamese: "Có thể phục hồi tương tác di chuyển đô thị bằng cách suy luận độc lập thành phần cấu trúc và thành phần hành vi từ lượng thông tin công khai tối đa.")*  
> **Evaluation Principle (Dissertation Directive):**  
> *"Matching the Meta input is merely in-sample consistency. It is not evidence of structural OD recovery."*  
> **Condensed Core Narrative:**  
> *"Aggregate mobility appears informative but non-identifying. The remaining scientific problem is determining what independent structural information is sufficient to resolve that ambiguity."*

---

## 1. Overall System Architecture & Derivation Flow

```text
                           RESEARCH KNOWLEDGE BASE (RKB)
                                 (Source of Truth)
                                        │
           ┌────────────────────────────┼────────────────────────────┐
           ▼                            ▼                            ▼
     OBSERVABILITY                    IDENTIFIABILITY            EMPIRICAL DEFENSIBILITY
       (Paper 1)                        (Paper 2)                   (HCMC Case Study)
Which info survives aggregation     What structure resolves       Is latent OD defensible on
    from aggregate TLD?               OD ambiguity?             UNCONSTRAINED properties?
```

The Knowledge Base serves as the background scientific operating system backing all publications and the PhD dissertation. It structures scientific knowledge into **8 Core Modules**, **4 Claim Hierarchy Layers** (with 4-field claim cards), and the **10 Strategic Decision Quick Tests (Q1–Q10)**.

---

## 2. Executive Matrix of 8 Scientific Modules

| Module | Scientific Core Question | Mission & Scope | Key Outcome / Paper Mapping |
| :--- | :--- | :--- | :--- |
| **Module 1. Spatial Interaction** | **Why treat Spatial Interaction as the central scientific object?** | Establish Spatial Interaction as the scientific object; position OD matrices as specific observation projections. | Conceptual foundation for entire dissertation. |
| **Module 2. Observability** | **Which information survives aggregation in Meta data?** | Synthesize observation layers (OD, GPS, CDR, LBS, Meta MDM \citep{MetaMovementDistributionMaps}, TLDs) under spatial support reliability. | Observability stream (**Paper 1**). |
| **Module 3. Identifiability & Ambiguity** | **What structure is sufficient to resolve OD ambiguity?** | Formulate the **Structure–Behaviour Decomposition Principle** as a mechanism to constrain underdetermined OD solution spaces. | Mathematical backbone ($T_{ij} = O_i A_j f(d_{ij}; \boldsymbol{\theta})$). |
| **Module 4. Urban Structure** | **How should Urban Structure ($R_S$) be represented and learned?** | Trace representation evolution from tabular variables ($R^2 \le 0.481$) to GNN-learned potential fields $(O_i, A_j)$ from open spatial features. | Identifiability stream (**Paper 2**). |
| **Module 5. Travel Behaviour** | **How should Travel Behaviour ($R_B$) be identified from aggregate data?** | Formulate parametric statistical inference of distance friction $\boldsymbol{\theta}$ from aggregate TLDs (20-bin & 3-bin Meta MDM). | Behaviour identification & inference pathway (**Paper 1**). |
| **Module 6. Learning Strategy** | **How do learning objectives shape encoded representations?** | Formalize the methodological chain: `Objective` $\to$ `Strategy` $\to$ `Representation` $\to$ `Encoded Info` $\to$ `Generalization`. | Epistemological separation between GeoAI embeddings $Z_{\text{task}}$ and scientific representation $R_S$. |
| **Module 7. Transferability** | **What components can transfer vs. what must be inferred locally?** | Evaluate structural transferability ($H_2$) across cities while maintaining local behavioral inference as a conservative design choice. | Zero-target-OD transfer protocol across heterogeneous urban domains (**Paper 2**). |
| **Module 8. Empirical Defensibility** | **How is reconstructed latent OD empirically defended without ground truth?** | Evaluate reconstructed flows on **unconstrained properties of OD allocation** using a 3-level validation hierarchy for Ho Chi Minh City. | Downstream OD reconstruction roadmap for **HCMC Case Study**. |

---

## 3. Strategic 10 Quick-Test Suite & Audit Execution Results

### 3.1 Test A Audit Results (Zero Oracle Leakage Verification)

To eliminate information leakage, **Test A Audit** evaluated four distinct models across 10 unseen test cities:

```text
Model A (TLD Only Baseline)       : Mean CPC = 0.5852 (Std: 0.0530)
Model B (Shuffled Control)         : Mean CPC = 0.5331 (Std: 0.0463)
Model C (Transferred Structure)    : Mean CPC = 0.6462 (Std: 0.0616, Median: 0.6525, Range: [0.4983, 0.7125])
Model D (Oracle Upper Bound)       : Mean CPC = 0.7159 (Std: 0.0419)  [CEILING ONLY]
```

* **Scientific Finding:** Transferred Urban Structure ($R_S$, $\text{CPC} = 0.6462$) learned strictly from open spatial features consistently outperforms both TLD-Only ($\text{CPC} = 0.5852$) and Shuffled Negative Control ($\text{CPC} = 0.5331$) across all 10 unseen test cities without relying on Oracle OD marginals!

---

## 4. Master Claim Cards & Refined Wording

#### Claim Card C.1 — Tabular Representation Ceiling & Relational Motivation
* **Claim:** Non-spatial tabular models display an empirical performance limit ($R^2 \approx 0.481$) when predicting operational structural quantities ($O_i, A_j$). The observed tabular performance ceiling motivates explicitly spatial relational representations, such as graph-based models.
* **Evidence:** Quantitative Experiment QT14 (Ridge $0.386$, RF $0.459$, GBDT $0.481$, MLP $0.445$). Feature expansion from 6 to 12 features yields only $+0.0024 R^2$ gain (QT13).
* **Boundary:** Does not theoretically disprove all possible feature representations; demonstrates the limitations of non-spatial tabular regression families.
* **Paper Role:** Paper 2 Motivation, Knowledge Base Module 4.

---
*Status: Updated V7.0 — Master Scientific Operating System (Test A Audit & Refined Core Narrative).*
