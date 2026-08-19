# CddInterface Method Test Gap Checklist (Archived Scope Violation)

Archived from active scope. Tracks GAP `CddInterface` polyhedral methods documented in
`docs/archive/scope_violations/cddinterface/lattice/cddinterface_lattice_reference.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Package Load Surface

- [ ] `LoadPackage("CddInterface")`

---

## 2. Polyhedron Constructors and Representation Conversion

- [ ] `Cdd_PolyhedronByInequalities(ineq)`
- [ ] `Cdd_PolyhedronByInequalities(eq, ineq)`
- [ ] `Cdd_PolyhedronByGenerators(gen)`
- [ ] `Cdd_PolyhedronByGenerators(line, gen)`
- [ ] `Cdd_Canonicalize(P)`
- [ ] `Cdd_V_Rep(P)`
- [ ] `Cdd_H_Rep(P)`
- [ ] `Cdd_V_Rep(P, r)`
- [ ] `Cdd_H_Rep(P, r)`

---

## 3. Attributes and Predicates

- [ ] `Cdd_AmbientSpaceDimension(P)`
- [ ] `Cdd_Dimension(P)`
- [ ] `Cdd_GeneratingVertices(P)`
- [ ] `Cdd_GeneratingRays(P)`
- [ ] `Cdd_Equalities(P)`
- [ ] `Cdd_Inequalities(P)`
- [ ] `Cdd_Lines(P)`
- [ ] `Cdd_Vertices(P)`
- [ ] `Cdd_IsEmpty(P)`
- [ ] `Cdd_IsCone(P)`
- [ ] `Cdd_IsLinSpace(P)`
- [ ] `Cdd_IsPointed(P)`

---

## 4. Faces, Interior Data, and Linearity Extension

- [ ] `Cdd_Faces(P)`
- [ ] `Cdd_FacesWithFixedDimension(P, d)`
- [ ] `Cdd_Facets(P)`
- [ ] `Cdd_InteriorPoint(P)`
- [ ] `Cdd_FacesWithInteriorPoints(P)`
- [ ] `Cdd_FacesWithFixedDimensionAndInteriorPoints(P, d)`
- [ ] `Cdd_ExtendLinearity(P, V)`

---

## 5. Containment, Intersection, LP, and Projection

- [ ] `Cdd_IsContained(P1, P2)`
- [ ] `Cdd_Intersection(P1, P2)`
- [ ] `Cdd_LinearProgram(P, b)`
- [ ] `Cdd_FourierProjection(P, var)`
- [ ] `Cdd_FourierProjection([A, b], var)`

---

## Domain Caveat

- `CddInterface` is a polyhedral-computation interface to cdd/cddlib, not a quadratic-form signature/genus/isometry classifier API.

---

## References

- `docs/archive/scope_violations/cddinterface/lattice/cddinterface_lattice_reference.md`
- GAP package page: `https://homalg-project.github.io/CddInterface/`
- CddInterface manual table of contents: `https://homalg-project.github.io/CddInterface/doc/chap0_mj.html`
- CddInterface manual chapter 2 (polyhedra/attributes): `https://homalg-project.github.io/CddInterface/doc/chap2_mj.html`
- CddInterface manual chapter 3 (linear programming/Fourier projection): `https://homalg-project.github.io/CddInterface/doc/chap3_mj.html`
- CddInterface manual chapter 4 (special functions): `https://homalg-project.github.io/CddInterface/doc/chap4_mj.html`
