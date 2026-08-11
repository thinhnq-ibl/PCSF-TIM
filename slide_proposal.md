# PhD Proposal Slides (Condensed 12 + 1)

## Slide 1 - Title

# Recovering Origin-Destination Flows from Aggregate Mobility Observations

### Information Sufficiency, Observation Design, and Complementary Urban Context

**PhD Dissertation Proposal**

Core question:

> How much spatial-interaction information can be recovered from incomplete aggregate mobility observations, and what additional observable information is needed for defensible OD reconstruction?

> **Key refs:** Barbosa et al. (2018); Pappalardo et al. (2023)

---

## Slide 2 - Research Motivation

# The Planning Need

Urban planning needs OD information for transport policy, infrastructure, and accessibility design.

But complete OD matrices are often unavailable in data-scarce cities.

$$
\text{Planning demand for OD information}
\gg
\text{Availability of complete OD data}
$$

Research motivation:

- Move from missing OD data to defensible OD inference.
- Study what can be supported by incomplete observations before claiming reconstruction.

> **Key refs:** Ortuzar and Willumsen (2011); Barbosa et al. (2018); Pappalardo et al. (2023)

---

## Slide 3 - Practical Problem

# The Observation Problem

Complete OD data are costly and difficult to obtain at scale.

Common sources are limited by cost, privacy, access, and coverage stability.

Resulting challenge:

- Cities may observe only aggregate mobility statistics.
- Cities still lack reliable disaggregated OD matrices.

Examples of incomplete observations:

- Distance-binned movement summaries.
- Mobility indices and marginals.
- Partial traffic or boarding counts.

$$
\text{Aggregate observation} \neq \text{Complete OD information}
$$

> **Key refs:** Oliver et al. (2020); Buckee et al. (2020); de Montjoye et al. (2013)

---

## Slide 4 - Scientific Problem Framing

# Conceptual Breakthrough

This dissertation treats OD reconstruction as an observation-and-identifiability problem.

Conceptual representation:

$$
\boxed{\mathbf{T}}
\xrightarrow{A}
\boxed{\mathbf{Y}}
$$

where:

- $\mathbf{T}$ = latent OD flow matrix.
- $A$ = aggregation / observation operator.
- $\mathbf{Y}$ = observed aggregate mobility statistics.

Core problem:

$$
A(\mathbf{T}_1)=A(\mathbf{T}_2)
\quad \text{while} \quad
\mathbf{T}_1 \neq \mathbf{T}_2
$$

$$
\mathrm{Observation\ consistency} \neq \mathrm{OD\ identification}
$$

> **Key refs:** Abrahamsson (1998); Cover and Thomas (2006)

---

## Slide 5 - Core Scientific Premises

# Evaluation Principle

1. Aggregate observation is informative but non-identifying at OD level.
2. Matching the observed aggregate input is not equivalent to valid OD reconstruction.
3. A reconstruction should be evaluated on OD properties that were not directly used as fitting constraints.

If the input constrains only an aggregate distance statistic such as $P(d)$, matching $P(d)$ is not independent validation.

Defensible validation should also examine unconstrained OD properties such as:

- OD overlap.
- Origin and destination marginals.
- Flow concentration.
- Network structure.
- Spatial heterogeneity.

$$
\text{Input consistency} \neq \text{Reconstruction validity}
$$

> **Key refs:** Abrahamsson (1998); Lenormand et al. (2016); Fotheringham (1981); Liang et al. (2013)

---

## Slide 6 - Research Gap Map

# What Existing Research Has Solved

Existing studies have established important components of the problem:

- Spatial interaction models can generate OD flows.
- Deep learning models can use urban and geographic features to predict flows.
- Aggregate mobility datasets provide useful but distorted partial views of mobility systems.

$$
\mathrm{Known\ pieces} \neq \mathrm{the\ missing\ scientific\ answer}
$$

What remains unknown is:

- What OD structure is identifiable from a specified aggregate observation.
- Which observation-design choices determine that recoverability.
- How much additional information each complementary observable source contributes once the aggregate observation is held fixed.

Gap type:

- An identifiability and incremental-information gap in OD reconstruction under aggregate observation constraints.

> **Key refs:** Abrahamsson (1998); Merlin (2020); Simini et al. (2021); Gallotti et al. (2024)

---

## Slide 7 - Gap 1

# Three Unanswered Questions

This proposal organizes the gap as a progression:

$$
\boxed{
\mathrm{Can\ we\ recover?}
\rightarrow
\mathrm{When\ can\ we\ recover?}
\rightarrow
\mathrm{What\ helps\ us\ recover\ more?}
}
$$

Gap 1 — Identifiability

Question:

> What OD information is recoverable from aggregate observations at all?

Gap 2 — Observation Design

> Which properties of the observation determine that recoverability?

Gap 3 — Information Complementarity

> What additional observable information reduces the remaining reconstruction uncertainty?

Need:

- A controlled recoverability map.
- A defensible dependency structure across the full thesis.

> **Key refs:** Merlin (2020); Cover and Thomas (2006)

---

## Slide 8 - Gap 2

# Validation Architecture

Level 1 — Controlled benchmark setting

$$
\mathbf{T}^{GT}
\xrightarrow{A}
\mathbf{Y}
\xrightarrow{\text{reconstruction}}
\hat{\mathbf{T}}
$$

Because $\mathbf{T}^{GT}$ is known, recoverability can be measured directly.

Level 2 — Real data-scarce city

$$
\mathbf{Y}_{\text{real}} + \mathbf{X}_{\text{urban}}
\xrightarrow{\text{reconstruction}}
\hat{\mathbf{T}}_{\text{real}}
$$

Then evaluate with independent partial observations rather than the fitting constraint itself.

Why this matters:

- Level 1 establishes the recoverability boundary.
- Level 2 establishes real-world external defensibility.

$$
\mathrm{controlled\ validity} + \mathrm{external\ validation}
$$

> **Key refs:** Gallotti et al. (2024); Merlin (2020)

---

## Slide 9 - Gap 3

# Unified Research Framework

Latent system:

$$
\mathbf{T}
\xrightarrow{A}
\mathbf{Y}
$$

Paper 1 asks:

$$
R(\mathbf{T} \mid \mathbf{Y})
$$

Paper 2 asks:

$$
\Delta R
=
R(\hat{\mathbf{T}}_{\mathbf{Y},\mathbf{X}}, \mathbf{T})
-
R(\hat{\mathbf{T}}_{\mathbf{Y}}, \mathbf{T})
$$

where $\mathbf{X}$ denotes complementary urban context.

Interpretation:

- Paper 1 establishes the information ceiling under observation alone.
- Paper 2 tests whether complementary observables close the remaining gap.

This makes the PhD one integrated inference program rather than two loosely related projects.

> **Key refs:** Fotheringham (1981); Simini et al. (2021); Gallotti et al. (2024)

---

## Slide 10 - Paper 1

# Paper 1: Recoverability Boundary

Research objective:

- Determine what OD-relevant information survives aggregation.
- Distinguish retained signal from lost fidelity.

Design:

- Controlled experiments with known OD ground truth.
- Systematic variation in spatial support, bin resolution, bin geometry, and model complexity.

Scientific output:

$$
R = f(\mathrm{support}, \mathrm{resolution}, \mathrm{geometry}, \mathrm{model\ flexibility})
$$

Expected contribution:

- A recoverability map under aggregate observation constraints.
- A principled boundary for when observation-only reconstruction becomes unreliable.

> **Key refs:** Hyman (1969); Tanner (1961); Fotheringham (1981); Rubio-Herrero and Munuzuri (2023)

---

## Slide 11 - Paper 2

# Paper 2: Complementary Information and HCMC Testbed

Research objective:

- Estimate the conditional value of complementary urban information once the aggregate observation is held fixed.
- Deploy the framework in a real data-scarce urban testbed.

Design:

- Compare $R(\hat{\mathbf{T}}_{\mathbf{Y}}, \mathbf{T})$ against $R(\hat{\mathbf{T}}_{\mathbf{Y},\mathbf{X}}, \mathbf{T})$.
- Use open urban features as auxiliary observables.
- Use Ho Chi Minh City as the empirical testbed for external validation with independent partial observations.

Expected output:

$$
\Delta R
=
R(\hat{\mathbf{T}}_{\mathbf{Y},\mathbf{X}}, \mathbf{T})
-
R(\hat{\mathbf{T}}_{\mathbf{Y}}, \mathbf{T})
$$

Operationally, $R$ can be evaluated using CPC and complementary unconstrained OD properties rather than a single metric alone.

> **Key refs:** Wilson (1971); Simini et al. (2021); Rong et al. (2023); Xu et al. (2025)

---

## Slide 12 - Dissertation Scope and Deliverables

# PhD Contribution

Scientific deliverables:

- A framework for determining what OD structure is supported by incomplete observations.
- A recoverability boundary under explicit observation-design choices.
- An estimate of the conditional value of complementary urban context.
- A validation architecture combining controlled benchmarks and real-world external checks.

Closing claim:

> The contribution is not another OD prediction model. It is a framework for determining what OD structure is supported by incomplete observations, when reconstruction becomes unreliable, and which additional observable information makes it more defensible.

Thesis logic:

$$
\mathrm{Incomplete\ Observation}
\rightarrow
\mathrm{Information\ Sufficiency}
\rightarrow
\mathrm{OD\ Recoverability}
\rightarrow
\mathrm{Complementary\ Information}
$$

> **Key refs:** Abrahamsson (1998); Fotheringham (1981); Simini et al. (2021); Liang et al. (2013)

---

## Slide 13 - References

# References (Used Across Slides 1-12)

- Abrahamsson, T. (1998). Estimation of Origin-Destination Matrices Using Traffic Counts: A Literature Survey. IIASA Interim Report IR-98-021.
- Barbosa, H., et al. (2018). Human mobility: Models and applications. Physics Reports, 734, 1-74.
- Buckee, C. O., et al. (2020). Aggregated mobility data could help fight COVID-19. Science, 368, eabb8021.
- Cover, T. M., and Thomas, J. A. (2006). Elements of Information Theory (2nd ed.). Wiley.
- de Montjoye, Y.-A., Hidalgo, C. A., Verleysen, M., and Blondel, V. D. (2013). Unique in the Crowd: The privacy bounds of human mobility. Scientific Reports, 3, 1376.
- Fotheringham, A. S. (1981). Spatial structure and distance-decay parameters. Annals of the Association of American Geographers, 71(3), 425-436. https://doi.org/10.1111/j.1467-8306.1981.tb01367.x
- Gallotti, R., Maniscalco, D., Barthelemy, M., and De Domenico, M. (2024). Distorted insights from human mobility data. Communications Physics, 7, 421.
- Hyman, G. M. (1969). The calibration of trip distribution models. Environment and Planning, 1, 105-112.
- Lenormand, M., Bassolas, A., and Ramasco, J. J. (2016). Systematic comparison of trip distribution laws and models. Journal of Transport Geography, 51, 158-169.
- Liang, X., Zhao, J., Dong, L., and Xu, K. (2013). Unraveling the origin of exponential law in intra-urban human mobility. Scientific Reports, 3, 2983. https://doi.org/10.1038/srep02983
- Merlin, L. A. (2020). A new method using medians to calibrate single-parameter spatial interaction models. Journal of Transport and Land Use, 13(1), 49-70.
- Oliver, N., et al. (2020). Mobile phone data for informing public health actions across the COVID-19 pandemic lifecycle. Science Advances, 6(23), eabc0764.
- Ortuzar, J. de D., and Willumsen, L. G. (2011). Modelling Transport (4th ed.). Wiley.
- Pappalardo, L., Manley, E., Sekara, V., and Alessandretti, L. (2023). Future directions in human mobility science. Nature Computational Science, 3, 588-600.
- Rong, C., Feng, J., and Ding, J. (2023). GODDAG: Generating origin-destination flow for new cities via domain adversarial training. IEEE Transactions on Knowledge and Data Engineering, 35(10), 10048-10057.
- Rubio-Herrero, J., and Munuzuri, J. (2023). Sparse regression for data-driven deterrence functions in gravity models. Annals of Operations Research, 323, 153-174.
- Simini, F., Barlacchi, G., Luca, M., and Pappalardo, L. (2021). A Deep Gravity model for mobility flows generation. Nature Communications, 12, 6576.
- Tanner, J. C. (1961). Factors Affecting the Amount of Travel. Road Research Technical Paper No. 51.
- Wilson, A. G. (1971). A family of spatial interaction models, and associated developments. Environment and Planning A, 3(1), 1-32.
- Xu, Y., et al. (2025). Predicting human mobility flows in cities using deep learning on satellite imagery. Nature Communications, 16, 10372.
