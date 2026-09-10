# HopfAlgebras

| field | value |
| --- | --- |
| module | `hopf_algebras` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_over_base_ring`](../../categories/Category_over_base_ring.md) |
| source | [`src/sage/categories/hopf_algebras.py:21`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L21) |
| loads at 10.10 | yes |

## Local axiom paths

- `WithBasis`

## Local construction paths

- `Realizations`
- `Super`
- `TensorProducts`

## Other local category paths

- `DualCategory`
- `Morphism`

## Declared features (6)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| `DualCategory` | other category | nested category class | `Category_over_base_ring` | [`src/sage/categories/hopf_algebras.py:176`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L176) |
| `Morphism` | other category | nested category class | `Category` | [`src/sage/categories/hopf_algebras.py:103`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L103) |
| [`Realizations`](../../constructions/Realizations.md) | functorial construction | nested category class | `RealizationsCategory` | [`src/sage/categories/hopf_algebras.py:187`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L187) |
| [`Super`](../../constructions/Super.md) | functorial construction | nested category class | `SuperModulesCategory` | [`src/sage/categories/hopf_algebras.py:109`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L109) |
| [`TensorProducts`](../../constructions/TensorProducts.md) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/hopf_algebras.py:147`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L147) |
| [`WithBasis`](../../axioms/WithBasis.md) | axiom | lazy-import binding | `sage.categories.hopf_algebras_with_basis.HopfAlgebrasWithBasis` | [`src/sage/categories/hopf_algebras.py:60`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras.py#L60) |

## Construction-generated classes at 10.10 (3)

| class | module | construction |
| --- | --- | --- |
| `HopfAlgebras.Realizations` | `hopf_algebras` | `Realizations` |
| `HopfAlgebras.Super` | `hopf_algebras` | `Super` |
| `HopfAlgebras.TensorProducts` | `hopf_algebras` | `TensorProducts` |
