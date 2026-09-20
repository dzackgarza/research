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
| **3. Some descendants still restate operations already inherited from their mathematical owners.** | `OWN-14`, `STY-154`, `DEV-10` | Current source inspection under `DEV-58` finds the selected framing datum centralized at the global `Framed` owner and specialized by groups, modules and algebras without separate framing records. The independently remaining residue is operation restatement rather than framing reconstruction; for example `lattices.py` still supplies its own `module_generator` specialization. Reconcile the complete remaining family under `inherited-operations-not-restated`, rather than reopening the framing contract. |
| **4. Internal representation vocabulary leaks into the public mathematical view.** | `LEX-01`, `LEX-04` | Public generator displays are literally named `"Module-generator family"` (`modules.py:2204`), `"Free-module generator family"` (`framed_free_modules.py:403`), `"Presented-module generator family"` (`finitely_presented_modules.py:825`), `"Lattice-generator family"` (`lattices.py:1491`), `"Fractional-ideal generator family"` (`fractional_ideals.py:233`), etc. This is exactly the type-theoretic implementation leakage you identified: the user asked for module generators, not an `IndexedFamily` implementation concept. |
| **7. Runtime refinement remains a second object-construction mechanism.** | `ARC-13`, `STY-08`, `OWN-02`–`03` | The original audit found **49 `refine(...)` call sites in 25 files**. Not every mathematically proved property refinement is forbidden, but construction outside the repaired ring family still depends on mutable post-allocation placement. A current unresolved architectural example is `refine_scheme()` mutating `_preamble_scheme_*` state and calling `_refine_category_` at `schemes.py:908–926`; remeasure the aggregate count at terminal T rather than treating the original count as current. |
| **8. `NotImplementedError` is still a normal mathematical control path.** | `CAT-01`, `DEF-06`, `STY-48`, `DEV-11` | There are **449 direct `raise NotImplementedError` statements**; AST classification finds **212 public callables containing one**. `CAT-01` explicitly says "`NotImplementedError` is not a mathematical implementation strategy"; unsupported computational cases must end at the declared assertion-gated frontier. Major concentrations include `schemes.py` (45 direct raises), `algebras.py` (37), `commutative_algebra.py` (29), `modules.py` (20), `lattice_morphisms.py` (16), `lattices.py` (14). |
| **13. A substantial Singular algorithm is still orchestrated locally in Python.** | `ENG-01`–`03`, `STY-57`–`59`, `OWN-08` | `_singular_presentation_kernel` in `finitely_presented_modules.py:2240ff` performs a long sequence of matrix construction, coefficient lifting, Singular `modulo`, relation reconstruction, and lift recovery through roughly lines 2270–2415. This is the exact current-tree exemplar named by `CONTRIBUTING.md`: the maintained engine should own the coherent kernel computation behind one crossing. |
| **15. Generic imperative algorithms catalogued by the guide remain live.** | various `STY-*` | Examples still present include the nested bilinear accumulation in `forms.py:245–250`; multiplicative `_multiply_in_target` loops in both `free_algebras.py:1464–1468` and `sparse_free_algebras.py:634–638`; `_divided_product_coefficient` in `powers.py:584ff`, including the algebraically inert second `*=1` loop; the append/filter loop in `absolute_galois_group.py:697–708`; `setdefault(...).append(...)` in `finitely_presented_algebras.py:119`; and numerous `frontier`/`seen` bespoke traversals in torsion forms, orthogonal quotients, lattices and lattice morphisms. |
| **16. Public mathematical products are still returned as Python tuples.** | `CON-15`, `SET-01`, `CAT-08` | `CommutativeSquare.components()` and `NaturalTransformation.naturality_square()` still return two-morphism Python tuples. `CON-15` expressly says a bare tuple never appears as a public mathematical return. Tensor variance/index families now use the owned product of two mathematical family objects, so that repaired case is no longer evidence for this complaint. |
| **17. The type surface systematically uses implementation-universal types instead of mathematical codomains.** | `LEX-12`–`LEX-15` | Current source contains **238 `-> Parent`**, **16 `-> Element`**, **1 `-> CategoryObject`**, and **6 `-> Any`** return annotations: **261 framework-universal return annotations**. `LEX-13` explicitly names `Parent`, `Element`, `SageObject`, and `CategoryObject` as empty types that assert nothing. Examples include `Functor.object_image -> Parent`, set `cardinality() -> Parent`, arbitrary `an_object() -> Parent`, and scheme methods returning `Any`. |
| **18. Public coordinate/storage escape hatches remain and are actively taught.** | `ARC-18`, `API-02`, `DEV-40` | Lattice elements expose `to_list`, `to_tuple`, `to_vector` at `lattices.py:3057–3077`; tensor elements expose raw `components()`/`list()` at `tensor.py:381–404`; ordinary `ModuleMorphism.matrix()` remains a public coordinate view at `module_morphisms.py:655ff`. Explicit coordinate views can be legitimate at a narrow framing boundary, but the notebook actively uses them as ordinary mathematical interaction, so the semantic firewall is not functioning. |
| **19. The canonical notebook violates the notebook/session rules.** | `NB-01`, `NB-03`, `NB-04`, `ARC-07`, `LEX-10`, `DEV-40` | Of 51 code cells, **30 are currently unexecuted**. A committed cell retains a `NotImplementedError` traceback at `preamble.ipynb:802–822`. Markdown at `:1214–1216` says the algebra “should look like” a polynomial ring instead of asserting the claim. `:1254` states the exact substitution behavior only in prose. Session code uses `.generators()` (`1227`, `1269`), `A.Hom(P)` (`1239`), positional `P.gen(i)` (`1241`), bare global `Hom(...)` (`1267`, `1290`), low-level `module_homset`/`TensorAlgebraOf`/`DividedPowerAlgebraOf` around `977–980`, and `.hom(...)` for Coxeter diagrams around `1097`. The heading “Coxeter diagrams as Sage parents and their morphisms” (`1080`) is also implementation-centered rather than a mathematical question (`NB-03`). |

The generated megadoc predates some source changes. Its placement diagnostics
require regeneration at T before they can establish additional current findings.
Execution ordering and closure live only in [TODO.md](TODO.md).

### Sheaf theory on non-affine schemes stops at the chart

**Missing general mathematics.**
For a ringed space \((X, \mathcal{O}_X)\) the tree has sheaves as functors on a site with descent (`Sheaves(coverage, D)`) and now has module sheaves with represented finite-atlas inverse image and pullback.  The remaining constructions sheaf theory on a non-affine scheme is built from are:
the fibered category of modules over varying rings, whose arrows are semilinear maps;
the general projectivization functor, as distinct from the projective-space entry now used by linear systems.
Underneath, general module products and equalizers now exist at `Modules(R)`, and the module of compatible sections is their selected Čech equalizer with its universal cone retained. The unframed tensor quotient/classifier and the algebra of global sections now pass through the owned `Modules(R)` and `Algebras(R)` entries rather than alternate section parents.

**Dependency path.**
Sheaves on \(\mathrm{Open}(X)\) with descent → sheaves of modules over \(\mathcal{O}_X\) → quasi-coherent and invertible sheaves and their morphisms → line bundles, Cartier divisors and linear systems.
Gluing needs finite atlases, the glued-scheme entry, semilinear transitions and module limits.

**Observed evidence.**
Read from source at `d83d43c2` (gluing) and `cf26db85` (divisors), after both subtrees were rebuilt through their categories as far as these foundations allow.
The glued scheme and its Hom now use `Schemes(R)` through a private realization (`6faa74327`, `755c1250b`). Finite affine atlases are now objects of `FiniteAffineAtlases(X)`, a subcategory of the represented Zariski covering families in \(\mathbf{Sch}_R/X\); their refinements are covering-family morphisms, and module/algebra finite-atlas gluing data declare `DescentDataOnCover` on that coverage. Module-valued \(\Gamma(X,F)\) is the selected equalizer in `Modules(O(X))`, and algebra-valued \(\Gamma(X,A)\) is built on that module through its owned tensor square and the `Algebras(R)` entry; the former `GlobalSectionModules(R)` and `GlobalSectionAlgebras(R)` alternate owners are gone.
`QuasiCoherentSheaves(X).Invertible()` states the scheme-theoretic locally-free-rank-one property, with a separate chosen-trivialization data category. `QuasiCoherentSheaves(X).Mor` now uses the represented affine module map on affine schemes and the existing compatible chart-map Hom on a finite affine atlas; its line-bundle realizations reuse those descent maps, and projective/multiprojective restriction comparisons are pullbacks of ambient line-bundle maps in the same QCoh Hom/Core. `AffineQuasiCoherentAdjunction` is the shared `Adjunction`, with sheaf-valued unit and counit. The linear systems use the shared projective-space entry with construction-time data (`39062eadb`, `31cfd1ea4`).

**Existing partial capability.**
`Sheaves(coverage, D)` with `DescentEqualizer`, `DescentData` and the entry `Sheaves.object`; `ModuleGluingData(cover)` and `AlgebraGluingData(cover)`; `QuasiCoherentSheaves(X)` with the affine equivalence, invertible axiom and coverwise Hom; and the varying-ring module category used by finite-atlas transitions. Current main returns the distinguished-cover module/algebra sheaves through `Sheaves.object` (`6a16a08b0`, `62006ee37`), represents the affine structure presheaf on the affine slice (`dd72f722a`), retains exact Čech structure-sheaf descent presentations (`fa1593da9`), constructs `X.structure_sheaf()` through `Sheaves.object` with the universal descent comparison inverted at the module Hom owner (`79d2caa83`), represents finite-atlas inverse image and pullback as functors before scalar extension, constructs finite-atlas module-valued compatible sections through the `Modules(O(X))` limit owner, classifies the chartwise product of compatible algebra sections through the owned unframed tensor square, constructs represented line bundles through `QuasiCoherentSheaves(X).Invertible()` with chosen trivialization carried separately as data, and keeps affine/finite-atlas quasi-coherent morphisms as sheaf-endpoint arrows.

**Affected consumers.**
Glued schemes and their sheaves; line bundles on projective space and its subschemes; complete and imposed-multiplicity linear systems.

**Coverage boundary.**
Read from source; no session was run.
Whether Sage or Singular supplies any of the remaining constructions for the specimens in question was not surveyed. The required source review and repair are scheduled as `varying-ring-modules`, `sheaf-descent-threading` and `projectivization` in TODO.

## Workflow Papercuts

Add concrete observed workflow friction here under a descriptive heading, with the user action, expected behavior, actual result, owning boundary and example.
Use `DEV-59` for capture and resolution.
Foundational mathematical gaps belong above even when first noticed as an inconvenient method or notebook interaction.

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
