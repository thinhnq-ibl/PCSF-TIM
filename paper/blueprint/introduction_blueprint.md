# INTRODUCTION BLUEPRINT V3.0

## Overall Strategy: From Observation to Parameter Identification

The Introduction should build a single scientific narrative rather than introducing a new framework.

The central scientific question is:

> **Can latent distance-deterrence parameters be identified directly from aggregate travel-distance distributions without observing origin–destination interactions?**

The Introduction progressively narrows from the general importance of spatial interaction modeling to this specific question.

### Narrative Flow

Spatial interaction

↓

Gravity-model calibration

↓

Dependence on observed OD interactions

↓

Aggregate observations become available

↓

Unknown statistical sufficiency

↓

Scientific hypothesis

↓

Three predictions

↓

Scientific contributions

---

# 1.1 Background

### Objective

Establish why origin–destination (OD) estimation and gravity-model calibration are fundamental in transportation science.

### Logic

Spatial interaction

↓

OD flows

↓

Transportation planning

↓

Accessibility

↓

Urban decision-making

### Key Message

Accurate spatial interaction modeling is essential for transportation planning, accessibility analysis, infrastructure design, and urban policy.

Gravity models remain one of the most widely used approaches because they provide an interpretable probabilistic description of human mobility.

---

# 1.2 Observation Challenge

### Objective

Explain why gravity-model calibration remains difficult.

### Logic

Gravity model

↓

Distance-deterrence parameter

↓

Requires calibration

↓

Requires observed OD interactions

↓

OD data are difficult to obtain

### Key Message

The predictive performance of gravity models depends critically on identifying city-specific distance-deterrence parameters.

Conventional calibration requires observed OD matrices or individual mobility trajectories, both of which are expensive, incomplete, or privacy-sensitive.

---

# 1.3 Opportunity from Aggregate Mobility

### Objective

Introduce aggregate travel-distance distributions as an alternative observation.

### Logic

Aggregate mobility products

↓

Privacy-preserving

↓

Widely available

↓

Compressed observations

↓

Potential statistical information

### Key Message

Recent aggregate mobility products provide population-level travel-distance distributions without revealing individual trajectories or OD identities.

These observations are increasingly available at large geographic scales.

---

# 1.4 Knowledge Gap

### Objective

Define the unresolved scientific question.

### Logic

Observed OD interactions

↓

Aggregate travel-distance distributions

↓

Unknown statistical sufficiency

↓

Unknown parameter identifiability

### Key Message

Although aggregate travel-distance distributions summarize collective travel behavior, it remains unknown whether they preserve sufficient statistical information to identify latent distance-deterrence parameters without observing OD interactions.

This is the central knowledge gap addressed in this study.

---

# 1.5 Central Hypothesis

### Objective

State the scientific hypothesis.

### Hypothesis

Aggregate travel-distance distributions preserve sufficient statistical information to identify latent city-specific distance-deterrence parameters.

The identified parameters should be statistically consistent with those obtained from complete OD observations and preserve the predictive consequences of gravity-model calibration.

---

# 1.6 Three Predictions

## Prediction 1 — Statistical Identifiability

Aggregate travel-distance observations induce a statistically valid likelihood for identifying latent distance-deterrence parameters.

---

## Prediction 2 — Parameter Consistency

Parameters identified from aggregate observations are statistically consistent with those calibrated from complete OD interactions.

---

## Prediction 3 — Predictive Consequence

The identified parameters preserve the downstream predictive behavior of gravity-model calibration.

---

# 1.7 Contributions

## Contribution 1 — Scientific Discovery

This study demonstrates that aggregate travel-distance distributions preserve sufficient statistical information to identify latent distance-deterrence parameters without observing origin–destination interactions.

---

## Contribution 2 — Methodological Contribution

A probabilistic parameter-identification framework is developed to infer latent distance-deterrence parameters directly from aggregate travel-distance observations and integrate them into gravity-model calibration.

---

## Contribution 3 — Practical Contribution

The resulting framework enables transferable, survey-free, and privacy-preserving gravity-model calibration for cities lacking observed OD matrices.

---

# 1.8 Paper Organization

Briefly summarize the organization of the manuscript.

- Section 2 reviews related work on spatial interaction modeling, parameter calibration, aggregate mobility representations, and transferable mobility prediction.

- Section 3 formulates gravity calibration as a probabilistic parameter-identification problem under aggregate observations.

- Section 4 presents the proposed probabilistic framework.

- Section 5 experimentally evaluates the three predictions derived from the central hypothesis.

- Section 6 discusses the broader scientific implications, limitations, and future research directions.

- Section 7 concludes the paper.

---

# Final Review Checklist

The Introduction should satisfy the following progression:

✓ Why are gravity models important?

↓

✓ Why is calibration difficult?

↓

✓ Why are aggregate observations interesting?

↓

✓ What remains scientifically unknown?

↓

✓ What hypothesis is proposed?

↓

✓ What predictions follow?

↓

✓ What evidence will the paper provide?

↓

✓ What are the scientific contributions?

---

## One-Sentence Narrative

> **This paper investigates whether aggregate travel-distance distributions preserve sufficient statistical information to identify latent distance-deterrence parameters without observing origin–destination interactions, and demonstrates that these identified parameters enable survey-free gravity-model calibration with predictive performance comparable to conventional OD-based calibration.**