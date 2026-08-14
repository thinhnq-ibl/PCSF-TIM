# Meta Movement Distribution Maps (MDM): 8 Core Technical Points & Pipeline

This document summarizes the core technical characteristics of the Meta Movement Distribution Maps dataset, defining the exact observation process and mathematical pipeline for the thesis.

## 8 Core Technical Points

1. **Movement Distribution is NOT an OD matrix.** The data only describes how far users travel from their home location within a day. It does *not* indicate that origin ($i$) connects to a specific destination ($j$).

2. **The measured quantity is home-to-ping distance, not traditional trip length.** Meta identifies a "home tile" from nighttime location updates, then randomly samples *one* location ping during the day and calculates the distance from the home tile to that ping.

3. **Distance is coarsely compressed into 4 bins:** (0) km; ($0 < D < 10$) km; ($10 \le D < 100$) km; and ($D \ge 100$) km. The output is therefore a distance distribution, not destination-resolved mobility.

4. **The population sample is selective.** The sample only includes Facebook mobile app users who have Location Services enabled, meaning the data is not inherently representative of the entire population.

5. **Each person contributes only ONE sampled ping.** This makes the observation process a statistical sampling of mobility behavior, rather than a complete recording of trajectories or all trips.

6. **Meta injects Differential Privacy noise.** The documentation specifies the use of $\epsilon=1$, adding Laplace noise with a strength of 1 to both the distance-bin counts and the total count of the home polygon.

7. **Privacy noise can result in negative fractions.** The `distance_category_ping_fraction` already includes this privacy noise. For the (100+) km bin, approximately 10% of the fractions can be negative. Therefore, the output is not always a mathematically "clean" probability vector.

8. **The data undergoes thresholding and temporal aggregation.** A polygon is only retained if the noisy person count exceeds 10. Furthermore, data is aggregated daily based on Pacific Time, not the local time zone.

---

## Technical Observation Pipeline

Based on these 8 points, the most appropriate technical pipeline for the thesis is defined as:

$$
M \xrightarrow{S(M)} H/V \xrightarrow{D} B(D) \xrightarrow{P(\cdot)} Q(\cdot) \xrightarrow{} Y_D^{\text{Meta}}
$$

Where:
- $M$: Underlying mobility process
- $S$: Selective sampling (Facebook users with location services)
- $H/V$: Home-visit construction (home tile to a single daytime ping)
- $D$: Distance calculation
- $B$: 4-bin aggregation ($0, 10, 100$ thresholds)
- $P$: Privacy perturbation (Laplace noise, $\epsilon=1$)
- $Q$: Thresholding and filtering (minimum count $>10$, Pacific Time aggregation)
- $Y_D^{\text{Meta}}$: The final observed Meta MDM variable.

## Research Implications (Paper 1 & Paper 2)

**The most critical research takeaway:**
Paper 1 should **NOT** ask whether Meta provides a "precise OD." Instead, the correct scientific question is whether a **sampled, coarsely binned, privacy-perturbed home-to-ping distance distribution** still retains a **measurement-valid mobility-distance signal**.

Following this, Paper 2 will investigate whether this empirically validated signal provides **additional destination-resolved OD information** beyond what is already captured by the urban context.
