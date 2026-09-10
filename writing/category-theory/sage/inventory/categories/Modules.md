# Modules

| field | value |
| --- | --- |
| module | `modules` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category_module`](../../categories/Category_module.md) |
| source | [`src/sage/categories/modules.py:33`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L33) |
| loads at 10.10 | yes |

## Local axiom paths

- `FiniteDimensional`
- `FinitelyPresented`
- `WithBasis`
- `Homsets.Endset`

## Local construction paths

- `CartesianProducts`
- `dual`
- `DualObjects`
- `Filtered`
- `Graded`
- `Homsets`
- `Super`
- `TensorProducts`
- `FiniteDimensional.TensorProducts`

## Declared features (20)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`CartesianProducts`](../../constructions/CartesianProducts.md) | functorial construction | nested category class | `CartesianProductsCategory` | [`src/sage/categories/modules.py:832`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L832) |
| [`DualObjects`](../../constructions/DualObjects.md) | functorial construction | subcategory interface method | `DualObjectsCategory.category_of(...)` | [`src/sage/categories/modules.py:263`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L263) |
| [`Filtered`](../../constructions/Filtered.md) | functorial construction | lazy-import binding | `sage.categories.filtered_modules.FilteredModules` | [`src/sage/categories/modules.py:593`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L593) |
| [`Filtered`](../../constructions/Filtered.md) | functorial construction | subcategory interface method | `FilteredModulesCategory.category_of(...)` | [`src/sage/categories/modules.py:384`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L384) |
| [`FiniteDimensional`](../../axioms/FiniteDimensional.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/modules.py:514`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L514) |
| [`FiniteDimensional`](../../axioms/FiniteDimensional.md) | axiom | subcategory interface method | `_with_axiom(FiniteDimensional)` | [`src/sage/categories/modules.py:341`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L341) |
| [`TensorProducts`](../../constructions/TensorProducts.md) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/modules.py:545`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L545) |
| [`FinitelyPresented`](../../axioms/FinitelyPresented.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/modules.py:562`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L562) |
| [`FinitelyPresented`](../../axioms/FinitelyPresented.md) | axiom | subcategory interface method | `_with_axiom(FinitelyPresented)` | [`src/sage/categories/modules.py:363`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L363) |
| [`Graded`](../../constructions/Graded.md) | functorial construction | lazy-import binding | `sage.categories.graded_modules.GradedModules` | [`src/sage/categories/modules.py:594`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L594) |
| [`Graded`](../../constructions/Graded.md) | functorial construction | subcategory interface method | `GradedModulesCategory.category_of(...)` | [`src/sage/categories/modules.py:420`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L420) |
| [`Homsets`](../../constructions/Homsets.md) | functorial construction | nested category class | `HomsetsCategory` | [`src/sage/categories/modules.py:720`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L720) |
| [`Endset`](../../axioms/Endset.md) | axiom | nested category class | `CategoryWithAxiom_over_base_ring` | [`src/sage/categories/modules.py:810`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L810) |
| [`Super`](../../constructions/Super.md) | functorial construction | lazy-import binding | `sage.categories.super_modules.SuperModules` | [`src/sage/categories/modules.py:595`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L595) |
| [`Super`](../../constructions/Super.md) | functorial construction | subcategory interface method | `SuperModulesCategory.category_of(...)` | [`src/sage/categories/modules.py:456`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L456) |
| [`TensorProducts`](../../constructions/TensorProducts.md) | functorial construction | nested category class | `TensorProductsCategory` | [`src/sage/categories/modules.py:932`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L932) |
| [`TensorProducts`](../../constructions/TensorProducts.md) | functorial construction | subcategory interface method | `TensorProductsCategory.category_of(...)` | [`src/sage/categories/modules.py:245`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L245) |
| [`WithBasis`](../../axioms/WithBasis.md) | axiom | lazy-import binding | `sage.categories.modules_with_basis.ModulesWithBasis` | [`src/sage/categories/modules.py:597`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L597) |
| [`WithBasis`](../../axioms/WithBasis.md) | axiom | subcategory interface method | `_with_axiom(WithBasis)` | [`src/sage/categories/modules.py:492`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L492) |
| [`DualObjects`](../../constructions/DualObjects.md) | functorial construction | subcategory API alias | `DualObjects` | [`src/sage/categories/modules.py:338`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L338) |

## Axiom-generated classes at 10.10 (3)

| class | module | axiom |
| --- | --- | --- |
| `Modules.FiniteDimensional` | `modules` | `FiniteDimensional` |
| `Modules.FinitelyPresented` | `modules` | `FinitelyPresented` |
| `Modules.Homsets.Endset` | `modules` | `Endset` |

## Construction-generated classes at 10.10 (4)

| class | module | construction |
| --- | --- | --- |
| `Modules.CartesianProducts` | `modules` | `CartesianProducts` |
| `Modules.FiniteDimensional.TensorProducts` | `modules` | `TensorProducts` |
| `Modules.Homsets` | `modules` | `Homsets` |
| `Modules.TensorProducts` | `modules` | `TensorProducts` |
