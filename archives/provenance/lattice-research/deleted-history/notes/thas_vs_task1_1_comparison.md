# Thas (1994) vs. Task 1.1 Sextic Examples Comparison

**Date:** 2026-03-30\
**Purpose:** Determine whether the repo's three Task 1.1 sextic examples are the same
construction as C. Thas (1994) or independent computational constructions.

* * *

## Summary

**Determination: INDEPENDENT CONSTRUCTIONS**

The three Task 1.1 sextic examples are **not** the Thas (1994) construction.
They are independent computational constructions using generic parametrizations, not the
Desargues-configuration-based parametrization from Thas.

* * *

## 1. Extracted Parametric Formulas

### Thas (1994) - Extracted from papers/extracted/thas_1994.md (lines 247-253)

The Thas parametrization arises from a specific geometric construction using a Desargues
configuration. In homogeneous coordinates $(X:Y:Z)$ with parameter $t$:

```
X = a*c*t^6 + a*(b*c - c + 1)*t^4 - a*(b*c - b + 1)*t^2 - a*b
Y = -2*((a*b*c - a*c + a)*t^5 - (2*a^2*b*c + b*c - b - c + 2*a^2 + 1)*t^4 
        + (2*a*b*c - 2*a*b + 2*a)*t^3 + a*b*t)
Z = 2*(a*c*t^5 + (2*a*b*c - 2*a*c + 2*a)*t^3 
        - (2*a^2*b*c + b*c - c - b + 2*a^2 + 1)*t^2 + (a*b*c - a*b + a)*t)
```

**Key structural features:**
- **Degree distribution:** X is degree 6; Y and Z are degree 5
- **Parameters:** Uses three parameters (a, b, c) that encode the specific Desargues
  configuration
- **Origin:** Derived from projectivities associated with a Desargues configuration (see
  Section 1-3 of Thas paper)

### Repo Example 1 - From computations/task1_1_sextic.sage (lines 62-64)

```python
f0 = s^6 + s^5*t + 2*s^4*t^2 + 3*s^3*t^3 + 2*s^2*t^4 + s*t^5 + t^6
f1 = 2*s^6 + 3*s^5*t + s^4*t^2 + 2*s^3*t^3 + 3*s^2*t^4 + s*t^5 + 2*t^6
f2 = 3*s^6 + 2*s^5*t + 3*s^4*t^2 + s^3*t^3 + 2*s^2*t^4 + 3*s*t^5 + t^6
```

### Repo Example 2 - From computations/task1_1_sextic_example2.sage (lines 22-24)

```python
f0 = s^6 + 2*s^5*t - s^4*t^2 + 3*s^3*t^3 + s^2*t^4 - 2*s*t^5 + t^6
f1 = 2*s^6 - s^5*t + 3*s^4*t^2 + 2*s^3*t^3 - s^2*t^4 + 3*s*t^5 + 2*t^6
f2 = 3*s^6 + s^5*t + 2*s^4*t^2 - s^3*t^3 + 3*s^2*t^4 + s*t^5 + t^6
```

### Repo Example 3 - From computations/task1_1_sextic_example3.sage (lines 20-22)

```python
f0 = s^6 + 3*s^5*t + 2*s^4*t^2 - s^3*t^3 + s^2*t^4 + 2*s*t^5 + t^6
f1 = 2*s^6 + s^5*t + 3*s^4*t^2 + 2*s^3*t^3 - s^2*t^4 + s*t^5 + 3*t^6
f2 = s^6 - s^5*t + s^4*t^2 + 3*s^3*t^3 + 2*s^2*t^4 - s*t^5 + 2*t^6
```

* * *

## 2. Structural Comparison

### Parametric Domain

| Source | Parametric Domain | Coordinate Functions |
| --- | --- | --- |
| **Thas (1994)** | P^1 → P^2 via rational functions of single parameter t | Non-homogeneous rational functions; effectively [X:Y:Z] with rational expressions in t |
| **Repo Examples** | P^1 → P^2 via homogeneous polynomials | [f0(s,t) : f1(s,t) : f2(s,t)] where each f_i is homogeneous of degree 6 in (s,t) |

### Degree Structure

| Source | X-coordinate degree | Y-coordinate degree | Z-coordinate degree |
| --- | --- | --- | --- |
| **Thas (1994)** | 6 | 5 | 5 |
| **Repo Examples** | 6 | 6 | 6 |

**Critical observation:** All three repo examples have **all three coordinates of degree
6**, while Thas has X of degree 6 and Y, Z of degree 5.

### Parameter Dependence

| Source | Parameters | Nature |
| --- | --- | --- |
| **Thas (1994)** | a, b, c | Encodes specific Desargues configuration; curve has nodes at the 10 points of the DC |
| **Repo Examples** | None (specific integer coefficients) | Generic random-looking coefficients chosen once; no geometric interpretation |

* * *

## 3. Geometric Origin

### Thas (1994) Construction

From the paper abstract (line 12):
> "We construct a rational curve of order 6 which has a node at each of the ten points
> [of a Desargues configuration]."

The parametrization in Thas arises from:
1. Starting with a Desargues configuration (10 points, 10 lines)
2. Considering projectivities associated with the configuration
3. Computing a locus: the second component is the sextic with nodes at the 10 DC points

The parameters a, b, c in Thas's formulas encode the position of the specific Desargues
configuration.

### Repo Examples Construction

From task1_1_sextic.sage (lines 19-23):
> "Construction approach:
> - Use a generic parametrization P¹ → P² given by three degree-6 polynomials
> - For generic coefficients, the image is a rational sextic
> - The number of nodes is maximal (10) for generic parametrizations"

The repo examples use **generic** parametrizations with **no reference** to any
Desargues configuration.
The coefficients appear to be randomly chosen integers, not derived from geometric
parameters.

* * *

## 4. Evidence of Independence

### Evidence that Repo Examples are NOT Thas:

1. **Different degree distributions:** Repo has degree 6 for all three coordinates; Thas
   has (6, 5, 5)

2. **No geometric parameters:** Thas uses parameters (a, b, c) that encode the specific
   Desargues configuration; repo uses fixed integer coefficients with no geometric
   interpretation

3. **Generic vs. Specific:** Thas constructs a specific curve associated with a specific
   Desargues configuration; repo constructs generic rational sextics

4. **Different coefficient patterns:** Even if we homogenize Thas's formulas, the
   coefficient structure (polynomials in a, b, c) doesn't match the integer coefficient
   patterns in the repo examples

### Evidence Against Possible Coordinate Transformation:

While one could theoretically apply a linear change of coordinates to Thas's formulas,
this would:
- Preserve the degree pattern (X degree 6, Y/Z degree 5, or permutation thereof)
- Still involve parameters a, b, c in the coefficients
- Not produce the specific integer coefficient patterns seen in the repo examples

The repo examples have **all three coordinates with equal degree 6** and **no free
parameters** — these are concrete numerical polynomials, not formulas with geometric
parameters.

* * *

## 5. Conclusion

The three Task 1.1 sextic examples are **clearly independent constructions** from C.
Thas (1994):

1. **Different parametric structure:** Repo uses homogeneous degree-6 polynomials; Thas
   uses rational functions with degree pattern (6, 5, 5)

2. **Different geometric origin:** Repo uses generic parametrizations; Thas derives from
   Desargues configuration projectivities

3. **Different parameter spaces:** Repo has fixed integer coefficients; Thas has
   parameters (a, b, c) encoding geometric configuration

4. **No evidence of relationship:** The coefficient patterns are completely different
   with no apparent transformation relationship

The repo examples represent **independent computational constructions** of 10-nodal
rational sextic curves, chosen for their generic properties, rather than implementations
of Thas's geometric construction.

* * *

## References

- Thas, C. (1994). "A Rational Sextic Associated with a Desargues Configuration."
  Geometriae Dedicata 51: 163-180.
- computations/task1_1_sextic.sage
- computations/task1_1_sextic_example2.sage
- computations/task1_1_sextic_example3.sage
