# Document Management Guide
## Kim Chỉ Nam Quản Lý Tài Liệu PhD

> **Version:** 1.0 | **Created:** 2026-08-06  
> **Purpose:** Maintain consistency and prevent synchronization drift across all PhD documents.

---

## 1. Kiến Trúc Tài Liệu & Vai Trò

| Document | Stage | Vai trò duy nhất | Trạng thái |
| :--- | :--- | :--- | :--- |
| `Handbook.md` | Stage 1 | Immutable knowledge anchor — literature synthesis toàn bộ background | 🔒 **Frozen. Không được sửa.** |
| `KnowledgeBase.md` | Stage 2 | Source of truth cho Literature Matrix (Layers A–H), citation evidence, và Executive Module Matrix | ✏️ Living document |
| `handbook_phd.md` | Stage 2 | PhD Operating System — 8 Modules, decision framework, QT evidence anchors | ✏️ Living document |
| `proposal_phd.md` | Output | High-level thesis argument synthesis (~20 pages) — references modules, không định nghĩa chúng | ✏️ Living document |
| `mind_map.md` | Navigation | Quick overview & logical flow — không chứa definitions | ✏️ Living document |
| `feasible_test/REPORT.md` | Evidence | Empirical test log (QT1–QT19) — không chứa framework definitions | ✏️ Living document |
| `handbook_references.bib` | Bibliography | Single source of truth cho tất cả citations | ✏️ Living document |

---

## 2. Nguyên Tắc Cốt Lõi

### Nguyên tắc 1 — One Document, One Role
> **Mỗi document có đúng một vai trò không thể thay thế.**  
> Không document nào được định nghĩa thứ gì mà document khác đã là source of truth.

### Nguyên tắc 2 — KnowledgeBase.md là Source of Truth
> **`KnowledgeBase.md` là nơi duy nhất** chứa full Executive Scientific Matrix (8 modules) và Layers A–H.  
> Các document khác *reference* đến nó, không *re-define*.

### Nguyên tắc 3 — Handbook.md là Immutable Anchor
> **`Handbook.md` không bao giờ được chỉnh sửa.**  
> Nó là bằng chứng của Stage 1 thinking. Sự tiến hóa khoa học được ghi nhận trong `handbook_phd.md`, không phải bằng cách sửa `Handbook.md`.

### Nguyên tắc 4 — Mỗi Reference chỉ có ở `handbook_references.bib`
> **Không được ghi citation key trong text** nếu entry chưa có trong bib.  
> Thứ tự: thêm vào `.bib` trước → sau đó cite trong document.

---

## 3. Update Order — Thứ Tự Cập Nhật Khi Thay Đổi

Khi thay đổi **bất kỳ khái niệm cốt lõi nào** (tên Principle, Module, Scientific Proposition, RQ...):

```
Bước 1 → handbook_phd.md
          [Định nghĩa mới / Module update]
             │
Bước 2 → KnowledgeBase.md
          [Executive Matrix + Layer cụ thể + Section 4 mapping]
             │
Bước 3 → proposal_phd.md
          [Synthesis output cập nhật theo]
             │
Bước 4 → mind_map.md
          [Navigation / overview update]
             │
Bước 5 → feasible_test/REPORT.md
          [Paradigm shift table + Proposition nếu có]
             │
Bước 6 → handbook_references.bib
          [Thêm entries mới nếu có citation mới]
```

> [!IMPORTANT]
> **Không bao giờ bỏ qua bước nào trong chuỗi này.** Synchronization debt tích lũy nhanh và khó phát hiện.

---

## 4. Checklist Khi Thay Đổi Thuật Ngữ

Khi đổi tên một khái niệm (ví dụ: "Separation" → "Decomposition"):

- [ ] `handbook_phd.md` — Mission Statement, Module definitions, Paradigm table
- [ ] `KnowledgeBase.md` — Header Core Principle, Executive Matrix, Layer E/F/H Attribution Boundary, Section 4 mapping
- [ ] `proposal_phd.md` — Section 3 (Principle name), Section 11 (Narrative table row)
- [ ] `mind_map.md` — Core Principle line
- [ ] `feasible_test/REPORT.md` — Paradigm shift table row, Central Proposition

---

## 5. Checklist Khi Thêm Citation Mới

- [ ] Xác minh DOI từ `verify_citation.md` hoặc nguồn gốc
- [ ] Thêm entry đầy đủ vào `handbook_references.bib` trước
- [ ] Cite trong Layer tương ứng của `KnowledgeBase.md` (APA format in-text)
- [ ] Nếu cần, thêm vào Evidence Map của Layer liên quan

---

## 6. Dấu Hiệu Cảnh Báo — Signs of Drift

Kiểm tra định kỳ nếu thấy các dấu hiệu sau:

| Dấu hiệu | Nghĩa | Hành động |
| :--- | :--- | :--- |
| Cùng một Principle có 2 tên khác nhau ở 2 file | Terminology drift | Chạy Update Order từ Bước 1 |
| Citation xuất hiện trong text nhưng không có trong bib | Missing reference | Thêm vào `.bib` ngay |
| Module description ở `handbook_phd.md` khác `KnowledgeBase.md` | Inconsistency | `KnowledgeBase.md` là source of truth |
| `proposal_phd.md` dùng ngôn ngữ cũ hơn `handbook_phd.md` | Output lag | Re-sync `proposal_phd.md` |

---

## 7. Canonical Definitions — Thuật Ngữ Chuẩn (V3.0)

Những định nghĩa này là **bất biến** cho toàn bộ hệ thống tài liệu:

| Thuật ngữ | Định nghĩa chuẩn |
| :--- | :--- |
| **Scientific Object** | Spatial Interaction (NOT Human Mobility) |
| **Core Principle** | Structure–Behaviour **Decomposition** Principle (NOT Separation) |
| **Scientific Proposition** | *"Although Spatial Interaction emerges from the interaction between Urban Structure Representation and Travel Behaviour Representation, treating these representations as analytically distinguishable enables different scientific questions to be formulated, different learning objectives to be defined, and different learning strategies to be developed."* |
| **Paper 1 maps to** | Module 5 (Travel Behaviour Representation) → RQ1 |
| **Paper 2 maps to** | Module 4 (Urban Structure Representation) → RQ2 |
| **OD Reconstruction is** | Validation evidence — NOT the research objective |
| **Gravity is** | Scientific language (Module 2) — NOT a predictive model |

---

*Last updated: 2026-08-06 | Framework Version: V3.0 (Refined 8-Module Framework)*
