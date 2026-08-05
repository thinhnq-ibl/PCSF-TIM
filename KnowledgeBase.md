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

### Executive Scientific Matrix

| Layer | One Scientific Question | Scientific Outcome |
| :---: | :--- | :--- |
| **Layer A** | What is Urban Human Mobility? | Define the scientific object. |
| **Layer B** | How can Urban Human Mobility be observed? | Define the observation space. |
| **Layer C** | What information is preserved by each observation? | Define the information hierarchy. |
| **Layer D** | What scientific principle governs Urban Mobility? | Establish the Gravity Principle. |
| **Layer E** | What hidden mechanism generates collective mobility? | Human Travel Behaviour (Paper 1). |
| **Layer F** | What observable mechanism supports mobility? | Urban Structure (Paper 2). |
| **Layer G** | How has the community modelled Urban Mobility? | Existing paradigms and assumptions. |
| **Layer H** | What scientific questions remain unanswered? | Research gaps (Knowledge $\to$ Gap). |

---

### Knowledge Tree Navigation

```text
Layer A: Defining Urban Human Mobility (Scientific Object)
   │
   ▼
Layer B: The Urban Mobility Data Revolution (Observation Space)
   │
   ▼
Layer C: Information Hierarchy (Information Preservation)
   │
   ▼
Layer D: Gravity as Scientific Language (Gravity Principle)
   │
   ▼
Layer E: Human Travel Behaviour (Hidden Mechanism & Identification) ───► Paper 1
   │
   ▼
Layer F: Urban Structure (Observable Mechanism & Feature Potentials) ───► Paper 2
   │
   ▼
Layer G: The Conventional Paradigm & Transferability (Existing Models & Assumptions)
   │
   ▼
Layer H: Scientific Synthesis & Research Gaps (Knowledge → Gap Transition)
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

### Layer B — The Urban Mobility Data Revolution (Observation Space)

#### 1. Scientific Master Matrix for Layer B

| Section | Scientific Question | Core Claim | Purpose in Proposal | Connection to Later Layers |
| :--- | :--- | :--- | :--- | :--- |
| **B. The Urban Mobility Data Revolution** | How has Urban Mobility become observable? | Mobility observations have evolved dramatically during the last decades. | Introduce the evolution of mobility observation. | Foundation of Information Hierarchy. |
| **B1. Survey Era** | How was mobility traditionally measured? | Household Travel Surveys (HTS) established the first systematic observation of urban mobility but are expensive and infrequently updated. | Historical baseline. | Motivation for alternative data. |
| **B2. Digital Mobility Era** | What changed with digital technologies? | GPS, mobile phones, smart cards and LBS dramatically increased the quantity and temporal resolution of mobility observations. | Explain the data revolution. | Richer observations. |
| **B3. Open Urban Data Era** | What information is publicly available today? | OpenStreetMap, GTFS, POIs, satellite imagery, census and remote sensing provide abundant descriptions of urban structure. | Introduce publicly available data. | Foundation for Paper 2. |
| **B4. Data Abundance Paradox** | Does abundant data imply complete mobility knowledge? | Despite abundant urban data, complete OD matrices remain unavailable for most cities. | Introduce the central paradox. | Motivation of proposal. |
| **B5. Transition** | What information is actually preserved by different observations? | Different datasets preserve different levels of mobility information. | Transition. | Layer C: Information Hierarchy. |

---

#### 2. Detailed Scientific Breakdown

##### 1. Scientific Question
How has the evolution of mobility data sources transformed the observational fidelity, scale, and privacy boundaries of spatial interaction analysis?

##### 2. Core Claims
* **Claim B.1:** Mobility data collection has evolved through distinct paradigms: Travel Surveys $\to$ Census Datasets $\to$ Mobile Phone CDRs $\to$ Location-Based Services (LBS) / App Data $\to$ Open Aggregate Mobility Releases.
* **Claim B.2:** Disaggregate individual trajectories offer complete spatial detail but carry extreme re-identification risks and strict access barriers.
* **Claim B.3:** Modern platforms release aggregate mobility products—such as Meta Movement Distribution Maps (MDM)—which provide privacy-preserving aggregate travel statistics.

##### 3. Evidence Map
* **Privacy & Trajectory Limits:** de Montjoye et al. (2013) *Unique in the Crowd: The privacy bounds of human mobility* (Scientific Reports); Houssiau et al. (2022) *On the Difficulty of Achieving Differential Privacy in Practice*.
* **Aggregate Releases:** Meta AI for Good (2026) *Movement Distribution Maps (MDM)*; Pappalardo et al. (2023) *Analytical framework for aggregate mobility data*.
* **Geospatial & POI Data:** Vu et al. (2021) *Enhanced Urban Functional Land Use Map with Open Data*.

##### 4. Critical Comparison
* **Disaggregate Trajectories (High detail, high privacy risk) vs. Aggregate Mobility Releases (Spatially noded/binned, low privacy risk, high accessibility).**

##### 5. Implications for Thesis
Justifies positioning Aggregate Mobility Products (specifically Trip-Length Distributions) as the primary observational input for survey-free calibration.

---

### Layer C — Information Hierarchy of Urban Mobility Observations

#### 1. Scientific Master Matrix for Layer C

| Section | Scientific Question | Core Claim | Purpose in Proposal | Connection to Later Layers |
| :--- | :--- | :--- | :--- | :--- |
| **C. Information Hierarchy of Urban Mobility Observations** | How much information is preserved by different observations? | Different observations preserve different amounts of mobility information. | Establish the theoretical foundation. | Foundation for Paper 1. |
| **C1. Observation vs Information** | Is more data equivalent to more information? | Data quantity and information content are fundamentally different concepts. | Introduce information perspective. | Hierarchy construction. |
| **C2. Mobility Observation Hierarchy** | How can mobility observations be organized? | Mobility observations can be ordered according to information preservation. | Introduce the hierarchy. | Information loss analysis. |
| **C3. Information Loss** | What information is lost during aggregation? | Every aggregation operation removes certain dimensions of mobility information. | Explain irreversible aggregation. | Behaviour inference. |
| **C4. Information Sufficiency** | Which observations remain sufficient for scientific inference? | Some aggregate observations still preserve sufficient statistical information for identifying behavioural mechanisms. | Scientific justification for Paper 1. | Behaviour Identification. |
| **C5. Transition** | What behavioural information is preserved? | Distance distributions preserve statistical information about travel behaviour. | Transition. | Layer D / Paper 1. |

---

#### 2. Detailed Scientific Breakdown

##### 1. Scientific Question
What statistical information survives spatial and link aggregation across mobility observation layers, and can aggregated observations retain sufficient information for parameter identification?

##### 2. Core Claims
* **Claim C.1:** Mobility evidence forms a strict Information Hierarchy characterized by spatial information reduction:
$$\text{Individual Trajectories} \longrightarrow \text{Disaggregate OD Matrix} \longrightarrow \text{Aggregate Travel Distance Distribution (TLD)} \longrightarrow \text{Scalar Summary Stats}$$
* **Claim C.2:** According to the Data Processing Inequality, spatial aggregation removes pairwise origin-destination identities.
* **Claim C.3:** Although pairwise cell-to-cell links are collapsed, aggregate TLD preserves a distinct collective statistical signature of spatial distance deterrence.

##### 3. Evidence Map
* **Information Theory Foundations:** Cover & Thomas (2006) *Elements of Information Theory*; Song et al. (2010) *Limits of Predictability in Human Mobility* (Science).
* **Aggregation Distortion:** Gallotti et al. (2024) *Distorted mobility data*; Erlander & Stewart (1990) *Interactive Spatial Interaction Models*.

##### 4. Critical Comparison
* **Traditional View:** TLD is viewed merely as an information loss or a downstream validation plot.
* **Proposed View:** TLD represents a privacy-safe, accessible observation space that retains sufficient statistical information for identifying the distance-decay parameter $\theta$.

##### 5. Implications for Thesis
Provides the theoretical foundation for **Paper 1**: supporting the hypothesis that TLD is an information-sufficient observation layer for statistical parameter inference.

---

### Layer D — Gravity as Scientific Language (Spatial Interaction Theory)

#### 1. Scientific Master Matrix for Layer D

| Section | Scientific Question | Core Claim | Purpose in Proposal | Connection to Later Layers |
| :--- | :--- | :--- | :--- | :--- |
| **D. Gravity as the Scientific Language** | How should collective mobility be represented? | Gravity provides a general scientific language for describing spatial interaction. | Introduce the conceptual framework. | Foundation of the proposal. |
| **D1. Spatial Interaction** | What is the essence of urban mobility? | Urban mobility is fundamentally a spatial interaction process between origins and destinations. | Define the phenomenon mathematically. | Gravity principle. |
| **D2. Gravity Principle** | Why has gravity remained central for decades? | Mobility emerges from the interaction between opportunity and travel impedance. | Introduce gravity as a principle rather than a model. | Unified interpretation. |
| **D3. Gravity Models** | How has the gravity principle been implemented? | Different gravity models represent different mathematical realizations of the same underlying principle. | Literature organization. | Behaviour models. |
| **D4. Behaviour and Structure** | What are the components of gravity? | Gravity separates naturally into Urban Structure and Human Travel Behaviour. | Introduce the proposal's conceptual separation. | Paper 1 & Paper 2. |
| **D5. Transition** | Which component remains poorly understood? | Behaviour remains the least directly observable component. | Transition to Layer E. | Layer E / Paper 1. |

---

#### 2. Detailed Scientific Breakdown

##### 1. Scientific Question
Why should Spatial Interaction be formulated as a generative scientific language separating spatial opportunity fields from distance deterrence, rather than an arbitrary black-box function?

##### 2. Core Claims
* **Claim D.1:** Spatial interaction modeling represents a probabilistic physical-statistical language expressing trip density as an interplay between origin potential, destination attractiveness, and distance friction.
* **Claim D.2:** Major theoretical derivations—Entropy Maximization (Wilson), Stouffer's Intervening Opportunities, and Simini's Radiation Model—all share an underlying structural factorization.
* **Claim D.3:** Gravity model factorization provides explicit parameterization and scientific interpretability impossible in unconstrained deep learning.

##### 3. Evidence Map
* **Entropy & Classical Gravity:** Wilson (1971) *A family of spatial interaction models*; Tanner (1961) *Factors affecting the amount of travel*; O'Kelly (2009) *Spatial Interaction Models*.
* **Radiation & Intervening Opportunities:** Stouffer (1940); Simini et al. (2012) *A universal model for mobility and migration patterns* (Nature); Alis et al. (2021) *Generalized Radiation Model*.
* **Comparative Evaluation:** Lenormand et al. (2016) *Systematic comparison of trip generation laws*.

##### 4. Critical Comparison
* **Entropy Maximization vs. Parameter-free Radiation vs. Machine Learning Flow Regression.**

##### 5. Implications for Thesis
Establishes the mathematical formulation $T_{ij} = O_i A_j f(d_{ij}; \theta)$ as the unified integration framework for the thesis.

---

### Layer E — Human Travel Behaviour as the Hidden Mechanism

#### 1. Scientific Master Matrix for Layer E

| Section | Scientific Question | Core Claim | Purpose in Proposal | Connection to Later Layers |
| :--- | :--- | :--- | :--- | :--- |
| **E. Human Travel Behaviour as the Hidden Mechanism** | What behavioural mechanism governs mobility? | Travel behaviour determines how people respond to spatial separation. | Introduce behaviour as the hidden component. | Paper 1. |
| **E1. What is Human Travel Behaviour?** | What does behaviour mean in collective mobility? | Behaviour is the collective response of travellers to travel impedance under a given urban environment. | Define behaviour scientifically. | Behaviour modelling. |
| **E2. Behaviour vs Urban Structure** | How is behaviour different from structure? | Structure provides opportunities; behaviour determines choices. | Formalize the separation principle. | Proposal foundation. |
| **E3. Distance Sensitivity** | How is behaviour expressed? | Behaviour manifests primarily through distance sensitivity. | Connect behaviour to observable quantities. | Distance-decay. |
| **E4. Distance-decay as Behaviour Representation** | How is behaviour mathematically represented? | Distance-decay functions are behavioural representations rather than merely mathematical fitting functions. | Reinterpret distance-decay. | Behaviour identification. |
| **E5. The Behaviour Identification Problem** | Can behaviour be identified from aggregate observations? | Behaviour cannot be directly observed and must be statistically inferred. | Introduce Paper 1. | Paper 1. |

---

#### 2. Detailed Scientific Breakdown

##### 1. Scientific Question
How does collective human response to spatial separation manifest as distance decay, and how can distance-deterrence parameters be statistically identified without OD matrices?

##### 2. Core Claims
* **Claim E.1:** Spatial interaction behaviour is captured by the distance-deterrence function $f(d; \theta)$, reflecting collective population travel impedance.
* **Claim E.2:** Standard functional forms include Power-law ($d^{-\alpha}$), Exponential ($e^{-\beta d}$), Tanner ($d^{-\alpha} e^{-\beta d}$), and Box-Cox transformations.
* **Claim E.3:** Deterrence parameters $\theta = (\alpha, \beta)$ can be statistically inferred via multinomial maximum likelihood estimation directly from aggregate TLD, conditioned on independent urban structure.

##### 3. Evidence Map
* **Deterrence Formulations:** Tanner (1961); Martinez & Viegas (2013); Liang et al. (2013) *Unraveling the Origin of Exponential Law in Intra-urban Human Mobility*.
* **Calibration Paradigms:** Hyman (1969) *Calibration of gravity models*; Merlin (2020) *Median-based gravity calibration*; Flowerdew & Aitkin (1982) *Fitting generalized linear models to OD matrices*.
* **Parameter Identification Evidence:** Verma & Ukkusuri (2025) *What Determines Travel Time and Distance Decay*; Casella & Berger (2002) *Statistical Inference*.

##### 4. Critical Comparison
* **Conventional Survey-based OD Fitting vs. Aggregate TLD-based Multinomial Parameter Identification.**

##### 5. Implications for Thesis
Forms the core literature, likelihood derivation, and empirical validation suite for **Paper 1**.

---

### Layer F — Urban Structure (Observable Mechanism & Feature Potentials)

#### 1. Scientific Master Matrix for Layer F

| Section | Scientific Question | Core Claim | Purpose in Proposal | Connection to Later Layers |
| :--- | :--- | :--- | :--- | :--- |
| **F. Urban Structure as the Observable Mechanism** | What observable mechanism supports mobility? | Urban spatial structure provides the spatial opportunity field $(O_i, A_j)$ supporting collective trips. | Introduce urban structure as the observable component. | Paper 2. |
| **F1. Spatial Opportunities** | What is urban structure? | Urban structure consists of spatial distributions of population, land use, POIs, and road networks. | Define urban structure mathematically. | Feature representation. |
| **F2. Feature Representation** | How can urban structure be quantified? | Open spatial data can be represented as structural potential fields $(O_i, A_j)$ via spatial GNNs or feature aggregation. | Structural estimation without flows. | Paper 2 methodology. |
| **F3. Transferability of Structure** | Can urban structure be transferred? | Structural opportunity mappings are transferable across cities with similar spatial typologies. | Justify structural transfer. | Cross-city generalization. |
| **F4. Open Data Feasibility** | Is open data sufficient? | Multi-source open data (OSM, WorldPop, POI registers) provide adequate proxy signals for structural potentials. | Data feasibility. | Survey-free estimation. |
| **F5. Transition** | How do existing models treat urban structure? | Existing paradigms conflate structure with behavior into end-to-end black boxes. | Transition to Layer G. | Layer G. |

---

#### 2. Detailed Scientific Breakdown

##### 1. Scientific Question
How can urban spatial structure—specifically origin trip production $O_i$ and destination attraction potential $A_j$—be effectively represented and estimated from multi-source open spatial data?

##### 2. Core Claims
* **Claim F.1:** Urban structure encompasses the spatial distribution of opportunities, land-use intensity, population density, POI distribution, and road network centrality.
* **Claim F.2:** High-dimensional spatial features can be compressed into latent structural representations $(O_i, A_j)$ using spatial graph neural networks (GNNs) or spatial representation learning.
* **Claim F.3:** Multi-source open datasets (OpenStreetMap, WorldPop, POI registers) provide sufficient proxy signals for estimating structural opportunity potentials.

##### 3. Evidence Map
* **Urban Feature Representation:** Liu et al. (2025) *Representation learning for geospatial data* (Annals of GIS); Vu et al. (2021) *Urban Functional Land Use Map*; Alis et al. (2021) *Urbanization Index*.
* **Spatial Deep Learning Inputs:** Simini et al. (2021) *DeepGravity* (Nature Communications); Robinson et al. (2021) *Imagery2Flow*.
* **Universal Network Representation:** Guo et al. (2025) *A universal geography neural network for mobility flow prediction*.

##### 4. Critical Comparison
* **Single Proxy (Population alone) vs. Multidimensional Open Urban Features (POI + Built environment + Network centrality).**

##### 5. Implications for Thesis
Establishes the structural representation paradigm for **Paper 2**, enabling independent estimation of $(O_i, A_j)$ without target-city mobility flows.

---

### Layer G — The Conventional Paradigm & Transferability

#### 1. Scientific Master Matrix for Layer G

| Section | Scientific Question | Core Claim | Purpose in Proposal | Connection to Later Layers |
| :--- | :--- | :--- | :--- | :--- |
| **G. The Conventional Paradigm & Transferability** | How has the community traditionally modelled urban mobility? | Existing approaches share a common paradigm requiring direct target mobility observations or black-box neural transfer. | Review conventional paradigms & transfer learning. | Layer H. |
| **G1. Model Calibration** | How are mobility models calibrated? | Behavioural parameters are estimated using observed target OD matrices or individual trajectories. | Review conventional workflow. | Hidden assumptions. |
| **G2. Data Dependency** | What data do current models require? | Most models assume access to detailed mobility observations, creating a severe data scarcity barrier. | Reveal data scarcity problem. | Motivation for new paradigm. |
| **G3. Modern Deep Learning & Transfer** | Has AI changed the paradigm? | Deep learning (e.g., GODDAG, TransGM, DeepGravity) improves prediction but transfers end-to-end black-box representations. | Show limitations of neural transfer. | Transfer learning limits. |
| **G4. Fundamental Limitation** | What is the common limitation? | Existing methods conflate urban structure and travel behavior rather than decoupling transferable knowledge. | Identify core paradigm limit. | Layer H. |
| **G5. Transition** | Where do these limitations lead? | The conventional paradigm leaves fundamental scientific questions unresolved. | Transition to Layer H. | Layer H. |

---

#### 2. Detailed Scientific Breakdown

##### 1. Scientific Question
Under what structural and spatial conditions can urban mobility models or representation modules be transferred across cities without observing target-city OD data?

##### 2. Core Claims
* **Claim G.1:** Cross-city mobility synthesis requires transferring structural or behavioural knowledge from data-rich source cities to data-scarce target cities.
* **Claim G.2:** Existing transfer methods (e.g., DeepGravity, GODDAG, TransGM) transfer end-to-end neural representations, conflating urban structure and mobility behaviour in a black-box.
* **Claim G.3:** Separating structure from behaviour enables zero-shot structural transfer while identifying city-specific behaviour independently from local aggregate TLD.

##### 3. Evidence Map
* **Domain Adaptation & GNN Transfer:** Rong, Feng, & Ding (2023) *GODDAG: Generating Origin-Destination Flow for New Cities Via Domain Adversarial Training* (IEEE TKDE).
* **Transferable Gravity & Neural Baselines:** Enaya et al. (2026) *TransGM: Transferable gravity models*; Simini et al. (2021) *DeepGravity*; Liu et al. (2025) *NeuroGravity*.
* **Predictability Limits in Zero-Data Settings:** Yang et al. (2014) *Limits of Predictability in Commuting Flows in the Absence of Data for Calibration* (Scientific Reports).

##### 4. Critical Comparison
* **Sub-categories of Transferability:**
  * **G1 — Transfer Behaviour:** Assuming distance-decay parameters $\theta$ are universal across cities (invalidated by urban scale differences).
  * **G2 — Transfer Structure:** Transferring structural opportunity mappings $(O_i, A_j)$ from urban features across similar urban typologies (Thesis Approach).
  * **G3 — End-to-End Black-box Neural Transfer:** Transferring joint neural embeddings via GNN/Domain Adversarial Training (GODDAG / TransGM).

##### 5. Implications for Thesis
Defines the methodological benchmark and state-of-the-art contrast for **Paper 2**.

---

### Layer H — Scientific Synthesis and Research Gaps

#### Mission
To synthesize the scientific knowledge established in the previous layers (A–G) and identify the unresolved scientific questions that motivate future research.

---

#### 1. Scientific Master Matrix for Layer H

| Section | Scientific Question | Outcome | Purpose | Leads to |
| :--- | :--- | :--- | :--- | :--- |
| **H. Scientific Synthesis and Research Gaps** | How does established scientific knowledge synthesize into core research gaps? | Knowledge $\to$ Gap Transition | Synthesize the entire literature foundation. | Research Proposal. |
| **H1. Scientific Consensus** | What has been established? | Scientific Consensus | Consolidate established facts across Layers A–G. | Identify boundaries of knowledge. |
| **H2. Scientific Uncertainties** | What remains uncertain? | Scientific Uncertainties | Highlight unresolved assumptions in current paradigms. | Reveal critical scientific limitations. |
| **H3. Research Gaps** | What are the unresolved research gaps? | Research Gaps | Formulate precise scientific gaps (Behavior & Structure). | Motivate scientific needs. |
| **H4. Scientific Significance** | Why do these gaps matter? | Scientific Significance | Establish why closing these gaps is scientifically essential. | Value to urban mobility science. |
| **H5. Transition** | Where do these gaps lead? | Proposal | Transition from Knowledge Base to Research Proposal. | Research Proposal. |

---

#### 2. Detailed Scientific Breakdown

##### 1. Scientific Question
How does the accumulated scientific evidence across Layers A–G synthesize into established consensus, scientific uncertainties, and critical research gaps?

##### 2. Core Claims
* **Claim H.1 (Scientific Consensus):** Urban mobility is a regular, explainable spatial interaction phenomenon emerging from Urban Structure and Travel Behaviour. Observations conform to an Information Hierarchy where aggregate distance distributions (TLD) preserve statistical signatures of travel friction.
* **Claim H.2 (Scientific Uncertainties):** It remains uncertain whether aggregate TLDs contain sufficient statistical information to identify behavioral parameters $\theta$ without observed OD flows, and whether urban spatial structure $(O_i, A_j)$ can be transferred cross-city without conflating it with local travel behavior.
* **Claim H.3 (Research Gaps):**
  * **Gap 1 (Behaviour Identification):** Lack of a multinomial likelihood inference formulation to extract distance-decay parameters directly from aggregate TLDs.
  * **Gap 2 (Structure Transferability):** Lack of an independent representation transfer mechanism that decouples transferable urban opportunity potentials from city-specific travel behavior.
* **Claim H.4 (Scientific Significance):** Resolving these gaps enables survey-free, privacy-preserving mobility reconstruction in data-scarce cities, bridging aggregate observational releases with open spatial data.

##### 3. Evidence Map
* **Synthesized Literature Base:** Integrates Wilson (1971), Barbosa et al. (2018), Cover & Thomas (2006), de Montjoye et al. (2013), Simini et al. (2021), Rong et al. (2023), and Verma & Ukkusuri (2025).

##### 4. Critical Comparison
* **Scientific Consensus vs. Scientific Uncertainties & Gaps:**

| Layer / Dimension | Established Scientific Consensus (Layers A–G) | Remaining Scientific Uncertainty & Gap |
| :--- | :--- | :--- |
| **Data & Information** | Aggregation preserves distance decay signatures (TLD). | Whether TLD is *sufficient* for full behavioral parameter identification. |
| **Spatial Interaction** | Gravity factorizes into Structure $(O_i, A_j)$ and Behaviour $f(d;\theta)$. | Existing models conflate structure and behavior into end-to-end black-boxes during cross-city transfer. |
| **Model Calibration** | Conventional models require observed target OD matrices. | Lack of zero-target-OD calibration methods leveraging open urban data + local aggregate TLD. |

##### 5. Implications for Thesis
Provides the complete, self-contained literature synthesis (Knowledge $\to$ Gap), serving as the direct scientific bridge into the Research Proposal.

---

## 4. Mapping RKB Layers to Thesis Deliverables

```text
┌─────────────────────────────────────────┬───────────────────────────┬───────────────────────────┐
│ Research Knowledge Base (RKB) Layer     │ PhD Proposal Section      │ Target Publication        │
├─────────────────────────────────────────┼───────────────────────────┼───────────────────────────┤
│ Layer A (Defining Scientific Object)    │ 1. Motivation             │ Both Papers (Intro)       │
│ Layer B (Data Revolution)               │ 1. Motivation             │ Paper 1 & Paper 2         │
│ Layer C (Information Hierarchy)         │ 3. Scientific Principle   │ Paper 1 (Foundations)     │
│ Layer D (Gravity as Scientific Lang)    │ 3. Scientific Principle   │ Both Papers (Methodology) │
│ Layer E (Human Travel Behaviour)        │ 7. Paper 1 Scope          │ Paper 1 (Main Target)     │
│ Layer F (Urban Structure Potentials)    │ 8. Paper 2 Scope          │ Paper 2 (Main Target)     │
│ Layer G (Conventional Paradigm & AI)    │ 2. Literature Review      │ Both Papers (Related Work)│
│ Layer H (Scientific Synthesis & Gaps)   │ 2. Gap & Contributions    │ PhD Dissertation Synthesis│
└─────────────────────────────────────────┴───────────────────────────┴───────────────────────────┘
```

---
*Status: Frozen Operating Blueprint V1.0 — System Master Standard for Research Program.*
