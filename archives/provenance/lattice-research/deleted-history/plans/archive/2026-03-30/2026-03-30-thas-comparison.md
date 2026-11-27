# Plan: Compare Thas (1994) Formulas Against Task 1.1 Examples

**Created**: 2026-03-30 17:38 UTC **Status**: Complete **Conclusion**: INDEPENDENT
CONSTRUCTIONS **SCHEDULE.md slot**: 17:00-18:00 (literature availability check)

## Context

C. Thas (1994) has been acquired in local machine-parseable form
(`papers/extracted/thas_1994.md`, 757 lines).
The paper provides explicit rational parametric equations for a 10-nodal sextic
associated with a Desargues configuration.

GAPS.md notes: "Still need to compare the repo's three computational examples (task1_1)
against these explicit Thas formulas to determine if they are the same construction or
independent."

## Goal

Determine whether the repo's three Task 1.1 sextic examples are the same construction as
Thas (1994) or independent computational constructions.

## Phase 1 — Extract Thas (1994) parametric formulas

From `papers/extracted/thas_1994.md` lines 244-253, the homogeneous parametric
representation of the sextic is:

```
X = a*c*t^6 + a*(b*c - c + 1)*t^4 - a*(b*c - b + 1)*t^2 - a*b
Y = -2*((a*b*c - a*c + a)*t^5 - (2*a^2*b*c + b*c - b - c + 2*a^2 + 1)*t^4 + (2*a*b*c - 2*a*b + 2*a)*t^3 + a*b*t)
Z = 2*(a*c*t^5 + (2*a*b*c - 2*a*c + 2*a)*t^3 - (2*a^2*b*c + b*c - c - b + 2*a^2 + 1)*t^2 + (a*b*c - a*b + a)*t)
```

With parameters a, b, c satisfying various non-vanishing conditions (from lines
165-198).

The rational parametrization yields a degree-6 curve with 10 nodes at the Desargues
configuration points.

## Phase 2 — Compare against repo's three examples

The repo has three task1_1 examples:
- `task1_1_sextic.sage` (example 1)
- `task1_1_sextic_example2.sage` (example 2)
- `task1_1_sextic_example3.sage` (example 3)

Each produces a sextic curve via different parametric maps P^1 -> P^2.

**Comparison approach**:
1. Read the parametric equations from each repo script
2. Determine if they match the Thas parametric form (possibly after coordinate change or
   parameter specialization)
3. Check if the repo's parameter choices correspond to specific values of (a, b, c) in
   Thas
4. Verify the 10 nodes appear at the expected positions

## Phase 3 — Document findings

**If same construction**: Update REFERENCES.md to note the repo's task1_1 examples are
implementations of Thas (1994). Update GAPS.md to close the explicit polynomial family
gap.

**If independent**: Document that repo uses independent construction.
Update GAPS.md to note this distinction.

**If unclear**: Document what is unknown and what further analysis would be needed.

## Verification

Success: Clear determination of whether repo's Task 1.1 sextics are Thas-derived,
independent, or unknown.
