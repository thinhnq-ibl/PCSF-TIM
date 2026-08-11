# Mechanism-Based Human Mobility Science — Mind Map & Architecture State (v7.0)

> **CORE DISSERTATION MASTER STATEMENT (FROZEN KEY SENTENCE):**  
> *"Human mobility can be reconstructed by independently inferring its structural and behavioural components from the maximum publicly available information."*  
> *(Vietnamese: "Có thể phục hồi tương tác di chuyển đô thị bằng cách suy luận độc lập thành phần cấu trúc và thành phần hành vi từ lượng thông tin công khai tối đa.")*

> **EVALUATION PRINCIPLE (DISSERTATION DIRECTIVE):**  
> *"Matching the Meta input is merely in-sample consistency. It is not evidence of structural OD recovery."*

> **CONDENSED CORE NARRATIVE:**  
> *"Aggregate mobility appears informative but non-identifying. The remaining scientific problem is determining what independent structural information is sufficient to resolve that ambiguity."*

---

## 1. 3-Stage Scientific Core & Test A Audit Verification

```text
       OBSERVABILITY                     IDENTIFIABILITY                 EMPIRICAL DEFENSIBILITY
         (Paper 1)                          (Paper 2)                       (HCMC Case Study)
┌──────────────────────────┐      ┌──────────────────────────┐      ┌──────────────────────────┐
│ R^2 = 0.9624             │      │ Q5: Same TLD JSD = 0,    │      │ Zero-shot Test CPC=0.6462│
│ Multi-start CV = 0.0000% │ ──►  │ yet OD CPC = 0.5373      │ ──►  │ Real Structure (0.6462)  │
│ Noise Error < 0.45%      │      │ Q6: Structure -> 1.0000  │      │ >> Shuffled (0.5331)     │
└──────────────────────────┘      └──────────────────────────┘      └──────────────────────────┘
```

---

## 2. Test A Audit Summary (Zero Oracle Leakage)

* **Oracle Upper Bound (Ground Truth Marginals):** $\text{CPC} = 0.7159$ (Ceiling ONLY).
* **Transferred Urban Structure ($R_S$):** Mean $\text{CPC} = 0.6462$ (Median: $0.6525$, Range: $[0.4983, 0.7125]$).
* **TLD-Only Baseline:** Mean $\text{CPC} = 0.5852$.
* **Shuffled Negative Control:** Mean $\text{CPC} = 0.5331$.
* **Net Gain over TLD-Only:** $+0.0610$ consistently across all 10 unseen test cities!

---
*Status: Updated V7.0 — Test A Audit Verified.*
