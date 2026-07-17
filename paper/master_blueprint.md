Master Blueprint v2.0 — Introduction Logic Blueprint
Block 1 – Importance
Core message

Accurate origin–destination (OD) flow prediction is fundamental to transportation planning, infrastructure development, and accessibility analysis.

Supporting points
Reliable OD information supports transportation planning and infrastructure investment.
It enables accessibility evaluation, travel demand forecasting, and urban policy analysis.
Consequently, accurate OD estimation has long been a central problem in transportation science.
Transition

Yet, acquiring the localized mobility data required to estimate or calibrate OD flows remains a major practical challenge.

Citation
Barbosa et al. (2018)
González et al. (2008)
Song et al. (2010)
Block 2 – Practical Problem
Core message

Reliable OD observations remain difficult to obtain because conventional mobility data collection is expensive, time-consuming, and often inaccessible.

Supporting points
Household travel surveys require substantial financial and institutional resources.
Mobile-phone and GPS trajectories provide rich mobility information but are frequently unavailable because of privacy regulations and commercial restrictions.
Consequently, most cities—particularly data-scarce regions—lack reliable local OD observations.
Transition

This challenge has motivated extensive research on estimating OD flows from incomplete or alternative mobility information.

Citation

Primary

Egu & Bonnel (2020)

Review

Transit OD Matrix Estimation Review (2021)
Block 3 – Existing Solutions
Core message

A wide range of analytical and data-driven models have been developed to estimate urban OD flows.

Supporting points

Classical models

Gravity
Radiation

Learning-based models

DeepGravity
MPGCN
GODDAG

Transfer-learning models

neuroGravity
TransGM
Yang et al. (2026)
Transition

Despite their methodological diversity, these approaches still rely on some form of observed mobility information.

Citation
Wilson (1971)
Simini et al. (2012)
Hu et al. (2020)
Rong et al. (2023)
Yang et al. (2026)
Enaya et al. (2026)
Block 4 – Shared Limitation
Core message

Existing OD prediction approaches ultimately depend on observed mobility data for model calibration, training, or transfer.

Supporting points
Gravity models require observed OD flows to calibrate distance-decay parameters.
Deep and graph learning methods require historical OD matrices for supervised learning.
Transfer-learning approaches still require mobility observations from source cities or auxiliary structural information for adaptation.
Mini conclusion

Although their modeling strategies differ substantially, they share the same underlying dependency on observed mobility information.

Transition

This common limitation motivates the search for alternative mobility information that is both accessible and privacy-preserving.

Citation
Simini et al. (2021)
Yang et al. (2026)
Enaya et al. (2026)
Block 5 – Emerging Opportunity
Core message

Recent aggregate mobility products provide a new source of standardized and privacy-preserving mobility information.

Supporting points
Meta Movement Distribution Maps (MDM) provide aggregated population-level trip-length distributions instead of individual trajectories or OD matrices.
These datasets are publicly available, globally consistent, and designed to preserve user privacy.
They therefore create new opportunities for mobility modeling in data-scarce environments.
Transition

However, whether aggregate trip-length distributions contain sufficient information to replace local OD observations remains unknown.

Citation
Meta Movement Distribution Maps
Pappalardo et al. (2023)
Block 6 – Scientific Hypothesis
Core message

Human mobility is fundamentally governed by spatial distance-decay mechanisms.

Supporting points
Distance decay is a well-established determinant of spatial interaction.
Aggregate trip-length distributions are the observable statistical outcome of these distance-decay processes.
Scientific hypothesis

Aggregate trip-length distributions may preserve sufficient information to recover city-specific distance-decay functions without requiring local OD observations.

Transition

This hypothesis naturally raises a fundamental question regarding the recoverability of distance-decay information from aggregate mobility summaries.

Citation
Tanner (1961)
Verma & Ukkusuri (2025)

(No citation for the hypothesis.)

Block 7 – Knowledge Gap
Core message

It remains unclear whether aggregate trip-length distributions contain sufficient information to recover expressive city-specific distance-decay functions under realistic urban conditions.

Supporting points
Previous studies have demonstrated that simple aggregate mobility statistics can calibrate simplified interaction models.
However, it remains unknown whether richer distance-decay functions can be recovered solely from aggregate trip-length distributions while accounting for heterogeneous urban structure.
Transition

To address this unresolved question, this study investigates the following research questions.

Citation
Merlin (2020)
Lenormand et al. (2016)
Block 8 – Research Questions
Transition

To address these knowledge gaps, this study investigates three sequential research questions.

RQ1 (Recoverability)

Can aggregate trip-length distributions recover city-specific distance-decay functions without access to local OD observations?

RQ2 (Information Content)

If recoverable, how much predictive information does the recovered distance-decay component contribute to OD prediction?

RQ3 (Practical Utility)

Can the recovered distance-decay information enable accurate survey-free OD prediction in data-scarce cities?

(No citation.)

Block 9 – Paper Overview & Research Claim
Paper overview

This paper proposes a survey-free framework for gravity-model calibration using aggregate trip-length distributions.

Framework overview

The proposed framework recovers city-specific distance-decay functions from aggregate trip-length distributions and integrates them with transferable estimates of origin production and destination attraction for survey-free OD prediction.

Main research claim

Aggregate trip-length distributions preserve sufficient information to recover city-specific distance-decay functions, enabling accurate gravity-model calibration and survey-free OD prediction without local OD observations.

(No citation.)

Overall Storyline
Importance
        │
        ▼
Reliable OD data are difficult to obtain
        │
        ▼
Many prediction methods have been proposed
        │
        ▼
But all still require observed mobility data
        │
        ▼
Aggregate mobility products are now available
        │
        ▼
They provide aggregate trip-length distributions
        │
        ▼
Trip-length distributions reflect distance-decay
        │
        ▼
Scientific hypothesis
        │
        ▼
Knowledge gap
        │
        ▼
Research questions
        │
        ▼
Proposed framework
        │
        ▼
Research claim