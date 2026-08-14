Case study: Ho Chi Minh City
Learning from Distance-Binned Mobility Distributions
Measurement Validity and Reconstructive Value for OD Reconstruction
help_outlineCentral Question
Under what conditions does a mobility distribution represented by a small number of coarse distance bins constitute a valid mobility-distance observation, and whether, and how much additional destination-resolved OD information does it provide beyond urban contextual information?
1
Presenter: Thinh Nguyen
1

Core Transportation Concept
Cities Need OD Matrices
What is an OD Matrix?
Tij
Represents the volume of trips moving from origin i to destination j.
Why It Matters
-Transport planning
-Accessibility analysis
-Infrastructure investment
-Scenario modelling
error_outline
The Challenge
Complete destination-resolved OD data are rarely observed in practice, presenting a significant barrier to effective urban analytics.
2
2

3
Case study: Ho Chi Minh City
Fragmented Evidence, Missing OD
Available Observations
-Meta Movement Distribution
-Traffic counts
-Bus boarding / alighting
-Urban structure
-Transport network
-OpenStreetMap / land-use proxies
error_outlinePractical Challenge
HCMC has mobility evidence, but not a complete destination-resolved OD matrix.
trending_upScientific Opportunity
HCMC provides a data-scarce setting to test whether compressed mobility observations can support defensible OD reconstruction.
Refs: Cascetta & Nguyen (1988); Barbosa et al. (2018); Meta AI for Good (n.d.); OpenStreetMap contributors (n.d.).
3

4
RESEARCH OBJECT
Distance-Binned Mobility Distributions
Describes how movement is distributed across distance ranges:
YD = [P(D ∈ b1), P(D ∈ b2), ..., P(D ∈ bK)]
What It Tells Us
-How far people tend to move
-How mobility is distributed across distance bands
-Whether short-, medium-, or long-distance movement dominates
What It Does Not Tell Us
cancelWhich origin connects to which destination
cancelDestination-specific allocation
cancelDirectional OD pairing
Empirical Testbed
Principal experimental platform:
mapMeta Movement Distribution Maps
Refs: Meta AI for Good (n.d.); Muller et al. (2025).
4

5
Observation Pipeline
Underlying mobility process: M
Step-by-step pipeline:
M
↓ selective sampling
S(M)
↓ distance binning
B(·)
↓ privacy / filtering
YD_obs
Key Characterization
YD_obs = YD_Meta
layersCompressed
securityPrivacy-preserved
visibility_offPartial mobility observation
warningImportant Distinction
Partial Observation =
Biased Observation
Selective sampling creates potential representativeness limitations, but bias must be assessed rather than assumed.
Refs: Meta AI for Good (n.d.); Muller et al. (2025); Gosselin et al. (2025); Gibbs et al. (2026).
CONCEPTUAL FRAMEWORK
Distance-Binned Observation Is Not Raw Mobility
5

6
Scientific Framework
From Distance Bins to OD Structure
Mathematical Model
Latent OD Matrix
T
Observed Compressed Signal
YD = AD(T)
where AD is a distance-binning operator.
Two-Stage Logic
STAGE 1 Is YD measurement-valid?
STAGE 2 Does valid YD reduce OD ambiguity?
Key Insight
lightbulb
Distance-bin fit ≠ 
OD recovery
Matching a compressed distance distribution constrains feasible OD structures, but does not uniquely determine destination-resolved OD pairing. 
Conceptual basis: Cascetta & Nguyen (1988); Lenormand et al. (2016).
6

7
Research Agenda
Two Gaps, Two Papers
Gap 1 — Paper 1
Measurement Validity of Distance-Binned Mobility Distributions
YD_Meta ↔ YD_Reference
Core Question
Can we trust the observed distance signal?
Gap 2 — Paper 2
Marginal Reconstructive Value of Distance-Binned Mobility Constraints
X_urban vs X_urban + YD
Core Question
If trustworthy, does it actually reduce OD ambiguity?
7

8
Gap Analysis
Gap 1: Measurement Validity
Refs: Meta AI for Good (n.d.); Muller et al. (2025); Gosselin et al. (2025); Gibbs et al. (2026).
Gap Statement
Under what observation conditions does the compressed YD preserve the intended distance signal?
Stress Factors
-Sampling
-Distance binning
-Spatial support
-Temporal support
-Privacy / filtering
Research Question 1
help_outline
Under what conditions does a distance-binned mobility distribution remain a valid quantitative representation of its intended mobility-distance property?
8

9
Paper 1
Measurement Validation Design
Controlled Components
FIXED INPUTS
O_i_GT, A_j
ATTRACTIVENESS PROXY
A_j = g(X_j)
Independently constructed destination-attractiveness proxy.
Validation Branches
REFERENCE BRANCH
(O_GT, A, YD_REF) → β̂REF
META BRANCH
(O_GT, A, YD_Meta) → β̂Meta
Validity is task-conditional
d(YD_Meta, YD_REF) ≤ ε_Y
|β̂Meta - β̂REF| ≤ ε_β
Methodology Purpose
track_changesESTIMATION CORE
Keep O, A, model specification, and estimation procedure fixed.
This ensures that all observed differences mainly reflect the distance-binned observation process.
Refs: Hyman (1969); Abdel-Aal (2014); Lenormand et al. (2016).
9

10
Paper 1
Validation Steps
Expected Output
assignment_turned_in
Measurement Validity Boundary
The final outcome of this validation process is to establish a clear boundary for measurement validity.
Steps 1 – 3
STEP 1
Convert reference OD / mobility data into comparable distance bins.
STEP 2
Match spatial and temporal support.
STEP 3
Construct fixed Oi_GT and Aj.
Steps 4 – 5
STEP 4: COMPARE BRANCHES
Evaluate discrepancy:
YD_Meta vs YD_Reference
β̂Meta vs β̂REF
STEP 5: SENSITIVITY TESTING
Test sensitivity to bin definition, spatial scale, temporal mismatch, and Aj specification.
Methodological basis: Hyman (1969); Lenormand et al. (2016).
10

Kill-Test Gap 1
What Has Already Been Solved?
Already Established & Critical Gaps
01 Gosselin: Meta Movement Distribution can capture temporal mobility changes.
↳ Kill-test: Meta validation is new
02 Muller: Seasonal and hazard-related mobility patterns have been studied.
↳ Kill-test: Meta seasonality is new
03 Abdel-Aal: Gravity parameters can be calibrated using trip-length or friction info.
↳ Kill-test: Additional-data value is new
04 Gibbs: Privacy–utility trade-offs in mobility data have been studied.
↳ Kill-test: Privacy–utility is new
05 Sakong & Zentefis: Estimation under privacy-distorted mobility data has been explored.
↳ Kill-test: Privacy mobility estimate gravity is new
The Remaining Gap
Can a coarse distance-binned observation be trusted as mobility evidence?
Remaining Question
help_outlineCORE INQUIRY
When is the combined observation process S+B+P measurement-valid?
Refs: Hyman (1969); Abdel-Aal (2014); Muller et al. (2025); Gosselin et al. (2025); Gibbs et al. (2026); Sakong & Zentefis (2023).

12
Gap 2
Marginal Reconstructive Value
Gap Statement
warning_amber
A measurement-valid distance-binned mobility distribution may still contain little destination-resolved information. It remains unclear how much such a constraint reduces OD ambiguity beyond urban contextual information alone, and when its marginal contribution is complementary, redundant, or insufficient.
Research Question 2
help_outline
How much additional destination-resolved OD information does a validated distance-binned mobility constraint provide beyond urban contextual information, and under which urban conditions is this incremental contribution reliable?
Core Idea
tips_and_updates
Measure Validity ≠ OD Reconstructive Value
Measurement validity is necessary but not sufficient for OD reconstructive value 
Refs: Cascetta & Nguyen (1988); Ait-Ali & Eliasson (2022); Zhang et al. (2025).
12

13
Paper 2
Incremental OD Value
settingsModel Setup
BASELINE
X_urban T̂
TREATMENT
X_urban + YD_validated T̂
compare_arrowsComparison
INCREMENTAL VALUE FORMULA
R = R(T|X_urban,YD) R(T|X_urban)
OD recovery R is evaluated across multiple dimensions:
flow magnitude, destination allocation, spatial topology, and network consequences.
R is evaluated on held-out benchmark cities with OD ground truth.
HCMC is external/indirect validation, not R ground-truth evaluation.
psychologyInterpretation
DECISION BOUNDARIES
R > meaningfully complementary|R| effectively redundant
là practical / uncertainty threshold
Interpret R relative to uncertainty and practical significance, not sign alone.
Related concept: Ait-Ali & Eliasson (2022).
13

14
Kill-Test Gap 2
What Has Already Been Solved?
Claims that should not be used as novelty
•Rong: Generate OD without target-city OD
•Rong, Wang: Generate OD from urban structure
•He et al., Rong, Feng & Ding: Cross-city OD prediction
•Liu et al.: Zero-shot OD generation
•Hyman: Gravity calibration from trip-distance information
•Cascetta & Nguyen: OD estimation from incomplete indirect observations
•OD estimation using aggregated mobility statistics
•Ait-Ali & Eliasson: Marginal value of additional data in some transport OD contexts
Thesis Boundary
Paper 2 is not about proving that OD can be generated from urban data.
Remaining Gap
help_outline
What destination-level OD information does YD add beyond urban context?
Refs: Cascetta & Nguyen (1988); Ait-Ali & Eliasson (2022); Rong et al. (2023); Zhang et al. (2025); Rong et al. (2025); Chen et al. (2026).
14

15
Gap 2 & Boundary
Zero-Target-OD Boundary
Already addressed in recent literature
GODDAG: OD generation for new cities
Transfer mobility learning across cities
LLM-based cross-city OD prediction
neuroGravity: zero-shot mobility-network reconstruction
UniMob: zero-shot / few-shot mobility generation
WorldMove: global mobility generation
GlODGen: satellite-derived global commuting OD generation
SEDAN: cross-city OD matrix generation with urban structure and semantics
The novelty is NOT:
“zero-shot OD generation exists.”
The novelty IS:
-_outline
measuring the marginal value of a validated distance-binned constraint
Refs: He et al. (2020); Rong et al. (2023); Yu et al. (2024); Rong et al. (2025); Yuan et al. (2025); Liu et al. (2026); Yang et al. (2026); Chen et al. (2026).
15

16
Analysis Framework
Where Does YD​ Add Unique Information? 
Secondary heterogeneity analysis
The value of YD may vary by:
density
centrality
land-use mix
polycentricity
accessibility
opportunity distribution
Core experiment
X_urban vs X_urban + YD
Research goal
track_changes
Identify when the distance-binned signal reduces OD ambiguity, and when urban context already explains most recoverable structure.
Refs: Rong et al. (2023); Chen et al. (2026).
16

17
HCMC Application
Applying the Framework to Ho Chi Minh City
settingsSetting
X_urban_HCMC + YD_Meta → T̂_HCMC
No complete HCMC OD matrix is assumed.
explorePrinciple
These observations test consistency, not uniqueness of the reconstructed OD.
alt_routeIndirect Validation
Road Network Flows
T̂ → assigned network flows → traffic counts / cameras
Transit Patterns
T̂transit → bus boarding / alighting patterns
assignment_turned_inExpected Output
An empirically constrained OD reconstruction strategy for HCMC under incomplete observation.
Refs: Cascetta & Nguyen (1988); Ait-Ali & Eliasson (2022).
17

18
Contributions
Expected Contributions
insightsContribution 1
Measurement Validity Domain
Determine when distance-binned mobility distributions preserve usable mobility-distance signal.
analyticsContribution 2
Marginal Reconstructive Value
Quantify whether validated distance constraints reduce OD ambiguity beyond urban contextual information.
mapContribution 3
HCMC Application
External Validation Framework under Missing Target-City OD Ground Truth 
Bottom-line contribution
Validate the observationeastMeasure its marginal reconstructive valueeastApply under incomplete target-city OD observation
18

Q & A
Questions & Answers

19
19

Thank You
for listening
20
20

Selected References
KMeasurement & Mobility References
Barbosa, H., Barthelemy, M., Ghoshal, G., et al. (2018).
Human mobility: Models and applications. Physics Reports, 734, 1–74.
Cascetta, E., & Nguyen, S. (1988).
A unified framework for estimating or updating origin/destination matrices from traffic counts. Transportation Research Part B, 22(6), 437–455.
Hyman, G. M. (1969).
The calibration of trip distribution models. Environment and Planning A, 1, 105–112.
Abdel-Aal, M. M. M. (2014).
Calibrating a trip distribution gravity model stratified by the trip purposes for the city of Alexandria. Alexandria Engineering Journal, 53(3), 677–689.
Lenormand, M., Bassolas, A., & Ramasco, J. J. (2016).
Systematic comparison of trip distribution laws and models. Journal of Transport Geography, 51, 158–169.
Meta AI for Good. (n.d.).
Movement Distribution Maps.
Muller, J. G., Dewalt, K., Goel, V., et al. (2025).
Integrating mobility, travel survey, and malaria case data to understand drivers of malaria importation to Zanzibar, 2022–2023. Malaria Journal, 24, 373.
21
21

22
Selected References
Measurement Validity, Privacy & Additional Information
Gosselin, C., Hubert, A., Devillet, G., & Dujardin, S. (2025).
Meta user movement data for analysing disaster-related mobility: sensitivity, bias, and usability. Research Square preprint.
Gibbs, H., Musolesi, M., Cheshire, J., & Eggo, R. M. (2026).
Impact of federated data with local differential privacy for human mobility modeling. EPJ Data Science.
Sakong, J., & Zentefis, A. K. (2023).
Bank Branch Access: Evidence from Geolocation Data. Federal Reserve Bank of Chicago Working Paper 2023-15.
Ait-Ali, A., & Eliasson, J. (2022).
The value of additional data for public transport origin–destination matrix estimation. Public Transport, 14, 419–439.
Zhang, C., Arora, N., Bian, C., et al. (2025).
Origin-Destination Travel Demand Estimation: An Approach That Scales Worldwide, and Its Application to Five Metropolitan Highway Networks. arXiv:2507.00306.
OpenStreetMap contributors. (n.d.).
OpenStreetMap tagging documentation: office, amenity, shop, building and landuse.
22

23
Selected References
OD Generation, Transfer & Cross-City References
He, T., Bao, J., Li, R., et al. (2020).
What is the human mobility in a new city: Transfer mobility knowledge across cities. The Web Conference 2020.
Rong, C., Feng, J., & Ding, J. (2023).
GODDAG: Generating origin-destination flow for new cities via domain adversarial training. IEEE TKDE, 35(10), 10048–10057.
Yu, C., Xie, X., Huang, Y., & Qiu, C. (2024).
Harnessing LLMs for Cross-City OD Flow Prediction. arXiv:2409.03937.
Rong, C., Zhang, X., Xi, Y., et al. (2025).
Satellites Reveal Mobility: A Commuting Origin-Destination Flow Generator for Global Cities. arXiv:2505.15870.
Yuan, Y., Zhang, Y., Ding, J., & Li, Y. (2025).
WorldMove, a global open data for human mobility. arXiv:2504.10506.
Liu, B., Li, T., Xiao, Z., et al. (2026).
All Cities are Equal: A Unified Human Mobility Generation Model Enabled by LLMs. arXiv:2602.19694.
Yang, J., Huang, S., Huang, Z., et al. (2026).
Transferable Human Mobility Network Reconstruction with neuroGravity. arXiv:2604.23678.
Chen, B., Meng, Z., Yang, F., et al. (2026).
Fusing Urban Structure and Semantics: A Conditional Diffusion Model for Cross-City OD Matrix Generation. arXiv:2605.00938.
23
