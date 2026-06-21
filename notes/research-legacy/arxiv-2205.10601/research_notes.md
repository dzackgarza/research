# Research Notes: "Orbits in Lattices" by Matthew Dawes

**arXiv ID**: 2205.10601  
**Title**: Orbits in Lattices  
**Author**: Matthew Dawes  
**URL**: https://arxiv.org/abs/2205.10601

## Abstract

This paper presents computational algorithms for determining orbit equivalence of vectors in integral lattices under orthogonal group actions. The work focuses on isotropic vectors and their role in constructing Tits buildings, with applications to boundary components of orthogonal modular varieties.

## Key Algorithms Extracted

### Algorithm 2.1: Non-Isotropic Vector Orbits (Definite Case)
- **Purpose**: Test orbit equivalence v₁ ~ v₂ under orthogonal group Γ ⊂ O(L)
- **Condition**: For vectors where v₁⊥ is definite
- **Method**: Uses Smith normal form and orthogonal complement computation
- **Implementation**: `src/isotropic_orbits_proper.sage:algorithm_2_1_detailed()`

### Algorithm 2.3: Non-Isotropic Vector Orbits (Indefinite Case)  
- **Purpose**: For vectors where v₁⊥ is indefinite
- **Requirement**: Surjectivity of O(L) → O(D(L))
- **Status**: Framework provided, full implementation requires advanced lattice theory

### Algorithm 3.1: General Tits Building Computation
- **Purpose**: Computes Tits buildings B(G₁) from B(G₂) for G₁ ⊂ G₂
- **Application**: Framework for general orbit computations
- **Status**: Theoretical framework, requires specialized implementation

### Algorithm 3.2: Maximal Lattice Tits Buildings
- **Purpose**: For split maximal lattices of signature (2,n)
- **Output**: Building structure with isotropic lines and planes
- **Implementation**: Partial in `src/isotropic_vector_orbits.sage:algorithm_3_2_tits_building_maximal()`

## Examples Implemented

### Example 2.2: L = U ⊕ A₃
- **Lattice**: U (hyperbolic plane) ⊕ A₃ (root lattice)
- **Vectors**: v₁ = (4, 4, 1, 2, -1), v₂ = (36, 144, 5, -30, 83)
- **Property**: Both have squared length v² = 20
- **Paper Result**: v₁ ~ v₂ under Ô⁺(L)
- **Implementation Result**: v₁ ≁ v₂ (different determinants of orthogonal complements)
- **Note**: Discrepancy may be due to simplified isometry testing

### Example 2.6: L = U ⊕ A₃  
- **Vectors**: v₁ = (1, -1, 0, 0, 0), v₂ = (1, 0, 1, 0, 0)
- **Property**: Both have squared length v² = -2
- **Paper Result**: v₁ ~ v₂ under ŜO⁺(L)
- **Implementation Result**: ✅ v₁ ~ v₂ (matching paper)

## Mathematical Concepts

### Lattices
- **U**: Hyperbolic plane with Gram matrix [[0,1],[1,0]]
- **A₃**: Root lattice with Gram matrix [[-2,-1,0],[-1,-2,-1],[0,-1,-2]]
- **Signature (t⁺,t⁻)**: Number of positive/negative eigenvalues

### Isotropic Vectors
- **Definition**: Vector v with v² = (v,v) = 0
- **Role**: Form building blocks of Tits buildings
- **Orbits**: Under orthogonal group actions O(L), SO(L), O⁺(L), SO⁺(L)

### Smith Normal Form
- **Usage**: Compute orthogonal complements v⊥
- **Implementation**: Essential for Algorithm 2.1
- **Verification**: All inner products (v, k_i) = 0 confirmed

### Tits Buildings
- **Structure**: Bipartite graphs with isotropic lines (P) and planes (C) as vertices
- **Purpose**: Encode orbit structure of isotropic subspaces
- **Algorithms**: 3.1 (general) and 3.2 (maximal lattices)

## Applications

1. **Boundary Components**: Understanding Baily-Borel compactifications of orthogonal modular varieties
2. **Modular Forms**: Improving computer arithmetic of orthogonal modular forms  
3. **Fourier Expansions**: Optimizing multiplication algorithms using orbit representatives

## Implementation Status

### ✅ Working Components
- Proper SageMath infrastructure using `IntegralLattice` class
- Smith normal form computation for orthogonal complements
- Isotropic vector detection (found 212 in U ⊕ A₃)
- Signature computation for lattices
- Examples 2.6 verification

### 🔄 Partial Implementation
- Algorithm 2.1 (basic version working, needs improved isometry testing)
- Tits building construction (framework provided)

### ❌ Missing Components
- Full Algorithm 2.3 for indefinite case
- Complete Algorithm 3.1 general implementation
- Advanced lattice isometry testing

## Files Structure

```
src/
├── isotropic_orbits_proper.sage      # Main proper implementation
├── isotropic_vector_orbits_fixed.sage # Working examples from paper
├── isotropic_vector_orbits.sage       # Original framework
└── test_isotropic_orbits.sage         # Additional tests

docs/arxiv-2205.10601/
└── research_notes.md                  # This file
```

## Future Work

1. **Implement sophisticated isometry testing** for Algorithm 2.1
2. **Complete Algorithm 2.3** for indefinite orthogonal complements
3. **Full Tits building algorithms** 3.1 and 3.2
4. **Performance optimization** for large lattices
5. **Extended examples** from other sections of the paper