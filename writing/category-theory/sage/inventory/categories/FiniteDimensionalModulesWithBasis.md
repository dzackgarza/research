# FiniteDimensionalModulesWithBasis

| field | value |
| --- | --- |
| module | `finite_dimensional_modules_with_basis` |
| role | public named category class |
| implementation | Python class |
| defined by | ModulesWithBasis + axiom FiniteDimensional |
| direct defining axiom | [`FiniteDimensional`](../../axioms/FiniteDimensional.md) |
| syntactic axiom chain | [`WithBasis`](../../axioms/WithBasis.md), [`FiniteDimensional`](../../axioms/FiniteDimensional.md) |
| bound as | `ModulesWithBasis.FiniteDimensional` |
| bases | [`CategoryWithAxiom_over_base_ring`](../../categories/CategoryWithAxiom_over_base_ring.md) |
| source | [`src/sage/categories/finite_dimensional_modules_with_basis.py:21`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_modules_with_basis.py#L21) |
| loads at 10.10 | yes |

## Local axiom paths

- `Homsets.Endset`

## Local construction paths

- `Homsets`
- `TensorProducts`

## Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Homsets`](../../constructions/Homsets.md) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/finite_dimensional_modules_with_basis.py:890`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_modules_with_basis.py#L890) |
| [`Endset`](../../axioms/Endset.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/finite_dimensional_modules_with_basis.py:892`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_modules_with_basis.py#L892) |
| [`TensorProducts`](../../constructions/TensorProducts.md) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/finite_dimensional_modules_with_basis.py:1050`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/finite_dimensional_modules_with_basis.py#L1050) |

## Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `FiniteDimensionalModulesWithBasis` | `finite_dimensional_modules_with_basis` | `(framework base)` |
| `FiniteDimensionalModulesWithBasis.Homsets.Endset` | `finite_dimensional_modules_with_basis` | `Endset` |

## Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `FiniteDimensionalModulesWithBasis.Homsets` | `finite_dimensional_modules_with_basis` | `Homsets` |
| `FiniteDimensionalModulesWithBasis.TensorProducts` | `finite_dimensional_modules_with_basis` | `TensorProducts` |
