# Paper 1 Scientific Blueprint: Constitution & Experimental Design

**Status:** FROZEN & APPROVED (Final Manuscript Constitution — Core Analyses Closed)  
**Date:** August 10, 2026  
**Target Venue:** Top-tier Transportation / GIScience / Spatial Data Mining Journal (e.g. Transportation Research Part C / ISPRS Journal / IJGIS)

---

## 1. Working Title & Central Scientific Thesis

### Title (Option A — Selected)
> **External Validity of Meta Movement Distribution Maps: Spatial-Support Sensitivity and Temporal Persistence across 50 U.S. Metropolitan Areas**

### The 3 Pillars of Paper 1's Scientific Narrative
$$\boxed{\mathbf{\text{1. Spatial support strongly conditions validity } (\rho = 0.6844 \text{ vs } 0.2020);}}$$
$$\boxed{\mathbf{\text{2. Temporal aggregation saturates early } (V(16d) \approx V(87d));}}$$
$$\boxed{\mathbf{\text{3. Structural geography explains part—but not all—of the Meta–OD correspondence } (\rho_{partial} = 0.3036).}}$$

### Master Scientific Hook
$$\boxed{\begin{aligned}
&\mathbf{\text{Spatial-support compatibility matters substantially more than temporal aggregation depth for}}\
&\mathbf{\text{the external validity of Meta Movement Distribution Maps: OD correspondence strengthens}}\
&\mathbf{\text{under exact spatial alignment, whereas mobility-distance signatures remain highly persistent}}\
&\mathbf{\text{across daily-to-quarterly observation horizons and gain little from longer averaging.}}
\end{aligned}}$$

### Central Scientific Thesis
$$\boxed{\begin{aligned}
&\text{Across 50 U.S. metropolitan study areas, Meta MDM exhibits moderate and highly robust correspondence}\
&\text{with independent OD distance structure } (\rho = 0.5452, p < 0.0001). \text{ This correspondence is substantially}\
&\text{stronger in strict matched-support analyses } (\rho = 0.6844 - 0.7724) \text{ than approximate mapping } (\rho = 0.2020),\
&\text{persists across 87 observed days spanning full Q2 2026 } (W = 0.9942, \text{MAE} = 0.42\text{ pp}, ICC_{87d} = 0.6573),\
&\text{exhibits early saturation with temporal aggregation, and attenuates but remains positive after jointly}\
&\text{adjusting for measured urban morphology and opportunity structure } (\rho_{partial} = 0.3036, p = 0.0321).
\end{aligned}}$$

---

## 2. Terminology Discipline & Claim Boundaries

| Permitted Terminology | Forbidden / Reviewer-Risk Terminology | Rationale |
| :--- | :--- | :--- |
| **87 observed days spanning full Q2 2026** | 87 continuous days / 100% full Q2 days | Calendar span is 92 days (1 April–1 July 2026) with 87 unique observed dates. |
| **Temporal replication across separate Meta windows** | Independent validation across 3 months | Monthly Meta windows are separate, but all compared to the same seasonal OD reference. |
| **Short and multi-month rank persistence** | Universal temporal stability | April, May, and full June 2026 exhibit near-perfect month-over-month rank concordance ($W = 0.9942$). |
| **Early saturation of external validity** | Temporal aggregation continuously improves validity | Validity plateaus early ($V(16d) \approx V(87d)$); temporal depth adds negligible OD gain. |
| **Modest place-specific residual correspondence** | Strong behavioral latent variable | Residual association $\rho_{partial} = 0.3036$ controls jointly for morphology and opportunity, but is modest in scale. |
| **Residual association $\neq$ incremental predictive utility** | Meta improves out-of-sample flow prediction | Meta carries OD-related structure, but does not improve LOCO prediction beyond structural baseline ($\Delta R^2_{LOCO} = -0.0223$). |

---

## 3. Three Frozen Research Questions & Hypotheses

### RQ1 — External Validity and Spatial-Support Sensitivity (45% Weight)
- **Question:** To what extent do Meta MDM distance shares correspond with seasonal OD distance structure across U.S. metropolitan study areas, and how is this correspondence conditioned by spatial-support compatibility?
- **Hypothesis $H_1$:** Meta's conditional distance shares exhibit positive rank correspondence with independent seasonal OD distance shares ($\rho_{50} = \mathbf{0.5452}$), which is substantially stronger under exact spatial-support alignment ($\rho_{\text{exact}} = \mathbf{0.6844} - \mathbf{0.7724}$) than approximate boundary mapping ($\rho_{\text{approx}} = \mathbf{0.2020}$).

### RQ2 — Temporal Persistence and Aggregation Saturation (20% Weight)
- **Question:** How persistent is the Meta mobility-distance signature from daily to multi-month horizons, and does longer temporal aggregation improve external OD correspondence?
- **Hypothesis $H_2$:** Place-specific spatial differences dominate daily measurement variation across multi-month windows (Kendall's $W = \mathbf{0.9942}$, MAE $= \mathbf{0.42\text{ pp}}$), while external OD validity saturates early ($V_{16d} \approx V_{87d}$), such that extending temporal aggregation depth yields diminishing, essentially negligible gains.

### RQ3 — Structural Explainability and Residual Correspondence (10% Weight)
- **Question:** How much of the observed Meta–OD correspondence can be explained by measurable urban morphology and spatial opportunity structure, and does residual place-specific correspondence remain after these factors are jointly accounted for?
- **Hypothesis $H_3$:** Observable urban morphology ($G_3$) and population-opportunity structure ($A$) account for part of the Meta–OD correspondence (attenuating down the ladder: $0.516 \rightarrow 0.360 \rightarrow 0.342 \rightarrow 0.304$), leaving a modest but statistically detectable residual association ($\rho_{\text{partial}} = \mathbf{0.3036}, p = \mathbf{0.0321}$). This residual association, however, does not translate into improved leave-one-city-out predictive performance ($\Delta R^2_{\text{LOCO}} = -0.0223$).

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
  - **External-validation sample**: 50 U.S. metropolitan study areas (11,777 census tracts).
  - **National temporal-persistence panel**: 1,840 U.S. counties with complete observations across all three monthly windows.
  - 1,095,260 deduplicated US telemetry rows across 9 Meta MDM datasets (87 observed days from 1 April to 1 July 2026), LODES seasonal OD baseline.
- **Table 2 — External Validity & Spatial-Support Quality Master Estimands**:
  - All 50 Metros ($N=50$): Spearman $\rho = 0.5452$, Pearson $r = 0.5529$, 95% bootstrap CI [0.2957, 0.7333], Jackknife LOO [0.5168, 0.5902], MAE = 6.61%.
  - Group A Exact Support ($N=25$ Metros): Spearman $\rho = 0.6844$, Pearson $r = 0.6912$, MAE = 6.52%. Group C Approx Support ($N=25$): Spearman $\rho = 0.2020$.
  - Core County Subset ($N=29$): Spearman $\rho = 0.7724$, $p_{\text{perm}} < 0.001$, 25-Metro Independent $\rho = 0.7900$, Cutoff Sensitivity ($8-80$ km & $12-120$ km).
- **Table 3 — Temporal Persistence, Monthly Replication & Aggregation Saturation**:
  - Balanced 3-Full-Month Panel ($N^* = 1,840$ counties), Kendall $W = 0.9942$, Median Absolute Shift MAE $= 0.42$ pp, 87-Day $ICC_{87d} = 0.6573$, Monthly OD Replication ($\rho_{\text{Apr}} = 0.6813, \rho_{\text{May}} = 0.5928, \rho_{\text{Jun}} = 0.5882$), Early Saturation Curve ($V(16d) = 0.6844 \rightarrow V(87d) = 0.6197$), Joint Partial Spearman $\rho(M, O \mid G_3, A) = 0.3036$ ($p = 0.0321$).

---

## 6. Formal Contributions Statement for Manuscript Introduction

1. **First**, we externally validate Meta Movement Distribution Maps against seasonal OD distance structure across 50 U.S. metropolitan study areas. The full-sample correspondence is moderate ($\rho = 0.545$), while exact-support metropolitan areas exhibit substantially stronger correspondence ($\rho = 0.684$) than approximately mapped areas ($\rho = 0.202$), identifying spatial-support compatibility as an important condition for interpreting aggregate mobility products.
2. **Second**, we characterize temporal persistence and aggregation saturation across 87 observed days spanning April–June 2026. County-level mobility-distance signatures exhibit near-complete rank concordance across monthly windows (Kendall's $W = 0.994$) and small month-to-month level shifts (median absolute difference $= 0.42$ percentage points). Meta–OD correspondence recurs across each monthly Meta window ($\rho = 0.588 - 0.681$), while extending temporal aggregation from 16 to 87 observed days provides no improvement in external validity, indicating early saturation of the OD-relevant spatial signal.
3. **Third**, we assess the structural explainability of Meta–OD correspondence by jointly accounting for observable urban morphology and population-opportunity distance structure. The association attenuates but remains positive after joint adjustment ($\rho_{\text{partial}} = 0.304, p = 0.032$), indicating residual place-specific correspondence not captured by the measured structural covariates. However, this residual association does not translate into improved leave-one-city-out prediction beyond the structural baseline in the present sample ($\Delta R^2_{\text{LOCO}} = -0.0223$).
