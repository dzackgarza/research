# Integral-affine manifolds and polyhedral constructions

This document specifies the mathematical objects and maps needed to construct the
integral-affine spheres of [AEGS, §4]. It is a category design, not a claim that
the stated constructions have been implemented. The research preamble presents
these objects and maps and may use maintained geometry engines privately. The
relevant existing presentations are
[`manifolds.py`](../../src/dzack_research/preamble/categories/manifolds.py),
[`polytopes.py`](../../src/dzack_research/preamble/categories/schemes/polytopes.py),
and the unfinished [`simplicial-and-cw-foundations`](../../TODO.md) node.

## Category graph and declaration kinds

The graph below enumerates the mathematical homes needed by the construction.
It is a dependency graph, not a proposed Sage inheritance graph. `⊂` and
`⊃` mean subcategory inclusion with the same parameters and stated morphisms. `→`
means an explicit functor or construction, often with changed maps, base, or
underlying object. A property following `.` is an axiom/refinement of its
owning category. A chosen datum belongs to a structured category or to an
existing slice, comma, functor, or Grothendieck construction. None of these
nodes is a preamble declaration until its objects, morphisms, data, and
inclusions are specified. This follows [`CAT-15`–`CAT-20` and
`CAT-30`](../../CONTRIBUTING.md), especially the ban on a class for a mere
property combination or a named datum already expressed by a standard
categorical construction.

```text
TopologicalSpaces
  ⊃ TopologicalManifolds
       .DimensionAtMost(n)
       .PureDimension(n); .PureDimension(2) = topological surfaces
  ⊃ TopologicalManifoldsWithBoundary / WithCorners (specified local models)

RealCkManifolds(k), k >= 1 → TopologicalManifolds
  .PureDimension(n); .PureDimension(2) = real C^k surfaces
  RealCkManifolds(j) → RealCkManifolds(k), j >= k
  SmoothRealManifolds = RealCkManifolds(infinity)
RealCkManifoldsWithBoundary / WithCorners → TopologicalSpaces

ComplexManifolds(m) → SmoothRealManifolds(2m)   [realification]
RR^n ∈ SmoothRealManifolds.PureDimension(n)
CC^m ∈ ComplexManifolds(m)

RealVectorSpaces(n) → RealAffineSpaces modelled on V
  affine lattice Lambda ↪ V → (affine space A, Lambda)
  (A, Lambda) → Aff_Lambda(A) = GL(Lambda) ⋉ V

IntegralAffineManifolds(n) → SmoothRealManifolds(n)
  .Oriented
IntegralAffineManifoldsWithBoundary / WithCorners →
  SmoothRealManifoldsWithBoundary / WithCorners
  strict lattice-point atlas → ordinary integral-affine atlas

(B, Sigma, atlas on B \ Sigma) = SingularIntegralAffineSpaces(n)
  → (B, Sigma) in selected-subobject geometry
  → IntegralAffineManifolds(n) on B \ Sigma
  .FiniteSingularSet.PureDimension(2)
       .Sphere = IAS^2; .Disk = IA disks; .RealProjectivePlane = IA RP^2
  higher-dimensional IAS^n requires its own singular local models

FiniteGradedPosets ⊃ AbstractPolytopes
affine space A → ConvexPolytopesIn(A) → AbstractPolytopes [face poset]
  .Dimension(2) = polygons
  .IntegralVertices relative to (A, Lambda) = lattice polytopes
EuclideanSpaces(E^n) → EuclideanPolytopesIn(E^n)
SphericalSpaces(S^n) → SphericalGeodesicPolytopesIn(S^n)
HyperbolicSpaces(H^n) → HyperbolicGeodesicPolytopesIn(H^n)
  each realized polytope → AbstractPolytopes [face incidence]

CellComplexes
  .RegularCW / .PLManifold (properties with exact hypotheses)
  PolytopalComplexes → CellComplexes
  SimplicialComplexes → CellComplexes by realization
  DeltaComplexes → CellComplexes by realization
  SimplicialSets → Spaces by realization; .Kan is a horn-filling property

(K, T, |T| → |K|) = chosen triangulation over K
  .Integral relative to a selected affine lattice/atlas
  .Unimodular relative to that lattice

finite diagram of faces and face maps → colimit complex B
  plus affine collar data → (B, Sigma, atlas on B \ Sigma)
subobject Q ↪ P and boundary isomorphism dQ' → dQ → surgery pushout
degeneration X_0 → dual complex Gamma(X_0) → CellComplexes

GObjects(G, C) → C, for C = complexes, polytopes, or singular IA spaces
Mor(C)(X, Y) holds an embedding/realization with exact endpoints
```

Several displayed labels name **objects or predicates**, not category classes.
`RR^n`, `CC^m`, a chosen lattice, a particular triangulation, a gluing
diagram, a surgery datum, an embedding, and `Gamma(X_0)` are each objects or
arrows of their owners. `IAS^2` denotes the sphere property of an object
with a selected singular affine structure; it does not require a separate
class for each sphere topology and decoration. `GObjects(G,C)` is the existing
category construction for a specified group action. Two commuting
involutions amount to an action of `C_2 × C_2`, with its actual action map,
when both generate that group.

The following table fixes the owner of each requested operation and the data
that its result must retain.

| Requested object or operation | Mathematical owner | Retained data or map |
| --- | --- | --- |
| Real or complex affine coordinate space | Affine spaces over `RR` or `CC`, then the manifold chart construction | Space, coordinate chart, topology, dimension |
| Smooth, `C^k`, complex manifold | Its atlas category | Underlying weaker manifold and chosen atlas; realification for complex manifolds |
| Integral-affine manifold | Integral-affine atlas structure over a smooth real manifold | Exact smooth manifold, maximal affine atlas, tangent lattice, forgetful functor |
| Singular integral-affine sphere | Singular integral-affine spaces with sphere property | `B`, inclusion `Sigma ↪ B`, atlas on `B \ Sigma`, monodromy |
| Abstract automorphism group | Automorphisms of the face-poset object | Permutations preserving rank and incidence |
| Integral-affine or metric symmetry | Automorphisms of the corresponding structured object | Explicit maps of the selected realization or atlas |
| Polytope in `E^n`, `S^n`, or `H^n` | Convex/geodesic polytopes over the selected ambient geometry | Ambient space, inclusion, faces and incidence |
| Lattice polytope | Integral-vertex refinement relative to `Lambda ↪ A` | Lattice inclusion and polytope placement |
| Chosen integral triangulation | Triangulation object over a polytope or complex | Triangle family, face maps, `|T| → |K|`, lattice |
| Stars, links, and subdivision | Cell/simplicial complex owner | Subcomplexes and their inclusions |
| Edge identification or many-piece gluing | Diagram and colimit in the applicable complex category | Face isomorphisms and every piece-to-quotient map |
| Corner or basis-triangle surgery | Subobject, boundary map, and pushout | Region inclusion, replacement, boundary identification, quotient maps |
| Dual complex | Construction from a degeneration's boundary incidence data | Incidence complex and source-to-complex correspondence |
| Embedding in `RR^3` or planar display | Morphism or display of the completed object | Explicit map, ambient space, edge-pair labels where applicable |

The graph is deliberately not a diamond of named combinations. A chosen
triangulation is not an `IntegralTriangulatedPolytope` class; it is an object
over a polytope, refined by an integrality predicate relative to its lattice.
Likewise, `IAS^2` with two involutions is a `G`-object in the category of
singular integral-affine spaces satisfying the sphere condition. An abstract
face-poset automorphism does not acquire a geometric realization merely from
membership in that automorphism group. These distinctions are required by
[`OWN-15`–`OWN-18` and `CAT-30`](../../CONTRIBUTING.md).

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
linear parts if dimensions vary. The category of integral-affine local
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
the dual complex. The AEGS triangulation and
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

## Public mathematical API and types

The signatures in this section specify a proposed semantic language. They
do not assert that the named methods exist today. Each signature identifies
the mathematical owner, input, output, and retained structural arrows. Write
`Mor(C)(X,Y)` for the hom object of a category `C`, `Sub_C(X)` for subobjects
with inclusions into `X`, and `Fin(I,X)` for an `I`-indexed family. A finite
family of points is a map `I -> U(X)`; an indexed family of objects of `C` is
a functor from the discrete category on `I` to `C`. These are established
constructions, not new category classes for each decorated family
([`CAT-30`](../../CONTRIBUTING.md)). All mathematical components reachable
from a public result, including family elements and morphism endpoints, remain
preamble values ([`OWN-04`](../../CONTRIBUTING.md)).

### Atlases and manifold maps

For `k >= 1`, the construction

`RealCkManifolds(k).on(B, atlas) -> M`

takes a specified topological manifold `B` and compatible `C^k` chart data.
It retains `B` as the underlying object. A chart is an isomorphism in the
appropriate local-map category from an open submanifold `U ↪ M` to an open
subobject of `RR^n`. An atlas retains its chart family, domain inclusions,
overlaps, and transition maps; its maximal extension determines the same
structure. The following operations have fixed owners and types:

| Operation | Type and defining data |
| --- | --- |
| `M.dimension()` | Dimension or locally constant dimension function on components; for pure dimension, the common value in `ZZ_{>=0}`. |
| `M.atlas()` | The established atlas and its open domains, charts, and transition morphisms. |
| `M.open_submanifold(i: U ↪ M)` | Restricted manifold structure on the exact open subobject `U`, retaining `i`. |
| `Mor(RealCkManifolds(k))(M,N)` | `C^k` maps with stated source and target; composition is the category's composition. |
| `RealCkManifolds(j).forget_to(k)` | Functor on objects and morphisms for `j >= k`. |
| `ComplexManifolds.realification()` | Functor on objects and holomorphic maps, with real dimension `2m` for complex dimension `m`. |

`RR^n` and `CC^m` enter by their standard charts through these same
constructions. The existing preamble already has chart, atlas, transition-map,
dimension, and sphere operations in [`manifolds.py`](../../src/dzack_research/preamble/categories/manifolds.py);
their current existence does not establish the entire signature above. Lee,
*Introduction to Smooth Manifolds*, Chapters 1–2 supplies the atlas and
smooth-map definitions.

### Integral-affine atlases and singularities

Let `M` be a specified smooth real `n`-manifold. The category-owned
construction

`IntegralAffineManifolds(n).on(M, A) -> X`

takes an atlas `A` whose coordinate changes lie in
`GL(Lambda) semidirect V` and retains the exact `M`, its chart domains, and
their transition morphisms. `X.underlying_smooth_manifold()` exposes that
retained object. `IntegralAffineManifolds(n).forget()` is the functor on both
objects and affine maps; the accessor does not rebuild `M`.

| Operation | Type and defining data |
| --- | --- |
| `X.integral_tangent_lattice()` | Locally constant lattice of integral tangent vectors on `X`, with transition action induced by the linear part of the atlas. |
| `X.affine_charts()` | Chart family with exact domains, affine models, and transitions. |
| `Mor(IntegralAffineManifolds)(X,Y)` | Maps locally of the form `x -> A x + b`, with the lattice condition on `A`; isomorphisms have invertible lattice maps. |
| `X.holonomy(x,frame)` | A representation `pi_1(X,x) -> GL(Lambda) semidirect V` after base point and affine frame are supplied. Without a frame, retain its conjugacy class. |
| `X.regular_open(i: U ↪ X)` | Restricted affine structure on an open subobject and its actual inclusion. |

Holonomy requires its base point and frame. An engine's selected matrix is a
coordinate representative, not the intrinsic representation without those
choices. The stricter translation lattice and the oriented determinant-one
condition are distinct refinements with the group stated at construction.

For the AEGS sphere, the constructor is instead

`SingularIntegralAffineSpaces(2).on(B, i: Sigma ↪ B, A_{B\Sigma}) -> X`.

The open complement `j: B\Sigma ↪ B` and the integral-affine structure on
its domain are defining data. `X.singular_locus()` returns `i`, and
`X.regular_locus()` returns `j` and the restricted structured manifold.
`X.local_monodromy(p, loop, frame)` takes `p in Sigma`, a loop in a
punctured neighbourhood, and an affine frame; it returns the corresponding
element of the affine group. A local singularity type requires the full stated
equivalence relation, not only a matrix trace. The `Sphere` property is a
condition on `B`; an involution or triangulation is an added datum. This is
the structure in [AEGS, Introduction and §4].

### Polytopes and chosen triangulations

For an ambient affine or metric space `A`, `PolytopesIn(A)(data) -> P`
establishes a polytope with its inclusion `P ↪ A`. The `data` parameter means
the mathematical defining datum specified by that category, such as vertices
or supporting halfspaces in the affine case; it is not an opaque engine
handle. The constructor of a lattice polytope also receives and retains the
selected lattice embedding `Lambda ↪ A`. Euclidean, spherical, and
hyperbolic versions use their own geometric convexity conditions. The
existing [`ConvexPolytopes(L)`](../../src/dzack_research/preamble/categories/schemes/polytopes.py)
already exposes vertices, facets, integral points, and a normal fan for its
presented rational affine case. Ziegler, *Lectures on Polytopes*, Chapters
1–2 supplies the affine face-lattice definitions.

| Operation | Type and defining data |
| --- | --- |
| `P.vertices()` | Finite set of points of the selected ambient space. |
| `P.faces(d)` | Finite family of `d`-faces, each with its inclusion into `P` and incidence maps. |
| `P.face_poset()` | Graded incidence poset derived from those faces and maps. |
| `P.boundary()` | Boundary complex with its inclusion into `P`. |
| `P.integral_points()` | Set of points of the selected affine lattice lying in `P`, when a lattice is given. |
| `P.abstract_automorphisms()` | `Aut(P.face_poset())`, acting on the face poset. |
| `P.geometric_automorphisms()` | Automorphisms preserving the specified placement and its stated affine or metric structure. |

A chosen triangulation over `P` is `(T, r: |T| -> P)`, with simplex and face
maps retained. The owner of `triangulations(P)` is the category of
triangulations over `P`, rather than a new class for every adjective. An
operation `P.triangulate()` may compute and return one such object. Its
`T.simplices(d)`, `T.simplex_inclusion(sigma)`, and `T.realization_map()`
have owned endpoints. `Integral` states that the chosen simplex vertices are
integral in the relevant local charts; `Unimodular` states normalized volume
one for each maximal simplex. Neither property supplies a hidden choice of
triangulation.

### Complexes, gluing, surgery, and dual complexes

The cell-complex owner supplies `K.cells(d)`, `K.face_poset()`,
`K.star(sigma)`, `K.link(sigma)`, and `K.subdivision()`. Stars and links are
subcomplexes with inclusion maps. A subdivision returns the new complex and
the comparison `|K'| -> |K|`. `K.realization()` retains each cell's
characteristic map. In a simplicial complex, `link(sigma)` consists of the
simplices disjoint from `sigma` whose joins with it lie in `K`. For a
triangulated surface, vertex links determine the local surface condition.
Hatcher, *Algebraic Topology*, §2.1 gives the `Delta`-complex gluing model;
the existing [`simplicial-and-cw-foundations`](../../TODO.md) node owns the
general complex foundation.

The general gluing input is a finite diagram `D: I -> CellComplexes` of
pieces, selected faces, and specified face maps. `CellComplexes.colimit(D)`
returns the quotient `B` and its universal cocone `q_i: D(i) -> B`. Pairwise
edge gluing and many-piece gluing use the same construction. When affine
collar maps are supplied, the structured construction also returns the
singular set, the atlas on its complement, and the maps from every original
piece. It verifies the topological surface condition separately from the
affine extension condition; a colimit in cell complexes alone does not imply
a colimit in singular integral-affine spaces.

Surgery takes `i: Q ↪ P`, replacement `Q'`, and an isomorphism
`f: boundary(Q') -> boundary(Q)`. Its result is the pushout of the complement
and replacement, with the old and new maps into that pushout. A basis-triangle
specialization supplies `p, u, v`, with `(u,v)` a basis of the local tangent
lattice; a corner specialization supplies its actual region and boundary map.
The Symington operation supplies its cut, size, and affine reglueing datum
as in [AEGS, §4]. Each specialization enters the same pushout construction.

For a suitable degeneration `X_0`, `X_0.dual_complex()` returns the
incidence complex `Gamma(X_0)` together with the correspondence between cells
and intersections of boundary components. An affine atlas on that complex is
constructed from additional degeneration data and hypotheses. The dual
complex alone does not determine it.

### Actions, embeddings, and display

For a category `C`, `GObjects(G,C)` owns actions `rho: G -> Aut_C(X)`.
Two specified commuting involutions on `X` define an action of
`C_2 × C_2`; faithfulness requires a further condition. `X.fixed_locus(g)`
is a subobject with inclusion where the fixed-locus construction exists.
There are separate actions on an abstract face poset, a realized polytope,
and a singular integral-affine space. The maps between their automorphism
groups are explicit restriction or forgetful homomorphisms, with hypotheses
for a lift. A symmetry line in a drawing needs an equivariant realization.

An embedding `e: B -> RR^3` is a morphism of the underlying topological or PL
objects with the embedding property. A sphere cannot embed in `RR^2`; a
planar picture presents polygon pieces and labelled edge-pairing arrows.
The drawing and rendering operations consume these mathematical maps. Plot
coordinates, a mesh, or an interactive view are display artifacts and cannot
replace `B`, its gluing cocone, or its affine atlas.

### Public/private execution boundary

| Public mathematical contract | Private implementation at its named owner |
| --- | --- |
| Categories, `Mor`, subobjects, indexed families, diagrams, functors, and actions | Engine classes, Python containers, adjacency tables, handles, and dispatch state. |
| Exact atlas, lattice, chart, face, inclusion, projection, and quotient maps | Coordinate arrays, polyhedron records, chart storage, and group-engine objects. |
| Stars, links, colimits, surgery pushouts, groups, embeddings, and owned results | Incidence traversal, maintained polyhedral and group algorithms, layout, and rendering. |

The selected mathematical operation and its hypotheses determine the private
computation. The adapter may lower its defining data to a maintained engine,
compute there, and raise the result through the same category constructor,
retaining every structural map ([`OWN-02`–`OWN-09`](../../CONTRIBUTING.md)).
Foreign result objects cannot cross the public boundary through accessors,
iterators, morphisms, or lazy families. A public `from_raw`, `from_engine`,
`unwrap`, backend selector, or dynamic forwarding path would create another
mathematical language from implementation details. Computation that supplies
only an invariant, such as a group order or polytope dimension, does not
supply the richer object, action, or embedding whose construction was asked
for. The general operation remains at its mathematical owner even when a
particular computational case is unavailable.

## Existing constructions and precise reuse paths

The following inventory is based on the inspected preamble source. A new
`super_categories()` edge is admitted only for an inclusion with the same parameters and morphisms;
a change of structure, ambient space, or morphisms uses a functor
([`CAT-15`–`CAT-16`](../../CONTRIBUTING.md)).

| Existing owner | Supplied mathematics | Wiring into the proposed constructions | Exact gap |
| --- | --- | --- | --- |
| [`TopologicalSpaces`](../../src/dzack_research/preamble/categories/topological_spaces.py) | Continuous `Mor`, open subsets, coproducts, coequalizers, and final-topology quotients. | Build the polygon gluing as a finite diagram of underlying spaces. Retain its quotient and every piece-to-quotient map as the underlying object of a singular-affine space. | A topological quotient still needs surface links and affine collar charts. General openness for predicate subsets is limited by the [finite-atlas complaint](../../COMPLAINTS.md). |
| [`TopologicalManifolds`, `DifferentiableManifolds`, `SmoothManifolds`, `ComplexManifolds`](../../src/dzack_research/preamble/categories/manifolds.py) | Dimensions, chart families, transitions, a stereographic smooth sphere, and a complex-to-smooth route. | Add the integral-affine atlas to the **same** smooth manifold; restrict it to the exact open complement of the singular set. Use the existing realification route for complex manifolds. | Direct constructors currently allocate a manifold from a dimension and name; they do not equip a supplied manifold. [`RR` manifold placement](../../TODO.md) remains unfinished. The transition constructor trusts supplied inverses, so the affine layer needs its own transition and cocycle conditions. |
| [`Cat`](../../src/dzack_research/preamble/categories/abstract_categories/cat.py) | `Mor`, slices, subobjects, finite-diagram colimits, and `pushout_construction` with a selected cocone. | Treat each face inclusion as a subobject arrow, each edge pairing as a diagram arrow, and each surgery as a pushout. Retain the cocone and universal factor map. | The applicable complex and affine morphism categories must be supplied. A generic colimit does not establish surface or affine structure. The [pushout complaint](../../COMPLAINTS.md) records an object-only route that loses the selected cocone. |
| [`ConvexPolytopes(L)`](../../src/dzack_research/preamble/categories/schemes/polytopes.py) | Rational affine polytopes from vertices or halfspaces; owned vertices, facets, integral points and normal fans; `Integral` and `Polygon` refinements. | AEGS lattice polygons enter `ConvexPolytopes(L).Integral().Polygon()` when they satisfy its coordinate contract. Their faces feed the common complex and triangulation constructions. | `facets()` returns face polytopes without their inclusions into the original polytope. No selected polygon triangulation or polygon-gluing construction is supplied by this owner. |
| [`RegularPolytopes`](../../src/dzack_research/preamble/categories/schemes/polytopes.py), [`PartiallyOrderedSets`](../../src/dzack_research/preamble/categories/sets/set_categories.py), and [`Graphs`](../../src/dzack_research/preamble/categories/graph_categories.py) | A Schläfli/Coxeter symmetry group for regular examples, an order category, and graphs. | Construct a general polytope's face poset with its order, then its abstract automorphism group. The one-skeleton is a graph image of the retained complex. | The regular group is not a general automorphism algorithm. The current regular-polytope order placement and monotone-map surface are unresolved in [`TODO.md`](../../TODO.md). A graph alone loses two-cells and attaching maps. |
| [`RationalPolyhedralCones(L)`](../../src/dzack_research/preamble/categories/polyhedral_cones.py) | Ray triangulation, simplicial subcones, ray-span saturation indices, and private Sage `PointConfiguration` computation. | Reuse its triangulation for cone-valued operations. Relate a cone and a polygon only through an actual section, homogenization, or projectivization map. Both feed the same chosen-triangulation concept. | `simplicial_subcone_inclusion()` is only a set map because cone `Mor` is missing ([`COMPLAINTS.md`](../../COMPLAINTS.md)). A cone-ray triangulation is not a polygon triangulation. |
| [`HyperbolicSpaces` and `HyperbolicPolyhedra`](../../src/dzack_research/preamble/categories/hyperbolic_geometry.py) | A selected hyperbolic space, projectivized rational cone, ordinary and ideal vertices, and wall data. | Keep this space and cone as the source for the supported hyperbolic-polytope specialization. Map its face incidence to the common abstract complex owner. | It does not supply every hyperbolic polytope, a spherical polytope, or a Euclidean ambient space. The proposed general categories require their own definitions. |
| [`GObjects(G,C)`](../../src/dzack_research/preamble/categories/group/g_objects.py) | An action functor `BG -> C`, equivariant maps, supported orbit sets and spaces, quotient projections, and stabilizers. | Construct the two AEGS involutions as one `C_2 × C_2` action on the singular-affine sphere. Forget it to compatible actions on its topological space and cell complex. Use its orbit projection for quotients. | `orbits()` computes only for `G`-sets in the inspected method; `orbit_space()` forms a topological quotient, which may be an orbifold. A cell permutation alone does not establish an integral-affine action. |
| [`RiemannianManifolds`](../../src/dzack_research/preamble/categories/manifolds.py) | A metric as extra structure on a smooth manifold. | Select `b_std` or another metric on an ambient Euclidean realization only when metric lengths or isometries are requested; compare its symmetry action to affine automorphisms by an explicit map. | An integral-affine lattice or a drawing does not select a Riemannian metric. |

### Where duplication would break the construction

**Atlases and lattices.** The affine structure is built on the exact manifold
whose topology and charts the manifold owner established. Its integral
tangent lattice is the local system given by the linear parts of those
selected transitions. Making a fresh Sage manifold for `IAS^2`, copying each
chart into an independent coordinate table, or deriving a new lattice from
each polygon's vertices would split the authority for overlaps. The
construction must retain the original manifold, open-domain inclusions and
affine transition maps ([`OWN-15`–`OWN-16`](../../CONTRIBUTING.md)).

**Gluing and surgery.** The existing finite-diagram colimit and pushout own
the quotient. A polygon-specific loop that merges vertex identifiers would
discard face arrows, piece maps and the universal cocone. Supply the face
inclusions and pairings as `Mor`, take the selected colimit in the underlying
category, then establish surface links and affine collar extension before
placing the quotient in the stronger category. Forgetfulness alone does not
prove preservation of that colimit ([`OWN-09`](../../CONTRIBUTING.md)).

**Triangulations and complexes.** A cone triangulation, polygon triangulation
and subdivision of a glued surface have the shared mathematical form
`(T, |T| -> X)` with indexed simplex inclusions. Their private algorithms
may differ. The cone owner already delegates ray triangulation to Sage's
`PointConfiguration`; applying that procedure directly to polygon vertices
would conflate rays with affine points. The common complex owner should
supply stars, links, face posets and subdivisions. A one-skeleton graph
cannot replace its two-cells, and a bare face poset cannot recover every
nonregular attaching map. The unfinished
[`simplicial-and-cw-foundations`](../../TODO.md) node owns this shared layer.

**Symmetries and quotients.** `RegularPolytopes.symmetry_group()` is specific
to the Schläfli/Coxeter construction. A general polytope's abstract
automorphism group acts on its actual face incidence object. Whether such an
automorphism lifts to an integral-affine or metric symmetry is a separate
map-lifting question with the selected placement as input. The AEGS
involutions are one `GObjects(C_2 × C_2,C)` action; separate callbacks in a
renderer, polygon gluer and quotient routine would yield unrelated actions.
The orbit-space projection is reused, while its smooth or affine structure
requires its own descent hypotheses. Faithfulness of the action is a further
property, not part of the statement that the involutions commute.

**Realization.** A planar unfolding consumes the edge-pairing arrows; an
embedding into `RR^3` consumes the completed topological or PL object and
an equivariant symmetry map. Mesh coordinates and rendering algorithms are
private display data. They do not redefine the abstract quotient, atlas,
singularities or group action ([`OWN-21`](../../CONTRIBUTING.md)).

The integrated path is a lattice polygon, then a chosen triangulation, a
surgery span, a finite gluing diagram, its topological colimit and cocone,
the surface-link condition, the induced regular-locus affine atlas, the
`IAS^2` sphere property, one group action, and an equivariant realization.
Each construction consumes the exact objects and maps produced before it.
The corresponding category, property, or functor is defined at its preamble
owner ([category presentation procedure](../../CONTRIBUTING.md)).

## External prior art and computational reuse

The reuse order for **every branch of the category graph** is: its existing
preamble owner, that owner's private engine, and only then another library for
a demonstrated missing computation. This table is an inventory of actual
interfaces, not a proposal for new implementations. A public result retains
its preamble object, arrows, and selected datum when an engine supplies the
answer.

| Category branch and basic construction | Preamble entry point | Prior art and exact reuse boundary |
| --- | --- | --- |
| Topological, real `C^k`, smooth, and complex manifolds; dimensions and charts | [`manifolds.py`](../../src/dzack_research/preamble/categories/manifolds.py): `TopologicalManifolds`, `DifferentiableManifolds`, `SmoothManifolds`, `ComplexManifolds`, chart families and transitions. | Already delegates to [SageManifolds charts and coordinate changes](https://doc.sagemath.org/html/en/reference/manifolds/sage/manifolds/differentiable/chart.html). Extend the exact manifold and selected atlas; do not build a second chart store. Check the preamble's current differentiability and dimension refinements before adding any `C^k` or `.PureDimension(n)` edge. Sage's [manifold catalog](https://doc.sagemath.org/html/en/reference/manifolds/sage/manifolds/catalog.html) supplies standard `RR^n`, spheres, and projective spaces privately. |
| Open complements, tangent data, affine connections | [`TopologicalSpaces`](../../src/dzack_research/preamble/categories/topological_spaces.py) and the manifold owner supply opens and restrictions. | [SageManifolds](https://doc.sagemath.org/html/en/reference/manifolds/index.html) has tangent bundles, vector fields, [vector bundles](https://doc.sagemath.org/html/en/reference/manifolds/sage/manifolds/differentiable/vector_bundle.html), [affine connections](https://doc.sagemath.org/html/en/reference/manifolds/sage/manifolds/differentiable/affine_connection.html), and [bundle connections](https://doc.sagemath.org/html/en/reference/manifolds/sage/manifolds/differentiable/bundle_connection.html). Use these for derivative and parallel-transport computations under the preamble manifold. The integral tangent lattice is a selected rank-`n` local subsystem of `TM|_(B\Sigma)`; a real connection alone does not select it. |
| Sheaves, local systems, and monodromy | [`Sheaves`](../../src/dzack_research/preamble/categories/abstract_categories/presheaves.py) is the generic descent category; [`SheafObjects`](../../src/dzack_research/preamble/categories/schemes/ringed_spaces.py) and `ModuleSheaves` specialize it. [`monodromy.py`](../../src/dzack_research/preamble/categories/schemes/monodromy.py) already represents a local system by a `GroupActionFunctor` from a pointed fundamental group and exposes its monodromy representation. | Generalize the **existing functor construction** to the chosen regular-locus space and `ZZ`-module or lattice fiber; do not copy the Legendre family's matrices. [Sage simplicial complexes](https://doc.sagemath.org/html/en/reference/topology/sage/topology/simplicial_complex.html) calculate an edge-path fundamental group using GAP. [CellularSheaves.jl](https://algebraicjulia.github.io/CellularSheaves.jl/dev/) and [pysheaf](https://github.com/kb1dds/pysheaf) are possible private engines for cellular sheaf computations, after checking their stalk/ring and dimension contracts. They do not replace the preamble's general sheaf or action-functor owner. |
| Affine spaces and lattices; Euclidean, spherical, hyperbolic ambients | [`AffineSpaces`](../../src/dzack_research/preamble/categories/schemes/schemes.py), [`Lattices`](../../src/dzack_research/preamble/categories/lattices.py), `FormModules`, and [`HyperbolicSpaces`](../../src/dzack_research/preamble/categories/hyperbolic_geometry.py). | Reuse existing affine coordinate, lattice, form, and hyperbolic realizations. Sage's [Euclidean space and embedded sphere](https://doc.sagemath.org/html/en/reference/manifolds/sage/manifolds/differentiable/examples/sphere.html) and [hyperbolic-plane models](https://doc.sagemath.org/html/en/reference/hyperbolic_geometry/index.html) provide private realizations. [CGAL spherical arrangements](https://doc.cgal.org/latest/Arrangement_on_surface_2/index.html) handle great-circle arcs and faces; [spherical triangulations](https://doc.cgal.org/6.2/Triangulation_on_sphere_2/index.html) handle geodesic triangle meshes. These are concrete candidates for spherical geometry after the preamble ambient-space and polytope definitions fix the input and output. A lattice and a metric are separate selected data. |
| Convex, lattice, and abstract polytopes; face posets and automorphisms | [`ConvexPolytopes(L)` and `RegularPolytopes`](../../src/dzack_research/preamble/categories/schemes/polytopes.py), plus preamble posets, graphs, and `GObjects`. | Sage [`Polyhedron`](https://doc.sagemath.org/html/en/thematic_tutorials/geometry/polyhedra_quickref.html) already computes vertices, faces, the face lattice, and [combinatorial and restricted affine automorphism groups](https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/polyhedron/base4.html). The default combinatorial group preserves full vertex-facet incidence; its vertex-graph option need not agree. Raise each computed face with its inclusion and each group element with its action. For a lattice-preserving subgroup, check the actual affine matrices against the selected lattice. [`Normaliz`](https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/polyhedron/backend_normaliz.html) is already a Sage polyhedron backend for exact lattice computations. |
| Chosen triangulations and integral refinements | [`RationalPolyhedralCones`](../../src/dzack_research/preamble/categories/polyhedral_cones.py) already uses Sage `PointConfiguration` for ray triangulation; polygon triangulation belongs over the polytope owner, with its face maps. | Sage [`PointConfiguration`](https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/triangulation/point_configuration.html) and `Polyhedron.triangulate()` compute triangulations; TOPCOM can be used through these interfaces. Select all needed lattice points, then check integrality and normalized simplex volumes. A regular triangulation need not be unimodular. [Macaulay2 `Polyhedra`](https://www.macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Polyhedra/html/index.html) and [polymake through OSCAR](https://oscar-system.github.io/Polymake.jl/) are alternate engines only for a verified gap. |
| Complexes, face gluings, quotient topology, stars and links | [`Cat`](../../src/dzack_research/preamble/categories/abstract_categories/cat.py) owns finite-diagram colimits and pushouts; topological-space quotients and the pending common cell-complex category supply their typed domains. | Sage [`PolyhedralComplex`](https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/polyhedral_complex.html) handles cells embedded in one affine ambient; [`DeltaComplex`](https://doc.sagemath.org/html/en/reference/topology/sage/topology/delta_complex.html) stores abstract face identifications and their realization; [`SimplicialComplex`](https://doc.sagemath.org/html/en/reference/topology/sage/topology/simplicial_complex.html) supplies simplicial invariants; [simplicial sets](https://doc.sagemath.org/html/en/reference/topology/sage/topology/simplicial_set.html) provide finite pushouts and pullbacks with their structure maps. [OSCAR simplicial complexes](https://docs.oscar-system.org/dev/Combinatorics/simplicialcomplexes/) provide `star_subcomplex`, `link_subcomplex`, `deletion`, `connected_sum`, `automorphism_group`, and `fundamental_group`; its `is_sphere` is heuristic and may return no decision. [polymake topaz](https://polymake.org/release_docs/2.12/topaz.html), [GAP simpcomp](https://github.com/simpcomp-team/simpcomp), and [Regina](https://regina-normal.github.io/7.1/engine-docs/classregina_1_1Triangulation_3_012_01_4.html) are additional complex engines. An embedded polyhedral complex is not a substitute for an abstract quotient. Retain the gluing diagram and selected cocone. |
| Polygonal edge pairings, surgery, and displays | The polytope, triangulation, subobject, pushout, manifold, and complex owners above; [`GObjects`](../../src/dzack_research/preamble/categories/group/g_objects.py) for compatible actions. | [`sage-flatsurf`](https://flatsurf.github.io/sage-flatsurf/examples/tour) already supports polygon edge pairings and planar layouts. Its similarity and translation surfaces cover useful special cases, and a [global `GL(2,RR)` action](https://flatsurf.github.io/sage-flatsurf/geometry/morphism.html) does not itself supply chartwise integral shear. A basis-triangle or corner removal selects the affected faces and boundary maps, forms the stated complement or replacement, then uses the category-owned pushout. Drawing consumes the completed quotient and labels; it does not define them. |
| Dual complexes, actions, and embeddings | A dual-complex construction must consume the degeneration's exact incidence maps; [`GObjects`](../../src/dzack_research/preamble/categories/group/g_objects.py) owns actions, stabilizers, and orbit projections; `Mor` owns embeddings. | Reuse the common complex face-poset and dual-incidence data, not an unrelated graph. Sage's [topology](https://doc.sagemath.org/html/en/reference/topology/index.html) and [graphics](https://doc.sagemath.org/html/en/reference/plotting/index.html), or polymake's complex visualization, can compute and display a placement. [CGAL surface-mesh parameterization](https://doc.cgal.org/latest/Surface_mesh_parameterization/index.html) supplies planar unfolding algorithms with stated injectivity conditions; [OSCAR simplicial complexes](https://docs.oscar-system.org/dev/Combinatorics/simplicialcomplexes/) offer a sphere test. [GAP/GRAPE](https://docs.gap-system.org/pkg/grape/doc/manual.pdf) is an optional private automorphism engine if Sage's face-incidence route does not suffice. An embedding in `RR^3` is a selected map of the completed object; a planar net records edge identifications. |

### Determining the two residues after preamble reuse

The table above lists sources. The following ledger records **what is
already owned**, **what the first residue can take from existing code**, and
**what remains after those checks**. “Construct” means compose existing
mathematics with its defining maps, or supply a missing category; it
does not mean write a competing computational engine. A candidate in the
middle column is not an adopted dependency until its precise contract is
checked against a concrete missing operation.

| Branch | Already in the preamble | First residue: existing code to reuse | Second residue: required new work |
| --- | --- | --- | --- |
| Manifold filtration and standard spaces | Topological, differentiable, smooth and complex manifold owners; atlases and transitions. `DifferentiableManifolds(d,name,k)` already records finite positive `k`; `SmoothManifolds` is a subcategory of it. | SageManifolds has differentiability degrees, chart restrictions, standard `RR^n` and spheres. | Present the requested *fixed-degree and fixed-dimension category fibers* and their forgetful functors; establish a constructor that equips the same existing manifold rather than allocating another when the current direct constructor cannot. No new differentiability computation is needed. |
| Integral-affine manifolds | Underlying manifold, chart arrows, affine spaces, lattices, and form/module morphisms. | SageManifolds differentiates transition maps and computes tangent data. | Specify the `GL(n,ZZ) ⋉ RR^n` transition predicate and cocycle on the **selected atlas**; connect its derivative to a rank-`n` lattice subsystem and define structure-preserving morphisms. The computation of derivatives is reused. |
| Singular integral-affine spaces and `IAS^2` | Topological quotients, open subobjects, smooth spheres, and the manifold and atlas operations above. | Sage finite complexes and OSCAR links, fundamental groups and sphere recognition compute related finite topology; OSCAR's `is_sphere` is a heuristic with an indeterminate result. | Represent the triple `(B, Sigma ↪ B, integral-affine atlas on B\Sigma)` with its exact complement inclusion and structured morphisms. For the two-dimensional sphere predicate, establish the surface links and sphere topology from the selected finite decomposition; attach the specified singular local models and their monodromy. No new sphere or link algorithm follows from this contract. |
| Sheaves, local systems, marked loci and monodromy | Generic sheaf descent, subobjects, group-action functors, and a concrete Legendre local system. `TopologicalSpaces._fundamental_group_at` is a protected contract whose general case is not computed. | Sage/GAP computes edge-path groups of finite simplicial complexes; SageManifolds computes bundle and connection data. Cellular-sheaf packages are candidates only for extra sheaf computations. | Raise the edge-path result to the preamble's pointed fundamental-group object for a selected complex. The existing action-functor pattern covers a connected space after choosing a base point and fiber; a base-point-free or disconnected local system uses the fundamental **groupoid** and a functor from it, or equivalent sheaf descent. Identify its transport with atlas derivatives. A marked finite subset is an existing subobject. A loop's monodromy is functor evaluation. |
| Ambient geometries and polytopes | Affine spaces, lattices, formed modules, convex/lattice polytopes, hyperbolic spaces and polyhedra; rational polyhedral cones already have a preamble owner. | Sage Polyhedron/Normaliz compute rational and integral polytope data; Sage has Euclidean and hyperbolic models; CGAL computes spherical great-circle arrangements and geodesic triangulations. For a spherical convex polytope contained in an open hemisphere, the standard [cone-sphere correspondence](https://arxiv.org/abs/2007.03011) identifies it with `C ∩ S^n` for a pointed polyhedral cone `C`, whose [face lattice Sage computes](https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/cone.html). | Place each polytope in its selected ambient space by an inclusion and retain inclusions of faces. Reuse the cone owner for hemispherical spherical polytopes and CGAL for spherical-surface arrangements. A definition allowing antipodal pairs or nonhemispherical cells needs its own geometric contract before its computational residue can be classified. |
| Abstract incidence, automorphisms and actions | Posets, graphs, groups and `GObjects`; regular-polytope symmetry for its existing special case. | Sage's face lattice and combinatorial/affine automorphism methods; GAP graph algorithms if needed. | Raise the complete face-incidence object and its action as preamble objects and arrows. Test which abstract automorphisms preserve the selected lattice, metric, atlas, or gluing data by the corresponding morphism conditions. |
| Triangulations and complexes | Cone ray-triangulation and generic colimits; the common cell-complex foundation is pending. | Sage `PointConfiguration`, `Polyhedron.triangulate`, `PolyhedralComplex`, `DeltaComplex`, and `SimplicialComplex`; OSCAR supplies star, link, deletion, connected sum, automorphisms and fundamental groups; polymake/Regina are capability-specific alternatives. | Define a chosen triangulation over its original polytope or complex with simplex inclusions and realization map; make integral and unimodular predicates relative to its selected lattice. Present the common complex category and its typed face maps. No triangulation or elementary complex-operation engine is required here. |
| Simplicial sets and Kan condition | The category graph requires a home for abstract simplicial constructions; the proposed cell-complex owner remains separate. | Sage simplicial sets have face maps, morphisms, finite pushouts and pullbacks. | Reuse the preamble's simplicial-set and groupoid constructions for any actual simplicial-set result. The Kan horn-filling condition is a property of a simplicial set, not a substitute for a cell-complex or surface category; no IAS operation in this plan requires a new Kan algorithm. |
| Gluing, surgery and dual complexes | Pushout/colimit, subobjects, topological quotient, manifold owner and `GObjects`. | Sage `DeltaComplex` handles combinatorial face identifications and simplicial sets compute finite pushouts; OSCAR has face deletion and connected sum; sage-flatsurf supplies polygonal translation/similarity gluings and layouts. | Build the typed finite gluing diagram and retain its cocone. Express each surgery as a region inclusion, replacement, boundary isomorphism and pushout; verify the resulting local manifold and affine-chart conditions. Define the dual-complex functor from the source degeneration's incidence maps. |
| Embeddings and visualization | Morphisms, ambient spaces, group actions and completed quotient objects. | Sage graphics, sage-flatsurf layouts, polymake visualizations, and CGAL surface-mesh planar parameterization. | Store an actual embedding or planar unfolding with its source, target and edge labels; impose equivariance only when a selected action is supplied. Placement algorithms remain private. |

For the capabilities actually checked above, the identified second residue is
**structural**: typed
category refinements, face and chart arrows, lattice-preserving atlas
conditions, selected triangulation and gluing diagrams, and the functors
that connect these existing objects. Each item has an input and result in
the category graph above. An unverified
external capability, such as spherical cells outside the stated
hemispherical model, stays open rather than being counted as code that
must be invented.

The mathematical composition is already described by
[Gross--Siebert's affine manifolds with polyhedral decompositions](https://arxiv.org/abs/math/0309070)
and by [AEGS] below. Its implementation should assemble the listed
building blocks, preserving their actual maps. In particular, monodromy is
the image of a loop under the local-system functor, and a polytope surgery is
a diagram of existing subobjects and face maps whose pushout has a selected
cocone. Neither calls for a new polytope, fundamental-group, sheaf, chart,
or quotient engine.

## Dependency-ordered implementation phases

Each phase has one mathematical output and an exit condition at the owner of
that output. A phase may use a private engine only after its input category,
result category, and retained arrows are fixed. The existing
[`simplicial-and-cw-foundations`](../../TODO.md) node owns the common complex
foundation and depends on `pullbacks-in-every-category`; these phases consume
that node rather than create a second complex hierarchy. The existing
[`the-real-line-is-a-smooth-manifold`](../../TODO.md) and
[`optional-manifold-tangent-bundles`](../../TODO.md) nodes likewise own those
foundational repairs. Phase labels describe dependency order, not separate
repositories or acceptance by an AEGS consumer.

### P1. Category subtree and complete typing

Present the graph above in the preamble, starting with
the existing nodes and their actual category constructions. Stub
only the mathematically missing nodes and methods. This phase defines the
public language; it does not select a data class, algorithm, renderer, or
special-case AEGS constructor.

The P1 ownership tree keeps existing owners in place. The three new
surfaces below are **category stubs**, not replacement algorithms; their
final filenames follow the mathematical owner in the preamble and
the existing complex TODO node.

```text
src/dzack_research/preamble/categories/
  abstract_categories/cat.py, presheaves.py  existing diagrams, colimits, sheaves
  topological_spaces.py                      existing spaces, opens, quotients
  manifolds.py                               existing C^k, smooth, complex atlases
  schemes/schemes.py, polytopes.py           existing affine spaces, polytopes
  lattices.py, polyhedral_cones.py           existing lattices, cones
  hyperbolic_geometry.py                    existing hyperbolic owners
  group/g_objects.py                        existing actions and quotients
  [common complexes owner]                  P1 stub at the existing TODO owner
  [integral-affine owner]                   P1 atlas and singular-space stubs
  [chosen-triangulation owner]              P1 construction over its target
```

The brackets are unresolved *paths*, not unresolved mathematical owners.
P1 closes them by following the category definitions and the
current modules. A new file cannot provide another route to an operation
already owned by one of the listed modules.

| Subtree | Required P1 surface |
| --- | --- |
| Manifolds | Topological, fixed `C^k`, smooth, complex, boundary/corner and pure-dimension categories; `RR^n`/`CC^m` placements; chart and atlas objects; points as elements; map `Mor`; same-object weakening and complex realification functors. |
| Affine geometry | Affine spaces over a selected vector space, lattices with embeddings, integral-affine manifolds and singular integral-affine spaces; atlas and singular-locus data; affine-map `Mor`; forgetful functors to smooth manifolds and spaces. |
| Polytopes | Abstract face-incidence objects; placed affine, Euclidean, spherical and hyperbolic polytopes; lattice and polygon refinements; face inclusions; corresponding map, isomorphism and automorphism categories. |
| Complexes | Existing finite diagram, simplicial, `Delta`, simplicial-set and CW constructions; polytopal complexes and realizations; cell/face morphisms, subcomplexes and realization functors. Consume the existing complex TODO owner. |
| Constructions over objects | Chosen triangulations over their exact targets; gluing diagrams and cocones; subobject surgery spans; dual-complex construction from its degeneration; actions through `GObjects(G,C)`; embeddings as `Mor` with exact endpoints. |

The source-level P1 register below records the inspected owner and missing
typing for each branch of the displayed graph. An existing preamble
class is partial presentation of the required category and its arrows.
The missing paths remain open in
[`integral-affine-polyhedral-p1`](../../TODO.md).

| Graph branch and arrow | Inspected owner or request | P1 remainder |
| --- | --- | --- |
| Topological, fixed `C^k`, smooth, boundary/corner and dimension strata; weakening and forgetful maps | [`manifolds.py`](../../src/dzack_research/preamble/categories/manifolds.py) presents topological, differentiable and smooth classes. | Fixed-degree and fixed-dimension categories, boundary/corner map classes and all functor images need typed owners. |
| Complex manifolds, `CC^m`, and realification to real dimension `2m` | `ComplexManifolds.affine_space` constructs a complex charted object; its declared smooth supercategory edge is the [recorded defect](../../COMPLAINTS.md#complex-manifold-realification-is-declared-as-a-supercategory-edge). | Replace that edge with an object-and-morphism realification functor. |
| `RR^n` as a smooth manifold | [`the-real-line-is-a-smooth-manifold`](../../TODO.md) records the missing `RR` placement. | Construct the same `RR` object with its identity chart; then the finite-product route must retain the exact `RR^n` object. |
| Vector and affine spaces, lattice embedding and integral-affine group | [`AffineSpaces`](../../src/dzack_research/preamble/categories/schemes/schemes.py), [`Lattices`](../../src/dzack_research/preamble/categories/lattices.py), and group constructions are partial presentations. | Fix the model vector space, selected affine lattice and action on charts as typed data and maps. |
| Integral-affine atlas, orientation, boundary/corners, strict lattice-point atlas and forgetful functors | No preamble atlas category appears in the inspected category paths. | Define its objects, local affine `Mor`, refinements, and functor images. |
| Singular locus, regular complement, `IAS^2` and higher-dimensional singular models | [`TopologicalSpaces`](../../src/dzack_research/preamble/categories/topological_spaces.py) has open subobjects. | Retain `Σ ↪ B`, the exact complement and its atlas; state singular map classes and dimension-specific local models. |
| Finite graded posets and abstract polytopes | [`RegularPolytopes`](../../src/dzack_research/preamble/categories/schemes/polytopes.py) is a partial regular case; its order placement is already a [complaint](../../COMPLAINTS.md#coxeter-diagrams-answer-subdiagram-orders-and-drawings-as-sage-objects). | General abstract face-poset objects, order and automorphism `Mor` remain to be typed. |
| Placed affine/lattice/Euclidean/spherical/hyperbolic polytopes and face-poset functors | [`ConvexPolytopes`](../../src/dzack_research/preamble/categories/schemes/polytopes.py) and [`HyperbolicPolyhedra`](../../src/dzack_research/preamble/categories/hyperbolic_geometry.py) are partial realizations. | Preserve each ambient inclusion and every face-to-polytope arrow; define remaining ambient geometries and their map conditions. |
| Cell, polytopal, simplicial, `Delta` and simplicial-set branches; realizations and `Kan` | [`simplicial-and-cw-foundations`](../../TODO.md) owns the preamble work. | Supply the common categories, face maps, realization functors, subcomplex maps and property refinements. |
| Chosen triangulation over `K`, integrality and unimodularity | Existing cone triangulation is an algorithm on rays, not a selected triangulation over a placed target. | Retain `T`, its simplex inclusions and `|T| → |K|` with the selected lattice comparison. |
| Face diagrams, colimit cocones and structured surgeries | [`Cat`](../../src/dzack_research/preamble/categories/abstract_categories/cat.py) presents generic diagrams, colimits and pushouts. | Construct the typed complex diagram, quotient cocone, boundary span and affine collar comparisons. |
| Degeneration to dual complex | The dual-complex construction needs the incidence data of its source degeneration. | Define the source-to-complex correspondence and its induced incidence map. |
| Actions, `Mor`, embeddings and displays | [`GObjects`](../../src/dzack_research/preamble/categories/group/g_objects.py) and generic `Mor` constructions exist. | Specialize them only after each target category and map class exists; retain action and embedding endpoints. |

For **each** node, record its parameter object, defining objects and
elements, `Mor` and identity/composition, `Hom(X,Y)`, `End(X)` and `Aut(X)`
through the existing category constructions, true supercategory inclusions,
non-inclusion functors on objects **and** morphisms, constructor chain, and
forgetful image. Do not manufacture a separate `Hom`/`Aut` class when `Cat`
already constructs it. A property such as `Sphere`, `Integral`, `Kan`, or
`PureDimension(2)` is a refinement of its owner under its stated
hypotheses. The P1 coverage register is the complete graph in this document:
every node and arrow must resolve to an existing preamble owner or a
new declaration at the mathematical owner before P1 closes. Sample chains include
`RR -> SmoothRealManifolds(1) -> TopologicalSpaces`,
`P -> faces(P) -> face_poset(P) -> Aut(face_poset(P))`, and
`D -> colimit(D) -> underlying_space(colimit(D))`. Each chain must preserve
the same source object and its actual arrows. A stub may raise for a missing
computation; it may not fabricate an object, drop a map, or use an engine
object as a public endpoint.

### P2. Defining data and canonical constructors

At each P1 owner, specify the minimum **mathematical** datum from which an
object is determined, then make its constructor retain that datum and its
source maps. A smooth manifold is the selected compatible atlas on the
same topological manifold; an integral-affine manifold selects affine
transitions on that smooth manifold; a singular one selects
`Sigma -> B` and an atlas on the exact complement. A placed polytope keeps
its ambient inclusion; a chosen triangulation keeps simplex inclusions and
`|T| -> |P|`; a glued complex keeps the diagram and cocone. Morphism
constructors check source, target and preservation of the selected data.

The public object is a preamble parent or element in its mathematical
category. A private `dataclass`, Pydantic model, or engine record is chosen
only when concrete repeated internal use justifies it; none is the public
definition. The exit condition is constructor chaining: direct data,
restriction, functor image, and raised engine result establish the **same**
defining datum and category placement. A diagram whose quotient has no
cocone, or a polytope face without its inclusion, fails P2 even if its
coordinates are correct.

### P3. Finish the preamble reuse path

Wire each P2 construction to the existing preamble operation before adding
an external dependency. This includes manifold charts and transitions,
open-subobject restrictions, `AffineSpaces`, `Lattices`, `Sheaves`, the
Legendre local-system functor pattern, `ConvexPolytopes`,
`RationalPolyhedralCones`, topological quotients, `Cat` colimits and
pushouts, `GObjects`, and the hyperbolic construction. The named TODO
foundations above supply the real-line placement, owned tangent bundle,
and common complex owners when their dependencies are met. P3 also exposes
the preamble operations' **structural output**: face inclusions, pointed
group objects, selected cocones, and functor images, rather than returning
only coordinates or invariants. Its exit condition is that every reusable
preamble operation in the prior-art table has a single typed call path and
no parallel construction in this subtree.

### P4. Port available computations through private interfaces

Prioritize the first residue before writing any new computational algorithm.
SageManifolds supplies chart differentiation, tangent and connection
calculations. Sage `Polyhedron`, its Normaliz backend, `PointConfiguration`,
finite complexes and simplicial sets supply polyhedral, triangulation and
quotient computations. For rational cone data, the existing cone owner
supplies hemispherical spherical faces by `C ∩ S^n`. Use CGAL's spherical arrangement or mesh
parameterization interface, OSCAR/polymake complex operations, GAP, Regina,
or sage-flatsurf only for the precise operation their inspected contract
adds. An adapter lowers a P2 datum, invokes the maintained implementation,
and raises the result **at its P1 owner**, with all face, chart, quotient or
action arrows. It never exports a foreign parent or makes the library's
class graph the category graph. Its exit condition is a source-linked
operation-to-engine map and a typed raise path for every adopted engine.

### P5. Standard derived operations and mathematical assertions

Expose category-owned faces, incidence posets, abstract and placed
automorphisms, stars, links, subdivisions, integral points, chosen
triangulations, local-system transport, colimits, and embeddings by
composing P3 and P4. At each owner, verify true assertions with an
independent source or oracle: a face inclusion preserves incidence;
simplex images cover the target and intersect along common faces; a
unimodular lattice triangle has normalized area one; `link_K(v)` is the
specified subcomplex; the face-poset group acts by rank-preserving
automorphisms; a finite quotient retains its universal cocone. Use Hatcher,
Lee, Ziegler, AEGS, the cited software documentation, or an independent
exact engine according to the assertion. The engine's own tests and claims
do not establish public mathematical correctness. P5 closes when these
standard operations return the full stated objects and maps, not just a
number, picture or successful backend call.

### P6. Construct the determined second residue

Only after P1--P5, implement the structural operations for which the
first-residue survey found no existing preamble presentation: the
integral-affine transition predicate and atlas on the exact manifold;
its integral tangent local system and comparison to derivatives; the
singular-locus/complement object; affine collar extension after a
polytope-diagram quotient; selected surgery spans and their structured
pushouts; the dual-complex map from degeneration incidence; and lifting
an abstract symmetry to a selected integral-affine action when its
hypotheses hold. `IAS^2` is then the sphere refinement of that singular
object. Each operation has the defining inputs and `Mor` endpoints in the
API section above. Its assertions are the atlas cocycle, lattice
preservation, correct local links, the stated monodromy of supplied loops,
and the universal property or comparison map of each quotient. A new
computational algorithm enters P6 only after an exact P4 capability gap
and its mathematical route are recorded; an unresolved external
capability is not silently promoted to an invention task.

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
* J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Chapters 1–2,
  for smooth atlases, smooth maps, and manifolds with boundary.
* A. Hatcher, [*Algebraic Topology*](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf),
  §2.1, for `Delta`-complexes and quotient cell structures.
* G. M. Ziegler, *Lectures on Polytopes*, Chapters 1–2, for convex polytopes
  and face lattices.
