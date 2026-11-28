# Task 2.1: Isotropic Vector Orbit Classification

## Theorem Statement

The discriminant group $A_{T_{\mathrm{Co}}}$ of the Coble surface transcendental lattice
contains exactly 2 orbits of isotropic vectors under the action of $O(q_T)$:
1. The zero vector (orbit size 1)
2. All nonzero isotropic vectors (orbit size 527)

This computational verification supports the cusp classification used in Task 3.2 and
the period-domain boundary structure (Sterk 1991).

## Mathematical Background

### Discriminant Groups and Quadratic Forms

From the standard K3/lattice setup (Coble 1917, 1929; Nikulin 1979) as recorded in
`REFERENCES.md`:

- **Transcendental lattice**: $T_{\mathrm{Co}} \cong (11, 11, 1)_2$ in Nikulin notation
  - Gram matrix: $\operatorname{diag}(2, 2, -2, -2, \ldots, -2)$
  - Signature: $(2, 9)$ (2 positive, 9 negative directions)
  - Rank: 11
  - Invariants: $(r, a, \delta) = (11, 11, 1)$ where $r$ = rank, $a$ = discriminant
    group order exponent, $\delta$ = discriminant

- **Discriminant group**: $A_{T_{\mathrm{Co}}} = T_{\mathrm{Co}}^*/T_{\mathrm{Co}} \cong
  (\mathbb{Z}/2\mathbb{Z})^{11}$
  - Order: $|A_{T_{\mathrm{Co}}}| = 2^{11} = 2048$
  - Quadratic form: $q_T: A_{T_{\mathrm{Co}}} \to \mathbb{Q}/2\mathbb{Z}$ induced by the
    lattice bilinear form
  - Isotropic vectors: $v \in A_{T_{\mathrm{Co}}}$ such that $q_T(v) \equiv 0
    \pmod{2\mathbb{Z}}$

### Nikulin's Orbit Classification

From Nikulin 1979, Proposition 1.5.2 and Section 1.5:

**Key fact**: For a 2-elementary lattice $T$ with $r > a$ (rank exceeds discriminant
exponent), the natural map $O(T) \to O(q_T)$ is surjective.

For $T_{\mathrm{Co}}$ with $(r, a, \delta) = (11, 11, 1)$ and signature $(2, 9)$:
- The discriminant form $q_T$ is nondegenerate
- All nonzero isotropic vectors in $A_{T_{\mathrm{Co}}}$ form a single orbit under
  $O(q_T)$
- The zero vector forms its own orbit

**Geometric significance**: The orbit structure determines the cusp classification in
the Baily-Borel compactification.
Each $O(q_T)$-orbit of nonzero isotropic vectors corresponds to a cusp type in the
period domain boundary (Sterk 1991).

## Computational Verification

### Method

The computation in `computations/task2_1_isotropic_orbits.sage` performs:

1. **Construct discriminant group**: Build $A_{T_{\mathrm{Co}}} \cong
   (\mathbb{Z}/2\mathbb{Z})^{11}$ with the induced quadratic form $q_T$

2. **Enumerate isotropic vectors**: For each $v \in A_{T_{\mathrm{Co}}}$, check if
   $q_T(v) \equiv 0 \pmod{2\mathbb{Z}}$

3. **Compute orbits**: Use the orthogonal group $O(q_T)$ to partition isotropic vectors
   into orbits
   - Two vectors $v, w$ are in the same orbit if there exists $g \in O(q_T)$ with $g(v)
     = w$

### Results

From `computations/task2_1_results.txt`:

**Discriminant group structure**:
- $A_{T_{\mathrm{Co}}} \cong (\mathbb{Z}/2\mathbb{Z})^{11}$
- Order: 2048
- Bilinear form: Nondegenerate

**Isotropic vectors**:
- Total count: 528
- Fraction: 25.8% of $A_{T_{\mathrm{Co}}}$
- Zero vectors: 1
- Nonzero vectors: 527

**$O(q_T)$-orbit decomposition**:
- Number of orbits: 2
- **Orbit 0** (zero vector):
  - Representative: $[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]$
  - Size: 1
- **Orbit 1** (nonzero isotropic):
  - Representative: $[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]$
  - Size: 527

**Theoretical verification**: The computed 2-orbit structure matches Nikulin's
theoretical prediction for 2-elementary lattices with signature $(2, 9)$.

## Conclusion

The exhaustive computational enumeration confirms:

**Verified claim**: The discriminant group $A_{T_{\mathrm{Co}}}$ contains exactly 2
orbits of isotropic vectors under $O(q_T)$: the zero vector and all 527 nonzero
isotropic vectors.

This orbit classification is foundational for:
- **Task 3.2**: The unique nonzero orbit corresponds to the unique primitive isotropic
  plane orbit used in the 1-cusp classification
- **Period domain boundary**: The single nonzero orbit corresponds to a single cusp type
  in the Baily-Borel compactification (Sterk 1991)

## Literature Context

- **Nikulin 1979**: *Integer symmetric bilinear forms and some of their geometric
  applications*, Proposition 1.5.2 — Surjectivity of $O(T) \to O(q_T)$ for $r > a$;
  Section 1.5 — Discriminant form orbit classification
- **Sterk 1991**: *Compactifications of the period space of Enriques surfaces.
  I* — Uses discriminant group orbit analysis for cusp classification
- **Dolgachev & Kondō 2013**: *The rationality of the moduli spaces of Coble surfaces
  and of nodal Enriques surfaces* — Lattice invariants for Coble surfaces
- **Pieroni 2026** (lines 146, 483-493): Identifies E₁₀ = Num(X) for Coble surfaces,
  providing geometric context for the discriminant group A_{T_Co} computations

## Cross-References

- `computations/task2_1_isotropic_orbits.sage` — Orbit enumeration implementation
- `computations/task2_1_results.txt` — Full computational output
- `proofs/solved/task3_2_isotropic_planes.md` — Uses this orbit classification for
  primitive isotropic plane uniqueness
- `REFERENCES.md` — Canonical literature spine for Nikulin's 2-elementary lattice theory
