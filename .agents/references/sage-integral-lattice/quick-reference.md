# IntegralLattice Quick Reference

## Core Methods You Actually Need

When working with IntegralLattice objects, these are the essential methods:

### 🎯 **Most Common Operations**
```sage
L = IntegralLattice(gram_matrix)

# Quadratic form evaluation (v²)
L.q(v)                    # Returns v² = (v,v)

# Bilinear form evaluation (inner product)  
L.b(u, v)                 # Returns (u,v) = u^T G v

# Signature
L.signature_pair()        # Returns (t+, t-) positive/negative eigenvalues

# Direct sum (orthogonal sum)
L.direct_sum(M)          # Returns L ⊕ M
```

### 📊 **Structure Information**
```sage
L.gram_matrix()          # Gram matrix G
L.basis()               # Lattice basis vectors
L.rank()                # Lattice rank
L.degree()              # Ambient space dimension
L.discriminant()        # det(G)
```

### 🔄 **Common Patterns**

**Instead of manual computation:**
```sage
# ❌ Don't do this
v_squared = v * L.gram_matrix() * v
inner_prod = u * L.gram_matrix() * v

# ✅ Do this  
v_squared = L.q(v)
inner_prod = L.b(u, v)
```

**For orthogonal sums:**
```sage
# ❌ Don't do this
gram_matrices = [L1.gram_matrix(), L2.gram_matrix()]
combined = block_diagonal_matrix(gram_matrices)
result = IntegralLattice(combined)

# ✅ Do this
result = L1.direct_sum(L2)

# For multiple lattices
from functools import reduce
result = reduce(lambda x, y: x.direct_sum(y), [L1, L2, L3])
```

## 🔍 **Method Discovery Strategy**

1. **Check this reference first** - covers 90% of use cases
2. **Use tab completion**: `L.<TAB>` in Sage
3. **Search for keywords**: `[m for m in dir(L) if 'signature' in m]`
4. **Read the source**: `L.method_name??` shows implementation

## ⚠️ **Common Gotchas**

- `L.q(v)` and `L.b(u,v)` expect vectors in the lattice's coordinate system
- For rational vectors from Smith normal form, may need manual computation
- `signature_pair()` returns (positive, negative) counts, not the signature itself