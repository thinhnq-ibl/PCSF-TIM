# PhD Proposal (Frozen V1.1)

## Title

**Learning Human Mobility from Aggregate Observations: Identification of Spatial Interaction Behaviour and Transferable Urban Structure for OD Matrix Reconstruction**

---

# 1. Motivation

* Mobility information is fundamental for transportation planning.
* Many rapidly urbanizing cities lack updated OD matrices.
* Household travel surveys are expensive and infrequent.
* Publicly available aggregate data are increasingly accessible.

This motivates the reconstruction of OD matrices from aggregate observations.

---

# 2. Research Gap

Existing studies either

* rely on interpretable gravity-type models with simplified assumptions,

or

* rely on deep learning models requiring abundant mobility observations.

Neither provides a unified framework that independently models

* Urban Structure

and

* Behaviour of Spatial Interaction.

---

# 3. Scientific Principle

## Structure–Behaviour Separation Principle

Human mobility is represented as

$$T_{ij} = O_i A_j f(d_{ij}; \theta)$$

where

### Urban Structure

$$(O_i, A_j)$$

describes the spatial distribution of trip production and attraction.

### Behaviour of Spatial Interaction

$$f(d; \theta)$$

describes the collective behavioural mechanism governing how spatial interaction changes with travel distance.

These two components should be inferred independently.

---

# 4. Central Scientific Proposition

> **Human mobility in data-scarce cities can be reconstructed by independently inferring the Behaviour of Spatial Interaction and Urban Structure from publicly available aggregate information, and integrating them through a gravity-based spatial interaction model.**

Đây là **mệnh đề khoa học trung tâm** của toàn bộ luận án.

Nó **không phải định lý toán học**.

Nó sẽ được kiểm chứng thông qua các bằng chứng tích lũy từ hai nghiên cứu.

---

# 5. Research Questions

### RQ1

Can the Behaviour of Spatial Interaction be statistically inferred from aggregate travel-distance distributions?

---

### RQ2

Under what conditions can Urban Structure be transferred between cities?

---

### RQ3

Can identified Behaviour and transferred Structure jointly reconstruct realistic OD matrices?

---

# 6. Research Framework

```text
Scientific Principle
        │
        ▼
Central Scientific Proposition
        │
 ┌──────┴──────┐
 │             │
 ▼             ▼
Paper 1     Paper 2
Behaviour   Structure
Inference   Transfer
 │             │
 └──────┬──────┘
        ▼
Gravity-based Integration
        ▼
OD Reconstruction
        ▼
Case Study
Ho Chi Minh City
```

---

# 7. Paper 1

## Identification of the Behaviour of Spatial Interaction from Aggregate Travel-distance Distributions

### Scientific Question

Can the Behaviour of Spatial Interaction be statistically identified from aggregate travel-distance observations?

### Contribution

* Define Behaviour of Spatial Interaction.
* Develop probabilistic observation model.
* Derive likelihood.
* Estimate $\theta$.
* Quantify uncertainty.

### Evidence provided

Supports the proposition that

> Behaviour can be independently inferred from aggregate observations.

---

# 8. Paper 2

## Transferable Urban Structure for OD Matrix Reconstruction

### Scientific Question

Can Urban Structure be transferred between similar cities?

### Contribution

* Define transferable Urban Structure.
* Identify transferability conditions.
* Estimate $(O_i, A_j)$.
* Reconstruct OD matrix.

### Evidence provided

Supports the proposition that

> Urban Structure can be independently estimated using publicly available urban information.

---

# 9. Integration

The outputs of the two papers are integrated through

$$T_{ij} = O_i A_j f(d_{ij}; \theta)$$

to reconstruct complete OD matrices.

This integration constitutes the primary methodological contribution of the dissertation.

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

Establish the **Structure–Behaviour Separation Principle** for human mobility reconstruction.

---

## Contribution 2

Develop a statistical inference framework for identifying the Behaviour of Spatial Interaction from aggregate observations.

---

## Contribution 3

Develop a transferable framework for estimating Urban Structure.

---

## Contribution 4

Propose a unified mobility reconstruction framework that integrates independently inferred Behaviour and Structure.

---

## Contribution 5

Demonstrate the framework through the reconstruction of the Ho Chi Minh City OD matrix.

---

# Synthesized Logic of the Proposal

Cấu trúc PhD Proposal này vận hành theo **4 tầng logic phương pháp luận**:

1. **Scientific Principle**
   * Structure–Behaviour Separation ($T_{ij} = O_i A_j f(d_{ij}; \theta)$).
   $$\Downarrow$$
2. **Central Scientific Proposition**
   * Mobility in data-scarce cities can be reconstructed by separately inferring these two components from open aggregate data.
   $$\Downarrow$$
3. **Empirical & Methodological Evidence**
   * **Paper 1:** Cung cấp bằng chứng thực nghiệm và suy luận thống kê cho thành phần **Behaviour** ($\theta$).
   * **Paper 2:** Cung cấp bằng chứng học chuyển giao cho thành phần **Structure** ($(O_i, A_j)$).
   $$\Downarrow$$
4. **Demonstration**
   * **Ho Chi Minh City:** Đóng vai trò là **Case Study thực tiễn** để kiểm chứng toàn bộ unified framework.

---
*Status: Frozen V1.1 — Reference Standard for PhD Dissertation Alignment.*
