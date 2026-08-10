# Paper 1 Scientific Blueprint: Constitution & Experimental Design

**Status:** Frozen & Approved  
**Date:** August 10, 2026  
**Target Venue:** Top-tier Transportation / GIScience / Spatial Data Mining Journal (e.g. Transportation Research Part C / ISPRS Journal / IJGIS)

---

## 1. Working Title & Central Scientific Thesis

### Working Title
> **How Much Meta Mobility Data Is Enough? External Validity, Temporal Persistence, and Data-Window Sufficiency of Privacy-Preserving Mobility-Distance Signatures**

### Central Scientific Thesis
$$\boxed{\text{Meta MDM contains a persistent, externally valid mobility-distance signature that corresponds with independent seasonal OD distributions, with residual correspondence beyond measured geographic controls.}}$$

---

## 2. Terminology Discipline & Claim Boundaries

| Permitted Terminology | Forbidden / Reviewer-Risk Terminology | Rationale |
| :--- | :--- | :--- |
| **Mobility-distance signature** | Behavioral latent variable | Meta pings reflect aggregated movement profiles, not isolated individual cognition. |
| **Empirical mobility-distance prior** | True travel behavior signal | Meta MDM serves as an empirical prior for spatial interaction modeling. |
| **Matched spatial-support validity** | OD matrix reconstruction | Paper 1 validates distance-decay structure, not full destination-pair topology. |
| **Residual Meta–OD correspondence** | Proven behavioral signal | Residual association $\rho_{partial} = 0.4108$ controls for measured geometry, not all omitted variables. |
| **Mean absolute difference ($5.65 - 6.42\%$)** | 93.3% matching accuracy | MAE is a percentage point difference, not a classification accuracy metric. |
| **Short-window sufficiency ($S(1) = 96.3\%$)** | 1 day estimates seasonal mobility | A 1-day observation retains 96.3% of the OD *rank correspondence* of the 16-day reference. |

---

## 3. Three Frozen Research Questions & Hypotheses

### RQ1 — External Validity (Primary Centerpiece)
- **Question:** To what extent do Meta Movement Distribution shares correspond to independently observed seasonal travel-distance distributions when evaluated on identical spatial support?
- **Hypothesis $H_1$:** Meta's conditional distance shares exhibit positive, statistically significant rank correspondence with independent seasonal OD distance shares on matched county support ($\rho(M_{10-100}, O_{10-100}) > 0$).
- **Primary Endpoint:** Medium-range travel bin ($10-100$ km): Spearman $\rho = \mathbf{0.7724}$ ($95\%$ bootstrap CI: $[0.5595, 0.8859]$, LOO Jackknife: $[0.7471, 0.8002]$, $p_{perm} < 0.001$).
- **Secondary Endpoint:** Short-range travel bin ($0-10$ km): Spearman $\rho = \mathbf{0.6384}$ ($95\%$ bootstrap CI: $[0.3103, 0.8308]$, LOO Jackknife: $[0.5982, 0.7110]$, $p_{perm} < 0.001$).

### RQ2 — Temporal Persistence & Data Sufficiency
- **Question:** How persistent is this origin-specific mobility-distance signature across daily Meta observations, and how much observation time is required to recover its full-period OD correspondence?
- **Hypothesis $H_2$:** Place-specific spatial differences dominate daily measurement variation, such that single-day observations preserve nearly all of the external OD correspondence obtained from multi-day aggregation.
- **Key Metrics:** $ICC = \mathbf{0.6965}$ ($69.65\%$ place variance), Daily Median $\rho_t = \mathbf{0.7616}$ (IQR: $[0.7362, 0.7826]$), Short-Window Sufficiency $S(1) = \mathbf{96.30\%}$.

### RQ3 — Structural Distinctiveness & Boundary Condition
- **Question:** To what extent does Meta–OD correspondence persist after accounting for observable urban geographic structure, and does it yield out-of-sample predictive gains over static land use?
- **Hypothesis $H_3$:** Meta–OD rank correspondence remains statistically significant after controlling for measured urban spatial geometry ($\rho(M, O \mid G) > 0$).
- **Boundary Condition:** Combining Meta MDM with static geography does not improve out-of-sample leave-one-city-out predictive performance ($\Delta R^2_{LOCO} = -0.0223$), establishing that residual association does not automatically imply out-of-sample predictive utility.
- **Key Metrics:** Partial Spearman $\rho_{partial} = \mathbf{0.4108}$ ($p = 0.0268$ under full control set $G_3$).

---

## 4. Main Figures Architecture (4 Figures)

1. **Figure 1 — Spatial Support & Measurement Framework Diagram**:
   - Visualizing tract-to-county spatial aggregation ($OD_{ab}^{tract} \rightarrow OD_{ij}^{county}$) and the conceptual decomposition $M_{i,t} = \mu_i + \delta_{i,t}$.
2. **Figure 2 — Primary External Validity Scatterplots (Matched County Support)**:
   - Panel A: Short-range travel ($0-10$ km, $\rho = 0.6384, N=29$).
   - Panel B: Primary Endpoint medium-range travel ($10-100$ km, $\rho = 0.7724, N=29$).
3. **Figure 3 — Daily Persistence & Sufficiency Timeline**:
   - X-axis: 16 individual Meta observation days ($t = 1 \dots 16$).
   - Y-axis: Daily Spearman correlation $\rho_t^{10-100}$ with 16-day reference line ($\rho = 0.7724$) and daily IQR band.
4. **Figure 4 — Geometry Sensitivity & Prediction Boundary**:
   - Panel A: Partial correlation $\rho_{partial}$ under nested control sets $G_1 \rightarrow G_2 \rightarrow G_3$.
   - Panel B: Out-of-sample LOCO-CV prediction performance comparison ($Model\ G$ vs $Model\ M$ vs $Model\ G+M$).

---

## 5. Main Tables Architecture (3 Tables)

- **Table 1 — Sample & Spatial Matching Specification**:
  - $N=29$ matched counties across 25 US Metropolitan Areas, 11,777 census tracts, 16 daily Meta MDM snapshots (`2026-04-01` to `2026-04-16`), LODES seasonal OD baseline.
- **Table 2 — External Validity Master Estimands**:
  - Primary (10–100 km) & Secondary (0–10 km) endpoints: Spearman $\rho$, $95\%$ bootstrap CI, $p_{perm} < 0.001$, LOO Jackknife range, MAE.
- **Table 3 — Persistence, Data Sufficiency & Partial Sensitivity**:
  - $ICC$, daily median/IQR, $S(1)$, nested partial correlations ($\rho_{M,O \mid G_1..G_3}$), LOCO-CV $R^2$ and MAE.

---

## 6. Conceptual Bridge to Paper 2

Paper 1 establishes Meta MDM as an **empirically validated structural mobility-distance prior** ($M_i$).

In **Paper 2**, this prior is directly integrated into the Spatial Interaction framework:
$$P(j \mid i) \propto \underbrace{A_j}_{\text{Destination Opportunities}} \times \underbrace{f(d_{ij} \mid M_i)}_{\text{Meta-informed Distance Prior}}$$

Meta telemetry does not compete with static geography; it supplies the empirical distance decay prior $f(d_{ij} \mid M_i)$ while destination spatial features $A_j$ govern spatial trip attraction.
