# Paper 1 Scientific Blueprint: Constitution & Experimental Design

**Status:** Frozen & Approved (Post-Audit: 79 Continuous Days / 3-Month Persistence Matrix Enforced)  
**Date:** August 10, 2026  
**Target Venue:** Top-tier Transportation / GIScience / Spatial Data Mining Journal (e.g. Transportation Research Part C / ISPRS Journal / IJGIS)

---

## 1. Working Title & Central Scientific Thesis

### Title (Option A — Selected)
> **External Validity of Meta Movement Distribution Maps: Spatial-Support Sensitivity and Temporal Persistence across 50 U.S. Metropolitan Areas**

### Central Scientific Thesis
$$\boxed{\begin{aligned}
&\text{Across 50 U.S. metropolitan study areas, Meta MDM exhibits moderate and highly robust correspondence}\
&\text{with independent OD distance structure } (\rho = 0.5452, p < 0.0001). \text{ This correspondence is substantially}\
&\text{stronger in strict matched-support analyses } (\rho = 0.6844 - 0.7724), \text{ persists across continuous}\
&\text{3-month observation windows } (ICC_{79d} = 0.6573, \text{3-Month } \rho = 0.9865 - 0.9953), \text{ and remains}\
&\text{substantial after adjustment for the measured population-opportunity distance structure } (\rho_{partial} = 0.6680).
\end{aligned}}$$

---

## 2. Terminology Discipline & Claim Boundaries

| Permitted Terminology | Forbidden / Reviewer-Risk Terminology | Rationale |
| :--- | :--- | :--- |
| **Short and multi-month persistence** | Universal multi-year invariance | 79 days (`2026-04-01` to `2026-06-23`) evaluates continuous 3-month stability, not multi-year invariance. |
| **3-month stability matrix ($\rho = 0.9865 - 0.9953$)** | Universal temporal stability | April, May, and June 2026 exhibit near-perfect month-over-month stability across 1,840 US counties. |
| **Short-window sufficiency ($S(1) = 96.3\%$)** | 1 day estimates seasonal mobility | A 1-day observation retains 96.3% of the OD *rank correspondence* of the multi-day reference. |
| **Mobility-distance signature** | Behavioral latent variable | Meta pings reflect aggregated movement profiles, not isolated individual cognition. |
| **Empirical mobility-distance prior** | True travel behavior signal | Meta MDM serves as an empirical prior for spatial interaction modeling. |
| **Matched spatial-support validity** | OD matrix reconstruction | Paper 1 validates distance-decay structure, not full destination-pair topology. |
| **Residual Meta–OD correspondence** | Proven behavioral signal | Residual association $\rho_{partial} = 0.4108 - 0.6680$ controls for measured geometry/opportunity, not all omitted variables. |
| **Mean absolute difference ($5.65 - 6.61\%$)** | 93.3% matching accuracy | MAE is a percentage point difference, not a classification accuracy metric. |

---

## 3. Re-balanced Contribution Weights & Three Frozen Research Questions

### Contribution Weights Allocation
- **50% External Validity**: Full-sample baseline across 50 US metropolitan study areas ($\rho_{50} = \mathbf{0.5452}, p < 0.0001, p_{\text{perm}} < 0.001$).
- **25% Spatial-Support Sensitivity**: Strong evidence consistent with spatial-support mismatch driving attenuation ($\rho_A = \mathbf{0.6844}$ vs $\rho_C = \mathbf{0.2020}, \Delta \rho = \mathbf{0.4824}, \beta_3 = \mathbf{+0.6050}$). Group B ($N=3$) treated as descriptive only due to insufficient sample size.
- **15% Temporal Persistence & Data Sufficiency**: 3-month stability matrix ($\rho = \mathbf{0.9865} - \mathbf{0.9953}$ across 1,840 US counties over 79 continuous days), $ICC_{79d} = \mathbf{0.6573}$, Daily Median $\rho_t = \mathbf{0.7616}$, $S(1) = \mathbf{96.30\%}$.
- **10% Geographic & Opportunity Robustness**: Partial Spearman $\rho(M, O \mid A_{\text{opp}}) = \mathbf{0.6680}$ ($p = 0.0001$), Partial Spearman $\rho_{G_3} = \mathbf{0.4108}$, LOCO-CV prediction boundary condition ($\Delta R^2_{LOCO} = -0.0223$).

---

## 4. Main Figures Architecture (4 Figures)

1. **Figure 1 — Spatial Support & Measurement Framework Diagram**:
   - Visualizing tract-to-county spatial aggregation ($OD_{ab}^{tract} \rightarrow OD_{ij}^{county}$) and the conceptual decomposition $M_{i,t} = \mu_i + \delta_{i,t}$.
2. **Figure 2 — Primary External Validity Scatterplots & Spatial-Support Stratification**:
   - Panel A: All 50 Metropolitan Study Areas Scatterplot ($\rho = 0.5452, r = 0.5529, N=50$).
   - Panel B: Spatial-Support Stratification Comparison (Group A $\rho = 0.6844$ vs Group C $\rho = 0.2020$).
   - Panel C: Core County Subset Scatterplot ($10-100$ km, $\rho = 0.7724, N=29$).
3. **Figure 3 — Multi-Month Persistence & 3-Month Matrix Timeline (79 Continuous Days)**:
   - Panel A: 3-Month Month-over-Month Matrix (April vs May vs June 2026 across 1,840 US Counties, $\rho > 0.986$).
   - Panel B: 79-Day Daily Spearman correlation $\rho_t^{10-100}$ with reference line ($\rho = 0.5192$).
4. **Figure 4 — Geometry Sensitivity & Prediction Boundary**:
   - Panel A: Partial correlation $\rho_{partial}$ under control sets $G_1 \rightarrow G_2 \rightarrow G_3$ and Opportunity Share $A_{\text{opp}}$.
   - Panel B: Out-of-sample LOCO-CV prediction performance comparison ($Model\ G$ vs $Model\ M$ vs $Model\ G+M$).

---

## 5. Main Tables Architecture (3 Tables)

- **Table 1 — Sample & Spatial Matching Specification**:
  - $N=50$ matched US Metropolitan Study Areas (11,777 census tracts), 7 continuous Meta MDM datasets (79 daily snapshots from `2026-04-01` to `2026-06-23`), LODES seasonal OD baseline.
- **Table 2 — External Validity & Spatial-Support Quality Master Estimands**:
  - All 50 Metros ($N=50$): Spearman $\rho = 0.5452$, Pearson $r = 0.5529$, 95% bootstrap CI [0.2957, 0.7333], Jackknife LOO [0.5168, 0.5902], MAE = 6.61%.
  - Group A Exact Support ($N=25$ Metros): Spearman $\rho = 0.6844$, Pearson $r = 0.6912$, MAE = 6.52%. Group C Approx Support ($N=25$): Spearman $\rho = 0.2020$.
  - Core County Subset ($N=29$): Spearman $\rho = 0.7724$, $p_{\text{perm}} < 0.001$, 25-Metro Independent $\rho = 0.7900$, Cutoff Sensitivity ($8-80$ km & $12-120$ km).
- **Table 3 — Multi-Month Persistence, 3-Month Stability Matrix & Geographic Sensitivity**:
  - 3-Month Month-over-Month Spearman $\rho = 0.9865 - 0.9953$ ($N=1,840$ counties), 79-Day $ICC_{79d} = 0.6573$, $S(1) = 96.30\%$, nested partial correlations ($\rho_{M,O \mid G_1..G_3}$ and $\rho_{M,O \mid A}$), LOCO-CV $R^2$ and MAE.

---

## 6. Formal Contributions Statement for Manuscript Introduction

1. **First**, we externally validate Meta Movement Distribution Maps against seasonal OD distance structure across **50 U.S. metropolitan study areas**. The full-sample association is moderate ($\rho = 0.5452, p = 4.24 \times 10^{-5}, p_{\text{perm}} < 0.001$), but correspondence is substantially stronger under exact spatial-support alignment ($\rho = 0.6844 - 0.7724$), while approximately mapped areas exhibit weak correspondence ($\rho = 0.2020$). This identifies spatial-support compatibility as a key condition for interpreting aggregate privacy-preserving mobility measures.
2. **Second**, we show that this correspondence is persistent over short and multi-month observation horizons: 3-month mobility signatures correlate at $\rho = 0.9865 - 0.9953$ ($p < 0.0001$) across 1,840 U.S. counties over April, May, and June 2026, daily matched-support correlations have a median of $\rho = 0.7616$, close to the full reference estimate, while the 79-day continuous ICC ($ICC_{79d} = 0.6573$) indicates substantial persistent between-place variation.
3. **Third**, we show that Meta–OD correspondence remains positive after adjustment for basic urban morphology and population-opportunity structure ($\rho_{partial} = 0.6680, p = 0.0001$), although Meta does not improve leave-one-city-out predictive performance beyond the geographic baseline in the present sample ($\Delta R^2_{\text{LOCO}} = -0.0223$).
