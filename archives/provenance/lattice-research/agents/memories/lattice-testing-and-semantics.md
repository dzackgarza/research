# Lattice Testing And Semantics

## Foundation Testing Style

Use family-based mathematical specification tests, not wrapper liveness probes.

### Rules

- Group tests by lattice family or theorem such as `A_n`, `B_n`, `C_n`, `D_n`, `E_n`, `F_4`, `G_2`, standard indefinite models, and minimal routing tests.
- Assert exact theory-backed invariants: Gram matrix, determinant, parity, signature, scale, simple-root norms, simple-root divisibilities, isotropy, and exact discriminant-form isometry classes.
- Use only semantic foundation constructors in tests such as `Lattice.*`, `rescale`, and `DiscriminantGroup.from_invariants_and_gram`.
- If the vocabulary is missing, add it to `src/` instead of inventing test-local constructions.
- Keep Sage routing tests narrow boundary tests only; do not spend the suite proving Sage works.
- Avoid weak assertions like cardinality-only or prime-power-only checks when the exact discriminant form is known.
- Avoid iterator trivia like `next(iter(L.gens()))` when the exact generator set is known.
- Prefer direct mathematical equalities like `== 1` over QC-noise style predicates such as `is_one()`.

## Dual And Discriminant Semantics

When working in `src/lattices/`, treat discriminant lifts and submodules semantically rather than through raw vectors.

- `DiscriminantGroupElement.lift()` should mean a lift to the dual lattice as a mathematical object.
- If backend interop needs the raw Sage representative vector, expose that explicitly as `lift_vector()` instead of overloading the semantic method.
- Do not assume a lattice or module basis matrix is square. Embedded submodules can have rectangular basis matrices, so coordinate extraction should solve against the transposed basis matrix instead of using `.inverse()`.
- Spans and orthogonal complements should return the most specific correct noun. If the result is degenerate, keep it at the `FreeBilinearModule` level rather than forcing it into `Lattice`.
- Use Sage linear algebra and native exact objects for these constructions. Do not add custom search or enumeration algorithms to fake missing generality.

## Semantic Guidance

- `scale()` is the ideal `<beta(L,L)>` in `ZZ`.
- Form multiplication belongs under `twist(...)` or `rescale(...)`, not `scale(...)`.
- `discriminant_class()` is trivial on integral lattice elements of `L`; the nontrivial semantic operation belongs on dual or rational lattice elements, motivating a future `DualLattice` layer.
- Do not introduce custom mathematical algorithms when Sage, GAP, or Julia already own the computation; the repo should compose exact backend computations into a semantic interface.
