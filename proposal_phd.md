# PhD Dissertation Proposal (V2.1 — Post Quick Tests 1–19 Validation)

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

> **Rather than treating urban mobility as a black-box prediction problem, this dissertation establishes a mechanism-based framework founded on the independent representation of Urban Structure and the independent identification of Behaviour, enabling quantitative explanation, diagnosis, policy evaluation, and transferable understanding of urban mobility systems.**

---

# 2. Research Gap

Existing studies learn mobility directly from observations. As a consequence, **urban structure and travel behaviour remain entangled**, preventing independent understanding, quantification, and transfer of their roles.

These limitations are not merely methodological but conceptual. Existing models jointly optimize urban structure and travel behaviour as a single predictive function, preventing either component from being independently interpreted, transferred, or statistically identified. Consequently, the literature motivates a scientific decomposition of Human Mobility into two complementary mechanisms—Urban Structure and Behaviour—rather than a new predictive architecture. This Structure–Behaviour Separation Principle therefore emerges as a necessary consequence of the limitations of the existing Observation-First paradigm, rather than an arbitrary modelling choice.

Neither the traditional gravity paradigm nor modern deep learning models (e.g., DeepGravity) provide a unified framework that independently models components according to their fundamentally distinct functional roles:

1. **Urban Structure** (where spatial opportunities exist), and
2. **Behaviour of Spatial Interaction** (how collective willingness/sensitivity attenuates over distance to utilize those opportunities).

---

# 3. Scientific Principle

## Structure–Behaviour Separation Principle

Human mobility is represented as a production-constrained spatial interaction process where **Behaviour acts on Structure**:

$$T_{ij} = O_i \frac{A_j f(d_{ij}; \boldsymbol{\theta})}{\sum_{m} A_m f(d_{im}; \boldsymbol{\theta})}$$

This decomposition immediately suggests a new scientific proposition. If Urban Structure can be represented and transferred independently, and Behaviour can be statistically identified from aggregate observations, then their probabilistic interaction provides sufficient information to reconstruct OD flows. The reconstructed OD matrix is therefore not the objective of the framework, but empirical evidence that these independently recovered mechanisms adequately explain observed mobility.

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
Urban Features
      │
Represent Structure
      │
      ▼

Aggregate Mobility
      │
Identify Behaviour
      │
      ▼

Probabilistic Integration
      │
(Gravity as Scientific Language)
      │
      ▼

OD Reconstruction
(Validation)
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

Urban Structure is directly observable through publicly available urban features. Because observable spatial characteristics can be systematically represented using spatial representation learning, the resulting Mobility Potential Field becomes transferable across cities. This observable → representable → transferable property forms the scientific basis for estimating Urban Structure in previously unseen urban environments.

### Main Contributions

* Formalize the Urban Mobility Potential Field consisting of Production Potential ($O_i$) and Attraction Potential ($A_j$).
* Prove that tabular model capacity ceilings ($R^2 \le 0.48$, QT14) mandate Spatial Graph Neural Network representations.
* Establish cross-city zero-shot transferability evaluation benchmarks (QT17: Test $\text{CPC} = 0.646$).

### Scientific Evidence Provided

Supports **Hypothesis 2**: The Mobility Potential Field of Urban Structure can be independently estimated and represented using publicly available urban features.

---

# 9. Probabilistic Integration Protocol & Scientific Contributions

### Integration Protocol

The principal methodological contribution of this dissertation is not a new Gravity model. Instead, it is a probabilistic integration protocol that combines two independently inferred scientific components: Urban Structure represented from observable urban features and Behaviour identified from aggregate mobility observations. Gravity serves as the common scientific language through which these independently recovered mechanisms interact to generate observable mobility flows.

### Contribution 1 (Theory of Behaviour Identification)
Develop a probabilistic inference theory and statistical proof showing that collective travel behaviour can be identified from aggregate mobility statistics.

### Contribution 2 (Scientific Representation of Urban Structure)
Develop a spatial representation framework that models Urban Structure as a Mobility Potential Field ($O_i, A_j$) using GeoAI and open urban data.

### Contribution 3 (Mechanism-based Probabilistic Integration Framework)
Establish a mechanism-based probabilistic integration framework that combines independently inferred Structure and Behaviour within a unified probabilistic spatial interaction model. The methodological novelty lies in integrating independently inferred Structure and Behaviour within a unified probabilistic spatial interaction framework.

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
*Status: Updated V2.1 — Post Quick Tests 1–19 Validation Reference Standard for PhD Proposal & Dissertation.*
