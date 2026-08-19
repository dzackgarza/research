<!--
Origin: gitclones/Coxeter/research/archive/2025-01-27-docs-restructure/OVERVIEW.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of this
corpus.
-->

# Coxeter Maximal Parabolic Project Overview

## Project Summary

This project develops mathematical algorithms and software for classifying maximal parabolic subdiagrams in hyperbolic Coxeter systems. The core mathematical focus is on indefinite lattices and their associated geometric structures.

## Mathematical Background

### Mathematical Focus
This project addresses fundamental problems in hyperbolic Coxeter group theory, particularly the classification of maximal parabolic subdiagrams and their geometric interpretation.

For complete mathematical background, see **[MATHEMATICAL_THEORY.md](MATHEMATICAL_THEORY.md)**.

## Implementation Approach

### Mathematical Rigor
- **Exact Arithmetic**: Work over ZZ, QQ, and algebraic number fields
- **Sage Integration**: Build on SageMath's validated lattice infrastructure  
- **Algorithm Verification**: Cross-check against known mathematical results

### Design Approach
Our implementation prioritizes mathematical rigor and follows strict conventions for indefinite lattice computation.

For complete design principles and conventions, see **[CONVENTIONS.md](../CONVENTIONS.md)**.

## Current Status

### Completed
- ✅ **Mathematical Framework**: Comprehensive convention system established
- ✅ **Interface Design**: Complete API specifications for lattice operations
- ✅ **Documentation**: Consolidated conventions and mathematical foundations  
- ✅ **Algorithm Research**: Identified correct approaches for indefinite lattices

### In Progress  
- 🔄 **Core Implementation**: AlgebraicLattice class with symbolic basis manipulation
- 🔄 **Algorithm Development**: Efficient maximal parabolic enumeration

### Next Steps
1. **Implement Core Classes**: AlgebraicLattice with natural mathematical notation
2. **Algorithm Optimization**: Efficient enumeration using mathematical properties
3. **Validation**: Test against all known finite and affine types
4. **Integration**: Full SageMath compatibility and category framework

## Technical Architecture

### Algebraic Lattice Implementation
The core innovation is a minimal lattice implementation supporting natural mathematical notation:

```python
# Hyperbolic plane U
U = AlgebraicLattice(['e', 'f'], 
                     bilinear_form={('e','f'): 1, ('f','e'): 1})
e, f = U.e, U.f

# Natural arithmetic
v = 2*e + 3*f
w = e - f
result = v * w  # Bilinear form evaluation → -5

# Construct from Coxeter types using LaTeX notation
L = Lattice.from_coxeter_type("A_3")        # Finite type
M = Lattice.from_coxeter_type("\\tilde{A}_2")  # Affine type
N = Lattice.from_coxeter_type("H_4")        # Non-crystallographic
```

### Key Features
- **Symbolic Basis Access**: `L.e`, `L.f` attribute notation
- **Bilinear Form Evaluation**: Direct `*` operator for inner products  
- **Indefinite Lattice Support**: Optimized for hyperbolic and parabolic types
- **Minimal Inheritance**: Based on `FreeModule_generic` for full control

## Documentation Structure

### Core References
- **[CONVENTIONS.md](../CONVENTIONS.md)** - Complete mathematical and coding conventions
- **[ALGORITHMS.md](api/ALGORITHMS.md)** - Algorithm specifications with indefinite lattice focus
- **[Interface Documentation](api/interfaces/)** - Complete API specifications

### Mathematical Context
- **Research TODO**: Future mathematical research directions
- **Category Theory**: Proper morphism and functor specifications
- **Field Extensions**: Handling non-crystallographic types (H₃, H₄)

## Getting Started

### For Implementers
1. Read **CONVENTIONS.md** for all project conventions
2. Review **api/interfaces/** for complete API specifications  
3. Check **ALGORITHMS.md** for indefinite lattice algorithm requirements
4. See algebraic lattice documentation in **api/interfaces/free_modules/free_bilinear_modules/symmetric_bilinear_modules/lattices/lattice_elements.md**

### For Mathematicians
1. Start with mathematical background above
2. Review Gram vs Cartan matrix distinctions in **CONVENTIONS.md**
3. Understand indefinite lattice classification in **ALGORITHMS.md**
4. Check **api/TODO.md** for future research directions

### For Users
The project aims to provide natural mathematical notation for lattice computations while maintaining the highest standards of mathematical rigor and computational efficiency.

## Links to External Resources

- **SageMath Documentation**: https://doc.sagemath.org/
- **Mathematical Literature**: See references in individual documentation files
- **Related Projects**: CoxIter (Guglielmetti), Vinberg's algorithms (Boyd)

This project represents a significant step forward in computational mathematics for hyperbolic geometry and indefinite lattice theory.