---
title: "PhD Operating System & Master Research Notebook (handbook_phd.md)"
subtitle: "Hệ Điều Hành Luận án Tiến sĩ & Sổ tay Nghiên cứu Khoa học Phân tích"
author: "PhD Candidate"
date: "2026"
anchor-reference: "Handbook.md (Anchor for Stage 1 Knowledge Base)"
system-protocol: "One Conversation → One Refinement"
---

# PhD Operating System & Master Research Notebook
# Hệ Điều Hành Luận án Tiến sĩ & Sổ tay Nghiên cứu Khoa học

---

## 📌 Three Evolutionary Stages of the PhD Journey

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 1 (Completed): Handbook.md                                                       │
│ • Focus: "What is Human Mobility?" (Knowledge Acquisition & Literature Synthesis).      │
│ • Role: Immutable Stage 1 Knowledge Base Anchor. Do NOT modify.                        │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 2 (Active - Operating System): handbook_phd.md                                   │
│ • Focus: "What is my specific scientific contribution to Spatial Interaction Science?"  │
│ • Role: Living PhD Notebook & Decision Operating System (8 Modules).                   │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 3 (Future Output): PhD Dissertation & Monograph                                  │
│ • Focus: 6-Chapter PhD Monograph Defense & Publications (Paper 1 & Paper 2).           │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

# CORE DISSERTATION MISSION STATEMENT

> **"To advance the scientific understanding of Spatial Interaction by independently identifying the Travel Behaviour Representation from aggregate mobility observations and independently learning the Urban Structure Representation from observable urban features—enabling quantitative explanation, diagnosis, policy evaluation, and transferable knowledge of urban mobility systems."**

---

# THE SCIENTIFIC PROPOSITION (End of Module 3)

> **"Although Spatial Interaction emerges from the interaction between Urban Structure Representation and Travel Behaviour Representation, treating these representations as analytically distinguishable enables different scientific questions to be formulated, different learning objectives to be defined, and different learning strategies to be developed."**

*Role:* Serves as the philosophical and methodological backbone of the dissertation.

---

# THE 8 SCIENTIFIC MODULES — MASTER MATRIX

| Module | Scientific Question | Mission | Key Outcome |
| :--- | :--- | :--- | :--- |
| **1. Spatial Interaction as the Scientific Object** | **Why should Spatial Interaction be treated as the central scientific object for understanding human mobility?** | Establish Spatial Interaction as the scientific object of the dissertation. | Spatial Interaction is established as the central scientific object. Human Mobility is the empirical phenomenon. |
| **2. Observing Spatial Interaction** | **How can Spatial Interaction be observed from available mobility data?** | Review how Spatial Interaction is observed through different mobility datasets. | Different mobility datasets (trajectories, OD matrices, TLDs, aggregate statistics) are recognized as different observations of the same underlying phenomenon. |
| **3. Identifying a Common Conceptual Decomposition in Spatial Interaction Models** | **Can a common conceptual decomposition be identified across existing spatial interaction models?** | Identify and synthesize recurring conceptual components across existing spatial interaction models, and formalize them as an analytical decomposition. | **Structure–Behaviour Decomposition Principle** together with the **Scientific Proposition**. |
| **4. Urban Structure Representation** | **How should Urban Structure be represented for spatial interaction modelling?** | Review the evolution of Urban Structure representations from handcrafted variables to learned potential fields. | Urban Structure remains the same scientific concept, while its representation evolves from handcrafted variables to learned representations → motivates **Paper 2**. |
| **5. Travel Behaviour Representation** | **How should Travel Behaviour be represented for spatial interaction modelling?** | Review the evolution of Travel Behaviour representations from analytical decay functions to statistically identified mechanisms. | Travel Behaviour representations evolve from simple analytical functions to empirically identified parameters → motivates **Paper 1**. |
| **6. Learning Representations for Spatial Interaction** | **How do learning objectives and learning strategies shape learned representations and their ability to generalize across spatial contexts?** | Explain the causal chain: **Learning Objective → Learning Strategy → Representation → Encoded Information → Generalization / Transferability.** | Learning objectives and strategies determine what information is encoded in representations and therefore govern their generalization and transferability across cities. |
| **7. Research Gaps** | **What scientific questions remain unresolved after introducing the Structure–Behaviour Decomposition Principle?** | Derive the research questions from the identified scientific gaps. | **Research Question 1** (Paper 1 — Travel Behaviour Identification) and **Research Question 2** (Paper 2 — Urban Structure Representation) are formulated. |
| **8. Dissertation Framework** | **How does this dissertation operationalize the Structure–Behaviour Decomposition Principle into a coherent research framework?** | Operationalize the principle into research questions, papers, and the dissertation framework. | **Structure–Behaviour Decomposition Principle → RQ1 → Paper 1 → RQ2 → Paper 2 → Dissertation Framework.** |

---

# LOGICAL FLOW OF THE 8 MODULES

```text
Spatial Interaction as Scientific Object (Module 1)
      │  [Why Spatial Interaction, not Human Mobility?]
      ▼
Observing Spatial Interaction (Module 2)
      │  [Trajectories / OD / TLD / Statistics = different observations of same phenomenon]
      ▼
Identifying Common Conceptual Decomposition (Module 3)
      │  → Structure–Behaviour Decomposition Principle
      │  → Scientific Proposition
      │
 ┌────┴────┐
 ▼         ▼
Urban Structure          Travel Behaviour
Representation           Representation
(Module 4)               (Module 5)
[observable → learnable] [aggregate → identifiable]
[→ Paper 2]              [→ Paper 1]
      │         │
      └────┬────┘
           ▼
Learning Representations for Spatial Interaction (Module 6)
[Learning Objective → Learning Strategy → Representation → Generalization]
           ▼
Research Gaps (Module 7)
[RQ1: Can Travel Behaviour be independently identified?]
[RQ2: Can Urban Structure be independently represented & transferred?]
           ▼
Dissertation Framework (Module 8)
[Decomposition Principle → RQ1 → Paper 1 → RQ2 → Paper 2 → Framework]
```

---

# STRATEGIC PARADIGM SHIFT (BEFORE vs. AFTER)

| Item | Before Quick Tests | After QT1–QT19 + Refined 8-Module Framework |
| :--- | :--- | :--- |
| **Scientific Object** | Human Mobility (phenomenon) | **Spatial Interaction (formal scientific object)** |
| **Dissertation Goal** | Build OD reconstruction framework | **Advance Spatial Interaction Science through independent representation identification** |
| **Core Principle** | Gravity model baseline | **Structure–Behaviour Decomposition Principle + Scientific Proposition** |
| **Module 3 Output** | A separability claim | **Scientific Proposition (philosophically grounded analytical distinguishability)** |
| **Paper 1** | Estimate decay $\beta$ | **Identify Travel Behaviour Representation from aggregate TLD** |
| **Paper 2** | Learn $O_i, A_j$ | **Learn transferable Urban Structure Representation** |
| **Module 6** | Information Hierarchy | **Learning Objective → Strategy → Representation → Generalization causal chain** |
| **Integration** | Reconstruct OD | **Explain Spatial Interaction — OD reconstruction is validation evidence** |

---

# DEEP DIVE: THE 8 MODULES

### Module 1. Spatial Interaction as the Scientific Object
**Scientific Question:** Why should Spatial Interaction be treated as the central scientific object for understanding human mobility?
- **Mission:** Establish Spatial Interaction as the formal scientific object of the dissertation.
- **Key Distinction:** Human Mobility = empirical phenomenon. Spatial Interaction = formal scientific object (mathematical representation of collective flow intensities between origins and destinations).
- **Empirical Anchors:** QT8 (Gravity CPC = 0.704), QT16 (ANOVA decomposition of flow variance).

### Module 2. Observing Spatial Interaction
**Scientific Question:** How can Spatial Interaction be observed from available mobility data?
- **Mission:** Show that Trajectories, OD Matrices, TLDs, and Aggregate Statistics are all different observation layers of the same latent Spatial Interaction phenomenon.
- **Key Insight:** Different datasets are not different phenomena — they are different projections. This justifies using aggregate TLD (Meta MDM \citep{MetaMovementDistributionMaps}) as a valid observation source for Paper 1.
- **Empirical Anchors:** QT1 ($R^2 = 0.9624$), QT18 (noise robustness $< 0.5\%$).

### Module 3. Identifying a Common Conceptual Decomposition
**Scientific Question:** Can a common conceptual decomposition be identified across existing spatial interaction models?
- **Mission:** Synthesize recurring components (Structure, Behaviour/decay) across Gravity, Radiation, Entropy, and Neural models into a formal analytical decomposition.
- **Key Output:** Structure–Behaviour Decomposition Principle + Scientific Proposition.
- **Empirical Anchors:** QT3 (CPC insensitive to $\beta$ perturbation), QT15 (linear degradation under structure noise), QT16 (ANOVA: Structure $\eta^2 = 81.3\%$, Behaviour $\eta^2 = 5.3\%$).

### Module 4. Urban Structure Representation
**Scientific Question:** How should Urban Structure be represented for spatial interaction modelling?
- **Mission:** Trace the evolution of Urban Structure representations: handcrafted census/POI variables → learned Mobility Potential Fields via GNNs.
- **Key Property:** *Observable → Representable → Transferable.* Urban structure is observable; spatial learning encodes it into a transferable representation.
- **Empirical Anchors:** QT4/5 ($R^2 \approx 0.45$), QT6 (Population 43.8%, POI 18.7%), QT13 ($\Delta R^2 < 0.005$ for extra tabular features), QT14 (ceiling $R^2 \le 0.48$ for all tabular models → GNN justified).

### Module 5. Travel Behaviour Representation
**Scientific Question:** How should Travel Behaviour be represented for spatial interaction modelling?
- **Mission:** Trace the evolution of Travel Behaviour representations: Power-law → Exponential → Tanner decay → Empirically identified $\hat{\boldsymbol{\theta}}$ from aggregate TLD.
- **Key Property:** *Aggregate-observable → Statistically identifiable.* Behaviour is not directly observable; it is inferred from the empirical consequences visible in TLDs.
- **Empirical Anchors:** QT1 ($R^2 = 0.9624$), QT2 (city-specific $\beta$, $CV = 28.7\%$), QT12 (multi-start $\text{CV} = 0.00\%$), QT18 ($<0.5\%$ error under $20\%$ noise).

### Module 6. Learning Representations for Spatial Interaction
**Scientific Question:** How do learning objectives and learning strategies shape learned representations and their ability to generalize?
- **Mission:** Explain the causal chain: **Learning Objective → Learning Strategy → Representation → Encoded Information → Generalization / Transferability.**
- **Application to Paper 1:** Learning Objective = identify $\boldsymbol{\theta}$; Learning Strategy = Conditional MLE; Representation = distance-decay parameter; Generalization = city-specific identification.
- **Application to Paper 2:** Learning Objective = represent $(O_i, A_j)$ transferably; Learning Strategy = Spatial GNN; Representation = Mobility Potential Field; Generalization = zero-shot cross-city transfer.
- **Empirical Anchors:** QT17 (zero-shot CPC = 0.646), QT19 (performance plateaus at 15–20 training cities).

### Module 7. Research Gaps
**Scientific Question:** What scientific questions remain unresolved after introducing the Structure–Behaviour Decomposition Principle?
- **Mission:** Formally derive RQ1 and RQ2 from the gaps left open by the Decomposition Principle.
- **Gap for RQ1:** Although Travel Behaviour is a component of Spatial Interaction, no framework has established that it can be independently identified from aggregate observations alone.
- **Gap for RQ2:** Although Urban Structure is observable, no framework has established a learned representation that is independently transferable to unseen cities without joint optimization with flow data.
- **Research Questions formulated:** RQ1 (Paper 1) and RQ2 (Paper 2).

### Module 8. Dissertation Framework
**Scientific Question:** How does this dissertation operationalize the Structure–Behaviour Decomposition Principle into a coherent research framework?
- **Mission:** Operationalize the principle into research questions, papers, probabilistic integration, and dissertation framework.
- **Derivation Chain:** Structure–Behaviour Decomposition Principle → RQ1 → Paper 1 (Behaviour Identification) → RQ2 → Paper 2 (Structure Representation) → Probabilistic Integration → Dissertation Framework.
- **Validation Logic:** Reconstructed OD matrix is not the goal — it is the empirical evidence that independently recovered representations adequately explain Spatial Interaction.
