# MagmaticAlgebras

| field | value |
| --- | --- |
| module | `magmatic_algebras` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](../../categories/Category_over_base_ring.md) |
| source | [`src/sage/categories/magmatic_algebras.py:23`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmatic_algebras.py#L23) |
| loads at 10.10 | yes |

## Local axiom paths

- `Associative`
- `Unital`
- `WithBasis`
- `WithBasis.FiniteDimensional`

## Declared features (4)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Associative`](../../axioms/Associative.md) | axiom | lazy-import binding | `sage.categories.associative_algebras.AssociativeAlgebras` | [`src/sage/categories/magmatic_algebras.py:100`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmatic_algebras.py#L100) |
| [`Unital`](../../axioms/Unital.md) | axiom | lazy-import binding | `sage.categories.unital_algebras.UnitalAlgebras` | [`src/sage/categories/magmatic_algebras.py:101`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmatic_algebras.py#L101) |
| [`WithBasis`](../../axioms/WithBasis.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/magmatic_algebras.py:119`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmatic_algebras.py#L119) |
| [`FiniteDimensional`](../../axioms/FiniteDimensional.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/magmatic_algebras.py:224`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmatic_algebras.py#L224) |

## Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `MagmaticAlgebras.WithBasis` | `magmatic_algebras` | `WithBasis` |
| `MagmaticAlgebras.WithBasis.FiniteDimensional` | `magmatic_algebras` | `FiniteDimensional` |
