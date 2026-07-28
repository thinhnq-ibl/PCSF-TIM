| Module                                                            | Scientific Question                                                                                                  | Mission                                                                                                                                                                                                            | Role in Paper 1                  | Future Development                                                                            |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- | --------------------------------------------------------------------------------------------- |
| **A. Gravity as the Scientific Foundation**                       | **Why is Gravity the natural scientific language for human mobility?**                                               | Establish Gravity as the canonical decomposition of mobility into **Urban Structure** and **Behaviour**.                                                                                                           | **Core**                         | Stable foundation                                                                             |
| **B. The Distance-decay Principle**                               | **Why does distance govern spatial interaction?**                                                                    | Establish distance decay as the universal behavioural law of spatial interaction rather than merely a Gravity component.                                                                                           | **Core**                         | Stable foundation                                                                             |
| **C. Conventional Behaviour Identification**                      | **How has behavioural distance decay traditionally been identified?**                                                | Review conventional calibration methods and show that they fundamentally require complete OD observations.                                                                                                         | **Core**                         | Stable foundation                                                                             |
| **D. The Aggregate Mobility Data Revolution**                     | **Why are aggregate mobility observations becoming the new standard?**                                               | Explain the transition from complete OD observations toward aggregate, scalable, privacy-preserving mobility data driven by cost, timeliness, and privacy regulations.                                             | **Core**                         | Stable foundation                                                                             |
| **E. Information Hierarchy, Compression and Information Loss**    | **How does aggregation transform mobility information?**                                                             | Organize mobility observations according to information preservation. Introduce Information Hierarchy, Information Compression, and Information Loss as the conceptual bridge between data and inference.          | **Core**                         | Later expanded into information-theoretic analysis                                            |
| **F. Research Gap**                                               | **Can behavioural parameters still be identified after information loss?**                                           | Formulate the central scientific challenge. Most calibration practice relies on observed OD flows, and the classical aggregate alternatives constrain only a single moment of the trip-length distribution. Ask whether the full aggregate distribution retains enough information for practical empirical identification.  | **Core**                         | Stable foundation                                                                             |
| **G. Empirical Behaviour Identification Framework**               | **Can behavioural distance-decay parameters be empirically recovered from aggregate travel-distance distributions?** | Present the proposed framework and its assumptions. Gravity serves as the first canonical demonstration rather than the ultimate objective.                                                                        | **Core contribution of Paper 1** | Later generalized beyond Gravity                                                              |
| **H. Statistical Foundation for Behaviour Identification**        | **Why is behavioural recovery statistically plausible?**                                                             | Develop the statistical inference framework: Observation Model → Likelihood → Identifiability → Estimator. Use empirical evidence rather than formal information-theoretic proof.                                  | **Core contribution of Paper 1** | Future work may extend to Fisher Information, Information Preservation, or Sufficiency Theory |
| **I. Empirical Evidence**                                         | **Does behavioural recovery actually work?**                                                                         | Validate the framework on synthetic and real-world cities, demonstrating robust empirical recovery of behavioural parameters.                                                                                      | **Core contribution of Paper 1** | Expanded with additional datasets and comparative studies                                     |
| **J. Research Program: Towards Behaviour Identification Science** | **What scientific questions emerge after this work?**                                                                | Position this paper as the first empirical demonstration of a broader research program on Behaviour Identification from aggregate observations.                                                                    | **Vision only**                  | Future papers progressively answer the open questions                                         |


Module A

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **A1** | Gravity is the canonical model of spatial interaction. | Zipf (1946); Wilson (1971); Haynes & Fotheringham (1984); Barbosa et al. (2018) | These works establish Gravity as the dominant and canonical framework for modelling aggregate spatial interaction across geography, transportation, migration, trade and human mobility. Zipf (1946) is an early sociological formalization rather than the historical origin of the gravity analogy. | None (Established knowledge). |
| **A2** | Gravity explicitly represents spatial interaction through origin, destination and distance components. | Wilson (1971); Fotheringham & O'Kelly (1989); Haynes & Fotheringham (1984) | The Gravity formulation explicitly consists of origin factors, destination factors and a distance-impedance function, providing a transparent decomposition of spatial interaction. | None (Established knowledge). |
| **A3** | Within the Gravity family of models, the distance-decay function provides an explicit representation of the collective response to spatial separation. | Wilson (1971); Haynes & Fotheringham (1984); Barbosa et al. (2018) | Classical Gravity models represent spatial impedance through an explicit distance-decay function describing how aggregate interaction changes with increasing spatial separation. | **Handbook interpretation:** the collective response to spatial separation provides the behavioural perspective adopted throughout this Handbook. |
| **A4** | Recent gravity-informed and physics-informed mobility models continue to preserve explicit Gravity-inspired origin, destination and distance components. | Yang et al. (2026, neuroGravity); Enaya et al. (2026, TransGM); Zhu & Ma (2026) | These models retain explicit Gravity-inspired structural components rather than replacing them entirely with black-box neural representations. | None (Evidence that the explicit Gravity formulation remains scientifically relevant). |
| **A5** | Gravity provides one of the clearest explicit formulations for separately analysing origin, destination and distance effects in aggregate spatial interaction. | Wilson (1971); Haynes & Fotheringham (1984); Fotheringham & O'Kelly (1989) | Because each component appears explicitly in the model formulation, their respective effects can be analysed separately. | None (Established interpretation of the explicit Gravity formulation). |
| **A6** | This Handbook adopts Gravity as its initial modelling framework because its explicit formulation enables the separate analysis of origin, destination, and distance effects on aggregate spatial interaction. | Supported by Claims A1–A5. | The explicit formulation of Gravity provides a transparent modelling framework suitable for subsequent methodological development throughout the Handbook. | **Methodological choice of this Handbook.** Gravity is adopted as the starting framework because of its explicit representation rather than because it is assumed to be universally superior to alternative mobility models. |

module B

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **B1** | Spatial interaction generally decreases with increasing spatial separation. | Tobler (1970); Haynes & Fotheringham (1984); Barbosa et al. (2018) | Classical geography and spatial interaction research consistently observe declining interaction with increasing separation due to spatial impedance. | None (Established knowledge). |
| **B2** | Within the Gravity family of models, responses to spatial separation are explicitly represented through parameterized distance-decay functions. | Wilson (1971); Haynes & Fotheringham (1984); Fotheringham & O'Kelly (1989) | Gravity models explicitly formulate spatial impedance through distance-decay functions whose parameters control the response to increasing separation. | None (Established knowledge). |
| **B3** | Distance-decay functions provide an explicit parameterization of aggregate responses to spatial separation. | Wilson (1971); Barbosa et al. (2018) | The distance-decay function specifies how aggregate interaction varies as spatial separation increases. | **Handbook interpretation:** this explicit parameterization provides the modelling basis adopted throughout the Handbook. |
| **B4** | Explicit distance-decay functions appear across a wide range of spatial interaction and accessibility models. | Huff (1963); Hansen (1959); Balcan et al. (2009); Martínez & Viegas (2013) | Retail trade-area models, accessibility measures and epidemiological commuting models all incorporate an explicit distance-impedance term. The complementary observation that some models omit it is established separately in B5. | None (Established synthesis). |
| **B5** | Alternative modelling paradigms demonstrate that aggregate spatial interaction can also be represented without explicit parametric distance-decay functions. | Stouffer (1940); Simini et al. (2012) | Intervening Opportunities and Radiation models explain spatial interaction without introducing an explicit parameterized distance-decay function. | Defines the scope of applicability of the Handbook. |
| **B6** | Models with explicit distance-decay formulations represent responses to spatial separation through explicit model parameters, enabling those parameters to be empirically estimated from observations. | Wilson (1971); Flowerdew & Aitkin (1982); Sen & Smith (1995) | Explicit parameterization makes the distance-response component directly estimable from observations without requiring reconstruction of individual behavioural processes. | **Methodological motivation for the Handbook.** Explains why the Handbook focuses on this class of models. |
| **B7** | The explicit parameterization of distance-response functions provides the methodological foundation for subsequent parameter estimation. | Supported by Claims B2–B6. | Once the response to spatial separation is explicitly parameterized, the remaining scientific problem becomes estimating those parameters from observations. | **Bridge to Module C.** |

module C

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **C1** | Parameters of explicit distance-decay functions have traditionally been estimated using observed Origin–Destination flows. | Wilson (1971); Haynes & Fotheringham (1984); Ortúzar & Willumsen (2011) | Classical Gravity calibration estimates the parameters governing the distance-decay function from observed OD interactions. | None (Established knowledge). |
| **C2** | Multiple estimation methods have been developed for calibrating distance-decay parameters. | Wilson (1971); Flowerdew & Aitkin (1982); Haynes & Fotheringham (1984); Lenormand et al. (2016) | Entropy-based calibration, least squares, Poisson likelihood and related methods all estimate the parameters of explicit distance-decay functions. | None (Established knowledge). |
| **C3** | Maximum Likelihood Estimation provides a statistically principled framework for parameter estimation. | Flowerdew & Aitkin (1982); Ben-Akiva & Lerman (1985) | Flowerdew & Aitkin formulate Gravity calibration as Poisson MLE on observed OD counts. Ben-Akiva & Lerman establish MLE for *disaggregate* choice models and is cited as general statistical precedent, not as an aggregate spatial-interaction estimator. | None (Established statistical methodology). |
| **C4** | Although estimation algorithms differ, they target the same underlying distance-decay parameters. | Wilson (1971); Flowerdew & Aitkin (1982); Lenormand et al. (2016) | Different optimisation procedures estimate the same parametric distance-response function. | **Handbook synthesis:** unifies classical calibration methods under a common parameter-estimation perspective. |
| **C5** | The most widely used estimation methods assume access to observed Origin–Destination flows for the study area. | Wilson (1971); Haynes & Fotheringham (1984); Ortúzar & Willumsen (2011); Flowerdew & Aitkin (1982) | Entropy, least-squares and Poisson-likelihood calibration are all defined on an observed OD matrix. | None (Established knowledge). |
| **C6** | A classical minority tradition already calibrates deterrence functions from aggregate trip-length information rather than from the full OD matrix. | Tanner (1961); Hyman (1969); Merlin (2020) | Tanner and Hyman calibrate the deterrence parameter by matching the *mean* observed trip length; Merlin (2020) uses the median. These procedures still require observed trips from the target city and constrain only one moment of the distribution. | **Important scope correction.** Aggregate calibration is not itself new; what remains open is calibration from the *full* distributional shape with no observed trips from the target city. |
| **C7** | Dependence on observed Origin–Destination flows limits the applicability of conventional parameter estimation when only published aggregate products are available. | Barbosa et al. (2018); Buckee et al. (2020); Oliver et al. (2020) | Aggregate mobility products generally do not release the OD interactions required by conventional estimation procedures. | **Motivates Module D.** |
| **C8** | Existing research has largely focused on improving estimation and prediction accuracy under available mobility supervision rather than on whether published aggregate observations alone suffice for parameter estimation. | Lenormand et al. (2016); Simini et al. (2021, Deep Gravity); Atwal et al. (2025); Xu et al. (2025, Imagery2Flow); Shi et al. (2020, MPGCN) | Most studies assume observed mobility flows are available for calibration or supervision, even when input features are derived from open data or deep graph networks. Yang et al. (2014) is the closest partial exception, studying commuting prediction without local calibration data, but does not estimate decay parameters from published aggregate distributions. | **Bridge to Modules D–F.** |


module D

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **D1** | Human mobility observation has shifted from survey-based measurements to continuously collected digital traces. | Barbosa et al. (2018); González et al. (2008); Song et al. (2010) | Advances in mobile sensing have fundamentally changed how population mobility is observed. | None (Established knowledge). |
| **D2** | Aggregate mobility products have become increasingly available through public and commercial platforms. | Meta Movement Distribution Maps (2026); Buckee et al. (2020) | Modern mobility products increasingly publish aggregated statistics instead of individual trajectories or complete OD matrices. | None (Established knowledge). |
| **D3** | Privacy, scalability and operational considerations increasingly favour the release of aggregate mobility observations. | de Montjoye et al. (2013); Oliver et al. (2020); Houssiau et al. (2022) | Individual trajectories are re-identifiable even when pseudonymised, which pushes data providers towards aggregated releases; aggregation is also operationally cheaper to publish at scale. | None (Established knowledge). |
| **D4** | Modern mobility observations increasingly consist of aggregate summaries rather than complete Origin–Destination observations. | Meta Movement Distribution Maps (2026); Barbosa et al. (2018); Buckee et al. (2020) | Many contemporary mobility datasets report aggregate indicators, including trip-length distributions, instead of complete OD matrices. | None (Established knowledge). |
| **D5** | Aggregate observations fundamentally differ from conventional Origin–Destination observations because they summarize rather than enumerate individual interactions. | Barbosa et al. (2018); Gallotti et al. (2024) | Aggregation changes the form of observation by compressing individual interactions into population-level summaries, and the choice of summary demonstrably changes what can be inferred. | **Bridge to Module E.** Introduces the idea that different observation types preserve different information. |
| **D6** | The transition to aggregate mobility observations changes the observational foundation upon which conventional parameter estimation was originally developed. | Built upon Modules C and D. | Conventional estimation methods assume detailed OD observations, whereas modern mobility datasets increasingly provide aggregate summaries. | **Primary conclusion of Module D.** Motivates the need to reconsider parameter estimation under modern observation regimes. |


module E

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **E1**   | Human mobility can be observed through multiple observational representations with different levels of detail.                                                                                                                | Barbosa et al. (2018); González et al. (2008); Song et al. (2010)   | Mobility has been represented as trajectories, Origin–Destination matrices, travel-distance distributions, accessibility measures and other aggregate summaries.                                                                                            | None (Established knowledge).                                                                  |
| **E2**   | Different observation representations preserve different information about spatial interaction.                                                                                                                               | Barbosa et al. (2018); Song et al. (2010); Gallotti et al. (2024)              | Each observational representation retains different spatial, temporal and relational information, and Gallotti et al. show that the representation chosen materially changes the conclusions drawn.                                                                                                                                                           | None (Established synthesis).                                                                  |
| **E3**   | Information aggregation transforms detailed mobility observations into more compact observational representations while preserving only part of the original information.                                                     | Casella & Berger (2002); Barbosa et al. (2018) | Aggregation includes transformations such as trajectories → OD matrices, OD matrices → travel-distance distributions, and travel-distance distributions → aggregate summary statistics. In statistical terms each step is a many-to-one map of the sample space, which is broader than spatial or temporal aggregation alone. | **Introduces the Handbook concept of Information Aggregation.**                                |
| **E4**   | Information aggregation is not limited to spatial or temporal aggregation but encompasses any transformation that changes the informational content of mobility observations.                                                 | Casella & Berger (2002)                                  | Any statistic of the data defines such a transformation, so aggregate observations may result from spatial aggregation, temporal aggregation, distributional summarization, statistical summarization or combinations thereof.                                                                                                                                          | **Clarifies the scope of aggregation used throughout the Handbook.**                           |
| **E5**   | Information aggregation progressively changes the information preserved by mobility observations.                                                                                                                             | Built upon E2–E4                                                    | As observations become increasingly aggregated, some information is preserved while other information is discarded or compressed.                                                                                                                           | **Introduces Information Compression and Information Preservation as complementary concepts.** |
| **E6**   | Mobility observations can usefully be organized according to the information they preserve rather than according to the technologies used to collect them.                                                                             | Barbosa et al. (2018); Pappalardo et al. (2023); Gallotti et al. (2024)                                              | Existing reviews commonly organize mobility data by sensing technologies (GPS, CDR, smart cards, surveys), whereas preserved information provides a technology-independent organizational principle. Information-theoretic treatments of mobility exist (e.g. predictability entropy), but they characterize *mobility processes* rather than organize *observation types*.                                                                                                        | **Conceptual framing of the Handbook** (an organizing principle, not a claim of unprecedented novelty).                                           |
| **E7**   | Information preservation provides a common framework for comparing heterogeneous mobility observations and naturally motivates the question of whether the preserved information remains sufficient for parameter estimation. | Built upon Modules C–E                                              | Once observations are organized by preserved information rather than by sensing technology, the next scientific question becomes whether the remaining information supports estimation of explicitly parameterized distance-response models.                | **Bridge to Module F.**                                                                        |

module F

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **F1** | The most widely used parameter estimation methods assume access to observed Origin–Destination flows. | Wilson (1971); Haynes & Fotheringham (1984); Ortúzar & Willumsen (2011); Flowerdew & Aitkin (1982) | Classical estimation procedures are defined on observed OD interactions. | None (Established paradigm). |
| **F2** | Modern mobility observations increasingly consist of aggregate summaries rather than complete Origin–Destination observations. | Barbosa et al. (2018); Meta Movement Distribution Maps (2026); Buckee et al. (2020); Oliver et al. (2020) | Contemporary mobility products increasingly publish aggregate statistics instead of detailed OD data. | None (Established trend). |
| **F3** | Existing research has primarily focused on improving estimation or prediction under available mobility supervision rather than on estimation directly from published aggregate observations. | Lenormand et al. (2016); Simini et al. (2021, Deep Gravity); Atwal et al. (2025); Xu et al. (2025, Imagery2Flow); Shi et al. (2020, MPGCN) | Most existing methods assume access to observed mobility flows for calibration or supervision, even when using open geospatial data or GCN architectures as inputs. | **Handbook synthesis.** Identifies the shared methodological assumption across classical and modern approaches. |
| **F4** | Aggregate mobility observations preserve different information from detailed Origin–Destination observations. | Built upon Module E; Gallotti et al. (2024). | Different observation forms preserve different subsets of information. | Logical consequence of Module E. |
| **F5** | Existing aggregate calibration methods constrain only a single moment of the travel-distance distribution and still require observed trips from the target city. | Tanner (1961); Hyman (1969); Merlin (2020); Yang et al. (2014) | Mean- and median-matching calibration use one summary statistic of locally observed trips; Yang et al. (2014) study prediction without local calibration data but do not estimate decay parameters from published distributions. | **Precise statement of what is already solved.** Prevents over-claiming in F6. |
| **F6** | It remains unresolved whether the *full shape* of a published aggregate travel-distance distribution, combined with urban structure derived from open data alone, provides enough information for practical empirical recovery of the parameters of an explicit distance-response model without any observed trips from the target city. | No direct reference (Research Gap); positioned against F5. | The literature addresses either OD-based calibration or single-moment aggregate calibration; the stated combination is not directly treated. | **Central research question of the Handbook and Paper 1.** |
| **F7** | Explicitly parameterized distance-response models provide the most appropriate starting point for investigating this question because their model parameters are directly targetable by statistical estimation. | Built upon Modules B–C. | These models expose explicit parameters that can, in principle, be estimated when the retained observations remain informative enough for recovery. | **Methodological justification for Paper 1.** |
| **F8** | Aggregate travel-distance distributions provide a natural first test case because they directly summarize observed responses to spatial separation. | Built upon Modules B and E. | Travel-distance distributions retain direct information about how interaction frequencies vary with spatial separation while discarding OD-specific information. | **Bridge to Module G.** |

module G

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **G1** | Explicit distance-response models provide parameterized representations that can be linked directly to aggregate mobility observations. | Built upon Modules B–F. | The explicit parameterization established in previous modules provides the basis for connecting model parameters with aggregate observations. | Foundation inherited from Modules B–F. |
| **G2** | Aggregate travel-distance distributions preserve observable information about responses to spatial separation. | Built upon Modules B and E. | Travel-distance distributions summarize how observed interaction frequencies vary with distance while abstracting away individual OD pairs. | **Observation model adopted in this Handbook.** |
| **G3** | The proposed framework estimates model parameters from the full shape of an aggregate travel-distance distribution, using urban structure derived from open data, without any observed Origin–Destination flows from the target city. | This Paper; contrasted with Tanner (1961); Hyman (1969); Merlin (2020); supported by Liang et al. (2013); Vu et al. (2021). | Classical aggregate calibration matches one moment of locally observed trips; the proposed framework matches the entire distribution (supported by intra-urban exponential decay mechanics in Liang et al., 2013) and requires no observed trips from the target city using open geospatial structure (Vu et al., 2021). | **Primary methodological contribution of Paper 1.** The differentiator is (i) full distributional shape rather than a single moment and (ii) no local trip observations. |
| **G4** | Parameter estimation can be formulated directly as a statistical inference problem on aggregate observations. | Built upon Module H; This Paper. | The framework defines an observation model and estimates parameters by maximizing the likelihood of aggregate observations. | **Methodological contribution.** |
| **G5** | The proposed framework provides an empirical approach for recovering distance-response parameters from aggregate observations. | This Paper. | Recovery accuracy is evaluated empirically rather than assumed theoretically. | **Primary contribution of Paper 1.** |
| **G6** | Gravity serves as the initial demonstration of a broader parameter-estimation framework applicable to explicitly parameterized distance-response models. | Conceptual synthesis. | Gravity is selected because it provides an explicit parameterization suitable for the first empirical investigation. | **Research vision.** Extension beyond Gravity remains future work. |


module H

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **H1** | Parameter estimation can be formulated as a statistical inference problem once an observation model is specified. | Casella & Berger (2002); Bishop (2006); Murphy (2012) | Classical statistical inference estimates unknown parameters from observed data through probabilistic observation models. | None (Established statistical methodology). |
| **H2** | Aggregate travel-distance observations can be modeled as counts generated by an underlying probabilistic spatial-interaction model. | Flowerdew & Aitkin (1982); Casella & Berger (2002); This Paper | Poisson count modelling of spatial interaction extends naturally from OD cells to distance bins, which are sums of OD cells. | Application of established statistical principles to aggregate mobility observations. |
| **H3** | The likelihood function can be constructed directly from aggregate observations without reconstructing complete Origin–Destination matrices. | This Paper; Flowerdew & Aitkin (1982); classical likelihood theory | The proposed observation model defines likelihood directly on aggregate travel-distance observations. | **Primary methodological contribution of Paper 1.** |
| **H4** | Validity of the estimates depends on the consistency between the aggregation operator assumed in the observation model and the aggregation actually applied by the data provider. | Casella & Berger (2002); Murphy (2012); Gallotti et al. (2024) | Statistical inference requires the observation model to correctly relate observed data to model parameters; misspecified binning, spatial masking or trip-definition rules bias the estimate. | **Handbook synthesis.** States the key falsifiable assumption underlying aggregate parameter estimation. |
| **H5** | Successful parameter recovery provides empirical evidence supporting the proposed estimation framework under its stated assumptions. | This Paper | Consistent recovery across experiments supports the practical validity of the framework and shows strong agreement with OD-based calibration in the evaluated cities. | **Empirical interpretation.** Not a theoretical proof. |
| **H6** | Formal questions concerning identifiability, sufficient statistics, and information preservation remain open theoretical problems. | Casella & Berger (2002); Cover & Thomas (1991) | These topics belong to statistical theory and information theory and are beyond the scope of Paper 1. | **Defines the theoretical boundary of the Handbook and motivates future research.** |

Module I

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **I1** | Synthetic experiments provide controlled conditions for evaluating parameter estimation accuracy. | Casella & Berger (2002); standard simulation-based validation practice | Synthetic experiments provide known ground-truth parameters against which estimation accuracy can be objectively evaluated. | Standard validation methodology. |
| **I2** | The proposed framework accurately estimates distance-response parameters from aggregate observations under controlled conditions. | Results of this paper | Synthetic experiments demonstrate accurate recovery of the underlying model parameters. | **Primary empirical contribution of Paper 1.** |
| **I3** | The proposed framework generalizes across multiple real-world urban systems. | Results of this paper | Experiments across multiple cities demonstrate that the framework is not restricted to a single urban environment. | **Empirical contribution.** |
| **I4** | Parameter estimation remains robust under diverse urban structures and mobility patterns. | Results of this paper | Recovery performance remains stable across heterogeneous cities and travel patterns. | **Empirical evidence.** |
| **I5** | Aggregate travel-distance observations are empirically informative enough to support practical recovery of the model parameters under the proposed framework. | Results of this paper | Consistent estimation accuracy demonstrates that aggregate observations contain practically useful information for recovering the model parameters under the assumptions of the framework, yielding strong agreement with OD-based calibration across the evaluated metropolitan areas. The term *sufficient* is deliberately avoided, since statistical sufficiency is not established (see H6). | **Empirical support for the proposed framework.** |
| **I6** | The empirical findings demonstrate the practical feasibility of aggregate parameter recovery while leaving broader theoretical questions open. | Discussion of this paper | Experimental success establishes practical empirical recoverability but does not constitute a theoretical proof of identifiability or information sufficiency. | **Defines the scientific scope of Paper 1.** |



module J

| Claim ID | Scientific Claim | Representative References | How the References Support the Claim | Handbook Contribution |
| -------- | ---------------- | ------------------------- | ------------------------------------ | --------------------- |
| **J1** | Paper 1 establishes empirical recoverability rather than complete theoretical understanding. | Results of Paper 1 | Experimental validation demonstrates that parameter recovery from aggregate observations is practically achievable under the proposed framework. | Defines the scientific scope of Paper 1. |
| **J2** | Formal characterization of information preservation, identifiability, and statistical sufficiency remains an open research problem. | Casella & Berger (2002); Cover & Thomas (1991) | These questions belong to statistical inference and information theory and are not resolved by the present empirical study. | Defines the principal theoretical agenda for future work. |
| **J3** | The proposed framework may be extended to other explicitly parameterized distance-response models beyond Gravity. | Huff (1963); Hansen (1959); Martínez & Viegas (2013) | The methodology is developed using Gravity as the initial demonstration but is not conceptually restricted to Gravity alone. | Future methodological direction. |
| **J4** | Alternative observation types may provide complementary information for parameter estimation. | Barbosa et al. (2018); Gallotti et al. (2024); Blondel et al. (2015) | Trajectories, OD matrices, travel-distance distributions and other aggregate summaries preserve different information. | Future observation framework. |
| **J5** | Future work may investigate transferable parameter estimation across cities, temporal monitoring, and integration with modern OD reconstruction models trained on open geospatial data or learned through cross-city transfer. | Enaya et al. (2026, TransGM); Yang et al. (2026, neuroGravity); Xu et al. (2025, Imagery2Flow); Wang et al. (2025, Similarity Transfer); Lenormand et al. (2016) | Transferable gravity models (neuroGravity, TransGM), similarity-based urban data transfer (Wang et al., 2025), and open-data OD predictors (Imagery2Flow, Deep Gravity) represent distinct but complementary directions; both naturally connect to the aggregate parameter estimation programme once it becomes feasible. | Future application agenda. |
| **J6** | Aggregate parameter estimation provides a foundation for a broader scientific programme connecting mobility modelling, statistical inference, and information preservation. | Synthesized from Modules A–I | The present work establishes an empirical starting point while leaving broader theoretical development to future research. | **Long-term research vision of the Handbook.** |
| **J7** | OD networks produced by modern mobility models—whether through cross-city transfer learning or open-data deep learning on satellite imagery—may serve as proxy knowledge for learning transferable urban structural characteristics in data-scarce contexts. | Yang et al. (2026, neuroGravity); Enaya et al. (2026, TransGM); Xu et al. (2025, Imagery2Flow) | Transferable models (neuroGravity, TransGM) and open-data OD predictors (Imagery2Flow) both produce reconstructed OD networks for cities; treated as informative representations rather than ground truth, their structural patterns may provide transferable knowledge where direct observations are unavailable. | **Future research vision — Knowledge Transfer direction.** |
| **J8** | Combining proxy structural knowledge with the Behaviour Identification framework may enable inference of plausible OD flows for cities lacking publicly available mobility observations. | Built upon Modules G–I; J7 | The Behaviour Identification framework (Paper 1) identifies distance-response parameters from aggregate observations; extending this with transferable structural knowledge addresses cities such as Ho Chi Minh City where neither OD data nor detailed mobility surveys are publicly available. | **Future research vision — extends Paper 1 from parameter identification toward knowledge-assisted mobility reconstruction.** |

---

### Future Research Direction: Knowledge Transfer for Mobility Reconstruction in Data-Scarce Cities

#### Positioning within the Landscape of OD Reconstruction

Recent advances in human mobility modelling have produced several complementary approaches to OD network reconstruction, each with distinct input requirements and outputs:

| Approach | Primary Input | Output | Requires OD supervision? |
| --- | --- | --- | --- |
| Deep Gravity (Simini et al., 2021) | Open urban features | OD flows | Yes |
| Imagery2Flow (Xu et al., 2025) | Satellite imagery | OD flows | Yes |
| neuroGravity (Yang et al., 2026) | Cross-city transfer learning | OD flows | Yes (source cities) |
| TransGM (Enaya et al., 2026) | Cross-city transfer learning | OD flows | Yes (source cities) |
| **This Handbook (Paper 1)** | **Aggregate travel-distance distribution + open urban structure** | **Behaviour parameters (θ)** | **No** |

This table highlights a fundamental distinction: existing approaches—whether using satellite imagery, open urban features, or cross-city transfer—target **OD flow prediction** directly and still require observed OD data for supervision or training. The Handbook addresses a different problem: **behaviour parameter identification** from published aggregate observations, without any observed OD flows from the target city.

#### Knowledge Transfer Vision

Many state-of-the-art transferable mobility models have reconstructed Origin–Destination (OD) networks for selected Vietnamese cities such as Hanoi and Da Nang, while large metropolitan areas including Ho Chi Minh City remain unavailable. Similarly, open-data OD predictors such as Imagery2Flow can generate OD networks for cities with available satellite imagery. Future research may investigate whether these reconstructed networks—from either source—can serve as **proxy knowledge** for learning transferable urban structural characteristics in the Vietnamese context.

Rather than treating the reconstructed OD networks as ground truth, they are regarded as informative representations produced by advanced mobility models. If structural patterns prove consistent across reconstructed cities, they may provide transferable knowledge for cities lacking publicly available mobility observations, while accounting for the inherent uncertainty in the reconstructed networks when transferring structural knowledge.

A key methodological challenge lies in distinguishing model-specific artefacts from genuinely transferable urban structural signals within the reconstructed networks—a challenge that applies equally to transfer-learned networks (neuroGravity, TransGM) and imagery-based networks (Imagery2Flow).

Combined with the Behaviour Identification framework developed in this Handbook, such transferable structural knowledge may enable the inference of plausible OD flows for previously unmodelled cities such as Ho Chi Minh City using only open urban data and aggregate mobility observations. This direction extends the Handbook from behavioural parameter identification toward knowledge-assisted mobility reconstruction for data-scarce urban environments, and represents a natural point of complementarity between the Handbook's aggregate parameter estimation programme and the broader landscape of modern OD reconstruction models.



References
---

# I. Spatial Interaction Foundations

| Ref ID | Reference                                                       | Year | BibTeX key | Hỗ trợ Module | Vai trò                                |
| ------ | --------------------------------------------------------------- | ---- | ---------- | ------------- | -------------------------------------- |
| R1     | Zipf, G.K. *The $P_1P_2/D$ Hypothesis: On the Intercity Movement of Persons*, Am. Sociol. Rev. 11(6) | 1946 | `zipf1946` | A             | Early sociological formalization of the gravity analogy (not its historical origin) |
| R2     | Wilson, A.G. *A Family of Spatial Interaction Models, and Associated Developments*, Env. Plan. A | 1971 | `wilson1971` | A, B, C       | Entropy derivation, Gravity foundation |
| R3     | Tobler, W. *A Computer Movie Simulating Urban Growth in the Detroit Region*, Econ. Geogr. | 1970 | `tobler1970computer` | B             | Source of the "First Law of Geography"; distance-decay principle |
| R4     | Haynes & Fotheringham. *Gravity and Spatial Interaction Models*, Sage | 1984 | `haynes1984gravity` | A, B, C       | Textbook kinh điển                     |
| R5     | Fotheringham & O'Kelly. *Spatial Interaction Models: Formulations and Applications*, Kluwer | 1989 | `fotheringham1989spatial` | A, B          | Spatial interaction theory             |
| R6     | Hansen, W. *How Accessibility Shapes Land Use*, JAIP 25(2) | 1959 | `hansen1959accessibility` | B             | Accessibility & distance decay         |
| R8     | Sen & Smith. *Gravity Models of Spatial Interaction Behavior*, Springer | 1995 | `sen1995gravity` | B, C | Statistical theory of gravity model estimation |

---

# II. Human Mobility Foundations

| Ref ID | Reference                                                               | Year | BibTeX key | Module | Vai trò                            |
| ------ | ----------------------------------------------------------------------- | ---- | ---------- | ------ | ---------------------------------- |
| R7     | Barbosa et al. *Human Mobility: Models and Applications*                | 2018 | `barbosa2018human` | A–F    | Review lớn nhất về Human Mobility  |
| R9     | González et al. *Understanding Individual Human Mobility Patterns*      | 2008 | `gonzalez2008understanding` | D, E   | Individual mobility (CDR)          |
| R10    | Song et al. *Limits of Predictability in Human Mobility*                | 2010 | `song2010limits` | D, E   | Human mobility predictability; entropy of mobility |
| R32    | Pappalardo et al. *Future Directions in Human Mobility Science*         | 2023 | `pappalardo2023analytical` | E, D   | Agenda review; framing of mobility data |
| R33    | Gallotti et al. *Distorted Insights from Human Mobility Data*           | 2024 | `gallotti2024distorted` | D, E, F, H | Representation choice changes inference |
| R34    | Blondel et al. *A Survey of Results on Mobile Phone Datasets Analysis*  | 2015 | `blondel2015survey` | D, J   | Survey of CDR-based mobility observation |

---

# III. Distance-decay & Alternative Models

| Ref ID | Reference                                                             | Year    | BibTeX key | Module | Vai trò                           |
| ------ | --------------------------------------------------------------------- | ------- | ---------- | ------ | --------------------------------- |
| R11    | Simini et al. *A Universal Model for Mobility and Migration Patterns* | 2012    | `Simini2012universal` | B      | Radiation Model                   |
| R12    | Stouffer. *Intervening Opportunities: A Theory Relating Mobility and Distance* | 1940 | `stouffer1940intervening` | B      | Alternative behavioural mechanism |
| R13    | Huff. *A Probabilistic Analysis of Shopping Center Trade Areas*, Land Econ. 39(1) | 1963 | `huff1963probabilistic` | B, J   | Huff Model                        |
| R14    | Ortúzar & Willumsen. *Modelling Transport*, 4th ed.                   | 2011    | `ortuzar2011modelling` | C, F   | Behaviour calibration             |
| R28    | Balcan et al. *Multiscale Mobility Networks and Infectious Diseases*  | 2009    | `balcan2009multiscale` | B      | Epidemic spatial model with a fitted gravity law |
| R29    | Lenormand et al. *Systematic Comparison of Trip Distribution Laws and Models* | 2016 | `lenormand2016systematic` | C, F, J | Systematic comparison of trip distribution laws and calibration |
| R35    | Martínez & Viegas. *A New Approach to Modelling Distance-Decay Functions* | 2013 | `martinez2013distance` | B, J   | Distance-decay functional forms for accessibility |
| R48    | Liang et al. *Unraveling the Origin of Exponential Law in Intra-Urban Human Mobility* | 2013 | `liang2013unraveling` | B, G | Proves intra-urban trips decay exponentially due to urban population density decay |

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
| R15    | Ben-Akiva & Lerman. *Discrete Choice Analysis*          | 1985 | `benakiva1985discrete` | C, H   | MLE (disaggregate choice; cited as statistical precedent only) |
| R16    | Bishop. *Pattern Recognition and Machine Learning*      | 2006 | `bishop2006pattern` | H      | Statistical inference             |
| R17    | Murphy. *Machine Learning: A Probabilistic Perspective* | 2012 | `murphy2012machine` | H      | Bayesian & likelihood             |
| R18    | Casella & Berger. *Statistical Inference*, 2nd ed.      | 2002 | `casella2002statistical` | E, H, I, J | Classical inference; statistics as many-to-one maps; sufficiency |
| R19    | Cover & Thomas. *Elements of Information Theory*        | 1991 | `cover1991elements` | H, J   | Future Information Theory         |
| R30    | Flowerdew & Aitkin. *A Method of Fitting the Gravity Model Based on the Poisson Distribution* | 1982 | `flowerdew1982method` | B, C, F, H | Primary reference for Poisson MLE gravity calibration |

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
| R51    | Wang et al. *Urban Human Mobility: Data-Driven Modeling and Prediction* | 2019 | `wang2019urban` | D, E | Survey taxonomy classifying collective vs individual human mobility |

> **Đã loại bỏ:** Google Community Mobility Reports và Apple Mobility Trends (cả hai chỉ công bố % thay đổi số lượt ghé thăm / yêu cầu chỉ đường, không phải OD hay phân bố quãng đường, và đã ngừng phát hành từ 2022); "GDPR" (văn bản luật, không phải reference khoa học — thay bằng R42/R43); "Nature Open Mobility Dataset paper 2024" (không xác định được tác giả/venue).

---

# VI. Deep Learning Mobility

| Ref ID | Reference    | Year | BibTeX key | Module  | Vai trò                     |
| ------ | ------------ | ---- | ---------- | ------- | --------------------------- |
| R25    | Simini et al. *A Deep Gravity Model for Mobility Flows Generation* | 2021 | `simini2021` | C, F   | OD prediction requiring mobility supervision |
| R26    | Atwal et al. *Commuting Flow Prediction Using OpenStreetMap Data* | 2025 | `atwal2025commuting` | C, F   | Open-data flow prediction; still OD-supervised   |
| R27    | Yang et al. *Transferable Human Mobility Network Reconstruction with neuroGravity* | 2026 | `neurogravity2026` | A, J   | Physics-informed DL; preserves gravity decomposition |
| R31    | Enaya et al. *TransGM: Transferable Gravity Models for Cross-City Policy Transfer* | 2026 | `transgm2026` | A, J   | Transferable gravity model      |
| R44    | Zhu & Ma. *Gravity-Informed Deep Flow Inference* | 2026 | `zhu2026gravitypanel` | A | Gravity-informed neural inference |
| R45    | Xu et al. *Predicting Human Mobility Flows in Cities Using Deep Learning on Satellite Imagery* | 2025 | `xu2025imagery2flow` | C, F   | OD prediction from satellite imagery; still requires OD supervision — doi:10.1038/s41467-025-65373-z |
| R47    | Shi et al. *Predicting Origin-Destination Flow via Multi-Perspective Graph Convolutional Network* | 2020 | `shi2020mpgcn` | C, F | Dynamic GNN OD prediction requiring time-series OD supervision |
| R49    | Wang et al. *Similarity Based City Data Transfer Framework in Urban Digitization* | 2025 | `wang2025similarity` | J | Similarity-based cross-city transfer framework for data-poor urban environments |
| R50    | Vu et al. *Enhanced Urban Functional Land Use Map with Free and Open-Source Data*, Int. J. Digit. Earth 14(11):1744–1757 | 2021 | `vu2021landuse` | G | Deriving urban spatial structures and land use zones from open data (OSM, POI); Q1 journal (Taylor & Francis) |

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

Các reference này **chưa dùng nhiều**, nhưng sẽ rất quan trọng. ID dùng tiền tố `FW` để tránh trùng với claim ID F1–F8 của Module F.

| Ref ID | Chủ đề                 | Module |
| ------ | ---------------------- | ------ |
| FW1    | Fisher Information     | J      |
| FW2    | Sufficient Statistics  | J      |
| FW3    | Information Bottleneck | J      |
| FW4    | Identifiability Theory | J      |
| FW5    | Information Geometry   | J      |
| FW6    | Knowledge Transfer for OD Reconstruction in Data-Scarce Cities | J (J7–J8) |

---

# Mapping sang Handbook

Bảng này phải khớp chính xác với cột *Representative References* trong từng bảng claim.

| Module | Main References                                   |
| ------ | ------------------------------------------------- |
| **A**  | R1, R2, R4, R5, R7, R27, R31, R44                 |
| **B**  | R2–R6, R8, R11–R13, R28, R30, R35, R48            |
| **C**  | R2, R4, R7, R8, R14, R15, R25, R26, R29, R30, R36–R41, R45, R47 |
| **D**  | R7, R9, R10, R20, R23, R33, R40–R43, R51           |
| **E**  | R7, R9, R10, R18, R32, R33, R51                   |
| **F**  | R7, R14, R20, R25, R26, R29, R30, R33, R36–R41, R45, R47 |
| **G**  | P1 + R36–R38, R48, R50                           |
| **H**  | P2 + R16–R19, R30, R33                           |
| **I**  | P3 + R18                                          |
| **J**  | R13, R18, R19, R27, R29, R31, R34, R35, R45, R49 + FW1–FW6  |

---

# Kiểm tra tính nhất quán (checklist trước khi viết bài)

- [x] Mọi reference trong bảng claim đều có bibkey tồn tại trong `paper/references.bib`.
- [x] Không còn ô reference dạng "… literature" (placeholder không kiểm chứng được).
- [x] Gap (F6) được phát biểu sau khi đã thừa nhận công trình calibration aggregate cổ điển (C6, F5).
- [x] Không dùng từ "sufficient" theo nghĩa thống kê ở phần thực nghiệm (I5), vì sufficiency chưa được chứng minh (H6).
- [x] ID claim và ID reference không trùng namespace (Module F dùng F1–F8; future work dùng FW1–FW5).

