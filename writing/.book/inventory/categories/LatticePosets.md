# LatticePosets

| field | value |
| --- | --- |
| module | `lattice_posets` |
| role | public named category class |
| implementation | Python class |
| bases | [`Category`](../../categories/Category.md) |
| source | [`src/sage/categories/lattice_posets.py:19`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L19) |
| loads at 10.10 | yes |

## Local axiom paths

- `ChainGraded`
- `CongruenceUniform`
- `Distributive`
- `Extremal`
- `Finite`
- `Semidistributive`
- `Stone`
- `Trim`
- `Trim.ChainGraded`

## Declared features (15)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`ChainGraded`](../../axioms/ChainGraded.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/lattice_posets.py:536`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L536) |
| [`ChainGraded`](../../axioms/ChainGraded.md) | axiom | subcategory interface method | `_with_axiom(ChainGraded)` | [`src/sage/categories/lattice_posets.py:93`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L93) |
| [`CongruenceUniform`](../../axioms/CongruenceUniform.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/lattice_posets.py:457`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L457) |
| [`CongruenceUniform`](../../axioms/CongruenceUniform.md) | axiom | subcategory interface method | `_with_axiom(CongruenceUniform)` | [`src/sage/categories/lattice_posets.py:144`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L144) |
| [`Distributive`](../../axioms/Distributive.md) | axiom | subcategory interface method | `_with_axiom(ChainGraded) then _with_axiom(Trim)` | [`src/sage/categories/lattice_posets.py:123`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L123) |
| [`Extremal`](../../axioms/Extremal.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/lattice_posets.py:214`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L214) |
| [`Extremal`](../../axioms/Extremal.md) | axiom | subcategory interface method | `_with_axiom(Extremal)` | [`src/sage/categories/lattice_posets.py:195`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L195) |
| [`Finite`](../../axioms/Finite.md) | axiom | lazy-import binding | `sage.categories.finite_lattice_posets.FiniteLatticePosets` | [`src/sage/categories/lattice_posets.py:211`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L211) |
| [`Semidistributive`](../../axioms/Semidistributive.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/lattice_posets.py:278`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L278) |
| [`Semidistributive`](../../axioms/Semidistributive.md) | axiom | subcategory interface method | `_with_axiom(Semidistributive)` | [`src/sage/categories/lattice_posets.py:158`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L158) |
| [`Stone`](../../axioms/Stone.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/lattice_posets.py:496`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L496) |
| [`Stone`](../../axioms/Stone.md) | axiom | subcategory interface method | `_with_axiom(Stone)` | [`src/sage/categories/lattice_posets.py:108`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L108) |
| [`Trim`](../../axioms/Trim.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/lattice_posets.py:239`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L239) |
| [`Trim`](../../axioms/Trim.md) | axiom | subcategory interface method | `_with_axiom(Trim)` | [`src/sage/categories/lattice_posets.py:180`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L180) |
| [`ChainGraded`](../../axioms/ChainGraded.md) | axiom | module-level binding | `DistributiveLattices` | [`src/sage/categories/lattice_posets.py:619`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L619) |

## Axiom-generated classes at 10.10 (6)

| class | module | axiom |
| --- | --- | --- |
| `LatticePosets.ChainGraded` | `lattice_posets` | `ChainGraded` |
| `LatticePosets.CongruenceUniform` | `lattice_posets` | `CongruenceUniform` |
| `LatticePosets.Extremal` | `lattice_posets` | `Extremal` |
| `LatticePosets.Semidistributive` | `lattice_posets` | `Semidistributive` |
| `LatticePosets.Stone` | `lattice_posets` | `Stone` |
| `LatticePosets.Trim` | `lattice_posets` | `Trim` |
