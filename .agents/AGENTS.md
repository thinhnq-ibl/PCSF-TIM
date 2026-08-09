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

### Multi-Tiered Evidence Bundle Architecture
Evidence for parameter identification under Hypothesis 1 must be presented as a multi-tiered evidence bundle:

1. **Likelihood surface & optimization stability**
   - Well-defined optimum and sharp likelihood surface (QT12: Multi-start $\text{CV} = 0.00\%$).
   - Direct evidence for estimator stability.

2. **Synthetic parameter recovery**
   - Generate TLD from known parameters and recover parameters accurately from synthetic TLD.
   - Primary direct evidence for parameter identifiability under the assumed generative model.

3. **Cross-city empirical reference consistency**
   - Independently estimate parameters for multiple cities (50 US metropolitan areas) and compare against OD-calibrated reference parameters ($R^2 = 0.9624$).
   - Measures external empirical reference agreement/consistency, NOT sole proof of formal statistical sufficiency by itself.

4. **Observation noise robustness**
   - Assess parameter estimation stability under observation noise perturbation (QT18: $<0.5\%$ error under $20\%$ noise).

5. **Downstream reconstruction adequacy**
   - Inferred parameters support downstream OD matrix reconstruction (TOST equivalence under oracle outflows).
   - Serves as downstream consequence validation, **not** as direct proof of parameter identifiability.

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
  - ❌ *"Causal chain: Learning Objective $\to$ Strategy $\to$ Representation $\to$ Generalization"*

- **Required Phrasing:**
  - ✅ *"Urban Structure + Travel Behaviour $\longrightarrow$ Spatial Interaction"* (Conceptual Ontology)
  - ✅ *"$R_S + R_B \longrightarrow \text{Spatial Interaction Process} \longrightarrow T_{ij}$"* (Core Operational Integration)
  - ✅ *"$T_{ij} = O_i A_j f(d_{ij}; \boldsymbol{\theta})$"* (Mathematical Gravity Integration)
  - ✅ *"Methodological chain: Learning Objective $\to$ Learning Strategy $\to$ Representation $\to$ Encoded Information $\to$ Generalization"*

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
Do NOT state that "Urban Structure is transferable" as an a priori assumption or established fact. Literature shows that some neural models generalize cross-regionally under specific conditions, but this does NOT prove that a scientifically defined Urban Structure Representation ($R_S$) is universally transferable. Transferability of $R_S$ is a **testable empirical hypothesis ($H_2$) evaluated in Paper 2 under explicit source–target conditions ($CPC = f(\text{structural similarity})$)**.

### Phrasing Matrix
- **Forbidden Phrasing:**
  - ❌ *"Urban Structure is transferable."*
  - ❌ *"Structural representation $R_S$ is inherently transferable."*
  - ❌ *"Urban Structure representations evolve into transferable potential fields."*

- **Required Phrasing:**
  - ✅ *"Paper 2 tests whether an Urban Structure Representation ($R_S$), learned from observable open spatial features, can transfer across cities and under what source–target conditions such transfer remains valid without relying on target-city OD labels."*
  - ✅ *"Structure transferability is an empirical hypothesis. Existing literature demonstrates cross-city generalization of several neural mobility models and representations, but does not establish that a scientifically defined Urban Structure Representation ($R_S$) is universally transferable. Paper 2 therefore tests the transferability of $R_S$ under explicit source–target conditions."*

## Rule: Identification Sufficiency vs Formal Statistical Sufficiency

### Context
Do NOT describe TLD as a "formal sufficient statistic" (in the Fisher–Neyman factorization sense) for full OD data or as a universal theorem for behaviour. Always scope "sufficient statistical information" by adding **under the specified spatial-interaction model and observation process**.

### Phrasing Matrix
- **Forbidden Phrasing:**
  - ❌ *"TLD is a sufficient statistic for travel behaviour."*
  - ❌ *"TLD is universally sufficient for parameter identification."*

- **Required Phrasing:**
  - ✅ *"Aggregate travel-distance distributions contain sufficient statistical information to identify city-specific distance-deterrence parameters under the specified spatial-interaction model."*
  - ✅ *"Identification Sufficiency: An aggregate mobility observation is considered sufficient for parameter identification when, under a specified probabilistic spatial-interaction model, it contains enough statistical information to identify the target parameter."*

## Rule: Scoping Shapley Value Attribution Claims (85.8% Predictive Gain)

### Context
Do NOT describe the 85.8% Shapley attribution result as "Behaviour accounts for 85.8% of human mobility" or as proof of "Behaviour ontologically dominating Structure". Shapley value analysis measures relative predictive contribution within a specific 3-component coalition experiment over a uniform-flow baseline.

### Phrasing Matrix
- **Forbidden Phrasing:**
  - ❌ *"Distance-decay behaviour accounts for 85.8% of total mobility."*
  - ❌ *"Travel Behaviour is responsible for 85.8% of mobility flow."*
  - ❌ *"Behaviour ontologically dominates Urban Structure by 85.8%."*

- **Required Phrasing:**
  - ✅ *"Within the evaluated spatial-interaction decomposition, distance deterrence accounts for 85.8% of the total CPC gain over the uniform-flow baseline."*
  - ✅ *"Shapley value attribution demonstrates that distance deterrence is the dominant predictive component among the three evaluated components in the tested spatial-interaction decomposition."*

## Rule: Oracle Equivalence vs. Survey-Free Deployment Scope

### Context
Do NOT claim that the fully survey-free OD reconstruction pipeline is "statistically equivalent to locally-calibrated Tanner gravity". TOST statistical equivalence ($\text{CPC} = 0.7337 \approx 0.7382$, $p = 0.00326$) holds strictly under **oracle outflow control** (true $O_i$). Fully survey-free deployment achieves $\text{CPC} = 0.6860$.

### Phrasing Matrix
- **Forbidden Phrasing:**
  - ❌ *"The proposed aggregate-calibrated model is statistically equivalent to locally-calibrated Tanner."*
  - ❌ *"Survey-free OD reconstruction achieves statistical equivalence with local OD calibration."*

- **Required Phrasing:**
  - ✅ *"Under oracle outflow control, the aggregate-calibrated distance-deterrence model achieves statistical equivalence to locally calibrated Tanner gravity within a pre-specified 0.01 CPC margin."*
  - ✅ *"In the fully survey-free deployment setting, the proposed model achieves CPC = 0.6860, demonstrating downstream reconstruction feasibility while leaving a performance gap relative to locally calibrated Tanner gravity (CPC = 0.7382)."*

## Rule: DeepGravity & Zero-Shot Neural Baselines Phrasing

### Context
Do NOT claim that "DeepGravity requires target-city OD data for inference" or that "deep learning cannot perform zero-shot flow prediction". DeepGravity is trained on source mobility flows and generates target flows without target-city OD matrices (achieving $\text{CPC} = 0.7529$). The thesis gap is NOT the inability to perform zero-shot prediction, but the **lack of explicit scientific decomposition into a transferable structural representation ($R_S$) and an independently identified behavioural representation ($R_B$)**.

### Phrasing Matrix
- **Forbidden Phrasing:**
  - ❌ *"DeepGravity requires historical target OD matrices for inference."*
  - ❌ *"Deep-learning approaches cannot perform zero-shot flow prediction."*
  - ❌ *"DeepGravity conflates Urban Structure and Travel Behaviour."*
  - ❌ *"DeepGravity is the proposed scientific representation $R_S$."*

- **Required Phrasing:**
  - ✅ *"DeepGravity is trained on observed mobility flows from source regions but generates flows for target regions without target-city OD observations, serving as a strong zero-shot neural baseline."*
  - ✅ *"Existing transfer models generally learn predictive representations that jointly encode structural and behavioural information, without explicitly defining these components as separate scientific representations."*
  - ✅ *"DeepGravity achieves higher predictive accuracy ($\text{CPC} = 0.7529$), whereas the proposed framework prioritizes explicit behavioural identification, structural decomposition ($R_S \neq R_B$), and lower-dimensional structural inputs (6 features vs. 27 features)."*
  - ✅ *"DeepGravity and other end-to-end mobility prediction models serve as comparative neural transfer baselines unless their learned representations are explicitly interpreted and independently validated as a scientific structural representation ($R_S^*$). A task-specific neural embedding ($Z_{\text{task}}$) is not $R_S$ by default."*

## Rule: Empirical Motivation vs. Architectural Necessity (Tabular Ceiling R^2 <= 0.48)

### Context
Do NOT claim that "tabular models hit a hard theoretical capacity ceiling ($R^2 \le 0.48$) that mandates GNN" or that "GNN is a necessary scientific architecture". The empirical baseline result ($R^2 \approx 0.48$) motivates the investigation of spatial representation learning, while graph-based learning (Spatial GNNs) is adopted as a candidate mechanism for learning $R_S$, NOT as a theoretical necessity or a scientific object itself.

### Phrasing Matrix
- **Forbidden Phrasing:**
  - ❌ *"Tabular models hit a hard capacity ceiling, mandating a GNN."*
  - ❌ *"GNN is mathematically necessary for learning Urban Structure."*
  - ❌ *"Urban Structure Representation is identical to a GNN embedding."*
  - ❌ *"R^2 <= 0.48 proves the information capacity ceiling of Urban Structure Representation."*

- **Required Phrasing:**
  - ✅ *"The limited performance of the evaluated non-spatial tabular baselines ($R^2 \approx 0.48$) motivates the investigation of spatial representation learning for Urban Structure."*
  - ✅ *"A graph-based architecture is adopted as a candidate mechanism for learning a transferable $R_S$, rather than being treated as a theoretical necessity or uniquely valid architecture."*
  - ✅ *"Operational prediction performance ($R^2 \le 0.48$) reflects baseline model limitations for the selected quantities $(O_i, A_j)$, not direct proof of $R_S$ scientific validity."*

## Rule: ANOVA Variance Decomposition & Separation Principle Scope

### Context
Do NOT claim that "Two-Way ANOVA proves / establishes the Structure–Behaviour Separation Principle as a universal law of nature" or that "Urban Structure is 81.3% important while Behaviour is only 5.3% important". ANOVA ($\eta^2_S = 81.27\%, \eta^2_B = 5.28\%$) measures relative variance contribution under a cross-matrix factor perturbation experiment, providing empirical support for the analytical usefulness of the proposed decomposition, NOT a metaphysical statement about nature.

### Phrasing Matrix
- **Forbidden Phrasing:**
  - ❌ *"ANOVA proves the Structure–Behaviour Separation Principle."*
  - ❌ *"Urban Structure is intrinsically 81.3% more important than Travel Behaviour."*
  - ❌ *"Behaviour is only 5.3% important in human mobility."*

- **Required Phrasing:**
  - ✅ *"Develop and empirically support the Structure–Behaviour Separation Principle as an analytical framework for decomposing spatial interaction into structural and behavioural representations."*
  - ✅ *"QT16 ANOVA provides empirical support for this decomposition by showing distinguishable variance contributions from structural ($\eta^2 = 81.27\%$) and behavioural ($\eta^2 = 5.28\%$) factors under the evaluated cross-city reconstruction experiment."*

## Rule: Privacy Nuance & Scoped Motivation Phrasing

### Context
Do NOT describe aggregate mobility products (such as TLDs or Meta MDM) as "inherently privacy-safe / privacy-preserving guarantees" or equate spatial aggregation with formal Differential Privacy ($\epsilon$-DP). Aggregation reduces observational disclosure granularity, but privacy guarantees depend on the specific release mechanism. Privacy is a practical motivation/constraint, NOT the scientific contribution of Paper 1.

### Phrasing Matrix
- **Forbidden Phrasing:**
  - ❌ *"TLD is a privacy-safe observation layer."*
  - ❌ *"Spatial aggregation guarantees differential privacy."*
  - ❌ *"Paper 1 develops a privacy-preserving reconstruction method."*

- **Required Phrasing:**
  - ✅ *"Aggregate mobility observations reduce the granularity of disclosed movement information by removing individual-level and pairwise spatial identities. Their privacy properties, however, depend on the aggregation and data-release mechanism and should not be equated automatically with formal privacy guarantees."*
  - ✅ *"Resolving these gaps enables mobility reconstruction in data-scarce cities using survey-free aggregate observational inputs that can reduce exposure to individual-level mobility information, subject to the privacy properties of the underlying data-release mechanism."*

## Rule: Decoupled Complementary Inference Pathways (Paper 1 & Paper 2 Parallel Architecture)

### Context
Do NOT claim that "Paper 2 must succeed before Paper 1 can be valid" or that "Paper 1 is sequentially dependent on Paper 2's structure transferability". Paper 1 identifies Travel Behaviour ($R_B$) from aggregate TLDs under a specified structural condition ($R_S$), while Paper 2 independently tests whether $R_S$ can be learned and transferred across cities. They are **complementary parallel tasks unified at the joint integration stage ($R_S + R_B \longrightarrow T_{ij}$)**.

### Phrasing Matrix
- **Forbidden Phrasing:**
  - ❌ *"Paper 2's transferability establishes the prerequisite condition for Paper 1."*
  - ❌ *"If Paper 2 transfers structure, then Paper 1 can identify behaviour."*
  - ❌ *"Paper 1 relies on Paper 2 to validate its structural inputs."*

- **Required Phrasing:**
  - ✅ *"Behavioural Identification (Gap I) and Urban Structure Transferability (Gap II) are complementary scientific problems unified by the Structure–Behaviour Separation Principle."*
  - ✅ *"The two papers jointly test whether Spatial Interaction can be decomposed into a transferable Urban Structure Representation ($R_S$) and a locally identifiable Travel Behaviour Representation ($R_B$). Each component is evaluated through its own inference pathway before their joint integration is assessed."*

## Rule: Zero-Target-OD vs. Target-Data-Free Positioning

### Context
Do NOT describe the framework as "target-data-free", "data-free", or "zero-shot for the entire pipeline". The framework requires target-city open spatial features ($X_S$) and target-city aggregate TLD ($D_{\text{target}}$). What the framework explicitly avoids are **disaggregated target-city origin-destination flow matrices ($T_{ij, \text{target}}^{\text{obs}}$)**. Always lock the scientific scope to **`Zero-Target-OD`**.

### Phrasing Matrix
- **Forbidden Phrasing:**
  - ❌ *"Reconstruct mobility without any target-city mobility data."*
  - ❌ *"Target-data-free flow prediction framework."*
  - ❌ *"Zero-shot mobility reconstruction without local observation."*

- **Required Phrasing:**
  - ✅ *"The framework is zero-target-OD rather than target-data-free: target-city reconstruction uses open structural features ($X_S$) and an aggregate travel-distance distribution ($D_{\text{target}}$) to infer the local Behaviour Representation ($R_B$), while explicitly avoiding disaggregated target-city OD observations."*
  - ✅ *"OD-free target-city reconstruction using aggregate mobility observations and open spatial features."*

## Rule: Paper 1 Novelty & Gap 1 Positioning (Full TLD Probabilistic Identification)

### Context
Do NOT claim that "no previous method calibrates gravity models from aggregate data" or that Paper 1 is the "first to perform aggregate gravity calibration". Prior literature has demonstrated calibration from OD data or compressed summary statistics (Tanner 1961, Hyman 1969, Merlin 2020 median-based estimator). Paper 1's novelty lies in treating the **full aggregate travel-distance distribution (the complete empirical histogram)** as a probabilistic observation layer, deriving an explicit **multinomial likelihood function $Y \sim \text{Multinomial}(N, \boldsymbol{p}(\boldsymbol{\theta}))$**, and empirically demonstrating city-specific parameter identification with strong agreement to OD-calibrated reference parameters.

### Phrasing Matrix
- **Forbidden Phrasing:**
  - ❌ *"No existing method calibrates gravity models from aggregate mobility statistics."*
  - ❌ *"First to calibrate gravity models without complete origin-destination matrices."*
  - ❌ *"Lack of any likelihood inference formulation for aggregate mobility data."*

- **Required Phrasing:**
  - ✅ *"Gap 1 (Behaviour Identification): Existing studies demonstrate calibration from OD data and, in some cases, from compressed summary statistics (such as mean or median travel time), but it remains insufficiently established whether a full aggregate travel-distance distribution can be formulated as a probabilistic observation model supporting city-specific parameter identification and agreement with OD-based reference estimates."*
  - ✅ *"The novelty of Paper 1 lies not in the general idea that gravity parameters can be calibrated without complete OD matrices, as prior work has demonstrated calibration from compressed summary statistics. Rather, the novelty lies in treating the full aggregate travel-distance distribution as a probabilistic observation layer, formulating an explicit multinomial observation likelihood, and empirically demonstrating city-specific parameter identification with strong agreement to OD-based reference estimates."*

## Rule: Epistemic Boundary of Model Integration (Joint OD Fit != Causal/Mechanistic Proof)

### Context
Do NOT claim that "fitting an integrated gravity model ($\hat{T}_{ij} \approx T_{ij}^{\text{obs}}$) proves the true underlying causal mechanisms of human mobility" or that RQ3 establishes "causal explanation". The framework is an **analytical/compositional framework**. OD matrix reconstruction evaluates the **explanatory and predictive adequacy of the proposed mechanism-oriented decomposition under the specified model**, NOT causal truth in reality.

### Phrasing Matrix
- **Forbidden Phrasing:**
  - ❌ *"OD reconstruction proves the underlying causal mechanism of human mobility."*
  - ❌ *"RQ3 provides a causal explanation of why Spatial Interaction occurs."*
  - ❌ *"Establishes the true physical mechanism governing urban travel."*

- **Required Phrasing:**
  - ✅ *"Can the probabilistic integration of the inferred Travel Behaviour representation and the learned Urban Structure representation provide an adequate mechanism-based account of observed Spatial Interaction under the specified model?"*
  - ✅ *"Develop a mechanism-oriented probabilistic integration framework... Its empirical role is to evaluate whether their joint integration provides adequate explanatory and predictive performance under the specified model, rather than establishing causal mechanisms."*
  - ✅ *"The dissertation evaluates the adequacy of a proposed mechanism-oriented decomposition under a specified model, not causal truth."*

















