# Foundational Gaps and Papercuts

Record unresolved issues observed anywhere in research or contribution work.
The primary subject is general mathematical machinery that should be available but is missing, incomplete, or bypassed in the owned language.
Concrete workflow papercuts also belong here.
This is neither a retrospective work log nor a list of hypothetical defects.

Use the [mathematical tracing method](CONTRIBUTING.md#mathematical-dependency-tracing) and the capture/lifecycle rule [`DEV-59`](CONTRIBUTING.md#dev-59-record-observed-foundational-gaps-and-papercuts).
State the mathematics before its implementation symptoms.
Extend an existing entry when another consumer exposes the same foundation.
Link execution details in [TODO.md](TODO.md); it owns implementation ordering under the single-worker `DEV-61` rule.
Remove resolved entries with evidence in the commit, retaining only unfinished needs and any required terminal verification.
Durable definitions and decisions belong at their mathematical declarations or in CONTRIBUTING, not solely here.

## Foundational Mathematics


The table's original source audit is based on `1cc95d7b3e59`. Its counts and line
references belong to that snapshot unless an entry explicitly identifies a later
inspection. They are discovery leads, not current measurements or closure criteria.
Source inspection has not executed Sage, tests or notebooks under `DEV-58`.
Recheck each complete owner and consumer family against its current TODO contract;
retain unresolved obligations without rebuilding a source-proven repair.

| Violation | Policies | Source evidence |
| --- | --- | --- |
| **7. Runtime refinement remains a second object-construction mechanism.** | `ARC-13`, `STY-08`, `OWN-02`–`03` | The original audit found **49 `refine(...)` call sites in 25 files**. Not every mathematically proved property refinement is forbidden, but construction outside the repaired ring family still depends on mutable post-allocation placement. A current unresolved architectural example is `refine_scheme()` mutating `_preamble_scheme_*` state and calling `_refine_category_` at `schemes.py:908–926`; remeasure the aggregate count at terminal T rather than treating the original count as current. |
| **17. The type surface systematically uses implementation-universal types instead of mathematical codomains.** | `LEX-12`–`LEX-15` | Current source contains **238 `-> Parent`**, **16 `-> Element`**, **1 `-> CategoryObject`**, and **6 `-> Any`** return annotations: **261 framework-universal return annotations**. `LEX-13` explicitly names `Parent`, `Element`, `SageObject`, and `CategoryObject` as empty types that assert nothing. Examples include `Functor.object_image -> Parent`, set `cardinality() -> Parent`, arbitrary `an_object() -> Parent`, and scheme methods returning `Any`. |
| **19. The canonical notebook violates the notebook/session rules.** | `NB-01`, `NB-03`, `NB-04`, `ARC-07`, `LEX-10`, `DEV-40` | Of 51 code cells, **30 are currently unexecuted**. A committed cell retains a `NotImplementedError` traceback at `preamble.ipynb:802–822`. Markdown at `:1214–1216` says the algebra “should look like” a polynomial ring instead of asserting the claim. `:1254` states the exact substitution behavior only in prose. Session code uses `.generators()` (`1227`, `1269`), `A.Hom(P)` (`1239`), positional `P.gen(i)` (`1241`), bare global `Hom(...)` (`1267`, `1290`), low-level `module_homset`/`TensorAlgebraOf`/`DividedPowerAlgebraOf` around `977–980`, and `.hom(...)` for Coxeter diagrams around `1097`. The notebook also still names the retired coordinate escape hatches `e.to_tuple()/to_list()/to_vector()` and tensor `identity.components()`; those source edits belong to the required `canonical-notebook-contract`, since `DEV-58` forbids notebook work before that node. The heading “Coxeter diagrams as Sage parents and their morphisms” (`1080`) is also implementation-centered rather than a mathematical question (`NB-03`). |

The generated megadoc predates some source changes. Its placement diagnostics
require regeneration at T before they can establish additional current findings.
Execution ordering and closure live only in [TODO.md](TODO.md).

### Group-automorphism subgroups reuse the ambient fixed-Mor family

For a subgroup `H <= Aut_C(X)`, its group inclusion and action on `X` must
retain the subgroup restriction without changing the selected `Iso_C(X,X)`.
Source inspection finds that `GroupAutomorphismGroup._subgroup_from_engine`
(`categories/group/groups.py`) constructs another mixed Mor/category parent with the ambient parent's
`mor_family()` and endpoints. That family's canonical record still selects
the full automorphism group. `MorCategories.__contains__` correctly reads the
record, so the new parent's category role is not placed there; its independent
group enrichment does not provide a placement in `Cat` either. Reconcile the
subgroup representation, inclusion, inherited arrows and construction owner
under `membership-by-placement`. This is a source finding, not an executed
failure; changing the family record to the subgroup would instead erase the
ambient fixed category and is not a repair.

### Set-theoretic behaviour is re-implemented instead of wired to a set engine

A set is determined by its membership condition. A finite set of listed points
decides membership by the points' identity; a set given by a predicate decides
it by the predicate; the image of a map decides it by an inverse or an inverse
image. An enumeration is a further chosen datum -- a bijection from an ordinal
onto the set -- which supplies order and rank and never decides membership.
Maintained engines already implement each of these: Sage's `Set` (a hashed
`frozenset`), `ConditionSet`, `ImageSubobject`, `cartesian_product`,
`DisjointUnionEnumeratedSets`, `Subsets`, `FiniteSetMaps`, `IntegerRange`,
`NonNegativeIntegers`; SymPy's `FiniteSet`, `ConditionSet`, `ImageSet`; GAP's
collections.

The preamble's set layer (`categories/sets/set_categories.py`,
`categories/sets/finite_ordered_sets.py`) instead builds every finite set as an
index set plus position/point lambdas and derived membership by comparing a
candidate with every point. Observed on 2026-09-23: framing labels are SR
symbols, each comparison is a symbolic proof attempt, and the star import took
460 s (a rank-8 lattice took 3.3 s, growing cubically). `from_indexed` now
defaults to Sage's hashed `Set` and a hash map for positions (`77b05adb`), and
product points keep their components (`cfc27a51`); the rest of the layer still
hand-rolls what the engines above compute:

| Owned construction | Membership now | Engine that computes it |
| --- | --- | --- |
| `_ImageSet` | inverse, or `Set` of the values for a finite source | `ImageSubobject(map, domain, inverse=...)` |
| `CartesianProductsOfSets` | category default; points rebuilt through factor constructors | `cartesian_product` |
| `CoproductsOfSets` | parent identity | `DisjointUnionEnumeratedSets` |
| `PowerSets`, `FixedCardinalitySubsetSets`, `FinitePowerSets` | hand-written through subobject placement (iteration already uses `Subsets`) | `Subsets(X)`, `Subsets(X, k)` |
| `FunctionSets` | membership in the owned Mor | `FiniteSetMaps(X, Y)` |
| `_ConditionSet` | the predicate (correct in shape) | `ConditionSet(universe, predicate)` |
| `FiniteOrdinalSets`, `NN` | bounds checks (correct in shape) | `IntegerRange(n)`, `NonNegativeIntegers()` |

The set layer is one instance. The same afternoon found an owned matrix
algebra, with its tensor-algebra framing, built for every lattice in order to
take one determinant (now Sage's matrix determinant, `_gram_determinant`), a
real-number relation decided by Maxima's `simplify_full` before `AA` or Arb
were tried (`rings/real.py`), and each Gram entry re-derived by building and
expanding a pure tensor. The general need is that owned objects keep public
mathematics owned and route computation through a maintained engine
privately (`OWN-06`); where the preamble re-rolls an engine's behaviour, the
owned code is a second, slower, less correct implementation.

**Consumers:** every framed module (framing labels), tensor products (pair
labels), lattices and forms (Gram entries), catalogues, and every membership
test in construction admission.
**Coverage boundary:** the set layer's constructions were read; other layers
were found only where profiling of the star import led. The audit of the
whole preamble for engine behaviour re-implemented locally is the TODO node
`engine-wiring-audit`.

## Workflow Papercuts

Add concrete observed workflow friction here under a descriptive heading, with the user action, expected behavior, actual result, owning boundary and example.
Use `DEV-59` for capture and resolution.
Foundational mathematical gaps belong above even when first noticed as an inconvenient method or notebook interaction.
### The test suite collapses under refactoring instead of stating mathematical facts

- **User action:** run the suite after a refactor of the preamble's internals.
- **Expected:** tests outside the protected specification subtrees are independently verifiable mathematical facts: about a tenth construct an object through its public mathematical entry, and the rest assert what can be done with it and what it computes. An internal refactor that keeps the mathematics leaves them green.
- **Actual:** the 2026-09-23 triage run (TODO section *Runtime triage*) failed 11,874 of 16,309 executed tests. Where the failures are raised: 96% inside preamble or Sage code while objects are built or used, 3,680 of them in fixture setup; 496 (4%) at an assertion in the test file. The failure rate barely depends on coupling to internals (tests importing private names or reaching engine internals: 78%; public API only: 70%; specification subtrees: 73%), so the collapse is mostly construction failing, concentrated in a few raising sites. The suite nevertheless couples to internals where it should not: of the 668 test files outside `tests/constructions/` and `tests/user_simulations/`, 151 import underscored preamble names (165 imports), 32 read private attributes (61), 45 assert through `repr`/`str` (114), 52 check classes or types (127), 23 reach engine objects (51) and 16 compare a `category()` by identity (24). Each such line tests a representation or a wiring pattern rather than a mathematical claim, and breaks when the representation changes while the mathematics stays.
- **Owning boundary:** the non-protected tests under `tests/`; `test-guidelines` and the expectation-subtree rule in `AGENTS.md`.
- **Example:** `rg -l -U 'from dzack_research[^ ]* import \(?[^)]*\b_[a-z]' tests` outside the protected subtrees.
- **Work:** TODO node `test-suite-mathematical-assertions`.


### Intended research Sage runtime needs terminal verification

- **User action:** run the repository's mandatory commit gate or regenerate the live preamble megadoc using the `SAGE_BIN` exported by the tracked `.envrc`.

- **Expected:** the tracked `.envrc` selects the intended stable research-Sage runtime and its declared dependencies; the normal just recipes can preparse and import the public session.

- **Observed:** on 2026-09-15 the source-checkout `sage`/`sage-preparse`
  launcher resolved into `/home/dzack/sage-mypy-plugin/sage-stubs/sage-src` and
  failed with `ModuleNotFoundError: No module named 'sage'`. Current `.envrc`
  instead defaults to `/home/dzack/gitclones/sage-dev-allopts/.venv/bin/sage`.
  Source inspection confirms that changed launch path, not its successful runtime
  behavior. `research-sage-runtime` in TODO owns the terminal verification and
  any reproduced repair; the historical launcher failure alone does not justify
  another installation or reverting this path.

- **Owner:** research-Sage runtime/environment provisioning and the tracked `.envrc` contract.

- **Example:** observed when banking the resumed architecture-remediation DAG on 2026-09-15; the commit gate reached `_sage-syntax` and then failed inside the stub-tree `sage-preparse`.
