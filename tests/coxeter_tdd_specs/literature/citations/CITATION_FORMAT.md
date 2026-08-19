# Citation Format Standards for Mathematical Tests

## Citation Format in Test Files

Every test asserting a mathematical truth (vs implementation detail) MUST include a file citation:

```python
# CITATION: research/papers/bogachev_kolpakov_thin_hyperbolic_2024.md
# FACT: Zariski dense groups characterized by limit set not in hypersphere
def test_zariski_density_characterization():
    """Test Zariski density characterization theorem."""
    # Test implementation
```

## Citation Categories

### Mathematical Facts
Tests asserting mathematical theorems, properties, or relationships:
- `# CITATION: research/papers/filename.md`
- `# FACT: Brief description of mathematical fact being tested`

### Literature Examples  
Tests based on specific examples from literature:
- `# CITATION: research/wikiwand/filename.md`
- `# EXAMPLE: Description of the specific example`

### Classification Results
Tests verifying classification theorems:
- `# CITATION: research/wikipedia/filename.md` 
- `# CLASSIFICATION: Type being classified (finite/affine/hyperbolic)`

### Convention Verification
Tests verifying our implementation follows standard conventions:
- `# CITATION: research/papers/filename.md`
- `# CONVENTION: Description of convention being verified`

## Required Citation Fields

1. **CITATION**: Relative path to research file (from project root)
2. **FACT/EXAMPLE/CLASSIFICATION/CONVENTION**: Brief description  
3. **Page/Section** (for papers): Specific location if applicable
4. **Mathematical Statement**: Key theorem or result being tested

## Example Citation Blocks

### For Eigenvalue Classification
```python
# CITATION: research/papers/bogachev_kolpakov_thin_hyperbolic_2024.md
# CLASSIFICATION: Coxeter group type by Gram matrix eigenvalues
# FACT: All positive → finite, all non-negative (≥1 zero) → affine, some negative → hyperbolic
def test_eigenvalue_classification():
```

### For Matrix Relationships
```python
# CITATION: research/wikiwand/coxeter_schlaefli_matrices.md
# FACT: Schläfli matrix C_ij = -2 cos(π/M_ij) from Coxeter matrix M
def test_coxeter_to_schlaefli_formula():
```

### For Literature Examples
```python
# CITATION: research/wikipedia/coxeter_groups_overview.md
# EXAMPLE: A2 triangular group with Gram matrix [[-2,1],[1,-2]]
def test_A2_gram_matrix():
```

## Non-Mathematical Tests (No Citations Required)

Implementation details that don't assert mathematical facts:
- Constructor argument validation
- Error handling behavior  
- API contract compliance
- Performance characteristics
- Code organization

## Citation Index

Maintain `research/citations/CITATION_INDEX.md` mapping:
- Mathematical facts → source files
- Test files → citations used
- Source files → tests that cite them