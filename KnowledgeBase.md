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

| Section | Scientific Question | Core Claim | Main Supporting References (APA) | Role of Literature |
| :--- | :--- | :--- | :--- | :--- |
| **A. Defining Urban Human Mobility as the Scientific Object** | What is the scientific object of this research? | Urban Human Mobility is a legitimate scientific object for quantitative investigation. | Barbosa, H., et al. (2018). *Human mobility: Models and applications*. **Physics Reports, 734, 1–74**. | Foundational review of Human Mobility Science. |
| **A1. Urban Human Mobility in the Open Data Era** | Why has Urban Human Mobility become a timely scientific problem? | Modern cities have become increasingly observable through publicly available spatial data. | Guo, Y., et al. (2025). *A universal geography neural network for mobility flow prediction in planning*. **CACE**; Liu et al. (2025). *Representation Learning for Geospatial Data*. | Demonstrates the growth of open urban data and geospatial representations. |
| **A2. Urban Mobility as Urban Intelligence** | Why is mobility fundamental to modern cities? | Urban mobility has become a fundamental information layer supporting transportation, planning and urban intelligence. | Barbosa et al. (2018); Big Mobile Data Review; Guo et al. (2025). | Role of mobility in modern urban applications. |
| **A3. Urban Mobility is Observable** | Can Urban Human Mobility be observed? | Urban mobility leaves observable traces through multiple complementary observation layers. | Barbosa et al. (2018); Zheng, Y. (2015). *Trajectory Data Mining*; Big Mobile Data Review. | Synthesizes observation sources: surveys, GPS, CDR, LBS, OD, trajectories. |
| **A4. Urban Mobility is Measurable** | Can Urban Human Mobility be quantitatively measured? | Urban mobility can be quantified using flows, trip distances, travel times, accessibility and other statistical indicators. | Barbosa et al. (2018). | Standard quantitative indicators in Human Mobility Science. |
| **A5. Urban Mobility Exhibits Regularities** | Does Urban Mobility exhibit scientific regularities? | Collective urban mobility exhibits robust statistical regularities despite heterogeneous individual behaviour. | Barbosa et al. (2018); Simini, F., et al. (2012). *A universal model for mobility and migration patterns*. **Nature**; Liang, X., et al. (2013). *Scientific Reports*. | Foundation for Gravity, Radiation, and distance-decay laws. |
| **A6. Urban Mobility is Explainable** | Can Urban Mobility be scientifically explained? | Collective mobility arises from systematic interactions rather than random movements. | Barbosa et al. (2018); Wilson, A. G. (1971). *A family of spatial interaction models*; Simini et al. (2012). | Basis for transition to the Gravity Principle (Layer D). |
| **A7. Urban Mobility is Predictable** | Can Urban Mobility be predicted or reconstructed? | The existence of stable regularities makes statistical modelling and reconstruction scientifically meaningful. | Barbosa et al. (2018); Simini et al. (2021). *DeepGravity* (**Nature Comm**); Guo et al. (2025). | Links to modern predictive models and generative reconstruction. |
| **A8. Transition to Layer B** | If Urban Mobility is observable, why is it still difficult to understand? | The challenge is no longer the absence of data, but the diversity, incompleteness and accessibility of mobility observations. | Big Mobile Data Review; Open Mobility Dataset papers; Barbosa et al. (2018). | Direct bridge to Layer B (Urban Mobility Data Revolution). |

---

#### 2. Detailed Scientific Breakdown

##### 1. Scientific Question
What is the scientific object of this research, why does intra-urban collective mobility satisfy the requirements of a scientific object, and how is the phenomenon distinguished from its empirical measurements?

##### 2. Core Claims
* **Claim A.1 (Phenomenon vs Dataset):** Urban Human Mobility is an underlying spatio-temporal phenomenon (the collective spatial movement of people within an urban system arising from daily activities), not any single dataset or measurement layer.
* **Claim A.2 (Essential Characteristics of the Scientific Object):** Intra-urban collective mobility is a legitimate scientific object because it is:
  1. **Observable:** Leaves physical traces across surveys, GPS, CDR, LBS, and aggregate travel-distance distributions.
  2. **Measurable:** Quantifiable via spatial flows ($T_{ij}$), trip lengths, travel times, and accessibility indices.
  3. **Regular:** Displays robust statistical regularities (distance-decay laws, spatial scaling).
  4. **Explainable:** Emerges from systematic interaction between Urban Structure ($(O_i, A_j)$) and Travel Behaviour ($f(d;\theta)$).
  5. **Predictable:** Stable regularities allow generative reconstruction in unobserved cities.
* **Claim A.3 (Ontological Definition):** *Urban Human Mobility is defined as the collective spatial interaction of people within an urban system, emerging from the interaction between Urban Structure and Human Travel Behaviour, and manifested through observable mobility patterns.*

##### 3. Evidence Map
* **Foundational Surveys:** Barbosa et al. (2018) *Human mobility: Models and applications* (Physics Reports); Zheng (2015) *Trajectory Data Mining*.
* **Open Urban Data & Deep Mobility:** Guo et al. (2025) *A universal geography neural network for mobility flow prediction* (CACE); Liu et al. (2025) *Representation Learning for Geospatial Data*; Simini et al. (2021) *DeepGravity* (Nature Communications).
* **Statistical Regularities & Gravity Foundations:** Wilson (1971) *Spatial interaction models*; Simini et al. (2012) *Nature*; Liang et al. (2013) *Scientific Reports*.

##### 4. Critical Comparison
* **Phenomenon vs. Data Layer:** Traditional research often conflates mobility itself with an observed OD matrix. RKB explicitly decouples the underlying spatial phenomenon from the observational layer (which may be incomplete, distorted, or aggregated).

##### 5. Implications for Thesis
Establishes the ontological baseline for the entire dissertation: because mobility is a regular, explainable phenomenon generated by Structure and Behaviour, OD matrices can be reconstructed even when direct OD observations are missing.

---

### Layer B — The Evolution of Urban Mobility Observations (Observation Space)

#### 1. Scientific Master Matrix for Layer B

| Section | Scientific Question | Core Claim | Main Supporting References (APA) | Role in the RKB |
| :--- | :--- | :--- | :--- | :--- |
| **B. The Evolution of Urban Mobility Observations** | How has Urban Human Mobility become observable? | Advances in sensing technologies and digital infrastructures have fundamentally transformed the observation of urban mobility. | Barbosa, H., et al. (2018). *Human mobility: Models and applications*. **Physics Reports, 734**, 1–74; Big Mobile Data Review. | Introduce the evolution of mobility observations. |
| **B1. The Survey Era** | How was urban mobility traditionally observed? | Household Travel Surveys established the first systematic observations of urban mobility but remain expensive, sparse, and infrequently updated. | Barbosa et al. (2018); Zheng, Y. (2015). *Trajectory Data Mining*. | Historical baseline of mobility observation. |
| **B2. The Digital Mobility Era** | How did digital technologies transform mobility observation? | GPS, mobile phones, smart cards and LBS dramatically improved the spatial and temporal resolution of mobility observations. | Barbosa et al. (2018); Zheng (2015); Big Mobile Data Review. | Demonstrate the digital transformation of mobility observations. |
| **B3. The Open Urban Data Era** | What urban information is publicly available today? | Public datasets such as OpenStreetMap, GTFS, POIs, census, building footprints and satellite imagery provide rich descriptions of urban structure. | Guo, Y., et al. (2025). *A universal geography neural network for mobility flow prediction in planning*; Liu et al. (2025). *Representation Learning for Geospatial Data*; Open Datasets papers. | Introduce the modern open-data ecosystem. |
| **B4. Modern Urban Mobility Observations** | How is Urban Human Mobility observed today? | Modern urban mobility is observed through multiple complementary observation layers rather than a single data source, including aggregate products such as Meta Movement Distribution Maps (MDM). | Barbosa et al. (2018); Zheng (2015); Meta AI for Good (2026) *Movement Distribution Maps (MDM)*; Big Mobile Data Review. | Summarize the diversity of observation layers. |
| **B5. Observation Diversity** | Do different observations provide the same knowledge about mobility? | Different observation layers differ in spatial resolution, temporal resolution, accessibility, privacy, and semantic richness. | Barbosa et al. (2018); Big Mobile Data Review; Zheng (2015). | Compare the characteristics of different observation layers. |
| **B6. Observation Principle (Transition to Layer C)** | What determines the scientific value of a mobility observation? | The scientific value of a mobility observation depends not only on how it is collected, but also on the information it preserves about the underlying mobility phenomenon. | Barbosa et al. (2018). *(The explicit "information preservation" interpretation is introduced by this thesis and becomes the basis for Layer C.)* | Transition from **Observation** to **Information Hierarchy** (Layer C). |

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
* **Geospatial & POI Data:** Vu et al. (2021) *Enhanced Urban Functional Land Use Map with Open Data*; Guo et al. (2025) *Computer-Aided Civil and Infrastructure Engineering*.

##### 4. Critical Comparison
* **Disaggregate Trajectories (High detail, high privacy risk) vs. Aggregate Mobility Releases (Spatially noded/binned, low privacy risk, high accessibility).**

##### 5. Implications for Thesis
Justifies positioning Aggregate Mobility Products (specifically Trip-Length Distributions) as the primary observational input for survey-free calibration.

---

### Layer C — Information Hierarchy of Urban Mobility Observations

#### 1. Scientific Master Matrix for Layer C

| Section | Scientific Question | Core Claim | Main Supporting References (APA) | Role in the RKB |
| :--- | :--- | :--- | :--- | :--- |
| **C. Information Hierarchy of Urban Mobility Observations** | How should different mobility observations be organized? | Different mobility observations should be organized according to the information they preserve rather than their data source. | Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory*; Barbosa, H., et al. (2018). *Human mobility: Models and applications*. | Introduce the information-centric perspective. |
| **C1. Observation versus Information** | Is more data equivalent to more information? | The quantity of data and the amount of scientific information are fundamentally different concepts. | Cover & Thomas (2006); Barbosa et al. (2018). | Distinguish observations from information. |
| **C2. Information Hierarchy** | How can mobility observations be systematically organized? | Mobility observations form a hierarchy according to the mobility information they preserve. | Cover & Thomas (2006); Song, C., Qu, Z., Blumm, N., & Barabási, A.-L. (2010). *Limits of Predictability in Human Mobility*. **Science**; Barbosa et al. (2018). | Introduce the hierarchy used throughout the thesis. |
| **C3. Information Reduction through Aggregation** | What information is lost during aggregation? | Every aggregation operation removes specific dimensions of mobility information while preserving others. | Cover & Thomas (2006); Gallotti, R., et al. (2024). *Distorted Mobility Data*; Barbosa et al. (2018). | Explain information reduction. |
| **C4. Information Sufficiency** | Does information loss imply scientific uselessness? | Information loss does not necessarily eliminate the information required to answer a specific scientific question. | Cover & Thomas (2006). *(The application to mobility observations is the interpretation proposed in this thesis.)* | Introduce the Information Sufficiency Principle. |
| **C5. Behavioural Information in Aggregate Observations** | What behavioural information is preserved by aggregate observations? | Aggregate travel-distance distributions preserve statistical signatures of collective travel behaviour despite losing pairwise OD information. | Liang, X., et al. (2013). *Scientific Reports*; Barbosa et al. (2018); Gallotti et al. (2024). | Scientific motivation for Paper 1. |
| **C6. Information Sufficiency Principle (Transition to Layer D)** | What determines whether an observation is scientifically useful? | The scientific usefulness of a mobility observation depends on whether it preserves the information required to answer a particular scientific question, rather than on the total amount of information it contains. | *(This principle is proposed by this thesis, supported conceptually by Information Theory rather than directly stated in the literature.)* | Transition from **Information** to **Scientific Mechanisms** (Layer D). |

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

### Layer D — The Gravity Principle of Urban Spatial Interaction

#### 1. Scientific Master Matrix for Layer D

| Section | Scientific Question | Core Claim | Main Supporting References (APA) | Role in the RKB |
| :--- | :--- | :--- | :--- | :--- |
| **D. The Gravity Principle of Urban Spatial Interaction** | What scientific principle governs collective Urban Human Mobility? | Collective urban mobility can be understood as a process of spatial interaction governed by attraction and travel impedance. | Wilson, A. G. (1971). *A family of spatial interaction models*; Barbosa, H., et al. (2018). *Human mobility: Models and applications*. | Introduce Gravity as the fundamental scientific principle. |
| **D1. Urban Mobility as Spatial Interaction** | What is the essence of Urban Human Mobility? | Urban mobility fundamentally consists of spatial interactions among locations rather than isolated individual movements. | Wilson (1971); Barbosa et al. (2018); Erlander, S., & Stewart, N. F. (1990). *The Gravity Model in Transportation Analysis*. | Define mobility as a spatial interaction phenomenon. |
| **D2. The Gravity Principle** | Why has Gravity remained the dominant paradigm? | Spatial interactions emerge from the balance between opportunities and travel impedance. | Wilson (1971); Tanner, J. C. (1961). *Factors affecting the amount of travel*; Barbosa et al. (2018). | Introduce the conceptual principle behind Gravity. |
| **D3. Alternative Theoretical Formulations** | Are different mobility models fundamentally different? | Entropy Maximization, Classical Gravity, Radiation and Intervening Opportunities are different theoretical realizations of the same spatial interaction problem, each emphasizing different assumptions. | Wilson (1971); Simini, F., et al. (2012). *A universal model for mobility and migration patterns*. **Nature**; Stouffer, S. A. (1940). *Intervening Opportunities*. | Compare competing theoretical paradigms without favoring one. |
| **D4. Structure and Behaviour in Gravity** | What components determine spatial interaction? | Gravity models naturally decompose mobility into Urban Structure (opportunities) and Human Travel Behaviour (travel impedance). | Wilson (1971); Tanner (1961); Barbosa et al. (2018). *(The explicit Structure–Behaviour interpretation is proposed by this thesis.)* | Establish the conceptual decomposition underlying the thesis. |
| **D5. Scientific Interpretation of Gravity** | Is Gravity merely a predictive model? | Gravity should be interpreted as a scientific framework for explaining spatial interactions rather than merely a predictive equation. | Wilson (1971); Barbosa et al. (2018). | Shift from model-centric to principle-centric thinking. |
| **D6. Transition to Layer E** | Which component remains the least observable? | While Urban Structure is increasingly observable, Human Travel Behaviour remains a latent mechanism that must be inferred statistically. | Barbosa et al. (2018); Tanner (1961). | Transition to Behaviour (Layer E). |

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

### Layer E — Human Travel Behaviour in Urban Spatial Interaction

#### 1. Scientific Master Matrix for Layer E

| Section | Core Claim | Strong Supporting References (APA) | Actual Reference Contribution | Attribution Boundary (What NOT to Attribute) |
| :--- | :--- | :--- | :--- | :--- |
| **E. Human Travel Behaviour in Urban Spatial Interaction** | Collective spatial interactions are governed by human responses to travel impedance. | Barbosa, H., et al. (2018). *Human mobility: Models and applications*. **Physics Reports, 734**, 1–74. | Establishes Human Mobility Science context; surveys population mobility models; affirms Gravity and distance deterrence as central components in mobility modeling. | Does not propose Structure–Behaviour Separation; does not investigate behavioural identifiability. |
| **E1. Human Travel Behaviour** | Human Travel Behaviour is the collective response to spatial impedance. | Tanner, J. C. (1961). *Factors affecting the amount of travel*; Barbosa et al. (2018). | Tanner establishes foundational concepts for travel impedance and distance-frequency relationships. Barbosa contextualizes it in modern Human Mobility Science. | Tanner does not define "behaviour" as an independent scientific object. |
| **E2. Behaviour versus Urban Structure** | Behaviour and Urban Structure are complementary components of spatial interaction. | Wilson, A. G. (1971). *A family of spatial interaction models*; Erlander, S., & Stewart, N. F. (1990). *The Gravity Model in Transportation Analysis*. | Wilson and Erlander demonstrate that spatial interaction depends simultaneously on opportunities and impedance. Forms the foundation for the thesis's interpretation into Structure and Behaviour. | Neither paper explicitly states the "Structure–Behaviour Separation Principle". This is the original thesis interpretation. |
| **E3. Spatial Impedance and Distance Sensitivity** | Behaviour is primarily expressed through sensitivity to travel distance. | Tanner (1961); Liang, X., et al. (2013). *Unraveling the origin of exponential law in intra-urban human mobility*. **Scientific Reports**. | Tanner formulates deterrence functions; Liang explains why distance decay emerges in intra-urban mobility and links it to collective movement patterns. | Liang does not study parameter identification from aggregate TLD. |
| **E4. Distance-decay as Behavioural Representation** | Distance-decay functions are mathematical representations of collective travel behaviour. | Tanner (1961); Martínez, L. M., & Viegas, J. M. (2013). *Calibration of gravity models*; Liang et al. (2013). | Tanner introduces the Tanner function; Martínez & Viegas review and compare deterrence functions; Liang provides empirical urban distance-decay evidence. | No paper explicitly calls distance-decay a "representation of behaviour". This is an explicit interpretation of this thesis. |
| **E5. Behaviour as a Latent Scientific Quantity** | Human Travel Behaviour cannot be directly observed and must be statistically inferred. | Casella, G., & Berger, R. L. (2002). *Statistical Inference*; Barbosa et al. (2018). | Casella & Berger provide foundations for latent parameters, likelihood, and statistical inference; Barbosa shows behaviour is typically inferred via models rather than directly observed. | Casella does not discuss Human Mobility; Barbosa does not demonstrate inference from aggregate observations. |
| **E6. Transition to Layer F** | Human Travel Behaviour alone cannot generate mobility; it interacts with Urban Structure. | Wilson (1971); Erlander & Stewart (1990). | Spatial interaction always requires attraction and impedance. Opens the path for Layer F (Urban Structure). | Should not attribute to Wilson that he proposed separating Structure and Behaviour into independent research objects. |

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

### Layer F — Urban Structure in Urban Spatial Interaction

#### 1. Scientific Master Matrix for Layer F

| Section | Scientific Question | Core Claim | Main Supporting References (APA) | Contribution of References | Thesis Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **F. Urban Structure in Urban Spatial Interaction** | What structural components determine spatial interactions? | Urban Structure provides the spatial opportunities and constraints within which Human Travel Behaviour generates mobility flows. | Wilson, A. G. (1971). *A family of spatial interaction models*; Barbosa, H., et al. (2018). *Human mobility: Models and applications*. **Physics Reports, 734**, 1–74. | Spatial interaction depends on origins, destinations and spatial opportunities. | Urban Structure is treated as an independent scientific object. |
| **F1. Urban Structure as Spatial Opportunity** | What constitutes Urban Structure? | Urban Structure consists of the spatial distribution of population, activities, infrastructure and opportunities. | Wilson (1971); Barbosa et al. (2018); Batty, M. (2013). *The New Science of Cities*. | Spatial interaction requires opportunities distributed in space. | Structure is defined independently of mobility observations. |
| **F2. Observable Urban Structure** | Can Urban Structure be directly observed? | Unlike behaviour, Urban Structure is increasingly observable through open urban datasets. | Guo, Y., et al. (2025). *A universal geography neural network for mobility flow prediction in planning*. **CACE**; Liu et al. (2025). *Representation Learning for Geospatial Data*; Open mobility/open datasets papers. | OpenStreetMap, POIs, census, buildings, satellite imagery, GTFS provide structural observations. | Structure becomes the observable component of the thesis. |
| **F3. Urban Structure Representation** | How should Urban Structure be represented? | Modern AI represents Urban Structure through learned geospatial representations rather than handcrafted variables. | Guo et al. (2025); Liu et al. (2025); Simini et al. (2021). *DeepGravity* (**Nature Comm**); Enaya et al. (2026). *TransGM*. | Reviews representation learning and feature learning for cities. | Representation learning is interpreted as learning structural information. |
| **F4. Transferability of Urban Structure** | Can Urban Structure be transferred across cities? | Many structural characteristics are transferable across cities because they describe physical urban organization rather than city-specific behaviour. | Enaya et al. (2026). *TransGM*; Guo et al. (2025); Simini et al. (2021). *DeepGravity*; Liu et al. (2025). *NeuroGravity*. | Existing work explores transferable embeddings and representations. | The thesis transfers only Urban Structure—not behaviour. |
| **F5. Urban Structure as the Observable Counterpart of Behaviour** | How are Structure and Behaviour related? | Urban Mobility emerges from the interaction between observable Urban Structure and latent Human Travel Behaviour. | Wilson (1971); Barbosa et al. (2018). | Spatial interaction depends on both opportunity and impedance. | Formalizes the Structure–Behaviour Separation Principle. |
| **F6. Transition to Layer G** | How are these two components currently modelled? | Existing models usually learn Structure and Behaviour jointly without explicitly separating them. | Simini et al. (2021); Liu et al. (2025); Enaya et al. (2026); Guo et al. (2025). | Modern AI models jointly optimize all components. | Leads naturally to the review of the conventional modelling paradigm (Layer G). |

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

### Layer G — The Conventional Paradigm of Urban Mobility Modelling

#### 1. Scientific Master Matrix for Layer G

| Section | Scientific Question | Core Claim | Main Supporting References (APA) | Contribution of References | Thesis Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **G. The Conventional Paradigm of Urban Mobility Modelling** | How is Urban Mobility traditionally modelled? | Existing methods generally learn Urban Mobility directly from observed mobility data. | Barbosa, H., et al. (2018). *Human mobility: Models and applications*. **Physics Reports, 734**, 1–74; DeepGravity (2021); NeuroGravity (2025); Universal Geography (2025). | Survey existing modelling paradigms. | Introduce the Observation-First paradigm. |
| **G1. Classical Spatial Interaction Models** | How were mobility models traditionally developed? | Classical models estimate behavioural parameters using observed OD matrices or travel surveys. | Wilson, A. G. (1971); Erlander, S., & Stewart, N. F. (1990); Tanner, J. C. (1961). | Calibration based on observed mobility. | Foundation of conventional modelling. |
| **G2. Machine Learning-based Mobility Models** | How has machine learning changed mobility modelling? | Machine learning improves predictive performance while preserving the same dependence on observed mobility labels. | Simini, F., et al. (2021). *DeepGravity* (**Nature Comm**); Liu et al. (2025). *NeuroGravity*; Guo, Y., et al. (2025). *Universal Geography Neural Network*. | Review AI-based mobility prediction. | AI changes the model, not the paradigm. |
| **G3. Transfer Learning for Mobility** | How is knowledge transferred across cities? | Existing transfer-learning methods mainly transfer model parameters or learned embeddings. | Enaya et al. (2026). *TransGM*; Liu et al. (2025). *NeuroGravity*; Guo et al. (2025). | Review transfer-learning approaches. | Transfer is generally model-centric. |
| **G4. Common Assumptions of Existing Models** | What assumptions are shared by existing methods? | Most existing methods assume that detailed mobility observations are available for training or calibration. | Barbosa et al. (2018); Simini et al. (2021); Enaya et al. (2026); Liu et al. (2025). | Reveal the hidden common assumption. | Define the Observation-First Paradigm. |
| **G5. Observation-First Paradigm** | What paradigm underlies existing research? | Urban Mobility is typically treated as an observable target from which models are learned. | Synthesized from Wilson (1971), Barbosa et al. (2018), Simini et al. (2021), and Enaya et al. (2026). | Literature demonstrates this pattern across classical and AI methods. | The thesis formalizes this shared paradigm. |
| **G6. Transition to Layer H** | What happens when mobility observations are unavailable? | Existing paradigms become difficult to apply in cities lacking detailed mobility observations. | Barbosa et al. (2018); Open Dataset papers; Guo et al. (2025). | Motivate the unresolved scientific problem. | Transition to Research Gaps (Layer H). |

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

| Section | Scientific Question | Core Claim | Main Supporting References (APA) | Contribution of References | Thesis Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **H. Scientific Synthesis and Research Gaps** | What remains scientifically unresolved? | Despite major advances in mobility modelling, two fundamental scientific questions remain unresolved. | Synthesized from Layers A–G. | Literature collectively reveals unresolved problems. | The thesis synthesizes these into a unified research agenda. |
| **H1. Scientific Consensus** | What has the community established? | Urban mobility is a measurable spatial interaction governed by systematic behavioural and structural mechanisms. | Barbosa et al. (2018); Wilson (1971); Tanner (1961); Guo et al. (2025). | Summarize established scientific knowledge. | No new interpretation beyond synthesis. |
| **H2. Scientific Uncertainties** | What remains uncertain? | Human Travel Behaviour remains latent, Urban Structure is increasingly observable, and their interaction is still difficult to disentangle. | Barbosa et al. (2018); Simini et al. (2021). *DeepGravity*; Guo et al. (2025). *Universal Geography*; Enaya et al. (2026). *TransGM*. | Literature reveals persistent challenges. | Synthesis across previous layers. |
| **H3. Research Gap I – Behaviour Identification** | Can Human Travel Behaviour be identified without detailed mobility observations? | Existing studies estimate behaviour from observed OD flows, while the identifiability of behaviour from aggregate mobility observations remains largely unexplored. | Barbosa et al. (2018); Liang et al. (2013); Casella & Berger (2002). | Literature motivates but does not solve the problem. | Motivation for Paper 1. |
| **H4. Research Gap II – Transferable Urban Structure** | Can Urban Structure be represented and transferred independently of behaviour? | Existing transfer-learning methods transfer models or embeddings, whereas transferable structural knowledge remains insufficiently understood. | Guo et al. (2025). *Universal Geography*; Enaya et al. (2026). *TransGM*; Liu et al. (2025). *NeuroGravity*. | Literature explores transfer learning but not explicit structural transfer. | Motivation for Paper 2. |
| **H5. Unified Scientific Perspective** | How are the two gaps related? | Behaviour Identification and Transferable Urban Structure are complementary problems arising from the same scientific decomposition of Urban Mobility. | Synthesized from Layers D–G. | Literature provides ingredients separately. | The thesis unifies them through the Structure–Behaviour Separation Principle. |
| **H6. Transition to the Research Proposal** | What scientific questions should be addressed next? | These research gaps motivate the research questions, objectives and methodology presented in the proposal. | Synthesized from the entire RKB. | Transition only. | Bridge from Knowledge Base to Proposal. |

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
