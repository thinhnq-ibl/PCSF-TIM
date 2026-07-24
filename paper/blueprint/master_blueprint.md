# MAIN BLUEPRINT V3.0

## Title

Recovering Latent Distance-Deterrence Parameters from Aggregate Travel-Distance Distributions for Survey-Free Spatial Interaction Modeling

---

# I. CENTRAL SCIENTIFIC QUESTION

> **Can latent distance-deterrence parameters be identified directly from aggregate travel-distance distributions without observing origin–destination interactions?**

*Observed OD matrices are used only as an empirical reference for validation rather than as an input to parameter identification.*

---

# II. CENTRAL HYPOTHESIS

```text
Aggregate travel-distance distributions
            │
            ▼
preserve sufficient statistical information
to identify latent distance-deterrence parameters
            │
            ▼
Recovered parameters preserve the predictive
behavior of gravity models
            │
            ▼
Survey-free gravity calibration becomes feasible.
```

---

# III. THREE PREDICTIONS

### Prediction 1 — Statistical Identifiability

Aggregate travel-distance observations induce a statistically valid likelihood for identifying latent distance-deterrence parameters.

**Flow**

Aggregate observations
→ Observation model
→ Likelihood
→ Parameter identification

---

### Prediction 2 — Parameter Consistency

Parameters identified from aggregate travel-distance distributions are statistically consistent with those calibrated from complete OD interactions.

**Flow**

Aggregate observations
→ Identified parameters
→ OD-calibrated parameters
→ Statistical consistency

---

### Prediction 3 — Predictive Equivalence

Parameters identified from aggregate observations preserve the predictive consequences of the underlying gravity model.

**Flow**

Recovered parameters
→ Gravity calibration
→ OD prediction
→ Predictive equivalence

---

# IV. CONTRIBUTIONS

## Layer 1 — Scientific Discovery (Core Contribution)

Aggregate travel-distance distributions preserve sufficient statistical information to identify latent city-specific distance-deterrence parameters without observing OD interactions.

---

## Layer 2 — Methodological Contribution

A probabilistic parameter-identification framework is established to infer latent distance-deterrence parameters directly from aggregate travel-distance observations.

---

## Layer 3 — Practical Contribution

The resulting calibration framework enables transferable, survey-free, and privacy-preserving gravity-model calibration for cities lacking observed OD matrices.

---

# V. STORYLINE OF THE PAPER

### Step 1. Background

Accurate OD flows are fundamental for transportation planning, accessibility analysis, and urban decision-making.

↓

### Step 2. Observation Challenge

Gravity models require distance-deterrence parameters, which are traditionally calibrated from observed OD interactions.

↓

### Step 3. Knowledge Gap

Aggregate travel-distance distributions are increasingly available, but it remains unknown whether they preserve sufficient statistical information for parameter identification.

↓

### Step 4. Scientific Hypothesis

Aggregate travel-distance distributions preserve sufficient statistical information to identify latent distance-deterrence parameters.

↓

### Step 5. Method

Derive a probabilistic observation model and infer latent distance-deterrence parameters from aggregate travel-distance distributions.

↓

### Step 6. Validation

Evaluate whether the inferred parameters

- match OD-calibrated parameters; and
- preserve downstream gravity-model predictions.

↓

### Step 7. Scientific Insight

Aggregate travel-distance distributions preserve the essential statistical information governing distance-deterrence behavior, enabling survey-free gravity-model calibration without observing OD interactions.