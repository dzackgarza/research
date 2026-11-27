# Task 5.1: Involution Construction on Glued Lattice Model

## Theorem Statement

There exists an explicit even unimodular lattice $\Lambda$ of signature $(3,19)$ with a
primitive orthogonal decomposition $\Lambda = S_{\mathrm{Co}} \oplus T$ and an
involution $\theta \in O(\Lambda)$ such that:
- $\theta$ acts by $-I$ on $S_{\mathrm{Co}}$
- $\theta$ acts by $+I$ on $T$
- $\theta^2 = I$ (involution property)
- $\theta^T G \theta = G$ (isometry property)

This computational verification establishes the existence of the sign involution on an
explicit glued K3 lattice model.

## Mathematical Background

### K3 Lattices and Involutions

From the standard K3/lattice setup (Coble 1917, 1929; Nikulin 1979) as recorded in
`REFERENCES.md`:

- **K3 lattice**: $\Lambda_{K3} \cong U^{\oplus 3} \oplus E_8(-1)^{\oplus 2}$ is the
  unique even unimodular lattice of signature $(3,19)$
- **Coble surface decomposition**: For a Coble surface, $\Lambda_{K3} = S_{\mathrm{Co}}
  \oplus T_{\mathrm{Co}}$ where:
  - $S_{\mathrm{Co}} \cong (1, 10)_2$ is the Picard lattice (signature $(1,10)$,
    discriminant $2^{11}$)
  - $T_{\mathrm{Co}} \cong (11, 11, 1)_2$ is the transcendental lattice (signature
    $(2,9)$, discriminant $-2^{11}$)
- **Involution**: The covering involution $\theta: X \to X$ on the K3 surface induces an
  involution $\theta \in O(\Lambda_{K3})$ with eigenspace decomposition matching the
  Picard/transcendental split

### Primitive Embeddings and Orthogonal Complements

From Nikulin 1979, Section 1.5:

**Key fact**: For a primitive embedding $S \hookrightarrow \Lambda$ of a lattice $S$
into an even unimodular lattice $\Lambda$, the orthogonal complement $T = S^\perp$
satisfies:
- $\Lambda = S \oplus T$ (orthogonal direct sum)
- $T$ is primitive in $\Lambda$
- $|A_S| \cdot |A_T| = |\det(S)| \cdot |\det(T)|$ (discriminant compatibility)
- $q_S \oplus q_T \cong 0$ in the discriminant form (Brown invariant condition)

## Computational Verification

### Method

The computation in `computations/task5_1_involution.sage` implements the corrected route
documented in `notes/task5_1_route_reset.md`:

1. **Construct glued K3 lattice model**: Build explicit even unimodular lattice
   $\Lambda$ of signature $(3,19)$ by gluing $S_{\mathrm{Co}}$ and
   $T_{\mathrm{expected}}$

2. **Primitive embedding**: Embed $S_{\mathrm{Co}} \cong (1,10)_2$ primitively into
   $\Lambda$
   - Target Gram matrix: $\operatorname{diag}(2, -2, -2, \ldots, -2)$
   - Verify primitivity via Smith normal form

3. **Compute orthogonal complement**: Calculate $T = S_{\mathrm{Co}}^\perp$ as the true
   orthogonal complement
   - Verify zero cross-pairing: $\langle S_{\mathrm{Co}}, T \rangle = 0$
   - Check signature, determinant, discriminant group

4. **Define involution**: Construct $\theta$ from the primitive decomposition
   - $\theta|*{S*{\mathrm{Co}}} = -I$ (sign flip on Picard lattice)
   - $\theta|_T = +I$ (identity on complement)
   - Verify integrality, involution property, isometry property

### Results

From `computations/task5_1_primitive_results.txt` and
`computations/task5_1_theta_output.txt`:

**Ambient lattice**:
- Rank: 22
- Signature: $(3, 19)$
- Determinant: $-1$
- Even: True

**Embedded $S_{\mathrm{Co}}$**:
- Primitive: True
- Gram diagonal: $[2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]$
- Signature: $(1, 10)$
- Determinant: $2048 = 2^{11}$

**Computed orthogonal complement $T$**:
- Rank: 11
- Signature: $(2, 9)$
- Determinant: $-2048 = -2^{11}$
- Cross pairing zero: True
- Discriminant group: $A_T \cong (\mathbb{Z}/2\mathbb{Z})^{11}$, order $2048$
- Brown invariant: $\text{Brown}(q_T) = 1 = -\text{Brown}(q_S) \pmod{8}$ ✓

**Involution $\theta$**:
- Integral in ambient basis: True
- $\theta^2 = I$: True ✓
- $\theta^T G \theta = G$: True ✓
- $\theta$ acts by $-I$ on embedded $S_{\mathrm{Co}}$: True ✓
- $\theta$ acts by $+I$ on computed complement $T$: True ✓

**Verification status**: PASS — exact theta verification succeeded on the glued ambient
lattice.

## Conclusion

The exhaustive computational construction confirms:

**Verified claim**: There exists an explicit glued K3 lattice model with a primitive
orthogonal decomposition $\Lambda = S_{\mathrm{Co}} \oplus T$ and a sign involution
$\theta \in O(\Lambda)$ satisfying all required properties (integrality, involution,
isometry, eigenspace decomposition).

This resolves the Task 5.1 lattice construction blocker via the corrected
primitive-embedding route documented in `notes/task5_1_route_reset.md`.

## Scope and Limitations

As documented in `notes/task5_1_exact_involution_note.md`, this computational
verification establishes:

**What is verified**:
- Existence of the sign involution on an explicit glued lattice model
- Primitive embedding of $S_{\mathrm{Co}}$ with correct Gram matrix
- Orthogonal complement with correct signature, determinant, discriminant group
- Integrality and isometry properties of $\theta$

**What is not claimed**:
- This computation alone does not prove the full geometric interpretation for Coble
  surfaces
- The broader period-domain, Torelli, and moduli layer requires literature citations
  (Dolgachev-Kondō 2013, Sterk 1991, Scattone 1987)
- The identification of the computed complement with the geometric $T_{\mathrm{Co}}$
  beyond this explicit model requires additional geometric arguments

## Literature Context

- **Nikulin 1979**: *Integer symmetric bilinear forms and some of their geometric
  applications*, Section 1.5 — Primitive embeddings, orthogonal complements,
  discriminant compatibility
- **Dolgachev & Kondō 2013**: *The rationality of the moduli spaces of Coble surfaces
  and of nodal Enriques surfaces* — Geometric interpretation of the involution and
  lattice decomposition
- **Sterk 1991**: *Compactifications of the period space of Enriques surfaces.
  I* — Period-domain framework for Enriques/Coble surfaces
- **Pieroni 2026** (Theorem 72, line 2068): Classification of involutions on Coble
  surfaces as lifts of Bertini involutions — provides geometric context for the sign
  involution constructed here

## Cross-References

- `computations/task5_1_involution.sage` — Glued lattice construction and involution
  verification
- `computations/task5_1_primitive_results.txt` — Primitive embedding verification output
- `computations/task5_1_theta_output.txt` — Involution verification output
- `notes/task5_1_exact_involution_note.md` — Canonical note documenting exact scope and
  limitations
- `notes/task5_1_route_reset.md` — Documents the corrected primitive-embedding route
- `REFERENCES.md` — Canonical literature spine for K3 lattices and primitive embeddings
