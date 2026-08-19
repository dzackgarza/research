# GAP CddInterface Lattice-Oriented Reference (Archived Scope Violation)
## Polyhedral H/V-representation workflows and cddlib-backed operations

Archived under `docs/archive/scope_violations/` because this surface is polyhedral/LP-focused and outside this project's bilinear-form lattice-theory scope.

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PKG]` | Provided by GAP package `CddInterface` |
| `[POLY]` | Polyhedral/cone computation workflow |
| `[REP]` | H-representation/V-representation conversion surface |
| `[LP]` | Linear-programming/Fourier projection workflow |

---

## 1. Scope

`CddInterface` is a GAP interface package to cdd/cddlib for rational polyhedra and cones.
Lattice-relevant surfaces in this repository are the integer/rational polyhedral APIs:

- polyhedron construction from inequalities/generators,
- conversion between H- and V-representations,
- face/facet/interior-point extraction,
- containment/intersection queries,
- LP and Fourier-projection workflows.

---

## 2. Constructors and Representation Conversion

| Function | Description | Tags |
|----------|-------------|------|
| `Cdd_PolyhedronByInequalities(ineq)` | Construct polyhedron from inequality matrix data. | `[PKG, POLY, REP]` |
| `Cdd_PolyhedronByInequalities(eq, ineq)` | Construct polyhedron from equalities plus inequalities. | `[PKG, POLY, REP]` |
| `Cdd_PolyhedronByGenerators(gen)` | Construct polyhedron from generator data. | `[PKG, POLY, REP]` |
| `Cdd_PolyhedronByGenerators(line, gen)` | Construct polyhedron from lineality and generator data. | `[PKG, POLY, REP]` |
| `Cdd_Canonicalize(P)` | Canonicalize/reduce representation by removing redundancy. | `[PKG, POLY, REP]` |
| `Cdd_V_Rep(P)` / `Cdd_H_Rep(P)` | Convert/retrieve reduced V- or H-representation. | `[PKG, POLY, REP]` |
| `Cdd_V_Rep(P, r)` / `Cdd_H_Rep(P, r)` | V/H conversion under explicit arithmetic ring parameter `r`. | `[PKG, POLY, REP]` |

---

## 3. Attributes and Predicates

| Function | Description | Tags |
|----------|-------------|------|
| `Cdd_AmbientSpaceDimension(P)` | Ambient dimension attribute. | `[PKG, POLY]` |
| `Cdd_Dimension(P)` | Intrinsic polyhedron dimension attribute. | `[PKG, POLY]` |
| `Cdd_GeneratingVertices(P)` / `Cdd_GeneratingRays(P)` | Vertex/ray generator accessors. | `[PKG, POLY]` |
| `Cdd_Equalities(P)` / `Cdd_Inequalities(P)` | Equality/inequality systems defining `P`. | `[PKG, POLY]` |
| `Cdd_Lines(P)` / `Cdd_Vertices(P)` | Lineality and vertex-level extraction accessors. | `[PKG, POLY]` |
| `Cdd_IsEmpty(P)` / `Cdd_IsCone(P)` / `Cdd_IsLinSpace(P)` / `Cdd_IsPointed(P)` | Core geometric predicates. | `[PKG, POLY]` |

---

## 4. Faces, Interior Data, and Linearity Extension

| Function | Description | Tags |
|----------|-------------|------|
| `Cdd_Faces(P)` | Face enumeration/combinatorial output. | `[PKG, POLY]` |
| `Cdd_FacesWithFixedDimension(P, d)` | Faces in fixed dimension `d`. | `[PKG, POLY]` |
| `Cdd_Facets(P)` | Facet extraction. | `[PKG, POLY]` |
| `Cdd_InteriorPoint(P)` | Interior-point extraction when available. | `[PKG, POLY]` |
| `Cdd_FacesWithInteriorPoints(P)` | Faces paired with interior-point data. | `[PKG, POLY]` |
| `Cdd_FacesWithFixedDimensionAndInteriorPoints(P, d)` | Fixed-dimension face extraction with interior points. | `[PKG, POLY]` |
| `Cdd_ExtendLinearity(P, V)` | Extend lineality with vectors `V` before recomputation. | `[PKG, POLY]` |

---

## 5. Containment, Intersection, LP, and Projection

| Function | Description | Tags |
|----------|-------------|------|
| `Cdd_IsContained(P1, P2)` | Polyhedral containment test. | `[PKG, POLY]` |
| `Cdd_Intersection(P1, P2)` | Polyhedral intersection operation. | `[PKG, POLY]` |
| `Cdd_LinearProgram(P, b)` | Solve linear-programming objective for polyhedron `P` and vector `b`. | `[PKG, POLY, LP]` |
| `Cdd_FourierProjection(P, var)` | Fourier projection of polyhedron `P` to selected variables. | `[PKG, POLY, LP]` |
| `Cdd_FourierProjection([A, b], var)` | Fourier projection from inequality/equality matrix form `[A, b]`. | `[PKG, POLY, LP]` |

---

## 6. Domain Notes

- `CddInterface` methods here are rational polyhedral and cone algorithms; they do not encode a real-signature positive-definite/indefinite quadratic-form regime.
- LP/projection operations are polyhedral elimination/optimization routines and should not be interpreted as arithmetic-lattice genus or discriminant-form classifiers.

---

## 7. Sources

- CddInterface package page: `https://homalg-project.github.io/CddInterface/`
- CddInterface manual table of contents: `https://homalg-project.github.io/CddInterface/doc/chap0_mj.html`
- CddInterface manual chapter 2 (polyhedra/attributes): `https://homalg-project.github.io/CddInterface/doc/chap2_mj.html`
- CddInterface manual chapter 3 (linear programming/Fourier projection): `https://homalg-project.github.io/CddInterface/doc/chap3_mj.html`
- CddInterface manual chapter 4 (special functions): `https://homalg-project.github.io/CddInterface/doc/chap4_mj.html`
