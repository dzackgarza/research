# SageMath Method Discovery Patterns

## The Problem We Just Solved

When working with SageMath classes, key methods are often buried in large classes with 100+ methods. Here are strategies that work:

## 🔍 **Discovery Techniques That Work**

### 1. **Mathematical Naming Conventions**
- Look for **single-letter methods** for core mathematical operations
- `q(v)` = quadratic form
- `b(u,v)` = bilinear form  
- `f(x)` = function evaluation
- These are intentionally terse for mathematical elegance

### 2. **Source Code Archaeology**
```sage
# Find all methods with keywords
[m for m in dir(L) if 'direct' in m]
[m for m in dir(L) if 'sum' in m] 
[m for m in dir(L) if 'signature' in m]

# Look at method source
L.method_name??

# Grep the source files (when you have them)
grep -n "def.*direct\|def.*sum" sage_source_file.py
```

### 3. **Test Small Examples**
```sage
# Create simple test case
L = IntegralLattice([[2, 1], [1, 2]])
v = vector([1, 1])

# Try likely method names
L.q(v)              # Often works!
L.evaluate(v)       # Sometimes works
L.quadratic_form()(v)  # Usually works but complex
```

### 4. **Read the Class Docstring**
```sage
help(IntegralLattice)
L.__doc__
```
Look for "EXAMPLES" sections - they often show core methods.

### 5. **Look for Properties vs Methods**
- Properties: `L.gram_matrix`, `L.basis`
- Methods: `L.q(v)`, `L.direct_sum(M)`

## 🎯 **Patterns We Discovered**

1. **Core operations are often single letters**: `q()`, `b()`
2. **Factory methods are verbose**: `IntegralLattice()`, `direct_sum()`  
3. **Properties are descriptive**: `gram_matrix()`, `signature_pair()`
4. **Advanced methods are very verbose**: `get_orbits_of_isotropic_k_planes()`

## 💡 **General Strategy**

1. **Start with mathematical intuition** - what would a mathematician call this?
2. **Try the obvious names first** - they often work
3. **Look for single-letter methods** - core operations
4. **Use method categories** - group related functionality
5. **When in doubt, read the source** - it's usually enlightening

## 🏆 **Success Story**

We found that `IntegralLattice` has perfect methods:
- `q(v)` for quadratic forms
- `b(u,v)` for bilinear forms  
- `direct_sum(M)` for orthogonal sums
- `signature_pair()` for signatures

But they were buried among 100+ methods with no clear organization!

The lesson: **mathematical libraries often have exactly what you need, but discoverability is the challenge.**