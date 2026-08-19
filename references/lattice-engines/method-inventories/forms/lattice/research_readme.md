# GAP Forms Package Lattice-Oriented Reference
## Finite-field sesquilinear/quadratic forms and orthogonal decomposition workflows

---

## Tag Legend

| Tag | Meaning |
|-----|---------|
| `[PKG]` | Provided by GAP package `Forms` |
| `[FFORM]` | Finite-field form setting (no real-signature PD/INDEF notion) |
| `[EQUIV]` | Isometry/similarity/equivalence workflow |
| `[GRP]` | Matrix-group interaction |
| `[DECOMP]` | Orthogonal decomposition / Witt-index workflow |

---

## 1. Scope

The GAP `Forms` package provides sesquilinear and quadratic-form APIs over finite fields and supporting matrix-group workflows.

This surface is lattice-relevant in the finite-field and group-action sense:

- form constructors from matrices and coercion APIs,
- form predicates/invariants (rank, radical, symmetry/alternation),
- isometry/similarity and form-preserving matrix-group computations,
- orthogonal decomposition and Witt-index methods.

---

## 2. Constructors and Coercions

### 2a. Matrix-based constructors

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `AsSesquilinearForm(obj[, field][, antiautomorphism])` | `obj`: matrix or form object, `field`: finite field (optional), `antiautomorphism`: involution (optional) | `IsSesquilinearForm` | Construct/coerce sesquilinear form from matrix/form object with optional field and involution control. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"ReflexiveSesquilinearForm" |
| `AsQuadraticForm(obj[, field])` | `obj`: matrix or form object, `field`: finite field (optional) | `IsQuadraticForm` | Construct/coerce quadratic form from matrix/form object with optional field override. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"QuadraticFormByMatrix" |
| `SesquilinearFormByMatrix(matrix[, field][, antiautomorphism])` | `matrix`: square matrix over finite field, `field`: finite field (optional), `antiautomorphism`: involution (optional) | `IsSesquilinearForm` | Build a sesquilinear form from matrix data. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"SesquilinearFormByMatrix" |
| `QuadraticFormByMatrix(matrix[, field])` | `matrix`: square matrix over finite field, `field`: finite field (optional) | `IsQuadraticForm` | Build a quadratic form from matrix data. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"QuadraticFormByMatrix" |
| `BilinearFormByMatrix(matrix[, field])` | `matrix`: symmetric or skew-symmetric square matrix, `field`: finite field (optional) | `IsBilinearForm` | Construct bilinear form from symmetric/skew-symmetric matrix. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"BilinearFormByMatrix" |
| `HermitianFormByMatrix(matrix, field)` | `matrix`: hermitian square matrix, `field`: finite field (required, square order) | `IsHermitianForm` | Construct hermitian form from matrix data. Field must have square order. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"HermitianFormByMatrix" |

### 2b. Polynomial-based constructors

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `BilinearFormByPolynomial(poly, r[, n])` | `poly`: homogeneous degree-2 polynomial, `r`: polynomial ring, `n`: dimension (optional) | `IsBilinearForm` | Construct bilinear form from polynomial. Not available in even characteristic. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"BilinearFormByPolynomial" |
| `QuadraticFormByPolynomial(poly, r[, n])` | `poly`: homogeneous degree-2 polynomial, `r`: polynomial ring, `n`: dimension (optional) | `IsQuadraticForm` | Construct quadratic form from polynomial. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"QuadraticFormByPolynomial" |
| `HermitianFormByPolynomial(poly, r[, n])` | `poly`: homogeneous degree-(q+1) polynomial, `r`: polynomial ring over GF(q²), `n`: dimension (optional) | `IsHermitianForm` | Construct hermitian form from polynomial. Field must have square order. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"HermitianFormByPolynomial" |

### 2c. Bilinear-quadratic conversions

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `QuadraticFormByBilinearForm(form)` | `form`: orthogonal bilinear form | `IsQuadraticForm` | Construct quadratic form Q such that Q(v) = form(v,v). Requires odd characteristic and orthogonal bilinear form. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"QuadraticFormByBilinearForm" |
| `BilinearFormByQuadraticForm(Q)` | `Q`: `IsQuadraticForm` | `IsBilinearForm` | Extract bilinear form f such that f(v,v) = Q(v). Requires odd characteristic. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"BilinearFormByQuadraticForm" |
| `AssociatedBilinearForm(Q)` | `Q`: `IsQuadraticForm` | `IsBilinearForm` | Returns bilinear form f such that f(v,w) = Q(v+w) - Q(v) - Q(w). | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"AssociatedBilinearForm" |

---

## 3. Categories, Attributes, and Predicates

### 3a. Category predicates

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `IsSesquilinearForm(obj)` | `obj`: any object | `true`/`false` | Category predicate for sesquilinear forms. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsSesquilinearForm" |
| `IsQuadraticForm(obj)` | `obj`: any object | `true`/`false` | Category predicate for quadratic forms. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsQuadraticForm" |
| `IsBilinearForm(obj)` | `obj`: any object | `true`/`false` | Category predicate for bilinear forms. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsBilinearForm" |
| `IsHermitianForm(obj)` | `obj`: any object | `true`/`false` | Category predicate for hermitian forms. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsHermitianForm" |
| `IsForm(obj)` | `obj`: any object | `true`/`false` | General form category predicate. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsForm" |
| `IsTrivialForm(obj)` | `obj`: any object | `true`/`false` | Category predicate for trivial form (maps all vectors to zero). | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsTrivialForm" |

### 3b. Form properties (reflexivity, symmetry, alternation)

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `IsReflexiveForm(form)` | `form`: `IsForm` | `true`/`false` | Reflexivity predicate. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsReflexiveForm" |
| `IsSymmetricForm(form)` | `form`: `IsForm` | `true`/`false` | Symmetry predicate. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsSymmetricForm" |
| `IsAlternatingForm(form)` | `form`: `IsForm` | `true`/`false` | Alternation predicate (f(v,v)=0 for all v). | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsAlternatingForm" |
| `IsOrthogonalForm(form)` | `form`: `IsSesquilinearForm` | `true`/`false` | Orthogonal predicate: symmetric bilinear in odd characteristic. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsOrthogonalForm" |
| `IsPseudoForm(form)` | `form`: `IsSesquilinearForm` | `true`/`false` | Pseudo form: symmetric but not alternating in even characteristic. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsPseudoForm" |
| `IsSymplecticForm(form)` | `form`: `IsSesquilinearForm` | `true`/`false` | Symplectic predicate (equivalent to alternating). | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsSymplecticForm" |

### 3c. Degeneracy and singularity

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `IsDegenerateForm(form)` | `form`: `IsForm` | `true`/`false` | Degeneracy predicate (non-trivial radical). | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsDegenerateForm" |
| `IsSingularForm(form)` | `form`: `IsQuadraticForm` | `true`/`false` | Singular predicate for quadratic forms. Differs from degenerate in even characteristic. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsSingularForm" |

### 3d. Vector space and matrix access

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `UnderlyingVectorSpace(form)` | `form`: `IsForm` | `GF` vector space | Return underlying vector space of form domain. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"UnderlyingVectorSpace" |
| `MatrixOfSesquilinearForm(form)` | `form`: `IsSesquilinearForm` | matrix | Matrix representation associated to a sesquilinear form. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"MatrixOfSesquilinearForm" |
| `MatrixOfQuadraticForm(form)` | `form`: `IsQuadraticForm` | matrix | Matrix representation for quadratic form (documented for odd characteristic). | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"MatrixOfQuadraticForm" |
| `GramMatrix(form)` | `form`: `IsForm` | matrix | Gram matrix of the form. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"GramMatrix" |
| `RankOfForm(form)` | `form`: `IsForm` | integer | Rank invariant of the form. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"RankOfForm" |
| `BaseField(form)` | `form`: `IsForm` | field | Base field of the form. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"BaseField" |

### 3e. Subspace invariants

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `RadicalOfForm(form)` | `form`: `IsForm` | vector space | Radical subspace of the form. | `[PKG, FFORM, DECOMP]` | `docs/forms/upstream/chap4_mj.html` §"RadicalOfForm" |
| `DiscriminantOfForm(form)` | `form`: `IsForm` | string ("square"/"nonsquare") | Discriminant of even-dimensional form. Not defined for hermitian forms. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"DiscriminantOfForm" |

### 3f. Form evaluation and subspace tests

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `EvaluateForm(f, u[, v])` | `f`: form, `u`: vector/matrix, `v`: vector (optional) | field element | Evaluate form on vector(s). | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"EvaluateForm" |
| `OrthogonalSubspaceMat(form, v)` | `form`: form, `v`: vector | matrix | Returns basis of subspace orthogonal to vector v. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"OrthogonalSubspaceMat" |
| `OrthogonalSubspaceMat(form, mat)` | `form`: form, `mat`: matrix | matrix | Returns basis of subspace orthogonal to span of mat's rows. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"OrthogonalSubspaceMat" |
| `IsIsotropicVector(form, v)` | `formv`: vector | `true`/``: form, `false` | Test if vector is isotropic (form(v,v)=0). | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsIsotropicVector" |
| `IsSingularVector(form, v)` | `form`: `IsQuadraticForm`, `v`: vector | `true`/`false` | Test if vector is singular. In odd characteristic, isotropic = singular. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsSingularVector" |
| `IsTotallyIsotropicSubspace(form, sub)` | `form`: form, `sub`: list of vectors | `true`/`false` | Test if subspace is totally isotropic. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsTotallyIsotropicSubspace" |
| `IsTotallySingularSubspace(form, sub)` | `form`: `IsQuadraticForm`, `sub`: list of vectors | `true`/`false` | Test if subspace is totally singular. | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"IsTotallySingularSubspace" |

### 3g. Polynomial representation

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `PolynomialOfForm(form)` | `form`: `IsForm` | polynomial | Returns polynomial defining the form (not bilinear in even char). | `[PKG, FFORM]` | `docs/forms/upstream/chap4_mj.html` §"PolynomialOfForm" |

Characteristic caveat:
- Manual chapter 4 documents `MatrixOfQuadraticForm` for odd characteristic and notes matrix reconstruction differences in characteristic `2`.

---

## 4. Equivalence and Symmetry Groups

### 4a. Isometry and similarity tests

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `IsometricForms(form1, form2)` | `form1`, `form2`: `IsForm` | `true`/`false` | Isometry test between forms. | `[PKG, FFORM, EQUIV]` | `docs/forms/upstream/chap4_mj.html` §"IsometricForms" |
| `SimilarityForms(form1, form2)` | `form1`, `form2`: `IsForm` | `true`/`false` | Similarity test between forms. | `[PKG, FFORM, EQUIV]` | `docs/forms/upstream/chap4_mj.html` §"SimilarityForms" |

### 4b. Groups preserving forms

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `IsometryGroup(form)` | `form`: `IsForm` | matrix group | Group preserving the form exactly. | `[PKG, FFORM, EQUIV, GRP]` | `docs/forms/upstream/chap4_mj.html` §"IsometryGroup" |
| `SimilarityGroup(form)` | `form`: `IsForm` | matrix group | Group preserving the form up to scalar factor. | `[PKG, FFORM, EQUIV, GRP]` | `docs/forms/upstream/chap4_mj.html` §"SimilarityGroup" |

### 4c. Basis change and canonical forms

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `BaseChangeToCanonical(f)` | `f`: `IsForm` | matrix | Returns transition matrix to canonical form representative. | `[PKG, FFORM, EQUIV]` | `docs/forms/upstream/chap4_mj.html` §"BaseChangeToCanonical" |
| `BaseChangeHomomorphism(b, gf)` | `b`: invertible matrix, `gf`: finite field | inner automorphism | Returns inner automorphism of GL(d,q) induced by transition matrix b. | `[PKG, FFORM, EQUIV]` | `docs/forms/upstream/chap4_mj.html` §"BaseChangeHomomorphism" |
| `IsometricCanonicalForm(f)` | `f`: `IsForm` | form | Returns canonical representative of isometry class. | `[PKG, FFORM, EQUIV]` | `docs/forms/upstream/chap4_mj.html` §"IsometricCanonicalForm" |
| `ScalarOfSimilarity(M, form)` | `M`: matrix, `form`: `IsForm` | field element or `fail` | Returns scalar λ such that M induces a similarity with factor λ. | `[PKG, FFORM, EQUIV]` | `docs/forms/upstream/chap4_mj.html` §"ScalarOfSimilarity" |

---

## 5. Invariant and Preserved Forms of Matrix Groups

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `InvariantBilinearForm(G[, involution][, isom])` | `G`: matrix group, `involution`: involution (optional), `isom`: isomorphism (optional) | bilinear form | Construct bilinear form invariant under matrix-group action. | `[PKG, FFORM, GRP]` | `docs/forms/upstream/chap5_mj.html` §"InvariantBilinearForm" |
| `InvariantQuadraticForm(G[, involution][, isom])` | `G`: matrix group, `involution`: involution (optional), `isom`: isomorphism (optional) | quadratic form | Construct quadratic form invariant under matrix-group action. | `[PKG, FFORM, GRP]` | `docs/forms/upstream/chap5_mj.html` §"InvariantQuadraticForm" |
| `PreservedSesquilinearForms(G)` | `G`: matrix group (absolutely irreducible) | list of forms | Return preserved sesquilinear forms for `G`; documented for absolutely irreducible groups. | `[PKG, FFORM, GRP]` | `docs/forms/upstream/chap5_mj.html` §"PreservedSesquilinearForms" |
| `PreservedQuadraticForms(G)` | `G`: matrix group (absolutely irreducible) | list of forms | Return preserved quadratic forms for absolutely irreducible groups over finite fields of odd characteristic. | `[PKG, FFORM, GRP]` | `docs/forms/upstream/chap5_mj.html` §"PreservedQuadraticForms" |
| `PreservedForms(G)` | `G`: matrix group | list of forms | Return all preserved forms (sesquilinear and quadratic) for a matrix group. | `[PKG, FFORM, GRP]` | `docs/forms/upstream/chap5_mj.html` §"PreservedForms" |

Workflow caveat:
- Chapter 5 states `PreservedSesquilinearForms`/`PreservedQuadraticForms` in an absolutely irreducible matrix-group regime; quadratic case is odd-characteristic only.

---

## 6. Orthogonal Decomposition and Witt Index

| Function | Argument Types | Return Type | Description | Tags | Source |
|----------|----------------|-------------|-------------|------|--------|
| `OrthogonalSubgroups(G, n[, s])` | `G`: matrix group, `n`: form, `s`: integer (optional) | record | Orthogonal decomposition helper returning subgroup data for form model `n`. | `[PKG, FFORM, DECOMP]` | `docs/forms/upstream/chap5_mj.html` §"OrthogonalSubgroups" |
| `OrthogonalSubgroupsAsList(G, n[, s])` | `G`: matrix group, `n`: form, `s`: integer (optional) | list | List-form output variant of orthogonal subgroup decomposition. | `[PKG, FFORM, DECOMP]` | `docs/forms/upstream/chap5_mj.html` §"OrthogonalSubgroupsAsList" |
| `OrthogonalComponents(G, n)` | `G`: matrix group, `n`: form | list of forms | Orthogonal components of module/group with respect to form `n`. | `[PKG, FFORM, DECOMP]` | `docs/forms/upstream/chap5_mj.html` §"OrthogonalComponents" |
| `OrthogonalComponentsOfSubgroup(U, n)` | `U`: subgroup, `n`: form | list of forms | Orthogonal components restricted to subgroup `U` of ambient row-space carrying form `n`. | `[PKG, FFORM, DECOMP]` | `docs/forms/upstream/chap5_mj.html` §"OrthogonalComponentsOfSubgroup" |
| `WittIndex(form)` | `form`: `IsForm` | integer | Witt-index computation for finite-field forms; characteristic `2` requires non-singular form. | `[PKG, FFORM, DECOMP]` | `docs/forms/upstream/chap5_mj.html` §"WittIndex" |
| `TypeOfForm(form)` | `form`: `IsForm` | string | Returns type classification: "hyperbolic", "elliptic", or "parabolic". | `[PKG, FFORM, DECOMP]` | `docs/forms/upstream/chap5_mj.html` §"TypeOfForm" |
| `IsHyperbolicForm(form)` | `form`: `IsForm` | `true`/`false` | Predicate for hyperbolic forms. | `[PKG, FFORM, DECOMP]` | `docs/forms/upstream/chap5_mj.html` §"IsHyperbolicForm" |
| `IsEllipticForm(form)` | `form`: `IsForm` | `true`/`false` | Predicate for elliptic forms. | `[PKG, FFORM, DECOMP]` | `docs/forms/upstream/chap5_mj.html` §"IsEllipticForm" |
| `IsParabolicForm(form)` | `form`: `IsForm` | `true`/`false` | Predicate for parabolic forms. | `[PKG, FFORM, DECOMP]` | `docs/forms/upstream/chap5_mj.html` §"IsParabolicForm" |

---

## 7. Definiteness and Domain Notes

- `Forms` is finite-field linear/form algebra and does not provide real-signature (`PD`/`INDEF`) contracts.
- Orthogonal and Witt-index methods here should not be conflated with integer-lattice genus/signature classification over `ZZ`/`QQ`.
- For integer-matrix normal forms and Euclidean reduction in GAP, use core integer-matrix and `LLLReduced*` APIs (documented in `docs/gap/lattice/research_readme.md`).

---

## 8. Sources

- Forms package page: `https://gap-packages.github.io/forms/`
- Forms manual TOC: `https://gap-packages.github.io/forms/doc/chap0_mj.html`
- Forms manual chapter 4: `https://gap-packages.github.io/forms/doc/chap4_mj.html`
- Forms manual chapter 5: `https://gap-packages.github.io/forms/doc/chap5_mj.html`
- Local upstream snapshot (provenance): `docs/forms/upstream/forms_online_provenance_2026-02-17.md`
- Local upstream chapters: `docs/forms/upstream/chap4_mj.html`, `docs/forms/upstream/chap5_mj.html` (type/characteristic caveats verified from these files)
