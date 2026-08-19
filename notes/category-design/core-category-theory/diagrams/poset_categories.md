<!--
Origin: gitclones/Coxeter/implementation/planning/diagrams/poset_categories.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Poset Categories: From Order Relations to Categories

Every poset (partially ordered set) naturally gives rise to a category, and every finite category with at most one morphism between any two objects comes from a poset. This is a fundamental construction that provides easy diagram categories for limits and colimits.

---

## Mathematical Foundation

### **Poset → Category Construction**

Given a poset (P, ≤), we construct a category **P** as follows:

- **Objects**: Elements of P
- **Morphisms**: Hom(x,y) = {x → y} if x ≤ y, ∅ otherwise
- **Composition**: Unique morphism composition (transitivity of ≤)
- **Identities**: x → x (reflexivity of ≤)

### **Key Properties**

1. **Thin Category**: At most one morphism between any two objects
2. **Skeletal**: No non-trivial isomorphisms (antisymmetry of ≤)
3. **Natural Diagrams**: Poset categories are perfect indexing categories for universal constructions

---

## Implementation Plan

### **1. Basic Poset Category Constructor**

```python
class PosetCategory(Category):
    """
    Category constructed from a poset.
    
    Given a poset (P, ≤), constructs the corresponding thin category
    where morphisms correspond to order relations.
    
    EXAMPLES::
    
        sage: # From a finite poset
        sage: P = Poset({1: [2, 3], 2: [4], 3: [4]})
        sage: C = PosetCategory(P)
        sage: C
        Category from poset with 4 elements
        
        sage: # Objects are poset elements
        sage: C.objects()
        [1, 2, 3, 4]
        
        sage: # Morphisms exist iff x ≤ y
        sage: C.hom_set(1, 4)  # 1 ≤ 4, so one morphism
        {1 → 4}
        sage: C.hom_set(2, 3)  # 2 ≰ 3, so no morphisms
        {}
    """
    
    def __init__(self, poset):
        """
        INPUT:
        - poset: A Poset object from SageMath
        
        EXAMPLES::
        
            sage: P = Poset([[1,2], [1,3], [2,4], [3,4]])
            sage: C = PosetCategory(P)
        """
        self._poset = poset
        super().__init__()
    
    def objects(self):
        """Return the objects (elements of the poset)."""
        return list(self._poset)
    
    def hom_set(self, x, y):
        """
        Return morphisms from x to y.
        
        Non-empty iff x ≤ y in the poset.
        """
        if self._poset.le(x, y):
            return {PosetMorphism(x, y, self)}
        else:
            return set()
    
    def compose(self, f, g):
        """
        Compose morphisms (uses transitivity of ≤).
        
        If f: y → z and g: x → y, then f ∘ g: x → z.
        """
        if f.domain() != g.codomain():
            raise ValueError("Morphisms not composable")
        return PosetMorphism(g.domain(), f.codomain(), self)
    
    def identity_morphism(self, x):
        """Return identity morphism x → x."""
        return PosetMorphism(x, x, self)
    
    def is_connected(self):
        """Test if poset is connected (as a category)."""
        return self._poset.is_connected()
    
    def has_initial_object(self):
        """Test if poset has minimum element."""
        return self._poset.has_bottom()
    
    def initial_object(self):
        """Return minimum element if it exists."""
        if self.has_initial_object():
            return self._poset.bottom()
        return None
    
    def has_terminal_object(self):
        """Test if poset has maximum element."""
        return self._poset.has_top()
    
    def terminal_object(self):
        """Return maximum element if it exists."""
        if self.has_terminal_object():
            return self._poset.top()
        return None

class PosetMorphism:
    """
    A morphism in a poset category.
    
    Represents the unique morphism x → y when x ≤ y.
    """
    
    def __init__(self, source, target, category):
        self._source = source
        self._target = target
        self._category = category
        
        # Verify x ≤ y
        if not category._poset.le(source, target):
            raise ValueError(f"No morphism {source} → {target}: not {source} ≤ {target}")
    
    def domain(self):
        return self._source
    
    def codomain(self):
        return self._target
    
    def __repr__(self):
        return f"{self._source} → {self._target}"
    
    def __eq__(self, other):
        """Morphisms equal iff same domain and codomain."""
        return (isinstance(other, PosetMorphism) and
                self._source == other._source and
                self._target == other._target)
    
    def __hash__(self):
        return hash((self._source, self._target))
    
    def __mul__(self, other):
        """Composition via category."""
        return self._category.compose(self, other)
```

### **2. Standard Poset Constructions**

```python
def chain_category(n):
    """
    Linear order category: 0 → 1 → 2 → ... → n-1.
    
    This is the category corresponding to a chain of length n.
    Perfect for constructing simplicial objects.
    
    EXAMPLES::
    
        sage: C = chain_category(4)  # 0 → 1 → 2 → 3
        sage: C.objects()
        [0, 1, 2, 3]
        sage: len(C.hom_set(0, 3))  # 0 ≤ 3, so one morphism
        1
    """
    chain_poset = Poset([list(range(n)), lambda i, j: i <= j])
    return PosetCategory(chain_poset)

def discrete_category(objects):
    """
    Discrete category: no morphisms except identities.
    
    Perfect indexing category for products and coproducts.
    
    EXAMPLES::
    
        sage: C = discrete_category(['a', 'b', 'c'])
        sage: C.objects()
        ['a', 'b', 'c']
        sage: len(C.hom_set('a', 'b'))  # No morphisms between distinct objects
        0
    """
    # Discrete poset: x ≤ y iff x = y
    discrete_poset = Poset([objects, lambda x, y: x == y])
    return PosetCategory(discrete_poset)

def parallel_pair_category():
    """
    Category with two objects and two parallel morphisms.
    
    Perfect for equalizers and coequalizers: X ⟹ Y.
    
    Structure:
    - Objects: {0, 1}  
    - Morphisms: id₀, id₁, f: 0 → 1, g: 0 → 1
    
    EXAMPLES::
    
        sage: C = parallel_pair_category()
        sage: # This is NOT a poset category! Need different construction.
    """
    # NOTE: This requires extending beyond posets since we have
    # two morphisms 0 → 1, violating the "thin" property
    raise NotImplementedError("Parallel pairs require non-poset categories")

def span_category():
    """
    Span category: 1 ← 0 → 2.
    
    Perfect for pushouts and colimits over spans.
    
    EXAMPLES::
    
        sage: C = span_category()
        sage: C.objects() 
        [0, 1, 2]
        sage: # 0 is the "central" object
    """
    # This is NOT a poset since 1 and 2 are incomparable
    # but both have morphisms from 0
    span_relations = [(0, 1), (0, 2)]  # 0 ≤ 1, 0 ≤ 2, but 1 ≰ 2, 2 ≰ 1
    span_poset = Poset([span_relations])
    return PosetCategory(span_poset)

def cospan_category():
    """
    Cospan category: 1 → 0 ← 2.
    
    Perfect for pullbacks and limits over cospans.
    
    EXAMPLES::
    
        sage: C = cospan_category()
        sage: C.objects()
        [0, 1, 2] 
        sage: # 0 is the "target" object
    """
    # Relations: 1 ≤ 0, 2 ≤ 0, but 1 ≰ 2, 2 ≰ 1
    cospan_relations = [(1, 0), (2, 0)]
    cospan_poset = Poset([cospan_relations])
    return PosetCategory(cospan_poset)
```

### **3. Diagram Construction from Functors**

```python
class PosetDiagram:
    """
    A diagram indexed by a poset category.
    
    This is a functor F: P → C where P is a poset category
    and C is any target category.
    """
    
    def __init__(self, poset_category, target_category, object_map, morphism_map=None):
        """
        INPUT:
        - poset_category: PosetCategory (indexing category)
        - target_category: Category (target category)  
        - object_map: dict {p ∈ P : F(p) ∈ C}
        - morphism_map: optional dict for morphism images
        
        EXAMPLES::
        
            sage: # Diagram for product A × B
            sage: discrete = discrete_category([0, 1])
            sage: Groups = Groups()
            sage: diagram = PosetDiagram(
            ....:     discrete, 
            ....:     Groups,
            ....:     {0: CyclicGroup(4), 1: CyclicGroup(6)}
            ....: )
        """
        self.index_category = poset_category
        self.target_category = target_category
        self.object_map = object_map
        self.morphism_map = morphism_map or {}
        
    def eval_object(self, p):
        """Evaluate functor at object p: returns F(p)."""
        return self.object_map[p]
    
    def eval_morphism(self, f):
        """
        Evaluate functor at morphism f: p → q.
        
        Returns F(f): F(p) → F(q) in target category.
        """
        if f in self.morphism_map:
            return self.morphism_map[f]
        else:
            # Default: if not specified, use identity when possible
            p, q = f.domain(), f.codomain()
            F_p, F_q = self.eval_object(p), self.eval_object(q)
            
            if F_p == F_q:
                return self.target_category.identity_morphism(F_p)
            else:
                raise ValueError(f"No morphism specified for {f} and F({p}) ≠ F({q})")
    
    def limit(self):
        """Compute limit of this diagram in target category."""
        return self.target_category.limit(self)
    
    def colimit(self):
        """Compute colimit of this diagram in target category."""
        return self.target_category.colimit(self)
```

---

## Usage Examples

### **1. Products via Discrete Diagrams**

```python
# Product of two groups
discrete_two = discrete_category([0, 1])
Groups = Groups()

product_diagram = PosetDiagram(
    discrete_two,
    Groups, 
    {0: CyclicGroup(4), 1: CyclicGroup(6)}
)

# Limit gives product
product_group, projections = product_diagram.limit()
# product_group ≅ C₄ × C₆ ≅ C₁₂
```

### **2. Chains for Filtered Objects**

```python
# Filtered module: M₀ ⊆ M₁ ⊆ M₂ ⊆ M₃
chain = chain_category(4)
Modules_ZZ = Modules(ZZ)

filtration_diagram = PosetDiagram(
    chain,
    Modules_ZZ,
    {0: ZZ, 1: 2*ZZ, 2: 4*ZZ, 3: 8*ZZ},
    # Morphisms are inclusions
    morphism_map = {
        chain.hom_set(0,1).pop(): inclusion_2ZZ_to_ZZ,
        chain.hom_set(1,2).pop(): inclusion_4ZZ_to_2ZZ,
        # etc.
    }
)

# Colimit gives quotient by "eventual image"
colimit_module = filtration_diagram.colimit()
```

### **3. Pullbacks via Cospan Diagrams**

```python
# Pullback of f: X → Z ← Y: g
cospan = cospan_category()  # 1 → 0 ← 2

pullback_diagram = PosetDiagram(
    cospan,
    Sets,
    {0: Z, 1: X, 2: Y},
    morphism_map = {
        cospan.hom_set(1,0).pop(): f,  # X → Z
        cospan.hom_set(2,0).pop(): g   # Y → Z  
    }
)

# Limit gives pullback
pullback_object, projections = pullback_diagram.limit()
# pullback_object = {(x,y) ∈ X×Y : f(x) = g(y)}
```

---

## Benefits of This Approach

### **1. Mathematical Clarity**
- **Natural**: Posets → categories is a fundamental construction
- **Intuitive**: Order relations become morphisms
- **Standard**: Used throughout category theory literature

### **2. Easy Diagram Construction**
- **Built-in shapes**: chains, discrete sets, spans, cospans
- **Flexible**: Can represent any thin diagram
- **Composable**: Easy to combine and modify

### **3. Universal Properties**
- **Automatic limits**: Initial/terminal objects from min/max elements  
- **Natural indexing**: Perfect for products, equalizers, filtered colimits
- **Clean notation**: Diagrams look like their mathematical descriptions

### **4. Implementation Benefits**
- **Efficient**: Thin categories have simple morphism structure
- **Cacheable**: Finite posets give finite categories
- **Debuggable**: Easy to visualize and understand

This provides the foundation for easy diagram category construction that we need for implementing universal properties properly!