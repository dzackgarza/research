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
