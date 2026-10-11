# Issue 401: remaining implementation work

Issue 401's research-side primitives are complete. Continue the remaining
mathematical placement and ownership work in the priority order below.

## Target

The research-side primitives required by the pinned `sage-indefinite-port` migration have been delivered at their mathematical owners, retaining their defining maps. The acceptance inventory is [the abstraction audit](docs/issue-401-abstraction-audit.md); [`indefinite-port-primitives`](TODO.md#indefinite-port-primitives) is closed and the active source audit is [`placement-audit`](TODO.md#placement-audit).

Read `INTENT.md`, `AGENTS.md`, `CONTRIBUTING.md`, `TODO.md`, `COMPLAINTS.md`, and `docs/preamble-megadoc.md` before editing. The formal authority is `lean-categories`; correctness acceptance belongs to `lean-cas-dsl`. Research is general mathematics: each operation is accepted by true assertions about pure mathematics at its owner. There are no integration tests, and no consumer gates research. Formal requests run beside computational work.

## Priorities

Do the work in this order. Do not start a later step while an earlier step has ready work.

1. **Everything that `sage-indefinite-port` needs.** This includes the primitives in this file, the audit rows, and every preamble owner that those primitives depend on. Each item is a blocker for the port.
2. **Obvious mathematical errors and wrong placements.** Read the audit views as a mathematician:
   - `just category-graph constructions --select CATEGORY` shows the category of each construction's result.
   - `just category-graph properties` shows the properties that each category places on its objects.
   - `just category-graph routes --operation NAME` shows the routes to one operation.

   Step 2 is about methods placed on the wrong categories, and methods that do not place their results in the correct category. No tool can determine this automatically: read the code and think about the mathematics. The views help you see it; they do not decide it.

   Read each line as a mathematical statement. A line that is obviously false is a defect. For example, an element of the power set of a finite set that is not placed in finite sets is a defect. Repair the placement at its owner, and file a TODO node when the repair is not immediate.

   Step 2's completion is measured against one list: run the complete `constructions` and `properties` views once, read every line, and write each false statement as an unchecked item under "Step-2 false statements" below. Then repair down that list. Inspecting an edge that turns out correct, validating arguments, and rejecting malformed inputs are not step-2 items and are not progress on it.
3. **Duplication.** Reduce duplicate implementations only after steps 1 and 2. A duplicate that blocks the port or causes a wrong placement belongs to the earlier step.

   Step 3's completion is measured against one list, as step 2's was: run `just refactor-survey --view duplicates` (and its same-name survey) once over the whole preamble, writing to a file, read every group, and write each genuine duplicate implementation of one mathematical operation as an unchecked item under "Step-3 duplicates" below. Identical bodies or names alone do not establish identical mathematics; judge each group. The whole survey is listed before the first consolidation; then consolidate down the list at the operation's owner.

A commit is not a stopping point. After banking a unit, take the next unchecked item under "Next checks" or "In progress" in the same turn, without re-reading the governing documents, and end a turn only when this file has no unchecked item left or a check is genuinely blocked on something outside the repository.

Step 1 is complete: `indefinite-port-primitives` is accepted on true mathematical assertions at each owner. Nothing in research waits on `sage-indefinite-port`; how the port consumes these operations is its own concern. Step 2's 36-item denominator and Step 3's fixed 18-item denominator are complete. The three descendant source pieces in the steward chain are closed. The earlier bounded `placement-audit` closure is superseded by the steward's 2026-10-11 owner-pass split. The parent now Needs all 641 canonical category-owner passes: the original 633 plus seven actual unit/semiring providers and the finite-magma-generation axiom reconciled in the source closures below. The existing twenty completed ring-owner passes remain closed. `Magmas.Unital`, `UnitalMagmaMor`, its fixed-category construction, and `Monoids.Commutative` are also closed. The complete nonunital semiring owner, its Commutative refinement, its Mor and fixed-Mor construction, OwnedSemirings and OwnedRngs are now closed as well: 43 complete passes and 598 unchecked. The required pending consumer changes were banked separately; a consumer repair closes its whole owner only after the full inventory and actual arrow path are discharged. The current bounded consumer reviews retain their outstanding mathematical obligations inside their existing nodes. `placement-owner-adelogpairs` is now closed on its full owner and selected-cover source assertions. The complete OwnedGroups pass and the new Magmas.FinitelyGeneratedAsMagma provider are also closed. The complete Algebras pass is now closed on its exact scalar datum, weaker operation homes, centre and arrow assertions. The complete AbelianGroupEndomorphismRings pass is now closed on the canonical End carrier, pointwise arithmetic, integer action and admitted-point assertions. The complete AbsoluteGaloisGroups pass is now closed on its exact stages and base maps, mixed element laws, inherited character arrows and finite-quotient assertions. The complete AbsoluteGaloisGroupsOfFiniteFields pass is now closed on inherited topological generating families, q-power Frobenius, and unknown-safe all-points family evaluation. The complete AdditiveEndomorphismRings pass is now closed on its retained scalar datum, canonical identity, law-preserving arithmetic suppliers and exact full-versus-structured Hom carriers. The complete AdditiveGroups root pass is now closed on its existing right-difference operation, primitive suppliers and actual additive-monoid Mor inheritance. The complete AdditiveGroups.AdditiveCommutative pass is now closed on the general notation-conversion home, exact commutative realization, actual additive Mor and undecided equality. The complete commutative-additive Mor-family pass is now closed on both its enriched additive arrows and its coherent inherited functor-category endpoints. The complete root additive-group Mor-family pass is now closed on automatic inverse preservation, literal weaker-Mor reuse and both actual arrow levels. The complete AdditiveMagmaMor pass is now closed on its actual generated arrows, shared canonical identity and weaker set-map composition. The current first literal ready row is `placement-owner-additivemagmas`. The parent closes only after every owner pass and final inventory reconciliation. Normalization/coefficient-data work retains its existing obligations. M1 source work remains open. The module-specific `normalization-quotient-coefficient-dimension` node and the finite affine piece of `normalization-extensions-retain-coefficients` are now closed. Its five public operations have moved to their mathematical owners and consume the actual normalization module and coefficient map. Known infinite dimension now also survives a selected finite field restriction at the existing module and field-basis owners. The finite-localization source piece is now closed with its actual module, maps, component survival and finite-annihilator transport. The admitted finite-localization coefficient presentation now supplies the shared dimension and preimage routines, closing the remaining nonzero cusp coefficient calculation. The complete PrimeLocalizations category pass is now closed: its local/residue operations inherit their actual owners, its selected maps and lazy datum remain coherent, and its field/dimension decisions keep their true hypotheses. LocalizationRings has now closed its whole operation/ancestor/arrow pass, including its final cardinality and fraction equality/admission work; the independent Local refinement pass is also closed. General nonfinite computations and the remaining category-survey obligations stay required.

**Step-3 owner cleanup:** The two selected finite Noetherian ideal-family algorithms (`finite_primary_decomposition` and `finite_associated_primes`) now share the private engine-to-owned-ideal family ingress. Their distinct mathematical definitions and applicability checks stay at their public owners. No changes to general nonenumerated loci.

**Step-3 binary ideal cleanup:** `CommutativeIdeals` now centralizes the repeated base-ring compatibility check, selected engine ingress, and owned-ideal result construction for ideal sum, product, and intersection. Their three distinct public operations retain their respective ring-theoretic calculations.

**Step-3 quotient-ideal cleanup:** `CommutativeIdeals.colon()` and `ideal_saturation()` share one private quotient-presentation transport path: lift both ideals to the cover, compute their distinct ideal operations, and descend the result. Their PID and nonquotient branches remain separate and unchanged.

**Step-3 PID ingress cleanup:** The same two operations now share the owner-local principal-generator ingress for their PID branches. Their quotient arithmetic and saturation iteration remain mathematically distinct.

**Step-3 ideal-property ingress cleanup:** Primality and maximality checks share the same quotient-cover ideal selection. Their distinct prime/maximal criteria remain separate, including the selected number-field and multivariate polynomial cases.

**Step-3 engine pair ingress cleanup:** Sum, product, intersection, colon, and saturation now reuse compatible engine ideal-pair ingress on their selected backend routes. This changes no mathematical operation or quotient-cover handling.

## Unit-owner source closure (2026-10-11)

**Closed nodes:** `placement-owner-magmas-unital`,
`placement-owner-unitalmagmamor`, and
`placement-owner-unitalmagmamorcategoryconstruction`. The substantive owner
and Mor definitions were banked together in `194e5bad284a`; this source closure
also repairs successive evaluation of their induced unit-group consumer.
The seven newly authored unit/semiring providers now each have exactly one
TODO row and one parent edge. Unreviewed complete owners remain unchecked.

**Owner and complete delta.** `Magmas.Unital` introduces `_MorCategory`, display
naming, the selected `one`, `_unit_decision`, and `is_unit`. Its strict owned
ancestors are exactly `Magmas`, `Sets`, and `Objects`: respectively a binary
multiplication, a set, and the mathematical root. Their definitions and the
complete introduced operations were read. Only the unital owner uniformly
supplies both multiplication and the selected two-sided unit. The relocated
predicate means `exists y: x*y=1 and y*x=1`; the realization returns True,
False, or that exact proposition. No unspecified decision becomes False.

`UnitalMagmaMor` adds no operation body. Its laws are preservation of the
binary product and the selected unit, with no associativity premise. It
inherits `MagmaMor` construction/identity, `MagmaMorphism` composition, and
`CategoricalMor` admission and generated-arrow operations. Its construction
introduces only `fixed_category_class() -> UnitalMagmaMor`, using the existing
fixed-endpoint interning. The complete actual arrow walk was read:
`MonoidMor -> UnitalMagmaMor -> MagmaMor -> SetMorCategory`; the generated
provider collection follows the fixed-Mor supergraph. Exact endpoint identity
and the declared stronger-Mor path govern existing-arrow reuse. A plain
multiplicative constant-zero map on the integers is not an existing unital
arrow. Constructing an arrow from a callable declares the requested laws as
premises; it does not prove those laws for arbitrary input data.

**True closure assertions.** On the rational vector space with basis
`1,a,b,c`, extend multiplication bilinearly, make `1` a two-sided unit, set
`ab=ba=ac=ca=1`, and make all other products among `a,b,c` zero. Then `b != c`
are both two-sided inverses of `a`, `(ba)c=c != b=b(ac)`, and `ab=ac` with
`b != c`. Thus the existential unit predicate is meaningful and true outside
associative monoids/rings, while uniqueness and unit-implies-regularity fail.
The generic predicate may remain represented rather than Boolean; this is
not a claim to have supplied a nonassociative inverse algorithm. The unit
itself has inverse itself. Identity preserves product and unit, and for
unital maps `f,g`, `(g*f)(xy)=g(f(x))g(f(y))` and `(g*f)(1)=1`.

For composable monoid maps `f:M->N`, `g:N->P` and an admitted `u` of `M^x`,
`U(f)(u)=f(u)` and `U(g)(U(f)(u))=g(f(u))=U(g*f)(u)`. The repaired evaluator
retains the source-unit premise supplied by its fixed group-arrow domain;
it delegates ambient admission to the retained monoid arrow instead of
reconstructing the intermediate predicate facade. It therefore preserves
this equality even when the ambient predicate for `f(u)` is undecided. The
literal unit-group endpoints and the generated group arrow are retained.

**Sources and phase.** Mathlib's
[unit definitions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Units/Defs.html),
[unit-map laws](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Units/Hom.html),
[unital magma-map laws](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/Defs.html),
and [regularity definition](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Regular/Defs.html)
were read against the source contracts. The displayed algebra is an explicit
independent separating calculation. This closes the complete M1 source
assertions, not a runtime claim: literal constructor, identity, composition,
and undecided-predicate evaluations remain retained under T. No Sage/import,
QC, build, or consumer-repository gate was run. Whole `Monoids`, rings,
algebras and groups are not closed by this record.

## Commutative-monoid square-class source closure (2026-10-11)

**Closed node:** `placement-owner-monoids-commutative`.
**Owner and delta:** `Monoids.Commutative` introduces precisely display naming,
`an_object`, the category-level square-class functor and the parent-level
square-class group. The definitions of all seven strict authored ancestors were read:
`Monoids` (associative multiplication with a selected unit), `Semigroups`
(associative multiplication), `Magmas.Unital` (a selected two-sided unit),
`Magmas.Commutative` (commuting multiplication), `Magmas`, `Sets`, and `Objects`.
The construction needs the commutative monoid's abelian group of units and
no additive law; the old commutative-ring home was too narrow.

For a commutative monoid `M`, write `Q(M)=M^x/(M^x)^2`. Squaring is a group
homomorphism, its image is a subgroup, `[u][v]=[uv]`, and `[u]^-1=[u]` because
`[u]^2=1`. The complete quotient implementation in `rings/square_classes.py`
was read, including equality, identity, order, hashing, admission, retained
ambient data, projection, and functor maps. `Q(M).monoid()` now retains the
exact `M`; the legacy `ring()` accessor only applies when that object is a
ring. Projection and source-unit admission explicitly use `M.unit_group()`.
The quotient no longer overrides its own group-of-units operation with the
source group: that inherited operation belongs to `Q(M)` itself.

**Actual arrow inheritance and assertions.** Commutativity adds an object law,
so this owner's fixed Mor is literally the inherited `MonoidMor`, with its
`UnitalMagmaMor -> MagmaMor -> SetMorCategory` providers. Identity and
composition preserve the unit and multiplication. A monoid map `f:M->N`
induces `[u] |-> [f(u)]`: `f(u)` is a unit, and `f(v^2)=f(v)^2`, so this is
well-defined. `Q(f)(projection_M(u))=projection_N(f(u))`,
`Q(id_M)=id_Q(M)`, and `Q(g*f)=Q(g)*Q(f)`. The implementation keeps the literal
quotient endpoints and calls its protected class constructor only with the
unit premise already established by admission, multiplication, projection,
or the retained monoid-map laws.

The represented nonring monoid `ZZ.unit_group()` witnesses the new home:
its units are `{1,-1}`, its squares are `{1}`, and its square-class group is
`C2`. Independently, for `M=C4`, `Q(M)=C2`; therefore the ambient object of
`Q(M).unit_group()` is this `C2`, not the original `C4`. Both statements are
true without any ring structure. Equality of `[u]` and `[v]` is the exact
square predicate for `uv` (equivalently `u/v`); an unavailable decision stays
an owned proposition, and an unavailable order or membership computation
reaches its named assertion. A constant hash within the fixed quotient is
compatible with all mathematically equal classes.

**Consumer disposition and phase.** The existing lattice square-class callers
continue to use the same object/functor operations and retained projection.
The source search found no external caller of the removed erroneous source
`unit_group()` accessor. The group-law and functor assertions above close this
complete M1 source pass; their executable instances remain under T. No Sage,
imports, tests, QC or build was run. This record does not close the independent
whole `Monoids` or `OwnedGroups` passes.

## Semiring/rng owner source closure (2026-10-11)

**Closed nodes:** `placement-owner-ownednonunitalsemirings`,
`placement-owner-ownednonunitalsemirings-commutative`,
`placement-owner-nonunitalsemiringmor`,
`placement-owner-nonunitalsemiringmorcategoryconstruction`,
`placement-owner-ownedsemirings`, and `placement-owner-ownedrngs`.
The semiring source and NN placement were banked in `7c532f342b`; this
closure supplies the required inherited additive-arrow result correction.
It does not close the independent ring or algebra owner passes.

**Complete introduced inventories.** In `categories/rings/semirings.py`:

| Owner | Complete direct operations and suppliers |
| --- | --- |
| OwnedNonUnitalSemirings | `_MorCategory`, naming, example, supercategories; `_reducedness_decision`, `is_reduced` |
| Its Commutative refinement | naming, example; `_nilradical_decision`, `nilradical`, `_krull_dimension_decision`, `krull_dimension`, `prime_ideal_locus`, `minimal_prime_locus`, `_finite_minimal_primes`, `minimal_primes`, `irreducible_component_locus` |
| OwnedSemirings | `_MorCategory`, example, supercategories, `initial_object`, `initial_morphism`; `_dual_numbers_construction`, `dual_numbers`, `_characteristic_decision`, `characteristic` |
| OwnedRngs | `_MorCategory`, example, supercategories; `_ideal_generated_by`, `ideal` |
| NonUnitalSemiringMor | no new operation bodies; stronger additive/zero/multiplicative laws with inherited construction, identity and composition |
| Its category construction | `fixed_category_class` selects `NonUnitalSemiringMor` |

The definitions of the complete authored up-sets were read. Put
`B={Objects, Sets, Magmas, Semigroups, AdditiveMagmas,
AdditiveMagmas.AdditiveCommutative, AdditiveSemigroups, AdditiveMonoids}`.
These supply, successively, objects, sets, multiplication and its
associativity, addition and its commutativity/associativity/zero. The strict
up-set of OwnedNonUnitalSemirings is exactly B (8 owners); its commutative
refinement adds OwnedNonUnitalSemirings and Magmas.Commutative (10).
OwnedSemirings adds OwnedNonUnitalSemirings, Monoids and Magmas.Unital (11);
OwnedRngs instead adds OwnedNonUnitalSemirings, AdditiveGroups and
AdditiveGroups.AdditiveCommutative (11). Nonunital semirings impose both
distributive laws and absorbing zero, semirings further select one, and rngs
further require additive inverses. Generated joins are not new authored
owners. The fixed-category constructions inherit the read
`MorCategoryConstruction -> _MorCategoryOf` mechanism; their mathematical
category is MorCategories, over Cat.

**Placement and true assertions.** Positive powers and zero define reducedness
without a unit or additive inverses; no weaker declared ancestor supplies all
of this multiplicative-zero structure. In the commutative refinement, if
`a^m=b^n=0`, distributivity shows `(a+b)^(m+n-1)=0`, and multiplication by any
ambient element preserves nilpotence. Thus nilpotents form an ideal here;
commutativity cannot be dropped (the two off-diagonal nilpotent matrix units
in M2(QQ) sum to an invertible matrix). The prime/minimal-prime loci are
subsets of the exact object's full power set, not a finite-generator proxy.
Their `V(p)` images retain actual minimal-prime subsets and may be infinite.
Dimension is the supremum of prime-chain lengths, including -infinity for
an empty spectrum and +infinity when unbounded. No unsupplied finite bound is
asserted. NN, outside rings, has nilpotent set `{0}`, and `{0}` is prime.
These are mathematical propositions; the generic NN suppliers may retain
them without a Boolean or computed ideal representation.

The unique unital semiring arrow `NN -> S` is `n |-> n*1`; distributivity
proves its multiplicativity. The source uses the selected zero/one/addition
and retains the literal NN and S endpoints. For NN dual numbers,
`(a,b)(c,d)=(ac,ad+bc)`, and `epsilon=(0,1)` is central and square-zero.
Characteristic records the natural-number kernel: the zero semiring has
characteristic 1; if no positive multiple of one vanishes it is 0. In the
Boolean semiring characteristic is 0 although `1+1=1`, so characteristic
zero does not imply injectivity of NN's map. Rng ideals instead are absorbing
additive subgroups: in the nonunital rng 2ZZ the ideal generated by 4 is 4ZZ.
This is a true witness outside unital rings; an absent represented ideal
algorithm reaches the declared ideal-construction assertion.

**Actual arrows and required repair.** Generated providers follow the actual
fixed-Mor supergraph. NonUnitalSemiringMor reaches MagmaMor and
AdditiveMonoidMor, then AdditiveMagmaMor/SetMorCategory. The commutative
refinement reuses that fixed Mor. SemiringMor also reaches MonoidMor and
UnitalMagmaMor; RngMor instead reaches AdditiveMor from its abelian additive
ancestor. Endpoint identity and the actual stronger theory govern reuse.
The constant-zero endomap of NN preserves addition, zero and multiplication,
but not one; it belongs to the nonunital theory, not the unital theory.

The inherited additive arithmetic had incorrectly constructed its results
back in RngMor. For `f=id_ZZ`, `(-f)(1*1)=-1 != 1=(-f)(1)(-f)(1)` and
`(f+f)(1*1)=2 != 4=(f+f)(1)(f+f)(1)`. Sums and negatives are additive maps,
not generally rng maps. The shared `_pointwise_mor` now retains a declared
additive enrichment when present and otherwise selects the actual additive
Mor with the same endpoints. Addition, negation, subtraction and integer
action use it; the existing linear refinement remains the linear Mor.
Composition is unchanged and still preserves the stronger rng theory.
An operand must already belong to the selected additive Mor: the set map
`q(n)=n^2` supplies no additive premise and is refused by addition/subtraction.
Indeed `(f+q)(2)=6 != 4=2*(f+q)(1)`. Constructor admission is not used to
manufacture that premise. Common-Mor comparison now admits an already
stronger rng arrow instead of falsely rejecting it solely by its parent.
Finite comparison uses conjunctions; an undecided infinite comparison stays
its exact owned proposition.

**Sources, consumers and computation boundaries.** The complete semiring and
final additive-owner files, the current ring suppliers, NN placement,
fixed-Mor/generated-provider routes, and existing additive/linear/endomorphism
consumers were inspected as source. Mathematical definitions are checked
against Mathlib's
[ring/semiring laws](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Defs.html),
[nonunital and unital morphisms](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Hom/Defs.html),
and [characteristic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/CharP/Defs.html).
The explicit separating calculations above are independent assertions.
Nilradical representation, prime-chain dimension, finite minimal-prime
computation, central dual-number construction, characteristic computation,
and rng ideal generation each retain their named selected-supplier boundary.
Nothing turns an unavailable algorithm into a negative predicate. These are
complete M1 source closures; executable constructor/arithmetic/unknown cases
remain under T. No Sage, imports, tests, QC, build or consumer gate was run.

## ADE log-pair owner source closure (2026-10-11)

**Closed node:** `placement-owner-adelogpairs`.
**Owner and delta:** the complete ADELogPairs inventory, its seven strict
authored ancestors, and both selected AT21 realization suppliers were read.
Scheme affineness now belongs to Schemes; the toric supplier decides it
from the fan and retains an unknown zero-ring predicate. Toric log-pair
codimension zero belongs to ToricLogPairs. The polygon invariant family
belongs to ConvexPolytopes, with rational normalized volume and the relative
lattice measure in lower dimension. ADE wrappers select their retained
geometric data and reuse those owners.

**Complete introductions and mathematical data.**

| Surface | Complete introduced operations and their retained data |
| --- | --- |
| ADE category | `an_object`, `_call_`, `at21`, naming and `super_categories`; construction selects an admitted type, polygon, point and side data |
| ADE parent views | `base`, `is_base`, `is_cover`, `dynkin_letter`, `dynkin_rank`, `letter`, `rank`, `dynkin_variant`, `variant`, `is_affine_type`, `coxeter_diagram`, `dynkin_diagram`; these inspect the selected ADE datum |
| ADE polygon views | `polygon`, `polygon_vertex_order`, `vertices`, `distinguished_point`, `p_star`, `polarizing_polytope`, `side_decorations`, `ade_svg`, `_repr_svg_`, `integral_invariants`; the invariant computation delegates to the polygon |
| ADE geometric constructions | `_blue_rays`, `distinguished_boundary_points`, `blue_divisor`, `blue_line_divisor`, `complementary_divisor`, `pyramid`, `cover_toric_threefold`; these use the selected point and polygon to choose the boundary and height-two pyramid |
| AT21 base supplier | Initialization/representation; `base_pair`, `scheme`, `toric_scheme`, `complementary_divisor`, `source_variant`, type/rank/affine-type/polygon/point/side/diagram/pyramid/threefold views; `branch_divisor_class`, `branch_line_bundle`, `branch_section_space`, `branch_section`, `full_newton_branch_section`, `branch_newton_polygon`, `source_normal_form_section`, `branch_subscheme`, `branch_log_canonicity`, `double_cover` |
| AT21 cover supplier | Initialization/representation; `base_pair`, `cover_base_scheme`, `branch_section`, `branch_subscheme`, `ambient_toric_threefold`, `ambient_polarizing_divisor`, `ambient_hypersurface_section`, `scheme`, `ambient_projection`, `ambient_open_immersion`, `ade_pair_condition`, `_cover_structure`, `cover_morphism`, `local_cover_map`, `deck_involution`, `local_deck_involution`, `ramification_subscheme`, `boundary_subscheme`, `pulled_back_boundary`, `base_boundary_subscheme`, `boundary_divisor`, `log_boundary_coefficient_ring`, `log_boundary_divisor`, `equipped_pair`, `dynkin_diagram`, `polarizing_polytope`, `local_surface_equation`, `local_surface_singularity`, `local_global_singularity_comparison` |

The strict chain is ToricLogPairs (toric scheme with invariant boundary),
LogPairs (scheme with chosen boundary), Schemes (scheme over the selected
Spec R), LocallyRingedSpaces (local stalks), RingedSpaces (structure sheaf
of rings), SheafedSpaces (space with a chosen sheaf), and Objects. Their
actual definitions were inspected. SheafedSpaces has no authored Sets or
TopologicalSpaces edge. ToricSchemes is a retained realization supplier,
not an ancestor of ToricLogPairs. The ADE type, point and side choices are
not uniformly supplied by any strict ancestor, so their specific views and
the constructions that require them stay here.

**Correct hypotheses and preserved input.** The low-level polygon constructor
and the AT21 entry now share the admitted shape range. The branch-pair
enhancement has the precise characteristic-zero-field hypothesis; the
polygon constructor remains available over general admitted rings. Rank and
exponent ingress uses the existing exact integer boundary, refusing 3/2
before conversion to a Python integer. Owned coefficients use their actual
ring ingress, while raw engine numerals cross the existing numeral boundary.
No coefficient is discarded merely because its zero predicate is unknown.

The selected branch divisor is a representative of a linear-equivalence
class, not a claimed literal equality with twice the complementary divisor.
The D/E source normal form retains coefficient +1 on x^2*y^2. The zero section
is not an effective branch divisor. A general nonzero branch equation gives
a hypersurface with its separate represented log-canonicity proposition;
construction does not declare that proposition True.

**Actual projection and arrow inheritance.** Let P be the pyramid over Q
with apex (p*,2). A neighborhood of the apex has a maximal normal cone whose
height projection covers the entire base cocharacter space. Thus the full
normal fan does not give a toric map V_P -> Y. The open U obtained by deleting
only that apex maximal cone, and retaining its proper faces, does map to Y.
Its inclusion in V_P uses the identity lattice map. The ambient section has
apex coefficient one, so its local coefficient is a unit on the deleted
orbit and the hypersurface misses that orbit scheme-theoretically.

The construction retains V_P, its divisor and its section, restricts the
actual Cartier coefficients to U through the inclusion's chart pullbacks,
and cuts out X chartwise. It does not ask an incomplete fan for the existing
complete-fan global-section algorithm. Its arrows are X -> U -> Y with
literal endpoints. The cover's `base_scheme()` again inherits Spec R;
`cover_base_scheme()` identifies Y and is used by the local-equation
consumer. These two bases are mathematically distinct.

Schemes selects the common SchemeMor category, through its locally ringed
space fixed-Mor construction. U's glued presentation selects
_GluedSchemeMorCategory. The retained inclusion lambda is passed through
that constructor to SchemeMorCategory, which evaluates it at the canonical
fixed H and returns the resulting arrow literally after requiring parent H.
The lambda's `toric_morphism` constructs ToricSchemeMorphism in that same
endpoint-cached H. Consequently `chart_target` and `chart_pullback` remain
on the selected inclusion; no generic arrow conversion erases them.
ToricSchemeMorphism inherits SchemeMorphism. The deck action and the glued
cover maps likewise reuse the actual common scheme/gluing arrow providers;
ADE introduces no private competing Mor theory.

**True closure specimens retained under T.**

- The toric affine shapes D6, E7 and E8 are admitted; affine A and E6 have no
  represented toric polygon. Affine D4 has a diagonal/conic boundary, so is
  outside this torus-invariant-boundary representation. Primed A1 and the
  represented primed D4 row are excluded; primed A2 and D6 are admitted.
  Primed A4 has right vertex (3,0).
- A2 right-short has selected side lengths 2,1; left-short has 1,2.
  Finite E8 has two length-one sides. Affine D6 and E7 have one length-four
  selected side, and affine E8 one length-three side. Side data are computed
  from all actual sides through p*, including the affine side's interior.
- Geometric affineness is independent of Dynkin naming. The toric affine
  line over QQ is affine and the toric projective line is not; both are
  outside ADELogPairs. A toric log pair on P1 has codimension zero in its
  retained toric scheme. A multi-cone toric scheme over a nonzero ring has a
  nonaffine field fiber; over the zero ring it is empty and affine.
- The rational triangle (0,0),(1/2,0),(0,1/2) has normalized volume 1/4 and
  area 1/8. The integral diagonal segment (0,0),(1,1) has relative normalized
  volume 1 and ambient area zero. The unit lattice square has normalized
  volume 2, area 1, four lattice points and no interior lattice points.
  These assertions witness the polygon owner outside ADE.
- For pure finite E8, the retained origin-chart equation is
  z^2+x^2*y^2+y^3+x^5+c0. Setting c0=0 and c0=1 gives different sections
  and Newton polygons. With c0=1 the origin does not lie on the hypersurface.
  The equation operation preserves the selected constant and every other
  branch coefficient.
- On each semigroup character (m,h), the deck pullback multiplies by (-1)^h.
  Squaring gives the identity; base characters have height zero, so
  pi*iota=pi. The boundary is the scheme-theoretic pullback of the selected
  base boundary. The apex monomial divisor on U is twice its positive-height
  base-facet prime; restricting that prime gives divisorial ramification R,
  locally z=0. It excludes the possible isolated deck-fixed points. The
  short A2 case separates R from the entire fixed subscheme.
- X.base_scheme() is Spec R; X.cover_base_scheme() is Y. The structure map
  ends in Spec R and the cover map ends in Y, with the same coefficient base.
  Admitted sections retain unknown coefficient equalities; a Newton support
  computation asks for those exact zero decisions instead of guessing.

For the actual diagonal section z^2+y^3+x^5, the gradient ideal has quotient
basis x^i*y^j, 0<=i<4, 0<=j<2. It is supported only at the origin, so the
existing global Jacobian calculation gives the correct local mu=tau=8.
For z^2+x^2*y^2+y^3+x^5, the gradient also vanishes at
(x,y,z)=(-45/8,-675/32,0), where the equation has value x^5/6 != 0.
A global Jacobian dimension therefore cannot be substituted for the local
Milnor dimension at the origin. The operation retains the actual equation
and names the needed localization algorithm. No hard-coded different germ
or unsupplied coordinate change is returned.

**Sources and remaining computation boundaries.** Shape limits, linear
equivalence, branch conditions and the distinction between ramification
and isolated fixed points were checked against Alexeev--Thompson,
[ADE surfaces and their moduli](https://arxiv.org/pdf/1712.07932v3),
Definitions 2.1 and 3.2, Lemma 3.4, Tables 1, 4 and 5, and Theorem 5.9.
The explicit projection, character action, polytope measures and gradient
calculations above also give independent separating proofs. Affineness uses
[Stacks 01S5](https://stacks.math.columbia.edu/tag/01S5) and the single-cone
criterion for toric varieties. The selected polytope measure follows
[Sage's exact volume contract](https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/polyhedron/base7.html).
General branch log canonicity, undecided Newton support, relative-volume
backend availability and localized singularity computation remain named
frontiers in the same owner; they create no prerequisite node. The complete
source assertions and selected constructor/Mor routes are closed. Executable
instances remain under T: no Sage, imports, tests, QC or build was run.

## Group owner and finite magma-generation source closure (2026-10-11)

**Closed nodes:** `placement-owner-ownedgroups` and the newly authored
`placement-owner-magmas-finitelygeneratedasmagma`. The original unit-functor
consumer was banked in `eccba97e91`. This commit closes the complete group
owner, including its selected arrow and subgroup consumers, and reconciles
the new axiom provider as its own completed pass and parent dependency.
The independent group refinements and Mor-category owner passes remain
unchecked.

**Complete direct inventory.** All of OwnedGroups through the start of its
Commutative refinement was read, together with its selected native/free/
general arrow providers and the actual consumers below.

| Introductions | Mathematical data and disposition |
| --- | --- |
| Native constructor catalogue | C, S, A, D, Dic, Q, V4, Abelian, Artin, Braid, Cactus, PureCactus, Weyl, Reflection, RightAngledArtin, classical matrix/projective groups, Heisenberg, affine/Euclidean/semimonomial, nilpotent/small, reflection/sporadic/transitive and Rubik groups retain their existing defining data and owned engine crossings; Free and Coxeter retain their specialized constructions |
| Category construction | `an_object`, `Mor`, `_MorCategory`, `_EndCategory`, `_IsoCategory`, naming and `super_categories` retain Grp and literal fixed endpoints |
| Structural functors | `group_algebra(base_ring)`, `abelianization`, `abelianization_adjunction`, `underlying_set` retain Grp as their stated domain and the actual selected functor maps |
| Category properties and suppliers | `FinitelyPresentedAsGroup` retains a group-presentation property; `FinitelyGeneratedAsMagma` moves to Magmas with its matching axiom; categorical product/coproduct suppliers retain their actual cones, cocones and maps |
| Element operations | `inverse`, `cyclic_subgroup`; unit, unit-inverse and regularity computations supply the weaker monoid/magma contracts; the optional cyclic-cardinality supplier reuses the native order algorithm when one exists |
| Resolution data | `has_selected_group_resolution`, `has_selected_finite_group_generating_set`, `selected_group_resolution`, `group_generating_set`, `group_generator_morphism`, `group_generator`, `group_generators`, `number_of_group_generators` retain the exact selected resolution |
| Action and map data | `invariant_overlattice`, `conjugation_morphism`, `classifying_category`, parent `Mor` and `_Hom_` retain the group/action data and actual arrow endpoints |
| Predicates and counts | Finiteness, abelianity/commutativity, finite generation/presentation, arithmeticity, topological-group, cardinality and order decisions retain their existing suppliers; unknown equations remain propositions |
| Quotients and finite search | `quotient_by_relators`, `finite_image_lifts` retain the actual normal closure and finite-image search; traversal defaults now require a selected finite generating family |
| Subgroups | `subgroup`, `predicate_subgroup`, `centralizer`, `normalizer`, `conjugate_subgroup`, `subgroups`, `supergroup`, `inclusion` retain their exact ambient group, predicate, action and inclusions |
| Conjugacy and cosets | Conjugation G-set, conjugacy classes/class, subgroup-conjugation G-set, their decision suppliers and left/right cosets remain at Groups with their existing finite and represented routes |
| Center and commutators | Public `center` and `center_inclusion` move to Magmas; the group owner supplies one cached pair. `commutator_subgroup` and `derived_subgroup` retain the group normal-closure definition |
| Endomorphisms and comparison | `End`, `Aut`, `is_isomorphic_to` keep their actual distinct families and selected computation boundaries |

The complete strict authored up-set has six owners: Monoids (associative
multiplication and a selected two-sided unit), Semigroups (associativity),
Magmas.Unital (a selected two-sided unit), Magmas (the binary law), Sets, and
Objects. Their definitions were read. Group-specific functors, inverse,
conjugation, presentations, subgroup normality and quotient data are not
uniformly available on a strict ancestor. Suppliers for existing weaker
operations stay as group computations, with the common public contract
inherited. This pass does not claim a separate whole-owner review of every
named group refinement.

**Center placement.** For any magma, a central element commutes with every
element and satisfies the left and right associator equations. Those
equations imply the middle associator equation, so this is the commutant
intersected with the nucleus. The center is closed under multiplication and
its induced law is associative and commutative. Thus multiplication alone
supplies the definition; neither inverses nor an ambient unit are required.

Magmas now owns the common public accessors and a cached protected
`(center, inclusion)` supplier. A group has full nucleus by associativity,
so its supplier is exactly the existing group center. An abelian group
returns itself and its typed identity. A represented finite nonabelian
group retains the GAP center and literal subgroup inclusion. A general
unsupported computation reaches the named center-construction assertion.
For an inclusion i_Z, dom(i_Z)=Z(G), cod(i_Z)=G and i_Z(z)=z.

Outside Groups, the two-element magma with constant-zero multiplication is
associative and commutative and has itself as center, but has no two-sided
unit. The center operation is now present at this binary-law owner; when
only that law is supplied, its call reaches the named center-construction
assertion. No absent method or falsely asserted inverse is substituted.
The multiplicative magma of F2 is another nongroup with full center; its
zero is not a multiplicative unit.

**Finite magma generation and its independent provider.** A finite subset
generates when closure under the selected binary law is the whole magma.
Every finite magma is therefore finitely generated by its whole set,
without choosing an enumeration or deciding equality. The qualified
`is_finitely_generated_as_magma` uses that fact or the existing axiom, and
otherwise calls its optional supplier. The default retains the exact
finite-generation proposition rather than inventing a generating family.

The new Magmas.FinitelyGeneratedAsMagma axiom introduces exactly its
existence property, `an_object` using the existing C2, and display naming.
Its strict ancestors are Magmas, Sets and Objects. It adds no associativity,
unit, inverse, finite-cardinality or selected-family datum. Its inherited
fixed Mor is MagmaMor with the existing Set/categorical arrow providers;
there is no additional arrow law. The matching axiom class backs the selector.

For the multiplicative magma of owned F2, the qualified predicate returns
True from finite-set placement; zero makes this a true specimen outside
Groups. Finite generation does not imply finite cardinality: positive
integers under addition are generated by 1. For a group generated by finite
S, S union S^-1 union {1} generates its magma; conversely magma generation
implies group generation. The existing group `is_finitely_generated`
entry uses this equivalence and preserves the old group decision hook,
including the actual absolute-Galois False/unknown supplier. The separate
group resolution classifier and chosen generators are unchanged.

**Actual group-arrow inheritance and maps.** The fixed Mor supergraph
delivers GroupMorphism, MonoidMorphism, MagmaMorphism and OwnedSetMorphism,
including the unital-magma and categorical-arrow protocols. The selected
providers reviewed in full are GroupMorphism, IndexedFreeGroupMorphism,
_GroupMorRealizationMixin, IndexedFreeGroupMor, GroupMor,
GroupAutomorphismMethods, GeneralGroupMor, GroupMorCategoryConstruction,
and the existing Group End/Iso constructions.

IndexedFreeGroupMorphism now actually inherits GroupMorphism, so it
receives kernel, preimage, lift, normality and cokernel operations while
retaining its exact basis map and reduced-word evaluator. The universal
extension is a homomorphism because adjacent inverse-letter cancellation
preserves the product of images. This proof works for an infinite basis;
neither construction nor equality enumerates that basis.

Ordinary admitted elementwise maps now construct and compose in the actual
GroupMor with literal endpoints, without a GAP engine or generating
resolution. For f:G->H and g:H->K, (g*f)(x)=g(f(x)). A left automorphism does
not promote an arbitrary composite to an automorphism. Existing selected
generator/GAP computations remain available. Injectivity and subgroup-image
premises are forwarded through the monoid initializer rather than lost.

Common-Mor admission precedes group-specific equality. A bare SetMor with
the same endpoints is not a group map merely because it agrees on group
generators; that comparison uses the weaker set theory. Two admitted group
maps use conjunction of image equalities on a selected finite generating
family. Otherwise the actual set supplier computes when its own hypotheses
hold or returns the equality proposition. No finite-group-to-ranked-set
conversion is inserted. Injectivity and surjectivity likewise use either
the retained GAP data or the existing Set Mor at the exact G,H endpoints.

A decided bijective homomorphism has a homomorphic inverse: applying f to
f^-1(x)f^-1(y) gives xy. The selected lift or Set inverse routine supplies
its rule; the result is in GroupMor(H,G). `as_isomorphism` retains that
inverse pair in core(Grp). The stronger automorphism inverse stays in the
actual Aut parent through GroupAutomorphismMethods. An inclusion H->G is
injective, evaluates h to h, and has image literally H.

**Actual subgroup consumers and true assertions.** Predicate subgroups reuse
the set owner's condition-subset membership, admission and enumeration on
the literal ambient group. For admitted x, membership is exactly P(x).
Unknown P(x) remains a proposition; exact admission/enumeration names that
boundary. The declared subgroup premise supplies the ambient identity
without a new predicate test. Intersections use conjunction and preimages
use the target subgroup's actual membership predicate.

A cyclic subgroup now retains its selected generator without querying an
absent order operation. Its optional native order supplier is reused only
for cardinality, finiteness or enumeration. The ambient identity generates
a cardinal-one subgroup; in C4=<g>, <g^2> has cardinal two and retains its
ambient elements. An unknown order does not prevent construction, and
unknown power membership is not answered False. A finite ambient walk is
bounded by its cardinality and asks for decided return-to-identity equality.

For a finite selected generating family S of H, the normalizer predicate
checks g*S*g^-1 subset H and g^-1*S*g subset H. These extend to both subgroup
containments and are equivalent to g*H*g^-1=H. For finite H, one containment
suffices by equal cardinality. General unresolved cases retain
`normalizes(g,H)`. Thus 1 belongs to N_G(H), N_G(G)=G, and every subgroup
of an abelian group is normalized by G. Fresh subgroup-parent identity is
not used as a test of this mathematical equality. Abelian conjugacy is the
actual element-equality proposition, including when undecided.

The free-product supplier now requires its constructed object to belong to
the requested category and retains that category in the diagram. C2*C2 is
infinite and nonabelian, so it cannot be advertised as an abelian-group
coproduct. Product/free-product known cases retain their exact maps and the
existing nonempty finite represented-family hypotheses. Finite-image and
Schreier defaults require selected finite generators. The abelianization
consumer uses its existing finite-group import.

**Source acceptance and retained T boundaries.** The preceding assertions
close these source passes. Execution is still required under T for the
literal constructor, composition, inclusion, unknown-predicate and finite
specimens. General engine/subgroup generation, group cardinality, conjugacy,
center outside the supplied cases, derived subgroup, isomorphism, image,
normality, factorization and cokernel computations retain their selected
engine/finite-basis/finite-target or abelian-inclusion requirements. Inverse
requires established bijectivity and an inverse/lift computation. No
unavailable computation is described as mathematical nonexistence.
The infinite-group `conjugacy_classes` assertion stays explicitly retained.

Mathematical definitions and laws were checked against Mathlib's
[group homomorphisms](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/Defs.html),
[units](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Units/Defs.html),
[regularity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Regular/Defs.html),
[center](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Center.html),
[finite generation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Finiteness.html)
and
[closure of finite generating sets](https://leanprover-community.github.io/mathlib4_docs/Mathlib/ModelTheory/FinitelyGenerated.html).
The displayed normalizer, center, inverse and cyclic calculations supply
independent separating proofs. Only focused source and whitespace checks
were run; no Sage, imports, tests, QC, build or consumer-repository gate.

## Algebra owner source closure (2026-10-11)

**Closed node:** `placement-owner-algebras`. The selected scalar-action
consumer was banked in `455a45e93a`; this unit closes the complete root
Algebras owner and its required consumers. The separate algebra refinements,
Mor-owner passes, `restricted-algebras-are-restricted-modules` and
`module-and-algebra-slice-objects-lie-in-their-slice` remain unchecked.

**Mathematical owner.** For a commutative unital coefficient ring R, an
algebra is an R-module M with an R-linear multiplication
m: M tensor_R M -> M. Thus r(xy)=(rx)y=x(ry). Associativity, a unit,
commutativity, alternation and Jacobi are additional laws. The root is not
restricted to associative unital algebras. For an associative unital
algebra the scalar datum is equivalently its selected central map
R -> Z(A) -> A. The parameter category now states the commutative-ring
hypothesis required by this tensor construction. A general noncommutative
left coefficient ring supplies no such uniform bilinear product: in
M_2(QQ), r=E12, x=E21, y=I give r(xy)=E11 but x(ry)=E22.

**Complete direct inventory.** The entire root definition, its selected
suppliers and the affected consumer paths were read.

| Introductions | Mathematical data and disposition |
| --- | --- |
| Category surface | Parameter category, `an_object`, naming, supercategories, underlying-module functor, fixed `Mor`, `_MorCategory`, and `_call_(module, multiplication)` retain the exact coefficient/module/multiplication datum |
| Subcategory surface | Underlying-module functor, `base_change_adjunction`, `scalar_extension`, `restriction_of_scalars`, and the Associative/Unital/Commutative/Lie selectors retain their stated categories. The existing scalar-change functors are explicitly the ambient associative-unital functors; calling them through a refinement does not claim a restricted functor |
| Construction-premise accessors | `associativity_decision`, `unit_laws_decision`, `commutativity_decision`, `alternation_decision`, `jacobi_decision` read the admitted data, not generic law predicates. Redundant overrides that replaced an unknown admitted law by True are removed |
| Algebra and module datum | `unformed_module`, `multiplication`, `multiplication_morphism`, `algebra_structure_morphism`, `algebra_base_ring`, `underlying_module` retain their exact maps and endpoints |
| Scalar change and derivations | `restrict_scalars`, `derivations`, `vector_fields` retain their general definitions and the available computation hypotheses |
| Membership and framing | `is_algebra`, `algebra_framing_owner`, `is_framed_algebra`, `selected_algebra_resolution`, `algebra_framing_source`, `algebra_framing_morphism`, `algebra_generating_set`, `algebra_generator_morphism`, `algebra_generator`, `algebra_generators`, `number_of_algebra_generators`, `finite_algebra_generators`, `product_on_algebra_generators` use the actual selected resolution, not a finite-generation property substituted for chosen data |
| Ideals, quotients and maps | Parent `Mor`, `algebra_ideal_generated_by`, `quotient_by_algebra_ideal`, `quotient_by_generated_algebra_ideal`, `algebra_quotient_projection`, `algebra_quotient_ideal` retain the actual ideal, quotient and projection |
| Element multiplication | `ElementMethods._mul_` supplies the inherited magma product from the retained bilinear map |
| Protected construction suppliers | Initialization, retained law/datum storage, cardinality, specialized structure construction, both unformed-module element crossings, selected scalar structure map, `_with_structure`, commutativity, centre construction and `_Hom_` were read with their actual callers |
| Root arrows and selected providers | Linear-map admission, multiplicativity supplier, centre-factor supplier, cokernel/projection and composition were read with the unital, legacy, presented, framed-free, sparse-free, power and cohomology implementations |

The table includes all 33 retained public root parent operations. A selected
consumer repair does not close that consumer's independent whole-owner row.

**Actual ancestor definitions and delivered arrows.** The strict authored
up-set is Modules(R), ModulesOverCommutativeRings,
AdditiveGroups.AdditiveCommutative, AdditiveGroups, AdditiveMonoids,
AdditiveSemigroups, AdditiveMagmas.AdditiveCommutative, AdditiveMagmas,
Magmas, Sets and Objects, with the propagated additive-commutativity axiom
expressions. Modules(R) supplies a fixed scalar action; its varying-base
ancestor supplies a module together with its commutative scalar ring and
semilinear arrows. The additive ancestors successively forget inverses,
the zero, associativity and commutativity. Magmas supplies only the
multiplication; Sets and Objects supply no algebra law. These definitions
were read rather than inferred from method availability. GeneralModules
is a selected realization over Modules(R), not an extra root ancestor.

For a represented group-algebra coefficient ring, the actual Modules
dispatch may select ModulesOverGroupAlgebra. Its superclass is the generic
Modules category on the same literal scalar ring, and GroupModuleMor reaches
that ordinary fixed module Mor. This adds selected action data; it is not a
cross-base inclusion.

AlgebraMorCategoryConstruction selects MultiplicativeAlgebraMor and
MultiplicativeAlgebraMorphism. Its module branch reaches ModuleMor/
ModuleMorphismMethods, SemilinearModuleMor/SemilinearModuleMorphism,
AdditiveMor/AdditiveMorphism, AdditiveMonoidMor/AdditiveMonoidMorphism,
AdditiveMagmaMor/AdditiveMagmaMorphism and SetMorCategory/OwnedSetMorphism.
The independent multiplicative branch reaches MagmaMor/MagmaMorphism.
The selected unital, legacy, presented, free, sparse, power and cohomology
Mors inherit these actual providers. The packet supercategory construction
transports fixed endpoints along the declared graph; CategoricalMor's
generated arrow type collects its ElementMethods. No additive arrow is
thereby given multiplicativity. The native Sage substrate is not an
authored mathematical ancestor.

**Upward moves and outside-owner assertions.**

| Operation and home | Retained true specimen outside the original fixed algebra owner |
| --- | --- |
| `product` at Magmas | S3 has its selected group product g h without an R-module datum |
| `center` and `center_inclusion` at Magmas, already established in the group closure | The selected centre of C3 is literally C3 with its typed identity inclusion |
| `corestrict_to_center` at MagmaMorphism | The identity of C3 corestricts as that same identity |
| `is_multiplicative` and its validator at MagmaMorphism | A magma identity satisfies f(xy)=f(x)f(y) without addition or scalars. Finite-pair evaluation needs both finite and enumerated source placement; otherwise it retains the proposition |
| `tensor_square_morphism` at ModuleMorphismMethods over commutative R | On the plain module QQ^2, (2 id) tensor (2 id)=4 id on its tensor square, without choosing an algebra multiplication |
| `affine_equation_family` at OwnedRings.Commutative | Spec(F_p[x]/(x^2)) -> Spec(F_p) is defined, while F_p admits no unital QQ-algebra structure |

The magma multiplicativity validator rejects only a proved False. Admission
to a Mor states its law; it is not itself a computation deciding that law.

**Exact scalar-action and element assertions.** Let R=QQ[t],
phi(t)=t^2, A=phi.as_algebra(), M=A.unformed_module(), and x=A(M(t)).
Then A(t) has underlying value t^2, while x has underlying value t.
The underlying values of x+0, -x, t*x and x*x are respectively
t, -t, t^3 and t^2. GeneralModules owns one result-data ingress, used by
construction, iteration, zero, addition, negation and both scalar-action
directions. Algebra arithmetic therefore never reinterprets a computed
module element as a fresh scalar input. For R=F_2 x F_2 with
phi(a,b)=(a,a), iteration still yields all four underlying elements.
The action given by t->t^3 remains a different selected datum from phi.

Both unformed-module coordinate crossings use the existing finite
containing coefficient family. An undecided zero coefficient is retained;
no predicate support is enumerated to reconstruct it.

For f:R->S, object restriction retains the exact module
U(Res_f A)=Res_f(U(A)), the action rho_A composed with f, the multiplication
and precisely the admitted source laws. Nonassociative/nonunital input
does not acquire a ring host. The general structure-change route uses the
existing defining-object construction. The ordinary route uses the actual
selected centre inclusion and checks its endpoints. The false implicit
Algebras(S)<=Algebras(R) relation is removed; scalar restriction uses f.
This proves the retained module datum, not the stronger direct
RestrictedScalarsModules interface deferred to its existing node.

**Centre assertions and hypotheses.** The common magma centre is the
commutant intersected with the nucleus. For a central z:
zx=xz, (zx)y=z(xy), and (xy)z=x(yz); these imply the middle associator
equation. Finite chosen module generators turn these into linear
equalizers in z, with pairs of generators for the nucleus. The induced
centre algebra is commutative and associative, with a unit only when the
ambient selected construction supplies one. The finite group-algebra
class-sum computation remains available.

Over QQ, the algebra with basis x,y and x^2=y, xy=yx=x, y^2=0 is
commutative but nonassociative. For z=a x+b y the left associators with
(x,y) and (x,x) are -a y and b y. Its magma centre is therefore zero;
its commutant is all of A. The former rank-two centre expectation is not
a true assertion and is recorded for correction under T.

In the characteristic-two Heisenberg Lie algebra, [x,y]=[y,x]=z and
[z,L]=0. All triple products vanish, so the bracket magma is associative
and commutative and has centre L. The Lie centre is only span(z), computed
as the kernel of the adjoint map. The qualified lie_center and
lie_center_inclusion retain that distinct operation.

For the source-owned exterior fixture E=Lambda_ZZ(e1,e2), algebra framing
is selected but finite module framing is not. The ordinary finite-algebra-
generator fallback follows the richer module branches and returns the
existing cached predicate ring centre with its actual inclusion.
Writing z=e1 e2, the map ZZ[t]->E, t->z, still factors with codomain
literally E.ring_center(); t and 1+t have their original values, and t^2
maps to zero. Indeed Z(E)=ZZ*1+ZZ*z with z^2=0. The archived QQ case is
preserved as well.

For a finite-module target M_2(QQ), the selected algebra centre is QQ*I.
A polynomial-source map with central image lifts through that exact
centre inclusion and returns an actual Alg_QQ factor. If i_Z is the
retained inclusion and g the factor, dom(i_Z)=cod(g) literally and
i_Z g=f in a shared arrow theory. Injectivity proves uniqueness. A ring
factor is used only for a literally selected predicate/scalar ring
centre, never by substituting an unrelated centre representation.

For tensor algebras, the scalar-centre word argument needs at least two
free module basis generators. A cyclic generating module gives a
commutative tensor algebra. The relationful module ZZ/2 direct-sum ZZ/3
has two generators but zero mixed tensor products; its tensor algebra is
commutative, so generator count alone cannot justify the free-rank-two
answer. The existing cardinal owner sends undecided cardinality to its
named normal-form assertion; it does not classify it as infinite.

**Derivations and arrow laws.** A derivation is R-linear and satisfies
D(xy)=D(x)y+xD(y), using both target actions. The current Kahler-
differential solver is selected only on commutative associative unital
algebras. Other inputs reach the named missing solver with both actions;
vector_fields follows this same route.

Composition checks literal middle endpoints and admission under the same
Alg_R before selecting Cat().join of the two actual Mor theories, hence
their common laws. A unital identity composed with a root zero endomap
is the root zero map and sends 1 to 0. Sparse generator substitution no
longer turns it into augmentation. Matching free/power/cohomology maps
retain their specialized algorithms; mixed admitted algebra maps use the
root composition of the actual underlying linear maps.

An arbitrary exact-endpoint Map supplies no construction-derived True
algebra-law decision. For the linear map f(x)=2x on QQ, f(1)=2!=1 and
f(1*1)=2!=4=f(1)^2. The multiplicativity diagnostic uses
U(f)m_A=m_B(U(f) tensor U(f)) in the actual module Mor. Exact module-map
ingress stores its datum without an eager finite-source check or Boolean
coercion of an unknown equation.

Presented relations have a lazy decision and an OWN-22 validator. For
R[t]/(a t), assigning t->1 is admitted under the relation premise a=0.
An undecided coefficient equality remains that premise. Decided relation
equations may justify the descended laws; generic algebra-law diagnostics
remain distinct. Inequality uses logical negation of the equality
proposition.

**Ideals and root cokernels.** The root category is pointed, and the
cokernel of f:A->B is B modulo the two-sided ideal generated by im(f).
For f:QQ->M_2(QQ), a->a E11, the image has dimension one but generates
all of M_2(QQ) as a two-sided ideal: E_i1 E11 E_1j=E_ij. The module
cokernel has dimension three, whereas the algebra cokernel is zero.
For a unit-preserving f the image ideal contains 1, again giving zero.
This is a cokernel after forgetting unit preservation; no pointed
unital-category assertion is made.

The selected field/finite-generator ideal algorithm adjoins left and
right products. True containment stops it, false containment increases
dimension, and undecided containment reaches its named computation
assertion. Finite dimension proves termination in the decided case.
The quotient retains its descended algebra laws. Its exact projection
is returned in the root Alg_R Mor, without asserting matrix, free or
graded object data discarded by the quotient.

**Source acceptance and T.** All displayed mathematical assertions are
retained for execution under T. Named frontiers remain for general
scalar-change functor/arrow suppliers beyond the available ordinary
adjunction, general derivation solvers, unsupported centre and relationful
tensor-centre computations, unavailable exact centre lifts, ideal closure
without the selected finite field data or with undecided containment, and
the represented image/module quotient computations used by cokernels.
An unknown law or relation remains a proposition. No new prerequisite was
filed and no computation failure is asserted to be mathematical
nonexistence.

The mathematical definitions were checked against Mathlib's
[centre](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Center.html)
and [Lie centre](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Abelian.html);
the displayed scalar-action, associator, exterior, tensor, composition and
matrix-ideal calculations provide independent proofs of the separators.
Only focused source/whitespace checks were used. No imports, Sage, tests,
QC, build, live survey or other repository's progress is claimed.

## Whole-category placement: AbelianGroupEndomorphismRings (2026-10-11)

**Closed node:** `placement-owner-abeliangroupendomorphismrings`.
**Owner and delta:** `AbelianGroupEndomorphismRings` in
`src/dzack_research/preamble/categories/group/groups.py` now enriches the
canonical group or additive `End(A)` rather than constructing a detached
ring of callbacks. Its pointwise arithmetic uses `AdditiveMorGroups` and
`AdditiveEndomorphismRings(ZZ)` in `group/additive_mors.py`. The fixed arrows
retain their literal source and target, existing determining data, and
admitted source/range membership. This is a complete source owner pass;
the distinct AdditiveEndomorphismRings, AdditiveMorGroups and GroupMor
owner rows remain open for their own complete inventories.

### Defining datum, full introduced inventory and actual ancestors

The datum is one abelian group A, written additively or multiplicatively.
The carrier is the set of all group homomorphisms A -> A, with pointwise
abelian addition, zero the trivial map, negative the pointwise inverse,
multiplication composition, and one the identity of A. Associativity is
associativity of composition. Both distributive laws follow from evaluation
and the homomorphism law. An arbitrary ring R supplied as A means End(R,+);
it does not impose R-linearity on these maps.

The complete direct category inventory is `an_object`, `_call_` and
`super_categories`; the complete direct object inventory is
`_commutativity_decision` and `_repr_`. There is no direct ElementMethods
or fixed-Mor declaration left in this owner. `an_object` still gives
End(ZZ,+). `_call_` uses
`AdditiveGroups().AdditiveCommutative().End(A)` for additive notation and
`OwnedGroups().End(A)` for multiplicative notation, rejects a nonabelian
input, and refines that same cached Mor object.

The old owner-local constructor, domain/codomain accessors, map evaluation,
one/zero, addition, negation and composition are supplied by the canonical
Mor and the existing enrichment. The old `_is_additive`, `_sum_values`,
`_negative_value` and `_identity_value` are now the one shared target-law
supplier in AdditiveMorGroups. The source need not be abelian: Hom(G,A)
has the pointwise abelian law whenever the target A is abelian. Only an
unrestricted diagonal receives endomorphism-ring placement. Aut(A) retains
its composition law and explicitly declines that additive placement.

The actual ancestor definitions were read along both branches:

- AbelianGroupEndomorphismRings -> AdditiveEndomorphismRings(ZZ).
- AdditiveEndomorphismRings -> AdditiveMorGroups ->
  AdditiveGroups.AdditiveCommutative and the additive group, monoid,
  semigroup, magma, set and object spine. The propagated commutative law
  reaches the actual AdditiveMagmas.AdditiveCommutative provider.
- AdditiveEndomorphismRings -> Algebras(ZZ).Associative().Unital(), including
  the root, Associative and Unital definitions and the OwnedRings branch.
  Root Algebras -> Modules(ZZ) and Magmas; Modules(ZZ) selects
  ModulesOverCommutativeRings and its abelian additive-group structure.
- OwnedRings -> OwnedSemirings and OwnedRngs. OwnedSemirings ->
  OwnedNonUnitalSemirings and Monoids; OwnedRngs ->
  OwnedNonUnitalSemirings and abelian additive groups.
  OwnedNonUnitalSemirings -> multiplicative Semigroups and commutative
  additive monoids. Monoids -> Semigroups and Magmas.Unital; both meet
  the common Magmas -> Sets -> Objects definitions.

The scalar ring is the literal owned ZZ, installed before each GroupMor,
GeneralGroupMor or IndexedFreeGroupMor is initialized. Integer action on
a multiplicatively written target is the existing integer-power operation.
The existing scalar-evaluation datum and an actual diagonal subgroup
inclusion identify scalar maps; no sampling, cache annotation or asserted
proof flag is used. The scalar-one map reuses the cached identity inclusion.
`Algebras.Unital.one` supplies that same identity for an additive End Mor.
The native abelian-group scalar_action now uses the existing ring Mor
`ZZ.Mor(E)(E._scalar_identity)`.

### Actual fixed arrows and the explicit construction contract

Two arrow levels must remain distinct. An element f of E=End(A) is an
actual map A -> A. GroupEndCategoryConstruction.Of reuses the diagonal
GroupMor/GeneralGroupMor/IndexedFreeGroupMor and attaches End; the additive
branch uses the actual AdditiveMor. CategoricalMor._generated_arrow_type
assembles the selected GroupMorphism or AdditiveMorphism providers.
Group arrows reach monoid, unital-magma, magma and set arrows. Additive
arrows reach additive-monoid, additive-magma and set arrows. Their
enrichment supplies arithmetic on those very arrows, preserving evaluation
and endpoint identity.

A ring or algebra arrow E -> F is a different object. OwnedRings().Mor
selects RingMorCategoryConstruction -> RingMor -> RingMorphism. The
unital ZZ-algebra Mor selects UnitalAlgebraMorCategoryConstruction and,
without selected algebra generators, UnitalMultiplicativeAlgebraMor with
its actual underlying linear map and multiplicativity/unit laws. These
are separate from the Mor object's 2-Mor surface: 1_E is the map A -> A,
whereas id_E is the map E -> E.

**Explicit constructor-contract change:** an untagged callable in the
canonical IndexedFreeGroupMor keeps its established meaning as images of
basis labels. The removed detached End carrier had interpreted every
callable as a map on group elements. Both interpretations cannot occupy
one untagged input of the same canonical Mor. A callback on group elements
therefore uses the existing explicit constructor
`E.elementwise(lambda element: ...)`; it is extended through the existing
free-basis realization. Nonfree GroupMor and AdditiveMor retain their
elementwise callable interpretation. Native scalar_action was changed
with this contract, and no duplicate wrapper or engine was introduced.

### Preserved admitted points, equality and operations

GroupMorphism evaluation now normalizes source and image through the
shared `_GroupMorRealizationMixin._normalize_admitted_element` contract.
A point whose actual parent is the literal endpoint is retained before
any facade traversal. Otherwise the actual submonoid engine's ambient
monoid, or the actual Subgroups(ambient) datum, supplies the representing
parent; nested facades are followed. A quotient is not unwrapped merely
because it has a supergroup accessor. Ordinary endpoints keep ordinary
ingress. The same supplier serves the cached subgroup inclusion.

This is evaluation on an admitted source point and an image supplied by
the map's range law, not admission of a new subgroup member or a decision
of a predicate. It is necessary when the ambient computation cannot
decide that an already admitted value is a unit. It also preserves groups
whose subgroup elements have their own actual parent, such as an open
absolute Galois subgroup. The source reader of that consumer supplied
the distinguishing own-parent case; the common guard repairs the new
supplier rather than adding an inclusion-specific exception.

General GroupMorphism composition keeps the actual rule f(g(x)) in the
canonical group Mor, avoiding a second SetMor predicate admission.
The existing free realization has one `_admitted_generator_image`
supplier. It retains the given basis-map range premise, reads an actual
OwnedSetMorphism's evaluator (or an existing native map's evaluation),
and uses the same target normalization. Reduced-word evaluation, image
generators, postcomposition and the free inclusion use that supplier.

Pointwise scalar multiplication requires a map already admitted in the
actual enriched Mor and delegates to its retained target action.
Addition/negation of an automorphism land in the full Mor, while
automorphism composition retains its existing restricted carrier.
Equality in finite group Mors still uses the selected determining
generators; maps from (ZZ,+) compare their values on 1. An undecided
target equality remains the corresponding owned proposition.
The commutativity supplier proves End(A) commutative for a selected
cyclic A (and for (ZZ,+)); it does not infer noncommutativity from a
longer chosen generator list.

### True closure assertions retained under T

1. For A=C3 with generator a, E has three elements. Put i=1_E and d=i+i.
   Then d(a)=a^2 != a, d != i, d*d=i, and d+i=0. These equations follow
   by the exponent calculus modulo three. The existing read-only archive
   assertions in tests/groups/test_groups_archive.sage remain required.
2. For E=End(ZZ,+), (i+i)(3)=6, (-i)(3)=-3, and i+i != i. Every additive
   map from ZZ is determined by 1. More generally an undecided equality
   of the two images of 1 is retained, not converted to a Boolean.
3. Outside the old End owner, Hom(S3,C2) is an abelian group under the
   pointwise law and sign+sign is the trivial map. Distinct endpoints
   do not receive ring placement. This proves the weaker home of the
   pointwise operations independently of a diagonal endomorphism carrier.
4. For A=C2 x C2 with generators a,b, let p(a)=a, p(b)=1, and let s swap
   a and b. Then (p*s)(a)=1 while (s*p)(a)=b, so End(A) is not
   commutative. Scalar maps n*id remain central. A general A with more
   than one chosen generator retains an undecided commutativity
   proposition unless an actual decision is available.
5. For the identity automorphism u of C2, u+u is the zero endomorphism
   and is not an automorphism. Its parent is the full End Mor. The
   composition u*u remains the identity automorphism.
6. If v=f(u) is the image of an admitted unit under a unital map and
   ambient is_unit(v) is undecided, the identity of the unit-group End
   sends v to v and its double sends v to v^2. Composition and the
   selected free-basis version retain that membership premise. For an
   abelian subgroup H with its own-parent element h, the identity of
   End(H) likewise sends h to h before any facade traversal.
7. The map ZZ -> End(A), n |-> n*id_A, preserves zero, one, sum and
   product: (n+m)id=nid+mid and (nm)id=(nid) composed with (mid).
   In multiplicative notation these are ordinary integer-power laws.
   The existing C4 scalar-action case sends its generator to its square
   under scalar 2.

The pointwise Hom theorem requires an abelian target, and the
endomorphism ring law is independently stated in the maintained
[Mathlib group-hom instances](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/Instances.html),
[endomorphism definitions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/End.html)
and [module endomorphisms](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/End.html).
The displayed finite calculations establish their own expected values.

**Source acceptance and named frontier:** all introduced operations, the
actual ancestor definitions, canonical carrier and delivered arrow
providers were source-reviewed, including an independent review of the
admitted-unit and own-parent cases. General infinite-map equality and
unknown commutativity retain owned propositions. A selected
multiplicatively written target without a computable inverse retains
that existing computation frontier for negative powers; this pass does
not invent an inverse algorithm. The examples above and the preserved
archive cases remain execution obligations under T. M1 / DEV-58 forbids
runtime, imports and tests in this source phase, and no execution result
is claimed.

## Whole-category placement: AbsoluteGaloisGroups (2026-10-11)

**Closed node:** `placement-owner-absolutegaloisgroups`.
**Owner and delta:** `AbsoluteGaloisGroups` in
`src/dzack_research/preamble/categories/group/profinite/absolute_galois_groups.py`.
The selected absolute-group realization in `absolute_galois_group.py`,
the character realizations in `galois_characters.py`, and the existing
group-operation suppliers in `group/groups.py` form this owner-sized unit.
It retains the exact base field and embeddings, composes the actual
conjugated finite-stage square, preserves mixed Frobenius/field-map laws
and undecided equations, and gives all selected character arrows the
generated group-Mor inheritance. No new category or prerequisite is added.

### Mathematical datum, full direct inventory and actual up-set

The defining datum is a field K, a chosen algebraic closure Kbar, and
the exact embedding e:K -> Kbar. G_K consists of automorphisms sigma of
Kbar satisfying sigma e=e, with composition and the Krull topology.
For an imperfect field the finite separable subextensions supply the
usual absolute Galois correspondence; the discussion does not identify
K with the fixed subfield of the entire inseparable algebraic closure.

The complete direct category inventory is `an_object`,
`_repr_object_names` and `super_categories`. The specimen is G_F2.
The complete final object inventory is `characteristic`,
`_conjugate_subgroup_construction`, `_subgroup_conjugacy_decision`,
`_normalizer_construction`, `_cardinality_decision`,
`_finite_quotient_witnesses` and `_cubic_splitting_field_restriction`.
There is no direct ElementMethods or Mor declaration in this category.

Characteristic remains the characteristic of the retained K: no actual
ancestor supplies a base field. The two former generator-capability
methods now belong to OwnedGroups and read its existing
`has_selected_group_resolution` datum. Their signatures are preserved.
The explicit capability contract is availability of a selected algebraic
generating-family realization, which may be lazy; it neither asserts
that all values were computed nor decides finite generation, enumeration
or the existence of an arbitrary algorithm. Topological generators alone
do not supply this algebraic datum.

Conjugation and normalizer were already public group operations.
They remain there, with protected `_conjugate_subgroup_construction`
and `_normalizer_construction` suppliers for selected computations.
The defaults use the existing predicate constructions; an unavailable
specialized construction returns None. The Absolute category supplies
its open-subgroup computation rather than replacing the public owner.
The existing subgroup-conjugacy hook still answers True, False or Unknown;
it applies `ask` to the exact extension-isomorphism proposition.

The full strict authored up-set is:

- ProfiniteGroups: inverse limits of finite groups with their profinite
  topology; its finite-quotient supplier and abelianity predicate were read.
- TopologicalGroups: groups with a group topology. Its authored
  `super_categories` declares OwnedGroups, not a TopologicalSpaces edge.
- OwnedGroups: associative multiplication, a two-sided unit and inverses.
- Monoids: associative multiplication and a two-sided unit.
- Semigroups: associative multiplication.
- Magmas.Unital: a binary law and a two-sided unit, without an
  associativity hypothesis.
- Magmas: a binary law on the carrier.
- Sets: the carrier and set maps.
- Objects: the common mathematical-object root.

The actual branches are ProfiniteGroups -> TopologicalGroups ->
OwnedGroups -> Monoids, then Semigroups and Magmas.Unital, meeting at
Magmas -> Sets -> Objects. All definitions were read with their selected
suppliers. The finite-field and open-subgroup refinements are actual
consumers inspected here; their separate complete owner passes remain open.

### Selected realization inventory and preserved construction routes

The actual absolute-group engine retains its initialization datum;
`base_field`, `algebraic_closure`, `base_embedding`/`geometric_point`,
`field_automorphism_mor`/`arrow_set`, `choice_data`,
`has_canonical_realization`, `slice_category`, `extension_object`,
`stage_category` and `slice_automorphism` read that exact datum and the
existing field/slice/Core constructions.

Its group/set suppliers are `_finiteness_decision`,
`_finite_generation_decision`, `_is_finite_field`, `_is_number_field`,
`base_field_order`, element ingress, membership, parent equality/hash,
`one`, `an_element`, `frobenius`, `_finite_frobenius_image`,
`_compose_elements`, `_inverse_element` and representation. Their public
group/set meaning is inherited; this engine supplies the selected
finite-field or exact-field-map computation. Finiteness and abstract
finite-generation decisions remain False only for finite and number
fields; other regimes retain the existing proposition/frontier.

`extension_data`, `finite_extension`, `finite_quotient`,
`_finite_quotient_of_stage`, `restriction_map`, `lift`, `lifts`,
`open_subgroup` and `open_subgroup_class` use the existing finite-stage,
finite-group, restriction, fiber and subgroup/orbit constructions.
`decomposition_group`, `decomposition_group_class`, `inertia_group`,
`inertia_group_class` and `frobenius_class` retain their existing selected
prime/prolongation constructions. `cyclotomic_character` and
`quadratic_character` retain their concrete character classes below.
A chosen finite-field lift is a representative of a fiber, not an
asserted homomorphic section of a finite quotient. Noncanonical lifts
remain the full existing LiftCoset; no new lift algorithm is claimed.

The selected element inventory comprises initialization; `as_morphism`
and `underlying_field_morphism`; domain/codomain and exact-action data;
`realized_stages`, `restriction_coordinate`, `extend_coordinate`;
`frobenius_exponent`, `is_globally_evaluable`, evaluation;
`fixes_base_field`, `validate_base_fixing`, `restrict`; multiplication,
inverse, powers, conjugacy class, equality/inequality, hash and display.
FrobeniusElement supplies its existing exponent initialization.
The full source route was read, including existing finite-coordinate
and field-arrow computations; it is not replaced by a new element engine.

### Exact conjugation and extension comparison

For a retained stage t=(K --j--> E --iota--> Kbar) and admitted g in G_K,
the new stage has exactly the same E and j and embedding g iota. The
existing CosliceMor._from_commuting_edges supplies the square with
left edge id_K and right edge g.as_morphism(). Its composite with
t.arrow() is constructed through
`G.stage_category().object(..., _engine=_FiniteGaloisExtensionEngine)`.
That existing engine reads all fields and maps from the square.
The exact source object is unchanged, so degree and separability are
unchanged. The triangle follows from (g iota)j=g(iota j)=ge=e.
No search for embeddings, or new separability decision, is required.

An automorphism g h g^-1 fixes g iota(E) exactly when h fixes iota(E).
Thus the represented subgroup is precisely g G_(E,iota) g^-1.
Two such open subgroups are conjugate exactly when the retained finite
separable K-extensions are isomorphic. `_same_k_extension` therefore
tests s j_E=j_F for the selected finite field-embedding candidates and
equal degrees. Conjunction and negation retain undecided candidate
equations; outside the existing finite/number-field computation regime
the actual extension-isomorphism proposition is retained.

The open subgroup's conjugacy-class constructor now passes its
`fixed_extension`, including j. An admitted stage takes precedence over
the bare-ring branch: it is itself a field through its slice/coslice
placement, so testing OwnedRings first would discard that very datum.
Only a bare field with a unique base embedding is inferred. The missing
OwnedRings import on this route is also repaired.

For N_G(G_E), the selected whole-group construction is used only when
normality is literally True. An undecided normality result reaches the
existing predicate normalizer. The usual law is
N_G(G_E)/G_E = Aut_K(E); N_G(G_E)=G exactly for a Galois E/K.

### Equality, group laws and actual arrows

The exact-action input belongs to the literal field Mor Kbar -> Kbar.
Base fixing is the map equation sigma e=e; OWN-22 keeps this admission
premise separate from its `validate_base_fixing` diagnostic, which
rejects a proved failure and preserves an undecided equation.
A K-endomorphism of the algebraic extension Kbar/K is an automorphism,
so the mathematical group law does not require an inverse computation
at construction (Stacks, Lemma 9.8.11).

Two integral Frobenius representations still compare their exponents.
Other same-parent comparisons use their actual retained field maps;
inequality is logical negation, not a comparison of a proposition with
a Boolean. Zeroth Frobenius uses the canonical identity field map.
Thus re-entering g.as_morphism() preserves a decided identical map
without confusing its representation with its mathematical value.
The hash depends only on the actual parent, so equal mixed
representations satisfy the hash law. The collision tradeoff does not
change equality or introduce an extra mathematical identifier.
Mixed composition retains left.as_morphism() * right.as_morphism().
The common base-fixing equation is preserved by composition; only
decided identity comparisons select an identity shortcut.
The existing inverse computation remains the selected supplier.

OwnedGroups.Mor -> GroupMorCategoryConstruction.Of selects GeneralGroupMor
for a profinite source. GeneralGroupMor.ElementMethods is GroupMorphism;
CategoricalMor.super_categories and _generated_arrow_type include the
actual MonoidMorphism, UnitalMagmaMorphism, MagmaMorphism and
OwnedSetMorphism providers. GaloisRestrictionMap and OpenSubgroupInclusion
already used the existing `_from_realization_engine` route.
The character classes now use that same route rather than merely giving
a raw Sage Morphism a GroupMor parent. Public class-call signatures are
preserved using Sage's non-inherited __classcall_private__ hook and
cooperative generated-arrow initialization. No wrapper or new category
is introduced. The chosen restriction, inclusion and character maps
are continuous by their constructions; the common abstract group Mor
does not itself assert continuity of every group homomorphism.

### Character data, root coherence and the exact kernel hypothesis

Cyclotomic characters retain n, the literal residue-ring unit group,
the primitive closure root, its selected stage root, and K(zeta_n).
Quadratic characters retain nonzero a, characteristic different from
two, the literal integer-unit target, both root realizations, and
K(sqrt(a)). For a square a, the stored closure root is now exactly
e(root_at_stage), so direct evaluation and an installed identity
coordinate agree even if independent square-root routines choose
opposite signs. Only decided root equalities supply a sign; an
undecided sign reaches its named computation assertion.

The two concrete roots generate their selected finite stage. Hence
chi(sigma)=1 iff sigma fixes that root iff sigma is in G_L. The existing
open-kernel formula is shared only by those concrete constructions.
A general character merely factoring through L need not be faithful
there, and uses the inherited group-map predicate kernel. The trivial
character through a nontrivial L separates these assertions.

RestrictedProfiniteCharacter retains the exact supplied H, the original
target and the actual inclusion i_H, in H.Mor(target), with
(chi|_H)(h)=chi(i_H(h)). This also admits ordinary represented subgroups
without demanding a profinite convenience method. Continuity is the
restriction theorem for the induced subgroup topology.
The bare ProfiniteCharacter interface retains a missing-defining-map
frontier, computing only the universal identity value f(1)=1; a finite
factor alone is not a uniquely specified character. That incomplete
generic computation is not a concrete closure specimen.

### True closure assertions retained under T

1. For finite or number fields K, |G_K|=2^aleph_0. The countable
   algebraic closure gives the upper bound. Finite fields have quotients
   of every positive order; number fields have
   [K(zeta_n):K] >= phi(n)/[K:QQ], hence unbounded finite quotients.
   An infinite profinite group has no isolated points; recursively
   splitting nonempty clopen cosets and compactness give continuum
   distinct elements. These groups are not finitely generated as
   abstract groups, since any finitely generated group is countable.
   Algebraically closed and real-closed bases give orders one and two
   as separators; the selected continuum supplier does not apply there.
2. Over QQ, x^3-2 is irreducible by Eisenstein and has nonsquare
   discriminant -108, so its splitting field has Galois group S3.
   Restriction is a continuous surjection with its exact open kernel.
   Over another number field the two selected cubics supply their
   actual splitting-field groups, not a blanket S3 claim. Failure to
   find a nonabelian quotient does not prove abelianity.
3. Put K=QQ(b), b^2=2, and E=QQ(x) in its real embedding with
   x^2=1+b; then x^4-2x^2-1=0. Norm(1+b)=-1 proves [E:K]=2.
   On the same abstract E put j_+(b)=x^2-1 and j_-(b)=1-x^2.
   These K-extensions are not isomorphic: an intertwining automorphism
   would send x to an element whose square is 1-b<0 in this real E.
   For fixed e(b)=sqrt(2), the images sqrt(1+sqrt(2)) and
   i*sqrt(sqrt(2)-1) give compatible closure embeddings respectively.
   Exact K-extension comparison therefore returns False despite
   identical underlying field objects. Conjugating either stage
   preserves its literal j and changes only iota to g iota.
4. For E=QQ(cube_root(2)), N(G_E)/G_E has order one. For
   E=QQ(sqrt(5)), it has order two and N(G_E)=G_QQ.
   The existing normalizer archive assertions are preserved.
5. In G_F9 arithmetic Frobenius is alpha |-> alpha^9, fixes F9,
   and its inverse cancels it. For alpha generating F_(9^4),
   alpha^9 != alpha^3. If h=G(g.as_morphism()), then h=g and
   (g*h)(alpha)=alpha^81. Unknown equality of other retained
   closure maps remains an owned equality proposition.
6. G_F25 -> G_F5 sends Frobenius_25 to Frobenius_5^2.
   Restriction to F625 has cyclic order four; its kernel has index
   four, contains Frobenius^4 and excludes Frobenius. The order-two
   coordinate has two lifts among exponents 0,1,2,3, namely 1 and 3.
   The common own-parent ingress from the End pass preserves H-owned
   points until the actual inclusion evaluator receives them.
7. On G_F5, chi_3(Frobenius)=-1 modulo three and the quadratic
   character of 2 has value -1. Their selected stages and kernels
   have degree/index two; chi(g h)=chi(g)chi(h). On G_F9,
   chi_5(Frobenius)=4 modulo five. If a is square, both direct
   identity evaluation and its retained identity coordinate give +1.
   Restricting a character to its concrete open kernel gives value one.
8. For chi_5 on G_F2 the factor has degree four and
   chi(Frobenius^e)=2^e mod 5. Its abelian unit-group target has itself
   as its retained center; inherited corestrict_to_center returns
   that same character with all defining data. Inherited pointwise
   addition evaluates as (chi+chi)(g)=chi(g)*chi(g).
9. Outside the original owner, a chosen free group supplies the
   selected algebraic generator datum, while G_Fq with only its
   topological Frobenius datum supplies no such resolution. In S3,
   conjugating <(12)> by (123) gives <(23)>, and the normalizer
   of <(12)> is itself. These are true group-level specimens for
   the retained common operation homes.

Primary mathematical sources are
[Stacks 0BMI, infinite Galois theory](https://stacks.math.columbia.edu/tag/0BMI),
[Stacks 0BU2, inverse limits and onto restrictions](https://stacks.math.columbia.edu/tag/0BU2),
[Stacks 0BMD, algebraic-extension endomorphisms](https://stacks.math.columbia.edu/tag/0BMD),
and [Keith Conrad, Finite Fields, Theorem 4.1](https://kconrad.math.uconn.edu/blurbs/galoistheory/finitefields.pdf).
The exact-base separator and displayed exponent/root calculations
establish their expected values independently of the implementation.
The character class-call mechanism was also checked against the
[primary Sage source](https://github.com/sagemath/sage/blob/develop/src/sage/misc/classcall_metaclass.pyx).

**Source acceptance and named frontier:** the full direct owner inventory,
actual ancestors, selected realizations and delivered arrow inheritance
were reviewed, including an independent final source review. The retained
tests/groups/test_absolute_galois.sage and the normalizer, generator,
open-subgroup and character archive assertions remain required under T.
Generic finite-stage embedding/equality and quotient computations,
unavailable inverses of arbitrary exact closure maps, noncanonical
individual lifts, general cardinality and the bare missing-character
map remain their existing computation frontiers. This pass does not
close the separate finite-stage wrapper or later refinement-owner rows.
M1 / DEV-58 requires source-only work: no imports, Sage, tests or runtime
acceptance are claimed.

## Whole-category placement: AbsoluteGaloisGroupsOfFiniteFields (2026-10-11)

**Closed node:** `placement-owner-absolutegaloisgroupsoffinitefields`.
This is a complete source pass; execution of the assertions below remains
unverified under M1 / DEV-58 and is retained for T.

**Owner and delta.** The entire introduced inventory before the move is
`an_object`, `_repr_object_names`, `super_categories`, and the two
parent operations `topological_group_generators` and
`topological_generating_family`. There is no introduced element method,
Mor category, or arrow operation. The three category methods retain their
roles: a selected example over the actual field of order two, the category
name, and the absolute-Galois, commutative-group and infinite-group laws.

Both public generating-family operations now belong to `TopologicalGroups`.
Their data are a topological group G and a family of its elements whose
generated subgroup is dense in G. This notion requires the represented
topology and group law, but neither profiniteness nor a finite base field.
The duplicate optional abstract declaration on `ProfiniteGroups` is removed
so actual descendants inherit the public owner. Its protected
`_topological_generating_family` value contract accepts a selected dense
family and otherwise returns None. The finite-field owner supplies precisely
the prior singleton containing its actual q-power Frobenius through that
contract. The two public signatures are unchanged and return the same
cached family.

Without a selected supplier, the public owner uses the existing
`indexed_family(G, lambda g: g)`. The index set is literally G; evaluation
uses an admitted point and does not enumerate G, construct a new topology,
assert finiteness, or select an algebraic group resolution. The values form
all of G, whose generated subgroup equals G and therefore has closure G.
A family retains its index set and is not identified with its image set.

**Complete actual up-set.** The fifteen strict authored providers and their
definitions were read: `AbsoluteGaloisGroups` retains the exact base field,
closure and base embedding; `ProfiniteGroups` supplies represented profinite
structure and finite continuous-quotient decisions; `TopologicalGroups`
supplies a compatible represented group topology; `OwnedGroups.Commutative`
adds the abelian law, its integer action and End construction;
`OwnedGroups.Infinite` adds the infinite axiom; `OwnedGroups` supplies the
group law; `Monoids.Commutative` adds the commutative monoid law and
square-class construction; `Monoids` supplies associativity and a selected
unit; `Semigroups` supplies associativity; `Magmas.Commutative` supplies
commutativity of the binary law; `Magmas.Unital` supplies its selected
two-sided unit; `Magmas` supplies multiplication; `Sets.Infinite` supplies
infinite cardinality; `Sets` supplies a set; and `Objects` is the root.
Generated axiom meets carry these laws, not additional authored providers.
In particular, the actual TopologicalGroups declaration has OwnedGroups as
its parent; this record does not invent a TopologicalSpaces edge.

The finite-field refinement adds no arrow law to this chain. Its actual
`GroupMorCategoryConstruction.Of` selects `GeneralGroupMor` on a profinite
source. The generated arrow inherits `GroupMorphism`, the monoid and
unital-magma arrow providers, `MagmaMorphism`, and the owned set-map
provider. The actual endpoint and base-map constructions closed in the
AbsoluteGaloisGroups pass remain in use. A topological generator does not
replace that Mor by homomorphisms of a finitely generated abstract group.

**Necessary indexed-family consumer repair.** The new all-points family
reaches the existing `IndexedFamily._value_at_normalized_index` cache.
Absolute-Galois elements with the same parent intentionally share a hash;
equality of two retained field maps can be an undecided proposition. A Python
dictionary keyed directly by those labels could truth-coerce that proposition.
The existing cache now uses integer-hash buckets and scans each bucket for
literal identity or equality that is literally True. Unknown equality keeps
both labels available without deciding that they are distinct. The same
scan serves unhashable labels and preserves their existing behavior.
Only hash computation catches TypeError; an error constructing a value is
not caught or retried through another cache. This repair discharges the
current node's actual outside-owner consumer, not a separate hashing task.

**True closure assertions retained for T.**

- For every finite field K of order q, each finite extension of degree n
  has cyclic Galois group of order n generated by x -> x^q. The compatible
  restrictions identify G_K with the inverse limit of these cyclic groups,
  and Frobenius maps to 1 modulo every n. Its powers therefore meet every
  finite-quotient coset, proving that the selected singleton is dense.
- In particular, for K = F_5, the two public operations return the same
  singleton family containing `G.frobenius()`, with cardinality one.
  G is abelian and infinite, has cardinality continuum, and is not finitely
  generated as an abstract group. Indeed a finitely generated abstract
  group is countable, whereas the profinite integers have continuum many
  elements. The singleton does not give a surjective map from the abstract
  infinite cyclic group onto G.
- For K = F_9, q is 9, not 3. The selected Frobenius acts by x -> x^9,
  fixes every element of the exact base field, and generates every finite
  extension quotient. The 3-power map fails to fix an element of
  F_9 outside F_3, so it is a true separating case. The unchanged retained
  exponent, exact base embedding and finite-stage restriction computations
  continue to express the 9-power map and its powers.
- Outside this finite-field owner, take the already represented
  G = AbsoluteGaloisGroup(QQ), with its Krull topology. For
  F = G.topological_generating_family(), `F.index_set() is G` and
  `F is G.topological_group_generators()`. Its value at each admitted
  group element represents that same element, so its values generate G
  itself and are dense. This uses an actual existing topological object,
  not an unsupported finite-group topology placement.
- At that G_Q, let U be `G.field_automorphism_mor()), and retain two
  separately supplied valid identity rules
  `sigma = G(U.elementwise(lambda x: x))` and
  `tau = G(U.elementwise(lambda x: x))`. Their represented equality is
  the existing undecided field-map equation and their hashes agree.
  Asking F.value(sigma) and F.value(tau) must return their admitted values
  without forcing that equation; repeated access at each identical label
  reuses its value. An independently decided-equal label may reuse the
  previously selected representative. Hence equality to the index is the
  universal mathematical claim, not Python identity with every alternative
  representation of it.
- A repeated decided-equal finite label, including the existing [0] and
  ([0],) unhashable examples in IndexedFamily, retains its chosen value.
  An undecided collision neither denies membership in the indexing group
  nor substitutes a Boolean equality answer. The selected Frobenius family
  remains the existing finite ordered set and does not use this cache.

**Sources, review and retained frontier.** The finite-field assertions use
Keith Conrad, [Finite Fields, Theorem 4.1 and its extension-field form](https://kconrad.math.uconn.edu/blurbs/galoistheory/finitefields.pdf),
and the compatible finite-Galois quotient description in
[Stacks 0BU2](https://stacks.math.columbia.edu/tag/0BU2) and
[Stacks 0BMI](https://stacks.math.columbia.edu/tag/0BMI).
The identity-family density proof above is independent of any algorithm
for enumerating a profinite group.

Read sources include the existing megadoc as an index; the complete
finite-field category and its selected absolute-Galois realization;
profinite_groups.py; the actual providers in groups.py, magmas.py,
set_categories.py, and the inherited abstract category/arrow constructions;
and indexed_families.py with its value, iteration and cache consumers.
The read-only finite-field construction, profinite-generator archive,
profinite-owned-boundary, absolute-Galois object and Galois-session
expectations retain their Frobenius/cardinality assertions. Independent
review accepted the complete four-source-file delta. The general
finite-stage and exact-map computation frontiers already recorded for
AbsoluteGaloisGroups remain named there; this pass does not claim those
algorithms executed. All retained specimens, including the new G_Q family
and undecided-collision assertions, remain under T.

## Whole-category placement: AdditiveEndomorphismRings (2026-10-11)

**Closed node:** `placement-owner-additiveendomorphismrings`.
**Owner:** `AdditiveEndomorphismRings` in
`src/dzack_research/preamble/categories/group/additive_mors.py`.
This is a complete source owner pass. M1 / DEV-58 retains execution of
every specimen below under T; no import, test or runtime result is claimed.

### Defining datum, complete inventory and weaker identity home

The datum is a diagonal Mor E = Hom_C(M,M) in an R-linear category, with
the actual commutative unital scalar ring R and R-bilinear composition.
The ring product is f*g = f composed with g; addition and negatives are
pointwise; 1_E is id_M; and r acts through r*id_M. Associativity follows
from function composition, distributivity from the admitted additive-map
laws, and centrality from R-linearity. Neither faithfulness of the scalar
action nor commutativity of E is assumed.

The complete old direct inventory is `an_object`,
`_repr_object_names`, `super_categories`, and the parent suppliers
`_compose_endomorphisms`, `_owned_scalar_multiple`, and `identity`.
There is no direct element method, fixed-Mor declaration or arrow operation.
The category now states its commutative-ring parameter through
`parameter_category`; the example remains the regular rank-one module's
End over that literal ring; the name and actual two supercategories remain.

Composition and scalar action stay at this enriched diagonal owner as
abstract supplier contracts. The actual additive, group, linear, graded,
equivariant and cochain Mor hosts fulfil them. The single private
`_pointwise_endomorphism_composite` serves the additive/group realizations;
linear and component realizations preserve their stronger retained
premises through their actual constructors. A value-producing generic
method no longer shadows those suppliers. This uses the existing abstract
contract resolution, without a new dispatch registry or descendant switch.

Identity belongs to the actual categorical diagonal, independently of
additive enrichment. The duplicate public identity here is removed;
the actual AdditiveMor host supplies its missing cached, diagonal-guarded
identity, and existing set/group/module/cochain identity suppliers remain
authoritative. For the already represented finite set X = {a,b},
i = Sets().Mor(X,X).identity() satisfies i(a)=a, i(b)=b and i*i=i,
although this full set End has no selected additive-ring structure.
This is the true outside-owner assertion for that consolidation.

### Complete actual authored up-set and both arrow levels

All twenty-three strict authored providers and their definitions were read:

- `AdditiveMorGroups` supplies the pointwise abelian law of the target.
  `AdditiveGroups.AdditiveCommutative`, `AdditiveGroups`,
  `AdditiveMonoids`, `AdditiveSemigroups`,
  `AdditiveMagmas.AdditiveCommutative` and `AdditiveMagmas` supply
  commutativity, additive inverses, zero, associativity and the binary law.
- `Algebras.Associative.Unital`, `Algebras.Associative`,
  `Algebras.Unital` and `Algebras` supply the actual scalar module,
  bilinear multiplication, associativity and two-sided unit.
  `Modules(R)` selects `ModulesOverCommutativeRings`, with the
  retained R-action and abelian additive law.
- `OwnedRings` has the actual `OwnedSemirings` and `OwnedRngs`
  branches; both reach `OwnedNonUnitalSemirings`, with distributivity
  and the additive/multiplicative laws. `Monoids`, `Semigroups`,
  `Magmas.Unital` and `Magmas` supply the multiplicative unit,
  associativity and binary operation.
- `Sets` supplies the underlying set and its fixed Mor; `Objects`
  is the root. Generated axiom meets carry these definitions and do not
  create additional authored providers.

An element f of E is a map M -> M, not an algebra map E -> E. Actual
AdditiveMor arrows inherit AdditiveMorphism and the additive-monoid,
additive-magma and owned-set providers. Actual group Mor arrows inherit
GroupMorphism and the monoid, unital-magma, magma and set providers.
Ordinary, auxiliary, matrix, tensor-syntax and divided-square-syntax
module Mors inherit the actual ModuleMorphism providers; the latter two
remain ordinary linear Hom, not form-preserving subspaces.
Graded, equivariant and cochain fixed Mors supply their respective stronger
arrow laws and inherit the actual weaker linear/additive/set providers
through the fixed-Mor supercategory construction.

The existing module-Mor initializer now carries the explicit construction
datum `full_linear_mor`: whether a full-linear-Hom realization is supplied. Ordinary, auxiliary, tensor-syntax and
divided-square-syntax Mors are full linear Hom. Graded and cochain Mors
instead select the pointwise centre module and diagonal endomorphism
algebra, without claiming the full coordinate Hom basis or model merely
from framed endpoints. For two free rank-one pieces in distinct degrees
0 and 1, graded End is R direct-product R: the cross-degree matrix units
are excluded. For C^0=C^1=ZZ and d=2, the degreewise pair (a,b) must also
satisfy 2a=2b, so cochain End is the diagonal copy of ZZ. These are true
separating assertions for the full-Hom computation hypothesis; ordinary
linear Hom retains its existing selected matrix and presentation routes.
These extra equations can be vacuous; no claim of a universally proper
submodule is made.

A map E -> F preserving the R-algebra structure instead uses the actual
UnitalAlgebraMorCategoryConstruction and its selected
UnitalMultiplicativeAlgebraMor, retaining the underlying linear map,
multiplicativity and unit law. RingMor supplies the corresponding ring
arrow when that theory is requested. The generated arrow type, rather
than resemblance between Python method names, delivers those providers.

The selected noncommutative matrix case required correction at this
boundary. MatrixEndomorphismSpaces(S) now declares its actual
AdditiveEndomorphismRings(Z(S)) ancestor and selects the existing unital
algebra Mor in both coefficient branches. Its objects already retained
this centre algebra through the ordinary module-Mor constructor.
For S=M_2(QQ) and E=End_S(S), id_E+id_E sends 1_E to 2*1_E,
so unit-preserving arrows E -> E cannot themselves be an additive Mor.
The selected algebra Mor has the correct carrier and its pointwise sums
forget to the ordinary linear Mor. This asserts Z(S)-linearity, never an
S-algebra structure. The now-unselected legacy MatrixEndomorphismMor
declaration remains for its separately queued full retirement/reconciliation
pass; direct legacy construction is not the selected route accepted here.

### Exact coefficients and preservation through the selected suppliers

Ordinary Hom_S(M,N) retains Z(S), including S itself when commutative.
The LinearMorModules accessor now reads that constructor datum instead of
recomputing a centre from its endpoints. An equivariant Mor can instead
retain Z(R) for its chosen coefficients R in S=R[G]. For R=QQ and G=C2,
that datum is QQ even though Z(QQ[C2]) is the larger QQ[C2].
Every actual ordinary, auxiliary, matrix, graded and cochain initializer
sets the datum before placement; GroupModuleMor sets its selected
coefficient centre explicitly.

For noncommutative coefficients, scalar evaluation uses the literal
retained ring centre's inclusion Z(S) -> S before the module action.
A differently realized magma/algebra centre is not substituted.
Equivariant arithmetic delegates to the retained coefficient-module maps,
so its existing coefficient inclusion R -> R[G] remains exact.
The underlying coefficient arrow is returned itself, with its endpoints
and linearity decision, rather than reconstructed as an unconditionally
linear callback. R[G]-linearity conjoins that coefficient linearity
with equivariance; these are not interchangeable decisions.

Module addition/subtraction and scalar multiplication require an already
admitted arrow in the actual Mor, or a genuine scalar multiple of the
identity. They do not send a weaker arbitrary set map through the explicit
constructor to invent another linearity premise. Identity shortcuts
require a decision literally True. Map-valued scalars remain scalars
unless they are actual composable maps.

Ordinary arithmetic retains the actual input linearity premises. Graded
arithmetic additionally retains degree-preservation premises; equivariant
arithmetic retains its own equivariance premises. A merely linear
construction does not acquire equivariance from the types of its inputs.
The cochain suppliers retain component formulas, the literal degree index,
and the actual cochain premises for addition, negatives, scalar action and
composition. Zero and identity have their construction proofs. These
formulas commute with the selected differentials when their input maps do,
so they need not invoke the generic differential checker to prove those
same laws again. Component normalization uses the ordinary S-linear Mor,
preserving the full selected Z(S) action on richer component realizations.
Unknown linearity, equivariance, degree and equality conditions remain
propositions; none is converted to a Boolean by this arithmetic.

### True closure assertions retained under T

1. On QQ^2, let i be the identity, s the coordinate swap, P=E_11 and N=E_12.
   Then s*s=i, P*N=N, N*P=0, and 2*i commutes with every endomorphism.
   The multiplication classifier has exact domain E tensor_R E and codomain
   E, and the algebra's unformed module is that same E.
2. Use the actual presented module M=ZZ^2/<2e_2>, isomorphic to
   ZZ direct-sum ZZ/2, not a finite source. Define
   f(e_1)=2e_1, f(e_2)=e_2 and g(e_1)=3e_1, g(e_2)=e_2.
   Their images respect the relation 2e_2=0. The composite has images
   (6e_1,e_2), and 2*f has images (4e_1,0), still with proved linearity.
   For p(a,b)=(a,0) and q=i-p, p^2=p, q^2=q, pq=qp=0 and p+q=i.
3. On M=ZZ/2, 2*id_M=0 although 2 differs from zero in ZZ. Equality
   of scalar endomorphisms therefore does not imply equality of scalars.
4. For S=M_2(QQ) acting on its left regular module, f_a(s)=s*a is
   S-linear and f_a*f_b=f_(b*a). With a=E_11 and b=E_12,
   f_a*f_b=0 whereas f_b*f_a=f_E12. The central element 2I acts through
   the exact Z(S) -> S inclusion. Left multiplication by E_11 is not
   S-linear: E_11*E_12=E_12 but E_12*E_11=0.
5. Let R=ZZ[t] and M=R.free_module(1) with basis e. The same-endpoint
   additive/set map u(ae)=a(0)e is not R-linear. In fact
   (id+u)(te)=te while t(id+u)(e)=2te. Arithmetic in End_R(M)
   must not promote that weaker arrow. The explicit conditional map
   constructor remains available with its unresolved or refuted law.
6. The existing GradedModules(ZZ,ZZ) construction from the constant
   indexed family ZZ.regular_module() gives M = direct-sum_(n in ZZ) ZZ e_n,
   without a selected finite homogeneous generating family. For its
   identity i, (i+i)(e_n)=2e_n, (-i)(e_n)=-e_n, and (3i)(e_n)=3e_n,
   all with degree preservation proved by construction. The parent
   composition supplier sends (2i,3i) to 6i. The actual component
   projection p(sum a_n e_n)=a_0 e_0 gives p^2=p and 3p(sum a_n e_n)
   =3a_0 e_0; its arithmetic keeps the supplied degree and linearity laws.
   An ordinary elementwise identity rule u on the same module without its
   degree proof retains the proposition preserves_degree(u), including
   through arithmetic and reparenting. More generally an infinite-module
   callback with undecided represented linearity retains that premise.
7. For the cochain complex C with ZZ in degrees 0 and 1 and differential
   multiplication by 2, i has identity components, and 2*i has component
   2*id in each degree. Both sides of d(2*i)=(2*i)d are multiplication
   by 4, and (2*i)*(2*i)=4*i. These formulas retain the selected
   differential and components rather than replacing C by its cohomology.
8. Let C2 act on QQ^2 by diag(1,-1). Coordinate swap is QQ-linear,
   but does not commute with that action, so it is not QQ[C2]-linear.
   The coefficient forgetful map retains its QQ-linearity; the ordinary
   group-algebra-linear forgetful route also needs its equivariance law.
   An undecided equivariance law must therefore remain in that latter
   linearity decision. The exact QQ scalar datum of the equivariant Mor
   stays QQ, although QQ[C2] has a larger centre.
9. The matrix second-arrow separator above excludes false additive
   placement, while E=End_S(M) retains its genuine central algebra.

**Sources, review and named computation frontier.** The maintained
[Mathlib linear-endomorphism definitions and instances](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/LinearMap/End.html)
state identity/composition and the opposite-ring description of End_S(S).
The central-action construction is also in
[Mathlib Algebra.Basic](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Algebra/Basic.lean).
The explicit finite-matrix, relationful-module and cochain computations
above give their own expected values. A bounded read-only local
formalization-corpus search had no matching result; upstream primary
sources supplied the contract without making corpus work a prerequisite.

The complete owner, twenty-three ancestor definitions, native suppliers,
actual fixed-Mor paths, scalar actions and selected consumer constructors
were reviewed, with an independent review of the final source delta.
General infinite linear-map equality and arbitrary linearity decisions
remain propositions. Equivariance without determining data remains its
named proposition; unavailable general module computations retain their
existing computation assertions. The generic nonfinite cochain component
and differential-validation code is not invoked by the derived arithmetic
accepted here; its unresolved validation obligations remain with the
separate CochainMor owner. No generic differential algorithm is claimed.
This pass introduces no new prerequisite and does not close those
consumers' separate full-inventory owner rows. All displayed assertions,
existing relevant construction specimens and megadoc regeneration remain
execution obligations under T.

## Whole-category placement: AdditiveGroups (2026-10-11)

**Closed node:** `placement-owner-additivegroups`.
**Owner:** `AdditiveGroups` in
`src/dzack_research/preamble/categories/group/magmas.py`.
**Delta:** no source repair is required for the complete root inventory.
The selected laws and their actual providers already satisfy this pass.
The separately queued AdditiveCommutative refinement is not included here.
Execution of the following source assertions remains under T.

**Complete direct inventory.** The root introduces
`_MorCategory.fixed_category_class`, selecting AdditiveMonoidMor;
`an_object`, returning the owned integers;
`super_categories`, returning AdditiveMonoids; and the element operation
`_sub_(x,y) = x + (-y)`. It introduces no root parent operation or arrow
method. The existing megadoc was used only as an index; the complete live
declaration and actual providers determine this inventory.

**Complete authored up-set.** The five strict ancestors were read in full:
AdditiveMonoids supplies the selected zero, monoidal_unit=zero and the
additive-monoid Mor; AdditiveSemigroups supplies associativity and the
additive-magma Mor; AdditiveMagmas supplies the selected binary addition;
Sets supplies owned sets, element ingress and its fixed set-Mor provider;
Objects is the root category/packet infrastructure. The nested
AdditiveMagmas.AdditiveCommutative axiom is a separate refinement, not a
law imposed on root AdditiveGroups.

The right difference belongs here because associativity and inverses give
(x+(-y))+y=x, x-x=0 and x-0=x for every admitted x,y. Commutativity is
unnecessary. In multiplicative notation the formula is x*y^(-1), in that
order. A monoid alone cannot supply this operation uniformly: the
natural-number additive monoid has no u with 1+u=0. No operation is moved
in this pass, so no new-home specimen obligation is invented.

**Actual fixed Mor and arrows.** AdditiveGroups and its immediate
AdditiveMonoids ancestor select the same fixed class AdditiveMonoidMor.
The common Mor-family construction reuses the inherited fixed Mor with
the literal endpoints. Its generated arrow reaches the actual
AdditiveMonoidMorphism, AdditiveMagmaMorphism and OwnedSetMorphism
providers; this is generated ancestry, not a static Python inheritance
claim. An additive-monoid map f between groups preserves inverses:
f(a)+f(-a)=f(a+(-a))=f(0)=0, so f(-a)=-f(a). Therefore
f(a-b)=f(a)-f(b), and no stronger arrow implementation is needed.
The existing identity and operation-preserving composition retain the
literal endpoints and the admitted map law. Root AdditiveGroups does not
supply the commutative refinement's separate pointwise AdditiveMor.

**Selected primitive and consumer review.** Native owned rings retain
their actual parent and native addition/negation. GeneralModules retains
its given addition, zero, inverse and scalar action. Sparse free modules
keep finite coefficient data and discard a coefficient only when its
vanishing is literally True. Presented modules add and negate in the
retained cover and preserve unresolved relation membership. Localized
modules use m/s+n/t=(t*m+s*n)/(s*t) and -(m/s)=(-m)/s.
Restricted-scalar modules retain the underlying additive elements;
function modules use their existing pointwise closure constructor; graded
direct sums act componentwise and retain undecided zero components.
Fractional ideals inherit the ambient field's additive law, and
fraction-field quotients retain their quotient representatives and
quotient equality. Additive, group and module-Mor suppliers include the
premise-preserving ingress accepted in the preceding End pass.

**True closure assertions.**

- In the owned integers, 7-10=-3, z+(-z)=0 and 0+z=z, in the same
  parent. On ZZ^2, (u-v)+v=u.
- In the existing FractionFieldQuotients(ZZ)(2), namely QQ/2ZZ,
  [1/2]+[1/3]=[5/6], [1/2]-[1/3]=[1/6], and
  -[1/2]=[-1/2], all in the same quotient parent.
- The admitted doubling additive map d on ZZ preserves subtraction:
  d(7-10)=d(7)-d(10)=-6. Its identity/composition and source/target
  data use the actual additive-monoid Mor providers.
- An undecided coefficient equality, cover-relation membership or
  localized equality remains its original proposition through these
  operations. Subtraction invokes addition and inverse; it does not
  decide that proposition or require a new decision algorithm.

The full provider review includes magmas.py and additive_mors.py; the
fixed-Mor and generated-arrow construction in abstract_categories;
ring_foundation.py; general_modules.py; framed_free_modules.py;
finitely_presented_modules.py; localizations.py; the restricted-scalar
provider in pure/modules.py; function_modules.py; graded_direct_sums.py;
fractional_ideals.py; and fraction_field_quotients.py. The existing
test_additive_groups_construct.sage, test_general_modules_construct.sage
and fraction-field-quotient arithmetic specimens were read only.
Independent source review accepted this no-delta root pass. There is
no new computation frontier: primitive addition/zero/inverse are the
supplied structure, and the existing undecided cases remain propositions.
No runtime, import, Sage, test or build was run.

## Whole-category placement: AdditiveGroups.AdditiveCommutative (2026-10-11)

**Node:** `placement-owner-additivegroups-additivecommutative`.
**Owner:** `group/magmas.py: AdditiveGroups.AdditiveCommutative`.
**Delta:** both public multiplicative-notation operations now belong to
`AdditiveGroups.ParentMethods`; their existing commutative GroupExp realization
retains the proved commutativity of its output and the literal additive input.
The returned group's inequality preserves undecided equality. The complete
source pass closes this owner; the two nested Mor-construction passes retain
their own rows.

### Complete inventory and authored up-set

The starting owner introduced exactly two parent operations,
`multiplicative_group_identification()` and `multiplicative_group()`, the
nested `_MorCategory.fixed_category_class()` selector, and the category display
name `_repr_object_names()`. It introduced no element operation, independent
constructor, extra supercategory, or arrow operation. The notation methods move
together. The selector and display name remain with the commutativity axiom.

All seven strict authored ancestor definitions were read, together with the
owned axiom and category-packet machinery:

| Authored ancestor | Mathematical data and hypotheses |
| --- | --- |
| `AdditiveGroups` | An associative additive law, its zero, and two-sided additive inverses; addition need not commute. Right difference is `a + (-b)`. |
| `AdditiveMonoids` | An associative additive law with its specified zero. |
| `AdditiveSemigroups` | An associative additive binary law. |
| `AdditiveMagmas.AdditiveCommutative` | A binary additive law satisfying `a+b=b+a`, with no associativity or inverse supplied by that axiom. |
| `AdditiveMagmas` | A selected additive binary operation on a set. |
| `Sets` | A carrier and maps of carriers, without an additive law. |
| `Objects` | The mathematical root, without additional structure. |

The actual `CategoryWithAxiom` provider at AdditiveMagmas implements
AdditiveCommutative and propagates through the stronger additive categories.
The remaining runtime scaffolding supplies no additional mathematical
hypothesis. The existing megadoc was used as an index and the live definitions
were authoritative; regeneration remains under T.

### Mathematical home and true separating assertions

For every additive group A, its multiplicative notation E(A) has elements
e(a), multiplication e(a)e(b)=e(a+b), identity e(0), and inverse e(-a).
The functions e and log are inverse maps of the exact carriers. Associativity,
the identity laws and inverse laws follow respectively from those of A;
commutativity is unnecessary. The construction is stated independently in
[Mathlib's additive/multiplicative type tags](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/TypeTags/Basic.html):
`Multiplicative.group` assumes `AddGroup`, while `ofAdd_add`,
`ofAdd_neg`, `ofAdd_sub`, `toAdd_ofAdd` and `ofAdd_toAdd` express the
corresponding laws.

The weakest authored ancestor supplying a *group* as output uniformly is
AdditiveGroups. The additive monoid NN has no inverse for 1, so its unchanged
carrier with the transported addition is not a group. Merely changing notation
on an additive magma would similarly supply neither associativity nor inverses.

The outside-old-owner specimen is the mathematical carrier S3 in additive
notation: a+b means a composed with b, zero is the identity permutation, and
-a is its inverse. Under right-to-left composition, s=(12) and t=(23) give
s+t=(123) and t+s=(132), so this is an additive group outside the commutative
refinement. Its transported group satisfies all of

- log(e(s))=s and e(log(e(t)))=e(t);
- e(s+t)=e(s)e(t), with no order reversal;
- e(0)=1 and e(-s)=e(s)^(-1);
- e(s-t)=e(s)e(t)^(-1).

These are assertions of mathematics, not a claim that the repository already
constructs a noncommutative additive S3. The bounded owned-constructor search
found no such realization. The public methods now exist at the general owner;
an input without the selected commutative realization reaches the named
multiplicative-notation computation assertion. No category label is used to
fabricate the missing law or engine.

### Selected realization, exact maps, and current consumers

The owner selects the existing GroupExp realization on known commutative
additive groups and states the unavailable general realization in its final
computation case. A missing known commutative placement is not evidence that
addition is noncommutative. `_AdditiveGroupForGroupExp` retains the literal A
and delegates its zero, admission and elements. The maintained
[Sage GroupExp implementation](https://github.com/sagemath/sage/blob/develop/src/sage/groups/group_exp.py)
wraps those additive elements; its multiplication wraps a+b and its inverse
wraps -a. The adapter now supplies the commutative owned-group refinement,
justified by a+b=b+a, without deciding arbitrary equality.

The cached identification retains its exact endpoints A and G. Its forward
map constructs the engine's wrapper of the admitted a; its backward map reads
that wrapper's retained additive value and returns it through A. The existing
`Sets().Core().Mor(A,G)._from_known_inverse_pair` carries the two actual maps.
`multiplicative_group()` returns that same identification's codomain.
The identification is a set isomorphism respecting the displayed two
notations, not an additive morphism into a multiplicatively presented group.

For A=ZZ, e(2)e(7)=e(9), e(0)=1, e(-2)=e(2)^(-1), and log(e(7))=7.
The output is a commutative owned group. For A=ZZ^2 the same statements hold
componentwise, including e((1,0))e((0,1))=e((1,1)).
`AffineModuleFibres.torsor` still uses its *entire* translation module K,
its actual inclusion i, its selected origin p0 and the exact inverse lift:
g maps to p0+i(log(g)), and p maps to e(i.lift(p-p0)).
These maps are inverse because i.lift inverts i on that fibre difference.
No finite generating span or replacement translation object is introduced.
For the Z-linear map L:QQ^2 -> QQ, L(s,t)=s+t, and j:ZZ -> QQ,
the full translation module is K=ZZ(1,0)+QQ(1,-1). All rational kernel
vectors remain in K; an integral generating span would give a false fibre.

### Delivered Mor inheritance and undecided propositions

The refinement's actual fixed selector remains `AdditiveMor`.
For literal endpoints A,B it retains A, B, the owned integer scalar ring,
the existing integer multiplication action on B and the supplied additive map.
The diagonal is AdditiveEndomorphismRings(ZZ); off the diagonal it is
AdditiveMorGroups. The actual generic `MorCategoryConstruction.Of` builds
this selected fixed class and its generated arrow providers reach
AdditiveMorphism, AdditiveMonoidMorphism, AdditiveMagmaMorphism and
OwnedSetMorphism. The root additive-group selector is the different
AdditiveMonoidMor class: there is no claim that these two fixed parents are
literally identical.

Composition remains left(right(a)); integer scalar identity is the actual
integer evaluator. Pointwise addition and negation retain the commutative
target hypothesis. They do not move with notation conversion: on S3 the
pointwise sum of id with itself sends g to g^2; it is not a homomorphism,
since s^2=t^2=1 but (st)^2=(132) is not 1.

For a represented undecided case take M=ZZ.regular_module(), as its distinct
free rank-one module rather than the literal integer-ring carrier, and
A=AdditiveGroups().AdditiveCommutative().End(M). Separate valid elementwise
identity callbacks f,g agree mathematically, but their existing general
infinite-domain equality remains an AtomicProposition. Sage's
[ElementWrapper comparison](https://github.com/sagemath/sage/blob/develop/src/sage/structure/element_wrapper.pyx)
returns the wrapped equality object; the owned group retains it.
The corrected inequality returns its logical negation, preserving both
decided cases and the undecided proposition without Boolean coercion.
No equality decision is inferred from the supplied map laws.

**Source grounding:** the project/global vault search for additive/multiplicative
notation found the completed structured-spines plan and the older flat-axiom
stub decision; both were read. They add no selected general notation realization.
A dated bounded search of the available formalization corpus for GroupExp,
Multiplicative.group and the additive type-tag laws found no local match;
the upstream primary type-tag declarations above supply their exact hypotheses.
That scoped miss is not a claim that the mathematics is unformalized, and no
other repository's progress is an acceptance dependency.

**Verification and frontiers:** independent full-owner source review and focused
`git diff --check` cover the two source files and this closure record.
M1 / DEV-58 permits no runtime claim: existing immutable assertions, the
commutative conversion, the exact affine torsor and unknown-equality specimens
remain under T and core-usability-session. The general additive-group
realization is explicitly unavailable at its named computation assertion.
No new prerequisite, engine, test expectation, or external repository gate
was introduced.

## Whole-category placement: AdditiveGroups.AdditiveCommutative._MorCategory (2026-10-11)

**Node:** `placement-owner-additivegroups-additivecommutative-morcategory`.
**Owner:** the nested declaration in `group/magmas.py`.
**Delta:** the selector retains the existing enriched AdditiveMor at its valid
home. Its own Mor exposed an endpoint inconsistency: a raw fixed-Mor input
could select the correct functor category but be recorded under raw keys while
the result held Cat.object endpoints. The shared _MorCategoryOf boundary now
uses the existing Cat.object representation before selecting and recording
that family Mor. This source repair is required by this node's actual
higher-arrow and exact defining-data assertions.

### Complete inventory, ancestry, and selected construction

The entire direct body selects AdditiveMor. It declares no other operation,
datum, ParentMethods, ElementMethods, arrow predicate, or family constructor.
Its implementation bases are MorCategoryConstruction (whose body is empty),
_MorCategoryOf and the owned plain-category infrastructure. The complete
authored semantic up-set of this family is MorCategories, then Cat:
MorCategories classifies the actually constructed fixed-endpoint Mor
categories; Cat classifies categories and their functors. Cat's declared
supercategory is the Sage Objects runtime substrate, not an authored
owned-Objects edge. The separate CategoryObject representation reaches
Objects.ParentMethods. These distinct paths are not conflated.

The complete definitions of _MorCategoryOf, MorCategories and Cat were read,
including their construction, endpoint and arrow operations. The underlying
object theory's seven authored ancestors are separately those recorded in
the preceding AdditiveGroups.AdditiveCommutative pass; they are not extra
semantic supercategories of the classifying family.

For A,B in commutative additive groups, the selected object consists of
homomorphisms A -> B, with pointwise abelian-group arithmetic. Its diagonal
also has composition and identity, with the canonical integer action.
[Mathlib's Hom instances](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/Instances.html)
state the commutative-target hypothesis and the corresponding pointwise
group and integer actions. That hypothesis is not supplied by a general
Mor category. On additively written S3, the pointwise sum of id with itself
is g -> g^2, and distinct transpositions s,t satisfy (st)^2 != s^2 t^2.
The commutative enrichment therefore cannot move uniformly to the root
additive-group selector.

The shared Of construction retains the literal base category and endpoints,
selects the fixed class and reuses an inherited parent only when that parent
has the selected class. Its cache and endpoint verification use identity;
family membership reads the actual construction record. AdditiveMor retains
owned ZZ, the existing IntegerMulAction, the admitted additive evaluator,
AdditiveMorGroups off the diagonal and AdditiveEndomorphismRings(ZZ) on the
literal diagonal. No endpoint equality decision or scalar reconstruction
stands in for those data.

### The family's own Mor retains the actual functor category

For F=AdditiveGroups().AdditiveCommutative().MorCategory() and
H=F.Of(ZZ,ZZ), let p=Cat().object(H). The complete ordinary ingress now
satisfies the source assertions

- F.MorCategory().Of(H,H) is F.MorCategory().Of(p,p);
- the returned category belongs to F.MorCategory();
- its literal domain_object and codomain_object are p, whose retained
  represented_category is H.

The selected result remains Cat's actual _FunctorCategory [H,H], whose
arrow_set is CategoryFunctorMor with CategoryFunctorMorphism arrows.
Those arrows retain their actual Functor and its category endpoints;
Cat().identity(H) acts identically on H's objects and morphisms.
The own Mor of the functor category still holds natural transformations,
not a substituted discrete relation. Existing functor equality keeps
factor identities when known and an equality proposition otherwise.

The override belongs to the shared _MorCategoryOf protocol: every object
of such a family is a category. Already represented endpoints keep identity.
Ordinary F.Of(A,B) still normalizes A,B through F.base_category(), so the
integer/module/group endpoints of the selected additive Mor do not change.
The same assertion applies outside this owner to Sets().MorCategory()
and a fixed SetMor on the two-element set. No additive law is supplied
or presumed at that outside-owner boundary.

### Actual additive arrows and closure assertions

The actual fixed-Mor graph generates the arrow type from AdditiveMorphism,
AdditiveMonoidMorphism, AdditiveMagmaMorphism, OwnedSetMorphism and the
CategoricalMor/Sage Morphism root. Neither selected fixed class uses the
legacy Element bypass. This is generated provider inheritance, not static
inheritance between the standalone mixins. The weaker root selector requests
AdditiveMonoidMor: its parent is not identified with this enriched AdditiveMor.

For H=AdditiveGroups().AdditiveCommutative().Mor(ZZ,ZZ), the supplied scalar
arrows H(2), H(3) and the canonical identity satisfy

- H(2)(n)=2n, H(3)(n)=3n, and id(n)=n;
- (H(2)+H(3))(n)=5n and (H(2)*H(3))(n)=6n;
- the selected zero and negative give (H(2)-H(2))(n)=0.

For an additive group of exponent two, 2 id=0 despite 2 != 0 in ZZ.
The retained scalar comparison therefore never turns unequal coefficients
into a proof of unequal maps. Equality on the literal source ZZ compares
images of 1; target equality may still be undecided. For other infinite
sources without the selected enumeration, equality remains its proposition
and inequality its logical negation. The current canonical identity and
pointwise construction retain their defining maps, not replacement callbacks.

**Verification and retained frontiers:** independent complete source review
and focused source/record diff checks discharge this owner pass. The bounded
formal-corpus filename search had no local result; the upstream primary
definitions fix the stated hypotheses. No new algorithm or prerequisite
is introduced. General map equality, injectivity, surjectivity and inverse
computation retain the existing set-map frontiers; an inherited set inverse
is not claimed to return an enriched additive arrow. All execution remains
under T and core-usability-session, with tests unchanged. Direct raw-endpoint
MorCategories().Mor(H,K) is a distinct remaining entry: that category does
not use the family override. Its same endpoint inconsistency is recorded
inside the existing placement-owner-morcategories row and COMPLAINTS.md;
this pass does not claim all category-of-categories ingress is repaired.

## Whole-category placement: AdditiveGroups._MorCategory (2026-10-11)

**Node:** `placement-owner-additivegroups-morcategory`.
**Owner:** the nested declaration in `group/magmas.py`.
**Delta:** complete source review closes the existing AdditiveMonoidMor
selection, including its actual inherited additive arrows and the family's
own functor arrows. No additional source change is needed after the shared
family endpoint repair in the preceding owner pass.

The entire direct inventory is `fixed_category_class()`, returning
AdditiveMonoidMor. It introduces no independent parent or element methods,
constructor, parameter, arrow law, or computation algorithm.
MorCategoryConstruction has an empty body; _MorCategoryOf supplies the
complete common family construction. Their owned infrastructure is not
another mathematical hypothesis. The complete authored semantic up-set of
the family is MorCategories (constructed fixed-Mor categories) and Cat
(categories and functors). Cat names only the Sage Objects runtime edge;
CategoryObject separately reaches the owned object implementation.
Those complete definitions and the common selection, cache, membership and
arrow construction were read. The underlying AdditiveGroups object's five
authored ancestors are accounted for in its earlier root pass.

A homomorphism of additive monoids between groups automatically preserves
inverses: f(x)+f(-x)=f(0)=0 and f(-x)+f(x)=0, so uniqueness of the
two-sided inverse gives f(-x)=-f(x). Hence f(x-y)=f(x)-f(y) without a
commutativity hypothesis.
[Mathlib's homomorphism definitions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/Defs.html)
use AddMonoidHom for these maps and state map_neg and map_sub under those
group hypotheses. A separate additive-group-arrow class or inverse datum
would duplicate that existing theory.

The fixed Mor therefore literally reuses the AdditiveMonoids parent when
the shared Of constructor selects its same AdditiveMonoidMor class and
literal endpoints. Its generated arrow providers reach
AdditiveMonoidMorphism, AdditiveMagmaMorphism, OwnedSetMorphism and the
CategoricalMor/Sage morphism root. This is actual generated provider
inheritance. The commutative refinement selects the different AdditiveMor
and its pointwise Hom enrichment; the two fixed parents are not identified.
No commutative pointwise addition law is asserted for the root Hom.

For K=AdditiveGroups().Mor(ZZ,ZZ), admit f(n)=2n and g(n)=3n as actual
homomorphisms. Its defining maps satisfy f(0)=0, f(-n)=-f(n),
f(n-m)=f(n)-f(m), (f*g)(n)=6n, and identity(n)=n.
In particular f(7-10)=-6=f(7)-f(10). The same weaker selected
additive-monoid owner serves doubling on NN, which is outside AdditiveGroups.
These are pointwise assertions, not claims that fresh callback expressions
have been decided equal. An already admitted exact-endpoint arrow is
preserved; wrong literal endpoints are rejected. Callable ingress supplies
its homomorphism law as mathematical data, not as an executed function-law
test.

The family's own Mor is also accounted for. Let F=AdditiveGroups().MorCategory(),
H=F.Of(ZZ,ZZ) and p=Cat().object(H). The shared endpoint repair gives

- F.Mor(H,H) is F.Mor(p,p) is Cat().Mor(H,H);
- the result's exact domain_object and codomain_object are p;
- the result is in F.MorCategory(), and F.End(H) is F.Mor(H,H);
- after that End construction the same result belongs to F.EndCategory().

The result is the actual functor category [H,H]. Its arrow_set is the
existing CategoryFunctorMor holding CategoryFunctorMorphism and the
retained Functor; its internal Mor still contains natural transformations.
The identity functor acts identically on each actual object and arrow of H.
Ordinary group endpoints in F.Of(A,B) continue through F.base_category(),
so this higher normalization does not replace the additive carriers.

**Retained computations:** the root arrow inherits set-level equality,
not AdditiveMorphism's special comparison on source ZZ. General infinite
source equality may therefore remain a proposition; inequality retains
logical negation. Injectivity and surjectivity keep their existing
predicate frontiers. The selected finite bijection inverse returns its
actual map in Sets().Mor(B,A); no stronger inverse-arrow placement is
claimed. The direct raw MorCategories ingress remainder remains in its
existing node and complaint, not in this already repaired family entry.

**Verification:** independent complete source review and focused record
diff checks; no source imports, tests or runtime execution. The formal-corpus
search was a scoped local miss; the primary homomorphism statements above
fix the mathematical hypotheses. No new prerequisite or computation
assertion is introduced. The displayed source assertions and existing
immutable specimens remain under T and core-usability-session.

## Whole-category placement: AdditiveMagmaMor (2026-10-11)

**Node:** `placement-owner-additivemagmamor`.
**Owner:** `group/additive_mors.py:AdditiveMagmaMor`.
**Delta:** reuse the existing canonical set-identity computation and repair
the actual weaker-map branch of the shared composition supplier. Both
changes serve this complete owner pass.

The entire direct inventory is ElementMethods=AdditiveMagmaMorphism,
_element_constructor_(datum), and identity. The selected arrow provider
introduces exactly its callable-preserving __init__ and _composition.
The existing _additive_operation_mor_element remains the constructor
supplier; no separate map representation or additive-law decision is added.

For H=AdditiveMagmas().Mor(A,B), the complete strict authored semantic
up-set is the fixed Sets Mor, the fixed Objects Mor, and Objects.
Their actual definitions, together with the complete relevant common
CategoricalMor, OwnedMor, UnderlyingSetMor and category-packet construction
routes, were read. Runtime Category/Homset bases do not add mathematical
hypotheses. The generated arrow actually gathers AdditiveMagmaMorphism,
OwnedSetMorphism and the common CategoricalMor/Sage morphism providers.
The inherited application, comparison, logical inequality, hash, images,
injection/surjection predicates and finite inverse therefore reach their
declared set-level suppliers.

A map at this owner preserves only the selected binary law:
f(x+y)=f(x)+f(y). Associativity, a zero and commutativity are unnecessary.
[Mathlib's AddHom definitions](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Hom/Defs.html)
give precisely this boundary, including identity and composition.
The scoped local formal-corpus search was a dated miss, not evidence that
the theory is absent. The mathematical placement is fixed by the actual
law and the primary definitions.

The old identity body constructed a fresh callback arrow each time. The
inherited is_identity diagnostic recognizes the canonical identity by
literal identity before considering extensional equality, so that duplicate
body lost a decided result on an infinite source. The owner now uses
SetMorCategory.__dict__["identity"]. This is the existing cached descriptor
under its original name, with its existing diagonal-endpoint check and
self.element_class(self, lambda element: element) body. It constructs this
Mor's actual additive arrow and caches it here.
[Sage's CachedMethod documentation](https://doc.sagemath.org/html/en/reference/misc/sage/misc/cachefunc.html)
distinguishes the raw class-dictionary descriptor from class attribute
lookup's cached-method caller. The same-name reuse does not rename a
cache. AdditiveMagmaMor still has its CategoricalMor host; the full
FunctionSets initializer of SetMorCategory is not imported into this Hom.

Let Z=AdditiveMagmas().an_object(), the actual owned integer ring, and
H=AdditiveMagmas().Mor(Z,Z). For i=H.identity(), the source gives

- i is H.identity(), i.parent() is H, and both endpoints are literally Z;
- i(n)=n and i.is_identity() is True, without enumerating Z;
- the attached End role obtains this same canonical arrow as its
  composition unit through the existing arrow_set().identity() ingress.

The weaker-home specimen is the existing finite ordered set of labels
("a","b"). Its set-Mor identity fixes both labels and has decided
is_identity() is True without any additive law on that carrier.
This is the same mathematical identity computation.

Composition retains the same operation-preserving supplier. Its new first
condition tests right.parent() in MorCategories() before reading
right.parent().mor_family(). The actual root Objects fixed-Mor arrow_set
is UnderlyingSetMor, whose parent has no mor_family. Such a map now reaches
the existing OwnedSetMorphism fallback; it is not declared additive by
same endpoints or by available method names.

For f(n)=2n and g(n)=3n admitted in H, (f*g)(n)=6n and the composite
has the canonical additive Mor parent and literal endpoints. For the
existing root arrow
q=Objects().Mor(Z,Z).arrow_set()(lambda n: n*n), the composite f*q
is the actual set map h(n)=2n^2 in Sets().Mor(Z,Z). It is not additive:
h(1+1)=8 whereas h(1)+h(1)=4. Its defining function and endpoints
are unchanged. A mismatched intermediate endpoint still returns the
existing NotImplemented result through the binary protocol.

Admission and construction remain distinct. H.accepts(g) checks literal
endpoints and actual declared parent ancestry. Public H(g) returns a
single already-admitted morphism literally through CategoricalMor.__call__,
including a stronger arrow whose real Mor graph reaches H. If the
protected constructor is reached with another same-endpoint morphism,
it retains datum.__call__ in a newly constructed arrow under the caller's
additive-law premise. An arbitrary set arrow does not gain membership
from that possible explicit construction. Noncallable data and wrong
literal endpoints retain their existing rejections.

The fixed category's own Mor still uses its existing discrete second-level
construction. At the same retained arrow object H.object(f), its internal
Mor has the canonical identity 2-arrow from MorArrowDiscreteMor and
MorArrowIdentity. The common generated first-level arrow path and this
second-level route were both inspected. This is separate from the
classifying family's own Cat functors and natural transformations.
No additional equality decision about separately supplied arrow objects
is asserted.

**Retained computations:** arbitrary infinite-source callback equality
remains the inherited owned proposition; inequality is its logical
negation, and hashing retains its existing endpoint data. Finite
extensional comparisons and the existing finite injection/surjection
decisions are unchanged. General injectivity and surjectivity retain
their predicates. The finite decided-bijection inverse remains an actual
set map in Sets().Mor(B,A); unavailable bijectivity computations retain
their existing assertion under T. No additive inverse-arrow result is
claimed. The separate AdditiveMonoidMor identity body remains an obligation
of its existing queued owner, not an unrecorded closure here.

**Verification:** independent full source and mathematical review accepted
the settled two-file delta. Focused source/record diff and TODO graph
checks pass. No imports, tests or runtime execution were performed. The
displayed source assertions and existing immutable specimens remain under
T and core-usability-session; no new prerequisite was filed.


## Step-3 duplicates (survey 2026-10-10; fixed inventory)

**Survey evidence and denominator:** `.tmp/step3-duplicates.txt` (identical AST-body groups) and `.tmp/step3-same-name.txt` (same-name operation survey), both from the full default `src, tests` population, source digest `fd4d76d2650d0baf2d906a065c1fe7c77482292db180547bd2f68f95063d482b`. The 14,513 declarations were grouped into 6,534 operation spellings, including 1,475 same-name groups; the complete same-name group index is `.tmp/step3-same-name-index.txt`. All same-name groups and AST-body groups have been screened. Pure spelling coincidences, generic category methods with different targets, intentionally dual constructions, and already-delegating wrappers do not create checklist items. The 18 rows below are the fixed Step-3 consolidation denominator. Repair them in list order at their mathematical owners without restarting the survey.

- [x] The exterior-degree word normalization `degree=0 -> (), degree=1 -> (label,), higher -> tuple(label)` now has one implementation in `modules/powers.py:_exterior_word`, with Cartan calculus, de Rham and Hodge callers importing the shared operation. No duplicate independent implementations remain.
- [x] `BilinearFormModules.FinitelyPresented.Torsion.ParentMethods.primary_components` and `QuadraticFormModules.FinitelyPresented.Torsion.ParentMethods.primary_components` now delegate to `_primary_form_component_family` at their common form-bearing owner, constructing the invariant-factor-prime index and associated primary parts once while each form type retains its own `primary_part` construction.
- [x] `_FiniteAtlasModuleGluingDatumEngine._transition_images` and `_FiniteAtlasAlgebraGluingDatumEngine._transition_images` now delegate to the shared `_ordered_transition_images` chart-pair normalization in `schemes/gluing.py`, preserving their separate module/algebra transition data.
- [x] `CategoricalMor.attach_end_family` and `FixedMorCategory.attach_end_family` (likewise their `attach_aut_family` methods) in `abstract_categories/mor_categories.py` now delegate to shared family-attachment helpers. The two Mor representations preserve their public routes while sharing the endomorphism/automorphism family attachment and uniqueness checks at the common owner.
- [x] `BilinearFormModules.FinitelyPresented.Torsion.ParentMethods` and `QuadraticFormModules.FinitelyPresented.Torsion.ParentMethods` delegate `orbit`, `orbits`, `orbits_on_subobjects`, `orbits_on_isotropic_subobjects`, and `metabolizer` to one set of finite-form action operations in `modules/framed/formed/form_modules.py`. Bilinear and quadratic form construction, isotropy predicates, and Lagrangian computations remain distinct.
- [x] `_ProjectiveSpaceLineBundleEngine.homogeneous_polynomial_comparison` and `_ProductProjectiveLineBundleEngine.homogeneous_polynomial_comparison` now share `_homogeneous_section_identity_comparison` for the owned section module. Both line-bundle models and their distinct section multiplications remain unchanged.
- [x] `AdditiveMagmaMorphism._composition` and `MagmaMorphism._composition` now delegate their identical endpoint/category compatibility and composite function construction to `_compose_operation_preserving_mor` at the common categorical Mor owner. Both additive and multiplicative ingress contracts and their fallback to weaker Mor composition remain distinct.
- [x] `QuadraticModuleMor.from_quadratic_map.generator_image` is the sole implemented generator-level polarization formula. `DividedSquareModules.ParentMethods.from_quadratic` already delegates to the former through its module Mor; its second `generator_image` was unreachable and is removed, preserving both outward factoring operations.
- [x] `_AlternatingAlgebraFunctor._apply_morphism` and `_DividedPowerAlgebraFunctor._apply_morphism` now delegate to `_lift_algebra_morphism`, which constructs the endpoint algebras through the respective selected functor and lifts via `source.Mor(target)(morphism)`. Their distinct algebra construction and morphism categories remain unchanged.
- [x] `RngMor.identity` and `RingMor.identity` in `rings/ring_foundation.py` now share `_ringlike_mor_identity`, retaining the selected fixed-Mor identity check and identity marker while keeping unital and nonunital morphism categories distinct.
- [x] `ConeMorphism.__eq__` and `CoconeMorphism.__eq__` in `abstract_categories/products.py` delegate to `_apex_morphism_equal` for equality within one fixed Mor parent via their apex maps. Their cone and cocone composition and diagram compatibility conditions remain separate.
- [x] `Algebras.Associative.Unital.FinitelyPresentedAsAlgebra.an_object` and `AlgebrasWithChosenFinitePresentation.an_object` now share `_dual_numbers_example` at the algebra presentation owner for the construction `R[x]/(x²)`; each category retains its example method and placement.
- [x] `ProjectiveCompleteIntersections.ParentMethods.integral_singular_cohomology` and `ToricSchemes.ParentMethods.integral_singular_cohomology` now use `_integral_singular_cohomology_over_rationals` in `schemes/geometric_cohomology.py`, retaining the exact `QQ -> CC` hypothesis and specialized public methods.
- [x] `GeneralModules.ElementMethods._acted_upon_` and `LocalizedModules.ElementMethods._acted_upon_` now share `_module_element_scalar_action` in `modules/general_modules.py`, preserving the coefficient-ring membership dispatch and `None` for non-scalars. Localization's independent fraction arithmetic is unchanged.
- [x] The single `_engine_ring_value` in `rings/ring_foundation.py` now lowers owned or already-engine ring values for both `commutative_algebra.py` and `commutative_ideals.py`, retaining the broader Sage-ring-parent route previously available only to commutative algebra.
- [x] `schemes/gluing.py:_finite_framing` retains its gluing-specific framed-module requirement and delegates the selected finite generator index set to the canonical `_finite_framing` in `sets/coordinate_families.py`; no second finiteness algorithm remains.
- [x] `CoveringFamilies.ParentMethods` in `abstract_categories/presheaves.py` now owns `cech_site`, `cech_covering_family`, and `cech_coverage`. Finite affine atlases and distinguished affine covers inherit the one construction from their existing covering-family placement, retaining the original member/pair indices, cached site/family identities, and their distinct geometric restriction realizations. The selected pair site labels are tuples in both cases.
- [x] `FiniteAtlasModuleGluingMorphismMethods` and `FiniteAtlasAlgebraGluingMorphism` now compose their actual local natural transformations through `NaturalTransformationMor` in `abstract_categories/cat.py`. Each datum's category owns its cached discrete chart diagram on the exact atlas index set, and diagram admission retains the original fixed-scalar module/algebra component arrows. The component multiplication has one owner; existing atlas-normalization and family accessors remain delegation wrappers. The resulting arrow keeps its exact descent-data endpoints, scalar-algebra composition keeps its original Mor, and finite arrow comparison delegates to `IndexedFamily` through `_richcmp_`. The distinct overlap restriction and compatibility equations remain at their module/algebra owners.

## Step-2 false statements from the complete construction/property views (2026-10-09)

**Full-view reading gate (2026-10-10):** Reviewed all 3,252 lines of `.tmp/step2-constructions.txt` and all 1,139 lines of `.tmp/step2-properties.txt`, including the eight oversized early property-category lists by splitting their comma-separated category declarations and checking their differences. The unchecked list below is the fixed Step-2 repair denominator; repairs proceed at the mathematical owners in listed order. Scanner artifacts and correct edges are excluded.

- [x] `Modules.X.determinant_line()` and `exterior_forms(degree)` were owned by arbitrary `Modules(R)` (`categories/modules/pure/modules.py`), but both delegate to `modules/hodge.py:58–72`, where `_require_finite_free(module)` requires a finite free module. The five Hodge methods now belong to `FramedFreeModules.FinitelyGenerated` instead of arbitrary modules. The separately useful global determinant for non-free finite projective modules is not falsely provided by the general owner and needs its own future realization.

  Partial owner correction (2026-10-10): the five finite-free Hodge methods (`determinant_line`, `exterior_forms`, `volume_trivialization`, `framing_volume_trivialization`, `poincare_duality`) were relocated from `Modules.ParentMethods` to `FramedFreeModules.FinitelyGenerated.ParentMethods`. The unchecked remainder is the determinant-line construction for finite projective modules that are not globally free, where top exterior power needs a locally constant rank decomposition rather than the selected-free-basis calculation. Sage is unavailable for an owner-local runtime check; both edited source files pass Python compilation and `git diff --check`.

  Further owner work: `Modules.Projective.ParentMethods.local_determinant_line(point)` now obtains the top exterior line over the local ring from the existing projective-module local free trivialization, without assuming a global basis. The global determinant object and transition/gluing datum for locally varying projective rank remain a separate unimplemented capability, not a false category placement.

  Correction: the local determinant is the top exterior power of the actual localized module, using the chosen local free source only to determine its rank; returning the free source's own determinant would not identify the requested module canonically. No global constant-rank assumption is made.

- [x] `Lattices.X.delta()` and `two_elementary_invariants()` were owned by arbitrary lattices (`categories/lattices.py:3948–4000`) but define Nikulin's invariants only for even, nondegenerate 2-elementary integral lattices. Both methods now belong to `EvenTwoElementaryLattices(ZZ)`, which checks the defining mathematical properties and uses the established `refine(lattice, category)` owner mechanism rather than a new private reconstruction. The named-lattice catalogue and focused call sites explicitly request the refinement.

  Owner correction: created `EvenTwoElementaryLattices(ZZ)` as the nondegenerate even 2-elementary refinement, with `delta()` and `two_elementary_invariants()` in its `ParentMethods`. The refinement now uses the same certified `refine` API as `HyperbolicLattices`; focused Sage runtime execution remains unavailable in this environment.

  The named-lattice block catalogue now explicitly refines each selected block through `EvenTwoElementaryLattices(ZZ)` before asking for Nikulin `delta`; the category is exported from `preamble.all`. Direct test and other session call sites remain to be migrated or represented as refined objects.

  Focused test and user-simulation call sites in `tests/lattices`, `tests/objects`, and `tests/user_simulations` have now been changed to request the even 2-elementary owner explicitly before computing the invariants. Runtime proof of the `_with_structure` refinement remains unavailable without Sage; the item stays unchecked until that category construction is validated.

- [x] `FormModules.X.raise_index_over_fraction_field(tensor, slot)` was owned by all formed modules over arbitrary coefficient rings (`categories/modules/framed/formed/form_modules.py`). It is now owned by `NondegenerateGenericFibreFormModules(R)`, whose base is an integral domain and whose constructors certify finite generation and nondegeneracy; it raises the index after extension to `Frac(R)`. Ordinary formed modules retain `raise_index` and `lower_index` without acquiring the generic-fibre method. The three focused callers explicitly use the specialized category. Sage runtime execution remains unavailable; Python compilation and diff checking passed.

- [x] `DiscriminantBilinearModules.X.associated_quadratic_form()` was incorrectly owned by every discriminant bilinear module, although an odd lattice has no canonical quadratic refinement. The method is now owned by the existing `DiscriminantQuadraticModules` category of even-lattice quadratic discriminant forms; the bilinear owner retains its bilinear operations. Its focused assertion was updated to use the quadratic discriminant object.

- [x] `ToricSchemes.X.fundamental_group()` was owned by arbitrary toric schemes but used a smooth complete rational toric realization returning a trivial cyclic group. The realization now belongs to `SmoothCompleteRationalToricSchemes(QQ)`; its constructor checks that the fan is smooth and complete and refines through the existing category mechanism. The general `ToricSchemes` owner no longer claims a cyclic fundamental group; the general quotient-lattice invariant remains a separate capability. The focused test explicitly enters the supported specialization.

- [x] `Schemes.X.generic_fiber()`, `special_fiber()`, `base_change_to_completion()`, and `special_fiber_comparison()` formerly belonged to all schemes. `generic_fiber` is now owned by `SchemesOverIntegralDomains(R)` and the distinguished special-fibre and completion methods by `SchemesOverLocalRings(R)`, each certifying its base-ring hypothesis before refining the scheme. The universal `fiber` and `fiber_over_ideal` operations remain general. Affected focused tests now explicitly request the appropriate base specialization; source compilation and diff validation passed. Sage runtime execution was unavailable.

- [x] `Schemes.X.diagonal_subscheme()` previously claimed a closed diagonal on every scheme despite requiring an affine coordinate algebra. The affine closed-diagonal equation construction is now owned by `Schemes(R).Affine().ParentMethods`; arbitrary schemes retain `diagonal_morphism()`. A general separated nonaffine diagonal remains expressible as a closed immersion, but its chart-glued closed-subscheme realization is not falsely claimed by the affine computation.

- [x] `ProjectiveSpaces.X.coordinate_swap_action(group)` was owned by every projective space, although the construction swaps the two homogeneous coordinates of `P¹`. The method now belongs to `ProjectiveLines(R)`, whose constructor certifies relative dimension one before refining a represented `P¹_R`. The two focused callers use that owner; general `ProjectiveSpaces` no longer claims this distinguished involution.

- [x] `ProjectiveSurfaces.X.del_pezzo_degree()` was available on every projective surface although the invariant requires a normal Gorenstein surface with ample anticanonical class. Its public method now belongs to `DelPezzoSurfaces(R)`, which certifies `is_del_pezzo()` before refinement; the general surface retains the mathematical predicate and realization hook, not the specialized degree operation. The focused Del Pezzo callers now refine explicitly. Compilation and diff checks passed; Sage runtime was unavailable.

- [x] `ProjectiveCompleteIntersections.X.integral_topology()` and `hodge_structure()` previously exposed the quartic-K3-only realizations on all projective complete intersections. Both methods now belong to `SmoothQuarticK3CompleteIntersections(QQ)`, which uses the existing smooth-quartic-K3 guard and the established category refinement. The K3 test callers explicitly enter this specialization; arbitrary complete intersections retain the general integral singular cohomology construction. Python compilation and diff validation passed; Sage runtime was unavailable.

- [x] `PrimeSpectra.ElementMethods.height()` formerly used `dim(R)-dim(R/p)` on every prime point in its purported domain. It now states and dispatches the intrinsic invariant `dim(R_p)`. `PrimeLocalizations.krull_dimension()` independently evaluates the dimension-difference formula only in its explicitly certified domain/PID-or-field-finite-type regime; no reverse call to `height()` remains. Outside this regime the local owner explicitly reports that a prime-chain/local-dimension realization is not yet available, rather than asserting a false dimension formula. Thus the wrong mathematical statement and circular dependency are repaired, while the general computation is a separately identified realization gap.

  Owner investigation (2026-10-10): `PrimeSpectra.ElementMethods.local_ring()` already constructs `R_p`, but `PrimeLocalizations.krull_dimension()` (`commutative_algebra.py:1559–1568`) currently calls `source.spectrum()(localized_prime).height()`. Simply replacing `height()` by `self.local_ring().krull_dimension()` would create an infinite recursion. The correct next owner change must give localized rings an independent intrinsic Krull-dimension route (or represented prime-chain construction), then make generic prime height use it; the special dimension-difference formula can remain an explicit optimization on its certified regime. Do not check this item on the strength of the circular replacement.

- [x] `PicardGroups.X.projective_base_picard_group()`, `projective_hyperplane_factor()`, `base_picard_inclusion()`, and `hyperplane_class()` formerly appeared on all Picard groups despite requiring the chosen projective-bundle decomposition `Pic(P^n_S) ≅ Pic(S) ⊕ ℤ[O(1)]`. They now belong to `ProjectiveBundlePicardGroups`, a specialization of `PicardGroups` and `BiproductModules(ZZ)`, and `PicardGroups.projective_bundle()` places its results there at construction. No generic Picard group acquires an unselected hyperplane summand. Python compilation and diff checks passed; Sage runtime unavailable.

- [x] `OpenImmersions.X.flat_pullback_cycle(cycle)` formerly restricted its general operation to the distinguished-open localization formula. The mathematical operation now belongs to all `OpenImmersions` and dispatches through `_flat_pullback_cycle`; the `DistinguishedOpenImmersions(X)` specialization supplies the existing localization-based computation. General nondistinguished open immersions correctly retain the operation with an explicit atlas-based realization frontier rather than claiming to be a principal localization.

  The localization calculation belongs to `DistinguishedOpenImmersions(X)`, which certifies `D(f)`, and both focused callers request this specialization. A general atlas-based realization of the mathematically defined restriction remains a separate implementation prerequisite; absence of that computation is not a false placement.

- [x] `ModulesOverGroupAlgebra.X.character()` and `brauer_character()` were wrongly exposed on every group-algebra module. The two methods now belong, respectively, to `OrdinaryCharacterRepresentations(R[G])` (finite group, finite free coefficient module, characteristic zero) and `BrauerCharacterRepresentations(R[G])` (finite group, finite free coefficient module, positive-characteristic coefficient field), refining through `FiniteFreeGroupRepresentations`. The character test explicitly constructs its specialized representation; Python compilation and diff checks pass. Sage runtime execution remains unavailable.

- [x] `Modules.X.generic_fibre_map()` and `torsion_submodule()` were owned by all modules despite requiring an integral-domain base. These methods and the generic-fibre torsion-freeness computation now belong to `ModulesOverIntegralDomains(R)`; the finitely presented PID/SNF torsion calculation retains its own owner. All direct source uses of `generic_fibre_map` were routed through the specialized category. The remaining represented torsion theories on other rings are independent operations, not claims that every ring has a fraction field.

  Owner correction underway: introduced `ModulesOverIntegralDomains(R)` with an integral-domain hypothesis and relocated `generic_fibre_map`, `torsion_submodule`, and the generic-fibre torsion-freeness realization there. Added exports and migrated the focused generic-fibre tests. Other callers and existing finite-presentation specializations require owner-local reconciliation before this item is checked.

  The finitely-presented-module `torsion_submodule` fallback explicitly enters `ModulesOverIntegralDomains(R)` rather than calling the removed general method; its PID/SNF branch retains its independent formula. Generic-fibre callers in `lattice_morphisms.py`, `isotropic_lifts.py`, `lattices.py`, `group/groups.py`, `modules/ideal_duals.py`, `modules/module_morphisms/module_morphisms.py`, and `modules/framed/formed/form_modules.py` now explicitly enter the domain-module category before invoking the map. Source compilation and diff checks pass. Sage runtime verification remains unavailable.

- [x] `GObjects.X.fixed_subobject_of(group_element)` and `nontrivial_stabilizer_subscheme()` formerly conflated the general fixed-object equalizer with scheme-specific fixed ideals. Set actions now produce the fixed subset, affine scheme actions retain their scheme-theoretic fixed locus, and other underlying categories expose the equalizer realization frontier. `nontrivial_stabilizer_subscheme` belongs to `AffineGSchemes`; the freeness predicate handles set actions without invoking scheme-only methods and remains undecided when the underlying category does not supply a representation.

- [x] `PrimeSpectra.X.generic_point()` previously treated the zero ideal as a unique generic point on arbitrary spectra. It is now owned by `IntegralPrimeSpectra`, constructed only for integral domains by the ring's `spectrum()` construction. Other spectra remain in `PrimeSpectra` with no intrinsic selected generic point; irreducible spectra with nonzero nilradical require a separate selected-component construction rather than silently identifying the zero ideal as a prime.

- [x] `GradedAlgebras.X.degree_zero_chart(localization)` and `degree_zero_chart_restriction(...)` formerly used an integral-domain fraction calculation on arbitrary graded algebras. Both methods now belong to `CommutativeGradedIntegralDomains`, whose supercategories supply the graded-algebra and integral-domain structure, and whose refinement checks both conditions. Focused callers explicitly select this owner. Python compilation and diff checks pass; Sage runtime was unavailable.

- [x] `ToricSchemes.X.hyperplane_divisor()`, `hyperplane_line_bundle()`, and `O1()` formerly appeared on every toric scheme, despite referring to the selected projective-space hyperplane. They now belong to `ToricProjectiveSpaces`; the toric variety constructor assigns this category only when its fan is isomorphic to the projective-space fan. Other toric varieties do not receive these methods. Python compilation and diff validation passed; Sage runtime was unavailable.

- [x] `ToricSchemes.X.canonical_line_bundle()` and `anticanonical_line_bundle()` falsely assigned invertible canonical sheaves to every toric scheme. The Cartier constructions and aliases now belong to `GorensteinToricSchemes`, while general toric schemes retain `canonical_divisor()` and the separate mathematical operation `canonical_reflexive_sheaf()` for the rank-one reflexive divisorial sheaf `O_X(K_X)`. The latter is realized by the invertible sheaf in the Cartier regime and explicitly identifies the non-Cartier divisorial-module gluing computation as not yet implemented; this remaining computational frontier does not assign a line bundle to a non-Gorenstein variety.

  Smooth-fan toric constructions are placed in `GorensteinToricSchemes` automatically, and `ToricProjectiveSpaces` inherits this owner. Non-Cartier reflexive-sheaf evaluation still needs a represented gluing construction, independently of this false-placement repair.

- [x] `GradedModules.ElementMethods.degree()` formerly computed the maximum degree of the finite homogeneous support even though arbitrary grading monoids need not be ordered. It now belongs to `IntegerGradedModules(R)`, which refines only objects with the integer grading. Graded direct sums with integer degree sets and free tensor/symmetric algebra constructions receive that owner; other graded modules retain the general `homogeneous_degree()` method without a spurious maximum. Python compilation and diff validation passed; Sage runtime unavailable.

- [x] `Lattices.X.reflective_roots()` previously falsely promised a finite family on arbitrary lattices. The general lattice now owns `reflective_root_locus()` as a predicate-defined possibly infinite subset (primitivity and integral-reflection condition). Finite `reflective_roots()` enumeration belongs to `DefiniteLattices(R)` alone; the definite root-system computation and A2 test explicitly refine their inputs. Python compilation and diff validation passed; Sage runtime unavailable.

- [x] `Curves.X.arithmetic_genus()` formerly assigned the Hilbert-polynomial arithmetic genus to all curves, including affine curves. This method now belongs to `ProjectiveCurves(k)`, requiring both `Curves(k)` and `Schemes(k).Projective()` over a field. Projective equation constructors place their curves in this category; normalization/genus callers explicitly request that owner. Affine curves have no inherited projective arithmetic genus.

- [x] `KahlerDifferentialModules(A)` formerly asserted that every Kähler differential module has a selected finite presentation. Its supercategory is now `Modules(A)`; the finite conormal-presentation branch of `_construct_kahler_differentials` independently constructs its result in `ModulesWithChosenFinitePresentation(A)`, and free/localized realizations retain only their actually established placements. Python compilation and diff validation passed; Sage runtime unavailable.

- [x] `LatticesOverGroupAlgebra.X.isotypic_lattice(character)` now explicitly constructs the result through the action-bearing `LatticesOverGroupAlgebra(R[G])` owner and establishes that the underlying formed subobject has coefficient ring `R`. Inspection established that `Lattices(R[G])` had already dispatched to this action-bearing category (rather than a lattice with an `R[G]`-valued form) via `Lattices.__classcall_private__`; the explicit owner call removes the misleading placement and preserves the `R`-valued form and restricted `G`-action. Python compilation and diff checks passed; Sage runtime unavailable.

- [x] `PermutationGroups.X.action_on(points)` no longer places arbitrary actions in finite `G`-sets. It constructs `FiniteGSets(G)` only when the selected point set belongs to `FiniteSets()`; otherwise it uses `GObjects(G, Sets()).on_set()` for the general set action. The natural finite permutation domain retains its existing specialization.

- [x] `ModulesOverGroupAlgebra.X.isotypic_characters()` no longer unconditionally returns a finite set. The finite enumeration now belongs to `FiniteFreeGroupRepresentations.finite_isotypic_characters()` and is selected only for a finite group acting on a finite-free coefficient module. The general character-support operation retains its mathematical role, with an explicit not-yet-realized character universe for infinite-support cases rather than falsely imposing finiteness. Source compilation and diff checks passed; Sage runtime unavailable.

- [x] `Modules.X.symmetric_power`, `exterior_power`, `divided_power_module`, and `divided_square` have their mathematical operations at the general module owner. The selected realization explicitly returns the unchanged original module in degree one and the regular module in degree zero; a finite-presentation result is constructed only from an admitted selected finite module presentation. A free-framed source produces a free-framed power. General higher powers lacking either realization now report a missing computation instead of attempting to obtain finite generators or asserting that every module is finitely presented. Source compilation and diff checks passed; Sage runtime unavailable.

- [x] `TopologicalManifolds.X.chart_labels()` and `atlas()` formerly asserted a finite atlas for every finite-dimensional manifold. They now retain arbitrary `chart_index_set` data and an indexed chart provider, producing a general lazy `indexed_family` rather than a finite indexed family. The finite chart registry is exposed separately through `selected_finite_chart_labels()` and remains the fallback for locally registered charts; finite dimension no longer forces finite atlas placement.

  The optional chart provider can realize an atlas indexed by a non-finite set without enumerating all charts. Python compilation and diff validation passed; Sage runtime unavailable.

- [x] `LeftCosetGSets(H)` now belongs to general `GObjects(G, Sets())`. For non-finite `G`, the quotient `G/H` is a symbolic set of coset representatives under the exact equivalence `gH=hH iff g⁻¹h∈H`, with an induced left action that does not enumerate the quotient. Finite groups retain the engine's enumerated cosets and finite placement; the regular action is finite only when `G` is finite. `Groups.left_cosets(H)` now reaches both representations. Python compilation and diff checks passed; Sage runtime unavailable.

  The infinite-coset representation is not enumerated; equality uses subgroup membership. Enumerated coset operations such as ranking are therefore not available without additional finite-index data.

- [x] `GObjects.X.orbit_representatives(points)` now places selected representatives in `OrbitRepresentativeSets(G)` over general `Sets()` rather than asserting finite cardinality. The constructor preserves already-owned arbitrary representative sets without enumeration; finite literal families are converted to finite ordered sets and receive `FiniteSets()` placement only when justified. The inclusion and orbit-quotient projection remain on the resulting object.

- [x] `CohomologyModules(R)` now inherits general `Modules(R)` and no longer asserts that arbitrary cohomology is finitely presented. The selected finite conormal/presentation route in `_cohomology` checks that the cycle module is finitely presented before constructing `ModulesWithChosenFinitePresentation(R)`. A general complex retains cohomology as the quotient `ker(d)/im(d)` mathematically, with the unrestricted realization explicitly outstanding rather than silently claiming a finite presentation.
- [x] `CommutativeIdeals.X.associated_primes()` no longer assumes finite support: outside the Noetherian regime it returns `associated_prime_locus()`, the image of the predicate subset of elements `a∈R` satisfying `(I:a)` prime under the annihilator map `a↦(I:a)`. This is exactly the associated-prime locus of `R/I`, with no enumeration or `FiniteSets` placement. The separately named `finite_associated_primes()` retains the Noetherian engine realization. Actual membership computations are bounded by the existing ideal quotient/primality realization, not a claim that every non-finitely-generated ideal is computable.

  The unrestricted nonenumerated set representation is supplied by the set image construction over the annihilator predicate.

  The Noetherian enumeration is also separately exposed as `finite_associated_primes()`; the unrestricted `associated_primes()` operation delegates to it only under the established finiteness hypothesis.
- [x] `CommutativeIdeals.X.primary_decomposition()` no longer returns a finite family without the Noetherian hypothesis. A separate `primary_decomposition_locus()` now constructs the possibly empty predicate set of finite families of primary ideal subsets of `R` whose intersection is `I`. This formulation distinguishes existence of a primary decomposition from selection of one, and retains the mathematical family locus without enumerating arbitrary ideals. The Noetherian backend remains independently exposed as `finite_primary_decomposition()`; membership in the general locus is proposition-valued where no decision procedure exists.

  A general primary decomposition need not exist; the presentation locus may be empty, and no engine assertion is used to declare its existence.

  The selected Noetherian algorithm is separately exposed as `finite_primary_decomposition()`, so its finite result is distinguished from the general primary-decomposition existence problem.

- [x] `QuotientRings.X.minimal_primes()` and `irreducible_components()` now select nonenumerated loci outside the Noetherian regime rather than `FiniteOrderedSets()`. The `prime_ideal_locus()` is a predicate subset of the **full power set of the underlying ring**, so even non-finitely-generated prime ideals are represented abstractly; `minimal_prime_locus()` selects minimal prime subsets, and `irreducible_component_locus()` maps each such prime to the closed subset of all prime subsets containing it. Computation of the associated predicates is deliberately not asserted. The finite Noetherian presentation route retains its existing algorithms and placements, without assuming that arbitrary prime ideals have generators.

  The internal finite minimal-prime enumeration requires the presentation ring to be Noetherian. In the general regime the full prime-ideal universe is represented by its set-theoretic ideal predicate rather than enumerated or forced into the finitely-generated ideal class.

  `QuotientRings.minimal_primes()` selects the predicate locus of minimal prime subsets outside the Noetherian regime, with no false enumeration.

  `irreducible_component_locus()` is the image of those minimal primes under Zariski closure, using prime-subset containment rather than incomplete finite-generated prime points. Further computational realization of these general predicates remains a separate `TODO.md` concern.

- [x] `Lattices.X.vectors_of_square_and_divisibility` claimed `FiniteOrderedSets()` for every lattice. On the indefinite lattice `U ⊕ ⟨-2⟩`, the vectors `(n²+1,1,n)` have square `2` and divisibility `1` for every nonnegative integer `n`, so this locus is infinite. The defining helper in `categories/definite_lattices.py` now retains the full predicate subobject of the square fibre unless the fibre is known finite. Focused Sage confirms membership of four distinct such vectors in the retained locus; on `⟨-2⟩`, the finite shell remains in `Sets().Finite()` and has cardinality two.

**Cross-family result-placement follow-up (2026-10-10).** The earlier full
construction/property report review was checked against source constructors
outside `Sets`: `GradedModules._call_` constructs through the graded-module
owner; `R[G]` is constructed as `GroupAlgebras(R)` and is additionally
commutative only when the coefficient ring is commutative and the group is
proved abelian; a cyclic subgroup is placed in `Subgroups(G)` and becomes
finite when `G` is finite; lattice construction retains its lattice category;
`Spec(A)` is placed in `Schemes(R).Affine()` with additional integral,
finite-type, and smooth assertions conditioned on their own hypotheses.
`AffineGroupSchemes(R)` represents a group object in affine schemes through
its selected internal group datum, not an ordinary group of points. No new
false mathematical result placement was established in these source slices.
This finding does not discharge the separate category-wide method-owner and
Mor-inheritance obligations of `placement-audit` in `TODO.md`.

**Covering-family presentation edge (2026-10-09).** The parameterized
`CoveringFamilies(Sets())` retains its site by identity, and its selected
supercategory is exactly the constructed `presentation_category()` (two
focused assertions). This is a category of diagrams into the site, not a
claim that a cover is itself a set or a scheme.

**Action-category forgetful Mor edge (2026-10-09).** For the trivial action
of `C_2` on `Sets.Δ[1]`, the evaluation functor of `GObjects(C_2,Sets())`
sends the acted object into `Sets()`. Its declared supercategory is exactly
`Sets()`, and `_mor_endpoints_in_supercategory(Sets(),X,X)` uses that same
forgotten object by identity (three targeted checks). The dependent
supercategory therefore retains correct endpoints through the selected
forgetful functor; it does not identify an acted object with its underlying set.

**Category-functor Mor endpoints reconciled (2026-10-09).** The apparent
`Cat().functor_mor(Sets(),Sets())` endpoint-identity failure compared the
represented `CategoryObject` endpoints with the unrepresented category.
Both endpoints are exactly `Cat().object(Sets())` and their
`represented_category()` is `Sets()` by identity. Its selected supercategory
is exactly `functor_category()` (five focused identity assertions passed).
This is a valid dynamic functor-category edge, not a wrong placement.

**Fibered formed-module Mor expression edge (2026-10-09).** On the hyperbolic
lattice `L=U`, scalar extension along `ZZ.fraction_field_map()` gives `V`.
`FiberedFormedModuleMor(L,V,f)` has endpoints `L,V` by identity, and its
selected supercategory is exactly its semilinear `module_mor()` with the same
endpoints (five focused assertions passed). This expression represents a
same-endpoint forgetful inclusion, not a false categorical placement.

**Group-module Mor expression edge (2026-10-09).** For the trivial `C_2` action
on the rank-one free `ZZ`-module, `V.Mor(V)` and its selected ordinary
`ZZ[C_2]`-linear Mor supercategory retain the exact two endpoints `V` by
identity. Their dynamic `ordinary` edge is consequently an inclusion of
equivariant morphisms into ordinary linear morphisms with the same endpoints;
the separate matrix-exemplar framing obligation remains open in `TODO.md`.

**Bare-placement audit disposition (construction view, 2026-10-09).** The
`placed in Sets()` and `placed in Objects()` lines do not, by themselves,
identify a group/ring/module/lattice/scheme constructed in the wrong category.
`Modules.pairings_with`, `bilinear_forms` and `quadratic_forms` use module Mor
classifiers for module-valued forms; the fallback `Sets()` object represents
callable-valued forms when that classifier does not apply. The `Objects()`
entries for algebra `presentation`, coproduct factors/injections, primary/Jordan
decompositions, lattice summands, and scheme point counts/affine charts are
indexed families of mathematical objects, not those objects themselves.
Likewise, isotropic-sublattice and flag **loci** are sets of lattice subobjects,
not lattices. The reported `tensor_power` placement is already a module with
its `TensorPowerModules` structure, including degrees zero and one. Further
repairs must come from a concrete false mathematical construction statement,
not from coercing one of these families or classifier sets into its element's
category.

Both complete reports were read together (478 construction lines and 410 property lines). The following are false *property-report assertions*, rather than defects in the categories' actual `super_categories()` declarations. Each came from scanning arbitrary calls in object methods as though they were categorical placements:

- [x] `WeilDivisorGroups ... places Affine`: a Weil divisor group is a free abelian group of divisors, not an affine scheme. Its `affine_divisor_coordinate_ring()` queries whether the **underlying scheme** is affine; the group itself declares `DivisorGroups()`.
- [x] `FiniteAffineAtlases ... places Affine`: an atlas of affine charts need not be an affine scheme (e.g. the standard atlas of projective space). Its objects are covering families, and its declaration is `ZariskiCoveringFamilies(X)`.
- [x] `_cartesian_product_of: input in EnumeratedSets` appears among the construction sites placing in `Sets.Finite`: being enumerated does not make a factor finite; this placement actually requires all factors finite and a finite index set. The scanner wrongly attributed a nested finite placement to one conjunct of the enclosing enumerability guard.
- [x] `_coproduct_of_indexed_family: input in EnumeratedSets` appears among the construction sites placing in `Sets.Finite`: enumerability of the index set or summands does not imply finiteness of the disjoint union. The finite placement is conditional on every summand being finite. The same nested-guard attribution defect caused this line.

The common owner repair is in `utilities/category_graph.py`: category property-placement inference inspects only supercategory declarations, not arbitrary member methods; construction-site inference no longer treats a conjunct of a compound guard as sufficient or attributes a nested conditional placement to the outer guard. The `Sets.Finite` category-name warnings concerning a *finite presentation*, a *finite field*, or the finite-subset construction are not mathematical assertions that the resulting groups/algebras/power sets are finite, and are not added as false placements.

## In progress

**Closed `placement-owner-ownedrings-artinian` (2026-10-11):** the entire three-introduction declaration, all 16 strict authored ancestors and actual inherited ring arrows are reviewed. The left-ideal convention and Hopkins–Levitzki edge are now explicit and consistent with Noetherian. The existing zero, finite-matrix, infinite-field and product constructors supply the required distinctions; the actual common finite-ring tail was read as part of the complete constructor route. All predicate and morphism behavior remains unchanged. Twenty of 633 whole-owner passes are closed. The complete Commutative ring owner pass is active next, including all its introductions and their weakest sufficient structures; its already closed Local/Complete descendants retain their separate records. No prerequisite or new owner is added. Runtime assertions remain under T.

**Closed `placement-owner-ownedrings-noetherian` (2026-10-11; `2fc8fa8028`):** both introductions, all 15 strict authored ancestors and the inherited ordinary ring arrows have their complete pass. The class, selector, common predicate and session-alias documentation now consistently state the primary source's left-Noetherian convention; the commutative shorthand keeps its exact value. The source changes no behavior, placement, constructor or arrow. ZZ, the zero ring and the existing undecided predicate provide the retained assertions, with no recognition algorithm inferred from the property. This was the nineteenth of 633 whole-owner passes; the sole changed Python file passed the required post-commit stdlib AST check. Artinian closes independently in its later bank. The common Commutative ring owner is now active; no new prerequisite or owner was added. Runtime assertions remain under T.

**Closed domain-owner passes (2026-10-11; `fd3aed3701`):** `placement-owner-ownedrings-nozerodivisors-commutative`, `placement-owner-ownedrings-nozerodivisors-nontrivial` and `placement-owner-ownedrings-nozerodivisors-commutative-nontrivial` each have a complete source pass and are [x]. The two new authored providers expose existing axiom meets and are added and closed in the same bank. Nonzero submonoids now use the weakest existing sufficient structure, including the actual noncommutative QQ<x,y> example; fraction constructions require commutativity and nontriviality. Selected fraction maps, normalized fractional-ideal data, zero-ring behavior and owned undecided propositions are preserved. Their full records below include the actual arrows and all constructor repairs. Protected construction assertions are unchanged; the missing category-level fraction-field entry and unsupported computations remain named inside the existing domain work and T. This bank completed eighteen of 633 whole-owner passes; all six changed Python files passed the required post-commit stdlib AST check. Noetherian and Artinian close independently in later banks; the common Commutative ring owner is now active. No new prerequisite was filed.

**Closed `placement-owner-ownedrings-nozerodivisors` (2026-10-11; `1a93093f4c`):** both introductions, all 15 strict authored ancestors and the inherited ring arrows have their complete pass. The category now names its exact zero-product axiom and states that commutativity and nontriviality are separate. Its integer witness and ordinary, possibly noninjective ring maps are preserved. This was the fifteenth of 631 owner passes at its bank; the sole changed Python file passed the required post-commit stdlib AST check. The commutative refinement and both new existing-meet providers are independently closed in the later domain bank below. Runtime assertions remain under T.

**Closed `placement-owner-ownedrings-nontrivial` (`0f443d4665`, 2026-10-11):** both introductions, all 15 strict authored ancestors and the actual inherited ring arrows are complete. The existing native integer constructor now explicitly records 0 != 1, admitting the owner's literal ZZ witness without a new recognition procedure or general Domain/Order implication. Nontriviality adds no injectivity requirement to ring maps. This completed the fourteenth of 631 owner passes; its sole changed Python file passed post-commit stdlib AST parsing. NoZeroDivisors is independently closed above; the commutative refinement's domain and fraction-field work is active in its existing node. Runtime assertions remain under T.

**Closed `placement-owner-ownedrings-division-commutative` (`820698c1b2`, 2026-10-11):** the Fields pass accounts for all twelve original introductions, all 27 strict authored ancestors and the actual inherited RingMor. Three public residue operations now inherit common Local, preserving selected quotient data and providing a lazy canonical field default only when needed. Field embedding enumeration explicitly selects ordinary ring arrows. This completed the thirteenth of 631 owner passes; its sole changed Python file passed post-commit stdlib AST parsing. Nontrivial and NoZeroDivisors are independently closed above; the commutative NoZeroDivisors refinement is active. Existing generator, enumeration, closure and selected-data computation limits remain inside this node and T.

**Closed `placement-owner-ownedrings-division` (`cfbf12acff`, 2026-10-11):** all four introductions, all 17 strict authored ancestors and the actual inherited ring arrows have their own completed pass. The unit theorem now uses owned negation of zero equality, retaining decided answers and undecided propositions. Nontriviality is explicit, and the nonunit 2 in ZZ prevents promotion to weaker ring properties. This completed the twelfth of 631 owner passes; its sole changed Python file passed post-commit stdlib AST parsing. Fields is independently closed above; inverse-computation boundaries and runtime assertions remain under T.

**Closed `placement-owner-ownedrings-division-commutative-prime` (`ab4aaa2466`, 2026-10-11):** both original introductions, the characteristic constructor, all 28 strict authored ancestors and the inherited RingMor are complete. Both public PrimeField entries now construct through this owner: zero selects QQ and positive prime p selects GF(p), while composite characteristics cannot select extension fields. Prime-domain map uniqueness precedes source transport and model access; GF(4)'s distinct Frobenius remains excluded from that theorem. This completed the eleventh of 631 owner passes; both changed Python files passed post-commit stdlib AST parsing. Division is independently closed above; the Fields pass is active. Existing required computation boundaries and all runtime assertions remain under T.

**Closed `placement-owner-formalpowerseriesrings` (`7012101c20`, 2026-10-11):** all ten original introductions, the corrected parameter declaration, all 26 strict authored ancestors and the actual unital algebra Mor have their own complete pass. Source generator positions, formal labels and scalar coefficients now agree without replacing the actual coefficient map by the completion map. The selected zero-ring and empty-family construction data are retained in `13d391e8f2`. This completed the tenth of 631 owner passes; its sole changed Python file passed post-commit stdlib AST parsing. The Prime refinement is independently closed above; Division is ready for closure, with Fields active. Runtime assertions and the stated coefficient/cardinality computation frontiers remain under T.

**Closed `placement-owner-adiccompletions` and `placement-owner-adiccompletions-local` (`13d391e8f2`, 2026-10-11):** all 27 original Adic introductions, its 18 strict authored ancestors, full selected-supplier inventory and delivered RingMor are reviewed and repaired. The new Local provider's two introductions and 21 strict ancestors have their own completed pass. Scalar and residue maps use their common owners; induced maps have actual endpoints and true hypotheses; exact source projection and finite precision remain distinct. The provider is added and closed in this bank, completing the eighth and ninth of 631 owner passes. All three changed Python files passed post-commit stdlib AST parsing. FormalPowerSeriesRings is independently closed above. Evaluation without exact source data remains explicitly named inside Adic and T, with no new prerequisite.

**Closed `placement-owner-ownedadicallycompleterings` (`0af4238b7b`, 2026-10-11):** all five introductions, all 17 strict authored ancestors and delivered RingMor have their own completed review. The common accessor exposes the actual chosen target ideal, preserves explicit supplier authority and accepts independent zero-adic native fields. Source, target and maximal ideals remain distinct. This completed the seventh owner pass; the selected Adic and its Local provider passes are independently closed above. The parent remains open, with runtime assertions retained under T.

**Closed `placement-owner-ownedrings-commutative-local-complete` (`94033b61a2`, 2026-10-11):** the four-introduction pass, all 20 strict authored ancestors and delivered RingMor are complete. The selected source ideal, its actual target extension and a potentially different maximal ideal remain distinct; native fields supply an independent zero-adic witness. The coherent source repair is in 05056101fb with all three changed Python files parsed after commit. This completed the sixth owner pass; the common Adic pass is independently closed above. Runtime assertions remain under T.

**Closed `placement-owner-ownedrings-commutative-local` (`05056101fb`, 2026-10-11):** all nine introductions, 18 strict authored ancestors and actual inherited ring arrows have their own completed review. The formal-series and dual-number suppliers retain actual ideal subobjects and residue maps, quotient elements supply their literal source lifts, and flat ideal transport uses the actual canonical completion arrow. This completed the fifth owner pass; the three changed Python files passed post-commit stdlib AST parsing. The Complete refinement is independently closed above. The common Adic pass is also independently closed above; AdicCompletions and FormalPowerSeriesRings reviews are active. The parent remains open; runtime assertions remain in T.

**Closed `placement-owner-localizationrings-local` (`befab02d6b`, 2026-10-11):** both introductions, all 20 strict authored ancestors and the delivered RingMor inheritance have their own completed review. The selected source-to-residue composite belongs exactly at this Local refinement and keeps its literal endpoints. This completed the fourth owner pass; the common Local pass is now independently closed above. The parent remains open and no runtime assertion is claimed.

**Closed `placement-owner-localizationrings` (`fdf89acdf5`, 2026-10-11):** the remaining fraction equality/admission and cardinality repairs complete this category's full source pass. The operation/ancestor disposition and retained assertions are in its whole-category section below. This completed the third owner pass; its Local refinement is independently closed below and the parent remains open. The optional count/dimension/engine cases were traced through their actual consumers, with no Sage execution or new prerequisite node.

**Owner-pass DAG split (steward instruction, 2026-10-11):** `placement-audit` is open and Needs one node for each canonical category owner. The original source-only inventory has 644 declarations, with 14 source-proved exclusions and 630 owner passes. At split commit `ad02191213`, QuotientRings and PrimeLocalizations were complete. Subsequent independent Localization, Local/Complete/Adic, FormalPowerSeriesRings, Prime, Division, Fields, Nontrivial and NoZeroDivisors passes are closed. The newly authored AdicCompletions.Local provider received its complete pass in the same source bank, giving 631 owners. The domain correction closes the existing commutative NoZeroDivisors pass and adds and closes the complete passes for the two authored providers on existing Nontrivial zero-product meets. The independent Noetherian and Artinian passes are also closed. There are now 633 owners: twenty complete and 613 unchecked. The common Commutative ring owner is active next. TODO.md records each pass and every parent dependency. The completed Step-2 and Step-3 surveys are unchanged; explicit new-provider accounting does not restart either survey.

**Closed `placement-audit` finite-integer localization field decision (2026-10-11):** the existing field hook supplies False when the selected inverted system has a finite generating family and the actual source lies in Modules(ZZ).Free().FinitelyGenerated(). No basis, rank, norm, characteristic computation, domain decision or engine classification is requested. A hypothetical nonzero field localization would contain ZZ injectively by torsion-freeness and be of finite type over it; [Stacks 00G4](https://stacks.math.columbia.edu/tag/00G4) and [0CY7](https://stacks.math.columbia.edu/tag/0CY7) exclude this. The zero localization is not a field either. The exact integer/order source ancestry was read, restoring the decided negative predicate for ZZ[1/2] through a general theorem. Predicate-S cases delegate through the same common Local provider and preserve the actual maximal-ideal zero decision. No new recognition layer or prerequisite is introduced; all execution assertions stay under T.

**Closed `placement-audit` localization universal-map piece (2026-10-11):** public induction now establishes the whole inverted system's unit-image hypothesis from selected finite generators or retained canonical maps. The one existing fraction evaluator has a declared protected owner/caller contract shared by the public operation, prime residue supplier, total-quotient map of a contracted localized ideal, and two maximal-completion producers. Their global premises are respectively generator images or canonical data, nonzero images in Frac(R/p), S-saturation of the contraction, and units outside a proved maximal ideal. The public route retains literal localization identity, zero targets, identical inverted systems, prime-containment restrictions and the matching quotient-to-a-field projection. Unknown hypotheses remain computation assertions. The original-prime completion reuse now requires proved maximality; k[x,y] at (x) is the separating false-arrow example because y is not a unit in k[y][[x]]. The actual completion of the local ring still exists; its absent general computation remains in this node. Source inspection covers all changed and unchanged consumers; the true map equations remain under T.

**Closed `placement-audit` localization predicate/scalar-owner piece (2026-10-11):** fraction-field recognition now expresses the actual domain-source and field-target proposition. The five algorithms that need the selected nonzero-element presentation instead consume a declared Boolean data guard, retaining their existing algorithms and avoiding recursion through local field recognition. The selected singleton-generator wording now permits stored denominators from its saturation. The redundant element multiplication override is removed after independently tracing the actual factories through OwnedParent.element_class to CommutativeRingElement and native Element multiplication: same-parent inputs use the retained fraction `_mul_`; mixed parents use the registered Modules scalar action before coercion. The unrelated native ring-element override remains necessary for its different ingress path. Source review supplies these dispositions; execution remains under T. The subsequent finite-integer supplier restores ZZ[1/2]'s decided False through its actual source-property theorem, while the selected-data separation remains unchanged.

**Closed `placement-audit` localization-map/coefficient-owner piece (2026-10-10):** the complete LocalizationRings definition and its 17 authored ancestors have been read; the category's remaining ownership and predicate questions stay in the same node. The constructor retains the exact old coefficient-base choice through the existing Modules/Algebras initialization, so algebra_base_ring now inherits its algebra owner. Three elementwise ring-map callbacks now explicitly use RingMor: the two selected fraction-field comparisons and restriction_to. Their real consumers are the domain fraction-field map and localized-module restriction; neither requires an unrelated finite module/algebra framing. Prime-containment conjunction retains undecided membership, and unknown unit-image/containment hypotheses report the missing computation without denying existence. The selected realization/comparison guards describe their retained-presentation requirement. Independent source review covers these maps, actual endpoints and constructor order; all execution assertions stay under T.

**LocalizationRings remainder, active in the same placement node:** moving its public cardinality formula must preserve actual source formulas such as a formal power-series ring's cardinality while optional size queries retain an unavailable answer. Exact fraction equality, denominator admission and external fraction membership remain active at their existing owners. Universal maps now preserve their global hypotheses; unretained unit-image decisions and the general nonmaximal completion calculation remain explicit partial algorithms. The negative field computation for ZZ[1/2] is now closed; broader fraction-field recognition/comparison computations not supplied by selected data remain named here. Selected finite-generation hypotheses must follow the retained submonoid data. No new prerequisite or dependency edge is filed.

**Closed `normalization-extensions-retain-coefficients` finite affine piece (2026-10-10):** normalization, its map and components, and conductor now belong to commutative rings. Delta belongs to the existing commutative unital algebra owner and restricts the actual normalization cokernel along its retained field map, with an optional actual F->k tower. The quotient's polynomial algebra base is not substituted for that field. The finite affine producer computes on the radical ideal while preserving the original A, its reduction factorization, N, eta and all component maps. Conductor and normality consume that actual module; native values remain private diagnostics. Identity and zero normalization are coherent constructions, and the presented zero-module annihilator now returns the unit ideal at its existing module owner. Source review covers the named assertions below; execution stays under T. No new prerequisite was filed.

| Normalization assertion | Retained construction |
| --- | --- |
| Normal affine line | The field-symmetric producer returns the original A, its ring identity, N=A_regular and eta=id. The cokernel is zero, so conductor is A and delta is zero. |
| Cusp k[t^2,t^3] | B=k[t]; the retained quotient is generated by the class of t, annihilated by (t^2,t^3). Its coefficient dimension is one. An actual quadratic QQ->k restriction gives dimension two through the same module. |
| Crossing k[x,y]/(xy) | B=k[x] x k[y], with both original-A component maps and projections. Eta has one diagonal image; its quotient is the difference of constant terms, giving conductor (x,y) and delta one. |
| Dual numbers | A->A_red->B kills epsilon. The normalization quotient is zero and conductor is the original unit ideal, but reducedness is False, so the original ring is not normal. |
| Infinite coefficient dimension | For the cusp times an affine line, B/image(A) is t*k[z]; its represented coefficient dimension is aleph0 and it has no finite field framing. |
| General hypotheses | The common owner supplies no finite placement. General nonfinite normalization, general component selection, localized computations and unsupported alternative field actions remain inside the existing node. |

**Closed finite field-tower remainder (2026-10-10):** the existing scalar-restriction constructor reads a represented vector-space dimension and the scalar field's selected finite basis along the exact supplied map. It retains their owned cardinal product, both original scalar maps and that scalar basis. The finite field basis does not manufacture a finite frame of the module. For the cusp-cylinder quotient, a further quadratic QQ->k restriction therefore retains aleph0 and no finite framing. Missing dimension or missing scalar-basis data retain their existing computation boundary. Source and independent owner review cover the number-field basis and cardinal multiplication; execution remains under T.

**Closed finite-localization source piece:** the existing localization owner transports a retained finite normalization over A to the actual L=S^-1 A. Its target is the product of surviving localized components, with original component labels, actual projections, B->B_S, localized reduction and coefficient maps. N_S, eta_S:L_regular->N_S and its one diagonal cokernel retain the existing localization functor's regular-source and cokernel comparison isomorphisms. The finite-module owner transports the actual annihilator to L, so conductor remains an ideal of the original localized ring. Proved-zero scalar restriction has dimension zero without a framing. Component numerator families pass through their actual P->A->L maps and retain their order and denominator position. Source and independent owner review are complete; the assertions below remain unexecuted under T.

| Localized normalization assertion | Retained construction |
| --- | --- |
| Cusp localized at x=t^2 | The component target is k[t,t^-1], the cokernel vanishes, conductor is the unit ideal and delta is zero. Reducedness and the zero cokernel give normality. Literal retargeting to L still needs its coherent computed inverse maps. |
| Cusp localized at x-1 | The component, coefficient action and cokernel remain actual localizations; conductor is (x,y)L. The exact coefficient presentation below supplies delta one over k and two along an actual quadratic QQ->k map. |
| Crossing xy=0 localized at x | The component with prime (x) is discarded and the (y) component survives as k[x,x^-1], preserving its original label. The one diagonal cokernel is zero, conductor is the unit ideal and delta is zero. |
| Dual numbers and killed components | Localizing dual numbers at a unit keeps a zero cokernel and delta zero while reducedness and normality remain False. Inverting epsilon kills every component and gives the actual zero ring as the empty product, with delta zero. |
| Maps and finite hypotheses | Component projections commute with the original ring maps, rho*nu=nu_S*lambda, and the regular-source and cokernel comparisons have their literal module endpoints. Undecided survival is retained; a finite source is required for annihilator transport. |

**Closed localized coefficient-presentation piece:** the existing inverse-variable quotient P[u]/(I,u_i f_i-1) of an admitted first-level finite-generator localization now supplies the ring owner's exact cover, relations and coefficient lift/descent hooks. Its decoder shape predicate is shared once, preserving all prior decoder branches. The selected presentation excludes flattened towers, alternate decoders and source-engine reuse; the existing module adapters still verify the actual scalar map. For the cusp localized at x-1, M is k[u]/(-u-1), so delta is one over k and two after an actual quadratic QQ->k restriction. The existing module preimage routine receives the same exact presentation: t^2/(t^2-1) has preimage x/(x-1), while t has none. At x, t has preimage y/x. No new module algorithm or presentation-record layer is introduced. Source and independent owner review cover these routes; execution remains under T.

Literal normal-target retargeting stays inside this node: eta_S.lift computes N_S->L_regular, but the retained B_old->B_model map cannot be retargeted to L without the corresponding B_model coordinates or inverse ring map. It retains its correct current endpoint. The next source work has returned to the remaining placement-audit category passes. Nonfinite computations and the full survey retain their required scope; no prerequisite is added.


**Closed `normalization-quotient-coefficient-dimension` (2026-10-10):** the existing chosen-presentation module owner now retains one exact coefficient-restriction dimension and, when finite, an actual basis with inverse coordinates. Its shared global polynomial calculation includes the coefficient ideal in every free coordinate. The restriction constructor retains the original module, the exact scalar map and its result; infinite dimension stays aleph0 without finite framing. The old scalar-ring basis route handles the actual quadratic field tower. The existing local-length calculation consumes the same cached dimension. Elementwise normalization component maps and the coefficient cover now use the general ring-map constructor, whose callbacks receive ring elements. Source review found no remaining blocker in these named cases; plain Python parsing follows the banked source commit, and Sage assertions remain under T. No prerequisite node was filed. Next: `normalization-extensions-retain-coefficients`.

| Coefficient-dimension assertion | Source correspondence |
| --- | --- |
| Cusp quotient over k | The retained presentation represents B/image(A). Its polynomial standard monomials give one basis class, represented by t; basis images descend to actual module elements and normal forms supply inverse coordinates. |
| Quadratic QQ->k tower | Restrict first along the retained k->A map, then along the selected QQ->k map. The existing scalar-basis construction combines the two field basis labels with the one module basis label, giving dimension two. |
| Infinite quotient and trailing free component | A missing leading component already supplies infinitely many standard monomials. Other infinite staircases return aleph0. Neither branch supplies a finite basis or finite presentation over the field. |
| Finite and zero quotients | kbase and the retained global standard basis provide mutually inverse basis images and coordinates; the empty framing and zero-dimensional quotient have their empty bases. |
| Same operation at the local-length consumer | The single-point support and residue-degree checks remain at finite_length_at_closed_point, while its coefficient dimension comes from the shared cached result. |


**Finite normalization module retained (2026-10-10):** the existing affine packet now carries the actual finite presented normalization module, its realization, one diagonal unit map, its cokernel and the exact coefficient map, together with component numerators and projections. It reuses the already delivered polynomial kernels/preimages and module biproduct. Numerator and variable-image families cross from Singular one polynomial at a time, preserving their defining order; passing them through an ideal constructor could erase a denominator position or collapse the cusp's two images. Source review establishes the module and map equations; execution remains under T. The active coefficient-dimension node supplies the next result, followed by the public normalization owner. No new prerequisite was filed.

**Closed `placement-audit` delivered invariant/locus piece (2026-10-10):** the semiring, set, monoid, additive-group and commutative-ring owners now carry the general operations identified in the selected quotient pass, with its actual quotient/localization computations and promoted consumers retained. The full disposition table below records the inspected category/up-set and arrow inheritance. This closes the fourth named steward-chain piece. The remaining category passes, five normalization introductions, optional supplied-cardinality transport and broader nonfinite value algorithms are explicitly named inside the existing nodes. The original whole-survey requirement remains part of the placement remainder; the [x] marker does not claim that survey is finished. `architecture-remediation` stays open, and now directly retains the existing normalization dependency. Next ready work: `normalization-quotient-coefficient-dimension`, followed by the normalization module/extension owner. No prerequisite node was filed.

**Closed `localized-quotient-invariants-use-exact-ideals` (2026-10-10):** the named finite integer quotients and reduced localized affine component maps now have their exact source constructions. Nonfinite quotient ideals use the actual augmented generator kernel and module inclusion; a source unit supplies its quotient inverse without a finite comparison. The proved-proper/local hypothesis is required to infer a quotient nonunit. Self-realized quotients retain their ideal radical computation and reach an explicit dimension assertion when no value algorithm is supplied. The broader nonfinite invariant algorithms remain named inside this existing node. No prerequisite was filed; next is closure of the delivered `placement-audit` piece.

| Named closure assertion | Source correspondence and mathematical reason |
| --- | --- |
| Z_(3)/(3), Z_(3)/(9), and Z_(3)/(1) | Contraction gives (3), (9), and (1) in ZZ. The cached canonical injection from ZZ/(d) is an isomorphism because every localized denominator acts injectively on that finite set and hence is a unit. Characteristic and cardinality are d, with one for the zero ring. |
| Field/domain/reduced/normal and dimension | Actual-ideal maximality, primality and radicals distinguish d=3 from d=9. The finite comparison transports dimension zero and normality; the zero ring follows the common owner's vacuous normality case. The class of 3 in the nine-element quotient is nonzero and has square zero. |
| Exact inverse and comparison maps | The inverse comparison sends [a/s] to [a][s]^-1, so [1/2] maps to 5 modulo 9. Both composites are identities on their actual parents; the selected source ideal and projection are retained. The same argument gives ZZ[1/2]/(3). |
| Minimal primes, components and finite total quotient | Exact source/cover prime families descend to owned ideals and actual localized component parents. A regular element in a finite ring is already a unit, so the retained total-quotient arrow is the identity, also for d=9. |
| Reduced two-component affine localization | Saturation removes precisely the components meeting the inverted system. The contracted quotient B injects into the localized quotient Q; B's total-quotient map factors through the actual localization by a/s mapping to g(a)g(s)^-1. This preserves both xy=0 component images, the surviving-component case and the exact target of the total-quotient arrow. No isomorphism B~=Q is inferred for infinite B. |
| Ideals of L/(x^2), L=QQ[x,y]_(x,y) | The preimage H=(lifts of generators)+(x^2) and the projected source relation kernel retain the presented ideal and inclusion. Ideal arithmetic, radical and finite prime transport compute on H. The inverse of 1+y descends from L, while y stays a nonunit in the proper local quotient. |

These are source-level closure correspondences, not executed Sage results. The actual runtime assertions remain in `core-usability-session` under T, as required during M1/DEV-58.

**Closed `free-module-coordinates-preserve-undecided-scalar-equality` (2026-10-10):** sparse vectors and presented coordinates retain finite containing coefficient families, discard only proved zeros, preserve equality propositions and construct exact support at the finite predicate-subset owner. Their actual framing, linear-map, relation, tensor, biproduct and localization consumers now use those families. Source follow-through during the localization review also repairs the dual-map transpose, orthogonal summand embedding and scalar-extension unit: these retain undecided coefficients through the same finite containing family, with their exact maps and labels unchanged. The quotient-ideal producer retains the exact source kernel, the presented ideal and its regular-module inclusion, including nonfinite localized quotient sources; computations do not replace that source by a fraction field. The shared polynomial adapter uses a global order on the actual cover. The final localized equality branch preserves undecided comparisons and requires the nonzero premise of its torsion-free argument. Source closure is recorded in the existing node; the separating expectations remain under T. Next in the steward's chain: reconcile and close `localized-quotient-invariants-use-exact-ideals`, then climb to `placement-audit`. No prerequisite was filed.

**Closed `finite-predicate-subsets-retain-undecided-membership` (2026-10-10):** the finite predicate-subset owner now retains undecided membership, FiniteSets placement and the actual inclusion without claiming an enumeration or exact count. Composition preserves the subset-inclusion premise, and the finite-subset and Mor constructors use the known finite bounds. Decided predicates retain their ordered filter. The closed piece and the broader optional-cardinality transport remainder are named inside the existing TODO node; no new prerequisite was filed. Next in the steward's chain: `free-module-coordinates-preserve-undecided-scalar-equality`, using the prepared coordinate and consumer patch.

**Exact polynomial-module source unit (2026-10-10):** finite affine quotients now expose their actual coefficient cover through the existing ring contract. The module owner shares exact lifted relations, kernel data and preimage solving over that cover, including the coefficient ideal in every free coordinate. Relation equality uses the same exact polynomial membership. Finite-free kernels outside PID cases delegate to the common finite-presentation owner. This supplies the preimage prerequisite for normalization fractions and the kernel prerequisite for nonfinite quotient ideals. The new required DAG nodes retain undecided finite support and module-specific coefficient dimension; their source work has started. Runtime assertions remain under T.

**Localized binary-ideal source unit (2026-10-10):** sum, product, finite intersection, colon, saturation and nonnegative powers now compute on retained source ideals and extend to the exact localization, recursively through localization towers. Colon and saturation of quotient ideals use the existing owned cover operations, including the integer PID case. The quotient-preimage proof no longer asserts that preimage preserves products. Optional exact-result seams keep localized membership and multiplicative-system predicates undecided when no source algorithm is selected. The maintained Sage ideal source explicitly supplies integer polynomial radical, primary decomposition and colon; Singular saturation iterates exact colon and standard-basis reduction and is also used by its integer primary-decomposition library. These integer polynomial cases remain admitted, without coefficient rationalization. Separating assertions are retained under T. Next: present ideals of nonfinite localized quotients through their exact quotient source, then reconcile the full localized-invariant node.

**Localized component-map source unit (2026-10-10):** the total-quotient map of a reduced localized quotient now factors through the existing total-quotient map of its retained contracted quotient. Saturation makes every denominator regular there, so the localization universal map supplies the exact arrow into the same component-field target. Actual irreducible components keep the selected localized source. `LocalizationRings.induced_morphism` no longer demands an unjustified map from its larger fraction-field realization. The two-component, single-survivor and fraction equations are retained unexecuted under T. Next: exact ideal arithmetic for nested localizations and quotient covers, then reconcile the full localized-invariant node.

**Finite-unit source checks:** `31b81e8134` passed focused AST parsing of its three source files. The required source-only construction view for `LocalizationRings` and `CommutativeIdeals` completed within its two-minute bound; all 62 lines of `.tmp/localized-quotient-owner-constructions.txt` were read. Its `None` alternatives follow optional private results past the public assertions and are static-inference limits. No Sage, tests or QC were run.


**Finite localized-quotient comparison source unit (2026-10-10):** the localization owner now retains the canonical injection from the contracted quotient and its explicit finite inverse pair in the owned ring core. Exact computation crossings keep the original quotient, source and projection; characteristic uses the injection, while cardinality, dimension, normality and unit inversion use the finite comparison. Ideal primality, radicals and finite prime families stay at their actual owners, including recursive owned PID cover operations. Optional-result dispatchers preserve propositions at unsupported cases. Every finite commutative ring now retains the identity as its total-quotient map. The separating integer, quotient-ideal and map assertions remain unexecuted under `core-usability-session`. The next source unit is the nonfinite component/total-quotient factorization through the contracted quotient and the exact nested-localization ideal operations it needs; the required node remains open.


**Exact localized-ideal source unit (2026-10-10):** `CommutativeIdeals.contraction_from_localization` now uses finite primary decomposition for a prime complement, retaining every primary component contained in the prime, including embedded components. PID decomposition reuses the owned factorization; quotient presentations transport through their cover, and localized primary components/radicals stay in the actual localized ring. The colon-based membership criterion remains independent of primary decomposition. The required quotient-invariant node stays open; its next work is the retained canonical comparison with the contracted quotient and the exact computation crossings. Separating assertions, including nonsaturated integer ideals and a zero-divisor source, are under `core-usability-session`.

**Banked quotient-owner source checks:** `8b392727bb` passed focused Python AST parsing together with the committed indexed-family and Čech changes. The TODO graph has 130 unique nodes, resolved dependencies and no cycle. The required source-only `just category-graph constructions --select QuotientRings --select OwnedRings.Commutative --select OwnedSemirings --select Monoids` completed in under a minute; all 36 returned lines in `.tmp/quotient-owner-constructions.txt` were read. Its unresolved hook returns are static-inference limits, not computed mathematical answers. No Sage or tests were run.


### Whole-category placement: `OwnedRings.Artinian` (2026-10-11; source pass closed)

This completes `placement-owner-ownedrings-artinian` in `categories/rings/ring_foundation.py`. Five related docstrings are clarified. Every method body, graph edge, placement, constructor, name and arrow remains unchanged; the complete declaration and its actual inherited structures and selected constructor routes have their own pass.

#### Definition and implication read before editing

The actual [Mathlib Artinian definition source](https://github.com/leanprover-community/mathlib4/blob/be31cde2c2cb07d7562e5e891b302f9286cd0a68/Mathlib/RingTheory/Artinian/Defs.lean)
and its [generated documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Artinian/Defs.html)
were read before the patch. The formal `IsArtinianRing R` is
`IsArtinian R R`: the left regular module has the descending chain
condition on submodules, equivalently on left ideals. The declaration
explicitly distinguishes this left convention from the right-module
condition. Although the introductory prose also describes a convention
using unqualified Artinian for both sides, that is not the formal predicate
being adopted here. The owned definition now states its side expressly.

The actual [Mathlib Hopkins–Levitzki source](https://github.com/leanprover-community/mathlib4/blob/6be3d352cec3ceabd28bf85266d28646e02f1975/Mathlib/RingTheory/HopkinsLevitzki.lean)
and its [documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/HopkinsLevitzki.html)
were also read. Its instance from `IsArtinianRing R` to
`IsNoetherianRing R` has the general `Ring R` hypothesis, with no
commutativity assumption. Thus the existing edge is correct for the
left-regular-module convention now used by both owned axioms. This is a
ring theorem; it does not promote every Artinian module over an arbitrary
ring to a Noetherian module.

The class, entry, predicate, and alias documentation now agree. The zero
ring is permitted. There is no right-Artinian implication, and existence
of a finite composition series does not supply a chosen series. The
commutative session shorthand remains the same category value.

#### Complete introduction inventory

| Introduction | Disposition and weakest hypotheses |
| --- | --- |
| `_repr_object_names()` | Retain the existing category name, "artinian rings", with the left convention defined by the class. |
| `an_object()` | Retain canonical owned `GF(2)`. A field's only left ideals are zero and the whole field, so it satisfies the axiom. |
| `extra_super_categories()` | Retain the exact edge to `OwnedRings().Noetherian()`. Hopkins–Levitzki applies to every left Artinian associative unital ring; no commutativity or extra selected data are needed. |

There are no own ParentMethods, ElementMethods, parameters, selected-data
suppliers, computation hooks, Mor introductions, or arrow providers. The
existing common SubcategoryMethods entry supplies the axiom refinement.
The common `is_artinian()` predicate reads its established placement and
otherwise returns an `AtomicProposition`; it is not duplicated here.
`OwnedArtinianRings()`, exported as `ArtinianRings`, still returns
`OwnedRings().Commutative().Artinian()`.

#### Complete strict authored up-set: 16 owners

| Strict authored ancestor | Retained structure |
| --- | --- |
| `OwnedRings.Noetherian` | The left regular module is Noetherian, by Hopkins–Levitzki. |
| `OwnedRings` | Associative unital ring. |
| `OwnedSemirings` | Unital multiplication, commutative addition, distributivity. |
| `OwnedRngs` | Associative multiplication and additive inverses. |
| `Monoids` | Associative unital multiplication. |
| `Semigroups` | Associative multiplication. |
| `Magmas.Unital` | Multiplication and its identity. |
| `Magmas` | Multiplication. |
| `AdditiveGroups.AdditiveCommutative` | Additive abelian group. |
| `AdditiveGroups` | Additive group. |
| `AdditiveMonoids` | Associative addition and zero. |
| `AdditiveSemigroups` | Associative addition. |
| `AdditiveMagmas.AdditiveCommutative` | Commutative addition. |
| `AdditiveMagmas` | Addition. |
| `Sets` | Underlying set. |
| `Objects` | Owned object. |

The own base and explicit Noetherian edge produce this complete authored
up-set. Synthetic axiom meets and implementation wrappers are not extra
authored owners. Commutative, NoZeroDivisors, Nontrivial, Division, Fields,
Local, Complete, PrincipalIdeals, finite cardinality, and a fixed
coefficient algebra are not uniform consequences. A field witness's
additional placements are not ancestors of this owner.

No mathematical operation remains at a needlessly restrictive owner. The
three introductions respectively name this category, supply its witness,
and express its implication. Noetherianity alone cannot supply an Artinian
witness on every admitted ring: the descending integer ideals `(2^n)` do
not stabilize. Nothing reverses the declared edge.

#### Actual fixed Mor

The already reviewed owned CategoryWithAxiom carries CategoryPacketMethods.
Its selector retains literal source and target objects and inherits the
OwnedRings RingMorCategoryConstruction through the declared supergraph.
The fixed provider remains RingMor with RingMorphism elements and the
inherited semiring, rng, multiplicative, additive, and set laws. The
additional Noetherian path refers to the same ring-arrow construction;
it introduces no second comparison category or stronger arrow condition.

The arrows are all unital ring maps between admitted objects. The first
projection from the selected finite product `GF(2) x GF(2)` to `GF(2)`
is a noninjective example: it kills `(0,1)`. The existing CartesianProduct
constructor reads the actual owned factors and expressly supplies Artinian
placement when all factors have it. Its target has the field-to-Artinian
edge. This demonstrates admitted endpoints without imposing injectivity
on RingMor. Identities and compositions retain the existing literal
endpoints and ring laws. No flatness, continuity, finite-type, or chosen
composition-series data are required.

#### Supplied examples and computation boundaries

The public `GF` constructor lowers its integer argument, invokes the native
finite-field constructor, and returns its canonical owned parent. The
selected finite-field branch supplies Fields, whose existing extra edge
supplies Artinian. The native QQ branch also supplies Fields while retaining
CountablyInfiniteSets, so the property cannot imply a finite underlying set.

The selected `Zmod(1)` branch supplies FiniteSets. The complete native
classifier then has a shared final step which adds Artinian to every
proved finite ring; the branch does not return before that step. Thus the
existing zero-ring source route is compatible with mathematical admission,
without a new recognizer or constructor change. Finite square matrices over
`GF(2)` likewise satisfy the condition while multiplication need not be
commutative. These examples separate extra hypotheses from the owner axiom.

This pass supplies no general algorithm deciding descending-chain
stabilization and no chosen composition series. A parent without supplied
Artinian placement still returns the existing owned proposition. In
particular, the mathematical non-Artinianity of ZZ does not make that
predicate's current unknown answer a computed False. The source changes
neither collapse propositions nor widen a selected algorithm's scope.

#### Closure assertions and scope

- The existing owner has exactly three introductions, all disposed above;
  its strict authored up-set has exactly 16 owners and its fixed Mor is the
  inherited all-unital-ring-map provider.
- `OwnedRings().Artinian().an_object()` returns owned `GF(2)` through the
  current selected constructor and field edge. Its inherited Noetherian
  placement is justified by the same-side Hopkins–Levitzki theorem.
- The zero ring remains permitted; QQ remains an infinite Artinian
  example; no commutativity, domain, field, or Nontrivial edge is added.
- The product-of-fields projection has admitted Artinian endpoints and
  demonstrates why the inherited arrow category has no injectivity
  requirement.
- The session alias remains the commutative refinement, and unknown common
  predicate results remain `AtomicProposition` values.

These are source-supported assertions, not executed results. The full
current owner and its related declaration sites were read; the relevant
unchanged constructor, field edge, common spine, axiom propagation, and
fixed-Mor sources were rechecked. There is no new prerequisite, owner row,
category edge, unfinished own introduction, or denominator change. Other
Artinian-consuming algorithms remain at their existing separately tracked
owners. Protected construction and user-simulation tests are untouched.

M1 verification is a focused diff check followed by post-commit stdlib AST of the sole changed Python file. No project import, Sage, runtime test or generated-view regeneration belongs to this bank.

### Whole-category placement: `OwnedRings.Noetherian` (2026-10-11; source pass closed)

This is the complete pass for `placement-owner-ownedrings-noetherian` in `categories/rings/ring_foundation.py`. It clarifies four related docstrings while preserving the category name, witness, graph, predicates, constructors and arrows. The complete own declaration, actual inherited structures and selected constructor examples were read before the repair.

#### Definition read before the clarification

The actual [Mathlib Noetherian definition source](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/RingTheory/Noetherian/Defs.lean)
and its [generated documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Noetherian/Defs.html)
were opened and read before writing the patch. `IsNoetherianRing R`
abbreviates the regular-module condition `IsNoetherian R R`. Its introductory
comment expressly selects the left-module convention in the absence of
commutativity. The chain-stabilization and ideal-finite-generation theorems
state the equivalent conditions.

Accordingly, this ring owner means that every ascending chain of **left
ideals** stabilizes, equivalently every left ideal is finitely generated.
It asserts neither commutativity nor a right-module condition. In a
commutative ring the side distinction disappears. The zero ring satisfies
the property, and finite generation is a proposition rather than a selected
generating-family datum. The existing accessor, class definition, and common
ring predicate now use consistent wording for this convention.

[Sage's Noetherian category documentation](https://doc.sagemath.org/html/en/reference/categories/sage/categories/noetherian_rings.html)
was also read directly: its category is expressly commutative. That narrower
Sage category cannot justify adding a commutativity edge to this existing
OwnedRings axiom. The current session alias already selects the commutative
refinement; its docstring now says so explicitly, with no change to its value.

#### Complete introduction inventory

| Introduction | Disposition |
| --- | --- |
| `_repr_object_names()` | Retain the category-specific name, "noetherian rings". No other owner may receive that name merely because it forgets this property. |
| `an_object()` | Retain canonical owned ZZ. It is a genuine Noetherian witness, reached through the existing native ring constructor. |

No ParentMethods, ElementMethods, parameter, selected-data supplier,
computation hook, extra supercategory edge, Mor family, or arrow provider is
introduced at this owner. Its registration in `all_axioms` and the existing
OwnedRings SubcategoryMethods accessor supply the axiom refinement. The
common ring predicate `is_noetherian()` reads established placement and
otherwise retains its owned proposition; it is not duplicated here.

The existing `OwnedNoetherianRings()` function, exported as
`NoetherianRings`, explicitly returns the commutative refinement. This is a
session shorthand and does not make commutativity a property of the present
bare owner. Its value remains unchanged.

#### Complete strict authored up-set: 15 owners

| Strict authored ancestor | Retained structure |
| --- | --- |
| `OwnedRings` | Associative unital ring. |
| `OwnedSemirings` | Unital multiplication, commutative addition, distributivity. |
| `OwnedRngs` | Associative multiplication and additive inverses. |
| `Monoids` | Associative unital multiplication. |
| `Semigroups` | Associative multiplication. |
| `Magmas.Unital` | Multiplication and its identity. |
| `Magmas` | Multiplication. |
| `AdditiveGroups.AdditiveCommutative` | Additive abelian group. |
| `AdditiveGroups` | Additive group. |
| `AdditiveMonoids` | Associative addition and zero. |
| `AdditiveSemigroups` | Associative addition. |
| `AdditiveMagmas.AdditiveCommutative` | Commutative addition. |
| `AdditiveMagmas` | Addition. |
| `Sets` | Underlying set. |
| `Objects` | Owned object. |

The existing CategoryWithAxiom construction retains the ring and these
ancestors. Synthetic axiom meets and implementation wrappers are not
additional authored owners. Commutative, NoZeroDivisors, Nontrivial, Local,
Complete, Artinian, Division, Fields, PrincipalIdeals, finite cardinality,
and a fixed coefficient algebra are not uniform consequences. In particular,
the Artinian-to-Noetherian edge is a descendant implication, not an upward
Noetherian-to-Artinian edge.

Every strict ancestor forgets the Noetherian property, so no operation has
been left here merely for a convenient finite algorithm. The two own
introductions implement the name and witness of this exact category, rather
than a mathematical operation that a weaker category should also supply.

#### Actual fixed Mor

CategoryWithAxiom carries the owned CategoryPacketMethods. Its fixed-endpoint
selector walks the declared supercategory packet, preserves the literal
endpoints, and inherits OwnedRings' RingMorCategoryConstruction. The actual
fixed provider is RingMor and its element provider is RingMorphism; the
existing semiring, rng, multiplicative, additive, and set providers deliver
their usual laws. No new arrow class or restriction is introduced here.

The arrows are all unital ring maps between the admitted rings. They need
not be injective: the existing map `ZZ -> GF(2)` has Noetherian endpoints and
kills 2. They need not be finite ring maps either: the canonical map
`ZZ -> QQ` retains the same ring-arrow interface. Identity is the existing
RingMor identity on the literal object, and composition uses its actual
middle endpoint. No finite-presentation, flatness, continuity, or chosen
ideal-generation data are implied by this arrow category.

#### Witness, property, and computation boundaries

The selected native integer branch already places canonical ZZ in the
Noetherian category, so the witness requires no recognition algorithm.
Mathematically every integer ideal is generated by one integer. The existing
commutative PrincipalIdeals owner also declares the Noetherian implication.
The actual zero ring `ZZ/1` is finite and Noetherian; the Noetherian category
does not imply distinct zero and one. These are selected source examples,
not runtime checks.

The property asserts finite generation of left ideals, not a chosen
generating family or an algorithm to find one. No such data supplier is
introduced by this pass. The common predicate preserves unknown status for
a ring without established Noetherian placement, and this owner has no
computation capable of deciding the general property. Consequently there is
no algorithmic remainder created by its name or witness; algorithm consumers
remain at their separately tracked owners.

The full common ring/semiring/rng/magma/additive/Set/Objects spine, owned
axiom propagation, fixed-Mor packet, canonical ZZ native placement, common
Noetherian predicate, and PrincipalIdeals implication were already read and
rechecked in their exact relevant source slices. This review does not widen
into all Noetherian consumers or claim their complete owner passes.

#### Closure assertions and exact scope

- The name still denotes the same existing ring-axiom owner, now with its
  left-ideal convention stated explicitly. No new category or property name
  is added, and the authored-owner denominator does not change.
- `OwnedRings().Noetherian().an_object()` returns the canonical owned ZZ
  already supplied by the native classifier. Its actual Noetherian placement
  makes the common predicate True without asking an engine to recognize it.
- The zero ring remains admitted through its existing finite-ring
  construction. No Nontrivial, commutativity, Artinian, domain, or field
  implication is introduced.
- The current `NoetherianRings()` alias still denotes
  `OwnedRings().Commutative().Noetherian()`.
- Fixed RingMor endpoints, ordinary ring identity/composition, and the
  admissible noninjective `ZZ -> GF(2)` example are unchanged. No stronger
  arrow property is claimed.
- A parent lacking supplied Noetherian placement retains the existing
  `AtomicProposition` from the common predicate; the definition change
  introduces neither a recognition algorithm nor Boolean coercion.

These are source-supported assertions, not executed results. The whole
two-introduction owner, all 15 strict authored ancestors, and its actual
fixed-Mor packet are covered. The selected producers already inspected in
the preceding source passes are compatible with this convention; this
closure does not claim all Noetherian-consuming algorithms. There is no new
prerequisite, unfinished own introduction, or broader consumer audit.

M1 verification is a focused diff check followed by post-commit stdlib AST of the sole changed Python file. No project import, Sage, runtime test or generated-view regeneration belongs to this bank.

### Whole-category placement: the three zero-product/domain owners (2026-10-11; source passes closed)

This bank completes three independent owner passes in `categories/rings/ring_foundation.py`. The existing commutative zero-product owner is corrected, and two providers are authored on existing Nontrivial axiom intersections. Each new provider has its complete pass in this bank; neither is an unfinished prerequisite.

| Complete owner pass | Original and remaining introductions | Strict authored ancestors |
| --- | --- | ---: |
| `OwnedRings.NoZeroDivisors.Commutative` | Seven original; two remain. | 18 |
| `OwnedRings.NoZeroDivisors.Nontrivial` | All three new introductions. | 17 |
| `OwnedRings.NoZeroDivisors.Commutative.Nontrivial` | All six new introductions. | 21 |

#### Definitions and the whole original inventory

The zero-product axiom says that `xy = 0` implies `x = 0` or `y = 0`. It holds in the zero ring. Nontriviality is the separate assertion `1 != 0`. A commutative ring with both properties is an integral domain. These definitions separate hypotheses that the former commutative provider conflated. They agree with the actual axiom declarations and the selected integer, field, quotient and localization constructions read before the repair.

For a nontrivial zero-product ring R, the subset R minus zero contains one and is multiplicatively closed. This does not require commutativity. A commutative fraction field instead needs the full integral-domain meet. A finite family of fractions spans a fractional R-ideal because the product of their nonzero denominators is a common nonzero denominator; Noetherianity or principality is not needed for this mathematical definition.

| Original introduction on the commutative zero-product owner | Complete disposition |
| --- | --- |
| `_repr_object_names()` | Retain here, naming commutative rings without zero divisors and allowing the zero ring. |
| `an_object()` | Retain the canonical owned ZZ witness. Its stronger placement does not strengthen this category's definition. |
| `nonzero_multiplicative_submonoid()` | Move to `NoZeroDivisors.Nontrivial`, removing unnecessary commutativity while adding necessary nontriviality. Keep the cached single existing construction. |
| `fractional_ideal(*module_generators)` | Move to `NoZeroDivisors.Commutative.Nontrivial`; retain the selected finite-family normalization and existing fractional-ideal constructor. |
| `fraction_field_localization()` | Move to the same exact domain owner; retain localization at the selected nonzero submonoid. |
| `fraction_field_map()` | Move with its selected canonical localization and field comparison maps. |
| `fraction_field()` | Move with the same selected target, retaining a field itself in the field case. |

The noncommutative provider introduces only its exact category name, canonical owned ZZ witness, and the moved cached nonzero-submonoid method. The full domain provider introduces only its name, the same canonical witness, and the four fraction operations above; it inherits the submonoid method. Neither adds an element provider, extra axiom implication, parameter, public forwarding layer, parallel constructor or arrow family. `OwnedIntegralDomains()` is the exact commutative/NoZeroDivisors/Nontrivial meet. `OwnedPrincipalIdealDomains()` adds PrincipalIdeals to that meet, and the exported aliases continue to delegate to these same owners.

Deleting Nontrivial admits the zero ring, whose complement of zero is empty and does not contain one. Deleting NoZeroDivisors admits ZZ/6, whose nonzero classes 2 and 3 multiply to zero. Deleting commutativity admits the selected QQ<x,y>, whose nonzero elements form a submonoid but which cannot embed in a commutative field. These separators establish the required hypotheses. The four fraction operations undergo a necessary-hypothesis correction; no impossible outside-old-home assertion is claimed for that restriction.

#### Complete strict authored up-sets

The three columns below enumerate every strict authored ancestor. C denotes the bare commutative zero-product owner, N the nontrivial zero-product owner, and D the full domain owner. Their respective totals are 18, 17 and 21. The existing CategoryWithAxiom propagation supplies the meets; generated axiom intersections and implementation wrappers are not additional authored identities.

| Authored ancestor | Definition retained | C | N | D |
| --- | --- | :---: | :---: | :---: |
| `OwnedRings.NoZeroDivisors.Commutative` | Commutative zero-product ring, possibly zero. | — | — | yes |
| `OwnedRings.NoZeroDivisors.Nontrivial` | Nontrivial zero-product ring, without commutativity. | — | — | yes |
| `OwnedRings.NoZeroDivisors` | The zero-product axiom. | yes | yes | yes |
| `OwnedRings.Nontrivial` | Distinct zero and one. | — | yes | yes |
| `OwnedRings.Commutative` | Commutative unital ring. | yes | — | yes |
| `Magmas.Commutative` | Commutative multiplication. | yes | — | yes |
| `OwnedRings` | Associative unital ring. | yes | yes | yes |
| `OwnedSemirings` | Unital multiplication, commutative addition and distributivity. | yes | yes | yes |
| `OwnedRngs` | Associative multiplication and additive inverses. | yes | yes | yes |
| `Monoids` | Associative multiplication with identity. | yes | yes | yes |
| `Semigroups` | Associative multiplication. | yes | yes | yes |
| `Magmas.Unital` | Multiplication with a two-sided identity. | yes | yes | yes |
| `Magmas` | Binary multiplication. | yes | yes | yes |
| `AdditiveGroups.AdditiveCommutative` | Abelian addition. | yes | yes | yes |
| `AdditiveGroups` | Addition with inverses. | yes | yes | yes |
| `AdditiveMonoids` | Associative addition with zero. | yes | yes | yes |
| `AdditiveSemigroups` | Associative addition. | yes | yes | yes |
| `AdditiveMagmas.AdditiveCommutative` | Commutative addition. | yes | yes | yes |
| `AdditiveMagmas` | Binary addition. | yes | yes | yes |
| `Sets` | Underlying set. | yes | yes | yes |
| `Objects` | Owned mathematical object. | yes | yes | yes |

No strict ancestor of N supplies both of its necessary premises; no strict ancestor of D supplies all three domain premises. Division, Fields, Local, Complete, Noetherian, PrincipalIdeals, finiteness and a selected scalar algebra are not uniform consequences of these owners. The new authored providers also become strict ancestors of already reviewed descendants: Division now has 18 rather than 17, Fields 29 rather than 27, and Prime 30 rather than 28. Their complete records above/below explicitly include these newly reviewed providers; their introductions and arrows do not change.

#### Actual arrows, inclusion and canonical fraction maps

All three owners inherit the ordinary RingMor packet. The owned axiom wrapper uses CategoryPacketMethods, whose fixed-endpoint selector walks the actual supercategories and retains the literal endpoints. OwnedRings supplies RingMorCategoryConstruction, its fixed RingMor and actual RingMorphism element provider, including the existing semiring, rng, multiplicative, additive and set providers. Identity and composition retain those exact endpoints; no property intersection introduces an injection-only or coefficient-algebra arrow restriction.

The existing nonzero-submonoid constructor retains the exact source R, its predicate, facade elements and `kind="nonzero_elements"` metadata. Its cached inclusion is `Monoids().Mor(S, R)._from_submonoid_inclusion()`, sending the source elements to themselves under multiplication. It does not select a fraction ring as codomain or enumerate the predicate truth set.

For a nonfield domain with the existing selected computation, set L to `R.fraction_field_localization()` and K to `R.fraction_field()`.

| Retained map | Exact domain | Exact codomain | Definition |
| --- | --- | --- | --- |
| `L.localization_map()` | R | L | r maps to r/1. |
| `L.fraction_field_comparison()` | L | K | The same fraction in the selected field realization. |
| `R.fraction_field_map()` | R | K | The comparison composed with the localization map, with literal middle object L. |

If R is already a field, K and the localization target are literally R, and the fraction map is the explicit ordinary RingMor identity. The fractional-ideal module companion now reads this actual fraction map and its codomain for scalar restriction; it does not reconstruct a map from a conversion callback. The same supplied finite family reaches the existing constructor. Its prior normalization is preserved: over ZZ the family is reduced by `_zz_fractional_generator` to the selected principal generator, so no claim is made that the original family remains verbatim as a framing.

The ordinary unital map ZZ to GF(2) is admissible and kills 2. It cannot restrict to the two nonzero submonoids or extend to QQ, where 2 is a unit. Thus neither operation is asserted to be a functor on all inherited ring arrows. No arrow restriction or nonexistent universal extension is added.

#### Undecided membership and affected consumers

The public predicate-submonoid contract now states the caller's actual premises: the truth set contains one and is closed under multiplication. The existing constructor still rejects proved false membership of one; it recognizes an owned Predicate before Boolean conversion. A one-point check is not presented as a closure proof.

The same engine's owned `is_parent_of` first examines membership in the exact source. Proved nonmembership returns False; proved membership permits normalization and evaluation; undecided ingress returns an Atomic proposition without applying the predicate outside its domain. An owned predicate result survives unchanged. Element construction rejects proved nonmembership and gives its explicit assertion for undecided admission; it does not use Python `in` internally. The nonzero predicate is owned `negation(element == R.zero())`. External Python `in` remains a Boolean protocol. Generated-submonoid membership and actual inverse algorithms are not expanded.

| Affected owner or consumer | Source correction and retained assertion |
| --- | --- |
| `is_integral_domain()` | True on the exact domain placement. On a bare commutative zero-product ring, return owned `negation(one == zero)`; zero is False and unknown stays a proposition. Other existing hooks remain. |
| `is_regular()` | The unique zero-ring element is regular because multiplication on the singleton is injective. A true domain uses owned negation of zero status; other rings retain the colon-ideal definition. |
| `total_quotient_map()` and Cartier | Preserve zero/finite identity cases; use a fraction field only for a true domain. Cartier asks this existing common map directly and retains its actual codomain. |
| `_placed_nonzero()` | Bare NoZeroDivisors no longer implies nontriviality; actual Nontrivial and infinite placement evidence remain. |
| Localization cardinality and fraction-value admission | Proved zero source gives cardinality one before domain handling. The domain helper and optional source fraction model require the full meet; undecided answers retain the existing boundary. The localized-module caller already uses the corrected IntegralDomains alias. |
| `FractionalIdeals` | Its existing parameter-category protocol requires the exact domain owner. Its module scalar restriction reuses the retained fraction map, without changing the selected ZZ/order algorithms. |

Literal weak zero-product occurrences were judged by their own mathematics. Multiplication by a nonzero ideal generator remains injective under the bare axiom. Zero/unit ideal cases already precede proper ideal cases. A prime localization has a proper prime and hence a nontrivial Local target. These correct uses are preserved.

#### Constructor evidence and actual outside-old-home witness

| Selected construction | Exact placement justified by its data |
| --- | --- |
| Native ZZ, fields, orders and DVR cases | Use the corrected exact domain/PID aliases where already justified. Native ZZ retains its explicit Nontrivial placement; orders use the actual integral-domain/Noetherian component. |
| Polynomial, Laurent and formal-series rings | Inherit Nontrivial independently through the constant embedding, alongside applicable zero-product placement. |
| Native ZZ/1 | Receives the bare zero-product axiom, never Nontrivial. |
| Native free associative algebra | Inherits NoZeroDivisors and Nontrivial independently from the coefficient ring, with no commutativity or Noetherian inference. |
| Quotients | A proved prime ideal is proper and yields the strict domain meet; a proved maximal ideal yields Fields. Only literal True predicates justify those placements. |
| Finite selected localization | Preserves the bare zero-product axiom even when zero is inverted. Strict domain/PID inheritance additionally requires proved exclusion of zero from S. |
| Prime localization | Properness and Local supply Nontrivial; weak zero-product inheritance remains correct. The optional source fraction model requires a strict source domain. |
| Adic completion | A proved proper defining ideal gives a surjection to a nonzero first quotient and hence Nontrivial. The unit-ideal zero case is preserved; an unknown properness test gives no such inference. No general completed-domain claim is taken from the truncation engine. |

The actual tensor-algebra construction on the framed QQ-module with labels x,y enters `_tensor_algebra_on`, `_native_free_algebra`, `_NativeFreeAlgebraParent`, `_OwnedAlgebraParent`, `_OwnedRingParent` and the common classifier. It retains the literal coefficient field, labels, word basis and finite coefficient data. In a degree/word order, the product of the largest words is the unique largest product and its coefficient is the nonzero product of leading coefficients. Constants embed, so zero differs from one. The distinct words xy and yx prove that this actual A = QQ<x,y> is outside the old commutative home. Its nonzero submonoid method is now supplied by N; x, y and xy belong, zero does not, and its exact inclusion preserves one and multiplication. These are source closure assertions, not execution results.

Selected ZZ retains its cached nonzero submonoid and literal QQ fraction target; its canonical map sends an integer to the same rational integer. QQ itself retains the field identity case. The fractional ideal of ZZ spanned by 2 retains its module in QQ, normalized generating family, inclusion and actual scalar map. Zero inversion and undecided propositions do not create a strict domain placement.

#### Named computation remainders and verification boundary

The current nonfield fraction factory still needs a supplied distinct computation model; an opaque self-realized domain without one retains its explicit assertion. The fractional-ideal realization still supplies the selected ZZ and OwnedOrders cases. General domain syzygies, ideal inverses, predicate decisions and generated-submonoid membership algorithms are not supplied merely by correcting placement.

The protected assertion `IntegralDomains().fraction_field()(ZZ) is QQ` in `tests/constructions/test_functors_construct.sage` is unchanged. The current implementation supplies `ZZ.fraction_field()` but not that requested category-level entry. The missing entry remains an interface/computation obligation inside this existing domain node and T. The assertion fixes the object result QQ; it does not demand a Frac extension on every ring arrow. No protected assertion is edited, relabeled, disabled or executed.

The protected additive NN assertions in `tests/constructions/test_group_actions_construct.sage` also remain fixed: even NN and the additive submonoid generated by 3 and 5, including 8 and 0 but excluding 7, need the additive construction. The current multiplicative entry requires one and does not supply it. This representation remainder is named at the existing unchecked AdditiveMonoids node, with no prerequisite and no whole-pass claim for that owner.

Source evidence comprises all three complete owner bodies, the entire relevant 379-row occurrence ledger, the complete fractional-ideal and predicate-submonoid sources, the actual producer chains and selected construction/map callers, and the already read full ring/semiring/magma/additive/set/object ancestry, owned axiom propagation and actual fixed-Mor definitions. Companion fixes do not count as complete passes at FractionalIdeals, Monoids, AdditiveMonoids, PrincipalIdeals or RingMor. M1 / DEV-58 limits this bank to focused source review, a diff check and post-commit stdlib AST of exactly the six changed Python files. Runtime assertions and generated views remain under T.

### Whole-category placement: `OwnedRings.NoZeroDivisors` (2026-10-11; source pass closed)

This is the complete pass for `placement-owner-ownedrings-nozerodivisors`.
Its defining assertion is `xy = 0 => x = 0 or y = 0`. This property holds
in the zero ring and does not assume commutativity. The old display name
`domains` obscured that independent nontriviality convention; it now says
`rings without zero divisors`, with those boundaries stated in the
definition. This changes no category edge, constructor, arithmetic,
predicate implementation or morphism.

**Complete introductions.** Exactly two methods are introduced here.

| Introduction | Placement and closure |
| --- | --- |
| `_repr_object_names()` | The category-specific name belongs here and now states the actual zero-product axiom. |
| `an_object()` | The literal canonical owned ZZ remains the stronger category's witness under the common category-witness contract. |

There is no own ParentMethods, ElementMethods, MorphismMethods, Mor-family,
protected computation hook, parameter or extra supercategory. The nested
Commutative class is a separately inventoried owner. No public mathematical
operation needs promotion to a weaker owner: category names and witnesses
implement the common category contract at their actual category. The
complete 50-line source/specimen search found no behavior selected by the
old display string; consumers select the axiom. Other integral-domain names
belong to the separate commutative refinement.

**Entire strict authored up-set: 15 owners.** CategoryWithAxiom retains
OwnedRings and all its authored ancestors; this owner adds no edge.

| Strict ancestor | Retained structure |
| --- | --- |
| `OwnedRings` | Associative unital ring. |
| `OwnedSemirings` | Unital multiplication, commutative addition and distributivity. |
| `OwnedRngs` | Associative multiplication and additive inverses. |
| `Monoids` | Associative unital multiplication. |
| `Semigroups` | Associative multiplication. |
| `Magmas.Unital` | Multiplication and its identity. |
| `Magmas` | Multiplication. |
| `AdditiveGroups.AdditiveCommutative` | Additive abelian group. |
| `AdditiveGroups` | Additive group. |
| `AdditiveMonoids` | Associative addition and zero. |
| `AdditiveSemigroups` | Associative addition. |
| `AdditiveMagmas.AdditiveCommutative` | Commutative addition. |
| `AdditiveMagmas` | Addition. |
| `Sets` | Underlying set. |
| `Objects` | Owned object. |

Generated axiom intersections and implementation wrappers create no
additional authored identity. Nontrivial, commutative rings, Division,
Fields, Local, Complete, Noetherian, finite sets and scalar algebras are
not uniform ancestors. A commutative witness cannot establish a commutative
edge; descendant implications do not propagate upward.

**Actual fixed arrows.** The owned axiom base carries CategoryPacketMethods,
where an object property adds no new arrows. Fixed-endpoint selection walks
the actual supercategories, retains literal endpoints and reuses their
unique inherited fixed Mor. OwnedRings selects RingMorCategoryConstruction,
whose fixed category is RingMor and whose actual element provider is
RingMorphism. Its semiring, rng, multiplicative, additive and set providers
remain in the existing packet. This owner declares no competing arrow
provider. These are all unital ring maps between the admitted objects.
The map `ZZ -> GF(2)` is a true noninjective specimen: both endpoints
satisfy the zero-product axiom, but 2 maps to zero. The existing RingMor
elementwise ingress represents that map through the target's conversion
from owned integers, keeping the exact retained parents.

The existing identity requires equal literal endpoints and retains the
elementwise identity with its datum. Existing RingMorphism composition
checks the intermediate endpoint and composes the element functions on
the retained source and target. Endpoint refinements do not silently
replace these arrows with algebra arrows. This pass introduces no unit,
inverse, kernel or injectivity computation.

**True closure assertions and separators.** The integer witness is admitted
by the native principal-domain placement, which reaches this parent.
The independent GF(2) constructor reaches it through Fields and Division's
explicit NoZeroDivisors edge. The zero ring satisfies the definition while
failing Nontrivial; no zero-ring recognizer was added by this pass. In
`ZZ/6`, the nonzero classes of 2 and 3 multiply to zero, so the property
cannot move to all rings. The nonunit 2 in ZZ prevents promotion of the
stronger Division unit theorem to this owner. No equality is forced to a
Boolean, no unknown proposition is decided, and no finite data or division
algorithm is selected. Identity and composition preserve the actual ring
contracts.

**Independent descendant closure.** The later domain bank closes
`placement-owner-ownedrings-nozerodivisors-commutative` on its own entire
inventory and adds and closes both authored existing-meet providers. Its
complete record reconciles the nontriviality convention, common domain
decision and fraction-field consumers. Named computation limits remain
inside that existing domain work and T; no prerequisite was created.

Evidence is the complete own declaration and nested boundary; the source
inventory and raw bases; the complete relevant semiring/rng and
magma/additive ancestry; Sets' Objects edge; the owned category-witness and
axiom propagation contracts; the fixed-Mor selector; and the actual
RingMor/RingMorphism endpoint, identity, composition and native-constructor
definitions already read for the adjacent passes. This closes this
owner's introductions and placement, without claiming a whole pass at
any ancestor or separately tracked descendant. M1 verification is limited
to a focused diff and post-commit stdlib AST of the changed Python file.
Runtime computation assertions remain under T; no Sage, project import,
runtime, notebook, test or generated-document build belongs to this bank.

### Whole-category placement: `OwnedRings.Nontrivial` (2026-10-11; source pass closed)

**Closed independent owner pass: `placement-owner-ownedrings-nontrivial`.** The complete two-introduction category body, actual ancestor definitions and delivered Mor are source-reviewed. The sole companion adds truthful construction data for the existing integer witness. It authors no category and changes no category-superclass implication, leaving 631 owner identities.

#### Complete inventory and disposition

The owner states `1 != 0` in a unital ring, equivalently that its underlying set has more than one element. Its entire declaration has two introductions:

| Introduction | Disposition |
| --- | --- |
| `_repr_object_names()` | Retain “nontrivial rings”, matching the stated axiom. |
| `an_object()` | Retain the literal owned ZZ witness, whose distinct zero and one establish the axiom. Repair its existing constructor placement as described below. |

There are no ParentMethods, ElementMethods, extra-supercategory edges, Mor declarations, constructors or nested owners in this body. The `Nontrivial()` selector belongs to OwnedRings.SubcategoryMethods and uses the existing registered axiom; it is not another introduction here. Neither display nor witness needs promotion. No new public operation or graph edge is proposed.

#### Necessary witness repair

Before this repair, the exact SageZZ constructor recorded PID, Noetherian, ordered, countably infinite and chosen integral-basis order placements. Those authored paths did not include Nontrivial: the inspected NoZeroDivisors, PrincipalIdeals and Ordered declarations supply no such edge; OwnedOrders adds a finitely generated ZZ-algebra and the existing domain/Noetherian intersection; OrdersWithChosenIntegralBasis adds that order and its finite free module. The later native ring/algebra/module joins do not add this axiom either. Mathematical nontriviality alone therefore does not make the selected ZZ witness an admitted object of this owner.

The source repair records `OwnedRings().Nontrivial()` in the existing SageZZ placement tuple, justified by the constructor's actual distinct zero and one. The owner body and literal witness stay unchanged. This uses selected construction data rather than introducing a general inequality recognizer or changing the convention at the pending Domain or Ordered owners.

#### Full strict authored up-set: 15 owners

| Authored ancestor | Retained structure |
| --- | --- |
| `OwnedRings` | Associative unital ring. |
| `OwnedSemirings` | Unital multiplication, commutative addition and distributivity. |
| `OwnedRngs` | Associative multiplication and additive inverses. |
| `Monoids` | Associative unital multiplication. |
| `Semigroups` | Associative multiplication. |
| `Magmas.Unital` | Multiplication and identity. |
| `Magmas` | Multiplication. |
| `AdditiveGroups.AdditiveCommutative` | Additive abelian group. |
| `AdditiveGroups` | Additive group. |
| `AdditiveMonoids` | Associative addition and zero. |
| `AdditiveSemigroups` | Associative addition. |
| `AdditiveMagmas.AdditiveCommutative` | Commutative addition. |
| `AdditiveMagmas` | Addition. |
| `Sets` | Underlying set. |
| `Objects` | Owned object. |

CategoryWithAxiom retains OwnedRings and its semantic ancestors. Rings declares Semirings and Rngs. Semirings reaches Monoids and additively commutative AdditiveMonoids; Rngs reaches Semigroups and additively commutative AdditiveGroups. The multiplicative spine reaches Magmas and Magmas.Unital; the additive spine reaches AdditiveMagmas and its authored commutative refinement. Both reach Sets, whose sole mathematical root is Objects. Generated axiom intersections and framework wrappers are not extra authored owners.

There is no uniform commutative, domain, division, Local, Complete, finite, ordered or coefficient-algebra ancestor. The integer witness's further structures do not propagate to the category. A nontrivial matrix ring need not be commutative; `Zmod(6)` has nonzero zero divisors; ZZ is infinite and its nonzero element 2 is not invertible. No promotion to a weaker ancestor is needed or claimed.

#### Actual inherited Mor

This property changes objects and adds no arrow condition. CategoryWithAxiom carries CategoryPacketMethods; its ordinary endpoint hook retains each literal ring. `_MorCategoryOf.Of` checks endpoint placement, follows the declared superclass Mor families, and reuses the unique compatible fixed Mor literally. OwnedRings declares RingMorCategoryConstruction, whose fixed class is RingMor. Its actual ElementMethods provider is RingMorphism; `_generated_arrow_type` also carries the inherited semiring, rng, monoid, additive and set providers. The category-level request therefore retains ordinary unital ring maps, even when a concrete endpoint also has an algebra or order Mor interface.

The existing ring identity requires identical endpoints and retains its identity datum. Existing composition checks the actual middle endpoint and returns the corresponding ring composite. No injectivity, surjectivity, coefficient-linearity or reflection of nonzero elements is added: the reduction map ZZ to Zmod(6) is a valid unital ring arrow with nonzero kernel. Both endpoints are nontrivial. A zero function between nontrivial rings fails the unital ring law; Nontrivial does not add a separate runtime law checker to the inherited declaration-based arrow constructor.

#### True closure assertions, unexecuted

- After the focused constructor repair, `OwnedRings().Nontrivial().an_object()` is the existing literal owned ZZ and is admitted by Nontrivial and all 15 strict ancestors. Its zero and one remain distinct.
- Existing `Zmod(6)` construction is admitted directly through its retained modulus being at least 2. It remains a ring with zero divisors and does not become a field through this axiom.
- The zero ring `Zmod(1)` does not receive the native Nontrivial placement; its equality `0 = 1` contradicts the owner contract. No smaller cardinality computation is needed by this repair.
- For admitted literal rings R and S, the category's fixed Mor is the existing OwnedRings fixed Mor on R and S. Its identity, underlying maps and ring-arrow providers are retained without a new parent or restricted arrow predicate.
- The actual reduction ZZ to Zmod(6) remains eligible; Nontrivial does not turn it into an embedding or move field-specific inverse theorems upward.
- No arbitrary ring's undecided zero/one equality is coerced. This owner adds no recognition or element algorithm; inherited optional and required computation frontiers remain at their existing owners. Their whole-owner passes are not declared closed by this ancestry review.

#### Exact source evidence and retained boundaries

The complete Nontrivial body, actual ring/Mor/arrow definitions, native integer and modular-ring placement cases, final ring join and subsequent algebra/module construction were read in `src/dzack_research/preamble/categories/rings/ring_foundation.py`. The PID, NoZeroDivisors, Ordered and OwnedOrders paths were traced there, with the chosen integral-basis order edge in `categories/rings/number_fields.py`. They explain why the existing integer witness needed its explicit axiom datum rather than an assumed implication. The actual semiring, magma, additive, set and Objects definitions and owned category/axiom/Mor sources supply the full strict ancestry and literal endpoint proof.

The true ZZ, Zmod(6), zero-ring and reduction-map assertions stay under T. No arbitrary zero/one equality is decided or Boolean-coerced, and no inverse, field, order or general-domain recognition algorithm is added. Inherited optional or required computation limits retain their existing owners. No project import, runtime test, generated graph or new prerequisite is part of this M1 source closure.

### Whole-category placement: `OwnedRings.Division.Commutative` (2026-10-11; source pass closed)

**Closed independent owner pass: `placement-owner-ownedrings-division-commutative`.** The complete Fields provider, its actual ancestor definitions, selected local data, concrete Mor delivery and all affected callers have been reviewed. The source repair is independently checked and closes this owner without adding a provider or changing the then-current 631-owner inventory. Division and nested Prime remain separately recorded completed passes.

#### Disposition and focused repair

Fields are nontrivial commutative rings in which every nonzero element is a unit. The owner introduces twelve methods and no arrow provider. Its field constructions and theorem supplier stay here. Its three public residue operations belong to the existing common Local owner and now inherit that implementation.

The common Local getter first retains the actual `_selected_local_ring_construction()` result. Only when that result is `None` and the object already belongs to Fields does it supply the canonical field datum. The existing record retains residue field `self`, an explicit `OwnedRings().Mor(self, self).identity()`, and an independent lazy factory for the owned zero ideal. The getter caches the fixed record, while the record's existing accessors independently cache their own results. Reading the residue field or map therefore does not request an ideal computation.

This precedence matters for a field presented as a selected prime localization or another local construction. Such a source may already retain an actual residue-field model and map with that model as codomain. Those exact objects must survive. The new behavior is not the assertion that every field's public residue field is literally itself: literal self and identity are the canonical default only when there is no selected local datum. A supplied record with an unavailable residue map retains the common Local map assertion; it is not silently replaced by an identity with a different codomain.

The remaining behavioral correction makes `exact_embeddings` call `OwnedRings().Mor(self, codomain).embeddings()`. Extra coefficient-algebra structure on either endpoint must not narrow the field's unital ring maps or select a generator-label algebra callback. The existing RingMor enumeration and its owned finite ordered result are reused unchanged. The first-embedding empty check now requires a proved equality with zero. Other changes state the actual finite-generator, embedding-enumeration and algebraic-closure computation frontiers without narrowing the mathematical category.

#### Complete original introduction inventory: 12 methods

| Introduction | Mathematical contract, owner and disposition |
| --- | --- |
| `_repr_object_names` | Retains the display name `fields`; the class description now states nontriviality explicitly. |
| `an_object` | Retains the existing F_2 constructor as an actual field witness. Its finiteness is not a uniform field axiom. |
| `extra_super_categories` | Retains principal ideals, Artinian rings and complete local rings. A field has exactly the ideals zero and itself, and is complete for its zero maximal ideal. |
| `SubcategoryMethods.Prime` | Retains the existing no-proper-subfield refinement selector. The nested Prime provider is a separate owner and is not part of this body inventory. |
| `_krull_dimension_decision` | Retains the field theorem that the only prime ideal is zero, hence dimension zero as an owned ZZ value. The public dimension definition already belongs to the common commutative-ring owner; this is a specific exact theorem supplier, not a duplicate public definition. |
| `field_generators` | Retains the field construction site and existing selected finite/number-field generator computation. The returned generators are actual elements of this field, sufficient to determine its outgoing unital field maps. The current selected computation includes relative number-field levels. No finite generating family is asserted for every field. |
| `exact_embeddings` | Retains the field construction site, using the actual ring-Mor owner for field embeddings. Repairs its Mor selection while retaining the selected finite ordered enumeration and literal endpoints. |
| `first_exact_embedding` | Retains selection from that supplied finite order. An empty enumeration raises the existing ValueError; there is no canonical first embedding determined by two abstract fields alone. |
| `maximal_ideal` | Removes the field public override and inherits common Local's actual selected maximal ideal. The canonical field default supplies the zero ideal lazily. |
| `residue_field` | Removes the field public override and inherits common Local's selected quotient field. An existing selected model is retained; absent selected data the result is literal `self`. |
| `residue_map` | Removes the field public override and inherits common Local's selected unital quotient arrow. The canonical field default has literal endpoints `self` to `self` and is the actual RingMor identity. |
| `absolute_galois_group` | Retains the field construction site delegating to the existing profinite-group owner. That owner retains the chosen algebraic closure and base embedding. No parallel group realization, extra field axiom or new closure algorithm is introduced. |

After removal there are nine declarations at this provider. The one common Local getter change uses its existing record and existing protected supplier. It adds no category, hook, registration family or independently selectable local structure.

The three removed operations use only the hypothesis of a commutative local ring. A selected localization source, a field, a coefficient algebra, a basis and an algorithmic field model are unnecessary for their definitions. None of the strict ancestors of Local uniformly singles out a unique maximal ideal, so Local remains their weakest available owner. The other field operations retain their actual field meaning: the selected field-generating family and field embeddings are not substitutions for a general ring's chosen algebra generators or for all injective maps of underlying sets; the absolute Galois construction is the field construction with its existing retained closure data.

#### Complete strict authored up-set: 29 owners

The original bank reviewed 27 strict authored ancestors. The domain bank adds and completely reviews two providers on existing Nontrivial meets, bringing the current up-set to 29. These are authored mathematical providers, not a runtime C3 linearization. Generated axiom intersections and framework category bases are not additional owners.

| Strict authored ancestor | Structure retained or forgotten |
| --- | --- |
| `OwnedRings.Division` | Every nonzero element is invertible; commutativity is forgotten. |
| `OwnedRings.NoZeroDivisors.Commutative.Nontrivial` | The exact integral-domain meet, with its complete new-provider fraction-construction pass. |
| `OwnedRings.NoZeroDivisors.Nontrivial` | The nontrivial zero-product meet and its nonzero submonoid. |
| `OwnedRings.NoZeroDivisors.Commutative` | Commutative zero-product rings, allowing the zero ring. |
| `OwnedRings.NoZeroDivisors` | A product can vanish only when a factor vanishes. |
| `OwnedRings.Commutative.PrincipalIdeals` | All field ideals are principal. |
| `OwnedRings.Artinian` | The two-ideal lattice has descending chain condition. |
| `OwnedRings.Noetherian` | The same lattice has ascending chain condition; reached from both principal ideals and Artinian. |
| `OwnedRings.Commutative.Local` | The unique proper maximal ideal is zero. |
| `OwnedRings.Commutative.Local.Complete` | The field is complete for that zero maximal ideal. |
| `OwnedAdicallyCompleteRings` | The existing complete-local edge supplies the canonical zero defining ideal when no independent chosen datum takes precedence. |
| `OwnedRings.Commutative` | Commutative unital associative multiplication and distributivity. |
| `OwnedRings.Nontrivial` | The consequence 1 differs from 0. |
| `OwnedRings` | Unital associative ring structure. |
| `OwnedSemirings` | Additive commutative monoid and multiplicative monoid with distributivity. |
| `OwnedRngs` | Additive abelian group and associative distributive multiplication. |
| `Monoids` | Associative multiplication with identity. |
| `Semigroups` | Associative multiplication. |
| `Magmas.Unital` | Multiplication with a two-sided identity. |
| `Magmas.Commutative` | Commutative multiplication. |
| `Magmas` | Binary multiplication. |
| `AdditiveGroups.AdditiveCommutative` | Abelian addition. |
| `AdditiveGroups` | Addition with inverses. |
| `AdditiveMonoids` | Associative addition with identity. |
| `AdditiveSemigroups` | Associative addition. |
| `AdditiveMagmas.AdditiveCommutative` | Commutative addition. |
| `AdditiveMagmas` | Binary addition. |
| `Sets` | The underlying set. |
| `Objects` | The authored mathematical root. |

Division supplies NoZeroDivisors and Nontrivial; the existing axiom propagation reaches the authored commutative zero-product refinement and both now-authored Nontrivial meets. Fields' explicit edges supply PrincipalIdeals, Artinian and Complete Local. Complete Local reaches the common chosen-adic owner. The two ring supercategories supply the multiplicative and additive branches, and Sets reaches Objects. The patch changes none of these edges.

A field need not be finite, ordered, a number field, finitely generated over its prime field, algebraically closed, or supplied with an enumerable family of embeddings into every other field. None of those is a uniform ancestor. Additional coefficient-algebra and selected localization or quotient placements belong to particular constructions. They do not redefine the ordinary field arrows.

#### Actual fixed Mor and arrow providers

Fields has no `_MorCategory`, `MorphismMethods`, element provider, arrow constructor or comparison shell. `CategoryWithAxiom` inherits the owned packet protocol. At fixed admitted endpoints, `_MorCategoryOf.Of` traverses the declared semantic supercategories, deduplicates their fixed Mors by identity and reuses the compatible inherited ring family. OwnedRings supplies `RingMorCategoryConstruction`, whose fixed class is RingMor. The generated arrow type follows that actual fixed-Mor graph and includes RingMorphism together with its inherited semiring, rng, additive, multiplicative and set providers.

Consequently Fields is the full property refinement with ordinary unital ring maps and literal endpoints. A unital map between nonzero fields is injective: its kernel is an ideal, and cannot be the whole source because it preserves 1. This is why its ordinary ring maps are the field embeddings. The category does not impose a chosen coefficient action, a local-map condition, continuity, or an order-preservation condition.

The repaired exact enumeration explicitly requests that RingMor. Its existing method verifies both endpoints are fields, calls the selected engine embedding enumeration and reconstructs each returned arrow through the same fixed `self` Mor. Thus an enumerated arrow has exactly the original owned domain and codomain, rather than the native engine fields as public endpoints. The finite ordered family and its order are retained from the supplied enumeration. Any additional AlgebraMor is a stronger condition and is not the implicit owner of this field operation.

No RingMor algorithm or equality rule is changed here. The separately banked Prime uniqueness companion and NumberFields' distinct real-embedding operation are not certified as new work by this pass.

#### Local datum, laziness and actual supplier callers

The common `_selected_local_ring_construction` default returns None. Native `_OwnedRingParent` initializes its selected slot before exposure and its supplier returns that exact slot. The prime-localization supplier already caches its actual source-defined maximal ideal, residue quotient field and map. The installation helper asks the protected supplier directly and preserves or rejects an existing fixed datum; it does not call the public getter. The common Local field predicate also asks the protected supplier directly, so the new public getter does not create a predicate cycle.

The added canonical fallback therefore neither competes with a concrete selected supplier nor installs a second independent local choice. No eager zero-ideal construction occurs. Existing selected datum identity is preserved on every access; for the canonical case, the getter and the record cache give one retained record and one retained identity arrow. As in the existing constructor contract, selected structure is fixed before the object is exposed; this patch does not add a mutation protocol for replacing that structure later.

The Complete defining-ideal supplier still obtains the actual maximal ideal through the common public owner. A field's canonical zero ideal has its literal field as ambient ring. Explicit adic target data retain the precedence already established by the common Adic pass. No completion algorithm or chosen-topology convention is changed.

#### True source closure assertions, unexecuted

1. The existing F_2 witness belongs to Fields and all 29 authored ancestors. Its dimension supplier returns owned integer zero. The zero ring is excluded by the inherited Nontrivial edge. QQ is an infinite field, so the witness does not supply universal finite placement.
2. For native owned QQ or GF(p) with no selected local datum, `local_ring_construction()` returns the cached canonical record. `residue_field()` is literally that field, and `residue_map()` is an actual `OwnedRings().Mor(K, K)` identity with those literal endpoints. Reading either does not evaluate the zero-ideal factory.
3. On that canonical path, `maximal_ideal()` is the existing owned zero ideal with `ideal.ring() is K`. Its construction is requested only by the ideal accessor. Repeated access uses the same selected record and its cached datum.
4. If an actual Fields object already supplies a record D, `local_ring_construction() is D`; its selected maximal ideal, residue-field model and quotient map survive unchanged. In particular a source-selected field realization is not forced to replace its retained residue model by itself. A supplied record's missing map retains the named common Local computation boundary.
5. The required new-home specimen outside Fields is R=ZZ localized at (3). Its existing prime-local datum supplies the owned ideal (3)R, residue field kappa=Frac(ZZ/(3)), and actual quotient map rho:R to kappa. These are the same three inherited common Local operations, with literal ambient/source/target objects. The maximal ideal is nonzero, contains 3 and excludes 1; R is not a field. For a/b with b outside (3), rho is the residue of a times the inverse of the residue of b.
6. For the existing finite-field pair F_4 to F_16, the selected embedding enumeration has two maps; the reverse direction has none. For the existing Gaussian-to-eighth-root field example the enumeration has two maps, while the recorded incompatible quadratic example has none. Every returned map is in the explicit ring Mor on the literal input fields. The first selection uses the retained order and raises the existing ValueError for an empty family.
7. For a represented number-field tower, the existing generator computation retains generators from the top and base levels and raises them into the actual field. QQ's supplied unit generator and finite-field generators retain their existing values and order. The method does not infer that an arbitrary field has a finite generating family merely from Fields membership.
8. The field's absolute Galois construction continues to return the existing profinite owner retaining the actual field, selected closure and chosen embedding. The zero-argument canonical cache and explicit-choice constructor remain unchanged. Unavailable closure or exact-embedding computations remain unavailable; the mathematical group is not restricted to the represented finite/number-field cases.
9. No unknown comparison is converted to a negative result by a new field body. The only changed comparison is the sufficient exact-empty-enumeration guard. Local datum availability uses `is None`, and field eligibility uses established category membership rather than a computational field predicate. The optional common Local field predicate is unchanged.

These are source and mathematical closure obligations, not executed tests or runtime graph claims. Items 6 and 7 retain the repository's existing assertion specimens and supplied algorithms. No claim of a universal field-embedding enumerator, algebraic-closure solver or arbitrary ideal algorithm is added.

#### Actual caller reconciliation and remaining computation limits

A complete current occurrence search covered the existing field-generator, embedding and absolute-Galois entries in src, tests and docs. The return types and calling conventions used there are preserved. No required operation is changed into an optional None result, and no caller is required to migrate to a new API.

- `field_generators` is used by ring-map equality/restriction signatures, the existing profinite Galois construction and quotient machinery, and finite/number-field assertion sources. They still receive the same finite ordered family of actual source elements in the represented cases. The helper's former error claimed that an unrecognized field was mathematically neither finite nor a number field; the new error states only that the selected computation is unavailable.
- `exact_embeddings` and `first_exact_embedding` occur in the Galois construction, exact field-map assertions, profinite owned-collection assertions, group-module constructions and selected extension/closure compatibility. Their unchanged ordered-family and arrow interfaces remain available, now with explicit ordinary RingMor ownership. The complete existing RingMor enumeration body was read; no new finite or enumeration axiom is inferred.
- `absolute_galois_group` is used by the existing profinite and Galois assertion sources. Both complete implementation files were read, including the canonical/explicit-choice constructors, retained field/closure/embedding accessors and finite-field specialization. This pass changes only the Fields construction-site documentation; it does not reopen those owners' independent arithmetic or finite-stage algorithms.
- Local accessor consumers retain the common record interface. Canonical no-selected-datum fields preserve literal self and identity; already selected field quotients now preserve their actual models and endpoints. Native and prime-local suppliers, installation, the common field predicate, and the Complete ideal supplier were read specifically for this precedence and recursion check.

The current same-owner computation limits are the selected finite/number-field generator algorithm, the finite native exact-embedding enumeration, the availability of an algebraic-closure/embedding realization, and any unavailable selected ideal or residue map computation. Infinite embedding sets need a different supplied representation; this patch does not turn them into empty finite sets. The NumberFields real-embedding adapter is a distinct existing operation and is left intact. These limits stay in the existing owner record; no prerequisite, new category or new registry is filed.

#### Source evidence and phase boundary

The full Fields declaration, all ring refinements, LocalRingConstruction and its installation, common/native protected suppliers, Complete ideal supplier, selected native placements, field generators and RingMor embeddings were read in `src/dzack_research/preamble/categories/rings/ring_foundation.py`. The selected prime-local supplier and local constructions were read in `categories/rings/commutative_algebra.py`. The actual number-field towers and separate real-embedding operation are in `categories/rings/number_fields.py`; the literal scalar-algebra maps and stronger Mor providers are in `categories/algebras/algebras.py`. Both complete existing Galois files, `categories/group/profinite/absolute_galois_group.py` and `categories/group/profinite/absolute_galois_groups.py`, were read with the full source/test/doc occurrence ledger. Abbreviated `categories/` paths here are relative to `src/dzack_research/preamble/`.

The actual category/axiom, join, fixed-Mor and generated-arrow sources, together with the ring/semiring/magma/set/Objects definitions, establish the authored ancestry and inherited arrow providers. The existing installation helper has no current src/tests caller beyond its import; the supplied local data remain fixed at construction, and the getter does not install or replace a datum. Independent source review confirms the selected-data precedence, endpoint preservation and separate lazy ideal computation. The earlier Local, Complete and common Adic field examples below are reconciled with this consolidation.

The mathematical specimens and required computation assertions stay under T. No project import, Sage execution, runtime test, generated-document build, new category or prerequisite is part of this M1 source closure.

### Whole-category placement: `OwnedRings.Division` (2026-10-11; source pass closed)

**Closed independent owner pass: `placement-owner-ownedrings-division`.** The whole four-introduction declaration is source-reviewed and repaired. The nested Fields and Prime declarations keep their distinct inventory identities; their additional hypotheses do not become Division ancestors.

A division ring is nontrivial and every nonzero element has a two-sided
multiplicative inverse. The patch makes nontriviality explicit in the class
doc and expresses the unit theorem using owned logical negation. There are
exactly four introduced methods and no new public operation or algorithm.

| Introduction | Complete disposition |
| --- | --- |
| `_repr_object_names()` | Retain the category's division-ring name. |
| `an_object()` | Retain the owned `GF(2)` witness. A commutative example is valid in this broader category and does not impose commutativity on every object. |
| `extra_super_categories()` | Retain exactly NoZeroDivisors and Nontrivial. Clarify both consequences in its doc. If `xy=0` and `x` is nonzero, multiplication by its inverse gives `y=0`; nontriviality is part of the division-ring convention. |
| `ElementMethods._unit_decision()` | Retain this specialized supplier at Division. Replace `self != zero` with `negation(self == zero)`, preserving an undecided owned equality through the existing monoid-unit contract. |

No promotion is justified. In `ZZ`, the nonzero element `2` is not a unit,
although the ring is nontrivial and has no zero divisors. Thus even the meet
of those two weaker ring properties does not supply this formula. More
general ancestors forget still more, and monoids alone do not supply zero.
The public `is_unit()` operation correctly remains at Monoids; Division
supplies its theorem through that owner's protected hook. Nontriviality
matters: zero is a unit in the zero ring, which is excluded from Division.

#### Entire strict authored up-set: 18 owners

The original bank reviewed 17 authored ancestors. The domain bank additionally
authors and completely reviews `OwnedRings.NoZeroDivisors.Nontrivial` on the
existing meet, bringing the current up-set to 18. CategoryWithAxiom retains
OwnedRings and its authored ancestors; the two explicit edges add
NoZeroDivisors and Nontrivial. Generated axiom intersections and implementation
wrappers are not extra owner identities.

| Authored ancestor | Retained structure |
| --- | --- |
| `OwnedRings.NoZeroDivisors.Nontrivial` | Distinct zero and one with the zero-product axiom; its complete new-provider pass supplies the nonzero submonoid. |
| `OwnedRings.NoZeroDivisors` | Products vanish only when a factor vanishes. |
| `OwnedRings.Nontrivial` | `1 != 0`. |
| `OwnedRings` | Associative unital ring. |
| `OwnedSemirings` | Unital multiplication, commutative addition, distributivity. |
| `OwnedRngs` | Associative multiplication and additive inverses. |
| `Monoids` | Associative unital multiplication. |
| `Semigroups` | Associative multiplication. |
| `Magmas.Unital` | Multiplication and identity. |
| `Magmas` | Multiplication. |
| `AdditiveGroups.AdditiveCommutative` | Additive abelian group. |
| `AdditiveGroups` | Additive group. |
| `AdditiveMonoids` | Associative addition and zero. |
| `AdditiveSemigroups` | Associative addition. |
| `AdditiveMagmas.AdditiveCommutative` | Commutative addition. |
| `AdditiveMagmas` | Addition. |
| `Sets` | Underlying set. |
| `Objects` | Owned object. |

There is no authored commutative-ring, field, finite-set, coefficient-algebra,
Local, or Complete ancestor here. The multiplicative set including zero is
not a group. Nested `Division.Commutative` and its `Prime` refinement are
separately tracked descendants; their extra edges do not propagate upward.

#### Actual Mor and proposition contracts

Division introduces neither a Mor override nor an arrow provider.
OwnedRings declares `RingMorCategoryConstruction`; that family's fixed
category is `RingMor`, whose actual ElementMethods provider is
`RingMorphism`. The packet selector follows the declared supercategories on
the same literal endpoints and reuses this inherited fixed Mor. Its generated
arrow type retains RingMorphism and the underlying semiring, rng, monoid,
additive, and set providers. The identity and composition are the existing
ring constructions, with exact endpoint checks; an endpoint's additional
algebra placement does not replace this category-level ring Mor.

These are unital ring maps. Such maps automatically preserve inverses of
nonzero elements: applying a map to both inverse equations gives the inverse
equations in the codomain. No new inverse-preservation test or specialized
arrow representation is needed.

`Monoids.ElementMethods._unit_decision` permits a Boolean or owned proposition;
its sole caller `is_unit()` returns that value unchanged. The Division
supplier obeys this inherited contract and adds no protected caller.
For the owned zero-equality proposition `P`, `negation(P)` returns its Boolean
complement when decided and a Negation object otherwise. It never calls
`bool(P)`. This removes dependence on a separately implemented `__ne__`, whose
inherited implementation can negate equality using Python Boolean coercion.
Computing an actual inverse remains the separate monoid inverse algorithm
and its existing availability boundary.

#### Source closure assertions and evidence

These are source assertions, not execution results:

- The existing owned `GF(2)` witness remains in Division and its two declared
  consequences. Its native equality supplies unit status False for zero and
  True for one.
- Whenever `a == D.zero()` returns True, the supplier returns False; when it
  returns False, the supplier returns True.
- If that equality returns an Atomic proposition, the supplier and public
  monoid `is_unit()` retain its Negation without Boolean coercion or an
  invented inverse computation. Concrete realization overrides keep their
  existing contracts and algorithms.
- For admitted endpoints `D,E`, the category's fixed Mor remains the existing
  ring Mor on exactly `D,E`, preserving identity, addition, multiplication,
  and composition. No field, scalar, finiteness, or commutativity premise is
  added.
- The zero ring is excluded; the `ZZ(2)` counterexample prevents promotion to
  either weaker ring owner or their meet.

#### Source evidence and retained computation frontier

The complete live Division declaration and adjacent ring refinements were read in `src/dzack_research/preamble/categories/rings/ring_foundation.py`, together with its actual inherited RingMor/RingMorphism definitions. The actual semiring, magma, set and object ancestor definitions, the logic owner's negation implementation, and the existing category-with-axiom, Mor packet and generated-arrow sources supply the inheritance and proposition proof. The source inventory records Division and its nested descendants separately. No source inference here relies on an executed MRO or the commutativity of the selected GF(2) witness.

Public monoid unit status retains a Boolean or owned proposition. Computing an inverse is a separate existing operation with its own availability boundary; this pass does not manufacture inverse data from a nonzero proposition. Concrete realization overrides keep their existing algorithms. These limits remain within this node and T. No project import, runtime test, new owner provider or prerequisite is part of this M1 closure.

### Whole-category placement: `OwnedRings.Division.Commutative.Prime` (2026-10-11; source pass closed)

**Closed independent owner pass: `placement-owner-ownedrings-division-commutative-prime`.** The authored declaration supplies this canonical TODO identity; the source graph's equivalent axiom-order vertex is `OwnedRings.Commutative.Division.Prime`. Ordinary Fields was independently closed in its later bank; RingMor retains its own pending pass. This original bank added no category provider and left the then-current 631-owner inventory unchanged.

#### Disposition and bounded repair

The refinement means a field with no proper subfield. Such a field is the copy generated by 1: it is QQ in characteristic zero or F_p in positive prime characteristic. No broader field algorithm is needed.

The existing `PrimeField(characteristic)` entries incorrectly delegated to `GF(characteristic)`, interpreting the argument as finite-field order. Thus 0 did not select QQ and 4 selected GF(4), which has proper subfield GF(2). The source repair puts construction at the existing Prime category and makes the ring-foundation entry a thin delegate. The witness now uses the same category entry. Zero returns the literal owned QQ; a positive prime p returns the existing GF(p); negative and composite characteristics, including 1, are rejected.

The complete `src/dzack_research/preamble/rings/__init__.py` public surface contains a second live wrapper. That wrapper now also returns `PrimeFields()(characteristic)`, using the existing import. This is the public entry retained by `ring_constructor_surface` and `__all__`, so session exports now reach the same category-owned construction. Both wrappers delegate; neither owns a second characteristic algorithm. Their export wiring remains unchanged.

The constructor reuses `_engine_numeral` for the existing Python/owned/preparsed numeral ingress, raises the result into the actual owned ZZ, and calls its existing zero, order and primality operations. No new primality algorithm, category, capability, record or field realization is introduced. An unresolved primality result cannot admit an object.

A narrow inherited RingMor companion makes PrimeFields uniqueness the first match case after literal endpoint checks. It applies to the actual prime-field domain before quotient/localization source transport or computation-engine access, including intersections with those presentation categories. The separate SageZZ case remains in its original position, and nonprime finite fields retain their generator comparison. This removes an unnecessary source/model dependency without closing the whole RingMor owner.

#### Complete introduction inventory

| Introduction | Disposition |
| --- | --- |
| `_repr_object_names` | Retains the display name “prime fields”. |
| `an_object` | Constructs F_2 through this category's characteristic entry. |
| `_call_` (repair) | Owns construction of the prime field from characteristic 0 or a positive prime. |

The original owner had the first two methods only. It declares no ParentMethods, ElementMethods, extra-supercategory, Mor override or further child. The `Prime()` refinement selector belongs to Fields; the `PrimeFields()` spelling remains an alias of this exact category. No mathematical operation is promoted to a strict ancestor. The general finite-field constructor GF remains at its existing home and continues to construct GF(4).

#### Complete strict authored up-set: 30 owners

The original bank reviewed 28 strict authored ancestors. The domain bank adds and completely reviews `OwnedRings.NoZeroDivisors.Nontrivial` and `OwnedRings.NoZeroDivisors.Commutative.Nontrivial`, bringing the current up-set to 30. Their definitions and operations are recorded in the complete domain pass. The original ten ring refinements beyond the previously read common Local ring spine are:

1. `OwnedRings.Division.Commutative`
2. `OwnedRings.Division`
3. `OwnedRings.NoZeroDivisors.Commutative`
4. `OwnedRings.NoZeroDivisors`
5. `OwnedRings.Commutative.PrincipalIdeals`
6. `OwnedRings.Artinian`
7. `OwnedRings.Noetherian`
8. `OwnedRings.Commutative.Local`
9. `OwnedRings.Commutative.Local.Complete`
10. `OwnedAdicallyCompleteRings`

The remaining eighteen are `OwnedRings.Commutative`, `OwnedRings.Nontrivial`, `OwnedRings`, `OwnedSemirings`, `OwnedRngs`, `Monoids`, `Semigroups`, `Magmas.Unital`, `Magmas.Commutative`, `Magmas`, `AdditiveGroups.AdditiveCommutative`, `AdditiveGroups`, `AdditiveMonoids`, `AdditiveSemigroups`, `AdditiveMagmas.AdditiveCommutative`, `AdditiveMagmas`, `Sets`, and `Objects`.

These are source-declared mathematical owners, not an executed MRO. Framework bases and generated axiom intersections are not extra owners. Division supplies NoZeroDivisors and Nontrivial; commutativity propagates to the authored zero-product refinement and both now-authored Nontrivial meets. Fields supplies principal ideals, Artinian and Complete Local. Principal ideals and Artinian each reach Noetherian; Complete Local reaches the chosen adic owner, using the zero maximal ideal for fields. The ring spine supplies both distributive operations, and Sets reaches the actual Objects root. No new graph edge is added.

Finite-set, ordered-ring and number-field placements belong to particular constructor results, not uniformly to this refinement. In particular QQ is infinite, while F_p is finite; positive-characteristic fields are not ordered rings. The review reads Fields as ancestry and does not certify all of its algorithms or declare that owner closed.

#### Actual Mor and endpoint inheritance

Prime adds an object property and no arrow condition. `CategoryWithAxiom` inherits the existing packet protocol. `_MorCategoryOf.Of` checks endpoint placement, follows the semantic supercategories and reuses the unique compatible inherited fixed Mor by identity. Fields explicitly retains ordinary ring arrows. `OwnedRings` supplies `RingMorCategoryConstruction`, whose fixed class is RingMor; `_generated_arrow_type` visits its actual supergraph and includes RingMorphism and the inherited semiring/rng/additive/multiplicative/set providers. Ordinary endpoint forgetting retains the literal fields.

Thus PrimeFields.Mor has the actual inherited unital ring arrows. From a fixed prime field to a fixed ring target there is at most one such map: every arrow fixes 1, hence the generated prime field. The equality helper first checks literal endpoints, then applies this theorem for any actual PrimeFields domain before presentation transport or model access. This also covers a prime field presented as a quotient or localization. Nonprime source domains retain their existing transport branches. There is no extra chosen coefficient map or continuity requirement. A hom-set may be empty; the theorem does not construct a map between incompatible characteristics.

The outside-home separator is GF(4): its identity and Frobenius a↦a² are distinct ring automorphisms. Its existing finite-field construction does not place it in PrimeFields, so the equality helper retains the generator comparison. Uniqueness must not move to all Fields. ZZ is a ring rather than a field and likewise does not enter this constructor's output category.

#### True closure assertions, unexecuted

- `PrimeFields()` is the canonical Prime refinement; its witness is the existing F_2 and belongs to all 30 declared ancestors.
- Both public `PrimeField(0)` wrappers, the existing session-exported entry and `PrimeFields()(0)` return literal owned QQ, including through supported owned/preparsed integer ingress. Characteristic zero is not a request for a finite field of order zero.
- For prime p, both public wrappers and the category entry return the existing GF(p), with characteristic p and PrimeFields placement. The exported characteristic-3 specimen retains F_3; `PrimeFields()(ZZ(5))` and `GF(5)` retain the same existing owned result.
- Inputs -2, 1, 4 and 9 raise the stated invalid-characteristic error through both wrappers and the category entry. An unresolved primality answer cannot become an admission.
- GF(4) remains a valid field outside PrimeFields. Its nontrivial Frobenius remains distinguishable from its identity.
- For an actual prime-field domain and fixed actual ring target, the inherited fixed Mor and ring-arrow providers are retained. Equal-endpoint outgoing arrows use prime-field uniqueness before source transport or model access, including quotient/localization intersections; different literal endpoints are not merged. Nonprime source transports keep their existing computation frontier.
- No uniform finite, ordered or number-field placement is inferred from the F_2 example. Existing required numeral/primality computations retain their ordinary errors; no arbitrary field recognition or embedding algorithm is added.

#### Source evidence and retained computation frontiers

The complete Prime declaration and all relevant ring refinements were read in `src/dzack_research/preamble/categories/rings/ring_foundation.py`, together with the PrimeFields alias, native field placement, owned-integer/primality ingress, QQ/GF constructors, literal endpoint equality helper and actual RingMor provider. The whole-preamble caller search covered `src/dzack_research/preamble` and `tests`. The complete public `preamble/rings/__init__.py` wrapper/export surface and `tests/objects/test_prime_field_f3.sage` were read, and `preamble/all.py` retains the public PrimeField/PrimeFields imports. The real semiring, magma, set and object definitions and category/axiom/Mor machinery supply the full ancestry and arrow proof; the original source inventory fixes the authored identity.

All constructor and equality assertions above are retained under T, without a project import or runtime test in M1. Existing numeral/primality availability and nonprime source-transport computations keep their stated boundaries. The Prime theorem uses only the actual domain property and literal endpoints, and does not construct an arrow in an empty hom-set. No new prerequisite, arbitrary-field recognition procedure or embedding algorithm is added.

### Whole-category placement: `FormalPowerSeriesRings` (2026-10-11; source pass closed)

**Closed independent owner pass: `placement-owner-formalpowerseriesrings`.** The full declaration and all actual ancestors justify this bounded source closure. No public formal-coordinate operation belongs at a weaker existing ancestor. The parameter declaration is corrected to the commutative coefficient rings required by the uniformly declared commutative algebra structure, including zero rings and non-Noetherian rings. The coefficient, label-correspondence and optional-cardinality repairs preserve the actual R-module action and both defining maps.

The coordinated selected-construction repair is banked in `13d391e8f2`: an actual framed symmetric-algebra source supplies retained finite ordered labels on the proved zero-source branch, or on the empty-family zero-ideal branch. An empty-family unit completion over a nonzero base receives no false Formal placement. General unframed sources keep their previous zero/unit paths. Thus the degenerate cases retain their data rather than acquire a new nontriviality or positive-variable hypothesis. Native empty-family parser notation remains unexecuted; the selected empty polynomial-source completion supplies that mathematical entry.

#### Mathematical datum and complete introduction inventory

The coefficient ring is the literal owned commutative ring `R`. The existing
constructor selects an ordered finite family `X`, the polynomial source
`P = R[X]`, its variable ideal `I`, and the completion `A = lim P/I^n`, together
with `lambda: P -> A`. The family consists of formal parameters; finiteness of
`X` does not say that these elements generate `A` as an ordinary algebra.
The constant-series map `c: R -> A` is the actual retained scalar action.

The original declaration contains exactly ten methods, including category
construction methods. The patch adds the parameter-category override and
introduces no new public element operation, Mor family, arrow provider,
nested refinement, comparison record, or series algorithm.

| Introduction | Disposition and owner justification |
| --- | --- |
| `an_object()` | Keep the existing one-variable formal series construction over the category's actual `R`. It is a category witness, not an operation on an arbitrary adically complete ring. |
| `_repr_object_names()` | Keep the name of this particular category. |
| `super_categories()` | Keep the unital commutative `R`-algebra and chosen-adic implications. Neither of them selects formal coordinates by itself. |
| `_call_(*args, **kwargs)` | Keep the established notation parser and the single AdicCompletions construction. It retains the parsed variables and computational precision, then enters through `R[X]` and its variable ideal. There is no parallel completion realization. |
| `formal_parameter_set()` | Keep the chosen family here. No strict ancestor supplies formal variables. An absent datum now gives an informative assertion instead of saying that an object already in the category is not a power-series ring. An empty supplied family remains a valid value. |
| `formal_parameter(label)` | Keep the evaluation of a retained formal label through `lambda`. The selected position now identifies the source's actual algebra label before its generator is passed through the completion map. Native names can differ from those source labels. |
| `power_series_variable()` | Keep the convenience accessor for a supplied family of cardinality one. A several-variable or empty-family object has no unique variable for this no-argument operation. Its exact cardinality request is part of this arity question, not an optional availability probe. |
| `_cardinality_decision()` | Keep this as a supplier for the existing Sets cardinality owner. The formula uses the coefficient cardinal and parameter cardinal supplied by the same retained data. The finite-parameter guard prevents a supplied infinite or unevaluated cardinal from being forced through `finite_value()`. |
| `ElementMethods.coefficient(degree)` | Keep scalar coefficient extraction here because it depends on the formal coordinates. The repair accepts exact integral exponents, uses an exponent tuple for several variables, and returns an element of the literal coefficient ring. |
| `ElementMethods.__getitem__(degree)` | Keep the syntax delegation to that one coefficient operation. It introduces no second implementation. |
| Added `parameter_category()` | State `OwnedRings().Commutative()` at the actual parameterized owner. A noncommutative ring cannot supply the declared commutative constant-series algebra with its faithful coefficient map. |

The category wrapper `OwnedCategoryOverBaseRing` normalizes an ordinary native
ring to its owned ring and then retains that parameter. Its bootstrap branch
preserves the actual under-construction owned parent. This patch does not
replace the parameter by an abstractly isomorphic ring, a residue field, the
polynomial source, or a native coefficient parent.

#### Complete strict authored up-set: 26 owners

The following is the authored mathematical ancestry with the existing axiom
propagation. It is not an executed Python MRO. Generated intersections of
axioms are not extra authored owner identities. Every parameterized algebra
or fixed module ancestor below retains the same `R`.

| Strict authored ancestor | Structure and parameter retained |
| --- | --- |
| `Algebras.Associative.Unital.Commutative(R)` | Commutative associative unital multiplication on the actual `R`-module. |
| `Algebras.Associative.Unital(R)` | Associative unital `R`-algebra; its declared ring implication supplies the ring branch. |
| `Algebras.Associative(R)` | Associative `R`-bilinear multiplication. |
| `Algebras.Unital(R)` | `R`-bilinear multiplication with its actual two-sided unit. |
| `Algebras.Commutative(R)` | Commutative `R`-bilinear multiplication. |
| `Algebras(R)` | The actual `R`-module and its bilinear multiplication. |
| `Modules(R)` | The fixed scalar ring and action; no finite module basis follows. |
| `ModulesOverCommutativeRings` | The module together with its commutative scalar ring. The fixed `R` branch lies over the identity scalar map. |
| `OwnedAdicallyCompleteRings` | Completeness for the selected target ideal, without selecting a polynomial presentation. |
| `OwnedRings.Commutative` | A commutative unital associative ring. |
| `OwnedRings` | A unital associative ring with additive inverses and distributivity. |
| `OwnedSemirings` | Commutative additive and unital multiplicative monoids, with distributivity and zero. |
| `OwnedRngs` | An additive abelian group and associative distributive multiplication. |
| `Monoids` | Associative multiplication with a two-sided identity. |
| `Semigroups` | Associative multiplication. |
| `Magmas.Unital` | Multiplication with a two-sided identity. |
| `Magmas.Commutative` | Commutative multiplication. |
| `Magmas` | Multiplication as a binary operation. |
| `AdditiveGroups.AdditiveCommutative` | An additive abelian group. |
| `AdditiveGroups` | An additive group. |
| `AdditiveMonoids` | Associative addition and zero. |
| `AdditiveSemigroups` | Associative addition. |
| `AdditiveMagmas.AdditiveCommutative` | Commutative addition. |
| `AdditiveMagmas` | Addition as a binary operation. |
| `Sets` | The underlying set and its common cardinality contract. |
| `Objects` | The common owned-object category. |

`OwnedCategoryOverBaseRing`, OwnedCategory, and the category-with-axiom
machinery are construction infrastructure, not additional mathematical
ancestors. AdicCompletions is a simultaneous construction placement of the
represented examples; it is not an authored superclass of FormalPowerSeriesRings.
Local, Complete, Nontrivial, Noetherian, integral domains, fields, finite sets,
free modules, finite modules, framed algebras, and finitely generated algebras
are not uniform ancestors of this owner.

In particular, `R[[X]]` is complete for the variable ideal independently of
whether `R` is Noetherian or local. If the selected coefficient ring is local,
the existing constructor can additionally place the result as local. It uses
the maximal ideal `m_R A + (X)`, and supplies completeness for that maximal
ideal only under its actual complete-local or field hypotheses. That ideal
must not replace a separately retained chosen adic ideal `(X)`.

#### Actual Mor packet and literal maps

FormalPowerSeriesRings introduces no `_MorCategory`, Mor override, or
MorphismMethods. Its algebra ancestry supplies the existing unital
`R`-algebra Mor family. The common adic branch supplies RingMor, which is
already an underlying Mor of the unital algebra branch. The packet selector
walks declared semantic supercategories with the same literal endpoints and
discards a Mor candidate that is strictly above another. It does not select a
stronger category merely because an endpoint also has a selected completion
presentation.

For the actual selected formal-series parents, `_AdicCompletionAlgebraParent`
passes `algebra_labels=None` to `_OwnedAlgebraParent`. The latter returns
without supplying an algebra resolution. The Unital algebra owner therefore
selects `UnitalMultiplicativeAlgebraMor`, through its existing
`_algebra_mor_class()` choice. Formal parameters have not been mislabeled as
ordinary algebra generators. This Mor retains an actual `R`-linear map and
the product/unit equations. Its identity uses the underlying module identity;
this route does not require a finite list of algebra generators. The existing
generated arrow graph also retains the underlying ring, monoid, additive,
module, and set operations appropriate to those declarations.

No separate continuity condition, preservation of selected variable labels,
or equality of chosen adic ideals is added by this Mor declaration. Any
automatic continuity theorem requires its own mathematical hypotheses; it is
not a new assertion of this pass.

The two important arrows have different sources:

| Arrow | Literal endpoints and equation |
| --- | --- |
| Polynomial coefficient inclusion `i` | `R -> P = R[X]`. |
| Completion map `lambda` | `P -> A`; for corresponding formal/source labels `x_j, q_j`, `formal_parameter(x_j) = lambda(P.algebra_generator(q_j))`. |
| Coefficient structure map `c` | `R -> A`; `c(r) = rho(r)(1_A)` and `c = lambda * i`. |
| Local residue map when selected | `A -> k(R)`; `f -> residue_R(coefficient(f, 0))`. |

The common ring-center owner returns `A` itself for a commutative ring, so
the scalar structure map's center codomain is literally `A` here. In the
Adic owner repair in `13d391e8f2`, the completion realization supplies `lambda`
to the common algebra structure-map hook only when its scalar ring is its
completion source. For Formal parents the coefficient ring is `R`, not `P`,
so the existing derivation from the retained `R`-action supplies `c` instead.
No formal coefficient map is replaced by the completion map with the wrong
domain. Both are ordinary owned ring maps when used at that interface.

#### Coefficient repair and source proof

The installed LazyModuleElement indexing implementation returns the degree
`d` homogeneous component of a several-variable series. For `d > 0` that
component is generally a polynomial in the formal variables, not an element
of `R`. The former method attempted to cross that polynomial into the owned
coefficient ring. Its degree-zero use was valid because the homogeneous
component there is constant.

The repaired operation first normalizes exact integral indices using Python's
index protocol. A tuple has exactly one exponent for each selected parameter.
Integer indexing retains the one-variable convention, and integer zero means
the constant term in every arity. Negative exponents return `R.zero()`.
A positive integer without a variable choice in arity other than one gives an
informative input error rather than fabricating one scalar coefficient.

The native free-algebra constructor also establishes the required source-label
correspondence. It retains the actual ordered module labels as its algebra
labels, while `_variable_names` may rename them for the native polynomial
model. Its generator evaluator sends the label at position `j` to native
`engine.gen(j)`. The positive-variable completion retains those native names
in the same source order. Therefore the formal parameter at position `j`
must use the source's actual algebra label at that position. The corrected
accessor does exactly this before applying the retained completion map. For
example, original label `0` can have native/formal name `x0` without asking the
source algebra to treat `x0` as its label. All retained labels and maps remain
unchanged.

For an exponent vector `a`, the multivariate operation reads the homogeneous
component of total degree `sum(a)` and asks its existing polynomial index for
the monomial coefficient. Installed libsingular source returns a scalar in its
actual base ring, or that ring's zero when the monomial is absent. The generic
polynomial documentation also specifies this exponent-tuple interface.
`_owned_engine_element(R, coefficient)` then performs the existing owned
crossing. No second coefficient algorithm, support enumeration, scalar
Boolean conversion, or new presentation is introduced.

Native completion preserves the requested variable order, which can differ
from the polynomial source's order when an ideal's selected generators are
permuted. The public exponent tuple refers to `formal_parameter_set()` order.
The patch permutes it by variable name into the native parent order before
the scalar lookup. It does not reorder or replace the retained parameter set.

The coefficient algorithm requires a selected finite ordered parameter
family before enumeration. A different or infinite parameter presentation
has an explicit computation frontier; it is not silently iterated or declared
finite. A proved zero coefficient ring returns its actual zero without
requiring the degenerate completion engine to have a series index. With an
empty family, the unique coefficient is the actual constant crossed into `R`.
An undecided equation `1_R = 0_R` is not coerced to Boolean and does not trigger
the zero-ring shortcut.

The existing completion element class, its owned algebra element base, and
the owned ring element base introduce no competing element coefficient or
indexing method. The category's element provider therefore reaches this
repair through the actual selected realization.

#### Cardinality, bases, and source closure assertions

For `n = |X|` finite, the coefficient functions are indexed by `N^n`.
When `n = 0`, this monomial set has one element, so the cardinal is `|R|`.
When `n > 0`, it is countably infinite, so the cardinal is `|R|^aleph0`.
The patch keeps this existing formula and the common optional cardinality
supplier contract. It never calls `R.cardinality()` just to discover whether
the coefficient cardinal is available.

| Source assertion | Justification and qualification |
| --- | --- |
| For `A = QQ[[t]]`, `coefficient(3 + 2t + 5t^2, 2) = QQ(5)`, and `[2]` gives the same value. | Integer indexing follows the existing one-variable native coefficient path and the actual QQ crossing. `(2,)` names the same exponent. |
| For retained `A = ZZ[[x,y]]`, the coefficient of `(1,0)` in `3 + 2x + 5y^2 + 7xy` is `ZZ(2)`, of `(0,2)` is `ZZ(5)`, and of `(1,1)` is `ZZ(7)`. | Homogeneous degrees one and two followed by the corresponding native monomial index. The result parents are the literal owned ZZ. |
| `coefficient(f, 0)` equals `coefficient(f, (0,0))` in that two-variable ring. | Both select its homogeneous constant and then the zero-exponent monomial. This preserves the Local residue-map consumer. |
| A completion of `P = R[x,y]` whose selected variable generators occur as `(y,x)` still interprets `(1,0)` as the coefficient of `x` when the retained formal labels are `(x,y)`. | The native completion keeps `(y,x)`; the new name-based permutation sends the public exponent tuple to `(0,1)` for that native index. |
| A native symmetric algebra on a free module with actual label `0` and native variable name `x0` yields `formal_parameter("x0") = lambda(P.algebra_generator(0))`. | Both labels have selected position zero. The source generator evaluator was explicitly constructed by that position; no equality between the integer label and the native string is assumed. |
| A negative exponent has coefficient `R.zero()`; wrong tuple length or a nonconstant integer index in several variables gives an informative error. | These branches need no scalar-equality decision or coefficient scan. Exact index conversion does not truncate a nonintegral input. |
| Over `R = ZZ/(9)`, the selected local residue map on `R[[x,y]]` sends constant `R(4)` to its class `1` in the actual residue field. | The existing explicit RingMor composes coefficient zero with the base's actual residue map; its maximal ideal is generated by the base maximal ideal and the formal variables. No field assumption on `R` is needed. |
| Over a finite nontrivial coefficient ring and positive finite `n`, the cardinal is continuum. | The retained finite cardinal is at least two, and its countable power is the existing cardinal expression. This includes finite nonfields as well as finite fields. |
| Over a countably infinite coefficient ring and positive finite `n`, the cardinal is continuum. | The formula is `aleph0^aleph0`; it does not require a field or characteristic zero. |
| For an arbitrary supplied infinite coefficient cardinal `kappa`, positive finite `n` supplies `kappa^aleph0`. | No continuum-hypothesis simplification or stronger size claim is made. |
| A retained empty family supplies cardinal `|R|`, and coefficient `()` or integer `0` lies in the actual `R`. | The guarded Adic metadata companion preserves the selected zero-variable case. Native parser notation is not claimed to have run. |
| Over the zero coefficient ring, every coefficient is its actual zero and the finite-variable cardinal is one, while the selected variable labels are retained. | The guarded degenerate Formal metadata branch supplies those actual labels and base. This gives no Nontrivial or Local placement. |
| Missing coefficient cardinal, missing parameter cardinal, or a supplied nonnormal or infinite parameter cardinal returns no optional formula. | The owner neither forces an exact count nor extends the countably-many-monomials formula to an unsupported infinite parameter presentation. |
| A commutative non-Noetherian coefficient ring is an admissible parameter; a bare noncommutative ring is not. | The parameter correction follows the commutative constant-series structure. Native realization or ideal computations can still have their existing reported frontier. |

These witnesses exercise positive degree and constants, one and several
variables, reordered native variables, finite and infinite coefficient sets,
finite nonfield local coefficients, and the two degenerate parameter cases.
They do not infer finite generation of the completed ring as an algebra or
module, flatness of arbitrary completion maps, locality for every coefficient
ring, or a native computation for every abstract commutative ring.

#### Exact source evidence and retained computation frontiers

The complete owner, selected completion factory, completion parent/element classes and Local constant-coefficient consumer were read in `src/dzack_research/preamble/categories/rings/commutative_algebra.py`. The literal ring wrapper and commutative center are in `categories/rings/ring_foundation.py`; the fixed algebra parameters, `_OwnedAlgebraParent`, scalar-map hook and actual multiplicative Mor providers are in `categories/algebras/algebras.py`. The native free-algebra constructor, variable-name normalization and position-to-generator correspondence are in `categories/algebras/free_algebras.py`. The actual module ancestors are in `categories/modules/pure/modules.py` and `categories/modules/fibered_modules.py`. The ring, semiring, magma, set and object definitions, axiom framework and actual Mor packet selector were read at their existing owners; these are authored source deductions, not runtime MRO observations. Paths abbreviated with `categories/` are relative to `src/dzack_research/preamble/`.

Installed primary Sage source was read for lazy-series degree indexing and multivariate homogeneous components (`sage/rings/lazy_series.py`), exact scalar monomial indexing (`sage/rings/polynomial/multi_polynomial_libsingular.pyx`), and polynomial completion's requested variable order, empty family and exact lazy mode (`sage/rings/polynomial/multi_polynomial_ring_base.pyx`). The corresponding public [lazy-series](https://doc.sagemath.org/html/en/reference/power_series/sage/rings/lazy_series.html), [multivariate polynomial coefficient](https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/multi_polynomial_libsingular.html), and [polynomial completion](https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/multi_polynomial_ring_base.html) interfaces support the retained algorithms.

Native realization of an arbitrary coefficient ring, an unselected or infinite formal parameter presentation, an unavailable coefficient computation and missing exact cardinal data remain computation frontiers inside this pass and T. They do not deny the corresponding mathematics. No project import, Sage execution, runtime test or additional prerequisite is part of this M1 closure. The original once-only Step-3 denominator remains 18.

### Whole-category placement: `AdicCompletions.Local` (2026-10-11; source pass closed)

**Closed independent owner pass: `placement-owner-adiccompletions-local`.** This newly authored provider implements the already existing Local axiom on selected completions. Its complete two-operation pass is added and closed in this same bank. The explicit source inventory changes from 630 to 631 owners; this is no new prerequisite, axiom or parallel category, and Step 3's completed 18-operation denominator remains fixed.

#### Definition and complete two-introduction inventory

An object is a selected adic completion `lambda: R -> A` whose target A is local under the repository's existing nonzero local-ring convention. Its source ideal I need not be maximal. A may be complete for its selected extended ideal without being complete for its maximal ideal. Locality supplies the canonical target maximal ideal, residue field and residue map; the selected completion supplies R, I and lambda.

| Introduction | Disposition and precise data |
| --- | --- |
| `an_object` | Keep the selected 2-adic completion of the canonical owned integers. Its source ideal is maximal, so the existing constructor supplies actual CompleteLocal placement and therefore Local. It also installs the actual target maximal ideal/residue field and the retained residue-map factory. |
| `ParentMethods.source_residue_map` | Own the canonical composite `R -> A -> k(A)`, cached from the already fixed completion map and local residue map. This needs both construction data and locality. General AdicCompletions may be nonlocal; general Local rings have no selected completion source. No stricter maximal-source-ideal hypothesis is needed. |

There is no new constructor, `extra_super_categories`, ElementMethods, MorphismMethods, `_MorCategory`, arrow type, topology datum or other method. The common public residue map remains at OwnedRings.Commutative.Local. This provider does not forward or redefine it.

This is a narrowing to the actual required hypothesis, not an upward promotion. An outside-Adic specimen would lack the retained completion source and is not claimed. The actual constructor specimens are the integer prime-adic completion and `Z_2[[t]]`, with the nonlocal completion excluded as stated below.

#### Actual applicability through owned axiom propagation

The existing `_AdicCompletionAlgebraParent` assembles AdicCompletions with actual Local or CompleteLocal placement only from its supplied source/coefficients. The new nested provider is reached by the existing machinery:

- `OwnedCategoryMixin._with_axiom_as_tuple` detects the authored Local provider and constructs that refinement.
- `_owned_join_as_tuple` gathers axioms from the actual construction branches and propagates them through the declared branches until stable.
- When the constructor supplies Local, the Adic branch therefore becomes AdicCompletions.Local and receives the provider through actual category realization. CompleteLocal also contains the Local axiom.

No source-ideal maximality predicate is recomputed by `source_residue_map`, and no getter refines the ring. A supplied nonlocal completion does not receive this provider merely because it is adically complete. The zero completion is likewise not local under the repository convention.

#### Complete strict authored up-set: 21

This is the complete declared source ancestry, not an executed synthetic-join or C3 report. The intersection adds AdicCompletions, common Local and its Nontrivial consequence to the 18 strict ancestors of AdicCompletions, with their shared spine counted only once.

| Strict ancestor | Retained structure |
| --- | --- |
| `AdicCompletions` | The selected source R, ideal I, completion map lambda and its computation realization. |
| `OwnedRings.Commutative.Local` | The local target ring, canonical maximal ideal and residue quotient. |
| `OwnedRings.Nontrivial` | The repository's `1 != 0` consequence of locality. |
| `OwnedAdicallyCompleteRings` | The selected target ideal of definition and actual completeness. |
| `OwnedRings.Commutative` | Commutative unital associative ring. |
| `OwnedRings` | Unital associative ring. |
| `OwnedSemirings` | Additive commutative and multiplicative unital monoids with distributivity. |
| `OwnedRngs` | Additive abelian group and distributive associative multiplication. |
| `Monoids` | Associative multiplication and unit. |
| `Semigroups` | Associative multiplication. |
| `Magmas.Unital` | Multiplication and two-sided unit. |
| `Magmas.Commutative` | Commutative multiplication. |
| `Magmas` | Binary multiplication. |
| `AdditiveGroups.AdditiveCommutative` | Additive abelian group. |
| `AdditiveGroups` | Additive group. |
| `AdditiveMonoids` | Associative addition and identity. |
| `AdditiveSemigroups` | Associative addition. |
| `AdditiveMagmas.AdditiveCommutative` | Commutative addition. |
| `AdditiveMagmas` | Binary addition. |
| `Sets` | Underlying set. |
| `Objects` | Mathematical root. |

CompleteLocal, Noetherian, domain, field, Artinian, finite/enumerated, coefficient-algebra, and topological-space categories are not uniform ancestors. For example a local coefficient ring not complete at its maximal ideal can produce a variable-adic complete local formal-series ring without granting maximal-adic completeness. The constructor's stronger examples do not change this owner definition.

#### Actual Mor and canonical composition

The owned CategoryWithAxiom contract explicitly states that a property axiom adds no new morphisms. Its packet follows the original category's semantic Mor supergraph and reuses the compatible fixed Mor. Neither this provider nor common Local nor common Adic introduces another arrow condition. Both branches reach OwnedRings' RingMor construction with actual RingMorphism implementation and literal endpoint reuse.

Thus the category inherits ordinary unital ring maps; it does not declare them local or continuous. The particular `source_residue_map` is the actual canonical ring-map composite. The completion constructor already makes lambda an explicit ring morphism. Common Local returns the supplied actual residue arrow, and RingMorphism composition preserves the literal endpoints. Even when the same object has a coefficient-algebra placement, this operation does not invent an AlgebraMor callback or change the source action.

The composite has domain `completion_source()` and codomain `residue_field()`. Its middle object is literally self: `completion_map().codomain() is self` and `residue_map().domain() is self`. Both source maps are fixed before the cached composition; the getter chooses no ideal, field, topology or alternate realization.

#### Concrete local suppliers and absence of recursion

For source I maximal, the existing constructor retains the actual target maximal ideal and residue field and now supplies a lazy residue factory in LocalRingConstruction. The factory reads the first source projection `A -> R/I`, then composes the canonical identification with the retained residue field only when the codomain is not already literal. It does not call the common residue accessor or the new source composite.

For a formal completion over an actual local coefficient ring, the previously banked Local producer supplies constant coefficient followed by that coefficient ring's residue map. That case does not require the chosen source completion ideal to be maximal. For `A=Z_2[[t]]`, the chosen target defining ideal is `(t)` while the maximal ideal is `(2,t)`; the common residue map kills both 2 and t. `source_residue_map` composes `Z_2[t] -> A` with that same map, with no false substitution of `(t)` for the maximal ideal.

The ideal-extension construction depends on the source ideal and lambda. The local maximal-ideal supplier is independently fixed by its source ideal. Neither needs the new source residue composite, so there is no mutual getter recursion or first-access datum selection.

#### Closure assertions

These are unexecuted source assertions for the already existing owner/test framework.

1. The provider introduces exactly the two methods above, retains the 21 strict authored ancestors, and introduces no arrow/Mor method.
2. The existing integer prime-adic construction belongs to AdicCompletions.Local by actual constructor placement plus owned axiom propagation. The new `an_object` supplies that real construction witness.
3. For `A=ZZ.adic_completion(3)`, `source_residue_map` has literal source ZZ, literal target A's residue field, and sends 5 to 2. The existing Adic residue assertion remains the same mathematical assertion.
4. For a local formal completion with nonmaximal chosen source ideal, such as `Z_2[[t]]`, the same operation is available and uses the actual constant-coefficient/base-residue composite. It does not require the source ideal `(t)` to be maximal.
5. Nonlocal `QQ[x,y]` completed at `(x)` has no Local placement and receives no local residue operation from AdicCompletions. The existing negative method-access test is migrated to the actual category assertion, rather than depending on an absent leaf method raising a particular exception.
6. Source-residue calls for prime localizations still use their separately owned LocalizationRings.Local operation. The two composites have distinct retained source constructions; identical short bodies do not identify that construction data or authorize a common ring owner with no such source.
7. The cached source composite retains the actual fixed maps and endpoints; evaluating it does not create a parallel residue field, completion map, or chosen target ideal.

**Source evidence:** the entire new provider, actual selected completion constructors and common Local data/accessors, owned axiom propagation, packet dispatch and RingMorphism composition were read together. The complete caller ledger distinguishes completion source-residue consumers from the unchanged prime-localization source-residue consumers. All execution assertions remain under T during M1/DEV-58.

### Whole-category placement: `AdicCompletions` (2026-10-11; source pass closed)

**Closed independent owner pass: `placement-owner-adiccompletions`.** All original introductions, selected suppliers, actual ancestors, delivered ring arrows and affected callers have their own completed source review. The coherent source repair and the two existing assertion-source migrations are included in this bank. Execution remains under T and core-usability-session during M1/DEV-58.

#### Definition, retained data, and hypotheses

Write `lambda: R -> A = completion_I(R)`. This owner retains the literal source R, its selected source ideal I, the actual completion map lambda, and a selected computation precision/realization. The completed ring A is an inverse limit, not its finite computational stage. Its common adic defining ideal is the actual target extension `J=I*A`, supplied through the already banked common adic owner. A local A may additionally have a different maximal ideal m. None of these three ideals is substituted for another.

This data owner is broader than prime-adic, maximal-adic, domain, Noetherian, or formal-series completions. Conversely, its ancestors do not retain the particular source R, ideal I, lambda, or selected finite-stage realization. Source-dependent constructions stay here. A theorem about completion at an arbitrary ideal does not automatically supply an exact computation. In particular, the supported source producers use their represented finite ideal generators and exact source models; the pass does not claim that completion at an arbitrary infinitely generated ideal is automatically complete for its extended ideal. The finitely generated source-ideal completeness theorem is the previously checked Stacks Tag 05GG.

An object may also carry an actual coefficient-algebra placement. The ordinary selected completion uses R as coefficient ring; a full-variable formal completion of `k[t_1,...,t_n]` uses k. That extra placement is construction data, not a uniform authored ancestor of AdicCompletions.

#### Complete original introduction inventory: 27

The original category has three category methods and 24 ParentMethods. It declares no ElementMethods, MorphismMethods, `_MorCategory`, or arrow-type provider. The patch removes three leaf public introductions, adds one protected result decision, and authors the two-method existing Local refinement separately. Every original introduction is dispositioned below.

| Original introduction | Weakest retained data / final disposition |
| --- | --- |
| `an_object` | Keep the selected 2-adic completion of the integers as this construction owner's witness. |
| `super_categories` | Keep the actual implication to `OwnedAdicallyCompleteRings`; the chosen target ideal is supplied by the concrete completion participant. No local/domain/Noetherian implication is added. |
| `_call_` | Keep authoritative ingress `(R,I,precision)`, normalize the actual owned source and ideal, and reuse the existing cached factory. Precision remains computation data. |
| `completion_source` | Keep the fixed source R. No ancestor supplies a selected predecessor ring. |
| `completion_ideal` | Keep the fixed source ideal I, whose ambient ring is R. It differs from the target defining ideal. |
| `completion_map` | Keep the already selected lambda; cache only its fixed realization and require both literal endpoints `R -> self`. |
| `_completion_projection_lift` | Keep the protected selected finite-stage supplier. Its declared callers are this owner's projection and the prime-local completion constructor transporting it. |
| `algebra_structure_morphism` | Remove the duplicate public implementation. The existing Algebras owner constructs this operation, reading a declared optional retained-map supplier before its existing module-action derivation. The concrete completion supplies lambda exactly when R is its coefficient ring; otherwise the actual lower coefficient action is preserved. |
| `ideal_extension` | Keep the selected view `IdealExtensionData(lambda,I)`. General extension mathematics remains at the existing ring-map/ideal owners; this cached operation binds the already fixed pair. |
| `extended_ideal` | Keep the result projection of that retained construction, `I*A`, with literal target ambient ring. It does not select another ideal or repeat extension mathematics. |
| `truncation_ideal_extension` | Keep extension of the selected I along the actual source quotient `R -> R/I^n`. |
| `completion_map_kernel` | Keep the exact-value operation `ker(lambda)=intersection I^n`. Reuse the added optional result decision; assert at this named algorithm boundary when no kernel is supplied/computed. |
| `is_adically_separated` | Keep the property of the retained source for I. Consume the same optional kernel result and retain an Atomic proposition if unavailable. |
| `is_completion_map_injective` | Keep its semantic equivalence with source I-adic separatedness. No second kernel algorithm or false-from-undecided path is introduced. |
| `is_flat_over_source` | Keep the selected-source property. Noetherian R supplies True for its canonical completion; otherwise the existing proposition remains. This is not a claim about arbitrary maps into A. The preceding common Local repair restricted the separate flat-transport selector to the literal canonical completion arrow. |
| `computation_precision` | Keep the selected realization datum. It is neither a ring cardinal nor a truncation of the mathematical object. |
| `adic_inverse_system` | Keep the actual diagram `n |-> R/I^(n+1)` in commutative rings. Its fixed source data are absent above this owner. |
| `adic_truncation` | Keep `R/I^n` for `n>0`; it is a source quotient, not an unrecorded substitution of `A/J^n`. |
| `adic_artin_truncation` | Keep the named selected stage, requiring actual Artinian placement. The underlying stage exists more generally and is exposed by `adic_truncation`. |
| `adic_transition_map` | Keep the canonical source-quotient map for `m>=n>0`; construct its elementwise evaluator in explicit RingMor. |
| `adic_projection` | Keep `A -> R/I^n`. First use an exact retained source expression at any n; otherwise use the selected finite-stage supplier with its element-level precision boundary. Use explicit RingMor. |
| `induced_map` | Keep continuous extension out of this selected completion. Admit an actual ring arrow from R either into the complete target or into another selected completion's source, and establish the corresponding ideal-image condition. The exact-source evaluator is shared by these routes. |
| `maximal_localization_comparison` | Keep the comparison between completing at a maximal ideal before/after localization. Its theorem is general; the current selected computation remains Noetherian. The repaired inverse extends `R_m -> A` into the already complete target, rather than requiring a nonexistent `R_m -> R`. |
| `residue_map` | Remove the nonlocal leaf public override. Existing common Local owns the residue map. The selected completion constructor now supplies its actual local quotient through the existing LocalRingConstruction, including a lazy maximal-source-ideal residue factory. |
| `source_residue_map` | Move to `AdicCompletions.Local`: the operation needs both lambda and the target's local residue map. General Adic objects may be nonlocal, while common Local objects need not have a completion source. |
| `adic_limit_cone` | Keep the actual cone with vertex A and legs `adic_projection(n+1)`. |
| `adic_limit_construction` | Keep the existing selected inverse-limit datum. Its supplied-cone identity factorizer uses explicit RingMor. Arbitrary compatible-series factorization remains its stated computation boundary. |

Added `_completion_map_kernel_decision` is a protected optional result at this same owner. Its declared consumers are the public kernel, source-separatedness, and exact-source element equality. It supplies an actual source ideal or None; None is not a zero ideal or an injectivity claim. There is no new capability flag, registry, comparison record, or public forwarding family.

The upward moves have actual specimens outside the old Adic category. The ordinary polynomial algebra `QQ[x]` receives `QQ -> QQ[x]` from the shared Algebras structure-map owner and its actual coefficient action; it is not a selected AdicCompletions object. The selected prime localization `ZZ_(3)` receives its residue map to its retained residue field through the same common Local accessor and its existing LocalRingConstruction; it likewise is not an Adic completion. These specimens exercise the promoted public homes. Moving `source_residue_map` to Adic.Local is instead a restriction to its required locality hypothesis: no outside-Adic specimen is possible or claimed for that construction-specific operation.

#### Complete strict authored up-set: 18

This is the source-declared mathematical up-set, including the existing axiom propagation. It is not an executed C3/MRO listing. Synthetic intersections are not extra authored owners.

| Strict ancestor | Structure retained after forgetting the completion datum |
| --- | --- |
| `OwnedAdicallyCompleteRings` | A commutative ring with its selected target defining ideal and actual completeness. It has no selected predecessor `(R,I,lambda)`. |
| `OwnedRings.Commutative` | Commutative unital associative ring. |
| `OwnedRings` | Unital associative ring with distributivity and an additive abelian group. |
| `OwnedSemirings` | Additive commutative and multiplicative unital monoids with distributivity and absorbing zero. |
| `OwnedRngs` | Associative distributive multiplication and additive abelian group. |
| `Monoids` | Associative multiplication with a two-sided unit. |
| `Semigroups` | Associative multiplication. |
| `Magmas.Unital` | Multiplication with a two-sided unit. |
| `Magmas.Commutative` | Commutative multiplication. |
| `Magmas` | Binary multiplication. |
| `AdditiveGroups.AdditiveCommutative` | Additive abelian group. |
| `AdditiveGroups` | Additive group. |
| `AdditiveMonoids` | Associative addition with identity. |
| `AdditiveSemigroups` | Associative addition. |
| `AdditiveMagmas.AdditiveCommutative` | Commutative addition. |
| `AdditiveMagmas` | Binary addition. |
| `Sets` | Underlying set. |
| `Objects` | Mathematical root. |

Local, CompleteLocal, Nontrivial, Noetherian, domain, field, Artinian, coefficient-algebra, finite/enumerated set, and topological-space owners are not uniform ancestors. Examples produced by stronger constructors do not add such a universal edge.

#### Actual Mor inheritance and the existing AlgebraMor inputs

AdicCompletions and OwnedAdicallyCompleteRings introduce no different Mor. The source graph reaches `OwnedRings` and its `RingMorCategoryConstruction`, whose fixed category is RingMor with the actual RingMorphism provider. The generated arrow type visits that declared fixed-Mor supergraph; it does not copy methods into a new shell. The category therefore has the existing unital ring maps. It does not silently require continuity or a local homomorphism. `induced_map` separately constructs a continuous ring map from its supplied sufficient continuity data.

The new source-map admission preserves the existing `line.Mor(line)` inputs in `test_completion_maps.sage`. The actual chain is:

1. `Algebras(k).Associative().Unital().extra_super_categories()` explicitly includes OwnedRings.
2. The algebra Mor family preserves the literal domain and codomain when forgetting coefficient action. `CategoricalMor.super_categories()` constructs the corresponding fixed super-Mors on those endpoints.
3. `CategoricalMor.__contains__` sends an actual Morphism to `accepts`, which checks both literal endpoints and `_already_parented_arrow`.
4. `_arrow_is_inherited_from_subcategory` admits a stronger fixed Mor only when its declared supergraph reaches the target RingMor. `_declared_category_reaches` follows those actual edges, not successful trial conversion or merely matching endpoints.
5. `_generated_arrow_type` reads the same graph, so the ring provider is actually delivered to these algebra arrows.

Consequently the existing x-to-x^2, algebra identity, and x-to-1 maps remain genuine admitted ring arrows. Their ideal-image conditions distinguish the first two from the third. An additive or set Map with the same endpoints is not admitted merely because its values happen to land in the target ideal. No change to RingMor or AlgebraMor is required for this admission.

The identity shortcut also respects actual supplied identity data. AlgebraMor caches its identity, while RingMor constructs a fresh identity with `_preamble_is_identity=True`. The patch retains the literal/cached branch and also accepts `source_morphism.is_identity() is True`, before asking for ideal containment. It returns the explicit ring identity on A.

#### Concrete selected producers and every affected element operation

The concrete classes are realizations of these data, not extra category owners.

| Supplier or concrete operation | Source disposition |
| --- | --- |
| `_adic_completion_from_owned_data` | Keep the one cached selected completion factory. Retain the source ideal, precision, kernel when proved, and each existing arithmetic/projection model. Sufficient equality branches require `is True`; undecided comparisons do not authorize a zero/unit/nilpotent/idempotent case. |
| Prime-local completion branch | Transport the selected bottom completion and its projection lift through the actual localization. The stored zero kernel is supplied only when the localized source is Noetherian, rather than claiming separatedness of every local source. |
| Unit-ideal branch | The inverse limit is the zero ring; stored source kernel is I=R. No proper-ideal Krull argument applies. |
| Zero-ideal branch | The completion is exactly its source realization and the kernel is zero. |
| Integer prime-adic branch | Retain the actual prime completion. The opaque projection supplier checks `value.precision_absolute()`, not the nominal cap of a containing parent. |
| Presented finite-stage branch | A finite quotient model remains an approximation unless an actual nilpotent or idempotent ideal calculation supplies exactness. An agreeing finite stage supplies no exact equality or zero kernel. |
| Polynomial-variable branch | Retain the maintained exact lazy completion and actual selected variables. The map from a polynomial ring is injective over any coefficient ring, by finite degree in those variables. No domain hypothesis is needed for this supplied zero kernel. |
| Degenerate formal companion | Only an already framed symmetric-algebra source with an actual finite ordered label family can supply metadata. A proved zero source, or an empty selected family with I=0, retains that coefficient ring and label family through scalar/zero engines. An empty-family unit completion of a nonzero source does not acquire false Formal placement. No native empty parser or notation execution is claimed. |
| `_AdicCompletionAlgebraParent.__init__` | Fix source I, completion-map factory, realization mode, precision and optional source kernel before exposing the parent. Keep actual chosen coefficient/formal data. Source maximality is not bool-coerced. Existing LocalRingConstruction receives a supplied actual residue map/factory, so common Local is the sole public residue owner. |
| `_selected_adic_defining_ideal` | Keep the already banked target-ideal supplier using the fixed `(lambda,I)` extension. It does not ask for the target maximal ideal. |
| Added `_selected_algebra_structure_morphism` | Supply the literal lambda when source and coefficient ring coincide; otherwise None requests the existing actual module-action derivation. No second map cache or independent scalar action is introduced. |
| `completion_arithmetic_mode`, `_completion_element` | Keep the selected mode and wrapping of the actual engine value with optional exact source expression. |
| `_element_constructor_`, `zero`, `one` | Keep canonical source ingress through lambda, preserving exact source expressions and literal parent identities. |
| `_AdicCompletionElement.__init__`, `exact_source_expression`, `_with_source_expression` | Retain exact source data separately from finite engine data. A finite approximation alone never fills that slot. |
| `_cache_key` and `__hash__` | Preserve the existing conservative exact-source/identity cache key and the unhashable equality-sensitive element contract. No undecided equality is used to merge opaque elements. |
| `_add_`, `_mul_`, `__mul__`, `__rmul__`, `_neg_`, `__pow__` | Existing arithmetic preserves exact source expressions when its operands/exponent supply them; scalar module dispatch remains unchanged. Negative powers may lose source expressions. These operations were read for changed equality/projection consumers, not rewritten. |
| `_exact_source_equality_status` | A proved zero source difference gives True. Otherwise use the optional source kernel; None remains unavailable, and actual ideal membership may remain a proposition. No bool-coercion turns an undecided membership into a decision. |
| `_completion_equal`, `__eq__`, `__ne__` | Retain exact source and existing exact backend/lazy decisions. Finite disagreement proves False; finite agreement gives an Atomic equality proposition. Inequality uses mathematical negation. |
| `__bool__`, `is_zero`, `is_one` | Zero and one queries retain the equality proposition. An explicit Python truth conversion continues to reject undecided propositions with the logic owner's TypeError; it is not a mathematical negative answer. |
| `_unit_decision`, `_unit_inverse_decision` | Keep the selected backend unit supplier. The inverse branch handles True/False/unknown distinctly: compute, reject a proved nonunit, or return None to the existing exact inverse frontier. It does not turn an unknown unit predicate into a nonunit. |
| `precision_absolute`, `refine_precision` | Preserve the represented element's actual precision and the existing exact-source-only refinement. An opaque element cannot acquire digits by changing the parent cap. Source refinement reuses the same source ideal and actual completion map. |
| `_AdicQuotientInverseSystem.__init__`, `completion`, `base_index_category`, `system_category`, `exponent`, `_apply_object`, `_apply_morphism` | Keep the seven existing functor operations. Index n corresponds to exponent n+1; an opposite index arrow gives the transition from the higher quotient to the lower. No finite-stage or arrow orientation changes. |

The optional kernel decision first respects a retained exact source kernel, then the existing zero/square-zero/idempotent ideal computations. Its Krull-intersection sufficient case requires a Noetherian source, domain or Local placement, and a proved proper ideal (`1 notin I`). Unknown properness is not false membership and does not justify kernel zero. The source review independently checked the Noetherian-local theorem at [Stacks 00IP](https://stacks.math.columbia.edu/tag/00IP) and the domain consequence using a maximal ideal containing I at [Stacks 00IJ](https://stacks.math.columbia.edu/tag/00IJ). The review does not add a general intersection-of-ideal-powers solver.

#### Caller reconciliation

The complete live src/tests/docs caller search and the four existing completion assertion files were read. Generated graph/megadoc entries remain source-phase snapshots.

| Actual caller family | Contract after this unit |
| --- | --- |
| Public kernel assertions in `test_adic_completions_construct`, `test_completion_maps`, `test_completion_comparisons` | The integer, nilpotent, idempotent and unit-collapse values remain exactly the same source ideals. Required exact calls assert when the optional decision has no result. |
| `is_adically_separated` and `is_completion_map_injective` | Optional predicate consumers no longer force the exact kernel accessor. |
| `_AdicCompletionElement._exact_source_equality_status` | Uses the optional result directly and preserves an undecided source-ideal membership. |
| Exact-expression arithmetic, cache, precision, Local maximal-ideal helper, quotient-completion comparison | Existing representation contract retained. Projection is the new consumer that can use an exact expression beyond the selected finite stage. |
| Maximal-localization comparison's two `induced_map` calls | Forward source map ends in the localized completion's source; inverse source map ends in the original completed target itself. Both now have literal valid endpoints. |
| `_quotient_completion_comparison` | Its quotient source map continues through the same source-to-source induced-map route. No quotient comparison mathematics is duplicated. |
| Existing `line.Mor(line)` induced-map tests | Actual inherited ring-arrow admission as proved above; x-to-x^2 and identity admitted, x-to-1 rejected by the ideal condition. |
| Existing integer RingMor identity test | Retained identity flag is accepted even though a fresh `.identity()` is not literally the same object. |
| Existing Adic residue tests | A selected local completion receives the common Local residue map and new Adic.Local source composition, with the same field and maps. |
| Prime-local source residue callers | Their existing LocalizationRings.Local operation is a different source construction and remains untouched. |
| Common Algebras public scalar-map caller | The existing helper is the sole caller of the declared retained-map supplier. Completion's public leaf duplicate is removed. |
| Common local datum hook | Its caller documentation no longer names the removed Adic public residue selector. The existing Local accessor/field decision/installation roles remain. |

Two existing assertion bodies require interface migration, supplied in the 43-line assertion companion. The nonlocal x-adic completion of `QQ[x,y]` now asserts absence from LocalRings instead of calling a method which belongs only to local rings. The existing fat-plane arithmetic test retains the true nonvanishing of y^4: modulo `(x,y)^5` it is visibly nonzero, while the cap-4 equality procedure carries an undecided proposition and explicit Boolean conversion raises TypeError. This does not weaken y^4 to a potentially zero mathematical element or pretend the current kernel algorithm decides it. The direct completion equality decision remains required later computation; the same test already has the true next-stage witness.

#### Source closure assertions and precise remaining computation boundaries

All following assertions are source-backed expectations retained for later authorized execution; none was executed here.

1. The 27 original introductions are all dispositioned, and the original 18 strict authored ancestors and RingMor are accounted for. Three public leaf operations move to their correct existing owners; the new Adic.Local provider receives its own complete two-method pass and owner inventory row.
2. `completion_source`, `completion_ideal`, and `completion_map` retain literal R, I and lambda. `lambda.domain() is R` and `lambda.codomain() is A`. The common target ideal remains `I*A`, even when A also has a distinct local maximal ideal.
3. For an ordinary selected completion the inherited Algebras structure map is literally lambda; for a full-variable formal completion it is the actual lower coefficient action. Existing algebra-map callbacks are not reinterpreted as elementwise ring callbacks.
4. Every canonical stage/transition/projection/induced map and supplied-cone identity is an actual owned ring arrow on its literal endpoints. `projection_n(lambda(r))` equals the source quotient image of r for every n for which that source quotient is supplied, even beyond the chosen approximation cap.
5. In an opaque p-adic value at precision 2, requesting a stage requiring precision 4 reaches the actual element-precision assertion. Coercing the value into a larger-cap parent does not authorize missing digits. Exact source images are handled separately by the previous assertion.
6. The nilpotent and idempotent source examples retain their known kernels, and completing at the unit ideal yields the zero ring with whole-source kernel. Noetherian domain/local proper-ideal cases have zero kernel. Finite agreement or unknown properness does not certify injectivity.
7. The fat-plane element y^4 is nonzero, witnessed by its nonzero image modulo the fifth ideal power. Current is_zero may remain Atomic; ask returns Unknown and host truth conversion refuses it. Exact source projection obtains the true finite-stage witness without promoting cap-4 agreement to equality.
8. The selected x-to-x^2 source map induces the expected continuous formal map; an actual supplied identity returns ring identity without an ideal-membership computation; x-to-1 is rejected. A merely additive x-to-2x-style map is rejected by actual ring-arrow admission even if an endpoint/ideal-only test would have accepted it.
9. For a maximal source ideal m, each `R/m^n` is already local, so localization outside m is an isomorphism at every stage; the inverse limits agree. The current construction still uses its Noetherian source regime and retained-expression evaluator. The repaired comparison arrows have actual inverse-direction endpoints and the mathematical inverse theorem.
10. A computed round trip on every represented element is not claimed. The existing localization evaluator divides even for denominator one, and completion unit inversion can lose exact source expressions. Thus finite-precision p-adic comparisons may return an opaque image whose equality is Atomic; applying another exact-source-only induced evaluator may assert. Exact-lazy polynomial comparisons can retain their supplied exact backend decisions. This is an existing representation/evaluation boundary, not a false inverse theorem or a new prerequisite.
11. The selected inverse-system orientation and positive exponent requirements are unchanged. The limit datum factors its own supplied cone by actual ring identity; an arbitrary compatible infinite cone still needs a selected construction not provided by this owner.
12. Degenerate formal metadata is preserved only from an existing chosen finite ordered frame. The zero coefficient ring and an already selected empty family with I=0 keep the correct base/labels through scalar realizations. No native parser or arbitrary unframed generator availability is inferred.

General ideal-power intersections, undecided ideal-image computations, arbitrary compatible-series factorization, arbitrary continuity beyond the supplied `f(I) subset J` condition, and missing exact-source metadata remain explicit limitations inside this owner. None is converted into a new prerequisite node, a false negative mathematical predicate, or a claim that a broader category lacks the operation.

**Source evidence:** the full live `categories/rings/commutative_algebra.py` Adic category, element/parent realizations, selected factory and quotient-completion consumer; `categories/algebras/algebras.py` scalar owner, module action and actual Mor providers; common Local and RingMor in `categories/rings/ring_foundation.py`; actual `owned_category.py`, `owned_category_bases.py`, `categories/abstract_categories/mor_categories.py` and `mor_foundation.py` dispatch; the complete additive/multiplicative/set ancestor definitions; and the four current completion assertion sources were read. Installed Sage LazySeries.truncate and LazyPowerSeries.polynomial confirm the existing exact finite-stage conversion. An independent source review reconciled all map/precision/hypothesis assertions. No Sage, project import or runtime assertion was run.

### Whole-category placement: `OwnedAdicallyCompleteRings` (2026-10-11; source pass closed)

**Closed independent owner pass: `placement-owner-ownedadicallycompleterings`.** An object is a commutative ring A with a chosen ideal J of A for which A is adically complete. Although every ring is complete for its zero-adic structure, bare ring membership selects no defining ideal. This category's chosen datum does not uniformly imply locality, nontriviality, Noetherianity, a domain, a field, finiteness, enumerability or a coefficient-algebra structure.

| Introduction (all five after repair) | Definition and disposition |
| --- | --- |
| `an_object` | Retain the actual 2-adic completion of the owned integers with its chosen defining ideal. |
| `super_categories` | Retain the direct commutative-ring edge. |
| `is_adically_complete` | Return True for this already supplied complete adic structure. |
| `ideal_of_definition` | Return the actual selected ideal of the literal ring; enforce its owned-ideal category and ambient-ring identity. |
| `_selected_adic_defining_ideal` | Declare the protected RealizationHook value contract, with None meaning no selected value is supplied. Existing stronger categories and concrete participants supply the data. |

The common owner introduces no ElementMethods, Mor family, arrow constructor, generic pair constructor or additional category. Both public parent operations belong here: every strict ancestor forgets the chosen complete adic datum, while a selected source-completion presentation is stronger than these operations require.

**Complete strict authored up-set (17 owners):** OwnedRings.Commutative; OwnedRings; OwnedSemirings; OwnedRngs; Monoids; Semigroups; Magmas.Unital; Magmas.Commutative; Magmas; AdditiveGroups.AdditiveCommutative; AdditiveGroups; AdditiveMonoids; AdditiveSemigroups; AdditiveMagmas.AdditiveCommutative; AdditiveMagmas; Sets; Objects. The actual definitions retain the commutative unital ring, its semiring/rng and multiplicative structures, its additive abelian group and weaker additive operations, and its underlying set/root. These same definitions are stated individually in the Prime up-set table. Local and Nontrivial are not common ancestors: in particular, the zero ring is allowed. Complete local rings and fields enter from stronger owners without turning their extra properties into uniform consequences here. There is no authored topological-space or topological-ring edge.

**Delivered arrows:** the category's actual packet Mor surface traverses its authored semantic supercategories, normalizes and checks literal endpoint objects, deduplicates inherited candidates by identity and reuses the compatible RingMor. OwnedRings declares RingMorCategoryConstruction, whose fixed Mor's ElementMethods is the actual RingMorphism provider; the generated arrow inherits that implementation. An incidental algebra placement of an endpoint does not change this category's arrows into coefficient-linear maps. The clarified common docstring states the existing convention: ordinary unital ring maps, with no continuity condition. For example, an underlying ring identity from a nondiscrete chosen adic structure to the same ring's zero-adic structure need not be continuous. No continuous-map family is inferred or added.

**Actual selected-data path:** the common accessor calls its supplier once, then accepts only a non-None result in CommutativeIdeals(A) with literal selected.ring() is A. It neither coerces a source ideal into A nor chooses another ideal after unavailable data. The Complete refinement supplies its actual maximal ideal as the canonical default. An explicit selected completion supplier wins through the existing RealizationHook participant dispatch and returns the target extension through its existing cached IdealExtensionData. A concrete supplier returning None remains authoritative missing data even if Complete placement is also present.

For the retained map lambda:R -> A=completion_I(R), the source and target data are:

| Existing operation | Retained mathematical datum |
| --- | --- |
| `completion_source()` | The literal original source R. |
| `completion_ideal()` | The original selected I as an ideal of R. |
| `completion_map()` | The retained canonical lambda:R -> A. |
| `ideal_extension()` | The cached IdealExtensionData(lambda,I). |
| `ideal_of_definition()` | That datum's actual target ideal J=I*A. |
| `adic_truncation(n)` and diagram stages | The source quotient R/I^n and its source projection. |
| `truncation_ideal_extension(n)` | Extension of source I along R -> R/I^n. |
| Kernel, separation, source-map hypotheses and precision refinement | Source I and its operations in the original R. |

The fixed source slot is selected in the constructor. Caches evaluate views of those fixed data and do not make a first-access choice of topology. The call graph is common accessor -> concrete supplier -> cached ideal_extension -> IdealExtensionData(completion_map(), completion_ideal()) -> existing ring-arrow ideal extension. No step calls the common accessor again. Its target extension stays lazy and retains the existing computation boundary.

**Separating data and independent witness:** Z_2[[t]], presented as the completion of Z_2[t] at (t), keeps source I=(t), target J=(t) and maximal ideal (2,t) in their respective ambient rings. The element 2 separates the last two ideals. Source stages remain Z_2[t]/(t^n), and the supplied local residue is constant coefficient followed by reduction modulo 2. A Complete refinement cannot replace the explicitly selected target ideal by the maximal ideal.

Native QQ and GF(p) provide an independent construction through the existing Fields -> Local.Complete edge. Their zero maximal ideal gives the constant inverse system K/(0)^n=K. The ordinary native-field constructor uses _OwnedRingParent. After the independent Fields consolidation, common Local supplies a cached canonical LocalRingConstruction when no selected datum exists: the actual owned zero ideal is lazy, the residue field is literal K, and the residue map is the explicit RingMor identity. The Complete supplier and common accessor receive that actual target zero ideal without an AdicCompletions constructor or invented completion-source presentation. An actual selected field quotient datum retains its precedence.

**True closure assertions under T (unexecuted):**

1. An available defining ideal is an actual object of CommutativeIdeals(A) with literal ambient ring A; is_adically_complete is True for the supplied chosen structure.
2. The canonical integer 2-adic completion retains its source (2) and canonical map, while the common accessor returns their actual target extension in A.
3. Repeated accessor requests use the retained cached IdealExtensionData and its fixed target ideal; no source ideal, map or topology is reselected.
4. In Z_2[[t]], the target defining ideal (t) remains distinct from (2,t), independent of accessor order. Source truncations and precision refinement retain the original source I.
5. Native owned QQ and GF(p) supply their zero-adic ideals independently of selected source completions, while their existing residue field and identity map remain literal.
6. An explicit supplier returning None reaches the named missing-data assertion. A supplied ideal in the wrong ambient ring violates the target-ideal contract and is rejected.
7. The actual fixed Mor keeps its literal endpoints and inherited RingMorphism implementation. The category imposes neither continuity nor an incidental coefficient action.
8. The 17 authored ancestors retain no uniform Local, Nontrivial, Noetherian, finite, field or domain consequence. The zero-adic structure is mathematically allowed on zero and nonlocal rings.

**Mathematical and computation frontier:** the common definition requires completeness for J and does not require finite generation. Placing a constructed inverse-limit completion in this category is a separate theorem: [Stacks Tag 05GG](https://stacks.math.columbia.edu/tag/05GG) proves completeness for a finitely generated source ideal and identifies the finite quotient stages; [Tag 00M9](https://stacks.math.columbia.edu/tag/00M9) explains why arbitrary-ideal completion is not automatically complete. The selected examples above have finitely generated source ideals. This pass adds no generic public constructor for an arbitrary complete pair (A,J), no inference of a topology from a bare ring and no total ideal-extension solver.

The coordinated RingMor repair in 05056101fb restricts its Noetherian flat-transport shortcut to the literal retained canonical completion map. An arbitrary f:k[x] -> k[[t]] with f(x)=0 is not flat: tensoring the injective multiplication-by-x map with its nonzero target makes that map zero. Such an arrow uses the ordinary image-ideal route and its availability boundary. The selected adic supplier uses the actual canonical map, for which [Stacks Tag 00MB](https://stacks.math.columbia.edu/tag/00MB) supplies the Noetherian flatness theorem. This evidence does not close the separate RingMor or AdicCompletions passes.

**Source evidence and phase:** the entire common declaration, all 17 authored ancestor definitions, actual packet and fixed-Mor dispatch, hook supplier precedence, selected-completion constructor and every affected source-I caller, native field constructors/direct suppliers and existing assertion sources were read. The coherent source repair is committed in 05056101fb; all three changed Python files passed post-commit stdlib AST parsing. Every execution assertion remains under T and core-usability-session during M1/DEV-58.

### Whole-category placement: `OwnedRings.Commutative.Local.Complete` (2026-10-11; source pass closed)

**Closed independent owner pass: `placement-owner-ownedrings-commutative-local-complete`.** This category consists of commutative local rings complete and separated for the maximal-ideal topology. It does not require Noetherianity, a domain, a field, a finite or enumerable underlying set, a coefficient algebra or a selected presentation as another ring's completion. The original three introductions and the added protected datum supplier have all been reviewed.

| Introduction (all four after repair) | Definition and disposition |
| --- | --- |
| `_repr_object_names` | Retain the presentation of this complete-local property. |
| `an_object` | Retain the actual 2-adic completion of the owned integers. Its computational precision does not make the mathematical object a finite quotient. |
| `extra_super_categories` | Retain the implication to the common chosen-adic owner. The canonical maximal-adic choice does not overwrite an explicitly selected defining ideal. |
| `ParentMethods._selected_adic_defining_ideal` | Supply the actual maximal ideal as the canonical complete-local default for the existing common accessor. This marked RealizationHook yields to an explicit participant supplier. |

**Complete strict authored up-set (20 owners):** OwnedRings.Commutative.Local; OwnedAdicallyCompleteRings; OwnedRings.Commutative; OwnedRings.Nontrivial; OwnedRings; OwnedSemirings; OwnedRngs; Monoids; Semigroups; Magmas.Unital; Magmas.Commutative; Magmas; AdditiveGroups.AdditiveCommutative; AdditiveGroups; AdditiveMonoids; AdditiveSemigroups; AdditiveMagmas.AdditiveCommutative; AdditiveMagmas; Sets; Objects. Their actual definitions are the Local owner's unique proper maximal ideal and residue quotient, the Adic owner's chosen complete ideal, and the common ring/additive/multiplicative/set structures enumerated in the adjoining Local pass and the Prime up-set table. Locality alone does not assert maximal-adic completeness; a chosen complete ideal alone need not be the maximal ideal. The complete-local supplier therefore belongs exactly at this refinement. Fields is a descendant supplying an independent example, not an extra ancestor. No topological-space or topological-ring owner appears.

**Delivered arrows:** this refinement introduces no ElementMethods, Mor family, arrow constructor or arrow operation. The actual axiom and category-packet machinery traverses both its Local and common Adic branches, reaches RingMorCategoryConstruction, reuses the compatible fixed RingMor on the literal endpoints and preserves the generated arrow's actual RingMorphism provider. These are ordinary unital ring maps. This source does not claim that all admitted maps preserve maximal ideals or are continuous.

**Selected datum repair, committed in `05056101fb`:** the common `ideal_of_definition()` now accepts only an actual object of CommutativeIdeals(A) whose ambient ring is literally A. A selected completion lambda:R -> A retains its source ideal I under `completion_ideal()`, backed by the renamed fixed source slot. Its concrete protected supplier returns I*A through the existing cached IdealExtensionData(lambda,I). The Complete default instead supplies its actual maximal ideal when no more explicit participant supplier is installed. The actual RealizationHook dispatch gives the concrete supplier precedence; an explicit supplier returning None remains unavailable data and never requests substitution of the maximal ideal.

The cached extension is a view of data fixed at construction. Its path is common accessor -> concrete supplier -> ideal_extension -> IdealExtensionData(completion_map(), completion_ideal()). It does not call the common accessor again, does not require the residue map and does not add a second mutable datum or eagerly compute the extension when the completion is created.

Every source-I consumer was reconciled against the full caller search: ideal_extension, truncation_ideal_extension, completion_map_kernel, adic_truncation, both source ideals in induced_map, maximal_localization_comparison, the fallback source-ideal residue specialization and element refine_precision. Source quotients remain R/I^n. The conflicting assertion source in tests/rings/test_completion_inverse_system.sage now states separately that completion_ideal has the source ambient ring and ideal_of_definition has the completed ambient ring. The four existing target-ideal assertions and FormalSpectrum's explicit (R,I) data retain their meaning.

**Separating actual data:** for R=Z_2[t] and A=Z_2[[t]], the selected source ideal is (t) in R, the selected target ideal is (t) in A and the maximal ideal is (2,t) in A. The element 2 is in the last ideal and not in the selected target ideal. A is complete for both relevant topologies; this does not identify the ideals or topologies. The concrete selected-completion supplier preserves (t) even after Complete placement is present. The coordinated Local producer supplies the constant-coefficient residue followed by reduction modulo 2 independently of whether its general maximal-ideal computation is available.

**Independent witness at the new common home:** the existing Fields edge reaches Local.Complete. A field K has maximal ideal zero, and K/(0)^n is the constant inverse system K with identity transitions. Native owned QQ and GF(p) use the ordinary _OwnedRingParent construction. The independently closed Fields pass now consolidates its former public residue overrides at common Local: absent selected quotient data, the existing LocalRingConstruction retains the lazy actual zero ideal, literal K and explicit OwnedRings().Mor(K,K) identity. Existing selected residue data win unchanged. The Complete hook and common accessor return the actual target zero ideal on this independent construction; no completion_source or completion_map is invented on the native field.

**True closure assertions under T (unexecuted):**

1. The owned 2-adic example retains its original integer source, source ideal (2), completion map and source finite quotients. Its target defining ideal is the actual extension in that literal completed ring.
2. Every supplied ideal_of_definition has the accessor's literal ring as ambient ring. A source ideal from another ring is not accepted as a target ideal.
3. The Z_2[[t]] source, selected target and maximal ideals remain distinct as above, independent of accessor order and Complete placement. Precision refinement retains the original source ideal.
4. The source ideal extension uses the same cached construction and map; it neither recurses into the common accessor nor replaces unavailable selected data by a different topology.
5. Native QQ and GF(p) are complete-local through their zero maximal ideals, and their existing field-specific ideal and residue methods supply the independent common Adic witness.
6. The actual fixed Mor inherits RingMorphism, keeps literal endpoint identity and ordinary ring-map composition, and adds no unproved continuity or local-map condition.

**Retained computation frontier:** a general source ideal's target extension may still require an unavailable algorithm. An actual complete-local datum is not a generic completion solver, a finite-precision exactness theorem or a presentation of arbitrary inverse limits. Those existing selected-completion and ideal-owner questions remain in their own passes. No new prerequisite or category owner was added for this repair.

**Source evidence and phase:** the complete refinement body, its 20 authored ancestor definitions, hook precedence, actual field constructors and direct value suppliers, full selected-completion source and every affected caller, Local producers and the actual Mor dispatch were read. The coordinated changes are committed in 05056101fb; post-commit stdlib AST parsing passed exactly its three changed Python files. No Sage, project import or runtime assertion was run during M1/DEV-58.

### Whole-category placement: `OwnedRings.Commutative.Local` (2026-10-11; source pass closed)

**Closed independent owner pass: `placement-owner-ownedrings-commutative-local`.** A commutative local ring has one proper maximal ideal m, its residue field R/m and the quotient map. These operations need no chosen localization source. This convention excludes the zero ring and requires no domain, Noetherian, Artinian, complete, finite, enumerable or finite-generation hypothesis. The Complete child's body has its own independent owner pass.

| Introduction (all nine) | Definition and disposition |
| --- | --- |
| `_repr_object_names` | Retain the presentation of this local-ring category. |
| `an_object` | Retain the actual owned Z_(2), which is local and nonzero. |
| `extra_super_categories` | Retain Nontrivial: a proper maximal ideal implies 1 != 0. |
| `SubcategoryMethods.Complete` | Retain the complete-local property refinement `_with_axiom("Complete")`; this does not compute a ring's completion. |
| `local_ring_construction` | Read the selected existing local datum, with an explicit missing-data assertion. |
| `maximal_ideal` | Return the selected unique maximal ideal as an actual ideal of this literal ring. |
| `residue_field` | Return the selected residue field with its actual parent. |
| `residue_map` | Return the selected unital quotient with literal endpoints R -> R/m. |
| `_field_decision` | Forward the actual maximal ideal's zero predicate. Missing selected/owned data uses the inherited decision; an undecided result stays undecided. |

**Complete strict authored up-set (18 owners):** OwnedRings.Commutative; OwnedRings.Nontrivial; OwnedRings; OwnedSemirings; OwnedRngs; Monoids; Semigroups; Magmas.Unital; Magmas.Commutative; Magmas; AdditiveGroups.AdditiveCommutative; AdditiveGroups; AdditiveMonoids; AdditiveSemigroups; AdditiveMagmas.AdditiveCommutative; AdditiveMagmas; Sets; Objects. The actual definitions are the unital commutative ring and nontrivial property, its semiring/rng structures, associative/unital/commutative multiplicative operations, the additive group/monoid/semigroup/magma structures, and the underlying set/root, as stated in the Prime up-set table below. The Local declaration adds Nontrivial to its commutative-ring axiom base. None of these strict ancestors uniformly selects a unique maximal ideal and residue quotient. No operation moves to a weaker owner in this pass.

**Delivered arrows:** Local declares no element arithmetic, Mor family or arrow provider. CategoryWithAxiom and the packet's semantic-supercategory traversal reach the existing RingMorCategoryConstruction through both ring branches. The fixed-Mor selector preserves endpoint objects, deduplicates by identity and reuses the compatible RingMor; its generated arrows inherit the actual RingMorphism provider. These are unital ring maps between local rings. The map Z_(2) -> QQ is admitted although it sends the nonunit 2 to a unit; no residue-field functor on every such arrow or extra local-homomorphism condition is asserted. The repaired residue suppliers explicitly use OwnedRings().Mor(A,kappa), with RingMorphism's literal endpoint composition.

**Concrete supplier correction:** `_maximal_ideal_over_local_base` formerly returned GeneratedIdealView, a ring/generator tuple view rather than an owned ideal or module subobject. Both its formal-series and dual-number consumers now use existing actual ideal constructions. GeneratedIdealView's legacy input adapter and exports remain available; the local-data producers no longer present that view as a maximal ideal. No generator is removed by Boolean conversion of an undecided zero predicate.

For A=R[[t_1,...,t_n]], the supplier retains P=R[t_1,...,t_n], its actual coefficient map R -> P, the selected completion map lambda:P -> A and each parameter's exact P expression. It forms mP+(t) as an owned source ideal and extends it along lambda. In the Noetherian regime the existing flat base-change construction transports the ideal's presentation and actual inclusion. Principal and zero ideals use that same transport; they do not re-enter a target-series syzygy computation. Inclusion coordinates use the source module's labels, which correctly handles a zero ideal with an empty frame and a retained ideal-generator family (0).

For D=R[e]/(e^2), the constructor now retains the actual owned polynomial source P and ideal (e^2); only its private native quotient construction lowers that ideal. Its native element constructor retains the actual P representative required by QuotientRings.ElementMethods.lift. Scalar ingress, basis images and arithmetic results enter through that element class, so there is still only one public quotient-lift operation. The maximal ideal uses the existing ordered augmented source-relation construction, with its actual source preimage and inclusion into D.regular_module. A source ideal inclusion is not transported as injective across this nonflat quotient.

Both constructors retain the actual residue map given by constant coefficient followed by R.residue_map(). The maximal-ideal factory is independent of that map. Thus a supplied residue map remains available when an arbitrary source ideal/presentation calculation is unavailable. The Adic residue accessor now reads this supplied local quotient before its maximal-source-ideal specialization, so Z_2[[t]] is not rejected merely because its chosen source ideal (t) is nonmaximal.

**Required companions at existing owners:** the ring-arrow flat-extension shortcut now requires the literal retained canonical completion map and a Noetherian source. An arbitrary map into a completion does not acquire flatness from its target. This is the exact hypothesis of [Stacks Tag 00MB](https://stacks.math.columbia.edu/tag/00MB). The coordinated adic-data correction distinguishes the source ideal I from its target extension I*A and the target maximal ideal. It updates every source-I consumer and the one conflicting existing assertion source. The Complete and common Adic owner reviews close independently; these companion edits alone do not close their nodes or the RingMor, Fields or AdicCompletions passes.

**True closure assertions under T (unexecuted):**

1. Local.an_object is the existing Z_(2); its actual maximal ideal is the extension of (2), contains 2, excludes 1 and is nonzero. The supplied local field decision is False.
2. After the independently closed Fields consolidation, an owned field with no selected local datum obtains the canonical cached LocalRingConstruction at this common owner: a lazy actual zero maximal ideal, literal residue field itself and the explicit RingMor identity. An actual supplied field residue model and map retain their identities instead. Reading the residue field or map does not compute the ideal.
3. An actual maximal ideal with an undecided zero predicate gives that same undecided local field result. Missing selected data retains the inherited proposition or the required accessor's named computation assertion.
4. The repaired QQ dual numbers retain an owned defining ideal in the literal QQ[e], the projection QQ[e] -> D, source representatives for every produced element, and an actual maximal-ideal subobject generated by e. Its residue map sends a+be to a, and D is not a domain.
5. For QQ[[t]], the actual maximal ideal is the flat extension of (t), with its target inclusion and transported presentation. The residue map sends t to zero and every coefficient to itself.
6. The existing Z_2[[t]] construction retains the residue of the constant coefficient. Its maximal ideal remains the actual (2,t) source-extension problem and its available computation; the source variable ideal (t) is not substituted for it.
7. Along the actual Noetherian completion map, zero, principal and multigenerator ideals retain their actual transported module presentations. The zero ideal's empty module frame remains empty even if its stored ideal-generator family is (0).
8. For f:k[x] -> k[[t]] with f(x)=0, the ideal extension of (x) is mathematically zero. Since f is not the retained completion arrow, the code uses its ordinary image-ideal route and availability boundary, without asserting an injective rank-one scalar extension.
9. Local.Mor inherits the actual ring-arrow implementation and preserves literal endpoints and composition. It does not impose a local-map condition.
10. Local.Complete() selects the actual complete-local refinement; Local.an_object is not asserted complete. Local excludes the zero ring while admitting nonzero nilpotents, infinite rings and rings with no supplied finite presentation.

**Named computation boundary retained in this owner:** a general local-base source ideal, syzygy or coefficient algorithm may be unavailable. A nonfield localization carrying only a larger computation model must supply the existing exact coefficient-presentation capability before its polynomial ideal computation is used; otherwise the maximal-ideal factory raises its explicit assertion. The retained residue morphism is independent. This pass supplies the correct mathematical result/domain and truthful computation boundary without claiming a general solver or certifying unrelated native element-admission algorithms.

**Source evidence:** the full common Local declaration, LocalRingConstruction, the original field overrides (now consolidated by the independent Fields pass), the actual formal and dual constructors, quotient element ingress, the ordered quotient-ideal and flat-extension owners, and every helper/adic-ideal caller were read. The category-packet, fixed-Mor, generated-arrow, axiom/join and complete ring-spine sources establish the stated inheritance. The source/data changes are reviewed; all execution assertions remain under T and core-usability-session during M1/DEV-58.

### Whole-category placement: `LocalizationRings.Local` (2026-10-11; source pass closed)

**Closed independent owner pass: `placement-owner-localizationrings-local`.** Its complete declaration introduces exactly two operations, with no element operations, computation hook, Mor family or arrow provider. Earlier PrimeLocalizations changes were evidence for this review, rather than automatic completion.

An object retains a commutative source R, its selected multiplicative submonoid S, and L = S^-1 R with its canonical map lambda. The Local property gives the target's unique maximal ideal m and residue quotient rho: L -> kappa(m). This property requires a nonzero target, but requires no prime-complement presentation, domain source, field target or Noetherian hypothesis.

| Introduction | Definition and disposition |
| --- | --- |
| `an_object` | Retain the category-specific witness for the general owned inhabitant contract. It constructs the nonzero-element localization of the canonical integers, whose field target is local. ZZ[1/2] would not be a Local witness. |
| `source_residue_map` | Retain the cached ring map rho * lambda: R -> kappa(m). LocalizationRings alone has no distinguished residue quotient; a common Local ring has no selected original source and localization map. No strict ancestor supplies both uniformly. The operation delegates composition to RingMor and adds no duplicate residue-field or localization algorithm. |

**Complete strict authored up-set (20 owners):** LocalizationRings; OwnedRings.Commutative.Local; OwnedRings.Commutative; OwnedRings.Nontrivial; OwnedRings; OwnedSemirings; OwnedRngs; Monoids; Semigroups; Magmas.Unital; Magmas.Commutative; Magmas; AdditiveGroups.AdditiveCommutative; AdditiveGroups; AdditiveMonoids; AdditiveSemigroups; AdditiveMagmas.AdditiveCommutative; AdditiveMagmas; Sets; Objects. Their localization, local, ring, additive, multiplicative and underlying-set definitions were read together and are also stated in the adjacent Prime up-set table. The common Local declaration explicitly implies Nontrivial. The actual axiom/join machinery propagates Local across the localization/field join. PrimeLocalizations and the Complete refinement are not ancestors of this owner.

**Delivered arrows:** the fresh complete `abstract_categories/mor_foundation.py` and the packet/fixed-Mor implementations show that both ancestry branches reuse the ring Mor on the same endpoints. OwnedRings selects RingMorCategoryConstruction, whose RingMor uses RingMorphism as its arrow provider; the generated arrow type inherits that provider as a base. The source-residue arrow itself lies in the fixed ring Mor from the original R to the selected residue field, since R need not be local. RingMorphism composition checks the literal intermediate endpoint and evaluates rho(lambda(r)). It does not substitute an incidental coefficient map or a larger computation field.

**Non-Prime-construction witness and closure assertions under T:** for L = ZZ.fraction_field_localization(), the factory retains the nonzero-element submonoid and obtains this Local refinement from its field placement. It does not select PrimeLocalizations or prime-complement metadata. Mathematically L is canonically ZZ_(0); the distinction is the retained construction data. The inherited field datum gives maximal ideal zero, residue field literally L and explicit RingMor residue identity. Thus `L.source_residue_map()` is literally the cached `L.localization_map()`, with exact endpoints ZZ -> L and value n/1 on an integer n. It preserves one, addition and multiplication; it is not asserted to be surjective.

The prime-spectrum consumer still obtains R -> kappa(p) by this inherited operation. The prime residue supplier builds the source quotient followed by its actual inclusion into Frac(R/p), and the triangle rho * lambda equals that composite. It does not call source_residue_map recursively. At the integer prime (3), the local fraction 1/2 maps to 2. The selected local datum retains independent lazy factories and the method asks for the required residue map through the existing public owner. A missing general residue computation reaches that owner's named assertion. A zero localization has no Local placement. These are source-justified assertions, with no Sage execution or runtime MRO claim.

No code move or repair was necessary. This pass closes on the complete inventory, actual ancestor definitions, weakest sufficient placement, delivered arrow inheritance, exact consumer diagram and retained computation frontiers.

### Whole-category placement: `LocalizationRings` (2026-10-11; source pass closed)

**Closed whole-owner source pass: `placement-owner-localizationrings`.** The complete source category, every introduced operation, all selected computation suppliers and the actual ancestor definitions were reviewed together. Its map/coefficient, predicate/scalar, universal-map, field-decision, fraction equality/admission and cardinality dispositions are now delivered. Its parent `placement-audit` stays open until every owner pass closes. Its 17 authored ancestors are OwnedRings.Commutative, OwnedRings, OwnedSemirings, OwnedRngs, Monoids, Semigroups, Magmas.Unital, Magmas.Commutative, Magmas, AdditiveGroups.AdditiveCommutative, AdditiveGroups, AdditiveMonoids, AdditiveSemigroups, AdditiveMagmas.AdditiveCommutative, AdditiveMagmas, Sets and Objects. Their defining ring, semiring, rng, multiplicative, additive and set structures are stated in the following PrimeLocalizations up-set table. None of these ancestors retains the selected localization source or inverted system. Locality, nontriviality and a field are not uniform hypotheses; LocalizationRings.Local is a descendant. A particular constructor also retains its actual coefficient-algebra placement.

LocalizationRings introduces no Mor family or arrow-method provider. Its uniform arrows inherit the existing fixed RingMor. Its ring-map constructors are object operations requiring selected source/submonoid data; the incidental algebra placement of an object does not turn their elementwise callbacks into algebra-generator images.

#### Category and element operations

| Introduced operation(s) | Disposition and exact owner reasoning |
| --- | --- |
| `an_object`, `super_categories` | Retain. They provide the construction category's example and its forgetful edge. The ordinary example `ZZ[1/2]` does not imply Local placement. |
| `Local.an_object`, `Local.ParentMethods.source_residue_map` | These belong to the distinct nested owner `LocalizationRings.Local`. Its own complete pass, `placement-owner-localizationrings-local`, is recorded above; the parent-owner review itself did not close it. |
| Element `__init__`, `numerator`, `denominator` | Retain as the exact selected fraction representation. A bare ring, set, or monoid does not select this source/denominator data. |
| Element `_add_`, `_mul_`, `_neg_` | Retain as the representation's implementations of inherited additive and multiplicative laws. The laws belong to the weaker additive-group and magma owners; these functions compute those laws on actual fractions. |
| Element `__mul__` | **Removed.** The actual factories use the category-generated CommutativeRingElement; the retained `_engine_ring` is data and is not an `_object_of` engine-class insertion. Native Element multiplication selects `_mul_` for a common parent and the coercion model's registered action before mixed-parent coercion. Modules registers both scalar actions over a commutative base. Thus the general ring/module interaction inherits its existing operator and action owners. The separate native ring-element ingress override is untouched. |
| Element `_unit_decision`, `_unit_inverse_decision` | Retain as suppliers of the Monoids contracts. A fraction is a unit exactly when its source numerator becomes an admissible denominator; both questions now share the actual source-ideal/submonoid predicate. The optional inverse computation reads a retained model only after the unit predicate is proved. A larger model never supplies the unit decision. |
| Element `__truediv__` | Already delegates directly to `Monoids.ElementMethods.divide_by_unit`; no new division algorithm is introduced. |
| Element `equality_status`, `_richcmp_` and parent `_fraction_equality_status` | **Consolidated at LocalizedModules.** After a proved source cross-product equality shortcut, the rank-one source regular module sends `a/s` to `(a*e)/s` under the actual localization functor; this preserves and reflects equality. Both images use the ordinary module fraction constructor. The module owner retains its selected annihilator, finite-orbit and domain/torsion-free cases, and reuses localized zero-ideal membership for finite stored free coordinates over an exact source presentation. A source coefficient proved to be plus or minus one settles the zero-annihilator case before constructing a localized ideal, preventing recursion. Same-parent comparison and inequality preserve owned propositions. |
| Element `_repr_` | Retain the selected fraction display. It abbreviates denominator one only when that equality is literally True; an undecided denominator equality remains in the full fraction display. |

#### Parent operations and selected computation suppliers

| Introduced operation(s) | Disposition and exact owner reasoning |
| --- | --- |
| Parent `__init__`, `_derived_construction_parameters` | Retain the construction of the exact source, submonoid, fraction representation, and actual algebra action. The derived `base_ring` remains supplied by this constructor. |
| `algebra_base_ring` | **Removed by the bounded patch.** The constructor computes the same selected coefficient base locally, uses it for the actual algebra category join, and passes it to Modules. The inherited Algebras accessor reads that exact stored module base. The duplicate `_localization_algebra_source` storage is unnecessary for the accessor. |
| `cardinality` | **Moved to the existing Sets owner.** LocalizationRings supplies `_cardinality_decision`: zero in S gives cardinal one; a domain with zero excluded transports its actual source's optional cardinal; an undecided predicate leaves the existing owner fallback. Finite domains are already fields; for an infinite domain the canonical injection and fraction representatives give the matching cardinal bounds. Standard Set formulas and the actual ring/algebra/module suppliers now use the same existing hook, preserving finite images, decided predicate subsets, formal series, free and presented modules, scalar restriction and the concrete real continuum supplier. |
| `inverted_submonoid_meets` | Retain as the predicate for the selected inverted S and an ideal of the actual source R. Existing callers are localized-module equality/zero predicates, localized-ideal membership and contraction, and normalization component survival. The generic submonoid owner selects S but has no existing general ideal-intersection decision interface; finite-set intersection cannot replace this computation. |
| `_selected_engine_ring`, `_engine_element`, `_from_engine_element` | Retain the selected ring realization crossings. The model supplier returns None when absent; existing optional unit/cardinality/presentation consumers preserve that absence, while the required `_engine_ring` adapter asserts at its named frontier. A model larger than the actual localization supplies no substitute membership, unit or cardinality predicate. Exact self-realized field/PID matrix computations retain their prior route; only distinct engines are checked against native categories. |
| `localization_functor`, `localize_module` | Retain as constructions from this exact localization map and submonoid. General scalar extension already belongs to Modules; ModuleLocalizationFunctor specializes it with fraction representations, exactness, and retained localized subobject maps. Merely substituting the generic tensor construction would discard this selected realization. |
| `_normalization_data`, `_normality_decision` | Already correctly placed as specialized suppliers of the public commutative-ring normalization and normality owners. The selected transport requires an actual finite presentation of the normalization module, a chosen finite ordered component family, and a finite chosen inverted family. It does not infer finite normalization for an arbitrary ring. |
| `_valid_denominator`, `fraction` | Retain construction at the source/submonoid owner. Admission asks whether the source principal ideal meets S, with selected positive witnesses and owned negation for prime/nonzero systems. Arbitrary predicate membership alone does not decide the saturation. True constructs; False and an undecided predicate reject this stated denominator with distinct explanations. Neither rejection asserts that the value has no other admissible representation. |
| `_element_constructor_`, `__call__`, `is_parent_of`, `__contains__` | Retain representation ingress and supply the existing Sets membership predicate. Literal elements, admitted unformed-module wrappers and source elements retain their positive routes. A tuple requests its exact numerator/denominator representation. A value of the actual Frac(R), verified against its canonical source map, belongs exactly when its numerator lies in the localized denominator ideal; the existing ideal owner computes this criterion. Unrecognized owned endpoints and undecided comparisons retain the actual localization-membership proposition. Python containment is only the Boolean boundary. The constructor does not invent a new denominator witness. |
| `_inverse_variable_engine_cover` | Retain as the one private gate shared by the old decoder and exact-coefficient capability. It inspects immutable selected source/engine layout; it is not a public category predicate. |
| `_has_selected_exact_coefficient_presentation`, `_exact_coefficient_presentation_ring`, `_exact_coefficient_presentation_relations`, `_lift_coefficient_to_presentation`, `_descend_coefficient_from_presentation` | Retain as suppliers of the existing ring-owner coefficient-presentation contract. The admitted finite first-level quotient presentation is exact; prime/fraction-field models, unsupported decoder layouts, flattened towers and all-unit engine reuse remain excluded. No additional module algorithm or presentation layer is introduced. |
| `zero`, `one` | Retain as the actual fraction representations supplying the inherited additive identity and multiplicative unit contracts. They are required instance data, not new mathematical operations. |
| Parent `_repr_` | Retain as display of the selected construction. |
| `localization_source`, `localization_submonoid` | Retain as authoritative defining-data accessors. No weaker ancestor selects these data. |
| `is_fraction_field_localization`, `_has_selected_nonzero_element_submonoid` | **Public predicate repaired; selected-data guard separated.** A domain-source localization is canonically its fraction field exactly when its actual target is a field. The public conjunction preserves unknown propositions. The declared guard reads only the retained nonzero-element tag for the five existing computation consumers; a true mathematical predicate does not invent their selected comparison data. The zero-prime example separates mathematics from presentation. ZZ[1/2]'s negative decision is now supplied by the finite-integer-module theorem below. |
| `_field_decision` | Supply the existing ring-owner field predicate for selected finite-generator localizations of finite free integer algebras. Torsion-freeness and finite type over the Jacobson ring ZZ prove the target is not a field, including the zero case. The property guard requires no chosen basis and no domain assumption. Cooperative fallback preserves the common Local supplier for predicate submonoids. |
| `fraction_field_realization`, `fraction_field_comparison`, `fraction_field_comparison_inverse` | Retain at the selected localization owner: they read the retained owned field and its exact fraction correspondence. **The patch chooses explicit RingMor for both maps and describes guard failures as unavailable selected presentations, not nonexistence of ring maps.** |
| `inverted_elements` | Retain as the chosen-generator accessor through the submonoid. An arbitrary predicate presentation has no selected generating family, and the existing submonoid accessor reports that boundary. This is not a finiteness assertion for every localization. |
| `inverted_element` | Retain as a query for the selected singleton generating family. Every element admits a power-denominator expression, but a stored denominator need only become a unit: 2 is allowed for 1/2 in ZZ[1/6]. The documentation now distinguishes these facts. A finite family also gives a principal localization through its product, but this accessor selects no new singleton or rewriting. |
| `quotient_contraction_map`, `_quotient_contraction_map_decision` | Retain at this localization owner. They need the actual quotient of L, contraction along its selected R-to-L map, and the exact source quotient. The public map remains defined mathematically even when the protected computation returns None. |
| `quotient_contraction_isomorphism`, `_finite_quotient_contraction_isomorphism` | Retain. They compare the exact retained quotient diagram and use finiteness of the contracted source quotient as a sufficient invertibility theorem. They do not infer a general equivalence or exact cardinality from finite placement alone. |
| `induced_morphism`, `_induced_morphism_from_unit_images` | Retain at LocalizationRings: the universal map requires the exact source and submonoid plus the global unit-image premise. **Admission repaired and the one evaluator shared.** Public cases establish the premise from selected generators or exact canonical data; residue, saturated-contraction total-quotient and proved-maximal completion producers use the declared protected contract. A predicate presentation alone and successful inversions of some denominators do not establish a ring arrow. Unavailable unit-image or nonmaximal completion algorithms are named without denying the mathematical construction. |
| `localization_map` | Retain as the selected construction's canonical R-to-L ring map. It already chooses explicit ring Mor. |
| `restriction_to` | Retain as the comparison over a common source, or the next step in the retained localization tower. **The patch constructs explicit RingMor, replaces the prime-containment Boolean reduction by conjunction, and separates True/False/undecided applicability.** It also states the correct generalization direction on spectra and selected-family boundary. |
| `localization_fraction_data` | Retain as the selected correspondence returning a numerator and denominator in the actual retained source. Existing consumers use it for scalar action, contraction comparisons and localization-tower descent. |

All introduced operations, the 17 authored ancestors and actual RingMor inheritance are now accounted for. Independent source review covers the equality/admission repair and the complete cardinality producer/caller changes. The existing participant-hook mechanism preserves ExactRealField's concrete continuum supplier; no refinement implementation, new computation interface or category was added. Required rank/Smith/engine consumers assert explicitly when no result is supplied, and optional transports retain absence. The generic self-realized exact-field elimination still has its existing undecided-pivot frontier; no total rank oracle is claimed.

**Retained closure assertions under T (not executed in M1):**

- For L = ZZ[1/2], the fractions 1/2 and 2/4 are equal, one differs from zero, and the cardinality is aleph_0. Its fraction-field predicate remains False by the delivered finite-integer theorem.
- For L = ZZ_(2), the external owned rational 1/2 does not belong and 1/3 does. In ZZ[1/2], the rational value 3/6 belongs, but the explicitly requested denominator-6 tuple is not admitted.
- For A = QQ[x,y]/(xy), localizing at y kills x, and localizing at the prime (x) also kills x. These equalities use the source ideal mathematics through localized modules. A represented source domain localized at zero becomes the zero ring, receives no domain/PID edge from the factory, and has cardinal one.
- An undecided zero-in-S proposition remains undecided and gives no domain/PID placement. Undecided denominator or localized-coordinate membership never supplies a false negative equality or an admitted fraction.
- A selected finite image with decided repeated values is counted correctly; undecided distinctness supplies no exact count. A predicate subset of a chosen finite set remains finite when membership is undecided, while its optional count is None and its public cardinality reaches its own assertion.
- Outside LocalizationRings, RR and QQ[[t]] have cardinal continuum through Sets; finite positive-rank free QQ modules have cardinal aleph_0 and rank zero has cardinal one. These witness the moved invariant at its weaker owner. The unchanged selected coefficient accessor likewise applies to an ordinary QQ polynomial algebra outside LocalizationRings.
- The selected cyclic ZZ module modulo 6 has cardinal 6; the selected relation row (6,4) gives cardinal 2 by the existing Smith computation. For the actual local PID ZZ_(3), quotient by 3 has cardinal 3 and a unit relation gives cardinal one; a larger QQ model cannot turn the nonunit 3 into a unit of that local ring.
- The canonical comparison, restriction, induced, residue and quotient-contraction arrows retain their exact RingMor endpoints and their recorded defining equations. The already recorded nonmaximal-completion separator remains required.

**Named computation frontiers retained at their owners:** an arbitrary field decision, nonmaximal completion construction, unselected fraction-field comparison, missing source ideal/kernel/presentation algorithm, unknown saturation, or undecided generic elimination pivot remains an explicit unavailable computation. This whole placement pass establishes the mathematical domain, owner and truthful behavior at those boundaries; it does not assert that every general computation is implemented. All runtime acceptance remains in T and `core-usability-session`. The Local refinement has its own independent completed pass above.



### Whole-category placement: `PrimeLocalizations` (2026-10-10)

**Closed source pass.** The category selects a commutative ring R, a prime ideal p, and the localization R_p at R minus p. All introduced object and element operations were judged together with the actual declared ancestors and arrow inheritance. The explicit edge now reaches LocalizationRings.Local, an existing axiom refinement whose method provider is materialized here. The owned axiom/join construction already supplied this intersection; no new axiom or recognition procedure is added.

The complete authored up-set was read from current declarations, including the existing local-localization refinement now carrying its provider. It contains 21 ancestors: LocalizationRings.Local; LocalizationRings; OwnedRings.Commutative.Local; OwnedRings.Commutative; OwnedRings.Nontrivial; OwnedRings; OwnedSemirings; OwnedRngs; Monoids; Semigroups; Magmas.Unital; Magmas.Commutative; Magmas; AdditiveGroups.AdditiveCommutative; AdditiveGroups; AdditiveMonoids; AdditiveSemigroups; AdditiveMagmas.AdditiveCommutative; AdditiveMagmas; Sets; Objects. Owned axiom propagation supplies their property meets; this is a source-declared inventory, not a claimed live C3 rendering.

| Up-set categories | Defining data relevant to placement |
| --- | --- |
| LocalizationRings.Local; LocalizationRings | A commutative localization with its exact source, multiplicative submonoid and map; the Local refinement also requires a local target. |
| OwnedRings.Commutative.Local; OwnedRings.Commutative; OwnedRings.Nontrivial; OwnedRings | Respectively a unique maximal ideal, commutative multiplication, 0 != 1, and a unital associative ring with additive abelian-group structure. |
| OwnedSemirings; OwnedRngs | A unital semiring supplies additive and multiplicative monoids with distributivity and absorbing zero; a rng supplies additive inverses and associative distributive multiplication without requiring one. |
| Monoids; Semigroups; Magmas.Unital; Magmas.Commutative; Magmas | Respectively associative multiplication with identity, associative multiplication, a unit, commutative multiplication, or an arbitrary binary operation. |
| AdditiveGroups.AdditiveCommutative; AdditiveGroups; AdditiveMonoids; AdditiveSemigroups; AdditiveMagmas.AdditiveCommutative; AdditiveMagmas | Respectively an abelian group, a group written additively, an additive monoid, an associative additive operation, a commutative additive operation, or an arbitrary additive operation. |
| Sets; Objects | An underlying set, then an object without the foregoing operations or selected localization data. |

| Introduction | Definition and disposition |
| --- | --- |
| `maximal_ideal` | The unique maximal ideal of a local ring; inherit OwnedRings.Commutative.Local. The Prime supplier retains the actual extension pR_p. |
| `residue_field` | The quotient of a local ring by its maximal ideal; inherit the same Local owner. The Prime supplier computes Frac(R/p), or the literal R/p when already a field. |
| `residue_map` | The quotient map with that maximal ideal as kernel; inherit the Local owner. The Prime supplier induces it from R -> R/p -> Frac(R/p). |
| `source_residue_map` | Compose the selected localization map with the residue map of its local target. It requires a selected localization and a local target, so belongs to LocalizationRings.Local, beyond prime-complement presentations. |
| `localized_prime` | Read the actual prime selected by the prime-complement construction. Retained at PrimeLocalizations; an arbitrary local ring or localization does not select this datum. |
| `localize_module` | Apply the selected localization functor to a module over the retained source. The identical Prime implementation is deleted in favor of LocalizationRings. |
| `fraction_field` | Localize an integral domain at its nonzero elements; move the generic method beside the existing domain fraction-field localization and map. Delete the obsolete Prime field slot and override. Integral domains are not a uniform ancestor of prime localizations. |
| Unit predicate and inverse realization | Public invertibility stays at Monoids. The generic localization hook already implements the prime-complement predicate, so delete the duplicate. Retain the Prime inverse calculation a/s -> s/a once its numerator is proved outside p. |
| Intrinsic dimension realization | dim(R_p) is the supremum of lengths of prime chains inside p. The dimension-difference calculation now requires a represented source domain and the actual PID or finite-type-over-a-field hypothesis. Unsupported cases name the missing intrinsic computation and never use the larger fraction-field model's dimension. |
| Local construction supplier | Reuse LocalRingConstruction with independently cached fixed factories for its three existing values. Its creation and maximal-ideal accessor do not force a residue-field computation. The common Local field hook asks whether the actual owned maximal ideal is zero and retains undecided propositions. Legacy installed ideal views keep their inherited hook. |
| Parent/category construction and specimen | Retain the selected source, submonoid, coefficient data and optional computation field; remove only the redundant stored fraction-field result. The Prime specimen remains ZZ_(2). The new Local refinement's specimen is the existing nonzero-element localization of ZZ. |
| Arrow operations | Neither PrimeLocalizations nor the Local refinement introduces an arrow type or arrow operation. Their Mor-family walk reaches the same fixed RingMor through both branches; identity deduplication retains its actual inheritance. |

For q:R->R/p, j:R/p->K=Frac(R/p), and lambda:R->R_p, the selected residue map rho has rho(a/s)=j(q(a))/j(q(s)), kernel pR_p, and rho*lambda=j*q. The residue-map factory constructs j*q directly; it never calls source_residue_map recursively. Existing completion and dual-number installation callers retain non-None maximal ideals/residue fields and their optional absent residue map. These source assertions use the usual [local-ring and residue-field construction](https://stacks.math.columbia.edu/tag/07BH).

**Witness outside PrimeLocalizations:** L=ZZ.fraction_field_localization() retains the nonzero-element submonoid and already selects field placement. Owned axiom propagation puts it in LocalizationRings.Local. Its residue field is literally L, its residue map is the explicit RingMor identity, and composing that identity after localization_map returns the original ZZ->L arrow. Both this field residue identity and the field branch of fraction_field_map now explicitly select OwnedRings().Mor(self,self); an unqualified algebra Mor could demand finitely many module generators over ZZ.

**Retained computations and limits:** the native field model of an already represented source domain remains available, but reducibility of R no longer asserts nonexistence of a fraction field for R_p. In k[x,y]/(xy) at (x), y is inverted and annihilates (x), so the actual maximal ideal vanishes. The common Local predicate follows that owned ideal rather than an ideal in a larger computation field. Its represented finite route uses the existing localized annihilator criterion; undecided propositions and unsupported ideal computations retain their frontier. Finite polynomial constructors explicitly select FinitelyGeneratedAsAlgebra for finite variable labels, so the tightened dimension guard preserves those admitted cases.

General recognition of domains obtained by localizing reducible sources, general local recognition for finite localizations, unpresented-ideal annihilator computations, and intrinsic dimension outside the stated hypotheses remain inside the existing placement node. The full category survey remains open. No prerequisite node or edge is added, and the completed Step-3 denominator stays 18. All separating assertions are retained under core-usability-session/T; no Sage/runtime execution is claimed. The next category pass has started at LocalizationRings itself.

### Whole-category placement: `QuotientRings` (2026-10-10)

All introduced object and element operations were reviewed together with the actual up-set. `QuotientRings` carries a commutative ring plus a selected presentation `P -> P/I`. Its declared chain reaches `OwnedRings.Commutative`, then `OwnedRings`, whose unital-semiring and rng branches reach `Monoids`, `AdditiveGroups`, their weaker operation spines, and `Sets`. These supply, respectively, commutative ideal/spectrum mathematics; unital-ring operations; zero/one/addition for characteristic; multiplication/identity for units; addition/inverse for subtraction; and underlying-set cardinality. No new supercategory edge was invented.

| Introductions on the selected quotient | Mathematical definition and disposition |
| --- | --- |
| `lift`, `representative`, element constructor and display | A chosen representative in `P` is data of this presentation. Retained at `QuotientRings`. |
| `_add_`, `_mul_`, `_neg_`, `_richcmp_` | Realize class arithmetic and equality `a-b in I`. Retained primitives; duplicate parent comparison removed and inequality preserves propositions. |
| `_sub_` | Right difference `a + (-b)` needs only an additive group. The common `AdditiveGroups.ElementMethods` implementation is inherited. |
| `is_unit`, `inverse_of_unit`, unit division | Two-sided invertibility and its unique inverse belong to `Monoids`. Existing native, quotient, localization, prime-localization, completion and real computations fulfil declared realization hooks. `divide_by_unit` owns the same-parent formula; quotient and localization `/` bind that descriptor. Native division that enlarges its result parent retains its distinct implementation. |
| Parent constructor, coercion/engine ingress, `zero`, `one`, `an_element` | Retained selected quotient realization and inherited identity/specimen implementations. The parent owns its private unit-inverse calculation and returns an element in the exact quotient. |
| `_is_zero_ring`, `_finiteness_decision`, field/domain/reducedness decisions | Retained property realizations. Zero-ring detection uses membership of one in the actual defining ideal. Localized-source predicates do not infer facts from a larger fraction-field model. |
| `cardinality` | A set invariant. Quotient algorithms now supply the existing `Sets._cardinality_decision`; an unsupported computation leaves the shared owner to its other cases. |
| `characteristic` | The generator of the natural-number zero fibre is defined for semirings (Mathlib `Algebra/CharP/Defs`, `ringChar`). Public ownership is `OwnedSemirings`, with owned integer results. Zero rings have characteristic one; the integer-ideal calculation uses its canonical full-ideal generator. An actual nonzero field quotient inherits its field's characteristic; a field used only as a source computation model does not supply this datum. |
| `krull_dimension` | Supremum of prime-chain lengths belongs to commutative rings. Quotient, field and prime-localization calculations now fulfil its declared hook. |
| `algebra_base_ring` | Inherited from the actual `Algebras(P)` construction and its selected base ring. The duplicate quotient getter is removed. |
| `quotient_source`, `defining_ideal`, `quotient_map` | Retained exact presentation data and projection. |
| `_module_basis_along` | Retained selected quotient power basis along its exact coefficient map, under the existing protected module-basis contract. |
| `localization_comparison`, `completion_comparison` | Their diagrams use the selected quotient presentation; retained at that owner with the existing localization and Noetherian-completion hypotheses. |
| `prime_ideal_locus`, `minimal_prime_locus`, `irreducible_component_locus` | General commutative-ring definitions using the full power set and `p -> V(p)`. Moved together without finite-generation or enumeration assumptions (Stacks `00ER`). |
| `minimal_primes`, `irreducible_components`, `_presentation_minimal_primes` | Public selection belongs to commutative rings. Exact Noetherian quotient computations remain private; upstairs primes are transported to the quotient. Component domains exist for nonreduced rings too. Localized presentations without exact ideal transport use the general loci. |
| `total_quotient_ring`, `total_quotient_map` | Localization at regular elements belongs to commutative rings. One cached arrow retains its target; domains use their fraction-field map and the zero ring its identity. The finite reduced quotient calculation uses the product of component fields (Stacks `02LV`, `035P`), with a direct one-factor image. The native product owner now derives commutative/Noetherian/Artinian/finite placement from its actual factors, without declaring products of fields to be fields or domains. |
| `is_normal` | The local-normal-domain predicate belongs to commutative rings (Stacks `037B`). The finite affine algorithm supplies a decision only with its actual field base; otherwise the proposition remains. |
| `_affine_normalization_data`, `normalization`, `normalization_map`, `normalization_components`, `conductor_ideal`, `delta_invariant` | The finite affine computation now fulfils the declared common normalization contract. Four public operations have moved to commutative rings; delta has moved to the commutative unital algebra owner and uses the retained field map. The original quotient, reduction factorization, normalization module, component maps and exact coefficient action survive. General computation remainders remain in the existing normalization node. |
| Arrow operations | `QuotientRings` introduces no separate arrow type. Its actual up-set reaches the existing ring Mor; quotient-arrow equality already uses the retained projection. That inheritance is preserved. |

**Retained required work:** the named exact-localized-quotient source piece has closed, with its broader algorithm remainder still recorded in that node. The five normalization introductions and the finite affine construction are delivered; their broader computation remainder stays in `normalization-extensions-retain-coefficients`, directly required by the open M1 architecture node. The full normalization family, conductor, component maps and chosen coefficient action remain required there. The wider category survey remains inside the existing placement node. The separate existing `quotient-ring-placement-follows-construction` obligation still owns eager primality/dimension calculations during quotient construction; this pass does not mark it complete.

**Source evidence and phase:** current owner source, the retained survey files and primary mathematical definitions were reviewed. All separating assertions are under `core-usability-session` or the two prerequisite nodes. No Sage, test suite, notebook or QC execution is claimed during M1/`DEV-58`. The stale general-minimal-prime paragraph in TODO is reconciled with the delivered full-power-set loci, preserving its original mathematical assertions under T.

**Step-3 follow-through:** `49407e4b5d` removes a Python-hashability assumption from Čech incidence, and `998b290927` makes the indexed-family cache handle a tuple containing an unhashable label. Both retain original labels. These are corrections on the promoted route; the completed 18-row survey denominator is unchanged. `a6f1377408` removes the orphan dependency on the finite-cardinal conversion retired by `00abc78e95`, while retaining its two exact assertions under T.

**Nonidentity well-order Mor composition checked (2026-10-10):** For the selected monotone inclusion `Δ[1] -> Δ[2]` followed by a nonidentity monotone endomorphism of `Δ[2]`, focused Sage verifies the composite lies in the exact `WellOrderedSets().Mor(Δ[1],Δ[2])`, its underlying set arrow retains both endpoints, and its values are `(2,2)`. Ingress of the reverse-order map is rejected. This closes the adjacent finite-Mor expression inspection without conflating ordinary order-preserving arrows with core isomorphisms.
**Infinite well-order and core Mor placement verified (2026-10-10):** The existing natural-number object `NN` belongs to `WellOrderedSets` and `TotallyOrderedSets`; its selected ranking has order type `omega(0)`. The order-type functor is defined on the *core* of well-ordered sets, not on arbitrary order-preserving morphisms. Focused Sage confirms that the selected inverse-pair identity in `WellOrderedSets().Core().Mor(NN,NN)` maps to the identity of its ordinal, while an ordinary Mor identity is not a valid input to that functor. The executable owner specimen records this precise Mor-category distinction; no source-category placement change is warranted.
**Infinite componentwise product/coproduct morphisms (2026-10-10):** The generic set product and coproduct componentwise-morphism owners now accept a selected `NaturalTransformation` of set-valued diagrams on their exact infinite discrete index category. Both compare the functor's actual source/target factor objects before applying each selected component; finite component callbacks retain their existing exact Mor-parent checks, whereas untyped infinite callbacks remain rejected. Focused Sage verifies maps on the genuine `NN`-indexed singleton product/coproduct at indices 0, 1 and 5, including their owned Mor parents and projection/injection equations. The construction is execution evidence and does not certify arbitrary natural transformations independently of their formal mathematical owner.
**Componentwise Cartesian-product functor arrow placement corrected (2026-10-10):** `_cartesian_product_morphism` now checks each finite-index component against the exact `Sets().Mor(source.factor(i),target.factor(i))` before constructing the induced map. The focused Sage regression checks both components on a nonidentity point, rejects a wrong target factor, and retains the public binary product-functor transposition specimen. Infinite component callbacks do not become typed families by being supplied to this construction.
**Componentwise coproduct functor arrow placement corrected (2026-10-10):** The binary set-coproduct functor's `_coproduct_morphism` now validates every component against its exact `Sets().Mor(source.cofactor(i),target.cofactor(i))` and retains the indexed injections. Focused Sage checks both injection naturality squares for a nonidentity pair of maps and rejects a component supplied with the wrong source. An infinite callback is not treated as a typed component family. The existing binary coproduct functor still constructs a five-point source and target in the positive specimen.
**Infinite coproduct universal map through a selected transformation (2026-10-10):** `CoproductsOfSets.from_maps` accepts an actual `NaturalTransformation` from the indexed set-valued diagram to the constant target diagram when its index category, codomain and target are exact. Components are evaluated via the existing natural-transformation owner, which checks each selected arrow at its actual index; the induced set morphism satisfies the injection equation at indices 0, 1 and 5 for a genuine `NN`-indexed singleton coproduct. An invalid component from a two-point source is rejected on evaluation. An arbitrary callback is still rejected. This is local construction evidence, not a claim that unchecked callback families are globally certified.
**Infinite coproduct map admission regression (2026-10-10):** A constant `NN`-indexed coproduct of singleton sets now refuses `from_maps` supplied with an arbitrary callback of component identities: the callback alone is not a selected family of arrows. The focused owner regression tests this refusal alongside the finite case's exact endpoint and injection-triangle checks. The universal map from an infinite coproduct remains mathematically defined and requires its typed-family realization; rejecting untyped callbacks is not a claim that the map is undefined.

**Coproduct induced-map component admission corrected (2026-10-10):** `CoproductsOfSets.from_maps` now checks the actual component maps for a finite indexed coproduct against the exact `Sets().Mor(cofactor,target)` parents before constructing the induced arrow. A focused owner regression verifies the two coproduct-injection triangles and rejects a component with the wrong source. An infinite coproduct no longer accepts an unchecked callback as evidence of a typed family of maps; the categorical family route remains to be constructed.

**Additive product assembly Mor verified (2026-10-10):** For a finite family of additive monoids, `CartesianProductsOfAdditiveMonoids.from_maps` now requires component arrows in their exact `AdditiveMonoids().Mor(source,factor)` parents and returns an arrow in `AdditiveMonoids().Mor(source,product)`. Focused Sage checks the assembled arrow's parent, both projections on the source unit and zero, and rejection of untyped set-map components (`29861e51df`). Infinite component families still require typed morphism-family data, not a callback declaration.

**Constant-family categorical admission repaired (2026-10-10):** `indexed_family(NN, Sets.Δ[1], value_category=AdditiveMonoids())` previously passed a false selected-value-category claim, causing its product to enter `CartesianProductsOfAdditiveMonoids` even though the two-point set is not an additive monoid. The indexed-family owner now checks the actual selected constant object against the declared category before constructing its diagram. Focused Sage verifies rejection of the false claim while both the valid infinite constant additive product and the parity-restricted nonconstant additive product still pass.


**Nonconstant infinite additive product from finite diagram restriction (2026-10-10):** The selected finite functor `DiscreteCategory(Δ[1]) -> AdditiveMonoids` with alternating additive-monoid/additive-group factors has its object images verified at the finite diagram owner. Precomposition by the parity functor `DiscreteCategory(NN) -> DiscreteCategory(Δ[1])` gives a genuine nonconstant infinite family; its product has additive-monoid placement and its odd projection preserves the zero and nontrivial sum (focused Sage). `indexed_family` now follows `RestrictedDiagram.original_diagram()` through nested restrictions and rejects any lineage whose originating `_DiscreteDiagram` has unchecked infinite object images. The checked finite source and the original functor and indexing map remain retained. General nonconstant infinite diagrams from unchecked callbacks remain prohibited.


**Empty discrete-diagram extrema verified (2026-10-10):** For the empty discrete indexing category `DiscreteCategory(Sets.Δ[-1])`, the canonical selected limit in `Sets()` is terminal of cardinality one and the canonical selected colimit is initial of cardinality zero. The focused regression exercises both through `Sets().Limits(index)` and `Sets().Colimits(index)`, retaining the zero-object shape rather than constructing fictitious factor data.


**Selected colimit cocone factorization verified (2026-10-10):** The finite two-object diagram of two- and three-point sets now has its universal colimit checked at the retained categorical owner, `Sets().Colimits(index).construction(diagram)`. Four nontrivial cocones into the two-point set factor through the selected colimit, with both costructure triangles commuting as actual Mor composites through `factor.apex_map()`. The same focused owner test continues to verify the six cone factorizations at the selected limit. No alternate limit/colimit method or algorithm was introduced.


**Finite diagram universal limit/colimit route corrected (2026-10-10):** The existing `Sets().Limits(index).construction(diagram)` and `Sets().Colimits(index).object(diagram)` are the canonical construction owners; the old `diagram.limit()`/`.colimit()` test calls had no such methods. The finite-shape adapter wrongly used the shape's *indexed family* of arrows as a set of indices for its arrow-target product. It now constructs the actual finite ordered set of arrows. Focused Sage on a discrete two-object diagram with two- and three-point values returns limit cardinality six and colimit cardinality five, and checks all six point-apex cones factor with both defining triangles commuting through the selected cone morphism's apex map. The old `Cones().Mor(point)` assertion was invalid because Mor requires source and target cones; it has been replaced by the actual universal factorization comparisons.


**Discrete diagram finite codomain checked at its owner (2026-10-10):** `_DiscreteDiagram` now rejects a family with a different exact index object set and verifies every object image lies in its declared codomain when the index set is provably finite. The focused owner specimen constructs a valid two-index set-valued diagram, rejects a callback returning nonsets, and rejects a family on another finite ordinal. General infinite callback-based diagrams remain unverified and cannot establish product placement; independent typed mathematical families are still required. The older diagram-cone specimen itself fails at the unrelated missing `diagram.limit()` method, so its limit/colimit assertions were not claimed.


**Unchecked infinite diagram codomain rejected (2026-10-10):** The earlier nonconstant `DiscreteCategory(NN) -> AdditiveMonoids` specimen was built by `_DiscreteDiagram` from an arbitrary `IndexedFamily` callback. That constructor does not establish the callback values lie in its codomain; the odd-index return can actually be an ordinary two-point set. `indexed_family` now rejects such an unchecked infinite `_DiscreteDiagram`, even when wrapped in a `Functor`, rather than treating its claimed codomain as mathematical evidence. Focused Sage checks verify rejection of the dishonest diagram and admission of the actual constant functor with additive projection. General nonconstant infinite families still require independently justified typed functors; the previous positive nonconstant assertion is withdrawn.


**Actual selected functor for nonconstant infinite products (2026-10-10):** The indexed-family owner now accepts a preexisting typed `Functor` from `DiscreteCategory(I)` to its actual codomain category, and reads values by applying it to its selected index objects. The product retains precisely this functor through `selected_diagram()` and places it in `CartesianProductsOfAdditiveMonoids` when the selected codomain is a subcategory of `AdditiveMonoids`. Targeted Sage checks alternate an additive monoid and an additive group over `NN`; the resulting product has additive placement, nonconstant sections, a projection in `AdditiveMonoids().Mor` at an odd index, and correct addition/zero after projection. Unsupported raw infinite callbacks declaring a category are still rejected. The mathematical legitimacy of the supplied typed functor belongs to its formal owner; a declaration in this preamble is not independent acceptance evidence.


**Infinite family evidence firewall corrected (2026-10-10):** A supplied Python callback and `value_category=C` do not constitute a mathematical functor into `C` on an infinite index set. The initial selected-diagram code at `768a737e77` incorrectly accepted this self-asserted codomain; a callback returning an ordinary set on odd indices can claim `AdditiveMonoids`. The owner now rejects nonconstant infinite callback/category claims with `TypeError`. Focused Sage confirms rejection of both a homogeneous callback and a dishonest mixed callback, while constant infinite additive products remain admitted and their additive projections pass. A true nonconstant infinite typed functor must be supplied and retained at its categorical owner before this placement can close.


**Infinite constant additive products constructed (2026-10-10):** `indexed_family(NN,A)` now represents the genuinely constant family with selected object `A`, rather than an opaque lambda whose values cannot be proved to lie in one category. `CartesianProductsOfSets` derives additive-monoid placement from that selected value without enumerating the infinite index. Focused Sage owner checks pass for category membership, nonconstant sections, componentwise addition and zero after projection at index two, and nonmonoid constant families receiving no additive placement. General nonconstant infinite families still require a typed functor/category of values; the separate `infinite-index-additive-product-placement` TODO retains that requirement and is not closed.


**Additive-product projection Mor corrected (2026-10-10):** The already selected `CartesianProductsOfAdditiveMonoids` now constructs each factor projection in `AdditiveMonoids().Mor(product,factor)` rather than merely `Sets().Mor`. The actual finite product of two additive monoids retains zero and componentwise addition; a focused Sage owner regression verifies the projection has that exact Mor parent, sends zero to zero and preserves a nonzero doubled element. Infinite-index additive placement still requires the selected value-category family datum under `infinite-index-additive-product-placement`; this finite-arrow correction does not claim its closure.


**Infinite-index additive-product placement defect (2026-10-10):** The finite product of two copies of `AdditiveMonoids().an_object()` lies in both `CartesianProductsOfAdditiveMonoids` and `AdditiveMonoids`; its pointwise zero is a left/right identity for a nonzero section. But `Sets().product(indexed_family(NN, lambda n:A))`, with the same additive monoid `A`, belongs to neither category (focused Sage). Its product constructor presently tests factors only after proving the index finite. This is a real missing result placement, rather than a nonmonoid counterexample. The indexed family has no selected value category for infinite indices; the required typed family and product transport are filed at `infinite-index-additive-product-placement` in TODO.md, with a negative mixed-family case and projection-morphism obligations.


**Well-order arrow and indexed coproduct placement (2026-10-10):** On the three-point ordinal, `WellOrderedSets().Mor(X,X)` admits the nonidentity monotone map `x ↦ min(2,x+1)`, retains it through left/right identity and nonidentity composition, and rejects the order-reversing map `x ↦ 2-x` (focused Sage). This checks a genuine arrow operation in the owned well-order Mor rather than only category membership. The indexed coproduct of `NN` with the two-point ordinal belongs to `EnumeratedCoproductsOfSets()` and has cardinality `aleph0`; its constructor rejects non-set factors. No incorrect placement was found in these inspected paths. The remaining category-wide Mor and operation audit is still open.

**Set exponential and ordered-enumeration placement (2026-10-10):** `FunctionSets()(Y,X)` delegates to the selected `Sets().Mor(X,Y)` owner, which rejects endpoints outside `Sets()`. Its finite-exponent refinement is attached at `SetMorCategory.__init__` rather than by a second exponential construction. `OrderedEnumeratedSets` inherits `WellOrderedSets` through `EnumeratedSets`, hence also `TotallyOrderedSets` and `PartiallyOrderedSets`; an actual finite ordinal has both ordered-category memberships and the inherited order comparison. The constant-family set power `X**n` was checked for `n=0,1,2` on a two-element set, with cardinalities `1,2,4`; its zero-fold index is the empty ordinal `Delta[-1]`. No incorrect mathematical placement was established in these paths. Continue the remaining set constructors and Mor introductions without revisiting these examined edges.

**Finite subset constructor source ownership (2026-10-10):** `FinitePowerSets()(X)` and `FixedCardinalitySubsetSets()(X,k)` now reject a source outside `Sets()` before computing the subset-family placement. Previously the cardinality owner's fallback could place a collection even with no set source (notably the `k=0` singleton branch). A focused Sage owner regression verifies both valid finite-ordinal constructions and both invalid-source rejections (`5fa2a292d0`). This is one set-family constructor-boundary repair, not closure of the category-wide operation/Mor placement audit.

**Matrix endomorphism placement on the acted regular module verified (2026-10-09):** After the rank-one selected regular framing, the generic `R[G]`-linear Mor `ordinary.Mor(A,A)` itself belongs to both `MatrixSpaces(R[G])` and `MatrixEndomorphismSpaces(R[G])` and retains `A` as both endpoints. This is distinct from the more restrictive equivariant Mor `A.Mor(A)`, whose comparison through the selected rank-one isomorphism was separately verified. Focused Sage confirms both matrix placements for `R=ZZ[C_2]`; the owner regression now records them.

**Rank-one regular resolution relation consistency repaired (2026-10-09):** The regular action's selected `R[G]`-framing has no relation morphism, even though its retained coefficient module may carry a different presentation. `_CoefficientModuleEngine._selected_relation_morphism()` now reads the free regular module's relation data from its `R[G]` resolution, not from `unformed_module()`. Focused Sage verifies `None` for the regular relation morphism, rank one over `ZZ[C_2]`, and coefficient rank two. The group-algebra regression records the zero-relation requirement.

**Regular representation rank-one framing constructed (2026-10-09):** The group-action module constructor now recognizes the exact left regular `R[G]`-module and selects its rank-one free `R[G]` resolution generated by the algebra unit, including `FramedFreeModules(R[G])` placement. Its original coefficient-module presentation is retained separately as `unformed_module()` with its independent `R`-basis. For `R=ZZ[C_2]`, targeted Sage confirms the acted module has rank one and one selected `R[G]` generator, the unformed coefficient module retains two generators, and the original selected inverse-pair isomorphism and nonidentity matrix/equivariant comparison pass their focused regression. Arbitrary actions are not inferred to be free over their group algebra.

**Nonidentity matrix-to-equivariant comparison verified (2026-10-09):** For the left regular `ZZ[C_2]`-module `A` and the selected rank-one free-module isomorphism `F -> A`, the matrix endomorphism of `F` sending its sole basis generator to its scalar multiple by the nonidentity group element transports to an admitted equivariant endomorphism of `A`. Targeted Sage verifies exact `A -> A` endpoints, the image of `1` is the selected group-algebra basis element `g`, and the transported endomorphism squares to the equivariant identity because `g^2=1`. The independent coefficient-module generating family remains unchanged; the stronger `FramedFreeModules(ZZ[C_2])` placement and selected rank-one basis on the acted object are not claimed.

**Generic module axiom expression results verified (2026-10-09):** `Modules(ZZ).FinitelyPresented().extra_super_categories()[0]` is the exact `Modules(ZZ).FinitelyGenerated()` category, and `Modules(ZZ).Free().extra_super_categories()[0]` is the exact projective-module category. An actual free rank-one `ZZ`-module lies in all four respective categories. Targeted Sage passed; the declared-base `self.base_category().FinitelyGenerated()` and `self.base_category().Projective()` edges now have owner-local executable specimens.

**Module-subobject base-category edge checked (2026-10-09):** For the ideal `2ZZ` as a submodule of `ZZ`, `SubobjectCategory(Modules(ZZ),ZZ)` has the exact `Modules(ZZ)` supercategory and retains the selected inclusion; its identity subobject morphism composes with itself. Focused Sage passed. The `self.base_category()` expression records ordinary module placement without identifying the restricted triangle Mor with every module map.

**Lattice embedding Mor inherited-endpoint expression checked (2026-10-09):** For `L=U`, every selected supercategory of `L.Mono(L)` retains exactly `L` as both endpoint objects; its chosen embedding identity composes to itself. Focused Sage passed, and the owner specimen now includes these assertions. The dependent `*inherited` graph entry is an endpoint-admissible family of monomorphism categories, not a declaration that all embeddings arise from one fixed scalar restriction.

**Graded algebra exemplar result placement checked (2026-10-09):** `GradedAlgebras(ZZ).an_object()` lies in its selected graded-algebra category, its graded-module category, and the associative unital algebra supercategory. Targeted Sage passed; the executable result-level assertions now supplement the prior declaration-only expression-edge check at the graded algebra owner.

**Group-algebra ordinary module-supercategory expression verified (2026-10-09):** For `R=ZZ[C_2]`, `Modules(R).super_categories()[0]` is exactly the generic `Modules(R)` constructed through its declaring base-category constructor, and `R.regular_representation()` lies in both that ordinary category and the specialized group-action category while retaining `R` as the identical scalar ring. Focused Sage passed and the specialization owner now has the executable result-placement specimen. This is not an assertion that its rank-two coefficient framing is an `R`-basis; the rank-one transport remains under its distinct TODO node.

**Semilinear formed-module Mor expression edge verified (2026-10-09):** With `L=U` over `ZZ`, the Mor category `FiberedFormedModuleMor(L,L.vector_space(),ZZ.fraction_field_map())` retains exactly the chosen integral lattice and rational extension as its endpoints and has the selected varying-ring module Mor as its immediate supercategory by identity. Focused Sage passed; the owner specimen now records both the endpoint and lower-Mor comparison without identifying a form-preserving arrow with an arbitrary semilinear arrow.

**Functor-category expression-edge endpoints verified (2026-10-09):** `Cat().functor_mor(Sets(),Sets())` has its actual functor category as its selected supercategory. Its source and target are the distinct endpoint *objects of Cat* representing `Sets()`, rather than literally the underlying `Sets()` category; both `.represented_category()` maps return the exact selected `Sets()`. Focused Sage passed, and the functor-Mor owner specimen now records the category-versus-category-object distinction.

**Chosen finite-presentation result/category edge checked (2026-10-09):** `ModulesWithChosenFinitePresentation(ZZ)` declares the generic `Modules(ZZ).FinitelyPresented()` as its exact supercategory, and its selected witness (the lattice `U`) lies in both categories. Focused Sage passed. The owner now records an executable specimen for `ordinary.FinitelyPresented()` that retains the same integer scalar ring rather than conflating the group-algebra coefficient action with an ordinary finitely presented module.

**Declared-base free-module edge checked (2026-10-09):** `FramedFreeModules(ZZ).an_object()` belongs to both its framed-free category and the generic `Modules(ZZ).Free()` declaration; its rank is one and its framing augmentation has exactly that module as target. The selected finite-presentation category independently declares the generic `Modules(ZZ).FinitelyPresented()` as its immediate supercategory. These are focused Sage assertions for the same scalar ring, not a restriction from a group algebra to its coefficient ring.

**Finite covering-family presentation placement verified (2026-10-09):** `CoveringFamilies(Sets()).an_object()` constructs a one-member identity cover, lies in both its covering-family category and the explicit presentation slice `Cat/Sets`, and its retained presentation targets `Sets()` by identity. Its selected covering-family Mor identity has the cover as its exact domain. Focused Sage passed; the owner-level specimen records this actual object-and-Mor comparison for `self.presentation_category()`.

**G-object forgetful endpoint comparison verified (2026-10-09):** The `C_2`-action on a two-point set constructs in both `GObjects(C_2,Sets())` and `Sets()`. Its forgetful value is a two-point set, but not literally the previously supplied `Sets.Δ[1]` object: it retains the selected action's separate representation. Focused Sage verifies that `GObjects._mor_endpoints_in_supercategory(Sets(),A,A)` uses the precise object returned by its forgetful functor. The owner now carries the executable specimen, without replacing selected object identity by equality of cardinalities.

**Direct-sum object result and structure morphisms verified (2026-10-09):** For `DirectSumObjects(Modules(ZZ)).an_object()`, focused Sage verifies both the selected direct-sum placement and the base-module placement, exactly two indexed summands, and the exact target of each injection and source of each projection. The executable specimen is recorded at `DirectSumObjects`. The `self.base_category()` edge therefore has a concrete result-and-arrow example without identifying all arrows of the chosen-decomposition category with unstructured module arrows.

**Coslice-category nonidentity square composition verified (2026-10-09):** Over `Sets.Δ[0]`, a map into the zero point of `Sets.Δ[1]` is fixed by the nonidentity collapse endomorphism. Focused Sage confirms its coslice square is idempotent, has the identity as the left fixed edge, and the collapse as the right edge; the executable owner specimen now records the source-dependent `self.base_category()` expression comparison. This complements the previously verified slice swap-square example without identifying their arrow theories.

**Finite injection and core-Mor cardinalities repaired (2026-10-09):** The fixed Mor of the monomorphism wide subcategory now computes finite-set injection counts from source and target cardinalities, giving `n!/(n-m)!` for `m <= n`, without attempting to iterate a native Mor. The finite-set core Mor similarly counts bijections as `n!` when endpoint cardinalities agree. Focused Sage execution of `test_injections_and_isomorphisms_of_a_two_element_set` passes: the injective and invertible endomorphism counts are both 2, the underlying endomorphism count is 4, collapse is rejected, and the swap squares to identity. The `finite-wide-mor-cardinality` node is closed; cardinality for unrestricted non-finite or general restricted Mor objects is not asserted.

**Slice-category nonidentity square composition checked (2026-10-09):** Over `Sets.Δ[0]`, the slice object defined by the unique map `Sets.Δ[1] -> Sets.Δ[0]` admits the nonidentity swap square. Focused Sage verifies that its square is the selected identity and that its left edge is the swap while its right edge is exactly the fixed object's identity. The executable specimen is retained at `SliceCategory` for the `self.base_category()` expression-edge audit.

**Finite wide-subcategory Mor cardinality deficiency isolated (2026-10-09):** The existing `test_injections_and_isomorphisms_of_a_two_element_set` reveals missing `FixedWideMorCategory.cardinality()` (the two-point injective endomorphism Mor should contain the identity and swap only). The apparent shortcut `self.object_set().cardinality()` fails with `Parent.__getitem__` recursion: underlying fixed Mor objects are not necessarily iterable sets. This is a separate finite-map enumeration obligation at the restricted Mor owner, filed as `finite-wide-mor-cardinality` in `TODO.md`; no false cardinality method was retained. The distinct endpoint comparison from `c235d63918` remains valid.

**Wide-subcategory fixed Mor supercategory endpoints checked (2026-10-09):** For the injective-map wide subcategory of `Sets()`, the selected fixed Mor over the two-point finite ordinal has an ordinary Mor supercategory with exactly the same source and target objects. Focused Sage verified both endpoint identities. An executable specimen is retained at `FixedWideMorCategory`; it does not assert that a collapse map belongs to the restricted Mor.

**Group-algebra Mor ordinary-supercategory expression verified (2026-10-09):** For the left regular `ZZ[C_2]`-module `A`, the equivariant Mor `A.Mor(A)` retains `A` as both endpoints, and its selected ordinary linear Mor supercategory also retains those exact endpoints. The equivariant identity composes with itself to the same arrow. Focused Sage passed; the `GroupModuleMor.super_categories()` owner now carries the separating executable specimen. This validates the particular expression edge, not the still-open transport of the regular module's chosen rank-one framing into matrix realization.

**Noncommutative matrix endomorphism result placement repaired (2026-10-09):** For `R=M_2(ZZ)`, `MatrixEndomorphismSpaces(R).an_object()` previously belonged to `MatrixSpaces(R)` but not its declared endomorphism category, despite its identical framed-free endpoints. The generic `Modules._mor_parent_placement` now places such an endomorphism in `MatrixEndomorphismSpaces(R)` as well as the central-linear Mor and additive-endomorphism owners. A focused Sage specimen verifies both matrix placements and exact endpoints/base ring, with an executable example at the endomorphism category owner. The separately active group-algebra framing task is not modified.

**Canonical rank-one group-algebra framing isomorphism constructed (2026-10-09):** The group algebra `R=ZZ[C_2]` retains two coefficient-module generators, while its left regular `R`-module `A` is canonically free of rank one. `R.regular_representation_basis_isomorphism()` now constructs the exact generic `R`-linear isomorphism `F_R(1) -> A` taking the sole basis vector to `1_R`, with inverse taking coefficient generator `g` to `g e`. Targeted Sage verifies both composites on their complete selected generating families and the exact endpoints. Conjugating the generic matrix identity by these maps yields an admitted equivariant identity endomorphism of `A` with both endpoints retained (owner-local test). This construction exposed and repaired two general owner faults: `GroupModule` coefficient coordinates must use `R_coeff -> R_coeff[G]` rather than raw ring coercion, and module morphism composition must reuse the declaring Mor category, not redispatch through the potentially stricter selected-action category. Both the group-algebra specimen and an ordinary integral-module doubling composition passed. The remaining task is transporting the chosen rank-one isomorphism to a `FramedFreeModules(R)` realization of `A` without discarding its independent coefficient presentation, followed by the full matrix/equivariant Mor comparison.

**Non-domain polynomial localization realized and toric scheme constructed (2026-10-09):** For a polynomial algebra over a ring with zero divisors, the generic localization owner now realizes `S^{-1}A` as the quotient obtained by adjoining inverse variables `t_i` with relations `t_i s_i = 1`. Its engine map and inverse-variable decoding retain the owned source and the chosen denominator family, without asserting a domain hypothesis. On `R=ZZ/(4)`, the owner-local specimen verifies `x * x^{-1} = 1` in `R[x,x^{-1}]`, the exact localization source/map and an engine round trip for `x^{-1}`. The toric owner independently constructs the fan presentation of `P^1_R`, verifies membership in `ToricSchemes(R)` and non-membership in `Varieties(R)` with identical base ring. Both focused Sage specimens passed. The former complaint and `toric-nondomain-localization` TODO item are resolved and removed; general structural category-audit work continues.

**Projective-point blowup and product-atlas comparisons repaired (2026-10-09):** The chart-overlap failure is traced to two native Sage `FormalCompositeMap` objects with identical owned endpoints whose native comparison returns `False`. The projective-product chart embedding now composes through its existing homogeneous-coordinate morphism, not through the native formal composite; this respects the projective coordinate substitution law. Focused Sage constructs the four-chart atlas of `P^1 x P^1`, the projective-plane point blowup `B=ProjectivePointBlowups(QQ).an_object()`, verifies membership in `ProjectivePointBlowups(QQ)` and `ProjectiveSurfaces(QQ)`, and confirms the blowdown arrow starts at `B` and ends at its original `P^2_QQ`. Both owner specimens are executable.


**Non-domain toric category edge falsified at construction (2026-10-09):** For `R=ZZ.quotient_ring(ZZ.ideal(4))`, focused Sage verifies `R.is_integral_domain()` is false and `Varieties(R)` is absent from `ToricSchemes(R).super_categories()`, as the guarded declaration requires. However `ToricSchemes(R).an_object()` fails at the shared commutative-ring localization engine: the fallback native Sage `localization(values)` requires an integral domain, though the universal localization exists for this ring. This is an actual mathematical construction deficiency, not a reason to delete the toric category edge. It is filed at `toric-nondomain-localization` in `TODO.md` with the required inverse-variable quotient construction and true ring-theoretic acceptance assertions.

**Toric construction and fixed-point blowup result categories verified (2026-10-09):** The actual objects `ToricSchemes(QQ).an_object()` and `ToricSchemes(ZZ).an_object()` construct and lie in both their toric categories and `Varieties(QQ)`/`Varieties(ZZ)` respectively. The actual `ToricFixedPointBlowups(QQ).an_object()` belongs to its fixed-point blowup category, the toric scheme category, `Blowups(QQ)`, and `Surfaces(QQ)`; its blowdown domain is the constructed blowup and its codomain is identically its retained source. Focused Sage passed, with executable examples at the two construction owners. The earlier source-only conditional-guard interpretation now has positive object-level examples for both toric edges; non-domain ring cases remain outside these specimens.

**Projective-point blowup category edge exposed two constructor defects (2026-10-09):** The `ProjectivePointBlowups(QQ).an_object()` route formerly stopped immediately because the native Sage projective space has `point_homset()`, not `point_mor()`. The projective point owner now uses the native point homset for projective factors and products; on `P^2_QQ`, the selected `Spec(QQ) -> P^2` point has the exact owned endpoints (focused Sage). The product line bundle `O(1,1)` has a standard-atlas gluing datum and transition units computed from its multidegree, just as `O(d)` does on a single projective space; the product engine now declares these as derived constructor data. The attempted full blowup then advances to an independent failure when constructing the standard affine atlas of the product: a chart-overlap square is rejected as noncommuting by `CommutativeSquareMor._square`. This does not establish either the correctness or incorrectness of the alleged equality of scheme maps; its maps need owner-level comparison before the blowup's resulting category placement can be accepted. No actual projective blowup result has been verified by this path.

**Subobject result construction kept canonical (2026-10-09):** Each Boolean operation of `SetSubobjectCategory.ParentMethods` already returns a represented subobject of the common ambient via the inclusion-morphism construction; constructing another slice object around its arrow is redundant. The owner now returns the construction's exact subobject instead of rewrapping it. Focused Sage confirms that the intersection of `{0}` and `{1}` is already in `Sets().Subobjects(Sets.Δ[2])` with the identical ambient target. The five-operation regression specimen still passes after removing the extra construction.

**Set-subobject dynamic finite-placement edge checked (2026-10-09):** The `categories` expression in `SetSubobjectCategory.super_categories()` is conditional on the ambient object's finiteness. Focused Sage confirms `Sets().Subobjects(Sets.Δ[2])` includes `Sets().Finite()` in its immediate supercategories whereas `Sets().Subobjects(NN)` does not. The corresponding executable owner specimen records the two cases. This is a valid condition-dependent placement, not a parser warning to suppress; the wider expression-edge audit remains active.

**Represented finite-subobject operations repaired (2026-10-09):** `Objects.ParentMethods._with_structure` now anchors an inherited private realization below the target's declared category providers whenever the target includes the owned root `Objects()`; a target lacking that root retains its original realization owner (including finite affine atlas objects). On `X=Sets.Δ[2]`, `A={0}` and `B={1}` now use the `SetSubobjectCategory` union, intersection, difference, symmetric difference and complement operations, rather than the received finite-ordered-set methods. The set-subobject owner passes each resulting represented subobject's actual inclusion arrow to the slice constructor, not the subobject object. A focused Sage specimen checks respective sizes `2,0,1,2,2`, the identical ambient inclusion codomain, finite placement, and unchanged ordinary finite-ordinal intersection. A separate focused check retains the two-chart atlas of `P^1_QQ`; the `subobject-realization-method-precedence` node is closed.

**Nonzero chartwise sheaf/descent composition checked (2026-10-09):** On the standard two-chart atlas of `P^1_QQ`, multiplication by two on the rank-one local modules gives a compatible nonzero, nonidentity sheaf endomorphism. The owner-local specimen verifies left and right identity composition, distinguishes it from the zero and identity arrows, and compares its square with the square of its selected descent arrow. Focused Sage passed. The independent subobject realization/provider precedence defect remains under its TODO owner.

**Nonidentity sheaf/descent composition comparison (2026-10-09):** The finite-atlas descent and sheaf Mor methods now implement Sage's `_richcmp_` rather than relying on Python `__eq__` in their compatibility shells. On the standard two-chart atlas of `P^1_QQ`, a zero sheaf endomorphism is distinct from the identity, both left and right composition with the identity recover zero, and the selected `descent_morphism()` preserves that nonidentity composition (focused Sage, `tests/schemes/test_cover_atlas.sage`). The same specimen constructs the distinct sheaves `F` and `F tensor F`, zero arrows in both directions, and verifies their sheaf composite and descent composite. Arbitrary nonzero chartwise maps are not asserted tested.

**Finite-atlas sheaf/descent Mor identity comparison verified (2026-10-09):** On the standard two-chart cover of `P^1_QQ`, the cover's selected engine now passes through the generic covering-family construction as computation, not as an extra mathematical datum. Its retained gluing presentation supplies the chosen overlap ordering. The corresponding rank-one descent datum constructs after correcting the generic semilinear morphism's premature endpoint access and its same-ring restriction-of-scalars realization. A sheaf morphism now initializes its sheaf endpoints and validates local maps at the descent owner. Focused Sage verifies the sheaf identity, its composition with itself, and equality of the resulting descent composite; the owner docstring contains the executable specimen. General nonidentity sheaf compositions remain to be checked.

**Distinguished affine-cover catalogue MRO repaired (2026-10-09):** The generic owned provider linearization now orders `Cat.ParentMethods` before the owned `Objects.ParentMethods` root when both occur. This is required by a category endpoint's retained realization and resolves the conflict between the fibre-to-catalogue and covering-presentation branches without deleting either mathematical inclusion. Targeted Sage constructs `DistinguishedAffineCovers().an_object()` and verifies membership both in its exact fibre `DistinguishedAffineCovers(X)` and in the catalogue, as well as in `CoveringFamilies(DistinguishedAffineCovers(X).site_category())`; the site category is retained by identity. The independent `category-graph-expression-edges-audit` remains the current frontier.

**Step-2 varying-ring formed Mor edge verified (2026-10-09):** For `L=U` and the canonical `ZZ→QQ` morphism, the exact `FiberedFormedModuleMor(L,L.vector_space(),f)` constructs and its selected supercategory is identically its retained underlying varying-ring semilinear `module_mor()`. Focused Sage passed, and the executable owner specimen records the comparison without identifying the form-preserving data with the underlying arrow.

**Category-graph functor-Mor edge verified (2026-10-09):** `Cat().functor_mor(Sets(),Sets())` is the `CategoryFunctorMor` owner; `Cat().Mor(Sets(),Sets())` instead returns its functor-category target and cannot serve as the specimen. Focused Sage verifies that the selected Mor owner's `super_categories()[0] is functor_category()`. This distinguishing call and passing assertion are retained in the owner docstring. The active audit remains separate from the deferred module-exemplar chain.

**Category-graph object-level verification continued (2026-10-09):** Focused Sage confirms the exact selected supercategory of `DirectSumObjects(Modules(ZZ))` is `Modules(ZZ)`, and that of `GObjects(Groups.C(2),Sets())` is `Sets()`. Their corresponding dynamic expression edges have executable runtime evidence in addition to source-level dispositions. Mor and universal-property comparisons remain distinct.

**Category-graph slice/coslice runtime check (2026-10-09):** Focused Sage on `X=Sets.Δ[0]` confirms both `SliceCategory(Sets(),X)` and `CosliceCategory(Sets(),X)` have `Sets()` as the selected supercategory and retain `X` as their fixed base object. This advances the active expression-edge audit without reopening the module-exemplar dependency or confusing an arrow-category forgetful functor with a supercategory assertion. The commuting-square Mor acceptance remains separate.

**Inherited embedding-Mor graph edge verified (2026-10-09):** The `*inherited` expression at the module, formed-module and lattice embedding Mor owners is an endpoint-filtered list of monomorphism categories of super-packets, not an unresolved uniform category name. Targeted Sage on `L=U` confirms `L.Mono(L)` has source and target `L` and three inherited/base supercategories. An executable lattice-owner specimen and TODO disposition retain that evidence. The graph flag is not a reason to replace endpoint-specific inheritance by an untyped category.

**Remaining category-graph expression edges inspected (2026-10-09):** `CategoryFunctorMor`, `FiberedFormedModuleMor`, `GradedAlgebras`, `FixedWideMorCategory`, and the three base-dependent toric/blowup constructions were checked at their `super_categories` owner methods. Their dynamic expressions reflect selected underlying morphisms, grading, or explicit ring-property case distinctions. The active TODO now records the mathematical interpretation and remaining evidence burden for each. The inherited embedding-Mor flag and concrete validation of the cover-fibre inclusion remain open; neither justifies suppressing the category-graph warnings without a counterexample.

**Category-graph expression audit advanced (2026-10-09):** Read the actual `super_categories` and owner comments for `CoveringFamilies` (`presentation_category`), `DirectSumObjects`, `GObjects` (`underlying_category` and forgetful Mor endpoint conversion), and slice/coslice (`base_category`). The corresponding source-level dispositions are now in the active `category-graph-expression-edges-audit` TODO node. The remaining flags still require individual mathematical assessment; no assertion was deleted merely to silence the graph renderer.

**Category-graph flag dispositions resumed (2026-10-09):** Inspected the source of the `DistinguishedAffineCovers` self-name flag and the `FiniteAtlasModuleSheafMor` (`gluing`, inherited quasi-coherent Mor), `MatrixEndomorphismSpaces` (`multiplicative_owner`), and `ModulesOverGroupAlgebra` (`ordinary`) expression edges. These represent parameterized catalogue inclusion, distinct Mor data, and hypothesis-dependent or generic category ownership respectively; no mathematical counterexample justifies removing those edges. The unparameterized cover catalogue constructs and declares `Objects()` as its supercategory, but `DistinguishedAffineCovers().an_object()` encounters a real `Cat.ParentMethods` / `Objects.ParentMethods` MRO failure before a concrete covering comparison is possible. This is filed as the independent `distinguished-affine-cover-catalogue-mro` TODO node. Continue examining the other flagged edges rather than resuming the deferred module-exemplar cascade.

**Step-2 frontier corrected (2026-10-09):** The group-module/matrix exemplar cascade is no longer an immediate obvious-placement repair. Its outstanding basis/action/Mor comparison has been filed as `group-algebra-matrix-exemplar-placement` in `TODO.md`; leave that dependency aside and resume the independent category-graph audit (flagged `DistinguishedAffineCovers` self-name, 13 expression-derived edges, construction and property views). Do not reopen the exemplar chain while the independent audit has ready work.

**Category-graph audit resumed (2026-10-09):** The current `audit` view reports zero missing named supercategories, zero cycles, 17 expression-derived edges (including recent generic declaring-category corrections), and one same-name flag for `DistinguishedAffineCovers`. Source inspection shows the flagged declaration is the fibre `DistinguishedAffineCovers(X)` inside its unparameterized catalogue, so the tool's blanket restriction-of-scalars diagnosis is not established. The `properties` view names `FinitePowerSets` among categories not under `Sets.Finite`, but `P_fin(X)` is infinite for infinite `X`; runtime independently checked `P_fin(Δ[2])` is finite of cardinality eight. The `constructions --select FinitePowerSets` invocation reached a 40-second timeout without output and is not a validation result. The remaining 17 expression edges and cover-fibre inclusion are separately recorded as `category-graph-expression-edges-audit` in TODO; do not conflate parser warnings with mathematical counterexamples.

**Step-2 matrix-category exemplars repaired (2026-10-09):** `MatrixSpaces(R).an_object()` and `MatrixEndomorphismSpaces(R).an_object()` formerly obtained a source via `Modules(R).an_object()`, which for `R=ZZ[C_2]` is a trivial-action coefficient module, not rank-one free over `R`. Their group-algebra specialization now selects the existing `R.regular_representation()`: the left regular `R`-module, free of rank one over the group algebra, with its action retained. Focused Sage verifies that both exemplar morphism objects construct, both sources are in `Modules(R)`, and their base ring is the exact `R`. Ordinary coefficient rings retain the prior exemplar path.

**Step-2 scalar-interface regression (2026-10-09):** The represented trivial-action `ZZ[C_2]`-module satisfies both the algebra identity action `M.scalar_multiple(R.one(),v)==v` and coefficient inclusion `M.scalar_multiple(ZZ(2),v)==v+v` in focused Sage. Both cases are now retained as executable owner docstring specimens, guarding against a change that fixes coefficient ingress by breaking the native group-algebra action.

**Step-2 coefficient scalar action repaired (2026-10-09):** A represented `R[G]`-module rejected scalars from `R` that had not been explicitly embedded into the group algebra. The group-module owner now uses the retained `coefficient_inclusion():R→R[G]` before applying its algebra action, while preserving native `R[G]` scalars. Focused Sage for the trivial `C_2`-module verifies `M.scalar_multiple(ZZ(4),v)==v+v+v+v`. A scalar in neither ring raises `TypeError` rather than being silently interpreted as a group-algebra element.

**Step-2 generic framing and resolution ownership repaired (2026-10-09):** The represented `ZZ[C_2]`-module has a valid equivariant Mor identity, but evaluating its selected generator formerly failed: `_framing_morphism` required the generic free source to be an object of the specialized selected-action category, and `Modules.resolutions()` redispatched its `Projective` axiom through `ModulesOverGroupAlgebra`. The framing now uses the generic `Modules(R)` owner, and the resolution owner uses that same declaring category for projective resolutions. Focused Sage verifies that the trivial-action rank-one module's selected generator exists and `(id*id)(v)==v`. Both generic free sources and selected equivariant actions retain their distinct category data.

**Step-2 equivariant identity initialization repaired (2026-10-09):** The represented `Modules(ZZ[C_2])` Mor constructed after the action-placement repair, but its `identity()` failed because the generated equivariant-arrow element inherited the scalar-extension `_initialize_lower_arrow` path, which passes unsupported `evaluator=` arguments into Sage's `Map`. `GroupModuleMorphismMethods` now initializes the morphism through `Morphism.__init__(self,parent)` at its own owner. Focused Sage constructs the identity of the trivial-action rank-one module and verifies both endpoints are that module. This is an owner-local correction, not a claim that every equivariant composition is certified.

**Step-2 represented group-algebra module placement repaired (2026-10-09):** `_equip_action` formerly constructed only an object of `GeneralModules(R[G])`, while its group-module methods required membership in `ModulesOverGroupAlgebra`. Its owned category is now the meet of `GeneralModules(R[G])` and `Modules(R[G])`, preserving the chosen action and underlying coefficient module. Focused Sage checks on the trivial `C_2`-action on `ZZ.free_module(1)` confirm membership in `Modules(ZZ[C_2])` and that `N.Mor(N)` constructs with base ring `ZZ[C_2]`. The unrelated generic `ZZ[C_2].free_module(1)` still does not acquire a *chosen group action* from this construction.

**Step-2 group-algebra module supercategory corrected (2026-10-09):** `ModulesOverGroupAlgebra.super_categories()` previously declared only commutative additive groups, although an `R[G]`-module is first a module over the ring `R[G]`. The owner now includes generic `Modules(R[G])` without redispatching to the specialized category; focused Sage confirms this generic supercategory and that `R.free_module(1)` still constructs with rank one. This does **not** resolve the separate selected-parent membership defect: the free module remains outside the specialized `Modules(R[G])` placement, so `M.Mor(M)` is not certified. An attempt to add the specialized placement directly caused an inherited `Modules.Free` axiom-descriptor mismatch and was reverted; similarly a global descriptor change broke an unrelated `AdditiveCommutative` axiom and was reverted. The remaining placement construction must respect both base module structure and specialized action data.

**Step-2 finite-presentation axiom ownership repaired (2026-10-09):** The general selected-presentation module category's `super_categories()` constructed `Modules(R).FinitelyPresented()`, and the `Modules.FinitelyPresented` axiom's `extra_super_categories()` constructed `Modules(R).FinitelyGenerated()`. On a group algebra, both redispatched to `ModulesOverGroupAlgebra` and raised inherited Sage axiom-base mismatches. Both now obtain those axioms through their declaring `Modules` base category. Focused Sage verifies `R=ZZ[C_2]`, `R.free_module(1)` has rank one and base ring exactly `R`. This establishes the free-module construction, not the entire equivariant-Mor integration.

**Step-2 free/projective axiom ownership repaired (2026-10-09):** `FramedFreeModules(R).super_categories()` now constructs `Modules.Free` on its generic `Modules` declaring category, even when `Modules(R)` routes to `ModulesOverGroupAlgebra`. `Modules.Free.extra_super_categories()` uses that exact base category to obtain `Projective`, instead of redispatching `Modules(R)` and triggering Sage's axiom-base mismatch. Focused Sage on `R=ZZ[C_2]` confirms the framed-free supercategory has `Free` and `Projective` axioms. Subsequent construction of an actual free `R`-module is still blocked by another inherited axiom `Modules.FinitelyPresented` mismatch; no claim of an end-to-end group-module object is made.

**Step-2 framed-free exemplar corrected (2026-10-09):** `FramedFreeModules(R).an_object()` previously constructed the hyperbolic *formed* lattice `U`, incorrectly requiring a bilinear form even for general coefficient rings. It now returns the rank-one framed free `R`-module. Focused Sage confirms rank one and base `ZZ` for the commutative specimen. Separately, attempting the permutation module over `ZZ[C_2]` exposed the inherited `Modules.Free`/`Modules.Projective` axiom-class mismatch on `ModulesOverGroupAlgebra`. Direct construction of the specialized free category remains a prerequisite; the two attempted local shortcuts did not solve it and were reverted. Do not claim the group-module Mor instance has been verified.

**Step-2 group-module Mor scalar placement (2026-10-09):** `GroupModuleMor.__init__` formerly selected `ZZ` as scalar ring whenever its coefficient ring was noncommutative. This discarded the canonical action of the *whole center* of that ring. The owner now selects `coefficient_ring.ring_center()`, parallel to the repaired matrix-Hom placement; it leaves commutative coefficient rings unchanged. A focused Sage specimen confirms that `M_2(ZZ)` is noncommutative and its constructed center belongs to `OwnedRings().Commutative()`. Direct end-to-end group-module Mor instantiation has not yet been checked.

**Step-2 noncommutative endomorphism placement verified (2026-10-09):** After repairing the center construction, the concrete noncommutative coefficient ring `R=M_2(ZZ)` now admits `MatrixSpaces(R)` with scalar base exactly `R.ring_center()` and `MatrixEndomorphismSpaces(R)` with ring placement `OwnedRings()`. Focused Sage checks both returned true. The two category-owner docstrings now retain these executable separating specimens; neither asserts an `R`-linear structure on the full Hom when `R` is noncommutative.

**Step-2 noncommutative center construction repaired (2026-10-09):** `_PredicateSubringParent` previously passed its own partially initialized parent as the base ring to `Algebras(self)` and `FinitelyGeneratedFreeModules(self)`, causing `AttributeError: subcategory_class` during `A.ring_center()` for `A=M_2(ZZ)`. Its construction now uses the already initialized `ZZ` scalar ring to obtain its commutative ring structure; this avoids pretending that a general center is already an algebra over itself during initialization. Focused Sage confirms `A.ring_center()` constructs, is in `OwnedRings().Commutative()`, and `MatrixSpaces(A).super_categories()[0] is LinearMorModules(A.ring_center())`. The predicate defining centrality remains retained, as do the unit and product operations. The construction no longer asserts an unproved finitely generated free module over the center for an arbitrary predicate subring.

**Step-2 matrix-Mor placement repaired (2026-10-09):** `MatrixSpaces(R).super_categories()` previously asserted `Hom_R(F,G)` was a finitely generated *left R-module* even when `R` is noncommutative. The owner now retains the framed free R-module placement only when R is commutative; otherwise it declares central-linear structure through `LinearMorModules(R.ring_center())`, consistent with `_mor_parent_placement` for noncommutative coefficients. The existing commutative ZZ category path passed a focused Sage check. Attempting a noncommutative matrix-algebra category instance exposed a pre-existing category-construction `subcategory_class` failure before reaching this supercategory method, so that runtime specialization remains unverified and needs its owner-level constructor path examined separately.

**Step 1 research-side complete; port stopped (2026-10-09):** All twenty numbered rows of `docs/issue-401-abstraction-audit.md` now state the research call/result/failure comparison against the frozen API, with differences explicitly assigned to the stopped port rather than silently changing research mathematical owners. `indefinite-port-primitives` remains unchecked solely because external port integration is stopped, not because research must implement port #18 or act on #33. Research step 2 started with `just category-graph --help`, which exposed a Python syntax error in the category-graph source (`except SyntaxError, OSError`); the parse error was repaired at its owner.

**Frozen-call rows 14, 17, 18 and 20 reconciled (2026-10-09):** The audit distinguishes twisted isometry and inverse transport from general nonunit scaling; full norm fibres from orbit quotients and binary reduction cycles; bounded signed shells from their exact-boundary spheres; and the formed ideal-dual inverse image with both comparison morphisms, including radical divisor zero. Existing owner specimens provide engineering evidence for these contracts. Port-side changes remain deferred under the stopped stream, and the research contracts are not replaced with orbit representatives, coordinate matrices or unsigned shells.

**Frozen-call rows 15 and 16 reconciled (2026-10-09):** `R.rational_lifts(target,psi)` returns the full marked-line kernel torsor, distinct from its selected base point and the `integral_members()` G-object; rank-one and rank-zero owner specimens establish the intended data. Formed modules expose `positive_vector()` and `vector_of_sign(sign)` with strict-sign result or `None`, reject invalid signs, and retain the source subobject as parent. The audit records both result and failure contracts; the stopped port must not substitute an affine matrix space for a nonlinear lift torsor.

**Frozen-call row 11 reconciled (2026-10-09):** The research `witt_extension(source_inclusion,target_inclusion)` returns a selected ambient isometry and retains its defining square via `witt_extension_locus()`. It validates the inclusion domains and rejects ambient-radical mismatch with `ValueError`, rather than relying on nondegenerate Witt extension in the degenerate case. Existing positive and negative owner specimens cover restriction, inverse and the radical obstruction.

**Frozen-call rows 7 and 8 reconciled (2026-10-09):** `integral_members(j)` belongs to the shared affine *solution-fibre* owner, returns the whole integral inverse-image fibre with its parameter inclusion, and raises for a nonzero target submodule or mismatched scalar-restriction ambient; it is not an enumeration of points. The matrix operator `A.symmetrized_right_multiplication()` returns the linear map, while `solution_fibre(B)` retains the inhomogeneous solution locus and `kernel()` only the homogeneous solutions. Focused Sage on `A=I_2`, `B=2I_2` verifies the solution origin, skew kernel and translation membership. The audit records both frozen names and their different result types, including the port-side requirement to create the solution fibre before intersecting with integral parameters.

**Frozen-call row 9 reconciled (2026-10-09):** `G.invariant_overlattice(L)` returns the owned orbit-generated integral submodule construction with its action and ambient inclusion. It is partial on the represented input category: the selected group must act through the orthogonal group of the same rational span, finite rank is required by the current realization, and a rational commensuration does not ensure any integral invariant overlattice exists. The existing U dilation obstruction passed the owner-local test. The audit now records the precise result and failure hypotheses rather than treating the frozen method as unconditional.

**Frozen-call row 5 reconciled (2026-10-09):** `R.integral_hyperbolic_splitting()` is the chosen integral decomposition `L→U⊥R` at the reduction owner, retaining the exact quotient `R` as a factor and both comparison isometries. It requires an even `ZZ` ambient, an isotropic line, and divisibility one, rejecting failures with `ValueError`. The existing owner specimen exercises the endpoint identities and the inverse; this entry records name, structured return object, and the hypothesis/failure boundary.

**Frozen-call row 6 reconciled (2026-10-09):** `L.two_hyperbolic_plane_splitting()` returns `None` when no two integral planes exist, or an isometry `U⊥U⊥K→L` preserving the summand inclusions and reduction comparisons; this is opposite to the single-reduction arrow `L→U⊥R`. The scrambled `2U+E8(-1)` inverse check already passed. The audit records the precise arrow variance and distinguishes mathematical nonexistence from an unavailable algorithm.

**Frozen-call rows 2 and 3 reconciled (2026-10-09):** Free-module `v.content()` returns the normalized integer generator while `v.order_ideal()` retains the intrinsic ideal; `primitive_part()` rejects zero. Lattice `v.bezout_partner()` returns a selected vector in the pairing-map fibre and zero at a radical zero input. On Gram `[[0,6],[6,0]]`, coordinates `(2,3)` give content one and partner pairing six, with zero-partner behavior verified in focused Sage. The audit now records the actual name, owner, result and failure boundary separately from formal proof obligations.

**Frozen-call rows 1 and 4 reconciled (2026-10-09):** The current `L.isotropic_vector()` uses the frozen name, returning a primitive integral nonzero null vector or raising on an empty null fibre; radical witnesses are permitted. The current `v.hyperbolic_partner()` returns a selected integral null partner outside an empty locus, which raises `ValueError`; `hyperbolic_partner_locus()` separately retains all solutions. The existing owner docstrings contain positive and separating failure specimens, so the audit records these contracts without introducing a redundant second implementation.

**Frozen-call row 13 reconciled (2026-10-09):** `phi.integral_similarity(L,E)` returns a formed monomorphism with denominator factor `scale()`, form `multiplier()`, and image `index()`. The genuine `diag(2,1/2)` isometry over the chosen labels of `U` returned `(2,4,4)` by focused Sage. An initial fixture using `j==0` instead of an actual frame label falsely produced rank one; this was a specimen error, not a failure of the index implementation. Both such docstring fixtures were corrected to use selected labels. The returned embedding need not be onto `E`.

**Frozen-call row 10 reconciled (2026-10-09):** The research owner exports exactly `extension_across(v,w)`, with optional explicitly retained perpendicular inclusions. It returns an isometry over the common fraction field and raises on zero/unequal vector squares or mismatched embeddings. The existing distinct-endpoint, noncanonical-arrow and integral-descent checks supply positive evidence; a zero-square failure specimen is now retained at the method. The audit's older `extend_from_perpendicular` trace is explicitly marked historical.

**Frozen-call row 19 reconciled (2026-10-09):** Research `L.affine_line_points(base,direction)` retains the frozen name and returns either `None` or the point/primitive-step presentation in `L×L`; the actual integral image with its maps is `L.affine_line_fibre(base,direction).image_point_set()`. On constant zero direction over U, targeted Sage verified the pair is `(0,0)` but the image cardinality is one. The audit now explicitly separates the return presentation from the point-set object and records the stopped port's responsibility not to conflate them.

**Frozen-call row 12 reconciled (2026-10-09):** `M.integral_isometry(phi)` returns an actual integral isometry or raises; `phi.is_integral_on(L)` is a forward-only Boolean and `phi.integral_restriction(L,M)` returns an integral isometry or `None`. On U, `diag(2,1/2)` gives respectively `ValueError`, `False` and `None` (focused Sage). The exact constructor failure specimen is retained at its owner and the audit identifies the three distinct contracts.

**Finite-image cardinality boundary repaired (2026-10-09):** The group owner's `finite_image_lifts(image_bound=...)` previously converted a nonintegral bound such as `2.5` to `2` silently, although its output represents a cardinality-bounded traversal and its finite-index Schreier consumer already rejects nonintegral bounds. It now rejects nonintegral bounds with `ValueError`, retaining the correct exact integer bound. Targeted Sage on `C4 -> C2` confirmed the valid bound yields two image lifts and the nonintegral bound is rejected. The contract check is retained in the focused group closure file.

**Ideal-dual pullback square compared (2026-10-09):** For the degenerate Gram matrix `diag(0,2)` and divisor `3`, the actual maps on `D=L.divisible_sublattice(3)` satisfy `j*i=u*k` on every module generator, where `j:L→L_Q`, `i:D→L`, `k:D→ideal_dual(3)`, and `u:ideal_dual(3)→L_Q`. Targeted Sage execution returned true; the comparison specimen is now at the lattice operation owner. This verifies the defining square, not merely point membership or ranks. Formal comparison at the ideal-dual owner remains distinct.

**Independent generated-subgroup index verified (2026-10-09):** The reopened `finite-index-subgroup-generators` TODO is closed by a separate calculation on the *actual matrices* of the twelve Schreier generators for `SL_2(ZZ) -> SL_2(F_2)`. Their matrix family contains `-I`, `T^2` and `-S*T^2*S^-1`, generating `Gamma(2)`; all twelve reduce to identity modulo two. Therefore their generated subgroup equals `Gamma(2)`, and Sage's independent arithmetic-subgroup implementation computes its index as six. The focused test passed. This uses neither the asserted Schreier theorem nor `kernel.index()` to determine the generated subgroup's index.

**Closure gate evidence (2026-10-09):** The TODO nodes `finite-index-subgroup-generators` and `images-of-subgroups-and-predicate-subsets` are checked with the four focused specimens in `tests/groups/test_finite_index_closure_401.sage`. The mod-two kernel of `SL_2(ZZ)` has computed index six and twelve Schreier generators mapping to the identity. For the indefinite lattice `U(2)`, the exchange and minus-identity isometries generate its four-element integral orthogonal group; the stable preimage returns four Schreier generators, all in `ker rho`, and its subgroup image under `rho` is trivial. The generated image of `O(A_2)` is all of its order-two discriminant group. A general infinite predicate-set image with no inverse correctly reports the missing image-membership procedure. Direct Sage execution passed all four functions; the targeted pytest entrypoint stopped on the independent preamble star-import 2-second timing gate. The canonical provider import for indefinite `O(L)` generators is not available in the current port tree; frozen `709f81a` does export it, so port snapshot parity remains part of the `indefinite-port-primitives` closure gate. The pinned port source, not the divergent current port tree, is authoritative.

**Pinned snapshot and remaining external obstruction (2026-10-09):** An isolated read-only extract of the port at `709f81a` successfully imported its `orthogonal_group_generators` symbol, but evaluating the selected resolution for `O(U(2))` raised `sage_indefinite_port.readiness.UnfinishedCapability`, identifying port work unit #18. The current port checkout instead lacks the exported name. By supplying the complete two-generator family of `O(U(2))` explicitly, research's kernel and image constructions pass without depending on this unfinished port provider. The separate scrambled `2U + E8(-1)` specimen constructed a two-plane splitting and its inverse recovered all twelve source generators (targeted Sage, under 65 seconds). Thus the research-side dependency specimens passed; the unfinished port generator provider and independent acceptance cannot be claimed complete. The kernel's finite-image index now returns the same owned cardinality type as the general subgroup index.

**Explicit selected orthogonal-group resolution (2026-10-09):** `O(L).select_group_resolution(generators=...)` now installs a complete generator family as the selected group resolution without asking an unfinished indefinite backend to compute it. The input must be proved complete by its caller; repeating selection is rejected rather than silently replacing an existing resolution. For `U(2)`, the exchange and minus-identity matrices are the full four-element `O(U(2))` and the default `stable_orthogonal_group().schreier_generators()` route now returns four generators in `ker rho` after explicit selection (focused Sage). This repairs the missing ordinary consumer route without assuming a selected subset generates every arithmetic orthogonal group.

**Indefinite membership-only subgroup image (2026-10-09):** `PredicateSubgroups.finite_index_schreier_generators` now accepts an explicitly supplied complete ambient generator family; `Subgroups.image_under` forwards that family along the bounded finite-index predicate route. The subgroup of `O(U(2))` defined solely by `rho(g)=1` now has a computable image under `rho` of order one using its known exchange and minus-identity generators and an index bound of four (focused Sage). The result does not require a selected ambient resolution or a finite quotient preimage object.

The remaining unit is integration of the affine fibres, integral lift torsors, and generated orthogonal-group actions. The checkpoint includes shared-owner changes whose broader contracts still need review:

| Owner | Check still needed |
| --- | --- |
| `categories/group/groups.py` | **GroupExp targeted checks passed:** on the regular ZZ-module, the additive/multiplicative identification has inverse, preserves addition as multiplication and sends zero to the identity; on the regular module over `ZZ/(2)`, the inverse and order-two generator relation hold. **Generated-subgroup word witnesses repaired:** `GeneratedSubgroups.membership_decision(candidate,word=...)` evaluates the witness through the chosen free-group generators, proving membership of `g^2` and `g^-2` in `<g>` for `g=diag(2,1/2)` on `U_QQ`; unwitnessed membership returns `is_member(candidate,H)` rather than the native infinite matrix engine's false negative. Python's Boolean `in` raises on undecided membership. Other realizations remain to check. |
| `categories/modules/framed/formed/torsion_form_modules.py` | **Targeted check passed:** on the discriminant quadratic form of `U(2)`, `O(q)` has order two; the subgroup on its nonidentity generator has order two and admits both that generator and the identity. The subgroup on no generators has order one, admits the identity, and rejects the nonidentity generator. This verifies both positive and negative membership in the generated finite orthogonal-subgroup protocol. |
| `categories/modules/framed/finitely_generated/finitely_presented_modules.py` | **Targeted checks passed after `db2cbc6a80`:** the cokernel of the zero endomorphism on the regular module over the finite non-PID ring `ZZ/(4)` is finite (`is_finite()=True`); for the analogous finite presentation over the infinite non-PID ring `ZZ[x]`, `is_finite()` returns the unresolved proposition `is_finite(M)` rather than asserting a PID-dependent cardinality. |
| `categories/abstract_categories/products.py` | **Targeted checks passed:** the diagram of two distinct but extensionally equal `Sets().Mor(X,Y)` maps retains the exact left and right arrow objects, repeat construction reuses the diagram, and reversing the arrows gives a distinct diagram with the reversed images. The construction is keyed by arrow identity, as the retained universal diagram contract requires. |
| `categories/lattice_engines.py` | **Targeted checks passed:** for Gram `diag(2,-4)`, bound 2 and primitive positive start `e`, the period map sends `e -> 3e+2f`, `f -> 4e+3f`, is invertible and preserves the form; the one-vector cycle is bounded. Zero/negative bounds return `None`, and nonprimitive/negative-square starts raise `ValueError`. Additional Gram matrices `diag(2,-6)`, `[[4,2],[2,-2]]`, and `diag(2,-4)` with bound 4 return cycle-family cardinalities 1, 1, and 2, respectively; each period has a two-sided inverse and every returned vector lies in its original parent with square in `(0,4]`. These specimens are retained on `reduction_cycle`. **Frozen runtime parity obtained:** the exact `edgewalk_rank2.py` at port commit `709f81a` was imported as a private temporary module into Sage, and all three cases agreed on every ordered cycle vector and every row of the period isometry, not only on cardinality. The proof of the iteration contract remains open. |

These paths are relative to `src/dzack_research/preamble/`. Continue at these owners; the lattice consumer must not acquire duplicate implementations.

## Next checks

The following checks are pending. Obtain actual results before closing their obligations.

1. **Full integral lift kernel (checked).** On `L=U + <2>`, reduction along the first null basis vector and `T=R.rational_lifts(R,id)`, targeted Sage execution confirms that the parameterization at the reduction generator `a` is integral and at `a/2` is not, its inverse recovers `a`, and the difference from the integral base point lies in the full integral kernel and acts on that base point to recover the lift at `a`. The finite parameter quotient has order two and is not substituted for the integral kernel.
2. **Infinite orbit closure obstruction (checked).** On U, the group generated by `diag(2,1/2)` now rejects an invariant integral overlattice through the finite containing-bound argument, raising `ValueError` that the orbit-generated submodule leaves its containing bound. The selected generator's inverse belongs to the generated subgroup after `21cef09ae5`; the generated matrix-group path does not require a full indefinite orthogonal-group engine. Since U is unimodular, its only integral overlattice is itself, while the generator does not preserve U. General membership decisions for arbitrary words in infinite matrix subgroups remain a separate obligation.
3. **Signed vectors on a retained subspace (checked).** On the formed subobject of U generated by `e+f` and `e-f`, targeted Sage execution confirms that `positive_vector()` and `negative_vector()` retain the subobject as parent, have positive and negative square respectively, and preserve their squares under the retained inclusion. The specimen is recorded at the owning `vector_of_sign` interface.
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

- **Finite power-object placement repaired:** on the `U+<2>` integral-lift residue quotient, the ordinary power set and finite-subset power object were both missing finite placement despite the source's proved finiteness. `PowerSets` and `FinitePowerSets` now accept `source.is_finite() is True` as well as explicit `FiniteSets()` membership. Both categorical placements passed targeted Sage checks, without enumeration.

- **Finite image placement repaired at the set owner:** a proved finite source of a set morphism now places its represented image in `Sets().Finite()` even before the source's category is refined. On the finite residue quotient for `U+<2>`, the identity map's image previously lacked finite placement; targeted Sage execution now gives `image in Sets().Finite()` as `True`. The image map and source remain retained; no enumeration was needed.

- **Finite residue-subset placement repaired at the set owner:** `Sets().condition_set` now recognizes a universe with a proved `is_finite() is True` even if its category is not yet refined to `FiniteSets()`. The `U+<2>` integral-lift residue quotient reports finite, and `integral_parameter_classes()` now belongs to `Sets().Finite()` with its inclusion still targeting that exact quotient. This placement check does not enumerate the integral-lift predicate or assert a residue count.

- **Finite generated-subgroup decision corrected:** for a finite containing group, an explicitly supplied but mismatched free-word witness no longer turns decidable membership into an unresolved proposition. After testing the word, membership falls back to the exact generated finite-subgroup engine. On `O(A_{U(2),q})` of order two, a mismatched word `t*t` for the nonidentity generator correctly returns membership `True`, and the trivial subgroup rejects it (`False`). For infinite containing groups the unresolved-proposition contract remains unchanged.

- **Generated-word evaluation uses its universal map:** `GeneratedSubgroups.membership_decision(candidate,word=...)` now evaluates the word through the morphism from the selected free group to the containing group, rather than independently multiplying extracted letters. The `diag(2,1/2)` specimen confirms the correct word `t*t` proves `g*g` and the mismatched word for `g` remains undecided. This retains the generating map as the owner of word evaluation.

- **Generated-subgroup witness validation corrected:** an explicitly supplied free-group word is evaluated before any direct generator/identity membership shortcut. The word `t*t` certifies `g*g` for `g=diag(2,1/2)` on the rational hyperbolic plane, but does not certify `g`; the latter query retains its undecided `is_member` proposition when accompanied by the mismatched word. Direct membership of the selected generator remains `True`. This distinguishes positive subgroup membership from validity of the supplied witness.

- **Bounded signed shell and sphere specimens verified:** for Gram `[2]`, target one-half of the selected generator and square bound zero, multiplier one gives no shell, while multiplier two gives a singleton shell; for Gram `[-2]` at target zero, bound `-2` and multiplier one give the two-point sphere. Both returned multiplier and cardinality were checked in Sage. The shell's existing doctest had assumed that the framing label was the Python integer `0`; the documented construction now reads the selected generator label instead, in the same commit as this status update.

- **Divisibility-sublattice specimen verified:** on Gram `diag(0,2)`, targeted Sage execution confirms that the inclusions for divisor zero, two, and three contain respectively `e` but not `f`; both `e` and `f`; and `e` and `3f` but not `f`. The defining inverse-image construction remains `ideal_dual(divisor).integral_pullback()`, retaining its pullback arrows. The selected membership checks are recorded at the lattice owner.

- **Twist functor isomorphism transport verified:** targeted Sage execution on U confirms that `TwistFunctor(2)` sends the identity isometry to an isomorphism with exactly the twisted source and target, whose inverse composes to the identity. The double sign twist returns the identical original parent. Its inverse-pair transport is already implemented; the stale audit assertion that it forgets isomorphism specialization has been corrected. General formal functoriality comparison remains open.

- **Integral hyperbolic-partner nontrivial norm-correction verified:** for Gram `[[0,2,0],[2,2,0],[0,0,-2]]`, the marked null vector has an integral null partner with pairing two; targeted Sage execution returned that partner in the original lattice. The Gram `[[0,2],[2,2]]` correctly raises `ValueError` because the minimal-pairing locus is empty. The positive case is now a specimen of the owner's finite norm-congruence selector, alongside the existing empty-locus specimen.

- **Rank-zero reduction-lift boundary checked:** reducing U along its first primitive null vector gives a zero-rank reduction and the associated marked-line lift torsor has a zero-rank parameter space. Targeted Sage execution constructs an integral base point. This boundary specimen is retained on `IsotropicReductionLiftTorsors` alongside the rank-one parameter and integral-kernel checks for `U + <2>`.

- **Nonidentity integral-torsor inverse and difference checked:** on `U + <2>`, the inverse trivialization of the lift at parameter `a` returns a nonidentity element of the full integral kernel, and the forward trivialization recovers the lift. The torsor now retains its already chosen base point as part of the trivialization presentation instead of reconstructing it by evaluating the identity through the represented action. Targeted Sage execution confirms the retained base point equals `integral_base_point()`, `difference(lift,base_point())` equals the inverse-trivialization coordinate, and the forward map of that difference recovers the lift.

- **Finite-image Schreier kernel generators:** `KernelSubgroups.schreier_generators()` now uses the ambient group's `finite_image_lifts` and chosen source generators, forming `t_(f(s)q)^-1 s t_q` for each image element `q` and source generator `s`. On `C4 -> C2`, targeted Sage execution confirms both produced generators belong to the kernel and generate a subgroup of the kernel's full cardinality. The infinite arithmetic orthogonal-group consumer still requires its ambient chosen generating set and its finite-image action; this finite example alone does not settle it.

- **Infinite-source Schreier specialization checked:** for `F_1 -> C2` sending the selected free generator to the order-two generator, `f.kernel().schreier_generators()` returns two elements in the kernel including `s^2` or its inverse (targeted Sage). The free-group morphism now exposes the kernel construction directly, using the same `KernelSubgroups` mathematical owner without requiring a GAP model. The live `f.kernel()` route and Schreier generators passed a focused Sage check.

- **Free-group image now retains its generating family:** `IndexedFreeGroupMorphism.image()` constructs the subgroup generated by the images of its finite chosen basis rather than invoking a nonexistent source GAP model. The map `F_1 -> C4` taking the generator to the square of the order-four generator has an image of order two containing the generator image (targeted Sage). An infinite free basis requires a non-finite generated-subgroup representation, and is not silently enumerated here.

- **Finite-index preimage Schreier generators:** `PreimageSubgroups.schreier_generators()` now enumerates the finite image with retained source lifts, selects right coset representatives modulo the image of the target subgroup, and constructs the Schreier words. The free-group morphism exposes `preimage_subgroup()` through its existing category owner. Focused Sage checks passed on `C4 -> C4`, with a proper order-two target subgroup (generators remain in the preimage and generate its full cardinality), and on `F_1 -> C4` with the same target subgroup (generators belong to the preimage and include `s^2` or its inverse). The arithmetic orthogonal-group cases still need their own selected finite-image morphisms and generators.

- **Subgroup image construction integrated:** `Subgroups.ParentMethods.image_under(f)` maps the generators of a represented generated subgroup, finite subgroup or Schreier-computable finite-index preimage and constructs their image subgroup in `f.codomain()`. It rejects an incompatible ambient source and predicate subgroups lacking a generator route. Targeted Sage execution on `C4 -> C2` confirms the order-two generated subgroup and the kernel as a preimage both have trivial images. Arithmetic orthogonal-group integration and independent acceptance remain open.

- **Discriminant orthogonal image uses the subgroup-image owner:** `L.Aut().discriminant_image()` now constructs the generated subgroup of the known `O(L)` generators and applies its `image_under(L.discriminant_representation())` rather than reproducing generator-image construction in the lattice morphism consumer. On `A2`, targeted Sage execution gives image order two, equal to `O(A_L)` order two. Indefinite groups without an available complete generating family and independent acceptance remain unresolved.

- **Stable orthogonal kernel consumes both generic group constructions:** for `L=A2`, `L.stable_orthogonal_group().schreier_generators()` returned four elements, all in the stable group, and its image under `L.discriminant_representation()` had order one (targeted Sage). The positive integration specimen is retained at the lattice owner; arithmetic indefinite cases with no known complete ambient generator family remain unresolved.

- **Nontrivial arithmetic preimage image checked:** on `A2`, the inverse image under `rho:O(L)->O(A_L)` of the subgroup generated by `O(A_L)`'s selected generators has two Schreier generators, and their image has order two, the full `O(A_L)` (targeted Sage). This exercises the full finite-index preimage to subgroup-image route rather than only the stable kernel with trivial image.

- **Preimage target ownership repaired:** `PreimageSubgroups` rejects a subgroup that is not a subgroup of the morphism's actual codomain before constructing the preimage predicate. Targeted Sage on `C4 -> C2` retains a valid preimage in `C4` and rejects a subgroup of `C4` incorrectly supplied as a subgroup of `C2`.

- **Nonnormal finite-index subgroup case checked:** in `S3`, the preimage of the order-two transposition subgroup along the group endomorphism fixing each selected generator has six Schreier words. All lie in the preimage and generate exactly the order-two subgroup (targeted Sage). This exercises the coset routing when the subgroup is not normal, unlike the earlier cyclic-group examples.

- **Nonnormal preimage image checked:** for the same `S3` endomorphism and order-two transposition subgroup, the image of the preimage under `Subgroups.image_under()` has order two and contains the transposition (targeted Sage). The combined preimage-to-image route now has a separating nonnormal subgroup specimen at its group owner.

- **General finite-index predicate Schreier construction added:** `PredicateSubgroups.finite_index_schreier_generators(index_bound=...)` uses coset membership to enumerate `rH` without a quotient morphism, then forms `t_(s r H)^-1 s r`. The explicit positive index bound prevents unbounded traversal when finiteness is not known. Targeted Sage checks passed for the nonnormal order-two transposition subgroup of `S3` (all outputs in the subgroup and generated subgroup order two) and for the index-two kernel predicate in infinite `F_1` (Schreier words include `s^2` or its inverse). This is not a finite-presentation algorithm, and no indefinite orthogonal-group generating set is inferred from it.

- **Finite-index bound rejection checked:** the order-two transposition subgroup of `S3` has index three. Calling its predicate Schreier construction with `index_bound=2` raises `ValueError` once a third coset is found (targeted Sage). The exceeded-bound failure specimen is retained on the group owner.

- **Index bound must be integral:** `finite_index_schreier_generators` now rejects nonintegral bounds rather than truncating them with `int`, as required for an index cardinality. A `1.5` bound on the full subgroup of `C2` raised the intended `ValueError` (targeted Sage).

- **Predicate subgroup images via explicit finite-index bound:** `Subgroups.image_under(f,index_bound=...)` now routes a subgroup specified only by membership to its coset-generated Schreier family. On the nonnormal transposition predicate subgroup of `S3`, the identity-on-generators group endomorphism gives an image of order two containing the transposition (targeted Sage). Without an index bound or another generating-family route, predicate subgroup images remain uncomputed.

- **Infinite predicate image route checked:** for the free group `F_1` mapped onto `C2`, the membership-only predicate subgroup cutting out the parity kernel has index two and `image_under(reduction,index_bound=2)` is the trivial subgroup of `C2` (targeted Sage). This verifies the general predicate generator/image composition does not require a finite source group.

- **Difference operation at the zero-parameter boundary:** on the reduction of U along its primitive null line, `integral_torsor().difference(origin,origin)` equals the kernel identity (targeted Sage, under 45 seconds). The general owner computes `inverse(left) * inverse(right).inverse()`, which is the group element taking `right` to `left` by the trivialization's action. The previous nonidentity comparison on `U + <2>` remains a separate unverified execution route; the smaller check does not discharge it.

- **Codimension-one Witt extension positive and negative cases verified:** over QQ in `U + <2>`, the hyperplane spanned by the first null generator and the norm-two generator has a one-dimensional radical. The partial isometry fixing the null direction and negating the norm-two direction extends to an ambient isometry; targeted Sage execution confirms its restriction through the retained subobject inclusion and the inverse identity. In the degenerate ambient Gram `diag(1,-1,0)`, the zero-form hyperplane spanned by `e+f` and the ambient radical `r` admits an abstract isometry interchanging them, but it cannot extend to the ambient space: targeted Sage execution rejects it with `ValueError` for failing to identify ambient radical intersections. Both specimens are retained at `LatticeIsometryMethods.witt_extension`.

- **Explicit perpendicular embeddings supported:** `LatticeIsometryMethods.extension_across` now accepts explicit `source_inclusion` and `target_inclusion` as the defining codimension-one embeddings, validates their domains against the isometry endpoints, and retains their scalar extensions through the orthogonal splittings. The existing canonical-inclusion route remains supported. A targeted Sage specimen on Gram `diag(2,2,-2)` verifies integral descent for the explicit-inclusion extension. General noncanonical embedding specimens and frozen-port reconciliation remain outstanding.

- **Endpoint validation corrected:** the explicit-inclusion validation now matches each embedding to its own isometry endpoint, rather than inferring an endpoint from whether the two ambient parent objects are identical. This fixes the source/target ambiguity when both embeddings land in one ambient lattice but are presented by distinct endpoint objects. A targeted Sage run confirmed the explicit-inclusion extension on Gram `diag(2,2,-2)` remains integral. The selected alternative subobject construction canonicalized to the same parent (`P is Q`), so a genuinely distinct-endpoint specimen remains open.

- **Distinct perpendicular endpoints verified:** on Gram `diag(2,2,-2)` with `v=e_0`, `w=e_1`, the perpendicular subobjects `P=v^perp` and `Q=w^perp` are distinct parents of rank two embedded in the same ambient lattice. The represented isometry `P -> Q` extends across the explicit embeddings and descends integrally (targeted Sage). This discharges the previously open distinct-endpoint regression specimen; it does not by itself settle general formed embeddings not presented as canonical subobjects.

- **Mismatched explicit endpoint rejected:** on the same distinct subobjects `P` and `Q`, supplying `Q.inclusion()` as the source embedding for an isometry `P -> Q` raises `ValueError` identifying the incorrect endpoint (targeted Sage). This separates actual arrow-domain validation from rank and orthogonality alone.

- **Integral-descent nonintegral boundary verified:** on the rational hyperbolic plane, the isometry with diagonal entries `2` and `1/2` does not carry the integral lattice U into itself. Targeted Sage execution confirms `is_integral_on(U)` is false and `integral_restriction(U,U)` returns `None`. The two-sided forward/inverse distinction for a proper integral embedding remains a separate comparison obligation.

- **Noncanonical formed embedding restriction verified:** on the same Gram `diag(2,2,-2)`, let `P=v^perp`, `j:P -> L` its inclusion, and `a=-id_P`. The explicit source embedding `j*a` differs from `j`, although both have the same image. Extending the identity of `P` with source embedding `j*a` and target embedding `j` gives an integral ambient isometry `h` satisfying `h*(j*a)=j` on every generator (targeted Sage). This checks that `extension_across` uses the *supplied arrows*, not only the endpoint objects or their images.

- Each audit operation is decided by its mathematical definition: return object, failure case, inclusions and inverse maps follow from the mathematics, not from what a consumer calls.
- **Two-plane recovery repaired at the decomposition owner:** `two_hyperbolic_plane_splitting()` uses the integral hyperbolic index to decide existence, then searches integral null vectors exhaustively by increasing coordinate height when PARI selects one with divisibility greater than one. The genus criterion is exact for a lattice whose genus contains `2U`, by Nikulin's indefinite genus uniqueness theorem and `rank(L) >= length(A_L)+4`; the analogous bound after removing one `U` is `rank >= length(A)+2`. Targeted Sage checks passed on `U(2)+U+U`, a permuted Gram presentation, and a nontrivial integral basis change. The resulting isometry retains the original reduction-owned comparison maps and has a two-sided inverse. Broader frozen-port parity and independent acceptance remain open.
- **Two-plane structural comparison extended:** targeted Sage execution on a nontrivial rank-four Gram presentation confirms both hyperbolic biproduct factors have rank two, the splitting and its inverse agree on the retained summand injections, and the two compositions are identities. The earlier abstraction-audit assertion that this operation bypasses reductions was stale and has been corrected at its contract row. Formal equivalence and independent acceptance remain open.
- Follow the group-consumer dependencies named in the TODO only where they remain necessary for the issue-401 contract.
- Update the audit, TODO, and relevant complaints. Their statements that every specimen remains unexecuted are stale. Keep all still-required proof work at its existing owner.
- Complete the applicable formatting and targeted checks, commit coherent units, and follow the repository's synchronization rules. Do not mark the task complete from source inspection or a few successful specimens alone.

## Workspace boundary

Other work is active in this checkout. Preserve the unrelated changes under `research/`, the untracked research notes, and `tests/lattices/test_lattice_database_owner_contracts.py`. Recheck status before staging and stage exact task paths. Preserve concurrent commits. The port's `research-401-primitives` branch is outside this implementation unit.
