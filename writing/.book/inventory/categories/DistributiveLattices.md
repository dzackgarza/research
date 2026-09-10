# DistributiveLattices

| field | value |
| --- | --- |
| module | `lattice_posets` |
| role | public named category class |
| implementation | Python class |
| defined by | LatticePosets.Trim + axiom ChainGraded |
| direct defining axiom | [`ChainGraded`](../../axioms/ChainGraded.md) |
| syntactic axiom chain | [`Trim`](../../axioms/Trim.md), [`ChainGraded`](../../axioms/ChainGraded.md) |
| bases | [`CategoryWithAxiom`](../../categories/CategoryWithAxiom.md) |
| source | [`src/sage/categories/lattice_posets.py:564`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L564) |
| loads at 10.10 | yes |
| notes | The public shorthand LatticePosets().Distributive() expands to Trim then ChainGraded; the implementation class is bound at LatticePosets.Trim.ChainGraded. |

## Local axiom paths

- `Finite`

## Declared features (1)

| feature | type | declaration | target or expansion | source |
| --- | --- | --- | --- | --- |
| [`Finite`](../../axioms/Finite.md) | axiom | nested category class | `CategoryWithAxiom` | [`src/sage/categories/lattice_posets.py:602`](https://github.com/sagemath/sage/blob/686dc1a8d420c2e0aabadd4f602d9a0aa4690c50/src/sage/categories/lattice_posets.py#L602) |

## Axiom-generated classes at 10.10 (2)

| class | module | axiom |
| --- | --- | --- |
| `DistributiveLattices` | `lattice_posets` | `(framework base)` |
| `DistributiveLattices.Finite` | `lattice_posets` | `Finite` |
