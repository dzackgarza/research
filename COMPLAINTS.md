# Foundational Gaps and Papercuts

GitHub issues own complaint evidence, remaining requirements, dependencies, and closure.
This file is the navigation index. Reuse an existing issue when another consumer exposes
the same gap; otherwise file an issue and place it in the [issue tree](https://github.com/dzackgarza/research/issues/46).
Follow the capture and closure rules in [DEV-59](CONTRIBUTING.md#dev-59-record-observed-foundational-gaps-and-papercuts).

[TODO.md](TODO.md) indexes the work queue. Native sub-issue order ranks work by mathematical
correctness, reusable capability, and reduction of later work. Native blocked-by relations
record actual prerequisites. Select ready work with `itree next dzackgarza/research`.

Each link below retains the original complaint's evidence and coverage boundary. Historical
observations, partial repairs, and unexecuted assertions remain dated in their issue records.
Issue state is authoritative; this index does not duplicate it.

## Foundational Mathematics

### Abstract polytope axioms lack a formal owner in the inspected source

[Issue #518](https://github.com/dzackgarza/research/issues/518) · [Complaint evidence](https://github.com/dzackgarza/research/issues/518#issuecomment-6381523287)

### Integral-affine collar extensions lack their defining compatibility laws

[Issue #519](https://github.com/dzackgarza/research/issues/519) · [Complaint evidence](https://github.com/dzackgarza/research/issues/519#issuecomment-6381523487)

### Metric ambient objects and local isometries lack their defining laws

[Issue #518](https://github.com/dzackgarza/research/issues/518) · [Complaint evidence](https://github.com/dzackgarza/research/issues/518#issuecomment-6381523287)

### Smooth and finite-degree manifold maps lack a common owned route

[Issue #518](https://github.com/dzackgarza/research/issues/518) · [Complaint evidence](https://github.com/dzackgarza/research/issues/518#issuecomment-6381523287)

### Local integral-affine isomorphisms lack their arrow predicate

[Issue #518](https://github.com/dzackgarza/research/issues/518) · [Complaint evidence](https://github.com/dzackgarza/research/issues/518#issuecomment-6381523287)

### Fundamental groupoid has no represented path category

[Issue #518](https://github.com/dzackgarza/research/issues/518) · [Complaint evidence](https://github.com/dzackgarza/research/issues/518#issuecomment-6381523287)

### Closed-locus complements have no open-subspace construction

[Issue #519](https://github.com/dzackgarza/research/issues/519) · [Complaint evidence](https://github.com/dzackgarza/research/issues/519#issuecomment-6381523487)

### Complex-manifold realification lacks object and morphism images

[Issue #519](https://github.com/dzackgarza/research/issues/519) · [Complaint evidence](https://github.com/dzackgarza/research/issues/519#issuecomment-6381523487)


### Rational radical quotient loses its presented rank when reframed as a lattice

For a finite free formed module over a field, the radical quotient must retain a
free presentation of rank `rank(L) - rank(rad(L))` and its descended Gram form.
On `Lattices(QQ)([[0,0,0],[0,0,1],[0,1,0]])`, the public
`L.radical_quotient()` resolves to the formed-module construction. It reports
rank two, but `Lattices(QQ)(L.radical_quotient())` retains a rank-three
underlying module with a rank-two Gram tensor, so pairing evaluation raises
`IndexError`. The lattice's radical embedding followed by
`isotropic_reduction()` does construct the rank-two quotient and is used by
the hyperbolic-index methods. The general formed-module quotient and its
presentation remain unresolved; terminal T owns the separating specimen.
This observation does not establish behavior over arbitrary rings or value modules.

### Constrained integral embedding search still needs applicable exclusion routes

The hyperbolic-splitting dependency index requires all isometric embeddings,
including nonprimitive images, with actual source and target maps. For example,
`U(2) -> U`, sending its basis to `2e,f`, is an index-two integral embedding
although the two lattices are not integrally isometric. A negative isometry
or primitive-embedding answer cannot exclude it.

The existing source now retains this distinction. Finite-rank embeddings with
nondegenerate source over ZZ and QQ have complete enumeration, finite
coordinate subsets and finite generator-image searches retain their inclusions,
and predicate subsets can filter them. Over QQ and AA, two finite
nondegenerate endpoints have a terminating emptiness decision from
`w(L orthogonal_sum -T) >= dim(T)`. Rational witness search first rejects the
empty case; AA witnesses use exact diagonalization and matching signs.

General nondegenerate integral embedding existence now has a finite source
route: exhaust all integral overlattices of the source via the discriminant
bilinear form, then decide primitive embedding into the target (or integral
isometry in equal rank). The saturation proof and the actual map
composition are in the theory note. Runtime and engine coverage remain
unverified under DEV-58.

**Remaining computation:** complete exclusion for constrained subsets where
required. Exhausting a finite coordinate box excludes only that box. The Li–Margulis representation bound in
[the theory note](docs/theory/hyperbolic-index.md#effective-search-bounds-for-embeddings)
still has an unevaluated dimension-dependent constant. The source now has
an explicit alternative for nondegenerate integral sources and indefinite
targets of rank at least three: `integral_embedding_coefficient_bound`
combines the completion bound with a Hermite basis of its finite-index
overlattice and a fully evaluated Calderon equivalence bound. The theory
note proves the spherical-function and Haar-volume majorants used to make
that chain numerical, including the separate archimedean volume factor.
It includes nonprimitive images and depends on the original target framing.
The scalar isometry bound is also exposed at `Lattices(ZZ)` from rank and
two Gram heights alone. These computations require neither an embedding nor
an isometry as input and construct neither.

**Split binary coverage:** the integral linear factorization of a rationally
split binary target now bounds every embedding from a nondegenerate source
in its original framing. The theory note proves the explicit bound, including
null source basis vectors controlled by their nonzero cross pairing. Thus
finite boxes cover all additional decidable constraints in this regime.

**Nonsplit binary coverage:** the existing complete finite norm-orbit
transversal now bounds a first basis image. The prescribed pairing and
source determinant bound the second after that target isometry, supplying
some embedding whenever one exists. This retains nonprimitive candidates.
The theory note gives the proof and PARI source contract; the positive,
negative, imprimitive, empty and rank-two specimens remain unexecuted.

**Invariant constraints:** the completed higher-rank proof identifies its
bounded embedding as the original one postcomposed by an integral target
isometry. Thus the computed bound meets every target-isometry orbit, as
does the nonsplit binary norm-orbit construction. Decidable invariant
conditions, including primitivity, admit complete finite exclusion using
the existing coordinate box and embedding subset. The new finite
U(2)->U specimen distinguishes embedding existence from primitive absence
and remains unexecuted under DEV-58.

**Witnessed subset coverage:** source inspection found that predicate
subsets retained admitted points but ignored them when deciding emptiness
over an infinite universe. The general subset owner now returns nonempty
from such a point, without starting another search. Its point selector now
also uses an admitted member before requesting iteration, which permits
point selection in real predicate subsets and norm fibres once zero or
a computed representation witness has been admitted. These real-subset
and fibre-inclusion specimens remain unexecuted. Failed membership and
unfinished searches supply no negative existence conclusion. The NN tail
and failed-membership specimens remain unexecuted under DEV-58.

**Remaining coverage:** arbitrary noninvariant constraints outside the
definite and split binary regimes still require an applicable bound or
complete solver: a coordinate-dependent predicate need not survive a
target isometry taking an embedding to a small representative. The theory
note proves that a uniform emptiness solver for all decidable embedding
filters is impossible, already for U -> U+<2>; particular additional
conditions still need their own applicable route. The sharper original Li–Margulis
formula is separate and unevaluated; it is not a prerequisite for the new
alternative. The nonprimitive, definite shear and zero-source specimens,
and the constant/normalization derivations, remain unverified under DEV-58.
Definite enumeration and the integral-overlattice classification remain
alternative existence routes. The representative and completion coefficient
bounds remain distinct from the new embedding and isometry bounds.

For definite integral targets of finite rank, `square_coordinate_bound` now gives
an exact bound containing every vector of a supplied square. The maximum
source-generator bound, the existing finite coordinate subset and the
finite embedding subset thus supply a complete constrained search for any
decidable extra predicate. The original framing is retained, including
large coordinates in sheared bases. Small proved coordinate boxes now use
exact finite enumeration; larger square shells delegate to Hecke's inclusive
`short_vectors` enumeration, restore both signs, and filter reflective
vectors by exact divisibility. It replaces the PARI `forqfvec` route whose
measured large-coefficient precision limitation is recorded in TRAPS.md.
The definite minimum also delegates to the maintained rational shortest-vector route instead of PARI ball counts, retains the signed closest-to-zero convention and rejects rank zero. The scaled A2 square-shell specimen has run through the exact small-box route. Its minimum, sign, coordinate and empty-shell specimens in
the theory note remain unexecuted under DEV-58. Source inspection of the
maintained rational enumeration is not runtime coverage evidence.

**Dependency path:** formed modules and form-preserving maps -> embedding
subset retaining its maps -> complete candidate enumeration -> an applicable
finite bound or a separate existence decision -> integral maximal splitting.
For constrained embeddings the predicate enters before the exclusion theorem,
not after it. **Coverage boundary:** source inspection and the cited mathematical
proofs; mathematical specimens remain unexecuted under DEV-58.
The formal embedding and module-morphism owners already distinguish
injectivity from invertibility; no missing formal foundation is asserted.
The remaining mathematical specimen execution belongs to
`terminal-session` in [TODO.md](TODO.md).

### Generic computable-real linear algebra still has partial scalar decisions

The owned exact `RR` field supplies closed real expressions and now regular
rational Cauchy presentations in the same real field, with arithmetic,
positive square roots and exact relation decisions where known.
The shared element isotropy, orthogonality and representation predicates
previously forced scalar equations through `bool`. They now return the
equations, preserving unknown real predicates. The lattice isotropy
override also previously fell through to `None` when nondegeneracy was
unknown; it now delegates that case to the common norm-zero fibre
proposition. The Cauchy-zero vector specimens remain source-only.
The rescaling source audit also found Python truth coercions of the
scalar's unit and equality predicates in `FormValueScalings`. These are
replaced by explicit-true checks, using nonzero status for field units.
Unknown status no longer blocks constructing the scaled form or becomes
a degeneracy conclusion; property shortcuts require known hypotheses.
The Cauchy-zero scaling specimen remains source-only, with the other
terminal assertions.
`vectors_of_square` also queried definiteness before selecting the
general fibre over nonintegral bases. It now returns the existing
equalizer first in those cases, so an undecided signature cannot block
norm-locus construction. The rank-one Cauchy-zero specimen retains the
original inclusion and canonical zero point, with source-only status.
The lattice Witt, norm-witness and field embedding routes previously rejected
it at their AA-only dispatch despite using congruence/sign/root constructions
that apply to this presentation too. Signature also lowered RR coefficients
to symbolic scalars and counted their signs inside Sage's generic routine.

The source now reuses the existing congruence constructions for represented
RR and counts diagonal signs only after raising the coefficients to the owned
real field. An undecided sign is refused, rather than coerced to a Python
truth value. Norm/isotropic witnesses, signed lattice vectors, Witt
index/decomposition and Emb/Isom retain the existing maps and inverses.
The pi-coefficient specimens in the theory note remain unexecuted under
DEV-58. Supplied nonsingular RR forms now have a returned diagonalizing
isometry and inverse from finite nonzero-norm search and fraction-free
projection, without scalar zero decisions. The existing downstream
`_real_witt_bases` now refines signs of its known nonzero diagonal entries
and computes roots and quotients under the resulting positivity hypotheses.
For nonsingular RR forms, `_real_representation_witness` now also refines
signs and normalizes under established hypotheses, once the requested
norm has decided zero status. Arbitrary requested-real zero status remains
partial. The nonsingular RR `witt_decomposition` now retains explicit
normalization and pair-coordinate changes, the diagonalization inverse,
and the actual module biproduct maps. It no longer sends that basis through
`subobject_on` or `orthogonal_decomposition` to rediscover its span/inverse.
Arbitrary singular oracle inputs still admit
no uniform zero decision.

**Represented-real pivot coverage:** source inspection found that the
congruence algorithm selected pivots over SR before checking final signs
in RR. The retained Sage route now uses RR coefficients and refuses
undecided pivot relations. The separate nonsingular construction searches
basis directions and pairwise sums simultaneously for a norm enclosure
excluding zero, then retains the inverse through elementary row updates.
The nonalgebraic off-diagonal/radical specimen,
form equation and both inverse composites remain unexecuted under DEV-58.
This congruence computation alone is not a total arbitrary-real route.

**Exact field preimages:** source tracing found another obstruction in
`_integral_preimage_solver`: finite-free real preimages required Smith
normalization, but `_selected_presentation_smith_backend` rejects SR
because `SR.is_exact()` is `False`, as Sage documents. The existing preimage owner now uses maintained rank and
linear-system operations over exact fields, computing RR elimination
with its own scalar protocol. An inconsistent augmented rank gives
absence; unknown scalar or solver failures propagate. Original source
coordinates and selected-lift precedence are retained. The pi, inconsistent
right-hand side, zero-source and integral-divisibility specimens remain
unexecuted under DEV-58. This supports affine pairing and partner equations
without constructing any maximal hyperbolic splitting.

**Kernel, inverse and span coverage:** their generic linear-algebra
computations now use the same coefficient-ring choice as field preimages
and congruence. An exact owned field with an inexact symbolic realization
keeps its own scalar comparisons and division during elimination and
kernel-span normalization. The actual kernel inclusion and inverse-map
endpoints are retained. The rank-two kernel of (pi,0,0), its inclusion
and lifts, triangular inverse composites and empty inverse remain
unexecuted under DEV-58. Private external-engine serialization retains
its selected computation ring.

**Approximation input and backend boundary:** direct RR ingress retains
closed expressions. `RR.of_cauchy(a)` now additionally retains an owned
map `a: NN -> QQ` under its stated regular Cauchy hypothesis, and
`x.cauchy_sequence()` supplies the selected map. The primitive enclosure
uses its rational center and the proved error radius. Mathlib's real
Cauchy-limit construction supplies the mathematical meaning. Maintained
Sage lazy arithmetic composes evaluations, while owned relations use
Arb signs and preserve unresolved comparisons as propositions; lazy-real
comparisons and hashes are not used to decide those relations. Generic
computation chooses RR coefficients before materializing matrices and
spans, rather than demanding symbolic serialization of a general limit.
Finite tensors supply recursive presentation cache keys for their
unhashable real coefficients; no real equality is inferred from caching.
The separate symbolic serialization contract retains SR. Explicit symbolic/algebraic conversion
still requires a supplied exact expression. The note gives the complete
rational inverse-norm stopping test and proof under nonsingularity.
FLINT documents its real LDL success test for positive definiteness, not
general indefinite inertia. No general absence of other backends is
asserted. Finite symmetric forms already placed as nondegenerate over RR
now route signature through Arb enclosures, rational midpoint matrices,
their exact row-sum error bound and the inverse-norm stopping test. This
source construction requires convergent evaluation of the represented
computations. Regular Cauchy input admission and the promised nonsingular
returned-basis computation are supplied. The regular sequence
`1+2^(-n)`, its actual map, arithmetic, roots, division and signature
`diag(x,-1)` have written specimens, alongside the off-diagonal pi,
near-singular positive, empty and singular forms. They remain unexecuted
under DEV-58. Nonsingular real normalization and explicit Witt inverse
maps now have source implementations; the index-wide map audit remains open.

**Scalar ingress into form construction:** the real field now retains
its usual ordered-ring placement, previously absent from its constructing
category despite the signature route requiring it. Real Gram determinants
now use the real field's Sage determinant protocol: symbolic division-free
arithmetic for closed expressions, and ball-coefficient division-free
arithmetic with a regular Cauchy limit for general presentations. The
regularity and unimodularity predicates preserve undecided
unit/nonzero propositions, and finite-rank evenness preserves actual
ideal-membership propositions. A Cauchy presentation of zero supplies the
written separating construction specimen. These repairs are source
findings and changes.
The intermediate coefficient normalization of Sage's `_charpoly_df`
now takes place over ball coefficients for Cauchy inputs. A ball containing
zero survives that support test unless it is the exact zero ball, so no
underlying real equality is decided there. The theory note proves the
enclosure-to-Cauchy construction, and the trace-zero rank-four and singular
specimens remain written but unexecuted. The real plane, Cauchy plane with
undecided diagonal zeros and empty space supply the new diagonalization
specimens. Its actual inverse pair and proof are in the theory note.
Lattice naming also no longer asks for a real signature that its displayed
name does not use. The source map audit is recorded in the theory note;
remaining mathematical specimen execution stays with `terminal-session` in TODO.md.

**Fresh norm-fibre point selection:** the zero-norm fibre previously needed
manual admission of zero before its set computation could select a point
over RR. The common formed-module constructor now retains that canonical
point, and symmetric bilinear forms inherit the same construction. Source
inspection also found unhashable exact-real arguments without Sage's
required cache-key protocol at the existing cached square-fibre method.
The real scalar now supplies a parent-and-expression presentation key,
or a retained presentation-identity token for Cauchy computations;
real equality stays partial and the scalar stays unhashable. The fresh
zero-fibre point, inclusion, nonemptiness and repeated-construction
specimens remain unexecuted under DEV-58.

**Dependency path:** exact real scalar arithmetic and relations -> congruence
diagonalization with its map -> inertia and normalized vectors -> field
Witt and embedding operations. No new mathematical definition is introduced;
the formal bilinear-form and Witt owners already supply these notions.
The source routes and map audit are recorded in the theory note. Remaining
mathematical specimen execution belongs to `terminal-session` in TODO.md.

### Labelled graphs present no isomorphisms or automorphism groups

[Issue #399](https://github.com/dzackgarza/research/issues/399) · [Complaint evidence](https://github.com/dzackgarza/research/issues/399#issuecomment-6381517131)

### A realization's class method is unreachable behind a category operation of the same name

[Issue #436](https://github.com/dzackgarza/research/issues/436) · [Complaint evidence](https://github.com/dzackgarza/research/issues/436#issuecomment-6381519272) · [Closed-subscheme equality #602](https://github.com/dzackgarza/research/issues/602) · [Coefficient modules #443](https://github.com/dzackgarza/research/issues/443)

### Port consumers of binary fibres and cone marks must move (port #33, #15)

[Issue #403](https://github.com/dzackgarza/research/issues/403) · [Complaint evidence](https://github.com/dzackgarza/research/issues/403#issuecomment-6381517574)

### Convex-polytope facets have no retained arrow into their polytope

[Issue #519](https://github.com/dzackgarza/research/issues/519) · [Complaint evidence](https://github.com/dzackgarza/research/issues/519#issuecomment-6381523487)

### `lean-categories` does not formalize finiteness of binary fixed-norm orbits

[Issue #583](https://github.com/dzackgarza/research/issues/583) · [Complaint evidence](https://github.com/dzackgarza/research/issues/583#issuecomment-6381627220)

### `lean-categories` defines integral reflection vectors but not roots of a lattice

[Issue #406](https://github.com/dzackgarza/research/issues/406) · [Complaint evidence](https://github.com/dzackgarza/research/issues/406#issuecomment-6381517807)

### Implementation code retains mathematical construction authority

[Issue #560](https://github.com/dzackgarza/research/issues/560) · [Complaint evidence](https://github.com/dzackgarza/research/issues/560#issuecomment-6381525346)

### Explicit isometries and automorphism generators lack their indefinite provider

[Issue #403](https://github.com/dzackgarza/research/issues/403) · [Complaint evidence](https://github.com/dzackgarza/research/issues/403#issuecomment-6381517574)

### Group morphisms lose computational closure across represented data

[Issue #396](https://github.com/dzackgarza/research/issues/396) · [Complaint evidence](https://github.com/dzackgarza/research/issues/396#issuecomment-6381516693)

### Effective group pullbacks require general products and equalizers

[Issue #514](https://github.com/dzackgarza/research/issues/514) · [Complaint evidence](https://github.com/dzackgarza/research/issues/514#issuecomment-6381523060)

### The product in Grp and its factor inclusions are not formalized in `lean-categories`

[Issue #428](https://github.com/dzackgarza/research/issues/428) · [Complaint evidence](https://github.com/dzackgarza/research/issues/428#issuecomment-6381518490)

### Group colimits do not compose chosen finite presentations

[Issue #428](https://github.com/dzackgarza/research/issues/428) · [Complaint evidence](https://github.com/dzackgarza/research/issues/428#issuecomment-6381518490)

### Nonenumerated relation quotients still need exact class computations

[Issue #428](https://github.com/dzackgarza/research/issues/428) · [Complaint evidence](https://github.com/dzackgarza/research/issues/428#issuecomment-6381518490)

### Module images require finite selected generators at the inspected owner

[Issue #428](https://github.com/dzackgarza/research/issues/428) · [Complaint evidence](https://github.com/dzackgarza/research/issues/428#issuecomment-6381518490)

### Formed-module Mono has a first-component-only definition

[Issue #568](https://github.com/dzackgarza/research/issues/568) · [Complaint evidence](https://github.com/dzackgarza/research/issues/568#issuecomment-6381624327)

### Protected formed-map expectations conflate two preservation laws

[Issue #496](https://github.com/dzackgarza/research/issues/496) · [Complaint evidence](https://github.com/dzackgarza/research/issues/496#issuecomment-6381521977)

### Protected bilinear constructors expect symmetry discovery

[Issue #496](https://github.com/dzackgarza/research/issues/496) · [Complaint evidence](https://github.com/dzackgarza/research/issues/496#issuecomment-6381521977)

### Direct tensor symmetry still coerces undecided equality

[Issue #496](https://github.com/dzackgarza/research/issues/496) · [Complaint evidence](https://github.com/dzackgarza/research/issues/496#issuecomment-6381521977)

### Core inverse data and its actual base-arrow representation

[Issue #569](https://github.com/dzackgarza/research/issues/569) · [Complaint evidence](https://github.com/dzackgarza/research/issues/569#issuecomment-6381624544)

### Protected Aut specimens conflate a fixed category and a group realization

[Issue #496](https://github.com/dzackgarza/research/issues/496) · [Complaint evidence](https://github.com/dzackgarza/research/issues/496#issuecomment-6381521977)

### Protected well-order reversal expects eager validation

[Issue #496](https://github.com/dzackgarza/research/issues/496) · [Complaint evidence](https://github.com/dzackgarza/research/issues/496#issuecomment-6381521977)

### Slice and coslice arrows still need their actual base-arrow initialization

[Issue #570](https://github.com/dzackgarza/research/issues/570) · [Complaint evidence](https://github.com/dzackgarza/research/issues/570#issuecomment-6381624791)

### Selected exterior computations and the protected augmentation spelling

[Issue #496](https://github.com/dzackgarza/research/issues/496) · [Complaint evidence](https://github.com/dzackgarza/research/issues/496#issuecomment-6381521977)

### Finite coefficient module kernels need exact coefficient presentations

[Issue #571](https://github.com/dzackgarza/research/issues/571) · [Complaint evidence](https://github.com/dzackgarza/research/issues/571#issuecomment-6381624957)

### Generic commutative-algebra specimens impose stronger laws

[Issue #496](https://github.com/dzackgarza/research/issues/496) · [Complaint evidence](https://github.com/dzackgarza/research/issues/496#issuecomment-6381521977)

### Free algebra constructions do not uniformly supply associative projective sources

[Issue #575](https://github.com/dzackgarza/research/issues/575) · [Complaint evidence](https://github.com/dzackgarza/research/issues/575#issuecomment-6381625690)

### Selected algebra presentations exceed the polynomial computations

[Issue #576](https://github.com/dzackgarza/research/issues/576) · [Complaint evidence](https://github.com/dzackgarza/research/issues/576#issuecomment-6381625887)

### A finite-generation reference confuses a property with a chosen family

[Issue #594](https://github.com/dzackgarza/research/issues/594) · [Complaint evidence](https://github.com/dzackgarza/research/issues/594#issuecomment-6381629331)

### General degree-zero algebras need represented homogeneous inclusions

[Issue #577](https://github.com/dzackgarza/research/issues/577) · [Complaint evidence](https://github.com/dzackgarza/research/issues/577#issuecomment-6381626082)

### General Kähler differentials exceed the selected finite conormal computation

[Issue #581](https://github.com/dzackgarza/research/issues/581) · [Complaint evidence](https://github.com/dzackgarza/research/issues/581#issuecomment-6381626813)

### Cohomology needs general represented cycle quotients

[Issue #582](https://github.com/dzackgarza/research/issues/582) · [Complaint evidence](https://github.com/dzackgarza/research/issues/582#issuecomment-6381627035)

### A coefficient presentation omits group-action relations

[Issue #443](https://github.com/dzackgarza/research/issues/443) · [Complaint evidence](https://github.com/dzackgarza/research/issues/443#issuecomment-6381520049)

### A module annihilator uses the additive endomorphism representation

[Issue #595](https://github.com/dzackgarza/research/issues/595) · [Complaint evidence](https://github.com/dzackgarza/research/issues/595#issuecomment-6381629487)

### An integral isotropic partner with minimal pairing can fail to exist

[Issue #401](https://github.com/dzackgarza/research/issues/401) · [Complaint evidence](https://github.com/dzackgarza/research/issues/401#issuecomment-6381517364)

### An affine integral parameter locus can contain a rational kernel

[Issue #401](https://github.com/dzackgarza/research/issues/401) · [Complaint evidence](https://github.com/dzackgarza/research/issues/401#issuecomment-6381517364)

### A commensurating group need not admit an invariant overlattice

[Issue #396](https://github.com/dzackgarza/research/issues/396) · [Complaint evidence](https://github.com/dzackgarza/research/issues/396#issuecomment-6381516693)

### Isotropic-reduction lifts need a kernel torsor with nonlinear evaluation

[Issue #401](https://github.com/dzackgarza/research/issues/401) · [Complaint evidence](https://github.com/dzackgarza/research/issues/401#issuecomment-6381517364)

### Clearing denominators requires similarity embeddings

[Issue #401](https://github.com/dzackgarza/research/issues/401) · [Complaint evidence](https://github.com/dzackgarza/research/issues/401#issuecomment-6381517364)

### Issue 401 migration does not match the frozen public contract

[Issue #401](https://github.com/dzackgarza/research/issues/401) · [Complaint evidence](https://github.com/dzackgarza/research/issues/401#issuecomment-6381517364)

### Hodge-isometry planning did not assign the general Hodge categories

[Issue #534](https://github.com/dzackgarza/research/issues/534) · [Complaint evidence](https://github.com/dzackgarza/research/issues/534#issuecomment-6381524900)

### K3 automorphism pullback lacks explicit chamber and Torelli consumers

[Issue #541](https://github.com/dzackgarza/research/issues/541) · [Complaint evidence](https://github.com/dzackgarza/research/issues/541#issuecomment-6381525110)

### Backing-core constructor narrowing and colimit lifting block integration specimens

[Issue #491](https://github.com/dzackgarza/research/issues/491) · [Complaint evidence](https://github.com/dzackgarza/research/issues/491#issuecomment-6381521602)

### Multiplicative integer submonoids do not supply the fixed power specimens

[Issue #578](https://github.com/dzackgarza/research/issues/578) · [Complaint evidence](https://github.com/dzackgarza/research/issues/578#issuecomment-6381626264)

### Fixed Mor categories with discrete 2-Morphisms do not realize their discrete universal constructions

[Issue #428](https://github.com/dzackgarza/research/issues/428) · [Complaint evidence](https://github.com/dzackgarza/research/issues/428#issuecomment-6381518490)

### Direct MorCategories ingress retains inconsistent represented endpoints

[Issue #579](https://github.com/dzackgarza/research/issues/579) · [Complaint evidence](https://github.com/dzackgarza/research/issues/579#issuecomment-6381626443)

### Discrete categories do not realize universal constructions that exist

[Issue #428](https://github.com/dzackgarza/research/issues/428) · [Complaint evidence](https://github.com/dzackgarza/research/issues/428#issuecomment-6381518490)

### Set-theoretic behaviour is re-implemented instead of wired to a set engine

[Issue #431](https://github.com/dzackgarza/research/issues/431) · [Complaint evidence](https://github.com/dzackgarza/research/issues/431#issuecomment-6381518656)

### Chosen generators are encoded as a global axiom instead of a resolution

[Issue #409](https://github.com/dzackgarza/research/issues/409) · [Complaint evidence](https://github.com/dzackgarza/research/issues/409#issuecomment-6381518037)

### Augmented objects are replaced by unrelated resolution specializations

[Issue #409](https://github.com/dzackgarza/research/issues/409) · [Complaint evidence](https://github.com/dzackgarza/research/issues/409#issuecomment-6381518037)

### Integral norm classification still needs terminal verification

[Issue #505](https://github.com/dzackgarza/research/issues/505) · [Complaint evidence](https://github.com/dzackgarza/research/issues/505#issuecomment-6381522667)

The former source gap in higher-rank nonzero integral norm witnesses and
ternary representation decisions now has a finite-classification route.
`<n>.Emb(L)` exhausts the integral overlattices of `<n>` and uses the
maintained primitive classifier or the integral Isom decision. Its witness
composes the actual inclusion and target map, so evaluation on the source
generator returns a vector of the original lattice. The saturation proof
in [the theory note](docs/theory/hyperbolic-index.md#general-integral-existence-through-integral-overlattices)
explains completeness; the procedure does not replace integral points by
rational points or an unbounded witness search.

**Remaining evidence:** these computations have not run under DEV-58.
`U + A_1 + A_1` at norm 2, `<1,1,-1,-1>` at norm 5 and `U + <1>` at norm 3
remain required. The theory note now supplies the distinguishing Borovoi
example with Gram [[-9,1,0],[1,7,0],[0,0,2]]: square 1 is represented
everywhere locally but not integrally, whereas square 2 is represented
integrally. The cited elementary exclusion proof and same-genus comparison
establish the expected answers and multiple-spinor-genus hypothesis;
these assertions and the positive witness remain unexecuted. The earlier
two single-spinor-genus trial examples do not replace this specimen. Retain these specimens and engine
coverage at `higher-rank-integral-lattice-representation` in [TODO.md](TODO.md).
No source route or mathematical argument here counts as executed acceptance.

### Genera of integral lattices are formalized without finiteness, parity or classification

[Issue #531](https://github.com/dzackgarza/research/issues/531) · [Complaint evidence](https://github.com/dzackgarza/research/issues/531#issuecomment-6381524493)

### The class theorems that decide isometry are not formalized

[Issue #531](https://github.com/dzackgarza/research/issues/531) · [Complaint evidence](https://github.com/dzackgarza/research/issues/531#issuecomment-6381524493)

### Dynamic peeking stands in for category membership across the preamble

[Issue #436](https://github.com/dzackgarza/research/issues/436) · [Complaint evidence](https://github.com/dzackgarza/research/issues/436#issuecomment-6381519272)

### Arithmetic reflection subgroups outside the definite and Vinberg regimes have no exact backend

[Issue #509](https://github.com/dzackgarza/research/issues/509) · [Complaint evidence](https://github.com/dzackgarza/research/issues/509#issuecomment-6381522862)

### `lean-categories` does not formalize the Vinberg invariant or the PID description of P^1(R)

[Issue #592](https://github.com/dzackgarza/research/issues/592) · [Complaint evidence](https://github.com/dzackgarza/research/issues/592#issuecomment-6381629001)

### A Coxeter diagram is not constructed by its category

[Issue #439](https://github.com/dzackgarza/research/issues/439) · [Complaint evidence](https://github.com/dzackgarza/research/issues/439#issuecomment-6381519485)

### Free session functions construct objects

[Issue #440](https://github.com/dzackgarza/research/issues/440) · [Complaint evidence](https://github.com/dzackgarza/research/issues/440#issuecomment-6381519698)

### Coxeter diagrams answer subdiagram orders and drawings as Sage objects

[Issue #441](https://github.com/dzackgarza/research/issues/441) · [Complaint evidence](https://github.com/dzackgarza/research/issues/441#issuecomment-6381519905)

### Satake diagrams and real forms have no formalization

[Issue #526](https://github.com/dzackgarza/research/issues/526) · [Complaint evidence](https://github.com/dzackgarza/research/issues/526#issuecomment-6381523650)

### Complex realization acts only on objects, and analytification exists only on affine spaces

[Issue #527](https://github.com/dzackgarza/research/issues/527) · [Complaint evidence](https://github.com/dzackgarza/research/issues/527#issuecomment-6381523861)

### The Hodge structure of a smooth complete intersection is present only for the quartic surface

[Issue #528](https://github.com/dzackgarza/research/issues/528) · [Complaint evidence](https://github.com/dzackgarza/research/issues/528#issuecomment-6381524057)

### Geometric lattice-database cards store no Betti numbers

[Issue #530](https://github.com/dzackgarza/research/issues/530) · [Complaint evidence](https://github.com/dzackgarza/research/issues/530#issuecomment-6381524244)

### Arrows of one Mor are built on handwritten hosts beside its element class

[Issue #454](https://github.com/dzackgarza/research/issues/454) · [Complaint evidence](https://github.com/dzackgarza/research/issues/454#issuecomment-6381520214)

### The classifying category of a group has no object set

[Issue #455](https://github.com/dzackgarza/research/issues/455) · [Complaint evidence](https://github.com/dzackgarza/research/issues/455#issuecomment-6381520451)

### Equivariant maps answer their natural transformation in two kinds

[Issue #456](https://github.com/dzackgarza/research/issues/456) · [Complaint evidence](https://github.com/dzackgarza/research/issues/456#issuecomment-6381520675)

### A graded module asks the ungraded Mor of its endpoints

[Issue #457](https://github.com/dzackgarza/research/issues/457) · [Complaint evidence](https://github.com/dzackgarza/research/issues/457#issuecomment-6381520845)

### Objects of Sets do not answer their endomorphisms or automorphisms

[Issue #458](https://github.com/dzackgarza/research/issues/458) · [Complaint evidence](https://github.com/dzackgarza/research/issues/458#issuecomment-6381521064)

### An object of one slice cannot be placed in a second slice

[Issue #468](https://github.com/dzackgarza/research/issues/468) · [Complaint evidence](https://github.com/dzackgarza/research/issues/468#issuecomment-6381521414)

### A finite owned ring does not enumerate its points

[Issue #572](https://github.com/dzackgarza/research/issues/572) · [Complaint evidence](https://github.com/dzackgarza/research/issues/572#issuecomment-6381625129)

### Spaces of modular forms with a character are not presented

[Issue #502](https://github.com/dzackgarza/research/issues/502) · [Complaint evidence](https://github.com/dzackgarza/research/issues/502#issuecomment-6381522381)

### `lean-categories` does not formalize the representation density or Siegel's formula

[Issue #585](https://github.com/dzackgarza/research/issues/585) · [Complaint evidence](https://github.com/dzackgarza/research/issues/585#issuecomment-6381627647)

### `lean-categories` does not formalize the values of a unimodular binary `ZZ_p`-lattice

[Issue #586](https://github.com/dzackgarza/research/issues/586) · [Complaint evidence](https://github.com/dzackgarza/research/issues/586#issuecomment-6381627810)

### The `even` ∧ `unimodular` join of owned lattices loses `delta()`

[Issue #573](https://github.com/dzackgarza/research/issues/573) · [Complaint evidence](https://github.com/dzackgarza/research/issues/573#issuecomment-6381625350)

### `lean-categories` does not formalize absolute Galois groups, their Frobenius elements, or the cyclotomic character

[Issue #587](https://github.com/dzackgarza/research/issues/587) · [Complaint evidence](https://github.com/dzackgarza/research/issues/587#issuecomment-6381628002)

### No embedding of the algebraic closure into Qbar_p is represented

[Issue #466](https://github.com/dzackgarza/research/issues/466) · [Complaint evidence](https://github.com/dzackgarza/research/issues/466#issuecomment-6381521268)

### `lean-categories` does not formalize symmetric groups as a functor on bijections

[Issue #432](https://github.com/dzackgarza/research/issues/432) · [Complaint evidence](https://github.com/dzackgarza/research/issues/432#issuecomment-6381518867)

### `lean-categories` does not formalize `GL_n` as a functor on rings

[Issue #432](https://github.com/dzackgarza/research/issues/432) · [Complaint evidence](https://github.com/dzackgarza/research/issues/432#issuecomment-6381518867)

### `lean-categories` uses "arithmetic subgroup" without defining it

[Issue #412](https://github.com/dzackgarza/research/issues/412) · [Complaint evidence](https://github.com/dzackgarza/research/issues/412#issuecomment-6381518289)

### `lean-categories` defines Coxeter systems but no morphisms of Coxeter data

[Issue #439](https://github.com/dzackgarza/research/issues/439) · [Complaint evidence](https://github.com/dzackgarza/research/issues/439#issuecomment-6381519485)

### Maps of a set into a module are not presented as a module

[Issue #588](https://github.com/dzackgarza/research/issues/588) · [Complaint evidence](https://github.com/dzackgarza/research/issues/588#issuecomment-6381628228)

### The real line is placed in no manifold category

[Issue #434](https://github.com/dzackgarza/research/issues/434) · [Complaint evidence](https://github.com/dzackgarza/research/issues/434#issuecomment-6381519095)

### The type of a finite root system is answered as a label

[Issue #589](https://github.com/dzackgarza/research/issues/589) · [Complaint evidence](https://github.com/dzackgarza/research/issues/589#issuecomment-6381628428)

### Category stubs presented ahead of `lean-categories` (2026-10-16)

[Issue #593](https://github.com/dzackgarza/research/issues/593) · [Complaint evidence](https://github.com/dzackgarza/research/issues/593#issuecomment-6381629165)

### Abelian groups and `ZZ`-modules are two categories with no equivalence

[Issue #533](https://github.com/dzackgarza/research/issues/533) · [Complaint evidence](https://github.com/dzackgarza/research/issues/533#issuecomment-6381524703)

### `integral_singular_cohomology` names two spaces on schemes

[Issue #527](https://github.com/dzackgarza/research/issues/527) · [Complaint evidence](https://github.com/dzackgarza/research/issues/527#issuecomment-6381523861)

### Families need base restriction and fibre products

[Issue #514](https://github.com/dzackgarza/research/issues/514) · [Complaint evidence](https://github.com/dzackgarza/research/issues/514#issuecomment-6381523060)

### Sheaves on a space are built on bases, not on `Open(X)`

[Issue #500](https://github.com/dzackgarza/research/issues/500) · [Complaint evidence](https://github.com/dzackgarza/research/issues/500#issuecomment-6381522173)

## Workflow Papercuts

### The live TODO has dependency edges to absent nodes

[Issue #46](https://github.com/dzackgarza/research/issues/46) · [Complaint evidence](https://github.com/dzackgarza/research/issues/46#issuecomment-6381515916)

### The required reading does not fit a worker context

[Issue #598](https://github.com/dzackgarza/research/issues/598) · [Complaint evidence](https://github.com/dzackgarza/research/issues/598#issuecomment-6381630082)

### Expectation files use names that AGENTS §5 calls aliases

[Issue #492](https://github.com/dzackgarza/research/issues/492) · [Complaint evidence](https://github.com/dzackgarza/research/issues/492#issuecomment-6381521799)

### TODO dependencies contain an unresolved ID and a prose prerequisite

[Issue #46](https://github.com/dzackgarza/research/issues/46) · [Complaint evidence](https://github.com/dzackgarza/research/issues/46#issuecomment-6381515916)

### Formal power series and their rings print without their coefficients

[Issue #596](https://github.com/dzackgarza/research/issues/596) · [Complaint evidence](https://github.com/dzackgarza/research/issues/596#issuecomment-6381629720)

### Finite cyclic subgroup membership is decided by enumerating powers

[Issue #431](https://github.com/dzackgarza/research/issues/431) · [Complaint evidence](https://github.com/dzackgarza/research/issues/431#issuecomment-6381518656)

### Zettlr all-workspace lint conflates component `id=` properties with Pandoc `#` identifiers

[Issue #599](https://github.com/dzackgarza/research/issues/599) · [Complaint evidence](https://github.com/dzackgarza/research/issues/599#issuecomment-6381630246)

### Flowmark Unicode-math lint scans inert comments and literal code

[Issue #600](https://github.com/dzackgarza/research/issues/600) · [Complaint evidence](https://github.com/dzackgarza/research/issues/600#issuecomment-6381630499)

### Source category-graph slices collapse parameterized fibres into self-edges

[Issue #597](https://github.com/dzackgarza/research/issues/597) · [Complaint evidence](https://github.com/dzackgarza/research/issues/597#issuecomment-6381629895)

### Toric scalar base change drops the toric construction data

[Issue #580](https://github.com/dzackgarza/research/issues/580) · [Complaint evidence](https://github.com/dzackgarza/research/issues/580#issuecomment-6381626623)

### Book recipes still target the former writing directory

[Issue #601](https://github.com/dzackgarza/research/issues/601) · [Complaint evidence](https://github.com/dzackgarza/research/issues/601#issuecomment-6381630671)

## Additional Mathematical Gaps

### Semantic lattice dispatch must retain the represented orbit, flag and sign data

[Issue #403](https://github.com/dzackgarza/research/issues/403) · [Complaint evidence](https://github.com/dzackgarza/research/issues/403#issuecomment-6381517574)

### Generators of parabolic subgroups of GL(M) over a PID

[Issue #398](https://github.com/dzackgarza/research/issues/398) · [Complaint evidence](https://github.com/dzackgarza/research/issues/398#issuecomment-6381516916)

### Double cosets in GL(J) for the lines of an isotropic plane

[Issue #396](https://github.com/dzackgarza/research/issues/396) · [Complaint evidence](https://github.com/dzackgarza/research/issues/396#issuecomment-6381516693)

### A finite presentation of GL_2(ZZ) is not formalized

[Issue #590](https://github.com/dzackgarza/research/issues/590) · [Complaint evidence](https://github.com/dzackgarza/research/issues/590#issuecomment-6381628630)

### Finiteness of O(L) for split binary lattices is not formalized

[Issue #584](https://github.com/dzackgarza/research/issues/584) · [Complaint evidence](https://github.com/dzackgarza/research/issues/584#issuecomment-6381627432)

### `lean-categories` does not state that O(V) is infinite for a definite rational space

[Issue #591](https://github.com/dzackgarza/research/issues/591) · [Complaint evidence](https://github.com/dzackgarza/research/issues/591#issuecomment-6381628818)

### The dual lattice of a unimodular lattice has integer norms without the field-element interface

[Issue #574](https://github.com/dzackgarza/research/issues/574) · [Complaint evidence](https://github.com/dzackgarza/research/issues/574#issuecomment-6381625538)

### Formed module categories are not below the chosen-presentation category

[Issue #565](https://github.com/dzackgarza/research/issues/565) · [Complaint evidence](https://github.com/dzackgarza/research/issues/565#issuecomment-6381623759)

### Base change of a discriminant module's underlying presented module asserts in the formed base change of its cover

[Issue #566](https://github.com/dzackgarza/research/issues/566) · [Complaint evidence](https://github.com/dzackgarza/research/issues/566#issuecomment-6381623951)

### Submodules of a finitely presented module have no owned equality or hash

[Issue #567](https://github.com/dzackgarza/research/issues/567) · [Complaint evidence](https://github.com/dzackgarza/research/issues/567#issuecomment-6381624137)
