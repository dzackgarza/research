# Engine conformance corpus

What the computer-algebra engines of issue #24 actually provide for lattice
mathematics, asserted rather than surveyed. Each test names one method in its
docstring (`method: <name>`) and asserts a mathematical fact about that method's
output; the shared `conftest.covered_methods_from_module` collects those tokens,
so each module can also assert its own coverage of a named surface.

Migrated 2026-08-20 from `~/gitclones/lattice_interface/tests/` and
`~/gitclones/lattice_extension/tests/`. This directory lives under
`computations/scripts/`, which is exempt from the repository QC gates: these
suites run third-party engines (Sage, GAP, Julia via `juliacall`) and record
their behaviour, so they are neither the repository's own mathematics nor a gate
on it.

## Contents

| Path | Engine surface | tests |
| --- | --- | --- |
| `sage/` | Sage: `IntegralLattice`, `IntegerLattice`, `FreeQuadraticModule`, genus, `TorsionQuadraticModule`, `GroupOfIsometries`, quadratic/binary/ternary forms, root systems, toric lattices, the number-field bridge, matrix methods | 604 |
| `sage-extension-clone/` | Sage, second independent pass: `IntegerLattice`, `IntegralLattice`, genus, quadratic/binary/ternary forms | 552 |
| `gap/` | GAP integer-matrix core: Hermite and Smith normal form with transforms, integer nullspace and solution, base, intersection and complement of integer row lattices, determinant, LLL on a basis and on a Gram matrix, shortest vectors, orthogonal embeddings | 16 |
| `julia/` | Hecke/Oscar through `juliacall`: `ZZLat` construction, attributes, reduction, enumeration, automorphisms, module operations, genus, torsion quadratic modules, hermitian lattices and genera, overlattices, primitive embeddings, equivariant primitive extensions, Vinberg, and both with-isometry families; plus `Indefinite.jl` | 432 |
| `julia-native-archived/` | The Julia-native (`Test.jl`) originals of the `julia/` suite, before migration to pytest, with their `Project.toml`/`Manifest.toml` pins | — |
| `surface-discovery/` | The two scripts that enumerate Sage's own method surface for `IntegerLattice`, `IntegralLattice`, `BinaryQF`, `QuadraticForm` and `TernaryQF` and subtract what is documented — the hidden-surface pass that keeps a coverage claim from being measured against a set the suite chose for itself. Scripts, not tests; `discover_all_methods.py` was renamed from `test_all_methods.py` at migration so pytest does not collect it. | — |

## The two Sage suites

The two clones each wrote a Sage conformance suite. Neither contains the other.

`sage/` covers seven modules `sage-extension-clone/` never touches — the free
quadratic module, `GroupOfIsometries`, `TorsionQuadraticModule`, root systems,
toric lattices, matrix methods (132 tests) and the number-field bridge (136
tests). On the four modules both cover, the extension clone is denser:

| module | `sage/` | `sage-extension-clone/` |
| --- | --- | --- |
| IntegerLattice | 15 | 142 |
| IntegralLattice | 30 | 153 |
| QuadraticForm | 155 | 157 |
| genus | 22 | 24 |
| BinaryQF | 31 | 36 |
| TernaryQF | 35 | 40 |

Both are therefore kept. `sage/` is the wider one and is the corpus's Sage entry
point; `sage-extension-clone/` is the deeper one on the four lattice and form
types the repository's own work uses most.

## Two suites that assert absence

`julia/test_quadform_and_isom_static.py` records twenty `QuadFormAndIsom`
operations as *not reachable* through the bridge — primitive embeddings and
extensions, the special and stable orthogonal groups, the whole stabilizer
family, the isometry predicates. `julia/test_oscar_bridge_static.py` records the
methods that *are* reachable, across construction, invariants, genus, mass,
local symbols, Hasse and Witt invariants, and automorphism generators. Read them as a pair: an absence assertion
alone is satisfied by a bridge that does nothing, so the reachable count is what
makes the unreachable list mean anything.

## Running

Nothing here runs under the repository gates. Each suite needs its own engine
present: Sage for `sage/` and `sage-extension-clone/`, a GAP the Sage interface
can reach for `gap/`, and a Julia with Hecke/Oscar plus `juliacall` for `julia/`.
Run a suite from this directory, e.g. `pytest sage/`, so the shared `conftest.py`
here is importable as `conftest`.

## Related

- The survey these suites were written against: `references/lattice-engines/`.
- The typed interface specification, which is the *unmet* obligations rather than
  the engines' behaviour: `notes/lattice-interface-contract/`.
