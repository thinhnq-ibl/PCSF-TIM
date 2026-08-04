---
title: "Master PhD Monograph Architecture & Scientific Blueprint"
subtitle: "Bản Thiết kế Luận án Tiến sĩ theo Kiến trúc Monograph 6 Chương"
author: "PhD Candidate"
date: "2026"
anchor-reference: "Handbook.md (Anchor for Chapter 3: Behaviour Identification)"
---

# Master PhD Monograph Architecture & Scientific Blueprint
# Bản Thiết kế Luận án Tiến sĩ theo Kiến trúc Monograph 6 Chương

---

## 📌 Relationship to `Handbook.md` (The Anchor)

* **[`handbook_phd.md`](file:///D:/research/PCSF-TIM/handbook_phd.md)**: Định hình toàn bộ **Kiến trúc Luận án Tiến sĩ 2 Tầng (Two-Tier Monograph Architecture)** gồm 6 Chương xoay quanh 1 Câu hỏi Trung tâm.
* **[`Handbook.md`](file:///D:/research/PCSF-TIM/Handbook.md)**: Giữ nguyên 100% vai trò **Neo giữ Lý thuyết (Theoretical Anchor)** chuyên sâu cho **Chapter 3 (Collective Behaviour Identification)**.

---

# I. The Grand Scientific Question of the Thesis

Toàn bộ Luận án Tiến sĩ xoay quanh **MỘT CÂU HỎI KHOA HỌC TRUNG TÂM DUY NHẤT**:

> **How can human mobility be understood by explicitly separating urban structure from collective travel behaviour?**
>
> *(Làm thế nào để hiểu về di chuyển của con người bằng cách tách biệt một cách rõ ràng giữa cấu trúc đô thị và hành vi di chuyển tập thể?)*

---

# II. Two-Tier Thesis Structure (Cấu trúc Luận án 2 Tầng Cân bằng)

```text
===================================================================================================
 TIER A: SCIENTIFIC CONTRIBUTION (Human Mobility Science)
 "How to infer OD without surveys?"
───────────────────────────────────────────────────────────────────────────────────────────────────
 • Core: Urban Structure (S_i) + Collective Behaviour (θ) ──► Survey-Free Zero-Shot OD Matrix (T_ij)
 • Target Audience: Human Mobility / Urban AI / Spatial Physics Committees
===================================================================================================
                                                │
                                                ▼ (Generated OD Matrix T_ij)
===================================================================================================
 TIER B: ENGINEERING CONTRIBUTION & POLICY IMPACT (Transportation Engineering)
 "What to do with the generated OD?"
───────────────────────────────────────────────────────────────────────────────────────────────────
 • Core: Generated OD ──► Transit Assignment ──► Indirect Boarding Validation & Bus/Metro Planning
 • Target Audience: Transportation Planning / Civil Engineering Committees & City Planning Authorities
===================================================================================================
```

---

# III. The 6-Chapter Monograph Architecture

Sáu chương của luận án là 6 bước tiến trình không thể tách rời:

```text
                               Grand Scientific Question:
 "How can human mobility be understood by explicitly separating urban structure from collective travel behaviour?"
                                            │
       ┌────────────────────────────────────┼────────────────────────────────────┐
       ▼                                    ▼                                    ▼
Chapter 1: Why separate?              Chapter 2: How represent?            Chapter 3: How identify?
What determines mobility?              How represent structure?             How identify behaviour?
(Human Mobility Theory)               (Urban Structure Representation)     (Behaviour Identification)
                                                                            [SCIENTIFIC CORE]
       │                                    │                                    │
       ├────────────────────────────────────┼────────────────────────────────────┘
       ▼                                    ▼                                    ▼
Chapter 4: How transfer?              Chapter 5: How generate OD?          Chapter 6: How support planning?
How transfer knowledge?               Can OD be generated survey-free?     How run transit assignment & policy?
(Transferable Urban Knowledge)        (Survey-Free OD Generation)          (Transportation Applications)
                                      [ENGINEERING DEMO]                   [INDIRECT VALIDATION & POLICY]
```

---

# IV. Detailed Chapter Breakdown & Scientific Questions

### Chapter 1. Human Mobility Theory
* **Scientific Question:** *What determines human mobility?*
* **Scope & Content:** Nền tảng lý thuyết Tương tác Không gian (Wilson 1967, Gravity, Radiation), Nguyên lý Tách biệt Cấu trúc vs Hành vi, và ranh giới tri thức hiện tại.
* **Role:** **Theoretical Foundation.**

### Chapter 2. Urban Structure Representation
* **Scientific Question:** *How should urban structure be represented?*
* **Scope & Content:** Phân rã các lớp cấu trúc đô thị (Population, Employment, POIs, Road Network, Land Use, Accessibility) và sử dụng Deep Learning/GNNs để học vectơ biểu diễn ẩn $\mathbf{S}_i$ (latent urban representation).
* **Role:** **Urban AI & Representation Learning.**

### Chapter 3. Collective Behaviour Identification
* **Scientific Question:** *How can collective travel behaviour be identified?*
* **Scope & Content:** Ước tính chỉ số hành vi suy giảm khoảng cách $\theta = (\alpha, \beta)$ từ các quan sát di chuyển nén (observed TLD) qua hàm khả năng xác suất (Conditional MLE) và đánh giá tính định danh (Identifiability). *(Được neo giữ bởi `Handbook.md`)*.
* **Role:** **THE SOUL OF THE THESIS (Primary Scientific Contribution).**

### Chapter 4. Transferable Urban Knowledge
* **Scientific Question:** *How can urban knowledge be transferred across cities?*
* **Scope & Content:** Học biểu diễn Cấu trúc $\mathbf{S}_i$ từ 50 thành phố US, xây dựng lý thuyết chuyển giao tri thức không gian vượt đô thị (Transferability & Domain Adaptation) mà không bị phụ thuộc vào dữ liệu OD địa phương.
* **Role:** **AI Transferability & Cross-City Generalization.**

### Chapter 5. Survey-Free OD Generation
* **Scientific Question:** *How can OD be generated without surveys?*
* **Scope & Content:** Hợp nhất Cấu trúc học được ($\mathbf{S}_i$, Ch 2/4) + Hành vi định danh được ($\theta$, Ch 3) vào mô hình Trọng lực suy luận để tái tạo ma trận lưu lượng OD $T_{ij}$ không cần khảo sát địa phương.
* **Role:** **ENGINEERING DEMONSTRATION & PROOF-OF-CONCEPT.**

### Chapter 6. Transportation Applications & Indirect Validation
* **Scientific Question:** *How can the framework support transportation planning and enable indirect model validation?*
* **Scope & Content:** 
  1. **Transit Assignment:** Chạy mô hình gán lưu lượng giao thông (Transit Assignment) từ ma trận OD $\hat{T}_{ij}$ sinh ra.
  2. **Indirect Boarding Validation:** So sánh Lượt khách dự báo tại trạm (*Predicted Boarding*) với Lượt khách thực tế (*Observed Smartcard Boarding*) để kiểm chứng gián tiếp độ chính xác của ma trận OD khi không có Ground-truth OD survey.
  3. **Planning Scenario Analysis:** Đánh giá kịch bản cắt/điều chỉnh tuyến bus (Route 08 removal) và tác động của Metro Số 2 lên mạng lưới bus gom (Feeder Bus Networks).
* **Role:** **INDIRECT VALIDATION, PRACTICAL UTILITY & POLICY IMPACT.**

---

# V. Precise Role of Bus Data: Application & Indirect Validation

```text
   INCORRECT (Training Trap):    Bus Data ──► Learn emission O_i / Gravity flows  (FLAWED)

   CORRECT (Gold-Standard):      Generated OD ──► Transit Assignment ──► Bus Planning
                                                         │
                                                         ▼
                                           Indirect Boarding Validation
                                          (Predicted vs Observed Boardings)
```

> **Nguyên tắc:** Dữ liệu xe buýt được chuyển từ **Training Data** sang **Application & Indirect Validation Data**. Đây là cách duy nhất để chứng minh độ chính xác của ma trận OD tại đô thị thiếu dữ liệu (TPHCM) mà không cần OD survey tốn kém.

---

# VI. The Literature Bible (10 Classical & SOTA Categories)

1. **Wilson (1967, 1970)** — Entropy & Spatial Interaction (*Chapter 1*)
2. **Ben-Akiva & Lerman (1985)** — Discrete Choice Analysis & Random Utility (*Chapter 1 & 3*)
3. **Ortúzar & Willumsen (2011)** — Modelling Transport (*Transportation & Transit Assignment Bible*)
4. **Michael Batty (2013)** — The New Science of Cities (*Urban Science*)
5. **Marc Barthelemy (2016, 2018)** — Cities & Complex Systems / Physics Reports 2018 (*Mobility Bible*)
6. **David Levinson** — Accessibility & Transport Geography (*Chapter 2 & 6*)
7. **Chodrow (2017)** — Spatial Information & Transferability (*Chapter 4*)
8. **Geo Representation Learning Literature** — Spatial embeddings (*Chapter 2*)
9. **Barbosa et al. (2018)** — Human Mobility Review (*Chapter 1*)
10. **GeoAI & Urban Foundation Models (2024–2026)** — SOTA Urban AI (*Chapter 2 & 4*)
