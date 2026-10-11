# Preamble capabilities for primitive isotropic orbit enumeration

The preamble has much of the required algebra. The general strategy still
needs complete finite images of integral orthogonal groups, constructive
isometries between stabilized genus representatives, and a usable generating
description of the subgroup fixing a primitive null vector. There are also
unresolved formal and presentation obligations for genera and their class sets.

This is a source assessment, dated 2026-10-11. The research baseline is
`050e51ab7e`; the inspected `lean-categories` checkout is `29ff4ad`, and the
inspected `sage-indefinite-port` checkout is `993029f`. A source route in the
tables below means that its implementation exists. It does not establish that
the route executes or that its answers are correct. Correctness acceptance
belongs to the permanent mathematical assertions in `lean-cas-dsl`, as stated
in [INTENT.md](../INTENT.md).

## Mathematical dependency account

The input is a finite-rank, nondegenerate, even integral lattice of signature
`(s+, s-)`, with both signs present. Enumeration requires actual lattice
vectors, lattice inclusions and isometries, rather than numerical invariants
alone.

The algebra unfolds through these constructions:

- A bilinear pairing identifies the metric dual in the rational span. Its
  quotient by the lattice carries the discriminant quadratic form.
- An isotropic discriminant element generates a subgroup. Its inverse image
  under the discriminant projection gives an even overlattice, with the
  original lattice retained by an inclusion.
- A primitive null vector defines its line and perpendicular submodule.
  Quotienting the perpendicular by the line gives a nondegenerate lattice.
- Local isometry defines genus equivalence. Global isometry defines the
  classes within a genus. A finite class set, together with a selected lattice
  in each class, supplies the enumeration input.
- Automorphisms act on module quotients, submodules, cosets and finite sets.
  Images and stabilizers are subgroups with inclusions. Inverse images are
  pullbacks of those inclusions along group morphisms.
- A finite left and right action defines a double-coset set. Selected lifts
  of its representatives through the reduction map recover integral vectors.

Groups, module quotients, finite products, set actions and quotient sets are
the common foundations. The arithmetic theorems that connect these objects
are additional obligations of `lean-categories`.

## What is already present

Paths in this table are relative to
`src/dzack_research/preamble/categories/`.

| Required operation | Source already present | Remaining boundary |
| --- | --- | --- |
| Discriminant quadratic module and its finite orthogonal group | `lattices.py:3907`; `modules/framed/formed/discriminant_modules.py:604` | Compute the image of the integral orthogonal group, which may be proper. |
| Isotropic discriminant subgroups and their orthogonal quotients | `discriminant_modules.py:429,509` | Retain the subgroup inclusion and the identification with the new overlattice's discriminant form. |
| Explicit overlattice | `lattices.py:3476` | This returns an embedding `L -> M`. Keep that map when forming `L/dM` and the distinguished residue coset. |
| Perpendicular quotient of an isotropic line | `lattices.py:3460,5502`; `IsotropicReductions` | Retain the line, perpendicular inclusion and projection. |
| Integral hyperbolic partner | `lattices.py:5372` | The divisibility-one even case is covered by the integral norm correction. A selected partner must be retained when constructing a split model. |
| Genus from a lattice or from signature and discriminant form | `lattices.py:3033,1350` | Its formal classification and existence comparisons remain open. |
| Genus representatives and class number | `_Genus.representatives:776`, `class_number:796`; `_genus_classes:868` | These are implemented, including indefinite and small-rank branches. Completeness is an acceptance obligation; the class-set presentation also needs the maps described below. |
| Isometry comparison and explicit isometry | `lattices.py:2726,2735`; `lattice_morphisms.py:2505` | General indefinite witnesses depend on the port provider. |
| Full orthogonal group as an object | `lattices.py:2110` | Construction of `O(L)` does not compute its generators. |
| Selected generators of `O(L)` | `lattice_morphisms.py:2201,2240` | The indefinite branch imports a provider not found in the inspected port source. |
| Group morphisms specified on generators | `group/groups.py:2495` | The generator images must respect the source relations. Evaluation also needs a word lift through the chosen generating epimorphism; a finite generating set alone does not supply that algorithm. |
| Generated subgroup images | `group/groups.py:4509` | Predicate membership alone does not supply an image-generating set. |
| Subgroup inverse images and finite-index generators | `group/predicate_subgroups.py:544,605` | Schreier computation needs complete ambient generators and a finite quotient or finite-index route. |
| Finite images with selected source lifts | `group/groups.py:3479` | An explicit generator argument gives the image of the subgroup those generators generate. |
| Finite actions, orbit sets and point stabilizers | `group/g_sets.py:61,292`; `group/g_objects.py:1077` | These can perform the finite part after the actual acting groups and actions exist. |
| Pointwise and setwise lattice stabilizers | `lattice_morphisms.py:2003,2036,2055` | Predicate subgroups are available; complete generating families are a separate computation. |
| Isotropic parabolic and Levi action | `lattices.py:6502,6508,6523` | Existing Levi-image computation is restricted to definite reductions and calls the isotropic stabilizer provider. |
| Eichler transvections | `lattices.py:4185` | Compose them with the split-model isometry and extended automorphisms of the complement to compute the required pointwise stabilizer image. |
| Finite congruence module and induced action | `rational_integral_stabilizers.py:238,301,325,334,344` | This supplies the quotient, projection, quotient automorphisms, action functor and intermediate submodule. It does not itself enumerate the full arithmetic image or supply all lifts. |
| Selected double-coset calculations | `orthogonal_quotients.py:258`; `rational_integral_stabilizers.py:214` | The former handles discriminant/determinant/spinor character quotients; the latter delegates its computation to the port. General finite double cosets also arise from the existing finite-action construction. |
| Primitive isotropic vector orbit decomposition | `isotropic_orbits.py:104,784` | The existing decomposition obtains representatives through the port's isotropic-line computation. The proposed reduction can supply computation at this existing owner. |

The generated [megadoc](preamble-megadoc.md) indexes these construction
families. Its lattice line locations differ from the live source; the live
source locations above govern this assessment.

## The missing or incomplete functionality

### Complete arithmetic images, with lifts

For a positive modulus `d`, the required object is the actual image of
`O(M) -> Aut(M/dM)`. Counting with the full automorphism group of the quotient
would use a different acting group. Counting with images of some known
integral isometries can use a proper subgroup of the required image.

The existing finite-image algorithm can enumerate the image and retain a lift
above each element once a complete source-generating family is supplied. Thus
the missing input is arithmetic image computation, not finite group closure.
It can be supplied either by full integral orthogonal-group generators or by
a computation of the exact finite image. Representative recovery further
requires lifts; a count-only image computation can suffice for counting.

The same issue occurs first for the discriminant action of `O(L)`. The outer
orbit calculation must use its image, even when a larger finite orthogonal
group is easy to construct.

In `lattice_morphisms.py:2201`, indefinite generators are imported from
`sage_indefinite_port.indefinite.recursive`. The inspected port `src/` tree
contains `__init__.py`, `exceptions.py`, `invariants.py` and `py.typed`; the
promised `indefinite/recursive.py` is not in that tree. The frozen port
contract discussed in [HANDOFF.md](../HANDOFF.md) is a different source
surface. This finding establishes an unmet provider contract in the inspected
checkout, not absence of orthogonal-group algorithms elsewhere.

### Constructive stabilization isometries

For every selected genus class, representative recovery needs an explicit
isometry from the orthogonal sum of a hyperbolic plane and its selected
representative into the overlattice. The isometry must transport the standard
null vector and all subsequent group actions.

The public `Isom` and `isometry_to` interfaces already express this request.
Their general indefinite branch at `lattice_morphisms.py:2593` imports
`isometry` from the same missing provider module. A theorem establishing
uniqueness in the genus supplies existence; it does not supply the required
computational witness. Definite isometry routines cannot resolve this step:
the stabilized lattices are indefinite even when the complements are definite.

For higher divisibility, counting also needs the residue of a selected null
vector in each full orthogonal orbit and its stabilizer image inside the
same finite reduction group. A stabilization isometry supplies these data.
An alternative computation of these finite marked data can suffice for a
count, but the genus class number alone supplies neither of them.

### The finite image of the subgroup fixing a null vector

An infinite-index vector stabilizer cannot be generated by the finite-index
Schreier route merely because its reduction image is finite. Its defining
predicate is already expressible, but its finite image requires more data.

For a selected splitting `M = U orthogonal-sum K` and a selected generator
`e` of the first null line, the subgroup fixing `e` has an explicit route.
Extend an isometry of `K` by the identity on `U`. Combine these extensions
with the transvections

\[
T_a(e)=e,\qquad
T_a(f)=f+a-\frac{(a,a)}2e,\qquad
T_a(x)=x-(a,x)e\quad(x\in K).
\]

Evenness makes these integral. An isometry fixing `e` induces an isometry
of `e`'s perpendicular quotient. After removing its extension, the remaining
isometry is uniquely a `T_a`; the displayed equations also give
`T_a T_b = T_(a+b)`. This derives the description `K semidirect-product O(K)`
for the subgroup fixing the vector.

Consequently a basis of `K` supplies the transvection generators, and the
required finite image of the extended `O(K)` supplies the other factor.
Reduction of `T_a` depends only on `a` modulo `dK`: replacing `a` by `a+db`
changes the half-norm by `d(a,b)+d^2(b,b)/2`, a multiple of `d`.

The preamble has the transvections and the pointwise subgroup. The remaining
work is this generated description, its transport through the chosen split
isometry, and its finite image with lifts. The inspected Levi-image method
accepts only definite reductions, so it does not cover arbitrary signatures.
For an indefinite `K`, an exact finite image of `O(K)` can suffice; computing
its entire infinite group is a stronger possible input.

The subgroup preserving the null line also permits `e -> -e`. The subgroup
used here fixes the vector. Their finite images can differ.

### Genus class sets and their maps

A categorical core retains objects and only invertible arrows. The set of
isometry classes is its set of connected components. Taking the core of the
category of lattices in a genus therefore does not itself give the class set.
The distinction is visible in
`abstract_categories/arrow_categories.py:2035`: `Core` keeps the same objects.

`lean-categories` already defines `GenusCat`, `genusClassSet`, `GenusClass`
and `classNumber` in `LocalGlobal.lean:244` and `Mass.lean:92-104`. The
preamble already computes selected genus representatives and a class number.
It therefore needs no new independent genus-enumeration interface merely to
start this calculation.

The presentation gap is that `_Genus` exposes lattices as facade points and
returns a finite set of representatives. The inspected owner supplies no
explicit class projection and selected section identifying this finite set
with the formal genus class set. The finite-family `isometry_classes`
operation partitions a supplied family; it does not supply those maps for the
whole genus. The required structural result is the formal class set, its
class projection, and a selected lattice representative of each class.
Constructive isometries remain a distinct operation on representatives.

### Formal genus and orbit theorems

The existing [genus complaint](../COMPLAINTS.md#genera-of-integral-lattices-are-formalized-without-finiteness-parity-or-classification)
and `genera-present-their-formalization` node already own the missing formal
comparisons. The inspected `Mass.lean:111` and `ReducedBasis.lean:458`
establish genus finiteness for positive definite lattices. The inspected
`GenusInvariants.lean` supplies rank, signature and determinant invariance.

For this strategy, the additional formal obligations include even-genus
classification and existence from discriminant data, indefinite genus
finiteness, stabilization uniqueness under the rank-length hypothesis, the
divisibility-one orbit/class-set correspondence, the passage through an
isotropic overlattice, and the finite-quotient orbit-splitting theorem. The
local `Valued/` search did not locate declarations for the latter orbit
reduction theorems. A search of the released registry, linked projects,
community sources and the pinned Mathlib dependency remains required before
asserting global absence. These are formalization capability questions, not
permission for local semantic replacements.

## Finite operations that compose from existing foundations

Let `G` be the computed finite reduction image, `H` the subgroup preserving
the marked submodule and residue coset, and `R` the computed vector-stabilizer
image. The admissible subset `D` consists of elements sending the selected
null-vector residue into the marked coset.

The action

\[
(H\times R)\times D\longrightarrow D,
\qquad ((h,r),g)\longmapsto hgr^{-1}
\]

has the desired double cosets as orbits. Closure follows because `H`
preserves the marked coset and `R` fixes the selected vector residue.
`FiniteGSets`, finite group products and orbit sets already express this
construction. A named double-coset method would expose that same construction;
its absence from the general group owner is not a missing fundamental
operation for this finite computation. GAP also supplies
[DoubleCosets](https://gap-system.github.io/gap/doc/ref/chap39_mj.html)
and selected representatives at its private computation boundary.

Likewise, preserving a submodule and a coset can be expressed as an action
on a marked pair, or as a setwise submodule stabilizer followed by a point
stabilizer on its quotient. A point stabilizer of one discriminant element
alone is insufficient to express an arbitrary marked submodule/coset pair.
The missing connection is the induced action on these marked objects, using
the actual inclusion and quotient maps.

Subgroup inverse images already suffice for the required congruence subgroup.
A general pullback of group maps is a separate reusable construction. The
category-level `fiber_product` expresses it through products and equalizers,
but the inspected group product implementation requires finite factors and
the group files supply no equalizer realization. General effective pullbacks
of arbitrary infinite generated groups remain a capability gap. They are not
required to count with the finite images once those images are available.

## Hypotheses and smaller computational targets

The rank-length condition used in stabilization follows once a complement
`K` exists: its discriminant group has generator length at most `rank(K)`,
and adjoining a hyperbolic plane increases rank without changing that group.
This places the stabilized even indefinite lattice within the uniqueness
criterion stated in Huybrechts, *Lectures on K3 Surfaces*, Chapter 14,
Remark 1.6 ([textbook](https://ncatlab.org/nlab/files/HuybrechtsLecturesOnK3.pdf)).
The criterion is used after establishing existence of a complement genus.

The required work depends on the output:

| Output | Required extra input beyond the existing constructions |
| --- | --- |
| Divisibility-one orbit count | The complement genus and its complete class number, with the formal orbit/class-number theorem. Full `O(L)` generators are unnecessary for this count. |
| Divisibility-one vector representatives | Selected genus representatives and explicit stabilization isometries. |
| General divisibility orbit count | The actual discriminant image, complete complement genera, exact congruence images, and selected null-vector residues with their stabilizer images in those groups. Obtain the marked data through stabilization isometries or an equivalent finite computation. |
| General divisibility vector representatives | The preceding data, explicit stabilization isometries, and source lifts of the selected finite representatives. |

Small-rank complements must retain their own arithmetic. In particular,
indefinite binary classes are not covered by the strong-approximation argument
for higher-rank indefinite spinor genera. The preamble has a separate binary
branch. Magma's documented number-field
[GenusRepresentatives](https://magma.maths.usyd.edu.au/magma/handbook/text/348)
requires rank at least three; its availability does not settle every
small-rank input. Its finite `Limit` option can also stop enumeration early.
These facts concern the surveyed interface, not a recommendation to replace
the present Sage route.

The decisive next capabilities are thus exact arithmetic images with the
needed lifts, constructive stabilization, the split vector-stabilizer action,
and the formal genus/class-set comparisons. Existing finite actions, subgroup
inverse images, overlattice embeddings and genus algorithms are inputs to that
work.
