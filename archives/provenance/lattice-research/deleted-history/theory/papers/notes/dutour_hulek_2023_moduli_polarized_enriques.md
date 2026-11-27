## Computational classification of moduli of polarized Enriques surfaces

**Source:** Dutour Sikirić & Hulek 2023 (arXiv:2302.01679)

### Main result

**Theorem:** There are, up to isomorphism, only finitely many different moduli spaces of polarized Enriques surfaces (Gritsenko-Hulek).

**This paper:** Computational investigation of the structure, using GAP for group-theoretic calculations.

### Lattice setup

**M(1/2) = U ⊕ E₈(-1):** Explicit Gram matrix and Z-basis provided

**Fundamental domain:** Computed as a basic cone

**Generators:** Define a Z-basis of U ⊕ E₈(-1), verify it's a basic cone

### Computational method

**Step 1:** Generate 1022 potential subgroups Γ_h⁺

**Step 2:** Represent as permutation groups acting on 2¹⁰ elements

**Step 3:** Compute invariants to check conjugacy:
- **Level 1 invariants:** Order, orbit sizes
- **For groups <1000 elements:** All subgroups and their level 1 invariants

**Step 4:** Reduce 1022 → **87 conjugacy classes** using GAP

### Lattice I with det(I)=3

**Explicit construction:** Vectors E_i with Gram matrix provided

**Verification:** det(I) = 3 by direct computation

**Application:** Related to specific moduli space component

### Test fixture targets

- [ ] Implement M(1/2) = U ⊕ E₈(-1) with explicit Gram matrix from paper
- [ ] Verify the given Z-basis is correct
- [ ] Compute fundamental domain, verify it's a basic cone
- [ ] Implement lattice I, verify det(I) = 3
- [ ] Compute Gram matrix of vectors E_i
- [ ] Generate 1022 potential subgroups Γ_h⁺ (reproduce paper's enumeration)
- [ ] Implement level 1 invariants: order, orbit sizes
- [ ] For small groups: compute all subgroups
- [ ] Use GAP to check conjugacy, reduce to 87 classes
- [ ] Verify 87 representatives match paper's classification

### Research directions

- **Algorithmic complexity:** What is the bottleneck in the 1022 → 87 reduction?
- **Invariant hierarchy:** Are level 1 invariants sufficient, or are higher-level invariants needed?
- **Generalization:** Can this method extend to other moduli spaces (K3, abelian varieties)?
- **Explicit representatives:** Can we write down explicit Gram matrices for all 87 classes?
- **Moduli dimension:** For each of 87 classes, what is the dimension of the moduli space?
- **Comparison with Gritsenko-Hulek:** How does the computational classification match the theoretical finiteness result?

### GAP integration

**Permutation group representation:** 2¹⁰ = 1024 elements

**Conjugacy checking:** GAP's built-in algorithms for permutation groups

**Subgroup lattice:** For groups <1000 elements, compute full subgroup lattice

**Practical consideration:** Need to compute suitable invariants to make conjugacy check tractable

### Connection to other work

**Gritsenko-Hulek:** Theoretical finiteness result

**This paper:** Explicit computational realization

**Alexeev-Engel-Garza-Schaffler 2023:** Compact moduli of Enriques surfaces with numerical polarization

### Proof technique: Invariant-based conjugacy

**Challenge:** 1022 subgroups is too many to check pairwise conjugacy naively

**Solution:** Compute invariants (order, orbit structure, subgroup lattice) to partition into equivalence classes

**GAP's role:** Efficient algorithms for permutation group conjugacy

**Key insight:** Level 1 invariants (order, orbit sizes) are often sufficient to distinguish conjugacy classes

### Explicit Gram matrices

**M(1/2):** Provided in paper (Section 2)

**Lattice I:** Gram matrix of E_i vectors (Section 4)

**Verification:** Straightforward computation shows det(I) = 3

**To extract:** Full Gram matrices for all 87 conjugacy class representatives
