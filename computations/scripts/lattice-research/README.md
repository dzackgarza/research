# The lattice-research code corpus

Migrated 2026-08-20 from `~/gitclones/lattice-research`, the first-attempt
lattice DSL repository, under the corpora-audit registry sections
R1-lattice-research-backends and R2-lattice-research-prose. The prose of the
same tree is at `archives/provenance/lattice-research/`, its theory at
`notes/topics/coble-enriques-lattice-theory/`, its literature extractions at
`references/literature/lattice-research/`.

This tree is **source material, not a maintained surface**. It lives under
`computations/scripts/`, so the quality-control gates do not run on it, and
nothing here is imported by the preamble or by any test. Read a claim in these
files as a claim about the source corpus at the time it was written.

Four kinds of content, one per subdirectory.

## `backends/` — the algorithms, as they were implemented

Reference implementations for lattice computations whose notions the preamble
now owns. The preamble's own methods were written against these, so they are
the citable reference for the hand-rolled parts.

| File | What it computes | Where the mathematics lives now |
|---|---|---|
| `isometry_backend.py` | The isometry obstruction ladder: rank, signature, determinant, discriminant-group isomorphism, discriminant-form isometry, rational isometry, local isometry at $p = 2, 3, 5$, genus; then a full decision. | `IsometryHomset.is_empty` (`lattice_homomorphisms.sage`), including the Nikulin $(r, a, \delta)$ branch for even indefinite 2-elementary lattices. |
| `dawes_orbit_backend.py` | Dawes Algorithms 2.1 / 2.2 / 2.3: orbits of a non-isotropic vector under a subgroup, by the definite-complement route and by the gluing route; the real spinor norm; the induced action on the discriminant group. | `vector_orbits.sage`; the spinor-norm character and $O^{+}$, $SO$ on `lattice_isometries.sage`. |
| `isotropic_gamma_orbit_backend.py` | Orbits of primitive isotropic lines, planes and flags under $O(L)$, and their splitting under a subgroup by double cosets in a finite quotient of $O(L)$. | `isotropic_orbits.sage`. |
| `orthogonal.py` | Predicate-cut subgroups of $O(L)$: $SO$, $O^{+}$, the preimage of a subgroup of $O(A_L)$, the kernel of the discriminant action, and stabilizers of a vector, an isotropic line, an isotropic plane and an isotropic flag. | `lattice_isometries.sage` (`special_orthogonal_subgroup`, `discriminant_preimage`) and `predicate_subgroups.sage`. |
| `oscar_centralizer/` | Invariant and coinvariant sublattices of an isometry; generators and order of the image of $Z_{O(L)}(f)$ in $O(A_L, D_f)$, by hermitian Miranda–Morrison theory. | The OSCAR seam in `engines.sage`. |
| `foliation_backend.py` | Milnor number, Picard–Fuchs operator, indicial polynomial, and the multiplicative Jordan decomposition of the local monodromy of a one-parameter hypersurface family. | **No owner.** The pipeline is written out in `notes/computations/hypersurface-family-monodromy.md`, which also states why: the preamble has no variation-of-Hodge-structure surface for it to be a method of. |

`backends/external/` holds two files about `polyhedral_common`
(Mathieu Dutour Sikirić): the capability table and build recipe for its
binaries, and `INDEF_FORM_TestEquivalenceIsotropicKplane.cpp`, a locally
authored adapter exposing the isotropic $k$-plane and $k$-flag equivalence
that upstream ships only as a library API. The vendored wrapper, the binaries
themselves, and the CARAT submodule are third-party and were not migrated.

## `specs/` — executable specifications

Assertion corpora written against an intended interface rather than an
existing one. They run only where that interface exists, so they are read as
requirements.

- `variety_spec/` (16 files, ~3600 lines) — standard surface theory stated as
  assertions: Enriques with $2K \sim 0$, $p_g = q = 0$, $\chi_{\mathrm{top}} = 12$
  and plurigenera $[1,0,1,0,1]$; the Coble surface and its K3 double cover;
  del Pezzo and Fano; blowup Picard lattices; adjunction for plane curves and
  for surfaces in $\mathbb P^3$; Riemann–Hurwitz for branched covers; toric
  fans; linear systems; ampleness, nefness, bigness; symplectic versus
  non-symplectic automorphisms; Deligne–Mumford stability; log-canonical pairs.
  **The gap:** the preamble's `categories/schemes/` and `categories/divisors/`
  nodes are thin, so none of this is executable here yet. Re-expressing it
  against the owned surface is the work these files specify.
- `sage_spec/` — the Sage category atlas (`category_construction_spec.sage`,
  `category_construction_structure_spec.sage`, `category_examples_spec.sage`):
  which named Sage categories equal which chained subcategories, and where
  `ZZ`, `QQ`, `AA`, `QQbar`, `RR`, `CC`, $\mathbb Z_p$, $\mathbb F_p$ and
  localizations sit in that graph. This is the fiber/capability data the Sage
  bridge wants. Also the module DSL spec (`module_methods.sage`, `misc.sage`),
  the root-lattice and Coxeter-diagram spec (`coxeter.sage`), and
  `research_workflows.sage`, the end-to-end Coble/Enriques script.
- `lattice_spec/` — the lattice interface specs, including
  `todo_general_indefinite_isometry_spec.py`: an odd indefinite basis change
  ($U$ twisted by 3) that must be detected as an isometry once every screen
  passes. `lattice_methods.sage` is the user specification's own copy, and
  `lattice_methods_sage_spec_variant.sage` the runnable variant of it that the
  corpus kept under `tests.bak/sage_spec/`, carrying its own header telling a
  reader not to delete it as a stale API.
- `tests/` — the corpus's own test drivers for the backends above, carrying
  the worked literature examples: Dawes Examples 2.2 and 2.6 against
  $U \oplus A_3$; Sterk's five 0-cusps and nine 1-cusps for the degree-two
  Enriques group; the two 0-cusps and two 1-cusps of $O(T_{\mathrm{En}})$;
  the stabilizer of $h = e' + f'$ with $h^2 = 4$; the Legendre family's Milnor
  number 2 and unipotent monodromy; and $\operatorname{diag}(1,2) \cong
  \operatorname{diag}(3,6)$ over $\mathbb Z_2$ with the explicit witness
  $M = \begin{pmatrix} 1 & -2 \\ 1 & 1\end{pmatrix}$.
- `LATTICE_TEST_STYLE.md` — what a weak lattice test looks like against a
  strong one, plus two API rulings: `scale()` is the ideal
  $\langle \beta(L, L)\rangle$, and rescaling belongs to `twist()`.
- `theory_spec/monodromy_foliation_backend.md` — why the Legendre-family
  Picard–Fuchs and monodromy assertions are basis-dependent, and which sources
  are needed before they can be asserted.
- `conftest.py` — the collection glue that ran the `.sage` spec files.

## `written-spec/` — the design of the first attempt

The prior design, kept because the preamble diverges from it deliberately.
`notes/category-design/lattice-dsl-prior-attempt.md` is the reading of these
files; the files themselves are here.

- `lattice_methods_recovered_from_codex_transcript_2026_04_13.sage` — the
  user-authored DSL specification, 161 lines, the closest thing the corpus has
  to a statement of intent.
- `lattices_written_spec_backup.py` — the 2112-line written specification of
  the whole class hierarchy, named constructors, genus and Nikulin invariants,
  orthogonal groups, and the orbit/stabilizer surface.
- `varieties.py` — the 879-line abstract noun layer for algebraic geometry
  that `specs/variety_spec/` is written against.
- `categories/`, `core/`, `morphisms/`, `lattice_vocabulary.py` — the class
  tree and its 22-noun public vocabulary.
- `live-adapter/` — the partial re-implementation that was in progress when
  the corpus froze.
- `presentations.py` — Pydantic validators encoding what a valid presentation
  is: square symmetric Gram matrix, nondegeneracy, matching generator counts,
  form-preserving morphism matrices. Superseded by the preamble's category
  obligations.

## Not migrated

`src/sage_patches/` — seven modules installing methods onto Sage's own classes
by `setattr` (module base rings, ideals as submodules, $\mathbb Q/\mathbb Z$
quotients, free and torsion parts, `End`/`Aut`, completions). The preamble owns
all of it through owned categories and override-refine, and monkey-patching
Sage's classes is banned outright. `category_specs/` is standing prior art,
already harvested. Third-party code (the `py_polyhedral` wrapper, CARAT,
Movasati's `foliation.lib`, Dawes's `buildings.sage`, the conda installers) was
never absorbed.
