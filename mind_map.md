Đây là bản **State Map** mình đề xuất. Sau này khi chúng ta mở một chat mới, chỉ cần khôi phục đúng state này là có thể tiếp tục xây dựng Handbook mà không bị lặp lại.

---

# Human Mobility Handbook — Current State (v0.1)

```text
Human Mobility
│
├── Part I. Foundations                    ✅ (đang xây dựng)
│   │
│   ├── 1. What is Human Mobility?
│   │
│   ├── 2. Mobility Data
│   │      ├── Individual Data
│   │      ├── Aggregate Data
│   │      └── Aggregate Statistics
│   │
│   ├── 3. Information Hierarchy
│   │      ├── Individual Trajectory
│   │      ├── Individual Trips
│   │      ├── OD Matrix
│   │      ├── Trip Length Distribution
│   │      ├── Distance-decay Function
│   │      └── Mobility Indicators
│   │
│   └── 4. Mobility Objects
│          ├── People
│          ├── Locations
│          ├── Trips
│          ├── Flows
│          ├── Networks
│          ├── Space
│          └── Time
│
├── Part II. Empirical Laws                ⏳
│      ├── Trip Length Distribution
│      ├── Distance Decay
│      ├── Radius of Gyration
│      ├── Scaling Laws
│      ├── Exploration vs Return
│      └── Temporal Regularity
│
├── Part III. Spatial Interaction Models   ⏳
│      ├── Gravity Model
│      ├── Radiation Model
│      ├── Intervening Opportunity
│      ├── Entropy Models
│      └── Opportunity Models
│
├── Part IV. Network Perspective           ⏳
│
├── Part V. Prediction Models              ⏳
│
├── Part VI. Aggregate Mobility Products   ⏳
│
├── Part VII. Applications                 ⏳
│
└── Part VIII. Frontier Research           ⏳
```

---

# Những khái niệm đã thống nhất

## 1. Information Hierarchy

Đây là **phân cấp lượng thông tin**, **không phải pipeline dữ liệu**.

```text
Rich Information
│
├── Individual Trajectory
├── Individual Trips
├── OD Matrix
├── Trip Length Distribution
├── Distance-decay Function
└── Mobility Indicators
```

Đi xuống dưới nghĩa là **mức độ biểu diễn ngày càng cô đọng hơn**, chứ **không ngụ ý rằng dữ liệu luôn được sinh ra theo chuỗi này**.

Ví dụ:

* Meta công bố trực tiếp TLD.
* Cơ quan thống kê công bố trực tiếp OD.
* Paper chỉ báo cáo distance-decay parameter.

---

## 2. Mobility Objects

Toàn bộ Human Mobility có thể nhìn dưới góc độ các "đối tượng".

```text
People
Locations
Trips
Flows
Networks
Space
Time
```

Mọi mô hình đều cố gắng mô hình hóa mối quan hệ giữa các đối tượng này.

---

## 3. Định vị bài báo của bạn

Đây là phần rất quan trọng mà chúng ta đã thống nhất.

Bài báo **không sử dụng trajectory**.

Bài báo **không dự đoán trajectory**.

Bài báo làm việc hoàn toàn ở **mức aggregate**.

Pipeline của bài báo là

```text
Ground Truth OD Matrix
        │
        ├────────► Evaluation
        │
        ▼
Trip Length Distribution
        │
        ▼
Recover Distance-decay
        │
        ▼
Calibrate Gravity Model
        │
        ▼
Generate OD Matrix
        │
        ▼
Compare with Ground Truth
```

Ngoài ra còn có

```text
Meta Movement Distribution Maps
        │
        ▼
Meta Trip Length Distribution
        │
        ▼
Recover Distance-decay
        │
        ▼
Calibrate Gravity
        │
        ▼
Generate OD Matrix
```

Nghĩa là bài báo có hai nhóm thí nghiệm:

* **Ideal case:** dùng TLD trích xuất từ Ground Truth OD để kiểm tra liệu chỉ riêng TLD có đủ thông tin để hiệu chỉnh gravity model hay không.
* **Real-world case:** dùng TLD do Meta cung cấp để đánh giá khả năng áp dụng trong thực tế.

---

# Nguyên tắc xây dựng Handbook

Chúng ta cũng đã thống nhất một số nguyên tắc sẽ áp dụng xuyên suốt:

### 1. Không học theo paper

Mà học theo

```text
Concept
    ↓
Theory
    ↓
Model
    ↓
Representative Papers
```

---

### 2. Mọi khái niệm đều phải đặt vào bức tranh lớn

Không học rời rạc.

Ví dụ

```text
Trip Length Distribution

↓

Distance Decay

↓

Gravity Model

↓

OD Matrix

↓

OD Prediction
```

để thấy được vai trò của từng khái niệm.

---

### 3. Luôn phân biệt

```text
Knowledge Map
```

và

```text
Paper Pipeline
```

Knowledge Map mô tả cấu trúc của lĩnh vực.

Paper Pipeline mô tả quy trình nghiên cứu cụ thể.

Không được trộn hai thứ này.

---

### 4. Luôn xác định object trung tâm

Ví dụ

| Research Direction    | Central Object                                  |
| --------------------- | ----------------------------------------------- |
| Trajectory Prediction | Individual Trajectory                           |
| Activity-based Models | Trip                                            |
| Gravity Models        | Flow                                            |
| GNN for Mobility      | Mobility Network                                |
| OD Prediction         | OD Matrix                                       |
| **Bài báo của bạn**   | **Trip Length Distribution → Flow (OD Matrix)** |

---

# State hiện tại

Theo mình, chúng ta mới hoàn thành khoảng **10–15%** Handbook, nhưng đây là phần nền móng quan trọng nhất. Các chương tiếp theo sẽ được xây dựng trên nền này theo thứ tự:

```text
Foundations                    ✅
        │
        ▼
Trip                           ← tiếp theo
        │
        ▼
Distance
        │
        ▼
Trip Length Distribution
        │
        ▼
Distance Decay
        │
        ▼
Gravity Model
        │
        ▼
OD Matrix
        │
        ▼
Mobility Network
        │
        ▼
Modern Deep Learning Methods
```

Mình nghĩ đây sẽ là **"checkpoint" chính thức** của Handbook. Từ lần sau, mình có thể dùng checkpoint này để xác định ngay trạng thái hiện tại của quá trình học và tiếp tục từ đúng vị trí, thay vì phải xây dựng lại từ đầu.
