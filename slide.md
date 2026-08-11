# PhD Proposal Slides

## Slide 1 — Title

# Learning Human Mobility from Aggregate Observations

### Sufficiency of Observable Information and Complementary Urban Context for Origin–Destination Matrix Reconstruction

**PhD Dissertation Proposal**

**Core scientific focus**

> How much spatial-interaction information can be recovered from incomplete aggregate mobility observations, and what additional observable information is required for defensible OD reconstruction?

---

## Slide 2 — Practical Problem

# Complete OD Matrices Are Rare Where They Are Needed Most

Urban planning requires knowledge of how people move between locations.

However, comprehensive OD matrices are expensive to obtain because they traditionally depend on:

* Household travel surveys
* Mobile-phone trajectories
* GPS/LBS observations
* Smart-card systems
* Large-scale transport surveys

This creates a major problem for data-scarce cities, particularly in the Global South.

### Practical setting

$$
\text{Urban planning need}
\quad \gg \quad
\text{Availability of complete OD data}
$$

**Ho Chi Minh City is used as the external data-scarce case study.**

Key refs: Ortúzar & Willumsen (2011); Barbosa et al. (2018); Pappalardo et al. (2023)

Dùng cho:

vai trò của OD/travel-demand information trong planning;
sự đa dạng và hạn chế của mobility data;
data availability, representativeness và privacy challenges.

---

## Slide 3 — New Observation Opportunity

# Aggregate Mobility Data Are Increasingly Available

Modern mobility products provide population-level movement observations without releasing detailed individual trajectories.

A prominent example is:

**Meta Movement Distribution Maps (MDM)**

These data provide highly compressed representations of movement, including coarse distance-based movement distributions.

Conceptually:

$$
OD
\longrightarrow
Aggregate\ Mobility\ Observation
$$

But aggregation removes information.

Therefore:

$$
\boxed{
Aggregate\ Observation
\neq
Complete\ Mobility\ Information
}
$$

Key refs: Oliver et al. (2020); Buckee et al. (2020); de Montjoye et al. (2013); Meta Movement Distribution Maps documentation

Dùng cho:

aggregate mobility products;
population-level mobility indicators;
lý do giảm granularity thay vì release individual trajectories.

Lưu ý wording: Không nói aggregation = privacy-safe.
---

## Slide 4 — The Scientific Problem

# What Information Survives Aggregation?

The key scientific issue is not simply whether aggregate mobility data are useful.

The deeper question is:

> **What OD-relevant information remains recoverable after mobility observations have been compressed?**

And if the observation is insufficient:

> **What additional observable information is required to reconstruct OD flows?**

This dissertation therefore reframes OD reconstruction as an:

# Information Sufficiency Problem

---
Key refs: Abrahamsson (1998); Cover & Thomas (2006)

Dùng cho:

incomplete observation / OD inverse problem;
conceptual background cho information loss.

Cover & Thomas chỉ là general information-theory foundation, không phải mobility evidence.

## Slide 5 — Scientific Backbone

# Seven-Stage Scientific Backbone

$$
\boxed{
Observation
\rightarrow
Recoverable\ Information
\rightarrow
Observation\ Sensitivity
\rightarrow
Underdetermination
\rightarrow
Complementary\ Context
\rightarrow
OD\ Reconstruction
\rightarrow
Independent\ Validation
}
$$

The dissertation does not assume that mobility can be cleanly separated into independently identifiable structural and behavioural components.

Instead, it studies what can be inferred from **different observable information sources**.

Key refs: Abrahamsson (1998); Fotheringham (1981); DeepGravity — Simini et al. (2021)

Ba nguồn hỗ trợ ba phần khác nhau:

partial observation → underdetermination;
estimated distance effects depend on spatial configuration;
complementary geographic context contributes predictive information.

Backbone tổng thể là synthesis của dissertation, không claim một paper đã đề xuất chuỗi này.
---

## Slide 6 — Three Core Scientific Premises

# Core Premises

### Premise 1

$$
\boxed{
Aggregate\ Observation
\neq
Complete\ Information
}
$$

Aggregation compresses OD information.

### Premise 2

$$
\boxed{
Input\ Consistency
\neq
Reconstruction\ Validity
}
$$

A reconstructed OD matrix may reproduce the input aggregate statistics while still having incorrect spatial allocation.

### Premise 3

$$
\boxed{
Validity\ Requires\ Improvement\ on\ Unconstrained\ OD\ Properties
}
$$

Evaluation must therefore examine information not directly imposed by the model inputs.

Aggregate Observation ≠ Complete Information

Refs: Cover & Thomas (2006); Gallotti et al. (2024)

Input Consistency ≠ Reconstruction Validity

Refs: Abrahamsson (1998); Lenormand et al. (2016)

Validity Requires Unconstrained Evaluation

Refs: Lenormand et al. (2016)

Premise thứ ba chủ yếu là dissertation evaluation principle, không nên nói literature đã chứng minh nguyên văn.

---

## Slide 7 — Literature Baseline

# What Existing Research Already Solves

Several mature research streams are directly relevant.

### Spatial Interaction Models

Wilson and subsequent work established constrained gravity models and distance deterrence as classical representations of spatial interaction.

### OD Estimation

Traditional OD estimation demonstrates that recovering a high-dimensional OD matrix from partial observations is generally an underdetermined inverse problem.

### Reduced-Information Calibration

Merlin (2020) demonstrates that even highly reduced summaries such as median travel time can support calibration of a single impedance parameter when the remaining spatial system is known.

### Geographic Flow Prediction

DeepGravity and related models demonstrate that population, POIs, roads, land use, and other geographic information improve mobility-flow prediction.

Key refs:

Wilson (1971)
Hyman (1969)
Flowerdew & Aitkin (1982)
Abrahamsson (1998)
Merlin (2020)
Simini et al. (2021)

Mapping:

Spatial Interaction
→ Wilson (1971)

Classical calibration
→ Hyman (1969); Flowerdew & Aitkin (1982)

OD estimation from incomplete observations
→ Abrahamsson (1998)

Reduced-information calibration
→ Merlin (2020)

Geographic flow prediction
→ Simini et al. (2021)

---

## Slide 8 — Important Literature Warning

# Aggregate Distance Patterns Are Not Pure Behaviour

Fotheringham showed that estimated distance-decay parameters depend on spatial configuration.

Liang et al. (2013) further demonstrated that an exponential urban trip-length distribution can arise from the spatial organization of population even when the underlying deterrence specification is not exponential.

Therefore:

$$
\boxed{
Observed\ Distance\ Distribution
\neq
Pure\ Behavioural\ Preference
}
$$

Distance-decay parameters in this dissertation are therefore used as:

> **interpretable probes of recoverable distance-related interaction information**

rather than ground-truth behavioural parameters.

Key refs: Fotheringham (1981); Liang et al. (2013)

Suggested footer:

Key refs: Fotheringham (1981); Liang et al. (2013)

Fotheringham supports:

$$
\hat{\theta}
\text{ depends on spatial configuration}
$$

Liang supports:

$$
Urban\ population\ structure
\rightarrow
aggregate\ trip\text{-}length\ pattern
$$

This is one of the most important citation pairs in the whole defense.

---

## Slide 9 — Research Gap

# Where Is the Remaining Gap?

Existing studies separately address:

$$
Partial\ Observations
\rightarrow
OD\ Estimation
$$

and:

$$
Urban\ Geographic\ Features
\rightarrow
Mobility\ Flow\ Prediction
$$

But less systematic attention has been given to:

$$
\boxed{
Observation
\rightarrow
Recoverable\ Information
\rightarrow
Complementary\ Information
\rightarrow
OD\ Recoverability
}
$$

under the **same aggregate observation constraints**.

Key refs: Abrahamsson (1998); Merlin (2020); Rubio-Herrero & Muñuzuri (2023); Simini et al. (2021); Gallotti et al. (2024)

This slide should make clear that the gap is a synthesis gap.

Suggested footer:

Positioned against: Abrahamsson (1998); Merlin (2020); Rubio-Herrero & Muñuzuri (2023); Simini et al. (2021); Gallotti et al. (2024)
---

## Slide 10 — Gap 1

# Gap 1 — Observation Sufficiency

### Scientific Question

> **What OD-relevant information survives highly compressed aggregate mobility observations?**

Existing work shows that reduced mobility summaries can retain useful calibration information.

However, we know less about how much spatial-interaction information remains available after strong aggregation such as coarse binned travel-distance observations.

Paper 1 therefore asks:

$$
OD
\rightarrow
Compressed\ Observation
\rightarrow
What\ remains\ recoverable?
$$

Key refs: Merlin (2020); Cover & Thomas (2006)

Most important contrast:

Merlin (2020) demonstrates reduced-summary calibration for a single parameter when complete spatial information is available; this dissertation studies systematic recoverability under explicitly controlled aggregation/compression.

Do not imply Merlin already solves the TLD problem.

---

## Slide 11 — Gap 2

# Gap 2 — Determinants of Observation Sufficiency

Recoverability may depend not only on the amount of data, but also on **how the observation is designed**.

This dissertation systematically studies:

$$
\text{Spatial Support}
$$

$$
\text{Bin Resolution}
$$

$$
\text{Bin Geometry}
$$

$$
\text{Model Complexity}
$$

### Question

> How do these observation-design choices affect parameter recoverability?

Key refs: Gallotti et al. (2024); Merlin (2020)

Gallotti supports the general proposition that observed mobility patterns depend on measurement/data-generation processes.

The specific axes:

$$
support,\ bin\ count,\ bin\ geometry,\ complexity
$$

are primarily your dissertation design.

Footer:

Motivated by: Merlin (2020); Gallotti et al. (2024).
Tested here: T28–T30, T35.

---

## Slide 12 — Gap 3

# Gap 3 — Complementary Reconstruction Value

When the aggregate observation is insufficient to determine OD allocation uniquely:

> **How much reconstruction improvement is obtained from adding open urban spatial information?**

Open information includes:

* Population
* POIs
* Road networks
* Land use
* Accessibility
* Other geographic context

The focus is not simply whether these variables improve prediction.

The focus is:

$$
\boxed{
Marginal\ Reconstruction\ Improvement
}
$$

under fixed aggregate mobility constraints.

Key refs: Simini et al. (2021); Xu et al. (2025, Imagery2Flow); Rong et al. (2023, GODDAG)

Use these to acknowledge that:

$$
Urban\ context
\rightarrow
better\ flow\ prediction
$$

is already established.

Your gap is the marginal value conditional on the same incomplete aggregate mobility observation.
---

## Slide 13 — Paper 1

# Paper 1 — Information Retention in Aggregate Mobility Observations

### Research Question

> **How does the design of an aggregate mobility observation determine what spatial-interaction information remains recoverable?**

### Experimental dimensions

$$
Spatial\ Support
\times
Bin\ Resolution
\times
Bin\ Geometry
\times
Model\ Complexity
$$

### Output

A systematic characterization of:

$$
Observation\ Compression
\rightarrow
Parameter\ Fidelity
$$

Key refs: Hyman (1969); Merlin (2020); Fotheringham (1981)

Footer:

Methodological baseline: Hyman (1969); Merlin (2020).
Interpretation caution: Fotheringham (1981).
---

## Slide 14 — Paper 1 Information Probes

# Three-Tier Information Probe Architecture

### Primary Probe — Exponential

$$
f(d)=e^{-\beta d}
$$

One parameter, simple interpretation, stable short-distance behavior.

### Robustness Probe — Power Law

$$
f(d)=d^{-\alpha}
$$

Same parameter complexity, different functional assumption.

### Complexity Stress Test — Tanner

$$
f(d)=d^{-\alpha}e^{-\beta d}
$$

Two parameters, used to examine whether richer parameterization demands more observational information.

Key refs: Hyman (1969); Haynes & Fotheringham (1984); Tanner (1961); Merlin (2020); Rubio-Herrero & Muñuzuri (2023)

Mapping:

Exponential → classical deterrence literature
Power → classical deterrence literature
Tanner → Tanner (1961)
functional-form flexibility → Rubio-Herrero & Muñuzuri (2023)

Suggested footer:

Deterrence-function background: Tanner (1961); Hyman (1969); Haynes & Fotheringham (1984); Rubio-Herrero & Muñuzuri (2023)

---

## Slide 15 — Paper 1 Preliminary Evidence

# Compression Produces Quantifiable Information Degradation

Chicago compression experiment:

$$
20
\rightarrow
10
\rightarrow
5
\rightarrow
3
\rightarrow
2
\rightarrow
1\ bins
$$

For the exponential probe:

* 20-bin error: approximately **0.77%**
* 3-bin error: approximately **44.4%**
* 1-bin: complete collapse

### Key interpretation

$$
\boxed{
Signal\ Retention
\neq
Parameter\ Fidelity
}
$$

Coarse observations may retain meaningful distance-related information while losing quantitative precision.
Source: Dissertation preliminary experiment T29.

No external citation necessary for the numerical findings.

Optional literature context:

Context: Merlin (2020); Gallotti et al. (2024).
Source of results: Dissertation T29.

---

## Slide 16 — Bin Geometry Matters

# Information Depends on Bin Geometry, Not Only Bin Count

T30 shifts the three-bin cut points by approximately ±20%.

Result:

$$
Parameter\ Error:
55.5%
\rightarrow
33.3%
$$

depending on cut-point configuration.

Therefore:

$$
\boxed{
Observation\ Sufficiency
========================

f(
Resolution,
Geometry,
Support
)
}
$$

Not all three-bin representations contain the same information.


Source: Dissertation preliminary experiment T30.

Optional:

Measurement-process context: Gallotti et al. (2024).
Source: Dissertation T30.

---

## Slide 17 — Functional-Form Robustness

# Compression Effects Are Not Unique to Exponential Deterrence

Chicago T35:

### Exponential

$$
0.77%
\rightarrow
44.4%
$$

### Power Law

$$
25.9%
\rightarrow
36.9%
$$

### Tanner

$$
65.3%
\rightarrow
96.2%
$$

### Preliminary interpretation

Compression-induced parameter degradation occurs across alternative deterrence specifications.

The Tanner results additionally suggest that:

$$
Higher\ Parameterization
\rightarrow
Greater\ Information\ Demand
$$

This remains a case-study hypothesis rather than a universal claim.

Key refs: Tanner (1961); Hyman (1969); Rubio-Herrero & Muñuzuri (2023)

Empirical source: Dissertation T35.

Footer:

Function background: Tanner (1961); Hyman (1969); Rubio-Herrero & Muñuzuri (2023).
Preliminary evidence: T35, Chicago.

---

## Slide 18 — Underdetermination

# Aggregate Distance Information Does Not Determine OD Topology

A key control experiment constructs two OD matrices with:

$$
JSD(TLD_1,TLD_2)=0
$$

but:

$$
CPC(OD_1,OD_2)\approx0.537
$$

Therefore:

$$
\boxed{
Same\ Aggregate\ Distance\ Observation
\not\Rightarrow
Same\ OD
}
$$

This is the fundamental bridge from Paper 1 to Paper 2.

Key refs: Abrahamsson (1998)

Empirical source: Dissertation Q5.

Suggested footer:

Inverse-problem context: Abrahamsson (1998).
Non-uniqueness control: Dissertation Q5.

Important: Q5 demonstrates empirical non-uniqueness for the tested aggregate representation; it is not a universal mathematical proof of all TLD-to-OD mappings.

---

## Slide 19 — Paper 2

# Paper 2 — Complementary Information for OD Reconstruction

### Research Question

> **How much complementary open urban information is needed to improve OD recoverability when aggregate mobility observations are insufficient?**

The aggregate observation provides distance-related interaction information.

Open urban features provide additional information about where flows are likely to originate and terminate.

Key refs: Simini et al. (2021); Rong et al. (2023); Xu et al. (2025)

These support the value of geographic/contextual information for OD generation.

Footer:

Related flow-generation literature: Simini et al. (2021); Rong et al. (2023); Xu et al. (2025).

---

## Slide 20 — Paper 2 Operational Framework

# Two Observable Information Sources

### Aggregate Mobility Observation

$$
D_{agg}
\rightarrow
\hat{\theta}
$$

### Open Urban Context

$$
X_U
\rightarrow
(\hat O_i,\hat A_j)
$$

### Integration

$$
\boxed{
\hat T_{ij}
===========

\hat O_i
\hat A_j
f(d_{ij};\hat\theta)
}
$$

The two sources are operationally integrated.

No assumption is made that they are statistically independent or uniquely separable scientific components.

Key refs: Wilson (1971); Simini et al. (2021); Fotheringham (1981)

Use Wilson only for the operational spatial-interaction form.

Use DeepGravity for geographic/context features.

Use Fotheringham as caution that distance effects are context-dependent.

---

## Slide 21 — Open Urban Information

# What Complementary Information Is Tested?

Candidate observable information:

$$
X_U=
{
Population,
POI,
Roads,
LandUse,
Accessibility,
Area,\ldots
}
$$

Paper 2 evaluates an information ladder:

$$
TLD
$$

$$
TLD+Population
$$

$$
TLD+POI
$$

$$
TLD+Population+POI
$$

$$
TLD+Full\ X_U
$$

The quantity of interest is:

$$
\Delta CPC
$$

for each added information source.

Slide 21 — Open Urban Information

Key refs: Simini et al. (2021); Alis et al. (2021); Vu et al. (2021); Xu et al. (2025)

Mapping:

population / POI / roads / land use → DeepGravity;
multidimensional opportunity proxies → Alis et al.;
open-data urban function representation → Vu et al.;
satellite urban context → Imagery2Flow.

The information ladder itself is the dissertation's experimental design.

---

## Slide 22 — Preliminary Open-Information Evidence

# Open Urban Information Improves OD Recovery

Clean experiment:

### Baseline

$$
CPC\approx0.5463
$$

### Open spatial information

$$
CPC\approx0.5948
$$

### Gain

$$
\Delta CPC\approx+0.0485
$$

A dedicated paired reliability audit estimates:

$$
Mean\ \Delta CPC=+0.0417
$$

with:

$$
95%CI=[0.0308,0.0527]
$$

This supports the incremental reconstruction value of open spatial information.

Source: Dissertation T20 + paired statistical audit.

No external reference should be used to support your CPC numbers.

Footer:

Source: Dissertation T20 and paired bootstrap/significance audit.

Optional context:

Related precedent: Simini et al. (2021).

---

## Slide 23 — Which Open Information Matters Most?

# Population and POIs Dominate the Tested Gain

T32 ablation results indicate that:

$$
Population+POI
$$

accounts for approximately:

$$
97.6%
$$

of the observed CPC improvement associated with the tested full open-feature representation.

Safe interpretation:

> Among the tested open spatial information sources, population and POI density provide most of the observed incremental reconstruction improvement.

Source: Dissertation T32.

Optional literature context:

Refs: Simini et al. (2021); Alis et al. (2021)

Footer:

Source: Dissertation T32.
Related context: Simini et al. (2021); Alis et al. (2021).

---

## Slide 24 — Clean Zero-Target-OD Stress Test

# 50-City Leave-One-City-Out Evaluation

For every target city:

* Train on the other 49 cities
* Hide target OD
* Infer target distance parameter from three-bin observation
* Predict spatial potentials from open features
* Reconstruct OD
* Reveal OD only for evaluation

### Result

$$
Mean\ CPC=0.6162
$$

$$
Median=0.6249
$$

$$
95%\ Bootstrap\ CI=
[0.5997,0.6317]
$$

This provides clean end-to-end feasibility evidence.

Source: Dissertation T21.

No external reference required for result.

For zero-target precedent, optionally cite:

Refs: Simini et al. (2021); Rong et al. (2023)

But explicitly distinguish:

Source-city OD is used in their training paradigms; target OD is absent at inference.

---

## Slide 25 — Boundary Conditions

# Reconstruction Difficulty Is Not Uniform Across Cities

Several medium-scale systems obtain CPC values close to:

$$
0.69
$$

while some large metropolitan systems are considerably more difficult:

* New York ≈ 0.433
* Chicago ≈ 0.504
* Los Angeles ≈ 0.512

Regression evidence shows a negative association between reconstruction performance and system dimensionality:

$$
CPC\sim\log(N)
$$

with coefficient approximately:

$$
-0.0611
$$

This is an empirical association, not a universal scaling law.

Source: Dissertation T21 + T33.

Optional context:

Refs: Yang et al. (2014); Gallotti et al. (2024)

Do not use literature to imply your (-0.0611) coefficient is externally established.

---

## Slide 26 — What Does Not Explain Transfer?

# Simple Feature Similarity Does Not Predict Transfer Performance

Pairwise cross-city experiment:

$$
\rho=0.0955
$$

$$
p=0.1681
$$

Therefore:

$$
\boxed{
Raw\ Feature\ Similarity
\not\Rightarrow
Transferability
}
$$

This negative result prevents an overly simplistic transfer narrative.

Source: Dissertation T26–T27.

Related ref: TransGM — Enaya et al. (2026)

Suggested footer:

Source: Dissertation T26–T27.
Related transfer literature: Enaya et al. (2026).

TransGM is useful because it demonstrates that cross-city transfer requires contextual/adaptive treatment rather than naive parameter copying.

---

## Slide 27 — Robustness to Distance Misspecification

# Open Spatial Context Remains Useful When Distance Information Is Wrong

T34 deliberately perturbs the reference distance-decay parameter by:

$$
\pm60%
$$

Across the perturbation range, the incremental CPC gain from open spatial features remains approximately:

$$
+0.0411
\quad \text{to} \quad
+0.0530
$$

Interpretation:

> Open spatial information continues to provide positive incremental reconstruction value under substantial misspecification of the distance component.
Source: Dissertation T34.

Context refs: Fotheringham (1981); Simini et al. (2021)

Footer:

Context: Fotheringham (1981); Simini et al. (2021).
Source: Dissertation T34.
---

## Slide 28 — Why HCMC?

# Ho Chi Minh City as the External Case Study

HCMC provides a scientifically demanding setting:

* Large metropolitan system
* Rapid urban transformation
* Limited complete OD ground truth
* Rich open geospatial information
* Availability of aggregate mobility observations

The city is therefore not used to establish feasibility.

The US benchmark establishes feasibility.

HCMC tests:

$$
\boxed{
External\ Applicability
}
$$
Key refs: Vu et al. (2021); Meta MDM documentation

Vu et al. is useful because it directly demonstrates open geospatial urban mapping in HCMC.

Do not cite it for mobility reconstruction.
---

## Slide 29 — HCMC Zero-Target-OD Pipeline

# HCMC Reconstruction

### Open spatial information

$$
OSM+
WorldPop+
POI+
Roads+
Accessibility
$$

↓

$$
(\hat O_i,\hat A_j)
$$

### Aggregate mobility observation

$$
Meta\ MDM
\rightarrow
\hat\theta
$$

### Reconstruction

$$
\boxed{
\hat T_{ij}
===========

\hat O_i
\hat A_j
f(d_{ij};\hat\theta)
}
$$

No disaggregated HCMC OD matrix is used during reconstruction.
Key refs: Wilson (1971); Simini et al. (2021); Vu et al. (2021); Meta MDM documentation

The complete pipeline is your dissertation contribution.

Footer:

Building blocks: Wilson (1971); Simini et al. (2021); Vu et al. (2021); Meta MDM.
Integration: proposed in this dissertation.
---

## Slide 30 — Validation Without Complete OD Ground Truth

# Reconstruction Must Be Defensible, Not Merely Plausible

### Level 1 — Model Diagnostics

* Flow conservation
* Numerical consistency
* Constraint satisfaction

### Level 2 — Independent Partial Observations

Subject to availability:

* Bus smart-card / boarding data
* Traffic corridor counts
* District commuting statistics
* Other independent mobility manifestations

### Level 3 — Falsification

Deliberately wrong inputs should reduce external agreement:

* Shuffled opportunities
* Incorrect spatial context
* Perturbed distance parameters
Key refs: Abrahamsson (1998); Pappalardo et al. (2023)

But the three-level validation/falsification hierarchy is primarily your methodological proposal.

Suggested footer:

Motivation: Abrahamsson (1998); Pappalardo et al. (2023).
Validation hierarchy: proposed in this dissertation.
---

## Slide 31 — Evaluation Principle

# Matching the Input Is Not Validation

A reconstructed OD matrix can perfectly reproduce the coarse input bins and still allocate trips incorrectly.

Therefore:

$$
\boxed{
Input\ Consistency
\neq
Valid\ OD\ Reconstruction
}
$$

Evaluation emphasizes **unconstrained OD properties**, including:

* Fine-resolution distance distribution
* Directional flow asymmetry
* Strong-flow topology
* Inter-district corridor allocation
* Independent external observations
Key refs: Abrahamsson (1998); Lenormand et al. (2016)

Empirical source: Dissertation Q5/T24 where clean.

Footer:

Evaluation context: Abrahamsson (1998); Lenormand et al. (2016).
Dissertation controls: Q5; T24 subject to clean no-oracle verification.
---

## Slide 32 — Scientific Contributions

# Expected Dissertation Contributions

### C1 — Aggregate Mobility Information Characterization

Characterize what information is retained and lost under mobility aggregation.

### C2 — Observation-Sensitivity Framework

Quantify how support, bin resolution, bin geometry, and model complexity affect recoverability.

### C3 — Complementary-Information OD Reconstruction

Develop a zero-target-OD reconstruction methodology combining aggregate mobility observations with open spatial information.

### C4 — Empirical Defensibility Framework

Evaluate reconstructed OD using unconstrained properties, independent partial observations, and falsification.

---

## Slide 33 — What the Dissertation Does Not Claim

# Explicit Scientific Boundaries

This dissertation does **not** claim that:

* Distance-decay parameters represent pure human behaviour
* Urban context and travel behaviour are independently identifiable
* Aggregate TLD uniquely determines an OD matrix
* Open spatial data completely solve OD underdetermination
* US benchmark performance validates HCMC
* Tanner is universally superior or inferior
* Any single mobility representation is the true generative law

The dissertation instead studies:

$$
\boxed{
Observable\ Information
\rightarrow
Recoverability
}
$$

Key refs: Fotheringham (1981); Liang et al. (2013)

These references mainly support the caution against interpreting distance-decay/TLD as pure behaviour.

The rest are explicit scope boundaries of the dissertation.

---

## Slide 34 — Two-Paper Dissertation Logic

# Paper 1 → Paper 2

### Paper 1

> **What can be recovered from aggregate mobility observations, and under what observation conditions?**

$$
Observation
\rightarrow
Recoverability
$$

### Paper 2

> **What additional observable information improves OD reconstruction when the aggregate observation is insufficient?**

$$
Aggregate\ Observation
+
Open\ Urban\ Context
\rightarrow
OD
$$

### HCMC

> **Can the resulting OD be empirically defended without complete target ground truth?**

---

## Slide 35 — Final Thesis Narrative

# Dissertation Narrative

Urban mobility is increasingly observed through aggregate rather than complete movement data.

Aggregation preserves some spatial-interaction information while destroying other information.

The amount that remains recoverable depends on how the observation is constructed.

Because aggregate mobility observations do not uniquely determine OD flows, complementary open urban information can reduce this ambiguity.

A reconstructed OD matrix is scientifically useful only if it performs well on information that was not directly imposed by its inputs.

Therefore:

$$
\boxed{
Observation
\rightarrow
Recoverability
\rightarrow
Complementary\ Information
\rightarrow
Reconstruction
\rightarrow
Independent\ Validation
}
$$
Suggested footer:

Synthesis informed by: Abrahamsson (1998); Merlin (2020); Fotheringham (1981); Liang et al. (2013); Simini et al. (2021); Gallotti et al. (2024).

This is a synthesis slide, so 5–6 references are acceptable.
---

## Slide 36 — Central Dissertation Question

# Central Question

> **How much spatial-interaction information can be recovered from incomplete aggregate mobility observations, and what additional observable information is required for defensible OD reconstruction?**

### Case Study

**Ho Chi Minh City**

### Scientific Goal

Move from:

$$
\text{Data availability}
$$

to:

$$
\boxed{
\text{Defensible inference from limited observable information}
}
$$

# Reference Slides
---

## Slide 37 — References I: Foundations & Calibration
Abrahamsson, T. (1998). Estimation of Origin-Destination Matrices Using Traffic Counts — A Literature Survey. IIASA Interim Report IR-98-021.
Flowerdew, R., & Aitkin, M. (1982). A method of fitting the gravity model based on the Poisson distribution. Journal of Regional Science, 22(2), 191–202.
Fotheringham, A. S. (1981). Spatial structure and distance-decay parameters. Annals of the Association of American Geographers, 71(3), 425–436.
Haynes, K. E., & Fotheringham, A. S. (1984). Gravity and Spatial Interaction Models. Sage.
Hyman, G. M. (1969). The calibration of trip distribution models. Environment and Planning, 1, 105–112.
Merlin, L. A. (2020). A new method using medians to calibrate single-parameter spatial interaction models. Journal of Transport and Land Use, 13(1), 49–70.
Tanner, J. C. (1961). Factors Affecting the Amount of Travel. Road Research Technical Paper No. 51.
Wilson, A. G. (1971). A family of spatial interaction models, and associated developments. Environment and Planning A, 3(1), 1–32.
---

## Slide 38 — References II: Mobility Data, Context & Modern Models
Alis, C., Legara, E. F., & Monterola, C. (2021). Generalized radiation model for human migration. Scientific Reports, 11, 22707.
Barbosa, H., et al. (2018). Human mobility: Models and applications. Physics Reports, 734, 1–74.
Gallotti, R., Maniscalco, D., Barthelemy, M., & De Domenico, M. (2024). Distorted insights from human mobility data. Communications Physics, 7, 421.
Liang, X., Zhao, J., Dong, L., & Xu, K. (2013). Unraveling the origin of exponential law in intra-urban human mobility. Scientific Reports, 3, 2983.
Pappalardo, L., Manley, E., Sekara, V., & Alessandretti, L. (2023). Future directions in human mobility science. Nature Computational Science, 3, 588–600.
Rong, C., Feng, J., & Ding, J. (2023). GODDAG: Generating origin-destination flow for new cities via domain adversarial training. IEEE Transactions on Knowledge and Data Engineering, 35(10), 10048–10057.
Rubio-Herrero, J., & Muñuzuri, J. (2023). Sparse regression for data-driven deterrence functions in gravity models. Annals of Operations Research, 323, 153–174.
Simini, F., Barlacchi, G., Luca, M., & Pappalardo, L. (2021). A Deep Gravity model for mobility flows generation. Nature Communications, 12, 6576.
Vu, T. T., Vu, N. V. A., Phung, H. P., & Nguyen, L. D. (2021). Enhanced urban functional land use map with free and open-source data. International Journal of Digital Earth, 14(11), 1744–1757.
Xu, Y., et al. (2025). Predicting human mobility flows in cities using deep learning on satellite imagery. Nature Communications, 16, 10372.
---

## Slide 39 — References III: Transfer & Data Governance
Buckee, C. O., et al. (2020). Aggregated mobility data could help fight COVID-19. Science, 368, eabb8021.
de Montjoye, Y.-A., Hidalgo, C. A., Verleysen, M., & Blondel, V. D. (2013). Unique in the Crowd: The privacy bounds of human mobility. Scientific Reports, 3, 1376.
Enaya, A., Zhong, C., Batty, M., Morphet, R., & Lopane, F. D. (2026). TransGM: Transferable gravity models for cross-city policy transfer. Computers, Environment and Urban Systems, 128, 102455.
Oliver, N., et al. (2020). Mobile phone data for informing public health actions across the COVID-19 pandemic lifecycle. Science Advances, 6(23), eabc0764.
Cover, T. M., & Thomas, J. A. (2006). Elements of Information Theory (2nd ed.). Wiley.