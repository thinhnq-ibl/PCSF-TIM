6.1 Scientific Implications: Recovering Behavior Rather than Flows
Opening

The central finding of this study is not simply that PIGF achieves competitive survey-free OD prediction, but that aggregate trip-length distributions preserve sufficient information to recover the latent behavioral mechanism governing spatial interaction. Across the experimental analyses, aggregate mobility summaries consistently enabled accurate recovery of city-specific Tanner distance-decay functions, identified distance decay as the dominant predictive component within the investigated gravity formulation, and supported downstream OD prediction without requiring target-city mobility observations. Taken together, these findings suggest that behavioral information can be inferred from aggregate mobility summaries to a much greater extent than has previously been assumed.

Đoạn này không nhắc lại từng bảng, mà tổng hợp RQ1–RQ3 thành một phát hiện chung.

6.1.1 From Flow Reconstruction to Behavioral Inference

Traditionally, survey-free mobility prediction has been approached as a flow reconstruction problem. Existing methods—including gravity calibration, deep learning, graph neural networks, and transfer-learning frameworks—primarily attempt to estimate complete origin–destination matrices, either by calibrating gravity parameters from observed OD flows or by learning direct mappings from historical mobility data. As a result, the availability of mobility observations remains central to most existing paradigms.

The findings of this study suggest an alternative perspective. Rather than reconstructing complete OD matrices directly, survey-free mobility prediction may instead be formulated as a behavioral inference problem. Aggregate trip-length distributions do not retain origin–destination identities, yet they preserve the statistical signature of travel-distance preferences. Recovering this latent behavioral mechanism, and combining it with independently estimated production and attraction components, provides sufficient information to reconstruct meaningful flow patterns.

This interpretation shifts the emphasis from recovering individual trips to recovering the behavioral process that generates those trips.

Đây chính là scientific contribution của paper.

6.1.2 Why Aggregate Mobility Remains Informative

An important implication of the experimental findings is that the usefulness of aggregate mobility data does not arise from preserving detailed spatial trajectories, but from preserving the dominant behavioral constraints governing destination choice.

The Shapley analysis shows that distance decay accounts for the majority of predictive performance within the investigated gravity framework, substantially exceeding the contributions of production and attraction estimation. This provides a mechanistic explanation for why highly compressed trip-length distributions remain informative despite discarding nearly all spatial identities. In other words, aggregate mobility summaries appear to retain the behavioral information that matters most for gravity-based interaction, even when individual travel records are no longer available.

This observation also helps explain why coarse aggregate products, such as three-bin movement distributions, continue to support effective calibration despite their limited spatial resolution.

Đoạn này giải thích RQ2, chứ không chỉ nhắc lại "85.8%".

6.1.3 Implications for Physics-Informed Mobility Modeling

The proposed framework also contributes to the broader development of physics-informed mobility modeling.

Recent years have seen increasing interest in combining physical principles with machine learning to improve interpretability and transferability. Most existing approaches, however, incorporate physical constraints after mobility observations have already been collected for training. In contrast, PIGF uses the physical structure of the gravity model to infer behavioral parameters directly from aggregate mobility statistics, without requiring target-city OD observations.

This distinction suggests that physical models can serve not only as predictive constraints but also as identification mechanisms, allowing latent behavioral parameters to be recovered from privacy-preserving aggregate data. More broadly, these results illustrate how interpretable physical formulations and aggregate mobility products can complement, rather than compete with, modern data-driven approaches.

Đây là đoạn nâng bài lên tầm physics-informed AI.

6.1.4 Scientific Perspective

Taken together, the experimental evidence supports a broader conceptual interpretation of survey-free mobility prediction. Rather than viewing aggregate mobility summaries as incomplete substitutes for origin–destination matrices, they may instead be regarded as observations of the underlying behavioral processes that govern spatial interaction. Under this perspective, the central task is no longer to reconstruct every individual movement, but to identify the dominant behavioral mechanism that shapes those movements.

Within the investigated gravity formulation, this behavioral mechanism is represented by the distance-decay function. The proposed Projection–Inference Gravity Framework demonstrates that recovering this latent mechanism from aggregate mobility summaries is sufficient to enable practical survey-free gravity calibration across the evaluated metropolitan areas. Although additional validation beyond the present dataset remains necessary, the results suggest a promising direction in which behavioral inference, rather than direct flow reconstruction, becomes the primary objective of survey-free urban mobility modeling.

6.2 Methodological and Practical Implications
Opening

Beyond its scientific implications, the proposed framework also has broader methodological and practical significance for urban mobility modeling. The experimental results suggest that the proposed decomposition strategy changes not only how distance-decay parameters are estimated, but also how survey-free mobility prediction can be constructed under severe data constraints.

Đoạn mở này không nhắc lại accuracy.

Mà nói

methodology.

6.2.1 Decomposition as a Modeling Strategy

Đây là ý đầu tiên.

Không nói

PIGF.

Mà nói

decomposition.

Most existing OD prediction methods optimize a single model to approximate complete origin–destination matrices. Whether based on classical calibration, deep learning, or transfer learning, these approaches generally learn a monolithic mapping between spatial inputs and mobility flows.

The proposed framework follows a different strategy by explicitly decomposing spatial interaction into production, attraction, and behavioral distance decay, allowing each component to be estimated from the information source most closely associated with its physical meaning.

This decomposition offers two methodological advantages. First, it enables each component to be estimated using the most appropriate information source rather than forcing all information into a single predictive model. Second, it produces a transparent inference pipeline in which each component can be independently validated, interpreted, and improved without retraining the entire system.

Đây là payoff của Method.

Không phải thuật toán.

Mà là design philosophy.

6.2.2 Aggregate Data as Calibration Signals

Đây là ý rất mạnh.

The results also suggest a broader role for aggregate mobility products.

Current aggregate datasets are frequently viewed as reduced substitutes for detailed trajectory records because they discard origin–destination identities and individual travel histories. Under this perspective, aggregate data are often considered insufficient for model calibration.

The present findings suggest a different interpretation. Aggregate mobility summaries may instead be regarded as behavioral calibration signals rather than incomplete mobility observations. Although they do not reveal where individual trips begin or end, they preserve information about the collective travel behavior governing destination choice. Consequently, aggregate mobility products can support model calibration even when they are insufficient for direct flow reconstruction.

This perspective may become increasingly relevant as privacy-preserving mobility products continue to replace individual-level trajectory datasets.

Đây là đoạn rất hay.

Reviewer sẽ nhớ.

6.2.3 Implications for Survey-Free Mobility Prediction

Đây mới nói practical.

From a practical perspective, the proposed framework substantially reduces the information required for gravity-model calibration.

Instead of requiring household travel surveys, GPS trajectories, or mobile-phone records, calibration relies only on publicly available spatial datasets together with aggregate trip-length distributions. These data sources are considerably easier to obtain, more consistent across regions, and inherently more compatible with modern privacy requirements.

As a result, the framework provides a feasible pathway for estimating commuting flows in metropolitan areas where conventional mobility surveys are unavailable, prohibitively expensive, or restricted by legal or privacy considerations.

Đây mới là practical.

Không cần nói smart city.

6.2.4 Scope of Applicability

Mình khuyên nên thêm.

Để reviewer thấy bạn hiểu phạm vi.

The proposed framework is particularly suited to deployment scenarios characterized by limited mobility observations but reasonable availability of open spatial data.

Examples include rapidly growing metropolitan regions, cities with infrequent household travel surveys, and privacy-sensitive applications where individual trajectories cannot be collected or shared.

Conversely, in data-rich environments where large-scale OD observations are routinely available, high-capacity supervised neural models may still achieve higher prediction accuracy. Under such circumstances, the primary advantage of PIGF lies in its interpretability, lower data requirements, and straightforward deployment rather than maximizing predictive performance.

Đoạn này cực kỳ quan trọng.

Reviewer sẽ đánh giá bạn rất công bằng.

Bạn không claim

PIGF tốt nhất.

Bạn claim

PIGF đúng chỗ.

Closing

Taken together, these methodological and practical implications suggest that the principal value of PIGF extends beyond the proposed implementation itself. By combining interpretable model decomposition with privacy-preserving aggregate mobility information, the framework illustrates a practical pathway toward survey-free urban mobility modeling that balances predictive performance, interpretability, and realistic data availability.

6.3 Scope and Limitations
Opening

Although the experimental results consistently support the proposed behavioral inference framework, the conclusions of this study should be interpreted within the scope of the present experimental setting and modeling assumptions. Recognizing these boundaries is important for understanding both the applicability of the proposed framework and the opportunities for future research.

Đây là opening.

Không xin lỗi.

Không defensive.

6.3.1 Scope of the Experimental Validation

Đây là limitation lớn nhất.

Không phải

US only.

Mà là

scope.

The empirical evaluation is conducted using 50 metropolitan areas in the United States, including 25 source cities for transferable production learning and 25 held-out target cities for evaluation. These metropolitan areas encompass diverse urban morphologies, ranging from dense transit-oriented cities to sprawling, polycentric, and coastal environments. Nevertheless, they remain embedded within a common national context characterized by similar census definitions, transportation systems, and data collection procedures.

Accordingly, the present experiments demonstrate robustness across heterogeneous U.S. metropolitan environments, but do not establish that the same behavioral relationships necessarily hold under substantially different institutional, socioeconomic, or transportation contexts. Additional evaluation across countries and mobility datasets will therefore be necessary before broader conclusions can be drawn.

Đoạn này wording rất an toàn.

6.3.2 Dependence on the Gravity Formulation

Đây là limitation quan trọng nhất về mặt học thuật.

The proposed framework is built upon the classical gravity formulation, in which spatial interaction is decomposed into origin production, destination attraction, and distance-dependent behavioral friction. Consequently, the interpretation of recovered behavioral information is specific to this modeling framework.

Although the experiments demonstrate that distance decay is the dominant predictive component within the investigated gravity formulation, this conclusion should not be interpreted as evidence that all urban mobility systems are governed primarily by geographical distance. In metropolitan areas where multimodal accessibility, public transportation networks, or socioeconomic interactions play a stronger role, additional behavioral mechanisms may become equally or more important.

This limitation reflects the scope of the current behavioral model rather than the behavioral inference framework itself.

Đây là câu rất mạnh.

Bạn không overclaim.

6.3.3 Aggregate Mobility Representation

Đây là limitation về data.

The present study evaluates behavioral recovery using aggregate trip-length distributions represented as one-dimensional histograms. Although such representations substantially reduce privacy exposure while preserving dominant travel-distance characteristics, they inevitably discard other dimensions of human mobility, including travel direction, temporal dynamics, transport mode, and activity purpose.

Consequently, the proposed framework should be interpreted as recovering the dominant distance-dependent component of aggregate mobility rather than the complete behavioral complexity of urban travel.

Đây là limitation rất hợp lý.

Không phải Meta.

Mà là

histogram.

6.3.4 Survey-Free Does Not Mean Data-Free

Đây là đoạn mình rất thích.

Reviewer sẽ nhớ.

Finally, although PIGF eliminates the need for target-city origin–destination observations, it should not be interpreted as a completely data-free approach. The framework still relies on publicly available spatial information, including population distributions, built-environment characteristics, and aggregate mobility summaries, to estimate the individual components of the gravity model.

Accordingly, the contribution of this work lies in reducing the dependence on localized mobility observations, rather than eliminating data requirements altogether. The proposed framework therefore complements, rather than replaces, data-rich mobility modeling when detailed observations are available.

Đây là câu rất hay.

Reviewer sẽ đánh giá rất cao.

Vì bạn chủ động làm rõ.

Closing

Taken together, these limitations define the current scope of the proposed behavioral inference framework rather than diminishing its principal findings. Within the evaluated setting, the experiments consistently demonstrate that aggregate trip-length distributions contain sufficient information to recover behaviorally meaningful distance-decay functions and support survey-free gravity calibration. Extending this framework beyond the present assumptions and evaluation domain remains an important direction for future research.

6.4 Future Research Directions
Opening

The limitations identified above also suggest several promising directions for future research. Rather than representing shortcomings specific to PIGF alone, they reflect broader challenges in survey-free mobility modeling and behavioral inference from aggregate data. Extending the present framework along these directions may further improve both the applicability and the theoretical understanding of aggregate-based mobility prediction.

Đây là mở đầu.

Không xin lỗi.

Không defensive.

6.4.1 Beyond U.S. Metropolitan Areas

Đây là limitation lớn nhất.

The present evaluation is conducted exclusively on U.S. metropolitan areas, whose commuting behavior, transportation systems, and urban structures exhibit relatively consistent characteristics.

An important next step is to evaluate whether the proposed behavioral inference framework remains applicable across cities with substantially different socioeconomic conditions, transport infrastructures, and cultural travel patterns.

Cross-country validation would help determine whether the recoverability of distance-decay functions represents a universal behavioral property or depends on regional mobility characteristics.

Đây là extension.

Không phải

collect more data.

6.4.2 Richer Behavioral Representations

Đây là rất hay.

Hiện paper

distance.

Tương lai

behavior.

The current framework models travel behavior exclusively through geographical distance.

Future research may extend the behavioral inference framework to incorporate richer impedance measures, including travel time, multimodal accessibility, transport cost, and temporal congestion.

Recovering multiple behavioral dimensions simultaneously may provide a more comprehensive description of urban mobility while preserving the survey-free philosophy of the proposed framework.

Đây là hướng research.

Không phải engineering.

6.4.3 Beyond Tanner Functions

Đây là hướng rất mạnh.

Although the Tanner formulation provides a flexible and interpretable representation of distance decay, the proposed inference framework is not fundamentally restricted to this particular functional form.

Future work may investigate non-parametric behavioral recovery, neural deterrence functions, or Bayesian formulations capable of representing more complex travel preferences while maintaining physical interpretability.

Such extensions would help determine whether the observed recoverability is specific to Tanner functions or reflects a broader property of aggregate mobility distributions.

Đây là hướng rất reviewer thích.

6.4.4 Toward Hybrid Physics-Informed Learning

Đây là mình thích nhất.

Finally, the decomposition strategy adopted by PIGF naturally suggests future integration with modern machine learning.

Rather than replacing physics-based models with end-to-end neural architectures, future research may combine behavioral inference from aggregate mobility summaries with representation learning, graph neural networks, or foundation models for urban systems.

Such hybrid approaches could preserve the interpretability and low data requirements of physics-informed models while benefiting from the expressive capacity of modern deep learning.

This direction may ultimately bridge the current separation between interpretable gravity models and high-capacity neural mobility predictors.

Đây là đoạn rất mạnh.

Không overclaim.

Closing

Taken together, these directions indicate that the proposed framework should be viewed not as a final solution, but as an initial demonstration of behavioral inference from aggregate mobility summaries. Future developments may extend this paradigm toward richer behavioral models, broader geographical settings, and hybrid physics-informed learning frameworks, further advancing survey-free urban mobility prediction.