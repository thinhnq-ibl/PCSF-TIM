# Abstract Blueprint V3.0

## Block 1. Background
**Objective:** Establish the importance of OD flow estimation in transportation science.

**Logic:**
Spatial interaction → OD flows → Transportation → Accessibility → Urban decision-making

**Template:**
> Accurate origin–destination (OD) flow estimation is fundamental to transportation planning, accessibility analysis, infrastructure assessment, and urban decision-making.

---

## Block 2. Knowledge Gap
**Objective:** Define the unresolved scientific question.

**Logic:**
Distance-deterrence governs spatial interaction → Requires calibration → Current calibration relies on observed OD interactions → Aggregate mobility is increasingly available → Unknown whether aggregate observations preserve sufficient information

**Template:**
> Gravity-model calibration requires identifying city-specific distance-deterrence parameters from observed OD interactions. Although privacy-preserving aggregate mobility data are increasingly available, it remains unknown whether aggregate travel-distance distributions preserve sufficient statistical information for parameter identification without observing OD interactions.

---

## Block 3. Objective
**Objective:** State the scientific objective.

**Template:**
> This study investigates whether latent distance-deterrence parameters can be identified directly from aggregate travel-distance distributions without observed OD interactions.

---

## Block 4. Method
**Objective:** Briefly summarize the methodological workflow.

**Logic:**
Aggregate mobility observation → Observation model → Likelihood → Parameter inference → Gravity calibration → OD estimation

**Template:**
> Aggregate movement-distance observations are obtained from Meta Movement Distribution Maps and linked to an explicit observation model within a multinomial likelihood framework to infer latent distance-deterrence parameters. OD-derived trip-length distributions are used as the controlled benchmark representation, and the recovered parameters are subsequently used to calibrate a gravity model for OD estimation.

---

## Block 5. Results
**Objective:** Summarize both validation and empirical findings.

**Logic:**
Parameter consistency → Gravity calibration → OD prediction

**Template:**
> The inferred parameters closely match locally calibrated references and produce statistically comparable OD prediction performance across multiple metropolitan areas without requiring target-city OD observations.

---

## Block 6. Scientific Discovery
**Objective:** State the primary scientific finding.

**Template:**
> The findings demonstrate that aggregate travel-distance distributions preserve sufficient statistical information to identify latent city-specific distance-deterrence parameters.

---

## Block 7. Contribution
**Objective:** Present the methodological and practical implication derived from the discovery.

**Template:**
> Building on this finding, the proposed probabilistic calibration framework enables transferable and privacy-preserving gravity-model calibration for data-scarce cities using only aggregate mobility observations.