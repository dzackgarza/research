# Lattice engines — method inventories and system references

External-input corpus for the computer-algebra systems this repository can compute
lattice mathematics with. It answers one question, per operation: *which engine
provides an algorithm for this, under which hypotheses, and over which base ring?*

Provenance: migrated 2026-08-20 from two locally-authored clones,
`~/gitclones/lattice_interface` (`docs/`, authored 2026-02) and
`~/gitclones/lattice_extension` (`docs/`). The clones are read-only sources; this
tree is the durable home.

## Layout

| Path | What it holds |
| --- | --- |
| `method-inventories/` | The `lattice_interface` documentation tree, verbatim: per-system research readmes, per-system coverage checklists, and the upstream documentation snapshots the readmes cite. |
| `system-references/` | The `lattice_extension` documentation tree, verbatim: one short method-level reference per system, indexed by its own `INDEX.md`, plus `DEFINITENESS_NOTES.md`. |
| `design/` | The locally-authored doctrine and procedure behind the corpus: its scope statement, the three agent playbooks, the plan that produced the typed contract, the coverage-audit changelog, and the extension clone's code-style ruling. |
| `polyhedral-common/` | Provisioning material for the indefinite-forms engine the preamble's `engines.sage` seam calls (migrated 2026-08-20 from `~/gitclones/lattice-research`): the capability table and exact build recipe for the `INDEF_FORM_*` binaries, including which binaries did not build on this machine and why, plus the locally-authored C++ adapter exposing polyhedral_common's isotropic k-plane/k-flag equivalence, which upstream ships only as a library API. |
| `integral-lattice-refactor/` | The `integral_lattice` clone's parity ledgers (migrated 2026-08-20, PLAN-corpora-audit-registry R3): `checklist.md` and `checklist_1.md` map Hecke's `ZZLat` and `ZZLatWithIsom` surfaces row by row, each row citing the Oscar signature and its definiteness hypothesis (`checklist_1.md` adds the clone's architectural ruling: nothing outside the module may be referenced except by extending existing Sage classes); `checklist2.md` covers Sage's `free_module_integer` reduction/CVP surface; `free_quadratic_module_integer_symmetric_refactor_checklist.md` is the 113-item plan mapping every function of Sage's integral-lattice module to a destination. |

The two trees are kept apart rather than merged because they are different
artifacts at different granularity, and both cite `sage/`, `gap/` and `julia/`
subdirectories of their own.

## The load-bearing documents

- `method-inventories/lattice_wrapper_capability_checklist.md` (1074 lines) —
  backend-agnostic capability specification. Each capability is stated as
  mathematics in LaTeX with its sources, and equivalent methods from different
  backends are deliberately merged into one bucket, so the checklist is indexed
  by *operation*, never by engine spelling.

- `method-inventories/method_ground_truth_tracker.csv` (623 rows, twelve
  mathematical sections) — one row per capability with method, status, test
  citations, review date and a verification note. Sections: lattices over
  $\mathbb{Z}$; matrix algorithms; number fields; quadratic forms over
  $\mathbb{Z}$; definite lattices; indefinite lattices and genera; hyperbolic
  lattices and root data; finite quadratic modules; rings of integers and
  ideals; space-with-isometry; lattice-with-isometry; equivariant primitive
  extensions.

- `method-inventories/julia/oscar_jl/lattice/research_readme.md` (857 lines) —
  typed inventory of the whole Julia lattice stack with definiteness tags,
  hypotheses and return types per method. The flagship document of the corpus.

- `method-inventories/julia/hecke_jl/lattice/research_readme.md` (286 lines) —
  the Hecke/Nemo inventory with an indefinite-first workflow ordering. Its own
  `GAPS.md` records that this directory holds **zero** upstream snapshots, so
  every contract stated here is locally unbacked.

- `system-references/DEFINITENESS_NOTES.md` — the cross-system table: for
  fourteen backends, whether a Gram matrix is accepted, whether indefinite forms
  are supported, whether a bilinear form independent of the standard Euclidean
  product is supported, and the base ring. This is the fibre question the repo
  asks of the issue-#24 engines, and the reason the corpus is indefinite-first:
  most reduction and enumeration software assumes the form is positive definite,
  because for an indefinite form there is no shortest-vector problem — null
  directions make $\{v : |q(v)| \le B\}$ infinite for every bound $B$. What
  replaces it for indefinite lattices is genus symbols, discriminant forms,
  orbits of isotropic vectors, and Vinberg's algorithm.

- `method-inventories/GAPS.md`, `method-inventories/TODO.md` — the corpus's own
  honest account of what is unverified: which upstream snapshots are cited but
  missing, and which packages never received the method-by-method
  upstream-versus-checklist comparison at all.

## The archived material

`method-inventories/archive/` holds what the corpus's own scope policy set aside:
the polyhedral and toric stacks (4ti2, cddlib and its two Python bindings, lrslib,
LattE integrale, Normaliz, PALP, polymake, TOPCOM, NConvex, the GAP toric and
polyhedral sections, the Sage toric sections), plus fplll. Each has a reference,
a checklist and, for most, an upstream provenance note. It is set aside rather
than deleted because a lattice reference that answers only "we do not document
that" is not traceable; the sections are also the natural entry point should
polytope work (Vinberg chambers, Delaunay and perfect-form machinery) need them.

Note the scope statement in `method-inventories/archive/README.md` defines a
lattice as a *free* $R$-module of finite rank with a symmetric nondegenerate
bilinear form. This repository defines it on a *projective* module; over
$\mathbb{Z}$ the two agree, and the divergence matters only when the base ring is
generalised.

## Errata recorded at migration

`system-references/DEFINITENESS_NOTES.md` is a survey written before the
method-level references it summarises. Three of its claims are contradicted by
other documents in this same tree; the file is landed verbatim, and the
divergences are recorded here rather than edited into it.

1. **Indefinite.jl entry-point names.** The notes and
   `system-references/julia/Indefinite.jl.md` name the entry points
   `IsometricEquivalent`, `FindAutomorphisms` and `IsotropicVectors`. The
   mechanical symbol inventory extracted from the package's own sources
   (`method-inventories/julia/indefinite_jl/inventory/indefinite_julia_gap_method_inventory.md`,
   generated 2026-02-16) lists no such symbols. The actual Julia-level entry
   points are `INDEF_FORM_TestEquivalence`, `INDEF_FORM_AutomorphismGroup`,
   `INDEF_FORM_GetOrbitRepresentative`, `INDEF_FORM_GetOrbit_IsotropicKplane`
   and `INDEF_FORM_GetOrbit_IsotropicKflag`. Prefer the inventory: it was
   extracted from source, the reference pages were not.

2. **"ZZLat.jl" is not a package.** The notes list `Julia ZZLat.jl` as a system
   of its own and open its example with `using ZZLat`. `ZZLat` is the integer
   lattice *type* in Hecke.jl, as `system-references/julia/ZZLat.md` states in
   its own first line. Its `Genus(signature=(1,1), level=2)` and
   `lattice(:hyperbolic, 2, 0)` constructor calls appear in no reference in this
   tree and should not be relied on.

3. **The GAP row.** The notes' GAP example calls `Lattice([[1,0],[1,1]])`. The
   GAP material in this tree (`method-inventories/gap/`, and the conformance
   suite migrated to `computations/scripts/conformance_lattice_engines/gap/`)
   documents the integer-matrix core — `HermiteNormalFormIntegerMat`,
   `SmithNormalFormIntegerMat`, `NullspaceIntMat`, `LLLReducedBasis`,
   `ShortestVectors` — and no `Lattice` constructor.

The tables' broad claim survives all three corrections: it is a claim about
which systems accept an arbitrary symmetric Gram matrix rather than the standard
Euclidean product, and it is the reason the repository's own work is sited on
`IntegralLattices`.

## Relation to the owned mathematics

This tree is a survey of *other people's* software. The repository's own lattice
mathematics lives in the preamble
(`src/dzack_research/preamble/categories/modules/framed/formed/integrallattice/`),
which owns the basic invariants, the dual lattice and correlation morphism, the
discriminant form, gluing and overlattices, $O(L)$ and the discriminant
representation, the definite-lattice metric algorithms, and Vinberg's algorithm
with Coxeter diagrams — the last strictly more richly than any source catalogued
here.

The capabilities this corpus catalogues that the preamble does **not** own, as
read at migration: the Minkowski–Siegel mass of a genus; Hasse and Witt
invariants at a place; a form module over a field (quadratic spaces) and hence
local isotropy and representation predicates; the lattice-with-isometry pair as a
first-class object with its type classification and equivariant primitive
extensions; quadratic and hermitian lattices over number fields with pseudo-bases
and coefficient ideals; the trace-form functor $G_{ij} = \operatorname{Tr}_{K/\mathbb{Q}}(b_i b_j)$
from orders and fractional ideals to integral lattices; kissing number and theta
series; Nikulin-style enumeration of primitive embeddings; orbits of totally
isotropic $k$-planes and flags under $O(L)$; and $p$-neighbours.

Conformance suites that run these engines and record what they actually provide:
`computations/scripts/conformance_lattice_engines/`.
The typed interface specification designed against this corpus:
`notes/lattice-interface-contract/`.
