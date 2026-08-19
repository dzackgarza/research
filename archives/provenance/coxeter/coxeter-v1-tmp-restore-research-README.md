<!--
Origin: gitclones/Coxeter/tmp_restore/research/README.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a PROVENANCE RECORD: a corpus map or superseded design plan, kept
so the routing decisions of the migration stay legible. It is not a
statement about the current repository.
-->

# Coxeter Research Data Collection

## Overview

This directory contains curated mathematical literature and research sources for the Coxeter maximal parabolic project. Every test asserting a mathematical truth includes proper file citations linking to authoritative sources.

## Directory Structure

```
research/
├── papers/           # Academic papers and preprints
├── wikiwand/        # Wikiwand mathematical articles  
├── wikipedia/       # Wikipedia reference articles
├── books/           # Book excerpts and references
├── preprints/       # ArXiv and other preprint sources
└── citations/       # Citation management and indexing
```

## Collected Sources

### Academic Papers
- **Bogachev & Kolpakov (2024)**: "Thin Hyperbolic Reflection Groups"
  - Key results: Zariski density, eigenvalue classification, thin groups
  - File: `papers/bogachev_kolpakov_thin_hyperbolic_2024.md`

### Reference Articles  
- **Wikiwand**: Coxeter Groups and Schläfli Matrices
  - Matrix relationships, classification criteria, examples
  - File: `wikiwand/coxeter_schlaefli_matrices.md`

- **Wikipedia**: Coxeter Groups Overview
  - Complete classification, applications, key theorems
  - File: `wikipedia/coxeter_groups_overview.md`

- **Wikipedia**: Coxeter-Dynkin Diagrams
  - Finite/affine/hyperbolic classification, diagram notation
  - File: `wikipedia/coxeter_dynkin_diagrams.md`

## Citation System

### Format Standard
Every mathematical test includes citations in this format:
```python
# CITATION: research/path/to/source.md
# FACT/EXAMPLE/CLASSIFICATION: Brief description
def test_mathematical_property():
    """Test description with source attribution."""
```

### Coverage Statistics
- **Unit Tests**: 6 tests with mathematical citations
- **System Tests**: 8 tests with literature citations  
- **Research Sources**: 4 comprehensive files
- **Mathematical Facts**: 12+ with source attribution

## Key Mathematical Results

### Classification Theorems
1. **Eigenvalue Classification** (Bogachev-Kolpakov):
   - All negative → finite type
   - All non-negative (≥1 zero) → affine type
   - Some positive → hyperbolic type

2. **Determinant Classification** (Multiple sources):
   - det(Schläfli) > 0 ⟺ finite type
   - det(Schläfli) = 0 ⟺ affine type  
   - det(Schläfli) < 0 ⟺ hyperbolic type

### Matrix Relationships
1. **Coxeter-Schläfli Formula** (Wikiwand):
   - C_ij = -2 cos(π/M_ij)
   - Transforms combinatorial → geometric data

2. **Symmetry Properties** (Multiple sources):
   - Gram matrices always symmetric
   - Inherit from inner product definition

### Literature Examples
1. **A₂ Triangle Group**:
   - Coxeter matrix: [[1,3],[3,1]]
   - Gram matrix: [[-2,1],[1,-2]]
   - Determinant: 3, Eigenvalues: [-3,-1]

2. **Non-reflective Lattice** (Bogachev-Kolpakov):
   - f(x) = 3x₀² + 14x₀x₁ + 98x₀x₂ + 49x₂²
   - Has roots but infinite-index reflection group

## Test Integration

### Unit Tests (`tests/unit/test_gram_matrices.py`)
- A₂ construction with literature verification
- Eigenvalue classification testing
- Matrix symmetry validation
- Negative diagonal convention

### System Tests (`tests/system/test_classification_examples.py`)  
- Complete finite type enumeration
- Exceptional type verification
- Affine type characterization
- Hyperbolic examples from literature

### Citation Index (`citations/CITATION_INDEX.md`)
- Maps mathematical facts → source files
- Tracks test coverage by source
- Identifies missing citations

## Research Methodology

### Source Prioritization
1. **Peer-reviewed papers**: Highest authority
2. **Standard references**: Wikiwand, Wikipedia for established facts
3. **Cross-verification**: Multiple sources for key results
4. **Literature examples**: Specific computational verification

### Citation Requirements
- Mathematical facts MUST have citations
- Implementation details do NOT require citations
- Examples should link to specific literature
- Classification results need authoritative sources

### Quality Assurance
- All matrices verified against literature
- Examples tested for correctness
- Sources checked for mathematical rigor
- Citations maintained in index

## Usage in Tests

### Adding New Citations
1. Collect research source in appropriate directory
2. Add citation block to test:
   ```python
   # CITATION: research/path/to/source.md  
   # FACT: Mathematical statement being tested
   ```
3. Update citation index
4. Verify mathematical correctness

### Citation Categories
- **FACT**: General mathematical theorem/property
- **EXAMPLE**: Specific computational example
- **CLASSIFICATION**: Type classification result
- **CONVENTION**: Standard mathematical convention

This research foundation ensures our Coxeter project tests are mathematically rigorous and properly attributed to authoritative sources.