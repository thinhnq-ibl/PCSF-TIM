# Paper 1 Scientific Blueprint: Constitution & Experimental Design

**Status:** Frozen & Approved (Post-Audit: Full Q2 87-Day Audit & Joint Partial Model Enforced)  
**Date:** August 10, 2026  
**Target Venue:** Top-tier Transportation / GIScience / Spatial Data Mining Journal (e.g. Transportation Research Part C / ISPRS Journal / IJGIS)

---

## 1. Working Title & Central Scientific Thesis

### Title (Option A — Selected)
> **External Validity of Meta Movement Distribution Maps: Spatial-Support Sensitivity and Temporal Persistence across 50 U.S. Metropolitan Areas**

### Master Scientific Hook
$$\boxed{\begin{aligned}
&\mathbf{\text{Spatial-support compatibility matters far more than temporal aggregation depth for the}}\
&\mathbf{\text{external validity of Meta Movement Distribution Maps: OD correspondence is substantially}}\
&\mathbf{\text{stronger under exact support alignment, whereas the mobility-distance signature itself}}\
&\mathbf{\text{remains highly persistent across daily-to-multi-month observation windows and gains little}}\
&\mathbf{\text{from longer averaging.}}
\end{aligned}}$$

### Central Scientific Thesis
$$\boxed{\begin{aligned}
&\text{Across 50 U.S. metropolitan study areas, Meta MDM exhibits moderate and highly robust correspondence}\
&\text{with independent OD distance structure } (\rho = 0.5452, p < 0.0001). \text{ This correspondence is substantially}\
&\text{stronger in strict matched-support analyses } (\rho = 0.6844 - 0.7724) \text{ than approximate mapping } (\rho = 0.2020),\
&\text{persists across 87 observed days spanning full Q2 2026 } (W = 0.9942, \text{MAE} = 0.42\text{ pp}, ICC_{87d} = 0.6573),\
&\text{exhibits early saturation with temporal aggregation, and remains positive after jointly adjusting for}\
&\text{measured urban morphology and population-opportunity structure } (\rho_{partial} = 0.3036, p = 0.0321).
\end{aligned}}$$

---

## 2. Terminology Discipline & Claim Boundaries

| Permitted Terminology | Forbidden / Reviewer-Risk Terminology | Rationale |
| :--- | :--- | :--- |
| **87 observed days spanning full Q2 2026** | 87 continuous days | Calendar span is 92 days (1 April–1 July 2026) with 87 unique observed dates. |
| **Short and multi-month rank persistence** | Universal temporal stability | April, May, and full June 2026 exhibit near-perfect month-over-month rank concordance ($W = 0.9942$). |
| **Early saturation of external validity** | Temporal aggregation continuously improves validity | Validity plateaus early ($V(16d) \approx V(87d)$); temporal depth adds negligible OD gain. |
| **Median absolute level shift (MAE = 0.42 pp)** | Meta values are temporally invariant | Ranks and magnitudes remain remarkably persistent over 3 full months with minimal shift. |
| **Product-level spatial mobility signature** | Individual population behavioral preference | Meta pings reflect aggregated movement profiles, not isolated individual cognition. |
| **Matched spatial-support validity** | OD matrix reconstruction | Paper 1 validates distance-decay structure, not full destination-pair topology. |
| **Residual Meta–OD correspondence** | Proven behavioral signal | Residual association $\rho_{partial} = 0.3036$ controls jointly for morphology and opportunity, not all omitted variables. |

---

## 3. Re-balanced Contribution Weights & Three Frozen Research Questions

### Contribution Weights Allocation
- **45% External Validity**: Full-sample baseline across 50 US metropolitan study areas ($\rho_{50} = \mathbf{0.5452}, p < 0.0001, p_{\text{perm}} < 0.001$). Exact-support metro analysis yielded $\rho = \mathbf{0.6844}$ ($N=25$); a complementary matched-county analysis yielded $\rho = \mathbf{0.7724}$ ($N=29$).
- **25% Spatial-Support Sensitivity**: Strong evidence consistent with spatial-support mismatch driving attenuation ($\rho_A = \mathbf{0.6844}$ vs $\rho_C = \mathbf{0.2020}, \Delta \rho = \mathbf{0.4824}, \beta_3 = \mathbf{+0.6050}$). Group B ($N=3$) treated as descriptive only due to sample size.
- **20% Temporal Persistence & Aggregation Saturation**: 3-full-month Kendall $W = \mathbf{0.9942}$, median absolute shift MAE $= \mathbf{0.42\text{ pp}}$, $ICC_{87d} = \mathbf{0.6573}$, monthly replication ($\rho_{\text{Apr}} = 0.6813, \rho_{\text{May}} = 0.5928, \rho_{\text{Jun}} = 0.5882$), early saturation plateau ($V(16d) \approx V(87d)$).
- **10% Structural & Opportunity Robustness**: Joint Partial Spearman $\rho(M, O \mid G_3, A) = \mathbf{0.3036}$ ($p = \mathbf{0.0321}$), LOCO-CV prediction boundary condition ($\Delta R^2_{LOCO} = -0.0223$).

---

## 4. Main Figures Architecture (4 Figures)

1. **Figure 1 — Spatial Support & Measurement Framework Diagram**:
   - Visualizing tract-to-county spatial aggregation ($OD_{ab}^{tract} \rightarrow OD_{ij}^{county}$) and the conceptual decomposition $M_{i,t} = \mu_i + \delta_{i,t}$.
2. **Figure 2 — Primary External Validity Scatterplots & Spatial-Support Stratification**:
   - Panel A: All 50 Metropolitan Study Areas Scatterplot ($\rho = 0.5452, r = 0.5529, N=50$).
   - Panel B: Spatial-Support Stratification Comparison (Group A $\rho = 0.6844$ vs Group C $\rho = 0.2020$).
   - Panel C: Core County Subset Scatterplot ($10-100$ km, $\rho = 0.7724, N=29$).
3. **Figure 3 — Temporal Persistence, Monthly Replication & Early Saturation Timeline**:
   - Panel A: 3-Full-Month Rank Concordance Scatterplot (April vs May vs Full June 2026 across 1,840 US Counties, $W = 0.9942$).
   - Panel B: Early Saturation Curve comparing $V(16d) \rightarrow V(57d) \rightarrow V(87d)$ across aggregation depths.
4. **Figure 4 — Geometry Sensitivity & Prediction Boundary**:
   - Panel A: Partial correlation $\rho_{partial}$ under control sets $G_1 \rightarrow G_2 \rightarrow G_3$ and Joint Model $(G_3 + A)$.
   - Panel B: Out-of-sample LOCO-CV prediction performance comparison ($Model\ G$ vs $Model\ M$ vs $Model\ G+M$).

---

## 5. Main Tables Architecture (3 Tables)

- **Table 1 — Sample, Spatial Matching & Deduplication Specification**:
  - $N=50$ matched US Metropolitan Study Areas (11,777 census tracts), 1,095,260 deduplicated US telemetry rows across 9 Meta MDM datasets (87 observed days from 1 April to 1 July 2026), LODES seasonal OD baseline.
- **Table 2 — External Validity & Spatial-Support Quality Master Estimands**:
  - All 50 Metros ($N=50$): Spearman $\rho = 0.5452$, Pearson $r = 0.5529$, 95% bootstrap CI [0.2957, 0.7333], Jackknife LOO [0.5168, 0.5902], MAE = 6.61%.
  - Group A Exact Support ($N=25$ Metros): Spearman $\rho = 0.6844$, Pearson $r = 0.6912$, MAE = 6.52%. Group C Approx Support ($N=25$): Spearman $\rho = 0.2020$.
  - Core County Subset ($N=29$): Spearman $\rho = 0.7724$, $p_{\text{perm}} < 0.001$, 25-Metro Independent $\rho = 0.7900$, Cutoff Sensitivity ($8-80$ km & $12-120$ km).
- **Table 3 — Temporal Persistence, Monthly Replication & Aggregation Saturation**:
  - Balanced 3-Full-Month Panel ($N^* = 1,840$ counties), Kendall $W = 0.9942$, Median Absolute Shift MAE $= 0.42$ pp, 87-Day $ICC_{87d} = 0.6573$, Monthly OD Replication ($\rho_{\text{Apr}} = 0.6813, \rho_{\text{May}} = 0.5928, \rho_{\text{Jun}} = 0.5882$), Early Saturation Curve ($V(16d) = 0.6844 \rightarrow V(87d) = 0.6197$), Joint Partial Spearman $\rho(M, O \mid G_3, A) = 0.3036$ ($p = 0.0321$).

---

## 6. Formal Contributions Statement for Manuscript Introduction

1. **First**, we externally validate Meta Movement Distribution Maps against seasonal OD distance structure across 50 U.S. metropolitan study areas. The full-sample correspondence is moderate ($\rho = 0.545$), while exact-support metropolitan areas exhibit substantially stronger correspondence ($\rho = 0.684$) than approximately mapped areas ($\rho = 0.202$), identifying spatial-support compatibility as an important condition for interpreting aggregate mobility products.
2. **Second**, we characterize temporal persistence and aggregation saturation across 87 observed days spanning April through June 2026. County-level signatures exhibit near-complete rank concordance across monthly windows ($W = 0.994$) and small month-to-month absolute shifts (median $0.42$ percentage points). Meta–OD correspondence recurs across each monthly observation window, while longer temporal aggregation yields little additional external validity.
3. **Third**, we assess structural robustness by adjusting Meta–OD correspondence for observable urban morphology and population-opportunity distance structure. Positive residual associations persist under each adjustment and under joint adjustment ($\rho_{\text{partial}} = 0.3036, p = 0.0321$), although adding Meta does not improve leave-one-city-out prediction beyond the geographic baseline in the current sample.
