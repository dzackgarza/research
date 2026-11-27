# Task 1.1 Sextic Parametrizations: Literature Search Audit

**Date**: 2026-03-30\
**Objective**: Determine if the three task1_1 sextic parametrizations connect to
acquired literature sources

## Task1_1 Parametrizations Overview

The repository contains three independent rational 10-nodal sextic constructions:
- `computations/task1_1_sextic.sage`
- `computations/task1_1_sextic_example2.sage`
- `computations/task1_1_sextic_example3.sage`

**Parametric form**: [f0(s:t), f1(s:t), f2(s:t)] where each fi is a degree-6 homogeneous
polynomial

**Example** (from task1_1_sextic_example2.sage, lines 22-24):
```
f0 = s^6 + 2*s^5*t - s^4*t^2 + 3*s^3*t^3 + s^2*t^4 - 2*s*t^5 + t^6
f1 = 2*s^6 - s^5*t + 3*s^4*t^2 + 2*s^3*t^3 - s^2*t^4 + 3*s*t^5 + 2*t^6
f2 = 3*s^6 + s^5*t + 2*s^4*t^2 - s^3*t^3 + 3*s^2*t^4 + s*t^5 + t^6
```

**Key characteristics**:
- Fixed integer coefficients (no geometric parameters)
- All three coordinates have degree 6
- Produces rational sextic with exactly 10 nodes

## Literature Sources Searched

### 1. Thas (1994) - "A Rational Sextic" (757 lines)

**Searched**: Lines 1-757, full paper\
**Search terms**: "parametric", "parametrization", "sextic", "explicit", "formula",
"coefficient"

**Found**:
- Explicit parametric representation (lines 236-254):
  ```
  X = (act^6 + (abc-ac+a)t^4 - (abc-ab+a)t^3 - ab) / (denominator)
  Y = (rational expression in t with parameters a,b,c)
  Z = (rational expression in t with parameters a,b,c)
  ```
- Construction based on Desargues configuration
- **Three geometric parameters**: a, b, c (not fixed integers)
- Parameters determine the Desargues configuration geometry

**Conclusion**: INDEPENDENT\
**Reason**: Thas construction has parametric family (a,b,c), while task1_1 has fixed
integer coefficients.
Already confirmed independent in prior work.

**Confidence**: High

* * *

### 2. Dolgachev-Kondō (2013) - "Rationality of Moduli Spaces of Coble Surfaces" (437 lines)

**Searched**: Lines 1-437, full paper\
**Search terms**: "sextic", "parametric", "parametrization", "explicit", "formula",
"construction", "Coble"

**Found**:
- Abstract discussion of Coble surfaces as blow-ups of 10 nodes of rational sextics
  (line 11, 91)
- Reference to Coble's original 1919 paper: "The ten nodes of the rational sextic and of
  the Cayley symmetroids" (line 414)
- Statement: "There is a beautiful relationship between Cayley quartic symmetroids and
  rational sextics" (line 288)
- Sections 7-8 discuss "geometric constructions" for Enriques and Coble surfaces (lines
  290-405)
- **NO explicit parametric formulas provided**
- Focus on moduli spaces, lattice theory, and birational geometry

**Conclusion**: NO CONNECTION FOUND\
**Reason**: Paper discusses Coble surfaces abstractly but provides no explicit sextic
parametrizations to compare against task1_1 constructions.

**Confidence**: High\
**Gaps**: Coble's original 1919 paper (referenced but not in our literature collection)

* * *

### 3. AEGS (2023) - "Compact Moduli of Enriques Surfaces" (1234 lines)

**Searched**: Lines 1-1234, full paper\
**Search terms**: "sextic", "parametric", "Coble", "explicit", "formula",
"construction", "polynomial", "coefficient"

**Found**:
- Mentions Coble surfaces in context of Enriques surface degenerations (lines 96, 182)
- Discusses toric constructions with equations z^2 + f(x,y) (lines 78, 92)
- Polynomials f(x,y) of bidegree (4,4) with 13 monomials (line 78)
- References Horikawa's analysis of possible equations f(x,y) (line 96)
- **NO explicit sextic parametrizations provided**
- Focus on moduli compactifications, integral-affine structures, and KSBA stable pairs

**Conclusion**: NO CONNECTION FOUND\
**Reason**: Paper discusses Coble surfaces in moduli-theoretic context but provides no
explicit sextic parametrizations.

**Confidence**: High\
**Gaps**: Horikawa's original work on explicit equations (referenced but not in our
collection)

* * *

## Search for Coble's Original Constructions

**Searched**: All three papers for references to Coble's original work

**Found**:
- Dolgachev-Kondō reference: A. Coble, "The ten nodes of the rational sextic and of the
  Cayley symmetroids", Amer.
  J. Math., 41 (1919), 243–265
- Dolgachev-Kondō reference: A. Coble, "Algebraic geometry and theta functions", Amer.
  Math. Soc. Coll. Publ., 10, Providence, R.I., 1929 (3rd ed., 1969)
- AEGS mentions "Coble surfaces" but does not reproduce original constructions

**Conclusion**: Coble's original 1919 parametrizations are NOT reproduced in the
acquired literature

**Confidence**: High\
**Gaps**: Coble (1919) and Coble (1929) not in our extracted papers

* * *

## Search for Coolidge References

**Searched**: All three papers for "Coolidge"

**Found**:
- Thas (1994) reference: J.L. Coolidge, "A treatise on Algebraic Plane Curves", Dover
  Publications, 1959 (line 752)
- **NO explicit constructions from Coolidge reproduced**

**Conclusion**: Coolidge's work referenced but not reproduced

**Confidence**: Medium\
**Gaps**: Coolidge (1959) treatise not in our collection

* * *

## Overall Conclusion

**Status**: INDEPENDENT

The three task1_1 sextic parametrizations appear to be INDEPENDENT from all acquired
literature sources based on the following evidence:

1. **Thas (1994)**: Confirmed independent (parametric family vs.
   fixed coefficients)
2. **Dolgachev-Kondō (2013)**: No explicit parametrizations provided
3. **AEGS (2023)**: No explicit parametrizations provided
4. **Coble (1919)**: Referenced but not reproduced in acquired literature
5. **Coolidge (1959)**: Referenced but not reproduced in acquired literature

**Confidence**: High

The acquired literature discusses rational 10-nodal sextics at an abstract level (moduli
spaces, lattice theory, geometric constructions) but does NOT provide explicit
parametric formulas that could be compared against the task1_1 constructions.

* * *

## Remaining Gaps

To achieve complete certainty, the following sources should be examined:

1. **A. Coble (1919)**: "The ten nodes of the rational sextic and of the Cayley
   symmetroids", Amer. J. Math., 41, 243–265
2. **A. Coble (1929)**: "Algebraic geometry and theta functions", Amer.
   Math. Soc. Coll. Publ., 10
3. **J.L. Coolidge (1959)**: "A treatise on Algebraic Plane Curves", Dover Publications
4. **E. Horikawa**: Papers on explicit equations for K3 surfaces (referenced in AEGS
   2023\)

These are the primary historical sources that might contain explicit parametric
constructions comparable to task1_1.

* * *

## Methodology Notes

**Search strategy**:
- Full-text grep for: "sextic", "parametric", "parametrization", "Coble", "Coolidge",
  "explicit", "formula", "construction", "coefficient", "polynomial", "degree 6"
- Manual reading of relevant sections in all three papers
- Cross-reference checking for cited works

**Line ranges examined**:
- Thas (1994): Lines 1-757 (complete)
- Dolgachev-Kondō (2013): Lines 1-437 (complete)
- AEGS (2023): Lines 1-1234 (complete, with focus on lines 1-100, 940-1100 for explicit
  constructions)

**Total matches found**:
- "sextic": 36 matches across all papers
- "parametric/parametrization": 12 matches
- "Coble": 22 matches
- "explicit": 0 matches in Dolgachev-Kondō, limited matches in AEGS (none for sextics)
