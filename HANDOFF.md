<<<<<<< HEAD
# Finish the resumed research / indefinite-port work

## Ambient task

The owner requested: **“finish ALL of the in-progress and incomplete work”** in the research / `sage-indefinite-port` handoff. Finish the two inherited workstreams, their mathematical and runtime prerequisites, every named remaining specimen, the port amendments and the applicable final acceptance. Source changes, isolated examples and local branch integration do not establish completion.

The task remains incomplete. The immediate structural problem is constructing an actual category with a chosen functor, needed by the projective-action consumer after removing separate functor-object representations. The other obligations below remain required while that problem is repaired.

Read `INTENT.md`, `AGENTS.md`, `CONTRIBUTING.md`, `TODO.md`, `COMPLAINTS.md`, `docs/preamble-megadoc.md` and the edited subtree's governing files before implementation. `TODO.md` remains the single dependency graph. This document is the authoritative session handoff; acceptance clauses and observed defects live at their TODO/complaint owners.

### Settled owner decisions

- A morphism `f: X -> Y` is itself an object of `Mor_C(X,Y)`. If it is an endomorphism, it is already in `End_C(X)`. **`X.End()(data)` is the constructor API.** There is no `X.End().object(...)` API.
- A functor `F: C -> D` is itself an arrow of `Cat` and an object of `Fun(C,D)`. A natural transformation has the actual functors as endpoints. Sage's representation constraints must be repaired in the runtime.
- An admitted arrow is retained unchanged. Applying an actual functor is how arrows move between categories. Constructors must distinguish foreign whole arrows from legitimate defining data such as generator maps, inverse pairs and module/value-map pairs.
- Routine naming and engineering decisions belong to the implementer. The gluing names are settled: `gluing_subgroup()` on a finite-index embedding or cyclotomic decomposition denotes the full glue `L/M` in `A_M`; `invariant_gluing_subgroup()` on `IsometryPrimitiveExtension` denotes the projected subgroup in the invariant lattice's discriminant group. Preserve the subgroup assertions under those names.
- No stubs were permitted for this resumed task. A missing computation remains an incomplete obligation; an issue or a TODO entry records it without discharging it.
- Research owns independent general primitives with supplied data; the port owns indefinite recursion, covering search and traversal. Use the concrete boundary in `AGENTS.md` and the function-level assignments in the port's `references/port-design.md`.
- Mathematical meaning belongs to `lean-categories`; correctness evidence belongs to the leaf-blind `lean-cas-dsl` acceptance suite. Research and port checks provide engineering diagnostics, not authority to change mathematics or frozen expectations.

## Completion conditions and present verification limits

Every row is required. “Source present” means implementation exists to review; it is not acceptance at the final revision.

| Required item | Completion condition | Present limit / next verification |
| --- | --- | --- |
| Actual arrows, functors and category objects | Repair `realization-methods-reach-their-category-operations`: actual objects and higher-arrow endpoints, both category/object operation readings, and all affected construction routes work through their owners. | Ordinary fixed-Mor and basic functor paths have bounded execution evidence. Category enrichment in `Cat/site` is unresolved; concrete two-argument category `Mor` overrides need review. The new category-slice assertion is still red in production. |
| Foreign-arrow constructor boundary | Discharge CON-17 across all affected research and port call sites. Existing arrows remain unchanged; unrelated arrows are refused; every legitimate defining-component case remains constructible. | The inherited WIP has substantial repairs. Full caller classification and final execution remain required, including the explicit cases under `terminal-session` in TODO. |
| Orthogonal-sum labels and cyclotomic divisors | Labels and integer divisors are owned points; all consumers indexing named summands retain their intended maps. Polynomial restrictions and component isometries agree with the decomposition. | Source exists; review the entire relabelling impact and verify on the final tree. The original three-cycle and `U+U` specimens remain required. |
| Arithmetic centralizers | Assemble the compatible component centralizer through finite glue, retaining restriction/extension maps and supplied groups. Include the `U+U` swap, the required `O(U(2))` generators, and the E8 specimen. | Earlier small executions are not final-revision acceptance. Recheck the formerly slow divided-power/glued route. Port cases 110, 88 and 96 still require a justified route for non-scalar indefinite Hermitian component centralizers or a formally approved #33 contract amendment. Ordinary component orthogonal groups do not answer that request. |
| Supplied-generator group primitives | Execute the 2U parabolic specimen, its supplied-kernel preimages and inverse data, plus the line-section construction in an infinite orthogonal group. | Source and earlier small-specimen evidence exist. Recheck the final runtime, including the strengthened split-line Levi form-preservation assertions for A1, A2 and E8, both signs and scales 1 and 2. |
| Radical isotropic actions | Realize `Hom(M/R,R) ⋊ (O(M/R) × GL(R))` through the existing general semidirect-product owner, with actual factors/actions/maps and its mathematical assertions. | General supplied-factor work exists; verify the complete action and map contracts on the final tree. Check `lean-categories` before inventing any missing foundation. |
| Eichler transfer | The port owns `TwoUFull` and the approximate generating-family/envelope algorithms; research dispatches and removes the transferred algorithm bodies. Repair the `EichlerEnvelope` complement-selection defect. | The #18 request is recorded; completion of the implementation and consumer acceptance remains required. |
| Remaining terminal mathematical specimens | Execute configurations, cones/integral points, projective-line cusps, norm-two root types, orbit splitting, binary fixed-norm orbits and all banked assertions in this scope under their live owners. | Earlier executions precede the shared arrow runtime changes. Preserve every remaining assertion and establish final-revision results. Named files are indexed below. |
| Construction cost and deferred validation | Discharge the applicable `construction-is-instant` clauses: defining data only at construction, validators governed by the shared strict flag, and derived data computed lazily through their owners. | The node remains open. Inspect indexed-category/finite-support-power and family-stabilizer paths, permutation checks, form symmetry, Leech backend checks, primitive embedding and glue checks. TODO contains source claims that require reconciliation against live code. |
| Observed performance defects | Profile the smallest slow specimen and repair its actual computational route while retaining the mathematical result. | Port `IsotropicCases_55` remains unresolved. Reassess the E8 centralizer, two-point binary fibre and D4 stabilizer costs; preserve the finding when a small case is slow. |
| Port amendments and full acceptance | Resolve #18/#33 obligations; reconcile obsolete strict xfails with the real capability contracts; review inherited port changes and run the complete frozen acceptance at the integrated dependency revision. | Full port acceptance is incomplete. The rank-three isotropic case prevents claiming completion. An empty `UNFINISHED` table does not justify dropping an expected assertion. |
| Delivery | Applicable import, lint, type, performance and final acceptance requirements hold for the actual source revision; integrate the authorized work on the line of record. | Final integrated verification is outstanding. The latest focused research gate stops before test execution because its fresh preamble import exceeds the unchanged two-second ceiling. |

### Permanent mathematical obligations

`TODO.md`'s `terminal-session` owns unexecuted assertions, including the constructor boundary's positive and negative cases. The former long handoff's mathematical specimens remain recoverable at the immutable Git source `f02974fd7099bd3e8991f548fdfe7b2b03828bbb:HANDOFF.md`, particularly **In progress**, **Next checks** and **Closure work**. Preserve and reconcile those assertions with their live TODO/test owners; historical closure prose is not acceptance or a new priority list. Retrieve the source with:

```sh
git show f02974fd7099bd3e8991f548fdfe7b2b03828bbb:HANDOFF.md
```

Useful existing assertion files:

- `tests/categories/test_categories_as_objects_in_cat.sage`, `test_mor_categories_answer_both_readings.sage`, `test_mor_arrow_constructor_boundary.sage`.
- `tests/constructions/test_mor_categories_construct.sage`, `test_category_functor_morphism_surface_construct.sage`, `test_core_and_arrow_mor_owner_construct.sage`, `test_natural_transformation_morphism_retention_construct.sage`, `test_isometry_primitive_extension_glue_surface_construct.sage`.
- `tests/divisors/test_projective_line_bundle_linearizations.sage` and `tests/schemes/test_formal_spectrum_of_the_three_adic_integers.sage`.
- `tests/lattices/test_cyclotomic_centralizer.sage`, `test_centralizer_gluing.sage`, `test_split_line_levi_generator_lifts.sage`, `test_parabolic_induction.sage`, `test_parabolic_gluing.sage`, `test_binary_fixed_norm_orbits.sage`, `test_norm_two_root_types.sage`, `test_orbit_splitting_along_finite_index_subgroups.sage`.
- Port `tests/acceptance/test_isotropic_orbits.sage` and `tests/fixtures/isotropic_cases_8821.json`; retain the complete frozen corpus, not only this failing fixture.

## Ranked next work

### 1. Repair the category construction, then finish the shared arrow boundary

Start with `test_a_category_with_a_chosen_functor_retains_its_category_operations` in `tests/categories/test_categories_as_objects_in_cat.sage`. The production failure is `SliceCategory._construct_on` asking an actual `PosetCategory` for `_with_structure`.

Trace `Cat`'s category-object construction against `Objects.ParentMethods._with_structure`, `OwnedCategoryObject` and the native category constructor. A category with a chosen functor must retain its category's defining objects, arrows, composition and identity while the slice level retains that functor. Implement this through the owner, including repeated slice enrichment and actual slice arrows. No production implementation of this repair has been committed.

Inspect `categories/abstract_categories/cat.py`, `mor_foundation.py`, `mor_categories.py`, `arrow_categories.py`, `products.py`, `presheaves.py`, `owned_category.py` and `owned_category_bases.py`. The generic public arrow checks now include `CategoricalArrow`; specialized `Map` checks still require role-by-role review. Keep engine-ingress checks distinct from public arrow admission. Review direct category `Mor(self, source, target)` methods that can bypass the shared descriptor, rather than adding per-category arity shims.

Then execute the actual category-slice, fixed-Mor, natural-transformation, projective section-action and adic reduction assertions. The projective route passes through `FiniteAffineAtlases -> _covering_family -> SliceCategory(Cat(), site)`; the section assertions have not yet been reached. Review `linearizations.py`, `formal_schemes.py` and all diagram/GObjects callers as consumers of the same structural change. The constructed-algebra-map supplier must build its linear datum at its immediate module owner; retain product/unit equations and exact scalar data.

### 2. Repair import cost and resume the mathematical/computational obligations

The focused research gate's import ceiling is two seconds. Its latest invocation on the pinned validation tree exits at 2.31 seconds, before collection. Profile the actual fresh pytest import path and repair eager dependencies; keep the checker and thresholds intact. Do not infer a cause from elapsed time alone.

After the structural repair, verify centralizers, supplied-generator primitives, radical actions and the remaining specimens against their actual contracts. Reconcile the source with TODO/complaints only after the required delta exists. Audit construction cost at the owner rather than converting each symptom into another consumer patch.

For port isotropic case 55, the Gram matrix is `[[1440,828,288],[828,480,168],[288,168,59]]`, determinant `-432`, with an isotropic line. The frozen assertion requires the actual primitive marking-class result. A mere isotropy/existence shortcut does not satisfy it. Use a bounded, seeded profile of the unchanged assertion; prior profiles reached the cell/facet traversal. Examine `indefinite/lorentzian_cells.py` and its retained positive-vector enumeration. Reuse the supplied module/tensor/solver data and maintained backend computations; preserve enumeration bounds and completeness. A timeout must produce a failing exit status.

Resolve the centralizer component route and transfer work at their actual owners. Existing requests:

- Port #18: <https://github.com/dzackgarza/sage-indefinite-port/issues/18#issuecomment-6214279462>.
- Port #33: <https://github.com/dzackgarza/sage-indefinite-port/issues/33#issuecomment-6213760771>.
- Report the measured rank-three traversal defect on port #15 with a reproducible mathematical specimen and actual profile evidence. Verify the current issue state before relying on these locators.

### 3. Establish the complete completion condition

Review the full inherited research and port changes against the scope table, regenerate/read the preamble documentation when authorized, and execute the applicable final requirements on a fixed dependency revision. Keep focused diagnostics, mathematical acceptance, full frozen-corpus acceptance and publication as separate claims. Verify the current source and remote state before integration; an old branch name or historical status does not establish either.

### Where to resume and what to verify first

The authoritative source work is in these existing worktrees. Inspect their current HEAD and dirty state before editing:

| Worktree | Branch / role |
| --- | --- |
| `/home/dzack/research/.tmp/wt-foreign` | `port-gaps8-foreign`: actual-arrow runtime and all current research repairs. |
| `/home/dzack/research/.tmp/wt-cyclo` | `port-gaps9-cyclo`: pinned validation/dependency tree; advance only after every reader exits. |
| `/home/dzack/gitclones/sage-indefinite-port/.tmp/wt-handoff` | `finish/handoff-remainder`: receiving port work and frozen consumer assertions. |

The original cyclotomic commits and the initial foreign-arrow WIP are already ancestors of the last inspected research `origin/main`; use ancestry and the actual diff to identify remaining work. Preserve unrelated dirty work in `/home/dzack/research` and the canonical port checkout. `.tmp/wt-port` / `port/after-410` belongs to another session and is outside this session's worktrees. `research-split-finish` has another owner; any relevant comparison is read-only. Recheck all of this live.

Worktree probes must print `dzack_research.__file__` and use the intended source explicitly:

```sh
direnv exec /home/dzack/research env   PYTHONPATH=/home/dzack/research/.tmp/wt-foreign/src:/home/dzack/gitclones/sage-indefinite-port/.tmp/wt-handoff/src   TMPDIR=/home/dzack/research/.tmp/wt-foreign/.tmp   sage -python <small-specimen-script>
```

`sage -python` here uses the local Docker wrapper. Keep scratch inside the repository. Use the project recipes and unchanged time gates; keep smallest-case probes bounded and profile slow ones. The wrapper does not forward `PYTEST_ADDOPTS`, so pass required pytest flags as actual arguments. Native Sage Python is 3.14 while host Python is 3.12: a host AST pass that silently skips newer syntax is not a complete inventory.

Check owned processes before resuming; no validation reader was active when this handoff was prepared. Machine-wide QC can queue behind other repositories. A queue is not a running test and provides no acceptance result. Preserve other owners' processes. The earlier gate sessions have exited.

### Retired or settled lanes

- The Mor-object representation and `X.End()(...)` API are settled by the owner. Implementation limitations create runtime repair work, not another contract question.
- The separate functor-object entry and legacy Cat arrow/category wrappers are removed. Their absence is part of the required result.
- The old issue-401 closure narrative and whole-owner audit chronology do not select the resumed task. The ranked work above and the live dependency graph do.
- No SSH workstation investigation is authorized for this handoff. Local source, explicit HTTPS GitHub access where needed, and the existing worktrees suffice for the identified work.
- Naming is settled as recorded above; the owner is not being asked to micromanage it.
=======
# Active task: geometry and cohomology categories in the preamble

## Ambient task

Present the categories, their placements and subtrees, and the functorial
constructions in the scope below. Make the named mathematical objects construct
through the preamble. Each construction must retain its defining data and maps,
lie in the correct category, and expose its operations at their mathematical
owners.

The initial request permitted category and operation stubs. The subsequent
construction pass requires every named construction to work through the session
star import, print the mathematical object and answer the named operation.
A construction failure or wrong placement is required repair work. Explicit
computational stubs remain permitted only at the boundaries stated below.

## Completion condition and complete scope

This task is incomplete. Every row below remains open until its full acceptance
condition has been checked against live source and the required mathematical
assertions. A verified specimen establishes only the stated result.

For each row, establish the public constructor, defining data, immediate
supercategories, inherited operations and relevant functors. Check functor
domains, codomains, action on arrows and the retained universal maps. Construct
objects through their mathematical owners; expose preamble objects throughout.

“Partial” records bounded verification from the current local line. It does not
establish the entire acceptance condition. Recheck the named source and
assertions before relying on that status.

| Required item | Acceptance condition | Verified status and remaining checks |
| --- | --- | --- |
| Exact complex field CC | Use Nemo/Calcium privately for exact complex computation. Retain the morphisms ZZ, QQ, QQbar and exact RR into CC. Conjugation is a field automorphism; absolute value lands in exact RR. Numerical approximation uses a named map. Polynomial rings and schemes over CC construct. | Partial: algebraic ingress, I² = −1, exp(Iπ) = −1, and distinction of 1 from 1 + 10⁻³⁰ were exercised. The Fermat quartic constructs with its stated variety placement. Check all field structure, elementary functions and scalar maps. |
| Varieties over k | Present integral, separated, finite-type schemes with their correct category parents and constructors, including exact CC as a base. | Partial: the Fermat quartic over CC constructs with explicitly stated variety placement. Reconcile the general constructors and hypotheses. |
| Curves and surfaces | Present the relative-dimension-one and relative-dimension-two varieties and their projective and proper refinements. | Partial: the real projective plane and the affine parabola through Curves(QQ).from_equation construct in their stated categories. Check all requested bases and refinement maps. General hypersurface construction alone does not assert integrality. |
| K3 surfaces | Construct the smooth quartic and the stated Horikawa family through their defining scheme and surface owners. Retain inclusions and family data. | Partial: the quartic supplies rank-22 cohomology with Hodge numbers (1,20,1). Horikawa defining bundles and invariant branch sections construct. Reconcile the remaining K3 requirements. |
| Families X → Y and one-parameter families X → C | Represent a family by its actual morphism, as an object of the appropriate slice. Construct fibres with their pullback projections and universal maps. | Partial: Hesse affine and projective pencils construct; a projective-pencil fibre retains both projections. The Legendre family morphism constructs. Check all named families, bases and fibre operations. |
| Function fields k(t) | Construct the function field of a nonempty affine chart of an integral scheme; P¹ gives k(t). | Partial: the projective-space function field constructs. Check the P¹ specimen and the chart and scalar maps. |
| Affine and projective hypersurfaces | Construct the defining coordinate rings, equation, closed subscheme and inclusion through the public owners. Retain homogeneous grading in the projective case. | Partial: both constructors are present and exercised. Check defining maps, required placement and all named specimens. |
| O on projective space and its twists O(m) | Construct the invertible sheaf and its sections. For O(m) on Pⁿ, H⁰ is the degree-m forms, Hⁿ is dual to the degree −m−n−1 forms, and intermediate cohomology vanishes. | Partial: H⁰(P²,O(1)) has rank three and derived global sections construct. Finite-atlas and restricted line bundles now compute chart and compatible global sections through module descent. Check positive and negative twists and the higher-cohomology specimens; none of the section functors has run. |
| Presheaves and sheaves valued in sets, groups, rings, ZZ-modules, R-modules and R-algebras | Present the value categories and the actual sections functor on opens, its restriction maps and sheaf descent. Keep fixed-value functor categories distinct from the varying-value construction. | Partial: the fixed-value presheaf categories construct for all listed values. The affine structure, associated-module, unit, total-quotient, descended-algebra, Cartier-quotient, finite-atlas module and line-bundle, meromorphic, and projective closed-subscheme structure constructors now retain open-site sections functors with their restriction maps. Source-level only: no constructor has run, and the generic `_UnpresentedSectionsPresheaf` route and its callers remain to be retired. Sections on non-basis opens still need their explicit missing-computation assertions checked. |
| Projectivization P(V) | Construct Proj Sym(V) with its projection, tautological invertible sheaf and universal quotient. Retain the comparison with projective space for a free module and the required relative maps. | Partial: rank-two projectivization, its surjective universal quotient and the projective-space comparison construct. Check the complete relative construction and slice API. |
| Module duals | Construct Mor_R(M,R¹) at the module owner with its module structure and evaluation maps. | Partial: the rank-two vector-space dual has rank two. Check the requested functorial maps and variance. |
| Linear systems and monomial section bases | Retain the selected section space, embedding into global sections, base locus, domain of definition and associated map. Construct restriction and jet maps where requested. | Partial: the complete conic system on P² has six monomial sections and its associated map. Coordinate-hyperplane restrictions and jet specimens were exercised. Reconcile the remaining maps and systems. |
| Graded singular cohomology | Construct H*(X;R) with grading, cup product, coefficient maps and functorial action. | Partial: the complex realization of P² supplies a graded algebra over ZZ. Check its operations and the required maps. |
| de Rham algebra and cohomology | Construct the relative graded-commutative DGA of a smooth affine scheme, its differential, and the stated cohomology. Include vector fields, graded derivations, contraction and Lie derivative at their owners. | Partial: QQ[x] de Rham algebra and degree-minus-one derivations construct; H²_dR(P²) has rank one. Reconcile the smooth affine relative specimen and Cartan operations. |
| Derived sheaf cohomology and RΓ | Construct derived global sections in the appropriate derived category. Sheaf cohomology in degree i is the ith cohomology of that object. Present the R-linear triangulated parent of D(R). | Partial: derived sections of O(1) on P² construct. Check category parents, the cohomology identification and the required maps. |
| Primitive cohomology | For a polarized smooth n-fold, retain the kernel and inclusion of L_h^(n−k+1): H^k → H^(2n−k+2). P² in degree two has primitive rank zero; a smooth plane cubic in degree one has rank two. | Partial: the P² specimen has rank zero. Check the cubic specimen, polarization and Lefschetz maps. |
| Residue maps on forms | Construct the residue map with its actual differential-form domain and codomain, including the stated plane-cubic specimen. | Partial: the plane-cubic residue object has rank-one domain and codomain. Check the defining spaces and maps. General residue computation may remain an explicit stub. |
| Homotopy Lie algebras | Construct the pointed-space graded Lie algebra with the Whitehead bracket and stated grading. For S², shifted degrees one and two have rank one and [ι,ι] = 2η. | Partial: these S² assertions were exercised. Check integral versus rational placement, the degree conventions and functorial maps. Computation of sphere homotopy in degrees at least four may remain a stated frontier. |
| Hodge and mixed Hodge structures | Present the coefficient objects, filtrations and their maps. Construct Tate twists, tensor products and duals. Include projective-space and K3 Hodge structures. | Partial: the named operations and P² and quartic K3 Hodge-number specimens were exercised. Reconcile all structure maps and category placement. |
| Connections and Gauss–Manin connections | Present bundles with connection and their morphisms. For a smooth proper family, construct the Gauss–Manin object in integrable connections on the base. | Partial: the Hesse smooth-locus object lies in integrable connections with finite locally free underlying bundle. Check connection morphisms and retained family maps. The Gauss–Manin connection matrix may remain an explicit computational stub. |
| Analytic disc fibres | Construct the analytic family, exact-complex disc points, fibres and fibre inclusions along the selected scalar embedding. | Partial: a disc-point fibre is a complex manifold and the inclusion retains that same fibre as domain. Reconcile all required family maps and analytification. |
| HH and Γ\\HH | Construct the upper half-plane, group action and quotient with their correct complex-manifold or orbifold placement. | Partial: HH and SL₂(ZZ)\\HH construct. Check action morphisms and quotient maps. |
| Real hyperbolic Hⁿ and its quotients | Construct H² and H³ through their Riemannian and globally symmetric owners. Retain the discrete isometry action and quotient map. | Partial: H² and its lattice-isometry quotient construct with Riemannian manifold and orbifold placement. Check H³ and the retained maps. |
| Siegel H_g and its quotients | Construct the symmetric-matrix domain with positive definite imaginary part and the symplectic action. Construct Sp₄(ZZ)\\H₂ as an orbifold. | Partial: H₂ and the stated arithmetic quotient construct. Reconcile the defining domain, action and quotient maps. |
| Symmetric spaces G/K by Satake type | Supply the classification type as a category parameter. Construct the correct Riemannian symmetric-space object and retain its defining data. | Partial: the SU(2,1) Satake specimen has real rank one and dimension four. Reconcile the full requested type construction and parents. |
| Hermitian symmetric domains by type | Present the domain classification through parameters of the appropriate category, with correct parent and dimension. | Partial: EIII and EVII construct with dimensions sixteen and twenty-seven. Check the remaining named types and defining data. |

### Permitted stubs

A general operation may retain an explicit computational stub where the
construction request permits it. The table names the specific residue,
Gauss–Manin matrix and higher sphere-homotopy frontiers already identified.
The mathematical object, its defining data, domain, codomain and placement must
still construct. Sections on a non-basis open may assert with the precise
missing computation; an empty sections functor is not a permitted substitute.

For other operations, establish the permission from the original construction
request before marking the item complete. An unverified permission stays open.

### Binding decisions

- Exact CC uses Nemo/Calcium as its private computational engine. Preamble
  QQbar remains at its own owner; CC accepts its elements through QQbar → CC.
- A derivation with regular-module codomain has values in A¹. Compare with A
  through the explicit regular-module identification. The public
  linear_endomorphism operation supplies that transport.
- Use picard_to_class_group_morphism for the existing projective-space map.
  Choose routine public names from the mathematical owner without requesting
  a naming decision.
- Present PicardGroups and ClassGroups as the stated full subcategories of
  abelian groups. Each value supplied by a scheme retains that scheme.
  Picard pullback for a plane cubic must send [O(1)] to [O_C(1)].
- A category parent states the actual mathematics. A missing parent requires
  its own category construction or an explicit abstract boundary.
- All public mathematical objects and their constituents are preamble
  objects. Reuse maintained engines privately.
- Preserve existing rack edits.

## Next work, ranked

Nothing in this handoff has been executed. Every sheaf-section constructor
named below was written under the DEV-58 source-phase rule, and none of its
mathematical assertions has run; treat every status above as a source-level
claim a running session must falsify before it believes it.

1. Execute the required assertions of the `sheaves-compute-sections-on-opens`
   TODO node as soon as execution is authorized: on `Spec(QQ[x])`, the sheaf
   associated to `M=QQ[x]^1` has whole-space sections `M`, sections `M_x` on
   `D(x)`, and the localization restriction; the regular-units sheaf has the
   unit group of `QQ[x]`; on `P^1_QQ`, the inverse image of a chart module
   sheaf has its stated chart sections. Repair at the shared owners whatever
   these specimens falsify; do not patch individual constructors.
2. Reconcile the `sheaves-compute-sections-on-opens` and
   `nonaffine-structure-sheaf-coverage` TODO rows against the delivered
   source, and complete their remaining delta: comparisons between distinct
   presentation atlases and nonprincipal Cartier divisors through common
   refinement, finite-atlas algebra descent on the open site without finite
   underlying modules of polynomial algebras, sections on general opens from
   their chart traces with explicit missing-computation assertions where a
   computation is absent, and removal of `_UnpresentedSectionsPresheaf` and
   `_unpresented_sheaf_placement` once their actual callers have sections
   functors.
3. Reconcile each remaining scope row against its live owner, immediate
   ancestors and public constructions, starting with the rows whose defining
   functors or maps remain unverified. Update this table with exact acceptance
   status and the remaining mathematical obligation.
4. Verify the remaining named constructions, including the plane-cubic
   primitive kernel, relative de Rham and Cartan maps, connection morphisms,
   higher-cohomology twists and classification parameters. Repair shared
   structural causes at their owners.
5. Close the task only after every required item meets its acceptance
   condition or has an explicitly permitted and precisely stated stub.
   Selected successful specimens alone do not satisfy that condition.

The earlier issue-401 implementation, port reconciliation and whole-preamble
audit lanes are retired from selection for this request. Their live obligations
belong to TODO.md and their owning artifacts.

### Working references

Read INTENT.md, AGENTS.md, CONTRIBUTING.md, TODO.md, COMPLAINTS.md and the
relevant entries of docs/preamble-megadoc.md before changing the affected
owners. Resolve mathematical placement from the governing architecture.

The original construction detail is in the Claude session
/home/dzack/.claude/projects/-home-dzack-research/7de3fff4-5627-45ef-b8ea-4645b6d2e760.jsonl.
Use the reading-transcripts parser to inspect it. The corresponding briefs are
under /tmp/claude-1000/-home-dzack-research/7de3fff4-5627-45ef-b8ea-4645b6d2e760/scratchpad/.
The 2026-10-16 sections-constructor pass is the Codex session
/home/dzack/.codex/sessions/2026/10/16/rollout-2026-10-16T19-46-12-01a14488-b1d8-7552-ae55-60e3162fb38f.jsonl.

For targeted specimens, use
env PYTHONPATH=/home/dzack/research/src /home/dzack/gitclones/sage-dev-allopts/.venv/bin/python.
For a worktree, select its src directory and verify dzack_research.__file__.
The Sage launcher here does not accept -python. Follow the repository rules
for targeted tests and its existing time budgets.
>>>>>>> 4b9e517526c6d8003c83d52fc18ef057acfd829a
