# LieAlgebras

| field | value |
| --- | --- |
| module | `lie_algebras` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](../../categories/Category_over_base_ring.md) |
| source | [`src/sage/categories/lie_algebras.py:34`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L34) |
| loads at 10.10 | yes |

## Local axiom paths

- `FiniteDimensional`
- `Nilpotent`
- `WithBasis`
- `FiniteDimensional.WithBasis`

## Local construction paths

- `Graded`

## Declared features (6)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`FiniteDimensional`](../../axioms/FiniteDimensional.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/lie_algebras.py:174`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L174) |
| [`WithBasis`](../../axioms/WithBasis.md) | axiom | lazy-import binding | `sage.categories.finite_dimensional_lie_algebras_with_basis.FiniteDimensionalLieAlgebrasWithBasis` | [`src/sage/categories/lie_algebras.py:175`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L175) |
| [`Graded`](../../constructions/Graded.md) | functorial construction | lazy-import binding | `sage.categories.graded_lie_algebras.GradedLieAlgebras` | [`src/sage/categories/lie_algebras.py:112`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L112) |
| [`Nilpotent`](../../axioms/Nilpotent.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/lie_algebras.py:203`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L203) |
| [`Nilpotent`](../../axioms/Nilpotent.md) | axiom | subcategory interface method | `_with_axiom(Nilpotent)` | [`src/sage/categories/lie_algebras.py:94`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L94) |
| [`WithBasis`](../../axioms/WithBasis.md) | axiom | lazy-import binding | `sage.categories.lie_algebras_with_basis.LieAlgebrasWithBasis` | [`src/sage/categories/lie_algebras.py:171`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L171) |

## Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `LieAlgebras.FiniteDimensional` | `lie_algebras` | `FiniteDimensional` |
| `LieAlgebras.Nilpotent` | `lie_algebras` | `Nilpotent` |
