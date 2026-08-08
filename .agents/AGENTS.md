# Project-Scoped Agent Rules

## Rule: Evaluate Whether Meta Movement Distribution Maps (MDM) Citation Should Be Added

### Objective
Evaluate whether the manuscript would benefit from explicitly citing the official **Meta AI for Good – Movement Distribution Maps (MDM)** dataset. The goal is to improve the logical connection between the motivation for aggregate mobility data, the proposed methodology, and the real-world dataset used in the experiments without inflating reference count.

### When to Recommend Adding the Citation
Recommend adding the official Meta MDM citation **only if all of the following are true**:
1. The manuscript later uses Meta Movement Distribution Maps as a real dataset.
2. The Introduction discusses the increasing availability of aggregate mobility products.
3. The Introduction does not explicitly mention Meta MDM.
4. Adding Meta MDM would strengthen the narrative from motivation → methodology → evaluation.

### Preferred Location
Prefer adding the citation in the Introduction, near statements such as *"aggregate mobility products are becoming increasingly available..."* rather than introducing Meta MDM for the first time in the Data section.

### Recommended Revision Example
Replace:
> "Aggregate mobility products are becoming increasingly available across platforms and regions..."
With:
> "Aggregate mobility products—including Meta's Movement Distribution Maps (MDM) \citep{MetaMovementDistributionMaps}—are becoming increasingly available across platforms and regions, providing privacy-preserving summaries of population travel behavior."

### Do NOT Recommend the Citation If
- The paper never uses Meta MDM.
- Meta MDM is only mentioned as an implementation detail.
- The citation would merely increase reference count without strengthening the argument.
- Another citation already supports exactly the same claim.

### Review Principle
- Prioritize citations that strengthen the scientific narrative.
- Avoid adding citations solely because a dataset exists.
- Every added citation should clearly improve one of: motivation, research gap, methodological justification, or experimental reproducibility.

## Rule: Evidence for Parameter Identification

### Context
The paper does **not** claim mathematical identifiability. Instead, it builds **empirical statistical evidence** that aggregate travel-length distributions (TLDs) contain sufficient information to support identification of the parameters governing collective distance-sensitive travel behaviour.

### Evidence Components
Evidence should consist of four complementary components:

1. **Likelihood evidence**
   - Well-defined optimum.
   - Sharp and stable likelihood surface.

2. **Synthetic recovery**
   - Generate TLD from known parameters.
   - Recover parameters accurately from the generated TLD.

3. **Cross-city consistency**
   - Independently estimate parameters for multiple cities.
   - Results are stable and consistent across cities.

4. **Downstream validation**
   - Parameters inferred from TLD enable accurate OD reconstruction.
   - OD reconstruction serves as validation of the inferred parameters, **not** as proof of identifiability.

### Writing principle
Always use evidence-oriented language:
- provide statistical evidence
- support identification
- support the hypothesis
- indicate
- suggest
- are consistent with

Avoid:
- prove
- mathematically prove
- uniquely determine
- recover human mobility behaviour
- demonstrate identifiability

## Rule: AI Latent Representation Rule

### Context
A task-specific AI latent representation $Z_{\text{task}}$ is a learned model representation, not a scientific object. It must not be identified with Urban Structure Representation $R_S$ merely because it is learned from geographic data or improves mobility-flow prediction. Such identification requires an explicit structural interpretation and independent validation.

### Writing & Phrasing Principle
- **Avoid (Forbidden):**
  - ❌ *"The GNN learns Urban Structure."*
  - ❌ *"The AI model identifies Urban Structure directly."*
  - ❌ *"Latent vector $Z$ is Urban Structure."*

- **Use (Required):**
  - ✅ *"The GNN learns a task-specific latent representation ($Z_{\text{task}}$) from observable urban features."*
  - ✅ *"We investigate whether this representation can support a scientifically meaningful Urban Structure Representation $R_S$."*

## Rule: Human Mobility & Spatial Interaction Ontology Rule

### Context
Do NOT define the conceptual ontology of Human Mobility using a direct multiplication product sign (e.g. ❌ $\text{Human Mobility} = \text{Urban Structure Representation} \times \text{Collective Behaviour}$). The gravity equation $T_{ij} = O_i A_j f(d_{ij}; \boldsymbol{\theta})$ serves strictly as the mathematical integration framework for flow reconstruction, not as the definition of the scientific object itself.

### Writing & Phrasing Principle
- **Avoid (Forbidden):**
  - ❌ *"Human Mobility = Urban Structure Representation × Collective Behaviour"*
  - ❌ *"Human Mobility is the product of Structure and Behaviour"*

- **Use (Required):**
  - ✅ *"Urban Structure + Travel Behaviour $\longrightarrow$ Spatial Interaction"* (Conceptual Ontology)
  - ✅ *"$R_S + R_B \longrightarrow \text{Spatial Interaction Process} \longrightarrow T_{ij}$"* (Operational Integration)
  - ✅ *"$T_{ij} = O_i A_j f(d_{ij}; \boldsymbol{\theta})$"* (Mathematical Integration Model)

## Rule: Analytical vs. Causal Phrasing Rule

### Context
This thesis proposes an **analytical/compositional framework** ($R_S + R_B \longrightarrow T_{ij}$), NOT a causal inference model. Avoid using causal phrasing that suggests a unidirectional causal relationship (e.g. ❌ $\text{Structure} \longrightarrow \text{Behaviour} \longrightarrow \text{OD}$) or absolute statistical independence (❌ $\text{Structure} \perp \text{Behaviour}$).

### Phrasing Matrix
- **Forbidden Phrasing:**
  - ❌ *"Structure causes Travel Behaviour"* ($\text{Structure} \longrightarrow \text{Behaviour} \longrightarrow \text{OD}$)
  - ❌ *"Behaviour determines Urban Structure"* ($\text{Behaviour} \longrightarrow \text{Structure} \longrightarrow \text{OD}$)
  - ❌ *"Structure and Behaviour are statistically independent"* ($\text{Structure} \perp \text{Behaviour}$)

- **Required Phrasing:**
  - ✅ *"Urban Structure + Travel Behaviour $\longrightarrow$ Spatial Interaction"* (Conceptual Ontology)
  - ✅ *"$R_S + R_B \longrightarrow \text{Spatial Interaction Process} \longrightarrow T_{ij}$"* (Core Operational Integration)
  - ✅ *"$T_{ij} = O_i A_j f(d_{ij}; \boldsymbol{\theta})$"* (Mathematical Gravity Integration)

## Rule: Structural Representation vs. Operational Quantities Rule

### Context
Do NOT conflate Urban Structure Representation $R_S$ solely with the two operational scalar quantities $(O_i, A_j)$. $R_S$ is a multi-dimensional structural opportunity field, while $(O_i, A_j)$ are operational quantities projected from $R_S$ for spatial interaction model execution: $\text{Urban Structure } \mathcal{S} \longrightarrow R_S \longrightarrow (O_i, A_j, \dots)$.

### Writing & Phrasing Principle
- **Avoid (Forbidden):**
  - ❌ *"Urban Structure Representation is $(O_i, A_j)$"*
  - ❌ *"R_S equals origin production and destination attraction"*

- **Use (Required):**
  - ✅ *"Urban Structure Representation $R_S$ is operationalized through structural quantities $(O_i, A_j)$ in spatial interaction models."*
  - ✅ *"$R_S \longrightarrow (O_i, A_j, \dots)$"*

## Rule: Avoid "Intrinsic / Inherent Property" Phrasing for Travel Behaviour

### Context
Do NOT describe local travel behaviour or parameter $\boldsymbol{\theta}$ as an "intrinsic local city property" or "inherently untransferable". Local parameter inference of $\boldsymbol{\theta}$ is a conservative **modelling principle and strategic design choice** to account for city-specific distance-sensitivity profiles, NOT a metaphysical claim of intrinsic essentialism.

### Phrasing Matrix
- **Forbidden Phrasing:**
  - ❌ *"$\boldsymbol{\theta}$ is an intrinsic local city property"*
  - ❌ *"Travel behaviour is inherently untransferable"*
  - ❌ *"Local behaviour is an intrinsic invariant"*

- **Required Phrasing:**
  - ✅ *"City-specific Travel Behaviour is represented operationally via $R_B(d; \boldsymbol{\theta})$, where $\boldsymbol{\theta}$ is locally inferred."*
  - ✅ *"Local inference of $R_B$ is a modelling principle to respect city-specific friction profiles and prevent cross-domain behavioural bias."*

## Rule: Structural Transferability as a Testable Hypothesis Rule

### Context
Do NOT state that "Urban Structure is transferable" as an a priori assumption. The transferability of structural representation $R_S$ is a **testable empirical hypothesis** evaluated in Paper 2, not a predefined fact.

### Phrasing Matrix
- **Forbidden Phrasing:**
  - ❌ *"Urban Structure is transferable."*
  - ❌ *"Structural representation $R_S$ is inherently transferable."*

- **Required Phrasing:**
  - ✅ *"Paper 2 tests the hypothesis that structural representations ($R_S$) learned from open spatial features can be transferred across heterogeneous urban domains."*
  - ✅ *"Structure transferability is an empirical hypothesis to be evaluated, while target-city Behaviour is locally inferred."*






