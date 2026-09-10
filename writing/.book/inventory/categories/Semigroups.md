# Semigroups

| field | value |
| --- | --- |
| module | `semigroups` |
| role | public named category class |
| implementation | Python class |
| defined by | Magmas + axiom Associative |
| direct defining axiom | [`Associative`](../../axioms/Associative.md) |
| syntactic axiom chain | [`Associative`](../../axioms/Associative.md) |
| bound as | `Magmas.Associative` |
| bases | [`CategoryWithAxiom`](../../categories/CategoryWithAxiom.md) |
| source | [`src/sage/categories/semigroups.py:30`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L30) |
| loads at 10.10 | yes |

## Local axiom paths

- `Aperiodic`
- `Finite`
- `FinitelyGeneratedAsMagma`
- `HTrivial`
- `JTrivial`
- `LTrivial`
- `RTrivial`
- `Unital`

## Local construction paths

- `Algebras`
- `CartesianProducts`
- `Quotients`
- `Subquotients`

## Declared features (17)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Algebras`](../../constructions/Algebras.md) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/semigroups.py:872`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L872) |
| [`Aperiodic`](../../axioms/Aperiodic.md) | axiom | lazy-import binding | `sage.categories.aperiodic_semigroups.AperiodicSemigroups` | [`src/sage/categories/semigroups.py:783`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L783) |
| [`Aperiodic`](../../axioms/Aperiodic.md) | axiom | subcategory interface method | `_with_axiom(Aperiodic)` | [`src/sage/categories/semigroups.py:729`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L729) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/semigroups.py:856`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L856) |
| [`Finite`](../../axioms/Finite.md) | axiom | lazy-import binding | `sage.categories.finite_semigroups.FiniteSemigroups` | [`src/sage/categories/semigroups.py:776`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L776) |
| [`FinitelyGeneratedAsMagma`](../../axioms/FinitelyGeneratedAsMagma.md) | axiom | lazy-import binding | `sage.categories.finitely_generated_semigroups.FinitelyGeneratedSemigroups` | [`src/sage/categories/semigroups.py:777`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L777) |
| [`HTrivial`](../../axioms/HTrivial.md) | axiom | lazy-import binding | `sage.categories.h_trivial_semigroups.HTrivialSemigroups` | [`src/sage/categories/semigroups.py:782`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L782) |
| [`HTrivial`](../../axioms/HTrivial.md) | axiom | subcategory interface method | `_with_axiom(HTrivial)` | [`src/sage/categories/semigroups.py:692`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L692) |
| [`JTrivial`](../../axioms/JTrivial.md) | axiom | lazy-import binding | `sage.categories.j_trivial_semigroups.JTrivialSemigroups` | [`src/sage/categories/semigroups.py:781`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L781) |
| [`JTrivial`](../../axioms/JTrivial.md) | axiom | subcategory interface method | `_with_axiom(JTrivial)` | [`src/sage/categories/semigroups.py:636`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L636) |
| [`LTrivial`](../../axioms/LTrivial.md) | axiom | lazy-import binding | `sage.categories.l_trivial_semigroups.LTrivialSemigroups` | [`src/sage/categories/semigroups.py:779`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L779) |
| [`LTrivial`](../../axioms/LTrivial.md) | axiom | subcategory interface method | `_with_axiom(LTrivial)` | [`src/sage/categories/semigroups.py:546`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L546) |
| [`Quotients`](../../constructions/Quotients.md) | functorial construction | nested category class | `QuotientsCategory` | [`src/sage/categories/semigroups.py:826`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L826) |
| [`RTrivial`](../../axioms/RTrivial.md) | axiom | lazy-import binding | `sage.categories.r_trivial_semigroups.RTrivialSemigroups` | [`src/sage/categories/semigroups.py:780`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L780) |
| [`RTrivial`](../../axioms/RTrivial.md) | axiom | subcategory interface method | `_with_axiom(RTrivial)` | [`src/sage/categories/semigroups.py:591`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L591) |
| [`Subquotients`](../../constructions/Subquotients.md) | functorial construction | nested category class | `SubquotientsCategory` | [`src/sage/categories/semigroups.py:786`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L786) |
| [`Unital`](../../axioms/Unital.md) | axiom | lazy-import binding | `sage.categories.monoids.Monoids` | [`src/sage/categories/semigroups.py:778`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semigroups.py#L778) |

## Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `Semigroups` | `semigroups` | `(framework base)` |
| `Semigroups_with_category` | `semigroups` | `(framework base)` |

## Construction-generated classes at 10.10 (6)

| class | module | construction |
| --- | --- | --- |
| `Semigroups.Algebras` | `semigroups` | `Algebras` |
| `Semigroups.CartesianProducts` | `semigroups` | `CartesianProducts` |
| `Semigroups.Quotients` | `semigroups` | `Quotients` |
| `Semigroups.Quotients_with_category` | `semigroups` | `Quotients_with_category` |
| `Semigroups.Subquotients` | `semigroups` | `Subquotients` |
| `Semigroups.Subquotients_with_category` | `semigroups` | `Subquotients_with_category` |
