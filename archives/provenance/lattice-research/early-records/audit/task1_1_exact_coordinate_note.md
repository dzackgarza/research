# Task 1.1 note: exact algebraic coordinate rendering

## Context

The Task 1.1 sextic computations produce ten singular points whose coordinates are
algebraic numbers (roots of polynomials over `QQ`). Early versions of the code saved
these as floating-point approximations, which are unsuitable for exact verification or
downstream lattice work.

## Current rendering method

The exact coordinate rendering path now uses:

```python
QQbar.polynomial_root(
    AA.common_polynomial(minpoly),
    isolating_interval(...)
)
```

This produces:
- a defining polynomial over `QQ` for each algebraic coordinate;
- an isolating interval that uniquely identifies the root;
- exact symbolic coordinates suitable for further exact computation.

## Where this is implemented

- `computations/task1_1_sextic.sage` (example 1)
- `computations/task1_1_sextic_example2.sage` (example 2)
- `computations/task1_1_sextic_example3.sage` (example 3)

Each script saves exact node coordinates to its corresponding output file:
- `computations/task1_1_example1_output.txt`
- `computations/task1_1_example2_output.txt`
- `computations/task1_1_example3_output.txt`

## Why this matters

Exact algebraic coordinates allow:
- verification that the nodes satisfy the sextic equation exactly (not approximately);
- downstream lattice computations that require exact rational or algebraic input;
- reproducible results independent of floating-point precision settings.

## What this note does not claim

- It does not claim this rendering method is the only correct approach.
- It does not claim the coordinates are rational (they are generally algebraic over
  `QQ`).
- It does not replace the birationality verification recorded in
  `audit/task1_1_birationality_note.md`.

Its role is narrower: it documents the exact-coordinate rendering path so that result
does not live only in code and raw output artifacts.
