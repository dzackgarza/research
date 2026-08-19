<!--
Origin: gitclones/Coxeter/research/README.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a PROVENANCE RECORD: a corpus map or superseded design plan, kept
so the routing decisions of the migration stay legible. It is not a
statement about the current repository.
-->

# Coxeter Research Environment

This directory contains the comprehensive research infrastructure for the Coxeter maximal parabolic project, providing mathematical foundations, literature resources, and ongoing research investigations.

## Overview

The research environment is organized to support both rigorous mathematical development and computational implementation. It separates theoretical foundations from exploratory research while maintaining connections to the broader mathematical literature.

## Directory Structure

```
research/
├── README.md                       # This file - research environment overview
├── foundations/                    # Core mathematical theory
│   ├── mathematical-theory.md      # Enhanced mathematical foundations
│   ├── classification-theory.md    # Definiteness-based classification framework  
│   ├── geometric-foundations.md    # Hyperbolic geometry and group actions
│   └── historical-development.md   # Evolution of Coxeter theory
├── explorations/                   # Active research investigations
│   ├── alternative-approaches.md   # Different mathematical perspectives
│   ├── research-notes.md          # Ongoing investigations and ideas
│   ├── open-questions.md          # Unsolved problems and conjectures
│   └── connections/               # Advanced mathematical connections
│       └── homotopy_theory/       # Homotopy-theoretic framework
└── literature/                    # Curated mathematical literature
    ├── README.md                  # Literature collection overview
    ├── BIBLIOGRAPHY.md            # Comprehensive bibliography
    ├── citations/                 # Citation management
    ├── papers/                    # Academic papers and preprints
    ├── sources/                   # Reference materials
    ├── tools/                     # Research tools
    └── wikipedia/                 # Wikipedia reference articles
```

## Mathematical Foundations

### Core Theory Documents

**[mathematical-theory.md](foundations/mathematical-theory.md)**: Comprehensive mathematical foundations combining formal exposition with research context. Covers indefinite quadratic forms, Coxeter system classification, field theory requirements, and algorithmic considerations.

**[classification-theory.md](foundations/classification-theory.md)**: Definiteness-based classification framework emphasizing the distinction between mathematical definitions and computational algorithms. Provides the theoretical foundation for our classification approach.

**[geometric-foundations.md](foundations/geometric-foundations.md)**: Geometric interpretation of Coxeter systems through hyperbolic geometry, group actions, and Vinberg's volume theory. Connects algebraic classification to geometric properties.

**[historical-development.md](foundations/historical-development.md)**: Evolution of Coxeter theory from crystallographic origins through modern computational approaches. Provides context for current research methods.

### Key Mathematical Principles

1. **Definiteness-Based Classification**: Classifications based on mathematical properties of matrices, not computational algorithms
2. **Exact Arithmetic**: All computations use exact fields (ℤ, ℚ, number fields) to maintain mathematical rigor
3. **Categorical Framework**: Objects live in well-defined categories with structure-preserving morphisms
4. **Basis-Free Construction**: Mathematical objects defined by intrinsic properties, independent of coordinate choices

## Research Explorations

### Active Research Areas

**[alternative-approaches.md](explorations/alternative-approaches.md)**: Exploration of different computational and theoretical approaches to Coxeter group problems. Includes comparison of eigenvalue vs definiteness methods, exhaustive vs pruning strategies, and various mathematical frameworks.

**[research-notes.md](explorations/research-notes.md)**: Ongoing research investigations including computational complexity questions, Galois theory applications, and connections to modern mathematics. Contains experimental approaches and preliminary results.

**[open-questions.md](explorations/open-questions.md)**: Catalog of unsolved problems ranging from computational complexity to deep mathematical conjectures. Organized by research area with specific problem statements and potential approaches.

### Advanced Mathematical Connections

**[connections/homotopy_theory/](explorations/connections/homotopy_theory/)**: Development of modern homotopy-theoretic approach to bilinear modules using stable ∞-categories and spectra. Represents cutting-edge mathematical framework development.

**Key Research Directions**:
- Stable homotopy theory for bilinear modules
- Galois actions on classification results  
- Higher-dimensional asymptotics
- Arithmetic vs non-arithmetic group properties
- Computational complexity optimization

## Literature Resources

The **[literature/](literature/)** directory contains comprehensive mathematical resources:

- **Academic papers**: Research papers and preprints relevant to Coxeter theory
- **Reference sources**: Wikipedia articles, textbook excerpts, and standard references
- **Citation system**: Systematic citation management linking mathematical facts to authoritative sources
- **Research tools**: Scripts and utilities for literature collection and processing

All mathematical assertions in the codebase include proper citations linking to sources in this literature collection.

## Research Methodology

### Mathematical Rigor Standards

**Exact Computation**: All algorithms maintain exact precision using appropriate number fields. Floating-point approximations are forbidden for classification purposes.

**Multiple Validation**: Results verified through:
- Multiple independent computational approaches
- Cross-reference with literature
- Theoretical consistency checks
- Numerical verification using interval arithmetic

**Literature Grounding**: Every mathematical fact supported by citations to authoritative sources with proper academic attribution.

### Development Philosophy

**Theory-Driven Implementation**: Computational methods guided by deep mathematical understanding rather than purely algorithmic optimization.

**Open Research**: Transparent research process with detailed documentation of investigations, both successful and unsuccessful.

**Interdisciplinary Connections**: Active exploration of connections to related mathematical areas including algebraic topology, number theory, and geometric group theory.

## Usage Guidelines

### For Researchers

**Starting Points**:
1. **Mathematical Context**: Begin with [mathematical-theory.md](foundations/mathematical-theory.md) for comprehensive foundations
2. **Implementation Guidance**: Use [classification-theory.md](foundations/classification-theory.md) for correct algorithmic approaches  
3. **Research Ideas**: Explore [open-questions.md](explorations/open-questions.md) for potential research directions

**Contributing Research**:
- Add new findings to [research-notes.md](explorations/research-notes.md)
- Update open questions with progress or new problems
- Contribute literature sources with proper citations
- Document experimental results and computational investigations

### For Implementers

**Algorithm Development**: Classification theory provides mathematically correct approaches, avoiding common implementation errors.

**Validation Requirements**: All implementations must validate against literature examples and maintain exact arithmetic throughout.

**Testing Strategy**: Use literature citations to create test cases with known mathematical results.

## Research Infrastructure

### Computational Requirements

**Exact Arithmetic Libraries**: SageMath for number field computations, exact eigenvalue analysis, and matrix operations over various fields.

**Literature Management**: Citation tracking system linking code assertions to authoritative mathematical sources.

**Experimental Framework**: Infrastructure for systematic enumeration, performance analysis, and result validation.

### Collaboration Framework

**Version Control**: All research content under git version control with detailed commit messages documenting mathematical progress.

**Reproducibility**: Computational experiments designed for reproducibility with explicit environment requirements.

**Open Science**: Research conducted openly with publicly available code, data, and documentation.

## Future Directions

### Short-Term Research Goals
- Complete systematic enumeration for small ranks
- Optimize algorithms for computational efficiency
- Develop Galois-equivariant methods for non-crystallographic types
- Create comprehensive test suite based on literature

### Long-Term Research Vision
- Connect to modern homotopy theory and stable ∞-categories
- Develop arithmetic theory of hyperbolic Coxeter groups
- Create certified computation methods with rigorous error bounds
- Establish comprehensive mathematical database

### Interdisciplinary Opportunities
- **Geometric group theory**: CAT(0) spaces and building theory
- **Algebraic topology**: K-theory and L-theory applications
- **Number theory**: Arithmetic properties of hyperbolic manifolds
- **Computer science**: Quantum algorithms and complexity theory

---

**Research Environment Mission**: Provide comprehensive mathematical foundations, active research exploration, and literature resources to support rigorous development of Coxeter group computational tools while maintaining the highest standards of mathematical correctness and scholarly attribution.

**Academic Integration**: This research environment is designed to produce results suitable for academic publication and to contribute meaningfully to the mathematical literature on Coxeter groups and related areas.