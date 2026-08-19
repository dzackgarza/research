<!--
Origin: gitclones/Coxeter/research/explorations/implementation-notes/chain_complexes.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of this
corpus.
-->

# Chain Complex Categories: Ch(C)

The category of chain complexes over an abelian category, where exactness is a natural property of sequences.

---

## Mathematical Definition

For an abelian category **C**, the category **Ch(C)** consists of:
- **Objects**: Chain complexes `(C•, d•)` where:
  - `C_n` ∈ C for all n ∈ ℤ
  - `d_n: C_n → C_{n-1}` (differentials)
  - `d_{n-1} ∘ d_n = 0` (equivalently: im(d_n) ⊆ ker(d_{n-1}))

- **Morphisms**: Chain maps `f: (C•, d^C) → (D•, d^D)` where:
  - `f_n: C_n → D_n` for all n
  - `f_{n-1} ∘ d^C_n = d^D_n ∘ f_n` (commutes with differentials)

---

## Implementation

```python
class ChainComplexes(Category):
    """
    The category Ch(C) of chain complexes over an abelian category C.
    
    EXAMPLES::
    
        sage: from sage.categories.chain_complexes import ChainComplexes
        sage: Ch_Mod_ZZ = ChainComplexes(Modules(ZZ))
        sage: Ch_Mod_ZZ
        Category of chain complexes over Category of modules over Integer Ring
        
        sage: # Create a simple complex 0 → Z → Z → Z → 0
        sage: C = ChainComplex({0: ZZ, 1: ZZ, 2: ZZ}, 
        ....:                  {1: matrix([[2]]), 2: matrix([[3]])})
        sage: C in Ch_Mod_ZZ
        True
    """
    
    def __init__(self, base_category):
        """
        Initialize Ch(C) for an abelian category C.
        
        INPUT:
        - base_category: An abelian category
        """
        if base_category not in AbelianCategories():
            raise ValueError("Base must be an abelian category")
        self._base_category = base_category
        super().__init__()
    
    def super_categories(self):
        """Ch(C) is itself an abelian category!"""
        return [AbelianCategories()]
    
    def _repr_(self):
        return f"Category of chain complexes over {self._base_category}"
    
    class ParentMethods:
        """Methods for chain complex objects."""
        
        def is_exact(self):
            """
            Test if this chain complex is exact everywhere.
            
            A complex is exact if im(d_n) = ker(d_{n-1}) at each degree.
            
            EXAMPLES::
            
                sage: # Exact sequence 0 → Z →×2 Z →/2 Z/2Z → 0
                sage: C = ChainComplex({0: ZZ, 1: ZZ, 2: ZZ.quotient(2*ZZ)},
                ....:                  {1: matrix([[2]]), 2: ZZ.quotient_map(2*ZZ)})
                sage: C.is_exact()
                True
                
                sage: # Non-exact: 0 → Z →×2 Z →×3 Z → 0
                sage: D = ChainComplex({0: ZZ, 1: ZZ, 2: ZZ},
                ....:                  {1: matrix([[2]]), 2: matrix([[3]])})
                sage: D.is_exact()
                False  # im(×2) ≠ ker(×3)
            """
            for n in self.degree_range():
                if not self.is_exact_at(n):
                    return False
            return True
        
        def is_exact_at(self, n):
            """
            Test exactness at degree n: im(d_{n+1}) = ker(d_n).
            
            INPUT:
            - n: degree to test exactness at
            
            EXAMPLES::
            
                sage: # 0 → Z →×2 Z → Z/2Z → 0
                sage: C = ChainComplex({0: ZZ, 1: ZZ, 2: ZZ/(2*ZZ)})
                sage: C.is_exact_at(1)  # Exact at middle term
                True
            """
            # Get the relevant differentials
            d_into = self.differential(n+1)  # C_{n+1} → C_n
            d_from = self.differential(n)     # C_n → C_{n-1}
            
            # Handle boundary cases
            if d_into is None:  # No map into degree n
                return d_from is None or d_from.is_zero()
            if d_from is None:  # No map from degree n  
                return d_into is None or d_into.is_zero()
            
            # Check im(d_{n+1}) = ker(d_n)
            image = d_into.image()[0]
            kernel = d_from.kernel()[0]
            return image == kernel
        
        def homology(self, n):
            """
            Compute the n-th homology H_n = ker(d_n) / im(d_{n+1}).
            
            EXAMPLES::
            
                sage: # Complex with homology: 0 → Z →×2 Z →0 Z → 0
                sage: C = ChainComplex({0: ZZ, 1: ZZ, 2: ZZ},
                ....:                  {1: matrix([[2]]), 2: matrix([[0]])})
                sage: C.homology(1)
                Z/2Z  # ker(0) / im(×2) = Z / 2Z
            """
            d_from = self.differential(n)     # C_n → C_{n-1}
            d_into = self.differential(n+1)   # C_{n+1} → C_n
            
            # Compute kernel
            if d_from is None or d_from.is_zero():
                kernel = self[n]  # Whole module
            else:
                kernel = d_from.kernel()[0]
            
            # Compute image  
            if d_into is None or d_into.is_zero():
                image = self[n].zero_submodule()
            else:
                image = d_into.image()[0]
            
            # Return quotient
            return kernel / image
        
        def is_acyclic(self):
            """
            Test if the complex is acyclic (all homology vanishes).
            
            Equivalent to being exact except possibly at the ends.
            
            EXAMPLES::
            
                sage: # Acyclic complex (exact everywhere)
                sage: C = ChainComplex({0: ZZ, 1: ZZ}, {1: identity_matrix(1)})
                sage: C.is_acyclic()
                True
            """
            for n in self.degree_range():
                if not self.homology(n).is_zero():
                    return False
            return True
        
        def __getitem__(self, n):
            """
            Get the module at degree n: C[n] = C_n.
            
            Natural notation for accessing terms.
            """
            return self.module(n)
        
        def shift(self, k):
            """
            Shift complex by k: (C[k])_n = C_{n-k}.
            
            The suspension/desuspension functor.
            """
            return ShiftedComplex(self, k)
        
        def truncate(self, low=None, high=None):
            """
            Truncate complex to degrees [low, high].
            
            Smart truncation that preserves homology where possible.
            """
            return TruncatedComplex(self, low, high)
        
        def cone(self, morphism):
            """
            Mapping cone of a chain map f: self → other.
            
            Fundamental construction: Cone(f)_n = other_n ⊕ self_{n-1}.
            """
            return MappingCone(morphism)

class ChainComplex:
    """
    A chain complex in Ch(C), specified by its differentials.
    
    KEY INSIGHT: A complex is entirely determined by its morphisms!
    The objects are just the domains and codomains.
    
    EXAMPLES::
    
        sage: # Short exact sequence 0 → A →f B →g C → 0
        sage: C = ChainComplex([f, g])
        sage: C
        A --f--> B --g--> C
        sage: C.is_exact()
        True
        
        sage: # Koszul complex for x,y in ZZ[x,y]  
        sage: R = PolynomialRing(ZZ, 'x,y')
        sage: x, y = R.gens()
        sage: d1 = R^2.hom([[x, y]], R)         # R^2 → R
        sage: d2 = R.hom([[-y], [x]], R^2)      # R → R^2
        sage: koszul = ChainComplex([d2, d1])
        sage: koszul
        R --[[-y],[x]]--> R^2 --[[x,y]]--> R
        sage: koszul.is_exact()
        True  # Exact except at ends
        
        sage: # Even simpler with operator notation
        sage: C = f >> g >> h  # Creates complex from morphism chain!
    """
    
    def __init__(self, morphisms, start_degree=0):
        """
        Create a chain complex from a list of morphisms.
        
        INPUT:
        - morphisms: list [d_n, d_{n-1}, ..., d_1] where d_i: A_i → A_{i-1}
        - start_degree: degree of the first domain (default 0)
        
        The complex looks like:
        ... → A_n →d_n A_{n-1} → ... → A_1 →d_1 A_0 → ...
        """
        self._morphisms = morphisms
        self._start_degree = start_degree
        
        # Verify composition is zero
        for i in range(len(morphisms) - 1):
            d_i = morphisms[i]
            d_next = morphisms[i + 1]
            
            # Check d_i ∘ d_{i+1} = 0
            if d_i.domain() != d_next.codomain():
                raise ValueError(f"Morphisms not composable: {d_next} and {d_i}")
            
            comp = d_i * d_next
            if not comp.is_zero():
                raise ValueError(f"d² ≠ 0: {d_next} ∘ {d_i} ≠ 0")
        
        # Build the sequence of objects
        self._objects = []
        if morphisms:
            # Start with domain of last morphism
            self._objects.append(morphisms[-1].domain())
            # Add codomains
            for m in reversed(morphisms):
                self._objects.append(m.codomain())
    
    def __repr__(self):
        """Natural representation as a sequence with arrows."""
        if not self._morphisms:
            return "Empty complex"
        
        parts = [str(self._objects[0])]
        for i, morphism in enumerate(reversed(self._morphisms)):
            parts.append(f"--{morphism}-->")
            parts.append(str(self._objects[i + 1]))
        
        return " ".join(parts)
    
    @classmethod  
    def from_morphism_chain(cls, first_morphism):
        """
        Build complex from chained morphisms using >> operator.
        
        EXAMPLES::
        
            sage: # Build using >> operator
            sage: C = ChainComplex.from_morphism_chain(f >> g >> h)
            sage: C
            A --f--> B --g--> C --h--> D
        """
        # Extract morphisms from the chain
        morphisms = []
        current = first_morphism
        
        while hasattr(current, '_next_morphism'):
            morphisms.append(current._morphism)
            current = current._next_morphism
        morphisms.append(current)
        
        return cls(list(reversed(morphisms)))
    
    def differential(self, n):
        """Get d_n: C_n → C_{n-1}."""
        idx = n - self._start_degree
        if 0 <= idx < len(self._morphisms):
            return self._morphisms[idx]
        return None
    
    def __getitem__(self, n):
        """Get object at degree n: C[n] = C_n."""
        idx = n - self._start_degree
        if idx < 0:
            return None
        elif idx < len(self._objects):
            return self._objects[idx]
        else:
            return None


# Make morphisms chainable with >>
class ChainableMorphism:
    """Wrapper to make morphisms chainable with >>."""
    
    def __init__(self, morphism, previous=None):
        self._morphism = morphism
        self._previous = previous
    
    def __rshift__(self, other):
        """Chain morphisms: f >> g creates a complex."""
        if isinstance(other, Morphism):
            # Verify composability
            if self._morphism.codomain() != other.domain():
                raise ValueError(f"Cannot chain {self._morphism} with {other}")
            return ChainableMorphism(other, self)
        else:
            raise TypeError(f"Cannot chain morphism with {type(other)}")
    
    def to_complex(self):
        """Convert chain to ChainComplex."""
        morphisms = []
        current = self
        while current:
            morphisms.append(current._morphism)
            current = current._previous
        return ChainComplex(morphisms)


# Enhance Morphism class
Morphism.__rshift__ = lambda self, other: ChainableMorphism(self) >> other
```

---

## The Beauty of Morphism-Based Complexes

Your insight that complexes are determined by morphisms gives us:

### 1. **Natural Construction**
```sage
# Just list the morphisms!
C = ChainComplex([f, g, h])  # A --f--> B --g--> C --h--> D

# Or use >> operator
C = f >> g >> h  # Even more natural!
```

### 2. **No Index Bookkeeping**
```sage
# Old way (ugly):
C = ChainComplex({0: A, 1: B, 2: C}, {1: f, 2: g})

# New way (clean):
C = ChainComplex([f, g])  # Objects inferred from morphisms!
```

### 3. **Mathematical Printing**
```sage
sage: C
A --f--> B --g--> C  # Exactly how we write it!
```

---

## Natural Operations on Chain Complexes

### Direct Sum: `C + D`
```sage
sage: C = ChainComplex({0: ZZ, 1: ZZ}, {1: matrix([[2]])})
sage: D = ChainComplex({0: ZZ, 1: ZZ}, {1: matrix([[3]])}) 
sage: (C + D)[1]  
ZZ ⊕ ZZ  # Direct sum at each degree
```

### Tensor Product: `C ⊗ D`
```sage
sage: C ⊗ D  # Total complex of the double complex
```

### Shift/Suspension: `C[1]`
```sage
sage: C[1]  # Shift by 1: (C[1])_n = C_{n-1}
```

---

## Special Constructors

### Short Exact Sequences
```sage
# Natural construction from morphisms
ses = ShortExactSequence(i, p)  # 0 → A →i B →p C → 0
ses.is_exact()  # Always True by construction
ses.is_split()  # Check if it splits
```

### Long Exact Sequences  
```sage
# From a list of morphisms
les = LongExactSequence([f1, f2, f3, f4, f5])
les.connecting_morphisms()  # Extract the connecting maps
```

### Resolutions
```sage
# Build resolutions as complexes
P = M.projective_resolution()  # Returns a ChainComplex!
P.morphisms  # [P_n → P_{n-1}, ..., P_1 → P_0 → M]
```

---

## Why This Design is Superior

### 1. **Exactness Where It Belongs**
```sage
# Old way (awkward):
sage: f.is_exact_at(g)  # What does this even mean?

# New way (natural):
sage: C.is_exact()      # Is the complex exact?
sage: C.is_exact_at(n)  # Is it exact at degree n?
```

### 2. **Sequences Are First-Class Objects**
```sage
# Create a short exact sequence
sage: ses = ShortExactSequence(A, B, C, i, p)
sage: ses.is_exact()  # Of course it is!
sage: ses.splitting()  # Find a splitting if one exists
```

### 3. **Natural Constructions**
```sage
# Mapping cone sequence
sage: f: A → B
sage: cone_seq = f.mapping_cone_sequence()
sage: # A → B → Cone(f) → A[-1]
sage: cone_seq.is_exact()  # Always true!
```

### 4. **Connects to Homological Algebra**
```sage
# Compute Ext via resolutions
sage: P = M.projective_resolution()  # A chain complex!
sage: Ext_complex = Hom(P, N)  # Complex of hom groups
sage: Ext_n = Ext_complex.homology(n)  # Ext^n(M, N)
```

---

## The Big Picture

By making Ch(C) a proper category:
1. **Exactness** becomes a property of sequences (where it belongs)
2. **Chain complexes** become first-class mathematical objects
3. **Natural constructions** (cone, cylinder, suspension) just work
4. **Homological algebra** flows naturally from the structure

This follows our philosophy: the natural mathematical structure (chain complexes form a category) should be reflected directly in the code!