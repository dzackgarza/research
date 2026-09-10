# MetricSpaces

| field | value |
| --- | --- |
| module | `metric_spaces` |
| role | public named category class |
| implementation | Python class |
| defined by | Sets.Metric() |
| defining construction | [`Metric`](../../constructions/Metric.md) |
| bound as | `Sets.Metric` |
| bases | [`MetricSpacesCategory`](../../categories/MetricSpacesCategory.md) |
| source | [`src/sage/categories/metric_spaces.py:76`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L76) |
| loads at 10.10 | yes |

## Local axiom paths

- `Complete`

## Local construction paths

- `CartesianProducts`
- `Homsets`
- `WithRealizations`
- `Complete.CartesianProducts`

## Declared features (6)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/metric_spaces.py:283`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L283) |
| [`Complete`](../../axioms/Complete.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/metric_spaces.py:347`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L347) |
| [`Complete`](../../axioms/Complete.md) | axiom | subcategory interface method | `_with_axiom(Complete)` | [`src/sage/categories/metric_spaces.py:330`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L330) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/metric_spaces.py:352`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L352) |
| [`Homsets`](../../constructions/Homsets.md) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/metric_spaces.py:224`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L224) |
| [`WithRealizations`](../../constructions/WithRealizations.md) | functorial construction | nested category class | `WithRealizationsCategory` | [`src/sage/categories/metric_spaces.py:263`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/metric_spaces.py#L263) |

## Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `MetricSpaces.Complete` | `metric_spaces` | `Complete` |
| `MetricSpaces.Complete_with_category` | `metric_spaces` | `Complete_with_category` |

## Construction-generated classes at 10.10 (6)

| class | module | construction |
| --- | --- | --- |
| `MetricSpaces` | `metric_spaces` | `(framework base)` |
| `MetricSpaces.CartesianProducts` | `metric_spaces` | `CartesianProducts` |
| `MetricSpaces.Complete.CartesianProducts` | `metric_spaces` | `CartesianProducts` |
| `MetricSpaces.Homsets` | `metric_spaces` | `Homsets` |
| `MetricSpaces.WithRealizations` | `metric_spaces` | `WithRealizations` |
| `MetricSpaces_with_category` | `metric_spaces` | `(framework base)` |
