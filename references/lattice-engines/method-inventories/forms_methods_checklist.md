# GAP Forms Package Method Test Gap Checklist

Tracks GAP `Forms` package methods documented in `docs/forms/lattice/research_readme.md`.
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Package Load Surface

- [ ] `LoadPackage("Forms")`
      Source: `docs/forms/upstream/chap0_mj.html` (Package loading)

---

## 2. Constructors and Coercions

### 2a. Matrix-based constructors

- [ ] `AsSesquilinearForm(obj[, field][, antiautomorphism])`
      Source: `docs/forms/upstream/chap4_mj.html` §4 (Constructors)
- [ ] `AsQuadraticForm(obj[, field])`
      Source: `docs/forms/upstream/chap4_mj.html` §4
- [ ] `SesquilinearFormByMatrix(matrix[, field][, antiautomorphism])`
      Source: `docs/forms/upstream/chap4_mj.html` §4
- [ ] `QuadraticFormByMatrix(matrix[, field])`
      Source: `docs/forms/upstream/chap4_mj.html` §4.2-2
- [ ] `BilinearFormByMatrix(matrix[, field])`
      Source: `docs/forms/upstream/chap4_mj.html` §4.2-1
- [ ] `HermitianFormByMatrix(matrix[, field])`
      Source: `docs/forms/upstream/chap4_mj.html` §4.2-3

### 2b. Polynomial-based constructors

- [ ] `BilinearFormByPolynomial(poly, r[, n])`
      Source: `docs/forms/upstream/chap4_mj.html` §4.3-1
- [ ] `QuadraticFormByPolynomial(poly, r[, n])`
      Source: `docs/forms/upstream/chap4_mj.html` §4.3-2
- [ ] `HermitianFormByPolynomial(poly, r[, n])`
      Source: `docs/forms/upstream/chap4_mj.html` §4.3-3

### 2c. Bilinear-quadratic conversions

- [ ] `QuadraticFormByBilinearForm(form)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.4-1
- [ ] `BilinearFormByQuadraticForm(Q)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.4-2
- [ ] `AssociatedBilinearForm(Q)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.4-3

---

## 3. Categories, Attributes, and Predicates

### 3a. Category predicates

- [ ] `IsSesquilinearForm(obj)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.1-1
- [ ] `IsQuadraticForm(obj)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.1-1
- [ ] `IsBilinearForm(obj)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.1-1
- [ ] `IsHermitianForm(obj)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.1-1
- [ ] `IsForm(obj)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.1-1
- [ ] `IsTrivialForm(obj)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.1-1

### 3b. Form properties (reflexivity/symmetry/alternation)

- [ ] `IsReflexiveForm(form)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.7-1
- [ ] `IsSymmetricForm(form)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.7-3
- [ ] `IsAlternatingForm(form)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.7-2
- [ ] `IsOrthogonalForm(form)` — symmetric bilinear in odd characteristic
      Source: `docs/forms/upstream/chap4_mj.html` §4.7-4
- [ ] `IsPseudoForm(form)` — symmetric in even characteristic
      Source: `docs/forms/upstream/chap4_mj.html` §4.7-5
- [ ] `IsSymplecticForm(form)` — equivalent to alternating
      Source: `docs/forms/upstream/chap4_mj.html` §4.7-6

### 3c. Degeneracy and singularity

- [ ] `IsDegenerateForm(form)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.7-7
- [ ] `IsSingularForm(form)` — quadratic forms only, even characteristic distinction
      Source: `docs/forms/upstream/chap4_mj.html` §4.7-8

### 3d. Vector space and matrix access

- [ ] `UnderlyingVectorSpace(form)`
      Source: `docs/forms/upstream/chap2_mj.html` (Vector space methods)
- [ ] `MatrixOfSesquilinearForm(form)`
      Source: `docs/forms/upstream/chap3_mj.html` (Matrix access methods)
- [ ] `MatrixOfQuadraticForm(form)`
      Source: `docs/forms/upstream/chap3_mj.html`
      Caveat: documented only for odd field characteristic.
- [ ] `GramMatrix(form)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.7-10
- [ ] `RankOfForm(form)`
      Source: `docs/forms/upstream/chap3_mj.html`
- [ ] `BaseField(form)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.7-9

### 3e. Subspace invariants

- [ ] `RadicalOfForm(form)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.7-11
- [ ] `DiscriminantOfForm(form)` — even dimension only, not defined for hermitian
      Source: `docs/forms/upstream/chap4_mj.html` §4.7-13

### 3f. Form evaluation and subspace tests

- [ ] `EvaluateForm(f, u[, v])`
      Source: `docs/forms/upstream/chap4_mj.html` §4.5-1
- [ ] `OrthogonalSubspaceMat(form, v|mat)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.6-1
- [ ] `IsIsotropicVector(form, v)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.6-2
- [ ] `IsSingularVector(form, v)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.6-3
- [ ] `IsTotallyIsotropicSubspace(form, sub)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.6-4
- [ ] `IsTotallySingularSubspace(form, sub)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.6-5

### 3g. Polynomial representation

- [ ] `PolynomialOfForm(form)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.7-12

---

## 4. Equivalence and Group Actions

### 4a. Isometry and similarity tests

- [ ] `IsometricForms(form1, form2)`
      Source: `docs/forms/upstream/chap3_mj.html` (Isometry methods)
- [ ] `SimilarityForms(form1, form2)`
      Source: `docs/forms/upstream/chap3_mj.html`

### 4b. Groups preserving forms

- [ ] `IsometryGroup(form)`
      Source: `docs/forms/upstream/chap3_mj.html` (IsometryGroup)
- [ ] `SimilarityGroup(form)`
      Source: `docs/forms/upstream/chap3_mj.html`

### 4c. Basis change and canonical forms

- [ ] `BaseChangeToCanonical(f)`
      Source: `docs/forms/upstream/chap3_mj.html`
- [ ] `BaseChangeHomomorphism(b, gf)`
      Source: `docs/forms/upstream/chap3_mj.html`
- [ ] `IsometricCanonicalForm(f)`
      Source: `docs/forms/upstream/chap3_mj.html`
- [ ] `ScalarOfSimilarity(M, form)`
      Source: `docs/forms/upstream/chap3_mj.html`

---

## 5. Invariant and Preserved Forms of Matrix Groups

- [ ] `InvariantBilinearForm(G[, involution][, isom])`
      Source: `docs/forms/upstream/chap4_mj.html` §4.8
- [ ] `InvariantQuadraticForm(G[, involution][, isom])`
      Source: `docs/forms/upstream/chap4_mj.html` §4.8
- [ ] `PreservedSesquilinearForms(G)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.8-2
      Caveat: documented for absolutely irreducible groups.
- [ ] `PreservedQuadraticForms(G)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.8-3
      Caveat: documented for absolutely irreducible groups over odd characteristic finite fields.
- [ ] `PreservedForms(G)`
      Source: `docs/forms/upstream/chap4_mj.html` §4.8-1

---

## 6. Orthogonal Decomposition and Witt Index

- [ ] `OrthogonalSubgroups(G, n[, s])`
      Source: `docs/forms/upstream/chap5_mj.html` §5
- [ ] `OrthogonalSubgroupsAsList(G, n[, s])`
      Source: `docs/forms/upstream/chap5_mj.html` §5
- [ ] `OrthogonalComponents(G, n)`
      Source: `docs/forms/upstream/chap5_mj.html` §5
- [ ] `OrthogonalComponentsOfSubgroup(U, n)`
      Source: `docs/forms/upstream/chap5_mj.html` §5
      Caveat: requires subgroup `U` generated by vectors in a row-space model carrying form `n`.
- [ ] `WittIndex(form)`
      Source: `docs/forms/upstream/chap5_mj.html` §5
      Caveat: algorithm documented for finite fields; in characteristic `2`, method requires a non-singular form.
- [ ] `TypeOfForm(form)`
      Source: `docs/forms/upstream/chap5_mj.html` §5
- [ ] `IsHyperbolicForm(form)`
      Source: `docs/forms/upstream/chap5_mj.html` §5
- [ ] `IsEllipticForm(form)`
      Source: `docs/forms/upstream/chap5_mj.html` §5
- [ ] `IsParabolicForm(form)`
      Source: `docs/forms/upstream/chap5_mj.html` §5

---

## Domain and Constraint Caveats

- The `Forms` package is finite-field form algebra (`GF(q)`) and does not use real-signature positive-definite/indefinite regimes.
- Quadratic-form matrix extraction (`MatrixOfQuadraticForm`) is documented for odd characteristic.
- `PreservedQuadraticForms` is documented for absolutely irreducible matrix groups over odd-characteristic finite fields.

---

## References

- `docs/forms/lattice/research_readme.md`
- GAP package page: `https://gap-packages.github.io/forms/`
- Forms manual table of contents: `https://gap-packages.github.io/forms/doc/chap0_mj.html`
- Forms manual chapter 4 (constructors/attributes/operations): `https://gap-packages.github.io/forms/doc/chap4_mj.html`
- Forms manual chapter 5 (preserved forms/orthogonal components/Witt index): `https://gap-packages.github.io/forms/doc/chap5_mj.html`
