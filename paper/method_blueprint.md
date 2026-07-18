# METHOD BLUEPRINT V2.0

## Overall Strategy: Behavioral Inference
The Method section (Section 4) must be framed as a **Behavioral Inference Framework** rather than just a "survey-free OD prediction methodology". The core narrative is that we are proving behavioral parameters (distance-decay) can be statistically identified from aggregate data. OD prediction is the downstream consequence.

### Narrative Flow
`Problem (Recover latent β) $\to$ Why β is identifiable $\to$ Projection theory $\to$ Inverse inference $\to$ Recover β $\to$ Independent estimation of production $\to$ Independent estimation of attraction $\to$ Recover gravity model $\to$ Generate OD $\to$ Behavioral properties $\to$ Hypotheses`

---

## Section Guidelines

### 3. Problem Formulation
**Objective**: Define the problem as inverse parameter inference.
**Constraint**: Do not frame the problem primarily as OD estimation.

*Template:*
> This study formulates survey-free gravity calibration as the problem of recovering the latent city-specific distance-decay parameter from aggregate mobility observations. Once recovered, the parameter is integrated into a gravity model to estimate origin–destination flows.

**Objective Functions**:
- **Primary Objective**: Recover latent $\theta$ ($\beta$).
- **Secondary Objective**: Estimate $T$ (OD matrix).

### 4.1 Gravity Foundation
**Objective**: Emphasize the separable structure of the gravity model.
**Logic**: 
- **Origin** = Demand generation
- **Attraction** = Opportunity distribution
- **Distance decay** = Behavior
**Key Insight**: Distance-decay $\beta$ is not merely a calibration parameter; it is the mathematical representation of traveler behavior.

### 4.2 Projection Theory
**Objective**: Explain the theoretical link between full OD matrices and aggregate distributions.
**Logic**: 
`OD matrix $\to$ Projection $\to$ Trip-length distribution $\to$ Behavior signature $\to$ Recover β`

### 4.3 Distance-Decay Formulation (Tanner Function)
**Objective**: Describe the chosen functional form.

### 4.4 Exposure Correction & Inverse Inference
**Objective**: Present the core methodological novelty.
**Logic**: 
`Observed histogram $\to$ Projection $\to$ Exposure correction $\to$ Recover latent behavior`
**Constraint**: Explicitly use the term "latent behavioral inference". The section details how behavior is statistically identified from structural spatial exposure.

### 4.5 Origin Production
**Objective**: Describe the machine learning pipeline for production estimation.
**Key Insight**: Emphasize that production (demand) is estimated completely independently from behavioral decay. 

### 4.6 Destination Attraction
**Objective**: Describe the heuristic for attraction estimation.

### 4.7 Survey-Free OD Flow Generation
**Objective**: Describe the final synthesis.
**Logic**: 
`Recovered behavior $\to$ Recovered gravity model $\to$ Generate OD`
**Constraint**: Present OD generation strictly as a downstream consequence of the successful behavioral recovery.

### 4.8 Properties of the Framework
**Objective**: List the theoretical advantages of the proposed PIGF framework.
1. **Behavioral Identifiability**: (Most critical property) The framework proves that distance-decay parameters can be statistically identified from aggregate trip-length distributions without full OD flow observations.
2. **Survey-Free Calibration**
3. **Component-wise Inference**
4. **Transferability**

### Closing Remarks / Empirical Hypotheses
**Objective**: Transition to the experiments by outlining the three core hypotheses to be tested.

*Hypotheses Flow:*
- **H1 (Recoverability)**: Aggregate mobility $\to$ Recover $\beta$
- **H2 (Dominance)**: Recovered $\beta$ $\to$ Replaces conventional OD calibration
- **H3 (Utility)**: Recovered gravity model $\to$ Competitive zero-shot OD prediction
