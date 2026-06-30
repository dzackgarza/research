# Synthetic Lattice Model

## Bounded Contexts

- Synthetic lattice parent/element/homset: owned Sage parents with distinguished bases, exact `QQ`-valued symmetric forms, and explicit morphisms.
- Finite discriminant group/form: finite Smith quotient objects carrying bilinear and quadratic pairings valued in `QQ/ZZ` or `QQ/2ZZ`.
- Sage reference coverage accounting: a manifest that records which Sage reference loci are adapted, superseded, rejected, generic, or still pending.
- Positive-definite algorithm adapter surface: exact lattice algorithms exposed only where the synthetic category contract owns them.

## Vocabulary

- `accepted reference contract`: Sage behavior intentionally adapted into this spike and proved by local tests.
- `rejected parity`: Sage-native behavior intentionally excluded from this synthetic spike.
- `synthetic supersession`: local synthetic behavior that replaces a Sage surface because the owned model is not Sage's ambient module model.
- `adapted doctest/reference surface`: a Sage doctest or API locus translated into a local exact algebraic test.
- `explicit limitation`: unsupported behavior that raises a precise exception and is recorded in the manifest.

## Invariants

- Lattices are synthetic modules with distinguished bases and `QQ`-valued symmetric bilinear forms.
- No public ambient-vector-space API is introduced.
- Explicit isometry generators are accepted; full generator computation is not promised.
- Odd lattices retain `QQ/ZZ` bilinear discriminant forms even when genus classification is unsupported.

## Error Policy

- External invalid input raises `TypeError`, `ValueError`, or `ArithmeticError`.
- Internal impossible states use explicit `raise AssertionError(...)`.
- Owned runtime and tests do not use `try/except`.
