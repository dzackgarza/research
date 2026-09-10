# HopfAlgebrasWithBasis

| field | value |
| --- | --- |
| module | `hopf_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | HopfAlgebras + axiom WithBasis |
| direct defining axiom | [`WithBasis`](../../axioms/WithBasis.md) |
| syntactic axiom chain | [`WithBasis`](../../axioms/WithBasis.md) |
| bound as | `HopfAlgebras.WithBasis` |
| bases | [`CategoryWithAxiom_over_base_ring`](../../categories/CategoryWithAxiom_over_base_ring.md) |
| source | [`src/sage/categories/hopf_algebras_with_basis.py:20`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L20) |
| loads at 10.10 | yes |

## Local axiom paths

- `FiniteDimensional`

## Local construction paths

- `Filtered`
- `Graded`
- `Super`
- `TensorProducts`

## Declared features (5)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Filtered`](../../constructions/Filtered.md) | functorial construction | lazy-import binding | `sage.categories.filtered_hopf_algebras_with_basis.FilteredHopfAlgebrasWithBasis` | [`src/sage/categories/hopf_algebras_with_basis.py:159`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L159) |
| [`FiniteDimensional`](../../axioms/FiniteDimensional.md) | axiom | lazy-import binding | `sage.categories.finite_dimensional_hopf_algebras_with_basis.FiniteDimensionalHopfAlgebrasWithBasis` | [`src/sage/categories/hopf_algebras_with_basis.py:157`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L157) |
| [`Graded`](../../constructions/Graded.md) | functorial construction | lazy-import binding | `sage.categories.graded_hopf_algebras_with_basis.GradedHopfAlgebrasWithBasis` | [`src/sage/categories/hopf_algebras_with_basis.py:161`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L161) |
| [`Super`](../../constructions/Super.md) | functorial construction | lazy-import binding | `sage.categories.super_hopf_algebras_with_basis.SuperHopfAlgebrasWithBasis` | [`src/sage/categories/hopf_algebras_with_basis.py:163`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L163) |
| [`TensorProducts`](../../constructions/TensorProducts.md) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/hopf_algebras_with_basis.py:284`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L284) |

## Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `HopfAlgebrasWithBasis` | `hopf_algebras_with_basis` | `(framework base)` |

## Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `HopfAlgebrasWithBasis.TensorProducts` | `hopf_algebras_with_basis` | `TensorProducts` |
