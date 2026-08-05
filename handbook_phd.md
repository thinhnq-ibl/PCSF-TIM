---
title: "PhD Operating System & Master Research Notebook (handbook_phd.md)"
subtitle: "Hệ Điều Hành Luận án Tiến sĩ & Sổ tay Nghiên cứu Khoa học Phân tích"
author: "PhD Candidate"
date: "2026"
anchor-reference: "Handbook.md (Anchor for Paper 2 / Stage 1 Knowledge Base)"
system-protocol: "One Conversation → One Refinement"
---

# PhD Operating System & Master Research Notebook
# Hệ Điều Hành Luận án Tiến sĩ & Sổ tay Nghiên cứu Khoa học

---

## 📌 Three Evolutionary Stages of the PhD Journey

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 1 (Completed): Handbook.md                                                       │
│ • Focus: "What is Human Mobility?" (Knowledge Acquisition & Literature Synthesis).      │
│ • Role: Immutable Anchor for Paper 2 (PCSF-TIM / Behaviour Identification).             │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 2 (Active - Operating System): handbook_phd.md                                   │
│ • Focus: "What is my specific scientific contribution to Human Mobility?"              │
│ • Role: Living PhD Notebook & Decision Operating System (8 Modules).                   │
└──────────────────────────────────────────┬─────────────────────────────────────────────┘
                                           │
                                           ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ STAGE 3 (Future Output): PhD Dissertation & Monograph                                  │
│ • Focus: 6-Chapter PhD Monograph Defense & Publications.                               │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

# MODULE 0: The 9-Step Scientific Argument Chain
# Chuỗi Lập luận Khoa học & Kiến trúc Phương pháp Độc lập

> **Grand Core Theme of the Dissertation:**
> **"Probabilistic Behavioural Identification under Information Compression"**
> 
> **Research Vision:**
> *"Rather than treating urban mobility as a black-box phenomenon, this dissertation decomposes mobility into interpretable structural and behavioural components, enabling quantitative diagnosis, policy evaluation, and mechanism-based interpretation of urban mobility systems."*

### The Immutable Scientific Principles vs Flexible Implementation Layer
A key property of this theoretical architecture is that **the core scientific principles are independent of specific implementation methods**. Not a single step in the 9-step logical chain depends strictly on Gravity, TLD, or MLE. These specific choices belong strictly to the **Implementation / Instantiation Layer**:

| Theoretical Abstraction Layer (Immutable Core) | Primary Dissertation Instantiation (Paper 2 / PCSF-TIM) | Future Alternative Instantiations |
| :--- | :--- | :--- |
| **1. Scientific Object** | Spatial Interaction | Spatial Interaction |
| **2. Scientific Representation** | Structure–Behaviour Factorization ($T_{ij} = S_{ij} \times f(d;\theta)$) | Utility Kernel / Neural Interaction Model |
| **3. Latent Mechanism** | Population Distance Sensitivity $\theta = (\alpha, \beta)$ | Heterogeneous Utility Parameters $\theta(x)$ |
| **4. Observable Evidence** | Distance-Domain Mobility Evidence | Spatiotemporal Flow Summaries |
| **5. Information Compression** | Pairwise OD Matrix $\to$ Bin Histogram Projection $\mathcal{P}$ | Graph Aggregation / Sectoral Projections |
| **6. Scientific Question** | *Can $\theta$ be identified under information loss?* | *Is compressed evidence statistically sufficient?* |
| **7. Probabilistic Inference Engine** | Conditional Maximum Likelihood Estimation (MLE) | Variational Inference / Bayesian MCMC |
| **8. Empirical Evaluation** | Likelihood Surface Concavity & Synthetic Recovery | Fisher Information Bounds / Hessian Spectrum |
| **9. Downstream Validation** | Transit Assignment & Indirect Smartcard Boarding | Traffic Count Assignment & Synthetic OD CPC |

Instead of a passive literature review, the theoretical foundation of this dissertation is structured as a **9-step logical progression**. Each step answers one scientific sub-question, leading to the conclusion that *when Urban Structure is specified and observations are aggregated due to privacy bounds, behavioural parameter identification is a relevant scientific inquiry.*

```text
1. Phenomenon & Object:     Empirical Phenomenon: Human Mobility ──► Formal Scientific Object: Spatial Interaction
          │
          ▼
2. Representation:          Spatial Interaction Factorization: Spatial Interaction ──► Structure (S_ij) + Behavioural Mechanism f(d; θ)
          │
          ▼
3. Latent Variable:         Behavioural Mechanism θ as an Unobservable Latent Descriptor (Why must it be inferred?)
          │
          ▼
4. Observation:             Observation Loss: Pairwise OD → Aggregate TLD (What do sensors/privacy observe?)
          │
          ▼
5. Information:             Residual Information Content under Aggregation Projection P (What information survives?)
          │
          ▼
6. Identifiability:         Statistical Identifiability Bounds (Can θ be identified from surviving information?)
          │
          ▼
7. Hypothesis:              Central Research Hypothesis (TLDs preserve sufficient information given S_ij)
          │
          ▼
8. Inference:               Conditional Maximum Likelihood Estimation (MLE) (How do we infer θ mathematically?)
          │
          ▼
9. Validation:              Indirect Boarding & Downstream Flow Benchmarking (How do we validate inferred θ?)
```

> **Scientific Conclusion:**
> *"If Urban Spatial Structure is specified ($S_{ij}$) and fine-grained mobility data is restricted to Aggregate Mobility Observations ($\mathbf{y}_{TLD}$), a natural scientific question is whether the behavioural mechanism governing spatial interaction remains statistically identifiable."*

---

### Deep Dive: STEP 1. Human Mobility and Spatial Interaction

#### Human mobility as a phenomenon
Human mobility is a real-world phenomenon describing the movement of people through space. It is directly observable in everyday life but, as a phenomenon, it is not itself the scientific object of quantitative analysis. To study human mobility scientifically, the phenomenon must first be represented in a mathematical and conceptual form.

#### Spatial interaction as the scientific object
In spatial interaction theory, spatial interaction is the scientific representation of human mobility. It describes the intensity of movement or interaction between origins and destinations, providing a formal framework for analysing mobility processes. Thus:

> **Human mobility is the phenomenon, whereas spatial interaction is its scientific representation.**

This distinction is fundamental because scientific inference is performed on spatial interaction rather than on the phenomenon itself.

#### Two fundamental components of spatial interaction
Spatial interaction emerges from the combination of two components with fundamentally distinct functional roles:
1. **Urban Structure (Mobility Potential Field $\boldsymbol{\Phi} = (\mathbf{O}, \mathbf{A})$)** – the spatial distribution of **Production Potential ($O_i$)** (latent origin trip-emission capacity) and **Attraction Potential ($A_j$)** (latent destination opportunity density), defining *where spatial opportunities exist*.
2. **Behaviour of Spatial Interaction** – defined as the **collective distance sensitivity governing the utilization of spatial opportunities**. Distance decay parameter vector $\boldsymbol{\theta}$ (e.g., Tanner deterrence $\alpha, \beta$) serves as the **mathematical proxy/representation** of this Behaviour.

Together, these two components determine the observed spatial interaction pattern when **Behaviour acts on Structure**:
\[ T_{ij} = O_i \frac{A_j f(d_{ij}; \boldsymbol{\theta})}{\sum_{m} A_m f(d_{im}; \boldsymbol{\theta})} \]

Urban Structure and Behaviour play complementary rather than equivalent roles in spatial interaction. Urban Structure defines the distribution of mobility opportunities through origin production and destination attraction potentials, whereas Behaviour determines how travellers utilize those opportunities by trading off travel opportunities against distance cost. Consequently, observed mobility emerges from the interaction between an opportunity field and a collective distance-sensitivity mechanism.

---

### Deep Dive: STEP 2. Representation of Spatial Interaction

#### Scientific Question
> **How should spatial interaction be represented to enable scientific understanding?**

*(Note: The starting point of this dissertation is NOT the Gravity model itself, but Scientific Representation Theory. The question is explicitly NOT "Which model achieves the highest accuracy?")*

#### Core Maxim & Representation Taxonomy
> **Representation determines scientific capability.**

Within spatial interaction theory, scientific representations fall into two paradigm classes:

```text
                               Human Mobility
                                     │
                                     ▼
                          Scientific Representation
                                     │
                 ┌───────────────────┴───────────────────┐
                 ▼                                       ▼
    End-to-End Representation                 Mechanism-based Representation
  (e.g., Deep Learning / Black-box)            (e.g., Spatial Interaction / Gravity)
                 │                                       │
     • High predictive performance             • Scientific interpretation & explanation
     • Limited mechanistic inference           • Explicit physical-statistical decomposition
     • Opaque internal states                  • Identifiable parameter vector θ
```

#### Core Position Statement on Mechanism-based Representation
> **"This dissertation adopts a mechanism-based representation because its primary objective is scientific understanding rather than prediction alone. Within spatial interaction theory, this is achieved by explicitly decomposing spatial interaction into urban structure and the behavioural mechanism governing interactions."**

#### Why Gravity? Gravity as an Instantiation of SciML
Gravity is not an arbitrary, outdated model chosen by default; it represents a classic, elegant instantiation of a **Mechanism-based Representation** aligned with modern Scientific Machine Learning (SciML):

\[ T_{ij} = O_i A_j f(d_{ij}; \theta) \]

where $O_i, A_j$ represent **Urban Structure**, and $f(d_{ij}; \theta)$ represents the **Behavioural Mechanism Governing Spatial Interaction**.

#### The Asymmetric Representation Progress Paradox
The core scientific gap driving this dissertation is not merely that travel behaviour is hard to measure, but that **the two components of Spatial Interaction Representation are advancing at asymmetric rates**:

```text
                               Spatial Interaction
                                        │
                                        ▼
                           Need Explicit Representation
                                        │
                                        ▼
                           Structure + Behaviour
                                        │
                 ┌──────────────────────┴──────────────────────┐
                 ▼                                             ▼
          Urban Structure                            Behavioural Mechanism
     (Observable & Data-Rich)                     (Poorly Observable & Scarce)
                 │                                             │
                 ▼                                             ▼
       AI/ML Advancing Rapidly                      Scientific Inference Lacking
 (POI, Satellite, Remote Sensing,                (Relies on Household Surveys, Census,
  Graph Neural Networks, Foundation Models)       Proprietary Telco Mobile OD Data)
                 │                                             │
                 └──────────────────────┬──────────────────────┘
                                        │
                                        ▼
                            RESEARCH OPPORTUNITY
```

#### Towards a Balanced Representation of Spatial Interaction
The higher-level scientific contribution of this dissertation is not merely parameter estimation, but **completing the scientific representation of spatial interaction**:

> **"Recent advances in geospatial data and machine learning have substantially improved the representation of urban structure. In contrast, the behavioural mechanism governing spatial interaction remains weakly observable and largely dependent on costly travel surveys. Consequently, the scientific challenge is no longer the representation of urban structure alone, but achieving a balanced representation of spatial interaction by advancing the identification of its behavioural component, thereby enabling more complete scientific analysis, inference, and predictive modelling of human mobility."**

> **Concluding Scientific Maxim of Step 2:**
> *"A scientific representation should not only reproduce observations but also reveal the underlying mechanisms that generate them."*

---

### Deep Dive: STEP 3. Behavioural Mechanism $\theta$ as a Latent Descriptor

#### Transition from Step 2 to Step 3: The Grand Academic Reframing
Step 3 elevates Paper 2 and Chapter 3 from a narrow parameter estimation task into a foundational scientific endeavor:

> **"Spatial interaction science is currently advancing asymmetrically: we have mastered Urban Structure Representation ($\mathbf{S}_i$), but understand very little about the underlying Behavioural Mechanism ($\theta$). This dissertation aims to complete the scientific representation of spatial interaction by advancing the identification of its behavioural mechanism under aggregate observation loss."**

#### The Latent Nature of the Behavioural Mechanism
Why can we not observe the Behavioural Mechanism $\theta$ directly?
* **Urban Structure ($\mathbf{S}_i$)** is observable from physical spatial data (GIS, POIs, road networks, satellite imagery).
* **The Behavioural Mechanism ($\theta = (\alpha, \beta)$)** is an unobservable **Latent Descriptor** representing collective distance sensitivity across a population.

Because $\theta$ cannot be measured directly by physical sensors due to privacy constraints and high survey costs, it must be inferred via statistical inverse problem formulation.

#### The 3-Tier Generative Physical-Statistical Chain
A crucial ontological distinction in this dissertation is that **Behaviour does not generate empirical data directly; Behaviour creates Spatial Interaction, which in turn generates Mobility Observations**:

```text
Behavioural Mechanism θ  (+ Urban Structure S_ij)
           │
           ▼  (Physical Generative Process)
Spatial Interaction T_ij  (Latent Pairwise Flow Matrix)
           │
           ▼  (Observation & Aggregation Projection P)
Mobility Observations y_TLD  (Empirical Binned Distance Histogram)
```

This 3-tier chain distinguishes the **physical generative process** ($\theta + S_{ij} \to T_{ij}$) from the **empirical observation process** ($T_{ij} \xrightarrow{\mathcal{P}} \mathbf{y}_{TLD}$). It clarifies why scientific inference operates as an inverse problem from observed $\mathbf{y}_{TLD}$ back to latent $\theta$, conditioned on $S_{ij}$.

#### Paper 2 / Chapter 3 Redefined
Paper 2 is not merely an empirical curve-fitting exercise to estimate scalar $\beta$. It is **a scientific step toward completing the scientific representation of spatial interaction**, transforming an unbalanced structural model into a complete, interpretable, mechanism-based spatial interaction framework.

---

### Deep Dive: STEP 4. Observable Mobility Evidence & Information Hierarchy

#### Scientific Question of Step 4
> **If the behavioural mechanism cannot be directly observed, how can it be scientifically studied?**

*(Note: We do NOT ask "How can we observe behavior directly?" In science, latent mechanisms are never observed directly; we observe their empirical consequences.)*

#### The Epistemological Principle & Physics Analogy
Many scientific disciplines investigate latent mechanisms that cannot be directly measured. In physics, fundamental forces such as gravity or magnetic fields are not observed directly; instead, they are inferred from their observable effects on the motion of physical bodies.

Likewise, the behavioural mechanism governing spatial interaction cannot be directly measured by physical sensors. It can only be inferred from **Observable Mobility Evidence**:

> **We do not observe behaviour; we observe the empirical consequences of behaviour.**

```text
Behavioural Mechanism θ (+ Urban Structure S_ij)
          │
          ▼  (Physical Generative Process)
Spatial Interaction T_ij
          │
          ▼  (Empirical Evidence Collection)
Observable Mobility Evidence (Data)
```

#### The Information Hierarchy of Mobility Evidence
Different forms of mobility evidence capture movement processes at varying resolution levels, forming an **Information Hierarchy**:

```text
Observable Mobility Evidence
            │
            ├───────────────────────────────────────────────────────┐
            ▼                                                       ▼
Individual Trajectories ──► OD Matrices ──► Aggregate Statistics (TLD) ──► Summary Indicators
```

#### Behavioural Information
Different forms of mobility evidence preserve different levels of **Behavioural Information**. 

> **"Different forms of mobility evidence preserve different levels of behavioural information. This information hierarchy determines both the scale at which mobility can be analysed and the extent to which latent behavioural mechanisms can be inferred."**

#### Transition to Step 5
Having established that mobility evidence forms an information hierarchy, the scientific question that motivates Step 5 is:

> **"If different forms of mobility evidence preserve different amounts of behavioural information, then what behavioural information survives after spatial aggregation?"**

---

### Deep Dive: STEP 5. Information Preservation & Information Sufficiency

#### Scientific Role of Step 5
*(Crucial Note: Step 5 does NOT attempt to claim that information is sufficient. Step 5 strictly formulates the core information-theoretic problem and shifts the paradigm from Information Loss to Information Sufficiency.)*

#### 1. Information Compression
Every spatial aggregation process is a projection of information compression:
\[ \text{Trajectories} \longrightarrow \text{OD Matrix} \longrightarrow \text{Trip-Length Distribution (TLD)} \longrightarrow \text{Summary Indicators} \]
At each projection step, specific dimensions of information are discarded. This compression is a consequence of physical aggregation and privacy constraints.

#### 2. Information is Not Lost Uniformly (Selective Information Preservation)
Aggregation is not merely destructive information loss; it is **Selective Information Preservation**:
* **Trajectory $\to$ OD Matrix:** Discards *route choices and temporal sequences*, but preserves *pairwise origin-destination interaction flows*.
* **OD Matrix $\to$ TLD:** Discards *spatial origin and destination identities*, but preserves *collective travel-distance statistical signatures*.

#### 3. The Core Information-Theoretic Question
The scientific question is explicitly NOT a narrow operational inquiry (*"Does TLD work?"*), but a fundamental information-theoretic question:
> **"Does the information preserved after aggregation remain sufficient for identifying the behavioural mechanism governing spatial interaction?"**

#### 4. TLD as an Exemplar Case Study (Not the Concept Boundary)
> *"Among highly aggregated observations, trip-length distributions provide an important example because they preserve collective travel-distance statistics while discarding spatial identities."*

TLD serves as an empirical **case study**, demonstrating how highly aggregated observations can be evaluated for behavioural identification.

#### 5. Grand Motivation & Concluding PhD Maxim
> **"If behavioural mechanisms remain identifiable after substantial information compression, the implications extend beyond a single data product. It would suggest that aggregate mobility observations can serve not only descriptive purposes but also as statistically informative evidence for scientific inference."**

> **Master Concluding Maxim of Step 5:**
> **"The central question is therefore not whether information is lost during aggregation—this is by design—but whether the behavioural information that survives is sufficient for scientific inference."**

---

### Deep Dive: STEP 6 — The Scientific Gap: Behavioural Identifiability

#### The Central Scientific Question of the Dissertation
> **"Can the behavioural mechanism governing spatial interaction be identified from aggregate mobility observations?"**

#### 1. The 3 Criteria of a High-Impact Scientific Question
Step 6 satisfies three criteria of a well-posed scientific question:
1. **Plausibility:** There is theoretical ground to suspect that structural conditioning ($S_{ij}$) isolates the residual parameter space of $\theta$.
2. **Unanswered Gap:** Nobody has established the exact bounds of statistical sufficiency under spatial aggregation.
3. **High Impact:** If true, it redefines aggregate data from descriptive summaries into statistical evidence for inference!

#### 2. Elevating Transportation Science to Statistical Inference
This dissertation elevates the problem from a narrow transport domain task to a fundamental question in **Statistical Inference**:

> **"When does compressed data remain statistically sufficient for inferring a latent mechanism?"**

* **Latent Mechanism:** The behavioural mechanism governing spatial interaction ($\theta$).
* **Compressed Data:** Aggregate mobility evidence ($\mathbf{y}_{TLD}$).
* **Case Study:** Trip-length distribution (TLD) functions as the primary empirical case study, NOT the concept boundary.

> **Positioning Statement:**
> **"This dissertation investigates the statistical sufficiency of aggregate mobility observations for behavioural identification. Trip-length distributions serve as the primary case study through which this broader scientific question is examined."**

#### 3. Real-world Timeliness & Practical Urgency
Due to privacy regulations (GDPR, Differential Privacy) and data collection costs, fine-grained trajectory and OD data are increasingly suppressed. Aggregate mobility products are becoming the dominant accessible data format. Thus, establishing information sufficiency bounds is a practical requirement for data-scarce urban regions.

#### 4. The Transformation of Aggregate Data
If statistical identifiability holds under aggregation:
* Aggregate mobility data ceases to be merely a **descriptive summary**.
* Aggregate mobility data becomes **statistically informative evidence for behavioural inference**.

#### 5. Master Concluding Statements for Step 6
> **"The central scientific question is therefore not whether aggregation reduces information—this is by design—but whether the information that survives remains sufficient for identifying the behavioural mechanism governing spatial interaction."**

> **"Answering this question would redefine the role of aggregate mobility data, transforming them from descriptive statistics into scientifically informative observations for behavioural inference."**

---

### Deep Dive: STEP 7 — Probabilistic Behavioural Inference

#### The Methodological Question of the Dissertation
> **"How can the behavioural mechanism governing spatial interaction be inferred from aggregate mobility observations?"**

*(Note: Step 7 represents the very first time in the 9-step logical chain where we transition from philosophical foundation and gap formulation to concrete Statistical Methodology.)*

#### The Fundamental Statistical Principle
Before introducing technical optimization procedures such as Maximum Likelihood Estimation (MLE) or Cross-Entropy, statistical inference must establish a foundational principle:

> **"Inference requires a probabilistic relationship between the latent mechanism and the observable evidence."**

#### The Probability Distribution as the Scientific Bridge
The **Probability Distribution** is the explicit mathematical bridge connecting the unobservable latent mechanism $\theta$ to empirical mobility evidence $\mathbf{y}_{TLD}$:

```text
Behavioural Mechanism θ (latent)
           │
           ▼
Spatial Interaction Model
           │
           ▼
Probability Distribution P(k | E_k, θ)  <=== THE SCIENTIFIC BRIDGE
           │
           ▼
Observed Aggregate Mobility Evidence y_TLD
```

#### The 5-Stage Methodological Backbone
Statistical inference progresses rigorously through a 5-stage causal-mathematical chain:

```text
Scientific Hypothesis ──► Probability Model ──► Likelihood ──► Estimator ──► Parameter β (or θ)
```

1. **Scientific Hypothesis:** Aggregate mobility evidence preserves sufficient statistical information to identify $\theta$ given urban spatial exposure $E_k$.
2. **Probability Model:** Multinomial bin distribution $P(k \mid E_k, \theta) = \frac{E_k f(d_k; \theta)}{\sum E_m f(d_m; \theta)}$.
3. **Likelihood Function:** Log-Likelihood $\log \mathcal{L}(\theta \mid \mathbf{y}, E_k) = \sum y_k \log P(k \mid E_k, \theta)$.
4. **MLE Estimator:** Numerical optimization $\hat{\theta}^* = \arg\max_\theta \log \mathcal{L}(\theta \mid \mathbf{y}, E_k)$ (solved via L-BFGS-B).
5. **Inferred Parameter $\hat{\beta}^*$ / $\hat{\theta}^*$:** Inferred collective distance sensitivity parameter vector representing the city's behavioural index.

#### Methodological Execution: Conditional Maximum Likelihood Estimation (MLE)
By establishing the probability distribution $P(k \mid E_k, \theta)$ as the scientific bridge, PCSF-TIM formulates a **Conditional Multinomial Likelihood**:

\[ P(k \mid E_k, \theta) = \frac{E_k \, f(d_k; \theta)}{\sum_{m=1}^K E_m \, f(d_m; \theta)} \]

where $E_k = \sum_{(i,j) \in \text{Bin}_k} O_i A_j$ represents the independently specified spatial exposure of distance bin $k$.

Parameter estimation is subsequently executed by maximizing the log-likelihood over observed aggregate evidence $\mathbf{y}$:

\[ \hat{\theta}^* = \arg\max_{\theta} \sum_{k=1}^K y_k \log P(k \mid E_k, \theta) \]

#### Statistical Test Condition for Empirical Evaluation
If aggregate mobility observations truly preserve sufficient statistical information, the conditional likelihood function $\mathcal{L}(\theta \mid \mathbf{y}, E_k)$ will possess the mathematical sharpness and concavity required to reliably **identify** the latent behavioural mechanism $\theta$. If not, the likelihood surface will remain flat or ill-conditioned. Testing this exact statistical property is the empirical objective of validation in Step 8.

> **Master Concluding Maxim of Step 7:**
> **"The proposed framework therefore formulates behavioural identification as a probabilistic inference problem, in which aggregate mobility observations constitute statistical evidence for estimating the latent behavioural mechanism governing spatial interaction."**

---

### Deep Dive: STEP 8 — Empirical Evaluation: Testing Statistical Identifiability

#### Scientific Question of Step 8
> **Does the empirical conditional likelihood surface possess the mathematical properties required to support behavioural parameter identification?**

#### The Statistical Test Condition
Step 8 translates the theoretical question into a rigorous empirical test:

* **IF** aggregate mobility evidence $\mathbf{y}_{TLD}$ truly preserves sufficient statistical information, **THEN** the conditional log-likelihood function $\log \mathcal{L}(\theta \mid \mathbf{y}, E_k)$ will exhibit a well-defined global optimum, sharp curvature, and strong Hessian concavity, enabling reliable identification of $\theta$.
* **IF NOT**, the likelihood surface will remain flat, ill-conditioned, or unidentifiable, failing parameter recovery tests.

#### The 4 Complementary Components of Empirical Evidence
To build rigorous empirical evidence without claiming unproven mathematical proof, evaluation is structured into four complementary components:

1. **Likelihood Evidence:** Sharpness, concavity, and global uniqueness of the log-likelihood surface over real-world data.
2. **Synthetic Parameter Recovery:** Generating synthetic TLD from known ground-truth $\theta^*$, then verifying that MLE accurately recovers $\hat{\theta}^* = \theta^*$.
3. **Cross-City Stability & Consistency:** Independently inferring $\hat{\theta}^*$ across 50 US cities to confirm that the inferred index is a stable physical-statistical property of urban populations.
4. **Downstream Flow Corroboration:** Verifying that inferred $\hat{\theta}^*$, when re-embedded into a complete gravity model, produces accurate OD flow matrices ($\hat{T}_{ij}$).

> **Master Concluding Maxim of Step 8:**
> **"Empirical evaluation does not attempt to mathematically prove universal identifiability; it builds rigorous statistical evidence testing whether aggregate observations preserve sufficient information to identify collective travel behaviour."**

---

### Deep Dive: STEP 9 — Downstream Validation & 3-Level Evaluation Architecture

#### Scientific Question of Step 9
> **How can inferred behavioural mechanisms be validated across controlled theory, empirical benchmarks, and decision-support applications?**

#### The 3 Distinct Validation Levels & Paper Scope Boundaries

```text
                               3-Level Validation Architecture
                                              │
         ┌────────────────────────────────────┼────────────────────────────────────┐
         ▼                                    ▼                                    ▼
 Level 1: Statistical Validation      Level 2: Benchmark Validation       Level 3: Policy & Planning Validation
 (Synthetic Parameter Recovery)       (50 US Cities Method Comparison)     (Decision-Support HCMC Application)
 ──► Scope of PAPER 2                ──► Scope of PAPER 2                 ──► Scope of PAPER 3
```

1. **Level 1 — Statistical Validation (Identifiability Proof - Paper 2):**
   * *Objective:* Test parameter recovery where ground truth $\theta^*$ is known by construction.
   * *Pipeline:* Known $\theta^* \to \text{Generate OD} \to \text{Aggregate TLD} \to \text{Infer } \hat{\theta}^* \to \text{Verify } \hat{\theta}^* = \theta^*$.

2. **Level 2 — Benchmark Validation (Method Comparison - Paper 2):**
   * *Objective:* Benchmark inferred $\theta_{Aggregate}$ against parameters $\theta_{OD}$ calibrated directly from ground-truth OD survey matrices across 50 US cities.
   * *Pipeline:* Ground-truth OD $\to \text{Aggregate TLD} \to \text{Infer } \theta_{Aggregate} \quad\text{vs}\quad \text{Ground-truth OD} \to \text{Calibrate } \theta_{OD}$.

3. **Level 3 — Policy and Planning Validation / Decision-Support Validation (Application Utility - Paper 3):**
   * *Objective:* Demonstrate practical planning utility in survey-free target cities (Ho Chi Minh City).
   * *Pipeline:* $\text{Transferred Structure } \mathbf{S}_i + \text{Inferred } \hat{\theta}^* \to \text{Generated OD } \hat{T}_{ij} \to \text{Transit Assignment} \to \text{Predicted Bus/Metro Boardings} \leftrightarrow \text{Observed Smartcard Boardings}$.

> **Crucial Scope Boundary Insight:** Bus Smartcard boardings do NOT prove behavioural identifiability ($\theta$) in Paper 2 because boardings depend on transit network topology, route frequency, capacity, and assignment algorithms. Bus boardings belong strictly to **Paper 3** to demonstrate that the inferred behaviour produces an OD matrix of practical utility for urban transport planning!

> **Master Concluding Maxim of Step 9:**
> **"The objective of validation is not merely to demonstrate predictive performance, but to evaluate whether aggregate mobility observations preserve sufficient statistical information to support behavioural identification."**

---

# MODULE 1: Research Vision

> **"Human mobility should not only be predicted through opaque end-to-end models, but also understood through the explicit theoretical separation of urban spatial structure and collective travel behaviour under aggregate observation loss."**

### Core Position Statement
Within spatial interaction theory, human mobility emerges from the interaction between urban spatial structure and a behavioural mechanism governing how spatial separation influences interactions. In gravity models, this behavioural mechanism is represented by the distance-decay function, but the concept itself is more general than any particular mathematical formulation.

This dissertation departs from the approach of treating spatial interaction as an undifferentiated end-to-end mapping ($\text{Spatial Data} \to \text{OD}$). Instead, it investigates a deeper information-theoretic question: **What statistical information survives spatial aggregation, and does aggregate mobility preserve sufficient information to identify the behavioural mechanism governing spatial interaction?**

---

# MODULE 2: Scientific Questions Chain

The entire PhD dissertation addresses **One Grand Scientific Question**, broken down into **Six Sequential Scientific Sub-Questions** corresponding to the 6 chapters of the PhD monograph:

### Grand Scientific Question
> **How can human mobility be understood by explicitly separating urban structure from collective travel behaviour?**

### Sequential Sub-Questions (Chapter Mapping)
* **Q1 (Chapter 1 - Theory):** *What determines human mobility?*
* **Q2 (Chapter 2 - Urban Structure):** *How should urban structure be represented from open spatial data?*
* **Q3 (Chapter 3 - Behaviour Identification - SCIENTIFIC CORE):** *How can the behavioural mechanism governing spatial interaction be identified from aggregate mobility observations under spatial information loss?*
* **Q4 (Chapter 4 - Transferability):** *How can urban structural knowledge be transferred across cities without local OD surveys?*
* **Q5 (Chapter 5 - Survey-Free OD - ENGINEERING DEMO):** *How can complete OD flow matrices be generated by combining transferred urban structure and locally identified behaviour?*
* **Q6 (Chapter 6 - Applications & Validation):** *How can the integrated framework support transportation planning and enable indirect model validation?*

---

# MODULE 3: Scientific Philosophy & Causal Chain

## 1. The Structure–Behaviour Decoupling Axiom

```text
Human Mobility (Empirical Phenomenon)
            │
            ▼
Spatial Interaction (Formal Scientific Object)
            │
     ┌──────┴──────┐
     ▼             ▼
Urban Structure   Behavioural Mechanism
(Opportunities S_ij) (Distance Sensitivity f(d; θ))
```
$$\text{Spatial Interaction } T_{ij} = \text{Urban Structure } (S_{ij}) \times \text{Behavioural Mechanism } f(d_{ij}; \theta)$$

* **Statistical Formulation:** Given known/observed Urban Structure $\mathbf{S}$, the residual parameter space $P(\text{TLD} \mid \theta, \mathbf{S})$ collapses to a low-dimensional unknown parameter vector $\theta = (\alpha, \beta)$, providing the mathematical intuition for parameter identification under aggregate loss.
* **Urban Structure ($\mathbf{S}_i$):** Objective, spatial distribution of human activities, land use, POIs, and transport networks. Learned via Deep Learning / GNNs.
* **Collective Behaviour ($\theta$):** Intrinsic population distance sensitivity and spatial friction response. Hypothesized to be identifiable via Probabilistic Likelihood Inference (MLE).
* **Formal Thesis Definition:** *In this dissertation, the behavioural mechanism governing spatial interaction refers to the component of a spatial interaction model that determines how travel propensity varies with spatial separation, after controlling for urban structural factors. Within the gravity framework, this mechanism is represented by the distance-decay function $f(d;\theta)$.*
* **Decoupling Value:** Solves the cross-city transferability dilemma: $\mathbf{S}_i$ is transferable across space, whereas $\theta$ is an intrinsic local city property identified from privacy-preserving aggregate TLDs.

## 2. The Evaluation–Inference Separation Axiom
> **Ground-truth OD matrices are used exclusively for scientific evaluation and benchmarking, not for behavioural inference. Behavioural parameters are inferred solely from aggregate mobility observations (TLD), while OD matrices serve only to assess the validity of the inferred behaviour through downstream reconstruction accuracy.**

### Conventional vs Proposed Evaluation Architecture
```text
Conventional Supervised Calibration:
   Ground-truth OD Matrix ──────► Calibration ──────► Parameter Estimator θ

Proposed PCSF-TIM Framework:
   Scientific Research Stage (Benchmarking):
   Ground-truth OD Matrix (Validation Benchmark Only)
            ▲
            │ (Downstream Flow Agreement Evaluation)
   Reconstructed Flows \hat{T}_{ij}
            ▲
            │ (Forward Gravity Factorization: S_i × f(d;\hat{\theta}^*))
   Inferred Behaviour Index \hat{\theta}^*
            ▲
            │ (Conditional Likelihood Inference P(TLD | S_i, θ))
   Aggregate Observations (observed TLD) + Open Urban Structure (S_i)

   Real-world Deployment Stage (Zero OD Surveys Required):
   Open Spatial Data (S_i) + Aggregate TLD ──────► Probabilistic MLE ──────► Inferred θ ──────► Generated OD Matrix
```
* **ML Analogy:** Ground-truth OD matrices function exactly like **test labels in Machine Learning**: they do NOT participate in inference/training, but serve strictly to compute test accuracy/goodness-of-fit metrics.

## 3. The Symmetric Dual-Engine & Mobility Synthesis Architecture (Framework V2)

The dissertation is structured around an elegant **Symmetric Dual-Engine Architecture** that infers the three basic components of spatial interaction ($O_i$, $A_j$, $\theta$) before synthesizing survey-free mobility:

```text
                 Observed Urban Features                   Aggregate Distance Distribution y_TLD
                            │                                                │
                            │ ML / GeoAI                                     │ Conditional MLE
                            ▼                                                ▼
             Engine A: Structural Component Inference         Engine B: Behavioural Inference
              (Infers Structural Components)                 (Infers Latent Behaviour Parameter)
              ┌─────────────┴─────────────┐                                  │
              ▼                           ▼                                  │
       Origin Potential          Destination Opportunity                     │
            (O_i)                       (A_j)                                │
              └─────────────┬─────────────┘                                  │
                            │                                                │
                            └──────────────────────────┬─────────────────────┘
                                                       │
                                                       ▼
                                        Engine C: Mobility Synthesis
                                           (Gravity Generative Engine)
                                                       │
                                                       ▼
                                        Reconstructed OD Matrix (T_ij)
                                                       │
                                                       ▼
                                       Policy & Planning Applications
```

### The 3 Symmetric Engines of the Thesis
| Component / Engine | Operational Input | Target Output | Scientific Method | Theoretical Role |
| :--- | :--- | :--- | :--- | :--- |
| **Engine A: Structural Component Inference** | Observable Urban Features (OSM, POIs, Satellite) | Structural Components $(O_i, A_j)$ | Machine Learning / GeoAI | Learns trip generation potential $O_i$ & attraction opportunity $A_j$ |
| **Engine B: Behavioural Inference** | Aggregate Travel-Distance Evidence ($\mathbf{y}_{TLD}$) | Latent Behaviour Parameter $\theta$ | Conditional Maximum Likelihood (MLE) | Recovers collective distance-decay parameter $\theta$ |
| **Engine C: Mobility Synthesis** | Inferred Structure $(O_i, A_j)$ + Inferred Behaviour $\theta$ | Full OD Flow Matrix ($T_{ij}$) | Forward Generative Gravity Model | Synthesizes survey-free OD matrix without fitting parameters |

### Updated Scientific Inference Framework (V2 Matrix)

| Stage | Scientific Question | Scientific Claim | Assumption | Inference Principle | Representative Literature |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Structural Component Inference** | How can structural components be inferred from open urban data? | Urban structure consists of **Origin Potential ($O_i$)** and **Destination Opportunity ($A_j$)**, both inferable from features. | **A1. Structure–Behaviour Separation** | Observable urban features $\to$ Structural representation $\to (O_i, A_j)$ | Wilson (1970); Generalized Radiation; Deep Gravity; UGNN; neuroGravity |
| **2. Forward Mobility Generation** | How are aggregate mobility observations generated? | Aggregate travel-distance distributions arise from interaction between structure and behaviour. | **A2. Gravity Forward Assumption** | $(O_i, A_j, \theta) \to \text{Gravity} \to \text{Travel Distance Distribution}$ | Gravity; Tanner; Barbosa Review |
| **3. Behavioural Inference** | Can behavioural parameters be recovered from aggregate evidence? | Aggregate travel-distance distributions preserve sufficient information to identify distance-decay. | **A3. Information Sufficiency**<br>**A4. Identifiability** | Likelihood / MLE : $\mathbf{y}_{TLD} \to \theta$ | **Core Contribution of the Thesis (Paper 2 / PCSF-TIM)** |
| **4. Mobility Synthesis** | Can inferred structure and behaviour jointly reproduce mobility? | Combining inferred structural components and inferred behaviour reconstructs complete OD matrix. | **A5. Generative Gravity** | $(O_i, A_j, \hat{\theta}) \to \text{Gravity} \to \text{OD}$ | Gravity; Deep Gravity; neuroGravity |
| **5. Planning Application** | Why reconstruct OD? | OD demand is the operational representation required by planning models. | **A6. Planning Sufficiency** | $\text{OD} \to \text{Planning Models} \to \text{Decision Support}$ | Barbosa Review; UGNN |

## 4. The Master 7-Column Literature & Conceptual Mapping Matrix

| Stage | Topic | Foundation | Classical | Modern | Review / Survey | Role in Framework |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Urban Structure Representation** | Urban structure | Wilson (1970) | Gravity Model | Deep Gravity (2021), Imagery2Flow (2025), UGNN (2025), neuroGravity (2026), Representation Learning (2025) | Barbosa et al. (2018) | Structural context & opportunities ($O_i, A_j, d_{ij}$) |
| **2. Distance-decay Mechanism** | Distance effect | Zipf (1946), Wilson (1970) | Gravity, Tanner, Exponential | Liang et al. (2013), Lenormand et al. (2016) | Barbosa et al. (2018) | Behavioural mechanism $f(d;\theta)$ |
| **3. Aggregate Mobility Observation** | Aggregate observations | Census tradition | OD matrix, Distance histogram | Gallotti et al. (2024), LBS review (2025) | Wang et al. (2019), Barbosa et al. (2018) | Observable evidence $\mathbf{y}_{TLD}$ |
| **4. Behaviour Identification** | Statistical inference | Fisher (MLE) | Likelihood inference | **Primary Dissertation Novelty (Paper 2 / PCSF-TIM)** | — | Inverse inference $\mathbf{y} \to \theta$ |
| **5. OD Reconstruction** | Spatial interaction | Gravity | Radiation (Simini 2012), IO | Deep Gravity (2021), UGNN (2025), neuroGravity (2026) | Lenormand et al. (2016) | Survey-free OD generation ($\hat{T}_{ij}$) |
| **6. Transport Planning** | Transport planning | Four-step model | OD-based planning | UGNN, Imagery2Flow | Barbosa et al. (2018) | Decision-support application (Level 3 Validation) |

## 5. The Interdisciplinary Scientific Schools Mapping Matrix

| Stage | Interdisciplinary Scientific School of Thought | Scientific Focus & Role |
| :--- | :--- | :--- |
| **1. Urban Structure Representation** | **Urban Geography / GIS / GeoAI** | Extraction of spatial opportunities, land-use attraction ($O_i, A_j$), and network accessibility ($d_{ij}$). |
| **2. Distance-decay Mechanism** | **Spatial Interaction Theory** | Conceptualization of friction of distance and collective travel deterrence behavior $f(d;\theta)$. |
| **3. Aggregate Mobility Observation** | **Mobility Data Science** | Processing privacy-preserving distance histograms ($\mathbf{y}_{TLD}$) and aggregate spatiotemporal evidence. |
| **4. Behaviour Identification** | **Statistical Inference / Inverse Problems** | Formulation of conditional multinomial likelihoods and numerical MLE estimation for latent parameters $\theta$. |
| **5. OD Reconstruction** | **Transportation Science** | Forward generative matrix synthesis producing survey-free origin-destination flow matrices $\hat{T}_{ij}$. |
| **6. Transport Planning Application** | **Transportation Planning** | Downstream traffic/transit assignment, smartcard boarding validation, and decision support for urban transit networks. |

## 6. The Core Theoretical Foundations Mapping Matrix

| Stage | Core Theory (Lý thuyết Cốt lõi) | Mathematical & Physical Principles |
| :--- | :--- | :--- |
| **1. Urban Structure Representation** | **Tobler's First Law of Geography & Spatial Heterogeneity** | Spatial autocorrelation, spatial decay of influence, land-use opportunity distributions. |
| **2. Distance-decay Mechanism** | **Entropy Maximization & Gravity Theory** | Wilson's (1970) entropy-maximizing state derivation under total distance constraints. |
| **3. Aggregate Mobility Observation** | **Information Theory** | Shannon entropy, information loss under projection $\mathcal{P}$, residual statistic sufficiency. |
| **4. Behaviour Identification** | **Maximum Likelihood Estimation & Inverse Problems** | Fisherian likelihood theory, concavity of conditional multinomial distributions. |
| **5. OD Reconstruction** | **Generative Spatial Interaction Models** | Forward matrix synthesis via multiplicative structural-behavioural factorization ($S_{ij} \times f(d;\theta)$). |
| **6. Transport Planning Application** | **Demand Forecasting Theory** | Four-step transportation model, Wardropian user equilibrium, network transit assignment. |

* **Behaviour ($\theta$)** serves as the **pivotal scientific bridge** connecting Urban Design ($\mathbf{S}_i$) to the Transportation System (Traffic, Public Transit).

---

# MODULE 4: Supporting Theoretical Foundations

*(This section contains the active theoretical pillars supporting THIS thesis, distinct from a generic literature review)*

### 1. Spatial Interaction & Factorization Theory
* **Wilson (1967, 1970)**: Entropy-maximizing foundations for spatial interaction decomposition $T_{ij} = O_i A_j f(d_{ij};\theta)$.
* **Erlander & Stewart (1990) / O'Kelly (2009)**: Mathematical separation of origin/destination attraction constraints from deterrence.
* **Merlin (2020)**: Inspiring methodological precedent demonstrating that median travel duration matching calibrates single-parameter gravity models under fixed structure, while explicitly warning against unconditioned TLD curve-fitting (which ignores spatial structure).

### 2. Random Utility & Discrete Choice Behaviour
* **Ben-Akiva & Lerman (1985)**: Random Utility Maximization (RUM) grounding destination choice.
* **Fotheringham & O'Kelly (1989)**: Spatial deterrence as spatial friction and opportunity availability.

### 3. Privacy Pruning & Information Theory Bounds
* **de Montjoye (2013)**: Trajectory re-identification bounds (95% re-identification from 4 spatiotemporal points).
* **Gallotti et al. (2024)**: Demonstrated that privacy-preserving matrix pruning distorts micro origin-destination flows.
* **Cover & Thomas (2006) / Casella & Berger (2002)**: Information-theoretic bounds and Multinomial Probabilistic Likelihood derivation for binned spatial data:
  \[ P(k \mid E_k, \theta) = \frac{E_k \, f(d_k; \theta)}{\sum_{m=1}^K E_m \, f(d_m; \theta)} \]

### 4. Urban Complexity & Spatial Heterogeneity Limits
* **Batty (2013) & Barthelemy (2016, 2018)**: Complex systems view of urban scaling, spatial networks, and population mobility distributions.
* **Yang et al. (2014)**: Limits of classical gravity assumptions under extreme spatial heterogeneity and polycentric urban structures.

### 5. Formal Theoretical Assumptions (A1–A7 Defense Taxonomy)
Each formal assumption protects exactly one explicit arrow in the causal derivation chain ($\text{Structure} \to \text{Observation} \to \text{Inference} \to \text{Reconstruction} \to \text{Planning}$):

#### Updated Assumption A1 (Structure–Behaviour Separability)
> **"Human mobility can be decomposed into:**
> * **Urban Structure, represented by the trip-generation potential of origins ($O_i$) and the trip-attraction opportunity of destinations ($A_j$);**
> * **Behaviour, represented by the distance-decay mechanism governing travellers' responses to spatial separation."**

#### Formal Scientific Claim of Stage 1
> **"Urban structure is a latent structural representation consisting of two complementary components: origin potential ($O_i$) and destination opportunity ($A_j$). Observable urban features serve as representations of these latent structural components rather than direct inputs to mobility models."**

#### The Internal Architecture of Urban Structure
| Component | Scientific Meaning | Gravity Variable | Typical Representation | Representative Literature |
| :--- | :--- | :--- | :--- | :--- |
| **Origin Potential** | Capacity of a region to generate trips | $O_i$ | Population, residential density, demographics, housing | Wilson (1970); Classic Gravity literature |
| **Destination Opportunity** | Capacity of a region to attract trips | $A_j$ | Employment, amenities, POIs, schools, healthcare, services, accessibility | Alis et al. (2021); Deep Gravity; UGNN; neuroGravity |

| ID | Derivation Step | Formal Assumption | Role & Defense |
| :--- | :--- | :--- | :--- |
| **A1** ⭐⭐⭐ | Structure + Behaviour $\to$ Flow | **Structure–Behaviour Separability:** Mobility can be factorized into Urban Structure ($O_i, A_j$) and a distance-decay behavioural mechanism ($T_{ij} = O_i A_j f(d;\theta)$). | Foundation of the entire framework. Without A1, structure and behavior cannot be decoupled. |
| **A2** | Structure + Behaviour $\to$ TLD | **Gravity Forward Assumption:** Aggregate mobility is generated by a gravity-type spatial interaction model. | Defines the forward generative model producing empirical observations. |
| **A3** ⭐⭐⭐ | TLD $\to$ Inferred Behaviour $\theta$ | **Information Sufficiency:** Aggregate travel-distance distributions preserve sufficient statistical information about the distance-decay parameters. | Enables inverse inference from aggregate distance histograms to $\theta$. |
| **A4** | TLD $\to$ Inferred Behaviour $\theta$ | **Parameter Identifiability:** Different behavioural parameters induce distinguishable travel-distance distributions (at least locally). | Ensures $\theta$ is uniquely or locally identifiable on the likelihood surface. |
| **A5** ⭐⭐⭐ | Inferred $\theta$ + Structure $\to$ OD Matrix | **Generative Gravity Assumption:** Given urban structure and identified behaviour, the OD matrix is uniquely generated by the gravity model. | Enables OD matrix reconstruction without requiring full OD survey observations. |
| **A6** | OD Matrix $\to$ Transport Planning | **Planning Sufficiency:** The reconstructed OD matrix is a sufficient operational input for downstream transit planning models. | Defines application bounds without requiring direct modeling of all planning nuances. |
| **A7** | Full Inference Engine | **Likelihood Correctness:** The statistical likelihood correctly represents the empirical observation process of the aggregate distance distribution. | Guarantees the statistical validity of MLE/inference. |

> **The 3 Core Pillars:**
> 1. **A1 (Separability):** If false, structural context and human behavior cannot be decoupled.
> 2. **A3 (Information Sufficiency):** If false, aggregate evidence cannot support behavioral inference.
> 3. **A5 (Generative Gravity):** If false, survey-free OD flow matrices cannot be reconstructed after identifying $\theta$.

---

### 6. Master 30-Paper Project Literature Allocation Matrix
This matrix maps the 30 active PDF literature assets in the project into the 5 stages of the dissertation derivation framework:

#### Stage 1: Urban Structure Representation (Biểu diễn Cấu trúc Đô thị)
| Short Reference | System PDF Filename | Theoretical Contribution & Role |
| :--- | :--- | :--- |
| **Alis et al. (2021)** | *Scientific Reports 11, 22707* | **Multidimensional Attractiveness Proof:** Demonstrates that population alone is an inadequate proxy for destination attractiveness ($A_j$); multidimensional urban amenities improve flow prediction by 10.3%. |
| **Vu et al. (2021)** | `Enhanced urban functional land use map with free and open-source data.pdf` | **Local Empirical Proof:** Land-use extraction from Sentinel-2 & OSM in Ho Chi Minh City. |
| **Liu et al. (2025)** | `Representation learning for geospatial data.pdf` | **GeoAI Foundation:** Representation learning for encoding urban spatial context. |
| **Hansen (1959)** | `hansen1959.pdf` | **Classical Foundation:** Accessibility defined as potential spatial interaction based on opportunity distribution. |
| **Haynes & Fotheringham (1984)** | `gravity-and-spatial-interaction-models-oqez7udowi.pdf` | **Structural Factorization:** Mathematical isolation of origin ($O_i$) and destination ($D_j$) attractions. |

#### Stage 2: Aggregate Travel-Distance Distribution (Phân phối Khoảng cách Gộp - TLD)
| Short Reference | System PDF Filename | Theoretical Contribution & Role |
| :--- | :--- | :--- |
| **González et al. (2008)** | `Understanding-individual-human-mobility-patterns.pdf` | **Individual Trajectories:** Individual mobility follows truncated power-law bounded by radius of gyration ($r_g$). |
| **Song et al. (2010)** | `Limits-of-Predictability-in-Human-Mobility.pdf` | **Entropy Limits:** 93% upper bound on individual mobility predictability. |
| **Liang et al. (2013)** | `unraveling.pdf` | **Exponential TLD Emergence:** Analytical derivation of exponential travel-distance distributions from urban structure. |
| **de Montjoye et al. (2013)** | `srep01376.pdf` | **Trajectory Re-identification:** 4 spatiotemporal points re-identify 95% of individuals (privacy justification for aggregation). |
| **Houssiau et al. (2022)** | `houssiau2022.pdf` | **Aggregate Privacy Risk:** Re-identification risk analysis on aggregate mobility data. |
| **Gallotti et al. (2024)** | `Detors.pdf` | **Privacy Filtering Distortion:** Differential privacy filtering distorts observed TLDs. |

#### Stage 3: Behaviour Identification (Định danh Tham số Hành vi - Core Novelty)
| Short Reference | System PDF Filename | Theoretical Contribution & Role |
| :--- | :--- | :--- |
| **Merlin (2020)** | `amyf,+Merlin_1614.pdf` | **Single-Parameter Precedent:** Calibration of gravity deterrence using median travel duration matching. |
| **Yang et al. (2014)** | `yang2014.pdf` | **Analytical Scaling Limits:** Parameter scaling in Extended Radiation Models without empirical OD matrices. |
| **Rubio-Herrero & Muñuzuri (2023)** | `Sparse-regression-for-data-driven-deterrence-functions-in-gravity-models.pdf` | **Sparse Deterrence Functions:** Data-driven deterrence approximation via sparse regression. |
| **Enaya et al. (2026)** | `TransferGM-2026.pdf` | **Structural Transferability:** TransGM behavioral parameter transfer across cities based on land-use similarity. |
| **Wilson (1971)** | `wilson1971.pdf` | **Classical Entropy Calibration:** Deterrence parameter calibration via macro average trip cost constraints. |
| **Flowerdew & Aitkin (1982)** | `flowerdew1982.pdf` | **Poisson MLE Estimation:** Generalized linear models (GLMs) for spatial interaction parameter estimation. |
| **O'Kelly (2009)** | `OKELLYSIIEHG.pdf` | **Spatial Deterrence Sensitivity:** Empirical evaluation of distance-decay stability and sensitivity. |

#### Stage 4: OD Reconstruction (Tái tạo Ma trận OD - Forward Generation)
| Short Reference | System PDF Filename | Theoretical Contribution & Role |
| :--- | :--- | :--- |
| **Simini et al. (2021)** | `deep-gravity.pdf` / `s41467-021-26752-4.pdf` | **Deep Gravity:** Deep neural spatial interaction model combining gravity factorization with neural features. |
| **Yang et al. (2026)** | `2604.23678v1.pdf` | **neuroGravity:** GNN + meta-Gravity for zero-shot transferrable mobility flow generation. |
| **Guo et al. (2025)** | `Computer aided Civil Eng - 2025 - Guo...pdf` | **UGNN:** Urban Semantic GNN predicting spatial interaction flows. |
| **Xu et al. (2025)** | `Predict-statellite-image.pdf` | **Imagery2Flow:** Unsupervised urban mobility flow prediction directly from satellite imagery. |
| **Shi et al. (2020)** | `shi2020.pdf` | **MPGCN:** Multi-view graph convolutional networks for dynamic OD flow prediction. |
| **Simini et al. (2012)** | `simini2012a.pdf` | **Original Radiation Model:** Parameter-free macro mobility generation based on job opportunities. |
| **Lenormand et al. (2016)** | `1-s2.0-S0966692315002422-main.pdf` | **Cross-Country Benchmark:** Large-scale evaluation of Gravity vs Radiation models across 8 countries (CPC/CPL). |
| **DUT Mobility Review (2018)** | `urban mobility repdict.pdf` | **Deep Graph Mobility Review:** Comprehensive review of deep graph learning for mobility flow prediction. |

#### Stage 5: Planning Application (Ứng dụng Quy hoạch & Decision Support)
| Short Reference | System PDF Filename | Theoretical Contribution & Role |
| :--- | :--- | :--- |
| **Barbosa et al. (2018)** | `barbosa2018.pdf` | **Human Mobility Encyclopedia:** Comprehensive review of human mobility science, models, and downstream applications. |
| **Oliver et al. (2020)** | `oliver2020.pdf` | **Epidemiological Planning:** Aggregate mobile data for evaluating non-pharmaceutical interventions in pandemic response. |
| **Buckee et al. (2020)** | `buckee2020.pdf` | **Ethics & Crisis Planning:** Privacy ethics and operational efficacy of aggregate mobile data in public health crisis. |
| **Pappalardo et al. (2023)** | `Future-directions-in-human-mobility-science.pdf` | **Future Horizon:** Strategic roadmap for explainable AI (XAI) and sustainable multi-modal transport planning. |

---

# MODULE 5: Master Research Framework & Publication Roadmap

```text
===================================================================================================
 TIER A: SCIENTIFIC CONTRIBUTION (Human Mobility Science) ──► Primary Novelty
 "How to infer OD without surveys?"
───────────────────────────────────────────────────────────────────────────────────────────────────
 • Structure (S_i) + Behaviour (θ) ──► PCSF-TIM Framework ──► Survey-Free Zero-Shot OD Matrix (T_ij)
===================================================================================================
                                                │
                                                ▼ (Generated OD Matrix T_ij)
===================================================================================================
 TIER B: ENGINEERING CONTRIBUTION & POLICY IMPACT (Transportation Engineering) ──► Demonstration
 "What to do with the generated OD?"
───────────────────────────────────────────────────────────────────────────────────────────────────
 • Generated OD ──► Transit Assignment ──► Indirect Boarding Validation & Bus/Metro Planning
===================================================================================================
```

### Publication Roadmap
1. **Paper 1 (Behaviour Identification):** *Identification of the Behaviour of Spatial Interaction from Aggregate Travel-Distance Distributions* (TR-B / PRE / Nature Comms).
2. **Paper 2 (Mobility Potential Representation):** *Representation of Urban Mobility Potential Field for Zero-Shot OD Matrix Reconstruction* (CEUS / IEEE TKDE / KDD).
3. **Paper 3 (Integrated Thesis):** *A Hybrid Survey-Free OD Estimation Framework for Data-Scarce Metropolitan Regions* (TR-C / TR-A / IEEE T-ITS).

---

# MODULE 6: Scientific Evidence Matrix

*(Mapping core scientific claims to authoritative supporting literature and empirical evidence)*

| Scientific Claim | Theoretical / Literature Basis | Empirical Evidence |
| :--- | :--- | :--- |
| **C1. Structure and Behaviour are mathematically separable.** | Zipf (1946), Wilson (1971), Erlander & Stewart (1990) | Gravity multiplicative decomposition $T_{ij} = O_i A_j f(d;\theta)$ |
| **C2. Deep Learning models encode structural context.** | Simini (2021), Yang (2026), Enaya (2026) | SOTA neural gravity models re-embed multiplicative structural factorization |
| **C3. Local OD calibration encounters privacy limits.** | de Montjoye (2013), Gallotti et al. (2024), Meta MDM (2021) | 95% trajectory re-identification & privacy matrix pruning distortion |
| **C4. Aggregate TLDs retain distance-decay signatures.** | Merlin (2020), Flowerdew (1982), Casella & Berger (2002) | Conditional Multinomial Likelihood concavity on binned histograms $\mathbf{y}_{TLD}$ |
| **C5. Structural exposure correction is mandatory.** | Hansen (1959), Fotheringham (1989), Merlin (2020) | Ablation $E_k \equiv 1$ causes $>30\%$ parameter shift in synthetic experiments |
| **C6. Indirect Boarding Validation validates zero-shot OD.** | Ortúzar & Willumsen (2011) | Transit assignment predicted boardings vs observed Smartcard boardings |

---

# MODULE 7: Open Problems and Future Directions

*(Structured along the 4-stage scientific progression: Data Quality ──► Urban Complexity ──► Statistical Inference ──► Scientific Generality)*

### 1. Structural Exposure Estimation (Measurement Problem)
The proposed framework assumes that the structural exposure term ($E_k$) can be estimated reliably from publicly available geographic information. Experimental evidence indicates that ignoring exposure ($E_k \equiv 1$) produces parameter biases exceeding 30%, demonstrating that exposure is a necessary component for separating urban structure from travel behaviour.

A remaining challenge is therefore the accurate extraction of exposure from heterogeneous open spatial datasets (road networks, land use, accessibility, built environment, and remote sensing products). Errors in exposure estimation propagate directly into behavioural parameter recovery.

* **Future Direction:** Develop more robust exposure estimators that integrate multiple spatial data sources while remaining transferable across cities.

---

### 2. Structural Heterogeneity and Polycentric Cities (Urban Complexity Problem)
The current framework assumes that behavioural parameters remain globally identifiable after accounting for structural exposure.

However, highly polycentric metropolitan regions exhibit strong spatial heterogeneity, multiple employment centres, and locally varying accessibility patterns. These factors may reduce the separability between structural effects and behavioural responses, thereby weakening parameter identifiability.

* **Future Direction:** Investigate multi-scale and hierarchical gravity formulations capable of explicitly modelling heterogeneous urban structures while preserving behavioural interpretability.

---

### 3. Behavioural Model Identifiability (Statistical Inference Problem)
The Tanner deterrence function:
\[ f(d) = d^{-\alpha} e^{-\beta d} \]
introduces two behavioural parameters describing short-distance attraction ($\alpha$) and long-distance decay ($\beta$).

Although preliminary experiments indicate stable optimisation, the statistical identifiability of these two parameters under different distance distributions remains an open question. Correlation between $\alpha$ and $\beta$ may emerge for certain cities or limited observation ranges, potentially increasing estimation uncertainty.

* **Future Direction:** Future work should investigate profile likelihood analysis, Fisher information, and Bayesian uncertainty estimation to better quantify parameter identifiability and confidence intervals.

---

### 4. Universality of Behavioural Recovery (Scientific Validation Problem)
The proposed framework is motivated by the hypothesis that aggregate travel-distance distributions preserve sufficient information to recover collective distance sensitivity.

While the framework performs consistently across multiple metropolitan areas, its applicability to cities with substantially different urban morphologies, socioeconomic conditions, and transportation systems remains to be systematically evaluated.

* **Future Direction:** Future work should investigate the universality of behavioural recovery across diverse geographic contexts and identify the structural conditions under which aggregate distance distributions remain sufficient statistics for behavioural inference.

---

# MODULE 8: Future Research Vault & Horizon Scanner

*(Idea Vault: Capturing new ideas without polluting the core theoretical framework)*

* **FR1 (Indirect Transit Assignment Validation):** Using HCMC bus boarding smartcard data to run transit assignment on $\hat{T}_{ij}$ for indirect ground-truth validation.
* **FR2 (Urban Foundation Models):** Exploring Geo-LLMs or Urban Foundation Models (2025–2026) for zero-shot urban structure embedding in Paper 1.
* **FR3 (Metro Line 2 Planning Impact):** Applying the integrated framework to evaluate feeder bus route restructuring for HCMC Metro Line 2.
* **FR4 (Multi-Modal Behavioural Breakdown):** Extending single-index $\theta$ to multi-modal decay profiles when mode-split TLDs become available.

---

# IX. Operating System Rules & Idea Evaluation Algorithm

Every new idea, data source, or literature suggestion MUST pass through this 3-Step Algorithm before inclusion:

```text
                          New Idea / Idea Suggestion
                                      │
                                      ▼
             [Step 1: Which Scientific Question does it answer?]
                 │                                        │
             (Answers Q1-Q6)                         (No direct Q)
                 │                                        │
                 ▼                                        ▼
    [Step 2: Assign Module]                     [Do NOT put in Core]
     • Q1-Q5 ──► Core Modules 1-5                 • App-only ──► Module 8 (Vault)
     • App   ──► Module 5/8 (App/Vault)           • Speculation ──► Module 7 (Open Prob)
                 │
                 ▼
    [Step 3: Vision Alignment Check]
     • Preserves Structure-Behaviour Decoupling? ──► Append to Module
     • Alters Core Vision?                      ──► Trigger Formal OS Revision
```

### Protocol: "One Conversation → One Refinement"
1. **Exploration:** Brainstorm and evaluate new ideas during conversation.
2. **Consolidation:** Immediately refine `handbook_phd.md` after each conversation to lock in progress.
