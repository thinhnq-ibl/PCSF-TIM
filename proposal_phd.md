# PhD Proposal (Frozen V1.1)

## Title

**Learning Human Mobility from Aggregate Observations: Identification of Spatial Interaction Behaviour and Transferable Urban Structure for OD Matrix Reconstruction**

---

# 1. Motivation & Vision

* Mobility data are a dynamic input to economic analysis, transportation planning, and public health applications.
* Modern cities have become increasingly observable through multi-source open spatial data (OSM, POIs, Sentinel/Landsat) and geospatial representation learning.
* Aggregate mobility products—including Meta's Movement Distribution Maps (MDM)—are becoming increasingly available across platforms and regions, providing privacy-preserving summaries of population travel behavior.
* However, a structural tension persists in current data availability: while spatial structural data are abundant, high-resolution origin-destination (OD) mobility matrices remain unavailable or heavily restricted due to privacy constraints.
* Many rapidly urbanizing cities lack updated OD matrices, as traditional household travel surveys are costly and infrequent.

This motivates the generative reconstruction of fine-grained OD matrices from publicly available aggregate mobility observations and open urban structure representations.

### Research Vision

> **Rather than treating urban mobility as a black-box phenomenon, this dissertation decomposes mobility into interpretable structural and behavioural components, enabling quantitative diagnosis, policy evaluation, and mechanism-based interpretation of urban mobility systems.**

---

# 2. Research Gap

Existing studies either

* rely on interpretable gravity-type models with simplified structural assumptions or unverified parameters,

or

* rely on deep learning models (e.g., DeepGravity) requiring dense mobility observations while blending spatial features and distance decay into opaque neural layers.

Crucially, existing literature conflates **Spatial Opportunity Density** with **Distance Decay**. Neither paradigm provides a unified framework that independently models components according to their fundamentally distinct functional roles:

1. **Urban Structure** (where spatial opportunities exist), and
2. **Behaviour of Spatial Interaction** (how willingness/sensitivity attenuates over distance to utilize those opportunities).

---

# 3. Scientific Principle

## Structure–Behaviour Separation Principle

Human mobility is represented as a production-constrained spatial interaction process:

$$T_{ij} = O_i \frac{A_j f(d_{ij}; \boldsymbol{\theta})}{\sum_{m} A_m f(d_{im}; \boldsymbol{\theta})}$$

Urban Structure and Behaviour play complementary rather than equivalent roles in spatial interaction. Urban Structure defines the distribution of mobility opportunities through origin production and destination attraction potentials, whereas Behaviour determines how travellers utilize those opportunities by trading off travel opportunities against distance cost. Consequently, observed mobility emerges from the interaction between an opportunity field and a collective distance-sensitivity mechanism.

where the two components perform **fundamentally distinct functional roles**:

### Urban Structure (Mobility Potential Field)

$$\boldsymbol{\Phi} = (\mathbf{O}, \mathbf{A})$$

describes the spatial distribution of **Production Potential ($O_i$)** (latent origin trip-emission capacity) and **Attraction Potential ($A_j$)** (latent destination opportunity density).

### Behaviour of Spatial Interaction

Defined as the **collective distance sensitivity governing the utilization of spatial opportunities**.

$$f(d; \boldsymbol{\theta})$$

describes the collective behavioural mechanism governing how travellers select among available spatial opportunities over travel distance. Distance decay vector $\boldsymbol{\theta}$ (e.g., Tanner deterrence parameters $\alpha, \beta$) serves as the **mathematical proxy/representation** of this Behaviour.

These two components must be inferred independently.

---

# 4. Central Scientific Proposition

> **Human mobility in data-scarce cities can be reconstructed by independently inferring the Behaviour of Spatial Interaction and the Mobility Potential Field of Urban Structure from publicly available aggregate information, and integrating them through a gravity-based spatial interaction model.**

Đây là **mệnh đề khoa học trung tâm** của toàn bộ luận án.

Nó **không phải định lý toán học**.

Nó sẽ được kiểm chứng thông qua các bằng chứng tích lũy từ hai nghiên cứu.

---

# 5. Research Questions

### RQ1

Can the Behaviour of Spatial Interaction be statistically identified from aggregate travel-distance distributions?

---

### RQ2

How can the Urban Mobility Potential Field be effectively represented from open spatial data and evaluated across heterogeneous urban environments?

---

### RQ3

Can identified Behaviour and represented Structure potential fields jointly reconstruct realistic OD matrices?

---

# 6. Research Framework

```text
Scientific Principle (Structure–Behaviour Separation)
        │
        ▼
Central Scientific Proposition
        │
 ┌──────┴──────┐
 │             │
 ▼             ▼
Paper 1     Paper 2
Behaviour   Potential Field
Identification  Representation
 │             │
 └──────┬──────┘
        ▼
Gravity Interaction (Behaviour Acting on Structure)
        ▼
OD Reconstruction
        ▼
Case Study: Ho Chi Minh City
```

---

# 7. Paper 1

## Identification of the Behaviour of Spatial Interaction from Aggregate Travel-Distance Distributions

### Scientific Objective

Identify the **Behaviour of Spatial Interaction** (collective distance sensitivity governing opportunity utilization) from aggregate travel-distance observations.
*(Note: Parameter vector $\boldsymbol{\theta}$ is the mathematical proxy of Behaviour, not the ultimate scientific goal).*

### Contribution

* Operationally define Behaviour of Spatial Interaction.
* Develop a binned probabilistic observation model under information loss.
* Derive exact conditional likelihood.
* Support statistical identification of distance sensitivity parameters $\boldsymbol{\theta}$.
* Quantify inference uncertainty across diverse city topologies.

### Evidence provided

Supports the proposition that

> Behaviour can be independently identified from aggregate travel-distance observations without requiring pairwise OD labels.

---

# 8. Paper 2

## Representation of Urban Mobility Potential Field for OD Matrix Reconstruction

### Scientific Objective

Learn and represent the **Urban Mobility Potential Field** ($\mathbf{O}, \mathbf{A}$) from multi-source open urban spatial data.
*(Note: Spatial transferability across cities serves as an evaluation diagnostic/benchmark to verify that the representation captures intrinsic urban structure rather than overfitting to a single city).*

### Contribution

* Formalize the Urban Mobility Potential Field consisting of Production Potential ($O_i$) and Attraction Potential ($A_j$).
* Develop GeoAI spatial representation models using open data (OSM, POIs, satellite imagery).
* Establish cross-city transferability evaluation benchmarks.
* Reconstruct zero-shot OD flow matrices.

### Evidence provided

Supports the proposition that

> The Mobility Potential Field of Urban Structure can be independently estimated and represented using publicly available urban information.

---

# 9. Integration

The outputs of the two papers are integrated through the production-constrained gravity formulation:

$$T_{ij} = O_i \frac{A_j f(d_{ij}; \boldsymbol{\theta})}{\sum_{m} A_m f(d_{im}; \boldsymbol{\theta})}$$

This interaction models **Behaviour acting on Structure to synthesize realized mobility flows**, constituting the primary methodological contribution of the dissertation.

---

# 10. Case Study

## Ho Chi Minh City

Ho Chi Minh City serves as the primary case study because

* updated OD matrices remain unavailable,
* planning demand is high,
* multiple public urban datasets are available.

The case study demonstrates the applicability of the proposed framework.

It is **not** the scientific contribution itself.

---

# 11. Expected Scientific Contributions

## Contribution 1

Establish the **Structure–Behaviour Separation Principle** with distinct functional roles for human mobility reconstruction.

---

## Contribution 2

Develop a statistical inference framework for identifying the Behaviour of Spatial Interaction from aggregate observations.

---

## Contribution 3

Develop a spatial representation framework for estimating the Urban Mobility Potential Field ($O_i, A_j$).

---

## Contribution 4

Propose a unified mobility reconstruction framework that models Behaviour acting on Structure.

---

## Contribution 5

Demonstrate the framework through the reconstruction of the Ho Chi Minh City OD matrix.

---

# Synthesized Logic of the Proposal

Cấu trúc PhD Proposal này vận hành theo **4 tầng logic phương pháp luận**:

1. **Scientific Principle**
   * Structure–Behaviour Separation with distinct functional roles ($T_{ij} = O_i \frac{A_j f(d_{ij}; \theta)}{\sum_m A_m f(d_{im}; \theta)}$).
   $$\Downarrow$$
2. **Central Scientific Proposition**
   * Mobility in data-scarce cities can be reconstructed by separately inferring Behaviour and Structure potential fields from open aggregate data.
   $$\Downarrow$$
3. **Empirical & Methodological Evidence**
   * **Paper 1:** Cung cấp bằng chứng thực nghiệm và suy luận thống kê cho thành phần **Behaviour Identification** ($\boldsymbol{\theta}$ là mathematical proxy).
   * **Paper 2:** Cung cấp giải pháp **Mobility Potential Field Representation** cho thành phần **Structure** ($(O_i, A_j)$) với đánh giá chuyển giao qua nhiều đô thị.
   $$\Downarrow$$
4. **Demonstration**
   * **Ho Chi Minh City:** Đóng vai trò là **Case Study thực tiễn** để kiểm chứng toàn bộ unified framework.

---
*Status: Updated V1.2 — Reference Standard for PhD Dissertation Alignment.*
