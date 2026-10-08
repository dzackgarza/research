# Issue 401: remaining implementation work

Issue 401 is unfinished. Continue the implementation in the priority order below.

## Target

Finish the research-side primitives required by the pinned `sage-indefinite-port` migration. Place each operation at its mathematical owner and compose its general construction, retaining all defining maps. The acceptance inventory is [the abstraction audit](docs/issue-401-abstraction-audit.md); the active node is [`indefinite-port-primitives`](TODO.md#indefinite-port-primitives).

Read `INTENT.md`, `AGENTS.md`, `CONTRIBUTING.md`, `TODO.md`, `COMPLAINTS.md`, and `docs/preamble-megadoc.md` before editing. The formal authority is `lean-categories`; correctness acceptance belongs to `lean-cas-dsl`. Research runtime checks establish engineering integration only. Formal requests run beside computational work.

## Priorities

Do the work in this order. Do not start a later step while an earlier step has ready work.

1. **Everything that `sage-indefinite-port` needs.** This includes the primitives in this file, the audit rows, and every preamble owner that those primitives depend on. Each item is a blocker for the port.
2. **Obvious mathematical errors and wrong placements.** Read the audit views as a mathematician:
   - `just category-graph constructions --select CATEGORY` shows the category of each construction's result.
   - `just category-graph properties` shows the properties that each category places on its objects.
   - `just category-graph routes --operation NAME` shows the routes to one operation.

   Read each line as a mathematical statement. A line that is obviously false is a defect. For example, an element of the power set of a finite set that is not placed in finite sets is a defect. Repair the placement at its owner, and file a TODO node when the repair is not immediate.
3. **Duplication.** Reduce duplicate implementations only after steps 1 and 2. A duplicate that blocks the port or causes a wrong placement belongs to the earlier step.

A defect that a check exposes in step 1 is the current unit: repair it at its owner before moving to the next check or row. A COMPLAINTS.md entry or a HANDOFF status line is the residue of that repair, committed with the code that makes it, never a commit on its own and never a substitute for the repair. File a TODO node instead only when the repair genuinely needs a prerequisite that is not yet built, and name that prerequisite.

A commit is not a stopping point. After banking a unit, take the next unchecked item under "Next checks" or "In progress" in the same turn, without re-reading the governing documents, and end a turn only when this file has no unchecked item left or a check is genuinely blocked on something outside the repository.

## In progress

The remaining unit is integration of the affine fibres, integral lift torsors, and generated orthogonal-group actions. The checkpoint includes shared-owner changes whose broader contracts still need review:

| Owner | Check still needed |
| --- | --- |
| `categories/group/groups.py` | **GroupExp targeted checks passed:** on the regular ZZ-module, the additive/multiplicative identification has inverse, preserves addition as multiplication and sends zero to the identity; on the regular module over `ZZ/(2)`, the inverse and order-two generator relation hold. **Generated-subgroup word witnesses repaired:** `GeneratedSubgroups.membership_decision(candidate,word=...)` evaluates the witness through the chosen free-group generators, proving membership of `g^2` and `g^-2` in `<g>` for `g=diag(2,1/2)` on `U_QQ`; unwitnessed membership returns `is_member(candidate,H)` rather than the native infinite matrix engine's false negative. Python's Boolean `in` raises on undecided membership. Other realizations remain to check. |
| `categories/modules/framed/formed/torsion_form_modules.py` | **Targeted check passed:** on the discriminant quadratic form of `U(2)`, `O(q)` has order two; the subgroup on its nonidentity generator has order two and admits both that generator and the identity. The subgroup on no generators has order one, admits the identity, and rejects the nonidentity generator. This verifies both positive and negative membership in the generated finite orthogonal-subgroup protocol. |
| `categories/modules/framed/finitely_generated/finitely_presented_modules.py` | **Targeted checks passed after `db2cbc6a80`:** the cokernel of the zero endomorphism on the regular module over the finite non-PID ring `ZZ/(4)` is finite (`is_finite()=True`); for the analogous finite presentation over the infinite non-PID ring `ZZ[x]`, `is_finite()` returns the unresolved proposition `is_finite(M)` rather than asserting a PID-dependent cardinality. |
| `categories/abstract_categories/products.py` | **Targeted checks passed:** the diagram of two distinct but extensionally equal `Sets().Mor(X,Y)` maps retains the exact left and right arrow objects, repeat construction reuses the diagram, and reversing the arrows gives a distinct diagram with the reversed images. The construction is keyed by arrow identity, as the retained universal diagram contract requires. |
| `categories/lattice_engines.py` | **Targeted check passed:** for Gram `diag(2,-4)`, bound 2 and primitive positive start `e`, the period map sends `e -> 3e+2f`, `f -> 4e+3f`, is invertible and preserves the form; the one-vector cycle is bounded. Zero/negative bounds return `None`, and nonprimitive/negative-square starts raise `ValueError`. The implementation was compared with `edgewalk_rank2.py` at frozen port commit `709f81a` (companion, promised step, shorter pair, reduction and period). Broader comparison of reduction-cycle specimens and the proof of the iteration contract remain open. |

These paths are relative to `src/dzack_research/preamble/`. Continue at these owners; the lattice consumer must not acquire duplicate implementations.

## Next checks

The following checks are pending. Obtain actual results before closing their obligations.

1. **Full integral lift kernel.** On `L=U + <2>`, let `R` be reduction along the first null basis vector and let `T=R.rational_lifts(R,id)`. For the reduction generator `a`, the parameterization at `a` must be integral and at `a/2` must fail integral descent. Check the parameterization's inverse. The difference between the lift at `a` and an integral base point must belong to the full integral kernel, even when the finite search uses the smaller period lattice `2ZZ*a`.
2. **Infinite orbit closure obstruction (checked).** On U, the group generated by `diag(2,1/2)` now rejects an invariant integral overlattice through the finite containing-bound argument, raising `ValueError` that the orbit-generated submodule leaves its containing bound. The selected generator's inverse belongs to the generated subgroup after `21cef09ae5`; the generated matrix-group path does not require a full indefinite orthogonal-group engine. Since U is unimodular, its only integral overlattice is itself, while the generator does not preserve U. General membership decisions for arbitrary words in infinite matrix subgroups remain a separate obligation.
3. **Signed vectors on a retained subspace.** Check `positive_vector()` and `negative_vector()` on a formed subobject of U: each vector must retain that parent, have the requested sign, and preserve its square under the inclusion.
4. **Split binary null vectors (checked).** The primitive null-vector family of U has cardinality four, is placed in finite sets, consists of square-zero vectors, and every member lies in the complete zero-square fibre (targeted Sage checks). The vector `2e` belongs to that fibre but not to the primitive family. Moreover `ne`, for each positive integer `n`, has content `n`, which is invariant under integral isometries; hence the complete fibre has infinitely many content orbits. Its runtime `is_finite` decision remains unresolved, rather than returning a false finite result. The earlier finite-family failure came from `PowerSets._from_finite_members` losing the explicitly finite domain's placement in the slice; repaired at the set owner in `6d996654d9`.
5. **Affine fibres and similarities beyond a selected point (targeted checks passed).** On the rational line along the first basis vector of U, the inverse-image fibre contains parameter 1 but not 1/2; its selected origin and the point at 1 have a nonidentity torsor difference, whose action sends the origin to the point. The generic G-object action no longer requires its group elements to be hashable (`027f70f811`). **Matrix fibre:** for the integral endomorphism `E(X)=X+X^t` on 2-by-2 matrices, extend `E` along `ZZ.fraction_field_map()` and intersect its rational solution fibre at `E(I)` using `E.domain().generic_fibre_map()`. The latter targets the restricted-scalars module of the extension, as required by the adjunction. The integral skew matrix `S=[[0,1],[-1,0]]` lies in the integral translation module; its nonidentity torsor difference acts on the selected origin to recover the translated point (targeted Sage run). The integral fibre's parameter module is the original integral matrix space, so its translation is `S`, not the image of `S` under the generic-fibre unit. **Similarity:** for `diag(2,1/2)` on U, `integral_similarity(U,U)` has `scale()=2`, `multiplier()=4`, and `index()=4` (targeted Sage run); `index()` reads the cokernel cardinality.

**Constant affine-image repair:** `AffineModuleFibres.image_point_set()` now retains a finite image of a zero-translation fibre by restricting its evaluation to a selected singleton (or the empty set). The full parameter fibre remains unchanged. On the constant line at zero in the rational span of `2ZZ*e + 3ZZ*f`, targeted Sage execution gives image cardinality one and image-translation rank zero. This repairs the previously undecided image cardinality of an infinite parameter fibre without identifying parameters with image points.

Use the actual Sage runtime:

```sh
direnv exec /home/dzack/research sage -c '<targeted specimen>'
```

Keep traceback output bounded with `traceback.print_exception(error, chain=False, limit=14)`. Targeted issue-401 execution is authorized. Full repository suites are not a substitute for these specific checks.

### Specimen construction details

- Use `ZZ.fraction_field_map()` and `L.base_change(...)` for the chosen rational extension. Construct isometries with `V.Isom(V)`. Use owned coefficients and `V.scalar_multiple(QQ(1)/QQ(2), v)`.
- For a rational matrix fibre with an integral intersection, construct the operator `E` over ZZ, then use `E.base_change(ZZ.fraction_field_map())`. Supply `E.domain().generic_fibre_map()` to `integral_members`. An independently constructed rational matrix parent is not the chosen scalar extension.
- Submodule generators with ordinal labels may print as `0`. Compare against `parent.zero()` and evaluate the retained inclusion; the printed label does not determine whether the vector vanishes.
- The frozen port source is available through `git -C /home/dzack/gitclones/sage-indefinite-port show 709f81a:<path>`. Its `references/port-design.md` is present at that revision even though it is absent from the current working-tree path.

## Closure work

- **Generated-word evaluation uses its universal map:** `GeneratedSubgroups.membership_decision(candidate,word=...)` now evaluates the word through the morphism from the selected free group to the containing group, rather than independently multiplying extracted letters. The `diag(2,1/2)` specimen confirms the correct word `t*t` proves `g*g` and the mismatched word for `g` remains undecided. This retains the generating map as the owner of word evaluation.

- **Generated-subgroup witness validation corrected:** an explicitly supplied free-group word is evaluated before any direct generator/identity membership shortcut. The word `t*t` certifies `g*g` for `g=diag(2,1/2)` on the rational hyperbolic plane, but does not certify `g`; the latter query retains its undecided `is_member` proposition when accompanied by the mismatched word. Direct membership of the selected generator remains `True`. This distinguishes positive subgroup membership from validity of the supplied witness.

- **Bounded signed shell and sphere specimens verified:** for Gram `[2]`, target one-half of the selected generator and square bound zero, multiplier one gives no shell, while multiplier two gives a singleton shell; for Gram `[-2]` at target zero, bound `-2` and multiplier one give the two-point sphere. Both returned multiplier and cardinality were checked in Sage. The shell's existing doctest had assumed that the framing label was the Python integer `0`; the documented construction now reads the selected generator label instead, in the same commit as this status update.

- Reconcile every audit row with the pinned migration contract, including return objects, failure cases, multiplier bounds, inclusions, and inverse maps. Resolve the remaining contract questions from the mathematical definitions and the recorded amendments.
- **Two-plane recovery repaired at the decomposition owner:** `two_hyperbolic_plane_splitting()` uses the integral hyperbolic index to decide existence, then searches integral null vectors exhaustively by increasing coordinate height when PARI selects one with divisibility greater than one. The genus criterion is exact for a lattice whose genus contains `2U`, by Nikulin's indefinite genus uniqueness theorem and `rank(L) >= length(A_L)+4`; the analogous bound after removing one `U` is `rank >= length(A)+2`. Targeted Sage checks passed on `U(2)+U+U`, a permuted Gram presentation, and a nontrivial integral basis change. The resulting isometry retains the original reduction-owned comparison maps and has a two-sided inverse. Broader frozen-port parity and independent acceptance remain open.
- Follow the group-consumer dependencies named in the TODO only where they remain necessary for the issue-401 contract.
- Update the audit, TODO, and relevant complaints. Their statements that every specimen remains unexecuted are stale. Separate pending engineering integration from formal comparisons and independent acceptance. Keep all still-required proof work at its existing owner.
- Complete the applicable formatting and targeted checks, commit coherent units, and follow the repository's synchronization rules. Do not mark the task complete from source inspection or a few successful specimens alone.

## Workspace boundary

Other work is active in this checkout. Preserve the unrelated changes under `research/`, the untracked research notes, and `tests/lattices/test_lattice_database_owner_contracts.py`. Recheck status before staging and stage exact task paths. Preserve concurrent commits. The port's `research-401-primitives` branch is outside this implementation unit.
