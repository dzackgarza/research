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

### Core inverse data and its actual base-arrow representation

An isomorphism datum u:A->B, v:B->A asserts v*u=id_A and u*v=id_B.
Its explicit law check must retain undecided equality separately from a
false equation. The current generic `CoreMor._element_constructor_`
calls `CategoricalIsomorphism(...,verify=True)`; that constructor computes
both composites and rejects any inverse equation not literally True.
The known-pair entry already passes `verify=False`. The actual generic
parent also declares the legacy `Element=CategoricalIsomorphism`, bypassing
the generated base-arrow route. Its future repair must initialize the
selected base-arrow representation, not merely rename that declaration.

**Searched / Found / Conclusion:** read the complete Core and categorical
isomorphism definitions, the selected element-class branch, known-pair
identity/composition routes and direct stronger consumers. Plane linear
right equivalences and torsion-form isometries explicitly retain supplied
inverse data with `verify=False`; the latter already has a separate
validator. The bounded protected search found positive swap and identity
pairs, but no explicit invalid inverse-pair rejection fixture.
The existing `placement-owner-coremor` owns these law-check and actual
representation obligations. Aut-family selection reuses fixed diagonal
categories without invoking pair ingress, so the completed
`placement-owner-autcategoryconstruction` does not require this repair.

### Protected Aut specimens conflate a fixed category and a group realization

The two-element set has four endomaps and two automorphisms; its
automorphism group is C2. Those true theorems in
`tests/objects/test_isomorphisms_of_a_two_element_set.sage` do not by
themselves select an ordinary group-engine representation for the fixed
categorical Aut object. Its `.order()`/`.is_isomorphic_to()` calls need
that representation, and its no-argument `.identity()` must distinguish
the identity automorphism from the identity two-arrow on an arrow object.
The actual fixed entries `.one()`/`identity_automorphism()` and
`.identity(arrow_object)` retain that distinction. The existing
`triage-long-tail` owns protected spelling/representation reconciliation;
the swap-square, identity-square and counting assertions remain under T.
The protected file is unchanged and unexecuted.

### Protected well-order reversal expects eager validation

The three-point reversal r(k)=2-k is not monotone: 0<=1, but r(0)=2 is
not <=r(1)=1. The protected
`tests/sets/test_cardinal_and_ordinal_order_morphisms.sage` expects this
failure during default construction. Under `OWN-22`, that true failed
inequality is diagnosed by an explicit check, while construction retains
the defining map. The existing `triage-long-tail` node owns reconciliation
of that timing. T retains the failed reversal, positive monotone maps and
the fact that the composite of two reversals is the identity. The protected
file is unchanged and unexecuted; no source repair remains for this entry.



### Slice and coslice arrows still need their actual base-arrow initialization

An object of `C/X` or `X/C` is an object of the actual `C` with its chosen
structure arrow (`CAT-16`, `CAT-20`, `OWN-16`). Its nonfixed triangle edge
is therefore a `C`-arrow. The generic `SliceMor` and `CosliceMor` select
the legacy `CommutativeSquare -> NaturalTransformationMorphism -> Morphism`
implementation; it retains the square but does not initialize the selected
module, group or other base-arrow representation promised by the declared
`C.Mor`. In the module slice over zero, the identity triangle on a rank-one
free module must carry its actual linear-map operations; the dual coslice
has the same requirement.

The exact associative-unital algebra slice over its canonical scalar
algebra now has its declared `_AugmentedAlgebraMor` implementation.
That route initializes the actual lower algebra map on the structured
endpoints and retains the existing square. This completes the scalar
augmentation route only; it does not settle generic module, group or
coslice initialization.

**Searched / Found / Conclusion:** read the slice/coslice carrier
`_with_structure` construction, their genuine `C` declaration, the fixed
Mor graph, generated-arrow selection and constructor transport. The
existing `_mor_endpoints_in_supercategory` and
`_transport_initialization_to_mor` protocols supply the correct repair
boundary, exemplified by the actual equivariant-arrow constructor. Merely
replacing `Element` with `ElementMethods` is insufficient: the retained
edge has the original carrier endpoints, whereas the newly structured
parents are distinct, and a module constructor can otherwise misread that
edge as generator data.

The existing `placement-owner-slicemor` and `placement-owner-coslicemor`
own this independent lower-arrow initialization. Their exact source
transformation, nonfixed edge, carrier transport and generated providers
must be delivered together. Reusing the common `identity_at` or deferring
the square's equation check neither depends on nor supplies that missing
initialization. No new prerequisite or executed result is asserted.

### Selected exterior computations and the protected augmentation spelling

The existing exterior-power realization selects a framed free module or
a chosen finite presentation for its higher pieces. The current
arbitrary-target exterior extension also selects a finite module-generating
family. Mathematical existence does not select those computational data;
the corresponding construction assertions remain named under T. The
inverse factorial comparison uses an actual rational coefficient
structure (apart from the proved zero-module case), and an arbitrary
whole divided-power algebra map still needs a procedure establishing
compatibility with the divided powers. These are the bounded existing
computation frontiers, not assertions that no other algorithm exists.

`tests/algebras/test_power_algebras.sage` still uses
`divided.augmentation(value)` for scalar evaluation, whereas the declared
augmentation operation returns the structural map. The true equation
`epsilon(1+x+gamma_2(y))=1` is retained under T; `triage-long-tail` owns
reconciliation of the protected spelling. The file is unchanged and
unexecuted. The source findings of `placement-owner-alternatingalgebras`
are resolved; its complete audit belongs in that delivery commit.

### Finite coefficient module kernels need exact coefficient presentations

For `R=Zmod(4)`, the kernel of multiplication by `2` is the actual submodule
`2R`. It is isomorphic to `R/2R`, not to a free rank-one `R`-module. The
Lie algebra `L=R h direct_sum R e` with `[h,e]=2e` therefore has center
`2L`, since centrality of `a h+b e` is exactly `2a=2b=0`.

**Source evidence (2026-10-11):** read the direct modular-ring placement,
the framed-free kernel hook, `_selected_presentation_kernel`, its PID/CAP
dispatch, and the Singular coefficient-presentation and kernel adapters.
The direct `Zmod(4)` object has no selected PID or exact polynomial cover
for this computation. Its nonzero adjoint kernel reaches the existing
assertion requiring an exact polynomial coefficient presentation. A
possible abstract quotient presentation does not itself transport this
literal coefficient ring, its modules or their maps.

**Searched / Found / Conclusion:** the existing module equalizer and
intersection constructions supply the Lie-center route, with the actual
kernel inclusion when computed. Their selected coefficient adapter is the
remaining boundary for the direct modular-ring case. The existing
`placement-owner-selectedfinitepresentationmodules` owns that computation
and transport review. Confidence is high for these read source paths;
no runtime result, general solver-absence claim or new prerequisite is
asserted. Retain the named computation boundary at the Lie consumer.

### Generic commutative-algebra specimens impose stronger laws

A commutative bilinear product need not be associative or unital. For the
algebra over `QQ` with `x^2=y`, `xy=yx=x`, `y^2=0`, the commutant is the
whole module. Its nucleus, hence its magma centre, is zero: for `z=ax+by`,
the associators with `(x,y)` and `(x,x)` are `-ay` and `by`. Commutativity
alone therefore does not justify the centre-rank-two expectation in
`tests/algebras/test_algebra_preservation.sage`. The earlier algebra-owner
source bank already records the correct centre; the protected expectation
remains unreconciled. Its bare product-table input also predates the actual
bilinear-map ingress used by the current algebra constructor.

The same ingress mismatch remains in `tests/algebras/test_lie_cokernels.sage`:
its raw tables enter root `Algebras(QQ)`, which neither interprets a table
as the defining tensor-domain morphism nor infers Lie axioms. The asserted
Cartan-ideal theorem in `sl_2(QQ)` is true: brackets with `h` give `2e,-2f`,
so the generated Lie ideal is the whole algebra. Its protected spelling
still needs the actual bilinear bracket and explicit Lie entry; the
existing `triage-long-tail` reconciliation retains this valid theorem.

Likewise, the standard polynomial tensor cocone is a coproduct in
associative unital commutative algebras, with unit-preserving arrows. The
root theory admits the maps `p -> (p(0),0)` and `q -> (0,q(0))` from
`QQ[x]` and `QQ[y]` to `QQ x QQ`. Their images of `1` differ, so there is
no factor through the tensor cocone's shared unit.
`tests/algebras/test_native_free_algebra_module_factor.sage` nevertheless
asks root `Algebras(QQ).Commutative()` for that coproduct.

**Actual supplier boundary:** root `Algebras.Commutative` inherits
`Modules.SubcategoryMethods.coproduct`, its module colimit supplier and
the module biproduct construction. That route supplies no algebra
multiplication or root-algebra coproduct universal property. The genuine
tensor supplier is on the distinct associative-unital commutative owner;
it is not selected from the two inputs' stronger object properties.

**Searched / Found / Conclusion:** read both complete protected
specimens, the common centre and tensor-classified product construction,
the root and associative-unital commutative owners, and the inherited
module coproduct/biproduct route. The equations above establish two false
specification identifications, not runtime failures. Existing
`triage-long-tail` owns reconciliation of the protected specifications;
`placement-owner-modules` owns the remaining inherited module-supplier
applicability. Preserve the valid centre, bilinear product and tensor
constructions. No test was changed or run, and this independent remainder
is not a prerequisite of the root commutative owner's three operations.

### Free algebra constructions do not uniformly supply associative projective sources

Projectivity of an associative `R`-algebra is relative to a specified class
of algebra maps. For underlying surjections, `T_R(M)` is projective when
`M` is projective. A commutative polynomial algebra need not be projective
in the associative theory: `QQ[x,y]` has no section of abelianization from
`QQ<x,y>`, since the degree-two commutator of any lifted generators is
`xy-yx`. Likewise, `T_ZZ(ZZ/2)` cannot lift its degree-one generator through
`ZZ<x> -> T_ZZ(ZZ/2)` while preserving its relation `2x=0`.

**Source evidence (2026-10-11):** `free_algebras.py` places native symmetric
and tensor constructions in the common `FreeAlgebras`; the relationful
construction in `finitely_presented_algebras.py` can also inherit this
placement through `GradedFreeAlgebras`. Neither placement alone proves
associative projectivity. The finite-generation classifier now selects the
existing intersection of `TensorAlgebras(R)` and `Modules(R).Projective()`,
and the actual underlying-set surjection family. Other uses of the common
free-algebra placement still require their own theory-specific review.

**Retained computation frontier:** the sparse construction on an actual
framed-free generating module supplies whole-module projectivity, and its
tensor algebra supplies qualified associative algebra projectivity. Other
represented projective generating modules still need the corresponding
property placement or an actual comparison/transport. Their homogeneous
pieces do not by themselves establish that the needed whole-object
placement is present. Preserve all defining maps; absence of placement is
not a theorem of nonprojectivity.

**Searched / Found / Conclusion:** read `FreeAlgebras`, its native and
relationful producers, the sparse producer, the tensor/module categories,
the finite-generation selector and `Resolutions`. Found the distinctions
above; the existing `placement-owner-freealgebras` owns the unresolved
theory/placement review. Confidence is high for these source paths; no
runtime failure or global absence theorem is claimed. This does not gate
the repaired finite-generation selector on another repository.

### Selected algebra presentations exceed the polynomial computations

An associative finite presentation retains its actual tensor or polynomial
source `P`, indexed relations, quotient `q:P -> A` and lift. A commutative
quotient can retain a noncommutative source: for example
`QQ[x,y] = QQ<x,y>/(xy-yx)`. Commutativity of `A` therefore does not
justify a polynomial computation on its selected `P`.

**Remaining computations:** general nonhomogeneous tensor relations and
coefficient realizations outside the selected exact-field homogeneous
reduction or existing linear-module construction still need a maintained
two-sided normal-form supplier. The valid presentation
`QQ<x,y>/(xy-1)` is a small nonhomogeneous boundary specimen. General
scalar-kernel intersections, membership with undecided coefficients and
torsion decisions outside the retained module/domain regimes remain
named computation frontiers. These are not negative mathematical claims.
Their defining assertions remain under terminal T's chosen-presentation
obligations; the placement pass is source delivery, not executed acceptance.

**Remaining transport:** the selected scalar-restriction computation uses
actual polynomial presentations of both the coefficient extension and its
algebra, their selected lifts, and the literal coefficient structure map.
Other associative restrictions retain their actual module, multiplication,
unit and scalar map. Their finite-presentation transport still needs an
appropriate associative supplier at
`placement-owner-restrictedscalarsalgebras`. No negative finite-presentation
claim follows from the missing selected computation. Polynomial
differentials/coproducts, commutative radical transport and lifted module
relations likewise retain their explicit actual-presentation hypotheses.

**Protected result-type finding (2026-10-11):** the last assertion of
`tests/constructions/test_algebra_presentation_normal_form_terms_construct.sage`
asks `terms.cardinality() == cardinal(2)`. Independently of that line,
API-02 defines coordinates as a finitely supported function on the chosen
basis, with support its condition subset; it says, “No coordinate readout
has a dictionary interface.” SET-01 requires the owned mathematical
collection. The former implementation returned a Python dictionary and
the protected line asks the cardinality of the wrong type. For
`QQ[x,y]/(xy)`, the true statement is that the coefficient function of
`x+y` has support cardinality two, value one on the two supported basis
labels, and reconstructs `x+y`. Retain this required mathematical
correction for T; no protected expectation was edited to match code.

**Searched / Found / Conclusion:** the complete selected-presentation
owner, quotient/lift adapters, actual tensor-module supplier, existing
coordinate function, scalar-restriction construction and changed
coefficient consumers were read. API-02, SET-01, CAT-01/CAT-05 and
DEV-67--69 supply no public-dictionary exception or permission to infer
polynomial input from quotient commutativity. The current explicit
frontiers and the protected type mismatch are source findings; no
runtime failure or universal absence theorem is claimed.

### A finite-generation reference confuses a property with a chosen family

A group generated by a finite family `S` is generated as a monoid by the
finite family `S union inverse(S)`. Thus the additive group `ZZ` is also
finitely generated as a monoid, by `1,-1`. The singleton `1` failing to
generate it as a monoid distinguishes a chosen family, not the existential
finite-generation property.

**Observed source (2026-10-11):** this project's vault reference
`references/categorical-presentation-principles.md`, in “Declaration and
pullback are factorization, not doctrine,” states the contrary `ZZ`
counterexample as a placement rule. The statement and its immediate context
were read directly after the required memory search. Correct that reference
and decisions relying on it within the existing
`placement-owner-ownedgroups-finitelygeneratedasmagma` work; no new
dependency is created. The counterexample is mathematically false with high
confidence by the explicit two-element generating family. Its downstream
uses have not been globally inspected, and no execution is claimed.

### General degree-zero algebras need represented homogeneous inclusions

For a strictly commutative differential graded `R`-algebra `B`, its degree-zero
algebra is the actual module `B^0` with the induced product and unit. For
`B=k[z] tensor exterior_k(e)` with `|z|=0`, `|e|=1` and zero differential,
`B^0=k[z]`; the coefficient algebra alone does not determine it. The de Rham
adjunction uses that algebra and the inclusion `B^0 -> B`, extending
`a |-> f(a)` by `da |-> d(f(a))`.

**Source evidence (2026-10-11):** `functors/de_rham.py`'s
`_DegreeZeroDGAFunctor._degree_zero_data` supplies exact de Rham data,
justified standard scalar restrictions, represented graded direct sums,
and finite framed homogeneous subobjects. A general represented homogeneous
piece with its inclusion and lift remains unavailable through this selected
route; it reaches a named assertion. The resulting algebra can also lack the
selected presentation required by `_DeRhamAdjunction._counit_component`.

**Searched / Found / Conclusion:** read the degree-zero functor, restricted
graded algebra, graded direct sum and graded-module piece suppliers; found
the constructions above, not a general inclusion/lift supplier. This is a
source-level computation frontier, not an executed failure or a claim that
every other representation lacks the mathematics. Confidence is high for
these inspected paths; other suppliers and runtime behavior are uninspected.
The existing `placement-owner-differentialgradedalgebras` owns the piece
construction; `placement-owner-kahlerdifferentialmodules` owns the needed
algebra-presentation remainder. No external repository gates either owner.
Mathematics: [de Rham construction](https://stacks.math.columbia.edu/tag/0FKF)
and [strict commutativity](https://stacks.math.columbia.edu/tag/061U).

### General Kähler differentials exceed the selected finite conormal computation

For every retained commutative ring map `R -> A`, `Omega^1_(A/R)` represents
`R`-derivations from `A`. In particular, for any index set `I`,
`Omega^1_(R[x_i : i in I]/R)` is the direct sum of copies of `R[x_i] dx_i`.
Finiteness is not a hypothesis of that universal construction.

**Source evidence (2026-10-11):** the path from the commutative algebra's
`kahler_differentials` and `de_rham_algebra` to
`derivations._commutative_presentation_data` uses selected polynomial or
quotient data with literally known finite polynomial labels. Infinite or
undecided label finiteness reaches the named conormal/differential assertion
before traversal. Existing localization and relative-zero cases remain.
An algebra constructed only on a degree-zero module can lack this selected
presentation even when it is isomorphic to its coefficient ring.

**Searched / Found / Conclusion:** read the Kähler, derivation, de Rham and
degree-zero suppliers and their selected presentation branches. Found the
finite conormal construction; the general infinite presentation computation
and presentation of a newly constructed degree-zero algebra remain at the
existing `placement-owner-kahlerdifferentialmodules` owner. Confidence is high
for the inspected source boundary; no execution or global absence claim is
made. Mathematics: [differentials and the conormal sequence](https://stacks.math.columbia.edu/tag/00RM).

### Cohomology needs general represented cycle quotients

For an arbitrary cochain complex of `R`-modules, `H^p` is the module of cycles
modulo boundaries, with its actual kernel, image, factorization and quotient
maps. It need not be finitely presented. For algebraic de Rham cohomology of
`F2[x]`, `H^0=F2[x^2]` and `H^1=F2[x^2] x dx` have infinite `F2`-dimension.

**Source evidence (2026-10-11):** `functors/cohomology.py` has the general
codomain `Modules(R)`, while `modules/cochain_complexes.py:_cohomology`
still selects a chosen finite cycle presentation after obtaining the actual
kernel, image and boundary-in-cycle factorization. The unresolved computation
is the general represented cycle quotient, not the functor's mathematical
codomain. The existing `placement-owner-cohomologymodules` owns this remainder
and its unavailable-computation assertions.

**Searched / Found / Conclusion:** read the cohomology functor, cycles,
boundaries, `_cohomology`, and the de Rham consumer; found the selected finite
construction and the named frontier, not a general unbounded solver along
this route. Confidence is high for this source trace; broader algorithms
and runtime behavior are uninspected. No execution is claimed. The displayed
`F2[x]` equations follow directly from the [de Rham differential](https://stacks.math.columbia.edu/tag/0FKF).

### A coefficient presentation omits group-action relations

**Observed during placement-owner-affinegschemes (2026-10-11):** asking
the selected relation supplier of a linearized group action returned the
coefficient module's R-linear relations as if they were all relations of
the R[G]-framing. For the trivial C2-action on the coefficient carrier
QQ[C2], that coefficient module is free, but the R[G]-framing has the
additional nonzero relations (g-1)e_i. Empty coefficient relations cannot
prove that its arbitrary generator images define an R[G]-linear map.

**Correction and retained remainder:** _CoefficientModuleEngine now keeps
the complete coefficient presentation on unformed_module() and returns
the existing missing-relation value None outside canonical regular
cases. ModuleMorphism consequently retains its linearity proposition;
tensor and scalar-restriction presentation algorithms reach their
existing named assertions. The genuine left regular action retains its
rank-one group-algebra frame only through the actual cached action
functor, while the trivial action on the same carrier receives no such
frame. A complete nonregular R[G]-relation computation remains inside
the existing placement-owner-modulesovergroupalgebra node.

**Dependency and inspected boundary:** exact coefficient module and
BG-action -> existing _equip_action scalar representation and spanning
family -> actual R[G]-kernel supplier -> module-map, tensor and
scalar-restriction consumers. The builder, _CoefficientModuleEngine,
GroupAlgebras.regular_representation and these selected consumers were
read as source. No runtime execution or test modification occurred.

### A module annihilator uses the additive endomorphism representation

For a left module M over a possibly noncommutative ring R, the defining
scalar representation is rho:R->End_Ab(U(M)), and Ann_R(M)=ker(rho).
Left multiplication by r need not be R-linear: on the regular left
module of M_2(QQ), r=E12 and s=E21 give r*s=E11 but s*r=E22.
Thus writing the scalar representation with target End_R(M) adds an
unavailable commutativity hypothesis.

`categories/modules/pure/modules.py:_ring_morphism_defining_module_action`
already constructs the actual ring arrow into End_Ab(U(M)). The two
`End_R(M)` mentions in its adjacent generic `annihilator` docstring still
state the wrong target. This documentation remainder belongs to the
existing `placement-owner-modules` in TODO.md; the AdditiveMor scalar
repair does not alter the already correct defining map.


### An integral isotropic partner with minimal pairing can fail to exist

[Research #401](https://github.com/dzackgarza/research/issues/401) requests,
for a primitive isotropic vector `v`, an integral isotropic vector `w` with
`b(v,w) = div(v)`. This requires an existence hypothesis. In the lattice
with Gram matrix `[[0,2],[2,1]]`, take `v = e`. Then `div(e) = 2`.
The pairing equation forces `w = a*e + f`, whose square is `4*a + 1`.
There is no integral solution. Evenness alone is insufficient: for
`[[0,2],[2,2]]` the same equation gives square `4*a + 2`.

The general dependency is the integral point locus cut out by `q(w)=0`
and `b(v,w)=div(v)` in the affine fibre of the pairing morphism. A Bezout
partner solves only the linear equation. The rational Witt construction
in `categories/lattices.py` corrects its square over the fraction field.
For an even integral lattice and `div(v)=1`, that correction is integral.

The inspected `find_hyperbolic_pair` in `sage-indefinite-port` at `b3fd95d`
instead forms `2*d*h - q(h)*v` after selecting a nonorthogonal `h`, giving
pairing `2*d^2`. Its bounded initial search also supplies no minimal-pairing
existence decision. Its consumers include the port's two-hyperbolic-plane
decomposition. The API must distinguish an integral solution, an empty
locus, and an unsupported computation. Research now decides the finite-rank
partner locus through the norm congruence on `K/(ZZ*v+2d*K)`, with K the
pairing kernel. Formal comparison, port contract reconciliation, and
independent acceptance remain owned by
[`indefinite-port-primitives`](TODO.md#indefinite-port-primitives).

### An affine integral parameter locus can contain a rational kernel

The affine-locus request in [research #401](https://github.com/dzackgarza/research/issues/401)
needs to retain the kernel of its parameter map. For `A: QQ^r -> QQ^n`,
the parameters with `c + A(lambda)` integral form a coset of
`A^-1(ZZ^n)`, when nonempty. If `A` is not injective, this group contains
`ker(A)` over `QQ` and need not be a finitely generated integral lattice.
For example, `A(s,t)=s+t` gives `ZZ*(1,0) + QQ*(1,-1)`.

At port revision `b3fd95d`, `IsometryExtensionTorsor.integral_parameters`
in `indefinite/isotropic_lifts.py` lifts generators of
`im(A) intersect ZZ^n` with `solve_right`, then constructs their integral
span. This omits `ker(A)` when the directions are dependent. The public
construction must retain the full inverse image as a scalar-restricted
submodule, or explicitly require injective parameterization. Its defining
data are the parameter morphism, the integral target inclusion, and their
pullback; Smith form only supplies a realization. The existing restricted
scalar finite-span constructor represents the lattice part. Research's
general affine inverse-image construction now retains the rational kernel,
both maps and the translation torsor. The port adoption and independent
acceptance of this construction remain in
[`indefinite-port-primitives`](TODO.md#indefinite-port-primitives).

### A commensurating group need not admit an invariant overlattice

The invariant-overlattice request in [research #401](https://github.com/dzackgarza/research/issues/401)
requires an existence hypothesis. On the rational hyperbolic plane, the
isometry `diag(2,1/2)` commensurates `ZZ^2`. The module generated by its
positive and negative powers is `ZZ[1/2]^2`, which is not a lattice. Thus
commensuration alone does not imply termination of repeated integral spans.

At port revision `b3fd95d`, `IntegralStructureAction._invariant_overlattice`
in `groups/integral_structures.py` repeats spans under generators and their
inverses until stabilization. This loop does not establish a bound on the
denominators. The general object is the submodule generated by the group
orbit. A finite acting group or a supplied finite stable containing module
provides a finite-generation case. Integral-valuedness of the restricted
form is separate: on `U`, the involution `e -> 2f, f -> e/2` generates
`ZZ*(e/2) + ZZ*f`, whose cross-pairing is `1/2`. Its finite orbit span
cannot be an integral-valued overlattice. Research's orbit-span construction
now retains the action and both inclusions. For nondegenerate integral L,
the bound `L^sharp subset L/abs(det L)` makes the integral-overlattice
decision terminate. Degenerate lattices use the finite-group realization.
Formal comparison, port adoption, and independent acceptance remain in
[`indefinite-port-primitives`](TODO.md#indefinite-port-primitives).

### Isotropic-reduction lifts need a kernel torsor with nonlinear evaluation

The frozen lift-family contract in [research #401](https://github.com/dzackgarza/research/issues/401)
requires the fibre of the reduction map on isometries. Its defining data
are the isotropic embeddings, the map on the marked isotropic line, the
isometry of the reductions, the kernel group, and its action on the fibre.
A chosen base point trivializes this torsor; it does not supply the action.

For the marked-vector case in a nondegenerate rational quadratic space,
the transvection parameter space is additive, but evaluation in matrices
is quadratic. On `U + <2>`, with basis `e,f,a`, the transvection with
parameter `t*a` maps `f` to `f+t*a-t^2*e`. The midpoint of the matrices
at `t=1` and `t=-1` maps `f` to `f-e`, which has square `-2`.
An affine-linear matrix family therefore does not represent these lifts.
See the cited transvection formula and the complete dependency account in
[the abstraction audit](docs/issue-401-abstraction-audit.md#15-lifts-through-isotropic-reductions--frozen-rrational_liftstargetpsi).

At port `b3fd95d`, `IsometryExtensionTorsor` stores a particular map and
linear directions, and `IsotropicVectorSection.rational_lift` supplies
empty directions. In research, `IsotropicReductions` retains the quotient
data. Research now constructs the marked-line lift torsor by transporting
the regular kernel action through a base lift. It retains transvection
parameters, nonlinear evaluation, and the integral-kernel action on the
integral descent locus. A finite parameter quotient now supplies complete
integral residue selection and a chosen integral torsor when nonempty.
Port adoption and formal comparison remain unresolved. The searched formal
slice and partial Witt/action declarations are recorded in the audit.
Their location or formalization and the comparison proofs belong to
lean-categories. Computational source repair follows the mathematical
construction traced above. Remediation belongs to
[`indefinite-port-primitives`](TODO.md#indefinite-port-primitives).

### Clearing denominators requires similarity embeddings

For chosen integral structures `L -> V` and `E -> W` and a rational
isometry `phi: V -> W`, denominator clearing constructs `sigma=N*phi`.
The resulting form multiplier is `N^2`, and the integral map need not be
onto. For `L=E=U` and `phi=diag(2,1/2)`, the least denominator is two,
`sigma=diag(4,1)` has index four, and its form multiplier is four.

The dependency is the denominator ideal of a rational module map,
factorization through integral subobjects, and transport of the form
equation. Research now constructs the denominator ideal at the module-map
owner and factors the scaled map through the integral target inclusion.
The formed monomorphism retains the rational isometry, ideal, denominator
factor, and value map. The [frozen amendment](https://github.com/dzackgarza/research/issues/401#issuecomment-6065197711)
specifies `.scale()` as the least denominator factor `N`; the form multiplier
is `N^2`.
The [audit](docs/issue-401-abstraction-audit.md#13-clearing-denominators-of-a-rational-isometry--frozen-phiintegral_similarityle-and-scale)
records the inspected formal change-of-value and module foundations,
the unresolved denominator-ideal/similarity-embedding declarations,
and the request boundary at lean-categories and port #33. Formal comparison,
contract reconciliation, and independent acceptance belong to
[`indefinite-port-primitives`](TODO.md#indefinite-port-primitives).

### Issue 401 migration does not match the frozen public contract

Resolved 2026-10-09: research does not answer to a consumer's frozen contract. Each issue-401 operation is placed at its mathematical owner and accepted by true assertions there (`TODO.md#indefinite-port-primitives`). Where the port calls a name or expects a result type that the mathematics does not give, that is the port's correction to make.

### Hodge-isometry planning did not assign the general Hodge categories

The `hodge-lattice-isometries` node previously referred to compatible Hodge
structures and a period stabilizer, while its research prerequisite only
asked for a dependency trace. Neither assigned delivery of the general
categories of pure and mixed Hodge structures, their morphisms or tensor
constructions. A Hodge-isometry group requires the Hodge object and pairing
first; its inclusion in the lattice orthogonal group is a forgetful map.

The inspected `_QuarticK3HodgeData` in
`categories/schemes/geometric_cohomology.py` supplies cohomology, a space of
holomorphic forms and Hodge numbers. Those methods do not supply a Hodge
filtration embedded in complexified integral cohomology, or general mixed
Hodge objects and their morphisms. `modules/hodge.py` implements Hodge-star
operations on formed modules; those are a different construction.

The formal source `LeanCategories/Homological/SpectralSequenceConvergence.lean`
has `FiniteIncreasingFiltration`, `FiniteDecreasingFiltration` and their
`gradedPiece` on a fixed object of an abelian category. The adjacent
`IncreasingFiltration` has quotient maps and a quotient functor. These give
actual retained subobjects and cokernels, not the whole category of
filtered objects with filtration-preserving arrows. `Modules/Total.lean`
supplies `ModulesOverRings` and its fixed-ring fibres and reindexing;
`Modules/Mathlib.lean` imports module change of rings.
`FOUNDATIONS.md` §61.1–61.2 gives pure/polarized Hodge definitions in prose.
Preamble `GradedModules`, scalar-change functors and semilinear arrows are
partial presentation owners. No named method is taken as proof that the
required Hodge category or comparison theorem exists.

The [upstream request](../gitclones/lean-categories/COMPLAINTS.md#hodge-structures-need-filtered-module-categories-and-their-comparison-maps)
records the named category chain, source locators, searched formal slice
and remaining search boundary. The formal source slice was inspected at
`lean-categories` revision `1008f05540c101e1fc0e1ad719ff6c6092508116`.
The additional LeanSearch
queries for filtered vector spaces and mixed Hodge structures returned
indexing-category filteredness and ring/module filtrations, respectively;
neither result supplies the requested Hodge categories. This is bounded
source evidence, not a global absence claim.

The research dependency chain is now
`filtered-objects-and-associated-graded` ->
`filtered-scalar-extension-and-conjugation` ->
`pure-and-mixed-hodge-structures` ->
`hodge-tensors-pairings-and-polarizations` -> `hodge-lattice-isometries`.
Each node names the categories, defining data, arrows and comparison maps
it must consume from the formal side before presenting them. K3
automorphisms and the other K3 consumers inherit this chain.

The computational consumer also requires complete generators and the inclusion
of the Hodge-isometry subgroup in the lattice orthogonal group, followed by its
discriminant action. The inspected `StabilizerSubgroups` in
`categories/group/predicate_subgroups.py` retains an action and predicate;
that alone does not compute this subgroup. The exact-period computation and
its finite completeness bound are assigned to
`hodge-isometry-subgroup-computation`, after the Hodge-category chain.
The Torelli and Fourier–Mukai nodes depend explicitly on that output.
Support for bounded enumeration with a real-algebraic Hodge metric remains
an engine-capability question, not an asserted absence from maintained systems.

### K3 automorphism pullback lacks explicit chamber and Torelli consumers

The cospan `P_S -> O(A_S) <- O_Hdg(T)` requires the actual ample-chamber
stabilizer, both discriminant actions, and integral extension followed by
strong Torelli. The inspected source supplies a generic product/equalizer
formula in `abstract_categories/cat.py`, discriminant representations and a
positive-cone subgroup in `categories/lattices.py`, and image lifts in
`categories/lattice_morphisms.py`. These are partial prerequisites; they do
not establish the K3 automorphism identification. The positive-cone subgroup
currently accepts signature `(1,n)` only for `n >= 1`, so it also does not
cover the Picard-rank-one positive ray.

Source searches in `src/dzack_research/preamble` for ample-cone stabilizers
and signed Miranda–Morrison constructions found no corresponding owner.
The existing TODO graph covered Hodge groups and lattice gluing but did not
name their ample-chamber or Torelli consumer. This is a source and queue
coverage finding, not a runtime claim or a claim that `lean-categories`
lacks these foundations. The upstream request is to locate or formalize
cones and chamber actions, their stabilizers and transporters, strong
Torelli, and the signed discriminant obstruction at their mathematical
owners. The dependency path runs from K3 cohomology and Hodge lattices
through chamber stabilizers and discriminant actions to the group pullback
and geometric automorphisms. Remediation is recorded in TODO nodes
`k3-ample-cones-and-stabilizers`,
`signed-discriminant-lifting-obstructions`, and
`k3-automorphisms-by-torelli`, with the full cospan coverage recorded there.

### Backing-core constructor narrowing and colimit lifting block integration specimens

The backing core must preserve the constructor of a fixed-endpoint Mor under
property restriction and must use a selected forgetful functor's supplied
coequalizer lifting. These are prerequisites for owned subset inclusions and
presented modules, respectively.

Fresh Sage execution on rack at sage-categories `5867543f` demonstrates two
failures. `Mor(Sets)(X,X).Monomorphisms().construction_owner()` returns the
unfixed Mor family, so supplying a map raises a missing-`codomain` error.
`SetSubobjects.from_predicate` reaches that route. Separately, the existing
presented-module consumer over M2(F2) registers the required colimit lift but
`FullSubcategory.colimit_construction` delegates to its ambient without
consulting selected-functor liftings; the coequalizer construction fails.

The inspected core already implements nested group construction, composite
structure transport, exact-category implementation installation and lifted
universal maps, with passing consumers in this assessment. The gap is the
shared constructor/dispatch route, not a claim that those foundations are
absent. The source owners, minimal reproduction, runtime and exact coverage
boundary are in [the execution assessment](docs/sage-categories-readiness.md).
The backing-core repair belongs to sage-categories; its research consumers
are `constructor-discovery` and `optional-sage-categories-property-layer` in
TODO. Later module factorization assertions remain unverified until quotient
construction succeeds.

### Multiplicative integer submonoids do not supply the fixed power specimens

The AdditiveMonoids source pass on 2026-10-11 read the unchanged
tests/constructions/test_group_actions_construct.sage and
tests/groups/test_multiplicative_submonoids_of_the_integers.sage.
Their multiplicative integer assertions require 8 in the submonoid
generated by 2, 6 outside it, and the canonical factor of <4> into <2>
fixing 4. These are true statements: <2> consists of 2^n for n>=0,
and 4=2^2.

The owned ZZ has no authored submonoid entry. Its existing
generated_submonoid([2]) instead reaches _SubmonoidEngine, whose
generator branch recognizes one and listed generators but supplies no
general power-membership calculation. Consequently the existing
MonoidMorphism generator-containment factor cannot discharge the
displayed <4> into <2> specimen through that supplier. The predicate
construction for odd integers is a different, multiplicative route.

**Owning boundary:** the existing `placement-owner-monoids` and
`placement-owner-monoidmor` rows in TODO.md retain these obligations.
The current additive NN constructors require zero and addition, while
these integer constructions require one and multiplication. Their
different defining laws and protected assertions must both remain.
The shared generator-containment conjunction preserves predicate-valued
answers, but is not a missing multiplicative membership algorithm.

**Coverage boundary:** the named protected sources, the authored
submonoid entries in group/magmas.py, their engine in group/submonoids.py
and the exact MonoidMorphism factor supplier were read. No test or
runtime result is claimed, no assertion was changed, and no new
prerequisite was filed.


### Fixed Mor categories with discrete 2-Morphisms do not realize their discrete universal constructions

For an ordinary represented fixed Mor category `Mor_C(A,B)` whose selected
2-Mor family is discrete, the objects are the represented arrows `A -> B` and
there is only an identity 2-morphism on each object.  Its finite universal
constructions are therefore exactly those of the discrete category on that
arrow set.  In particular `Mor_Set(*,*)` for a singleton set has one object and
is the terminal category, so every represented finite diagram into it has the
unique arrow object as both limit and colimit.  This statement does not apply
to special fixed Mor categories that declare a non-discrete 2-Mor, such as
functor categories with natural transformations.

Observed during `category-method-coverage-sweep` on 2026-09-25:
`FixedMorCategory`/`CategoricalMor`
(`categories/abstract_categories/mor_categories.py`) select
`_DiscreteTwoMorCategoryOf` for their ordinary 2-Mor, but source search finds no
`_categorical_product`, `_categorical_coproduct`, `_categorical_equalizer`,
`_categorical_coequalizer`, or family realization on that discrete fixed-Mor
route.  Consequently even the one-object `End_Set(*)` cannot answer the
universal operations inherited from `Cat`.  `_FunctorCategory` is explicitly
excluded: it overrides the 2-Mor with natural transformations and therefore is
not evidence that `MorCategories()` as a whole is discrete.  This is source
evidence; pre-T execution remains suspended by `DEV-58`.

**Dependency path:** fixed Mor with `_DiscreteTwoMorCategoryOf` -> discrete
category on represented arrows -> selected universal construction with forced
identity 2-morphisms -> the inherited `Cat` product/(co)equalizer and
`Limits`/`Colimits` operations.
**Consumers:** `test_mor_categories_construct.sage`, induced functors between
ordinary fixed Mor categories, and any construction using such a Mor category
as a diagram target.
**Coverage boundary:** the ordinary discrete fixed-Mor route and the singleton
set specimen were inspected; no claim is made about non-discrete specializations.
Repair: `discrete-fixed-mor-universal-constructions` in [TODO.md](TODO.md).

### Direct MorCategories ingress retains inconsistent represented endpoints

A fixed-Mor category H is an object of MorCategories. Its functor Mor to K
must use the exact represented endpoints Cat.object(H) and Cat.object(K),
and its classifying family's admission record must name those same objects.

Source inspection on 2026-10-11 found that direct
MorCategories().Mor(H,K) uses the default raw endpoint ingress. The inherited
Cat construction returns the genuine functor category with represented
endpoints, but the generic family records it under raw H,K; its own
identity-sensitive lookup then cannot recover that record from the returned
endpoints. Supplying Cat.object(H), Cat.object(K) already works. This is a
construction/admission defect, not missing mathematics or evidence that the
functor category is discrete.

The shared _MorCategoryOf boundary now normalizes the objects of individual
Mor/End/Aut families, as required by the completed commutative-additive
Mor-family pass. Direct MorCategories itself is not such a family.
Its remaining entry belongs to `placement-owner-morcategories` in TODO.md.
The retained dependency is exact category representation -> inherited
functor Mor -> coherent admission record; no other repository gates it.
The remedy must reuse Cat.object and preserve the actual Functor and natural
transformation constructions. M1 / DEV-58 leaves the corresponding execution
under T. No new mathematical foundation or formalization request is indicated.

### Discrete categories do not realize universal constructions that exist

The discrete category on one object is the terminal category.  Every diagram
into it has exactly one cone and one cocone, hence its limit and colimit are the
unique object.  More generally, a finite product, coproduct, equalizer or
coequalizer in a represented discrete category exists exactly when the
corresponding universal cone/cocone exists; when it exists its structure maps
are forced identities.  Nonexistence for other discrete diagrams is part of
the mathematics and should be reported as such, not conflated with an absent
implementation.

Observed during `category-method-coverage-sweep` on 2026-09-25:
`DiscreteCategory` (`categories/abstract_categories/functors.py`) represents
objects and their identity-only Mor correctly, but defines none of the
`_categorical_product`, `_categorical_coproduct`, `_categorical_equalizer`,
`_categorical_coequalizer`, or family construction hooks inherited from
`Cat.ParentMethods`.  Thus even `Disc({*})` cannot realize the finite universal
constructions that are mathematically forced.  The same omission prevents the
generic selected `Limits`/`Colimits` reduction from reaching its valid answer.
This is source evidence; pre-T execution remains suspended by `DEV-58`.

**Dependency path:** represented discrete category -> existence criterion for
the relevant universal cone/cocone -> selected universal construction with its
identity structure maps -> generic product/(co)equalizer reduction ->
`Limits`/`Colimits` and their functors.
**Consumers:** `test_discrete_categories_construct.sage`, finite diagram
constructions, and every consumer using a discrete target as an actual
category rather than merely as an indexing shape.
**Coverage boundary:** the one-object case and the missing construction hooks
were inspected. Repair: `discrete-category-universal-constructions` in
[TODO.md](TODO.md).

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
| `AugmentedSimplexCategory`, `NN` | bounds checks (correct in shape) | `IntegerRange(n)`, `NonNegativeIntegers()` |

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

### Chosen generators are encoded as a global axiom instead of a resolution

A chosen generating epimorphism, a chosen presentation and a chosen syzygy
tower are truncations of one datum, a resolution of the object by free (or
`P`-projective) objects, and they belong to a category of resolutions over
`C` (`CAT-29`). The tree encodes the first of them as a global `Framed`
axiom on `Objects`, with `FramedModules(R)` and `FramedAlgebras(R)` as its
specializations, and decides membership by whether a framing was stored on
the object. Every object is resolvable -- the counit `F(UX) ->> X` starts the
canonical comonadic resolution -- so the axiom names no property, and Sage's
joins, which close under axioms, propagate it across branches as if it were
one.

Observed on 2026-09-25: the meet of `ZZ.category()` and `RR.category()`
contains `Algebras(ZZ).Associative().Unital().Framed()`, `ZZ` is not placed
there, and `RR.coerce_map_from(ZZ)` raises `ValueError`, so `4 / pi**2`
fails. Placing `ZZ` with its empty algebra framing moves the failure to
`QQ.coerce_map_from(ZZ)`: the meet then carries `Framed` on `Modules(ZZ)`.
Rack's separation of algebra framing from module framing (`09215fd7e`) made
framings relative to their category, which the global axiom cannot express.

**Dependency path:** resolutions over `C` (`lean-categories` `FOUNDATIONS.md`
§76-77 for the additive case, extension filed as dzackgarza/lean-categories#62;
simplicial objects over a projective class in
general) -> truncations and finiteness properties -> chosen generators and
presentations -> coercion and every consumer of chosen generators.
**Consumers:** coercion of session integers into `QQ` and `RR`; algebra
generators, presentation display, module generators, the matrix-unit algebra
structure of `End_R(F)`; the `tests/functions` Lebesgue tests and the D4
Gaussian heuristic.
**Coverage boundary:** the `Framed` population was counted by the `rg` in the
`framed-axiom-retired` node; the coercion was observed for `ZZ` into `QQ` and
`RR` only. Repair: `categories-of-resolutions`, `framed-axiom-retired`,
`integers-coerce-into-rationals-and-reals` in [TODO.md](TODO.md).

### Indefinite integral lattices of rank at least three have no exact represented-value witness backend

For an integral lattice `L` and integer `n`, `representation_vector(n)` must
return an integral vector `v in L` with `b(v, v) = n`, or establish that none
exists. Rational solvability of `b(v, v) = n` is a different problem.
`Lattices(ZZ)` answers `represents(n)` and `representation_vector(n)` for
`n = 0` (PARI `qfsolve`, cleared to a primitive integral vector), for definite
`L` (`vectors_of_square`, inside the region of Cassels, *Rational Quadratic
Forms*, Ch. 9, §1, (1.2)--(1.3)) and for indefinite `L` of rank 2 (PARI
`qfbsolve` when `L tensor QQ` is anisotropic, a divisor search in the basis of
a primitive isotropic vector and its Bezout partner otherwise). For indefinite
`L` of rank at least 3 and `n != 0`, `represents(n)` reads the local
conditions from `Genus.local_representations`; it answers `True` in rank at
least 4 (Cassels, Ch. 9, Thm. 1.5) and in rank 3 when the genus has one spinor
genus (Cassels, Ch. 9, Thm. 1.3 and Ch. 11, Thm. 1.4).

Two operations remain without a route. `representation_vector(n)` has no
integral witness in that regime and asserts. `represents(n)` in rank 3, when
the genus has more than one spinor genus and the local conditions hold,
returns the proposition `represents(L, n)`, since `n` can be a spinor
exception. Installed Sage, Hecke and OSCAR source supplies rational
quadratic-space isotropy, isometry-class representation and hyperbolic
decomposition, but no integral witness for a prescribed norm, so
`QuadraticForm.solve` and Hecke's `represents` cannot supply it.

The sources in the Zotero library (searched 2026-10-09) state strong
approximation as an existence theorem with no bound and no construction:
O'Meara, *Introduction to Quadratic Forms*, 104:3 (vectors of a prescribed
norm, dimension at least 4), 104:4 (rotations, dimension at least 3) and
104:5 (class equals proper spinor genus for indefinite dimension at least 3);
Kneser--Scharlau, *Quadratische Formen*, (22.1), (24.1), (25.2) and (25.3).
Cassels, Ch. 9, Lemma 6.1, puts the integral representations of `n != 0` in
finitely many orbits of the integral proper orthogonal group; its proof
completes a primitive representation `b` to a basis of `ZZ^n` in which the
form becomes one of a finite set of forms `h`, so a witness is the first
column of an integral isometry from `h` to the form of `L`. No installed
engine constructs an integral isometry between indefinite lattices (Hecke
0.39.21 `is_isometric_with_isometry` has no indefinite method). Grunewald--Segal,
"On the integer solutions of quadratic equations" (J. reine angew. Math. 569,
2004), Thm. 0.1 and §2, Step 3, Case 2, decide representability in every rank
with a finite set containing a representative of each such orbit. That set is
constructed in §5 of Grunewald--Segal, "How to solve a quadratic equation in
integers" (Math. Proc. Cambridge Philos. Soc. 89, 1981, 1--5), which is not in
the library. Generators of the integral orthogonal group (Grunewald--Segal,
Ann. Math. 112, 1980, Algorithm B, in the library; Siegel, "Zur Theorie der
quadratischen Formen", Nachr. Akad. Wiss. Göttingen 1972, Satz 9, not in the
library) are needed only for congruence conditions, which `represents` does
not impose. The spinor-exception papers of Schulze-Pillot and of
Earnest--Hsia, and a theorem bounding a smallest integral solution of
`b(x, x) = n`, are not in the library. Kneser, "Klassenzahlen indefiniter
quadratischer Formen in drei oder mehr Veränderlichen" (1956), is in the
library and was not read for this.

**Dependency path:** local integral representability (delivered) -> a finite
set of representatives of the integral proper orthogonal orbits on the
vectors of norm `n` (Cassels, Ch. 9, Lemma 6.1; constructed in
Grunewald--Segal 1981, §5) -> exact integral witness or exact
nonrepresentation in every indefinite rank at least 3, the rank-3 spinor
exceptions included.
**Consumers:** `Lattices(ZZ).representation_vector(n)` and, in rank 3,
`represents(n)`. The distinguishing specimens are `U + A_1 + A_1` at
`n = 2`, `<1> + <1> + <-1> + <-1>` at `n = 5` and `U + <1>` at `n = 3`: each
`represents` call answers `True` and each `representation_vector` call
asserts.
**Coverage boundary:** Sage's quadratic-form and binary-form sources, the
installed Hecke/Oscar quadratic-form sources, the repository's lattice engine
capability map and the four books above were inspected. No indefinite ternary
genus with more than one spinor genus was found among the specimens tried
(`A_2 + <-18>` and `-A_2 + <18>` each have one). The owner ruled on 2026-10-09
that the preamble owns the algorithm. Repair is the
`higher-rank-integral-lattice-representation` node in [TODO.md](TODO.md).

### Genera of integral lattices are formalized without finiteness, parity or classification

The genus of a nondegenerate integral lattice `L` is the set of isometry
classes of lattices locally isometric to `L` at every place [PS24, Def.
1.9.1]. Every genus is finite [PS24, Cor. 1.10.4], from the Eisenstein-Hermite
theorem for nondegenerate lattices of bounded discriminant [PS24, Thm.
1.10.1]; its cardinality is the class number [PS24, Def. 1.10.5]. Parity is a
genus invariant [PS24, Prop. 1.9.2(2)]. The signature and the discriminant
quadratic form determine the genus of an even lattice [nikulin1979integral,
Cor. 1.9.4], and [nikulin1979integral, Thm. 1.10.1] decides which pairs occur.
An odd genus is fixed by the signature and the local symbols at every prime
[CS10, Ch. 15, §7]. A genus is a union of spinor genera, a power of 2 in
number, and an indefinite spinor genus of rank at least 3 is one class [CS10,
Ch. 15, §9.1, Thm. 14].

The preamble presents the genus: `L.genus()` is an object of `FiniteSets()`
whose elements are the isometry classes of the genus, `representatives()`
enumerates them, `class_number()` is its cardinality, `is_even()` reads its
parity, equality compares the signature, the determinant and the local
symbols, and `Lattices(ZZ).genus(signature, q)` constructs an even genus from
Nikulin's data. `lean-categories` (`LeanCategories/Lattices/Valued/`, checkout
`1008f05`, 2026-10-03) states `SameGenus` (`LocalGlobal.lean:133`), the set of
genera `IntegralLatticeGenus` (`:223`) with the surjection
`isometryClassToGenus` (`:226`, `:231`), the full subcategory `GenusCat L` of
lattices in the genus of `L` (`:244`), the class set `genusClassSet L`
(`Mass.lean:92`), `classNumber L` given a `Finite` instance (`Mass.lean:101`),
rank, signature and determinant as genus invariants
(`GenusInvariants.lean:192`, `:208`, `:238`), and finiteness only for
positive definite `L` (`genus_finite`, `ReducedBasis.lean:458`). A search of
`LeanCategories/` for `SameGenus`, `genusSetoid`, `genusClassSet`,
`classNumber`, `GenusCat` and `Nikulin` found no parity invariant, no
finiteness of an indefinite genus, neither of Nikulin's results and no
classification of odd genera by local symbols.

**Dependency path:** local isometry at every place -> `SameGenus` -> the class
set of a genus -> its finiteness and its class number -> parity and the
discriminant quadratic form as genus invariants -> the classification of even
genera by signature and discriminant form, and of odd genera by local symbols.
**Consumers:** `L.genus()` and `Lattices(ZZ).genus(signature, q)`;
`Lattices(ZZ).isometry_classes`, which groups a family by genus; lattice-db
duplicate detection (`latticedb.records.definite_isometry_problems`).
**Coverage boundary:** `_Genus` and `_genus_classes` in
`categories/lattices.py`, Sage's `sage/quadratic_forms/genera/genus.py`, and
the `lean-categories` files above were inspected. The finiteness of an
indefinite binary genus rests on PS24, Cor. 1.10.4; no binary-form source was
opened.
**Request (not yet filed):** `lean-categories` formalizes the finiteness of
`genusClassSet L` for every nondegenerate `L` [PS24, Thm. 1.10.1, Cor.
1.10.4]; parity as a genus invariant [PS24, Prop. 1.9.2(2)]; the discriminant
quadratic form as a genus invariant and Nikulin's classification and existence
theorem for even genera [nikulin1979integral, Cor. 1.9.4, Thm. 1.10.1]; and
the classification of genera by local symbols [CS10, Ch. 15, §7]. Repair is the
`genera-present-their-formalization` node in [TODO.md](TODO.md).

### Dynamic peeking stands in for category membership across the preamble

`AGENTS.md`, *Dynamic peeking is prohibited; the category is the type*, bans
`getattr`, `setattr`, `hasattr`, `isinstance`, `type(...)` comparisons and
`cast` in mathematical code, and `try`/`except` in owned runtime code, outside
four named exceptions: `__contains__`, `_element_constructor_`, a documented
Sage runtime protocol or an `OWN-06` adapter, and `TYPE_CHECKING`
declarations. On 2026-10-08, `rg -n 'isinstance\(|getattr\(|hasattr\(|setattr\(|\bcast\(|^\s*try:' src/dzack_research/preamble`
listed 383 `isinstance`, 29 `getattr`, 1 `hasattr`, 5 `setattr`, 9 `cast` and
40 `try:` sites; the `isinstance`, `getattr`, `hasattr`, `setattr` and `cast`
sites were heaviest in `categories/modules/` (112), `categories/algebras/`
(63) and `categories/rings/` (51). Which sites fall inside an exception was not
inspected. One that does not: `LocalGenusSymbol.__eq__`
(`categories/lattices.py:413`) decides equality by
`isinstance(other, LocalGenusSymbol)`, and `LocalGenusSymbol` is a plain
Python class in no category, so `A2.genus().local_symbol(3)`, the isometry
class of `A2 ⊗ ZZ_3` [CS10, Ch. 15, §7], is no preamble object.

**Dependency path:** category membership as the type -> routing by
`case`/`match` on membership -> every public result an object of its category.
**Consumers:** every routing site the tell lists; `L.genus().local_symbol(p)`
and `excess(p)`.
**Coverage boundary:** the counts come from the tell above; only
`LocalGenusSymbol` and the genus code in `categories/lattices.py` were read.
Repair is the `membership-replaces-dynamic-peeking` node in
[TODO.md](TODO.md).

### Arithmetic reflection subgroups outside the definite and Vinberg regimes have no exact backend

For a nondegenerate integral lattice `L`, `W(L)` is generated by every
integral reflection. The current tree has exact finite enumeration in the
definite case and a Vinberg chamber algorithm in signature `(1,n)`/`(n,1)`.
For indefinite signature with both inertia indices at least two, roots of an
admissible norm need not form a finite set and no chamber algorithm in the
current engine population certifies that a finite search found every
reflection generator. A bounded search therefore constructs only a subgroup,
not `W(L)`.

There is a second, distinct gap even in the hyperbolic case. For a proper norm
set `S`, `W_S(L)` is generated by all reflections in roots of norms in `S`.
Filtering the simple roots of a Vinberg chamber is not equivalent to this:
other `S`-roots can lie in the full `W(L)`-orbit structure and need not be
simple for the full chamber. Magma and standard Coxeter software construct
reflection subgroups from supplied roots/root data, but the inspected APIs do
not construct this infinite norm-defined root family from the lattice itself.

**Dependency path:** integral root criterion and finite admissible norm set ->
complete root-orbit/reflection-subgroup enumeration -> owned subgroup of
`O(L)`; in the hyperbolic restricted case, a complete norm-defined reflection
subgroup/chamber construction.
**Consumers:** `Lattices.reflection_group(S)`, the Coxeter-system structure of
reflection groups, and later abelianization/growth computations.
**Coverage boundary:** current Sage/OSCAR/Hecke/project reflection machinery and
Magma's documented real-reflection/reflection-subgroup APIs were inspected.
No exact backend was found for either missing construction. Repair requires
the two reflection-engine ruling nodes in [TODO.md](TODO.md).

### A Vinberg invariant is not yet a point of the projective line

The invariant of two mirrors is the point `[4 b(r,s)^2 : q(r) q(s)]` of
`P^1`; for normals of positive square it dehomogenizes to `4 g^2`, where `g`
is the entry of the Gram matrix of the unit normals (Vinberg, *Hyperbolic
reflection groups*, 1985, section 1). An `R`-point of `P^1_R` is a morphism
`Spec R -> P^1_R`. `VinbergInvariantMatrices.vinberg_invariant`
(`categories/vinberg_invariants.py`) asks the owned scheme
`ProjectiveSpaces(R)(1)` to accept the pair `[numerator, denominator]`, and
that scheme has no element constructor: the call raises `AttributeError`
for `_element_constructor_`. So `vinberg_invariant`, `vertex_label`,
`edge_label` and `weighted_graph` fail on every invariant matrix, while
`vinberg_ratio` (the dehomogenized value) works.
**Dependency path:** owned `ProjectiveSpaces(R)(n)` -> its `R`-points as
`Mor(Spec R, P^n_R)` -> the Vinberg invariant -> the labelled graph of
mirrors. `Schemes(R).projective_morphism_from_coordinates` builds such a
morphism from a basepoint-free coordinate family; over `ZZ` the pair
`(4 b^2, q(r) q(s))` need not generate the unit ideal (`(4, 4)` for two
roots of square `-2` with product `1`), so the point is that of the
primitive pair, which exists because `P^1(ZZ) = P^1(QQ)`.
**Consumers:** `VinbergInvariantMatrices.vinberg_invariant`, its graph
labels and `weighted_graph`; the lattice-db graph cards that read them.
**Coverage boundary:** the scheme route was not executed on 2026-10-07:
`Spec ZZ.projective_morphism_from_coordinates` failed earlier, in
`_restriction_to_base`, with `RngMorphism.__init__() got an unexpected
keyword argument 'evaluator'` from the module-morphism construction.
Repair: `vinberg-invariants-are-points-of-the-projective-line` in TODO.

### A Coxeter diagram is not constructed by its category

An object of a category is constructed by the category applied to its
defining data. A Coxeter diagram on a finite set `V` is determined by its
Coxeter matrix `m: V x V -> Card`, and a finite family of roots of a
lattice determines one through the pairings of its roots. `CoxeterDiagrams`
(`categories/coxeter_diagrams.py`) constructs diagrams only through
`from_coxeter_matrix`, `from_roots` and `from_cartan_type`; the category has
no element constructor, so `CoxeterDiagrams()(datum)` raises
`NotImplementedError` from Sage's `Category.__call__` (observed 2026-10-07).
**Dependency path:** the Coxeter matrix as the owned function
`m: V x V -> Card` -> the category applied to `m`, or to a family of roots
-> the diagram, equal to the one the `from_*` route builds.
**Partial capability:** `from_coxeter_matrix` and `from_roots` build the
diagram; their Coxeter matrices compare equal on equal data.
**Consumers:** `tests/lattices/test_coxeter.sage` (4 failures),
`test_coxeter_subdiagrams.sage` (5 failures), `test_vinberg_invariants.sage`
(through `rooted_diagram` and the Cartan-type and matrix calls),
`test_coxeter_gram_archive.sage` and `tests/objects/test_coxeter_diagram_a2.sage`.
**Coverage boundary:** the Cartan-type datum enters as a Sage `CartanType`,
which *Coxeter diagrams answer subdiagram orders and drawings as Sage
objects* already records as engine input.
Repair: `coxeter-diagrams-construct-from-their-data` in TODO.

### Free session functions construct objects

A matrix is an element of the topological `R`-module `Mat_{n x m}(R)`, and a
linear map is an element of `Hom_R(R^m, R^n)`. The map between them is
neither injective nor surjective in general. The session's free `matrix`
(`preamble/language_runtime.py:63`) reads the ring from the entries and
returns an element of `ring.matrix_space(n, m)`, which `MatrixSpaces`
presents as a Mor object. So one free function hides the parent and turns a
matrix into a map. Five other free session functions also return new
objects without their category: `finite_ordered_set`, `nikulin_invariants`,
`signature_pair`, `signature_pairs` and `reflection_cosines` (session
survey, 2026-10-08). The code-wrangling helpers `lmap`, `lzip`, `zipsum` and
`to_var_names` are typed loosely.
**Consumers:** `tests/lattices/test_vinberg_invariants.sage:145` and
`tests/user_simulations/test_newcomer_session.sage:126` call `matrix(ZZ, ...)`.
Repair: `session-objects-are-built-by-their-parents` in TODO.

### Coxeter diagrams answer subdiagram orders and drawings as Sage objects

The induced subdiagrams of a Coxeter diagram, ordered by inclusion of
their vertex sets, form a finite partially ordered set, and so do the
`Aut`-orbits of subdiagrams under the order that inclusion induces on orbits. `CoxeterDiagrams`
(`categories/coxeter_diagrams.py`) returns both as Sage `Poset` objects
through `_subdiagram_poset_on` and `_subdiagram_orbit_poset_on`: the six
public methods `subdiagram_poset`, `elliptic_subdiagram_poset`,
`parabolic_subdiagram_poset`, `subdiagram_orbit_poset`,
`elliptic_subdiagram_orbit_poset` and `parabolic_subdiagram_orbit_poset`
put a raw engine object on the public surface (`OWN-03`). The owned
`PartiallyOrderedSets()` (`categories/sets/set_categories.py`) has no
constructor of a finite poset from its underlying set and its order
relation, so no owned object can be returned today. `plot()` returns a
Sage `Graphics`.
The same category still admits engine input: `from_coxeter_matrix`
accepts a Sage `CoxeterMatrix`, `from_cartan_type` a Sage `CartanType`,
and `Groups.Coxeter` (`categories/group/groups.py`) passes any argument
other than the owned Coxeter matrix to Sage's `CoxeterGroup` unchanged
(`OWN-04`). `lexicon/geometry.py` exports Sage's `CoxeterMatrix`.
**Dependency path:** finite posets in `PartiallyOrderedSets()` from
`(X, <=)` -> inclusion of subdiagrams and the order it induces on
`Aut`-orbits -> the public poset methods.
**Partial capability:** the Coxeter matrix is the owned function
`m: V x V -> Card` (`coxeter_matrix()`), and the Coxeter graph and the root
intersection graph are objects of `LabelledGraphs()`.
**Consumers:** the six poset methods, their callers in
`tests/lattices/test_coxeter_subdiagrams.sage`, and the expectation files
under `tests/constructions/` that ask for their cardinalities.
Repair: `coxeter-diagram-orders-are-owned-posets` in TODO.

**Observed 2026-10-07:** `Groups.Coxeter(["A", 2])` and
`Groups.Coxeter(D.coxeter_matrix())` both raise `NotImplementedError`.
`_own_group` places the raised group at construction, and
`_owned_group_category` calls `_is_abelian_witness`, which calls
`is_abelian()` on Sage's `CoxeterMatrixGroup`; Sage's `Group.is_abelian`
raises for that class. Deciding commutativity is a computation done at
construction (`OWN-22`). Repair: `construction-is-instant` in TODO.

### Satake diagrams and real forms have no formalization

A Satake diagram is a Dynkin diagram with black nodes `X` and a diagram
involution `tau`, and it is one exactly when `(X, tau)` is admissible (Kolb,
*Quantum symmetric Kac-Moody pairs*, 2014, Definition 2.3; Araki 1962). The
preamble now presents the category (`categories/satake_diagrams.py`) with
admissibility as its validator, and lattice-db builds its Satake cards as its
objects. A GitHub code search of `dzackgarza/lean-categories` for `Satake`
and `real form` on 2026-10-07 found only the Baily-Borel/Satake
compactification row FC11-C19-U035 and quadratic-form uses of "real form":
neither the diagrams, the admissibility condition, nor real forms of a
semisimple Lie algebra. This host has no local checkout.
**Dependency path:** Cartan matrix of a finite-type root basis -> its
automorphisms `Aut(A, X)` and the longest element `w_X` of a parabolic
subgroup -> admissible pairs -> the real form a Satake diagram presents.
**Consumers:** `SatakeDiagrams.is_admissible`; the lattice-db Satake cards;
the real-form functor of `satake-diagrams-present-real-forms` in TODO.
**Request:** `lean-categories` formalizes admissible pairs from Kolb,
Definition 2.3, and real forms of complex semisimple Lie algebras with Araki's
classification by Satake diagrams. Filed as dzackgarza/lean-categories#86.

### Complex realization acts only on objects, and analytification exists only on affine spaces

For a field `k` of characteristic 0 and an embedding `sigma: k -> CC`, the
complex realization `X -> X(CC)_sigma` is a functor from schemes of finite type
over `k` to topological spaces, and the comparison theorem (Freitag-Kiehl
[FK88] Ch. I Thm 11.6) identifies the l-adic Betti numbers of `X_{kbar}` with
the Betti numbers of `X(CC)_sigma`. `Schemes(k).FiniteType.complex_realization`
(`categories/schemes/schemes.py`) acts on objects only: no morphism `f: X -> Y`
has an image `f(CC)`, so no induced map `H^k(Y(CC); ZZ) -> H^k(X(CC); ZZ)`
exists. Analytification exists only as `AffineSpaces(k).analytification`
(`schemes.py`, `analytic_families.py`), on affine spaces and polynomial maps.
The realization computes integral cohomology for projective space, smooth
complete toric varieties and smooth projective complete intersections only, and
the embedding `sigma` is constructed only for `k = QQ`.

**Dependency path:** analytification of a scheme of finite type -> its action on
morphisms -> complex realization as a functor -> induced maps on singular
cohomology; separately, the embeddings of a number field into `CC`.
**Consumers:** `Schemes(k).FiniteType.betti_number` and `euler_characteristic`
on schemes that are neither toric nor complete intersections, including the
branched double covers of `P^1 x P^1` in
`tests/schemes/test_horikawa_k3_family.sage` and
`tests/schemes/test_horikawa_enriques_family.sage` (`chi = 24`); every
pullback on cohomology.
**Coverage boundary:** the realization owner in `geometric_cohomology.py`, the
analytification owner in `analytic_families.py` and the scheme categories in
`schemes.py` were inspected. Repair is the `complex-realization-is-a-functor`
node in [TODO.md](TODO.md).

### The Hodge structure of a smooth complete intersection is present only for the quartic surface

A smooth complete intersection `X` of multidegree `(d_1, ..., d_r)` in `P^n`
over a field of characteristic 0 has Hodge numbers determined by `n` and the
`d_i`; outside the middle degree they are those of projective space. The tree's
`ProjectiveCompleteIntersections(k).hodge_structure()`
(`categories/schemes/complete_intersections.py`) builds `_QuarticK3HodgeData`
only, so every other multidegree has no Hodge numbers.

**Dependency path:** smooth projective complete intersection -> Lefschetz
hyperplane theorem outside the middle degree -> generating function of the
middle-degree Hodge numbers -> `hodge_number(p, q)`.
**Consumers:** `Schemes(k).Proper().Smooth().hodge_number` on complete
intersections; the `hodge_poincare` series stored on lattice-database
geometric cards.
**Coverage boundary:** the Zotero library was searched for a source stating the
general formula. The item labelled SGA 7 II (`CMV4MC6A`, LNM 340) holds an
extraction of SGA 7 I; the item labelled SGA 4 volume 305 (`ZXUPYTKS`) holds
tome 1, Exposés I to IV; SGA 4½ (`HRUVM374`) holds a table of contents only;
Hirzebruch, *Topological Methods in Algebraic Geometry*, is absent. Dimca
[Dim92] (B34) states the Steenbrink formula for quasismooth weighted
hypersurfaces only. Repair is the `complete-intersection-hodge-sources` and
`complete-intersection-hodge-structure` nodes in [TODO.md](TODO.md).

### Geometric lattice-database cards store no Betti numbers

Of the 37 cards in `lattice-database/geometric-objects/`, only
`k3-surface.md` stores `betti_numbers`. The others store a Hodge series, a
linked cohomology lattice or neither, so no card-level Betti number or Euler
characteristic exists to compare with `Schemes(k).FiniteType.betti_number`.

**Dependency path:** a cited source or a constructed preamble object ->
`b_k` and `chi` on the card.
**Consumers:** the lattice-database geometric-object pages and every
comparison of a card with the preamble's realization.
**Coverage boundary:** the frontmatter of every card under
`lattice-database/geometric-objects/` was read. Repair is the
`geometric-cards-store-betti-numbers` node in [TODO.md](TODO.md).

### Arrows of one Mor are built on handwritten hosts beside its element class

A morphism `A -> B` of a category `C` is an element of `C.Mor(A, B)`, and its
type is the one the Mor category graph generates. The Mors of sets, of
injections and surjections, of finite `G`-sets, of modules, of graded modules
of cones and cocones and of the core of a category now construct every
arrow as their element class, and so do the module arrows of scalar change,
localization, algebra augmentations and units, tensor classifiers, sheaf
modules and connections, the inclusions of subsets, subgroups and
submonoids, the class functions of finite groups, and the module
monomorphisms that a construction gives (subobject inclusions, localized
inclusions, homogeneous pieces, correlations of nondegenerate forms, the
inclusion of a fractional ideal into `Frac(R)` and of a framing's
sub-framing). Schemes, the restriction of
projective sections, the degreewise linear maps of graded algebras and the
arrows of the Mors of derivations and connections still construct their
arrows as instances of handwritten classes (the private hosts the node's tell
lists and the public bases `SchemeMorphism`, `FramingMorphism`
and `ModuleMorphism`), so one Mor holds arrows on several classes and none of
them is its element class.

**Dependency path:** category `C` -> `C.Mor(A, B)` -> generated arrow type ->
the Mor's private operation that applies its element class to the arrow's
defining data, with the linearity or invertibility the operation gives as a
premise.
**Consumers:** every comparison, composition and category membership test on
those Mors; the scheme, cone and connection constructions.
**Coverage boundary:** the two population tells of the node were run over
`src/dzack_research/preamble` on 2026-10-08, and the constructor sites of the
public bases were listed. Repair is the `every-arrow-is-an-element-of-its-mor`
node in [TODO.md](TODO.md).

### The classifying category of a group has no object set

An action of `G` on an object of `C` is a functor `BG -> C`, where `BG` is the
one-object groupoid of `G` (`lean-categories` FOUNDATIONS, Definition 34.1).
`BG` is a small category with the one-point object set. `ClassifyingCategory`
(`categories/group/classifying_categories.py`) answers `object()` but not
`object_set()`, which discrete categories, fixed Mor categories and products
answer. `Groups.S(3).classifying_category().object_set()` raises
`AttributeError`.

**Dependency path:** group `G` -> `BG` -> its object set `{*}` -> the
components of a natural transformation between action functors.
**Consumers:** `tests/constructions/test_g_object_mor_construct.sage` and
`test_group_module_morphism_surface_construct.sage`, which read a component at
the element of that set.
**Coverage boundary:** `classifying_categories.py` and the `object_set`
owners in `abstract_categories/` were read. Repair is the
`classifying-categories-have-an-object-set` node in [TODO.md](TODO.md).

### Equivariant maps answer their natural transformation in two kinds

A map of actions is a natural transformation between the action functors
`BG -> C`, and `GObjects(G, Modules(R)) ≃ Modules(R[G])` is an explicit
equivalence. `EquivariantMorphismMethods.natural_transformation`
(`categories/group/g_objects.py`) returns the `NaturalTransformation`;
`GroupModuleMorphismMethods.natural_transformation` (`group_modules.py`)
returns its arrow in the functor category, and the restriction functor along a
subgroup inclusion consumes that arrow.

**Dependency path:** `R[G]`-module map -> the equivalence with
`GObjects(G, Modules(R))` -> the natural transformation between the action
functors.
**Consumers:** `_RestrictionAlongGroupInclusionFunctor._apply_morphism`;
`test_group_module_morphism_surface_construct.sage`.
**Coverage boundary:** source reading only. No `R[G]`-module constructs while
`modules-over-a-group-algebra-keep-the-module-axioms` is open, so the group
module route was not run. Repair is the
`equivariant-module-maps-give-their-natural-transformation` node in
[TODO.md](TODO.md).

### A graded module asks the ungraded Mor of its endpoints

A morphism of graded `R`-modules preserves degree (`lean-categories`,
`LeanCategories/Modules/Graded.lean`: `GradedObject ι (ModuleCat R)`). The
endpoint hook `Modules.ParentMethods.Mor` (`modules/pure/modules.py`) names
`Modules(self.base_ring())`, and the graded level declares no hook of its own.
For `M = GradedModules(QQ).an_object()`, `M.Mor(M)` is the Mor of `Modules(QQ)`
and `GradedModules(QQ).Mor(M, M)` is the graded Mor.

**Dependency path:** graded module -> its category `GradedModules(R)` -> the
endpoint hook -> `GradedModules(R).Mor(M, N)`.
**Consumers:** every graded construction that asks `M.Mor(N)` and expects a
degree-preserving map.
**Coverage boundary:** the endpoint hooks of `Modules`, the lattice level,
`Modules(R[G])` and `GradedModules` were read. Repair is the
`graded-modules-ask-their-mor-of-the-endpoints` node in [TODO.md](TODO.md).

### Objects of Sets do not answer their endomorphisms or automorphisms

`End(X) = Mor(X, X)` and `Aut(X)` are asked of `X`. Objects of `Sets()` answer
`Mor` through their category's hook but not `End` or `Aut`;
`Sets.Δ[0].End()` raises `AttributeError`.

**Dependency path:** object `X` of `Sets()` -> its category's hook ->
`End(X)` and `Aut(X)`.
**Consumers:** `tests/constructions/test_mor_categories_construct.sage`, whose
specimens start from `Sets.Δ[0].End()`.
**Coverage boundary:** the `ParentMethods` of `Sets()` in
`categories/sets/set_categories.py` were read. Repair is the
`objects-of-sets-answer-their-endomorphisms` node in [TODO.md](TODO.md).

### An object of one slice cannot be placed in a second slice

An object of the slice `C/X` is a pair `(A, p: A -> X)`; `SliceCategory`
and `CosliceCategory` (`abstract_categories/arrow_categories.py`) declare
`C` and construct `(A, p)` through the owner of `C` on the data of `A`
(placement ruled 2026-10-07: `C/X` and `X/C` declare `C`, and only `C`,
by `CAT-16` and `CAT-20`). One object can be over two objects at once: a
relative spectrum `Y -> X` over `Spec(QQ)` is an object of `Sch/X` and of
`Sch/Spec(QQ)`. Every slice level stores its arrow under the one name
`slice_arrow`, and every coslice level under `coslice_arrow`, so the second
level cannot add its arrow.
**Evidence (2026-10-07):** with `X = QQ["x"].affine_spectrum()` and
`Y = X.relative_spectrum(id)`, `Schemes(QQ).as_slice_object(Y)` raises
`AssertionError: cannot add the data ['slice_arrow', 'slice_category']`
from `Objects.ParentMethods._with_structure`.
**Dependency path:** the slice `C/X` adds `p: A -> X` to `A` -> an object
is in `C/X` and `C/Y` with one arrow for each -> a family over `X` is also
a scheme over the base ring.
**Existing capability:** one slice level and one coslice level on one
object, as in the Galois stage `F_{q^d}`, an object of
`(F_q / Fields) / e`.
**Consumers:** `Schemes(R).as_slice_object` on any object of a scheme slice
`Sch/X`, the relative spectra of `schemes.py` and `relative_spec.py`
included.
**Coverage boundary:** observed on schemes; the same storage is shared by
every slice and coslice.
Repair: `an-object-lies-in-several-slices`, in TODO.

### A finite owned ring does not enumerate its points

`GF(25)` is in `FiniteSets()`, but `iter(GF(25))` does not give its 25
elements. The owned ring has no `__iter__`, so Python uses the sequence
protocol of `OwnedRings.ParentMethods.__getitem__`
(`rings/ring_foundation.py:2561`). For an index `k`, the case `names in self`
returns the ring itself, so the iterator gives `GF(25)` without end
(observed 2026-10-07). `Set(GF(25))` enumerated through this protocol and did
not stop; `Set()` now returns an owned set that is not a finite enumerated set
unchanged.
**Dependency path:** a finite ring is a finite set -> its points are the
points of its underlying set -> enumeration comes from the `Sets()`
placement, never from adjunction syntax.
**Existing capability:** the engine field enumerates its elements;
`cardinality()` of the owned ring is correct.
**Consumers:** every caller that iterates a finite owned ring or builds a
literal set from one. No TODO node yet.

### Spaces of modular forms with a character are not presented

Let `L` be a positive definite integral lattice of rank `n`, level `N` and
quadratic character `chi`. Then `theta_L` is a modular form of weight `n/2`
for `Gamma_0(N)` with character `chi`. Its cuspidal component
`theta_L - theta_gen(L)` lies in `S_{n/2}(Gamma_0(N), chi)`. The coordinates
of that component in a basis of `S_{n/2}(Gamma_0(N), chi)` are the input of
the Bhargava–Hanke and Rouse cusp constant. `M_k(Gamma, chi)` is the set of
holomorphic functions `f` on the upper half-plane `H` that satisfy
`f|_k gamma = chi(d) f` for every `gamma` in `Gamma` and are holomorphic at
the cusps. `S_k(Gamma, chi)` is the subset of forms that vanish at the cusps.
So `M_k(Gamma, chi)` is a subset of the hom `Mor(H, C)`, hence a
subcategory of that hom-category. It is also a subobject of `Mor(H, C)`, with
its inclusion, in topological `C`-modules.

**Dependency path:** `H` as an open complex submanifold of `C` ->
`ComplexManifolds().Mor(H, C)` with its `C`-module structure and topology ->
the weight-`k` slash action of `SL_2(ZZ)` on that hom -> the subset cut out
by `Gamma_0(N)`-invariance up to `chi` and the cusp conditions -> a basis of
the subset, with `q`-expansions at infinity -> the coordinates of the
cuspidal component of `theta_L`.
**Existing capability:** `ComplexManifolds` (`categories/manifolds.py`)
presents `Mor(X, Y)` only for maps given by polynomials in selected charts,
and presents only affine spaces as objects. No preamble object is the upper
half-plane, and `Mor(H, C)` has no `C`-module structure, no slash action and
no `q`-expansion. A search of `src/dzack_research/preamble` for
`upper half`, `modular form`, `cusp` and `slash` found no presentation
(2026-10-09). `Lattices.ParentMethods.theta_series_cuspidal_component`
returns the component as a power series, without the space it lies in.
Sage's `ModularForms(Gamma0(N), k, chi)` computes bases in integral weight,
and `half_integral_weight_modform_basis` computes them in half-integral weight.
**Consumers:** the lattice-db field `definite.cusp_form_coordinates`, which is
not requested until this space exists, and the cusp constant of
`definite-representation-exceptions`.
**Coverage boundary:** the `lean-categories` checkout (`LeanCategories/`,
`FOUNDATIONS.md`, `FOUNDATIONAL_FRONTIER.md`, `TODO.md`) was searched for
`modular form`, `ModularForm`, `SlashAction` and `Siegel`. It formalizes the
theta series of a definite integral lattice (Definition 29b.1, `Theta.lean`)
and nothing about modular forms. Mathlib was not inspected, because no local
checkout and no corpus index was found.
**Request (not yet filed):** `lean-categories` formalizes
`M_k(Gamma_0(N), chi)` and `S_k(Gamma_0(N), chi)`, in integral and
half-integral weight, as subsets of the holomorphic functions on `H`. It
also formalizes the statement that `theta_L` lies in
`M_{n/2}(Gamma_0(N), chi)`. Sources: Miyake, *Modular Forms*, §2.1 and
§4.3; Shimura, *On modular forms of half integral weight* (Ann. of Math. 97,
1973); Iwaniec, *Topics in Classical Automorphic Forms*, Chapter 10.
Repair: `modular-forms-and-hecke-algebras`, then
`theta-cusp-form-coordinates`, in TODO.

### `lean-categories` does not formalize the representation density or Siegel's formula

`Genus.siegel_eisenstein_coefficient` computes the coefficient `a_E(m)` of
`q^m` in the genus theta series as Siegel's product of the real density and
the local representation densities `beta_p(L, m)`, and
`Genus.local_density` computes `beta_p(L, m)`. Both present notions that
`lean-categories` does not formalize.
**Dependency path:** the representation density `beta_p(L, m)` -> Siegel's
product over all places -> Siegel's formula `theta_gen(L) = E_L`.
**Existing capability:** the preamble computes both, citing Siegel (1935) and
Hanke (2004); on `A_2`, `diag(1,1,1)`, `diag(1,1,16)` and the sum of four
squares the product agrees with `Genus.theta_series` through `q^12`.
**Consumers:** the lattice-db field `definite.siegel_eisenstein_coefficients`,
`definite.local_densities`, and the Eisenstein lower bound of
`definite-representation-exceptions`.
**Coverage boundary:** `lean-categories` formalizes the local density only as
the Haar volume of the local integral orthogonal group
(`Valued/LocalDensity.lean`, `Valued/DensityProduct.lean`).
**Request (not yet filed):** `lean-categories` formalizes the representation
densities `beta_p(L, m)` and Siegel's formula
`theta_gen(L) = E_L`, the Eisenstein series whose coefficients are the
product of the local representation densities. Sources: Siegel, *Über die
analytische Theorie der quadratischen Formen* (Ann. of Math. 36, 1935);
Hanke, *Local densities and explicit bounds for representability by a
quadratic form* (Duke Math. J. 124, 2004).
Repair: file the request with `lean-categories`. It runs beside the preamble
computation and blocks no node.

### `lean-categories` does not formalize the values of a unimodular binary `ZZ_p`-lattice

`Genus.local_representations` gives the least represented valuation of each
square class of `QQ_p^x` for a lattice of rank 1 or 2. At an odd prime `p`
where `L tensor ZZ_p` is unimodular of rank 2, `_least_represented_valuations`
in `categories/lattices.py` uses a criterion. If `L tensor QQ_p` is isotropic,
it represents every nonzero element of `ZZ_p`. If it is anisotropic, it
represents exactly the elements of even valuation. `lean-categories` states
neither theorem.
**Dependency path:** the values of a unimodular `ZZ_p`-lattice of rank 2 ->
the least represented valuation of each square class -> the local
representation conditions of the genus at every prime.
**Existing capability:** the preamble computes the criterion, citing Serre,
*A Course in Arithmetic*, Ch. IV, 1.7, Prop. 4, and Ch. II, 2.2, Cor. 2 of
Thm. 1. On `A_2`, `<1>` and `diag(2, 6)` it gives the values in `TRAPS.md`
(2026-10-09).
**Consumers:** `Genus.anisotropic_primes` and `Genus.local_representations`
in rank 1 and 2, and the lattice-db fields `integral.anisotropic_primes` and
`integral.local_representations`, whose schema states the rule at primes not
dividing `2 det L`.
**Coverage boundary:** `lean-categories` has these results over fields:
- `exists_repr_of_isotropic` (`ForMathlib/WittCancellation.lean`): an
  isotropic binary form over a field represents every scalar.
- `not_isNormFromSqrt_p` (`Lattices/Valued/PadicMixedSymbol.lean`): for a
  nonsquare unit `u`, the norm form `x^2 - u y^2` does not take the value
  `p`.
It does not have the integral statement for a unimodular `ZZ_p`-lattice.
**Request (not yet filed):** `lean-categories` formalizes the following. For
an odd prime `p` and a unimodular `ZZ_p`-lattice `M` of rank 2:
- if `M tensor QQ_p` is isotropic, `M` represents every element of `ZZ_p`;
- if it is anisotropic, `M` represents exactly the elements of `ZZ_p` of
  even valuation.
Source: Serre, *A Course in Arithmetic*, Ch. II, 2.2, Cor. 2 of Thm. 1;
Ch. IV, 1.7, Prop. 4; Ch. IV, 2.2, Thm. 6.
Repair: file the request with `lean-categories`. It runs beside the preamble
computation and blocks no node.

## Workflow Papercuts

### Formal power series and their rings print without their coefficients

`QQ.power_series_ring("q")` prints as `Ring over Rational Field`, and each of
its elements prints as `element of Ring over Rational Field`. The element text
comes from the last branch of the element display in
`categories/rings/ring_foundation.py`, which has no case for a power series.
So `Lattices(ZZ)([[1, 0, 0], [0, 1, 0], [0, 0, 16]]).genus().theta_series()`
shows nothing of its value at a prompt. The coefficients are still available
by index: the genus series begins `1, 2, 4, 0, 4, 8` (observed 2026-10-09).

**Dependency path:** `FormalPowerSeriesRings(R)` -> its element type -> a
display that states the truncated expansion `sum a_i q^i + O(q^n)` and the ring
`R[[q]]`.
**Consumer:** every theta series, genus theta series and cuspidal component
shown in a session or a notebook.
**Repair:** the element type of `FormalPowerSeriesRings` owns its display,
instead of one more branch in the shared fallback.

### Finite cyclic subgroup membership is decided by enumerating powers

`CyclicGroups.__contains__` in
`categories/group/cyclic_subgroups.py` currently answers membership in a
finite cyclic subgroup by constructing `_finite_elements()` and comparing the
candidate against every power of the selected generator. Membership in the
represented subgroup is a group-engine question when the ambient realization
supports subgroup membership; enumeration is a separate chosen presentation
of the finite set and should not be the decision procedure.

**Dependency path:** selected cyclic generator -> represented subgroup in the
ambient group engine -> engine membership decision -> owned subgroup
membership. Infinite cyclic membership retains its explicit discrete-log
computability boundary when no maintained route applies.
**Consumer:** `CyclicGroups.__contains__`; iteration may continue to enumerate
finite cyclic groups, but membership must not depend on that enumeration.
**Repair:** `engine-wiring-audit` in [TODO.md](TODO.md).

### Zettlr all-workspace lint conflates component `id=` properties with Pandoc `#` identifiers

Running the Zettlr linter across the configured writing and site workspaces
should lint valid component attribute blocks without aborting.  The site
component contract uses key-value attributes such as
`{.component type="video" provider="youtube" id="E_Ly2NWX1g8"}`; the same
form is used by multiple site documents.

Observed on 2026-09-29: all-workspace lint aborts with
`Inconsistent attribute block: id "E_Ly2NWX1g8" not found ...`.
`extract-references.ts::locateAttribute` in the Zettlr/Pandoc integration
calls `parsePandocAttributes`, sees `attributes.id`, and then requires that
value to occur as an authored `#<id>` token.  A component's ordinary
key-value `id=...` property therefore reaches the identifier-token branch and
throws even though the authored attribute block is valid for the component
renderer.  Linting the `/research/writing` workspace alone is clean through
warning severity; adding the site workspace exposes the failure.

**Expected behavior:** a generic key-value `id=...` property remains component
data and is not treated as a Pandoc reference identifier unless an authored
`#...` identifier token is present.  Explicit `#...` reference identifiers
must continue to be located with their exact source range.
**Owning boundary:** Zettlr/Pandoc attribute parsing and reference extraction,
not the research documents or the site component syntax.
**Examples:** the Benson Farb video block above, together with established site
video blocks using `id="3IjAy0gHRyY"` and `id="zRPa-VAvl6Q"`.
**Coverage boundary:** the concrete all-workspace failure, the identifier
locator source, and these three site video-component uses were inspected.  No
claim is made about other key-value `id=` consumers.

### Flowmark Unicode-math lint scans inert comments and literal code

Running Flowmark's `math/unicode-symbol` rule on authored Markdown should
inspect mathematical prose, not text Pandoc treats as inert or literal.  The
rule currently reports Unicode-math warnings inside both HTML comments and
inline code spans.

Observed on 2026-09-29 with minimal stdin specimens: a comment containing
`F\u2082d` and `\u0393\u2082d` reports warnings for those Unicode math code
points, while an inline code span containing `AltBil\u2286SkewBil` and
`\u03b3` reports the same rule.  The same first
failure accounts for the remaining `math/unicode-symbol` diagnostics in
commented archival notes in
`writing/dissertation/sections/1-part-combinatorial/3-chapter-enriques-k3/450-scattone.md`
and
`writing/dissertation/sections/3-part-main-theorem/6-chapter/600-finite-coarsening.md`;
the inline-code failure appears in literal bad/good authoring examples in
`writing/CONTRIBUTING.md`.

**Expected behavior:** HTML comments and code spans are excluded from
`math/unicode-symbol`; Unicode mathematical notation in rendered prose remains
diagnosed.
**Owning boundary:** Flowmark's Markdown token scoping for the
`math/unicode-symbol` rule, not the dissertation comments or literal examples.
**Coverage boundary:** the two minimal stdin specimens and the current
repository occurrences above were reproduced.  No claim is made about other
math lint rules or other Markdown literal-node kinds.

### Source category-graph slices collapse parameterized fibres into self-edges

The source-only category graph is an inspection tool for the M1 placement
audit, so selecting a category must remain usable while execution is suspended.
On 2026-09-29,
`just category-graph slice --select PermutationGroups --direction up` aborted
before producing the requested slice with
`Self-declarations cannot define a strict category order:
['DistinguishedAffineCovers']`.

The triggering declaration is
`DistinguishedAffineCovers(X).super_categories()`, whose parameterized fibre
lists the unparameterized catalogue `DistinguishedAffineCovers()` together
with `CoveringFamilies(AffSch_R/X)`.  The source graph records category classes
but not this parameter distinction, so the fibre-to-catalogue inclusion is
collapsed to an apparent class self-edge and blocks inspection of unrelated
categories.

**Expected behavior:** a source slice for an unrelated category does not abort
because a parameterized category and its catalogue share one implementation
class.  The graph either represents their parameters sufficiently to retain
the strict relation or records that relation outside its class-level strict
poset.
**Owning boundary:** `dzack_research.utilities.category_graph`'s source model of
parameterized category declarations, not the `PermutationGroups` placement
pass and not, by this observation alone, the mathematics of distinguished
affine covers.
**Coverage boundary:** the failing slice command and the declaration at
`categories/schemes/ringed_spaces.py::DistinguishedAffineCovers.super_categories`
were inspected.  No claim is made here about other same-class parameterized
relations.

### A slice object does not answer the set invariants of its underlying object

**Missing general mathematics:** an object `(A, p: A -> X)` of `C/X` has the
underlying object `U(A, p) = A` under the projection `U: C/X -> C`, so its
underlying set, its cardinality and its finiteness are those of `A`. A subset
of `X` is the case `C = Set` with `p` monic.
**Dependency path:** `Sets().Subobjects(X)` and `X.power_set()` construct a
subset as an object of `Set/X` through `SliceCategory._construct_on` and
`Objects.ParentMethods._with_structure`; `Sets().ParentMethods.cardinality`
answers only from placement in a cardinality category or from a formula.
**Evidence (2026-10-09):** with `points = Sets.Δ[2]` and
`pair = points.power_set()((points(0), points(1)))`, `pair.category()` is the
join of the facade sets and `Sets/{0,...,2}`; `pair.domain() in FiniteSets()`
is `True`; `pair.cardinality()` and `points.power_set().top().cardinality()`
raise `AssertionError: cannot compute the cardinality ... it is not known to be
finite or countably infinite`. The protected expectation
`tests/objects/test_power_set_of_a_three_element_set.sage::test_the_boolean_operations`
asks `pair.cardinality() == 2`. `Lattices(ZZ).vectors_of_square` returns such
a subset, so `represents` reads `.domain().cardinality()` in its place.
**How it entered:** `520ffee4d8` (2026-10-08) applied the owner's ruling that
an object of `C/X` lies in `C/X` and its supercategories only, and removed
`FiniteSets` with the other categories of `A`. Its specimen asserted that the
slice object is not in `FiniteSets`; no specimen asked a slice object for a
set invariant. `SetSubobjectCategory`'s docstring states that the points,
membership and cardinality of `(A, i)` are those of `A`; no level supplies them.
**Existing partial capability:** the arrow's domain answers every set
question; `SetSubobjectCategory` supplies the subobject lattice only.
**Affected consumers:** every subset of a set (`power_set`, `finite_subsets`,
`Subobjects`, `subsets_of_size`), every slice object over a set, and
`represents`.
**Coverage boundary:** `set_categories.py` power sets,
`arrow_categories.py` `SliceCategory` and `SetSubobjectCategory`, and
`objects.py` `_with_structure` were inspected; the module and algebra
`_with_structure` routes were not probed.
**Repair:** `TODO.md` `slice-objects-answer-the-set-invariants-of-their-underlying-object`.

### Module-subobject joins and meets do not transport canonical ideal structure

The placement audit found that `CommutativeIdeals(R)` is a strict subcategory
of `ModuleSubobjects(R)`, but it reimplements both `sum` and `intersection`
with raw ideal-engine operations.  Mathematically these are the same join and
meet of the two submodules of the regular module `R`: the sum of ideals is the
module sum and the intersection of ideals is the module-subobject pullback.

The general owner already implements both constructions in
`categories/modules/pure/modules.py::ModuleSubobjects.ParentMethods`, but its
results are constructed only as module subobjects.  Simply deleting the ideal
overrides would therefore discard the canonical fact that the result is again
an ideal, together with the selected ideal-generator/engine data required by
the current `CommutativeIdeals` representation.  The ideal overrides in
`categories/rings/commutative_ideals.py` preserve that structure only by
maintaining a second computation path.

**Expected behavior:** the module-subobject sum/meet construction has one
authority and transports any structural category whose closure under the
selected construction is part of its declared contract.  In particular,
intersections and sums of commutative ideals return `CommutativeIdeals(R)`
without a second public `sum`/`intersection` implementation at the ideal leaf.
**Dependency path:** selected module subobjects and their inclusions -> general
subobject join/pullback -> structure-preservation datum for commutative ideals
-> one result carrying both `ModuleSubobjects(R)` and `CommutativeIdeals(R)`.
**Consumers:** `CommutativeIdeals.sum`, `CommutativeIdeals.intersection`, and
all callers that subsequently require ideal operations on those results.
**Coverage boundary:** the live module-subobject implementations at
`modules/pure/modules.py` and the two ideal implementations at
`rings/commutative_ideals.py` were inspected during `placement-audit`.  No
claim is made here about preservation of arbitrary additional subobject
categories; each such closure law requires its own mathematical justification.

### Toric scalar base change drops the toric construction data

Scalar base change of a toric scheme should retain the fan that defines the
toric variety.  On 2026-09-29 the construction-chain review for projective
surface method placement found that `_SchemeBaseChangeFunctor._apply_object`
routes every scheme presented by a finite affine gluing through
`_glued_object` before inspecting any toric specialization.  `ToricSchemes`
are built by exactly such a gluing.  `_glued_object` then reconstructs only a
generic glued scheme in `FiberProductSchemes(R')`; it does not retain
`ToricSchemes(R')`, the fan, or the optional polarizing polytope.

**Expected behavior:** for a scalar map `R -> R'`, the base change of
`X_Sigma` remains the toric scheme `X_Sigma` over `R'`, carrying the same fan
and any selected polarization together with the fibre-product projections.
Properties determined by the fan, such as smoothness and (for complete toric
surfaces over a field) projective-surface placement, are then inherited from
that same retained datum rather than re-guessed after gluing.
**Dependency path:** `ToricSchemes(R)` and its defining fan -> affine-atlas
gluing -> scheme scalar base change -> fibre-product gluing over `R'` ->
retained toric construction data and category placement.
**Owning boundary:** the scheme base-change constructor together with the
toric-scheme constructor, not the individual toric operations that disappear
after the base change.
**Coverage boundary:** `_SchemeBaseChangeFunctor._apply_object` and
`_glued_object`, and the toric construction in `_toric_variety`, were inspected
as source.  No runtime execution was performed under the current M1 execution
suspension, and no claim is made here about other specialized affine-gluing
families that may also need structure-preserving base change.

### Book recipes still target the former writing directory

The book source and Quarto project are at `research/` and `research/.book/`.
The root `justfile` recipes `docs-assets`, `docs-check`, and `docs-lint` still
target `writing/`, as does `scripts/docs_check.py`. That directory is absent
in this checkout. A chapter author cannot use the documented render recipe
against the current project location. The owning repair is to reconcile the
book recipes and checker with the source root; the inspected boundary is
these recipes, the checker path, and `research/.book/_quarto.yml`.

Add concrete observed workflow friction here under a descriptive heading, with the user action, expected behavior, actual result, owning boundary and example.
Use `DEV-59` for capture and resolution.
Foundational mathematical gaps belong above even when first noticed as an inconvenient method or notebook interaction.
