# Integral-affine manifolds and polyhedral constructions

This document specifies the mathematical objects and maps needed to construct the
integral-affine spheres of [AEGS, §4]. It is a category design, not a claim that
the stated constructions have been implemented. Semantic declarations belong to
`lean-categories`; the research preamble presents them and may use maintained
geometry engines privately. The relevant existing presentations are
[`manifolds.py`](../../src/dzack_research/preamble/categories/manifolds.py),
[`polytopes.py`](../../src/dzack_research/preamble/categories/schemes/polytopes.py),
and the unfinished [`simplicial-and-cw-foundations`](../../TODO.md) node.

## Manifolds and the dimension filtration

Fix Hausdorff and second-countable manifolds of finite dimension. A real
`C^k` manifold, for `k >= 1`, has an equivalence class of atlases whose
coordinate changes are `C^k` diffeomorphisms. Its morphisms are `C^k` maps.
An atlas is a presentation of the structure; compatible atlases determine the
same maximal atlas. `C^infinity` gives smooth real manifolds. For `j >= k`,
forgetting derivatives defines a functor `C^jMan -> C^kMan`. It is not an
inclusion with the same hom sets: a `C^k` map between smooth objects need not
be smooth. Topological manifolds receive the corresponding forgetful functor.

The dimension is locally constant. Let `Man_n` denote objects of dimension
exactly `n`; for connected objects this is unambiguous, while a disconnected
manifold can have components of different dimensions unless the category
requires pure dimension. The filtration by dimension at most `n` is a full
subcategory for any chosen map class. The exactly `n` objects form its pure
dimension stratum. `Man_2` consists of surfaces; “surface” alone does not
imply compactness, orientation, boundary, or a smooth structure. Manifolds
with boundary and corners require explicit local models and distinct map
conditions. Polygon pieces are such objects before edge gluing.

A complex analytic `m`-manifold has holomorphic charts in `CC^m` and
holomorphic morphisms. Its realification is a smooth real manifold of dimension
`2m`. A complex manifold is thus structured over a real smooth manifold, not
an alternative value for a field parameter on a single undifferentiated
manifold category. `RR^n` and `CC^m` have their standard identity charts and
must be admitted as objects of the corresponding manifold categories. In the
current preamble, `DifferentiableManifolds` stores a finite degree,
`SmoothManifolds` presents smooth real manifolds, and `ComplexManifolds`
forgets to smooth real manifolds. The placement of `RR` itself remains a
separate recorded gap in [`TODO.md`](../../TODO.md).

## Integral-affine structure: selected data and forgetful functors

Let `V` be a real vector space of dimension `n` with a full lattice
`Lambda <= V`. Its integral-affine group is

`Aff_Lambda(V) = GL(Lambda) semidirect V`.

An integral-affine atlas on a real `n`-manifold `B` consists of charts to open
subsets of `V` whose changes of coordinates are restrictions of elements of
`Aff_Lambda(V)`. Equivalently, it is a maximal atlas of that kind. A specified
atlas or an equivalent developing-map and holonomy presentation determines a
chosen integral-affine structure. The lattice of integral tangent vectors is
part of that structure. A smooth atlas alone does not select it. Distinct
integral-affine structures may live over the same smooth manifold.

There are two useful map categories. In `IAff_n`, morphisms are locally maps
`x |-> A x + b` with `A(Lambda) <= Lambda'`; isomorphisms require
`A(Lambda) = Lambda'`. These maps may have noninvertible or rectangular
linear parts if dimensions vary. The subgroupoid of integral-affine local
isomorphisms uses `A in GL_n(ZZ)`. Both have a forgetful functor to smooth real
manifolds. Over a fixed smooth `B`, the fibre records its possible selected
integral-affine structures and maps over `id_B`. The functor does not make
those structures properties of `B`.

Translations in this definition lie in `V`, not necessarily in `Lambda`.
If an application requires chart origins and overlaps to preserve lattice
*points*, it asks for the stricter group `GL(Lambda) semidirect Lambda`, plus
the resulting integral-point data. AEGS uses the latter convention for its
specified charts [AEGS, Introduction]; it must not silently replace the
general definition. An oriented integral-affine atlas has linear changes in
`SL(Lambda)`. Orientation is a refinement of the selected structure; it does
not follow from dimension two.

Integral-affine maps forget to smooth maps. Ordinary smooth maps do not lift
canonically to integral-affine maps. Products have product atlases. A quotient
or gluing is integral-affine only after its local transition maps, including
those near identified faces, satisfy the atlas conditions.

## Singular integral-affine spaces and spheres

The sphere in [AEGS, §4] is not an integral-affine manifold on all of `S^2`.
Its data are `(B, Sigma, A)`, where `B` is a topological surface, `Sigma` is a
finite subset, and `A` is an integral-affine atlas on `B \ Sigma`. The atlas
does not extend across a point of `Sigma`; a punctured neighbourhood has an
affine monodromy representation, with linear part in `GL_2(ZZ)`. If the
construction uses orientation, its linear part lies in `SL_2(ZZ)`. Some
applications also retain a chosen triangulation with integral vertices, an
affine polarization, or group actions. These are further data, not implicit
in `(B, Sigma, A)`.

Define the category of singular integral-affine surfaces with maps of the
underlying topological surfaces that carry the specified singular sets as
required and restrict to integral-affine maps on their regular loci. The
exact morphism condition at a singular point must be stated for each map
class; isomorphisms preserve the singular set and affine structure. Its
topological-sphere subcategory has `B` homeomorphic to `S^2` and is the
natural home of `IAS^2`. The dimension-`n` analogue gives `IAS^n`, with a
specified singular subset of appropriate codimension and local models. A
two-dimensional puncture model alone does not define the higher-dimensional
theory.

An abstract dual complex `Gamma(X_0)` records intersections of components of
`X_0`. It does not determine `A` or `Sigma`. Under the hypotheses of the
degeneration, the affine structure is extra data or a derived construction on
the dual complex [Foundations, Definition 62.6]. The AEGS triangulation and
commuting involutions must be retained as separate structure on the sphere.

## Polytopes, ambient spaces, and triangulations

A polytope has an abstract face incidence structure and, when realized, a
placement in an ambient geometric space. Keep these apart:

* A finite abstract polytope or polytopal complex has its face poset, rank,
  attaching or incidence maps, and abstract automorphisms.
* A Euclidean polytope is a bounded convex subset of an affine space modelled
  on an inner-product space `E^n`; the embedding into that space is selected.
  An affine lattice `Lambda <= E^n` makes lattice vertices meaningful. The
  metric `b_std` on `ZZ^n` is useful for Euclidean lengths and orthogonal
  symmetries but is not required by integral-affine geometry.
* Spherical and hyperbolic polytopes lie in `S^n` and `H^n`, with geodesic
  faces and the relevant convexity hypotheses. They have common incidence
  operations with Euclidean polytopes, while their geometric maps and metric
  computations remain specific to their ambient geometries.

For a chosen triangulation `T` of a polygon or complex `P`, retain the
triangles, all face inclusions, and the map `|T| -> P`. An integral
triangulation has vertices in the specified local affine lattices and
integral-affine attaching maps. “Unimodular triangulation” is stronger: each
top-dimensional simplex has normalized lattice volume one. Completeness
requires the triangles to cover `P` with intersections equal to shared faces.
For a singular integral-affine surface, specify a triangulation compatible
with `Sigma` and check integrality in each regular chart. The existing
`ConvexPolytopes(Lambda)` presents rational coordinate polytopes and their
integral points; it does not yet present selected triangulations or the full
geometric range described here.

## Face gluings and surgeries

For a finite family of polygonal complexes `P_i`, a gluing datum is a finite
family of paired boundary faces and specified face isomorphisms. The quotient
`B = (disjoint union P_i)/~` is a topological colimit with structure maps
`P_i -> B`. Face subdivisions must make each pairing cellular. A proposed
surface is checked locally: interior points have disk links; boundary points
have interval links if boundary is allowed. At a vertex the cyclic order of
incident sectors determines whether its link is a circle, an interval, or
another graph. Incidence alone gives the quotient topology, not its affine
atlas.

To glue integral-affine pieces, every regular face pairing must extend to an
integral-affine identification of adjacent collars. Continue the charts over
regular glued edges. Around a vertex, compose the affine transition maps in
cyclic order. Trivial affine monodromy with a compatible neighbourhood permits
a regular chart; nontrivial monodromy or failed extension marks a singular
point. Record the resulting singular set and holonomy. Topological surface
checks and affine extension checks are distinct mathematical obligations.

A surgery is specified by an embedded subcomplex or local region `Q -> P`, a
replacement `Q'`, and a boundary identification `dQ' -> dQ`. Its output is
the pushout `(P \ int Q) union_{dQ} Q'`, with the inherited cell maps and any
induced affine atlas on its regular part. “Remove a corner” or “remove a basis
triangle” is not a complete operation until the region, lattice basis,
replacement, and boundary map are given. A unimodular triangle is the simplex
on `p, p+u, p+v` for a basis `(u,v)` of the local tangent lattice. Symington
surgeries require their own stated cut and regluing data, size, and resulting
monodromy [AEGS, §4]; they should use this general surgery owner rather than
define a second gluing mechanism.

For the AEGS doubling `B(ell) = P(ell) union_{boundary} P(ell)^opp`, the
specified common-boundary identification is the gluing datum. The result is
topologically a sphere when `P(ell)` is a disk. Its affine structure is
checked on the two interiors and across the glued boundary away from the
listed singularities. The Enriques and del Pezzo involutions are explicit
automorphisms of the resulting structured sphere, with their actions on
faces, singularities, and affine charts. [AEGS, Introduction and §4] gives
the relevant constructions and examples.

## Complexes, stars, links, and realizations

A glued polygonal surface is naturally a two-dimensional cell or polytopal
complex. It is a regular CW complex when every closed cell embeds and its
attaching map is a homeomorphism onto its image. Self-identifications can
break regularity. A compatible triangulation can give a simplicial complex
when simplices are determined by distinct vertex sets and meet in common
faces. A `Delta`-complex allows more face identifications. A simplicial set
is another presentation, with degeneracies; the Kan condition is a horn
filling condition and is not inherent in a polygon gluing. A PL manifold
requires the relevant vertex links to be PL spheres or balls. Thus none of
these labels follows from the words “dual complex” alone. These constructions
meet the existing [`simplicial-and-cw-foundations`](../../TODO.md) node.

For a cell `sigma` in a selected complex `K`, its closed star is the union of
closed cells containing `sigma`; its link is the complex of directions
transverse to `sigma` in that star (equivalently, in a simplicial complex, the
simplices disjoint from `sigma` whose joins with `sigma` lie in `K`). Retain
their inclusions into the subdivision or ambient complex. The link of a
regular interior vertex of a triangulated surface is a circle; a boundary
vertex has an interval link. Stars and links are combinatorial constructions
and can also inherit restricted affine data away from singularities.

There are three distinct symmetry questions. `Aut(face(P))` is the abstract
incidence automorphism group. Integral-affine automorphisms preserve the
selected affine placement or atlas. Isometries preserve a selected ambient
metric and embedding. A combinatorial involution may have no realization as
an affine map or Euclidean reflection. To draw its fixed line, first give an
explicit realization and an equivariant action. A planar polygon drawing
with edge-pair labels and an embedding `B -> RR^3` are presentation maps;
neither defines the abstract quotient or its integral-affine structure.

## Dependency and acceptance boundary

The mathematical dependency chain is: spaces and maps; manifolds and atlases;
affine spaces with lattices and affine groups; polytopes with faces;
complexes, subcomplexes and quotients; selected triangulations; singular
integral-affine atlases; then spheres, actions and realizations. The finite
gluing diagram is a colimit, but an affine structure on that colimit requires
the additional local extension argument above. No leaf computation or drawing
is evidence for a mathematical assertion in this chain.

Useful mathematical assertions at the owners include: the face maps of a
triangulation cover its polygon with the prescribed intersections; the
boundary quotient of two disks is a sphere; every regular vertex link is a
circle; the product of transition maps around a designated singular vertex
is its stated monodromy; and the two specified involutions square to the
identity, commute, and preserve the affine structure on their regular loci.
An abstract group computation is accepted by its action on the face poset;
the stronger geometric symmetry claims require their own placement data.

## References

* [AEGS] V. Alexeev, P. Engel, D. Z. Garza, and L. Schaffler,
  [*Compact moduli of Enriques surfaces of degree 2*](https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/compact-moduli-of-enriques-surfaces-of-degree-2/BFE699F491BB75D1D4DFC61B1556780B),
  *Nagoya Mathematical Journal* **259** (2025), 581–624, Introduction and §4.
  The local [source extraction](../../references/literature/lattice-research/aegs_2023.md)
  records the atlas convention, triangulations, Symington polygons, doubling,
  and involutions.
* [Foundations] [`lean-categories/FOUNDATIONS.md`, Definition 62.6](../../../gitclones/lean-categories/FOUNDATIONS.md),
  integral-affine structure with singularities on a dual complex.
* J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Chapters 1–2,
  for smooth atlases, smooth maps, and manifolds with boundary.
* A. Hatcher, [*Algebraic Topology*](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf),
  §2.1, for `Delta`-complexes and quotient cell structures.
* G. M. Ziegler, *Lectures on Polytopes*, Chapters 1–2, for convex polytopes
  and face lattices.
