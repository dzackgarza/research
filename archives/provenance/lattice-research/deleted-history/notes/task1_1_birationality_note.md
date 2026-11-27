# Task 1.1 note: what the exact sextic computations establish

The classical literature already supplies the ambient Coble-surface picture.
Task 1.1 is not proving that such sextics should exist in principle; it is producing
exact worked examples inside that picture.

## What the current computations prove

Across the three Task 1.1 examples, the repo now verifies the following exact facts:

- the elimination step produces a degree-6 plane equation `F(x,y,z)=0`;
- `F` is irreducible over `QQ` and squarefree/reduced;
- the singular locus consists of exactly 10 projective points;
- each singular point is an `A₁` node by the Hessian-rank test;
- the parametrization is generically injective, witnessed by generic fiber gcd `u-a`;
- the saved node coordinates are now exact algebraic coordinates, rendered via
  `QQbar.polynomial_root(AA.common_polynomial(minpoly), isolating_interval(...))` rather
  than floating approximations.

## Why this implies rational birational sextic examples

For a degree-6 plane curve, the arithmetic genus is

`g_a = (6-1)(6-2)/2 = 10`.

Each node contributes delta-invariant `1`, so ten nodes force geometric genus `0`.
Because the sextic is irreducible and the parametrization has generic fiber degree `1`,
the map `P^1 -> C` is birational onto its image.
Thus each Task 1.1 example is an exact explicit rational sextic with ten nodes, i.e. an
exact worked Coble-curve example.

## What this note does not claim

- It does not replace the classical literature on Coble surfaces.
- It does not prove that every sextic in a larger family has the same behavior.
- It does not settle the broader moduli theory by computation alone.

Its role is narrower: it records that the repo now contains exact audited examples whose
outputs match the standard literature picture.
