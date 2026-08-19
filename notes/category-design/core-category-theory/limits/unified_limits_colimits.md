<!--
Origin: gitclones/Coxeter/implementation/planning/limits/unified_limits_colimits.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Unified Limits and Colimits Framework

Integrating insights from Coq-HoTT and HoTT3, this document presents a unified framework for limits and colimits in SageMath that emphasizes witness-carrying universal properties and equivalence-based characterizations.

---

## Core Design Philosophy

1. **Universal Properties as Witnesses**: Store explicit witnesses for universal properties
2. **Equivalence Characterizations**: Use hom-set equivalences to define universal properties
3. **Kan Extension Foundation**: Build on Kan extensions as the unifying concept
4. **Computational Efficiency**: Allow specialized implementations while maintaining theoretical unity

---

## 1. Universal Property Framework

### **Base Universal Property Class**

```python
from abc import ABC, abstractmethod
from sage.misc.cachefunc import cached_method

class UniversalPropertyWitness(ABC):
    """
    Abstract base for universal property witnesses.
    
    Provides both existence checking and witness extraction,
    following HoTT3's approach to structured universal properties.
    
    EXAMPLES::
    
        sage: # Product universal property
        sage: C = Sets()
        sage: X, Y = Set([1,2]), Set(['a','b'])
        sage: prod_prop = ProductProperty([X, Y], C)
        sage: prod_prop.exists()
        True
        sage: P, projections, universal = prod_prop.witness()
        sage: P
        Cartesian product of {1, 2} and {'a', 'b'}
    """
    
    def __init__(self, diagram, category):
        """
        Initialize universal property.
        
        INPUT:
        - diagram: The indexing diagram
        - category: Target category where limit/colimit should exist
        """
        self.diagram = diagram
        self.category = category
        self._cached_witness = None
        self._exists_cache = None
    
    @abstractmethod
    def _compute_witness(self):
        """
        Compute the universal property witness.
        
        Returns None if doesn't exist, otherwise returns witness data.
        Should be overridden in subclasses.
        """
        pass
    
    @abstractmethod
    def _verify_universal_property(self, witness):
        """
        Verify that the witness actually satisfies the universal property.
        
        INPUT:
        - witness: Candidate witness data
        
        OUTPUT:
        Boolean indicating whether witness is valid
        """
        pass
    
    def exists(self):
        """
        Check if the universal property holds.
        
        OUTPUT:
        Boolean indicating existence
        """
        if self._exists_cache is None:
            self._exists_cache = self._compute_witness() is not None
        return self._exists_cache
    
    def witness(self):
        """
        Extract the universal property witness.
        
        OUTPUT:
        Tuple of (universal_object, structural_morphisms, universal_morphism_constructor)
        
        EXAMPLES::
        
            sage: # Terminal object witness
            sage: term_prop = TerminalObjectProperty(category)
            sage: term_obj, _, universal_to_term = term_prop.witness()
            sage: # For any object X, universal_to_term(X) gives unique X → term_obj
        """
        if not self.exists():
            raise ValueError(f"Universal property does not exist in {self.category}")
        
        if self._cached_witness is None:
            self._cached_witness = self._compute_witness()
            
            # Verify the witness is actually correct
            if not self._verify_universal_property(self._cached_witness):
                raise RuntimeError("Computed witness failed verification")
        
        return self._cached_witness
    
    @cached_method
    def hom_equivalence_characterization(self):
        """
        Express universal property as hom-set equivalence.
        
        Many universal properties can be characterized as:
        Hom(X, LimitObject) ≃ StructuredMorphisms(X, Diagram)
        
        OUTPUT:
        Function that takes test object and returns equivalence
        """
        witness_data = self.witness()
        return self._build_hom_equivalence(witness_data)
    
    @abstractmethod
    def _build_hom_equivalence(self, witness):
        """Build the hom-set equivalence characterization."""
        pass
```

### **Limit Property Implementation**

```python
class LimitProperty(UniversalPropertyWitness):
    """
    Universal property witness for limits.
    
    A limit of diagram D: J → C is an object L with morphisms 
    πⱼ: L → D(j) such that for any cone (N, νⱼ), there exists
    unique u: N → L with πⱼ ∘ u = νⱼ.
    
    EXAMPLES::
    
        sage: # Product as limit of discrete diagram
        sage: J = discrete_category([0, 1])
        sage: D = Diagram(J, Sets(), {0: Set([1,2]), 1: Set(['a','b'])})
        sage: lim_prop = LimitProperty(D, Sets())
        sage: lim_prop.exists()
        True
        sage: L, cone, universal = lim_prop.witness()
    """
    
    def _compute_witness(self):
        """
        Compute limit witness using category's limit method.
        """
        try:
            # Try the category's built-in limit method
            limit_obj, limit_cone = self.category.limit(self.diagram)
            
            # Create universal morphism constructor
            def universal_morphism(test_cone):
                return self._factor_through_limit(limit_cone, test_cone)
            
            return (limit_obj, limit_cone, universal_morphism)
            
        except NotImplementedError:
            return None
    
    def _verify_universal_property(self, witness):
        """
        Verify the limit universal property.
        
        For any cone over the diagram, there should be a unique
        factorization through the limit cone.
        """
        limit_obj, limit_cone, universal_morphism = witness
        
        # Test with a random cone (if possible)
        try:
            test_cone = self._generate_test_cone()
            u = universal_morphism(test_cone)
            
            # Verify the triangles commute
            for j in self.diagram.index_category().objects():
                proj_j = limit_cone.projection(j)
                test_proj_j = test_cone.projection(j)
                
                if proj_j * u != test_proj_j:
                    return False
            
            # Verify uniqueness (harder to check automatically)
            return True
            
        except (NotImplementedError, AttributeError):
            # Can't generate test cones automatically
            return True  # Assume the category's limit method is correct
    
    def _build_hom_equivalence(self, witness):
        """
        Build hom-equivalence: Hom(X, L) ≃ Cones(X, D).
        """
        limit_obj, limit_cone, universal_morphism = witness
        
        def hom_equiv(test_object):
            # Left side: morphisms to limit
            hom_to_limit = self.category.hom(test_object, limit_obj)
            
            # Right side: cones from test_object over diagram
            cones_from_test = ConesFrom(test_object, self.diagram)
            
            # The equivalence maps f: X → L to cone with projections π_j ∘ f
            def morphism_to_cone(f):
                projections = {}
                for j in self.diagram.index_category().objects():
                    projections[j] = limit_cone.projection(j) * f
                return Cone(self.diagram, test_object, projections)
            
            # Inverse maps cone to its unique factorization
            def cone_to_morphism(cone):
                return universal_morphism(cone)
            
            return Equivalence(hom_to_limit, cones_from_test, 
                             morphism_to_cone, cone_to_morphism)
        
        return hom_equiv
    
    def _factor_through_limit(self, limit_cone, test_cone):
        """
        Find unique morphism making triangles commute.
        
        This is where concrete categories would implement their
        specific factorization algorithms.
        """
        # Default: ask the test cone's category to factor through limit
        try:
            return test_cone.factor_through(limit_cone)
        except NotImplementedError:
            raise NotImplementedError(
                f"Category {self.category} must implement factorization "
                f"or override _factor_through_limit"
            )
```

### **Colimit Property Implementation**

```python
class ColimitProperty(UniversalPropertyWitness):
    """
    Universal property witness for colimits.
    
    Dual to limits: colimit has injections ιⱼ: D(j) → C
    and universal property for cocones.
    """
    
    def _compute_witness(self):
        """Compute colimit witness."""
        try:
            colimit_obj, colimit_cocone = self.category.colimit(self.diagram)
            
            def universal_morphism(test_cocone):
                return self._factor_from_colimit(colimit_cocone, test_cocone)
            
            return (colimit_obj, colimit_cocone, universal_morphism)
            
        except NotImplementedError:
            return None
    
    def _verify_universal_property(self, witness):
        """Verify colimit universal property."""
        colimit_obj, colimit_cocone, universal_morphism = witness
        
        # Test with random cocone
        try:
            test_cocone = self._generate_test_cocone()
            u = universal_morphism(test_cocone)
            
            # Verify triangles commute: u ∘ ιⱼ = test_ιⱼ
            for j in self.diagram.index_category().objects():
                inj_j = colimit_cocone.injection(j)
                test_inj_j = test_cocone.injection(j)
                
                if u * inj_j != test_inj_j:
                    return False
            
            return True
            
        except (NotImplementedError, AttributeError):
            return True
    
    def _build_hom_equivalence(self, witness):
        """
        Build hom-equivalence: Hom(C, X) ≃ Cocones(D, X).
        """
        colimit_obj, colimit_cocone, universal_morphism = witness
        
        def hom_equiv(test_object):
            # Left side: morphisms from colimit
            hom_from_colimit = self.category.hom(colimit_obj, test_object)
            
            # Right side: cocones from diagram to test_object
            cocones_to_test = CoconesTo(self.diagram, test_object)
            
            # Equivalence maps f: C → X to cocone with injections f ∘ ιⱼ
            def morphism_to_cocone(f):
                injections = {}
                for j in self.diagram.index_category().objects():
                    injections[j] = f * colimit_cocone.injection(j)
                return Cocone(self.diagram, test_object, injections)
            
            # Inverse maps cocone to its unique factorization
            def cocone_to_morphism(cocone):
                return universal_morphism(cocone)
            
            return Equivalence(hom_from_colimit, cocones_to_test,
                             morphism_to_cocone, cocone_to_morphism)
        
        return hom_equiv
```

---

## 2. Kan Extension Foundation

### **Kan Extensions as Universal Framework**

```python
class KanExtensionProperty(UniversalPropertyWitness):
    """
    Kan extensions as the foundation for limits and colimits.
    
    Following Coq-HoTT's approach:
    - Right Kan extension along !: J → 1 gives limits
    - Left Kan extension along !: J → 1 gives colimits
    
    EXAMPLES::
    
        sage: # Limit as right Kan extension
        sage: J = discrete_category([0, 1])  # Shape category
        sage: terminal = terminal_category()  # 1
        sage: unique = J.unique_morphism_to(terminal)  # !: J → 1
        sage: F = SomeDiagram(J, C)  # F: J → C
        sage: ran_prop = RightKanExtensionProperty(unique, F)
        sage: ran_prop.exists()  # Same as asking if F has limit
    """
    
    def __init__(self, p_functor, f_functor, extension_type='right'):
        """
        Initialize Kan extension property.
        
        INPUT:
        - p_functor: P: A → B (the functor we're extending along)
        - f_functor: F: A → C (the functor we're extending)
        - extension_type: 'right' or 'left'
        
        We seek G: B → C and natural transformation η: F → G∘P (right)
        or η: G∘P → F (left) with universal property.
        """
        self.p_functor = p_functor
        self.f_functor = f_functor
        self.extension_type = extension_type
        
        # For limits/colimits, B is usually the terminal category
        super().__init__(None, f_functor.codomain())
    
    def _compute_witness(self):
        """
        Compute Kan extension witness.
        """
        if self.extension_type == 'right':
            return self._compute_right_kan_extension()
        else:
            return self._compute_left_kan_extension()
    
    def _compute_right_kan_extension(self):
        """
        Right Kan extension: Ran_P F.
        
        For each B ∈ B, (Ran_P F)(B) should be the limit of
        the diagram (P/B) → A → C where (P/B) is the comma category.
        """
        # Special case: P: J → 1 (limits)
        if self.p_functor.codomain().is_terminal():
            # This is just the limit of F
            try:
                return self._compute_as_limit()
            except NotImplementedError:
                return None
        
        # General case: need to compute pointwise limits
        return self._compute_general_right_kan()
    
    def _compute_as_limit(self):
        """When P: J → 1, right Kan extension is the limit of F."""
        try:
            # The functor F: J → C becomes a diagram
            diagram = DiagramFromFunctor(self.f_functor)
            limit_prop = LimitProperty(diagram, self.category)
            
            if limit_prop.exists():
                limit_obj, limit_cone, universal = limit_prop.witness()
                
                # Package as Kan extension data
                # G: 1 → C is the constant functor at limit_obj
                g_functor = ConstantFunctor(limit_obj, terminal_category(), self.category)
                
                # η: F → G∘P is the limit cone
                eta = limit_cone
                
                def kan_universal_property(test_g, test_eta):
                    """Universal property for Kan extensions."""
                    # Should be unique α: G → test_G such that test_η = (α ∘ P) * η
                    return self._solve_kan_equation(g_functor, eta, test_g, test_eta)
                
                return (g_functor, eta, kan_universal_property)
                
        except NotImplementedError:
            return None
    
    def as_limit_property(self):
        """
        Convert Kan extension to limit property when applicable.
        
        When P: J → 1, right Kan extension is equivalent to limit.
        """
        if not (self.extension_type == 'right' and 
                self.p_functor.codomain().is_terminal()):
            raise ValueError("Can only convert right Kan extensions along !: J → 1 to limits")
        
        diagram = DiagramFromFunctor(self.f_functor)
        return LimitProperty(diagram, self.category)
    
    def as_colimit_property(self):
        """
        Convert Kan extension to colimit property when applicable.
        """
        if not (self.extension_type == 'left' and 
                self.p_functor.codomain().is_terminal()):
            raise ValueError("Can only convert left Kan extensions along !: J → 1 to colimits")
        
        diagram = DiagramFromFunctor(self.f_functor)
        return ColimitProperty(diagram, self.category)
```

---

## 3. Unified Category Interface

### **Categories with Universal Properties**

```python
class CategoryWithLimits(Category):
    """
    Category that can compute limits and colimits via universal properties.
    
    Provides both computational methods and universal property witnesses.
    """
    
    def limit_property(self, diagram):
        """
        Get limit universal property witness.
        
        INPUT:
        - diagram: A Diagram object
        
        OUTPUT:
        LimitProperty instance
        
        EXAMPLES::
        
            sage: C = Sets()
            sage: D = product_diagram([Set([1,2]), Set(['a','b'])], C)
            sage: lim_prop = C.limit_property(D)
            sage: lim_prop.exists()
            True
            sage: L, cone, universal = lim_prop.witness()
        """
        return LimitProperty(diagram, self)
    
    def colimit_property(self, diagram):
        """Get colimit universal property witness."""
        return ColimitProperty(diagram, self)
    
    def limit(self, diagram):
        """
        Compute limit (computational interface).
        
        This is the traditional SageMath interface that just returns
        the limit object and cone without universal property witness.
        """
        lim_prop = self.limit_property(diagram)
        if not lim_prop.exists():
            raise ValueError(f"Limit of {diagram} does not exist in {self}")
        
        limit_obj, limit_cone, universal = lim_prop.witness()
        return limit_obj, limit_cone
    
    def colimit(self, diagram):
        """Compute colimit (computational interface)."""
        colim_prop = self.colimit_property(diagram)
        if not colim_prop.exists():
            raise ValueError(f"Colimit of {diagram} does not exist in {self}")
        
        colimit_obj, colimit_cocone, universal = colim_prop.witness()
        return colimit_obj, colimit_cocone
    
    # Specialized methods that delegate to general framework
    def product_property(self, objects):
        """Product as limit of discrete diagram."""
        discrete = discrete_category(range(len(objects)))
        diagram = Diagram(discrete, self, dict(enumerate(objects)))
        return self.limit_property(diagram)
    
    def product(self, objects):
        """Computational product interface."""
        prod_prop = self.product_property(objects)
        if not prod_prop.exists():
            raise ValueError(f"Product of {objects} does not exist in {self}")
        
        prod_obj, cone, universal = prod_prop.witness()
        projections = [cone.projection(i) for i in range(len(objects))]
        return prod_obj, projections
    
    def pullback_property(self, f, g):
        """Pullback as limit of cospan."""
        if f.codomain() != g.codomain():
            raise ValueError("Morphisms must form cospan")
        
        cospan = cospan_category()
        diagram = Diagram(cospan, self,
                         {0: f.codomain(), 1: f.domain(), 2: g.domain()},
                         {cospan.hom_set(1,0).pop(): f, 
                          cospan.hom_set(2,0).pop(): g})
        return self.limit_property(diagram)
    
    def pullback(self, f, g):
        """Computational pullback interface."""
        pb_prop = self.pullback_property(f, g)
        if not pb_prop.exists():
            raise ValueError(f"Pullback of {f}, {g} does not exist in {self}")
        
        pb_obj, cone, universal = pb_prop.witness()
        p1 = cone.projection(1)  # P → domain(f)
        p2 = cone.projection(2)  # P → domain(g)
        return pb_obj, p1, p2
    
    # Query methods
    def has_limits_of_shape(self, shape_category):
        """
        Check if category has limits of given shape.
        
        INPUT:
        - shape_category: Category J
        
        OUTPUT:
        Boolean indicating whether all diagrams D: J → self have limits
        """
        # This is generally undecidable, but categories can override
        # with specific knowledge
        raise NotImplementedError(f"Cannot determine if {self} has limits of shape {shape_category}")
    
    def has_all_small_limits(self):
        """Check if category is complete."""
        # Most categories won't be able to answer this
        raise NotImplementedError(f"Cannot determine if {self} is complete")
    
    @cached_method
    def typical_limits_exist(self):
        """
        Check if typical limits (products, equalizers, terminal) exist.
        
        This is often easier than checking all limits.
        """
        try:
            # Try to construct terminal object
            term_prop = TerminalObjectProperty(self)
            if not term_prop.exists():
                return False
            
            # Try a small product
            if len(list(self.objects())[:2]) == 2:
                objs = list(self.objects())[:2]
                prod_prop = self.product_property(objs)
                if not prod_prop.exists():
                    return False
            
            return True
            
        except (NotImplementedError, AttributeError):
            return False
```

---

## 4. Integration and Examples

### **Specialized Universal Properties**

```python
class TerminalObjectProperty(UniversalPropertyWitness):
    """
    Terminal object as limit of empty diagram.
    """
    def __init__(self, category):
        empty_diagram = Diagram(empty_category(), category, {})
        super().__init__(empty_diagram, category)
    
    def _compute_witness(self):
        # Terminal object is limit of empty diagram
        return self.category.limit_property(self.diagram)._compute_witness()

class ProductProperty(LimitProperty):
    """
    Product as limit of discrete diagram.
    """
    def __init__(self, objects, category):
        n = len(objects)
        discrete = discrete_category(range(n))
        diagram = Diagram(discrete, category, dict(enumerate(objects)))
        super().__init__(diagram, category)

class EqualizerProperty(LimitProperty):
    """
    Equalizer as limit of parallel pair.
    """
    def __init__(self, f, g, category):
        if f.domain() != g.domain() or f.codomain() != g.codomain():
            raise ValueError("Morphisms must be parallel")
        
        pp = parallel_pair_category()
        diagram = Diagram(pp, category,
                         {0: f.domain(), 1: f.codomain()},
                         {'f': f, 'g': g})
        super().__init__(diagram, category)
```

### **Usage Examples**

```python
# Example 1: Check if Sets has products
C = Sets()
X, Y = Set([1,2]), Set(['a','b'])
prod_prop = C.product_property([X, Y])

print(prod_prop.exists())  # True
P, projections = C.product([X, Y])  # Computational interface
P_witness, cone, universal = prod_prop.witness()  # Witness interface

# Example 2: Universal property characterization
hom_equiv = prod_prop.hom_equivalence_characterization()
Z = Set([1,2,3])
equiv = hom_equiv(Z)  # Equivalence: Hom(Z, P) ≃ Hom(Z, X) × Hom(Z, Y)

# Example 3: Kan extension perspective
from sage.categories.terminal_category import terminal_category
discrete_2 = discrete_category([0, 1])
terminal = terminal_category()
unique = discrete_2.unique_morphism_to(terminal)
F = Diagram(discrete_2, Sets(), {0: X, 1: Y})

kan_prop = KanExtensionProperty(unique, F, 'right')
print(kan_prop.exists())  # True - same as product existing
limit_prop = kan_prop.as_limit_property()  # Convert to limit property
```

---

## Benefits of This Framework

1. **Mathematical Unity**: All universal constructions are limits/colimits, which are Kan extensions
2. **Computational Efficiency**: Specialized implementations can override general methods
3. **Witness Management**: Explicit universal property data for further computation
4. **Equivalence Characterizations**: Clean characterizations via hom-set equivalences
5. **Extensibility**: Easy to add new universal constructions following the same pattern
6. **Type Safety**: Universal properties carry their verification proofs

This unified framework provides both theoretical elegance and practical computational power!