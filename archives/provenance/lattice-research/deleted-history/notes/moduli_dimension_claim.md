# Moduli Dimension Claim: 9-Dimensional Period Domain for Coble Surfaces

This note records the standard literature-backed moduli dimension claim that the repo
uses throughout its computational verification work.

## The Standard Claim

For a Coble surface (the quotient of a K3 surface by a fixed-point-free involution
arising from a 10-nodal rational sextic), the associated period domain has complex
dimension 9.

More precisely:
- The transcendental lattice $T_{\mathrm{Co}}$ of a Coble surface has signature $(2,9)$
  and rank 11
- The Type IV period domain for K3 surfaces with this lattice structure is a
  9-dimensional complex manifold
- The moduli space of Coble surfaces (with appropriate polarization data) is described
  via this period domain and its Baily-Borel compactification

## Literature Attribution

This is a standard fact from the period-domain theory of K3 and Enriques surfaces, not a
new repo theorem.

### Canonical Sources

1. **Scattone (1987)**: *On the Compactification of Moduli Spaces for Algebraic K3
   Surfaces*
   - Provides the Type IV period-domain and Baily-Borel compactification framework on
     the K3 side
   - Establishes the dimension count from the lattice signature

2. **Sterk (1991)**: *Compactifications of the period space of Enriques surfaces.
   I*
   - Develops the Enriques-side period-space and cusp framework
   - Connects isotropic plane orbits to boundary structure

3. **Dolgachev & Kondō (2013)**: *The rationality of the moduli spaces of Coble surfaces
   and of nodal Enriques surfaces*
   - Provides the moduli-theoretic Coble/Enriques picture
   - Establishes rationality statements and the standard period-domain framing

4. **Friedman (1984)**: *A New Proof of the Global Torelli Theorem for K3 Surfaces*
   - Standard reference for the Torelli step (passing from lattice/period data to
     moduli)

### The Claim Flow

1. **Lattice setup** (Coble 1917, 1929; Nikulin 1979): The transcendental lattice
   $T_{\mathrm{Co}}$ has signature $(2,9)$
2. **Period domain** (Scattone 1987): A lattice with signature $(2,9)$ yields a Type IV
   period domain of complex dimension 9
3. **Moduli description** (Dolgachev-Kondō 2013, Sterk 1991): The Coble moduli space is
   described via this period domain
4. **Torelli** (Friedman 1984): The passage from period data to moduli is standard
   global Torelli

## Repo-Facing Consequence

**Use the literature above for the ambient moduli dimension claim.**

The repo's computational role is NOT to rediscover or reprove the 9-dimensional count.
Instead, repo computations:
- Produce exact worked examples of Coble surfaces inside this standard period-domain
  picture
- Verify lattice-theoretic predictions (e.g., isotropic plane orbits, stabilizer
  computations)
- Support the standard moduli description with explicit numerical evidence

**When citing this claim in repo prose:**
- State clearly that the 9-dimensional period domain is a standard literature fact
- Cite Scattone (1987), Sterk (1991), Dolgachev-Kondō (2013) as the canonical source
  chain
- Mark any repo computation as "supporting evidence" or "exact verification" within that
  framework, not as the primary justification

## Cross-References

- `REFERENCES.md`: Full bibliographic details for canonical sources
- `notes/literature_claim_map.md`: Standard claim flow for Coble surfaces, K3 covers,
  and period domains
- `notes/proofs/task3_2_isotropic_planes.md`: Computational verification of isotropic
  plane orbits within the period-domain framework
- `notes/proofs/task6_1_slc_stability.md`: Computational verification of slc stability
  within the KSBA/compactification framework
