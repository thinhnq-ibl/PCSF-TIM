# PhD Proposal Slides (Condensed 12 + 1)

## Slide 1 - Title

# Learning Human Mobility from Aggregate Observations

### Sufficiency of Observable Information and Complementary Urban Context for OD Reconstruction

**PhD Dissertation Proposal**

Core question:

> How much spatial-interaction information can be recovered from incomplete aggregate mobility observations, and what additional observable information is needed for defensible OD reconstruction?

> **Key refs:** Barbosa et al. (2018); Pappalardo et al. (2023)

---

## Slide 2 - Research Motivation

# Why This Topic Matters

Urban planning needs OD information for transport policy, infrastructure, and accessibility design.

But complete OD matrices are often unavailable in data-scarce cities.

$$
\text{Planning demand for OD information}
\gg
\text{Availability of complete OD data}
$$

Research motivation:

- Move from data scarcity to defensible OD inference.
- Build a method that works under incomplete mobility observations.

> **Key refs:** Ortuzar and Willumsen (2011); Barbosa et al. (2018); Pappalardo et al. (2023)

---

## Slide 3 - Practical Problem

# The Core Practical Problem

Complete OD data are costly and difficult to obtain at scale.

Common sources are limited by cost, privacy, access, and coverage stability.

Resulting challenge:

- Cities may have aggregate mobility signals.
- Cities still lack reliable disaggregated OD matrices.

$$
\text{Aggregate observation} \neq \text{Complete OD information}
$$

> **Key refs:** Oliver et al. (2020); Buckee et al. (2020); de Montjoye et al. (2013)

---

## Slide 4 - Scientific Problem Framing

# Information Sufficiency Problem

This dissertation treats OD reconstruction as an information-sufficiency problem.

Main scientific issue:

- What information survives aggregation?
- What is lost?
- What additional information is needed for recovery?

$$
\text{Observation} \rightarrow \text{Recoverable Information} \rightarrow \text{OD Recoverability}
$$

> **Key refs:** Abrahamsson (1998); Cover and Thomas (2006)

---

## Slide 5 - Core Scientific Premises

# Three Premises

1. Aggregate observation is informative but non-identifying at OD level.
2. Matching aggregate input is not equivalent to valid OD reconstruction.
3. Validity requires improvement on unconstrained OD properties.

$$
\text{Input consistency} \neq \text{Reconstruction validity}
$$

> **Key refs:** Abrahamsson (1998); Lenormand et al. (2016); Fotheringham (1981); Liang et al. (2013)

---

## Slide 6 - Research Gap Map

# Where the Gap Remains

Existing literature supports pieces of the puzzle.

The remaining gap is the integrated question:

$$
\text{Aggregate observation constraints}
\rightarrow
\text{What is recoverable}
\rightarrow
\text{How complementary context improves OD reconstruction}
$$

Gap type:

- Synthesis and inference gap under shared observation constraints.

> **Key refs:** Abrahamsson (1998); Merlin (2020); Simini et al. (2021); Gallotti et al. (2024)

---

## Slide 7 - Gap 1

# Gap 1: Observation Sufficiency

Question:

> What OD-relevant information remains recoverable after strong aggregation?

Need:

- Controlled analysis of compression vs recoverability.
- Clear boundary between retained signal and lost fidelity.

> **Key refs:** Merlin (2020); Cover and Thomas (2006)

---

## Slide 8 - Gap 2

# Gap 2: Determinants of Sufficiency

Question:

> How do observation-design choices affect recoverability?

Test dimensions:

- Spatial support
- Bin resolution
- Bin geometry
- Model complexity

$$
\text{Recoverability} = f(\text{support, bins, geometry, complexity})
$$

> **Key refs:** Gallotti et al. (2024); Merlin (2020)

---

## Slide 9 - Gap 3

# Gap 3: Complementary Reconstruction Value

Question:

> How much OD reconstruction improvement is gained from open urban spatial information?

Target quantity:

$$
\Delta \text{CPC}
$$

under fixed aggregate mobility constraints.

Focus is marginal improvement, not just predictive performance.

> **Key refs:** Simini et al. (2021); Rong et al. (2023); Xu et al. (2025)

---

## Slide 10 - Paper 1

# Paper 1: Information Retention in Aggregate Mobility Observations

Research objective:

- Quantify what information is retained and lost after aggregation.

Design:

- Systematic experiments across support, bins, geometry, and complexity.

Expected output:

$$
\text{Observation Compression} \rightarrow \text{Parameter Fidelity / Recoverability Profile}
$$

> **Key refs:** Hyman (1969); Tanner (1961); Fotheringham (1981); Rubio-Herrero and Munuzuri (2023)

---

## Slide 11 - Paper 2

# Paper 2: Complementary Information for OD Reconstruction

Research objective:

- Estimate incremental OD reconstruction value from open spatial context.

Design:

- Combine aggregate mobility observation with open urban features.
- Evaluate marginal gains under the same observation constraints.

Expected output:

$$
\text{Aggregate Mobility Signal} + \text{Open Spatial Context}
\rightarrow
\text{Improved OD Recoverability}
$$

> **Key refs:** Wilson (1971); Simini et al. (2021); Fotheringham (1981)

---

## Slide 12 - Dissertation Scope and Deliverables

# What Will Be Delivered

Scientific deliverables:

- A recoverability map under aggregate observation constraints.
- A framework for observation-sensitivity analysis.
- A complementary-information reconstruction pipeline.
- A defensibility-oriented evaluation logic for reconstructed OD.

Thesis logic:

$$
\text{Observation} \rightarrow \text{Recoverability} \rightarrow \text{Complementary Information} \rightarrow \text{Defensible Reconstruction}
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
