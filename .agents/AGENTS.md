# Project-Scoped Agent Rules

## Rule: Evaluate Whether Meta Movement Distribution Maps (MDM) Citation Should Be Added

### Objective
Evaluate whether the manuscript would benefit from explicitly citing the official **Meta AI for Good – Movement Distribution Maps (MDM)** dataset. The goal is to improve the logical connection between the motivation for aggregate mobility data, the proposed methodology, and the real-world dataset used in the experiments without inflating reference count.

### When to Recommend Adding the Citation
Recommend adding the official Meta MDM citation **only if all of the following are true**:
1. The manuscript later uses Meta Movement Distribution Maps as a real dataset.
2. The Introduction discusses the increasing availability of aggregate mobility products.
3. The Introduction does not explicitly mention Meta MDM.
4. Adding Meta MDM would strengthen the narrative from motivation → methodology → evaluation.

### Preferred Location
Prefer adding the citation in the Introduction, near statements such as *"aggregate mobility products are becoming increasingly available..."* rather than introducing Meta MDM for the first time in the Data section.

### Recommended Revision Example
Replace:
> "Aggregate mobility products are becoming increasingly available across platforms and regions..."
With:
> "Aggregate mobility products—including Meta's Movement Distribution Maps (MDM) \citep{MetaMovementDistributionMaps}—are becoming increasingly available across platforms and regions, providing privacy-preserving summaries of population travel behavior."

### Do NOT Recommend the Citation If
- The paper never uses Meta MDM.
- Meta MDM is only mentioned as an implementation detail.
- The citation would merely increase reference count without strengthening the argument.
- Another citation already supports exactly the same claim.

### Review Principle
- Prioritize citations that strengthen the scientific narrative.
- Avoid adding citations solely because a dataset exists.
- Every added citation should clearly improve one of: motivation, research gap, methodological justification, or experimental reproducibility.

## Rule: Evidence for Parameter Identification

### Context
The paper does **not** claim mathematical identifiability. Instead, it builds **empirical statistical evidence** that aggregate travel-length distributions (TLDs) contain sufficient information to support identification of the parameters governing collective distance-sensitive travel behaviour.

### Evidence Components
Evidence should consist of four complementary components:

1. **Likelihood evidence**
   - Well-defined optimum.
   - Sharp and stable likelihood surface.

2. **Synthetic recovery**
   - Generate TLD from known parameters.
   - Recover parameters accurately from the generated TLD.

3. **Cross-city consistency**
   - Independently estimate parameters for multiple cities.
   - Results are stable and consistent across cities.

4. **Downstream validation**
   - Parameters inferred from TLD enable accurate OD reconstruction.
   - OD reconstruction serves as validation of the inferred parameters, **not** as proof of identifiability.

### Writing principle
Always use evidence-oriented language:
- provide statistical evidence
- support identification
- support the hypothesis
- indicate
- suggest
- are consistent with

Avoid:
- prove
- mathematically prove
- uniquely determine
- recover human mobility behaviour
- demonstrate identifiability
