# Mechanism-Based Human Mobility Science — Mind Map & Architecture State (v13.0+)

### Subtitle
*Towards Mechanism-Based Human Mobility Science through Observability, Recoverability, and Empirical Defensibility*

> **CORE DISSERTATION MASTER STATEMENT (FROZEN KEY SENTENCE):**  
> *"This dissertation investigates the sufficiency of observable information for reconstructing urban spatial interaction under mobility data scarcity. It examines what information is retained or lost under aggregate mobility observation, how observation design affects recoverability, and how complementary open urban information improves OD reconstruction when the mobility observation alone is insufficient."*  
> *(Vietnamese: "Luận án này nghiên cứu tính đầy đủ của thông tin quan sát được để khôi phục tương tác không gian đô thị trong điều kiện khan hiếm dữ liệu di chuyển. Luận án phân tích thông tin nào được giữ lại hoặc mất đi dưới các quan sát di chuyển gộp, thiết kế quan sát ảnh hưởng thế nào đến khả năng định danh, và thông tin không gian đô thị mở bổ trợ cải thiện việc khôi phục OD ra sao khi bản thân quan sát di chuyển không đủ đơn độc.")*  

> **EVALUATION PRINCIPLE (DISSERTATION DIRECTIVE):**  
> *"Matching the Meta input is merely in-sample consistency. It is not evidence of structural OD recovery."*

> **METHODOLOGICAL VALIDITY PRINCIPLE (T24 CORE PREMISE):**  
> $$\boxed{\text{Input Consistency } \neq \text{ Reconstruction Validity}}$$  
> $$\boxed{\text{Validity Requires Improvement on Unconstrained OD Properties}}$$

> **FEASIBILITY & FORMALIZATION STATE:**  
> $$\boxed{\text{FEASIBILITY PHASE = FROZEN}}$$  
> $$\boxed{\text{PROPOSAL FORMALIZATION = ACTIVE}}$$
> $$\boxed{\text{Aggregate Observation } \neq \text{ Complete Information}}$$

---

## 1. Refined 7-Stage Master Derivation Backbone

```text
OBSERVATION ──► RECOVERABLE ──► OBSERVATION ──► UNDERDETERMINATION ──► COMPLEMENTARY ──► OD RECONSTRUCTION ──► INDEPENDENT
                INFORMATION     SENSITIVITY                              CONTEXT                                VALIDATION
  (Meta MDM Obs.) (Paper 1)      (T29-T30)       (Agg. Obs. -> OD Non-ID) (Paper 2)         (C3 Pipeline)        (HCMC Case Study)
```

---

## 2. Statistical Significance & Reliability Audit Summary

* **Statistical Significance & Bootstrap CIs:** Net CPC gain $+0.0417$, $95\%\text{ CI } [0.0308, 0.0527]$, Paired $t$-test $t = 6.9316, p < 0.001$, Wilcoxon $W = 0.0, p < 0.002$.
* **Clean LOOCV Performance (T21):** Leave-One-City-Out Cross-Validation on all 50 US metropolitan areas under completely clean zero-target-OD 3-bin beta MLE yields Mean CPC $= 0.6162$ (Median $= 0.6249$, $95\%\text{ Bootstrap CI } [0.5997, 0.6317]$).
* **Multi-Seed Protocol Reliability:** Multi-seed evaluation across 5 random seeds yields Mean $\text{CPC} = 0.5832 \pm 0.0006$, $\text{CV} = 0.0965\% < 0.1\%$.
* **Complexity-Controlled Failure Regression:** $\text{CPC} \sim \log(N)$ yields $\beta = -0.0611$ ($p < 0.01$), confirming spatial system scale $\log(N)$ maintains an independent negative difficulty association after density control.
* **Negative Evidence on Simple Feature Similarity:** Proper cross-city model transfer reveals that simple similarity in raw feature space does not significantly predict transfer performance directly ($\rho = +0.0955, p = 0.1681$).
* **Robustness of Spatial Context:** In downstream OD reconstruction, the incremental CPC gain provided by independent spatial features is highly robust to parameter misspecification in the distance decay function (gain remains stable between $+0.0411$ and $+0.0530$ across $\pm 60\%$ beta perturbations).
* **Deterrence Robustness & Complexity (T35):** In the Chicago case study, compression-induced parameter degradation is observed across alternative deterrence specifications (Exponential, Power-law, Tanner), with Tanner exhibiting higher instability under coarse compression.

---
*Status: Updated V13.0+ — Feasibility Frozen & Proposal Scientifically Locked.*
