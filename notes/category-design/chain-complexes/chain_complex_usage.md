<!--
Origin: gitclones/Coxeter/research/explorations/implementation-notes/chain_complex_usage.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of this
corpus.
-->

# Chain Complex Usage Patterns

Both notations are natural for different contexts:

---

## Setup: Working in Categories

```sage
# Set up the categorical context
R = ZZ
C = Modules(R)           # Category of R-modules
ChC = Ch(C)              # Category of chain complexes over C

# Generic objects for examples
A, B, C = C.generic_objects(3)  # or C.an_object() for specific ones

# Morphisms
f = Hom(A, B).an_element()  # or construct specific morphism
g = Hom(B, C).an_element()
```

---

## Notation 1: Categorical Construction

```sage
# Explicit categorical construction
C_bullet = ChC([f, g])

# Clear about which category we're in
# Good for:
# - Programmatic construction
# - When building from morphism lists
# - Clarity about the ambient category
```

**Advantages:**
- Explicit about living in Ch(C)
- Can pass additional parameters
- Clear when reading code
- Works with any list of morphisms

---

## Notation 2: Natural Arrow Syntax

```sage  
# Natural mathematical notation
C_bullet = f >> g

# Just like we write on paper
# Good for:
# - Interactive exploration
# - Simple sequences
# - Mathematical clarity
```

**Advantages:**
- Matches mathematical notation exactly
- Minimal syntax
- Intuitive for sequences
- Great for short exact sequences

---

## Combined Usage

```sage
# Start with arrow notation for exploration
ses = f >> g >> h  # Quick construction

# Convert to categorical object when needed
ses_in_ChC = ChC(ses)  # or ChC.from_morphism_chain(ses)

# Or build complex structures programmatically
morphisms = [construct_differential(i) for i in range(n)]
resolution = ChC(morphisms)
```

---

## Special Patterns

### Short Exact Sequences
```sage
# Both work!
ses1 = ChC([injection, projection])  # Categorical
ses2 = injection >> projection        # Natural

# With special constructor
ses = ShortExactSequence(injection, projection)
ses.is_split()  # Check if it splits
```

### Building Resolutions
```sage
# For computed sequences, list notation is clearer
def projective_resolution(M, length=5):
    morphisms = []
    current = M
    for i in range(length):
        P, proj = current.projective_cover()
        morphisms.append(proj)
        current = proj.kernel()[0]
    return ChC(morphisms)
```

### Long Exact Sequences
```sage
# Arrow notation for small sequences
les = f1 >> f2 >> f3 >> f4 >> f5

# List notation for programmatic construction  
connecting_maps = compute_connecting_morphisms(spectral_sequence)
les = ChC(connecting_maps)
```

---

## Best Practices

1. **Use `>>` for mathematical clarity** when writing specific sequences
2. **Use `ChC([...])` for programmatic construction** and clarity about categories
3. **Both are first-class** - no "preferred" notation
4. **Document intent** - the notation itself documents whether you're thinking categorically or sequentially

---

## Implementation Note

The `>>` operator returns a `ChainableMorphism` object that can be:
- Used directly as a complex
- Converted to `ChC` with `ChC(chain)` or `chain.to_complex()`
- Extended with more morphisms: `(f >> g) >> h`

This gives maximum flexibility while maintaining mathematical clarity.