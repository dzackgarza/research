# GAP Forms Online Provenance Snapshot (2026-02-17)

Date accessed (UTC): 2026-02-17
Auditor: Codex
Scope: package-level checklist/reference expansion for GAP `Forms` finite-field form methods.

---

## Surveyed sources

- Package page:
  - `https://gap-packages.github.io/forms/`
- Manual table of contents:
  - `https://gap-packages.github.io/forms/doc/chap0_mj.html`
- Constructors/categories/attributes/properties/operations:
  - `https://gap-packages.github.io/forms/doc/chap4_mj.html`
- Invariant/preserved forms, orthogonal components, Witt index:
  - `https://gap-packages.github.io/forms/doc/chap5_mj.html`

---

## Evidence notes captured for docs

- Constructor signatures with optional parameters:
  - `AsSesquilinearForm(obj[, field][, antiautomorphism])`
  - `AsQuadraticForm(obj[, field])`
  - `SesquilinearFormByMatrix(matrix[, field][, antiautomorphism])`
  - `QuadraticFormByMatrix(matrix[, field])`
- Category/attribute/property methods:
  - `IsSesquilinearForm`, `IsQuadraticForm`,
  - `UnderlyingVectorSpace`, `MatrixOfSesquilinearForm`, `MatrixOfQuadraticForm`,
  - `RankOfForm`, `BaseField`,
  - `IsReflexiveForm`, `IsSymmetricForm`, `IsAlternatingForm`, `IsDegenerateForm`,
  - `RadicalOfForm`.
- Group/equivalence methods:
  - `IsometricForms`, `SimilarityForms`, `IsometryGroup`, `SimilarityGroup`,
  - `InvariantBilinearForm`, `InvariantQuadraticForm`,
  - `PreservedSesquilinearForms`, `PreservedQuadraticForms`.
- Orthogonal/Witt methods:
  - `OrthogonalSubgroups`, `OrthogonalSubgroupsAsList`,
  - `OrthogonalComponents`, `OrthogonalComponentsOfSubgroup`,
  - `WittIndex`.

---

## Constraint notes captured for docs

- `MatrixOfQuadraticForm` documented in odd characteristic; chapter text records characteristic-2 matrix representation caveat.
- `PreservedSesquilinearForms` documented for absolutely irreducible matrix groups.
- `PreservedQuadraticForms` documented for absolutely irreducible groups over finite fields of odd characteristic.
- `WittIndex` documentation records characteristic-2 non-singularity condition.

---

## Known residual gap from this survey

- GAP `NConvex` package method-level canonical documentation endpoints were not fetchable through current web retrieval path during this pass; only package-level existence/status could be confirmed from package-index snippets.
- Resulting action in this pass: close the missing `Forms` checklist surface now and carry `NConvex` method-surface expansion as explicit follow-up.
