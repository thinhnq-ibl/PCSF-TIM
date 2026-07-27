| Module                                                            | Scientific Question                                                                                                  | Mission                                                                                                                                                                                                            | Role in Paper 1                  | Future Development                                                                            |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- | --------------------------------------------------------------------------------------------- |
| **A. Gravity as the Scientific Foundation**                       | **Why is Gravity the natural scientific language for human mobility?**                                               | Establish Gravity as the canonical decomposition of mobility into **Urban Structure** and **Behaviour**.                                                                                                           | **Core**                         | Stable foundation                                                                             |
| **B. The Distance-decay Principle**                               | **Why does distance govern spatial interaction?**                                                                    | Establish distance decay as the universal behavioural law of spatial interaction rather than merely a Gravity component.                                                                                           | **Core**                         | Stable foundation                                                                             |
| **C. Conventional Behaviour Identification**                      | **How has behavioural distance decay traditionally been identified?**                                                | Review conventional calibration methods and show that they fundamentally require complete OD observations.                                                                                                         | **Core**                         | Stable foundation                                                                             |
| **D. The Aggregate Mobility Data Revolution**                     | **Why are aggregate mobility observations becoming the new standard?**                                               | Explain the transition from complete OD observations toward aggregate, scalable, privacy-preserving mobility data driven by cost, timeliness, and privacy regulations.                                             | **Core**                         | Stable foundation                                                                             |
| **E. Information Hierarchy, Compression and Information Loss**    | **How does aggregation transform mobility information?**                                                             | Organize mobility observations according to information preservation. Introduce Information Hierarchy, Information Compression, and Information Loss as the conceptual bridge between data and inference.          | **Core**                         | Later expanded into information-theoretic analysis                                            |
| **F. Research Gap**                                               | **Can behavioural parameters still be identified after information loss?**                                           | Formulate the central scientific challenge. Existing mobility science assumes complete OD matrices are necessary. Ask whether aggregate observations retain sufficient behavioural information for identification. | **Core**                         | Stable foundation                                                                             |
| **G. Empirical Behaviour Identification Framework**               | **Can behavioural distance-decay parameters be empirically recovered from aggregate travel-distance distributions?** | Present the proposed framework and its assumptions. Gravity serves as the first canonical demonstration rather than the ultimate objective.                                                                        | **Core contribution of Paper 1** | Later generalized beyond Gravity                                                              |
| **H. Statistical Foundation for Behaviour Identification**        | **Why is behavioural recovery statistically plausible?**                                                             | Develop the statistical inference framework: Observation Model → Likelihood → Identifiability → Estimator. Use empirical evidence rather than formal information-theoretic proof.                                  | **Core contribution of Paper 1** | Future work may extend to Fisher Information, Information Preservation, or Sufficiency Theory |
| **I. Empirical Evidence**                                         | **Does behavioural recovery actually work?**                                                                         | Validate the framework on synthetic and real-world cities, demonstrating robust empirical recovery of behavioural parameters.                                                                                      | **Core contribution of Paper 1** | Expanded with additional datasets and comparative studies                                     |
| **J. Research Program: Towards Behaviour Identification Science** | **What scientific questions emerge after this work?**                                                                | Position this paper as the first empirical demonstration of a broader research program on Behaviour Identification from aggregate observations.                                                                    | **Vision only**                  | Future papers progressively answer the open questions                                         |


Module A

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **A1** | Gravity is the canonical model of spatial interaction. | Zipf (1946); Wilson (1971); Haynes & Fotheringham (1984); Barbosa et al. (2018) | These works establish Gravity as the dominant and canonical framework for modelling aggregate spatial interaction across geography, transportation, migration, trade and human mobility. | None (Established knowledge). |
| **A2** | Gravity explicitly represents spatial interaction through origin, destination and distance components. | Wilson (1971); Fotheringham & O'Kelly (1989); Haynes & Fotheringham (1984) | The Gravity formulation explicitly consists of origin factors, destination factors and a distance-impedance function, providing a transparent decomposition of spatial interaction. | None (Established knowledge). |
| **A3** | Within the Gravity family of models, the distance-decay function provides an explicit representation of the collective response to spatial separation. | Wilson (1971); Haynes & Fotheringham (1984); Barbosa et al. (2018) | Classical Gravity models represent spatial impedance through an explicit distance-decay function describing how aggregate interaction changes with increasing spatial separation. | **Handbook interpretation:** the collective response to spatial separation provides the behavioural perspective adopted throughout this Handbook. |
| **A4** | Recent physics-informed mobility models continue to preserve explicit Gravity-inspired origin, destination and distance components. | neuroGravity (2026); TransGM (2026) | Recent physics-informed mobility models retain explicit Gravity-inspired structural components rather than replacing them entirely with black-box neural representations. | None (Evidence that the explicit Gravity formulation remains scientifically relevant). |
| **A5** | Gravity provides one of the clearest explicit formulations for separately analysing origin, destination and distance effects in aggregate spatial interaction. | Wilson (1971); Haynes & Fotheringham (1984); Fotheringham & O'Kelly (1989) | Because each component appears explicitly in the model formulation, their respective effects can be analysed separately. | None (Established interpretation of the explicit Gravity formulation). |
| **A6** | This Handbook adopts Gravity as its initial modelling framework because its explicit formulation enables the separate analysis of origin, destination, and distance effects on aggregate spatial interaction. | Supported by Claims A1–A5. | The explicit formulation of Gravity provides a transparent modelling framework suitable for subsequent methodological development throughout the Handbook. | **Methodological choice of this Handbook.** Gravity is adopted as the starting framework because of its explicit representation rather than because it is assumed to be universally superior to alternative mobility models. |

module B

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **B1** | Spatial interaction generally decreases with increasing spatial separation. | Tobler (1970); Haynes & Fotheringham (1984); Barbosa et al. (2018) | Classical geography and spatial interaction research consistently observe declining interaction with increasing separation due to spatial impedance. | None (Established knowledge). |
| **B2** | Within the Gravity family of models, responses to spatial separation are explicitly represented through parameterized distance-decay functions. | Wilson (1971); Haynes & Fotheringham (1984); Fotheringham & O'Kelly (1989) | Gravity models explicitly formulate spatial impedance through distance-decay functions whose parameters control the response to increasing separation. | None (Established knowledge). |
| **B3** | Distance-decay functions provide an explicit parameterization of aggregate responses to spatial separation. | Wilson (1971); Barbosa et al. (2018) | The distance-decay function specifies how aggregate interaction varies as spatial separation increases. | **Handbook interpretation:** this explicit parameterization provides the modelling basis adopted throughout the Handbook. |
| **B4** | Explicit distance-decay functions appear in many, though not all, spatial interaction models. | Gravity; Huff (1963); Hansen (1959); Balcan et al. (2009) | Many classical spatial interaction models explicitly include distance-decay, although alternative formulations also exist. | None (Established synthesis). |
| **B5** | Alternative modelling paradigms demonstrate that aggregate spatial interaction can also be represented without explicit parametric distance-decay functions. | Stouffer (1940); Simini et al. (2012) | Intervening Opportunities and Radiation models explain spatial interaction without introducing an explicit parameterized distance-decay function. | Defines the scope of applicability of the Handbook. |
| **B6** | Models with explicit distance-decay formulations represent responses to spatial separation through explicit model parameters, enabling those parameters to be empirically estimated from aggregate observations. | Gravity literature; parameter estimation literature | Explicit parameterization makes the distance-response component directly estimable from observations without requiring reconstruction of individual behavioural processes. | **Methodological motivation for the Handbook.** Explains why the Handbook focuses on this class of models. |
| **B7** | The explicit parameterization of distance-response functions provides the methodological foundation for subsequent parameter estimation. | Supported by Claims B2–B6. | Once the response to spatial separation is explicitly parameterized, the remaining scientific problem becomes estimating those parameters from observations. | **Bridge to Module C.** |

module C

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **C1** | Parameters of explicit distance-decay functions have traditionally been estimated using observed Origin–Destination flows. | Wilson (1971); Haynes & Fotheringham (1984); Ortúzar & Willumsen | Classical Gravity calibration estimates the parameters governing the distance-decay function from observed OD interactions. | None (Established knowledge). |
| **C2** | Multiple estimation methods have been developed for calibrating distance-decay parameters. | Wilson (1971); Flowerdew & Aitkin (1982); Haynes & Fotheringham (1984); Lenormand et al. (2016) | Entropy-based calibration, least squares, Poisson likelihood and related methods all estimate the parameters of explicit distance-decay functions. | None (Established knowledge). |
| **C3** | Maximum Likelihood Estimation provides a statistically principled framework for parameter estimation. | Flowerdew & Aitkin (1982); Ben-Akiva & Lerman (1985) | MLE formulates parameter estimation directly through probabilistic models of observed spatial interaction. | None (Established statistical methodology). |
| **C4** | Although estimation algorithms differ, they target the same underlying distance-decay parameters. | Wilson (1971); Flowerdew & Aitkin (1982); Lenormand et al. (2016) | Different optimisation procedures estimate the same parametric distance-response function. | **Handbook synthesis:** unifies classical calibration methods under a common parameter-estimation perspective. |
| **C5** | Conventional estimation methods require complete or sufficiently detailed Origin–Destination observations. | Gravity calibration literature; Ortúzar & Willumsen; Barbosa et al. (2018) | Classical calibration relies on observed OD interactions to estimate distance-decay parameters. | None (Established knowledge). |
| **C6** | Dependence on detailed Origin–Destination observations limits the applicability of conventional parameter estimation when only aggregate observations are available. | Barbosa et al. (2018); modern mobility literature | Aggregate mobility products generally do not provide complete OD matrices required by conventional estimation procedures. | **Motivates Module D.** |
| **C7** | Existing research has largely focused on improving estimation algorithms under available observations rather than investigating whether aggregate observations alone are sufficient for parameter estimation. | Lenormand et al. (2016); Deep Gravity (2021); Imagery2Flow (2025) | Most studies assume detailed mobility observations are available and concentrate on improving prediction or calibration accuracy. | **Bridge to Modules D–F.** |


module D

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **D1** | Human mobility observation has shifted from survey-based measurements to continuously collected digital traces. | Barbosa et al. (2018); González et al. (2008); Song et al. (2010) | Advances in mobile sensing have fundamentally changed how population mobility is observed. | None (Established knowledge). |
| **D2** | Aggregate mobility products have become increasingly available through public and commercial platforms. | Meta Movement Distribution Maps (MDM); Google Community Mobility; Apple Mobility Trends; WorldPop | Modern mobility products increasingly publish aggregated statistics instead of individual trajectories or complete OD matrices. | None (Established knowledge). |
| **D3** | Privacy, scalability and operational considerations increasingly favour the release of aggregate mobility observations. | GDPR; Barbosa et al. (2018); aggregate mobility initiatives | Modern mobility data are increasingly disseminated in aggregated form due to privacy protection and operational scalability. | None (Established knowledge). |
| **D4** | Modern mobility observations increasingly consist of aggregate summaries rather than complete Origin–Destination observations. | Aggregate mobility literature; Meta; Google; Apple | Many contemporary mobility datasets report aggregate indicators instead of complete OD matrices. | None (Established knowledge). |
| **D5** | Aggregate observations fundamentally differ from conventional Origin–Destination observations because they summarize rather than enumerate individual interactions. | Barbosa et al. (2018); aggregate mobility literature | Aggregation changes the form of observation by compressing individual interactions into population-level summaries. | **Bridge to Module E.** Introduces the idea that different observation types preserve different information. |
| **D6** | The transition to aggregate mobility observations changes the observational foundation upon which conventional parameter estimation was originally developed. | Built upon Modules C and D. | Conventional estimation methods assume detailed OD observations, whereas modern mobility datasets increasingly provide aggregate summaries. | **Primary conclusion of Module D.** Motivates the need to reconsider parameter estimation under modern observation regimes. |


module E

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **E1**   | Human mobility can be observed through multiple observational representations with different levels of detail.                                                                                                                | Barbosa et al. (2018); González et al. (2008); Song et al. (2010)   | Mobility has been represented as trajectories, Origin–Destination matrices, travel-distance distributions, accessibility measures and other aggregate summaries.                                                                                            | None (Established knowledge).                                                                  |
| **E2**   | Different observation representations preserve different information about spatial interaction.                                                                                                                               | Barbosa et al. (2018); mobility observation literature              | Each observational representation retains different spatial, temporal and relational information.                                                                                                                                                           | None (Established synthesis).                                                                  |
| **E3**   | Information aggregation transforms detailed mobility observations into more compact observational representations while preserving only part of the original information.                                                     | Statistical aggregation literature; mobility observation literature | Aggregation includes transformations such as trajectories → OD matrices, OD matrices → travel-distance distributions, and travel-distance distributions → aggregate summary statistics. It is therefore broader than spatial or temporal aggregation alone. | **Introduces the Handbook concept of Information Aggregation.**                                |
| **E4**   | Information aggregation is not limited to spatial or temporal aggregation but encompasses any transformation that changes the informational content of mobility observations.                                                 | Statistical aggregation literature                                  | Aggregate observations may result from spatial aggregation, temporal aggregation, distributional summarization, statistical summarization or combinations thereof.                                                                                          | **Clarifies the scope of aggregation used throughout the Handbook.**                           |
| **E5**   | Information aggregation progressively changes the information preserved by mobility observations.                                                                                                                             | Built upon E2–E4                                                    | As observations become increasingly aggregated, some information is preserved while other information is discarded or compressed.                                                                                                                           | **Introduces Information Compression and Information Preservation as complementary concepts.** |
| **E6**   | Mobility observations can be organized according to the information they preserve rather than according to the technologies used to collect them.                                                                             | Barbosa et al. (2018)                                               | Existing reviews commonly organize mobility data by sensing technologies (GPS, CDR, smart cards, surveys), whereas preserved information provides a technology-independent organizational principle.                                                        | **Primary conceptual contribution of the Handbook.**                                           |
| **E7**   | Information preservation provides a common framework for comparing heterogeneous mobility observations and naturally motivates the question of whether the preserved information remains sufficient for parameter estimation. | Built upon Modules C–E                                              | Once observations are organized by preserved information rather than by sensing technology, the next scientific question becomes whether the remaining information supports estimation of explicitly parameterized distance-response models.                | **Bridge to Module F.**                                                                        |

module F

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **F1** | Conventional parameter estimation methods assume detailed Origin–Destination observations. | Wilson (1971); Haynes & Fotheringham (1984); Ortúzar & Willumsen; Flowerdew & Aitkin (1982) | Classical estimation procedures are developed using detailed OD interactions. | None (Established paradigm). |
| **F2** | Modern mobility observations increasingly consist of aggregate summaries rather than complete Origin–Destination observations. | Barbosa et al. (2018); Meta; Google; Apple; aggregate mobility literature | Contemporary mobility products increasingly publish aggregate statistics instead of detailed OD data. | None (Established trend). |
| **F3** | Existing research has primarily focused on improving estimation or prediction under available observations rather than investigating estimation directly from aggregate observations. | Lenormand et al. (2016); Deep Gravity (2021); Imagery2Flow (2025) | Most existing methods assume access to detailed mobility observations for calibration or supervision. | **Handbook synthesis.** Identifies the shared methodological assumption across classical and modern approaches. |
| **F4** | Aggregate mobility observations preserve different information from detailed Origin–Destination observations. | Built upon Module E. | Different observation forms preserve different subsets of information. | Logical consequence of Module E. |
| **F5** | It remains unknown whether the information preserved after aggregation is sufficient for estimating the parameters of explicit distance-response models. | No direct reference (Research Gap). | Existing literature does not directly address this question. | **Central research question of the Handbook and Paper 1.** |
| **F6** | Explicitly parameterized distance-response models provide the most appropriate starting point for investigating this question because their model parameters are directly observable through statistical estimation. | Built upon Modules B–C. | These models expose explicit parameters that can, in principle, be estimated if sufficient observational information remains. | **Methodological justification for Paper 1.** |
| **F7** | Aggregate travel-distance distributions provide a natural first test case because they directly summarize observed responses to spatial separation. | Built upon Modules B and E. | Travel-distance distributions retain direct information about how interaction frequencies vary with spatial separation while discarding OD-specific information. | **Bridge to Module G.** |

module G

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **G1** | Explicit distance-response models provide parameterized representations that can be linked directly to aggregate mobility observations. | Built upon Modules B–F. | The explicit parameterization established in previous modules provides the basis for connecting model parameters with aggregate observations. | Foundation inherited from Modules B–F. |
| **G2** | Aggregate travel-distance distributions preserve observable information about responses to spatial separation. | Built upon Modules B and E. | Travel-distance distributions summarize how observed interaction frequencies vary with distance while abstracting away individual OD pairs. | **Observation model adopted in this Handbook.** |
| **G3** | The proposed framework estimates model parameters directly from aggregate travel-distance observations without reconstructing complete Origin–Destination matrices. | This Paper. | The estimation framework operates directly on aggregate observations rather than reconstructed OD flows. | **Primary methodological contribution of Paper 1.** |
| **G4** | Parameter estimation can be formulated directly as a statistical inference problem on aggregate observations. | Built upon Module H; This Paper. | The framework defines an observation model and estimates parameters by maximizing the likelihood of aggregate observations. | **Methodological contribution.** |
| **G5** | The proposed framework provides an empirical approach for recovering distance-response parameters from aggregate observations. | This Paper. | Recovery accuracy is evaluated empirically rather than assumed theoretically. | **Primary contribution of Paper 1.** |
| **G6** | Gravity serves as the initial demonstration of a broader parameter-estimation framework applicable to explicitly parameterized distance-response models. | Conceptual synthesis. | Gravity is selected because it provides an explicit parameterization suitable for the first empirical investigation. | **Research vision.** Extension beyond Gravity remains future work. |


module H

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **H1** | Parameter estimation can be formulated as a statistical inference problem once an observation model is specified. | Casella & Berger (2002); Bishop (2006); Murphy (2012) | Classical statistical inference estimates unknown parameters from observed data through probabilistic observation models. | None (Established statistical methodology). |
| **H2** | Aggregate travel-distance observations can be modeled probabilistically. | Aggregate mobility literature; This Paper | Aggregate travel-distance distributions are treated as realizations generated by an underlying probabilistic model. | Application of established statistical principles to aggregate mobility observations. |
| **H3** | The likelihood function can be constructed directly from aggregate observations without reconstructing complete Origin–Destination matrices. | This Paper; Classical likelihood theory | The proposed observation model defines likelihood directly on aggregate travel-distance observations. | **Primary methodological contribution of Paper 1.** |
| **H4** | Parameter estimation depends on the consistency between the observation model and the underlying distance-response model. | Casella & Berger (2002); Murphy (2012) | Statistical inference requires the observation model to correctly relate observed data to model parameters. | **Handbook synthesis.** Clarifies the assumptions underlying aggregate parameter estimation. |
| **H5** | Successful parameter recovery provides empirical evidence supporting the proposed estimation framework under its stated assumptions. | This Paper | Consistent recovery across experiments supports the practical validity of the framework. | **Empirical interpretation.** Not a theoretical proof. |
| **H6** | Formal questions concerning identifiability, sufficient statistics, and information preservation remain open theoretical problems. | Casella & Berger (2002); Cover & Thomas (1991) | These topics belong to statistical theory and information theory and are beyond the scope of Paper 1. | **Defines the theoretical boundary of the Handbook and motivates future research.** |

Module I

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **I1** | Synthetic experiments provide controlled conditions for evaluating parameter estimation accuracy. | Statistical simulation literature | Synthetic experiments provide known ground-truth parameters against which estimation accuracy can be objectively evaluated. | Standard validation methodology. |
| **I2** | The proposed framework accurately estimates distance-response parameters from aggregate observations under controlled conditions. | Results of this paper | Synthetic experiments demonstrate accurate recovery of the underlying model parameters. | **Primary empirical contribution of Paper 1.** |
| **I3** | The proposed framework generalizes across multiple real-world urban systems. | Results of this paper | Experiments across multiple cities demonstrate that the framework is not restricted to a single urban environment. | **Empirical contribution.** |
| **I4** | Parameter estimation remains robust under diverse urban structures and mobility patterns. | Results of this paper | Recovery performance remains stable across heterogeneous cities and travel patterns. | **Empirical evidence.** |
| **I5** | Aggregate travel-distance observations provide sufficient empirical evidence for accurate parameter estimation under the proposed framework. | Results of this paper | Consistent estimation accuracy demonstrates that aggregate observations contain practically useful information for estimating the model parameters under the assumptions of the framework. | **Empirical support for the proposed framework.** |
| **I6** | The empirical findings demonstrate the practical feasibility of aggregate parameter estimation while leaving broader theoretical questions open. | Discussion of this paper | Experimental success establishes empirical feasibility but does not constitute a theoretical proof of identifiability or information sufficiency. | **Defines the scientific scope of Paper 1.** |



module J

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **J1** | Paper 1 establishes empirical feasibility rather than complete theoretical understanding. | Results of Paper 1 | Experimental validation demonstrates that parameter estimation from aggregate observations is practically achievable under the proposed framework. | Defines the scientific scope of Paper 1. |
| **J2** | Formal characterization of information preservation, identifiability, and statistical sufficiency remains an open research problem. | Casella & Berger (2002); Cover & Thomas (1991) | These questions belong to statistical inference and information theory and are not resolved by the present empirical study. | Defines the principal theoretical agenda for future work. |
| **J3** | The proposed framework may be extended to other explicitly parameterized distance-response models beyond Gravity. | Gravity; Huff; Accessibility; related spatial interaction models | The methodology is developed using Gravity as the initial demonstration but is not conceptually restricted to Gravity alone. | Future methodological direction. |
| **J4** | Alternative observation types may provide complementary information for parameter estimation. | Mobility observation literature | Trajectories, OD matrices, travel-distance distributions and other aggregate summaries preserve different information. | Future observation framework. |
| **J5** | Future work may investigate transferable parameter estimation across cities, temporal monitoring, and broader observation models. | Mobility comparison literature | These directions naturally follow once aggregate parameter estimation becomes feasible. | Future application agenda. |
| **J6** | Aggregate parameter estimation provides a foundation for a broader scientific programme connecting mobility modelling, statistical inference, and information preservation. | Synthesized from Modules A–I | The present work establishes an empirical starting point while leaving broader theoretical development to future research. | **Long-term research vision of the Handbook.** |



References
---

# I. Spatial Interaction Foundations

| Ref ID | Reference                                                       | Year | Hỗ trợ Module | Vai trò                                |
| ------ | --------------------------------------------------------------- | ---- | ------------- | -------------------------------------- |
| R1     | Zipf, G.K. *The P1 P2 / D Hypothesis*                           | 1946 | A             | Gravity đầu tiên                       |
| R2     | Wilson, A.G. *A Family of Spatial Interaction Models*           | 1971 | A, B, C       | Entropy derivation, Gravity foundation |
| R3     | Tobler, W. *First Law of Geography*                             | 1970 | B             | Distance decay principle               |
| R4     | Haynes & Fotheringham. *Gravity and Spatial Interaction Models* | 1984 | A, B, C       | Textbook kinh điển                     |
| R5     | Fotheringham & O'Kelly. *Spatial Interaction Models*            | 1989 | A, B          | Spatial interaction theory             |
| R6     | Hansen, W. *Accessibility in Urban Transportation Planning*     | 1959 | B             | Accessibility & distance decay         |

---

# II. Human Mobility Foundations

| Ref ID | Reference                                                               | Year | Module | Vai trò                            |
| ------ | ----------------------------------------------------------------------- | ---- | ------ | ---------------------------------- |
| R7     | Barbosa et al. *Human Mobility: Models and Applications*                | 2018 | A–F    | Review lớn nhất về Human Mobility  |
| R9     | González et al. *Understanding Individual Human Mobility Patterns*      | 2008 | D, E   | Individual mobility (CDR)          |
| R10    | Song et al. *Limits of Predictability in Human Mobility*                | 2010 | D      | Human mobility predictability      |

---

# III. Distance-decay & Alternative Models

| Ref ID | Reference                                                             | Year    | Module | Vai trò                           |
| ------ | --------------------------------------------------------------------- | ------- | ------ | --------------------------------- |
| R11    | Simini et al. *A Universal Model for Mobility and Migration Patterns* | 2012    | B      | Radiation Model                   |
| R12    | Stouffer. *Intervening Opportunities*                                 | 1940    | B      | Alternative behavioural mechanism |
| R13    | Huff. *Defining and Estimating a Trading Area*                        | 1963    | B      | Huff Model                        |
| R14    | Ortúzar & Willumsen. *Modelling Transport*                            | Various | C      | Behaviour calibration             |
| R28    | Balcan et al. *Multiscale Mobility Networks and Infectious Diseases*  | 2009    | B      | Epidemic spatial model with distance-decay |
| R29    | Lenormand et al. *Systematic Comparison of Trip Distribution Laws*    | 2016    | C, F   | Systematic comparison of gravity calibration methods |

---

# IV. Statistical Inference

| Ref ID | Reference                                               | Year | Module | Vai trò                   |
| ------ | ------------------------------------------------------- | ---- | ------ | ------------------------- |
| R15    | Ben-Akiva & Lerman. *Discrete Choice Analysis*          | 1985 | C, H   | MLE (discrete choice)             |
| R16    | Bishop. *Pattern Recognition and Machine Learning*      | 2006 | H      | Statistical inference             |
| R17    | Murphy. *Machine Learning: A Probabilistic Perspective* | 2012 | H      | Bayesian & likelihood             |
| R18    | Casella & Berger. *Statistical Inference*               | 2002 | E, H   | Classical inference; sufficiency  |
| R19    | Cover & Thomas. *Elements of Information Theory*        | 1991 | H, J   | Future Information Theory         |
| R30    | Flowerdew & Aitkin. *A Method of Fitting the Gravity Model Based on the Poisson Distribution* | 1982 | C | Primary reference for Poisson MLE gravity calibration |

---

# V. Aggregate Mobility Revolution

| Ref ID | Reference                          | Year    | Module | Vai trò                  |
| ------ | ---------------------------------- | ------- | ------ | ------------------------ |
| R20    | Meta Data for Good                 | ongoing | D      | Aggregate mobility       |
| R21    | Google Community Mobility Reports  | 2020    | D      | Aggregate mobility       |
| R22    | Apple Mobility Trends              | 2020    | D      | Aggregate mobility       |
| R23    | WorldPop                           | ongoing | D      | Population datasets      |
| R24    | Nature Open Mobility Dataset paper | 2024    | D      | Open aggregate datasets  |

---

# VI. Deep Learning Mobility

| Ref ID | Reference    | Year | Module  | Vai trò                     |
| ------ | ------------ | ---- | ------- | --------------------------- |
| R25    | Deep Gravity | 2021 | C, F   | OD prediction requiring mobility supervision |
| R26    | Imagery2Flow | 2025 | A, F   | AI mobility reconstruction; OD supervision   |
| R27    | neuroGravity | 2026 | A, B   | Physics-informed DL; preserves gravity decomposition |
| R31    | TransGM      | 2026 | A, B   | Physics-informed DL; transferable gravity model      |

---

# VII. Behaviour Identification (Paper 1)

Đây là nhóm reference **của chính bài báo**.

| Ref ID | Reference  | Module | Vai trò                              |
| ------ | ---------- | ------ | ------------------------------------ |
| P1     | This Paper | G      | Behaviour Identification Framework   |
| P2     | This Paper | H      | Statistical Behaviour Identification |
| P3     | This Paper | I      | Empirical Validation                 |

---

# VIII. Future Papers

Các reference này **chưa dùng nhiều**, nhưng sẽ rất quan trọng.

| Ref ID | Chủ đề                 | Module |
| ------ | ---------------------- | ------ |
| F1     | Fisher Information     | J      |
| F2     | Sufficient Statistics  | J      |
| F3     | Information Bottleneck | J      |
| F4     | Identifiability Theory | J      |
| F5     | Information Geometry   | J      |

---

# Mapping sang Handbook

| Module | Main References         |
| ------ | ----------------------- |
| **A**  | R1–R7, R27, R31                           |
| **B**  | R2–R7, R11–R13, R27–R28, R31              |
| **C**  | R4, R14–R15, R18, R30, R25–R26, R29        |
| **D**  | R7, R9–R10, R20–R24                       |
| **E**  | R7, R9, R18, R20–R24                      |
| **F**  | R7, R25–R26, R29                           |
| **G**  | P1 + R2 + R27 + R31                       |
| **H**  | P2 + R15–R19, R30                         |
| **I**  | P3                                        |
| **J**  | R19 + F1–F5                               |

