<!--
Origin: gitclones/Coxeter-v2/archive/cold_storage_pre_integration/background-research/sage-planning/modules_bak/RMod/RMod_subobjects.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Submodule Testing with <= Operator

Implementation of natural submodule testing notation: `S <= M` means "S is a submodule of M".

## Current SageMath Behavior

```sage
# Current verbose syntax:
sage: V = QQ^3
sage: S = V.submodule([V.0 + V.1, V.1 + V.2])
sage: T = V.submodule([V.0, V.1, V.2])  # T = V

# Test if S is submodule of T
sage: S.is_submodule_of(T)  # Verbose method call
True

# No natural notation equivalent
```

## Proposed Enhancement

```sage
# Natural mathematical notation:
sage: S <= V  # Should return True (S is submodule of V)
True

sage: V <= S  # Should return False (V is not submodule of S)
False

sage: S <= S  # Should return True (reflexive)
True
```

## Implementation via __le__ Override

```python
class RModule(Module):
    """R-module with natural submodule testing notation."""
    
    def __le__(self, other):
        """
        Test if self is a submodule of other.
        
        Uses the <= operator for natural mathematical notation.
        
        INPUT:
        - other -- another R-module over the same base ring
        
        OUTPUT:
        - True if self ⊆ other as R-modules, False otherwise
        
        EXAMPLES::
        
            sage: V = QQ^3
            sage: S = V.submodule([V.0 + V.1, V.1 + V.2])
            sage: T = V.submodule([V.0, V.1])
            
            # Natural submodule testing
            sage: S <= V
            True
            
            sage: T <= V  
            True
            
            sage: S <= T
            False
            
            sage: T <= S
            False
            
            # Reflexivity
            sage: S <= S
            True
            
            # Zero submodule
            sage: zero = V.submodule([])
            sage: zero <= S
            True
            
            # Different ambient spaces should raise error
            sage: W = QQ^2
            sage: U = W.submodule([W.0])
            sage: S <= U
            TypeError: Cannot compare submodules from different ambient spaces
        """
        # Type checking
        if not isinstance(other, Module):
            return NotImplemented  # Let Python try other.__ge__
        
        # Must be modules over the same base ring
        if self.base_ring() != other.base_ring():
            raise TypeError(f"Cannot compare modules over different base rings: {self.base_ring()} vs {other.base_ring()}")
        
        # For submodules, check if they have the same ambient space
        if hasattr(self, 'ambient_module') and hasattr(other, 'ambient_module'):
            if self.ambient_module() != other.ambient_module():
                raise TypeError("Cannot compare submodules from different ambient spaces")
        
        # Use the existing is_submodule_of method
        return self.is_submodule_of(other)
    
    def __ge__(self, other):
        """
        Test if other is a submodule of self.
        
        Implements other <= self via self >= other.
        """
        if not isinstance(other, Module):
            return NotImplemented
        
        return other.__le__(self)
    
    def __lt__(self, other):
        """
        Test if self is a proper submodule of other.
        
        Returns True iff self <= other and self != other.
        """
        if not isinstance(other, Module):
            return NotImplemented
        
        return self <= other and self != other
    
    def __gt__(self, other):
        """
        Test if other is a proper submodule of self.
        
        Returns True iff other < self.
        """
        if not isinstance(other, Module):
            return NotImplemented
        
        return other < self
```

## Extended Lattice Operations

```python
class RModule(Module):
    """Enhanced R-module with natural lattice operations."""
    
    def __add__(self, other):
        """
        Context-dependent addition: submodule sum vs direct sum.
        
        MATHEMATICAL DISTINCTION:
        - If M, N ≤ A (submodules of same ambient A): M + N = ⟨M ∪ N⟩ ≤ A
        - If M, N are independent modules: M + N = M ⊕ N (external direct sum)
        
        INPUT:
        - other -- another R-module
        
        OUTPUT:
        - Submodule sum ⟨M ∪ N⟩ if both are submodules of same ambient space
        - External direct sum M ⊕ N if modules are independent
        
        EXAMPLES::
        
            sage: V = QQ^3
            
            # Case 1: Submodules of same ambient space (INNER sum)
            sage: S = V.submodule([V.0, V.1])      # Span{e₁, e₂} ≤ V
            sage: T = V.submodule([V.1, V.2])      # Span{e₂, e₃} ≤ V
            sage: U = S + T                        # ⟨S ∪ T⟩ = Span{e₁, e₂, e₃} = V
            sage: U == V
            True
            sage: U <= V  # Result is submodule of V
            True
            
            # Case 2: Independent modules (OUTER direct sum)
            sage: W = QQ^2  # Independent from V
            sage: X = V + W  # This is V ⊕ W (5-dimensional)
            sage: X.rank()
            5  # rank(V) + rank(W) = 3 + 2
            sage: X.ambient_module() is None  # Not a submodule
            True
            
            # Case 3: Intersection vs direct sum
            sage: P = V.submodule([V.0])           # 1-dimensional
            sage: Q = V.submodule([V.1])           # 1-dimensional  
            sage: R = P + Q                        # Submodule sum in V
            sage: R.rank()
            2  # Span{e₁, e₂} has rank 2
            sage: R <= V
            True
            
            # If P, Q were independent modules instead:
            sage: P_indep = QQ^1  # Independent 1D module
            sage: Q_indep = QQ^1  # Another independent 1D module
            sage: direct = P_indep + Q_indep  # External direct sum
            sage: direct.rank()
            2  # Still rank 2, but now it's QQ^1 ⊕ QQ^1 ≅ QQ^2
        """
        if not isinstance(other, Module):
            return NotImplemented
        
        # Check compatibility
        if self.base_ring() != other.base_ring():
            raise TypeError(f"Cannot add modules over different rings: {self.base_ring()} vs {other.base_ring()}")
        
        # CASE 1: Both are submodules of the same ambient space
        # → Return INNER sum: ⟨M ∪ N⟩ ≤ A
        if (hasattr(self, 'ambient_module') and hasattr(other, 'ambient_module') and 
            self.ambient_module() == other.ambient_module()):
            
            ambient = self.ambient_module()
            
            # Combine generators from both submodules
            self_gens = list(self.gens())
            other_gens = list(other.gens())
            all_gens = self_gens + other_gens
            
            # Return submodule of ambient space generated by union
            return ambient.submodule(all_gens)
        
        # CASE 2: Independent modules or different ambient spaces
        # → Return OUTER direct sum: M ⊕ N
        try:
            return self.direct_sum(other)
        except (AttributeError, TypeError):
            # Fallback: manual direct sum construction
            return DirectSumModule([self, other])
    
    def submodule_sum(self, other):
        """
        Explicit submodule sum: ⟨M ∪ N⟩ (inner sum).
        
        This method always computes the submodule generated by the union,
        regardless of context. Use this when you specifically want inner sum.
        
        INPUT:
        - other -- another submodule of the same ambient space
        
        OUTPUT:
        - Submodule ⟨M ∪ N⟩ of the common ambient space
        
        EXAMPLES::
        
            sage: V = QQ^3
            sage: S = V.submodule([V.0 + V.1])
            sage: T = V.submodule([V.1 + V.2])
            
            sage: # Explicit submodule sum
            sage: U = S.submodule_sum(T)
            sage: U.rank()
            3  # Generates all of V
            
            sage: # This is the same as S + T when both are submodules
            sage: U == S + T
            True
        """
        if not isinstance(other, Module):
            raise TypeError("Can only sum with another module")
        
        if self.base_ring() != other.base_ring():
            raise TypeError("Cannot sum modules over different rings")
        
        # Require same ambient space
        if not (hasattr(self, 'ambient_module') and hasattr(other, 'ambient_module')):
            raise TypeError("Both modules must be submodules for inner sum")
        
        if self.ambient_module() != other.ambient_module():
            raise TypeError("Modules must have the same ambient space for submodule sum")
        
        # Generate union
        ambient = self.ambient_module()
        all_gens = list(self.gens()) + list(other.gens())
        return ambient.submodule(all_gens)
    
    def direct_sum_with(self, other):
        """
        Explicit external direct sum: M ⊕ N (outer sum).
        
        This method always computes the external direct sum,
        regardless of whether the modules are related.
        
        INPUT:
        - other -- another R-module over the same base ring
        
        OUTPUT:
        - External direct sum M ⊕ N
        
        EXAMPLES::
        
            sage: V = QQ^2
            sage: W = QQ^3
            
            sage: # External direct sum
            sage: X = V.direct_sum_with(W)
            sage: X.rank()
            5  # 2 + 3
            
            sage: # Even for submodules, this creates external sum
            sage: S = V.submodule([V.0])  # 1D submodule of V
            sage: T = V.submodule([V.1])  # 1D submodule of V  
            sage: external = S.direct_sum_with(T)
            sage: external.rank()
            2  # 1 + 1, but NOT a submodule of V
            
            sage: # Compare with inner sum:
            sage: inner = S + T  # This gives 2D submodule of V
            sage: inner <= V
            True
            sage: external <= V  # This is False - external sum is independent
            False
        """
        if not isinstance(other, Module):
            raise TypeError("Can only take direct sum with another module")
        
        if self.base_ring() != other.base_ring():
            raise TypeError("Cannot take direct sum of modules over different rings")
        
        try:
            return self.direct_sum(other)
        except AttributeError:
            # Manual construction if direct_sum method not available
            return DirectSumModule([self, other])
    
    def intersection(self, other):
        """
        Submodule intersection: M ∩ N.
        
        EXAMPLES::
        
            sage: V = QQ^3
            sage: S = V.submodule([V.0 + V.1, V.1 + V.2])
            sage: T = V.submodule([V.0 + V.2, V.1])
            
            sage: I = S.intersection(T)
            sage: I <= S and I <= T
            True
        """
        if not isinstance(other, Module):
            raise TypeError("Can only intersect with another module")
        
        if self.base_ring() != other.base_ring():
            raise TypeError("Cannot intersect modules over different rings")
        
        # For submodules of the same ambient space
        if (hasattr(self, 'ambient_module') and hasattr(other, 'ambient_module') and
            self.ambient_module() == other.ambient_module()):
            
            # Use SageMath's built-in intersection if available
            if hasattr(self, 'intersection'):
                return super().intersection(other)
            
            # Manual computation via span intersection
            ambient = self.ambient_module()
            
            # Get matrices for both submodules
            self_matrix = matrix([g.list() for g in self.gens()]).transpose()
            other_matrix = matrix([g.list() for g in other.gens()]).transpose()
            
            # Solve the intersection problem
            # Elements in intersection satisfy: self_matrix * x = other_matrix * y
            combined = self_matrix.augment(-other_matrix)
            ker = combined.right_kernel()
            
            # Extract intersection generators
            n_self = len(self.gens())
            intersection_gens = []
            for v in ker.gens():
                coeffs = v[:n_self]
                gen = sum(c * g for c, g in zip(coeffs, self.gens()))
                if gen != 0:
                    intersection_gens.append(gen)
            
            return ambient.submodule(intersection_gens)
        
        raise NotImplementedError("Intersection not implemented for general modules")
```

## Mathematical Background: Inner vs Outer Sums

The `+` operator for modules has a **context-dependent meaning** that depends on the mathematical setting:

### Inner Sum (Submodules of Same Ambient Space)

When `M, N ≤ A` are both submodules of the same ambient module `A`:
```
M + N = ⟨M ∪ N⟩ = {m + n : m ∈ M, n ∈ N} ≤ A
```

**Properties:**
- The result is a submodule of the same ambient space `A`
- `rank(M + N) ≤ rank(M) + rank(N)` (equality iff `M ∩ N = 0`)
- `M + N` contains both `M` and `N` as submodules
- This is the **join** in the lattice of submodules of `A`

**Examples:**
```sage
sage: V = QQ^3
sage: M = V.submodule([V.0, V.1])        # Span{e₁, e₂}
sage: N = V.submodule([V.1, V.2])        # Span{e₂, e₃}  
sage: M + N == V                         # Span{e₁, e₂, e₃} = V
True
sage: (M + N) <= V                       # Result is submodule of V
True
```

### Outer Sum (Independent Modules)

When `M` and `N` are independent modules (no common ambient space):
```
M + N = M ⊕ N = {(m, n) : m ∈ M, n ∈ N}
```

**Properties:**
- The result is a new module, not embedded in either `M` or `N`
- `rank(M ⊕ N) = rank(M) + rank(N)` (always)
- `M` and `N` appear as direct summands, not submodules
- This is the **coproduct** in the category of R-modules

**Examples:**
```sage
sage: V = QQ^2
sage: W = QQ^3
sage: X = V + W                          # External direct sum V ⊕ W
sage: X.rank()
5                                        # 2 + 3 = 5
sage: X.ambient_module() is None         # Not a submodule of anything
True
```

### The Subtlety

The same notation `M + N` means different things depending on context:

```sage
# Case 1: Submodules of same ambient space → inner sum
sage: V = QQ^3
sage: S = V.submodule([V.0])             # 1D submodule
sage: T = V.submodule([V.1])             # 1D submodule
sage: inner = S + T                      # ⟨S ∪ T⟩ ⊆ V
sage: inner.rank(), inner <= V
(2, True)                                # 2D submodule of V

# Case 2: Independent modules → outer sum  
sage: S_indep = QQ^1                     # Independent 1D module
sage: T_indep = QQ^1                     # Another independent 1D module
sage: outer = S_indep + T_indep          # S ⊕ T ≅ QQ^2
sage: outer.rank(), hasattr(outer, 'ambient_module')
(2, False)                               # 2D module, not a submodule
```

### Implementation Strategy

Our `__add__` method uses **context detection**:

1. **Check ambient spaces**: If both modules have the same `ambient_module()`, use inner sum
2. **Otherwise**: Use outer direct sum

This matches mathematical convention while providing explicit methods when needed:
- `M.submodule_sum(N)` - Always inner sum ⟨M ∪ N⟩
- `M.direct_sum_with(N)` - Always outer sum M ⊕ N

## Usage Examples

```sage
# Basic submodule testing
sage: V = QQ^4
sage: S = V.submodule([V.0 + V.1, V.2 + V.3])
sage: T = V.submodule([V.0, V.1, V.2, V.3])  # T = V

sage: S <= V  # Natural notation!
True

sage: V <= S  # Reverse inclusion
False

sage: S <= S  # Reflexive
True

# Proper submodules
sage: S < V   # S is proper submodule of V
True

sage: V < S   # V is not proper submodule of S
False

# Lattice operations
sage: P = V.submodule([V.0, V.1])
sage: Q = V.submodule([V.1, V.2])

sage: R = P + Q  # Submodule sum
sage: R.rank()
3

sage: I = P.intersection(Q)  # Should be span{V.1}
sage: I.rank()
1

# Chain of inclusions
sage: zero = V.submodule([])
sage: line = V.submodule([V.0])
sage: plane = V.submodule([V.0, V.1])

sage: zero <= line <= plane <= V
True

sage: zero < line < plane < V  # All proper inclusions
True
```

## Benefits

### 1. **Mathematical Naturalness**
- `S <= M` matches handwritten mathematics exactly
- Much clearer than `S.is_submodule_of(M)`
- Supports chained comparisons: `A <= B <= C`

### 2. **Lattice Structure**
- Natural `<`, `<=`, `>`, `>=` for submodule lattice
- Enables sorting and ordering of submodules
- Works with Python's `min()`, `max()`, `sorted()`

### 3. **Extended Operations**
- `S + T` for submodule sum (when unambiguous)
- `S.intersection(T)` for submodule intersection
- Rich algebraic structure on submodule lattice

### 4. **Error Handling**
- Clear errors for incompatible modules
- Type checking prevents nonsensical comparisons
- Graceful fallback for unsupported operations

## Implementation Notes

### 1. **Compatibility**
- `NotImplemented` return allows other types to handle comparison
- Preserves existing `is_submodule_of` method for explicit calls
- Works with existing SageMath module hierarchy

### 2. **Performance**
- Delegates to existing optimized `is_submodule_of` implementations
- No performance penalty over current methods
- Could cache results for repeated queries

### 3. **Type Safety**
- Checks base ring compatibility before comparison
- Ensures submodules belong to same ambient space
- Clear error messages for invalid operations

This enhancement makes submodule testing dramatically more natural and aligns SageMath with standard mathematical notation!
