# The fundamental chamber as an intersection of root half-spaces, and its containment in the hyperbolic domain

Status: corrected mathematics, landed 2026-08-20 beside the owned surface's stated gap. The owned `fundamental_chamber` and `weyl_group` on `HyperbolicLattices` (`src/dzack_research/preamble/categories/modules/framed/formed/integrallattice/hyperbolic_lattices.sage`) are declared `abstract_method`s — the construction below is what they are contracted to produce, recorded here until the Vinberg surface implements them. Root enumeration itself is owned (`vinberg_algorithm`, `allcock_edgewalk` on the same category), and reflectivity is now decided by the edgewalk engine (`is_reflective`).

Sources: the working cone construction in `archives/notebooks/Coble Lattice Invariants.ipynb` (the `Polyhedron`/`Cone` cells over the 22-root $(18,2,0)$-plus-two configuration; export cells 130–148), and the prototype `computations/scripts/components/coxeter-vinberg/Vinberg_L_2_1.py`, which the corpora-audit registry marks WRONG — its recorded defects are restated below, plus two further structural ones found at this landing.

## The chamber

Let $L$ be a hyperbolic lattice with Gram matrix $G$ — in this repo's convention signature $(1,n)$, timelike meaning positive square — and let $R = \{r_1, \ldots, r_k\} \subset L$ be a set of roots (the simple roots a Vinberg or edgewalk enumeration returns). The fundamental chamber they determine is the polyhedral cone

$$C \;=\; \{\, x \in L \otimes \mathbb{R} \;:\; b(r_i, x) \ge 0 \ \text{for all } i \,\}.$$

The linear functional of $b(r, \cdot)$ in coordinates is the row $r^{\mathsf{T}} G$, **not** the coordinate row $r$ itself. Sage encoding, as the Coble notebook writes it correctly:

```python
ineqs = [(0,) + tuple(r * G) for r in roots]   # b(r, x) >= 0
C = Polyhedron(ieqs=ineqs, backend='normaliz')
```

From this object the notebook extracts exactly what the registry row names: the extremal `rays()`, the `facets()`, primitive integral ray generators (clear denominators by the lcm, divide by the gcd), the Hilbert basis and `integral_points_generators()` through the Normaliz backend, and random-element containment assertions (`assert all(b(r, x) >= 0 ...)` over sampled `x`).

## Containment in the hyperbolic domain

$C$ is a cone with apex the origin (every defining hyperplane passes through $0$). Its intersection with hyperbolic space is therefore controlled by its **rays and lineality**, never by its vertex list: a pointed cone's one vertex is the origin, which lies on the light cone boundary and says nothing.

With the hyperbolic domain the chosen sheet of $\{q(x) > 0\}$ (signature $(1,n)$; for the $(n,1)$ transport read $q < 0$), the correct test on a chamber cone is:

- **every extremal ray generator $v$ has $q(v) \ge 0$** — timelike ($q > 0$, an ordinary vertex of the hyperbolic polyhedron) or isotropic ($q = 0$, an ideal vertex);
- **all ray generators lie in one (the future) half**, i.e. their pairings against one fixed timelike vector share a sign;
- **the lineality space is trivial** — a cone containing a line is never contained in the closed future cone.

Under that test the hyperbolic polyhedron $C \cap \mathbb{H}^n$ has finite volume, and it is **compact exactly when no ray is isotropic** — the ideal vertices are the isotropic rays. This is the criterion the recorded runs use: the notebook's edgewalk driver reports `is_cocompact = max(vertex norms) < 0` in the $(n,1)$ convention, and the VinAl runs in `notes/computations/sterk-root-count-discrepancy.md` report their isotropic rays as "ideal vertices".

## The prototype's recorded errors (`Vinberg_L_2_1.py`)

The registry's error record, restated at this landing site; the only enrichment content of the file is the *idea* of the two constructions above, and both of its realizations are defective.

1. **The chamber pairs with the wrong bilinear form.** `chamber_polyhedron` writes the inequality rows as `[0] + [-x for x in r]` — the Euclidean functional $-r \cdot x \ge 0$, omitting the Gram matrix. For $Q = \mathrm{diag}(-1,1,1)$ these are not the root half-spaces $b(r,x) \ge 0$ (and the sign faces the chamber away from the roots). The corrected encoding is the `r * G` row above.
2. **The containment test is constant-false on pointed cones and blind on unpointed ones.** `chamber_fully_in_hyperbolic` iterates `chamber.vertices()` and demands each vertex be strictly timelike and forward — but a pointed cone's only vertex is the origin, which always fails, so the test can never pass; and a non-pointed chamber's lineality lines are not examined at all. The corrected test is the ray/lineality test above.
3. **The function named `vinberg_algorithm` is not Vinberg's algorithm.** It closes a root set under reflections in the roots it already holds, which enumerates (part of) the Weyl-group *orbit* of the seed — the root system, not a simple system. Vinberg's algorithm enumerates candidate roots in order of increasing distance from a control point and admits a root only when it pairs non-acutely with every accepted root; the chamber shrinks as roots are added rather than the root set growing. The written procedure can neither terminate correctly nor produce fundamental roots when the reflection group is infinite. The owned enumeration is `vinberg_algorithm` (vendored `vinal`) and `allcock_edgewalk` (polyhedral_common) on `HyperbolicLattices`.
4. **Floating tolerances decide exact questions.** Squares, coincidence of integer vectors, and isotropy are compared against `1e-12`/`1e-14` where the Lorentzian form on integer vectors is exact integer arithmetic.
5. **Both dihedral-angle tables are wrong.** With `val` $= -b(r_i,r_j)/2$ for norm $-2$ roots the correct values are $0, -\tfrac12, -\tfrac1{\sqrt2}, -\tfrac{\sqrt3}2, -1$ for $m = 2, 3, 4, 6, \infty$; the code's tables set $m{=}2 \mapsto -1$ and $m{=}4 \mapsto 0$ (labeling orthogonal pairs $m{=}4$), its "no edge" test fires on `val == 1`, which is never attained, and two entries apply `QQ(...)` to irrational numbers, which raises. The owned bond computation is exact and rational: $t = 4\,b(v,w)^2 / (q(v)\,q(w))$ at `coxeter_diagrams.sage` `_coxeter_exponent`, with the repo's minimal realizations and the no-triple-edge proof at `minimal_edge_lattices`.
6. **The example is mathematically incoherent.** For $Q = \mathrm{diag}(-1,1,1)$ the seed vectors $(-1,1,0)$ and $(-1,0,1)$ are isotropic and $(-2,1,1)$ is timelike, while roots of a hyperbolic reflection group must be spacelike for their mirrors to meet $\mathbb{H}^2$; no reflection in an isotropic vector exists at all.

## The working construction to reconcile against

The Coble notebook's cone cells are the correct realization over a live specimen: the 22 root functionals of the $(18,2,0)$-plus-two configuration (owned as `Sterk.roots_18_2_0()` in `preamble/sterk.sage`), restricted to the rank-10 invariant sublattice of the block-exchange involution — the same construction whose eleven-root configuration is now owned at `preamble/coble.sage` (`Coble.rank_ten_coxeter_roots`). Its chamber there is full-dimensional, closed, non-compact, with the ray and integral-point data extracted through Normaliz.

## What the owned implementation needs

`fundamental_chamber` is contracted to return an object of the owned `ConvexPolytopes` category (`categories/schemes/polytopes.sage`), built from the roots `vinberg_algorithm`/`allcock_edgewalk` enumerate, with: the $b(r,x) \ge 0$ half-space presentation, rays with primitive integral generators, the ray/lineality hyperbolic-domain test above (with the timelike/isotropic split naming the ideal vertices), and the Normaliz-backed Hilbert basis and integral points. `weyl_group` is the group generated by `reflection(r)` over the same roots. Neither is implemented; this note is the record of the construction until they are.
