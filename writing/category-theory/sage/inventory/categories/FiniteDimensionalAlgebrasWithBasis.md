# FiniteDimensionalAlgebrasWithBasis

| field | value |
| --- | --- |
| module | `finite_dimensional_algebras_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | AlgebrasWithBasis + axiom FiniteDimensional |
| direct defining axiom | [`FiniteDimensional`](../../axioms/FiniteDimensional.md) |
| syntactic axiom chain | [`Associative`](../../axioms/Associative.md), [`Unital`](../../axioms/Unital.md), [`WithBasis`](../../axioms/WithBasis.md), [`FiniteDimensional`](../../axioms/FiniteDimensional.md) |
| bound as | `AlgebrasWithBasis.FiniteDimensional` |
| bases | [`CategoryWithAxiom_over_base_ring`](../../categories/CategoryWithAxiom_over_base_ring.md) |
| source | [`src/sage/categories/finite_dimensional_algebras_with_basis.py:36`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_algebras_with_basis.py#L36) |
| loads at 10.10 | yes |

## Local axiom paths

- `Cellular`

## Local construction paths

- `Cellular.TensorProducts`

## Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Cellular`](../../axioms/Cellular.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/finite_dimensional_algebras_with_basis.py:1571`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_algebras_with_basis.py#L1571) |
| [`Cellular`](../../axioms/Cellular.md) | axiom | subcategory interface method | `_with_axiom(Cellular)` | [`src/sage/categories/finite_dimensional_algebras_with_basis.py:2020`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_algebras_with_basis.py#L2020) |
| [`TensorProducts`](../../constructions/TensorProducts.md) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/finite_dimensional_algebras_with_basis.py:1846`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_algebras_with_basis.py#L1846) |

## Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `FiniteDimensionalAlgebrasWithBasis` | `finite_dimensional_algebras_with_basis` | `(framework base)` |
| `FiniteDimensionalAlgebrasWithBasis.Cellular` | `finite_dimensional_algebras_with_basis` | `Cellular` |

## Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `FiniteDimensionalAlgebrasWithBasis.Cellular.TensorProducts` | `finite_dimensional_algebras_with_basis` | `TensorProducts` |
