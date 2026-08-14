## Slide 5 - Measurement Validity of Aggregate Observations

# Observed Mobility $\neq$ Latent Mobility

Observed mobility is a measurement of mobility, subject to distortions from the collection and processing pipeline:

$$
\boxed{
M \rightarrow S(M) \rightarrow B(\cdot) \rightarrow P(\cdot) \rightarrow Y_D^{obs}
}
$$

*   **Mobility observations depend on sampling, spatial aggregation, processing, and privacy mechanisms; observed patterns are therefore not automatically equivalent to latent mobility behavior.**
*   **Paper 1 tests whether Meta's sampled, four-bin, privacy-perturbed home-to-ping distribution remains measurement-valid for spatial-interaction inference.**

> **Key References:**
> - **Meta Data for Good (2022)** $\rightarrow$ What the observation pipeline actually does.
> - **Gallotti et al. (2024)** $\rightarrow$ Why data-source/processing distortion matters.
> - **Gosselin et al. (2025)** $\rightarrow$ Bias/sensitivity specifically in Meta mobility data.
> - **Gibbs et al. (2026)** $\rightarrow$ Why differential privacy can affect mobility utility.
