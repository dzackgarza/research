---
id: SPEC-DISCRIMINANT-FORM-ORBIT-SURFACES
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[SPEC-MAPPING-LATTICES]]'
- '[[PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT]]'
title: Define discriminant-form isotropic orbit objects
status: in-progress
priority: medium
requirement: 'The Coble cusp and discriminant-orbit arguments require finite
  discriminant-form objects, their automorphism groups, isotropic subsets, finite orbit
  sets, stabilizers, and the separate lattice-lifting theorem or algorithm that relates
  discriminant-form orbits to primitive isotropic lattice vectors.'
acceptanceCriteria:
- Each object or operation is stated as a mathematical claim with category/refinement,
  hypotheses, witnesses, codomain or return object, and source evidence.
- The finite formed-module objects are separated from lattice-level lifting and
  primitive-isotropic orbit theorems.
- The spec does not promise generators, presentations, or full lattice orbit algorithms
  unless the stronger group category or backend witness is named.
- Sage TorsionQuadraticModule, QuadraticForm, GAP, Oscar, Hecke, and stored Dawes or
  building evidence are used only as implementation witnesses for the stated
  mathematical operations.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Spec: Discriminant-Form Isotropic Orbit Objects

## Relationship to existing specs

Phase 4 (PHASE-LATTICE-04-DUALS-MEETS-AND-DISCRIMINANT-DESCENT) already specifies
discriminant-group methods: `b(x,y)`, `q(x)`, `invariants()`, `cardinality()`,
`isotropic_elements()`, `elements_of_norm(n)`, `is_isometric_to(other)`,
`isomorphic_as_groups(other)`, `is_p_elementary(p)`, `p_rank(p)`, `value_map()`.

These operations give the finite torsion module `A`, the quotient-valued quadratic
form `q: A -> Q/2Z`, and the subset of isotropic elements.  The remaining mathematical
objects needed for cusp and orbit computations are:

- the automorphism group `O(A,q) = Aut_{TorsionQuadraticModules}(A,q)`;
- the action of `O(A,q)` or a specified subgroup `G <= O(A,q)` on the finite set `A`;
- the finite subset `Iso(A,q) = {a in A : q(a) = 0}`;
- orbit sets such as `Iso(A,q)/G` and `{a in A : q(a)=n}/G`;
- stabilizers `Stab_G(a)` or `Stab_G(S)` for elements or subgroups;
- the separate lattice theorem or algorithm relating a discriminant class to primitive
  isotropic vectors in a lattice with discriminant form `(A,q)`.

## Mathematical Claims

### Discriminant Orthogonal Group

For a finite torsion quadratic module `(A,q)`, the orthogonal group

`O(A,q) = Aut_{Modules(ZZ).WithForms().Quadratic().Torsion()}(A,q)`

is the group of automorphisms of the underlying finite abelian group preserving `q`
and the associated bilinear form where present.

Weakest category:
`Modules(ZZ).WithForms().Quadratic().Torsion().AutCategory()`.

Witnesses:
finite torsion module presentation, quotient-valued quadratic form, and a certified
automorphism or stronger finite/generated group representation when generator methods
are claimed.

Computational consequence:
membership of a proposed automorphism is checkable by finite abelian group
automorphism data plus form preservation.  Methods such as `gens()`,
`presentation()`, or a concrete matrix-group return are valid only for a refinement
whose construction supplies generator or presentation witnesses.

### Isotropic Elements and Norm Fibers

For a finite torsion quadratic module `(A,q)`,

`Iso(A,q) = {a in A : q(a) = 0 in Q/2Z}`

is a finite subset of `A`.  More generally, for a value `n in Q/2Z`,

`A_n = {a in A : q(a) = n}`.

Weakest category:
finite torsion quadratic modules with an enumerable finite carrier.

Witnesses:
finite presentation of `A`, value codomain for `q`, exact equality in `Q/2Z`, and
enumeration of the finite carrier or a source-backed finite subset constructor.

### Orbit Sets and Stabilizers

For a subgroup `G <= O(A,q)` acting on a finite subset `X <= A` preserved by `G`, the
orbit set

`X/G`

is a finite quotient set.  For `x in X`, the stabilizer is

`Stab_G(x) = {g in G : g(x) = x}`.

When `G` is given by certified generators and the action on `A` is effective on the
finite set `X`, the representative-level constructions are:

- `orbit_G(x) = {x*g : g in G} <= X`;
- `orbits_G(X) = {orbit_G(x) : x in X}`;
- a representative set `R <= X` with one element in each orbit;
- `Stab_G(x)` as a subgroup of `G`, with generator witnesses only when the finite
  group-action backend returns them in the same group representation.

Weakest category:
finite group actions when `G` is finite with an enumerable or generated action; lazy
group-action objects when `G` is only defined by predicates and membership witnesses.

Witnesses:
the subgroup inclusion `G <= O(A,q)`, a certified action on `A`, proof or check that
`X` is `G`-stable, and finite enumeration or generator witnesses when orbit
representatives are requested.

Typed computation requirement:
a finite backend may enumerate orbits only after choosing a bijection between `X` and a
finite action domain and proving that every generator of `G` preserves `X`.  The backend
output must be converted back to elements of `A` and subgroups of the original
generated `G`.  Raw GAP points, tuples, permutation labels, or Smith-coordinate lists
are not public return objects for discriminant-form orbits.

For stabilizers, the conversion must preserve the acting group.  If the backend acts
directly with `G.gap()` on encoded elements of `X`, then a GAP stabilizer subgroup can
be converted back through the same `FqfOrthogonalGroup` subgroup constructor.  If the
backend first replaces the action by a permutation image `rho(G) <= Sym(X)`, then
`PermutationGroup.stabilizer(label(x))` returns `Stab_{rho(G)}(label(x))`, not
`Stab_G(x)`.  The public stabilizer is the preimage
`rho^{-1}(Stab_{rho(G)}(label(x)))`; returning only the image stabilizer is a different
object and must be named as such.

Public consequences:
`isotropic_orbits()` is shorthand for `Iso(A,q)/O(A,q)` only when the chosen
orthogonal-group realization supplies the finite action data needed to enumerate
orbits.  Otherwise the spec should expose the orbit object and membership/equality
claims without promising representatives.

### Lattice Lifting

Let `L` be an even nondegenerate integral lattice with discriminant form `(A_L,q_L)`.
The natural homomorphism

`O(L) -> O(A_L,q_L)`

is a group homomorphism induced by the action on `L^#/L`.  Its kernel is the stable
orthogonal group `\widetilde O(L)`.

For a primitive lattice vector `v in L`, let

`div(v) = <b(v,w) : w in L> = d Z`

in the scalar-valued integral case.  Then `v/d in L^#`, and the class

`\bar v = v/d + L in A_L`

is the discriminant class attached to `v`.  If `v` is isotropic, then
`q_L(\bar v) = v^2/d^2 = 0 in Q/2Z`, so `\bar v` lies in `Iso(A_L,q_L)`.

The implication from lattice orbits to discriminant-form orbits is formal: if
`g in O(L)` and `w=g(v)`, then `div(w)=div(v)` and
`\bar w = \bar g(\bar v)` under the induced action of `O(L)` on `A_L`.  Thus an
`O(L)`-orbit of primitive isotropic vectors maps to an orbit for the image subgroup
`im(O(L) -> O(A_L,q_L))`.

The converse is not a finite discriminant-form operation.  A claim that finite
`O(A_L,q_L)`-orbits classify primitive isotropic `O(L)`-orbits requires a theorem or
backend with hypotheses.  The source-backed theorem patterns currently available to
the spec are the following.

- Nikulin surjectivity: if `L` is an even indefinite two-elementary lattice, then the
  homomorphism `O(L) -> O(A_L,q_L)` is surjective.  This lets a finite
  `O(A_L,q_L)`-orbit be read as an orbit for the image of `O(L)` only after the
  lattice has been verified to be even, indefinite, and two-elementary.
- Nikulin's stronger uniqueness/surjectivity theorem for an even indefinite lattice
  requires the checked local length hypotheses of Theorem 1.14.2: for every `p != 2`,
  `rank(L) >= ell((A_L)_p)+2`, and in the borderline 2-primary case the 2-primary
  discriminant form has a required `u_+^(2)(2)` or `v_+^(2)(2)` summand.
- Eichler criterion: when `L` contains `2U`, two primitive vectors are equivalent under
  `tilde SO^+(L)` exactly when they have the same square and the same discriminant
  class `v/div(v) + L`.  For primitive isotropic vectors this reduces stable-plus
  equivalence to the discriminant class, but only under the `2U` hypothesis and for the
  stable-plus subgroup.
- For the Coble target `T_Co ~= N=2(<1>+E_10)`, this cited Eichler criterion is not
  available: every pairing in `N` is divisible by `2`, so `N` contains no copy of the
  hyperbolic plane `U` and hence cannot contain `2U`.
- a named primitive-isotropic orbit backend for isotropic line or plane orbit
  computation when the previous theorem hypotheses are not enough.

Surjectivity of `O(L) -> O(A_L,q_L)` does not by itself construct primitive vector
representatives, prove divisibility values, or compute stable-subgroup orbits.  Those
are separate lattice obligations.  Since `\widetilde O(L)` acts trivially on `A_L`,
stable orbit statements must be made with the actual discriminant class fixed and with
the additional theorem or backend that controls the kernel action.

For the Coble/K3 pipeline, the admissible statement is therefore: first compute the
actual Coble lattice `T`, its discriminant form `(A_T,q_T)`, the divisibility of the
primitive isotropic vectors under consideration, and the finite orbit structure in
`Iso(A_T,q_T)`; then apply a checked Nikulin, Eichler, stable-plus, or backend theorem
to convert that finite result into a lattice orbit claim.  The finite orbit
calculation alone is not a proof of the lattice statement.

For the Dolgachev-Kondo standard Coble target

`N = <2> + E_10(2)`

the source states that the K3 orthogonal complement `N_X` is two-elementary of signature
`(2,9)`, has discriminant form `q_N = -q_M`, and is isomorphic to this `N`.  Thus
Nikulin's even indefinite two-elementary surjectivity theorem applies to this standard
target as a statement about `O(N) -> O(q_N)`.  The project decision identifies
`S_Co=f^*Pic(S)` with Dolgachev-Kondo's `M_X` and identifies
`T_Co=(f^*Pic(S))^\perp` with `N_X ~= N`, so the source-level Coble target is fixed.
Implementation code that builds `T_Co` from geometric input still owes the
corresponding constructor or isometry witness.

For the same standard target, every primitive vector has divisibility `2`: with the
repo convention `E_10=U+E_8(-1)`, one has

`N = <2> + E_10(2) = 2(<1> + E_10),`

and `<1>+E_10` is unimodular.  A primitive vector in the underlying unimodular lattice
therefore has pairing ideal `Z`, so the pairing ideal in `N` is `2Z`.  This settles the
standard-target divisibility claim, but it transfers to the project `T_Co` only through
the construction or isometry witness above.

For this standard target, the finite isotropic set is also determined:

`|Iso(A_N,q_N)| = 528`.

This is an exact enumeration of the `2^11` classes in `B/2B` for
`N=2B`, `B=<1>+U+E_8(-1)`, using the criterion `q_N(a/2+N)=0` iff
`B(a,a)=0 mod 4`.  The full finite discriminant orthogonal group is the stabilizer in
`GL(B/2B)` of the four fibers of `Q(a mod 2B)=B(a,a) mod 4`; exact GAP/Sage
computation gives orbit sizes `[1, 527]` on `Iso(A_N,q_N)`.  This is a finite
discriminant-form orbit statement, not a lattice orbit classification.

Weakest category:
lattices with discriminant descent plus a specified orthogonal subgroup/refinement.

Witnesses:
the lattice `L`, the discriminant descent `L -> L^# -> A_L`, the subgroup of `O(L)`,
the image subgroup in `O(A_L,q_L)`, and the theorem or backend that identifies the
lattice orbit with the finite discriminant-form orbit.

Primitive totally isotropic planes are a further lattice-level object.  Their orbit
statements require a primitive plane `J <= L`, the quotient lattice `J^\perp/J`, and a
building or isotropic-subspace orbit theorem/backend.  They are not methods on a
single element of `A_L`.

Source evidence:
`theory/references/literature/nikulin1979integral.md:882-898` for Theorem 1.14.2,
`theory/references/literature/nikulin1979integral.md:1595-1597` for surjectivity of
`O(S) -> O(q_S)` for even indefinite two-elementary lattices,
`theory/references/literature/dolgachev_kondo_2013.md:97-101` for the Coble K3
orthogonal complement as a two-elementary lattice of signature `(2,9)` isomorphic to
`N=<2>+E(2)`,
`.agents/plans/features/FEATURE-COBLE-CUSP-ORBIT-CLASSIFICATION/decisions/DECISION-TCO-DEFINITION-AND-SIGNATURE.md:40-43`
for the convention `E_10=U+E_8(-1)` and the presentation
`N=<2>+U(2)+E_8(-2)`,
`theory/foundations/coble-standard-target-discriminant-form.md` for the exact
standard-target finite isotropic count,
`theory/foundations/reflective-two-elementary-lattices.md:372-385` for the Eichler
criterion, and `theory-orbit-and-building-backends` for the separate
isotropic-line/plane backend shape.

## Source-Backed Implementation Evidence

`TorsionQuadraticModule.orthogonal_group(gens=None, check=False)` is Sage evidence for
the finite generated group refinement of `O(A,q)` for Sage torsion quadratic modules.
The source constructs the ambient automorphism group of the finite abelian group with
Smith invariants `A.invariants()`, then returns `FqfOrthogonalGroup(ambient, gens, A)`.
If `gens` is supplied, Sage coerces each supplied matrix, automorphism, or acting object
through the ambient abelian-group automorphism group; this realizes the subgroup of
`O(A,q)` generated by certified finite automorphisms.  If `gens is None`, Sage calls
`_isom_fqf(A)` and caches a small generating set for the full orthogonal group; the
source labels this a slow brute-force computation.

Source evidence:
`sage/modules/torsion_quadratic_module.py:816-887` and
`sage/groups/fqf_orthogonal.py:490-578`.

`FqfOrthogonalGroup._preserves_form(f)` is Sage evidence for the membership witness:
for Smith generators `g_i`, it checks `q(f(g_i)) = q(g_i)` and
`b(f(g_i), f(g_j)) = b(g_i,g_j)`.  This is the finite formed-module preservation
condition, not a lattice-level isometry computation.

Source evidence:
`sage/groups/fqf_orthogonal.py:282-297`.

`ActionOnFqf` is Sage evidence for the right action of the generated orthogonal group
on the torsion quadratic module and invariant subquotients.  Elements are acted on by
the matrix of a group element relative to Smith-form generators, then converted back to
the torsion module by `linear_combination_of_smith_form_gens`.

Source evidence:
`sage/groups/fqf_orthogonal.py:299-487`.

Sage's carrier enumeration and element data come from the finitely presented PID-module
parent inherited by `TorsionQuadraticModule`: `gens()` returns selected generators or
Smith-form generators, element evaluation uses `b` and `q`, and finite enumeration is
owned by the underlying finite FGP module.

Source evidence:
`sage/modules/torsion_quadratic_module.py:420-537` and `[[SPEC-MAPPING-LATTICES]]`.

Oscar/Hecke backend evidence:
the current Oscar/Hecke documentation gives exact `TorQuadModule` discriminant-group
objects, element lifts, `is_isometric_with_isometry(T,U)`, submodules,
`stable_submodules(T, G)`, torsion quadratic modules with a chosen isometry
`(T,f)`, and `automorphism_group_with_inclusion(T,f)`, where `O(T,f)` is the
centralizer of `f` in `O(T)` with an inclusion into `O(T)`.

Source evidence:
Oscar/Hecke discriminant-group docs, `https://docs.oscar-system.org/v1.4/Hecke/manual/quad_forms/discriminant_group/`;
Oscar/Hecke torsion-quadratic-module-with-isometry docs,
`https://docs.oscar-system.org/dev/NumberTheory/QuadFormAndIsom/torquadmodwithisom/`;
Hecke `src/QuadForm/Torsion.jl:2540-2585`;
Oscar `src/NumberTheory/QuadFormAndIsom/torsion_quadratic_module_with_isometry.jl:341-415`;
`theory/backends/oscar-lattices`; `theory-backend-routing`.

Backend consequence:
Oscar/Hecke is a candidate exact backend for discriminant-form objects, isometry tests,
stable submodule enumeration, and centralizer subgroups attached to a specified
isometry.  Oscar also has generic finite group-action objects: for a group `G`, an
explicit finite set `Omega`, and an action function `Omega x G -> Omega`, its `GSet`
methods compute orbits and stabilizers, including setwise stabilizers of finite
subsets.  This is exact finite group-action evidence, not a typed torsion-quadratic
module operation by itself; a discriminant-form use must still supply the conversion
from elements of `A` to the finite action carrier and back.

Source evidence:
Oscar `docs/src/Groups/action.md`;
Oscar `src/Groups/gsets.jl:571-627` and `src/Groups/gsets.jl:671-740`;
Oscar `src/Groups/action.jl:667-736`.

Oscar's torsion-quadratic-module-specific stabilizer methods act on subgroup
inclusions, not arbitrary finite subsets of elements.  The method
`stabilizer(O::AutomorphismGroup{TorQuadModule}, i::TorQuadModuleMap)` returns the
stabilizer of the image of an inclusion `i` under the action on subgroups of the
codomain.  The lattice methods
`stabilizer_discriminant_subgroup`, `pointwise_stabilizer_in_orthogonal_group`, and
`setwise_stabilizer_in_orthogonal_group` compute stabilizers of discriminant subgroups
or sublattices under their stated lattice hypotheses.  They do not provide a public
operation whose input is an arbitrary finite subset `X <= A` and a specified subgroup
`G <= O(A,q)`.

Source evidence:
Oscar `src/Groups/abelian_aut.jl:651-705`;
Oscar `src/NumberTheory/QuadFormAndIsom/finite_group_actions.jl:327-378`;
Oscar `src/NumberTheory/QuadFormAndIsom/finite_group_actions.jl:623-787`.

Negative finding:

- Searched: Hecke commit `59fda6c7f49a87112cccff49dc96871c951d384a`,
  Oscar commit `3e172ec3133371e73f710b3907fcf48549a1c40e`, the Oscar/Hecke
  discriminant-group docs, the Oscar torsion-quadratic-module-with-isometry docs, the
  Oscar group-action docs, Hecke `src/QuadForm/Torsion.jl`, Oscar
  `src/NumberTheory/QuadFormAndIsom/torsion_quadratic_module_with_isometry.jl`,
  Oscar `src/NumberTheory/QuadFormAndIsom/finite_group_actions.jl`, Oscar
  `src/Groups/abelian_aut.jl`, Oscar `src/Groups/action.jl`, Oscar
  `src/Groups/gsets.jl`, and local memories `theory/backends/oscar-lattices`,
  `theory/backends/gap-orbits`, and `theory-backend-routing`.
- Found: exact `TorQuadModule` construction and invariants, isometry and anti-isometry
  tests with maps, stable-submodule enumeration under supplied maps, and
  `automorphism_group_with_inclusion(T,f)` for centralizers in `O(T)`.  Oscar also
  provides generic `GSet` orbit and stabilizer operations once a finite carrier and
  action function are supplied.  The checked torsion-quadratic-module and
  lattice-specific methods stabilize subgroups, images of inclusion maps, sublattices,
  or diagonal primitive-extension data, not arbitrary finite subsets of elements of a
  discriminant form.
- Conclusion: based on the checked docs and source, Oscar/Hecke should be recorded as
  a backend for formed-module objects, stable submodules, subgroup stabilizers,
  centralizers, primitive embeddings, equivariant extension work, and generic finite
  group actions.  I found no source evidence in these versions for a
  torsion-quadratic-module-specific operation taking `G <= O(A,q)` and an arbitrary
  finite subset `X <= A` and returning typed orbit representatives and stabilizers in
  `G`; the project-owned Sage/GAP conversion layer remains the typed route for that
  operation.
- Confidence: High for the checked commits and files.
- Gaps: newer Oscar/Hecke commits or undocumented downstream examples may expose such
  a typed route; any future backend card should cite that newer source before replacing
  the local finite-action conversion witness.

Stored theory to keep separate:
`theory-orbit-and-building-backends`, `theory-backend-routing`, and
`theory/foundations/reflective-two-elementary-lattices.md` distinguish finite
discriminant-form orbits from lattice-level stable/plus orbit algorithms.

Runtime witness:
for `D = TorsionQuadraticForm(matrix.identity(2)/2)`, Sage constructs
`G = D.orthogonal_group()` with `G.gens()`, `G.order()`, `G.subgroup(...)`, and a right
action `D.gen(0) * G.gen(0)`.  The same object has no public `orbit`, `orbits`, or
`stabilizer` methods.  The only source-backed orbit code found in this Sage family is
the private helper inside `_isom_fqf`, which calls GAP `Orbits(..., OnTuples)` while
searching for generators or isometries.

Source evidence:
`sage/groups/fqf_orthogonal.py:520-536`, `sage/groups/perm_gps/permgroup.py:1672-1948`,
and runtime probe of `FqfOrthogonalGroup_with_category`.

Sage's `PermutationGroup.orbit(point, action=...)`, `orbits()`, and
`stabilizer(point, action=...)` are implementation evidence for the finite-action
backend shape: GAP computes orbits and stabilizers on a finite permutation domain, and
Sage converts the result back to the permutation group's domain or subgroup
representation.  This is evidence for a project conversion layer from typed
discriminant-form elements to finite action labels and back, not evidence that
`FqfOrthogonalGroup` already owns public typed orbit methods.

Source evidence:
`sage/groups/perm_gps/permgroup.py:1672-1968`.

`FqfOrthogonalGroup._subgroup_constructor(libgap_subgroup)` is Sage evidence for the
direct-GAP stabilizer route: a subgroup produced inside the libgap representation of
`G` can be converted back to a generated `FqfOrthogonalGroup` subgroup by coercing GAP
generators through the parent group.

Source evidence:
`sage/groups/fqf_orthogonal.py:344-365`.

Consequence:
finite orbit and stabilizer enumeration for discriminant-form subsets is not inherited
as a public Sage method of `FqfOrthogonalGroup`.  The project should specify it as a
bounded local construction from the finite carrier `X`, the generated finite group
`G`, and the certified action `x * g`; a GAP-backed implementation may use
`libgap.Orbits` and `libgap.Stabilizer` only after the conversion between project
elements and GAP action points is stated.

Project implementation witness:
`category_specs/lattices/subcategories/constructions/discriminant_form_actions.py`
implements this finite-action conversion for Sage torsion quadratic modules.  For
`G <= O(A,q)` realized as a Sage `FqfOrthogonalGroup`, let `D = G.invariant_form()`
be the torsion quadratic module and let `B = G.domain()` be Sage's underlying finite
abelian-group parent.  The action label of `x in D` is the GAP point `B(D(x)).gap()`,
and a returned GAP point `y` is converted back to the torsion quadratic module by
`D.linear_combination_of_smith_form_gens(B(y).exponents())`.
The subset constructor checks that the supplied finite tuple has no duplicate module
elements and that every generator of `G` preserves the subset.  Point stabilizers are
computed by `libgap.Stabilizer(G.gap(), label(x), libgap.OnPoints)` and converted back
to a subgroup of the original generated group by `G._subgroup_constructor`, so the
public return object is `Stab_G(x) <= G`, not a stabilizer inside a permutation image.

Example witness:
`category_specs/lattices/category_obligations.sage` constructs
`D = TorsionQuadraticForm(I_2/2)` and the generated subgroup of `O(D)` swapping the two
Smith generators.  The category-obligation example verifies that the two generators of
`D` form one orbit and that the stabilizer of one generator is the trivial subgroup of
the original generated orthogonal group.

## Non-Goals

- Do not re-specify the discriminant group's bilinear/quadratic form evaluation (Phase 4).
- Do not specify lattice-level isometry backends as methods on the finite discriminant
  object.
- Do not identify `O(A,q)` with a matrix group carrying generators unless the chosen
  realization actually supplies that stronger finite generated group data.
- Do not implement orbit enumeration from first principles before surveying existing
  finite-group orbit methods in GAP/Sage/Oscar.

## Remaining Lattice-Level Obligations

The finite discriminant-form actions and the conditional lattice-lifting theorem
families above are source-grounded.  The unresolved claims are now the lattice-level
subgroup/lifting data and the plane-orbit backend, not the finite orbit object:

- the subgroup of `O(T_Co)` whose orbit is being asserted, its image in `O(A_T,q_T)` if
  it is not full `O(A_T,q_T)`, and the Nikulin/Eichler hypotheses or backend theorem
  controlling primitive-isotropic lattice orbits;
- the implementation-level construction of `T_Co=(f^*Pic(S))^\perp` from geometric
  input, if later code must build the lattice rather than use the accepted source-level
  target `N=<2>+E_10(2)`;
- a named backend or theorem for primitive isotropic plane or flag orbits whenever the
  statement involves `J <= L` rather than a primitive vector class.
