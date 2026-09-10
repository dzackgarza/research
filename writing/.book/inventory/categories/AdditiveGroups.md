# AdditiveGroups

| field | value |
| --- | --- |
| module | `additive_groups` |
| role | public named category class |
| implementation | Python class |
| defined by | AdditiveMonoids + axiom AdditiveInverse |
| direct defining axiom | [`AdditiveInverse`](../../axioms/AdditiveInverse.md) |
| syntactic axiom chain | [`AdditiveAssociative`](../../axioms/AdditiveAssociative.md), [`AdditiveUnital`](../../axioms/AdditiveUnital.md), [`AdditiveInverse`](../../axioms/AdditiveInverse.md) |
| bound as | `AdditiveMonoids.AdditiveInverse` |
| bases | [`CategoryWithAxiom_singleton`](../../categories/CategoryWithAxiom_singleton.md) |
| source | [`src/sage/categories/additive_groups.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_groups.py#L19) |
| loads at 10.10 | yes |

## Local axiom paths

- `AdditiveCommutative`
- `Finite`

## Local construction paths

- `Algebras`
- `Finite.Algebras`

## Declared features (4)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`AdditiveCommutative`](../../axioms/AdditiveCommutative.md) | axiom | lazy-import binding | `sage.categories.commutative_additive_groups.CommutativeAdditiveGroups` | [`src/sage/categories/additive_groups.py:69`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_groups.py#L69) |
| [`Algebras`](../../constructions/Algebras.md) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/additive_groups.py:58`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_groups.py#L58) |
| [`Finite`](../../axioms/Finite.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/additive_groups.py:62`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_groups.py#L62) |
| [`Algebras`](../../constructions/Algebras.md) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/additive_groups.py:63`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_groups.py#L63) |

## Axiom-generated classes at 10.10 (3)

| class | module | axiom |
| --- | --- | --- |
| `AdditiveGroups` | `additive_groups` | `(framework base)` |
| `AdditiveGroups.Finite` | `additive_groups` | `Finite` |
| `AdditiveGroups_with_category` | `additive_groups` | `(framework base)` |

## Construction-generated classes at 10.10 (2)

| class | module | construction |
| --- | --- | --- |
| `AdditiveGroups.Algebras` | `additive_groups` | `Algebras` |
| `AdditiveGroups.Finite.Algebras` | `additive_groups` | `Algebras` |
