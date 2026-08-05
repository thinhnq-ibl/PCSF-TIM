# PhD Dissertation Proposal (V2.0 — Post Quick Tests Validation)

## Title

**Learning Human Mobility from Aggregate Observations: Identification of Spatial Interaction Behaviour and Transferable Urban Structure for OD Matrix Reconstruction**

### Subtitle
*Towards Mechanism-based Human Mobility Science through Behaviour Identification and Urban Structure Representation*

---

> **Single Master Opening Statement:**
> **"This research aims to establish a mechanism-based scientific framework for Human Mobility by independently identifying the Behaviour of Spatial Interaction from aggregate mobility observations and representing Urban Structure from observable urban features. The reconstructed OD matrix serves as empirical evidence that these independently recovered components capture the fundamental mechanisms governing urban mobility."**

---

# 1. Motivation & Vision

Urban mobility is one of the most important collective phenomena in modern cities. Mobility data serve as a dynamic input to economic analysis, transportation planning, and public health policies.

Modern cities have become increasingly observable through multi-source open spatial data (OSM, POIs, Sentinel/Landsat) and geospatial representation learning. Furthermore, aggregate mobility products—including Meta's Movement Distribution Maps (MDM) \citep{MetaMovementDistributionMaps}—are becoming increasingly available across platforms and regions, providing privacy-preserving summaries of population travel behavior.

However, **current studies primarily model mobility as a prediction problem rather than a scientific phenomenon**. Consequently, although OD matrices can be predicted via black-box machine learning models, **the underlying mechanisms generating urban mobility remain poorly understood**.

### Research Vision

> **Rather than treating urban mobility as a black-box prediction problem, this dissertation establishes a mechanism-based framework that decomposes mobility into interpretable structural and behavioural components, enabling quantitative explanation, diagnosis, policy evaluation, and transferable understanding of urban mobility systems.**

---

# 2. Research Gap

Existing studies learn mobility directly from observations. As a consequence, **urban structure and travel behaviour remain entangled**, preventing independent understanding, quantification, and transfer of their roles.

Neither the traditional gravity paradigm nor modern deep learning models (e.g., DeepGravity) provide a unified framework that independently models components according to their fundamentally distinct functional roles:

1. **Urban Structure** (where spatial opportunities exist), and
2. **Behaviour of Spatial Interaction** (how collective willingness/sensitivity attenuates over distance to utilize those opportunities).

---

# 3. Scientific Principle

## Structure–Behaviour Separation Principle

Human mobility is represented as a production-constrained spatial interaction process where **Behaviour acts on Structure**:

$$T_{ij} = O_i \frac{A_j f(d_{ij}; \boldsymbol{\theta})}{\sum_{m} A_m f(d_{im}; \boldsymbol{\theta})}$$

Urban Structure and Behaviour play complementary rather than equivalent roles in spatial interaction:

### Urban Structure (Mobility Potential Field)

$$\boldsymbol{\Phi} = (\mathbf{O}, \mathbf{A})$$

describes the spatial distribution of **Production Potential ($O_i$)** (latent origin trip-emission capacity) and **Attraction Potential ($A_j$)** (latent destination opportunity density), defining *where spatial opportunities exist*.

### Behaviour of Spatial Interaction

Defined as the **collective distance sensitivity governing the utilization of spatial opportunities**:

$$f(d; \boldsymbol{\theta})$$

describes how travellers trade off spatial opportunities against travel distance. Distance decay vector $\boldsymbol{\theta}$ (e.g., Tanner deterrence parameters $\alpha, \beta$) serves as the **mathematical proxy/representation** of this Behaviour.

---

# 4. Central Scientific Proposition & Hypotheses

### Hypotheses

* **Hypothesis 1 (H1 — Paper 1):**  
  *The Behaviour of Spatial Interaction can be independently identified from aggregate travel-distance observations.*

* **Hypothesis 2 (H2 — Paper 2):**  
  *Urban Structure can be independently represented from observable urban features.*

### Central Scientific Proposition

> **Human Mobility emerges from the interaction between Urban Structure and Behaviour.**  
> The reconstructed OD matrix serves as empirical validation evidence that these independently recovered components capture the fundamental mechanisms governing urban movement flows.

---

# 5. Research Questions

### RQ1 (Paper 1 — Behaviour Identification)

*Can the Behaviour of Spatial Interaction be independently identified from aggregate travel-distance observations?*

---

### RQ2 (Paper 2 — Urban Structure Representation)

*Can Urban Structure be independently represented from observable urban features?*

---

### RQ3 (Integration — Mechanism-based Mobility Science)

*Can Human Mobility be explained through the interaction between the identified Behaviour and the represented Structure?*

*(Note: The objective of RQ3 is **explanation**, not merely prediction. OD matrix reconstruction is the empirical validation evidence).*

---

# 6. Master Research Framework

```text
                       HUMAN MOBILITY
                              │
                              ▼
           Structure–Behaviour Separation Principle
                              │
        ┌───────────────┴───────────────┐
        ▼                               ▼
 Urban Structure                  Behaviour
(Mobility Potential)      (Distance Sensitivity)
        │                               │
 Represented from             Identified from
 Urban Features               Aggregate Mobility
        │                               │
        └───────────────┬───────────────┘
                        ▼
              Gravity-based Interaction
                        ▼
               Observed Mobility (OD)
```

---

# 7. Paper 1

## Identification of the Behaviour of Spatial Interaction from Aggregate Travel-Distance Distributions

### Scientific Objective

Provide empirical statistical evidence supporting parameter recovery of the **Behaviour of Spatial Interaction** (collective distance sensitivity $\beta$) from aggregate travel-distance observations (TLDs).

### Main Contributions

* Operationally define Behaviour of Spatial Interaction as collective distance sensitivity.
* Develop a binned probabilistic observation model under aggregate information loss.
* Derive exact conditional likelihood and evaluate likelihood surface sharpness (QT12: Multi-start $\text{CV} = 0.00\%$).
* Demonstrate parameter recovery robustness under observational noise (QT18: $<0.5\%$ error under $20\%$ noise).

### Scientific Evidence Provided

Supports **Hypothesis 1**: Behaviour can be independently identified from aggregate travel-distance observations without requiring pairwise OD labels ($R^2 = 0.9624$).

---

# 8. Paper 2

## Representation of Urban Mobility Potential Field for Spatial Interaction Modeling

### Scientific Objective

Learn and represent the **Urban Mobility Potential Field** ($\mathbf{O}, \mathbf{A}$) from multi-source open urban spatial features, demonstrating that non-spatial tabular models ceiling at $R^2 \approx 0.48$ (QT14) and establishing the necessity of Spatial Graph Neural Networks.

### Main Contributions

* Formalize the Urban Mobility Potential Field consisting of Production Potential ($O_i$) and Attraction Potential ($A_j$).
* Prove that tabular model capacity ceilings ($R^2 \le 0.48$, QT14) mandate Spatial Graph Neural Network representations.
* Establish cross-city zero-shot transferability evaluation benchmarks (QT17: Test $\text{CPC} = 0.646$).

### Scientific Evidence Provided

Supports **Hypothesis 2**: The Mobility Potential Field of Urban Structure can be independently estimated and represented using publicly available urban features.

---

# 9. Expected Scientific Contributions

### Contribution 1 (Theory of Behaviour Identification)
Develop a probabilistic inference theory and statistical proof showing that collective travel behaviour can be identified from aggregate mobility statistics.

### Contribution 2 (Scientific Representation of Urban Structure)
Develop a spatial representation framework that models Urban Structure as a Mobility Potential Field ($O_i, A_j$) using GeoAI and open urban data.

### Contribution 3 (Mechanism-based Framework for Human Mobility)
Establish a mechanism-based scientific framework that explains collective human movement flows through the interaction of independently recovered Structure and Behaviour.

---

# 10. Expected Scientific Impact

```text
Scientific Understanding ──► Quantitative Diagnosis ──► Policy Interpretation ──► Mechanism-based Evaluation ──► Transferable Mobility Knowledge
```

---

# 11. Narrative Evolution Summary (Before vs. After Quick Tests)

| Component | Before Quick Tests | After Quick Tests (QT1–QT19) |
| :--- | :--- | :--- |
| **Motivation** | Better OD prediction | **Better scientific understanding** |
| **Research Gap** | Lack of transferability | **Lack of scientific decomposition (Structure & Behaviour entangled)** |
| **Scientific Principle** | Gravity model baseline | **Structure–Behaviour Separation Principle** |
| **Paper 1** | Estimate decay $\beta$ | **Identify Behaviour from aggregate TLD** |
| **Paper 2** | Learn $O_i, A_j$ | **Represent Urban Structure (Mobility Potential Field)** |
| **Integration** | Reconstruct OD | **Explain Human Mobility mechanisms** |
| **Validation** | CPC score optimization | **Empirical scientific evidence** |
| **Contribution** | Better AI model | **New Mechanism-based Scientific Framework** |

---
*Status: Updated V2.0 — Post Quick Tests 1–19 Validation Reference Standard for PhD Proposal & Dissertation.*
