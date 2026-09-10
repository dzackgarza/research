# Rings

| field | value |
| --- | --- |
| module | `rings` |
| role | public named category class |
| implementation | Python class |
| defined by | Rngs + axiom Unital |
| direct defining axiom | [`Unital`](../../axioms/Unital.md) |
| syntactic axiom chain | [`Distributive`](../../axioms/Distributive.md), [`AdditiveAssociative`](../../axioms/AdditiveAssociative.md), [`AdditiveCommutative`](../../axioms/AdditiveCommutative.md), [`AdditiveUnital`](../../axioms/AdditiveUnital.md), [`Associative`](../../axioms/Associative.md), [`AdditiveInverse`](../../axioms/AdditiveInverse.md), [`Unital`](../../axioms/Unital.md) |
| bound as | `Rngs.Unital` |
| bases | [`CategoryWithAxiom`](../../categories/CategoryWithAxiom.md) |
| source | [`src/sage/categories/rings.py:24`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L24) |
| loads at 10.10 | yes |

## Local axiom paths

- `Commutative`
- `Division`
- `NoZeroDivisors`

## Declared features (5)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Commutative`](../../axioms/Commutative.md) | axiom | lazy-import binding | `sage.categories.commutative_rings.CommutativeRings` | [`src/sage/categories/rings.py:311`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L311) |
| [`Division`](../../axioms/Division.md) | axiom | lazy-import binding | `sage.categories.division_rings.DivisionRings` | [`src/sage/categories/rings.py:310`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L310) |
| [`Division`](../../axioms/Division.md) | axiom | subcategory interface method | `_with_axiom(Division)` | [`src/sage/categories/rings.py:287`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L287) |
| [`NoZeroDivisors`](../../axioms/NoZeroDivisors.md) | axiom | lazy-import binding | `sage.categories.domains.Domains` | [`src/sage/categories/rings.py:309`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L309) |
| [`NoZeroDivisors`](../../axioms/NoZeroDivisors.md) | axiom | subcategory interface method | `_with_axiom(NoZeroDivisors)` | [`src/sage/categories/rings.py:264`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/rings.py#L264) |

## Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `Rings` | `rings` | `(framework base)` |
| `Rings_with_category` | `rings` | `(framework base)` |
