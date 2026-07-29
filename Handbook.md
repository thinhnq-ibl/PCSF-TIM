# Theoretical Background and Methodological Blueprint

## Scientific Thesis

> **This handbook develops the scientific argument that behavioural parameters governing collective distance sensitivity may be identifiable from observed Trip-Length Distributions because mobility aggregation preserves behaviour-relevant statistical information that can be interpreted within the Gravity framework.**

*This Handbook serves as the theoretical justification for the manuscript. It is structured as a scientific proof: each module poses a core scientific question, answers it with a central claim, and supports that claim through a series of evidence-backed arguments. This rigorous progression establishes the necessity and validity of inferring distance-decay parameters from observed Trip-Length Distributions.*

---

### Master Strategic Notes (Core Conceptual Positioning)

> [!NOTE]
> **Key Strategic Positioning for Manuscript Drafting:**
> 0. **Model–Observation Compatibility Principle:** When the observation space is restricted to aggregate TLD $\mathbf{y} = (y_1, \dots, y_K)$, inference relies on explaining the full distribution shape. The parametric decay model must match the observation space shape requirements (e.g., Tanner provides dual parameters: $\alpha$ for short-to-intermediate shape and $\beta$ for long-range decay).
> 1. **Terminology Standard:** Standardized on **observed Trip-Length Distribution (observed TLD)** to anchor the observation space to empirical binned histograms $y = (y_1, \dots, y_K)$.
> 2. **Enduring Value of Physics-Based Models:** Contemporary deep learning frameworks (Deep Gravity \citep{simini2021}, neuroGravity \citep{neurogravity2026}, TransGM \citep{transgm2026}) extend rather than replace Gravity. Gravity provides the indispensable structural inductive bias ($O_i, D_j$ vs. $f(d_{ij};\theta)$) required for interpretability and cross-city generalization.
> 3. **Factorization Principle (Lenormand et al. 2016):** Demographic/economic opportunity distributions ($O_i, D_j$) and spatial impedance decay ($f(d_{ij};\theta)$) are interacting yet mathematically independent components, allowing behavioural sensitivity $\theta$ to be isolated from local structural density.
> 4. **Novelty Positioning (Lenormand 2016 vs. PCSF-TIM):** Landmark mobility studies use TLD as a downstream evaluative benchmark metric (CPC / Sørensen index) for models calibrated on OD matrices. In contrast, **PCSF-TIM shifts TLD from an evaluation target to the primary probabilistic observation space**, enabling direct parameter identification without requiring local OD flow supervision.

---

# Human Mobility Handbook V4.0 (Frozen Architecture)

| Module | Scientific Question | Scientific Answer | Leads to... |
| :--- | :--- | :--- | :--- |
| **A. Gravity as the Scientific Foundation** | **Why is Gravity an appropriate scientific framework for human mobility?** | Human mobility can be represented as spatial interactions between origins and destinations, with movement constrained by travel impedance. Gravity provides a principled mathematical description of this process. | If Gravity is the framework, **what governs travel impedance?** |
| **B. Distance-Decay as the Behavioural Mechanism** | **Why is distance-decay the central behavioural mechanism in Gravity models?** | Distance-decay determines how interaction probability decreases with distance and therefore governs collective distance sensitivity. The parameters of the distance-decay function become the primary quantities of scientific interest. | If θ is the key behavioural quantity, **can it be identified from available data?** |
| **C. Information Transformation through Mobility Aggregation** | **What information remains after mobility observations are aggregated?** | Aggregate datasets (e.g., Trip-Length Distributions) preserve overall travel-distance statistics but no longer explicitly record Origin–Destination interactions. Whether these aggregate observations contain sufficient information to identify the distance-decay parameters remains an open scientific question. | If this is unknown, **how can we determine it scientifically?** |
| **D. Inference Principle: A Probabilistic Framework** | **How can the parameters of the distance-decay function be statistically identified from observed Trip-Length Distributions?** | Treat parameter identification as a probabilistic inverse problem. Construct an observation model linking the latent distance-decay parameters to the observed Trip-Length Distribution, then estimate θ using statistical inference. | This framework is then implemented and validated in the proposed method. |
| **E. Mathematical Framework: Gravity-based Statistical Identification** | **How is the probabilistic identification framework implemented for distance-decay parameter estimation?** | Specify the probabilistic model (Gravity + Observation Model + Likelihood) that links the latent parameters to the observed distribution. | **Does empirical evidence support the hypothesis?** |
| **F. Empirical Evaluation of the Identification Hypothesis** | **Do observed Trip-Length Distributions contain sufficient empirical evidence to identify the parameters of the distance-decay function?** | Empirically evaluate the central scientific hypothesis using the probabilistic framework to see if it reproduces mobility patterns. | **Scientific Conclusion.** |

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
| **Central Claim**          | **Gravity remains the canonical scientific framework for aggregate spatial interaction because it explicitly separates urban structure from behavioural distance sensitivity, thereby facilitating the explicit identification and transfer of distance sensitivity across urban contexts.** |

### Supporting Claims

| **Supporting Claim** | **Purpose** | **Representative Evidence (SOTA)** | **Expected Conclusion** |
| --- | --- | --- | --- |
| **Claim A1. Gravity has evolved from an empirical analogy into the canonical mathematical representation of spatial interaction.** | Chứng minh Gravity không chỉ là mô hình lịch sử mà đã trở thành nền tảng lý thuyết của spatial interaction. | • Zipf (1946): Gravity analogy.<br>• Wilson (1971): Entropy-maximizing derivation.<br>• Flowerdew & Aitkin (1982): Statistical estimation (Poisson framework).<br>• Haynes & Fotheringham (1984): Classical spatial interaction modelling.<br>• Barbosa et al. (2018): Physics Reports review. | Gravity cung cấp cơ sở lý thuyết và toán học chuẩn mực để mô hình hóa tương tác không gian vĩ mô. |
| **Claim A2. Modern mobility models extend rather than replace the Gravity paradigm.** | Trả lời phản biện rằng Deep Learning đã thay thế Gravity. | • Deep Gravity (Simini et al., 2021).<br>• neuroGravity (Yang et al., 2026).<br>• TransGM (Enaya et al., 2026).<br>• Universal Geography Neural Network (Guo et al., 2025).<br>• Imagery2Flow (Xu et al., 2025). | AI và Deep Learning chủ yếu tăng cường khả năng biểu diễn hoặc học các thành phần của Gravity chứ không thay thế cấu trúc khoa học của nó. |
| **Claim A3. Gravity explicitly separates urban structure from spatial interaction behaviour.** | Thiết lập decomposition sẽ được dùng xuyên suốt Handbook và bài báo. | • Wilson (1971).<br>• Lenormand et al. (2016).<br>• Comparative studies of gravity models. | Gravity phân tách rõ **Urban Structure** ($O_i$, $D_j$) khỏi **Behaviour** ($f(d_{ij};\theta)$). |
| **Claim A4. The distance-decay function is the unique component that explicitly represents spatial impedance.** | Cô lập đúng đối tượng nghiên cứu của bài báo. | • Tanner (1961).<br>• Liang et al. (2013).<br>• Lenormand et al. (2016). | Trong toàn bộ mô hình Gravity, chỉ **distance-decay function** trực tiếp mô tả ảnh hưởng của khoảng cách lên xác suất tương tác. |
| **Claim A5. Explicit identification of distance sensitivity facilitates its transferability across urban contexts.** | Bổ sung cầu nối logic từ Module A sang Module E — giải quyết câu hỏi tại sao identification là prerequisite. | • Theoretical reasoning grounded in A3 & A4.<br>• TransGM (Enaya et al., 2026).<br>• Similarity-based City Transfer (Wang et al., 2025). | Việc nhận diện $\theta$ một cách tường minh tạo cơ sở lý thuyết cho việc chuyển giao độ nhạy cảm khoảng cách sang các ngữ cảnh đô thị khác mà không cần dữ liệu OD địa phương. |

### Core Mathematical Representation

| **Purpose** | **Content** |
| --- | --- |
| **Scientific Formulation**    | $T_{ij}=O_iD_jf(d_{ij};\theta)$ |
| **Urban Structure**           | $O_i$: Origin emission (trip production).<br>$D_j$: Destination attraction (trip attraction). |
| **Behavioural Component**     | $f(d_{ij};\theta)$: Distance-decay function describing collective distance sensitivity. |
| **Scientific Interpretation** | Aggregate mobility can be viewed as the interaction between urban opportunities ($O_i,D_j$) and behavioural responses to travel distance ($f(d_{ij};\theta)$). Behaviour is only transferable once $\theta$ has been independently identified. |

### Deep Dive: Theoretical Evolution of Gravity (Claim A1 & A2)

> The Gravity model originated as an empirical analogy adapting Newton's law of gravitation to spatial-sociological interactions \citep{zipf1946}. It was subsequently established on a rigorous theoretical foundation within spatial interaction modelling through the entropy-maximizing principle \citep{wilson1971}. This theoretical grounding was further solidified as Gravity was integrated into formal statistical inference frameworks, defining spatial flows $T_{ij}$ as probabilistic random variables \citep{flowerdew1982method, haynes1984gravity}. Comprehensive modern surveys \citep{barbosa2018human} confirm that Gravity remains the canonical paradigm for collective mobility.

> A common misconception in contemporary mobility science is that deep learning architectures have rendered physical spatial interaction models obsolete. In reality, pure black-box machine learning approaches often struggle with output interpretability and cross-city transferability due to spatial non-stationarity. State-of-the-art models overcome these limitations not by replacing Gravity, but by extending it. Frameworks such as Deep Gravity \citep{simini2021} leverage neural networks to learn complex, non-linear representations of urban opportunities from high-dimensional open data (e.g., POIs, satellite imagery), while strictly preserving the multiplicative spatial interaction structure of Gravity. Furthermore, physics-informed architectures like neuroGravity \citep{neurogravity2026} and TransGM \citep{transgm2026} explicitly embed the gravity-based separation of urban structure and behavioural distance decay into their neural layers.

> This hybrid paradigm demonstrates that Gravity provides the indispensable structural inductive bias required for deep learning models to achieve both superior predictive realism and robust cross-context generalization. Ultimately, this confirms that physics-based spatial interaction models retain their foundational scientific value: far from being superseded, physical principles remain the indispensable cornerstone for building explainable, robust, and transferable mobility models.

### Deep Dive: Structural-Behavioural Factorization (Claim A3)

> At its theoretical core, the Gravity framework achieves a fundamental mathematical factorization: it explicitly decouples urban spatial structure from spatial interaction behaviour \citep{wilson1971, lenormand2016systematic}. In the canonical formulation $T_{ij} = O_i D_j f(d_{ij};\theta)$, demographic and economic opportunity distributions ($O_i, D_j$) and spatial impedance decay ($f(d_{ij};\theta)$) constitute two interacting yet mathematically independent components \citep{lenormand2016systematic}. The origin emission $O_i$ and destination attraction $D_j$ encode the spatial distribution of opportunities governed by land-use geometry and built-environment configurations, whereas the distance-decay function $f(d_{ij};\theta)$ isolates the collective human behavioural response to spatial impedance. This explicit factorization is scientifically indispensable because it disentangles structural opportunity density from intrinsic travel preferences; observed differences in travel lengths across cities may reflect variations in spatial opportunity layout rather than shifts in underlying behavioural sensitivity. By isolating $\theta$ from local structural constraints, the Gravity decomposition provides the prerequisite framework for identifying transferable behavioural parameters across heterogeneous urban systems.

### Deep Dive: Unique Functional Role of Distance-Decay (Claim A4)

> Within the functional architecture of Gravity models, the distance-decay function $f(d_{ij};\theta)$ serves as the unique component explicitly encoding spatial impedance—capturing how spatial separation diminishes interaction probability independently of origin emission capacity $O_i$ or destination attraction scale $D_j$ \citep{tanner1961, lenormand2016systematic}. While $O_i$ and $D_j$ quantify the spatial distribution of urban opportunities, $f(d_{ij};\theta)$ is the sole structural component designed to represent the travel friction imposed by distance. Consequently, because $f(d_{ij};\theta)$ exclusively isolates collective distance sensitivity from urban spatial opportunities, its governing parameter vector $\theta$ constitutes the primary behavioural object of scientific interest for identification.

### Deep Dive: Identification as a Prerequisite for Behavioural Transferability (Claim A5)

> Formally identifying the distance-decay parameter vector $\theta$ is a theoretical prerequisite for transferable mobility modelling and scalable cross-city flow prediction \citep{transgm2026}. If behavioural distance sensitivity remains entangled with local urban features or embedded implicitly within black-box neural weights, deploying the model to a new urban context necessitates complete local recalibration using supervised Origin–Destination flow matrices. This requirement severely limits model scalability, particularly in data-scarce urban environments or forward-looking policy scenarios where local OD flows are unavailable. Conversely, when $\theta$ is explicitly identified independently of origin-destination structural density ($O_i, D_j$), the inferred behavioural parameter can be directly transferred across heterogeneous urban systems—requiring only open spatial structure data (e.g., POI distributions, land-use geometry) at the target city to reconstruct mobility flows \citep{wang2025similarity}.

> [!NOTE]
> **Ý nghĩa cốt lõi của Claim A5:** Nhận diện tường minh $\theta$ là cầu nối duy nhất giúp mô hình di chuyển có thể mở rộng quy mô (scalable) sang các đô thị thiếu dữ liệu OD matrix. Khi $\theta$ được tách rời khỏi cấu trúc đô thị địa phương, việc chuyển giao mô hình di chuyển sang một đô thị mới chỉ đòi hỏi dữ liệu không gian mở (POIs, land-use) tại đô thị đích.

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
| **Gravity formulation**        | $T_{ij}=O_iD_jf(d_{ij};\theta)$ |
| **Focus of this module**       | Giữ nguyên $O_i$ và $D_j$, tập trung vào $f(d_{ij};\theta)$. |
| **Behavioural interpretation** | $\theta$ điều khiển mức độ nhạy cảm của tương tác đối với khoảng cách, trong bối cảnh cấu trúc đô thị đã cho. |
| **Scientific interpretation**  | Distance-decay không trực tiếp mô tả từng cá nhân mà mô tả phản ứng thống kê của toàn bộ hệ thống đối với khoảng cách. |

### Deep Dive: Theoretical Evolution of Gravity (Claim A1 & A2)

> The Gravity model originated as an empirical analogy adapting Newton's law of gravitation to spatial-sociological interactions \citep{zipf1946}. It was subsequently established on a rigorous theoretical foundation within spatial interaction modelling through the entropy-maximizing principle \citep{wilson1971}. This theoretical grounding was further solidified as Gravity was integrated into formal statistical inference frameworks, defining spatial flows $T_{ij}$ as probabilistic random variables \citep{flowerdew1982method, haynes1984gravity}. Comprehensive modern surveys \citep{barbosa2018human} confirm that Gravity remains the canonical paradigm for collective mobility. Crucially, the emergence of modern deep learning models does not replace this established paradigm; instead, state-of-the-art architectures extend the Gravity framework by embedding its physics-informed decomposition into neural networks, enhancing both predictive accuracy and behavioural interpretability. Ultimately, this confirms that physics-based spatial interaction models retain their foundational scientific value: far from being superseded, physical principles remain the indispensable cornerstone for building explainable, robust, and transferable mobility models \citep{simini2021, neurogravity2026, transgm2026}.

### Deep Dive: Structural-Behavioural Factorization (Claim A3)

> At its theoretical core, the Gravity framework achieves a fundamental mathematical factorization: it explicitly decouples urban spatial structure from spatial interaction behaviour \citep{wilson1971, lenormand2016systematic}. In the canonical formulation $T_{ij} = O_i D_j f(d_{ij};\theta)$, demographic and economic opportunity distributions ($O_i, D_j$) and spatial impedance decay ($f(d_{ij};\theta)$) constitute two interacting yet mathematically independent components \citep{lenormand2016systematic}. The origin emission $O_i$ and destination attraction $D_j$ encode the spatial distribution of opportunities governed by land-use geometry and built-environment configurations, whereas the distance-decay function $f(d_{ij};\theta)$ isolates the collective human behavioural response to spatial impedance. This explicit factorization is scientifically indispensable because it disentangles structural opportunity density from intrinsic travel preferences; observed differences in travel lengths across cities may reflect variations in spatial opportunity layout rather than shifts in underlying behavioural sensitivity. By isolating $\theta$ from local structural constraints, the Gravity decomposition provides the prerequisite framework for identifying transferable behavioural parameters across heterogeneous urban systems.

### Deep Dive: Uniqueness and Behavioural Richness of Distance-Decay (Claim A4)

> Within the functional architecture of Gravity models, the distance-decay function $f(d_{ij};\theta)$ serves as the unique component explicitly encoding spatial impedance—capturing how spatial separation diminishes the probability of interaction independently of origin emission capacity or destination opportunity scale \citep{tanner1961, lenormand2016systematic}. While simple functional forms such as exponential ($e^{-\beta d}$) or power-law ($d^{-\alpha}$) decay impose rigid behavioural assumptions, the Tanner deterrence function $f(d;\alpha, \beta) = d^{-\alpha} e^{-\beta d}$ provides a structurally rich behavioural representation \citep{liang2013unraveling}. Specifically, the power-law component $d^{-\alpha}$ models short-to-intermediate distance travel preferences, while the exponential term $e^{-\beta d}$ governs long-distance spatial deterrence. Because $f(d_{ij};\theta)$ is the sole model component representing spatial friction, the parameter vector $\theta = (\alpha, \beta)$ constitutes the primary behavioural object of scientific interest for identification.

### Deep Dive: Identification as a Prerequisite for Behavioural Transferability (Claim A5)

> Formally identifying the distance-decay parameter vector $\theta$ is a theoretical prerequisite for transferable mobility modelling and scalable cross-city flow prediction \citep{transgm2026}. If behavioural distance sensitivity remains entangled with local urban features or embedded implicitly within black-box neural weights, deploying the model to a new urban context necessitates complete local recalibration using supervised Origin–Destination flow matrices. This requirement severely limits model scalability, particularly in data-scarce urban environments or forward-looking policy scenarios where local OD flows are unavailable. Conversely, when $\theta$ is explicitly identified independently of origin-destination structural density ($O_i, D_j$), the inferred behavioural parameter can be directly transferred across heterogeneous urban systems—requiring only open spatial structure data (e.g., POI distributions, land-use geometry) at the target city to reconstruct mobility flows \citep{wang2025similarity}.

> [!NOTE]
> **Ý nghĩa cốt lõi của Claim A5:** Nhận diện tường minh $\theta$ là cầu nối duy nhất giúp mô hình di chuyển có thể mở rộng quy mô (scalable) sang các đô thị thiếu dữ liệu OD matrix. Khi $\theta$ được tách rời khỏi cấu trúc đô thị địa phương, việc chuyển giao mô hình di chuyển sang một đô thị mới chỉ đòi hỏi dữ liệu không gian mở (POIs, land-use) tại đô thị đích.

### Scientific Consequence

| **Component** | **Content** |
| --- | --- |
| **Scientific Conclusion** | Distance-decay function là thành phần duy nhất trong mô hình Gravity trực tiếp mô tả cách khoảng cách điều chỉnh tương tác tập thể. **Therefore, $\theta$ becomes the primary quantity of interest.** |

### Deep Dive: Model–Observation Compatibility & Tanner Flexibility (Claim B3)

> Because the available observation consists only of the aggregate trip-length distribution $\mathbf{y} = (y_1, y_2, \dots, y_K)$, detailed Origin–Destination identities and network topology are unobservable. The primary statistical information preserved in this aggregate space is the geometric shape of the distance distribution. Consequently, parameter identification relies on the ability of the distance-decay function to explain the entire observed distributional shape rather than individual pairwise interactions. 

> Simple functional forms impose constrained shape assumptions: the exponential model ($e^{-\beta d}$) controls only the long-range decay rate, while the power-law model ($d^{-\alpha}$) governs proportional scaling. In contrast, the Tanner function $f(d; \alpha, \beta) = d^{-\alpha} e^{-\beta d}$ provides two independent parameters: $\alpha$ modulates short-to-intermediate distance shape dynamics, and $\beta$ controls long-range exponential attenuation \citep{ortuzar2011modelling}. Under the principle of **Model–Observation Compatibility**, because the observation space is reduced to the distributional shape of TLD, the distance-decay model must possess sufficient functional flexibility to explain both short-range and long-range decay characteristics within a single parametric formulation.

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
| **Central Scientific Question** | **Can observed Trip-Length Distributions support identification of the behavioural distance-decay parameters?**                                                                                                                                                                                           |
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
| **Scientific Question**    | **How can the parameters of the distance-decay function be statistically identified from observed Trip-Length Distributions?**                                 |
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

### Deep Dive: Evaluative Benchmarking vs. Inference-Space Paradigm (Lenormand 2016 vs. PCSF-TIM)

> Previous landmark studies \citep{lenormand2016systematic, simini2012universal} have established Trip-Length Distributions (TLD) as the gold standard for evaluative model benchmarking using quantitative goodness-of-fit metrics like the Sørensen-Dice index (Common Part of Commuters - CPC). However, existing literature treats TLD primarily as a downstream evaluation target for models calibrated on full Origin–Destination flow matrices. In contrast, our framework shifts TLD from an evaluative output metric to the primary probabilistic observation space, enabling direct behavioural parameter identification ($\hat{\theta}$) without requiring local OD flow supervision.

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

### Comparative Mathematical Analysis: PCSF-TIM vs. State-of-the-Art Paradigms

| Tiêu chí | **Deep Gravity** (Simini 2021) | **neuroGravity** (Yang 2026) | **TransGM** (Enaya 2026) | **Bài báo này (PCSF-TIM)** |
| :--- | :--- | :--- | :--- | :--- |
| **Công thức tổng quát** | $P(i \to j) = \text{Softmax}\big(\text{MLP}(\mathbf{x}_i, \mathbf{x}_j, d_{ij})\big)$ | $T_{ij} = \text{NN}_O(\mathbf{x}_i) \cdot \text{NN}_D(\mathbf{x}_j) \cdot f(d_{ij}; \theta)$ | $T_{ij}^{(c)} = O_i D_j f(d_{ij}; \theta^{(c)})$ với $\theta^{(c)} = \text{MetaNet}(\mathbf{Z}^{(c)})$ | $P(k \mid \theta) = \sum_{(i,j) \in \text{Bin}_k} \frac{O_i D_j f(d_{ij}; \theta)}{\sum_{m,n} O_m D_n f(d_{mn}; \theta)}$ |
| **Observation Space** | **OD Matrix space:** $T_{ij}^{obs}$ | **OD Matrix space:** $T_{ij}^{obs}$ | **OD Matrix space:** $T_{ij}^{obs}$ | **Distance Bin space (TLD):** $\mathbf{y}_{TLD} = (y_1, \dots, y_K)$ |
| **Xử lý tham số $\theta$** | Trộn lẫn trong trọng số $W_{MLP}$ (**Black-box**) | Sinh ra từ Mạng nơ-ron đồ thị (PINN) | Nhận diện qua Meta-Learning / Domain Adaptation | **Tách biệt tường minh (Explicit):** $\theta = (\alpha, \beta)$ dạng closed-form |
| **Hàm Likelihood** | $\mathcal{L} = \text{Cross-Entropy}(T_{ij}^{obs}, \hat{T}_{ij})$ | $\mathcal{L} = \text{MSE}(T_{ij}^{obs}, \hat{T}_{ij}) + \lambda \mathcal{L}_{physics}$ | $\mathcal{L} = \text{Domain Loss} + \text{Flow Loss}(T_{ij}^{obs})$ | $\mathcal{L}(\theta \mid \mathbf{y}_{TLD}) = \sum_{k=1}^K y_k \ln P(k \mid \theta)$ |
| **Nguồn dữ liệu giám sát** | **Supervised by Local OD Matrix** | **Supervised by Local OD Matrix** | **Supervised by Source OD Matrix** | **Unsupervised by OD Matrix** (Chỉ cần observed TLD) |

#### Mathematical Breakdown & Strategic Contribution

1. **Deep Gravity (Simini et al., 2021):** Biến $O_i, D_j$ thành vector đặc trưng đa chiều $\mathbf{x}_i, \mathbf{x}_j$ và dùng mạng đa lớp MLP thay cho $f(d_{ij})$. Dù tăng độ chính xác dự báo, $\theta$ bị chôn sống trong trọng số mạng nơ-ron, mất tính giải thích và bắt buộc phải có OD matrix địa phương $T_{ij}^{obs}$ để huấn luyện.
2. **neuroGravity (Yang et al., 2026):** Dùng mạng GNN để tự động học $O_i, D_j$ và $\theta$ dưới các ràng buộc vật lý bảo toàn dòng. Tuy nhiên, hàm Loss chính vẫn phải tính trên sai số OD matrix thực tế $T_{ij}^{obs}$. Nếu thiếu OD matrix địa phương, GNN không thể lan truyền ngược (backpropagation).
3. **TransGM (Enaya et al., 2026):** Dùng Meta-Learning để học hàm mapping từ đặc trưng đô thị $\mathbf{Z}^{(c)}$ sang $\theta^{(c)}$. TransGM giải quyết bài toán transfer nhưng vẫn cần OD matrix tại đô thị nguồn (source city) và nhạy cảm với sự chênh lệch văn hóa di chuyển giữa các đô thị (domain shift).
4. **PCSF-TIM (This Paper):** Chuyển dịch bài toán suy luận từ **OD Space** sang **Distance Bin Space (TLD)** thông qua Phép chiếu Xác suất (Probabilistic Forward Operator). Bằng cách giải bài toán **Probabilistic Inverse Problem** trực tiếp trên không gian TLD quan sát được, mô hình nhận diện tham số $\theta$ một cách tường minh mà **không cần bất kỳ sự giám sát nào từ dữ liệu OD matrix địa phương**.

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
| **Scientific Question**    | **Do observed Trip-Length Distributions contain sufficient empirical evidence to identify the parameters of the distance-decay function?**                  |
| **Mission**                | Empirically evaluate the central scientific hypothesis proposed in Module C using the probabilistic framework developed in Modules D and E.   |
| **Inheritance**            | Module F closes the loop. It inherits the entire logical chain from A to E to answer the foundational scientific question.                  |
| **Scientific Consequence (If Supported)** | The empirical evidence supports the hypothesis that observed Trip-Length Distributions retain sufficient information for identifying distance-decay parameters. |
| **Scientific Consequence (If Rejected)**  | The empirical evidence suggests that observed Trip-Length Distributions alone are insufficient for reliable parameter identification. |

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
