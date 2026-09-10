# AdditiveMagmas

| field | value |
| --- | --- |
| module | `additive_magmas` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_singleton`](../../categories/Category_singleton.md) |
| source | [`src/sage/categories/additive_magmas.py:25`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L25) |
| loads at 10.10 | yes |

## Local axiom paths

- `AdditiveAssociative`
- `AdditiveCommutative`
- `AdditiveUnital`
- `AdditiveUnital.AdditiveInverse`

## Local construction paths

- `Algebras`
- `CartesianProducts`
- `Homsets`
- `AdditiveCommutative.Algebras`
- `AdditiveCommutative.CartesianProducts`
- `AdditiveUnital.Algebras`
- `AdditiveUnital.CartesianProducts`
- `AdditiveUnital.Homsets`
- `AdditiveUnital.WithRealizations`
- `AdditiveUnital.AdditiveInverse.CartesianProducts`

## Declared features (18)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`AdditiveAssociative`](../../axioms/AdditiveAssociative.md) | axiom | lazy-import binding | `sage.categories.additive_semigroups.AdditiveSemigroups` | [`src/sage/categories/additive_magmas.py:167`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L167) |
| [`AdditiveAssociative`](../../axioms/AdditiveAssociative.md) | axiom | subcategory interface method | `_with_axiom(AdditiveAssociative)` | [`src/sage/categories/additive_magmas.py:78`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L78) |
| [`AdditiveCommutative`](../../axioms/AdditiveCommutative.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/additive_magmas.py:563`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L563) |
| [`AdditiveCommutative`](../../axioms/AdditiveCommutative.md) | axiom | subcategory interface method | `_with_axiom(AdditiveCommutative)` | [`src/sage/categories/additive_magmas.py:104`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L104) |
| [`Algebras`](../../constructions/Algebras.md) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/additive_magmas.py:580`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L580) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/additive_magmas.py:564`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L564) |
| [`AdditiveUnital`](../../axioms/AdditiveUnital.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/additive_magmas.py:599`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L599) |
| [`AdditiveUnital`](../../axioms/AdditiveUnital.md) | axiom | subcategory interface method | `_with_axiom(AdditiveUnital)` | [`src/sage/categories/additive_magmas.py:134`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L134) |
| [`AdditiveInverse`](../../axioms/AdditiveInverse.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/additive_magmas.py:898`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L898) |
| [`AdditiveInverse`](../../axioms/AdditiveInverse.md) | axiom | subcategory interface method | `_with_axiom(AdditiveInverse)` | [`src/sage/categories/additive_magmas.py:621`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L621) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/additive_magmas.py:899`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L899) |
| [`Algebras`](../../constructions/Algebras.md) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/additive_magmas.py:965`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L965) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/additive_magmas.py:936`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L936) |
| [`Homsets`](../../constructions/Homsets.md) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/additive_magmas.py:857`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L857) |
| [`WithRealizations`](../../constructions/WithRealizations.md) | functorial construction | nested category class | `WithRealizationsCategory` | [`src/sage/categories/additive_magmas.py:1008`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L1008) |
| [`Algebras`](../../constructions/Algebras.md) | functorial construction | nested category class | `AlgebrasCategory` | [`src/sage/categories/additive_magmas.py:492`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L492) |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/additive_magmas.py:452`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L452) |
| [`Homsets`](../../constructions/Homsets.md) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/additive_magmas.py:438`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/additive_magmas.py#L438) |

## Axiom-generated classes at 10.10 (6)

| class | module | axiom |
| --- | --- | --- |
| `AdditiveMagmas.AdditiveCommutative` | `additive_magmas` | `AdditiveCommutative` |
| `AdditiveMagmas.AdditiveCommutative_with_category` | `additive_magmas` | `AdditiveCommutative_with_category` |
| `AdditiveMagmas.AdditiveUnital` | `additive_magmas` | `AdditiveUnital` |
| `AdditiveMagmas.AdditiveUnital.AdditiveInverse` | `additive_magmas` | `AdditiveInverse` |
| `AdditiveMagmas.AdditiveUnital.AdditiveInverse_with_category` | `additive_magmas` | `AdditiveInverse_with_category` |
| `AdditiveMagmas.AdditiveUnital_with_category` | `additive_magmas` | `AdditiveUnital_with_category` |

## Construction-generated classes at 10.10 (10)

| class | module | construction |
| --- | --- | --- |
| `AdditiveMagmas.AdditiveCommutative.Algebras` | `additive_magmas` | `Algebras` |
| `AdditiveMagmas.AdditiveCommutative.CartesianProducts` | `additive_magmas` | `CartesianProducts` |
| `AdditiveMagmas.AdditiveUnital.AdditiveInverse.CartesianProducts` | `additive_magmas` | `CartesianProducts` |
| `AdditiveMagmas.AdditiveUnital.Algebras` | `additive_magmas` | `Algebras` |
| `AdditiveMagmas.AdditiveUnital.CartesianProducts` | `additive_magmas` | `CartesianProducts` |
| `AdditiveMagmas.AdditiveUnital.Homsets` | `additive_magmas` | `Homsets` |
| `AdditiveMagmas.AdditiveUnital.WithRealizations` | `additive_magmas` | `WithRealizations` |
| `AdditiveMagmas.Algebras` | `additive_magmas` | `Algebras` |
| `AdditiveMagmas.CartesianProducts` | `additive_magmas` | `CartesianProducts` |
| `AdditiveMagmas.Homsets` | `additive_magmas` | `Homsets` |
