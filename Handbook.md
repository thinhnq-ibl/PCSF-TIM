# Theoretical Background and Methodological Blueprint

## Scientific Thesis

> **This handbook develops the scientific argument that behavioural parameters governing collective distance sensitivity may be identifiable from aggregate trip-length observations because mobility aggregation preserves behaviour-relevant statistical information that can be interpreted within the Gravity framework.**

*This Handbook serves as the theoretical justification for the manuscript. It is structured as a scientific proof: each module poses a core scientific question, answers it with a central claim, and supports that claim through a series of evidence-backed arguments. This rigorous progression establishes the necessity and validity of inferring distance-decay parameters from aggregate mobility observations.*

---

# Human Mobility Handbook V4.0 (Frozen Architecture)

| Module | Scientific Question | Scientific Answer | Leads to... |
| :--- | :--- | :--- | :--- |
| **A. Gravity as the Scientific Foundation** | **Why is Gravity an appropriate scientific framework for human mobility?** | Human mobility can be represented as spatial interactions between origins and destinations, with movement constrained by travel impedance. Gravity provides a principled mathematical description of this process. | If Gravity is the framework, **what governs travel impedance?** |
| **B. Distance-Decay as the Behavioural Mechanism** | **Why is distance-decay the central behavioural mechanism in Gravity models?** | Distance-decay determines how interaction probability decreases with distance and therefore governs collective distance sensitivity. The parameters of the distance-decay function become the primary quantities of scientific interest. | If θ is the key behavioural quantity, **can it be identified from available data?** |
| **C. Information Transformation through Mobility Aggregation** | **What information remains after mobility observations are aggregated?** | Aggregate datasets (e.g., Trip-Length Distributions) preserve overall travel-distance statistics but no longer explicitly record Origin–Destination interactions. Whether these aggregate observations contain sufficient information to identify the distance-decay parameters remains an open scientific question. | If this is unknown, **how can we determine it scientifically?** |
| **D. Inference Principle: A Probabilistic Framework** | **How can the parameters of the distance-decay function be statistically identified from aggregate Trip-Length Distribution observations?** | Treat parameter identification as a probabilistic inverse problem. Construct an observation model linking the latent distance-decay parameters to the observed Trip-Length Distribution, then estimate θ using statistical inference. | This framework is then implemented and validated in the proposed method. |
| **E. Mathematical Framework: Gravity-based Statistical Identification** | **How is the probabilistic identification framework implemented for distance-decay parameter estimation?** | Specify the probabilistic model (Gravity + Observation Model + Likelihood) that links the latent parameters to the observed distribution. | **Does empirical evidence support the hypothesis?** |
| **F. Empirical Evaluation of the Identification Hypothesis** | **Do aggregate Trip-Length Distribution observations contain sufficient empirical evidence to identify the parameters of the distance-decay function?** | Empirically evaluate the central scientific hypothesis using the probabilistic framework to see if it reproduces mobility patterns. | **Scientific Conclusion.** |

### Frozen Logic Graph (V4.0)

```mermaid
flowchart TD
    subgraph Handbook ["HUMAN MOBILITY HANDBOOK V4.0"]
        A["A. Why Gravity?
(Scientific foundation)"] --> B["B. What is the key behavioural mechanism?
(Distance-decay governs mobility interactions)"]
        B --> C["C. Can aggregate observations identify θ?
(Knowledge gap: Unknown)"]
        C --> D["D. How should this question be answered?
(Inference principle: Probabilistic inverse problem)"]
        D --> E["E. How is the probabilistic model constructed?
(Mathematical realization: Gravity + Likelihood)"]
        E --> F["F. Does empirical evidence support the hypothesis?
(Scientific evidence)"]
    end

    F --> S["Scientific Conclusion"]

    style Handbook fill:#f0f8ff,stroke:#00509e,stroke-width:2px,stroke-dasharray: 5 5
```

---

# Module A — Gravity as the Scientific Foundation

| **Component**              | **Content** |
| -------------------------- | --- |
| **Module Title**           | **Gravity as the Scientific Foundation of Human Mobility Modelling** |
| **Scientific Question**    | **Why should human mobility be studied within the Gravity framework?** |
| **Why is this module indispensable?** | Without Gravity, distance-decay has no scientific context. |
| **Mission**                | Thiết lập Gravity là ngôn ngữ khoa học chuẩn để mô tả dòng di chuyển tổng hợp, đồng thời chứng minh rằng decomposition của Gravity thành urban structure và behavioural response là nền tảng cho việc nhận diện và chuyển giao hành vi. |
| **Central Claim**          | **Gravity remains the canonical scientific framework for aggregate spatial interaction because it explicitly separates urban structure from behavioural distance sensitivity. Behaviour can only become transferable after it is explicitly identified.** |

### Supporting Claims

| **Supporting Claim** | **Purpose** | **Representative Evidence (SOTA)** | **Expected Conclusion** |
| --- | --- | --- | --- |
| **Claim A1. Gravity has evolved from an empirical analogy into the canonical mathematical representation of spatial interaction.** | Chứng minh Gravity không chỉ là mô hình lịch sử mà đã trở thành nền tảng lý thuyết của spatial interaction. | • Zipf (1946): Gravity analogy.<br>• Wilson (1971): Entropy-maximizing derivation.<br>• Flowerdew & Aitkin (1982): Statistical estimation (Poisson framework).<br>• Haynes & Fotheringham (1984): Classical spatial interaction modelling.<br>• Barbosa et al. (2018): Physics Reports review. | Gravity là ngôn ngữ khoa học chuẩn để mô tả aggregate spatial interactions. |
| **Claim A2. Modern mobility models extend rather than replace the Gravity paradigm.** | Trả lời phản biện rằng Deep Learning đã thay thế Gravity. | • Deep Gravity (Simini et al., 2021).<br>• neuroGravity (Yang et al., 2026).<br>• TransGM (Enaya et al., 2026).<br>• Universal Geography Neural Network (Guo et al., 2025).<br>• Imagery2Flow (Xu et al., 2025). | AI và Deep Learning chủ yếu tăng cường khả năng biểu diễn hoặc học các thành phần của Gravity chứ không thay thế cấu trúc khoa học của nó. |
| **Claim A3. Gravity explicitly separates urban structure from spatial interaction behaviour.** | Thiết lập decomposition sẽ được dùng xuyên suốt Handbook và bài báo. | • Wilson (1971).<br>• Lenormand et al. (2016).<br>• Comparative studies of gravity models. | Gravity phân tách rõ **Urban Structure** ($O_i$, $D_j$) khỏi **Behaviour** ($f(d_{ij};	heta)$). |
| **Claim A4. The distance-decay function is the unique component that explicitly represents spatial impedance.** | Cô lập đúng đối tượng nghiên cứu của bài báo. | • Tanner (1961).<br>• Liang et al. (2013).<br>• Lenormand et al. (2016). | Trong toàn bộ mô hình Gravity, chỉ **distance-decay function** trực tiếp mô tả ảnh hưởng của khoảng cách lên xác suất tương tác. |
| **Claim A5. Behaviour can only become transferable after it has first been explicitly identified.** | Bổ sung cầu nối logic từ Module A sang Module E — giải quyết câu hỏi tại sao identification là prerequisite. | • Theoretical reasoning grounded in A3 & A4.<br>• Yang et al. (2026).<br>• Enaya et al. (2026). | Nếu distance-decay ($	heta$) không được nhận diện một cách tường minh, không thể chuyển giao hành vi từ ngữ cảnh này sang ngữ cảnh khác mà không cần OD matrix. |

### Core Mathematical Representation

| **Purpose** | **Content** |
| --- | --- |
| **Scientific Formulation**    | $T_{ij}=O_iD_jf(d_{ij};	heta)$ |
| **Urban Structure**           | $O_i$: Origin emission (trip production).<br>$D_j$: Destination attraction (trip attraction). |
| **Behavioural Component**     | $f(d_{ij};	heta)$: Distance-decay function describing collective distance sensitivity. |
| **Scientific Interpretation** | Aggregate mobility can be viewed as the interaction between urban opportunities ($O_i,D_j$) and behavioural responses to travel distance ($f(d_{ij};	heta)$). Behaviour is only transferable once $	heta$ has been independently identified. |

### Scientific Consequence

| **Component** | **Content** |
| --- | --- |
| **Scientific Conclusion** | Gravity remains the dominant scientific framework for modelling aggregate spatial interactions. It naturally decomposes mobility into **urban structure** and **distance-dependent behavioural response**, identifying the distance-decay function as the primary object of analysis. **Therefore, behavioural identification becomes a scientifically meaningful objective.** |

### Transition to Module B

| **Component** | **Content** |
| --- | --- |
| **Transition Question**     | **If Gravity is the framework, what governs travel impedance?** |
| **Motivation for Module B** | Understanding the scientific meaning of the distance-decay function is essential before asking whether its parameters can be identified from aggregate observations. |

---

# Module B — The Scientific Meaning of the Distance-Decay Function

| **Component**              | **Content** |
| -------------------------- | --- |
| **Module Title**           | **The Scientific Meaning of the Distance-Decay Function** |
| **Scientific Question**    | **What does the distance-decay function represent, and why is it the central object of behavioural analysis in Gravity models?** |
| **Why is this module indispensable?** | Without understanding distance-decay, there is no identifiable behavioural object. |
| **Mission**                | Thiết lập ý nghĩa khoa học của distance-decay function, làm rõ vai trò của các tham số trong việc mô tả collective distance sensitivity và chuẩn bị nền tảng để nghiên cứu khả năng suy luận các tham số này từ Trip-Length Distributions. |
| **Central Claim**          | **The distance-decay function is the behavioural component of Gravity models, encoding collective distance sensitivity under a given urban environment.** |

### Supporting Claims

| **Supporting Claim** | **Purpose** | **Representative Evidence (SOTA)** | **Expected Conclusion** |
| --- | --- | --- | --- |
| **Claim B1. Distance-decay represents spatial impedance rather than merely geographic distance.** | Làm rõ khoảng cách trong Gravity không chỉ là độ dài hình học mà là chi phí, thời gian và trở ngại đối với tương tác. | • Tanner (1961).<br>• Wilson (1971).<br>• Tobler (1970).<br>• Hansen (1959).<br>• Lenormand et al. (2016). | Distance-decay mô tả tác động tổng hợp của spatial impedance lên xác suất tương tác. |
| **Claim B2. Different functional forms represent different hypotheses about collective distance sensitivity.** | Giải thích vì sao tồn tại nhiều hàm deterrence khác nhau thay vì chỉ một công thức. | • Exponential model.<br>• Power-law model.<br>• Tanner function.<br>• Comparative studies (Lenormand et al., Liang et al.). | Mỗi hàm distance-decay tương ứng với một giả thuyết hành vi khác nhau về cách khoảng cách ảnh hưởng đến di chuyển. |
| **Claim B3. Tanner provides a more flexible behavioural representation than classical exponential decay.** | Giải thích lý do lựa chọn Tanner trong nghiên cứu. | • Tanner (1961).<br>• Liang et al. (2013).<br>• Lenormand et al. (2016). | Tanner có khả năng mô tả đồng thời **near-distance preference** và **long-distance deterrence**, vượt ra ngoài giả định suy giảm đơn điệu đơn giản của exponential decay. |
| **Claim B4. The parameters of the distance-decay function quantify collective distance sensitivity rather than immutable human behaviour.** | Tránh diễn giải quá mức rằng tham số phản ánh "bản chất con người". | • Wilson (1971).<br>• Lenormand et al. (2016).<br>• Barbosa et al. (2018).<br>• Hansen (1959).<br>• Huff (1963). | Các tham số distance-decay phản ánh hành vi di chuyển tập thể dưới những điều kiện hạ tầng, khả năng tiếp cận và cấu trúc đô thị hiện tại, chứ không phải đặc tính cố hữu của con người. |

### Conceptual Representation

| **Purpose** | **Content** |
| --- | --- |
| **Gravity formulation**        | $T_{ij}=O_iD_jf(d_{ij};	heta)$ |
| **Focus of this module**       | Giữ nguyên $O_i$ và $D_j$, tập trung vào $f(d_{ij};	heta)$. |
| **Behavioural interpretation** | $	heta$ điều khiển mức độ nhạy cảm của tương tác đối với khoảng cách, trong bối cảnh cấu trúc đô thị đã cho. |
| **Scientific interpretation**  | Distance-decay không trực tiếp mô tả từng cá nhân mà mô tả phản ứng thống kê của toàn bộ hệ thống đối với khoảng cách. |

### Scientific Consequence

| **Component** | **Content** |
| --- | --- |
| **Scientific Conclusion** | Distance-decay function là thành phần duy nhất trong mô hình Gravity trực tiếp mô tả cách khoảng cách điều chỉnh tương tác tập thể. **Therefore, $	heta$ becomes the primary quantity of interest.** |

### Transition to Module C

| **Component** | **Content** |
| --- | --- |
| **Transition Question**     | **If θ is the key behavioural quantity, can it be identified from available data?** |
| **Motivation for Module C** | Bài báo không quan sát trực tiếp từng cặp OD mà chỉ quan sát dữ liệu tổng hợp. Vì vậy cần trả lời liệu quá trình tổng hợp có còn bảo tồn thông tin cần thiết để nhận diện distance-decay hay không. |

---

# Module C — Information Transformation through Mobility Aggregation

| **Component**                   | **Content**                                                                                                                                                                                                                                                                                        |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Module**                      | **C. Information Transformation through Mobility Aggregation**                                                                                                                                                                                                                                                         |
| **Scientific Question**         | **What information is retained when detailed mobility observations are aggregated, and can these aggregate observations potentially support behavioural parameter identification?**                                                                                                                                    |
| **Why is this module indispensable?** | Without information transformation, aggregate observations cannot justify inference. |
| **Mission**                     | Explain how mobility aggregation changes the available observations, distinguish what is directly observable from what is lost, and motivate the scientific question addressed in this study without assuming the answer.                                                                                              |
| **Established Facts**           | (1) Aggregate datasets (e.g., Trip-Length Distributions, including Meta's Movement Distribution Maps (MDM) \citep{MetaMovementDistributionMaps}) preserve overall travel-distance statistics.<br>(2) Detailed Origin–Destination interactions and individual trajectories are no longer explicitly observable after aggregation.<br>(3) Aggregation therefore changes the information available for inference. |
| **Knowledge Gap**               | It remains unknown whether the behavioural information preserved in aggregate Trip-Length Distributions is sufficient to identify the parameters governing the underlying distance-decay function.                                                                                                                     |
| **Central Scientific Question** | **Can aggregate Trip-Length Distribution observations support identification of the behavioural distance-decay parameters?**                                                                                                                                                                                           |
| **Role in the Handbook**        | This module does **not** attempt to prove that aggregation preserves sufficient information. Instead, it formulates the scientific question that motivates the probabilistic framework and empirical validation presented later.                                                                                       |
| **Connection to Module D**      | Since behavioural identifiability cannot be assumed from aggregate observations alone, a statistical inference framework is required to test whether behavioural parameters can indeed be recovered.                                                                                                                   |
| **Scientific Consequence**      | The problem shifts from **recovering missing Origin–Destination data** to **determining whether aggregate observations are informative enough for behavioural inference**.                                                                                                                                             |

### Conceptual Logic Graph

```mermaid
flowchart TD
    A[Detailed mobility observations] -->|"Mobility aggregation"| B[Aggregate observations
(Trip-Length Distribution)]
    
    B --> C["Preserve:
• distance frequencies"]
    B --> D["Lose:
• individual trajectories
• OD identities"]
    
    C --> E[Open Scientific Question]
    D --> E
    
    E -->|Can aggregate observations identify θ?| F[Probabilistic framework]
    F --> G[Empirical validation]
    
    style E fill:#fff3cd,stroke:#856404,stroke-width:2px,stroke-dasharray: 4 4
```

### Transition to Module D

| **Component** | **Content** |
| --- | --- |
| **Transition Question**     | **If this is unknown, how can we determine it scientifically?** |
| **Motivation for Module D** | Since behavioural identifiability cannot be assumed from aggregate observations alone, a statistical inference framework is required. |

---

# Module D — Inference Principle: A Probabilistic Framework

| **Component**                  | **Content**                                                                                                                                                                     |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Module Title**           | **A Probabilistic Framework for Distance-Decay Parameter Identification**                                                                                                |
| **Scientific Question**    | **How can the parameters of the distance-decay function be statistically identified from aggregate Trip-Length Distribution observations?**                                 |
| **Mission**                | Establish a probabilistic framework linking aggregate observations to the parameters of the distance-decay function without requiring complete Origin–Destination matrices. |
| **Core Principle**         | Distance-decay parameters are latent variables and must be inferred probabilistically from aggregate observations rather than directly observed.                            |
| **Inference Goal**         | Provide statistical evidence supporting identification of the parameter vector **θ** governing the distance-decay function.                                               |
| **Scientific Consequence** | The problem becomes one of statistical parameter identification instead of OD reconstruction.                                                                               |

### Supporting Claims

| **Supporting Claim** | **Purpose** | **Representative Evidence (SOTA)** | **Expected Conclusion** |
| --- | --- | --- | --- |
| **Claim D1. Parameter identification from aggregate data constitutes a probabilistic inverse problem.** | Khái niệm hóa bài toán suy luận tham số từ phân bố khoảng cách dưới góc độ bài toán nghịch đảo thống kê. | • Casella & Berger (2002).<br>• Bishop (2006). | Việc nhận diện tham số cần được giải quyết bằng khung suy luận xác suất. |
| **Claim D2. Classical aggregate calibration methods demonstrate early precedent but lack general probabilistic formulations.** | Nhìn lại các phương pháp calibration vĩ mô cổ điển. | • Tanner (1961).<br>• Hyman (1969).<br>• Merlin (2020). | Lịch sử đã sử dụng dữ liệu tổng hợp cho calibration nhưng chưa tổng quát hóa thành bài toán nhận diện tham số tường minh. |
| **Claim D3. Modern statistical inference provides tools to derive likelihood functions directly in aggregate observation spaces.** | Kết nối với lý thuyết thống kê hiện đại. | • Flowerdew & Aitkin (1982).<br>• Ortúzar & Willumsen (2011). | Có thể xây dựng likelihood trực tiếp trên quan sát TLD. |

### Conceptual Framework

```mermaid
flowchart TD
    A[Aggregate observations] --> B[Need statistical inference]
    B --> C[Need likelihood]
    C --> D[Need estimation]
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#d4edda,stroke:#28a745,stroke-width:2px
```

### Transition to Module E

| **Component** | **Content** |
| --- | --- |
| **Transition Question**     | **What probabilistic model do we actually use?** |
| **Motivation for Module E** | Module D establishes *why* we need probabilistic inference. Module E must mathematically specify *how* this is implemented (Gravity equation, Observation model, Likelihood). |

---

# Module E — Mathematical Framework: Gravity-based Statistical Identification

| **Component**                  | **Content**                                                                                                                     |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Module Title**           | **Gravity-based Statistical Identification Framework**                                                                   |
| **Scientific Question**    | **How is the probabilistic identification framework implemented for distance-decay parameter estimation?**                  |
| **Mission**                | Specify the probabilistic model that links the latent distance-decay parameters to the observed Trip-Length Distribution.   |
| **Core Assumption**        | Mobility follows a gravity process in which the distance-decay function is governed by parameter vector θ.                  |
| **Observation Model**      | The observed Trip-Length Distribution is regarded as a probabilistic observation generated by the underlying gravity model. |
| **Likelihood Formulation** | Derive the likelihood of observing the aggregate Trip-Length Distribution conditional on θ.                                 |
| **Estimator**              | Estimate θ by maximizing the likelihood (or minimizing the equivalent negative log-likelihood).                             |
| **Output**                 | Estimated distance-decay parameters together with the predicted Trip-Length Distribution.                                   |
| **Scientific Consequence** | The conceptual inference principle is now realized as a fully specified mathematical framework ready for empirical testing. |

### Supporting Claims

| **Supporting Claim** | **Purpose** | **Representative Evidence (SOTA)** | **Expected Conclusion** |
| --- | --- | --- | --- |
| **Claim E1. The observation model maps latent Gravity interaction probabilities into expected distance bin frequencies.** | Xây dựng hàm chiếu từ không gian Gravity sang không gian quan sát TLD. | • Wilson (1971).<br>• Lenormand et al. (2016). | Cho phép tính toán phân bố khoảng cách lý thuyết dựa trên $\theta$ và cấu trúc đô thị. |
| **Claim E2. Maximum Likelihood Estimation provides a consistent statistical basis for parameter recovery.** | Xác định phương pháp ước lượng tham số từ likelihood thu được. | • Flowerdew & Aitkin (1982).<br>• Casella & Berger (2002). | Việc tối đa hóa likelihood thu được tham số $\hat{\theta}$ tối ưu tương thích với quan sát TLD. |

### Logic Graph

```mermaid
flowchart TD
    A[Latent θ] --> B[Gravity model]
    B --> C[Predicted TLD]
    C --> D[Likelihood]
    D --> E[Estimate θ]
    
    style A fill:#fff3cd,stroke:#856404,stroke-width:2px
    style E fill:#d4edda,stroke:#28a745,stroke-width:2px
```

### Transition to Module F

| **Component** | **Content** |
| --- | --- |
| **Transition Question**     | **Does empirical evidence support the hypothesis?** |
| **Motivation for Module F** | Evaluate whether the identified parameters accurately reproduce empirical mobility patterns across cities, thus answering the central scientific question posed in Module C. |

---

# Module F — Scientific Evidence: Empirical Evaluation of the Identification Hypothesis

| **Component**                  | **Content**                                                                                                                     |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Module Title**           | **Empirical Evaluation of the Identification Hypothesis**                                                                   |
| **Scientific Question**    | **Do aggregate Trip-Length Distribution observations contain sufficient empirical evidence to identify the parameters of the distance-decay function?**                  |
| **Mission**                | Empirically evaluate the central scientific hypothesis proposed in Module C using the probabilistic framework developed in Modules D and E.   |
| **Inheritance**            | Module F closes the loop. It inherits the entire logical chain from A to E to answer the foundational scientific question.                  |
| **Scientific Consequence (If Supported)** | The empirical evidence supports the hypothesis that aggregate Trip-Length Distribution observations retain sufficient information for identifying distance-decay parameters. |
| **Scientific Consequence (If Rejected)**  | The empirical evidence suggests that aggregate Trip-Length Distribution observations alone are insufficient for reliable parameter identification. |

### Supporting Claims

| **Supporting Claim** | **Purpose** | **Representative Evidence (SOTA)** | **Expected Conclusion** |
| --- | --- | --- | --- |
| **Claim F1. Synthetic recovery experiments provide evidence of numerical stability and parameter identifiability.** | Đánh giá khả năng khôi phục tham số trong điều kiện kiểm soát (synthetic setup). | • Controlled synthetic experiments (Paper). | Tham số gốc có thể khôi phục chính xác từ TLD sinh ra bởi mô hình. |
| **Claim F2. Cross-city empirical application indicates consistent parameter estimation across diverse urban structures.** | Kiểm chứng thực nghiệm trên nhiều đô thị thực tế. | • Meta Movement Distribution Maps \citep{MetaMovementDistributionMaps}.<br>• Real-world validation (Paper). | Khung suy luận hoạt động ổn định trên dữ liệu tổng hợp đô thị thực tế. |
| **Claim F3. Downstream validation of reconstructed flows provides proxy support for the inferred behavioural parameters.** | Sử dụng OD reconstruction làm bài kiểm tra kiểm chứng downstream (không phải bằng chứng toán học độc lập). | • Empirical validation across benchmark cities (Paper). | OD được tái tạo từ $\hat{\theta}$ đạt độ tương thích cao với dòng di chuyển thực tế. |

### Closing the Loop

Module F is not merely a model validation step; it is the **empirical evaluation of a scientific hypothesis**. 
It evaluates the overarching claim that behaviour is preserved and identifiable from aggregate signatures. 
Regardless of the outcome (supported or rejected), the finding constitutes a rigorous scientific conclusion, establishing a definitive answer to the question formulated in Module C.

---

# References

## I. Spatial Interaction Foundations

| Ref ID | Reference | Year | BibTeX key | Hỗ trợ Module | Vai trò |
| ------ | --------- | ---- | ---------- | ------------- | ------- |
| R1 | Zipf, G.K. *The $P_1P_2/D$ Hypothesis: On the Intercity Movement of Persons*, Am. Sociol. Rev. 11(6) | 1946 | `zipf1946` | A | Early sociological formalization of the gravity analogy |
| R2 | Wilson, A.G. *A Family of Spatial Interaction Models, and Associated Developments*, Env. Plan. A | 1971 | `wilson1971` | A, B, E | Entropy derivation, Gravity foundation |
| R3 | Tobler, W. *A Computer Movie Simulating Urban Growth in the Detroit Region*, Econ. Geogr. | 1970 | `tobler1970computer` | B | Source of the "First Law of Geography"; distance-decay principle |
| R4 | Haynes & Fotheringham. *Gravity and Spatial Interaction Models*, Sage | 1984 | `haynes1984gravity` | A, B | Textbook kinh điển |
| R5 | Fotheringham & O'Kelly. *Spatial Interaction Models: Formulations and Applications*, Kluwer | 1989 | `fotheringham1989spatial` | A, B | Spatial interaction theory |
| R6 | Hansen, W. *How Accessibility Shapes Land Use*, JAIP 25(2) | 1959 | `hansen1959accessibility` | B | Accessibility & distance decay |
| R8 | Sen & Smith. *Gravity Models of Spatial Interaction Behavior*, Springer | 1995 | `sen1995gravity` | B | Statistical theory of gravity model estimation |

---

## II. Human Mobility Foundations

| Ref ID | Reference | Year | BibTeX key | Hỗ trợ Module | Vai trò |
| ------ | --------- | ---- | ---------- | ------------- | ------- |
| R7 | Barbosa et al. *Human Mobility: Models and Applications* | 2018 | `barbosa2018human` | A, B, C | Review lớn nhất về Human Mobility |
| R9 | González et al. *Understanding Individual Human Mobility Patterns* | 2008 | `gonzalez2008understanding` | C | Individual mobility regularities surviving aggregation |
| R10 | Song et al. *Limits of Predictability in Human Mobility* | 2010 | `song2010limits` | C | Human mobility predictability & entropy |
| R32 | Pappalardo et al. *Future Directions in Human Mobility Science* | 2023 | `pappalardo2023analytical` | C | Agenda review; framing of mobility data |
| R33 | Gallotti et al. *Distorted Insights from Human Mobility Data* | 2024 | `gallotti2024distorted` | C, F | Representation choice changes inference |

---

## III. Distance-Decay & Aggregate Calibration

| Ref ID | Reference | Year | BibTeX key | Hỗ trợ Module | Vai trò |
| ------ | --------- | ---- | ---------- | ------------- | ------- |
| R11 | Simini et al. *A Universal Model for Mobility and Migration Patterns* | 2012 | `Simini2012universal` | B | Radiation Model |
| R12 | Stouffer. *Intervening Opportunities: A Theory Relating Mobility and Distance* | 1940 | `stouffer1940intervening` | B | Alternative behavioural mechanism |
| R13 | Huff. *A Probabilistic Analysis of Shopping Center Trade Areas*, Land Econ. 39(1) | 1963 | `huff1963probabilistic` | B | Huff Model |
| R14 | Ortúzar & Willumsen. *Modelling Transport*, 4th ed. | 2011 | `ortuzar2011modelling` | D, E | Behaviour calibration |
| R29 | Lenormand et al. *Systematic Comparison of Trip Distribution Laws and Models* | 2016 | `lenormand2016systematic` | A, B, E | Systematic comparison of trip distribution laws |
| R36 | Tanner, J.C. *Factors Affecting the Amount of Travel*, RRL Tech. Paper 51 | 1961 | `tanner1961` | B, D | Deterrence function & trip-length calibration |
| R37 | Hyman, G.M. *The Calibration of Trip Distribution Models*, Env. Plan. A | 1969 | `hyman1969calibration` | D | Classical mean-trip-length calibration |
| R38 | Merlin, L.A. *A New Method Using Medians to Calibrate Single-Parameter Spatial Interaction Models* | 2020 | `merlin2020medians` | D | Calibration from summary statistics |
| R48 | Liang et al. *Unraveling the Origin of Exponential Law in Intra-Urban Human Mobility* | 2013 | `liang2013unraveling` | B | Distance decay functional forms |

---

## IV. Statistical Inference & Data Products

| Ref ID | Reference | Year | BibTeX key | Hỗ trợ Module | Vai trò |
| ------ | --------- | ---- | ---------- | ------------- | ------- |
| R18 | Casella & Berger. *Statistical Inference*, 2nd ed. | 2002 | `casella2002statistical` | D, E | Classical statistical inference & inverse problems |
| R20 | Meta. *Movement Distribution Maps* (AI for Good) | 2026 | `MetaMovementDistributionMaps` | C, F | Privacy-preserving aggregate travel-distance dataset |
| R30 | Flowerdew & Aitkin. *A Method of Fitting the Gravity Model Based on the Poisson Distribution* | 1982 | `flowerdew1982method` | A, D, E | Poisson MLE gravity fitting |

---

## V. Deep Learning & Transfer Baselines

| Ref ID | Reference | Year | BibTeX key | Hỗ trợ Module | Vai trò |
| ------ | --------- | ---- | ---------- | ------------- | ------- |
| R25 | Simini et al. *A Deep Gravity Model for Mobility Flows Generation* | 2021 | `simini2021` | A | Deep Learning gravity baseline |
| R27 | Yang et al. *Transferable Human Mobility Network Reconstruction with neuroGravity* | 2026 | `neurogravity2026` | A | Physics-informed neural gravity |
| R31 | Enaya et al. *TransGM: Transferable Gravity Models for Cross-City Policy Transfer* | 2026 | `transgm2026` | A | Cross-city transferable gravity model |
