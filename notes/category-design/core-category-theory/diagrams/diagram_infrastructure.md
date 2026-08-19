<!--
Origin: gitclones/Coxeter/implementation/planning/diagrams/diagram_infrastructure.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Diagram, Cone, and Cocone Infrastructure

This document outlines the implementation of the fundamental infrastructure for limits and colimits in SageMath categories: Diagrams, Cones, and Cocones.

---

## Mathematical Foundation

### **Diagrams**
A diagram D of shape J in category C is a functor D: J → C.
- **J**: Index category (often small)
- **C**: Target category
- **D**: Assigns objects and morphisms from J to objects and morphisms in C

### **Cones**
A cone over diagram D: J → C consists of:
- **Apex**: An object N in C
- **Projections**: Family of morphisms πⱼ: N → D(j) for each j ∈ J
- **Coherence**: For each f: j → k in J, we have D(f) ∘ πⱼ = πₖ

### **Cocones**
A cocone under diagram D: J → C consists of:
- **Nadir**: An object N in C  
- **Injections**: Family of morphisms ιⱼ: D(j) → N for each j ∈ J
- **Coherence**: For each f: j → k in J, we have ιₖ ∘ D(f) = ιⱼ

### **Limits and Colimits**
- **Limit**: Universal cone (initial in category of cones)
- **Colimit**: Universal cocone (terminal in category of cocones)

---

## Implementation Plan

### **1. Base Diagram Class**

```python
class Diagram:
    """
    A diagram in a category, represented as a functor F: J → C.
    
    A diagram consists of an index category J, a target category C,
    and mappings for objects and morphisms that define a functor.
    
    EXAMPLES::
    
        sage: # Simple diagram for product A × B
        sage: J = discrete_category([0, 1])
        sage: C = Sets()
        sage: D = Diagram(J, C, {0: ZZ, 1: QQ})
        sage: D
        Diagram from Discrete category on {0, 1} to Category of sets
        
        sage: # Parallel pair for equalizer
        sage: J = parallel_pair_category()
        sage: C = Groups()
        sage: G, H = SymmetricGroup(3), CyclicGroup(6)
        sage: f = G.hom(H, ...)
        sage: g = G.hom(H, ...)
        sage: D = Diagram(J, C, 
        ....:     object_map={0: G, 1: H},
        ....:     morphism_map={'f': f, 'g': g})
    """
    
    def __init__(self, index_category, target_category, object_map, morphism_map=None):
        """
        Initialize a diagram.
        
        INPUT:
        - index_category: The shape category J
        - target_category: The target category C
        - object_map: Dictionary {j ∈ J: F(j) ∈ C}
        - morphism_map: Dictionary {f ∈ Mor(J): F(f) ∈ Mor(C)}
        
        The morphism_map can use various key formats:
        - Morphism objects from J
        - String labels for named morphisms
        - Tuples (source, target, label) for identification
        """
        self._index = index_category
        self._target = target_category
        self._objects = object_map
        self._morphisms = morphism_map or {}
        self._validate_functor_laws()
    
    def _validate_functor_laws(self):
        """
        Verify this defines a valid functor:
        1. F(id_X) = id_F(X) for all objects X
        2. F(g∘f) = F(g)∘F(f) for all composable f,g
        """
        # Check identity preservation
        for obj in self._objects:
            if obj in self._index.objects():
                id_j = self._index.identity_morphism(obj)
                F_obj = self._objects[obj]
                id_F_obj = self._target.identity_morphism(F_obj)
                
                if id_j in self._morphisms:
                    if self._morphisms[id_j] != id_F_obj:
                        raise ValueError(f"Functor doesn't preserve identity at {obj}")
        
        # Check composition preservation (for small index categories)
        # Implementation depends on ability to enumerate morphisms
        pass
    
    def index_category(self):
        """Return the index category J."""
        return self._index
    
    def target_category(self):
        """Return the target category C."""
        return self._target
    
    def eval_object(self, j):
        """
        Evaluate the diagram at object j.
        
        Returns F(j) in the target category.
        """
        if j not in self._objects:
            raise KeyError(f"Object {j} not in diagram domain")
        return self._objects[j]
    
    def eval_morphism(self, f):
        """
        Evaluate the diagram at morphism f.
        
        Returns F(f) in the target category.
        """
        # Try direct lookup first
        if f in self._morphisms:
            return self._morphisms[f]
        
        # Try to infer for identity morphisms
        if hasattr(f, 'is_identity') and f.is_identity():
            obj = f.domain()
            if obj in self._objects:
                return self._target.identity_morphism(self._objects[obj])
        
        raise KeyError(f"Morphism {f} not specified in diagram")
    
    def objects(self):
        """Return the image objects in target category."""
        return list(self._objects.values())
    
    def morphisms(self):
        """Return the image morphisms in target category."""
        return list(self._morphisms.values())
    
    def is_commutative(self):
        """
        Check if all squares in the diagram commute.
        
        For each pair of parallel paths in J, check that
        their images in C are equal.
        """
        # This is non-trivial for general diagrams
        # Would need to enumerate all parallel paths
        raise NotImplementedError("General commutativity check not implemented")
    
    def __repr__(self):
        return f"Diagram from {self._index} to {self._target}"
```

### **2. Cone Class**

```python
class Cone:
    """
    A cone over a diagram D: J → C.
    
    Consists of an apex object N and projections πⱼ: N → D(j)
    satisfying coherence conditions.
    
    EXAMPLES::
    
        sage: # Cone over discrete diagram (for products)
        sage: J = discrete_category([0, 1])
        sage: C = Sets()
        sage: D = Diagram(J, C, {0: ZZ, 1: QQ})
        sage: 
        sage: # Apex is ZZ × QQ
        sage: apex = cartesian_product([ZZ, QQ])
        sage: proj_0 = projection_map(apex, ZZ, 0)
        sage: proj_1 = projection_map(apex, QQ, 1)
        sage: 
        sage: cone = Cone(D, apex, {0: proj_0, 1: proj_1})
        sage: cone.is_limit()  # Check if universal
    """
    
    def __init__(self, diagram, apex, projections):
        """
        Initialize a cone.
        
        INPUT:
        - diagram: The base Diagram object
        - apex: The apex object in target category
        - projections: Dict {j ∈ J: morphism apex → D(j)}
        """
        self._diagram = diagram
        self._apex = apex
        self._projections = projections
        self._validate_cone_conditions()
    
    def _validate_cone_conditions(self):
        """
        Verify cone coherence: D(f) ∘ πⱼ = πₖ for f: j → k.
        """
        J = self._diagram.index_category()
        
        # For each morphism in index category
        for j in self._projections:
            for k in self._projections:
                # Check all morphisms j → k
                for f in J.hom_set(j, k):
                    # Coherence: D(f) ∘ πⱼ = πₖ
                    D_f = self._diagram.eval_morphism(f)
                    pi_j = self._projections[j]
                    pi_k = self._projections[k]
                    
                    composed = D_f * pi_j  # D(f) ∘ πⱼ
                    if composed != pi_k:
                        raise ValueError(f"Cone condition fails for {f}: "
                                       f"D({f}) ∘ π_{j} ≠ π_{k}")
    
    def apex(self):
        """Return the apex object."""
        return self._apex
    
    def projection(self, j):
        """Return projection πⱼ: apex → D(j)."""
        return self._projections[j]
    
    def projections(self):
        """Return all projections as a dict."""
        return self._projections.copy()
    
    def diagram(self):
        """Return the underlying diagram."""
        return self._diagram
    
    def factor_through(self, other_cone):
        """
        Find the unique morphism from other_cone.apex() to self.apex()
        making the cone morphism triangles commute.
        
        This exists iff self is a limit cone.
        """
        # For each j, need: πⱼ ∘ u = other_cone.projection(j)
        # This gives a system of equations to solve for u
        
        target_cat = self._diagram.target_category()
        
        # This is where we'd need the target category's
        # ability to solve such systems (e.g., in abelian categories)
        raise NotImplementedError("Universal factorization not implemented")
    
    def is_limit(self):
        """
        Check if this cone is a limit (universal cone).
        
        A cone is a limit iff for every other cone over the same
        diagram, there exists a unique morphism from the other
        apex to this apex making all triangles commute.
        """
        # This requires ability to:
        # 1. Enumerate all cones over the diagram
        # 2. Check unique factorization for each
        # Generally undecidable without more structure
        raise NotImplementedError("Limit checking requires more structure")
    
    def __repr__(self):
        return f"Cone over {self._diagram} with apex {self._apex}"
```

### **3. Cocone Class**

```python
class Cocone:
    """
    A cocone under a diagram D: J → C.
    
    Consists of a nadir object N and injections ιⱼ: D(j) → N
    satisfying coherence conditions.
    
    EXAMPLES::
    
        sage: # Cocone under span (for pushout)
        sage: J = span_category()  # 1 ← 0 → 2
        sage: C = Sets()
        sage: D = Diagram(J, C, 
        ....:     {0: ZZ, 1: ZZ/2ZZ, 2: ZZ/3ZZ},
        ....:     morphism_map={...})
        sage: 
        sage: # Nadir is the pushout
        sage: nadir = ZZ/6ZZ  # pushout of ZZ → ZZ/2ZZ and ZZ → ZZ/3ZZ
        sage: inj_1 = canonical_map(ZZ/2ZZ, ZZ/6ZZ)
        sage: inj_2 = canonical_map(ZZ/3ZZ, ZZ/6ZZ)
        sage: 
        sage: cocone = Cocone(D, nadir, {1: inj_1, 2: inj_2})
    """
    
    def __init__(self, diagram, nadir, injections):
        """
        Initialize a cocone.
        
        INPUT:
        - diagram: The base Diagram object
        - nadir: The nadir object in target category
        - injections: Dict {j ∈ J: morphism D(j) → nadir}
        """
        self._diagram = diagram
        self._nadir = nadir
        self._injections = injections
        self._validate_cocone_conditions()
    
    def _validate_cocone_conditions(self):
        """
        Verify cocone coherence: ιₖ ∘ D(f) = ιⱼ for f: j → k.
        """
        J = self._diagram.index_category()
        
        # For each morphism in index category
        for j in self._injections:
            for k in self._injections:
                # Check all morphisms j → k
                for f in J.hom_set(j, k):
                    # Coherence: ιₖ ∘ D(f) = ιⱼ
                    D_f = self._diagram.eval_morphism(f)
                    iota_j = self._injections[j]
                    iota_k = self._injections[k]
                    
                    composed = iota_k * D_f  # ιₖ ∘ D(f)
                    if composed != iota_j:
                        raise ValueError(f"Cocone condition fails for {f}: "
                                       f"ι_{k} ∘ D({f}) ≠ ι_{j}")
    
    def nadir(self):
        """Return the nadir object."""
        return self._nadir
    
    def injection(self, j):
        """Return injection ιⱼ: D(j) → nadir."""
        return self._injections[j]
    
    def injections(self):
        """Return all injections as a dict."""
        return self._injections.copy()
    
    def diagram(self):
        """Return the underlying diagram."""
        return self._diagram
    
    def factor_through(self, other_cocone):
        """
        Find the unique morphism from self.nadir() to other_cocone.nadir()
        making the cocone morphism triangles commute.
        
        This exists iff self is a colimit cocone.
        """
        # For each j, need: u ∘ ιⱼ = other_cocone.injection(j)
        # This gives a system of equations to solve for u
        
        target_cat = self._diagram.target_category()
        
        # This is where we'd need the target category's
        # ability to solve such systems
        raise NotImplementedError("Universal factorization not implemented")
    
    def is_colimit(self):
        """
        Check if this cocone is a colimit (universal cocone).
        
        A cocone is a colimit iff for every other cocone under the
        same diagram, there exists a unique morphism from this nadir
        to the other nadir making all triangles commute.
        """
        # This requires ability to:
        # 1. Enumerate all cocones under the diagram
        # 2. Check unique factorization for each
        # Generally undecidable without more structure
        raise NotImplementedError("Colimit checking requires more structure")
    
    def __repr__(self):
        return f"Cocone under {self._diagram} with nadir {self._nadir}"
```

### **4. Category Methods for Limits/Colimits**

```python
# Methods to add to the Category base class

def limit(self, diagram):
    """
    Compute the limit of a diagram in this category.
    
    INPUT:
    - diagram: A Diagram object D: J → self
    
    OUTPUT:
    - (limit_object, limit_cone) if limit exists
    - None if limit doesn't exist
    
    EXAMPLES::
    
        sage: # Product via limit
        sage: J = discrete_category([0, 1])
        sage: D = Diagram(J, Sets(), {0: ZZ, 1: QQ})
        sage: lim, cone = Sets().limit(D)
        sage: lim
        Cartesian product of Integer Ring and Rational Field
    """
    # Default: try specialized methods based on diagram shape
    J = diagram.index_category()
    
    # Discrete diagram → product
    if self._is_discrete_diagram(J):
        objects = [diagram.eval_object(j) for j in J.objects()]
        return self.product(objects)
    
    # Parallel pair → equalizer
    if self._is_parallel_pair(J):
        # Extract the two morphisms
        morphisms = list(diagram.morphisms())
        if len(morphisms) == 2:
            return self.equalizer(morphisms[0], morphisms[1])
    
    # Cospan → pullback
    if self._is_cospan(J):
        # Extract the cospan morphisms
        # ... implementation ...
        pass
    
    # General case: need to construct limit directly
    raise NotImplementedError(f"Limit for diagram shape {J} not implemented")

def colimit(self, diagram):
    """
    Compute the colimit of a diagram in this category.
    
    INPUT:
    - diagram: A Diagram object D: J → self
    
    OUTPUT:
    - (colimit_object, colimit_cocone) if colimit exists
    - None if colimit doesn't exist
    
    EXAMPLES::
    
        sage: # Coproduct via colimit
        sage: J = discrete_category([0, 1])
        sage: D = Diagram(J, Groups(), {0: CyclicGroup(2), 1: CyclicGroup(3)})
        sage: colim, cocone = Groups().colimit(D)
        sage: colim
        Cyclic group of order 6
    """
    # Default: try specialized methods based on diagram shape
    J = diagram.index_category()
    
    # Discrete diagram → coproduct
    if self._is_discrete_diagram(J):
        objects = [diagram.eval_object(j) for j in J.objects()]
        return self.coproduct(objects)
    
    # Parallel pair → coequalizer
    if self._is_parallel_pair(J):
        morphisms = list(diagram.morphisms())
        if len(morphisms) == 2:
            return self.coequalizer(morphisms[0], morphisms[1])
    
    # Span → pushout
    if self._is_span(J):
        # Extract the span morphisms
        # ... implementation ...
        pass
    
    # General case: need to construct colimit directly
    raise NotImplementedError(f"Colimit for diagram shape {J} not implemented")

def has_limits(self, shape=None):
    """
    Check if this category has limits of given shape.
    
    INPUT:
    - shape: A category J (or None for all small diagrams)
    
    OUTPUT:
    - True if category has all limits of shape J
    - False otherwise
    """
    if shape is None:
        # Check for completeness (all small limits)
        return self.is_complete()
    
    # Check specific shape
    # This is generally undecidable without more info
    raise NotImplementedError("Limit existence checking not implemented")

def has_colimits(self, shape=None):
    """
    Check if this category has colimits of given shape.
    
    INPUT:
    - shape: A category J (or None for all small diagrams)
    
    OUTPUT:
    - True if category has all colimits of shape J
    - False otherwise
    """
    if shape is None:
        # Check for cocompleteness (all small colimits)
        return self.is_cocomplete()
    
    # Check specific shape
    raise NotImplementedError("Colimit existence checking not implemented")
```

### **5. Helper Classes for Common Diagram Shapes**

```python
class ProductDiagram(Diagram):
    """
    Specialized diagram for products (discrete indexing).
    
    EXAMPLES::
    
        sage: diag = ProductDiagram([ZZ, QQ, RR], category=Rings())
        sage: prod, cone = diag.limit()
    """
    
    def __init__(self, objects, category):
        # Create discrete indexing category
        n = len(objects)
        J = discrete_category(range(n))
        
        # Map to objects
        object_map = dict(enumerate(objects))
        
        super().__init__(J, category, object_map)

class EqualizerDiagram(Diagram):
    """
    Specialized diagram for equalizers (parallel pair).
    
    EXAMPLES::
    
        sage: f = ZZ.hom(QQ, ...)
        sage: g = ZZ.hom(QQ, ...)
        sage: diag = EqualizerDiagram(f, g)
        sage: eq, cone = diag.limit()
    """
    
    def __init__(self, f, g):
        if f.domain() != g.domain() or f.codomain() != g.codomain():
            raise ValueError("Morphisms must be parallel")
        
        # Create parallel pair category
        J = parallel_pair_category()
        category = f.parent()  # Morphism category
        
        object_map = {0: f.domain(), 1: f.codomain()}
        morphism_map = {'f': f, 'g': g}
        
        super().__init__(J, category, object_map, morphism_map)

class PullbackDiagram(Diagram):
    """
    Specialized diagram for pullbacks (cospan).
    
    EXAMPLES::
    
        sage: f = X.hom(Z, ...)
        sage: g = Y.hom(Z, ...)
        sage: diag = PullbackDiagram(f, g)
        sage: pb, cone = diag.limit()
    """
    
    def __init__(self, f, g):
        if f.codomain() != g.codomain():
            raise ValueError("Morphisms must form cospan")
        
        # Create cospan category
        J = cospan_category()
        category = f.parent()
        
        object_map = {0: f.codomain(), 1: f.domain(), 2: g.domain()}
        morphism_map = {
            J.hom_set(1, 0).pop(): f,
            J.hom_set(2, 0).pop(): g
        }
        
        super().__init__(J, category, object_map, morphism_map)
```

---

## Design Principles

### **1. Functorial Perspective**
- Diagrams are functors - this is the mathematically correct view
- Validate functor laws (identity and composition preservation)
- Natural transformations between diagrams give morphisms of diagrams

### **2. Shape Categories**
- Use our PosetCategory and DigraphCategory for diagram shapes
- Standard shapes (discrete, chain, span, cospan) have convenience constructors
- Custom shapes easy to create

### **3. Universal Properties**
- Cones and cocones encode the universal property directly
- Limit/colimit detection via universal factorization
- Clean separation between data (cone) and property (being limit)

### **4. Practical Implementation**
- Default to specialized algorithms for common shapes
- Fall back to general construction when needed
- Clear error messages when limits don't exist

### **5. Integration Points**
- Categories implement limit() and colimit() methods
- Diagrams know their shape and target
- Cones/cocones validate coherence automatically

---

## Next Steps

With this infrastructure in place, we can:

1. **Implement general limit/colimit algorithms** for categories with enough structure
2. **Add convenience methods** like `product_diagram()`, `equalizer_diagram()`
3. **Optimize for specific categories** (e.g., limits in Sets, Groups, Modules)
4. **Build derived constructions** (kernels as equalizers, fibers as pullbacks, etc.)

This completes the foundational infrastructure needed for proper categorical limits and colimits!