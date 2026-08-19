# Lattice Foundation Test Style

The lattice foundation tests should read like mathematics, not like a wrapper
audit.

## Weak Test Styles

- Testing Sage instead of the repository-owned interface.
  The only required Sage interop tests are routing tests at the boundary, e.g.
  `Lattice.from_gram(...)` agreeing with the corresponding foundation
  constructor after the sign convention is accounted for.
- Inflating test count by splitting one mathematical theorem into many trivial
  wrapper checks.
- Building lattices in tests with raw `diagonal_matrix`, ad hoc Gram matrices,
  or local helper constructors when the foundation already owns the noun.
- Checking only weak shadows of known facts:
  cardinality instead of discriminant-form isometry,
  prime-power cardinality instead of the exact finite quadratic module,
  nonempty/image-size checks instead of exact semantic equalities.
- Using iterator trivia like `next(iter(L.gens()))` when the exact number of
  generators is known from theory and the test should say which generators are
  being discussed.
- Encoding quality-control noise into mathematical assertions, e.g.
  `is_one()` when the mathematical fact is `== 1`.

## Preferred Replacement Style

- Group tests by lattice family or theorem:
  `A_n`, `B_n`, `C_n`, `D_n`, `E_n`, `F_4`, `G_2`, standard indefinite models,
  and narrow boundary-routing tests.
- State exact theory-backed invariants as functions of the family parameter:
  Gram matrix, determinant, parity, signature, scale, simple-root norms,
  simple-root divisibilities, isotropy, and discriminant-form isometry class.
- Use only semantic constructors from the foundation layer in tests:
  `Lattice.A(n)`, `Lattice.U()`, `Lattice.rescale(...)`,
  `DiscriminantGroup.from_invariants_and_gram(...)`, etc.
- When an expected object cannot be expressed cleanly with the current public
  vocabulary, treat that as a foundation defect and add the missing noun/verb to
  `src/` instead of hiding the gap with test-local helpers.
- Prefer exact semantic relations:
  lattice isometry,
  discriminant-form isometry,
  exact Gram matrix equality,
  exact signatures and determinants.

## API Guidance Exposed By The Test Rewrite

- `scale()` is an invariant extractor:
  the ideal `<beta(L, L)>` in `ZZ`.
- Scalar multiplication of the form belongs under `twist(...)` or
  `rescale(...)`, not `scale(...)`.
- For integral elements of `L`, `discriminant_class()` is always the zero class
  in `L^*/L`.
  The nontrivial discriminant-class operation belongs on dual-lattice or
  rational-lattice elements.
  The correct long-term interface direction is a distinct `DualLattice` layer
  whose elements project canonically to the discriminant group.

## Delegation Rule

The foundation layer should compose known exact computations from Sage, GAP,
Julia, or other existing backends.
Do not introduce custom mathematical algorithms where a known backend already
owns the computation.
The repository owns the semantic interface and the composition logic, not a new
reimplementation of standard lattice theory algorithms.
