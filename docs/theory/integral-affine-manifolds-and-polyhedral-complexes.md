# Integral-affine manifolds and polyhedral constructions

This document specifies the mathematical objects and maps needed to construct the
integral-affine spheres of [AEGS, §4]. It is a category design, not a claim that
the stated constructions have been implemented. Semantic declarations belong to
`lean-categories`; the research preamble presents them and may use maintained
geometry engines privately. The relevant existing presentations are
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
nodes is a preamble declaration until `lean-categories` formalizes its objects,
morphisms, data, and inclusions. This follows [`CAT-15`–`CAT-20` and
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
the structure in [AEGS, Introduction and §4] and [Foundations, Definition
62.6].

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
complex alone does not determine it [Foundations, Definition 62.6].

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

The following inventory is based on the inspected preamble source. It does
not assert that a proposed category has been formalized in `lean-categories`
or implemented in the preamble. A new `super_categories()` edge is admitted
only for an inclusion with the same parameters that `lean-categories` states;
a change of structure, ambient space, or morphisms uses a functor
([`CAT-15`–`CAT-16`](../../CONTRIBUTING.md)).

| Existing owner | Supplied mathematics | Wiring into the proposed constructions | Exact gap |
| --- | --- | --- | --- |
| [`TopologicalSpaces`](../../src/dzack_research/preamble/categories/topological_spaces.py) | Continuous `Mor`, open subsets, coproducts, coequalizers, and final-topology quotients. | Build the polygon gluing as a finite diagram of underlying spaces. Retain its quotient and every piece-to-quotient map as the underlying object of a singular-affine space. | A topological quotient still needs surface links and affine collar charts. General openness for predicate subsets is limited by the [finite-atlas complaint](../../COMPLAINTS.md). |
| [`TopologicalManifolds`, `DifferentiableManifolds`, `SmoothManifolds`, `ComplexManifolds`](../../src/dzack_research/preamble/categories/manifolds.py) | Dimensions, chart families, transitions, a stereographic smooth sphere, and a complex-to-smooth route. | Add the integral-affine atlas to the **same** smooth manifold; restrict it to the exact open complement of the singular set. Use the existing realification route for complex manifolds. | Direct constructors currently allocate a manifold from a dimension and name; they do not equip a supplied manifold. [`RR` manifold placement](../../TODO.md) remains unfinished. The transition constructor trusts supplied inverses, so the affine layer needs its own transition and cocycle conditions. |
| [`Cat`](../../src/dzack_research/preamble/categories/abstract_categories/cat.py) | `Mor`, slices, subobjects, finite-diagram colimits, and `pushout_construction` with a selected cocone. | Treat each face inclusion as a subobject arrow, each edge pairing as a diagram arrow, and each surgery as a pushout. Retain the cocone and universal factor map. | The applicable complex and affine morphism categories must be supplied. A generic colimit does not establish surface or affine structure. The [pushout complaint](../../COMPLAINTS.md) records an object-only route that loses the selected cocone. |
| [`ConvexPolytopes(L)`](../../src/dzack_research/preamble/categories/schemes/polytopes.py) | Rational affine polytopes from vertices or halfspaces; owned vertices, facets, integral points and normal fans; `Integral` and `Polygon` refinements. | AEGS lattice polygons enter `ConvexPolytopes(L).Integral().Polygon()` when they satisfy its coordinate contract. Their faces feed the common complex and triangulation constructions. | `facets()` returns face polytopes without their inclusions into the original polytope. No selected polygon triangulation or polygon-gluing construction is supplied by this owner. |
| [`RegularPolytopes`](../../src/dzack_research/preamble/categories/schemes/polytopes.py), [`PartiallyOrderedSets`](../../src/dzack_research/preamble/categories/sets/set_categories.py), and [`Graphs`](../../src/dzack_research/preamble/categories/graph_categories.py) | A Schläfli/Coxeter symmetry group for regular examples, an order category, and graphs. | Construct a general polytope's face poset with its order, then its abstract automorphism group. The one-skeleton is a graph image of the retained complex. | The regular group is not a general automorphism algorithm. The current regular-polytope order placement and monotone-map surface are unresolved in [`TODO.md`](../../TODO.md). A graph alone loses two-cells and attaching maps. |
| [`RationalPolyhedralCones(L)`](../../src/dzack_research/preamble/categories/polyhedral_cones.py) | Ray triangulation, simplicial subcones, ray-span saturation indices, and private Sage `PointConfiguration` computation. | Reuse its triangulation for cone-valued operations. Relate a cone and a polygon only through an actual section, homogenization, or projectivization map. Both feed the same chosen-triangulation concept when it is formalized. | `simplicial_subcone_inclusion()` is only a set map because cone `Mor` is missing ([`COMPLAINTS.md`](../../COMPLAINTS.md)). A cone-ray triangulation is not a polygon triangulation. |
| [`HyperbolicSpaces` and `HyperbolicPolyhedra`](../../src/dzack_research/preamble/categories/hyperbolic_geometry.py) | A selected hyperbolic space, projectivized rational cone, ordinary and ideal vertices, and wall data. | Keep this space and cone as the source for the supported hyperbolic-polytope specialization. Map its face incidence to the common abstract complex owner. | It does not supply every hyperbolic polytope, a spherical polytope, or a Euclidean ambient space. The proposed general categories require their own formal definitions. |
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
The corresponding formal category, property or functor must first be found
in `lean-categories`; missing mathematics is requested there, rather than
defined a second time in the preamble ([category presentation
procedure](../../CONTRIBUTING.md)).

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
