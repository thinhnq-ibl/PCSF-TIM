2.1 Mobility Prediction under Data Scarcity

Accurate origin–destination (OD) prediction is a fundamental task in transportation planning, accessibility analysis, infrastructure design, and urban policy because it quantifies how travel demand is distributed between locations. Traditionally, reliable OD matrices are constructed from household travel surveys, census commuting records, mobile-phone trajectories, GPS traces, or smart-card transactions. While these data sources provide detailed mobility observations, they are often expensive to collect, infrequently updated, geographically incomplete, and increasingly constrained by privacy regulations. Consequently, obtaining high-quality OD matrices remains one of the primary bottlenecks for applying mobility models, particularly in data-scarce cities and rapidly developing regions.

To alleviate this limitation, a wide range of OD prediction methods has been proposed. Classical spatial interaction models estimate mobility through analytical formulations such as gravity and radiation models, whereas more recent approaches employ deep neural networks, graph neural networks, and transfer learning to improve predictive performance by exploiting spatial representations learned from historical mobility data. These advances have substantially improved OD prediction accuracy under data-rich conditions and expanded the ability of models to capture complex spatial interactions.

Despite their methodological differences, however, most existing approaches continue to depend on some form of mobility observation during model construction or calibration. Classical gravity models require observed OD flows to estimate city-specific distance-decay parameters, while supervised deep-learning models depend on historical OD matrices or trajectory datasets for training. Even recent transfer-learning and zero-shot approaches typically assume that representative mobility observations are available in source cities from which transferable knowledge can be learned. As a result, reliable mobility observations remain an essential prerequisite for most existing OD prediction frameworks.

Ending (Transition)

These limitations motivate an important question: can meaningful mobility behavior be inferred without relying on conventional OD observations? Addressing this question requires understanding not only how mobility flows are predicted, but also how the underlying behavioral mechanism governing destination choice can be identified. This issue is closely related to the estimation of distance-decay functions, which forms the focus of the next section.

2.2 Distance-Decay Modeling and Recovery

Distance decay has long been recognized as the fundamental behavioral mechanism underlying spatial interaction. Within gravity-based mobility models, it describes how interaction probability decreases with increasing travel impedance and serves as the principal constraint governing destination choice. Since the pioneering work of Tanner and Wilson, distance-decay functions have formed the behavioral core of spatial interaction models and have been widely adopted in transportation planning, accessibility analysis, migration studies, and urban mobility forecasting (Tanner, 1961; Wilson, 1971; Fotheringham & O'Kelly, 1989; Sen & Smith, 1995). More recent studies continue to demonstrate that the choice of deterrence function substantially influences the accuracy and interpretability of mobility prediction models (Lenormand et al., 2016; Atwal et al., 2025).

To represent heterogeneous travel behavior, numerous functional forms have been proposed, including exponential, power-law, logistic, and Tanner-type deterrence functions. Among these, the Tanner function has become one of the most widely used formulations because it simultaneously captures short-distance attraction and long-distance attenuation using only two interpretable parameters. Recent research has further extended distance-decay calibration through statistical estimation, robust optimization, sparse regression, Bayesian inference, and physics-informed modeling to improve parameter stability and transferability while preserving behavioral interpretability (Flowerdew & Aitkin, 1982; Lenormand et al., 2016; Stewart et al., 2024; Atwal et al., 2025).

Despite these methodological advances, existing calibration approaches share a common assumption: the availability of observed mobility flows. Classical gravity models estimate deterrence parameters directly from origin–destination matrices using maximum-likelihood estimation or least-squares optimization, while more recent data-driven approaches similarly rely on household travel surveys, mobile-phone trajectories, GPS traces, or complete OD observations to infer behavioral parameters (Wilson, 1971; Flowerdew & Aitkin, 1982; Stewart et al., 2024; Yang et al., 2026). Consequently, improvements have primarily focused on how to estimate distance-decay functions more accurately, rather than whether the underlying behavioral mechanism can be recovered without mobility observations.

This limitation becomes increasingly important as privacy-preserving mobility products replace individual trajectory datasets. Although aggregate mobility summaries no longer preserve origin–destination identities, they still retain the statistical distribution of travel distances, suggesting that they may encode the latent behavioral constraints governing destination choice. Whether such aggregate information is sufficient to recover city-specific distance-decay functions, however, remains largely unexplored. Addressing this question represents a critical prerequisite for enabling survey-free gravity calibration and forms the focus of the present study.

Transition sang R3

The possibility of recovering behavioral information from aggregate mobility summaries depends fundamentally on the information preserved in emerging aggregate mobility products. We therefore next review recent developments in privacy-preserving aggregate mobility datasets and their applications in urban mobility analysis.

Citation đề xuất

Mình khuyến nghị sử dụng các citation sau (theo vai trò, không phải theo năm).

Classical spatial interaction
Tanner, J. C. (1961). Factors affecting the amount of travel.
Wilson, A. G. (1971). A family of spatial interaction models.
Fotheringham, A. S., & O'Kelly, M. E. (1989). Spatial Interaction Models: Formulations and Applications.
Sen, A., & Smith, T. E. (1995). Gravity Models of Spatial Interaction Behavior.

Vai trò: nền tảng của distance decay và gravity.

Tanner calibration and deterrence functions
Flowerdew & Aitkin (1982).
Lenormand et al. (2016), A new method using medians to calibrate single-parameter spatial interaction models.
Stewart et al. (2024), Sparse regression for data-driven deterrence functions.
Atwal et al. (2025), What determines travel time and distance decay in spatial interaction and accessibility?

Vai trò: các phương pháp hiệu chỉnh hiện đại.

Physics-informed / modern calibration
Atwal et al. (2025), Gravity-informed deep flow inference.
Yang et al. (2026), NeuroGravity.

Vai trò: cho thấy ngay cả các phương pháp hiện đại vẫn cần dữ liệu OD hoặc dữ liệu di chuyển để học hoặc hiệu chỉnh.

2.3 Aggregate Mobility Products for Privacy-Preserving Mobility Analysis

The growing availability of digital mobility data has substantially advanced the study of human movement, yet it has also intensified concerns regarding privacy protection, data governance, and the responsible sharing of individual travel records. Mobile-phone trajectories, GPS traces, and app-based location data contain detailed information about individual mobility behavior, making them highly valuable for transportation research while simultaneously raising significant privacy and ethical challenges. Consequently, recent years have witnessed a shift from publishing individual mobility records toward releasing privacy-preserving aggregate mobility products, which summarize collective travel behavior while preventing the reconstruction of individual trajectories (De Montjoye et al., 2013; Blondel et al., 2015; European Commission, 2020).

Several large-scale aggregate mobility datasets have been developed following this paradigm. Examples include Meta Movement Distribution Maps (MDM), which provide differentially private trip-length distributions aggregated over spatial regions; Google Community Mobility Reports, which summarize temporal changes in population activity across different place categories; and aggregated mobility datasets released through the Humanitarian Data Exchange (HDX) and related humanitarian initiatives for disaster response and population monitoring. Although these products differ in spatial resolution, aggregation strategy, and intended application, they share a common objective: preserving useful mobility information while substantially reducing privacy risks associated with individual trajectory data (Meta, 2024; Google, 2022; HDX, 2024).

Because aggregate mobility products intentionally discard origin–destination identities, previous studies have primarily employed them for descriptive mobility analysis, accessibility assessment, epidemic modeling, disaster response, and large-scale urban monitoring (Oliver et al., 2020; Buckee et al., 2020; Tizzoni et al., 2022). Within this literature, aggregate mobility statistics are generally regarded as high-level indicators of collective movement patterns rather than as information suitable for calibrating behavioral mobility models. Consequently, their potential value for recovering the behavioral mechanisms underlying spatial interaction has received comparatively little attention.

Nevertheless, aggregate mobility products preserve an important characteristic that is directly relevant to gravity-based mobility modeling. Although they no longer identify individual origins or destinations, they retain the empirical distribution of travel distances across an urban system. Since distance-decay functions describe precisely how interaction probability varies with travel distance, these aggregate trip-length distributions may encode the latent behavioral information governing destination choice. Whether such aggregate statistics contain sufficient information to recover city-specific distance-decay functions, however, remains largely unexplored. Addressing this question is essential for enabling survey-free gravity calibration and motivates the behavioral inference framework proposed in this study.

Transition to R4

While aggregate mobility products substantially reduce the dependence on individual trajectory data, existing mobility prediction approaches have only partially exploited the behavioral information preserved in these datasets. We therefore next review recent efforts toward survey-free and zero-shot mobility prediction and discuss their remaining limitations.

Citation đề xuất

Mình khuyến nghị dùng các tài liệu sau.

Privacy and mobility data

Đây là nhóm citation nền.

de Montjoye, Y.-A., Hidalgo, C. A., Verleysen, M., & Blondel, V. D. (2013).
Unique in the Crowd: The privacy bounds of human mobility.
Scientific Reports.
Blondel, V. D., Decuyper, A., & Krings, G. (2015).
A survey of results on mobile phone datasets analysis.
EPJ Data Science.
Aggregate mobility products
Meta Movement Distribution Maps Documentation (2024).

Đây là citation chính.

Google Community Mobility Reports (2022).
Humanitarian Data Exchange (HDX) Mobility Data Documentation.
Applications
Oliver et al. (2020).
Mobile phone data for informing public health actions across the COVID-19 pandemic.
Nature Communications.
Buckee et al. (2020).
Aggregated mobility data could help fight COVID-19.
Science.
Tizzoni et al. (2022).
(Mobility data for epidemic modelling and public health.)

2.4 Survey-Free and Zero-Shot Mobility Prediction

The increasing scarcity of high-quality mobility observations has stimulated growing interest in survey-free and zero-shot mobility prediction. Rather than calibrating models independently for each city, these approaches aim to transfer mobility knowledge learned from data-rich regions to locations where conventional travel surveys are unavailable. By exploiting transferable spatial representations or behavioral regularities, they seek to reduce the dependence on locally collected OD observations while maintaining competitive predictive performance.

Recent studies have explored several transfer strategies. Deep learning approaches such as DeepGravity demonstrate that complex nonlinear relationships between land use, population distribution, and travel demand can be learned directly from historical OD matrices, achieving substantial improvements over classical gravity models in data-rich environments (Xiong et al., 2019). More recent graph-based and transfer-learning frameworks further improve cross-city prediction by learning transferable representations of urban mobility networks. For example, NeuroGravity reconstructs human mobility networks by combining neural representation learning with gravity-inspired inductive biases, while TransGM and related cross-city transfer models explicitly transfer mobility knowledge from source cities to previously unseen target regions (Yang et al., 2026; relevant TransGM reference).

These approaches significantly improve the practicality of mobility prediction under limited local data. However, they continue to rely on mobility observations during the learning process. Deep learning models require historical OD matrices or trajectory datasets for supervised training, whereas transfer-learning methods assume that representative mobility observations are available in one or more source cities from which transferable knowledge can be extracted. Consequently, although the target city may contain no OD observations, the predictive model itself remains fundamentally dependent on observed mobility behavior during model development.

An emerging line of research has begun incorporating physical principles into learning-based frameworks to improve interpretability and transferability. Physics-informed gravity models and hybrid neural architectures embed distance-decay constraints or spatial interaction mechanisms into deep learning models, reducing overfitting while preserving behavioral consistency (Atwal et al., 2025; Yang et al., 2026). Nevertheless, these methods still estimate behavioral mechanisms from observed mobility data rather than inferring them directly from privacy-preserving aggregate mobility summaries.

Therefore, despite substantial progress in survey-free and zero-shot mobility prediction, an important gap remains. Existing approaches primarily transfer behavioral knowledge learned from observed mobility data, whereas it remains unclear whether the behavioral mechanism itself can be recovered directly from aggregate mobility products without access to OD observations or trajectory records.

Transition sang R5

This remaining challenge motivates the central research gap addressed in this study. The following section synthesizes the limitations of existing literature and positions the proposed behavioral inference framework within the broader landscape of survey-free mobility prediction.

Citation nên dùng
Deep learning
DeepGravity
Xiong et al., 2019.
Transfer learning
TransGM
NeuroGravity
Yang et al., 2026.
Physics-informed
Gravity-informed Deep Flow Inference
Gravity-inspired Truck OD
NeuroGravity (nếu muốn nhấn mạnh hybrid).

2.5 Research Gap and Positioning

The preceding review demonstrates substantial progress in origin–destination prediction, spatial interaction modeling, aggregate mobility analysis, and survey-free mobility prediction. Classical gravity models have established distance decay as the fundamental behavioral mechanism governing spatial interaction, while recent deep learning and transfer-learning approaches have significantly improved prediction accuracy by exploiting increasingly rich mobility observations. At the same time, emerging privacy-preserving aggregate mobility products have expanded access to large-scale mobility information without exposing individual travel trajectories. Collectively, these developments have substantially advanced the state of urban mobility modeling. However, they also reveal a common conceptual limitation: behavioral information is consistently treated as something that must be learned from observed mobility flows rather than inferred directly from aggregate mobility statistics.

This distinction is fundamental. Existing gravity-based approaches estimate distance-decay functions from observed origin–destination matrices through model calibration (Wilson, 1971; Flowerdew & Aitkin, 1982; Sen & Smith, 1995), whereas recent neural and transfer-learning methods learn transferable behavioral representations from historical mobility observations (Xiong et al., 2019; Yang et al., 2026). Although these approaches differ considerably in modeling philosophy, they all assume that behavioral knowledge originates from some form of observed mobility data. Similarly, studies using privacy-preserving aggregate mobility products have primarily focused on descriptive mobility analysis, accessibility assessment, and population monitoring, rather than investigating whether these aggregate statistics themselves contain sufficient information for behavioral model calibration (Oliver et al., 2020; Buckee et al., 2020; Meta, 2024).

These observations suggest that the central challenge in survey-free mobility prediction may not be the absence of OD matrices themselves, but rather the absence of a framework capable of recovering latent behavioral mechanisms directly from aggregate mobility information. If aggregate trip-length distributions preserve the statistical signature of distance-dependent travel behavior, then behavioral model calibration may be reformulated as an inverse inference problem instead of a conventional flow reconstruction problem. Such a perspective fundamentally differs from existing survey-free approaches, which primarily transfer behavioral knowledge learned elsewhere, by investigating whether the behavioral mechanism itself can be identified without first observing origin–destination flows.

Motivated by this perspective, this study formulates survey-free gravity calibration as a behavioral inference problem. Specifically, we investigate whether privacy-preserving aggregate trip-length distributions contain sufficient information to recover city-specific Tanner distance-decay functions and whether the recovered behavioral mechanism can support competitive OD prediction when integrated with transferable production estimation and analytical destination attraction. By shifting the objective from flow reconstruction to behavioral inference, the proposed Projection–Inference Gravity Framework (PIGF) provides an interpretable and privacy-preserving alternative for mobility prediction in data-scarce environments.

The next section formalizes the problem setting and introduces the proposed behavioral inference framework.

Logic của R5

Đoạn này thực chất chỉ có 4 bước.

Previous studies
        │
        ▼
Common assumption
(behavior comes from OD)

        │
        ▼
Missing question
(Can behavior be inferred directly?)

        │
        ▼
Our positioning
Behavioral inference instead of flow reconstruction

Đây là synthesis, không phải literature review.

Citation Mapping
Nội dung	Citation đề xuất
Gravity calibration requires OD	Wilson (1971); Flowerdew & Aitkin (1982); Sen & Smith (1995)
Distance decay as behavioral mechanism	Tanner (1961); Fotheringham & O'Kelly (1989); Lenormand et al. (2016)
Deep OD prediction	Xiong et al. (2019) – DeepGravity
Transfer / zero-shot	Yang et al. (2026) – NeuroGravity; TransGM
Aggregate mobility applications	Oliver et al. (2020); Buckee et al. (2020); Meta MDM (2024)

