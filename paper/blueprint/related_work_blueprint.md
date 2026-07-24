# RELATED WORK BLUEPRINT V3.0

## Overall Strategy: Literature Argument

The Related Work should develop a single scientific argument rather than a survey of mobility models.

The central question is:

> **Can latent distance-deterrence parameters be identified without observing origin–destination interactions?**

The literature review progressively narrows toward this question through the following logic:

Observation
→ Statistical representation
→ Parameter identification
→ Gravity calibration
→ Spatial interaction prediction

The review should explain why the current limitation is fundamentally an **observation problem**, rather than merely a modeling problem.

---

# 2.1 Spatial Interaction Modeling under Limited Observations

### Objective

Introduce the importance of gravity-model calibration and the dependence of existing approaches on observed mobility interactions.

### Logic

Spatial interaction
→ Gravity models
→ Parameter calibration
→ Requires observed OD interactions
→ Observation limitation

### Key Message

Current spatial interaction models differ substantially in formulation, but almost all identify distance-deterrence parameters from observed OD interactions or trajectory data.

---

# 2.2 Distance-Deterrence Parameter Identification

### Objective

Explain why distance-deterrence parameters are the key identifiable quantities governing spatial interaction.

### Logic

Spatial interaction
→ Distance deterrence
→ Latent parameter
→ Statistical identification

### Key Message

Distance-deterrence parameters summarize how interaction probability changes with separation distance. Identifying these parameters is therefore a prerequisite for gravity-model calibration.

---

# 2.3 Aggregate Mobility as a Statistical Representation

### Objective

Review aggregate mobility from the perspective of statistical representation rather than privacy.

### Logic

Aggregate observations
→ Compressed representation
→ Statistical information
→ Potential identifiability

### Key Message

Aggregate travel-distance distributions discard OD identities but preserve distributional information describing collective travel behavior. Whether this representation retains sufficient information for parameter identification remains largely unexplored.

---

# 2.4 Survey-Free Mobility Modeling

### Objective

Review zero-shot and transferable mobility models.

### Logic

Transfer learning
→ Flow reconstruction
→ Dependence on learned OD behavior
→ Remaining limitation

### Key Message

Recent transferable models (DeepGravity, neuroGravity, TransGM, etc.) reduce data requirements but continue to assume that behavioral parameters are learned from observed mobility data before transfer. None directly identify distance-deterrence parameters from aggregate observations alone.

---

# 2.5 Research Gap: From Observation to Parameter Identification

### Objective

Define the scientific gap motivating this paper.

### Logic

Observed OD interactions
→ Aggregate observations
→ Unknown statistical sufficiency
→ Parameter identification
→ Proposed formulation

### Key Message

Existing research has focused primarily on predicting flows from increasingly limited observations. A more fundamental question remains unresolved:

Can aggregate travel-distance distributions themselves provide sufficient statistical information for identifying latent distance-deterrence parameters?

This paper addresses that question by formulating gravity calibration as a probabilistic parameter-identification problem under aggregate observations.

---

# Review Criteria

Each paragraph should satisfy all of the following:

1. Does it clarify the observation problem?

2. Does it explain what information is required for parameter identification?

3. Does it narrow the literature toward the scientific question of identifiability?

4. Does removing the paragraph weaken the argument that aggregate observations may be statistically sufficient?

If not, the paragraph is likely discussing generic OD prediction rather than supporting the central scientific narrative.