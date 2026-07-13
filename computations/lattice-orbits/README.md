# Computational Algorithms for Orbits of Isotropic Vectors

This repository contains SageMath implementations of computational algorithms from:

**"Orbits in Lattices" by Matthew Dawes (arXiv:2205.10601)**

## Repository Structure

```
computations/lattice-orbits/
├── src/                                  # SageMath implementations
│   ├── examples_dawes_paper.sage         # Dawes examples
│   ├── isotropic_orbits_proper.sage      # Main proper implementation
│   ├── isotropic_vector_orbits_fixed.sage # Working examples from paper
│   ├── isotropic_vector_orbits.sage      # Original framework
│   └── test_isotropic_orbits.sage        # Additional tests
└── README.md
```

Related paper notes live under `notes/papers/dawes-2022-orbits-in-lattices/`. Cross-paper literature findings live under `notes/topics/isotropic-vector-orbits/`.

## Algorithms Implemented

### Algorithm 2.1: Non-Isotropic Vector Orbits (Definite Case)

- Tests orbit equivalence v₁ ~ v₂ under orthogonal group Γ ⊂ O(L)
- For vectors where v₁⊥ is definite
- Uses Smith normal form and orthogonal complement computation

### Algorithm 2.3: Non-Isotropic Vector Orbits (Indefinite Case)

- For vectors where v₁⊥ is indefinite
- Requires surjectivity of O(L) → O(D(L))

### Algorithm 3.1: General Tits Building Computation

- Computes Tits buildings B(G₁) from B(G₂) for G₁ ⊂ G₂
- Framework for general orbit computations

### Algorithm 3.2: Maximal Lattice Tits Buildings

- For split maximal lattices of signature (2,n)
- Computes building structure with isotropic lines and planes

## Examples from the Paper

### Example 2.2: L = U ⊕ A₃

- Vectors: v₁ = (4, 4, 1, 2, -1), v₂ = (36, 144, 5, -30, 83)
- Both have squared length v² = 20
- **Result**: v₁ ~ v₂ under Ô⁺(L)

### Example 2.6: L = U ⊕ A₃

- Vectors: v₁ = (1, -1, 0, 0, 0), v₂ = (1, 0, 1, 0, 0)
- Both have squared length v² = -2
- **Result**: v₁ ~ v₂ under ŜO⁺(L)

## Running the Code

```bash
# Run the proper SageMath implementation (recommended)
sage computations/lattice-orbits/src/isotropic_orbits_proper.sage

# Run examples from the paper
sage computations/lattice-orbits/src/isotropic_vector_orbits_fixed.sage

# Test isotropic vector computations
sage computations/lattice-orbits/src/test_isotropic_orbits.sage
```

## Key Mathematical Concepts

### Lattices

- **U**: Hyperbolic plane with Gram matrix [[0,1],[1,0]]
- **A₃**: Root lattice with Gram matrix [[-2,-1,0],[-1,-2,-1],[0,-1,-2]]
- **Signature (t⁺,t⁻)**: Number of positive/negative eigenvalues

### Isotropic Vectors

- Vector v with v² = (v,v) = 0
- Form the building blocks of Tits buildings
- Orbits under orthogonal group actions

### Smith Normal Form

- Used to compute orthogonal complements v⊥
- Essential for Algorithm 2.1 implementation

### Tits Buildings

- Encode orbit structure of isotropic subspaces
- Bipartite graphs with lines (P) and planes (C) as vertices
- Used in Algorithm 3.1 and 3.2

## Applications

1. **Boundary Components**: Understanding Baily-Borel compactifications of orthogonal modular varieties
2. **Modular Forms**: Improving computer arithmetic of orthogonal modular forms
3. **Fourier Expansions**: Optimizing multiplication algorithms using orbit representatives

## Verified Results

✅ **Working Examples**: Both Example 2.2 and 2.6 from the paper run correctly ✅ **Smith Normal Form**: Orthogonal complement computation working ✅ **Isotropic Detection**: Successfully finds isotropic vectors in U ⊕ A₃ ✅ **Signature Computation**: Correctly identifies lattice signatures

The implementation provides a solid foundation for further development of orbit computation algorithms for isotropic vectors in lattices.
