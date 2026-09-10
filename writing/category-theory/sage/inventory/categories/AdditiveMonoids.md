# AdditiveMonoids

| field | value |
| --- | --- |
| module | `additive_monoids` |
| role | public named category class |
| implementation | Python class |
| defined by | AdditiveSemigroups + axiom AdditiveUnital |
| direct defining axiom | [`AdditiveUnital`](../../axioms/AdditiveUnital.md) |
| syntactic axiom chain | [`AdditiveAssociative`](../../axioms/AdditiveAssociative.md), [`AdditiveUnital`](../../axioms/AdditiveUnital.md) |
| bound as | `AdditiveSemigroups.AdditiveUnital` |
| bases | [`CategoryWithAxiom_singleton`](../../categories/CategoryWithAxiom_singleton.md) |
| source | [`src/sage/categories/additive_monoids.py:17`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_monoids.py#L17) |
| loads at 10.10 | yes |

## Local axiom paths

- `AdditiveCommutative`
- `AdditiveInverse`

## Local construction paths

- `Homsets`

## Declared features (3)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`AdditiveCommutative`](../../axioms/AdditiveCommutative.md) | axiom | lazy-import binding | `sage.categories.commutative_additive_monoids.CommutativeAdditiveMonoids` | [`src/sage/categories/additive_monoids.py:47`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_monoids.py#L47) |
| [`AdditiveInverse`](../../axioms/AdditiveInverse.md) | axiom | lazy-import binding | `sage.categories.additive_groups.AdditiveGroups` | [`src/sage/categories/additive_monoids.py:48`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_monoids.py#L48) |
| [`Homsets`](../../constructions/Homsets.md) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/additive_monoids.py:89`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_monoids.py#L89) |

## Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `AdditiveMonoids` | `additive_monoids` | `(framework base)` |
| `AdditiveMonoids_with_category` | `additive_monoids` | `(framework base)` |

## Construction-generated classes at 10.10 (1)

| class | module | construction |
| --- | --- | --- |
| `AdditiveMonoids.Homsets` | `additive_monoids` | `Homsets` |
