| Module | Scientific Question | Scientific Claim | Role in Paper 1 | Future Development |
| --- | --- | --- | --- | --- |
| **A. Gravity as the Scientific Representation of Human Mobility** | **Why should collective human mobility be formulated in a gravity representation?** | Gravity representation provides the most principled explicit representation for separating urban structure from travel behaviour, thereby enabling behavioural identification. | **Core** | Stable foundation |
| **B. Representation of Collective Distance Sensitivity** | **How is collective distance sensitivity represented within the gravity representation?** | Distance-decay provides an explicit mathematical representation of collective distance sensitivity in human mobility. | **Core** | Stable foundation |
| **C. Classical Parameter Identification** | **How has travel behaviour traditionally been identified?** | Behavioural parameters are statistically identifiable when complete observations are available. | **Core** | Stable foundation |
| **D. Aggregate Mobility Observation** | **What changes when mobility is observed only in aggregate form?** | Every mobility dataset is a projection of the underlying spatial interactions rather than a different reality. | **Core** | Stable foundation |
| **E. Information Preservation under Aggregation** | **What behavioural information is preserved after aggregation?** | Different observation levels preserve different amounts of behavioural information. | **Core** | Expanded into information-theoretic analysis |
| **F. The Distance-decay Identification Problem** | **Can collective distance sensitivity still be identified from aggregate observations?** | Behavioural identifiability after projection is the central unresolved scientific problem. | **Core** | Stable foundation |
| **G. Distance-decay Identification Framework** | **How can distance-decay parameters be identified from aggregate travel-distance distributions?** | The proposed framework solves this inverse problem by recovering distance-decay parameters from aggregate observations. | **Core contribution of Paper 1** | Generalized beyond Gravity |
| **H. Urban Structure Representation** | **How should urban structure be represented independently of mobility observations?** | Urban structure can be explicitly represented through functional zones, populations, and POIs, serving as the structural counterpart to behavioural distance-decay. | **Supporting Context** | **Core contribution of Paper 2** |
| **I. Transferability of Urban Structure** | **Which components of urban structure are transferable across cities?** | Structural representations learned from data-rich environments can be transferred to data-scarce environments. | **Literature Review** | **Core contribution of Paper 2** |
| **J. The Limits of Identifiability** | **When are distance-decay parameters identifiable from aggregate observations?** | Identifiability depends systematically on urban structure characteristics, data resolution, and observational noise. | **Discussion** | **Core contribution of Paper 3** |
| **K. Future Directions** | **What remains beyond behaviour identification?** | Behaviour identification opens pathways to theoretical extensions including Information Theory and General Representations. | **Discussion** | Future Research |

> **Scoping Definition:** *Throughout this handbook, we use the term "behavioural representation" to refer specifically to the collective response to spatial separation encoded by the distance-decay function, rather than to the full spectrum of travel behaviour studied in transportation science.*

Module A

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **A1** | Gravity is a canonical representation of spatial interaction, not merely a predictive model. | Zipf (1946); Wilson (1971); Haynes & Fotheringham (1984); Barbosa et al. (2018) | These works establish Gravity as the dominant framework for modelling aggregate spatial interaction. | **Representation Shift:** Framing Gravity as a representation rather than just a predictive model. |
| **A2** | Gravity explicitly represents spatial interaction by factorizing origin, destination, and distance components. | Wilson (1971); Fotheringham & O'Kelly (1989); Haynes & Fotheringham (1984) | The Gravity formulation explicitly separates origin factors, destination factors, and spatial impedance. | None (Established knowledge). |
| **A3** | Within the Gravity representation, the distance-decay function isolates the collective response to spatial separation. | Wilson (1971); Haynes & Fotheringham (1984); Barbosa et al. (2018) | Classical Gravity models isolate spatial impedance into an explicit distance-decay function. | **Handbook interpretation:** the collective response to spatial separation provides the behavioural perspective adopted throughout this Handbook. |
| **A4** | Recent gravity-informed models continue to preserve this explicit factorization of origin, destination, and distance components. | Yang et al. (2026, neuroGravity); Enaya et al. (2026, TransGM); Zhu & Ma (2026) | These models retain explicit structural components rather than replacing them entirely with black-box neural representations. | None (Evidence that the explicit representation remains scientifically relevant). |
| **A5** | The Gravity representation provides one of the clearest explicit formulations for separating urban structure from travel behaviour. | Wilson (1971); Haynes & Fotheringham (1984); Fotheringham & O'Kelly (1989) | Because each component is explicitly factorized, structural effects can be analysed separately from behavioural effects. | **Handbook synthesis.** |
| **A6** | **First Principle of Mobility Representation:** *Collective human mobility should be formulated in an explicit representation that separates urban structure from travel behaviour. Throughout this handbook, we adopt the gravity representation because it provides the clearest explicit factorization for this purpose.* | Supported by Claims A1–A5. | The explicit factorization provides a transparent representation suitable for subsequent parameter identification. | **Fundamental Principle of this Handbook.** Gravity is adopted as a principled starting representation, not because it is universally superior at predicting flows, but because it adheres to this First Principle. |

Module B

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **B1** | Spatial interaction generally decreases with increasing spatial separation. | Tobler (1970); Haynes & Fotheringham (1984); Barbosa et al. (2018) | Classical geography consistently observes declining interaction with increasing separation due to spatial impedance. | None (Established knowledge). |
| **B2** | Once mobility is formulated in a Gravity representation, responses to spatial separation are explicitly encoded through parameterized distance-decay functions. | Wilson (1971); Haynes & Fotheringham (1984); Fotheringham & O'Kelly (1989) | Gravity representation explicitly factorizes spatial impedance through distance-decay functions. | None (Established knowledge). |
| **B3** | Distance-decay functions provide the explicit mathematical representation of collective distance sensitivity in human mobility. | Wilson (1971); Barbosa et al. (2018) | The distance-decay function completely specifies how aggregate interaction varies as spatial separation increases, isolating behaviour from scale. | **Handbook interpretation:** distance-decay is not just a function, it is the behavioural representation of distance sensitivity itself. |
| **B4** | Explicit behavioural representations through distance-decay appear across a wide range of spatial interaction models. | Huff (1963); Hansen (1959); Balcan et al. (2009); Martínez & Viegas (2013) | Retail trade-area models, accessibility measures and epidemiological models all rely on this behavioural encoding. | None (Established synthesis). |
| **B5** | Alternative modelling paradigms demonstrate that spatial interaction can also be represented without parameterized distance-decay functions. | Stouffer (1940); Simini et al. (2012) | Intervening Opportunities and Radiation models explain spatial interaction using different behavioural representations. | Defines the scope of applicability of the Handbook. |
| **B6** | Models with explicit distance-decay formulations encode behaviour through specific model parameters, establishing a direct link between mathematical representation and statistical identifiability. | Wilson (1971); Flowerdew & Aitkin (1982); Sen & Smith (1995) | Explicit parameterization makes the behavioural representation directly identifiable from observations. | **Methodological motivation for the Handbook.** |
| **B7** | The explicit parameterization of distance-decay provides the necessary mathematical foundation for formulating behaviour identification as a statistical problem. | Supported by Claims B2–B6. | Once behaviour is explicitly parameterized, recovering that behaviour becomes a parameter identification problem. | **Bridge to Module C.** |

Module C

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **C1** | Behavioural representations have traditionally been identified (calibrated) using complete, observed Origin–Destination flows. | Wilson (1971); Haynes & Fotheringham (1984); Ortúzar & Willumsen (2011) | Classical Gravity calibration identifies the behavioural representation from complete OD matrices. | None (Established knowledge). |
| **C2** | Multiple calibration methods have been developed to identify these behavioural parameters. | Wilson (1971); Flowerdew & Aitkin (1982); Haynes & Fotheringham (1984); Lenormand et al. (2016) | Entropy, least squares, and Poisson likelihood all serve as algorithms for identifying the underlying behavioural representation. | None (Established knowledge). |
| **C3** | Maximum Likelihood Estimation provides a statistically principled framework for behaviour identification. | Flowerdew & Aitkin (1982); Ben-Akiva & Lerman (1985) | Formulating calibration as statistical inference provides rigorous likelihood evidence for parameter identification. | None (Established statistical methodology). |
| **C4** | Although algorithms differ, classical calibration methods all attempt to identify the same underlying behavioural representation. | Wilson (1971); Flowerdew & Aitkin (1982); Lenormand et al. (2016) | Different optimisation procedures are just different ways to estimate the same behavioural parameters. | **Handbook synthesis:** unifies calibration methods as different solutions to the same identification problem. |
| **C5** | The most widely used identification methods assume access to complete Origin–Destination flow observations. | Wilson (1971); Haynes & Fotheringham (1984); Ortúzar & Willumsen (2011); Flowerdew & Aitkin (1982) | Classical calibration requires the full OD interaction matrix to identify parameters. | None (Established knowledge). |
| **C6** | A classical minority tradition already identifies behavioural representations from aggregate trip-length moments rather than full OD flows. | Tanner (1961); Hyman (1969); Merlin (2020) | Tanner and Hyman calibrate parameters by matching the mean observed trip length; Merlin (2020) uses the median. These require observed trips from the target city. | **Important scope correction.** Aggregate identification exists, but typically constrains only a single moment and requires local trip observations. |
| **C7** | The requirement for complete Origin–Destination flows prevents the identification of behavioural representations when only aggregate mobility observations are available. | Barbosa et al. (2018); Buckee et al. (2020); Oliver et al. (2020) | Aggregate mobility products generally do not release the complete OD interactions required by conventional identification. | **Motivates Module D.** |
| **C8** | Existing research focuses heavily on improving prediction accuracy using complete mobility observations, rather than on whether behavioural representations can be identified when observations are incomplete. | Lenormand et al. (2016); Simini et al. (2021, Deep Gravity); Atwal et al. (2025); Xu et al. (2025, Imagery2Flow); Shi et al. (2020, MPGCN) | Most studies assume observed mobility flows are available for supervision. | **Bridge to Modules D–F.** |

Module D

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **D1** | Human mobility observation has fundamentally shifted toward continuously collected digital traces. | Barbosa et al. (2018); González et al. (2008); Song et al. (2010) | Advances in mobile sensing changed the nature of mobility observation. | None (Established knowledge). |
| **D2** | Aggregate mobility products—including Meta's Movement Distribution Maps (MDM)—are becoming increasingly available across platforms and regions, providing privacy-preserving summaries of population travel behavior. | Meta Movement Distribution Maps (2026); Buckee et al. (2020) | Modern mobility products publish aggregated statistics instead of complete trajectories or OD matrices. | None (Established knowledge). |
| **D3** | Privacy, scalability, and operational constraints increasingly force the transformation of complete mobility observations into aggregate projections. | de Montjoye et al. (2013); Oliver et al. (2020); Houssiau et al. (2022) | Re-identifiability risks push data providers to project raw data into lower-dimensional aggregate summaries. | None (Established knowledge). |
| **D4** | Modern mobility observations are not a different reality, but rather projected summaries of the underlying spatial interactions. | Meta Movement Distribution Maps (2026); Barbosa et al. (2018); Buckee et al. (2020) | Datasets reporting aggregate indicators (e.g. trip-length distributions) are projections of the full OD matrix. | **Handbook interpretation:** framing data products as mathematical projections. |
| **D5** | Every mobility dataset represents a specific projection of the underlying mobility reality (Trajectory → OD → Distance Distribution → Moments). | Barbosa et al. (2018); Gallotti et al. (2024) | Aggregation transforms the observation by compressing individual interactions into population-level projections. | **Bridge to Module E.** |
| **D6** | The transition to aggregate observations fundamentally changes the mathematical form of the observation, necessitating a new approach to behaviour identification. | Built upon Modules C and D. | Conventional identification assumes complete OD projections, whereas modern data provides lower-dimensional projections. | **Primary conclusion of Module D.** |

Module E

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **E1**   | Every observational projection fundamentally acts as an information filter, preserving certain structural and behavioural signals while irrevocably destroying others. | Casella & Berger (2002); Gallotti et al. (2024) | In statistical terms, projections are many-to-one maps that reduce dimensionality and induce information loss. | **Establishes the link between mathematical projection and information theory.** |
| **E2**   | Different observational projections preserve different amounts of behavioural information. | Barbosa et al. (2018); Song et al. (2010); Gallotti et al. (2024) | Each projection retains different spatial, temporal and relational information. | None (Established synthesis). |
| **E3**   | Successive projections compress mobility observations while preserving specific structural and behavioural properties. | Casella & Berger (2002); Barbosa et al. (2018) | In statistical terms, each projection (OD → TLD) is a many-to-one map of the sample space that discards some information while preserving others. | **Introduces Information Preservation as a core concept.** |
| **E4**   | Aggregation is formally equivalent to applying an observational projection that alters the informational content of the data. | Casella & Berger (2002) | Any statistic of the data defines a projection transformation (spatial, temporal, or distributional). | **Clarifies the statistical nature of aggregation.** |
| **E5**   | Observational projections progressively change the balance of preserved structural vs. behavioural information. | Built upon E2–E4 | As observations are projected to lower dimensions, the separability of urban structure and travel behaviour may change. | **Key theoretical insight of the Handbook.** |
| **E6**   | Mobility datasets should be analyzed based on the information they preserve rather than the sensing technology used to collect them. | Barbosa et al. (2018); Pappalardo et al. (2023); Gallotti et al. (2024) | Preserved information provides a technology-independent, representation-centric organizational principle. | **Conceptual framing of the Handbook.** |
| **E7**   | Analyzing information preservation naturally motivates the question of whether a given projection preserves sufficient information to identify the underlying behavioural representation. | Built upon Modules C–E | The central scientific question shifts from "Do we have enough data?" to "Does this projection preserve identifiability?" | **Bridge to Module F.** |

Module F

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **F1** | Most behaviour identification methods assume the availability of complete Origin–Destination flow projections. | Wilson (1971); Haynes & Fotheringham (1984); Ortúzar & Willumsen (2011); Flowerdew & Aitkin (1982) | Classical estimation relies on the full OD matrix. | None (Established paradigm). |
| **F2** | Modern observations increasingly provide highly compressed, aggregate projections of mobility. | Barbosa et al. (2018); Meta Movement Distribution Maps (2026); Buckee et al. (2020); Oliver et al. (2020) | Contemporary products publish aggregate statistics instead of complete OD data. | None (Established trend). |
| **F3** | Existing research primarily focuses on improving flow prediction under complete observation, assuming the behaviour is inherently identifiable. | Lenormand et al. (2016); Simini et al. (2021, Deep Gravity); Atwal et al. (2025); Xu et al. (2025, Imagery2Flow); Shi et al. (2020, MPGCN) | Most methods assume complete flows are available for calibration or supervision. | **Handbook synthesis.** |
| **F4** | Aggregate projections preserve fundamentally different behavioural information than complete Origin–Destination projections. | Built upon Module E; Gallotti et al. (2024). | Different projection forms preserve different subsets of information. | Logical consequence of Module E. |
| **F5** | Existing aggregate identification methods rely on single-moment projections and still require local observations to constrain the behavioural representation. | Tanner (1961); Hyman (1969); Merlin (2020); Yang et al. (2014) | Mean- and median-matching calibration use one summary statistic of locally observed trips. | **Precise statement of what is already solved.** |
| **F6** | It remains a central unresolved scientific problem whether behavioural representations remain identifiable after projection onto aggregate travel-distance distributions without any observed local trips. | No direct reference (Research Gap); positioned against F5. | The literature addresses either complete OD-based identification or single-moment identification; full-distribution identifiability from projections is an open question. | **Central research question of the Handbook and Paper 1.** |
| **F7** | Explicitly parameterized behavioural representations provide the most rigorous framework for investigating this theoretical gap. | Built upon Modules B–C. | Explicit representation allows behaviour identification to be formulated as a statistical inverse problem. | **Methodological justification for Paper 1.** |
| **F8** | Aggregate travel-distance distributions (TLDs) provide a natural test case for identifiability because they directly project responses to spatial separation while compressing spatial structure. | Built upon Modules B and E. | TLDs retain information about distance-decay while abstracting away individual OD pairs. | **Bridge to Module G.** |

Module G

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **G1** | The recovery of behavioural representations from projected aggregate observations can be formulated as a statistical inverse problem. | Built upon Modules B–F; Casella & Berger (2002); Bishop (2006) | Formulating an observation model allows statistical inference to recover underlying parameters from projected data. | **Methodological foundation of Paper 1.** |
| **G2** | Aggregate travel-distance distributions (TLDs) provide a sufficient projection of reality to formulate a computable likelihood function for the behavioural representation. | This Paper; Flowerdew & Aitkin (1982) | The proposed framework defines a likelihood function directly on aggregate TLDs without reconstructing the full OD matrix. | **Primary methodological contribution of Paper 1.** |
| **G3** | The proposed Identification Framework recovers the behavioural representation by matching the full shape of the projected aggregate distribution using urban structure derived from open data. | This Paper; contrasted with Tanner (1961); Hyman (1969); supported by Liang et al. (2013); Vu et al. (2021) | Differs from classical methods by leveraging the full distributional shape and requiring no observed local trips. | **Primary algorithmic contribution.** |
| **G4** | Successful parameter recovery provides strong empirical statistical evidence that the underlying behavioural representation remains identifiable after aggregate projection. | This Paper; Casella & Berger (2002) | Consistent parameter recovery across synthetic and real-world experiments supports practical identifiability, demonstrating stable likelihood surfaces and accurate downstream validation. | **Empirical contribution of Paper 1.** |
| **G5** | The framework yields consistent behavioural identification across diverse urban structures, demonstrating the robustness of the representation separation. | Results of this paper | Recovery performance remains stable and consistent across heterogeneous cities, confirming that the framework effectively factors out varying urban structures. | **Empirical evidence.** |
| **G6** | While empirical recoverability is established, formal theoretical characterization of information preservation and statistical sufficiency remains an open research problem for future extensions. | Casella & Berger (2002) | Experimental success provides empirical evidence, bounding the scope of this empirical framework. | **Defines the boundary of Paper 1.** |
| **G7** | Behavioural identification from aggregate projections provides a foundation for knowledge-assisted mobility reconstruction in data-scarce environments. | Yang et al. (2026, neuroGravity); Enaya et al. (2026, TransGM); Xu et al. (2025, Imagery2Flow); Wang et al. (2025, Similarity Transfer) | Once behaviour is identified, transferring structural knowledge from deep mobility models can enable OD reconstruction where no mobility observations exist. | **Future Research Vision.** |

Module H

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **H1** | Urban structure provides the spatial context in which collective mobility behaviour unfolds. | Zipf (1946); Wilson (1971) | Classical gravity explicitly separates this structure (masses) from the behavioural cost. | None (Established knowledge). |
| **H2** | Modern open data sources (OSM, POIs, Land Use) provide high-resolution, objective representations of this urban structure. | Vu et al. (2021) | Open data enables extraction of urban structures without relying on proprietary mobility data. | **Supporting Context.** |
| **H3** | Deep learning embeddings can capture latent spatial and functional representations of these urban structures. | Yang et al. (2026, neuroGravity); Enaya et al. (2026, TransGM) | Neural networks encode structural features for mobility generation. | **Supporting Context.** |
| **H4** | Representing urban structure independently of mobility observations is a prerequisite for separating structure from behaviour. | Built upon A5 and H1–H3 | Ensures the structural term in the Gravity representation does not leak behavioural information. | **Foundation for Paper 2.** |

Module I

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **I1** | While mobility behaviour (distance sensitivity) is context-dependent, fundamental representations of urban structure often exhibit transferability across cities. | Wang et al. (2025, Similarity Transfer) | Deep structure mappings show generalizability. | None (Established literature). |
| **I2** | Deep mobility models demonstrate that learned structural embeddings can be transferred to unseen cities. | Yang et al. (2026); Enaya et al. (2026) | Models like neuroGravity and TransGM achieve zero-shot or few-shot transfer. | **Literature Review.** |
| **I3** | Transferable urban structure, when combined with locally identified behaviour, provides a mechanism for zero-OD reconstruction. | Built upon G7 and I2 | Fusing local $\theta$ with transferred structural embeddings solves the data-scarce reconstruction problem. | **Foundation for Paper 2.** |

Module J

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **J1** | Parameter identifiability is not a binary property but a spectrum determined by data quality and urban context. | Casella & Berger (2002) | Theoretical identifiability bounds depend on the sample space properties (the urban structure). | None (Statistical foundation). |
| **J2** | The ability to recover behavioural parameters depends systematically on the amount of information preserved by the projection (e.g., TLD bin resolution, noise). | Gallotti et al. (2024) | Information loss directly reduces the curvature of the likelihood surface. | **Handbook synthesis.** |
| **J3** | Specific urban structural characteristics (e.g., density, polycentricity) inherently make distance-decay parameters easier or harder to identify. | Built upon Modules H, I | Different spatial layouts provide different amounts of structural variance to constrain the behavioural estimation. | **Discussion point in Paper 1.** |
| **J4** | Establishing the theoretical and empirical boundaries of identifiability is essential for knowing when and where to trust aggregate mobility inference. | Built upon Modules G, H, J1–J3 | Establishes the need for a robust meta-analysis across large-scale datasets with known ground truth. | **Foundation for Paper 3.** |

Module K

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **K1** | The empirical success of parameter identification from aggregate data poses deeper theoretical questions regarding information sufficiency. | Casella & Berger (2002) | Empirical identifiability suggests underlying mathematical sufficiency. | **Theoretical gap identification.** |
| **K2** | Formalizing mobility projections using Information Geometry and Fisher Information offers a pathway to prove theoretical limits of behaviour identification. | (Future Works) | Advanced information theory provides bounds on parameter recovery. | **Future Direction.** |
| **K3** | Generalizing the identification framework beyond Gravity representations remains a grand challenge in human mobility science. | Simini et al. (2012); Gallotti et al. (2024) | Moving from parameterized distance-decay to general non-parametric representations. | **Future Direction.** |

---

### The Distance-decay Identification Research Program (3-Paper Scope)

**Scientific Program:** This PhD research aims to establish a scientific framework for mobility inference under limited observations through three complementary stages:
1. Behaviour identification (Can we infer?)
2. Mobility inference (Can we use it?)
3. Scientific characterization of identifiability (When should we believe it?)

This Handbook establishes the foundation for a broader research program spanning three distinct papers to be executed over 3–5 years. The program progressively expands from parameter identification to full mobility reconstruction, culminating in a robust evaluation of its own scientific limits:

```text
Paper 1
=================
Estimate θ

Paper 2
=================
Estimate OD

Paper 3
=================
Evaluate confidence
Understand limits
Quantify uncertainty
Characterize identifiability
```

#### Paper 1: The Distance-decay Identification Framework (This Handbook)
- **Central Question:** Can collective distance sensitivity (distance-decay parameters) be identified from aggregate mobility observations?
- **Pipeline:** Reality → Gravity representation → Distance-decay representation → Classical parameter identification → Aggregate observation → Information preservation → Distance-decay identification.
- **Core Contribution:** Establishes the Distance-decay Identification Framework, demonstrating that behavioural parameters can be consistently identified across diverse urban structures, while revealing systematic variations that motivate further investigation.

#### Paper 2: Zero-OD Mobility Reconstruction
- **Central Question:** Can local behaviour and transferable structure be decoupled?
- **Hypothesis:** Urban structure is substantially more transferable across cities than travel behaviour.
- **Pipeline:** Behaviour identified (from Paper 1) + Open urban structure → Transferable structure learning (from deep models) → OD reconstruction.
- **Core Contribution:** Estimates OD without target-city mobility observations by combining locally identified behaviour with transferable urban structure, demonstrating the zero-OD reconstruction approach on target case studies.

#### Paper 3: Understanding the Conditions for Identifiability
- **Central Question:** When are distance-decay parameters identifiable from aggregate mobility observations?
- **Pipeline:** Empirical Identification → Data Degradation Experiments (Noise, Bins, Sample Size) → Urban Structure Profiling → Identifiability Meta-analysis.
- **Core Contribution:** Shifts from methodological application to deep scientific understanding by investigating the conditions that make mobility inference reliable. A possible outcome is defining a quantitative Identifiability Index, but the primary focus is mapping the theoretical and empirical boundaries that define *when* behaviour can be reliably recovered across 50 full-OD cities under varied experimental conditions.

#### Strategic Evaluation as a PhD Research Program
This 3-paper architecture provides a complete, cohesive, and low-risk foundation for a "PhD by Publication" (Cumulative Dissertation).
- **The "Red Thread" (Cohesion):** The program follows a rigorous logical progression: Methodological Innovation (Paper 1) → High-Impact Application (Paper 2) → Statistical Validation and Meta-Analysis (Paper 3). This avoids the common pitfall of disjointed dissertation chapters.
- **Data Feasibility and Scale:** Operating on a dataset of ~50 structurally diverse cities elevates the research from localized case studies to a large-scale empirical evaluation. A sample size of N=50 provides:
  - **For Paper 1:** Robust proof of generalized applicability across varying urban structures (demonstrating consistency via distribution metrics rather than cherry-picked examples).
  - **For Paper 2:** A rigorous K-fold cross-validation setup (e.g., train on 40 source cities, transfer to 10 target cities) to definitively validate structural transferability.
  - **For Paper 3:** The availability of 50 full-OD ground truth matrices enables a profound meta-analysis of identifiability limits. It allows us to perturb the data (e.g., varying TLD bins, spatial resolution, and noise) and regress recovery accuracy against city-level descriptors (polycentricity, density), elevating the paper from a simple reliability report to a foundational scientific study of when mobility inference succeeds.
- **Risk Mitigation:** Utilizing open urban data (OSM, WorldPop) alongside explicitly aggregated open mobility datasets (e.g., Meta MDM) reduces data-acquisition risk to near zero, ensuring a highly feasible 3-to-4-year research timeline.


References
---

# I. Spatial Interaction Foundations

| Ref ID | Reference                                                       | Year | BibTeX key | Hỗ trợ Module | Vai trò                                |
| ------ | --------------------------------------------------------------- | ---- | ---------- | ------------- | -------------------------------------- |
| R1     | Zipf, G.K. *The $P_1P_2/D$ Hypothesis: On the Intercity Movement of Persons*, Am. Sociol. Rev. 11(6) | 1946 | `zipf1946` | A             | Early sociological formalization of the gravity analogy (not its historical origin) |
| R2     | Wilson, A.G. *A Family of Spatial Interaction Models, and Associated Developments*, Env. Plan. A | 1971 | `wilson1971` | A, B, C, F    | Entropy derivation, Gravity foundation |
| R3     | Tobler, W. *A Computer Movie Simulating Urban Growth in the Detroit Region*, Econ. Geogr. | 1970 | `tobler1970computer` | B             | Source of the "First Law of Geography"; distance-decay principle |
| R4     | Haynes & Fotheringham. *Gravity and Spatial Interaction Models*, Sage | 1984 | `haynes1984gravity` | A, B, C, F    | Textbook kinh điển                     |
| R5     | Fotheringham & O'Kelly. *Spatial Interaction Models: Formulations and Applications*, Kluwer | 1989 | `fotheringham1989spatial` | A, B          | Spatial interaction theory             |
| R6     | Hansen, W. *How Accessibility Shapes Land Use*, JAIP 25(2) | 1959 | `hansen1959accessibility` | B, G          | Accessibility & distance decay         |
| R8     | Sen & Smith. *Gravity Models of Spatial Interaction Behavior*, Springer | 1995 | `sen1995gravity` | B    | Statistical theory of gravity model estimation |

---

# II. Human Mobility Foundations

| Ref ID | Reference                                                               | Year | BibTeX key | Module | Vai trò                            |
| ------ | ----------------------------------------------------------------------- | ---- | ---------- | ------ | ---------------------------------- |
| R7     | Barbosa et al. *Human Mobility: Models and Applications*                | 2018 | `barbosa2018human` | A–G | Review lớn nhất về Human Mobility  |
| R9     | González et al. *Understanding Individual Human Mobility Patterns*      | 2008 | `gonzalez2008understanding` | D, E   | Individual mobility (CDR)          |
| R10    | Song et al. *Limits of Predictability in Human Mobility*                | 2010 | `song2010limits` | D, E   | Human mobility predictability; entropy of mobility |
| R32    | Pappalardo et al. *Future Directions in Human Mobility Science*         | 2023 | `pappalardo2023analytical` | D, E   | Agenda review; framing of mobility data |
| R33    | Gallotti et al. *Distorted Insights from Human Mobility Data*           | 2024 | `gallotti2024distorted` | D, E, F, G | Representation choice changes inference |
| R34    | Blondel et al. *A Survey of Results on Mobile Phone Datasets Analysis*  | 2015 | `blondel2015survey` | G      | Survey of CDR-based mobility observation |

---

# III. Distance-decay & Alternative Models

| Ref ID | Reference                                                             | Year    | BibTeX key | Module | Vai trò                           |
| ------ | --------------------------------------------------------------------- | ------- | ---------- | ------ | --------------------------------- |
| R11    | Simini et al. *A Universal Model for Mobility and Migration Patterns* | 2012    | `Simini2012universal` | B      | Radiation Model                   |
| R12    | Stouffer. *Intervening Opportunities: A Theory Relating Mobility and Distance* | 1940 | `stouffer1940intervening` | B      | Alternative behavioural mechanism |
| R13    | Huff. *A Probabilistic Analysis of Shopping Center Trade Areas*, Land Econ. 39(1) | 1963 | `huff1963probabilistic` | B, G   | Huff Model                        |
| R14    | Ortúzar & Willumsen. *Modelling Transport*, 4th ed.                   | 2011    | `ortuzar2011modelling` | C, F   | Behaviour calibration             |
| R28    | Balcan et al. *Multiscale Mobility Networks and Infectious Diseases*  | 2009    | `balcan2009multiscale` | B      | Epidemic spatial model with a fitted gravity law |
| R29    | Lenormand et al. *Systematic Comparison of Trip Distribution Laws and Models* | 2016 | `lenormand2016systematic` | C, F, G | Systematic comparison of trip distribution laws and calibration |
| R35    | Martínez & Viegas. *A New Approach to Modelling Distance-Decay Functions* | 2013 | `martinez2013distance` | B, G   | Distance-decay functional forms for accessibility |
| R48    | Liang et al. *Unraveling the Origin of Exponential Law in Intra-Urban Human Mobility* | 2013 | `liang2013unraveling` | G    | Proves intra-urban trips decay exponentially due to urban population density decay |

---

# III-b. Aggregate / Moment-Based Calibration (counter-evidence to the gap)

⚠️ Đây là nhóm reference **bắt buộc phải trích** để tránh over-claim ở Module C và F.

| Ref ID | Reference | Year | BibTeX key | Module | Vai trò |
| ------ | --------- | ---- | ---------- | ------ | ------- |
| R36 | Tanner, J.C. *Factors Affecting the Amount of Travel*, RRL Tech. Paper 51 | 1961 | `tanner1961` | C, F, G | Deterrence function calibrated against trip-length information |
| R37 | Hyman, G.M. *The Calibration of Trip Distribution Models*, Env. Plan. A | 1969 | `hyman1969calibration` | C, F, G | Classical mean-trip-length calibration |
| R38 | Merlin, L.A. *A New Method Using Medians to Calibrate Single-Parameter Spatial Interaction Models* | 2020 | `merlin2020medians` | C, F, G | Calibration from a single summary statistic |
| R39 | Yang et al. *Limits of Predictability in Commuting Flows in the Absence of Data for Calibration* | 2014 | `yang2014limits` | C, F | Closest prior work on estimation without local calibration data |

---

# IV. Statistical Inference

| Ref ID | Reference                                               | Year | BibTeX key | Module | Vai trò                   |
| ------ | ------------------------------------------------------- | ---- | ---------- | ------ | ------------------------- |
| R15    | Ben-Akiva & Lerman. *Discrete Choice Analysis*          | 1985 | `benakiva1985discrete` | C      | MLE (disaggregate choice; cited as statistical precedent only) |
| R16    | Bishop. *Pattern Recognition and Machine Learning*      | 2006 | `bishop2006pattern` | G      | Statistical inference             |
| R17    | Murphy. *Machine Learning: A Probabilistic Perspective* | 2012 | `murphy2012machine` | G      | Bayesian & likelihood             |
| R18    | Casella & Berger. *Statistical Inference*, 2nd ed.      | 2002 | `casella2002statistical` | E, G | Classical inference; statistics as many-to-one maps; sufficiency |
| R30    | Flowerdew & Aitkin. *A Method of Fitting the Gravity Model Based on the Poisson Distribution* | 1982 | `flowerdew1982method` | B, C, F, G | Primary reference for Poisson MLE gravity calibration |

---

# V. Aggregate Mobility Revolution

| Ref ID | Reference                          | Year    | BibTeX key | Module | Vai trò                  |
| ------ | ---------------------------------- | ------- | ---------- | ------ | ------------------------ |
| R20    | Meta. *Movement Distribution Maps* (AI for Good) | 2026 | `MetaMovementDistributionMaps` | D, F | Aggregate travel-distance product used in this paper |
| R23    | Tatem. *WorldPop, Open Data for Spatial Demography* | 2017 | `worldpop2018` | D      | Cited as example of open spatial-demography data products (not used as data in this paper; cite only when population data is actually introduced) |
| R40    | Buckee et al. *Aggregated Mobility Data Could Help Fight COVID-19* | 2020 | `buckee2020aggregated` | C, D, F | Rationale for aggregate mobility release |
| R41    | Oliver et al. *Mobile Phone Data for Informing Public Health Actions* | 2020 | `oliver2020mobile` | C, D, F | Aggregate mobility products in practice |
| R42    | de Montjoye et al. *Unique in the Crowd: The Privacy Bounds of Human Mobility* | 2013 | `de2013unique` | D      | Re-identifiability motivating aggregation |
| R43    | Houssiau et al. *On the Difficulty of Achieving Differential Privacy in Practice* | 2022 | `houssiau2022dpaggregate` | D      | Privacy guarantees for aggregate location data |
| R51    | Wang et al. *Urban Human Mobility: Data-Driven Modeling and Prediction* | 2019 | `wang2019urban` | —    | Survey taxonomy classifying collective vs individual human mobility (available; not currently cited in claims) |

> **Đã loại bỏ:** Google Community Mobility Reports và Apple Mobility Trends (cả hai chỉ công bố % thay đổi số lượt ghé thăm / yêu cầu chỉ đường, không phải OD hay phân bố quãng đường, và đã ngừng phát hành từ 2022); "GDPR" (văn bản luật, không phải reference khoa học — thay bằng R42/R43); "Nature Open Mobility Dataset paper 2024" (không xác định được tác giả/venue).

---

# VI. Deep Learning Mobility

| Ref ID | Reference    | Year | BibTeX key | Module  | Vai trò                     |
| ------ | ------------ | ---- | ---------- | ------- | --------------------------- |
| R25    | Simini et al. *A Deep Gravity Model for Mobility Flows Generation* | 2021 | `simini2021` | C, F   | OD prediction requiring mobility supervision |
| R26    | Atwal et al. *Commuting Flow Prediction Using OpenStreetMap Data* | 2025 | `atwal2025commuting` | C, F   | Open-data flow prediction; still OD-supervised   |
| R27    | Yang et al. *Transferable Human Mobility Network Reconstruction with neuroGravity* | 2026 | `neurogravity2026` | A, G   | Physics-informed DL; preserves gravity decomposition |
| R31    | Enaya et al. *TransGM: Transferable Gravity Models for Cross-City Policy Transfer* | 2026 | `transgm2026` | A, G   | Transferable gravity model      |
| R44    | Zhu & Ma. *Gravity-Informed Deep Flow Inference* | 2026 | `zhu2026gravitypanel` | A | Gravity-informed neural inference |
| R45    | Xu et al. *Predicting Human Mobility Flows in Cities Using Deep Learning on Satellite Imagery* | 2025 | `xu2025imagery2flow` | C, F, G   | OD prediction from satellite imagery; still requires OD supervision — doi:10.1038/s41467-025-65373-z |
| R47    | Shi et al. *Predicting Origin-Destination Flow via Multi-Perspective Graph Convolutional Network* | 2020 | `shi2020mpgcn` | C, F | Dynamic GNN OD prediction requiring time-series OD supervision |
| R49    | Wang et al. *Similarity Based City Data Transfer Framework in Urban Digitization* | 2025 | `wang2025similarity` | G | Similarity-based cross-city transfer framework for data-poor urban environments |
| R50    | Vu et al. *Enhanced Urban Functional Land Use Map with Free and Open-Source Data*, Int. J. Digit. Earth 14(11):1744–1757 | 2021 | `vu2021landuse` | G | Deriving urban spatial structures and land use zones from open data (OSM, POI); Q1 journal (Taylor & Francis) |

---

# VII. Behaviour Identification (Paper 1)

Đây là nhóm reference **của chính bài báo**.

| Ref ID | Reference  | Module | Vai trò                              |
| ------ | ---------- | ------ | ------------------------------------ |
| P1     | This Paper | G      | Behaviour Identification Framework   |
| P2     | This Paper | G      | Statistical Behaviour Identification |
| P3     | This Paper | G      | Empirical Validation                 |

---

# VIII. Future Papers

Các reference này **chưa dùng nhiều**, nhưng sẽ rất quan trọng. ID dùng tiền tố `FW` để tránh trùng với claim ID F1–F8 của Module F.

| Ref ID | Chủ đề                 | Module |
| ------ | ---------------------- | ------ |
| FW6    | Knowledge Transfer for OD Reconstruction in Data-Scarce Cities | G |

---

# Mapping sang Handbook

Bảng này phải khớp chính xác với cột *Representative References* trong từng bảng claim.

| Module | Main References                                   |
| ------ | ------------------------------------------------- |
| **A**  | R1, R2, R4, R5, R7, R27, R31, R44                 |
| **B**  | R2–R7, R8, R11–R13, R28, R30, R35, R48            |
| **C**  | R2, R4, R7, R14, R15, R25, R26, R29, R30, R36–R41, R45, R47 |
| **D**  | R7, R9, R10, R20, R33, R40–R43                |
| **E**  | R7, R9, R10, R18, R32, R33                        |
| **F**  | R2, R4, R7, R14, R20, R25, R26, R29, R30, R33, R36–R41, R45, R47 |
| **G**  | P1–P3, R16–R18, R27, R30, R31, R33, R36–R38, R45, R48–R50, FW6 |
| **H**  | R2, R27, R31, R50 |
| **I**  | R27, R31, R49 |
| **J**  | R16–R18, R33, R43 |
| **K**  | R11, R18, R33 |

---

# Kiểm tra tính nhất quán (checklist trước khi viết bài)

- [x] Mọi reference trong bảng claim đều có bibkey tồn tại trong `paper/references.bib`.
- [x] Không còn ô reference dạng "… literature" (placeholder không kiểm chứng được).
- [x] Gap (F6) được phát biểu sau khi đã thừa nhận công trình calibration aggregate cổ điển (C6, F5).
- [x] Không dùng từ "sufficient" theo nghĩa thống kê ở phần thực nghiệm (G5), vì sufficiency chưa được chứng minh (G6).
- [x] ID claim và ID reference không trùng namespace (Module F dùng F1–F8; future work dùng FW6).
