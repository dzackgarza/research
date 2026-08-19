# Isometry Surface Online Provenance Note (2026-02-17)

This note localizes the online source evidence used in passes `20260217-12` and `20260217-13` for `QuadSpaceWithIsom`, `ZZLatWithIsom`, `TorQuadModuleWithIsom`, and related group-action isometry surfaces.

## Online sources surveyed

- OSCAR stable NumberTheory `QuadFormAndIsom` pages:
  - https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/spacewithisom/
  - https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/latwithisom/
  - https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/torquadmodwithisom/
  - https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/manualindex/
- OSCAR dev NumberTheory `QuadFormAndIsom` pages (drift cross-check):
  - https://docs.oscar-system.org/dev/NumberTheory/QuadFormAndIsom/spacewithisom/
  - https://docs.oscar-system.org/dev/NumberTheory/QuadFormAndIsom/latwithisom/
  - https://docs.oscar-system.org/dev/NumberTheory/QuadFormAndIsom/torquadmodwithisom/
  - https://docs.oscar-system.org/dev/NumberTheory/QuadFormAndIsom/manualindex/
- OSCAR `v1` Experimental `QuadFormAndIsom` pages (signature-block cross-check for current generated method surfaces):
  - https://docs.oscar-system.org/v1/Experimental/QuadFormAndIsom/spacewithisom/
  - https://docs.oscar-system.org/v1/Experimental/QuadFormAndIsom/latwithisom/
  - https://docs.oscar-system.org/v1/Experimental/QuadFormAndIsom/torquadmodwithisom/
  - https://docs.oscar-system.org/v1/Experimental/QuadFormAndIsom/manualindex/
- OSCAR stable Hecke manual (lattices with isometry):
  - https://docs.oscar-system.org/stable/Hecke/manual/lattices/lattices_with_isometry/
- OSCAR dev Hecke manual (lattices with isometry, drift cross-check):
  - https://docs.oscar-system.org/dev/Hecke/manual/lattices/lattices_with_isometry/
- OSCAR release notes stream (surface-change corroboration for isometry/group-action methods):
  - https://github.com/oscar-system/Oscar.jl/releases

Access date (UTC): 2026-02-17

## Contracts verified from online docs

- `order_of_isometry(::QuadSpaceWithIsom)` contract includes explicit infinite-order and rank-zero behavior:
  - infinite order stored as `PosInf`,
  - rank-zero edge case uses `-1`.
- `quadratic_space_with_isometry(::Hecke.QuadSpace, ::QQMatrix; check=...)` has conflicting default wording across visible generated docs (`check::Bool=false` in signature block vs prose saying default checks are performed). Local docs now advise passing `check` explicitly instead of asserting a single default.
- Current generated signatures for `direct_sum` on `QuadSpaceWithIsom` and `ZZLatWithIsom` include both vararg and vector-input forms (not vector-only shorthand):
  - `direct_sum(Vf::Union{QuadSpaceWithIsom, Vector{QuadSpaceWithIsom}}...)`,
  - `direct_sum(Lf::Union{ZZLatWithIsom, Vector{ZZLatWithIsom}}...)`,
  and binary forms are documented with tuple outputs carrying embedding maps.
- `ZZLatWithIsom` construction from an ambient pair includes both ambient-lattice extraction and basis-matrix construction surfaces:
  - `lattice(::QuadSpaceWithIsom)`,
  - `lattice(::QuadSpaceWithIsom, ::MatElem{<:RationalUnion})`.
- `integer_lattice_with_isometry(::ZZLat, ::QQMatrix; ambient_representation=...)` explicitly distinguishes matrix representation in ambient-space basis versus fixed lattice basis.
- `trace_lattice_with_isometry` is documented with two call surfaces in current pages:
  - `trace_lattice_with_isometry(H)`,
  - `trace_lattice_with_isometry(H, res)` (explicit residue-embedding choice).
- `discriminant_group` for `ZZLatWithIsom` is documented beyond plain `TorQuadModule` output, including typed forms with induced action:
  - `discriminant_group(Lf::ZZLatWithIsom)`,
  - `discriminant_group(::Type{TorQuadModuleWithIsom}, Lf::ZZLatWithIsom; ambient_representation=true)`.
- `image_in_Oq` is documented as the general image-of-`π` computation (Miranda-Morrison context), distinct from `image_centralizer_in_Oq`.
- `torsion_quadratic_module_with_isometry` constructors are documented with broader action-data types than the minimal local signature form (current generated signatures include map/hom/matrix/group-element style action inputs).
- Generated method lists for finite-module and group-action layers show signature granularity that local docs now mirror more closely, notably:
  - `admissible_triples(::ZZGenus, ::Int)` / `is_admissible_triple(::ZZGenus, ::ZZGenus, ::ZZGenus, ::Int)`,
  - `splitting(::ZZLatWithIsom, ::Int, ::Int)` and prime-power splitting variants,
  - `is_stable_isometry(::ZZLatWithIsom)` / `is_special_isometry(::ZZLatWithIsom)`.
- For group-action layers, current manual indexes list both `invariant_coinvariant_pair(::ZZLatWithIsom)` and a distinct `fingrpact` entry for `invariant_coinvariant_pair` on plain lattices under matrix/group actions; local docs now explicitly represent the `ZZLat` action signature from the local `fingrpact` snapshot:
  - `invariant_coinvariant_pair(::ZZLat, ::Union{QQMatrix, Vector{QQMatrix}, MatGroup})`.
- `fingrpact` section wording identifies `is_isometry*` and `is_isometry_group*` helpers as non-exported input-check utilities and frames `extend_to_ambient_space` / `restrict_to_lattice` as coordinate-representation conversion between ambient-space and fixed lattice bases for collections of isometries.

## Pass-14 addendum (2026-02-17): stabilizer signature-surface fidelity

- Re-surveyed online index surfaces for `Collections of isometries` method names:
  - stable manual index: https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/manualindex/
  - dev manual index: https://docs.oscar-system.org/dev/NumberTheory/QuadFormAndIsom/manualindex/
  - v1 manual index: https://docs.oscar-system.org/v1/Experimental/QuadFormAndIsom/manualindex/
- Local snapshot source for the same section:
  - `docs/julia/oscar_jl/number_theory/quad_form_and_isom/fingrpact.md`
- Verified from these sources:
  - typed dispatch entries are explicitly shown for `is_isometry*`, `is_isometry_group*`, `special_*`, `stable_*`, `maximal_extension(::ZZLat, ::ZZLat, ::MatGroup)`, and `saturation` overloads,
  - stabilizer-family entries are currently listed by runtime method name (`stabilizer_*`) without explicit typed dispatch blocks in the available docs surfaces.
- Inference recorded for local docs/checklist alignment:
  - keep stabilizer-family methods runtime-name exact (`...` placeholders) rather than asserting speculative argument types,
  - keep `extend_to_ambient_space(::ZZLat, ...)` / `restrict_to_lattice(::ZZLat, ...)` framed as basis-representation conversion for collections of isometries, matching upstream section text.

## Pass-19 addendum (2026-02-18): map-return contract fidelity for isometry APIs

- Re-surveyed upstream pages for tuple return shapes and preconditions:
  - https://docs.oscar-system.org/v1.4/Hecke/manual/lattices/integrelattices/
  - https://docs.oscar-system.org/v1/Hecke/manual/quad_forms/torquadmod/
  - https://docs.oscar-system.org/dev/Hecke/manual/quad_forms/torquadmodwithisom/
- Verified from these pages:
  - `is_isometric_with_isometry(L, M; depth=3, bacher_depth=5, ambient_representation=true)` has explicit tuple-return contract:
    - returns `(true, f)` when an isometry exists,
    - returns `(false, zero_matrix(QQ, 0, 0))` otherwise.
  - `is_isometric_with_isometry(T, U)` / `is_anti_isometric_with_anti_isometry(T, U)` on finite quadratic modules are documented with tuple-return shape and explicit preconditions:
    - modulus compatibility (`modulus_quadratic_form` equality) or prior rescaling,
    - semiregular decomposition conditions on the relevant direct sums.
  - `is_isomorphic_with_map(Tf, Sf)` / `is_anti_isomorphic_with_map(Tf, Sf)` on `TorQuadModuleWithIsom` are documented with explicit failure sentinel:
    - success returns `(true, map)` (or anti-map),
    - failure returns `(false, 0)`.

## Pass-20 addendum (2026-02-18): `TorQuadModuleWithIsom` submodule signature fidelity

- Re-checked local snapshot and online surfaces for `TorQuadModuleWithIsom` submodule enumeration:
  - local snapshot: `docs/julia/oscar_jl/number_theory/quad_form_and_isom/torquadmodwithisom.md`
  - online pages re-used from this provenance note:
    - https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/torquadmodwithisom/
    - https://docs.oscar-system.org/dev/NumberTheory/QuadFormAndIsom/torquadmodwithisom/
- Verified from these docs surfaces:
  - the documented isometry-equipped submodule enumerator is `submodules(::TorQuadModuleWithIsom)`,
  - no `quotype` keyword is documented on this `TorQuadModuleWithIsom` method surface.
- Local documentation alignment action:
  - removed unsupported placeholder `submodules(Tf; quotype=...)` from Julia umbrella and Hecke mirror references/checklist,
  - replaced with the typed contract `submodules(::TorQuadModuleWithIsom)`.

## Pass-21 addendum (2026-02-18): `ZZLatWithIsom.order_of_isometry` contract fidelity

- Re-checked the lattice-with-isometry order contract in local snapshot text:
  - local snapshot: `docs/julia/oscar_jl/number_theory/quad_form_and_isom/latwithisom.md`
- Verified from this source:
  - `ZZLatWithIsom` is described as a quadruple `(Vf, L, f, n)` where `n` is the order of lattice isometry `f`,
  - this order is documented as a divisor of the order of the ambient isometry,
  - the same section explicitly states support for both finite-order and infinite-order isometries.
- Local documentation alignment action:
  - replaced vague `order_of_isometry(Lf)` wording in Julia/Oscar and Hecke references with the source-backed divisor/support contract,
  - added matching caveat text in `docs/julia_methods_checklist.md`.

## Pass-22 addendum (2026-02-18): genus-constructor signature fidelity (`integer_genera`, `hermitian_genera`)

- Re-surveyed Hecke genus manuals for typed signatures and argument constraints:
  - https://docs.oscar-system.org/v1.4/Hecke/manual/quad_forms/genera/
  - https://docs.oscar-system.org/v1.4/Hecke/manual/quad_forms/genusherm/
- Verified from these pages:
  - `integer_genera` is documented with typed overloads:
    - `integer_genera(sig::Tuple{Int, Int}, det::RationalUnion; even::Bool=true, kwargs...)`,
    - `integer_genera(sig::Tuple{Int, Int}, det::QQFieldElem; even::Bool=true, max_scale::Int=Int(det), rank::Int=sum(sig), kwargs...)`.
  - `integer_genera` argument constraints are explicit:
    - determinant sign compatibility with `sig=(s_+, s_-)`,
    - parity compatibility (`det ∈ 2ZZ` when `even=true`; `det ∈ ZZ` when `even=false`).
  - `hermitian_genera` is documented with explicit typed signature and defaults:
    - `hermitian_genera(E::NumField, rank::Int, signatures::Vector{Tuple{Int, Int}}, determinant::Vector{QQFieldElem}; min_scale::Int=(determinant[1] != 0 ? 0 : -3), max_scale::Int=(determinant[1] != 0 ? 0 : 3), kwargs...)`.
  - `hermitian_genera` constraints include:
    - `E` imaginary quadratic,
    - `rank > 0`,
    - determinants must have a common sign (positive for even rank, negative for odd rank).
  - `hermitian_local_genera` typed signature is documented as:
    - `hermitian_local_genera(E::NumField, p::AbsNumFieldOrderIdeal, rank::Int, determinant::QQFieldElem, min_scale::Int, max_scale::Int)`.
- Local documentation alignment action:
  - replaced `...` placeholders with typed signatures and source-backed constraint caveats in Julia umbrella and Hecke mirror references/checklist.

## Pass-23 addendum (2026-02-18): `TorQuadModuleWithIsom.submodules` keyword-contract drift reconciliation

- Re-surveyed current OSCAR `torquadmodwithisom` docs:
  - https://docs.oscar-system.org/v1/Hecke/manual/quad_forms/torquadmodwithisom/
  - https://docs.oscar-system.org/dev/NumberTheory/QuadFormAndIsom/torquadmodwithisom/
- Verified from these pages:
  - Hecke manual surface documents `submodules(::TorQuadModuleWithIsom; quotype::Vector{Int}=Int[])`,
  - same surface constrains supported selector values to `0,1,2,3`,
  - OSCAR dev NumberTheory docs expose the `submodules(...; kwargs...)` surface and document `quotype::Vector{Int}` as the active submodule-filter keyword,
  - current generated method list still includes one `automorphism_group(::TorQuadModuleWithMap)` signature location in the same page context.
- Local documentation alignment action:
  - restored the `quotype` keyword contract on `submodules` in Julia umbrella and Hecke mirror references/checklist,
  - replaced prior "no `quotype` keyword documented" caveats with a source-backed drift note against the local snapshot file.

## Pass-24 addendum (2026-02-18): `TorQuadModule.submodules`/`stable_submodules` typed signatures and `TorQuadModuleWithIsom` constructor type-union correction

- Re-surveyed OSCAR stable upstream docs:
  - `https://docs.oscar-system.org/stable/Hecke/manual/quad_forms/discriminant_group/` (TorQuadModule submodule/stable_submodules surface).
  - `https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/torquadmodwithisom/` (constructor type union).
- Verified from these pages:
  - `submodules(T::TorQuadModule; kw...)` is documented with four keyword filters: `order::Int` (by cardinality), `index::Int` (by index in `T`), `subtype::Vector{Int}` (by abelian-group invariants of submodule), `quotype::Vector{Int}` (by abelian-group invariants of quotient).
  - `stable_submodules(T::TorQuadModule, act::Vector{TorQuadModuleMap}; quotype::Vector{Int})` is documented with `act` typed as `Vector{TorQuadModuleMap}` and only `quotype` as keyword filter.
  - `torsion_quadratic_module_with_isometry(T::TorQuadModule, [f::U]; check::Bool=true)` documents `U` as any of: `AutomorphismGroupElem{TorQuadModule}`, `TorQuadModuleMap`, `FinGenAbGroupHom`, `ZZMatrix`, `MatGroupElem{QQFieldElem, QQMatrix}`; both parameters are optional (identity default when `f` is omitted).
  - `torsion_quadratic_module_with_isometry(q::QQMatrix, [f::ZZMatrix]; check::Bool=true)` also documents `f` as optional.
- Local documentation alignment actions:
  - Replaced `submodules(T; ...)` and `stable_submodules(T, act; ...)` placeholders with source-backed typed signatures in Julia umbrella reference (§2.11) and Hecke mirror reference (§2.10).
  - Added `AutomorphismGroupElem{TorQuadModule}` to the documented type union for the `f` parameter in both `torsion_quadratic_module_with_isometry` constructor rows across Julia umbrella reference (§2.18), Hecke mirror reference (§2.13), and checklist (§2.18).
  - Added optional-parameter fidelity notation (`[f]`) to both `torsion_quadratic_module_with_isometry` rows in all three surfaces.

## Pass-25 addendum (2026-02-18): `kernel_lattice` typed signatures and `image_centralizer_in_Oq` even-lattice precondition

- Source used: local snapshot `docs/julia/oscar_jl/number_theory/quad_form_and_isom/latwithisom.md`.
- Verified from this snapshot:
  - `kernel_lattice(::ZZLatWithIsom, ::Union{ZZPolyRingElem, QQPolyRingElem})` — typed polynomial argument; upstream describes resulting sublattice as primitive in `L` (non-degeneracy).
  - `kernel_lattice(::ZZLatWithIsom, ::Integer)` — computes kernel of `f^l - 1`; also primitive.
  - `image_centralizer_in_Oq` section text states: "Important note: hermitian Miranda-Morrison is only available for even lattices." Simple cases (definite, ±identity, Euler-totient-rank) do not invoke Miranda-Morrison.
- Local documentation alignment actions:
  - Replaced `kernel_lattice(Lf, p)` / `kernel_lattice(Lf, l)` placeholder entries with typed dispatch signatures and primitivity caveats in:
    - `docs/julia_methods_checklist.md` (§2.14 Kernel sublattices),
    - `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` (§2.14 Kernel sublattices).
  - Added even-lattice precondition to `image_centralizer_in_Oq` in:
    - `docs/julia_methods_checklist.md` (§2.14 Discriminant groups),
    - `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` (§2.14 Discriminant groups).
  - Added `image_in_Oq` differentiation caveat in checklist.
  - Updated `docs/julia/hecke_jl/lattice/nemo_hecke_lattice_reference.md` §2.11 to reflect typed `kernel_lattice` overloads and `image_centralizer_in_Oq` even-lattice restriction.

## Pass-26 addendum (2026-02-18): `TorQuadModuleWithIsom` submodule/aut group return types from upstream fetch

- Source used: OSCAR stable upstream `torquadmodwithisom` page (fetched 2026-02-18).
- Verified from this source:
  - `sub(Tf::TorQuadModuleWithIsom, gene::Vector{TorQuadModuleElem})` returns `(TorQuadModuleWithIsom, TorQuadModuleMap)`.
  - `primary_part(Tf::TorQuadModuleWithIsom, m::IntegerUnion)` returns `(TorQuadModuleWithIsom, TorQuadModuleMap)`.
  - `orthogonal_submodule(Tf::TorQuadModuleWithIsom, S::TorQuadModule; check::Bool=true)` returns `(TorQuadModuleWithIsom, TorQuadModuleMap)`.
  - `automorphism_group_with_inclusion(Tf::TorQuadModuleWithIsom)` returns `(AutomorphismGroup{TorQuadModule}, GAPGroupHomomorphism)`.
  - `is_isomorphic_with_map` / `is_anti_isomorphic_with_map` both typed as `(::TorQuadModuleWithIsom, ::TorQuadModuleWithIsom)`.
- Local documentation alignment actions:
  - Updated `sub`, `primary_part`, `orthogonal_submodule`, `automorphism_group_with_inclusion`, `automorphism_group`, `is_isomorphic_with_map`, `is_anti_isomorphic_with_map` entries in:
    - `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` (§2.18),
    - `docs/julia/hecke_jl/lattice/nemo_hecke_lattice_reference.md` (§2.13),
    - `docs/julia_methods_checklist.md` (§2.18).

## Pass-27 addendum (2026-02-18): ZZLatWithIsom return types and ZZLat vector-enumeration signature corrections

- Sources used: OSCAR stable upstream `latwithisom` page and `integer_lattices` page (fetched 2026-02-18).
- Key corrections verified:
  - `discriminant_group(Lf::ZZLatWithIsom)` returns `(TorQuadModule, AutomorphismGroupElem)` — not just a module pair.
  - `discriminant_group(::Type{TorQuadModuleWithIsom}, Lf::ZZLatWithIsom; ...)` — type argument is `::Type{...}`, not a positional value.
  - `image_centralizer_in_Oq` returns `(AutomorphismGroup{TorQuadModule}, GAPGroupHomomorphism)`.
  - `discriminant_representation(L::ZZLat, G::MatGroup; ambient_representation::Bool=true, full::Bool=true, check::Bool=true)` — `full` and `check` keywords were undocumented.
  - `invariant_coinvariant_pair(Lf::ZZLatWithIsom)` returns `(ZZLatWithIsom, ZZLatWithIsom)`.
  - `signatures(Lf)` constrained to hermitian-type with irreducible cyclotomic minimal polynomial; returns `Dict{Int, Tuple{Int, Int}}`.
  - `rational_spinor_norm(Lf; b::Int=-1)` — default `b=-1`, not unspecified.
  - `rational_span(Lf::ZZLatWithIsom)` returns `QuadSpaceWithIsom`, not plain `QuadSpace`.
  - `lll(L::ZZLat; same_ambient::Bool=true, redo::Bool=false, ctx::LLLContext=...)` — `redo` and `ctx` kwargs were missing.
  - `close_vectors(L::ZZLat, v::Vector, [lb,] ub; check::Bool=false)` — `check` defaults to `false`, not `true`.
- Local documentation alignment actions:
  - All corrections applied to:
    - `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` (§2.5, §2.14),
    - `docs/julia/hecke_jl/lattice/nemo_hecke_lattice_reference.md` (§2.5, §2.11),
    - `docs/julia_methods_checklist.md` (§2.5, §2.14 discriminant groups, spinor norm).

## Documentation caveat captured

In current generated docs for torsion quadratic modules with isometry, one automorphism signature location typesets `TorQuadModuleWithMap` while the page/type context is `TorQuadModuleWithIsom`. Local references treat this as a documentation typing inconsistency and keep semantic interpretation aligned with the page context.

## Local snapshot linkage

For reproducible offline context, see:

- `docs/julia/oscar_jl/number_theory/quad_form_and_isom/spacewithisom.md`
- `docs/julia/oscar_jl/number_theory/quad_form_and_isom/latwithisom.md`
- `docs/julia/oscar_jl/number_theory/quad_form_and_isom/torquadmodwithisom.md`
- `docs/julia/oscar_jl/number_theory/quad_form_and_isom/fingrpact.md`
- `docs/julia/oscar_jl/number_theory/quad_form_and_isom/enumeration.md`
- `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md`
- `docs/julia_methods_checklist.md`
