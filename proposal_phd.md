# PhD Dissertation Proposal (V3.0 — Refined 8-Module Framework)

## Title

**Learning Human Mobility from Aggregate Observations: Identification of Spatial Interaction Behaviour and Transferable Urban Structure for OD Matrix Reconstruction**

### Subtitle
*Towards Mechanism-based Human Mobility Science through Behaviour Identification and Urban Structure Representation*

---

> **Single Master Opening Statement:**
> **"This research aims to establish a mechanism-based scientific framework for Human Mobility by inferring a representation of city-specific Travel Behaviour from aggregate mobility observations and representing Urban Structure from observable urban features to evaluate cross-city transferability. The reconstructed OD matrix serves as empirical evidence that integrating these two distinct scientific components adequately explains observed Spatial Interaction flows."**

---

# 1. Motivation & Vision

Urban mobility is one of the most important collective phenomena in modern cities. Mobility data serve as a dynamic input to economic analysis, transportation planning, and public health policies.

Modern cities have become increasingly observable through multi-source open spatial data (OSM, POIs, Sentinel/Landsat) and geospatial representation learning. Furthermore, aggregate mobility products—including Meta's Movement Distribution Maps (MDM) \citep{MetaMovementDistributionMaps}—are becoming increasingly available across platforms and regions, providing privacy-preserving summaries of population travel behavior.

However, **current studies primarily model mobility as a prediction problem rather than a scientific phenomenon**. In doing so, they treat the phenomenon directly as an observable, bypassing the need to identify the latent mechanisms that generate it. Consequently, although OD matrices can be predicted via black-box machine learning models, **the underlying mechanisms governing Spatial Interaction remain poorly understood**.

### Research Vision

> **Rather than treating urban mobility as a black-box prediction problem, this dissertation adopts Spatial Interaction as its formal scientific object and establishes a mechanism-based framework founded on the distinct representation of Urban Structure and the inference of city-specific Travel Behaviour. This approach enables quantitative explanation, diagnosis, policy evaluation, and transferable understanding of urban mobility systems.**

---

# 2. Research Gap

Existing studies learn mobility directly from observations. As a consequence, **Urban Structure Representation and Travel Behaviour Representation remain entangled** within a single predictive function, preventing independent understanding, quantification, and transfer of their roles.

These limitations are not merely methodological but conceptual. Existing models jointly optimize Urban Structure and Travel Behaviour as a single predictive function, preventing either representation from being independently interpreted, transferred, or statistically identified. Consequently, the literature motivates a scientific decomposition of Spatial Interaction into two analytically distinguishable representations—Urban Structure and Travel Behaviour—rather than a new predictive architecture. The **Structure–Behaviour Decomposition Principle** therefore emerges as a necessary conceptual consequence of the limitations of the existing Observation-First paradigm, rather than an arbitrary modelling choice.

Neither the traditional gravity paradigm nor modern deep learning models (e.g., DeepGravity) provide a unified framework that independently models the two representations according to their fundamentally distinct functional roles:

1. **Urban Structure Representation** (encoding where spatial opportunities exist and how they are distributed), and
2. **Travel Behaviour Representation** (encoding how collective willingness to traverse distance governs opportunity utilization).

---

# 3. Structure–Behaviour Decomposition Principle

Spatial Interaction is represented as a production-constrained process where **Travel Behaviour acts on Urban Structure**:

$$T_{ij} = O_i \frac{A_j f(d_{ij}; \boldsymbol{\theta})}{\sum_{m} A_m f(d_{im}; \boldsymbol{\theta})}$$

> **Scientific Proposition (End of Module 3):**
> *Although Spatial Interaction emerges from the interaction between Urban Structure Representation and Travel Behaviour Representation, treating these representations as analytically distinguishable enables different scientific questions to be formulated, different learning objectives to be defined, and different learning strategies to be developed.*

This decomposition immediately suggests a research programme. If Urban Structure can be represented and transferred across cities, and a representation of city-specific Travel Behaviour can be statistically inferred from aggregate observations through distinct inference pathways, then their probabilistic interaction provides empirical evidence to reconstruct OD flows. The reconstructed OD matrix is therefore not the objective of the framework, but **empirical evidence** evaluating whether integrating these two distinct scientific components adequately explains observed Spatial Interaction.

Urban Structure and Travel Behaviour play complementary rather than equivalent roles. This research conceptualizes Urban Structure and city-specific Travel Behaviour as two distinct scientific components, each represented and inferred through different sources of information, and investigated through different transferability and inference strategies:

### Urban Structure and Its Representation

Urban Structure refers to the spatial organization of opportunities and constraints that shapes the potential landscape of spatial interaction. In this research, Urban Structure is not directly equated with any single observable dataset or model variable. Instead, it is represented through observable and inferred structural information, which is operationalized in the spatial interaction model through structural representations such as origin-side production $O_i$ and destination-side attraction $A_j$:

$$\text{Urban Structure} \longrightarrow R_S \longrightarrow (O_i, A_j)$$

where:
* **Urban Structure**: Scientific object (the spatial organization of opportunities and constraints).
* **$R_S$**: Urban Structure representation (e.g., Mobility Potential Field learned from multi-source spatial data).
* **$O_i, A_j$**: Operational structural quantities used by the spatial interaction model (origin-side production and destination-side attraction).

Because observable spatial characteristics can be systematically encoded using spatial representation learning, the resulting Urban Structure representation ($R_S$) provides a basis for testing cross-city structural transferability. Paper 2 therefore evaluates, rather than assumes, whether $R_S$ learned from source cities can generalize to unseen urban environments. This *observable → representable → testable-transferability* logic forms the scientific basis of Paper 2.

### City-Specific Travel Behaviour and Its Representation

City-specific Behaviour is conceptualized as the collective behavioural component governing how travellers respond to spatial separation and the spatial opportunities defined by Urban Structure. Behaviour is not directly observed. Instead, it is represented operationally in the spatial interaction model through a distance-deterrence function:

$$R_B(d; \boldsymbol{\theta}) = f(d; \boldsymbol{\theta})$$

$$\text{City-specific Behaviour} \longrightarrow R_B(d; \boldsymbol{\theta}) = f(d; \boldsymbol{\theta}) \longrightarrow \boldsymbol{\theta} = (\alpha, \beta)$$

where:
* **City-specific Behaviour**: Scientific object (the collective behavioural component governing how travellers respond to spatial separation and spatial opportunities).
* **$R_B(d; \boldsymbol{\theta}) = f(d; \boldsymbol{\theta})$**: Travel Behaviour representation (e.g., Tanner deterrence function operationalized in the spatial interaction model).
* **$\boldsymbol{\theta} = (\alpha, \beta)$**: Behavioural representation parameters (mathematical proxies estimated from aggregate mobility evidence).

For example, under the Tanner specification:

$$f(d; \alpha, \beta) = d^{-\alpha} e^{-\beta d}$$

where $(\alpha, \beta)$ parameterize the behavioural representation rather than being identified directly with Behaviour itself.

Because aggregate travel-distance distributions (TLD) preserve statistical signatures of travel friction, aggregate mobility observations provide empirical statistical evidence supporting the identification of behavioural representation parameters ($\boldsymbol{\theta}$) given a specified Urban Structure. This *aggregate-observable → statistical-evidence-supported identification* property forms the scientific basis of Paper 1.

### Distinction Between Scientific Representation and AI-Learned Embeddings

A critical epistemological contribution of this framework is distinguishing explicitly between three levels:

$$\text{Scientific Object} \longrightarrow \text{Scientific Representation } (R_S, R_B) \longrightarrow \text{AI-Learned Latent Representation } (Z_{\text{task}})$$

Specifically, for Urban Structure:

$$\text{Urban Structure} \longrightarrow R_S \longrightarrow \text{AI / GNN Model} \longrightarrow Z_{\text{task}}$$

* **Scientific Object (Urban Structure / Behaviour)**: Real-world physical spatial organization of opportunities and collective travel response.
* **Scientific Representation ($R_S, R_B$)**: Explicitly specified, interpretable structural quantities $(O_i, A_j)$ and deterrence function $f(d; \boldsymbol{\theta})$ operationalized in the Spatial Interaction model.
* **AI-Learned Latent Representation ($Z_{\text{task}}$)**: High-dimensional latent embeddings (e.g., GNN or DeepGravity hidden states) optimized for a specific downstream prediction task.

Crucially, **$Z_{\text{task}} \neq R_S$ or $R_B$ by default**. Standard black-box AI models (e.g., DeepGravity, Imagery2Flow) learn task-driven embeddings ($Z_{\text{task}}$) that entangle Urban Structure and Travel Behaviour into a single latent vector. However, a learned latent representation ($Z_{\text{task}}$) may be interpreted as supporting a scientific representation ($Z_{\text{task}} \approx R_S$) only when that interpretation is explicitly justified and validated—namely, when it is learned strictly from structural inputs ($X_S$) without target mobility contamination, demonstrates structural interpretability, preserves necessary opportunity information, and generalizes across structural domains. In contrast, Paper 2 does not merely aim to generate a "better neural embedding," but to learn an **explicit, interpretable structural representation ($R_S$)** whose cross-city transferability can be systematically evaluated.

### Epistemological Clarification on Model Residuals and Information Sufficiency

A fundamental methodological pitfall in mobility modelling is conflating unexplained model error (residuals) directly with human behaviour. In this research, model residuals are treated strictly as **unexplained variation**, not automatically as Travel Behaviour:

$$\text{OD} = f(R_S) + \underbrace{\epsilon}_{\text{unexplained variation}}$$

Crucially, unexplained variation ($\epsilon$) could stem from either an incomplete structural representation (e.g., missing spatial features in $R_S$) or distance-decay travel friction ($R_B$). Therefore, model error alone does not "prove" Behaviour; it merely **motivates the hypothesis** that a behavioural representation is required:

$$\text{Hypothesized Component of Residual: } \epsilon \approx R_B(d; \boldsymbol{\theta})$$

The core scientific test is evaluating whether integrating the explicit behavioural representation ($R_B$) with the structural representation ($R_S$) provides a superior explanation of spatial interaction:

$$R_S + R_B \longrightarrow \text{Superior Mechanism-based Explanation of Mobility}$$

Furthermore, testing structural sufficiency does not claim to disprove all possible physical structural configurations; it evaluates **only the sufficiency of the adopted representation** ($R_S$).

### Validation Philosophy: Three-Tier Empirical Evidence

In alignment with the epistemological separation of Structure and Behaviour, validation in this framework does not rely solely on downstream OD matrix reconstruction. Instead, validation is structured across three complementary evidence tiers:

$$\begin{aligned}
\text{Urban Structure} &\longrightarrow R_S \longrightarrow \text{(Structural Representation \& Transfer Evidence — Paper 2)} \\
\text{City-specific Behaviour} &\longrightarrow R_B \longrightarrow \text{(Behavioural Representation Identification Evidence — Paper 1)} \\
R_S + R_B &\longrightarrow \text{OD} \longrightarrow \text{(Downstream Joint Integration Evidence — Dissertation Framework)}
\end{aligned}$$

1. **Behavioural Representation Identification Evidence (Paper 1)**: Evaluated *prior* to flow reconstruction through likelihood surface stability, synthetic parameter recovery from generated TLDs under the assumed generative model, and cross-city parameter consistency.
2. **Structural Representation and Transfer Evidence (Paper 2)**: Evaluated *prior* to flow reconstruction through spatial encoding capacity limitations ($R^2 > 0.48$) and cross-city zero-shot transferability metrics ($\text{CPC}$, $\text{KL-divergence}$).
3. **Downstream Joint Integration Evidence (Dissertation Framework)**: OD matrix reconstruction serves as downstream evidence of the **joint integration** of $R_S$ and $R_B$, demonstrating joint explanatory and predictive capability rather than acting as singular proof of individual component correctness.

### Epistemological & Transferability Shift

| Dimension | Conventional Conflated Framing | Refined Decoupled Framing |
| :--- | :--- | :--- |
| **Urban Structure** | $\text{Urban Structure} = (O_i, A_j)$ | $\text{Urban Structure} \longrightarrow R_S \longrightarrow (O_i, A_j)$ |
| **Structural Quantities** | $(O_i, A_j)$ directly equals Structure | $(O_i, A_j)$ are operational structural quantities of $R_S$ |
| **AI Learning Target** | AI learns Urban Structure directly | AI learns task-specific latent representations ($Z_{\text{task}}$) from structural inputs |
| **Latent Embedding Role** | Latent embedding ($Z_{\text{task}}$) = Structure | $Z_{\text{task}} \neq R_S$ by default ($Z_{\text{task}}$ entangles Structure & Behaviour) |
| **Scientific vs AI Repr.** | Scientific representation = neural embedding | Scientific representation ($R_S$) $\neq$ Black-box neural embedding ($Z_{\text{task}}$) |
| **Paper 2 Objective** | Paper 2 = better neural embedding | Paper 2 = Explicit structural representation ($R_S$) + evaluate transferability |
| **Object Transferred** | Urban Structure is transferred | Urban Structure representation ($R_S$) is transferred |
| **Transfer Type** | Structural transfer | Transfer of structural representation ($R_S$) |
| **Travel Behaviour** | $\text{Behaviour} = f(d; \boldsymbol{\theta})$ | $\text{City-specific Behaviour} \longrightarrow R_B(d; \boldsymbol{\theta}) \longrightarrow \boldsymbol{\theta}$ |
| **Deterrence Function** | Distance decay function *is* Behaviour | Distance decay function *is a representation* ($R_B$) of Behaviour |
| **Behaviour Processing** | Behaviour is independently identified | Behaviour representation ($R_B$) is locally inferred |
| **Parameters ($\boldsymbol{\theta}$)** | $\boldsymbol{\theta}$ *is* Behaviour | $\boldsymbol{\theta}$ parameterizes the representation $R_B$ |
| **Inference Path** | $\text{TLD} \longrightarrow \text{Behaviour}$ | $\text{TLD} \longrightarrow \text{infer } R_B (\boldsymbol{\theta}) \longrightarrow \text{interpret as Behaviour}$ |
| **Target Integration** | Transfer structure + behaviour | Transfer $R_S$, retain/infer local $R_B$ |
| **Claim Nature** | Absolute independence claim | Distinct scientific components + testable empirical claims |
| **Model Residual** | Residual = Behaviour | Residual = **unexplained variation** (not automatically Behaviour) |
| **Model Error Role** | Error proves Behaviour | Error only **motivates the Behaviour hypothesis** |
| **Unexplained Variance Source** | Missing info is definitely Behaviour | Could be missing Structure representation ($R_S$) OR Behaviour ($R_B$) |
| **Behaviour Definition** | Behaviour is the entire residual | Behaviour is a **hypothesized component** of remaining variation |
| **Sufficiency Tests** | Representation sufficiency disproved | Evaluates **sufficiency of the adopted representation** only |
| **Hypothesis Verification** | Fit model directly to residual | Test: $R_S + R_B \longrightarrow \text{Superior explanation of mobility}$ |
| **OD Role** | OD reconstruction validates scientific objects | OD reconstruction validates **their joint integration** |
| **Good Flow Fit** | Good OD fit $\to$ components are correct | Good OD fit $\to$ **joint explanatory/predictive value** |
| **Evidence Scope** | OD reconstruction is the sole evidence | Multi-tiered evidence (Component + Transfer + Integration) |
| **Behaviour Validation** | Behaviour validated solely by OD fit | $R_B$ validated first via likelihood & synthetic TLD recovery |
| **Structure Validation** | Structure validated solely by OD fit | $R_S$ validated first via representation capacity & transfer tests |
| **Paper Distinction** | Papers differ by dataset/algorithm | Papers execute **two distinct scientific tasks & inference pathways** |
| **Behaviour Task** | Behaviour is learned | Behaviour representation ($R_B$) is **statistically inferred** (via MLE) |
| **Structure Task** | Structure is identified | Structure representation ($R_S$) is **constructed/learned** (via GeoAI) |
| **Parameter $\boldsymbol{\theta}$ Nature** | $\boldsymbol{\theta}$ = latent feature | $\boldsymbol{\theta}$ = inferred behavioural representation parameter |
| **Representation $R_S$ Nature** | $R_S$ = latent feature | $R_S$ = structural representation |
| **AI Role** | AI = scientific method itself | AI = **possible implementation method** |
| **Local Behaviour Data** | Behaviour = local data | Behaviour is scientific object; local data is used to infer $R_B$ |
| **Local Parameter $\boldsymbol{\theta}_c$** | Local Behaviour = $\boldsymbol{\theta}_c$ | $\boldsymbol{\theta}_c$ = representation of city-specific Behaviour |
| **Behaviour Transferability** | Behaviour is untransferable | **Does not assume global transferability** by default |
| **Local Inference Rationale** | Proof of non-transferability | Local inference = **modelling principle / strategic choice** |
| **Zero-shot Target OD** | Zero-shot OD prediction | **Structural zero-shot transfer + local Behaviour inference** |
| **Cross-city Strategy** | Transfer structure, no behaviour | **Transfer $R_S$, locally infer $R_B$** |
| **Transfer Goal** | Source $\to$ Target model | Source $\to$ **structural knowledge/representation transfer** |
| **Transfer Scope** | Transfer model = transfer everything | Does not assume transferring everything by default |
| **Cross-city Behaviour** | Behaviour transferred from source to target | **Target Behaviour inferred locally** ($R_{B, \text{target}}$) |
| **Target Data Needs** | Target needs no information | Target needs open spatial features ($X_{S, \text{target}}$) & local TLD ($D_{\text{target}}$) |
| **Representation Transfer** | $R_{S, \text{source}} = R_{S, \text{target}}$ | Source representation knowledge transferred & **instantiated** on target |
| **Target Case Study Role** | Target city = research object | Target city (e.g., HCMC) = **target demonstration/validation case** |
| **Zero-Shot Transfer** | Zero-shot OD prediction | **Zero-shot structural transfer ($R_{S, \text{target}}$)** |

### Distinct Scientific Tasks and Inference Pathways (Paper 1 vs. Paper 2)

Paper 1 and Paper 2 do not merely differ in datasets or algorithms; they execute fundamentally different **scientific tasks** via distinct inference pathways:

1. **Pathway 1: Statistical Inference Pathway (Paper 1 — Behavioural Stream)**:
   $$D_{\text{TLD}} \mid R_S \xrightarrow{\text{statistical inference (MLE)}} \hat{R}_B(\hat{\boldsymbol{\theta}})$$
   * **Task:** Parametric statistical inference of collective distance sensitivity ($\boldsymbol{\theta}$) from aggregate travel-distance distributions given an independently specified structural representation ($R_S$). AI/optimization functions as a numerical implementation tool rather than the scientific method itself.

2. **Pathway 2: Representation Learning Pathway (Paper 2 — Structural Stream)**:
   $$\text{Open Spatial Information (OSM, POI, Satellite)} \xrightarrow{\text{representation learning (GeoAI/GNN)}} R_S(O_i, A_j)$$
   * **Task:** Spatial representation learning and domain adaptation to construct transferable structural representations ($R_S$) from multi-source geographic contexts.

### Strategic Transfer & Local Inference Protocol

The framework adopts a deliberate modeling strategy for cross-city application: **transfer structural representations ($R_S$), while locally inferring behavioural representations ($R_B$)**:

$$\text{Structural Transfer \& Instantiation: } X_{S, \text{source}} \longrightarrow R_{S, \text{transfer}} \xrightarrow{X_{S, \text{target}}} R_{S, \text{target}}$$

$$\text{Local Behaviour Inference: } D_{\text{target}} \mid R_{S, \text{target}} \xrightarrow{\text{local inference}} R_{B, \text{target}}(\boldsymbol{\theta}_{\text{target}})$$

$$\text{Unified Integration: } R_{S, \text{target}} + R_{B, \text{target}} \longrightarrow \text{Gravity Protocol} \longrightarrow \text{OD}_{\text{target}}$$

Crucially:
* **Object Transferred**: The source spatial representation knowledge ($R_{S, \text{transfer}}$) is transferred and instantiated on the target city using open spatial features ($X_{S, \text{target}}$).
* **Target Information Requirements**: The target domain still requires open spatial features ($X_{S, \text{target}}$) to instantiate structural representation $R_{S, \text{target}}$, and low-cost aggregate mobility summaries ($D_{\text{target}}$) to infer local behaviour $R_{B, \text{target}}$.
* **Local Inference Rationale**: Locally inferring $R_{B, \text{target}}$ is a **modelling principle and strategic design choice** of the framework to respect city-specific friction profiles and prevent cross-domain behavioural bias: *Structure transferability is an empirical hypothesis to be tested, while target-city Behaviour is locally inferred unless its transferability is separately demonstrated*. Local inference from low-cost aggregate TLDs provides a robust, city-specific calibration mechanism without making a dogmatic claim of intrinsic untransferability.
* **Demonstration Case**: Specific target cities (e.g., Ho Chi Minh City) function as **demonstration and empirical validation cases** to evaluate cross-city transferability and matrix reconstruction, rather than the primary scientific object of the dissertation.

---

# 4. Central Scientific Proposition & Hypotheses

> **Central Scientific Proposition:**
> *Although Spatial Interaction emerges from the interaction between Urban Structure Representation and Travel Behaviour Representation, treating these representations as analytically distinguishable enables different scientific questions to be formulated, different learning objectives to be defined, and different learning strategies to be developed. The reconstructed OD matrix serves as empirical evidence that integrating these two distinct scientific components adequately explains observed Spatial Interaction.*

### Hypotheses

* **Hypothesis 1 (H1 — Paper 1 — Module 5):**
  *A representation of city-specific Travel Behaviour can be statistically inferred from aggregate travel-distance observations given an independently specified structural representation.*

* **Hypothesis 2 (H2 — Paper 2 — Module 4):**
  *An Urban Structure Representation learned from observable urban features can provide transferable structural information across heterogeneous urban environments under appropriate cross-city conditions.*

---

# 5. Research Questions (Derived from Module 7: Research Gaps)

The following research questions are derived from the scientific gaps identified after introducing the Structure–Behaviour Decomposition Principle (Module 7):

### RQ1 (Paper 1 — Travel Behaviour Representation)

*Can a representation of city-specific Travel Behaviour be statistically inferred from aggregate travel-distance observations when the relevant Urban Structure is represented independently, and does the inferred representation support spatial interaction reconstruction?*

---

### RQ2 (Paper 2 — Urban Structure Representation)

*Can Urban Structure be represented from observable urban features using spatial representation learning, and does the learned representation generalize across heterogeneous urban environments?*

---

### RQ3 (Integration — Module 8: Dissertation Framework)

*Can Spatial Interaction be explained through the probabilistic integration of the inferred Travel Behaviour representation and the learned Urban Structure representation?*

*(Note: The objective of RQ3 is **explanation** of the mechanisms governing Spatial Interaction, not merely OD prediction. OD matrix reconstruction is the empirical validation evidence).*

---

# 6. Dissertation Framework (Module 8 Operationalization)

The dissertation operationalizes the Structure–Behaviour Decomposition Principle into a coherent research framework:

```text
                      SPATIAL INTERACTION
                      (Scientific Object)
                              │
                              ▼
         ┌────────────────────────────────────────┐
         │  Structure–Behaviour Decomposition      │
         │  Principle + Scientific Proposition     │
         └──────────────────┬─────────────────────┘
                            │
           ┌────────────────┴────────────────┐
           ▼                                 ▼
Urban Structure Representation     Travel Behaviour Representation
   (Module 4 → Paper 2)               (Module 5 → Paper 1)
           │                                 │
 Observable Urban Features        Aggregate Mobility Observations
           │                                 │
  Learning Objective:                Learning Objective:
  Transferable Potential Field       Statistical Identification
  (Module 6 — Learning Strategy)     (Module 6 — Learning Strategy)
           │                                 │
           └─────────────┬───────────────────┘
                         ▼
         ┌───────────────────────────────────┐
         │  Probabilistic Integration        │
         │  (Gravity as Scientific Language) │
         └───────────────────────────────────┘
                         │
                         ▼
              OD Matrix Reconstruction
              (Validation Evidence)
```

**Derivation chain (Module 8):**
Structure–Behaviour Decomposition Principle → RQ1 → Paper 1 → RQ2 → Paper 2 → Dissertation Framework

---

# 7. Paper 1

## Identification of the Travel Behaviour Representation of Spatial Interaction from Aggregate Travel-Distance Distributions

*(Addresses Module 5: Travel Behaviour Representation — evolution to statistically identified parameters; and RQ1 from Module 7: Research Gaps)*

### Scientific Objective

Provide empirical statistical evidence supporting parameter identification of the **Travel Behaviour Representation** (collective distance sensitivity $\boldsymbol{\theta}$) from aggregate travel-distance observations (TLDs), advancing the representation from analytical decay functions to empirically calibrated parameters.

### Learning Objective & Strategy

* **Learning Objective:** Identify $\boldsymbol{\theta}$ from aggregate TLD without requiring pairwise OD labels.
* **Learning Strategy:** Conditional Maximum Likelihood Estimation (MLE) under a binned Multinomial observation model.

### Main Contributions

* Operationally define Travel Behaviour Representation as collective distance sensitivity $\boldsymbol{\theta}$.
* Develop a binned probabilistic observation model formalizing aggregate information loss.
* Demonstrate a well-defined likelihood surface supporting parameter identification (QT12: Multi-start $\text{CV} = 0.00\%$).
* Demonstrate parameter recovery robustness under observational noise (QT18: $<0.5\%$ error under $20\%$ noise).

### Scientific Evidence Provided

Supports **Hypothesis 1**: A representation of city-specific Travel Behaviour can be statistically inferred from aggregate travel-distance observations given an independently specified structural representation ($R^2 = 0.9624$ vs. OD-fitted parameters across 50 US cities).

---

# 8. Paper 2

## Representation of Urban Mobility Potential Field for Spatial Interaction Modelling

*(Addresses Module 4: Urban Structure Representation — evolution to learned representations; and RQ2 from Module 7: Research Gaps)*

### Scientific Objective

Learn and evaluate an **Urban Structure Representation ($R_S$)** from multi-source open urban features, following the *observable → representable → testable-transferability* logic, and determine whether the resulting representation can be operationalized into relevant structural quantities such as $O_i$ and $A_j$ for spatial interaction modelling.

### Learning Objective & Strategy

* **Learning Objective:** Learn $R_S$ from observable urban features and evaluate whether it can be instantiated to produce useful structural quantities ($O_i, A_j$) in unseen cities.
* **Learning Strategy:** Spatial representation learning (Spatial GNNs / DeepGravity), motivated by the observed capacity limitations of non-spatial tabular models ($R^2 \le 0.48$, QT14).

### Main Contributions

* Formalize the Urban Mobility Potential Field consisting of Production Potential ($O_i$) and Attraction Potential ($A_j$).
* Demonstrate that tested non-spatial tabular models show capacity limitations ($R^2 \le 0.48$, QT14), motivating the investigation of spatial graph neural network representations.
* Establish cross-city zero-shot transferability evaluation benchmarks (QT17: Test $\text{CPC} = 0.646$).

### Scientific Evidence Provided

Supports **Hypothesis 2**: An Urban Structure Representation learned from observable urban features can provide transferable structural information across heterogeneous urban environments under appropriate cross-city conditions.

---

# 9. Probabilistic Integration Protocol & Scientific Contributions

### Integration Protocol

The principal methodological contribution of this dissertation is not a new Gravity model. Instead, it is a **Probabilistic Integration Protocol** that combines two distinct scientific representations: Urban Structure Representation learned from observable urban features, and Travel Behaviour Representation inferred from aggregate mobility observations. Gravity serves as the common **scientific language** (Module 2) through which these two distinct components interact to generate observable Spatial Interaction flows.

### Contribution 1 — Theory of Travel Behaviour Identification
Advance Travel Behaviour Representation from analytical decay functions to a statistically identified probabilistic inference framework showing that a representation of city-specific travel behaviour can be inferred from aggregate mobility statistics.

### Contribution 2 — Scientific Representation of Urban Structure
Advance Urban Structure Representation from handcrafted variables to a learned Mobility Potential Field ($O_i, A_j$) using spatial GeoAI and open urban data, with cross-city transferability as an evaluation diagnostic.

### Contribution 3 — Mechanism-based Probabilistic Integration Framework
Establish a mechanism-based probabilistic integration framework that combines representations of the two distinct scientific components within a unified Spatial Interaction model. The methodological novelty lies in **treating the two representations as analytically distinguishable** with distinct learning objectives, learning strategies, and empirical evaluation pipelines, rather than jointly optimizing them in a single black-box function.

---

# 10. Expected Scientific Impact

```text
Scientific Understanding ──► Quantitative Diagnosis ──► Policy Interpretation ──► Mechanism-based Evaluation ──► Transferable Mobility Knowledge
```

---

# 11. Narrative Evolution Summary

| Component | Before Quick Tests | After QT1–QT19 + Refined 8-Module Framework |
| :--- | :--- | :--- |
| **Scientific Object** | Human Mobility (phenomenon) | **Spatial Interaction (formal scientific object)** |
| **Motivation** | Better OD prediction | **Better scientific understanding of Spatial Interaction** |
| **Research Gap** | Lack of transferability | **Representations entangled — no independent learning objective** |
| **Core Principle** | Gravity model baseline | **Structure–Behaviour Decomposition Principle + Scientific Proposition** |
| **Paper 1** | Estimate decay $\beta$ | **Identify Travel Behaviour Representation from aggregate TLD** |
| **Paper 2** | Learn $O_i, A_j$ | **Learn transferable Urban Structure Representation** |
| **Module 6** | Information Hierarchy | **Learning Objective → Strategy → Representation → Generalization chain** |
| **Integration** | Reconstruct OD | **Explain Spatial Interaction — OD is validation evidence** |
| **Contribution** | Better AI model | **Mechanism-based Probabilistic Integration Framework** |

---
*Status: Updated V3.0 — Refined 8-Module Framework (Structure–Behaviour Decomposition Principle).*
