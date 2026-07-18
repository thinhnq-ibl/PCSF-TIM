# RELATED WORK BLUEPRINT V2.0

## Overall Strategy: Literature Argument
The Related Work section must function as a cohesive *Literature Argument*, not merely a categorical review. Every subsection must serve the central question: **Can latent behavior be recovered?**

The logical axis is:
`Behavioral inference (distance-decay recovery) $\to$ gravity calibration $\to$ transferable OD estimation`

### Narrative Flow
1. Behavior governs mobility.
2. Behavior is represented by distance-decay.
3. Existing studies learn behavior from observed mobility.
4. Aggregate mobility may preserve behavior.
5. Can behavior be recovered instead of learned? $\to$ Yes (Our approach).

---

## Section Guidelines

### 2.1 Mobility Modeling under Limited Behavioral Information
**Objective**: Establish the need for behavioral observations, not just OD matrices.
**Logic**: 
`Need mobility prediction $\to$ Need behavioral information $\to$ Behavior usually comes from OD $\to$ OD is scarce`
**Constraint**: Shift the problem framing from "we lack OD" to "we lack behavioral observations".

### 2.2 Distance-Decay as Behavioral Representation
**Objective**: Position the distance-decay parameter ($\beta$) as the core behavioral mechanism.
**Logic**: 
`Behavior $\to$ Distance-decay $\to$ Behavior parameter $\beta$`
**Key Insight**: Distance-decay parameters provide a compact behavioral representation of how travelers balance travel cost against destination attractiveness. Thus, recovering $\beta$ means recovering behavior.

### 2.3 Information Preservation in Aggregate Mobility
**Objective**: Argue that aggregate mobility preserves statistical information, rather than just highlighting its privacy benefits.
**Logic**: 
`Aggregate mobility $\to$ Information preservation`
**Constraint**: Focus on the specific statistical signatures preserved in aggregate data that are necessary for behavioral recovery. Privacy is a secondary motivation.

### 2.4 Behavior Transfer in Zero-Shot Prediction
**Objective**: Review existing zero-shot prediction methods (e.g., DeepGravity, NeuroGravity, TransGM) by demonstrating their common assumption.
**Logic**: 
`Methods learn/transfer behavior $\to$ Behavior comes from OD`
**Constraint**: Highlight that all current state-of-the-art models assume behavior must first be learned from an observed OD matrix before it can be transferred.

### 2.5 The Research Gap: From Learning to Inference
**Objective**: Identify the critical knowledge gap and introduce the paper's formulation as the solution.
**Logic**: 
`Existing studies $\to$ Behavior is learned $\to$ Never inferred $\to$ Behavior recovery $\to$ Behavior inference $\to$ Our framework`
**Key Insight**: If aggregate mobility preserves the statistical signature of distance-dependent travel behavior, behavioral model calibration can be reformulated as an inverse behavioral inference problem rather than a conventional flow reconstruction problem.
**Constraint**: Introduce the Projection-Inference Gravity Framework (PIGF) as a logical consequence of this discovery, not prematurely as the primary novelty.

---

## Review Criteria for Revisions
Every paragraph in the Related Work must answer "Yes" to the following:
1. Does this clarify "behavior"?
2. Does this advance the argument toward the question "Can behavior be recovered?"
3. If this paragraph is removed, does the central hypothesis weaken?
*(If the answer is "No", the content is likely focused on generic OD prediction and should be revised or removed).*
