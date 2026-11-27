## Conjugacy classes of parabolic subgroups via isotropic orbit classification

**Source:** Lee 2022 (isotropic-orbits.pdf from Farb's course page)

### Main result

**Theorem:** There are exactly **two conjugacy classes** of maximal parabolic subgroups of O⁺(1,9)(Z).

**Equivalently:** Two O(Λ^⊥)-orbits of primitive isotropic vectors/planes in Λ^⊥ where Λ = ℤ{H} ⊂ ℤ^{1,9}.

### Setup

**Lattice:** ℤ^{1,9} = ℤ{H, e₁,...,e₉} with symmetric bilinear form Q of type (1,9):
```
Q = diag(1, -1, -1, ..., -1)
```

**Sublattice:** Λ = ℤ{H} (rank 1, isotropic)

**Quotient:** Λ^⊥/Λ (signature (1,9))

### Proof technique: Splitting and unimodularity

**Key observation:** Any primitive isotropic w ∈ ℤ^{10} lies in a copy of the hyperbolic plane U ≅ (1) ⊕ (-1).

**Splitting:** Since U is unimodular, it splits off: ℤ^{10} = U ⊕ U^⊥

**Signature calculation:** U^⊥ has signature (0,8)

**Classification:** L^⊥ is even, indefinite, odd → L^⊥ ≅ (1) ⊕ (-1)

**Restriction to L^⊥:** Even, negative definite, rank 8 → **L^⊥ ≅ -E₈** (unique such lattice)

**Conclusion:** All primitive isotropic vectors in ℤ^{10} are O(ℤ^{10})-conjugate.

### Connection to parabolic subgroups

**Maximal parabolic:** Stabilizer of a primitive isotropic vector

**Two conjugacy classes:** Correspond to the two "types" of isotropic vectors (related to the two orbits mentioned in the theorem statement)

**To clarify:** The paper title says "two conjugacy classes" but the proof shows unique orbit of isotropic vectors. Need to reconcile this.

### Test fixture targets

- [ ] Implement ℤ^{1,9} with Q = diag(1,-1,...,-1)
- [ ] Verify any primitive isotropic w lies in a copy of U
- [ ] Compute splitting ℤ^{10} = U ⊕ U^⊥ for given w
- [ ] Verify U^⊥ has signature (0,8)
- [ ] Compute L^⊥ for L = ℤ{w}, verify L^⊥ ≅ -E₈
- [ ] Enumerate primitive isotropic vectors up to O(ℤ^{10})-action
- [ ] Verify there is exactly one orbit (or two, depending on interpretation)
- [ ] Compute stabilizers (maximal parabolic subgroups)
- [ ] Verify two conjugacy classes of maximal parabolics

### Research directions

- **Clarification:** Reconcile "two conjugacy classes" with "unique orbit" — are these counting different things?
- **Generalization:** Does this extend to ℤ^{1,n} for other n? What is the orbit count?
- **Comparison with Alexeev-Liu-Schütt:** They also use unimodularity to collapse orbits for Π_{1,9} ≅ U ⊕ E₈. Is this the same lattice?
- **Tits building:** How does this orbit classification relate to the Tits building of O⁺(1,9)(Z)?
- **Parabolic classification:** Can we explicitly describe the two maximal parabolic subgroups?

### Proof technique: Unimodularity shortcut

**General principle:** If a primitive isotropic vector v lies in a unimodular sublattice U, then U splits off, and the quotient is determined by signature.

**Classification of unimodular lattices:** Even unimodular lattices of given signature are unique (up to isometry).

**Application:** Collapses orbit count without explicit enumeration.

**Comparison:** Same technique as Alexeev-Liu-Schütt 2025 for Π_{1,9}.

### Connection to Dawes 2022

**Dawes' algorithms:** Compute orbits explicitly via coset enumeration.

**Lee's shortcut:** Uses unimodularity to avoid explicit computation.

**Trade-off:** Lee's method only works for special lattices (with unimodular sublattices); Dawes' method is general.

### Minimal example for testing

**Simplest case:** ℤ^{1,1} = U (hyperbolic plane)
- Primitive isotropic vectors: {(1,0), (0,1), (1,1), (1,-1), ...}
- All O(U)-conjugate (unique orbit)
- Stabilizer = parabolic subgroup

**Next case:** ℤ^{1,2} = U ⊕ ⟨-1⟩
- Primitive isotropic vectors: lie in U summand
- Unique orbit (by unimodularity of U)

**Lee's case:** ℤ^{1,9} = U ⊕ (-E₈)
- Same argument: unique orbit of primitive isotropic vectors
