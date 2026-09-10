# AdditiveSemigroups

| field | value |
| --- | --- |
| module | `additive_semigroups` |
| role | public named category class |
| implementation | Python class |
| defined by | AdditiveMagmas + axiom AdditiveAssociative |
| direct defining axiom | [`AdditiveAssociative`](../../axioms/AdditiveAssociative.md) |
| syntactic axiom chain | [`AdditiveAssociative`](../../axioms/AdditiveAssociative.md) |
| bound as | `AdditiveMagmas.AdditiveAssociative` |
| bases | [`CategoryWithAxiom_singleton`](../../categories/CategoryWithAxiom_singleton.md) |
| source | [`src/sage/categories/additive_semigroups.py:20`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L20) |
| loads at 10.10 | yes |

## Local axiom paths

- `AdditiveCommutative`
- `AdditiveUnital`

## Local construction paths

- `Algebras`
- `CartesianProducts`
- `Homsets`

## Declared features (5)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`AdditiveCommutative`](../../axioms/AdditiveCommutative.md) | axiom | lazy-import binding | `sage.categories.commutative_additive_semigroups.CommutativeAdditiveSemigroups` | [`src/sage/categories/additive_semigroups.py:53`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L53) |
| [`AdditiveUnital`](../../axioms/AdditiveUnital.md) | axiom | lazy-import binding | `sage.categories.additive_monoids.AdditiveMonoids` | [`src/sage/categories/additive_semigroups.py:54`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L54) |
| [`Algebras`](../../constructions/Algebras.md) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/additive_semigroups.py:123`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L123) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/additive_semigroups.py:105`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L105) |
| [`Homsets`](../../constructions/Homsets.md) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/additive_semigroups.py:88`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_semigroups.py#L88) |

## Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `AdditiveSemigroups` | `additive_semigroups` | `(framework base)` |
| `AdditiveSemigroups_with_category` | `additive_semigroups` | `(framework base)` |

## Construction-generated classes at 10.10 (3)

| class | module | construction |
| --- | --- | --- |
| `AdditiveSemigroups.Algebras` | `additive_semigroups` | `Algebras` |
| `AdditiveSemigroups.CartesianProducts` | `additive_semigroups` | `CartesianProducts` |
| `AdditiveSemigroups.Homsets` | `additive_semigroups` | `Homsets` |
