# METHOD BLUEPRINT V3.0

## Overall Strategy: Probabilistic Parameter Identification

The Method section presents a **probabilistic parameter-identification framework** rather than an OD prediction pipeline.

The central objective is to demonstrate that latent distance-deterrence parameters can be statistically identified from aggregate travel-distance observations.

OD prediction is presented only as the downstream consequence used to validate the identified parameters.

### Narrative Flow

Observation
→ Aggregate representation
→ Probabilistic observation model
→ Likelihood
→ Parameter identification
→ Gravity calibration
→ Independent production estimation
→ Independent attraction estimation
→ OD generation
→ Theoretical properties
→ Experimental predictions

---

# 3. Problem Formulation

### Objective

Formulate the problem as statistical parameter identification under limited observations.

### Key Message

Rather than estimating OD flows directly, this study formulates gravity calibration as the problem of identifying latent distance-deterrence parameters from aggregate travel-distance observations.

The identified parameters are subsequently used to calibrate a gravity model for downstream OD estimation.

### Objectives

Primary

Identify latent distance-deterrence parameters θ.

Secondary

Generate OD flows using the identified parameters.

---

# 4.1 Gravity Model Foundation

### Objective

Introduce the separable structure of gravity models.

### Logic

Origin production
↓

Destination attraction
↓

Distance deterrence
↓

Spatial interaction

### Key Message

Distance-deterrence parameters define the probability structure governing spatial interaction and therefore constitute the principal quantities to be identified.

---

# 4.2 Observation Model

### Objective

Formalize aggregate travel-distance distributions as statistical observations.

### Logic

OD interactions
↓

Observation operator

↓

Aggregate travel-distance distribution

↓

Statistical representation

### Key Message

Aggregate travel-distance distributions are treated as an observation layer induced by the underlying spatial interaction process.

---

# 4.3 Probabilistic Observation Model

### Objective

Derive the probability model linking latent parameters to aggregate observations.

### Logic

Gravity model
↓

Predicted trip-length probabilities
↓

Multinomial observation model

### Key Message

The aggregate observations induce a multinomial likelihood over travel-distance bins.

---

# 4.4 Parameter Identification

### Objective

Identify latent distance-deterrence parameters through maximum likelihood estimation.

### Logic

Observed histogram
↓

Likelihood

↓

MLE

↓

Cross-entropy optimization

### Key Message

Cross-entropy minimization is exactly the maximum likelihood estimator induced by the multinomial observation model.

The normalization of histogram counts changes only a positive scaling constant and therefore preserves the optimizer.

---

# 4.5 Origin Production

### Objective

Estimate origin production independently of distance-deterrence identification.

### Key Message

Origin production is estimated separately using machine learning and is not involved in identifying distance-deterrence parameters.

---

# 4.6 Destination Attraction

### Objective

Estimate destination attractiveness independently.

### Key Message

Destination attraction is specified separately from parameter identification to preserve the decomposed structure of the gravity model.

---

# 4.7 Gravity Calibration and OD Generation

### Objective

Combine independently estimated components.

### Logic

Identified parameters
+

Origin production
+

Destination attraction

↓

Gravity model

↓

OD estimation

### Key Message

OD prediction serves as the downstream predictive consequence of successful parameter identification rather than the primary methodological objective.

---

# 4.8 Theoretical Properties

### Property 1 — Statistical Identifiability

Latent distance-deterrence parameters can be identified from aggregate travel-distance distributions.

### Property 2 — Observation Efficiency

Complete OD interactions are unnecessary for parameter identification.

### Property 3 — Decomposability

Distance deterrence, production, and attraction are estimated independently.

### Property 4 — Transferability

The identified parameters enable survey-free gravity calibration in unseen cities.

---

# Transition to Experiments

The empirical evaluation tests the three predictions derived from the central hypothesis.

### Prediction 1

Aggregate observations induce a statistically valid likelihood for parameter identification.

### Prediction 2

Parameters identified from aggregate observations are statistically consistent with OD-based calibration.

### Prediction 3

The identified parameters preserve the downstream predictive consequences of the gravity model.