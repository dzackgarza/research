<!--
Origin: gitclones/integral_lattice/{constructors.py, lattice_utils.py,
indefinite_jl_interface.py}. Landed 2026-08-20 by the integral_lattice
enrichment migration (PLAN-corpora-audit-registry, section R3), as the two
notions of that corpus whose durable home is a record rather than preamble
code. Every other R3 notion landed as owned code, a reference ledger, or a
script; the "Where the rest went" table below names each destination.
-->

# The integral-lattice bridge: the notions that stay records

Two notions of the `integral_lattice` bridge corpus are recorded here
instead of landing as preamble code. In both cases the corpus file states a
specification whose executable part is either wrong or already owned by a
dependency, so relocating the *statement* is what preserves the content.

## 1. The lattice expression grammar

`constructors.py` accepts a whole direct sum as one string —
`IntegralLattice("U^2 + A_1")` — parsed by splitting on `+`, expanding
powers, dispatching a Gram builder on the type letter, and applying a
twist. The productions, and what the preamble owns for each:

| Production | Example | Owned spelling |
|---|---|---|
| sum | `U + A_1` | `Lattices.U + Lattices.A1` (`+` is the monoidal operation on lattices) |
| power | `U^2`, `U^{2}` | `Lattices.U ** 2` |
| twist | `A_1(3)` | `Lattices.A1.twist(3)` |
| rank one | `<7>` | `Lattices.rank_one_negative(7)` |
| root type | `A_5`, `E_8` | `IntegralLattice("A5")` through `_gram_from_name`, which also records the Cartan type on the lattice |
| hyperbolic plane | `U`, `H` | `Lattices.U` |
| unimodular families | `I_{p,q}`, `II_{2,10}` | `Lattices.IPQ(p, q)`, `Lattices.IIPQ(p, q)` |
| twisted family | `II_{2,10}(3)` | `Lattices.IIPQ(2, 10).twist(3)` |
| affine root type | `~A_3` | **not owned by name** — see below |

The grammar is a specification in the corpus, not a working parser: the
regular expressions in `_latex_normalize` and `_parse_normalized` are
written with `\\s`, `\\{` and `\\(` inside raw strings, so they match a
literal backslash followed by `s`, `{` or `(` and never fire on the
documented inputs.

**The affine types are the one genuinely unnamed family.** A hyperbolic or
euclidean Coxeter diagram is owned (`coxeter_diagrams.sage`, whose
`is_parabolic` asks Sage whether every component is affine), and a
degenerate lattice is an ordinary object here — `integral_lattices.sage`
routes a lattice whose correlation has nonzero kernel into
`Lattices(ℤ).FinitelyGenerated().Integral()` rather than into
`IntegralLattices`, deliberately. So an affine root lattice is
constructible today from its Gram matrix; what is missing is only the
`~A_n` name and a construction of that matrix.

That construction is where the corpus's affine branch must not be ported as
written. `_gram_from_simple_roots` builds `G = L^T L` from
`RootSystem(ct).ambient_space().simple_roots()`, each root taken through
`to_vector()`. In the finite case those coordinates are orthonormal, so
`L^T L` is the root-system Gram matrix. The invariant form of an affine
root system is positive semidefinite of corank 1, its radical spanned by
the imaginary root $\delta$; any construction returning a nonsingular Gram
matrix for `~A_n` has computed something else. Whether Sage's affine
ambient coordinates reproduce the invariant form under the Euclidean dot
product is the question to settle first, against a rank-2 specimen where
the answer is checkable by hand ($\tilde A_1$: Gram $\begin{pmatrix}-2 &
2\\ 2 & -2\end{pmatrix}$ in this repo's negative-definite convention,
determinant $0$).

The corpus's own docstring for `_gram_from_simple_roots` shows `A_2` as
$\begin{pmatrix}2 & -1\\ -1 & 2\end{pmatrix}$ while its body returns the
negation; the body is the one that matches this repo's convention.

## 2. Random lattices and random unimodular matrices

`lattice_utils.random_lattice(n)` samples a random unimodular integer
matrix $M$ and returns the lattice with Gram matrix $M + M^{\mathsf T}$,
resampling until that is nonsingular.
`indefinite_jl_interface.random_lattice_indefinite_jl(n)` supplies the
sampler through GAP instead, as (upper triangular, unit diagonal) $\times$
(permutation) $\times$ (lower triangular, unit diagonal).

Two facts about this, both of which is why it is a record:

- **The sampler is already a dependency.** Sage's
  `random_matrix(ZZ, n, n, algorithm="unimodular")` is what the corpus's
  own `random_lattice` calls; the GAP routine is a second implementation of
  the same object.
- **$M + M^{\mathsf T}$ is not even.** The diagonal of $M + M^{\mathsf T}$
  is $2M_{ii}$, so the form is even exactly when the sampler is
  unconstrained on the diagonal — the construction produces a symmetric
  integral form of arbitrary parity, not an even one, and the corpus does
  not say so.

The preamble has no `random_element` on `IntegralLattices`, by policy: test
specimens in this repo are small and named, and a claim about a random
lattice is a claim about a distribution nobody has specified. A random
specimen belongs in a script when a search wants one, constructed from
Sage's sampler in two lines, not on the category.

## Where the rest went

Every other notion the R3 audit named landed as code or as a maintained
document:

| Notion | Destination |
|---|---|
| Primitive embedding into a genus / into an even unimodular lattice; the glue map of a primitive extension | `integrallattice/lattice_homomorphisms.sage` (`EmbeddingHomset`), `integral_lattices.sage` (`embed_in_even_unimodular`, `glue_map`) |
| Indefinite $O(L)$, isometry and vector equivalence, orbits, stabilizers, Allcock's edgewalk, Vinberg over a number field, the rational spinor norm, the polyhedral_common wire format | `integrallattice/engines.sage` (the engine seams), consumed by `lattice_isometries.sage`, `isotropic_orbits.sage`, `hyperbolic_lattices.sage` |
| Cocompactness of the reflection group's fundamental domain | `hyperbolic_lattices.sage` `is_cocompact` |
| Mass of a genus, the representative set | `integral_lattices.sage` `class Genus` |
| Leech, Mukai, Beauville–Bogomolov–Fujiki, $I_{p,q}$, $II_{p,q}$ | `categories/modules/framed/formed/lattices.sage`, `catalogue.sage` |
| ADE recognition, Coxeter number, highest root, the root sublattice | `root_lattices.sage`, `definite_lattices.sage` |
| Kissing number, vectors of prescribed square and divisibility, quadratic triples | `definite_lattices.sage` |
| Coimage, section, retraction of a module morphism | `modules/module_morphisms/module_morphisms.sage` |
| The Eichler transvection | `integral_lattices.sage` |
| The Gram matrix as a weighted graph | `categories/forms/gram_matrices.sage` (`gram_matrix_graph`, `gram_matrix_from_graph`) |
| $\operatorname{Sym}(X)$ and the torsor of orderings | `categories/sets/owned_sets.py` `symmetric_group` |
| The finitely-presented-modules axiom scheme | `notes/category-design/fp-modules-axiom-scheme/` |
| The Hecke/`ZZLat` parity ledgers and the Sage refactor plan | `references/lattice-engines/integral-lattice-refactor/` |
| The automorphism-group coverage checklist over ~90 Sage group constructors | `computations/scripts/conformance_sage_group_constructors/` |
| The 2-polygraph / Knuth–Bendix encoding | `computations/scripts/kbmag-two-polygraph/` |
| The $(\infty,n)$-category tower and `newcat2.md` | `notes/category-design/n-category-tower/` |
| The lattice-category roster | `notes/category-design/lattice-categories-roster.md` |
