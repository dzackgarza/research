<!--
Origin: gitclones/Coxeter/research/explorations/implementation-notes/sagemath_notation_deficiencies.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is an ALGORITHM/REQUIREMENT SURVEY written against SageMath as it
stood in the source tree. Rows now owned by the preamble, and errors the
audit recorded, are listed in the README.md of this directory.
-->

# SageMath Natural Notation Deficiencies

Beyond the `f^(-1)(y)` morphism preimage syntax, SageMath lacks many other **natural mathematical notations** that mathematicians expect to work. This creates friction between mathematical thinking and computational implementation.

---

## ❌ Missing Natural Notation

### 1. **Direct Sum Notation: `M ⊕ N`**

**What mathematicians write:**
```
M ⊕ N  (direct sum of modules)
```

**What SageMath requires:**
```sage
# Clunky current syntax:
sage: M.direct_sum(N)
# or even worse:
sage: DirectSum([M, N])
```

**What should work:**
```sage
# Natural notation (doesn't work):
sage: M + N  # Should mean direct sum for modules
sage: M ⊕ N  # Unicode direct sum (doesn't work)
```

### 2. **Tensor Product Notation: `M ⊗ N`**

**What mathematicians write:**
```
M ⊗_R N  (tensor product over R)
```

**What SageMath lacks:**
```sage
# None of these work:
sage: M * N      # Should mean tensor product
sage: M @ N      # Python 3.5+ matrix multiplication operator
sage: M ⊗ N      # Unicode tensor product symbol
sage: M.tensor(N)  # Even this doesn't exist!
```

### 3. **Composition Notation: `g ∘ f`**

**What mathematicians write:**
```
g ∘ f  (composition: first f, then g)
```

**What SageMath requires:**
```sage
# Backwards and unnatural:
sage: g * f  # This means g(f(x)), but * suggests multiplication
sage: g.compose(f)  # Verbose
```

**What should work:**
```sage
# Natural mathematical notation:
sage: g ∘ f      # Unicode composition symbol
sage: g.after(f) # Clear English
sage: f.then(g)  # Clear order
```

### 4. **Subset/Submodule Notation: `S ⊆ M`**

**What mathematicians write:**
```
S ⊆ M  (S is a submodule of M)
S ⊂ M  (S is a proper submodule of M)
```

**What SageMath lacks:**
```sage
# None of these work naturally:
sage: S <= M  # Should test if S is submodule of M
sage: S < M   # Should test if S is proper submodule of M
sage: S in M  # Different meaning (element membership)
```

### 5. **Quotient Notation: `M / N`**

**What mathematicians write:**
```
M / N  (quotient module)
```

**What SageMath requires:**
```sage
# Verbose current syntax:
sage: M.quotient(N)
sage: M.quotient_module(N)
```

**What should work:**
```sage
# Natural division notation:
sage: M / N  # Should create quotient module M/N
```

### 6. **Dual Space Notation: `M*` or `M^*`**

**What mathematicians write:**
```
M*   (dual space/module)
V^⊥  (orthogonal complement)
```

**What SageMath lacks:**
```sage
# None of these work:
sage: M.dual()     # Method doesn't exist
sage: M*           # SyntaxError  
sage: M^(-1)       # We just implemented this for morphisms!
sage: ~M           # Could mean dual
```

### 7. **Interior/Closure Notation**

**What mathematicians write:**
```
cl(S)    (closure)
int(S)   (interior)  
S°       (interior)
S̄        (closure)
```

**What SageMath lacks:**
```sage
# Geometric/topological operations often missing:
sage: S.closure()   # Sometimes works, often doesn't
sage: S.interior()  # Rarely implemented
sage: ~S            # Could mean complement
```

### 8. **Action Notation: `g · x`**

**What mathematicians write:**
```
g · x    (group element g acts on x)
σ(x)     (permutation σ acts on x)
```

**What SageMath requires:**
```sage
# Inconsistent action syntax:
sage: g(x)           # Sometimes works
sage: g.action(x)    # Verbose
sage: x.act_by(g)    # Backwards
```

**What should work:**
```sage
# Natural action notation:
sage: g * x    # Should mean group action (when clear from context)
sage: g · x    # Unicode middle dot
```

### 9. **Set Operations with Natural Symbols**

**What mathematicians write:**
```
A ∪ B    (union)
A ∩ B    (intersection)  
A ∖ B    (set difference)
A △ B    (symmetric difference)
```

**What SageMath requires:**
```sage
# Verbose method calls:
sage: A.union(B)
sage: A.intersection(B)
sage: A.difference(B)
sage: A.symmetric_difference(B)
```

### 10. **Logical Notation in Predicates**

**What mathematicians write:**
```
∀x ∈ S: P(x)    (for all x in S, P(x) holds)
∃x ∈ S: P(x)    (exists x in S such that P(x))
```

**What SageMath lacks:**
```sage
# No natural quantifier syntax:
sage: all(P(x) for x in S)     # Pythonic but not mathematical
sage: any(P(x) for x in S)     # Pythonic but not mathematical

# Would be nice:
sage: ∀(x in S, P(x))  # Universal quantifier
sage: ∃(x in S, P(x))  # Existential quantifier
```

### 11. **Limit Notation**

**What mathematicians write:**
```
lim_{x→a} f(x)     (limit as x approaches a)
lim_{n→∞} a_n      (limit as n goes to infinity)
```

**What SageMath requires:**
```sage
# Verbose function calls:
sage: limit(f(x), x=a)
sage: limit(a_n, n=oo)
```

### 12. **Derivative Notation**

**What mathematicians write:**
```
f'(x)      (derivative)
f''(x)     (second derivative)
∂f/∂x      (partial derivative)
```

**What SageMath requires:**
```sage
# Function call syntax:
sage: diff(f, x)        # Not f'(x)
sage: diff(f, x, 2)     # Not f''(x)
sage: diff(f, x, y)     # Mixed partials work but syntax is verbose
```

### 13. **Integral Notation**

**What mathematicians write:**
```
∫ f(x) dx           (indefinite integral)
∫_a^b f(x) dx       (definite integral)
∮ f(z) dz           (contour integral)
```

**What SageMath requires:**
```sage
# Function calls:
sage: integrate(f, x)         # Not ∫ f dx
sage: integrate(f, (x, a, b)) # Not ∫_a^b f dx
```

### 14. **Matrix/Vector Notation**

**What mathematicians write:**
```
⟨v, w⟩        (inner product)
||v||         (norm)
v × w         (cross product)
[v₁, v₂, v₃]  (vector with subscripts)
```

**What SageMath partially supports:**
```sage
# Some work, some don't:
sage: v.inner_product(w)  # Works but verbose
sage: v.norm()            # Works
sage: v.cross_product(w)  # Works for R^3
sage: v[0], v[1], v[2]    # Subscripts work but no automatic subscript notation
```

---

## 🔧 Potential Solutions

### 1. **Operator Overloading**
Many of these could be implemented via Python's operator overloading:

```python
class ModuleElement:
    def __add__(self, other):
        # M + N could mean direct sum
        return self.parent().direct_sum(other.parent())
    
    def __mul__(self, other):
        # Context-dependent: scalar mult, tensor product, or composition
        if isinstance(other, scalar):
            return scalar_mult(self, other)
        elif isinstance(other, Module):
            return tensor_product(self, other)
    
    def __truediv__(self, other):
        # M / N means quotient
        return self.quotient(other)
    
    def __le__(self, other):
        # S <= M means "S is submodule of M"
        return self.is_submodule_of(other)
```

### 2. **Unicode Symbol Support**
SageMath could recognize Unicode mathematical symbols:

```python
# Map Unicode to operations
UNICODE_OPS = {
    '⊕': 'direct_sum',
    '⊗': 'tensor_product', 
    '∘': 'compose',
    '⊆': 'is_submodule_of',
    '∩': 'intersection',
    '∪': 'union',
    '∖': 'difference',
}
```

### 3. **Smart Context Detection**
Operations could behave differently based on context:

```python
def __mul__(self, other):
    if isinstance(self, GroupElement) and hasattr(other, 'act_by'):
        return other.act_by(self)  # Group action
    elif isinstance(self, Morphism) and isinstance(other, Morphism):
        return self.compose(other)  # Morphism composition
    elif isinstance(self, Module) and isinstance(other, Module):
        return self.tensor_product(other)  # Tensor product
    # etc.
```

### 4. **Preprocessor Extensions**
Extend SageMath's preprocessor to handle more mathematical notation:

```python
# Transform mathematical notation in preprocessor
def preprocess_math(code):
    code = code.replace('∀', 'forall')
    code = code.replace('∃', 'exists') 
    code = code.replace('⟨', 'inner_product(')
    code = code.replace('⟩', ')')
    return code
```

---

## 🎯 Most Important Missing Notations

### **High Priority** (would dramatically improve usability):
1. **`M / N`** - quotient modules
2. **`M ⊕ N`** or **`M + N`** - direct sums  
3. **`M ⊗ N`** or **`M * N`** - tensor products
4. **`f^(-1)(y)`** - preimage (we implemented this!)
5. **`S ⊆ M`** - submodule testing

### **Medium Priority** (nice to have):
6. **`g ∘ f`** - composition with correct order
7. **`M*`** or **`~M`** - dual modules
8. **`⟨v,w⟩`** - inner products
9. **Unicode set operations** (∪, ∩, ∖)
10. **`g · x`** - group actions

### **Lower Priority** (specialized):
11. Limit notation with arrows
12. Integral notation with bounds
13. Quantifier notation (∀, ∃)
14. Advanced geometric notation

---

## 📊 Comparison with Other Systems

### **Mathematica**:
- **Strengths**: Excellent Unicode support, natural mathematical notation
- **Examples**: `D[f, x]` for derivatives, `Integrate[f, x]` with nice display

### **Julia**:
- **Strengths**: Excellent operator overloading, Unicode variable names
- **Examples**: Can define `⊗(A,B) = kron(A,B)` for tensor products

### **Python + SymPy**:
- **Strengths**: Good symbolic math notation, LaTeX rendering
- **Weaknesses**: Still function-call heavy, not as natural as handwritten math

### **Lean/Coq**:
- **Strengths**: Mathematical notation matches formal proofs exactly
- **Examples**: `∀ x ∈ S, P x` works directly

---

## 💡 Implementation Strategy

For our bilinear modules project, we could:

1. **Start with high-priority operators**: Implement `⊕`, `⊗`, `/`, `⊆`
2. **Use context-aware dispatch**: Same operator behaves differently for different types
3. **Provide both**: Unicode symbols AND verbose methods for accessibility
4. **Extend gradually**: Add more notation as the framework grows
5. **Document extensively**: Show both notations in examples

This would make our bilinear modules much more natural to use than current SageMath modules!