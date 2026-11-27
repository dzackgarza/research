## Algorithms for orbits in lattices and Tits' buildings

**Source:** Dawes 2022 (arXiv:2205.10601)

### Main results

**Algorithms 2.1, 2.2, 2.3:** Find orbits of vectors in L for certain subgroups of O(L)

**Algorithms 3.2, 3.4:** Calculate Tits' building of subgroups of O(L) when L has signature (2,n)

**Software:** GAP package available for computing Tits' buildings (§4 examples)

### Motivations

1. **Algebraic geometry:** Understand configuration of boundary components in Baily-Borel compactification of orthogonal modular varieties
2. **Computational:** Improve performance of computer arithmetic of orthogonal modular forms (e.g., Fourier expansions of Borcherds products)

### Basic lattice definitions

**Lattice L:** Even, non-degenerate integral quadratic form on free abelian group of finite rank

**Bilinear form:** (−,−)

**Gram matrix:** G(L) = ((xᵢ,xⱼ))ᵢ,ⱼ for Z-basis {xᵢ}

**Examples:**
- Root lattices: Aₙ, Dₙ, E₆, E₇, E₈ (negative definite)
- Rank 1 lattice: ⟨d⟩ with single element x where x² = d
- Hyperbolic plane U: Gram matrix `[[0,1],[1,0]]`

### Smith Normal Form

**For matrix A:** Exists P, Q ∈ GL_n(Z) such that PAQ = diag(d₁,...,dᵣ,0,...,0) where dᵢ|dᵢ₊₁

**Application:** Compute structure of discriminant group D(L) = L^∨/L from Gram matrix G(L)

### Orbit equivalence

**Definition:** v₁ ∼_Γ v₂ if ∃g ∈ Γ ⊂ O(L) such that gv₁ = v₂

**Algorithms 2.1-2.3:** Decide equivalence for non-isotropic vectors

**Section 3:** Handles isotropic case separately

### Boundary configuration of F_L(Γ)*

**Setup:** Γ ⊂ O(L), compute boundary components of Baily-Borel compactification

**Algorithms 3.1, 3.2, 3.4:** Calculate boundary configuration using orbit algorithms

### Test fixture targets

- [ ] Implement hyperbolic plane U with Gram = [[0,1],[1,0]]
- [ ] Implement root lattices A₂, D₄, E₆, E₇, E₈ with standard Gram matrices
- [ ] Implement Smith Normal Form algorithm for computing D(L)
- [ ] Implement Algorithm 2.1: orbit equivalence for non-isotropic vectors
- [ ] Implement Algorithm 2.2: (variant for specific subgroups)
- [ ] Implement Algorithm 2.3: (variant for specific subgroups)
- [ ] Implement Algorithm 3.2: Tits' building for signature (2,n)
- [ ] Implement Algorithm 3.4: (variant)
- [ ] Download and test GAP package for Tits' buildings
- [ ] Reproduce §4 examples from paper

### Research directions

- **Complexity analysis:** What is the time complexity of Algorithms 2.1-2.3 as a function of rank(L) and |Γ|?
- **Isotropic case:** Can the isotropic orbit algorithm be unified with the non-isotropic case?
- **Generalization:** Do these algorithms extend to hermitian lattices (cf. Brandhorst-Hofmann 2021 §6)?
- **Tits building structure:** Can the building be computed incrementally for large Γ?
- **Comparison with Vinberg:** How do these algorithms relate to Vinberg's algorithm for reflection groups?

### Connection to other work

- **Dawes 2016, 2021:** Applies these algorithms to specific modular varieties (boundary of F₂, generalized Kummer 4-folds)
- **Lee 2022:** Uses orbit classification for O⁺(1,9)(Z) to count parabolic subgroups
- **Brandhorst-Hofmann 2021:** Miranda-Morrison theory provides alternative for computing O(L) → O(D_L) image

### Proof technique: Lemma 2.1

**Key lemma:** (Contained but not proved in [reference])

**Application:** Proves correctness of Algorithms 2.1-2.3

**To investigate:** What is the precise statement of Lemma 2.1? Is it a standard result in lattice theory?

### Software availability

- **GAP package:** For Tits' buildings (author's implementation)
- **Integration:** Works with GAP, Sage, Magma
- **§4 examples:** Concrete calculations demonstrating the algorithms
