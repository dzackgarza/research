# AlgebrasWithBasis

| field | value |
| --- | --- |
| module | `algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | Algebras + axiom WithBasis |
| direct defining axiom | [`WithBasis`](../../axioms/WithBasis.md) |
| syntactic axiom chain | [`Associative`](../../axioms/Associative.md), [`Unital`](../../axioms/Unital.md), [`WithBasis`](../../axioms/WithBasis.md) |
| bound as | `Algebras.WithBasis` |
| bases | [`CategoryWithAxiom_over_base_ring`](../../categories/CategoryWithAxiom_over_base_ring.md) |
| source | [`src/sage/categories/algebras_with_basis.py:21`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L21) |
| loads at 10.10 | yes |

## Local axiom paths

- `FiniteDimensional`

## Local construction paths

- `CartesianProducts`
- `Filtered`
- `Graded`
- `Super`
- `TensorProducts`

## Declared features (6)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/algebras_with_basis.py:200`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L200) |
| [`Filtered`](../../constructions/Filtered.md) | functorial construction | lazy-import binding | `sage.categories.filtered_algebras_with_basis.FilteredAlgebrasWithBasis` | [`src/sage/categories/algebras_with_basis.py:124`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L124) |
| [`FiniteDimensional`](../../axioms/FiniteDimensional.md) | axiom | lazy-import binding | `sage.categories.finite_dimensional_algebras_with_basis.FiniteDimensionalAlgebrasWithBasis` | [`src/sage/categories/algebras_with_basis.py:125`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L125) |
| [`Graded`](../../constructions/Graded.md) | functorial construction | lazy-import binding | `sage.categories.graded_algebras_with_basis.GradedAlgebrasWithBasis` | [`src/sage/categories/algebras_with_basis.py:126`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L126) |
| [`Super`](../../constructions/Super.md) | functorial construction | lazy-import binding | `sage.categories.super_algebras_with_basis.SuperAlgebrasWithBasis` | [`src/sage/categories/algebras_with_basis.py:127`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L127) |
| [`TensorProducts`](../../constructions/TensorProducts.md) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/algebras_with_basis.py:283`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L283) |

## Axiom-generated classes at 10.10 (1)

| class | module | axiom |
| --- | --- | --- |
| `AlgebrasWithBasis` | `algebras_with_basis` | `(framework base)` |

## Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `AlgebrasWithBasis.CartesianProducts` | `algebras_with_basis` | `CartesianProducts` |
| `AlgebrasWithBasis.TensorProducts` | `algebras_with_basis` | `TensorProducts` |
