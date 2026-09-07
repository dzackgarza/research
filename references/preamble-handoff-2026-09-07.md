# Preamble cutoff handoff — 2026-09-07

The cutoff is the committed construction foundation through research `b67b35e3`.
It includes direct-action modules, additive endomorphisms, localized module actions, and the classifying category of a group.
The associated assertions are **unverified**.
The full preamble DAG remains open.

This file records the restart boundary and implementation findings.
[TODO.md](../TODO.md) remains the sole work queue and completion authority.
Its [DAG](../TODO.md#remaining-workstreams-as-a-dependency-graph),
[requirements](../TODO.md#mathematical-requirements), and
[edit locations](../TODO.md#edit-locations) retain their full scope.
Read [AGENTS.md](../AGENTS.md), [COMPLEXITY.md](../COMPLEXITY.md), and the
[construction design](preamble-architecture.md) before resuming.

## Restart boundary

The implementation workers have stopped and their source edits are committed.
The A0 and localized-M0 reservations are released with this handoff.
The next session must inspect current files and claim its exact edit paths again.
A candidate path set below is a proposed task boundary, not a continuing reservation.

Resume substantive implementation when continuation is requested.
The cutoff does not complete the full-programme goal or establish an external blocker.
The first unresolved shared construction is an equipped object whose forgetful image is the exact supplied module.
Two algebra products on that module must define two algebra objects.
Resolve this construction before converting the general algebra node.

The existing verification rule remains in force: construction and assertions are committed **unverified** until terminal T.
It also defers Sage execution, notebooks, QC, and generated megadoc surveys.
The two stated exceptions are selected tool provisioning and a short import check after integration.
The cutoff introduces no additional verification phase.

## Repository checkpoints

These are source checkpoints, not current mathematical acceptance claims.

| Repository | Checkpoint | Released source boundary |
| --- | --- | --- |
| `research` | `e472b85a` | Shared construction/refinement hooks; additive Hom and End; direct-action modules; forgetting to additive groups on objects and maps. |
| `research` | `78494432` | Endomorphism enrichment over the selected commutative scalar ring. |
| `research` | `d7aef49c` | `G.classifying_category()` and `ClassifyingFunctor(phi)` for group homomorphisms. |
| `research` | `41d239c0`, `dcdb3814`, `b67b35e3` | Localized fraction actions into additive endomorphisms; transported framing data through cooperative construction. |
| `research` | `70f17402`, `e2294760` | Persistent OSCAR calls through the actual Julia bridge; structured matrix conversion and engine initialization errors. |
| `research` | `785749ee` | Singular `modulo` for presented quotient kernels and their relations; native `lift` for inclusion. |
| `sage-julia-bridge` | `6625927cf72399ce124d118c16efea4065fdd161` | Bridge-owned Julia environment and Python dependencies. |
| `sage-categories` | `e59ab4f52032e48695e4bba352f079b5696ced72` | Relative bimodule tensor, maps, regular unit, associator, and unit comparisons on represented abelian groups. |

Sibling checkouts are `/home/dzack/gitclones/sage-julia-bridge` and `/home/dzack/gitclones/sage-categories`.
The latter has independent ongoing development.
Its observed HEAD at cutoff was `856a3dc`; the F release above is an earlier included commit.
Read the current upstream specifications before choosing a transfer.

The previous finite glued-quotient release `1847d9c1` is already integrated in research.
Its old Q reservation was released at `c5d37dc9`.
It supplies affine G-charts, descended quotient overlaps, descent squares, and affine-target factorization in its stated finite regime.
Its constructors still require reconciliation with the forthcoming A0/G contracts.

## Released module contract

The ordinary-module datum is the ring morphism into endomorphisms of an additive group.
The [module design](preamble-architecture.md#module-actions) states the mathematical boundary and its enriched generalization.

```python
Ab = AdditiveGroups().AdditiveCommutative()
E = Ab.End(X)
rho = Rings().Mor(R, E).elementwise(...)
M = Modules(R)(rho)

M.scalar_action() is rho
M.underlying_additive_group() is X
U = Modules(R).underlying_additive_group_functor()
```

The two-argument spelling `Modules(R)(X, rho)` checks these same endpoints.
`U` maps module morphisms to additive morphisms between the corresponding exact underlying groups.
The constructor stores the defining action before inherited initialization uses it.
The alternate binary-operation construction of `GeneralModules` must satisfy this same public contract.

The defining target is `End_Ab(X)`.
The regular module over `M_2(QQ)` distinguishes it from `End_R(M)`.
Pointwise addition defines additive Hom groups; composition defines endomorphism multiplication.
Right scalar action registration is restricted to commutative bases.

`AdditiveEndomorphismRings(S)` retains its selected commutative scalar ring `S`.
For commutative `R`, represented module endomorphisms can therefore retain their `R`-algebra enrichment.
Generic additive endomorphisms and the current noncommutative module-Hom construction receive integer enrichment.
The required enrichment over `Z(R)` remains M0 work.

The principal changed owners are:

- `categories/group/additive_homsets.py` and `categories/group/magmas.py`;
- `categories/modules/general_modules.py` and `categories/modules/pure/modules.py`;
- `categories/modules/module_morphisms/module_morphisms.py`;
- `categories/functors/module_additive_groups.py`;
- `owned_category.py`, `refine.py`, and `categories/abstract_categories/hom_categories.py`.

Paths in these owner lists are relative to `src/dzack_research/preamble/`.
`OwnedParent` and categorical Hom construction share initialization-hook state through nested refinement.
Category-owned data must be available before dependent hooks run.
Pass constructor-owned data through the cooperative constructor arguments that consume it.

### Localized modules

`categories/modules/localizations.py` now defines fraction scalar actions through additive endomorphisms.
The localization retains its source module and localization functor.
For a framed source, it transports the selected module generating set and its image map through constructor arguments.
For an unframed source, construction passes only the data accepted by that category chain.
This is a source release of the action and initialization boundary.
Further localization and scalar-change obligations remain in M0/M1.

### Next bounded M0 consumer

Inspect these existing constructors before adding any accessor:

- `categories/modules/framed/framed_free_modules.py`;
- `categories/modules/framed/finitely_generated/finitely_presented_modules.py`.

The free constructor already stores its base, labels, and basis map before inherited construction.
The presented constructor already stores its free cover and relation data before inherited construction.
Source inspection found no separate action override in those paths.
They may already inherit the released action contract.
The next task is to establish the actual constructor relationship and repair only a demonstrated gap.

Use `ZZ/6` as both a presented module and a direct-action module.
Give an explicit intertwining isomorphism between them.
Then use a free-plus-torsion module and an infinitely indexed free module with finite-support elements.
Their public action must be the action used for scalar evaluation.
These constructions exercise finite torsion, free parts, and infinite indexing without conflating their data.

Existing assertion owners include `tests/modules/test_general_module_through_the_module_graph.py`,
`test_cardinality_and_exponent_over_any_pid.py`, and `test_invariant_factor_framing.py` in the same directory.
Any new assertions remain **unverified** until T.

Selected presentations are the next higher-complexity M0 release.
Use the [existing framing design](../TODO.md#framed-designed-and-not-built) and
[presentation design](preamble-architecture.md#presentations-construct-the-action).
A selected presentation has commuting diagrams as maps.
Arbitrary linear maps on its free terms differ from maps induced by functions on framing labels.
The latter belong to a stricter framed-family construction.
Finite generation as a property supplies no chosen epimorphism.

## Released classifying category and next A0 construction

`categories/group/classifying_categories.py` realizes `BG` for an owned group.
`categories/group/groups.py` exposes the cached group-owned construction.
The following public usage is recorded in committed, **unverified** assertions:

```python
from dzack_research.preamble.all import Groups
from dzack_research.preamble.categories.group.classifying_categories import ClassifyingFunctor

G = Groups.C(4)
H = Groups.C(2)
g = next(iter(G.group_generators()))
h = next(iter(H.group_generators()))
phi = G.Mor(H)({g: h})

BG = G.classifying_category()
point = BG.an_object()
arrows = BG.Mor(point, point)
arrow = arrows(g)
arrow.group_element()
arrow * arrow
arrow.inverse()
arrows.identity()

Bphi = ClassifyingFunctor(phi)
Bphi(point)
Bphi(arrow)
```

`ClassifyingFunctor` uses the explicit import above.
The group determines the unique object, and its elements determine the arrows.
Composition, inverse, and equality use the group operations.
The construction applies without enumerating the group.

### A0 acceptance and implementation order

The next object is `GObjects(G, C)(F)`, where `F` is an actual functor `BG -> C`.
Its underlying object is evaluation at the unique object of `BG`.
Its equivariant maps are natural transformations.
The general functor and natural-transformation owners already exist in `categories/abstract_categories/cat.py`.

`FunctorCategory` currently expects an object with `arrow().functor()`.
Its morphisms expose `transformation()`, `component()`, and `naturality_square()`.
`Functor` checks exact endpoints for morphism images and records provenance.
Use these contracts when replacing the current action datum in `group/g_objects.py`.

1. Construct actions and equivariant arrows through the existing functor-category machinery.
2. Put represented action construction on the supplied category `C`, using its category-owned specialization.
3. Implement restriction along a group homomorphism by precomposition with `ClassifyingFunctor(phi)`.
4. Implement transport along a functor `C -> D` by postcomposition, including nonidentity arrows.
5. Convert group modules to actual modules over the group algebra and adapt their scalar restrictions.

The proposed dispatch method is `C._construct_group_action(G, X, action)`.
Dispatch belongs to `C`, since one parent can support several mathematical structures.
Sets, modules, and schemes supply their represented constructions at their respective owners.
A category-owned action-category construction lets schemes retain their quotient operations.
Move the generic action owner's scheme quotient and cyclic fixed-locus methods to the scheme subtree.
Retain the distinction between abstract-group actions and group-scheme actions.

General naturality is a defining mathematical hypothesis.
Finite or represented specializations own applicable decidable checks.
The [construction design](preamble-architecture.md) records the separate Ab-enriched formulation for ring modules.
An ordinary multiplicative action alone does not supply scalar additivity.

### The group-algebra parent is part of A0's next release

`modules/group_modules/group_modules.py::_equip_action` currently constructs an `R`-module with additional category placement.
Its construction uses an `R`-free or `R`-presented parent while also declaring `Modules(R[G])`.
The next release must return an actual `Modules(R[G])` parent with base ring `R[G]`.
Its defining action is `R[G] -> End_Ab(X)`.

Retain a selected `R`-presentation on the restricted `R`-module along `R -> R[G]`.
The original relation matrix describes that restricted module.
Induction, coinduction, invariants, coinvariants, and scalar change must consume that module and its maps.
`action_of(g)` acts on the retained original `R`-module.
This also preserves the mathematical expectation in `tests/constructions/test_groups_construct.py`.
That expectation file remains read-only.

The generic `Modules` constructor should obtain any group-algebra category specialization from the ring owner.
The specialization must construct the fundamental action through the shared module path.
Ordinary scalar restriction also needs repair at `functors/scalar_change.py`:
restriction along `f:S -> R` retains the exact additive group and uses `rho_M compose f`.
The current `RestrictedScalarsModuleView` is a source boundary to inspect during this conversion.

First A0 specimens:

- `C2` acting on a two-point set, with the equivariant swap map;
- restriction along the non-inclusion `C4 -> C2`;
- transport through the free-module functor, including a nonidentity permutation map;
- the sign action on `QQ`, with multiplication by two as an equivariant map;
- `Modules(R[G])(M, action_callable)` producing the actual group-algebra module and its scalar restriction.

Candidate A0 write paths, relative to the preamble root:

```text
categories/group/g_objects.py
categories/group/g_sets.py
categories/group/groups.py
categories/group/classifying_categories.py
categories/abstract_categories/objects.py
categories/sets/set_categories.py
categories/modules/pure/modules.py
categories/modules/group_modules/group_modules.py
categories/modules/group_modules/group_lattices.py
categories/algebras/group_algebras.py
categories/rings/ring_foundation.py
categories/functors/group_actions.py
categories/functors/group_induction.py
categories/functors/group_scalar_change.py
categories/functors/scalar_change.py
categories/schemes/schemes.py
categories/schemes/quotients.py
```

The only A0 source edits delivered at cutoff are the classifying-category file and the group accessor.
The action conversion above remains implementation work.
Its assertion owner is `tests/groups/test_categorical_group_actions.py`.

## C/P: the exact underlying-module construction

The first P specimen needs two algebra structures on one exact supplied module.
Refining that module in place cannot represent both structures at once.
Reconstructing a finite presentation changes the forgotten object and restricts the mathematical construction.
The shared equipped-object construction must settle this boundary.

Inspect the upstream Magmas equipped-object construction and its full dependencies.
Also inspect the existing preamble category construction for an equivalent usable owner.
Choose the construction that preserves the exact supplied object, structure morphisms, and maps.
If a framework transfer is selected, transfer the complete dependency path required by this specimen.
This choice was unresolved at cutoff; a P-local module representation is not a released design.

The falsifiable acceptance is two distinct algebra products on `M`, both forgetting to `M`, with the appropriate nonidentity maps.
Use this specimen to settle the construction before broad algebra edits.
This is shared C/P responsibility, scored 100.

### P's resulting algebra interface

The [algebra design](preamble-architecture.md#multiplication-and-algebra-axioms) supplies the mathematical definitions.
For commutative `R`, construct `Algebras(R)(M, m)` from `m:M tensor_R M -> M`.
An inferred spelling `Algebras(R)(m)` can recover the same endpoints.
The object exposes its exact `underlying_module()` and `multiplication_morphism()`.
Its module action is the supplied module's action.

Associativity, a chosen unit with its equations, commutativity, and the Lie identities have their own category refinements.
The unit route accepts `eta:R -> M` and gives unit-preserving morphisms.
The associative unital central-map route accepts `R -> Z(A)` and constructs the same algebra/module data.
`AssociativeAlgebras(R)` denotes the associative refinement.
`CommutativeAlgebras(R)` retains its associative unital commutative meaning.

The current queue also names `WithChosenMultiplication`.
Reconcile that interface with the mandatory multiplication datum at the general algebra node.
Retain the queue's requirement until the delivered construction resolves its role.
Selected presentations remain additional data even when multiplication is fundamental.

The common algebra Hom preserves multiplication:
`f compose m_A = m_B compose (f tensor f)`.
The unital Hom also preserves `eta`.
Lie morphisms use the common multiplication-preserving Hom.
General laws remain mathematical hypotheses; finite-table algorithms retain their stated effective scope.

The commutator functor changes multiplication to `m - m compose swap`.
Its source requires associativity, while a unit is unnecessary.
For noncommutative bases, use the required bimodule and relative monoidal structure.
The arbitrary left-module tensor over a noncommutative ring does not supply that construction.

P's first mathematical consumers are:

- the associative unital algebra `M_2(QQ)` and its commutator Lie algebra on the same module;
- a nonidentity conjugation map transported through the commutator functor;
- a characteristic-two Lie multiplication satisfying alternation and Jacobi;
- the Cartan inclusion into `sl_2(QQ)`, whose Lie cokernel is zero.

The last consumer distinguishes a Lie-ideal quotient from the dimension-two linear cokernel.
Universal constructions must use their categorical owner even when evaluation reuses module operations.

### P write boundary and shared edits

Candidate paths, relative to `src/dzack_research/preamble/`:

```text
categories/algebras/algebras.py
categories/algebras/associative_algebra_morphisms.py
categories/algebras/lie_algebras.py
categories/algebras/augmented_algebras.py
categories/algebras/free_algebras.py
categories/algebras/graded_algebras.py
categories/algebras/restricted_scalars.py
categories/algebras/sparse_free_algebras.py
categories/abstract_categories/hom_categories.py
categories/group/additive_homsets.py
categories/functors/algebra_modules.py
categories/functors/commutator_lie_algebras.py
categories/functors/algebra_scalar_change.py
```

Assertions belong in `tests/algebras/test_general_algebra_structure.py` and `tests/algebras/test_lie_algebra_structure.py`.
They remain **unverified** until T.

Coordinate these additional edits with A0's owner:

| Shared owner | Required relationship |
| --- | --- |
| `modules/pure/modules.py` | Endomorphism algebras retain their selected scalars and associative unital placement after the general-node conversion. |
| `algebras/group_algebras.py` | `R[G]` uses the common multiplication constructor, its group-identity unit, and explicit associative unital placement. Retain framing, augmentation, and relative presentation. |
| `functors/group_induction.py`, `group_scalar_change.py`, `scalar_change.py` | Functor endpoints distinguish general algebras from associative unital algebras. |
| `rings/ring_foundation.py` | Ring-owned algebra endpoints retain the intended associative unital meaning. |

The candidate `OwnedCategoryMixin` export in `abstract_categories/objects.py` is already present.
P source edits had not started at cutoff.

## Existing candidates to consume selectively

The worktree branches are source inputs, with their original requirements retained in the
[earlier handoff](../TODO.md#handoff-2026-09-06).

| Candidate | Reusable source | Remaining construction work |
| --- | --- | --- |
| `work/algnode`, `57465081` | General-node split and supercategory changes in the algebra, augmented, free, and restricted-scalar owners. The Hom packet filtering is already on main. | Exact underlying-module construction; independent unit refinement; general multiplication; common algebra/Lie Hom; actual commutator structure; graded/sparse placement; scalar-change endpoints; selected End enrichment; Lie universal constructions. |
| `work/discgroup`, `cdf80a75` | Stable category ordering using the Sage flag, declared depth, and qualified category name; replacement for initialization-order dependence; owned-category changes for subobjects, root lattices, and ringed spaces. | Reconcile with current shared construction and resolve the recorded subobject-Hom recursion. Its ordering change is not a completed C release. |

The full `work/algnode` candidate still builds general multiplication through finite module presentations and recovers units algorithmically.
Those source paths do not satisfy the general P construction above.
Read the candidate by mathematical owner and integrate only the relevant construction.
Preserve other worktrees and their owners during adoption.

## E and F continuation

### Existing engine owners

Research's OSCAR adapter remains in `categories/lattice_engines.py`.
It uses persistent `Julia.call` with structured matrix input/output.
The bridge owns its environment under `src/sage_julia_bridge/julia_env/`.
Its `Project.toml` requires JSON major version 1 and Oscar exactly `1.7.1`.
The tracked nested `Manifest.toml` realizes that dependency selection.
The bridge's `mrdi.py` and wire-format documentation require that Oscar serialization version.

The bridge's `just install` installs into the Python interpreter selected by the actual Sage launcher:

```bash
uv pip install --python "$(sage -c 'import sys; print(sys.executable)')" -e .
```

Use it from the bridge repository when provisioning is needed.
Python dependencies include the declared Pydantic dependency.
The root-level untracked Julia project files in that checkout belong to pre-existing work.
The bridge-owned environment is the nested tracked one.
Startup and the required mathematical OSCAR operations remain **unverified** until T.

The polynomial-presentation kernel implementation is in
`categories/modules/framed/finitely_generated/finitely_presented_modules.py`.
It uses Singular's native `modulo` for the quotient kernel and its relations, then `lift` for the inclusion.
Future E tasks follow an actual consuming construction and its owned return maps.

### Relative bimodule tensor in sage-categories

The F release changes `src/sage_categories/algebra/abelian.py` and its package export.
`AbelianBimoduleTensor(R)` returns the selected monoidal structure on represented `(R,R)`-bimodules.
The tensor descends the outer actions; maps use `relative_tensor_morphism`.
Its unit is the regular bimodule.
The associator and inverse descend through the relative tensor mediators.
The unit maps use the existing relative unitors.
The cached `relative_tensor` construction preserves its selected projection across consumers.

The underlying abelian tensor now accepts free and mixed Smith presentations.
Its representation still requires retained Smith-coordinate presentation data.
General realization in arbitrary abelian groups remains F work.
This release therefore supports its represented consumer and is not a complete preamble framework transfer.

Upstream already has `Modules(A, actegory)(rho)` with action, forgetful, homomorphism, transport, and restriction operations.
Read its live specifications, including chosen-data diagrams and relative monoidal constructions.
The general algebra transfer requires its complete construction path.
Independent upstream Cat/kernel and static-projection work continued through the cutoff.
Coordinate ownership before editing those paths.

## Remaining DAG execution

Use the [workstream table](../TODO.md#workstreams) for exact inputs, scores, and full acceptance conditions.
An edge consumes the particular released construction; it does not wait for every item in the upstream stream.
Previously recorded releases retain their stated hypotheses and must fit the current shared contracts.

| Next release group | Construction to advance | First required consumer |
| --- | --- | --- |
| C, M0, A0, P | Exact defining data, selected structures, module actions, functorial group actions, and common multiplication. | The concrete module, action, and two-product algebra specimens above. |
| A1 | Group-module restriction, extension, coextension, induction, invariants, and coinvariants through the released scalar-change owners. | A nonidentity representation map with exact underlying scalar restriction. |
| R and M1 | Local rings/ideals and exact local module algorithms through their existing presentation owners. | The local algebra of `xy=t`; localization killing `QQ[x]/(x)` when `x` is inverted. |
| S and D | Relative Spec, base change, differentials, Fitting loci, and supported local criteria. | `xy=t`, its special fiber, and the structural maps determining its relative nonsmooth locus. |
| H0 and G | Chain-map lifting, derived module operations, covers, refinements, and scheme/module/algebra gluing. | A nonidentity induced Tor/Ext map; compatible local maps glued through actual overlaps. |
| J0 and J1 | Projective and toric chart algebras, followed by their glued schemes. | Degree-zero standard charts and toric face-localization maps. |
| V0, Q0, Q1 | Invertible sheaves and affine/glued action quotients through the new G/A0 contracts. | Local trivializations and section maps; quotient factorization across a represented cover. |
| B0 and V1 | Relative Spec, cyclic covers, divisors, cycles, and linear systems. | The scheme of a glued finite cover algebra and its structural map; divisor/section comparisons. |
| B1, L, H1 | Branch/ramification geometry, completions, singularities, and geometric cohomology comparisons. | Ramification from differential data; a completed local quotient with its comparison map; maps on geometric cohomology. |
| Y and I | Families, blowups, quotient geometry, and ADE/log-pair applications. | The particular family or pair consuming the released cover, divisor, singularity, and diagram objects. |
| O0, O1, X | Form/lattice ownership, finite discriminant and gluing maps, arithmetic groups, and reflection algorithms. | Actual form/subobject maps, then the selected arithmetic application; external port operations only where required. |
| E, F, N | Engine integration, complete framework transfers, and research use on their selected inputs. | The actual owned construction and its maps; notebook execution follows the standing policy. |
| U, then T | Complete transfers, consolidation, remaining archive coverage, then final mathematical execution. | Surviving exported constructions meet the original detailed requirements and immutable expectations. |

Geometry remains the scheduling priority over independent arithmetic applications.
The detailed archive requirements remain in TODO's ownership map and checklists.
This restart map does not replace them or declare a stream complete from a single specimen.
The terminal phase executes the required assertions and repairs failures at their mathematical owners.
Generated megadoc and graph surveys require the permitted execution boundary.

## Worker assignments and shared-file discipline

The following are suitable next assignments under [COMPLEXITY.md](../COMPLEXITY.md).
Choose from the models actually available in the next session.

| Assignment | Score | Model / effort used or suitable here | Ownership condition |
| --- | --- | --- | --- |
| Orchestration and exact C/P equipped-object construction | 100 | Astra / max | Own the shared constructor choice and the first exact-module specimen. |
| A0 functors and actual group-algebra module conversion | 95 | Astra / max | Reserve its complete coupled constructor/scalar-change path. |
| P algebra conversion after the shared construction | 90 | Sol / max | Coordinate A0's shared module/ring/action files before edits. |
| Bounded free/presented M0 constructor consumer | 55 | Terra / high | Escalate the score if shared presentation semantics require redesign. |
| A settled engine adapter or native algorithm integration | 35–50 | Terra / high; Luna for the lower settled range | Keep the existing bridge and mathematical return owner. |
| Complete upstream framework construction | 100 | Astra / max | Coordinate the live upstream writer and transfer full mathematical dependencies. |

At cutoff, `/root/construction_contracts` used Astra/max, `/root/engine_review` used Terra/high,
and `/root/framework_alignment` used Sol/max.
All have stopped.
Their conclusions are incorporated in the concrete restart boundaries above.

There were four available concurrency slots including the orchestrator.
Allocate workers to independent mathematical owners, then serialize shared-file edits.
One useful first wave has a foundation owner, an A0 owner, and a bounded M0/E owner.
Start the P conversion after the shared equipped-object construction is released.
If A0 needs the same core constructor, coordinate that dependency before its source edits.
Mechanical changes with predetermined targets belong to symbolic tools.

Use TODO's [claim and release procedure](../TODO.md#claim-and-release).
The shared-checkout coordination mutex is `.git/preamble-coordination.lock`.
Acquire it for claim transactions and staging/committing; inspect the live index while holding it.
An example held shell is:

```bash
flock -n -E 75 /home/dzack/research/.git/preamble-coordination.lock bash --noprofile --norc
```

Exit 75 means another transaction owns the mutex.
The held shell owns the lock until it exits.
Commit only the exact owned paths after checking the staged index.
Preamble work and this cutoff record use the prescribed hook-skipping route, `git commit --no-verify`.
Preserve unknown changes and resolve their ownership before editing them.

### Concurrent work at cutoff

These observations describe the cutoff, not permanent reservations:

- Research had an untracked `.semgrepignore` from another writer.
- The bridge had pre-existing root-level untracked `Project.toml` and `Manifest.toml`.
- Upstream had modified `.ai-review-ci/sage/normalize-common.log`, `sage-mypy.diagnostics.log`, `sage-mypy.log`, and `sage-syntax.log`.
- Upstream source changes seen earlier had reached its separate `856a3dc` checkpoint by this observation.

Reinspect all three repositories before claiming work.
Research's cutoff is a red checkpoint; assertion execution remains deferred to T.
Inspect sibling remote refs separately when adopting their recorded implementation commits.

## Assertion locations for terminal T

All assertions listed here are **unverified** in this release.

| Assertion owner | Mathematical claim |
| --- | --- |
| `tests/categories/test_owned_construction_contracts.py` | Defining-action modules, noncommutative regular action, distinct actions on one additive group, forgetting composition, and selected scalar enrichment. |
| `tests/groups/test_categorical_group_actions.py` | `BG` composition, identity, inverse, and the classifying functor of the non-inclusion `C4 -> C2`. |
| `tests/modules/test_localized_module_vanishing.py` | Localized module vanishing and its defining additive action. |
| Upstream `tests/algebra/test_abelian_tensor_scaffold.sage` | Free and mixed Smith-presentation tensor constructions. |
| Upstream `tests/algebra/test_bimodule_tensor_monoidal_scaffold.sage` | Relative bimodule tensor, structural maps, triangle/pentagon, and a nonidentity factor-swap automorphism for a noncommutative example. |

The immutable expectation subtrees remain `tests/constructions/`, `tests/user_simulations/`, and their shared `tests/conftest.py`.
Read their contribution rules before using them at T.
They measure the implementation against the mathematical expectations.
Source inspection and committed assertions at this cutoff do not establish their runtime results.
