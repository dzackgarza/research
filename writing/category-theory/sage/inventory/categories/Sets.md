# Sets

| field | value |
| --- | --- |
| module | `sets_cat` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](../../categories/Category_singleton.md) |
| source | [`src/sage/categories/sets_cat.py:98`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L98) |
| loads at 10.10 | yes |

## Local axiom paths

- `Enumerated`
- `Facade`
- `Finite`
- `Infinite`
- `Infinite.Finite`

## Local construction paths

- `Algebras`
- `CartesianProducts`
- `IsomorphicObjects`
- `Metric`
- `Quotients`
- `Realizations`
- `Subobjects`
- `Subquotients`
- `Topological`
- `WithRealizations`

## Declared features (26)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Algebras`](../../constructions/Algebras.md) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/sets_cat.py:2721`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2721) |
| [`Algebras`](../../constructions/Algebras.md) | functorial construction | subcategory interface method | `AlgebrasCategory.category_of(...); calls Rings()` | [`src/sage/categories/sets_cat.py:695`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L695) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/sets_cat.py:2185`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2185) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | subcategory interface method | `CartesianProductsCategory.category_of(...)` | [`src/sage/categories/sets_cat.py:303`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L303) |
| [`Enumerated`](../../axioms/Enumerated.md) | axiom | lazy-import binding | `sage.categories.enumerated_sets.EnumeratedSets` | [`src/sage/categories/sets_cat.py:1879`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1879) |
| [`Enumerated`](../../axioms/Enumerated.md) | axiom | subcategory interface method | `_with_axiom(Enumerated)` | [`src/sage/categories/sets_cat.py:776`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L776) |
| [`Facade`](../../axioms/Facade.md) | axiom | subcategory interface method | `_with_axiom(Facade)` | [`src/sage/categories/sets_cat.py:799`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L799) |
| [`Finite`](../../axioms/Finite.md) | axiom | lazy-import binding | `sage.categories.finite_sets.FiniteSets` | [`src/sage/categories/sets_cat.py:1880`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1880) |
| [`Finite`](../../axioms/Finite.md) | axiom | subcategory interface method | `_with_axiom(Finite)` | [`src/sage/categories/sets_cat.py:736`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L736) |
| [`Infinite`](../../axioms/Infinite.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/sets_cat.py:1887`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1887) |
| [`Infinite`](../../axioms/Infinite.md) | axiom | subcategory interface method | `_with_axiom(Infinite)` | [`src/sage/categories/sets_cat.py:756`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L756) |
| [`Finite`](../../axioms/Finite.md) | axiom | subcategory interface method | — | [`src/sage/categories/sets_cat.py:1890`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1890) |
| [`IsomorphicObjects`](../../constructions/IsomorphicObjects.md) | functorial construction | nested category class | `IsomorphicObjectsCategory` | [`src/sage/categories/sets_cat.py:2156`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2156) |
| [`IsomorphicObjects`](../../constructions/IsomorphicObjects.md) | functorial construction | subcategory interface method | `IsomorphicObjectsCategory.category_of(...)` | [`src/sage/categories/sets_cat.py:575`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L575) |
| [`Metric`](../../constructions/Metric.md) | functorial construction | lazy-import binding | `sage.categories.metric_spaces.MetricSpaces` | [`src/sage/categories/sets_cat.py:1883`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1883) |
| [`Metric`](../../constructions/Metric.md) | functorial construction | subcategory interface method | `MetricSpacesCategory.category_of(...)` | [`src/sage/categories/sets_cat.py:683`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L683) |
| [`Quotients`](../../constructions/Quotients.md) | functorial construction | nested category class | `QuotientsCategory` | [`src/sage/categories/sets_cat.py:2081`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2081) |
| [`Quotients`](../../constructions/Quotients.md) | functorial construction | subcategory interface method | `QuotientsCategory.category_of(...)` | [`src/sage/categories/sets_cat.py:462`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L462) |
| [`Realizations`](../../constructions/Realizations.md) | functorial construction | nested category class | `RealizationsCategory` | [`src/sage/categories/sets_cat.py:3157`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L3157) |
| [`Subobjects`](../../constructions/Subobjects.md) | functorial construction | nested category class | `SubobjectsCategory` | [`src/sage/categories/sets_cat.py:2125`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2125) |
| [`Subobjects`](../../constructions/Subobjects.md) | functorial construction | subcategory interface method | `SubobjectsCategory.category_of(...)` | [`src/sage/categories/sets_cat.py:517`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L517) |
| [`Subquotients`](../../constructions/Subquotients.md) | functorial construction | nested category class | `SubquotientsCategory` | [`src/sage/categories/sets_cat.py:1952`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1952) |
| [`Subquotients`](../../constructions/Subquotients.md) | functorial construction | subcategory interface method | `SubquotientsCategory.category_of(...)` | [`src/sage/categories/sets_cat.py:325`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L325) |
| [`Topological`](../../constructions/Topological.md) | functorial construction | lazy-import binding | `sage.categories.topological_spaces.TopologicalSpaces` | [`src/sage/categories/sets_cat.py:1881`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L1881) |
| [`Topological`](../../constructions/Topological.md) | functorial construction | subcategory interface method | `TopologicalSpacesCategory.category_of(...)` | [`src/sage/categories/sets_cat.py:671`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L671) |
| [`WithRealizations`](../../constructions/WithRealizations.md) | functorial construction | nested category class | `WithRealizationsCategory` | [`src/sage/categories/sets_cat.py:2797`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/sets_cat.py#L2797) |

## Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `Sets.Infinite` | `sets_cat` | `Infinite` |
| `Sets.Infinite_with_category` | `sets_cat` | `Infinite_with_category` |

## Construction-generated classes at 10.10 (10)

| class | module | construction |
| --- | --- | --- |
| `Sets.Algebras` | `sets_cat` | `Algebras` |
| `Sets.CartesianProducts` | `sets_cat` | `CartesianProducts` |
| `Sets.IsomorphicObjects` | `sets_cat` | `IsomorphicObjects` |
| `Sets.Quotients` | `sets_cat` | `Quotients` |
| `Sets.Quotients_with_category` | `sets_cat` | `Quotients_with_category` |
| `Sets.Realizations` | `sets_cat` | `Realizations` |
| `Sets.Subobjects` | `sets_cat` | `Subobjects` |
| `Sets.Subquotients` | `sets_cat` | `Subquotients` |
| `Sets.Subquotients_with_category` | `sets_cat` | `Subquotients_with_category` |
| `Sets.WithRealizations` | `sets_cat` | `WithRealizations` |
