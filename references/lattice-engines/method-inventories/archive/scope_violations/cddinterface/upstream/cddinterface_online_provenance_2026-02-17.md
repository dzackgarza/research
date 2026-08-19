# GAP CddInterface Online Provenance Snapshot (2026-02-17)

Archived from active scope under `docs/archive/scope_violations/`.

Date accessed (UTC): 2026-02-17
Auditor: Codex
Scope: first-class checklist/reference expansion for GAP `CddInterface` polyhedral methods.

---

## Surveyed sources

- Package page:
  - `https://homalg-project.github.io/CddInterface/`
- Manual table of contents:
  - `https://homalg-project.github.io/CddInterface/doc/chap0_mj.html`
- Polyhedra/attributes and H/V representation surface:
  - `https://homalg-project.github.io/CddInterface/doc/chap2_mj.html`
- LP/Fourier projection surface:
  - `https://homalg-project.github.io/CddInterface/doc/chap3_mj.html`
- Special functions surface:
  - `https://homalg-project.github.io/CddInterface/doc/chap4_mj.html`

---

## Evidence notes captured for docs

- Constructor signatures:
  - `Cdd_PolyhedronByInequalities(ineq)` and `Cdd_PolyhedronByInequalities(eq, ineq)`
  - `Cdd_PolyhedronByGenerators(gen)` and `Cdd_PolyhedronByGenerators(line, gen)`
- Representation and canonicalization:
  - `Cdd_Canonicalize`, `Cdd_V_Rep`, `Cdd_H_Rep`, and ring-parameter variants.
- Attributes/predicates:
  - `Cdd_AmbientSpaceDimension`, `Cdd_Dimension`,
  - `Cdd_GeneratingVertices`, `Cdd_GeneratingRays`,
  - `Cdd_Equalities`, `Cdd_Inequalities`,
  - `Cdd_Lines`, `Cdd_Vertices`,
  - `Cdd_IsEmpty`, `Cdd_IsCone`, `Cdd_IsLinSpace`, `Cdd_IsPointed`.
- Face/interior/linearity operations:
  - `Cdd_Faces`, `Cdd_FacesWithFixedDimension`, `Cdd_Facets`,
  - `Cdd_InteriorPoint`, `Cdd_FacesWithInteriorPoints`,
  - `Cdd_FacesWithFixedDimensionAndInteriorPoints`, `Cdd_ExtendLinearity`.
- LP and elimination/projection:
  - `Cdd_LinearProgram(P, b)`,
  - `Cdd_FourierProjection(P, var)` and `Cdd_FourierProjection([A, b], var)`.

---

## Constraint notes captured for docs

- Surface is polyhedral/combinatorial and not a PD/INDEF quadratic-form classification API.
- `Cdd_FourierProjection` supports both polyhedron and matrix-form (`[A, b]`) inputs per manual examples.
