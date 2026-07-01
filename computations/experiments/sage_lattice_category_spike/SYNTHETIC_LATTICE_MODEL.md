# Synthetic Lattice Model

## Bounded Contexts

- Synthetic lattice parent/element/homset: owned Sage parents with distinguished bases, exact `QQ`-valued symmetric forms, and explicit morphisms.
- Finite discriminant group/form: finite Smith quotient objects carrying bilinear and quadratic pairings valued in `QQ/ZZ` or `QQ/2ZZ`.
- Positive-definite algorithm adapter surface: exact lattice algorithms exposed only where the synthetic category contract owns them.

## Vocabulary

- `accepted reference contract`: Sage behavior intentionally adapted into this spike and proved by local tests.
- `lattice-aware wrapper`: Sage-native module, quotient, Smith-coordinate, or morphism behavior promoted to a lattice-category method with a lattice, quadratic-space, quotient, discriminant-form, or morphism return type.
- `raw-accessor-only`: Sage-native behavior reachable through an explicit underlying-object accessor, not promoted as a public lattice-category method.
- `native-integration-required`: Sage-native lattice/module behavior that is meaningful for the original lattice-category prompt but not completed by this synthetic spike.
- `adapted doctest/reference surface`: a Sage doctest or API locus translated into a local exact algebraic test.
- `explicit limitation`: unsupported behavior that raises a precise exception at the API boundary.

## Invariants

- Lattices are synthetic modules with distinguished bases and `QQ`-valued symmetric bilinear forms.
- Raw ambient-module and ambient-vector-space APIs are not exposed as public lattice methods in this spike; the promoted public surface is `ambient_quadratic_space()`, which preserves the rational ambient form.
- Explicit isometry generators are accepted; full generator computation is not promised.
- Odd lattices retain `QQ/ZZ` bilinear discriminant forms even when genus classification is unsupported.

## Error Policy

- External invalid input raises `TypeError`, `ValueError`, or `ArithmeticError`.
- Internal impossible states use explicit `raise AssertionError(...)`.
- Owned runtime and tests do not use `try/except`.
