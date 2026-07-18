# MAIN BLUEPRINT V2.0

## Title
Recovering Latent Distance-Decay Behavior from Aggregate Mobility Data for Survey-Free Spatial Interaction Inference

---

## I. CENTRAL SCIENTIFIC QUESTION

> **Can aggregate mobility data preserve sufficient information to recover the latent city-specific distance-decay parameter governing human spatial interactions?**

*Note: Origin-Destination (OD) prediction is utilized strictly as the downstream application to empirically validate this hypothesis.*

---

## II. CENTRAL HYPOTHESIS

```text
Aggregate mobility data
        │
        ▼
contain sufficient information to recover the latent city-specific distance-decay parameter (β)
        │
        ▼
Recovered β can replace OD-based calibration
        │
        ▼
Gravity models become transferable to cities without observed OD matrices.
```

---

## III. THREE-LAYER CONTRIBUTION

### Layer 1 — Scientific Discovery (Core Contribution)
**Research Question:** Does aggregate mobility preserve sufficient information to recover the latent distance-decay parameter?
**Discovery Flow:**
`Aggregate mobility $\to$ latent distance-decay $\to$ recoverable`
*This constitutes the primary scientific contribution of the paper.*

### Layer 2 — Methodological Contribution
**Framework:** Building on the scientific discovery, a zero-shot gravity calibration framework is established.
**Methodological Flow:**
`Recovered β $\to$ Zero-shot gravity calibration $\to$ No observed OD required`

### Layer 3 — Practical Contribution
**Application:** The methodology enables practical applications in data-scarce environments.
**Practical Flow:**
`Transferable gravity model $\to$ Transferable OD estimation $\to$ Data-scarce cities $\to$ Scalable $\to$ Privacy-preserving`
*Note: Privacy-preservation is a practical benefit, not the core novelty.*

---

## IV. STORYLINE OF THE PAPER

### Step 1: Background
**Why?** OD matrices are critically important for urban and transportation planning.

### Step 2: Problem
**Challenge:** The Gravity model requires parameter $\beta$. Calibrating $\beta$ traditionally requires observed OD matrices. OD matrices are often unavailable.

### Step 3: Opportunity
**Alternative:** Aggregate mobility data is widely available and privacy-preserving.

### Step 4: Unknown (Knowledge Gap)
**Gap:** Can aggregate mobility data substitute for full OD matrices to recover $\beta$?

### Step 5: Solution
**Methodology:** Introduce the Projection-Inference Gravity Framework (PIGF) to recover $\beta$ from aggregate mobility.

### Step 6: Validation
**Results:** The recovered $\beta$ is validated by reconstructing the complete OD matrix.

### Step 7: Conclusion
**Insight:** Aggregate mobility data preserves the core behavioral parameters governing spatial interaction.
