<!--
Origin: gitclones/Coxeter/tmp_restore/content-audit.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a PROVENANCE RECORD: a corpus map or superseded design plan, kept
so the routing decisions of the migration stay legible. It is not a
statement about the current repository.
-->

# Mathematical Content Audit

## Executive Summary

This audit systematically reviews current documentation to identify critical mathematical content that must be preserved during reorganization. The analysis reveals significant mathematical theory currently distributed across multiple files, with some unique content at risk of loss and substantial redundancy that can be safely archived.

## File-by-File Analysis

### 1. docs/OVERVIEW.md

**Mathematical Content Summary:**
- Brief mathematical background reference (delegates to MATHEMATICAL_THEORY.md)
- Technical architecture with AlgebraicLattice implementation example
- Natural mathematical notation specifications (`v * w` for bilinear form evaluation)
- Core feature specifications: symbolic basis access, bilinear form evaluation, indefinite lattice support
- References to documentation structure and external resources

**Preservation Priority:** IMPORTANT (Should Preserve)
- Contains unique technical architecture details not found elsewhere
- Provides important implementation context for mathematical notation
- Serves as architectural foundation document

**Location Recommendation:** Top-level (keep as overview)
- Architectural content is unique and valuable
- Provides important bridge between mathematical theory and implementation

### 2. docs/MATHEMATICAL_THEORY.md

**Mathematical Content Summary:**
- **Core Mathematical Framework**: Complete definitions of indefinite quadratic forms, signature theory
- **Classification Theorems**: Elliptic/Parabolic/Hyperbolic definitions based on definiteness properties
- **Mathematical Properties**: Eigenvalue monotonicity theorem, signature inheritance theorem, Vinberg's volume finiteness criteria
- **Gram vs Cartan Matrix**: Comprehensive distinction and relationship analysis
- **Field Theory Requirements**: Complete specifications for crystallographic and non-crystallographic types
- **Algorithmic Implications**: Mathematical requirements for definite vs indefinite lattice algorithms
- **Comprehensive Mathematical Definitions**: Detailed definitions of Gram matrices, subdiagrams, maximal parabolic subdiagrams
- **Implementation Requirements**: Mathematical rigor standards and correct implementation approaches

**Preservation Priority:** CRITICAL (Must Preserve)
- Contains unique mathematical definitions not in CONVENTIONS.md
- Provides complete theoretical foundation for entire project
- Includes precise theorem statements and proofs references
- Contains field theory specifications essential for non-crystallographic types
- Defines algorithmic requirements for mathematical correctness

**Location Recommendation:** Top-level as MATHEMATICAL_FOUNDATIONS.md
- This content is the mathematical heart of the project
- Required reference for all implementation work
- Should remain easily accessible at top level

### 3. docs/REQUIREMENTS.md

**Mathematical Content Summary:**
- **Core Mathematical Requirements**: Exact arithmetic specifications, categorical framework requirements
- **Signature-Based Classification**: Complete classification scheme (p,q,r) for lattice types
- **Field Extension Requirements**: Detailed specifications for non-crystallographic field extensions
- **Indefinite Lattice Algorithms**: Critical distinctions between definite and indefinite algorithm requirements
- **Morphism Requirements**: Mathematical specifications for lattice morphisms and coercion philosophy

**Preservation Priority:** CRITICAL (Must Preserve)
- Contains unique algorithmic requirements not found elsewhere
- Provides precise specifications for mathematical correctness
- Includes critical field theory requirements
- Defines morphism framework essential for categorical correctness

**Location Recommendation:** Top-level (possibly merge into MATHEMATICAL_FOUNDATIONS.md)
- Mathematical requirements are distinct from implementation requirements
- Field extension specifications are unique and critical
- Algorithmic distinctions for indefinite lattices are essential

### 4. docs/IMPLEMENTATION_GUIDE.md

**Mathematical Content Summary:**
- **Algebraic Lattice Foundation**: Technical specifications for mathematical notation implementation
- **Algorithm Selection by Signature**: Mathematical approach to algorithm selection based on definiteness
- **Mathematical Validation**: Framework for validating against known mathematical results
- **Common Implementation Pitfalls**: Mathematical errors to avoid (Gram vs Cartan confusion, definite vs indefinite algorithms)

**Preservation Priority:** IMPORTANT (Should Preserve)
- Contains important mathematical implementation patterns
- Provides critical guidance on mathematical pitfalls
- Includes validation strategies for mathematical correctness
- Mathematical content has implementation context but mathematical significance

**Location Recommendation:** Reference documentation
- Implementation-focused but mathematically rigorous content
- Important for implementers but not core mathematical theory
- Could be condensed and moved to docs/reference/

### 5. docs/TESTING.md

**Mathematical Content Summary:**
- **Mathematical Property Tests**: Framework for testing mathematical invariants
- **Cross-Validation Tests**: Approach for validating against SageMath and literature
- **Mathematical correctness principles**: Property-based testing for mathematical algorithms
- **Regression Testing**: Framework for preserving known classification results

**Preservation Priority:** IMPORTANT (Should Preserve)
- Contains important mathematical validation strategies
- Provides framework for ensuring mathematical correctness
- Includes references to known mathematical results for validation

**Location Recommendation:** Reference documentation
- Testing strategies have mathematical content but are implementation-focused
- Important for maintaining mathematical rigor
- Could be moved to docs/reference/testing.md

## Content Categories Analysis

### Unique Mathematical Definitions to Preserve

**CRITICAL - Must be in MATHEMATICAL_FOUNDATIONS.md:**

1. **Indefinite Quadratic Forms Theory** (from MATHEMATICAL_THEORY.md):
   - Definition and signature (p,q,r) specification
   - Definiteness classification scheme

2. **Coxeter System Classification** (from MATHEMATICAL_THEORY.md):
   - Mathematical definitions of Elliptic/Parabolic/Hyperbolic based on definiteness
   - Signature inheritance theorem
   - Eigenvalue monotonicity theorem

3. **Gram vs Cartan Matrix Distinction** (from MATHEMATICAL_THEORY.md):
   - Complete mathematical distinction and relationship analysis
   - Critical for avoiding implementation errors

4. **Field Theory Requirements** (from MATHEMATICAL_THEORY.md + REQUIREMENTS.md):
   - Non-crystallographic field extensions (H₃, H₄, I₂(p))
   - Field specifications: ℤ[φ], ℤ[τ], ℤ[2cos(π/p)]

5. **Vinberg's Geometric Framework** (from MATHEMATICAL_THEORY.md):
   - Volume finiteness criteria
   - Cusp correspondence theory
   - Maximal parabolic subdiagram definition

### Algorithm Specifications Requiring Preservation

**CRITICAL - Must preserve in MATHEMATICAL_FOUNDATIONS.md:**

1. **Indefinite Lattice Algorithm Requirements** (from REQUIREMENTS.md + MATHEMATICAL_THEORY.md):
   - Vector enumeration: QuadraticForm.find_reps() for indefinite vs IntegerLattice.vectors_of_length() for definite
   - Automorphism groups: Custom implementation required for indefinite
   - Algorithmic implications for indefinite lattices

2. **Correct Implementation Approaches** (from MATHEMATICAL_THEORY.md):
   - Definiteness-based methods (is_positive_semidefinite())
   - Forbidden approaches (eigenvalue counting as primary method)
   - Maximality testing via poset construction

3. **Mathematical Validation Framework** (from IMPLEMENTATION_GUIDE.md + TESTING.md):
   - Cross-validation against known results
   - Property-based testing strategies

### Literature References to Maintain

**From MATHEMATICAL_THEORY.md - Must preserve:**
- Vinberg's volume finiteness theorem
- ADE/Affine/Lannér classification references
- Eigenvalue interlacing theorem references
- Bourbaki labeling conventions

**From OVERVIEW.md - Can consolidate:**
- SageMath documentation links
- Related projects (CoxIter, Vinberg's algorithms)

### Implementation Patterns Worth Keeping

**From IMPLEMENTATION_GUIDE.md - Should preserve in reference docs:**
- Natural mathematical notation implementation (`v * w` for bilinear form)
- Algorithm selection by signature pattern
- Constructor validation for mathematical correctness
- Mathematical validation against known results pattern

## Migration Recommendations

### What goes to MATHEMATICAL_FOUNDATIONS.md

**Consolidate from multiple files:**

1. **Complete theoretical framework** from MATHEMATICAL_THEORY.md (preserve entirely)
2. **Field theory requirements** from REQUIREMENTS.md (mathematical sections only)
3. **Algorithmic mathematical requirements** from REQUIREMENTS.md (indefinite lattice algorithms)
4. **Mathematical definitions** scattered across other files

**Result:** Single comprehensive mathematical reference document

### What goes to docs/reference/

**Create new reference directory structure:**

1. **docs/reference/implementation-patterns.md**:
   - Mathematical implementation patterns from IMPLEMENTATION_GUIDE.md
   - Common mathematical pitfalls and solutions
   - Algorithm selection strategies

2. **docs/reference/testing-mathematical-correctness.md**:
   - Mathematical property testing from TESTING.md
   - Cross-validation strategies
   - Literature validation approaches

3. **docs/reference/technical-requirements.md**:
   - Non-mathematical requirements from REQUIREMENTS.md
   - SageMath integration requirements
   - Performance and quality standards

### What goes to docs/archive/

**Safe to archive (redundant with api-planning/ or outdated):**

1. **General development practices** from IMPLEMENTATION_GUIDE.md that duplicate api-planning/
2. **Project management content** from OVERVIEW.md (status updates, getting started)
3. **Non-mathematical sections** that are covered comprehensively in api-planning/

**Note:** The api-planning/ directory contains extensive detailed specifications that make many general implementation discussions redundant.

### What can be safely removed as redundant

**Completely redundant content:**
- Implementation status updates (covered in api-planning/TODO.md)
- General SageMath integration guidance (covered extensively in api-planning/)
- Basic development setup instructions (covered in api-planning/)

## Risk Assessment

### Mathematical Content at Risk of Loss

**HIGH RISK:**

1. **Field Theory Specifications** (REQUIREMENTS.md):
   - Non-crystallographic field requirements are scattered and could be lost
   - ℤ[φ], ℤ[τ] specifications are unique and critical

2. **Indefinite Lattice Algorithm Requirements** (REQUIREMENTS.md + MATHEMATICAL_THEORY.md):
   - Critical distinctions between definite/indefinite algorithms
   - Specific Sage method recommendations (QuadraticForm.find_reps())

3. **Mathematical Implementation Patterns** (IMPLEMENTATION_GUIDE.md):
   - Algorithm selection by signature
   - Mathematical validation approaches

**MEDIUM RISK:**

1. **Literature References**:
   - Scattered across multiple files
   - Need consolidation to prevent loss

2. **Mathematical Pitfall Documentation**:
   - Important error-prevention content
   - Currently in implementation guide but has mathematical significance

### References That Would Become Broken

**Current cross-references that need updating:**
- OVERVIEW.md → MATHEMATICAL_THEORY.md (will become MATHEMATICAL_FOUNDATIONS.md)
- IMPLEMENTATION_GUIDE.md → TESTING.md (both moving to reference/)
- Multiple files referencing CONVENTIONS.md (stable)

**External references to preserve:**
- SageMath documentation links
- Literature references (Vinberg, Bourbaki, etc.)
- Related project references (CoxIter, etc.)

### Implementation Knowledge That Would Be Lost

**Critical knowledge requiring preservation:**

1. **Mathematical Notation Implementation**:
   - `v * w` bilinear form evaluation design
   - Symbolic basis access (`L.e`, `L.f`) 
   - Natural mathematical syntax requirements

2. **Algorithm Selection Patterns**:
   - Signature-based algorithm selection
   - Definiteness property checking
   - Mathematical validation frameworks

3. **Common Mathematical Errors**:
   - Gram vs Cartan matrix confusion
   - Definite vs indefinite algorithm misuse
   - Floating point in exact computation

## Recommended Action Plan

### Phase 1: Critical Content Preservation
1. **Create docs/MATHEMATICAL_FOUNDATIONS.md** by consolidating:
   - Complete MATHEMATICAL_THEORY.md content
   - Mathematical requirements from REQUIREMENTS.md
   - Field theory specifications

2. **Update CONVENTIONS.md** to reference MATHEMATICAL_FOUNDATIONS.md for mathematical theory

### Phase 2: Reference Documentation Organization
1. **Create docs/reference/ directory structure**
2. **Move implementation patterns** from IMPLEMENTATION_GUIDE.md
3. **Move testing strategies** from TESTING.md
4. **Create technical requirements** document from non-mathematical REQUIREMENTS.md content

### Phase 3: Archive and Cleanup
1. **Archive redundant content** to docs/archive/
2. **Update OVERVIEW.md** to remove redundant project management content
3. **Update cross-references** throughout documentation

This migration preserves all critical mathematical content while eliminating redundancy and improving organization.