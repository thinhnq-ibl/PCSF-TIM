# APPENDIX BLUEPRINT V3.0

## Overall Strategy: Supporting Scientific Evidence

The Appendix is not a repository for supplementary figures.

It systematically supports the central scientific argument:

> **Aggregate travel-distance distributions preserve sufficient statistical information to identify latent distance-deterrence parameters without observing origin–destination interactions.**

### Narrative Flow

Statistical Identifiability Evidence

↓

Methodological Validation

↓

Reproducibility

↓

Mathematical Foundations

---

# Appendix A. Statistical Identifiability Evidence

### Objective

Provide additional evidence that latent distance-deterrence parameters are genuinely identified from aggregate observations rather than merely fitted for OD prediction.

---

## A1. Parameter Identification across Cities

Recovered parameter trajectories across all metropolitan areas.

---

## A2. City-wise Parameter Estimates

Detailed identification statistics for every city.

---

## A3. Representative Case Studies

Detailed analyses of representative metropolitan areas with different urban morphologies.

---

## A4. Parameter Consistency

Agreement between aggregate-identified parameters and OD-calibrated references.

Focus on parameter agreement rather than downstream prediction.

---

## A5. Aggregate Representation Resolution

Sensitivity to different histogram resolutions and aggregate representations.

---

## A6. Cross-City Identification Stability

Distribution of recovered parameters across all cities.

---

# Appendix B. Methodological Validation

### Objective

Explain why the probabilistic parameter-identification framework works.

---

## B1. Full Factorial Ablation

Contribution of each methodological component.

---

## B2. Complete Shapley Analysis

Component attribution results.

---

## B3. Feature Importance

Origin-production feature ranking.

---

## B4. Feature Sensitivity

Performance versus feature dimensionality.

---

## B5. Observation Exposure Correction

Demonstrate why exposure correction is necessary for unbiased parameter identification.

---

## B6. Adaptive Self-loop Parameter

Validation of adaptive δ.

---

## B7. Attraction Modeling

Additional analyses for destination-attraction estimation.

---

# Appendix C. Reproducibility

### Objective

Provide sufficient implementation details for full reproducibility.

---

## C1. Overall Pipeline

---

## C2. Datasets

---

## C3. Hyperparameters

---

## C4. Optimization

---

## C5. Runtime

---

## C6. Hardware

---

## C7. Random Seeds

---

## C8. Data Splits

---

## C9. Code Availability

---

## C10. Computational Complexity

Empirical runtime and scalability.

---

# Appendix D. Mathematical Foundations

### Objective

Provide complete theoretical derivations supporting the probabilistic formulation.

---

## D1. Observation Operator

Derivation of aggregate travel-distance observations from OD interactions.

---

## D2. Probabilistic Observation Model

Derivation of the multinomial observation model.

---

## D3. Likelihood Derivation

Complete derivation of the multinomial log-likelihood.

---

## D4. Cross-Entropy Equivalence

Proof that cross-entropy optimization is exactly maximum likelihood estimation under normalized observations.

---

## D5. Observation Exposure Correction

Derivation of exposure normalization.

---

## D6. Statistical Identifiability Discussion

Discussion of why aggregate observations retain sufficient information for parameter identification.

---

## D7. Computational Complexity

Theoretical complexity analysis.

---

# Appendix E. Extended Discussion (Optional)

### Objective

Present broader conceptual discussions beyond the main manuscript.

---

## E1. Why Tanner?

Justification for the chosen deterrence function.

---

## E2. Why Aggregate Travel-Distance Distributions?

Why this representation preserves statistical information.

---

## E3. Observation versus Reconstruction

Why parameter identification differs fundamentally from flow reconstruction.

---

## E4. Observation-Centered Spatial Interaction Modeling

Relationship to physics-informed models, probabilistic inference, and modern AI methods.

---

# Final Review Checklist

Each appendix section should answer at least one of the following:

✓ Does this strengthen statistical identifiability?

✓ Does this explain why the probabilistic formulation is valid?

✓ Does this improve reproducibility?

✓ Does this strengthen the theoretical foundations?

If not, the material is likely supplementary implementation detail that can be removed.