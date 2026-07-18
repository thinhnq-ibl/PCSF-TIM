BLOCK 1. BACKGROUND

Mục tiêu

Trả lời câu hỏi:

Tại sao bài toán này quan trọng?

Không nói phương pháp.

Không nói gap.

Không nói contribution.

Reviewer chỉ cần hiểu vấn đề.

Nội dung nên có
lĩnh vực
bài toán
ứng dụng
Template
[Research problem] is essential for
[application 1],
[application 2],
and
[application 3].
Ví dụ đối với bài của bạn
Accurate origin–destination (OD) flow prediction is essential for transportation planning, accessibility analysis, and urban management.
Độ dài

15–25 từ

BLOCK 2. RESEARCH GAP

Đây là block quan trọng nhất.

Reviewer sẽ quyết định paper có đáng đọc hay không.

Trả lời
Existing studies still cannot ...

hoặc

Current approaches rely on ...
Logic
Current methods

↓

Need local OD matrix

OR

Need trajectory data

↓

Expensive

↓

Privacy issues

↓

Cannot transfer

↓

Not suitable for data-scarce cities
Template
Existing approaches generally rely on ________,
which limits ________.

hoặc

However,
current methods require ________,
making them difficult to apply in ________.
Độ dài

20–35 từ

BLOCK 3. OBJECTIVE

Reviewer muốn biết

Paper này làm gì?

Đây không phải contribution.

Đây không phải method.

Chỉ là mục tiêu.

Template
This study investigates whether ...


hoặc

This paper proposes ...

Đối với bài của bạn
This study investigates whether aggregate mobility data can recover city-specific distance-decay functions for gravity-model calibration.
Độ dài

20–30 từ

BLOCK 4. METHOD

Đây là phần dài nhất.

Không giải thích toán.

Không ghi equation.

Không ghi loss function.

Chỉ mô tả workflow.

Workflow blueprint
Input

↓

Feature extraction

↓

Estimate hidden information

↓

Build model

↓

Predict

↓

Evaluate
Riêng bài của bạn
Meta Movement Distribution Maps

↓

Trip-length distribution

↓

Recover distance-decay

↓

Calibrate gravity model

↓

Generate OD matrix

↓

Evaluate
Template
We first ...

Next ...

Finally ...

Ví dụ

We first derive trip-length distributions from aggregate mobility data.

Next,
we estimate the underlying distance-decay function and calibrate a gravity model.

Finally,
we predict OD flows and evaluate performance across multiple cities.
Độ dài

40–60 từ

BLOCK 5. EXPERIMENT

Đây là block nhiều người bỏ quên.

Nên có một câu mô tả phạm vi đánh giá.

Trả lời
How did you verify it?

Template

Experiments were conducted on ...

Ví dụ

Experiments were conducted across multiple cities using publicly available mobility datasets.

Hoặc

The proposed framework was evaluated against representative gravity-model calibration approaches.

Khoảng

15–20 từ

BLOCK 6. RESULTS

Reviewer đọc đầu tiên.

Không được viết

The proposed method performs well.

Câu này vô nghĩa.

Phải trả lời
Better than whom?

By how much?

Under what conditions?
Template
Results show that ...


Tiếp

The proposed approach consistently ...

Nếu chưa có số

achieves competitive performance

outperforms existing calibration methods

produces robust predictions

accurately recovers

Nếu có số

reduces RMSE by ...

improves MAE by ...

improves CPC by ...
Độ dài

25–40 từ

BLOCK 7. IMPLICATION

Reviewer sẽ hỏi

So what?

Ý nghĩa của kết quả.

Không lặp lại result.

Template
These findings demonstrate that ...

Ví dụ

These findings demonstrate that aggregate mobility products contain sufficient information to calibrate gravity models without direct OD observations.
BLOCK 8. CONTRIBUTION

Đây là câu cuối.

Reviewer sẽ nhớ câu này.

Không mô tả method.

Không nói result.

Chỉ nói đóng góp.

Template
This work provides ...


Ví dụ

This work provides a transferable and privacy-preserving framework for OD flow estimation in data-scarce cities.
TOÀN BỘ FLOW
────────────────────────────────────

Background
Why is this problem important?

────────────────────────────────────

Gap
Why are existing studies insufficient?

────────────────────────────────────

Objective
What does this paper aim to solve?

────────────────────────────────────

Method
How is the problem solved?

────────────────────────────────────

Experiment
How is the method validated?

────────────────────────────────────

Results
What are the main findings?

────────────────────────────────────

Implication
Why do the findings matter?

────────────────────────────────────

Contribution
What is the key scientific contribution?

────────────────────────────────────
Blueprint dành riêng cho bài báo của bạn
1. Background
Accurate OD flow prediction is essential for transportation planning, accessibility analysis, and urban management.

↓

2. Gap
Existing approaches typically require observed OD matrices or individual mobility trajectories, limiting their applicability in data-scarce and privacy-sensitive settings.

↓

3. Objective
This study investigates whether aggregate mobility data can recover city-specific distance-decay functions for gravity-model calibration.

↓

4. Method
Trip-length distributions are derived from Meta Movement Distribution Maps.
The underlying distance-decay function is recovered and used to calibrate a gravity model.
The calibrated model generates OD flow estimates.

↓

5. Experiment
The framework is evaluated across multiple cities and compared with representative calibration baselines.

↓

6. Results
The recovered distance-decay functions closely match reference patterns and consistently improve or maintain competitive OD prediction accuracy relative to conventional calibration approaches.

↓

7. Implication
The results demonstrate that privacy-preserving aggregate mobility data can provide sufficient information for gravity-model calibration without requiring direct OD observations.

↓

8. Contribution
This work introduces a transferable and privacy-preserving framework for OD flow estimation, expanding