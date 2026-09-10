# FiniteDimensional

| field | value |
| --- | --- |
| status | production |
| registry entry | [`src/sage/categories/category_with_axiom.py:1676`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L1676) |
| defining categories | `finite_dimensional_algebras_with_basis.FiniteDimensionalAlgebrasWithBasis`, `finite_dimensional_bialgebras_with_basis.FiniteDimensionalBialgebrasWithBasis`, `finite_dimensional_coalgebras_with_basis.FiniteDimensionalCoalgebrasWithBasis`, `finite_dimensional_graded_lie_algebras_with_basis.FiniteDimensionalGradedLieAlgebrasWithBasis`, `finite_dimensional_hopf_algebras_with_basis.FiniteDimensionalHopfAlgebrasWithBasis`, `finite_dimensional_modules_with_basis.FiniteDimensionalModulesWithBasis` |
| interface declarations | `category_with_axiom.Blahs:FiniteDimensional; cw_complexes.CWComplexes:FiniteDimensional; manifolds.Manifolds:FiniteDimensional; modules.Modules:FiniteDimensional` |
| implementation or binding | `algebras_with_basis.AlgebrasWithBasis:FiniteDimensional [lazy-import binding]; category_with_axiom.Blahs:FiniteDimensional [nested category class]; category_with_axiom.DummyObjectsOverBaseRing:Commutative.FiniteDimensional [nested category class]; category_with_axiom.DummyObjectsOverBaseRing:FiniteDimensional [nested category class]; category_with_axiom.TestObjects:Commutative.FiniteDimensional [nested category class]; category_with_axiom.TestObjects:FiniteDimensional [nested category class]; cw_complexes.CWComplexes:FiniteDimensional [nested category class]; filtered_modules_with_basis.FilteredModulesWithBasis:FiniteDimensional [nested category class]; graded_algebras_with_basis.GradedAlgebrasWithBasis:FiniteDimensional [nested category class]; graded_lie_algebras.GradedLieAlgebras:Stratified.FiniteDimensional [nested category class]; graded_lie_algebras_with_basis.GradedLieAlgebrasWithBasis:FiniteDimensional [lazy-import binding]; hopf_algebras_with_basis.HopfAlgebrasWithBasis:FiniteDimensional [lazy-import binding]; lie_algebras.LieAlgebras:FiniteDimensional [nested category class]; magmatic_algebras.MagmaticAlgebras:WithBasis.FiniteDimensional [nested category class]; manifolds.Manifolds:FiniteDimensional [nested category class]; modules.Modules:FiniteDimensional [nested category class]; modules_with_basis.ModulesWithBasis:FiniteDimensional [lazy-import binding]; semisimple_algebras.SemisimpleAlgebras:FiniteDimensional [nested category class]; triangular_kac_moody_algebras.TriangularKacMoodyAlgebras:FiniteDimensional [nested category class]; vector_spaces.VectorSpaces:FiniteDimensional [nested category class]; vector_spaces.VectorSpaces:WithBasis.FiniteDimensional [nested category class]` |
| method expansions | `category_with_axiom.Blahs:FiniteDimensional -> _with_axiom(FiniteDimensional); cw_complexes.CWComplexes:FiniteDimensional -> _with_axiom(FiniteDimensional); manifolds.Manifolds:FiniteDimensional -> _with_axiom(FiniteDimensional); modules.Modules:FiniteDimensional -> _with_axiom(FiniteDimensional)` |

## Declared in (25)

| category | declaration | source |
| --- | --- | --- |
| [`AlgebrasWithBasis`](../../categories/AlgebrasWithBasis.md) | lazy-import binding | [`src/sage/categories/algebras_with_basis.py:125`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/algebras_with_basis.py#L125) |
| [`Blahs`](../../categories/Blahs.md) | nested category class | [`src/sage/categories/category_with_axiom.py:2632`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2632) |
| [`Blahs`](../../categories/Blahs.md) | subcategory interface method | [`src/sage/categories/category_with_axiom.py:2625`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2625) |
| [`DummyObjectsOverBaseRing`](../../categories/DummyObjectsOverBaseRing.md) | nested category class | [`src/sage/categories/category_with_axiom.py:2828`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2828) |
| [`DummyObjectsOverBaseRing`](../../categories/DummyObjectsOverBaseRing.md) | nested category class | [`src/sage/categories/category_with_axiom.py:2816`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2816) |
| [`TestObjects`](../../categories/TestObjects.md) | nested category class | [`src/sage/categories/category_with_axiom.py:2783`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2783) |
| [`TestObjects`](../../categories/TestObjects.md) | nested category class | [`src/sage/categories/category_with_axiom.py:2771`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/category_with_axiom.py#L2771) |
| [`CWComplexes`](../../categories/CWComplexes.md) | nested category class | [`src/sage/categories/cw_complexes.py:110`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cw_complexes.py#L110) |
| [`CWComplexes`](../../categories/CWComplexes.md) | subcategory interface method | [`src/sage/categories/cw_complexes.py:84`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/cw_complexes.py#L84) |
| [`FilteredModulesWithBasis`](../../categories/FilteredModulesWithBasis.md) | nested category class | [`src/sage/categories/filtered_modules_with_basis.py:1161`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/filtered_modules_with_basis.py#L1161) |
| [`GradedAlgebrasWithBasis`](../../categories/GradedAlgebrasWithBasis.md) | nested category class | [`src/sage/categories/graded_algebras_with_basis.py:157`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_algebras_with_basis.py#L157) |
| [`GradedLieAlgebras`](../../categories/GradedLieAlgebras.md) | nested category class | [`src/sage/categories/graded_lie_algebras.py:60`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_algebras.py#L60) |
| [`GradedLieAlgebrasWithBasis`](../../categories/GradedLieAlgebrasWithBasis.md) | lazy-import binding | [`src/sage/categories/graded_lie_algebras_with_basis.py:41`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/graded_lie_algebras_with_basis.py#L41) |
| [`HopfAlgebrasWithBasis`](../../categories/HopfAlgebrasWithBasis.md) | lazy-import binding | [`src/sage/categories/hopf_algebras_with_basis.py:157`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/hopf_algebras_with_basis.py#L157) |
| [`LieAlgebras`](../../categories/LieAlgebras.md) | nested category class | [`src/sage/categories/lie_algebras.py:174`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lie_algebras.py#L174) |
| [`MagmaticAlgebras`](../../categories/MagmaticAlgebras.md) | nested category class | [`src/sage/categories/magmatic_algebras.py:224`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/magmatic_algebras.py#L224) |
| [`Manifolds`](../../categories/Manifolds.md) | nested category class | [`src/sage/categories/manifolds.py:312`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L312) |
| [`Manifolds`](../../categories/Manifolds.md) | subcategory interface method | [`src/sage/categories/manifolds.py:117`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/manifolds.py#L117) |
| [`Modules`](../../categories/Modules.md) | nested category class | [`src/sage/categories/modules.py:514`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L514) |
| [`Modules`](../../categories/Modules.md) | subcategory interface method | [`src/sage/categories/modules.py:341`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules.py#L341) |
| [`ModulesWithBasis`](../../categories/ModulesWithBasis.md) | lazy-import binding | [`src/sage/categories/modules_with_basis.py:195`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/modules_with_basis.py#L195) |
| [`SemisimpleAlgebras`](../../categories/SemisimpleAlgebras.md) | nested category class | [`src/sage/categories/semisimple_algebras.py:111`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/semisimple_algebras.py#L111) |
| [`TriangularKacMoodyAlgebras`](../../categories/TriangularKacMoodyAlgebras.md) | nested category class | [`src/sage/categories/triangular_kac_moody_algebras.py:341`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/triangular_kac_moody_algebras.py#L341) |
| [`VectorSpaces`](../../categories/VectorSpaces.md) | nested category class | [`src/sage/categories/vector_spaces.py:285`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L285) |
| [`VectorSpaces`](../../categories/VectorSpaces.md) | nested category class | [`src/sage/categories/vector_spaces.py:225`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/vector_spaces.py#L225) |

## Classes the framework generates at 10.10 (17)

| class | module |
| --- | --- |
| `Blahs.FiniteDimensional` | `category_with_axiom` |
| `DummyObjectsOverBaseRing.Commutative.FiniteDimensional` | `category_with_axiom` |
| `DummyObjectsOverBaseRing.FiniteDimensional` | `category_with_axiom` |
| `TestObjects.Commutative.FiniteDimensional` | `category_with_axiom` |
| `TestObjects.FiniteDimensional` | `category_with_axiom` |
| `CWComplexes.FiniteDimensional` | `cw_complexes` |
| `FilteredModulesWithBasis.FiniteDimensional` | `filtered_modules_with_basis` |
| `GradedAlgebrasWithBasis.FiniteDimensional` | `graded_algebras_with_basis` |
| `GradedLieAlgebras.Stratified.FiniteDimensional` | `graded_lie_algebras` |
| `LieAlgebras.FiniteDimensional` | `lie_algebras` |
| `MagmaticAlgebras.WithBasis.FiniteDimensional` | `magmatic_algebras` |
| `Manifolds.FiniteDimensional` | `manifolds` |
| `Modules.FiniteDimensional` | `modules` |
| `SemisimpleAlgebras.FiniteDimensional` | `semisimple_algebras` |
| `TriangularKacMoodyAlgebras.FiniteDimensional` | `triangular_kac_moody_algebras` |
| `VectorSpaces.FiniteDimensional` | `vector_spaces` |
| `VectorSpaces.WithBasis.FiniteDimensional` | `vector_spaces` |
