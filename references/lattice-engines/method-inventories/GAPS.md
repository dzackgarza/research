# Documentation Coverage Gaps

Gaps between upstream doc snapshots and checklist entries. Only upstream docs and checklists matter — self-authored reference docs are not a tracked deliverable.

## Gap 1: Checklist entries missing vs upstream docs

Methods present in local upstream snapshots but absent from the corresponding checklist.

Initial spot-checks for FLINT, NTL, and PARI/GP have been performed. These packages have received attention but are not exhaustively verified — the same method-by-method comparison as noted in Gap 3 applies to them as well.

## Gap 2: Upstream docs referenced in readmes but not locally copied

### NTL

- `HNF.cpp` / `HNF.cpp.html` — cited in research_readme as the source for `HNF(W, A, D)`, but not present under `docs/ntl/upstream/`. URL: `https://libntl.org/doc/HNF.cpp.html`

### Sage

5 modules referenced in `docs/sage/lattice/research_readme.md` with no local upstream copy:

- `sage.modules.free_quadratic_module` — generic free quadratic module (the `_integer_symmetric` variant IS present, but the generic base module is not)
- `sage.quadratic_forms.constructions` — lattice construction helpers
- `sage.quadratic_forms.count_local_` — local counting routines
- `sage.quadratic_forms.genera.normal_form` — genus normal form algorithms
- `sage.quadratic_forms.qfsolve` — quadratic form solving routines

### Sage directory structure

`docs/sage/special_forms/` is an invented grouping — not a Sage module. The four upstream docs it contains correspond to `sage.quadratic_forms.*` submodules:

- `binary_quadratic_forms/` → `sage.quadratic_forms.binary_qf`
- `bqf_class_group/` → `sage.quadratic_forms.bqf_class_group`
- `ternary_quadratic_forms/` → `sage.quadratic_forms.ternary_qf`
- `ternary_helpers/` → `sage.quadratic_forms.ternary`

These should be under `docs/sage/quadratic_form/` to mirror the actual Sage module hierarchy.

### Julia / Oscar.jl

The core Oscar `ZZLat` / integer lattice documentation page is not locally copied. The `oscar_jl/` tree has `number_theory/quad_form_and_isom/` pages (latwithisom, torquadmodwithisom, etc.) and `algebraic_geometry/surfaces/` pages, but no local copy of the primary integer lattice API page that documents constructors like `integer_lattice()`, `gram_matrix()`, `genus()`, `rank()`, `det()`, etc.

### Julia / Hecke.jl

`docs/julia/hecke_jl/` contains only `lattice/research_readme.md` — zero upstream doc copies. All Hecke lattice methods in the readme have no locally-backed upstream source.

## Gap 3: Upstream-vs-checklist comparison not done for remaining packages

The above spot-checks cover FLINT, NTL, and PARI/GP. The same upstream-vs-checklist comparison has not been systematically performed for:

- SageMath (283 checklist entries across many upstream files)
- Julia / Oscar.jl / Hecke.jl (357 checklist entries)
- GAP core (69 checklist entries)
- HyperCells (241 checklist entries)
- Crystallographic stack (31 checklist entries)
- g6k (30 checklist entries)
- flatter (12 checklist entries)

Each of these needs the same method-by-method comparison against its upstream snapshots to identify missing checklist entries.
