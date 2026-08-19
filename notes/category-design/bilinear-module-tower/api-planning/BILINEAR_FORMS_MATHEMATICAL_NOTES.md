<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/BILINEAR_FORMS_MATHEMATICAL_NOTES.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Mathematical Notes on Bilinear Forms

## Terminology Precision

**Bilinear Form**: A function B: V × V → K that is linear in both arguments.

**Inner Product**: A positive-definite, symmetric bilinear form. Specifically requires:
1. Symmetry: B(x,y) = B(y,x)
2. Positive definiteness: B(x,x) > 0 for all x ≠ 0
3. Non-degeneracy: B(x,y) = 0 for all y implies x = 0

**DO NOT** use "inner product" for general bilinear forms! Use:
- "bilinear form" (general case)
- "bilinear pairing" (emphasizes the pairing aspect)
- "quadratic form" (when discussing B(x,x))

**Examples of what is NOT an inner product:**
- Indefinite forms (signature (p,q) with q > 0)
- Skew-symmetric forms
- Degenerate forms
- Complex Hermitian forms (these are sesquilinear, not bilinear)

## Important Distinctions

### Orthogonality and Complements

For a bilinear form `B(x,y)` on a module M:

1. **For symmetric forms**: `B(x,y) = B(y,x)`
   - Orthogonality is symmetric: if `B(x,y) = 0` then `B(y,x) = 0`
   - Orthogonal complements are well-defined
   - The orthogonal complement of v is `{w ∈ M : B(v,w) = 0}`

2. **For skew-symmetric forms**: `B(x,y) = -B(y,x)`
   - If `B(x,y) = 0` then `B(y,x) = 0` (still symmetric relation)
   - Orthogonal complements are well-defined
   - BUT: Every element is orthogonal to itself: `B(v,v) = 0` for all v
   - No notion of "norm" or "length"

3. **For general (non-symmetric) forms**: `B(x,y) ≠ B(y,x)` in general
   - Need to distinguish left and right orthogonality:
     - Left orthogonal: `{w : B(w,v) = 0}`
     - Right orthogonal: `{w : B(v,w) = 0}`
   - These can be different sets!
   - No well-defined single "orthogonal complement"

## Implications for API Design

### FreeBilinearModules (Base Category)
Should NOT include:
- `orthogonal_complement()` - not well-defined in general
- `norm_squared()` - only makes sense for symmetric forms
- `reflection()` - requires symmetry

Should include:
- `left_orthogonal_to(v)` - elements w where B(w,v) = 0
- `right_orthogonal_to(v)` - elements w where B(v,w) = 0
- `is_left_orthogonal(v, w)` - test if B(v,w) = 0
- `is_right_orthogonal(v, w)` - test if B(w,v) = 0

### SymmetricBilinearModules
Can now include:
- `orthogonal_complement()` - well-defined since left = right
- `norm_squared()` - returns B(v,v)
- `reflection()` - the reflection operator

### SkewSymmetricBilinearModules  
Should include:
- `orthogonal_complement()` - well-defined
- Should NOT include `norm_squared()` - always zero
- Should NOT include `reflection()` - undefined for isotropic vectors

## Correct Category Hierarchy

```
BilinearModules
├── SymmetricBilinearModules
│   ├── DefiniteBilinearModules
│   │   ├── PositiveDefiniteBilinearModules
│   │   └── NegativeDefiniteBilinearModules
│   ├── IndefiniteBilinearModules
│   │   └── HyperbolicBilinearModules
│   └── DegenerateBilinearModules
│       └── ParabolicBilinearModules
├── SkewSymmetricBilinearModules
│   └── AlternatingBilinearModules
└── GeneralBilinearModules (neither symmetric nor skew)
```

## Examples

### General bilinear form (not symmetric)
```
B = [[1, 2],
     [3, 4]]

B(e₁, e₂) = 2
B(e₂, e₁) = 3  # Different!

Right orthogonal to e₁: {w : B(e₁,w) = 0} means w₁ + 2w₂ = 0
Left orthogonal to e₁: {w : B(w,e₁) = 0} means w₁ + 3w₂ = 0
```

### Skew-symmetric form  
```
B = [[ 0, 1],
     [-1, 0]]

B(v,v) = 0 for all v (every vector is isotropic)
Orthogonal complement is well-defined
Used in symplectic geometry
```

### Symmetric form
```
B = [[2, 1],
     [1, 3]]

B(v,w) = B(w,v) for all v,w
Orthogonal complement is well-defined
Can define reflections, norms, etc.
```