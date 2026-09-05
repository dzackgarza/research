# Preamble parallel work and ownership

This file owns scheduling, active claims, and current progress for the preamble work in the root TODO files.
[PORT_TODO.md](PORT_TODO.md) owns the mathematical requirements and source assessment.
[TODO-PRIORITIES.md](TODO-PRIORITIES.md) owns research priorities and the boundary with `sage-categories`.
Scheme foundations precede orbit applications. Work within those foundations follows the dependency graph below.

Contents: [workstreams](#workstreams), [parallel schedule](#parallel-schedule), [lock boundaries](#lock-boundaries), [claim and release](#claim-and-release), [active claims](#active-claims), [overall progress](#overall-progress).

## Workstreams

Paths in this section are relative to `src/dzack_research/preamble/categories/` unless stated otherwise.
A prerequisite means the named operation and its maps are available at a recorded commit.
It does not require completion of the whole supplying workstream.
The source assessment predates ongoing edits: each claimant must inspect the current implementation before selecting a remaining item.

| Stream | Work and first release | Prerequisites for that release | Principal edit locations |
| --- | --- | --- | --- |
| C — construction and inheritance | A needed algebra construction uses its underlying module's initialized arithmetic, presentation, and morphism operations. Bound each repair by its actual consumer. | Existing construction that exposes the missing inheritance; criteria in TODO-PRIORITIES. | `algebras/algebras.py`, `functors/algebra_modules.py`; common runtime paths below only when required. |
| R — local rings and ideals | Quotient-ring prime localization, local units, residue maps, and localized ideal operations. First specimen: the special fiber of `xy=t`, localized at `(x,y)`. | Existing quotient and ideal/module owners; request C only for an observed construction failure. | `rings/ring_foundation.py`, `rings/commutative_algebra.py`, `rings/commutative_ideals.py`. |
| M — exact modules over local bases | Presentation-based localized equality and vanishing, exact maps, fibers, annihilators, and local freeness. First release: localization detects a module killed by an inverted element. | R's denominator/unit contract for prime-local cases; finite-monoid presentation work can start against existing localization. | `modules/localizations.py`, `modules/framed/finitely_generated/finitely_presented_modules.py`, `modules/module_morphisms/module_morphisms.py`, `modules/pure/modules.py`, `functors/module_localization.py`. |
| P — relative algebra presentations | Quotients of quotients, parameter structure maps, scalar change, pushouts, and compatible underlying modules. First release: `xy=t` as an algebra over the parameter ring and its special fiber. | Existing presentations and module operations; C only where inherited structure fails. | `algebras/free_algebras.py`, `algebras/algebras.py`, `algebras/restricted_scalars.py`, `functors/algebra_scalar_change.py`, `functors/algebra_modules.py`. |
| D — differential and local criteria | Differential localization/base change, conormal maps, tangent/cotangent spaces, and supported smoothness/flatness criteria. First release: the differential/Fitting calculation for `xy=t` feeds its singular subscheme and stalks. | P for relative presentations; R/M for localized modules and fibers; S for geometric loci. Algebraic differential maps can precede the scheme connection. | `algebras/derivations.py`, `algebras/kahler_differentials.py`; M owns new Fitting/local-freeness algorithms. |
| S — affine schemes and families | Equations, successive closed embeddings, distinguished opens, fiber products, parameter morphisms, and their pullbacks. First release: the family `xy=t`, its special fiber, and the maps between them. | P's presentations and maps; R only for opens/stalks. A family morphism can precede a flatness result from D. | `schemes/schemes.py`, `schemes/affine_spec.py`, `schemes/ringed_spaces.py`. |
| G — covers, gluing, and sheaves | Restriction morphisms, overlaps, refinements, gluing, and sheaves of modules/algebras. First release: compatible local sections and module maps on a distinguished affine cover. | S's open immersions and coordinate pullbacks; R's localization maps; M's localized module maps. | `schemes/ringed_spaces.py`, `schemes/schemes.py`; claim new cover/sheaf files by exact path. |
| J — projective and toric charts | Graded localization and degree-zero charts; character/cocharacter modules, cone algebras, and overlap maps. First releases: projective standard charts, then an affine toric chart with its actual character module. | P for chart algebras; existing integer modules, module duality, graded algebras, and polytopes. G is needed to assemble charts, not to construct individual charts. | `algebras/graded_algebras.py`, `schemes/polytopes.py`; claim projective/toric files separately. Shared presentation changes belong to P. |
| A — group actions | Common categorical actions and equivariant maps, integrating existing G-sets and group modules. First release: the same action construction specializes to these existing categories. | Existing group/Hom/functor owners; C for changes to common categorical construction. | `group/g_sets.py`, `modules/group_modules/group_modules.py`, `functors/g_sets.py`, `functors/group_actions.py`, `functors/group_scalar_change.py`. |
| Q — scheme actions and quotients | Affine fixed ideals, supported invariant algebras, quotient maps, and freeness predicates with stated hypotheses. First release: an affine involution's fixed subscheme and quotient morphism. | A and S/P for affine work; G for gluing equivariant charts and global quotients. New invariant-module algorithms belong to M/A. | Claim scheme action/quotient files separately; shared `schemes/schemes.py` and `algebras/free_algebras.py` require their own locks. |
| V — line bundles, divisors, and cycles | Invertible sheaves, Cartier/Weil constructions, supported Pic/Cl calculations, local multiplicities, and intersections. First releases: a rank-one gluing datum; a principal divisor computed through local algebra. | G and M's local trivializations for invertible sheaves; R's local lengths/vanishing orders for multiplicities. Normalization, total quotient rings, and local factoriality extend R. | `divisors/`; claim line-bundle/cycle files separately. Ring algorithms stay with R, module/form algorithms with M or their existing owner. |
| B — relative Spec and branched covers | Algebra sheaves and relative Spec; cyclic cover multiplication, local equations, base change, and deck actions. First release: local cover algebras glue over a line bundle's trivializing cover. | P, G, and V's invertible sheaves; A/Q for deck actions; D for ramification calculations. Local cyclic algebras can precede gluing. | Claim relative-Spec/cover files separately; shared algebra multiplication and underlying modules require C/P locks. |
| L — completions and singularities | Local-base maximal ideals, supported adic completions, normalization, local singularity models, and formal/DVR families. First release: completion of a supported local polynomial quotient with its structural maps. | R's local rings; M for module completion; S for placing the result at a point/in a family. Topological disc families additionally need H's topology. | `rings/commutative_algebra.py` overlaps R; claim local-singularity files separately. |
| H — homological and topological invariants | Longer resolutions, Tor/Ext, geometric complexes, integral cohomology/cup products, Hodge data, cycle maps, and higher direct images in supported cases. First releases distinguish a supplied complex's cohomology from a scheme's constructed complex. | Existing exact module operations for supplied complexes; M for wider resolution regimes; G for cover-derived complexes; D for de Rham inputs; V for cycle sources. Topological models/comparison maps are separate inputs. | `modules/cochain_complexes.py`, `modules/dg_modules.py`, `algebras/cohomology_algebras.py`, `algebras/de_rham_algebras.py`, relevant functors; M owns shared kernel/resolution edits. |
| N — research notebooks | Use each released construction for explicit geometry, recording the required next operation. | Only the operations used by that notebook; follow its kernel and file ownership. | Exact files in `computations/notebooks/`; the live kernel is a separate shared resource. |
| F — framework development and transfer | `sage-categories` develops the replacement independently. Transfer one complete preamble dependency when its constructors, functors, and inherited operations are usable there. | Transfer criterion in TODO-PRIORITIES; record the upstream commit consumed. | Upstream development stays in `~/gitclones/sage-categories`. A transfer claims common runtime and every affected preamble leaf/consumer. |
| O — orbit and reflection applications | Extend the arithmetic applications in PORT_TODO after the geometry prerequisites needed by research. | Existing module/form/action owners and the particular required algorithms. | Exact lattice, arithmetic-group, Coxeter, or engine files selected for the construction. |

## Parallel schedule

**First allocations:** R, P, A, and H's supplied-complex work can proceed together when their declared paths are disjoint.
M can work on finite-localization presentation calculations alongside R; prime-local integration waits for R's released maps.
C repairs a named shared dependency when required. P and C serialize edits to algebra construction and its underlying-module functor.
N and upstream F can proceed throughout against the interfaces they actually use.

**After individual releases:** S consumes P's equations and maps while D develops differential comparisons.
J can construct chart algebras alongside S.
A permits Q's affine work once S's scheme maps exist.
G starts with S's distinguished opens and R/M's restriction maps.
S and G serialize their shared scheme files; separate files alone do not resolve changing coordinate-map contracts.

**After gluing and local module releases:** V, toric/projective assembly in J, global actions in Q, and geometric complexes in H can proceed together.
Their changes to G's shared sheaf/cover interfaces serialize.
B consumes V's invertible sheaves and G/P's algebra gluing; it need not wait for Pic/Cl computation or intersection theory.
L can extend a released local-algebra interface alongside these geometric consumers, but serializes with R in `commutative_algebra.py`.
Families begin in S; flatness comes from D/M, formal local models from L, and higher direct images from H.

**Transfer:** upstream F requires no preamble lock during independent framework development.
A preamble transfer pauses edits to its affected dependency chain, including C and the relevant mathematical owners.
Unrelated leaves and notebooks using a separate released checkout can continue.
O remains lower priority than the requested general geometry; it does not become a prerequisite for toric modules or cohomology lattices.

These are dependency releases, not whole-phase barriers.
A worker may use an already available operation immediately after inspecting its implementation and maps.
If the operation needs repair, return that repair to its mathematical owner and update the consumer's prerequisite.

## Lock boundaries

A workstream identifies mathematical responsibility. A lock reserves a concrete editing resource.
Lock the smallest complete set of paths needed for the next construction.
Use repository-relative file paths or directory paths ending in `/`; directory locks include all descendants and new files.
Two reservations conflict when their paths are equal or either directory contains the other path.
Renaming requires both source and destination reservations.

| Shared resource | Reserve together when changing its contract | Affected work |
| --- | --- | --- |
| Runtime category construction | `src/dzack_research/preamble/owned_category.py`, `owned_category_bases.py`, `refine.py` under that same root; exact affected files in `categories/abstract_categories/` and `categories/functors/core.py` | C/F; coordinate affected leaf constructors before resuming consumers. |
| Ring localization and ideal representation | The three R files in the stream table | R/M/D/G/V/L; R and L cannot independently edit their shared file. |
| Module presentations and exact maps | The M files in the stream table; add `modules/internal_hom.py`, `tensor_products.py`, `base_change.py`, or `functors/scalar_change.py` only when edited | M/D/V/H/A; shared algorithms have one writer. |
| Algebra presentations and underlying modules | The P files in the stream table | C/P/D/J/B/Q; constructor and morphism changes need a common released interface. |
| Affine schemes and restriction/gluing | The S/G files in the stream table | S/G/J/Q/V/B/L; serialize shared files, then narrow claims as distinct owners emerge. |
| Actions | The A files in the stream table; exact group/Hom files when needed | A/Q/B/O; reserve common abstract-category files separately. |
| Forms and lattices | Exact files in `categories/modules/framed/formed/`, `categories/forms/`, and the existing lattice owners | V/H/J/O; using their public operations needs no write lock. |
| Imports and generated documentation | Exact `__init__.py`/session entrypoints; `docs/preamble-megadoc.md` and `docs/preamble-graph.{json,dot,html}` as one generated set | All streams. One worker integrates exports and regenerates a coherent source snapshot. |
| Live notebook kernel | `kernel:<server>:<kernel-id>`, plus each edited notebook path | One worker changes a kernel's state at a time. Read/execution use follows the repo's japi rules. |
| Git index and work-board updates | The transaction mutex below | All workers sharing this checkout; commits and claim updates serialize. |

Ordinary source reading needs no reservation. Record the dependency commit used.
Use a `read` reservation when a live source snapshot must remain stable, such as megadoc generation.
Read reservations can overlap; a `write` reservation conflicts with either mode.
A shared-file lock alone does not stabilize an interface: record affected consumers and the release commit for contract changes.
On a shared checkout, pause affected consumers during that edit. Separate worktrees can read their pinned dependency commits.

## Claim and release

The authoritative live board is `/home/dzack/research/TODO-WORKSTREAMS.md` on this machine.
Every local worktree and clone participating in this preamble work uses this same board and mutex.
Their copied boards are snapshots. This local protocol requires coordination before adding writers on another machine.
Locks are cooperative reservations; `flock` makes board transactions mutually exclusive, not arbitrary filesystem writes.

Acquire the transaction mutex in a persistent terminal:

```sh
flock -n -E 75 /home/dzack/research/.git/preamble-coordination.lock bash --noprofile --norc
```

Exit 75 means another transaction owns it. Read the board and do independent work, then retry.
Keep that shell open while performing the following transaction; type `exit` to release the mutex.
The lock file remains in place. Process exit releases the OS lock; file deletion is unnecessary.
The shell/PTY must remain alive when an agent edits through another tool call.

**Claim:** under the mutex, reread this board and run:

```sh
git -C /home/dzack/research status --short
git -C /home/dzack/research diff --cached --name-only
git -C /home/dzack/research rev-parse HEAD
git -C /home/dzack/research worktree list
```

1. Select one concrete release in the workstream table and inspect its current dependencies.
2. Compare every intended path with active claims and existing uncommitted work.
3. Reserve all required paths together. If any conflict, acquire none; narrow the work or wait for release.
4. Add an active-claim row with a unique claim ID, task/session reference, checkout, exact paths/mode, base commit, and UTC update time.
5. Update that stream's progress row to name the claimed construction and its unmet prerequisite, if any.
6. Commit only the board change, then exit the mutex shell. Source editing can now proceed under the recorded reservation.

The durable claim remains active after the transaction shell exits.
Waiting for a dependency releases reservations that the worker cannot currently use.
Acquire additional paths through another all-or-nothing board transaction before editing them.
Two workers may claim one stream when their concrete releases and paths are disjoint and their interfaces are stable.

**Checkpoint/progress:** reacquire the mutex before staging or committing in the shared checkout.
Inspect the index first; preserve another worker's staged work and wait for its commit.
Commit only owned paths. Update progress with the resulting commit and the exact available operation or remaining gap.
Then release the mutex while retaining any active source reservations.
Use the repo's scope-specific verification rules; distinguish source inspection from execution evidence.

**Release:** stop writing the reserved paths and commit the owned source changes first.
Under the mutex, update overall progress and prerequisite release commits, then remove the active-claim row.
Commit that board update before releasing the mutex. Partial work records its remaining operation and stays incomplete.
A worktree result becomes available to shared-checkout consumers only after integration; record both commits where they differ.

**Handoff/recovery:** transfer a claim only after its owner stops editing and supplies the checkpoint and remaining work.
An old timestamp or a crashed terminal does not cancel a durable claim.
Check the referenced task, checkout, and uncommitted files before resolving an abandoned claim.
If ownership remains uncertain, preserve the reservation and ask the owner/user; unrelated claims can continue.
The UTC field records the latest claim, checkpoint, handoff, or release transaction. It is not a lease expiry.

## Active claims

| Claim | Stream / concrete release | Owner task/session and checkout | Reserved resources and mode | Base / checkpoint | Updated UTC |
| --- | --- | --- | --- | --- | --- |
| D-localized-differentials-20260905 | D — realize Kähler differentials of a represented localization as the localized source differential module and extend derivations to fractions | ChatGPT continuation `2026-09-05-localization-recovery`; `/home/dzack/research` | write: `src/dzack_research/preamble/categories/algebras/kahler_differentials.py`; `src/dzack_research/preamble/categories/algebras/derivations.py`; `tests/algebras/test_de_rham.py` | `1e43425fe7484f9b149c98b787aa72a78736224b`; R/M now supply exact localized fraction equality, ideal contraction, transported presentations, and localized Fitting ideals. Define `Omega^1_{S^{-1}A/R}` by the canonical base-change theorem `S^{-1}Omega^1_{A/R}`, retain the localization comparison through its source/unit metadata, and extend the universal derivation by `d(a/s)=s^{-1}d(a)-a s^{-2}d(s)`. | 2026-09-05T16:14:13Z |
| R-quotient-radical-20260905 | R — compute radicals of ideals in selected quotient presentations, restoring the denominator-radical witness consumed by localized-module equality | ChatGPT continuation `2026-09-05-localization-recovery`; `/home/dzack/research` | write: `src/dzack_research/preamble/categories/rings/commutative_ideals.py`; `tests/rings/test_commutative_algebra.py` | `3a3abf052fc5ccf84643b3132bec0cf4651d2ca5`; D exposed `Ann_A(dy)=(x^2)` for `A=k[x,y]/(xy)`, but `radical()` asks Singular to operate in Sage's quotient parent and fails before proving `x in sqrt(Ann(dy))`. Lift the ideal plus presentation relations to the selected polynomial cover, take the radical there, and descend it. | 2026-09-05T16:18:11Z |

### Existing work awaiting adoption

At setup, the checkout has uncommitted changes across ring, module, algebra, scheme, action, form/lattice, export-adjacent, and generated-doc owners.
Those changes belong to their existing workers; this board has not identified those workers or certified their completion claims.
Before a new claim, use the live `git status --short` output to identify its exact overlapping paths.
Treat every dirty path outside a recorded claim as reserved to an unidentified existing owner.
That owner can adopt the paths into a claim and checkpoint them, or explicitly hand them over.
Clean paths remain claimable when their interface dependencies are stable.
The whole pre-existing dirty tree was checkpointed as one commit on 2026-09-05; correctness is measured against the current tree, and a broad past reservation never blocks a stream whose files are idle.

## Overall progress

Update this table at each release or handoff. It records current usable results and the next missing construction.
Acceptance follows PORT_TODO's mathematical requirements; edit counts and completed administrative steps do not measure mathematical completion.
`Unclaimed` describes this board's ownership only; ongoing pre-adoption work can still exist.
Replace the initial source-assessment references with inspected implementation commits as workers adopt the streams.

| Stream | Current result / evidence | Next release or prerequisite | Claim state |
| --- | --- | --- | --- |
| C | `4b1786db`: constructor/refinement audit checkpointed with the regenerated 18,609-line megadoc; the production `refine()` census is property-only. The torsion constructor preserves the caller's owned base ring, so the public order-view `ZZ` is retained and the exact `FinitelyPresentedTorsionModules(ZZ)` / `TorsionModules(ZZ)` specimens pass 2/2 under the Sage pytest runtime. | No C prerequisite remains; downstream streams consume the released constructor/refinement substrate. | Released / complete |
| R | `8e4b7ae7`: represented quotient ideals compute exact module relations by lifting generators and defining equations to the polynomial cover; quotient Krull dimension and nested quotient computations use the same cover data. The `xy=0` origin is prime/maximal, its prime localization has the expected local units/maximal ideal/residue map, and finite/prime localization preserves algebra bases and validates external fraction denominators. `64755e6d`: `LocalizationRings.ParentMethods.localize_module()` restores the public ring-side module-localization dispatch through the owned localization functor. `84a15b05`: localization equality uses owned addition/negation for cross-products, explicit quotient lifts for quotient rings, and saturation of the selected exact coefficient presentation for finitely generated localizations. `70d7b363`: contraction of a localized ideal from a selected quotient presentation lifts the ideal, defining relations, and denominator product to the presentation ring before saturation; for `A=k[x,y]/(xy)`, localizing `(x,y)` at `x` now contracts to the unit ideal. In an isolated `HEAD` archive with only the claim applied, the ideal/localization regressions pass 3/3 and the full commutative-algebra file is 22 passed with only the four unrelated `Mor`/`Coproduct`/`Pushout` baseline failures. | No R equality or ideal-contraction prerequisite remains for the first D localization/Fitting release. The next blocker is M-owned Fitting/local-freeness transport over localized coefficients. | Released: `70d7b363` |
| M | `55c16f43`: represented finite-presentation localization has exact fraction equality and finite-generator vanishing from cyclic annihilators, retains the exact prime-localized module used by fibers, preserves `ModuleSubobjects` and their chosen inclusion through `ModuleLocalizationFunctor`, and transports kernels directly instead of recomputing an image over the localized ring. `65fe44e6`: selected Fitting ideals now commute with localization by extending the source Fitting ideal, so transported presentations need no second minor engine over `S^{-1}R`; for `Omega_{k[x,y]/(xy)/k}`, `Fitt_1=(x,y)` becomes the unit ideal after localizing at `x`. In an isolated `HEAD` archive, the prior six-test M/R localization gate plus the new Fitting regression pass 7/7. | The first D localization/Fitting release can now consume exact localized presentations and Fitting ideals. General local-freeness/projectivity and trivialization algorithms remain later M work. | Released: `65fe44e6` |
| P | `66466ec7`: relative `xy=t`, special fiber, and scalar-preserving successive algebra quotients. `86ed6a99`: free/presented pushout spans. `289d4756`: number-field algebras retain their field engine and chosen primitive presentation. S consumed the represented algebra maps at `7b40b82a`, where affine Spec/FiberProduct maps now preserve owned endpoints. The public ring-side quotient remains an explicit R prerequisite. | No P prerequisite remains for the first `xy=t` family/special-fiber scheme release; resume quotient/localization factorization when R releases presented-quotient ideals and local arithmetic. | Released: `289d4756` |
| D | Differential presentations and Fitting operations in PORT §8.4. | Localization/base-change comparisons, then S's singular subscheme. | Unclaimed |
| S | `d73b5709`: affine `Spec` carries an explicit scheme base and the affine-Spec cache distinguishes the coordinate-algebra/base-ring view. `dbef76cc`: the relative family `Spec(T[x,y]/(xy-t)) -> Spec(T)` and the closed point `Spec(T/(t)) -> Spec(T)` have a represented pullback; quotient base change realizes `A ⊗_T T/(t) ≅ A/(t)`, the special-fiber coordinate algebra satisfies `xy=0`, both square composites agree, and the owned slice category supplies its identity square. The claimed affine-scheme regression file passes 12/12. | The first `xy=t` family/special-fiber release is complete. Distinguished-open/stalk integration consumes R; later cover/gluing work consumes G. | Released: `dbef76cc` |
| G | Structure-sheaf local values in PORT §§8.4, 9.4. | Restriction maps and compatible affine/module gluing from R/M/S. | Unclaimed |
| J | Graded algebras and module-based polytopes in PORT §§8.4, 16. | Degree-zero projective charts and character-module toric charts. | Unclaimed |
| A | `0e25eedb`: the owned group algebra `R[G]` with group inclusion, augmentation, centre and Maschke; `Groups().group_algebra(R)` on subgroup inclusions. `2ddbfcb4`: group modules are `Modules(R[G])`, refining `GObjects(G, Modules(R))`; `GroupModules` retired. `d73b5709`: G-set vocabulary on `FiniteSets()`/`FiniteGSets(G)`; lattices with an action are `Lattices(ZZ[G])`. `5ad9314c`: `Modules(S)(M, rho)` from a ring morphism `S -> End(M)`; `Hom_R(S, -)` as `Modules(R).coextension_of_scalars(f)` for `S` finitely framed over `R`, with `Res_f -| Hom_R(S, -)`; the scalar-change triple spelled on `Modules(R)`. `bd7a44e8`: induction/restriction/coinduction are scalar extension/restriction/coextension along `R[H] -> R[G]`, recognized on the map and realized on a transversal; `Modules(R[G])(M, rho)` restricts a ring morphism along `G -> R[G]`. `fd12b070`: the trivial action, invariants and coinvariants are restriction, coextension and scalar extension along the augmentation `R[G] -> R`, taken as a ring morphism; the standalone adjunction functions left the session. `233963af`: restriction along `R -> R[G]` forgets the action, so `Res -| Hom_R(R[G], -)` along the structure map has its unit and counit; group modules multiply by group-algebra scalars. | `R[G].augmentation()` as an algebra morphism needs `R` placed as an algebra over itself (TODO.md witness). Coextension along `ZZ -> ZZ[x]` needs countable products of modules. Torsor membership and transporters; stabilizers as predicate subgroups; submonoids of `NN`/`ZZ`; the scheme specialization `GObjects(G, Schemes)` for Q. Known red: the two G-set adjunction tests in `tests/groups/test_group_adjunctions.py` (chosen preimage of the underlying-set functor) fail on `bd7a44e8` and before it. | Unclaimed |
| Q | Requirements in PORT §13.3. | Affine fixed ideals and invariant-algebra quotient maps from A/P/S. | Unclaimed |
| V | Module-valued divisor/Pic/Cl constructors in PORT §§8.4, 11. | Invertible sheaves from G/M; local divisor calculations from R. | Unclaimed |
| B | Module multiplication-to-algebra construction in PORT §§8.4, 13.2. | Compatible local cyclic algebras; global assembly consumes G/V. | Unclaimed |
| L | Principal-ideal completion and local examples in PORT §§8.4, 12, 15. | Supported local-quotient completion and structural comparison maps. | Unclaimed |
| H | `2845d8fe`: `Tor(n, M, N)` and `Ext(n, M, N)` green over ZZ and QQ[x]; internal Homs between presented modules are presented by their model; matrix spaces are free modules; the chosen free resolution is one object. | Functoriality of Tor/Ext in the resolved argument (chain-map lifting); `ext`/`tor`/`projective_dimension` methods on presented modules; longer resolutions beyond PIDs. | Unclaimed |
| N | Notebook work is independently owned by file and kernel. | Consume released operations; record missing ones at their mathematical owner. | Unclaimed |
| F | Independent upstream development; no upstream release is certified by this board. | Record the upstream revision and a complete consumer before claiming a preamble transfer. | External / transfer unclaimed |
| O | Existing arithmetic implementations and remaining PORT requirements. | Select after the general geometry required by research is usable. | Unclaimed |
