# Research Knowledge Base (RKB) Architecture
## Background Operating System for PhD Program

> **Status:** Architecture Blueprint V1.0  
> **Role:** Master Background Operating System supporting Proposal (~20 pages), Paper 1, Paper 2, and PhD Dissertation (~150-300 pages).  
> **Core Principle:** Structure–Behaviour Separation ($T_{ij} = O_i A_j f(d_{ij}; \theta)$).

---

## 1. Overall System Architecture

```text
                           Research Program Architecture
                                       │
           ┌───────────────────────────┼───────────────────────────┐
           ▼                           ▼                           ▼
      PhD Proposal                  Paper 1                     Paper 2
   (proposal_phd.md)        (Behaviour Inference)         (Structure Transfer)
       ~20 pages                    (TLD $\to \theta$)              ($(O_i, A_j)$)
           │                           │                           │
           └───────────────────────────┼───────────────────────────┘
                                       │
                                       ▼
                       Research Knowledge Base (RKB)
                       (Handbook.md / KnowledgeBase.md)
                               ~150–300 pages
```

* **Proposal (`proposal_phd.md`):** High-level scientific synthesis (~20 pages) referencing RKB modules for detailed theoretical proofs and evidence maps.
* **Paper 1:** Methodological & empirical proof that Spatial Interaction Behaviour ($\theta$) can be statistically inferred from aggregate travel-distance distributions (TLD).
* **Paper 2:** Methodological & empirical proof that Urban Structure ($(O_i, A_j)$) can be transferred across cities using open spatial features.
* **Research Knowledge Base (`KnowledgeBase.md` & `Handbook.md`):** The comprehensive background operating system organized into 8 modular layers.

---

## 2. Standardized Layer Template

To function as a **Background Operating System**, every layer in the RKB strictly follows a 5-component modular architecture:

1. **Scientific Question:** What core scientific question does this layer answer?
2. **Core Claims:** Explicit scientific assertions established in the literature.
3. **Evidence Map:** Categorized literature support, key empirical findings, and foundational papers.
4. **Critical Comparison:** Methodological paradigms, underlying assumptions, and structural boundaries.
5. **Implications for Thesis:** Direct logical bridge leading to thesis hypotheses, Paper 1, or Paper 2.

---

## 3. The 8-Layer Knowledge Architecture

```text
Knowledge Tree Navigation:

Layer A: Why Human Mobility? (Societal & Planning Foundation)
   │
   ▼
Layer B: Data Revolution (Data Evolution & Observation Layers)
   │
   ▼
Layer C: Information Hierarchy (Resolution Reduction & Signature Preservation)
   │
   ▼
Layer D: Gravity as Scientific Language (Spatial Interaction Theory)
   │
   ▼
Layer E: Behaviour (Distance Deterrence & Behaviour Identification) ───► Paper 1
   │
   ▼
Layer F: Urban Structure (Spatial Potentials & Feature Representations) ───► Paper 2
   │
   ▼
Layer G: Transferability (Cross-City Knowledge Generalization)
   │
   ▼
Layer H: Research Gap & Convergence (Unified Methodological Framework)
```

---

### Layer A — Defining Urban Human Mobility as the Scientific Object

#### 1. Scientific Master Matrix for Layer A

| Section | Scientific Question | Core Claim | Purpose in Proposal | Connection to Later Layers |
| :--- | :--- | :--- | :--- | :--- |
| **A. Defining Urban Human Mobility as the Scientific Object** | What is the scientific object of this research? | Urban Human Mobility is the scientific object of this research. | Establish the research object, scope and scientific significance. | Foundation for the entire proposal. |
| **A1. What is Urban Human Mobility?** | What exactly is Urban Human Mobility? | Urban Human Mobility is the collective spatial movement of people within an urban system arising from daily activities. It is a phenomenon rather than a dataset. | Define the research object and distinguish the phenomenon from its observations. | Leads to Information Hierarchy (Layer C). |
| **A2. Scope of the Scientific Object** | Why focus on urban mobility instead of all human mobility? | This research focuses on intra-urban collective mobility because urban environments provide rich observable structure and abundant publicly available data. | Clearly delimit the research scope. | Motivates the exclusive focus on cities throughout the proposal. |
| **A3. Urban Mobility as a Scientific Object** | Why can Urban Human Mobility be studied scientifically? | Urban Human Mobility satisfies the essential characteristics of a scientific object. | Justify the scientific legitimacy of the research topic. | Bridges toward modelling and theory. |
| **A3.1 Observable** | Can it be observed? | Mobility can be observed through trajectories, OD matrices, surveys, GPS, LBS, travel-distance distributions and other mobility datasets. | Demonstrate that mobility leaves measurable evidence. | Leads naturally to Data Revolution (Layer B). |
| **A3.2 Measurable** | Can it be quantified? | Mobility can be quantified through flows, trip lengths, travel times, accessibility and other aggregate indicators. | Introduce measurable quantities for scientific analysis. | Supports later estimation problems. |
| **A3.3 Regular** | Does mobility exhibit regular patterns? | Although individual trips are heterogeneous, aggregate urban mobility exhibits stable statistical regularities such as gravity laws and distance decay. | Justify scientific modelling. | Leads directly to Gravity (Layer D) and Behaviour (Layer E). |
| **A3.4 Explainable** | Can these regularities be explained? | Collective mobility emerges from the interaction between Urban Structure and Human Travel Behaviour. | Introduce the conceptual framework behind the proposal. | Direct foundation for Structure–Behaviour Separation Principle. |
| **A3.5 Predictable** | Can mobility be predicted? | The existence of stable regularities makes prediction and reconstruction scientifically meaningful. | Justify the need for mobility models. | Leads toward OD reconstruction (Paper 2). |
| **A4. Scientific Definition** | How will this proposal define Urban Human Mobility? | Urban Human Mobility is the collective spatial interaction of people within an urban system, emerging from the interaction between Urban Structure and Human Travel Behaviour, and manifested through observable mobility patterns. | Provide the official definition used consistently throughout the proposal. | Serves as the ontology for all subsequent chapters. |
| **A5. Transition to Layer B** | If mobility is a scientific object, why is it still difficult to study? | Although mobility is observable, measurements are incomplete, heterogeneous and often aggregated, creating a gap between the phenomenon and available observations. | Introduce the central challenge of the proposal. | Leads directly to **Layer B – The Urban Mobility Data Revolution**. |

---

#### 2. Detailed Scientific Breakdown

##### 1. Scientific Question
What is the scientific object of this research, why does intra-urban collective mobility satisfy the requirements of a scientific object, and how is the phenomenon distinguished from its empirical measurements?

##### 2. Core Claims
* **Claim A.1 (Phenomenon vs Dataset):** Urban Human Mobility is an underlying spatio-temporal phenomenon (the collective spatial movement of people within an urban system arising from daily activities), not any single dataset or measurement layer.
* **Claim A.2 (Five Characteristics of the Scientific Object):** Intra-urban collective mobility is a legitimate scientific object because it is:
  1. **Observable:** Leaves physical traces across surveys, GPS, LBS, and aggregate travel-distance distributions.
  2. **Measurable:** Quantifiable via spatial flows ($T_{ij}$), trip lengths, travel times, and accessibility indices.
  3. **Regular:** Displays robust statistical regularities (distance-decay laws, spatial scaling).
  4. **Explainable:** Emerges from the interaction between Urban Structure ($(O_i, A_j)$) and Travel Behaviour ($f(d;\theta)$).
  5. **Predictable:** Stable regularities allow generative reconstruction in unobserved cities.
* **Claim A.3 (Ontological Definition):** *Urban Human Mobility is defined as the collective spatial interaction of people within an urban system, emerging from the interaction between Urban Structure and Human Travel Behaviour, and manifested through observable mobility patterns.*

##### 3. Evidence Map
* **Foundational Surveys:** Barbosa et al. (2018) *Human mobility: Models and applications* (Physics Reports); Zheng (2015) *Trajectory data mining*.
* **Complexity & Urban Regularities:** Batty (2013) *The New Science of Cities*; Bettencourt (2013) *Origins of scaling in cities*.
* **Epidemiology & Societal Need:** Buckee et al. (2020) (Science); Oliver et al. (2020) (Nature Communications).

##### 4. Critical Comparison
* **Phenomenon vs. Data Layer:** Traditional research often conflates mobility itself with an observed OD matrix. RKB explicitly decouples the underlying spatial phenomenon from the observational layer (which may be incomplete, distorted, or aggregated).

##### 5. Implications for Thesis
Establishes the ontological baseline for the entire dissertation: because mobility is a regular, explainable phenomenon generated by Structure and Behaviour, OD matrices can be reconstructed even when direct OD observations are missing.

---

### Layer B — Data Revolution (Data Evolution & Observation Layers)

#### 1. Scientific Question
How has the evolution of mobility data sources transformed the observational fidelity, scale, and privacy boundaries of spatial interaction analysis?

#### 2. Core Claims
* **Claim B.1:** Mobility data collection has evolved through distinct paradigms: Travel Surveys $\to$ Census Datasets $\to$ Mobile Phone CDRs $\to$ Location-Based Services (LBS) / App Data $\to$ Open Aggregate Mobility Releases.
* **Claim B.2:** Disaggregate individual trajectories offer complete spatial detail but carry extreme re-identification risks and strict access barriers.
* **Claim B.3:** Modern platforms release aggregate mobility products—such as Meta Movement Distribution Maps (MDM)—which provide privacy-preserving aggregate travel statistics.

#### 3. Evidence Map
* **Privacy & Trajectory Limits:** de Montjoye et al. (2013) *Unique in the Crowd: The privacy bounds of human mobility* (Scientific Reports); Houssiau et al. (2022) *On the Difficulty of Achieving Differential Privacy in Practice*.
* **Aggregate Releases:** Meta AI for Good (2026) *Movement Distribution Maps (MDM)*; Pappalardo et al. (2023) *Analytical framework for aggregate mobility data*.
* **Geospatial & POI Data:** Vu et al. (2021) *Enhanced Urban Functional Land Use Map with Open Data*.

#### 4. Critical Comparison
* **Disaggregate Trajectories (High detail, high privacy risk) vs. Aggregate Mobility Releases (Spatially noded/binned, low privacy risk, high accessibility).**

#### 5. Implications for Thesis
Justifies positioning Aggregate Mobility Products (specifically Trip-Length Distributions) as the primary observational input for survey-free calibration.

---

### Layer C — Information Hierarchy (Resolution Reduction & Signature Preservation)

#### 1. Scientific Question
What statistical information survives spatial and link aggregation across mobility observation layers, and can aggregated observations retain sufficient information for parameter identification?

#### 2. Core Claims
* **Claim C.1:** Mobility evidence forms a strict Information Hierarchy characterized by spatial information reduction:
$$\text{Individual Trajectories} \longrightarrow \text{Disaggregate OD Matrix} \longrightarrow \text{Aggregate Travel Distance Distribution (TLD)} \longrightarrow \text{Scalar Summary Stats}$$
* **Claim C.2:** According to the Data Processing Inequality, spatial aggregation removes pairwise origin-destination identities.
* **Claim C.3:** Although pairwise cell-to-cell links are collapsed, aggregate TLD preserves a distinct collective statistical signature of spatial distance deterrence.

#### 3. Evidence Map
* **Information Theory Foundations:** Cover & Thomas (2006) *Elements of Information Theory*; Song et al. (2010) *Limits of Predictability in Human Mobility* (Science).
* **Aggregation Distortion:** Gallotti et al. (2024) *Distorted mobility data*; Erlander & Stewart (1990) *Interactive Spatial Interaction Models*.

#### 4. Critical Comparison
* **Traditional View:** TLD is viewed merely as an information loss or a downstream validation plot.
* **Proposed View:** TLD represents a privacy-safe, accessible observation space that retains sufficient statistical information for identifying the distance-decay parameter $\theta$.

#### 5. Implications for Thesis
Provides the theoretical foundation for **Paper 1**: proving that TLD is an information-sufficient observation layer for statistical parameter inference.

---

### Layer D — Gravity as Scientific Language (Spatial Interaction Theory)

#### 1. Scientific Question
Why should Spatial Interaction be formulated as a generative scientific language separating spatial opportunity fields from distance deterrence, rather than an arbitrary black-box function?

#### 2. Core Claims
* **Claim D.1:** Spatial interaction modeling represents a probabilistic physical-statistical language expressing trip density as an interplay between origin potential, destination attractiveness, and distance friction.
* **Claim D.2:** Major theoretical derivations—Entropy Maximization (Wilson), Stouffer's Intervening Opportunities, and Simini's Radiation Model—all share an underlying structural factorization.
* **Claim D.3:** Gravity model factorization provides explicit parameterization and scientific interpretability impossible in unconstrained deep learning.

#### 3. Evidence Map
* **Entropy & Classical Gravity:** Wilson (1971) *A family of spatial interaction models*; Tanner (1961) *Factors affecting the amount of travel*; O'Kelly (2009) *Spatial Interaction Models*.
* **Radiation & Intervening Opportunities:** Stouffer (1940); Simini et al. (2012) *A universal model for mobility and migration patterns* (Nature); Alis et al. (2021) *Generalized Radiation Model*.
* **Comparative Evaluation:** Lenormand et al. (2016) *Systematic comparison of trip generation laws*.

#### 4. Critical Comparison
* **Entropy Maximization vs. Parameter-free Radiation vs. Machine Learning Flow Regression.**

#### 5. Implications for Thesis
Establishes the mathematical formulation $T_{ij} = O_i A_j f(d_{ij}; \theta)$ as the unified integration framework for the thesis.

---

### Layer E — Behaviour (Distance Deterrence & Behaviour Identification)

#### 1. Scientific Question
How does collective human response to spatial separation manifest as distance decay, and how can distance-deterrence parameters be statistically identified without OD matrices?

#### 2. Core Claims
* **Claim E.1:** Spatial interaction behaviour is captured by the distance-deterrence function $f(d; \theta)$, reflecting collective population travel impedance.
* **Claim E.2:** Standard functional forms include Power-law ($d^{-\alpha}$), Exponential ($e^{-\beta d}$), Tanner ($d^{-\alpha} e^{-\beta d}$), and Box-Cox transformations.
* **Claim E.3:** Deterrence parameters $\theta = (\alpha, \beta)$ can be identified via multinomial maximum likelihood estimation directly from aggregate TLD, conditioned on independent urban structure.

#### 3. Evidence Map
* **Deterrence Formulations:** Tanner (1961); Martinez & Viegas (2013); Liang et al. (2013) *Unraveling the Origin of Exponential Law in Intra-urban Human Mobility*.
* **Calibration Paradigms:** Hyman (1969) *Calibration of gravity models*; Merlin (2020) *Median-based gravity calibration*; Flowerdew & Aitkin (1982) *Fitting generalized linear models to OD matrices*.
* **Parameter Identification Evidence:** Verma & Ukkusuri (2025) *What Determines Travel Time and Distance Decay*; Casella & Berger (2002) *Statistical Inference*.

#### 4. Critical Comparison
* **Conventional Survey-based OD Fitting vs. Aggregate TLD-based Multinomial Parameter Identification.**

#### 5. Implications for Thesis
Forms the core literature, likelihood derivation, and empirical validation suite for **Paper 1**.

---

### Layer F — Urban Structure (Spatial Potentials & Feature Representations)

#### 1. Scientific Question
How can urban spatial structure—specifically origin trip production $O_i$ and destination attraction potential $A_j$—be effectively represented and estimated from multi-source open spatial data?

#### 2. Core Claims
* **Claim F.1:** Urban structure encompasses the spatial distribution of opportunities, land-use intensity, population density, POI distribution, and road network centrality.
* **Claim F.2:** High-dimensional spatial features can be compressed into latent structural representations $(O_i, A_j)$ using spatial graph neural networks (GNNs) or spatial representation learning.
* **Claim F.3:** Multi-source open datasets (OpenStreetMap, WorldPop, POI registers) provide sufficient proxy signals for estimating structural opportunity potentials.

#### 3. Evidence Map
* **Urban Feature Representation:** Liu et al. (2025) *Representation learning for geospatial data* (Annals of GIS); Vu et al. (2021) *Urban Functional Land Use Map*; Alis et al. (2021) *Urbanization Index*.
* **Spatial Deep Learning Inputs:** Simini et al. (2021) *DeepGravity* (Nature Communications); Robinson et al. (2021) *Imagery2Flow*.
* **Universal Network Representation:** Guo et al. (2025) *A universal geography neural network for mobility flow prediction*.

#### 4. Critical Comparison
* **Single Proxy (Population alone) vs. Multidimensional Open Urban Features (POI + Built environment + Network centrality).**

#### 5. Implications for Thesis
Establishes the structural representation paradigm for **Paper 2**, enabling independent estimation of $(O_i, A_j)$ without target-city mobility flows.

---

### Layer G — Transferability (Cross-City Knowledge Generalization)

#### 1. Scientific Question
Under what structural and spatial conditions can urban mobility models or representation modules be transferred across cities without observing target-city OD data?

#### 2. Core Claims
* **Claim G.1:** Cross-city mobility synthesis requires transferring structural or behavioural knowledge from data-rich source cities to data-scarce target cities.
* **Claim G.2:** Existing transfer methods (e.g., DeepGravity, GODDAG, TransGM) transfer end-to-end neural representations, conflating urban structure and mobility behaviour in a black-box.
* **Claim G.3:** Separating structure from behaviour enables zero-shot structural transfer while identifying city-specific behaviour independently from local aggregate TLD.

#### 3. Evidence Map
* **Domain Adaptation & GNN Transfer:** Rong, Feng, & Ding (2023) *GODDAG: Generating Origin-Destination Flow for New Cities Via Domain Adversarial Training* (IEEE TKDE).
* **Transferable Gravity & Neural Baselines:** Enaya et al. (2026) *TransGM: Transferable gravity models*; Simini et al. (2021) *DeepGravity*; Liu et al. (2025) *NeuroGravity*.
* **Predictability Limits in Zero-Data Settings:** Yang et al. (2014) *Limits of Predictability in Commuting Flows in the Absence of Data for Calibration* (Scientific Reports).

#### 4. Critical Comparison
* **Sub-categories of Transferability:**
  * **G1 — Transfer Behaviour:** Assuming distance-decay parameters $\theta$ are universal across cities (invalidated by urban scale differences).
  * **G2 — Transfer Structure:** Transferring structural opportunity mappings $(O_i, A_j)$ from urban features across similar urban typologies (Thesis Approach).
  * **G3 — End-to-End Black-box Neural Transfer:** Transferring joint neural embeddings via GNN/Domain Adversarial Training (GODDAG / TransGM).

#### 5. Implications for Thesis
Defines the methodological benchmark and state-of-the-art contrast for **Paper 2**.

---

### Layer H — Research Gap & Convergence (Unified Methodological Framework)

#### 1. Scientific Question
How do the gaps across Layers A–G converge to necessitate the **Structure–Behaviour Separation Principle** and the unified mobility reconstruction framework?

#### 2. Core Claims
* **Gap 1 (Addressed by Paper 1):** Existing studies treat aggregate TLD as a downstream evaluation metric rather than a primary observation space for statistical parameter identification. No prior framework extracts multinomial likelihoods from aggregate TLD to identify distance-decay behaviour $\theta$.
* **Gap 2 (Addressed by Paper 2):** Current transfer learning models (GODDAG, DeepGravity, TransGM) transfer end-to-end black-box representations, conflating urban structure and distance deterrence. No framework enables independent transfer of urban structure $(O_i, A_j)$ while conditioning on locally identified behaviour $\theta$.
* **Unified Convergence:** Reconstructing OD matrices in data-scarce cities requires unifying aggregate-identified behaviour $\theta$ (Paper 1) and open-data estimated structure $(O_i, A_j)$ (Paper 2) via the gravity factorization $T_{ij} = O_i A_j f(d_{ij}; \theta)$.

#### 3. Evidence Map
* **Synthesized Evidence Base:** Integrates Wilson (1971), Barbosa et al. (2018), Cover & Thomas (2006), Simini et al. (2021), Rong et al. (2023), and Verma & Ukkusuri (2025).

#### 4. Critical Comparison
* **Summary Table of Literature Gaps vs. Thesis Contributions:**

| Dimension | Conventional Gravity | Deep Transfer (GODDAG / TransGM) | Proposed Thesis Framework |
| :--- | :--- | :--- | :--- |
| **Observation Input** | Target-city OD matrix / Surveys | Source-city OD + Target urban features | Target aggregate TLD + Open urban features |
| **Structure--Behaviour Status** | Combined in fitting | Conflated in neural embedding | **Explicitly Separated** ($O_i, A_j$ vs. $f(d;\theta)$) |
| **Parameter Interpretability** | High ($\theta$ explicit) | Low (Black-box neural weights) | **High** ($\theta$ identified + $O_i, A_j$ explicit) |
| **Target City Requirement** | Full OD survey required | Zero OD, but requires OD-rich source city | **Zero target OD; uses local aggregate TLD** |

#### 5. Implications for Thesis
Directly leads to the 5 Expected Scientific Contributions and the Ho Chi Minh City case study validation.

---

## 4. Mapping RKB Layers to Thesis Deliverables

```text
┌─────────────────────────────────────────┬───────────────────────────┬───────────────────────────┐
│ Research Knowledge Base (RKB) Layer     │ PhD Proposal Section      │ Target Publication        │
├─────────────────────────────────────────┼───────────────────────────┼───────────────────────────┤
│ Layer A (Why Human Mobility?)           │ 1. Motivation             │ Both Papers (Intro)       │
│ Layer B (Data Revolution)               │ 1. Motivation             │ Paper 1 & Paper 2         │
│ Layer C (Information Hierarchy)         │ 3. Scientific Principle   │ Paper 1 (Foundations)     │
│ Layer D (Gravity as Scientific Lang)    │ 3. Scientific Principle   │ Both Papers (Methodology) │
│ Layer E (Behaviour & Identification)    │ 7. Paper 1 Scope          │ Paper 1 (Main Target)     │
│ Layer F (Urban Structure)               │ 8. Paper 2 Scope          │ Paper 2 (Main Target)     │
│ Layer G (Transferability)               │ 8. Paper 2 Scope          │ Paper 2 (Related Work)    │
│ Layer H (Research Gap & Convergence)    │ 2. Gap & 11. Contributions│ PhD Dissertation Synthesis│
└─────────────────────────────────────────┴───────────────────────────┴───────────────────────────┘
```

---
*Status: Frozen Operating Blueprint V1.0 — System Master Standard for Research Program.*
