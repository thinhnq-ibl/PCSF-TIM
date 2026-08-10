# Mechanism-Based Human Mobility Science — Mind Map & Architecture State (v3.0)

> **CORE DISSERTATION MISSION STATEMENT:**  
> *"To advance the scientific understanding of Spatial Interaction by independently identifying the Travel Behaviour Representation from aggregate mobility observations and independently learning the Urban Structure Representation from observable urban features—enabling quantitative explanation, diagnosis, policy evaluation, and transferable knowledge of urban mobility systems."*

> **SCIENTIFIC PROPOSITION (End of Module 3):**  
> *"Although Spatial Interaction emerges from the interaction between Urban Structure Representation and Travel Behaviour Representation, treating these representations as analytically distinguishable enables different scientific questions to be formulated, different learning objectives to be defined, and different learning strategies to be developed."*

> **CORE PRINCIPLE:** Structure–Behaviour **Decomposition** Principle (analytically distinguishable representations).

---

## 1. The 8 Realigned Scientific Modules & Causal Chain

```text
Spatial Interaction as Scientific Object (Module 1)
      │
      ▼
Observing Spatial Interaction (Module 2)
      │
      ▼
Identifying Common Conceptual Decomposition & Scientific Proposition (Module 3)
      │
 ┌────┴────┐
 ▼         ▼
Urban Structure Representation   Travel Behaviour Representation
      (Module 4)                           (Module 5)
          │                                     │
          └──────────────────┬──────────────────┘
                             ▼
Learning Representations for Spatial Interaction (Module 6)
(Learning Objective ──► Learning Strategy ──► Representation ──► Generalization)
                             ▼
                     Research Gaps (Module 7)
               (Formulate RQ1 & RQ2)
                             ▼
                 Dissertation Framework (Module 8)
(Principle ──► two parallel pathways [Gap I ──► RQ1 ──► Paper 1; Gap II ──► RQ2 ──► Paper 2] ──► Joint Integration / RQ3 ──► Downstream Validation ──► Dissertation Synthesis)
```

---

## 2. Module Mapping & Scientific Questions Matrix

| Module | Scientific Question | Mission | Key Outcome |
| :--- | :--- | :--- | :--- |
| **Module 1** | **Why should Spatial Interaction be treated as the central scientific object for understanding human mobility?** | Establish Spatial Interaction as the formal scientific object of the dissertation, framing Human Mobility as its empirical phenomenon. | Spatial Interaction is established as the formal scientific object of the dissertation. |
| **Module 2** | **How can Spatial Interaction be observed from available mobility data?** | Synthesize mobility data sources (HTS, CDR, GPS, LBS, Meta MDM \citep{MetaMovementDistributionMaps}, TLDs, OD matrices) as complementary observation projections. | Mobility datasets are unified as different observation projections of the same underlying Spatial Interaction phenomenon. |
| **Module 3** | **Can a common conceptual decomposition be identified across existing spatial interaction models?** | Analyze Gravity, Radiation, and Neural models to synthesize recurring conceptual components into a formal analytical decomposition. | Formulate the **Structure–Behaviour Decomposition Principle** and the **Scientific Proposition**. |
| **Module 4** | **How should Urban Structure be represented for spatial interaction modelling?** | Trace the evolution of Urban Structure representations from handcrafted census/POI variables to learned Mobility Potential Fields. | Urban Structure representation evolves from handcrafted variables to learned, transferable potential fields (**Paper 2**). |
| **Module 5** | **How should Travel Behaviour be represented for spatial interaction modelling?** | Trace the evolution of Travel Behaviour representations from analytical decay functions to statistically identified parameter vectors $\hat{\boldsymbol{\theta}}$ from aggregate TLDs. | Travel Behaviour representation evolves from analytical decay functions to statistically identified parameter vectors (**Paper 1**). |
| **Module 6** | **How do learning objectives and strategies shape learned representations and their ability to generalize?** | Explain causal chain: **Learning Objective $\to$ Learning Strategy $\to$ Representation $\to$ Encoded Information $\to$ Generalization.** | Establish the scientific mechanism linking learning objectives with representation transferability across spatial contexts. |
| **Module 7** | **What scientific questions remain unresolved after introducing the Structure–Behaviour Decomposition Principle?** | Formally derive research questions from the open scientific gaps following the Decomposition Principle. | Formulate **Research Question 1** (Paper 1 — Travel Behaviour Identification) and **Research Question 2** (Paper 2 — Urban Structure Representation). |
| **Module 8** | **How does this dissertation operationalize the Structure–Behaviour Decomposition Principle into a coherent research framework?** | Operationalize the principle into research questions, papers, probabilistic integration, and dissertation framework. | Establish derivation structure: **Structure–Behaviour Decomposition Principle $\to$ two complementary parallel pathways (Gap I $\to$ RQ1 $\to$ Paper 1; Gap II $\to$ RQ2 $\to$ Paper 2) $\to$ Joint Integration (RQ3) $\to$ Downstream OD Reconstruction Validation $\to$ Dissertation Synthesis.** |

