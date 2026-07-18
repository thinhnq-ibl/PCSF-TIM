# ABSTRACT BLUEPRINT V2.0

## Structural Design

### Block 1. Background
**Objective**: Answer why understanding and modeling spatial interaction is important. Establish the broad context.
**Constraint**: Exclude discussions of aggregate mobility, gravity models, distance-decay, or the paper's specific contribution.
**Logical Flow**:
`Spatial interaction $\to$ OD flows $\to$ Transportation $\to$ Accessibility $\to$ Urban planning`

*Template:*
> Accurate origin–destination (OD) flow estimation is fundamental to transportation planning, accessibility analysis, and urban management.

### Block 2. Research Gap
**Objective**: Define the core knowledge gap. Show that while distance-decay calibration is necessary, current methods rely on observed OD matrices, leaving it unknown whether aggregate data can suffice.
**Logical Flow**:
`Gravity models need distance-decay calibration $\to$ Calibration requires observed OD $\to$ Aggregate mobility exists $\to$ Unknown if aggregate mobility can recover $\beta$`

*Template:*
> Existing gravity-model calibration approaches rely on observed OD matrices or individual mobility trajectories, leaving it unclear whether aggregate mobility data preserve sufficient information to recover the latent city-specific distance-decay parameter governing spatial interactions.

### Block 3. Objective
**Objective**: Explicitly state the hypothesis investigation.
**Constraint**: Do not state that the goal is simply OD estimation. Focus on the recovery of the latent parameter.

*Template:*
> This study investigates whether aggregate mobility data can recover the latent city-specific distance-decay parameter required for gravity-model calibration without observed OD matrices.

### Block 4. Method
**Objective**: Outline the technical workflow.
**Logical Flow**:
`Aggregate mobility $\to$ Trip-length distribution $\to$ Recover $\beta$ $\to$ Calibrate gravity $\to$ Estimate OD $\to$ Evaluate`

*Template:*
> Trip-length distributions are derived from Meta Movement Distribution Maps. The latent distance-decay parameter is recovered and used to calibrate a gravity model. The calibrated model is then applied to estimate OD flows across cities.

### Block 5. Experiment
**Objective**: Describe how the hypothesis is tested. Focus on validating the recovered parameter $\beta$ against locally calibrated models.
**Logical Flow**:
`Recover $\beta$ $\to$ Validate $\beta$ $\to$ Compare calibration`

*Template:*
> The recovered distance-decay parameter and the resulting gravity model are evaluated against locally calibrated references across multiple metropolitan areas.

### Block 6. Results
**Objective**: Summarize the empirical findings. Emphasize that the recovered behavior matches the reference, leading to successful OD generation.
**Logical Flow**:
`Recovered $\beta$ matches reference $\to$ Gravity works $\to$ OD works`

*Template:*
> The recovered distance-decay parameters closely match locally calibrated references and enable statistically comparable OD prediction performance relative to conventional calibration approaches.

### Block 7. Scientific Insight
**Objective**: State the primary scientific discovery.
**Constraint**: Focus on the fundamental property of aggregate mobility, not the framework itself.

*Template:*
> The results indicate that aggregate mobility data preserve sufficient information to recover latent city-specific distance-decay parameters without requiring observed OD matrices.

### Block 8. Contribution
**Objective**: Conclude with the methodological and practical application derived from the scientific insight.

*Template:*
> Building on this insight, this work introduces a zero-shot gravity-model calibration framework that enables transferable OD estimation for cities lacking observed OD matrices, with privacy-preserving aggregate mobility serving as a practical and scalable data source.
