# APPENDIX BLUEPRINT V2.0

## Overall Strategy: Cohesive Narrative Support
The Appendix must not be a repository for leftover figures. It is structured to systematically support the central scientific argument: **aggregate mobility data contains sufficient information to recover the behavioral distance-decay parameter**. 

### Narrative Flow
`Behavioral Recovery Evidence $\to$ Methodological Validation $\to$ Reproducibility $\to$ Mathematical Foundation`

---

## Section Guidelines

### Appendix A: Behavioral Recovery Evidence
**Objective**: Persuade the reader that $\beta$ is genuinely recovered, not just fitted to minimize OD error.
*Note: Renamed from "Additional Experimental Results" to explicitly link to the central hypothesis.*

- **A1. Recovery curves**: Evidence across 25 cities.
- **A2. City-wise parameter recovery**: Detailed metrics per city.
- **A3. Representative case studies**: Deep dives into 3 cities with distinct morphologies (e.g., Atlanta, Seattle, Los Angeles).
- **A4. Behavioral consistency**: Correlation between recovered $\beta$ and local $\beta$, demonstrating behavioral alignment independent of OD flow outcomes.
- **A5. Behavioral Recovery under Different Histogram Resolutions**: (Formerly Bin sensitivity) Robustness of recovery against varying data resolutions.
- **A6. Cross-city recovery distribution**: Boxplots illustrating the stability of recovery across the 25 cities.

### Appendix B: Methodological Validation
**Objective**: Validate *why* the Projection-Inference Gravity Framework (PIGF) works.

- **B1. Full factorial ablation**: Isolating component effects.
- **B2. Complete Shapley tables**: Comprehensive game-theoretic attributions.
- **B3. SHAP feature ranking**: Importance of spatial features.
- **B4. Feature-count sensitivity**: Performance vs. model parsimony.
- **B5. Exposure correction**: (Moved up due to its importance as a novelty). Demonstrating why uncorrected histograms yield incorrect $\beta$ and how exposure correction recovers the true $\beta$.
- **B6. Adaptive $\delta$**: Validation of the self-loop handling.
- **B7. Attraction heuristic**: Details on destination opportunity mapping.

### Appendix C: Reproducibility
**Objective**: Provide exhaustive details required to replicate the experiments.

- **C1. Pipeline**: Overall system architecture.
- **C2. Data**: Dataset descriptions and sourcing.
- **C3. Hyperparameters**: Model tuning configurations.
- **C4. Optimizer**: Solver details.
- **C5. Runtime**: Execution speed.
- **C6. Hardware**: Computing resources used.
- **C7. Seeds**: Random seed initialization for stochastic processes.
- **C8. Split**: Training, validation, and testing partition logic.
- **C9. Code**: Link to code availability.
- **C10. Complexity**: Move empirical computational complexity here (appeals to reviewers focused on implementation).

### Appendix D: Mathematical Foundations
**Objective**: Provide rigorous theoretical proofs and derivations.
*Note: Titled "Mathematical Foundations" rather than "Details" to project theoretical strength.*

- **D1. Projection derivation**: Proof linking OD matrices to trip-length distributions.
- **D2. Inverse inference**: Derivation of Equations (5–7).
- **D3. Exposure correction**: Mathematical derivation of the spatial exposure normalization.
- **D4. Adaptive $\delta$**: Proof backing the adaptive self-loop parameter.
- **D5. Identifiability discussion**: Theoretical discussion explaining why observed histograms coupled with projection uniquely identify $\beta$. (Does not require a formal proof, but a strong logical discussion).
- **D6. Complexity proof**: Theoretical big-O complexity analysis.

### Appendix E (Optional): Broader Discussion
**Objective**: Provide extended conceptual discussions beyond empirical results.

- **E1. Why Tanner?**: Justification for the functional form.
- **E2. Why aggregate mobility?**: Extended rationale.
- **E3. Why behavioral inference?**: Philosophical positioning against flow reconstruction.
- **E4. Physics-informed learning**: Expanding on the relationship with modern AI methods.
