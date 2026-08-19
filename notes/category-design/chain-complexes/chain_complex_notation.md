<!--
Origin: gitclones/Coxeter/research/explorations/implementation-notes/chain_complex_notation.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of this
corpus.
-->

# Natural Chain Complex Notation

The challenge: How to write `A →_f B →_g C` naturally in code?

---

## Option 1: Arrow Operator `>>` 

```python
# Build complexes with >> as arrow
C = A >> f >> B >> g >> C >> h >> D

# Or with explicit degree markers
C = (A, 0) >> f >> (B, 1) >> g >> (C, 2)

# Short exact sequences
ses = 0 >> A >> i >> B >> p >> C >> 0
```

**Pros**: Reads left-to-right like math
**Cons**: Need to overload >> on modules AND morphisms

---

## Option 2: Shift Operator `<<` or `>>`

```python
# Use << to mean "follows" (like function composition)
C = D << h << C << g << B << f << A

# Reads as "D follows from C via h, which follows from B via g..."
```

**Pros**: Single direction of composition
**Cons**: Backwards from how we write math

---

## Option 3: Builder Pattern with Natural Methods

```python
# Start with an object and chain
C = Chain(A).then(f, B).then(g, C).then(h, D)

# Or more concisely
C = Chain(A)[f:B][g:C][h:D]

# With automatic inference
C = Chain(A)[f][g][h]  # Targets inferred from morphisms
```

**Pros**: Clear and extensible
**Cons**: Still not quite mathematical notation

---

## Option 4: The `@` Operator (Matrix Multiplication)

```python
# Repurpose @ as "then"
C = A @ f @ B @ g @ C

# Short exact sequence
ses = 0 @ A @ i @ B @ p @ C @ 0
```

**Pros**: Unused operator, reads linearly
**Cons**: @ usually means composition/multiplication

---

## Option 5: List/Tuple Building

```python
# Just list objects and morphisms
C = ChainComplex([A, f, B, g, C])

# With explicit pairing
C = ChainComplex([(A, f), (B, g), (C, None)])

# Or as a literal sequence
C = ChainComplex(A -> f -> B -> g -> C)  # If -> worked...
```

---

## Option 6: **The Radical Approach - Custom Syntax**

What if we implemented a simple parser for mathematical notation?

```python
C = complex("A -f-> B -g-> C -h-> D")

# With indices
C = complex("A_0 -f-> A_1 -g-> A_2")

# Short exact sequences  
ses = complex("0 -> A -i-> B -p-> C -> 0")

# Even differentials
koszul = complex("R -[x,y]-> R^2 -[[-y],[x]]-> R")
```

**Implementation sketch**:
```python
def complex(notation):
    """Parse mathematical notation into chain complex."""
    # Parse "A -f-> B -g-> C" syntax
    # Extract objects, morphisms, and build complex
    tokens = parse_arrow_notation(notation)
    return ChainComplex.from_sequence(tokens)
```

---

## Option 7: **Context Manager Magic**

```python
with ChainComplex() as C:
    A >> f >> B >> g >> C >> h >> D

# Or even better - hijack comparison operators in context
with ExactSequence() as E:
    0 > A > i > B > p > C > 0
    
# The context manager captures the chain
```

---

## My Recommendation: **Hybrid Approach**

### 1. For Simple Cases: Operator Overloading
```python
# Define >> on morphisms to build sequences
class Morphism:
    def __rshift__(self, other):
        if isinstance(other, Module):
            # f >> B creates a partial complex
            return PartialComplex([self.domain(), self, other])
        elif isinstance(other, Morphism):
            # f >> g chains morphisms
            return PartialComplex([self.domain(), self, 
                                   self.codomain(), other])

# Usage
C = f >> g >> h  # Creates complex automatically
```

### 2. For Complex Cases: String Notation
```python
# When you need clarity
C = complex("""
    ZZ[x,y] -[x,y]-> ZZ[x,y]^2 -[[-y],[x]]-> ZZ[x,y]
""")

# Parses mathematical notation directly
```

### 3. For Programmatic Building: Smart Constructor
```python
# When building dynamically
C = ChainComplex()
C[0] = A
C[1] = B  
C.d[1] = f  # differential B -> A
```

---

## The Deep Problem

The issue is that mathematical notation is **2-dimensional**:
- Objects sit at different heights (degrees)
- Arrows flow horizontally
- We often omit degree labels when obvious

But code is **1-dimensional** (linear text).

Perhaps the best solution is to support multiple notations:
- **Operator style** for simple sequences: `f >> g >> h`
- **String parsing** for complex cases: `complex("A -f-> B -g-> C")`
- **Dict style** for programmatic construction

What notation feels most natural to you?