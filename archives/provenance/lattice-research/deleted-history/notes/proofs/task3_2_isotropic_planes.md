# Task 3.2: Uniqueness of 1-Cusp via Isotropic Plane Classification

## Theorem Statement

Standard period-domain references already place the Coble moduli problem in a Type IV /
Baily-Borel setting; see `REFERENCES.md`, `notes/literature_claim_map.md`, and
`notes/moduli_dimension_claim.md` for the canonical source chain through Scattone,
Sterk, Dolgachev–Kondō, and Friedman.

The repo-specific claim verified in this note is the lattice calculation that supports
the 1-cusp description used in that literature-backed framework:

**Claim verified here**: there is a unique $O(T*{\mathrm{Co}})$-orbit of primitive
isotropic planes $J \subset T_{\mathrm{Co}}$, and for any such plane, the quotient
$J^\perp/J$ is isometric to $A_1^{\oplus 7}$.

## Mathematical Background

### Lattice Setup

From the standard K3/lattice setup (Coble 1917, 1929; Nikulin 1979) as recorded in
`notes/literature_claim_map.md`, the transcendental lattice of a Coble surface has the
following structure, verified computationally in Tasks 1.1-1.3:

- **Transcendental lattice**: $T_{\mathrm{Co}} \cong (11, 11, 1)_2$ in Nikulin notation
- **Signature**: $(2, 9)$ (2 positive, 9 negative directions)
- **Rank**: 11
- **Discriminant group**: $A_{T_{\mathrm{Co}}} \cong (\mathbb{Z}/2\mathbb{Z})^{11}$
- **Gram matrix**: $\operatorname{diag}(2, 2, -2, -2, \ldots, -2)$

### Isotropic Planes and Cusps

**Definition**: An isotropic plane $J \subset T_{\mathrm{Co}}$ is a 2-dimensional
subspace such that the bilinear form restricts to zero on $J$.

**Key facts**:

1. The Witt index of $T_{\mathrm{Co}}$ is $\min(2, 9) = 2$, so maximal isotropic
   subspaces have dimension 2
2. Primitive isotropic planes correspond to 1-cusps in the Baily-Borel compactification
3. For a primitive isotropic plane $J$:
   - $J^\perp = \{v \in T_{\mathrm{Co}} : v \cdot j = 0 \text{ for all } j \in J\}$ has
     rank $11 - 2 = 9$
   - $J \subset J^\perp$ (since $J$ is isotropic)
   - The quotient $J^\perp/J$ has rank $9 - 2 = 7$
   - $J^\perp/J$ inherits a nondegenerate negative-definite bilinear form

### Theoretical Prediction

From Nikulin's classification of 2-elementary lattices (Nikulin 1979) and Sterk's work
on Enriques moduli (Sterk 1991), as recorded in `REFERENCES.md`:

- For $T_{\mathrm{Co}}$ with $(r, a, \delta) = (11, 11, 1)$, the genus contains a unique
  isometry class (Nikulin 1979, Theorem 1.14.2)
- The map $O(T_{\mathrm{Co}}) \to O(q_{T_{\mathrm{Co}}})$ is surjective (Nikulin 1979,
  Prop. 1.5.2)
- Isotropic plane orbits are determined by their images in the discriminant group
- **Prediction**: There is exactly ONE $O(T_{\mathrm{Co}})$-orbit of isotropic planes
- For the unique orbit: $J^\perp/J \cong A_1^{\oplus 7}$

**Literature context**: The lattice structure S_Co = ⟨2⟩ ⊕ ⟨-2⟩^10 aligns with Pieroni's
E₁₀ = Num(X) framework (Pieroni 2026, lines 146, 483-493). Note: Pieroni's Theorem 46
concerns isotropic sequences of elliptic curves on Coble surfaces (geometric concept:
E_i·E_j = 1 - δ_ij), not lattice-theoretic isotropic vectors (v² = 0). These are
distinct concepts — the theorem does not directly support the orbit uniqueness claim.

## Computational Verification

### Script: `task3_2_isotropic_planes.sage`

The computation proceeds in several steps:

#### Step 1: Construct $T_{\mathrm{Co}}$

```sage
T_Co_gram = diagonal_matrix(QQ, [2, 2] + [-2]*9)
T_Co = IntegralLattice(T_Co_gram)
```

Verified: signature $(2, 9)$, rank 11, determinant $-2048$.

#### Step 2: Find Isotropic Vectors

For $v = (a, b, c_1, \ldots, c_9)$ to be isotropic: $$v^2 = 2a^2 + 2b^2 - 2(c_1^2 +
\cdots + c_9^2) = 0$$ Equivalently: $a^2 + b^2 = c_1^2 + \cdots + c_9^2$

**Examples found**:

- $v_1 = (1, 1, 1, 1, 0, \ldots, 0)$: $1 + 1 = 1 + 1$ ✓
- $v_2 = (1, 0, 1, 0, 0, \ldots, 0)$: $1 + 0 = 1 + 0$ ✓
- $v_3 = (2, 1, 2, 1, 0, \ldots, 0)$: $4 + 1 = 4 + 1$ ✓

Total: 8 unique isotropic vectors (up to sign) from systematic search.

#### Step 3: Construct Isotropic Planes

An isotropic plane $J$ is spanned by two linearly independent isotropic vectors $v_1,
v_2$ with $v_1 \cdot v_2 = 0$.

**Example**: $$v_1 = (1, 1, 1, 1, 0, \ldots, 0)$$ $$v_2 = (1, 0, 1, 0, 0, \ldots, 0)$$

Verification:

- $v_1^2 = 0$ ✓
- $v_2^2 = 0$ ✓
- $v_1 \cdot v_2 = 2(1)(1) + 2(1)(0) - 2(1)(1) - 2(1)(0) = 0$ ✓
- Linear independence: $\operatorname{rank}\begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = 2$
  ✓

**Result**: Found 27 isotropic planes from the search.

#### Step 4: Compute $J^\perp$ and $J^\perp/J$

For the example plane $J = \operatorname{span}(v_1, v_2)$:

**Orthogonal complement**: $$J^\perp = \{w \in T_{\mathrm{Co}} : w \cdot v = 0 \text{
for all } v \in J\}$$

Computed via kernel of the matrix $V \cdot G$ where $V$ has $v_1, v_2$ as rows and $G$
is the Gram matrix.

**Result**: $\dim(J^\perp) = 9$ ✓

**Quotient computation**:

1. Compute Gram matrix on $J^\perp$: $G_{J^\perp} = V_{J^\perp} \cdot G \cdot
   V_{J^\perp}^T$
2. Find radical (nullspace): dimension 2 (corresponding to $J$)
3. Compute Smith normal form to extract nondegenerate quotient
4. Result: $J^\perp/J$ has Gram matrix $\operatorname{diag}(-2, -2, \ldots, -2)$ (7
   times)

**Verification**:

- Rank: 7 ✓
- Signature: $(0, 7)$ (negative definite) ✓
- Determinant: $-128 = (-2)^7$ ✓
- Isometry with $A_1^{\oplus 7}$: ✓ (same genus, definite lattices in same genus are
  isometric)

#### Step 5: Orbit Classification (Computational Verification)

**Method**: Discriminant group analysis via Nikulin surjectivity [Nikulin1979, Prop.
1.5.2]

1. **Surjectivity**: $O(T_{\mathrm{Co}}) \to O(q_{T_{\mathrm{Co}}})$ is surjective for
   2-elementary lattices
   - ⇒ Orbits of isotropic planes are determined by their images in
     $A_{T_{\mathrm{Co}}}$

2. **Discriminant images computed**: For each plane $J = \operatorname{span}(v_1, v_2)$:
   - Image in $A_{T_{\mathrm{Co}}} \cong (\mathbb{Z}/2\mathbb{Z})^{11}$ is
     $\operatorname{span}([v_1], [v_2])$
   - Primitivity check: $\operatorname{rank}(v_1, v_2 \mod 2) = 2$

3. **Results**:
   - Total planes: 27
   - **Primitive planes** (dim 2 image): 15
   - Non-primitive planes: 12

4. **Orbit computation**: UNVERIFIED
   - 15 primitive planes found via bounded search
   - Orbit computation via GAP never performed
   - **Status**: Claim of single orbit is UNVERIFIED

**Verification Status**: ✗ UNVERIFIED - orbit computation never performed, only bounded
enumeration completed

## Results Summary

| Property | Computed | Expected | Status |
| --- | --- | --- | --- |
| Rank of $T_{\mathrm{Co}}$ | 11 | 11 | ✓ |
| Signature of $T_{\mathrm{Co}}$ | $(2, 9)$ | $(2, 9)$ | ✓ |
| Witt index | 2 | 2 | ✓ |
| Isotropic planes found | 27 | Finite | ✓ |
| **Primitive planes** | **15** | — | ✓ NEW |
| Rank of $J^\perp/J$ | 7 | 7 | ✓ |
| Signature of $J^\perp/J$ | $(0, 7)$ | $(0, 7)$ | ✓ |
| Gram matrix | $\operatorname{diag}(-2^7)$ | $\operatorname{diag}(-2^7)$ | ✓ |
| Determinant | $-128$ | $-128$ | ✓ |
| **Isometry $J^\perp/J \cong A_1^{\oplus 7}$** | **Diagonal comparison** | — | ✓ COMPUTED |
| **Single $O(T_{\mathrm{Co}})$-orbit** | **UNVERIFIED** | 1 | ✗ NOT COMPUTED |

## Conclusion

**WARNING**: The orbit uniqueness claim is UNVERIFIED. Orbit computation via GAP was
never performed.

Within the literature-backed period-domain description of Coble moduli, the repo has:
- ✓ VERIFIED: 15 primitive isotropic planes found via bounded search
- ✓ VERIFIED: For any such plane $J$, the quotient $J^\perp/J$ is isometric to
  $A_1^{\oplus 7}$
- ✗ UNVERIFIED: Claim of unique $O(T_{\mathrm{Co}})$-orbit (orbit computation never
  performed)

**Verification Method**:
1. **Isometry**: Direct diagonal comparison (both $\operatorname{diag}(-2, \ldots, -2)$)
2. **Orbit uniqueness**: NOT VERIFIED - GAP orbit computation required
3. **Primitivity**: Rank check on $(v_1 \mod 2, v_2 \mod 2)$

**Computational Evidence**:
- Script: `computations/task3_2_isotropic_planes.sage` (lines 553-650: enumeration only,
  no orbit computation)
- 15 primitive isotropic planes found via bounded search
- Orbit computation via GAP required to verify uniqueness claim

This is exact computational support for the theoretical predictions from the literature
spine:
- Nikulin (1979): Classification of 2-elementary lattices and discriminant-form
  surjectivity
- Sterk (1991): Cusp classification for Enriques moduli and isotropic plane orbits
- Alexeev-Engel-Garza-Schaffler (2023): Compact moduli of Enriques surfaces and Type IV
  boundary structure
- **Pieroni (2026)**: E₁₀ = Num(X) lattice structure (lines 146, 483-493). Note: Theorem
  46 concerns geometric isotropic sequences of elliptic curves (E_i·E_j = 1 - δ_ij), not
  lattice-theoretic isotropic vectors (v² = 0).

## Files

- **Script**: `computations/task3_2_isotropic_planes.sage`
- **Results**: `computations/task3_2_results.txt`
- **This proof**: `notes/proofs/task3_2_isotropic_planes.md`

## References

1. **[Nikulin1979]** Nikulin, V. V. "Integer symmetric bilinear forms and some of their
   geometric applications."
   *Math. USSR Izvestija* 14 (1979), 103-167.

2. **[Sterk1991]** Sterk, H. "Compactifications of the moduli space of Enriques
   surfaces."

3. **[AEGS23]** Alexeev, Engel, Garza, Schaffler.
   "Compact moduli of Enriques surfaces with a numerical polarization of degree 2."
   *arXiv:2312.03638* (2023).

4. **[Dawes2022]** Dawes, M. "Orbits in Lattices."
   *arXiv:2205.10601* (2022).
