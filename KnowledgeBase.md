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

#### 1. Scientific Master Matrix for Layer A (Optimized)

| Section | Scientific Question | Core Claim | Main Supporting References (APA) | Role of Literature |
| :--- | :--- | :--- | :--- | :--- |
| **A. Defining Urban Human Mobility as the Scientific Object** | What is the scientific object of this research? | Urban Human Mobility is a legitimate scientific object for systematic quantitative investigation. | Barbosa, H., Barthelemy, M., Ghoshal, G., James, C. R., Lenormand, M., Louail, T., Menezes, R., Ramasco, J. J., Simini, F., & Tomasini, M. (2018). Human mobility: Models and applications. *Physics Reports*, 734, 1–74. | Foundational review establishing the ontology, taxonomy, and mathematical boundaries of Human Mobility Science. |
| **A1. Urban Human Mobility in the Open Data Era** | Why has Urban Human Mobility become a timely scientific problem? | Modern cities and urban environments have become increasingly observable through publicly available spatial data and representation learning. | Guo, Y., Bai, S., Li, X., Xian, K., Liu, E., Ding, W., & Ma, X. (2025). A universal geography neural network for mobility flow prediction in planning scenarios. *Computer-Aided Civil and Infrastructure Engineering*; Liu, Y., Wang, S., Wang, X., Zheng, Y., Chen, X., Xu, Y., & Kang, C. (2024). Towards semantic enrichment for spatial interactions. *Annals of GIS*; Maas, P., et al. (2019). Facebook Disaster Maps. *Data for Good*. | Demonstrates how the fusion of multi-source open urban data (OSM, POIs, Sentinel/Landsat) and aggregate mobility products—including Meta's Movement Distribution Maps (MDM)—enables rich, scalable representations of urban structure and privacy-preserving population travel behavior summaries. |
| **A2. Urban Mobility as Urban Intelligence** | Why is mobility fundamental to modern cities? | Urban mobility constitutes a critical dynamic layer that shapes economic activity, spatial planning, public health, and urban intelligence. | Barbosa et al. (2018); Wang, J., Kong, X., Xia, F., & Sun, L. (2019). Urban Human Mobility: Data-Driven Modeling and Prediction. *Dalian University Survey*; Oliver, N., et al. (2020). Mobile phone data for informing public health actions across the COVID-19 pandemic life cycle. *Science Advances*. | Documents the operational utility of mobility modeling in real-world planning, infrastructure design, and epidemic containment. |
| **A3. Urban Mobility is Observable** | Can Urban Human Mobility be observed? | Urban mobility leaves highly structured, multi-granular digital traces across complementary observation layers. | Barbosa et al. (2018); Zheng, Y. (2015). Trajectory Data Mining: An Overview. *ACM TIST*; Wang, J., et al. (2019). | Synthesizes passive observation sources, including Call Detail Records (CDRs), GPS trajectories, smart card transactions, and LBSNs. |
| **A4. Urban Mobility is Measurable** | Can Urban Human Mobility be quantitatively measured? | Urban mobility can be rigorously quantified using standard statistical metrics of flows, trip distances, travel times, and network centralities. | Barbosa et al. (2018); Wang, J., et al. (2019). | Defines and mathematicalizes key spatial metrics (e.g., radius of gyration, trip displacement, and origin-destination flows). |
| **A5. Urban Mobility Exhibits Regularities** | Does Urban Mobility exhibit scientific regularities? | Collective urban mobility displays robust, scaling, and highly reproducible statistical regularities despite individual behavioral complexity. | González, M. C., Hidalgo, C. A., & Barabási, A. L. (2008). Understanding individual human mobility patterns. *Nature*; Simini, F., González, M. C., Maritan, A., & Barabási, A. L. (2012). A universal model for mobility and migration patterns. *Nature*; Liang, X., Zhao, J., Dong, L., & Xu, K. (2013). Unraveling the origin of exponential law in intra-urban human mobility. *Scientific Reports*. | Establishes the empirical existence of universal distance-decay laws, truncated power-law distributions, and the exponential nature of intra-urban trips. |
| **A6. Urban Mobility is Explainable** | Can Urban Mobility be scientifically explained? | Collective human spatial interactions emerge from systematic, explainable forces governing urban structure and spatial impedance. | Wilson, A. G. (1971). A family of spatial interaction models, and associated developments. *Environment and Planning A*; Simini et al. (2012). | Provides the physics-guided and entropy-maximizing foundations that mathematically separate structural opportunities from behavioral resistance. |
| **A7. Urban Mobility is Predictable** | Can Urban Mobility be predicted or reconstructed? | The stable coupling between urban structure and collective behavior makes mobility flow generation and generative network reconstruction scientifically viable. | Simini, F., Barlacchi, G., Luca, M., & Pappalardo, L. (2021). A Deep Gravity model for mobility flows generation. *Nature Communications*; Yang, J., et al. (2026). Transferable Human Mobility Network Reconstruction with neuroGravity. *Zenodo/SJTU*; Xu, Y., Gao, S., Huang, Q., Göçmen, A., Zhu, Q., & Zhang, F. (2025). Predicting human mobility flows in cities using deep learning on satellite imagery. *Nature Communications*. | Demonstrates how deep learning (Deep Gravity), graph neural networks (neuroGravity), and computer vision (Imagery2Flow) successfully reconstruct unobserved flow networks from open geographic contexts. |
| **A8. Transition to Layer B** | If Urban Mobility is observable, why is it still difficult to understand? | The modern challenge is a severe "data paradox": while spatial data is abundant, high-resolution mobility flows are increasingly restricted and compressed due to systemic privacy constraints. | de Montjoye, Y. A., Hidalgo, C. A., Verleysen, M., & Blondel, V. D. (2013). Unique in the crowd: The privacy bounds of human mobility. *Scientific Reports*; Buckee, C. O., et al. (2020). Aggregated mobility data could help fight COVID-19. *Science*; Gallotti, R., Bazzani, A., Rambaldi, S., & Barthelemy, M. (2024). Detors: Biases in human mobility data impact epidemic modeling. *Preprint/Nature*. | Bridges to Layer B by proving that privacy bounds prevent the publication of fine-grained OD matrices, forcing a reliance on aggregated, pruned, and compressed mobility statistics. |


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

#### 1. Scientific Master Matrix for Layer B (Optimized)

| Section | Scientific Question | Core Claim | Main Supporting References (APA) | Role of Literature |
| :--- | :--- | :--- | :--- | :--- |
| **B. The Evolution of Urban Mobility Observations** | How has Urban Human Mobility become observable? | Advances in mobile sensing, computing infrastructures, and digital traces have fundamentally transformed urban mobility from a scarce, hard-to-observe phenomenon into a highly recorded spatial process. | Barbosa, H., et al. (2018). Human mobility: Models and applications. *Physics Reports*, 734, 1–74; Wang, J., Kong, X., Xia, F., & Sun, L. (2019). Urban Human Mobility: Data-Driven Modeling and Prediction. *SIGKDD Explorations*, 21(1), 1–19. | Establishes the historical and technological baseline of the transition from physical questionnaires to passive digital footprinting. |
| **B1. The Survey Era** | How was urban mobility traditionally observed? | Traditional Household Travel Surveys (HTSs) and census programs (e.g., CTPP, LODES) provided the first systematic, origin-constrained interaction networks but are severely limited by high financial costs, spatial sparsity, and low update frequencies. | Barbosa et al. (2018); Wang et al. (2019); Yang, Y., Herrera, C., Eagle, N., & González, M. C. (2014). Limits of predictability in commuting flows in the absence of data for calibration. *Scientific Reports*, 4, 5662. | Establishes the historical baseline, highlighting the data-scarcity bottleneck in developing regions (such as the Global South) where census surveys are rarely updated. |
| **B2. The Digital Mobility Era** | How did digital technologies transform mobility observation? | The integration of Call Detail Records (CDRs), high-resolution GPS trajectories, and Automated Fare Collection (AFC) smart cards dramatically scaled the spatial-temporal granularity and coverage of collective mobility observations. | González, M. C., Hidalgo, C. A., & Barabási, A. L. (2008). Understanding individual human mobility patterns. *Nature*, 453, 779–782; Pappalardo, L., Manley, E., Sekara, V., & Alessandretti, L. (2023). Future directions in human mobility science. *Nature Computational Science*, 3, 588–600; Toole, J. L., et al. (2015). The path most traveled: Travel demand estimation using big data resources. *Transportation Research Part C*, 58, 162–177. | Outlines the passive collection mechanisms of major mobile traces (Voronoi-based CDR vs. precise GPS coordinate logging and public transit smart-card taps). |
| **B3. The Open Urban Data Era** | What urban information is publicly available today? | Publicly accessible spatial platforms (OpenStreetMap, POI APIs, satellite imagery, and building outlines) provide a dense, globally available, and low-cost digital representation of the urban physical structure. | Guo, Y., et al. (2025). A universal geography neural network for mobility flow prediction in planning scenarios. *CACE*, 38(14); Liu, Y., et al. (2024). Towards semantic enrichment for spatial interactions. *Annals of GIS*; Vu, T. T., Vu, N. V. A., Phung, H. P., & Nguyen, L. D. (2021). Enhanced urban functional land use map with free and open-source data. *International Journal of Digital Earth*. | Confirms that multi-modal urban characteristics (POIs, road networks, land-use zoning) can be accurately mapped from free open-source data to represent the "Urban Structure" ($S_{ij}$). |
| **B4. Modern Urban Mobility Observations** | How is Urban Human Mobility observed today? | Modern mobility observation relies on a highly fragmented, multi-layered ecosystem of aggregated digital data products (e.g., Google, Meta Data for Good, Cuebiq, SafeGraph) managed through proprietary pipelines rather than unified raw datasets. | Gallotti, R., Maniscalco, D., Barthelemy, M., & De Domenico, M. (2024). Distorted insights from human mobility data. *Nature Communications*; Oliver, N., et al. (2020). Mobile phone data for informing public health actions across the COVID-19 pandemic life cycle. *Science Advances*, 6; Buckee, C. O., et al. (2020). Aggregated mobility data could help fight COVID-19. *Science*, 368. | Documents the real-world operational reliance on corporate "Data for Good" products and systematically compares their structural differences across multiple platforms. |
| **B5. Observation Diversity and Biases** | Do different observations provide the same knowledge about mobility? | Different observation layers do not describe the same physical reality; they exhibit systemic demographic skewness, spatial resolution biases, and proprietary processing distortions that alter the observed travel-distance distributions. | Gallotti et al. (2024); Pappalardo et al. (2023) [Box 1 on "Issues with mobility data"]. | Proves that empirical data cannot be used as an objective "ground truth" without auditing. Highlights the underrepresentation of low-income groups and the spatial distortions introduced by corporate pruning algorithms. |
| **B6. Observation Principle (Transition to Layer C)** | What determines the scientific value of a mobility observation? | The scientific utility of a mobility observation is determined by the specific entropy and behavioral information it preserves after passing through privacy-preserving aggregation and compression filters. | de Montjoye, Y. A., Hidalgo, C. A., Verleysen, M., & Blondel, V. D. (2013). Unique in the crowd: The privacy bounds of human mobility. *Scientific Reports*, 3, 1376; Houssiau, F., Rocher, L., & de Montjoye, Y. A. (2022). Tapas: A framework for membership inference attacks on aggregated mobility data. *Nature Communications*. | Forms the theoretical justification for the "Information Preservation Taxonomy" (Layer C) by showing that individual uniqueness necessitates aggregation, thereby shifting the observation focus from raw trajectories to aggregate statistics. |


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

#### 1. Scientific Master Matrix for Layer C (Optimized)

| Section | Scientific Question | Core Claim | Main Supporting References (APA) | Role of Literature |
| :--- | :--- | :--- | :--- | :--- |
| **C. Information Hierarchy of Urban Mobility Observations** | How should different mobility observations be organized? | Mobility observations must be systematically classified based on the mathematical entropy and behavioral information they preserve, rather than their physical collection technology. | Barbosa, H., et al. (2018). Human mobility: Models and applications. *Physics Reports*, 734, 1–74; Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory*. Wiley-Interscience. | Establishes the information-centric paradigm, shifting the research focus from data volume to active information preservation. |
| **C1. Observation versus Information** | Is more data equivalent to more information? | Data volume and scientific information are fundamentally distinct; high-resolution digital traces often contain redundant structural signals while obscuring latent behavioral parameters. | Song, C., Qu, Z., Blumm, N., & Barabási, A. L. (2010). Limits of predictability in human mobility. *Science*, 327(5968), 1018–1021; Cover & Thomas (2006). | Mathematically distinguishes raw spatial points from structural information using the formal definitions of random, uncorrelated, and actual entropy. |
| **C2. Information Hierarchy of Mobility** | How can mobility observations be systematically structured? | Mobility observations form a strict mathematical hierarchy of decreasing information content: Trajectories $\rightarrow$ OD Matrices $\rightarrow$ Distance Distributions (TLDs) $\rightarrow$ Summary Statistics. | de Montjoye, Y. A., Hidalgo, C. A., Verleysen, M., & Blondel, V. D. (2013). Unique in the crowd: The privacy bounds of human mobility. *Scientific Reports*, 3, 1376; Song et al. (2010); Barbosa et al. (2018). | Maps the transition from high-entropy, privacy-sensitive individual paths to highly compressed, anonymous population-level statistics. |
| **C3. Information Reduction through Aggregation** | What mathematical information is lost during spatial and temporal aggregation? | Aggregation and privacy-preserving filters (e.g., pruning and spatial zoning) systematically eliminate individual trajectory dimensions while shifting and distorting the tail of observed displacement distributions. | de Montjoye et al. (2013); Gallotti, R., Bazzani, A., Rambaldi, S., & Barthelemy, M. (2024). Distorted insights from human mobility data. *Nature Communications*; Houssiau, F., Rocher, L., & de Montjoye, Y. A. (2022). Tapas: A framework for membership inference attacks on aggregated mobility data. *Nature Communications*. | Quantifies how reducing spatial and temporal resolution decreases unicity via a power law, and documents how corporate privacy filters distort baseline networks and TLDs. |
| **C4. Information Sufficiency** | Does information loss imply the loss of scientific inferability? | Information compression does not necessarily eliminate the statistical evidence required to identify low-dimensional latent behavioral parameters under known structural constraints. | Cover & Thomas (2006); Merlin, L. A. (2020). A new method using medians to calibrate single-parameter spatial interaction models. *Journal of Transport and Land Use*, 13(1), 49–70. | Introduces the core thesis concept that a highly compressed observation (such as median travel time) contains sufficient information to solve the inverse calibration problem. |
| **C5. Behavioural Information in TLDs** | What behavioral information survives aggregate observations? | Aggregate travel-distance distributions (TLDs) preserve the statistical signatures of collective spatial friction and distance-decay, independent of pairwise connection details. | Liang, X., Zhao, J., Dong, L., & Xu, K. (2013). Unraveling the origin of exponential law in intra-urban human mobility. *Scientific Reports*, 3, 2983; Gallotti et al. (2024); Barbosa et al. (2018). | Demonstrates that robust, collective distance-decay regularities (such as the exponential law) emerge consistently at the aggregate scale despite massive individual heterogeneity. |
| **C6. Information Sufficiency Principle (Transition to Layer D)** | What determines whether a compressed observation is scientifically useful? | An aggregated mobility observation is scientifically sufficient if its mutual information with the latent behavioral parameter is preserved under the constraints of the known urban structure. | *(Proposed by this thesis, conceptually bridged by Information Theory and empirically validated by the sufficiency of Merlin's 2020 median-based estimator)* | Direct epistemological bridge to Layer D (The Gravity Principle and Scientific Mechanisms). |


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

#### 1. Scientific Master Matrix for Layer D (Optimized)

| Section | Scientific Question | Core Claim | Main Supporting References (APA) | Role of Literature |
| :--- | :--- | :--- | :--- | :--- |
| **D. The Gravity Principle of Urban Spatial Interaction** | What scientific principle governs collective Urban Human Mobility? | Collective urban mobility can be conceptualized as a structured process of spatial interaction governed by origin production, destination attraction, and spatial travel impedance. | Wilson, A. G. (1971). A family of spatial interaction models, and associated developments. *Environment and Planning A*, 3(1), 1–32; Barbosa, H., et al. (2018). Human mobility: Models and applications. *Physics Reports*, 734, 1–74. | Establishes the gravity framework as the primary first-principles paradigm for modeling population-level spatial interaction flows. |
| **D1. Urban Mobility as Spatial Interaction** | What is the scientific essence of Urban Human Mobility? | Urban mobility is not a collection of isolated, random movements but emerges as systematic spatial interactions connecting discrete geographical locations. | Haynes, K. E., & Fotheringham, A. S. (1984). *Gravity and Spatial Interaction Models*. Scientific Geography Series, Vol. 2, Sage Publications; O'Kelly, M. E. (2009). Spatial Interaction Models. *Elsevier*, 9, 381–386. | Defines spatial interaction as any human-induced movement over space (commuting, migration, commodity flows) resulting from spatial decision-making. |
| **D2. The Gravity Principle** | Why has the Gravity formulation remained the dominant paradigm of spatial interaction? | Spatial interactions arise from a fundamental balance between structural opportunities (masses) and the spatial resistance of distance (travel impedance). | Zipf, G. K. (1946). The $P_1 P_2 / D$ hypothesis: on the intercity movement of persons. *American Sociological Review*, 11(6), 677–686; Wilson, A. G. (1971); O'Kelly, M. E. (2009). | Traces the evolution from Newtonian analogies of physical masses (Carey, 1858; Zipf, 1946) to statistical mechanics and entropy maximization (Wilson, 1970). |
| **D3. Alternative Theoretical Formulations** | Are competing mobility models (Gravity, Radiation, Intervening Opportunities) fundamentally different? | Entropy Maximization, Classical Gravity, Radiation, and Intervening Opportunities represent different mathematical realizations of the same spatial interaction problem under varying constraints and assumptions. | Stouffer, S. A. (1940). Intervening opportunities: A theory relating mobility and distance. *American Sociological Review*, 5(6), 845–867; Simini, F., González, M. C., Maritan, A., & Barabási, A. L. (2012). A universal model for mobility and migration patterns. *Nature*, 484(7392), 96–100; Lenormand, M., Bassolas, A., & Ramasco, J. J. (2016). Systematic comparison of trip distribution laws and models. *Journal of Transport Geography*, 51, 158–169. | Conceptualizes alternative models (e.g., Radiation and Intervening Opportunities) and evaluates them empirically against Gravity models using global census datasets. |
| **D4. Structure and Behaviour in Gravity** | How does the Gravity formulation mathematically separate urban form from travel behavior? | The doubly-constrained gravity model acts as a structural decomposition operator, using balancing factors to isolate the effects of urban morphology from latent behavioral distance-decay. | Wilson, A. G. (1971); Haynes, K. E., & Fotheringham, A. S. (1984); O'Kelly, M. E. (2009). | Formally demonstrates that balancing factors ($A_i, B_j$) absorb competitive spatial structure, freeing the deterrence function ($f(d_{ij})$) to represent pure behavioral sensitivity. |
| **D5. Scientific Interpretation of Gravity** | Is Gravity merely a predictive curve-fitting tool? | Gravity must be interpreted as a physical-guided explanatory framework for understanding spatial interaction mechanisms rather than an empirical predictive regression. | Wilson, A. G. (1971); O'Kelly, M. E. (2009); Barbosa, H., et al. (2018). | Argues against treating gravity as a "black-box" regression, positioning it as an entropy-maximizing model of spatial allocation under macro-state constraints. |
| **D6. Transition to Layer E** | Which component of the spatial interaction representation is the most challenging to observe? | While urban structural forces (origins and destinations) are increasingly observable, collective behavioral sensitivity to distance remains a latent, unobservable mechanism. | Haynes, K. E., & Fotheringham, A. S. (1984); Barbosa, H., et al. (2018). | Bridges to Layer E (Human Travel Behaviour and Distance-Decay) by demonstrating that spatial impedance parameters ($\theta$) are hidden and must be statistically identified. |


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

#### 1. Scientific Master Matrix for Layer E (Optimized)

| Section | Core Claim | Strong Supporting References (APA) | Actual Reference Contribution | Attribution Boundary (What NOT to Attribute) |
| :--- | :--- | :--- | :--- | :--- |
| **E. Human Travel Behaviour in Urban Spatial Interaction** | Collective spatial interactions are systematically governed by human responses and psychological friction to spatial travel impedance. | Barbosa, H., Barthelemy, M., Ghoshal, G., James, C. R., Lenormand, M., Louail, T., Menezes, R., Ramasco, J. J., Simini, F., & Tomasini, M. (2018). Human mobility: Models and applications. *Physics Reports*, 734, 1–74. | Establishes the modern Human Mobility Science paradigm; comprehensively surveys population-level spatial interaction models; and affirms the central role of travel impedance and distance-decay in collective flows. | Does not propose the explicit ontological separation of Structure and Behaviour; does not address the question of behavioral parameter identifiability under aggregate data constraints. |
| **E1. Human Travel Behaviour** | Within the spatial interaction framework, Human Travel Behaviour is formally represented as the collective population-level response to spatial separation. | Tanner, J. C. (1961). Factors affecting the amount of travel. *Road Research Technical Paper*; Barbosa et al. (2018); Lenormand, M., Bassolas, A., & Ramasco, J. J. (2016). Systematic comparison of trip distribution laws and models. *Journal of Transport Geography*, 51, 158–169. | Tanner establishes foundational concepts for travel impedance and distance-frequency relationships. Barbosa (2018) and Lenormand (2016) contextualize it as a collective behavioral mechanism. | Tanner does not define collective distance sensitivity as an independent, latent behavioral object of scientific identification. |
| **E2. Behaviour versus Urban Structure** | Human travel behavior (impedance sensitivity) and urban physical structure (distribution of masses and opportunities) are complementary, separable components of spatial interaction. | Wilson, A. G. (1971). A family of spatial interaction models, and associated developments. *Environment and Planning A*, 3(1), 1–32; Haynes, K. E., & Fotheringham, A. S. (1984). *Gravity and Spatial Interaction Models*. Sage Publications. | Wilson and Haynes demonstrate that spatial flows depend simultaneously on structural opportunities (origins/destinations) and physical impedance (distance-decay). | Neither source explicitly formulates the "Structure–Behaviour Separation Principle" as a core epistemological axiom for behavioral reconstruction. This interpretation is original to this thesis. |
| **E3. Spatial Impedance and Distance Sensitivity** | Collective human travel behavior in cities is primarily expressed through systematic, non-linear sensitivity to travel distance and route displacement. | Liang, X., Zhao, J., Dong, L., & Xu, K. (2013). Unraveling the origin of exponential law in intra-urban human mobility. *Scientific Reports*, 3, 2983; Lenormand et al. (2016). | Liang et al. explain why exponential distance decay emerges in intra-urban mobility. Lenormand (2016) provides empirical evidence of distance sensitivity across multiple national scales. | Liang et al. do not investigate the statistical possibility of identifying this distance sensitivity parameter from highly compressed aggregate TLDs. |
| **E4. Distance-decay as Behavioural Representation** | Distance-decay functions (e.g., exponential, power-law, or Tanner formulations) are mathematical representations of collective travel behavior rather than mere empirical curve-fitting equations. | Rubio-Herrero, J., & Muñuzuri, J. (2023). Sparse regression for data-driven deterrence functions in gravity models. *Annals of Operations Research*; Wilson, A. G. (1971). | Wilson shows how entropy maximization under system travel cost constraints yields specific decay functions. Rubio-Herrero (2023) frames the deterrence function as an expression of traveler preferences under system constraints. | No prior study explicitly labels distance-decay as a "mathematical representation of collective behavior." This conceptualization is original to this thesis. |
| **E5. Behaviour as a Latent Scientific Quantity** | Collective travel behavior is a latent scientific quantity that cannot be observed directly and must be statistically inferred from observable mobility evidence. | Merlin, L. A. (2020). A new method using medians to calibrate single-parameter spatial interaction models. *Journal of Transport and Land Use*, 13(1), 49–70; Flowerdew, R., & Aitkin, M. (1982). A method of fitting the gravity model based on the poisson distribution. *Journal of Regional Science*, 22(2), 191–202; Rubio-Herrero & Muñuzuri (2023). | Flowerdew & Aitkin outline the maximum likelihood estimation of impedance parameters. Rubio-Herrero shows that the true deterrence function is fundamentally unknown and latent. Merlin demonstrates it can be inferred from a single median statistic. | These papers do not establish a generalized "Information Preservation Taxonomy" or investigate the theoretical boundaries of parameter recovery from aggregate TLDs under privacy constraints. |
| **E6. Transition to Layer F** | Human travel behavior alone cannot generate physical mobility flows; it must dynamically interact with and be constrained by the physical urban structure. | Wilson, A. G. (1971); Haynes, K. E., & Fotheringham, A. S. (1984). | Formally demonstrates that spatial interaction is a joint product of structural attraction and behavioral impedance. | Should not attribute to Wilson or Haynes the proposition of treating behavioral parameters as transportable policy targets independent of the underlying urban morphology. |


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

#### 1. Scientific Master Matrix for Layer F (Optimized)

| Section | Scientific Question | Core Claim | Main Supporting References (APA) | Contribution of References | Thesis Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **F. Urban Structure in Urban Spatial Interaction** | What structural components determine spatial interactions? | Urban Structure provides the physical spatial opportunities and morphological constraints within which latent Human Travel Behaviour dynamically generates collective mobility flows. | Wilson, A. G. (1971). A family of spatial interaction models, and associated developments. *Environment and Planning A*, 3(1), 1–32; Barbosa, H., et al. (2018). Human mobility: Models and applications. *Physics Reports*, 734, 1–74. | Demonstrates that population-level spatial interaction flows depend systematically on origin propulsiveness, destination attractiveness, and spatial opportunities. | Urban Structure ($S_{ij}$) is treated as an independent, logically separable scientific object of the spatial interaction representation. |
| **F1. Urban Structure as Spatial Opportunity** | What constitutes Urban Structure? | Urban Structure consists of the spatial distribution of population masses, functional land-use activities, transportation infrastructures, and localized opportunities. | Wilson (1971); Barbosa et al. (2018); Batty, M. (2013). *The New Science of Cities*. MIT Press. | Establishes that collective spatial interaction requires a geographical distribution of discrete opportunities, resources, and destination facilities. | Urban Structure is formally defined by the spatial configuration of the built environment, independent of active mobility observations. |
| **F2. Observable Urban Structure** | Can Urban Structure be directly observed and mapped? | Unlike latent travel behavior, Urban Structure is highly observable, measurable, and digitalized through heterogeneous open-source geospatial platforms. | Guo, Y., et al. (2025). A universal geography neural network for mobility flow prediction in planning scenarios. *CACE*, 40, 5769–5789; Liu, Y., et al. (2024). Towards semantic enrichment for spatial interactions. *Annals of GIS*; Herfort, B., et al. (2023). A spatio-temporal analysis investigating completeness and inequalities of global urban building data in OpenStreetMap. *Nature Communications*, 14, 3985; Vu, T. T., et al. (2021). Enhanced urban functional land use map with free and open-source data. *International Journal of Digital Earth*, 14(12). | Demonstrates that OpenStreetMap (OSM) road networks, Point-of-Interest (POI) distributions, and high-resolution Sentinel-2/Landsat satellite imagery provide rich, empirical structural inputs. | Urban Structure serves as the fully observable and mathematically grounded counterpart of the spatial interaction equation. |
| **F3. Urban Structure Representation** | How should Urban Structure be represented in spatial models? | Modern spatial artificial intelligence represents Urban Structure through self-supervised, high-dimensional geospatial representations rather than handcrafted spatial variables. | Guo et al. (2025); Liu et al. (2024); Simini, F., et al. (2021). A Deep Gravity model for mobility flows generation. *Nature Communications*, 12(1), 6576; Xu, Y., et al. (2025). Predicting human mobility flows in cities using deep learning on satellite imagery. *Nature Communications*. | Introduces deep fully connected neural networks, graph attention networks (GAT), and self-supervised contrastive learning (SimCLR) to extract deep semantic embeddings from satellite images and multi-source geocontext. | Spatial representation learning (GeoAI) is interpreted as a tool for extracting the structural features of geographical units. |
| **F4. Transferability of Urban Structure** | Can Urban Structure representations be transferred across geographical contexts? | Physical urban structural configurations and functional arrangements exhibit robust transferability across cities because they capture universal architectural, demographic, and morphological organizations. | Enaya, A., et al. (2026). TransGM: Transferable gravity models for cross-city policy transfer. *Computers, Environment and Urban Systems*, 128, 102455; Yang, J., et al. (2026). Transferable Human Mobility Network Reconstruction with neuroGravity. *Preprint/SJTU*; Guo et al. (2025); Simini et al. (2021). | Employs spatial Kullback-Leibler (KL) divergence, domain-adversarial neural networks, and pre-trained GNN encoders to transfer learned structural contexts across "unseen" target urban domains. | This thesis establishes that while Urban Structure embeddings are highly transferable, the latent collective travel behavior ($\theta$) requires localized parameter identification. |
| **F5. Urban Structure as the Observable Counterpart of Behaviour** | How do Structure and Behaviour mathematically relate to generate collective mobility? | Urban Human Mobility patterns emerge from the non-linear interaction between the observable physical Urban Structure and the latent Human Travel Behaviour (distance-decay sensitivity). | Wilson (1971); Barbosa et al. (2018). | Mathematically operationalizes spatial flows as a function of origin-destination opportunities constrained by distance impedance. | Formalizes the Structure–Behaviour Separation Principle as the foundational axiom for aggregate behavioral identification. |
| **F6. Transition to Layer G** | How are these structural and behavioral components modeled in state-of-the-art AI? | SOTA machine learning models optimize flow prediction by learning Structure and Behaviour jointly in an end-to-end, entangled black-box architecture. | Simini et al. (2021); Liu et al. (2024); Enaya et al. (2026); Guo et al. (2025). | Shows that end-to-end deep learning pipelines (GNNs, FCNNs) merge distance decay and geographical context into dense neural layers, sacrificing interpretability. | Leads directly to the systematic review and critique of the Conventional Joint Modelling Paradigm (Layer G), where behavior cannot be isolated or identified. |


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

#### 1. Scientific Master Matrix for Layer G (Optimized)

| Section | Scientific Question | Core Claim | Main Supporting References (APA) | Contribution of References | Thesis Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **G. The Conventional Paradigm of Urban Mobility Modelling** | How is collective Urban Human Mobility traditionally modeled and understood? | Existing spatial interaction and predictive models generally learn mobility networks directly from high-resolution, observed flow datasets. | Barbosa, H., Barthelemy, M., Ghoshal, G., James, C. R., Lenormand, M., Louail, T., Menezes, R., Ramasco, J. J., Simini, F., & Tomasini, M. (2018). Human mobility: Models and applications. *Physics Reports*, 734, 1–74; Simini, F., Barlacchi, G., Luca, M., & Pappalardo, L. (2021). A Deep Gravity model for mobility flows generation. *Nature Communications*, 12(1), 6576. | Synthesizes the historical development of collective flow estimation, establishing origin-destination (OD) flows as the primary modeling target. | Formally introduces the Observation-First Paradigm, wherein the availability of observed mobility interaction labels ($T_{ij}$) is a non-negotiable prerequisite. |
| **G1. Classical Spatial Interaction Models** | How did classical spatial interaction models calibrate collective behavior? | Classical interaction models mathematically estimate spatial impedance parameters ($\theta$) by fitting curves directly to observed OD flow matrices. | Wilson, A. G. (1971). A family of spatial interaction models, and associated developments. *Environment and Planning A*, 3(1), 1–32; Flowerdew, R., & Aitkin, M. (1982). A method of fitting the gravity model based on the poisson distribution. *Journal of Regional Science*, 22(2), 191–202; Haynes, K. E., & Fotheringham, A. S. (1984). *Gravity and Spatial Interaction Models*. Sage Publications. | Establishes maximum likelihood estimation (MLE) and entropy maximization as the mathematical standards for parameter calibration using observed flow records. | Demonstrates that even low-dimensional classical models require complete, high-cost OD surveys or census matrices to resolve behavior. |
| **G2. Machine Learning-based Mobility Models** | How has the integration of AI changed the modeling of spatial interactions? | Modern machine learning models dramatically improve flow prediction accuracy while retaining a fundamental dependence on observed mobility labels for supervised training. | Simini et al. (2021); Guo, J., Bai, S., Li, X., Xian, K., Liu, E., Ding, W., & Ma, X. (2025). A universal geography neural network for mobility flow prediction in planning scenarios. *Computer-Aided Civil and Infrastructure Engineering*, 40(8), 5769–5789; Shi, H., Zhang, C., Yao, Q., Li, Y., Sun, F., & Jin, D. (2020). Predicting origin-destination flow via multi-perspective graph convolutional network. *IEEE ICDE*. | Leverages GNNs, CNNs, and deep FCNNs (Deep Gravity, UGNN, MPGCN) to automatically extract highly non-linear geographical and structural features for flow generation. | Demonstrates that deep learning models alter the mathematical representation of the structure but fail to change the paradigm: they remain supervised regression networks hungry for raw flow labels. |
| **G3. Transfer Learning for Mobility** | How does existing research transfer learned mobility knowledge across different cities? | Existing transfer-learning methods focus on transferring neural network parameters, model weights, or learned spatial embeddings across geographic domains. | Rong, C., Feng, J., & Ding, J. (2023). GODDAG: Generating Origin-Destination Flow for New Cities Via Domain Adversarial Training. *IEEE TKDE*; Yang, J., et al. (2026). Transferable Human Mobility Network Reconstruction with neuroGravity. *Preprint/SJTU*; Enaya, A., et al. (2026). TransGM: Transferable gravity models for cross-city policy transfer. *Computers, Environment and Urban Systems*, 128, 102455; Xu, Y., et al. (2025). Predicting human mobility flows in cities using deep learning on satellite imagery. *Nature Communications*. | Employs domain adversarial training (GODDAG), GNN meta-optimization (neuroGravity), spatial KL-divergence regularization (TransGM), and self-supervised visual encoders (Imagery2Flow) to adapt models to unobserved cities. | Argues that existing transfer is model-centric or embedding-centric; they attempt to transfer the black-box function rather than identifying and transferring the pure, decoupled behavioral mechanism ($\theta$) itself. |
| **G4. Common Assumptions of Existing Models** | What are the shared mathematical prerequisites of state-of-the-art mobility models? | Existing SOTA models (both physics-informed and deep learning) require total localized trip production/attraction or observed baseline flows as constraints to estimate absolute volumes. | Simini et al. (2021); Enaya et al. (2026); Guo et al. (2025); Yang et al. (2026). | Admits that Deep Gravity requires known total outflows to generate absolute flow volumes. UGNN and TransGM rely on known origin productions ($O_i$) or target-city destination attractions to scale their predictions. | Exposes the critical systemic bottleneck: existing models cannot operate in a true "zero-shot" data-sparse city where local flow constraints ($O_i, D_j$) are entirely missing. |
| **G5. Observation-First Paradigm** | What is the unifying methodological paradigm that limits current mobility science? | Current human mobility research operates under a shared "Observation-First" paradigm, treating flow patterns as observable targets from which models are supervised. | Synthesized from Wilson (1971), Barbosa et al. (2018), Simini et al. (2021), Rong et al. (2023), Guo et al. (2025), and Yang et al. (2026). | Demonstrates the historical consistency of mapping from observed interactions ($T_{ij}$) to fit model parameters ($\theta$) or neural weights across classical and AI frameworks. | Formalizes this shared paradigm as the root cause of the field's vulnerability: when detailed observations are withheld, the entire supervised framework collapses. |
| **G6. Transition to Layer H** | Why does the conventional paradigm fail in the modern data era? | The conventional paradigm collapses in cities lacking detailed mobility observations due to cost barriers or strict privacy-preserving data aggregation and pruning. | de Montjoye, Y. A., Hidalgo, C. A., Verleysen, M., & Blondel, V. D. (2013). Unique in the crowd: The privacy bounds of human mobility. *Scientific Reports*, 3, 1376; Gallotti, R., Bazzani, A., Rambaldi, S., & Barthelemy, M. (2024). Detors: Biases in human mobility data impact epidemic modeling. *Preprint/Nature*; Yang, Y., Herrera, C., Eagle, N., & González, M. C. (2014). Limits of predictability in commuting flows in the absence of data for calibration. *Scientific Reports*, 4, 5662. | Documents the breakdown of predictive models in data-poor and privacy-restricted environments, demonstrating that data pruning severely distorts baseline networks and epidemic simulations. | Direct theoretical bridge to Layer H (Research Gaps): establishes the urgent scientific need for a paradigm shift from "Observation-First" to "Behavioural Identifiability" from highly compressed aggregate statistics. |


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

#### 1. Scientific Master Matrix for Layer H (Optimized)

| Section | Scientific Question | Core Claim | Main Supporting References (APA) | Contribution of References | Thesis Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **H. Scientific Synthesis and Research Gaps** | What remains systematically unresolved in human mobility science? | Despite significant advances in representation learning and spatial prediction, two fundamental scientific gaps persist regarding collective behavioral identification and pure structural transferability. | Synthesized from Layers A–G. | Documents the limitations of the conventional supervised, "Observation-First" paradigm in data-sparse or privacy-restricted urban contexts. | Synthesizes existing literature to establish a new, unified research agenda grounded in behavioral identifiability. |
| **H1. Scientific Consensus** | What fundamental principles has the scientific community established? | Urban Human Mobility is a measurable, highly structured spatial interaction process governed jointly by physical urban morphology (opportunities) and collective distance-decay (behavior). | Barbosa, H., et al. (2018). Human mobility: Models and applications. *Physics Reports*, 734, 1–74; Wilson, A. G. (1971). A family of spatial interaction models. *Environment and Planning A*; Tanner, J. C. (1961). Factors affecting the amount of travel. *RRT*; Guo, J., et al. (2025). A universal geography neural network. *CACE*. | Establishes the empirical existence of stable distance-decay regularities and the capability of GeoAI to represent multi-modal urban features. | Validates the physical and behavioral foundations of spatial interaction modeling before introducing the data-scarcity problem. |
| **H2. Scientific Uncertainties** | What core tensions remain unresolved in current spatial models? | Collective travel behavior remains a latent, unobservable utility parameter, and current deep learning models fail to disentangle this behavioral sensitivity from the underlying urban morphology. | Barbosa et al. (2018); Simini, F., et al. (2021). A Deep Gravity model for mobility flows generation. *Nature Communications*; Guo et al. (2025); Enaya, A., et al. (2026). TransGM. *CEUS*. | Demonstrates that state-of-the-art predictive networks (Deep Gravity, UGNN) jointly optimize features in an end-to-end black box, entangling structure and behavior. | Frames the "entanglement" of physical urban form and traveler preferences as the root cause of transferability failure. |
| **H3. Research Gap I – Behaviour Identification** | Can latent collective travel behavior ($\theta$) be identified in the absence of fine-grained flow observations? | Existing estimation paradigms require complete, high-cost OD matrices to calibrate behavioral parameters, while the scientific possibility of recovering $\theta$ from compressed, privacy-preserving aggregate statistics remains unformalized. | Merlin, L. A. (2020). A new method using medians to calibrate single-parameter spatial interaction models. *JTLU*; Liang, X., et al. (2013). Unraveling the origin of exponential law. *Scientific Reports*; Yang, Y., et al. (2014). Limits of predictability in commuting flows. *Scientific Reports*; Gallotti, R., et al. (2024). Distorted insights from human mobility data. *Nature Communications*. | Merlin (2020) demonstrates the sufficiency of a single median travel time for calibration. Yang (2014) highlights calibration failure under data scarcity. Gallotti (2024) reveals biases introduced by aggregate privacy-preserving filters. | Identifies Gap I: Prior work either curve-fits TLDs without structural constraints or relies on full ODs. This thesis formalizes behavioral identification directly from aggregate TLDs under known structures. |
| **H4. Research Gap II – Transferable Urban Structure** | Can physical urban structure representations be transferred across geographical domains independently of behavioral bias? | Current transfer-learning models transfer entire neural networks (model-centric) or multi-modal spatial embeddings (embedding-centric), which fail when target cities exhibit different behavioral profiles or segregation dynamics. | Yang, J., et al. (2026). Transferable Human Mobility Network Reconstruction with neuroGravity. *Preprint/SJTU*; Enaya et al. (2026); Guo et al. (2025); Xu, Y., et al. (2025). Predicting human mobility flows using satellite imagery. *Nature Communications*. | Yang (2026) demonstrates that spatial income segregation bounds model transferability. Enaya (2026) uses KL divergence to adapt models based on spatial patterns but still relies on target-domain flow signals. | Identifies Gap II: Existing transfer learning adapts black-box weights rather than transferring the pure, decoupled physical structure. This thesis proposes transferring only represented Urban Structure. |
| **H5. Unified Scientific Perspective** | How are the two gaps theoretically connected? | Behavioral Identification (Gap I) and Transferable Urban Structure (Gap II) are complementary problems unified under the Structure–Behaviour Separation Principle of spatial interaction. | Synthesized from Wilson (1971), Haynes & Fotheringham (1984), Simini et al. (2021), and Enaya et al. (2026). | Prior literature provides separate components of spatial friction and opportunities but treats them as joint statistical targets. | Formalizes a unified epistemological framework: if we can represent and transfer Structure (Gap II), we can use it as a hard constraint to resolve latent Behaviour from aggregate statistics (Gap I). |
| **H6. Transition to the Research Proposal** | What formal scientific framework must be developed next? | These gaps motivate the development of the Probabilistic Constrained Spatial Flow - Travel Impedance Model (PCSF-TIM) framework to provide empirical statistical evidence for behavioral identifiability and evaluate downstream planning applications. | Synthesized from the entire Research Knowledge Base (RKB). | Literature motivates the limits of prediction, necessitating a transition to a mathematically bounded, generative reconstruction framework. | Direct transition from the systematic literature review to the formal mathematical and experimental proposal. |


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
