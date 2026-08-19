<!--
Origin: gitclones/Coxeter/research/explorations/implementation-notes/lessons_from_hott3.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of this
corpus.
-->

# Lessons from HoTT3 (Lean 3 HoTT Library)

After exploring the HoTT3 library, here are key insights we can apply to our SageMath categorical framework, particularly for universal properties and type-theoretic approaches.

---

## 1. Type-Theoretic Universal Properties

### **HoTT3 Approach to Pullbacks**
```lean
structure pullback (f₂₁ : A₂₀ → A₂₂) (f₁₂ : A₀₂ → A₂₂) :=
  (fst : A₂₀)
  (snd : A₀₂)
  (fst_snd : f₂₁ fst = f₁₂ snd)

structure pullback_square (f₁₀ : A₀₀ → A₂₀) (f₁₂ : A₀₂ → A₂₂) 
                          (f₀₁ : A₀₀ → A₀₂) (f₂₁ : A₂₀ → A₂₂) :=
  (comm : Πa, f₂₁ (f₁₀ a) = f₁₂ (f₀₁ a))
  (is_pullback : is_equiv (pullback_corec comm : A₀₀ → pullback f₂₁ f₁₂))
```

### **Key Insights**
1. **Pullback as Structure**: The pullback itself is just a triple (x, y, proof that f(x) = g(y))
2. **Universal Property as Equivalence**: The pullback square property is characterized by an equivalence
3. **Witness-Carrying**: Every universal property explicitly carries its proof/witness
4. **Equivalence-Based**: Uses `is_equiv` rather than existence + uniqueness

### **Adaptation for SageMath**
```python
class PullbackObject:
    """
    Pullback of cospan f: X → Z ← Y: g as structured object.
    
    Consists of projections and commutativity witness.
    """
    def __init__(self, X, Y, Z, f, g, projections, witness):
        self.X, self.Y, self.Z = X, Y, Z
        self.f, self.g = f, g
        self.proj_X, self.proj_Y = projections
        self.witness = witness  # proof that f ∘ proj_X = g ∘ proj_Y
    
    def verify_universal_property(self, other_X, other_Y, other_f, other_g):
        """
        Verify there's unique morphism making the diagram commute.
        
        Returns (unique_morphism, proof_of_uniqueness).
        """
        # Implementation would depend on the category
        pass

def pullback_equivalence_characterization(f, g):
    """
    Pullback characterized by equivalence of mapping spaces.
    
    For cospan f: X → Z ← Y: g, the pullback P satisfies:
    Hom(W, P) ≃ {(h: W → X, k: W → Y) | f ∘ h = g ∘ k}
    """
    def pullback_hom_equiv_factorizations(W, P):
        # Left side: morphisms to pullback
        left = P.parent_category().hom(W, P)
        
        # Right side: commutative pairs
        def commutative_pairs():
            for h in P.parent_category().hom(W, P.X):
                for k in P.parent_category().hom(W, P.Y):
                    if P.f * h == P.g * k:
                        yield (h, k)
        
        # The equivalence maps a morphism W → P to its composite projections
        return Equivalence(left, commutative_pairs, ...)
```

---

## 2. Half-Adjoint Equivalences and Coherence

### **HoTT3 Approach**
```lean
def linv (g : B → A) (f : A → B) := Π(a : A), g (f a) = a
def rinv (g : B → A) (f : A → B) := Π(b : B), f (g b) = b

def qinv (f : A → B) := Σ(g : B → A), linv g f × rinv g f

def lcoh (f : A → B) (h: qinv f) (y : B) :=
  h.η (h.inv y) = ap h.inv (h.ε y)

def is_hadj_l (f : A → B) :=
  Σ(g : B → A) (η : linv g f) (ε : rinv g f), Π(y : B), lcoh f ⟨g, (η, ε)⟩ y

-- Key theorem: Half-adjoint equivalence is a proposition
instance is_prop_hadj_l (f : A → B) : is_prop (is_hadj_l f)
```

### **Key Insights**
1. **Coherence Data**: Additional coherence laws (lcoh/rcoh) beyond basic inverse laws
2. **Propositional Refinement**: Half-adjoint equivalences are propositions (unique when they exist)
3. **Multiple Characterizations**: Different ways to present the same concept with different computational properties
4. **Witness Extraction**: Can extract computational content from existence proofs

### **Adaptation for SageMath**
```python
class IsomorphismData:
    """
    Structured approach to isomorphisms with coherence conditions.
    
    Rather than just "has inverse", record the actual inverse and proofs.
    """
    def __init__(self, f, g, left_inverse_proof, right_inverse_proof, coherence=None):
        self.morphism = f
        self.inverse = g
        self.left_inv = left_inverse_proof   # g ∘ f = id
        self.right_inv = right_inverse_proof # f ∘ g = id
        self.coherence = coherence           # Additional coherence data
    
    def is_coherent(self):
        """Check additional coherence conditions if provided."""
        if self.coherence is None:
            return True
        return self.coherence.verify(self)
    
    @cached_method
    def as_equivalence(self):
        """Convert to a computational equivalence."""
        # This would return a SageMath Morphism with .inverse() method
        pass

def unique_isomorphism_data(f):
    """
    In many categories, isomorphism data is essentially unique.
    
    This reflects the HoTT insight that half-adjoint equivalences
    form a proposition.
    """
    # Look for existing isomorphism data
    if hasattr(f, '_isomorphism_data'):
        return f._isomorphism_data
    
    # Try to construct it
    try:
        g = f.inverse()
        left_proof = verify_composition(g, f, f.domain().identity())
        right_proof = verify_composition(f, g, f.codomain().identity())
        return IsomorphismData(f, g, left_proof, right_proof)
    except NotImplementedError:
        return None
```

---

## 3. Equivalences vs. Isomorphisms

### **HoTT3 Insight**
```lean
-- Multiple equivalent characterizations:
def qinv (f : A → B) := Σ(g : B → A), linv g f × rinv g f       -- quasi-inverse
def is_hadj_l (f : A → B) := ...                                 -- half-adjoint
def adj (f : A → B) := ...                                       -- full adjoint

-- Key theorem: These are all equivalent to is_equiv
def is_hadj_l_equiv_is_equiv (f : A → B) : is_hadj_l f ≃ is_equiv f
```

### **Key Insights**
1. **Computational vs. Proof-Relevant**: Different characterizations have different computational behavior
2. **Contractible Choices**: The space of inverse data is contractible when it exists
3. **Witness Management**: Can choose which witnesses to work with computationally

### **Adaptation for SageMath**
```python
class UniversalPropertyWitness:
    """
    Manage witness data for universal properties.
    
    Provides both existence (boolean) and witness extraction.
    """
    def __init__(self, property_type, verification_method, witness_extractor):
        self.property_type = property_type
        self.verify = verification_method
        self.extract_witness = witness_extractor
        self._cached_result = None
    
    def exists(self):
        """Boolean check: does the universal property hold?"""
        if self._cached_result is None:
            self._cached_result = self.verify()
        return self._cached_result is not None
    
    def witness(self):
        """Extract the actual witness (morphisms, objects, etc.)"""
        if not self.exists():
            raise ValueError(f"Universal property {self.property_type} does not hold")
        return self.extract_witness(self._cached_result)
    
    def is_essentially_unique(self):
        """Check if witness is essentially unique (up to canonical isomorphism)"""
        # For many universal properties, witnesses are unique up to unique isomorphism
        return True  # Default assumption

# Example: Product universal property
def product_universal_property(X, Y, category):
    """
    Product universal property as witness-carrying object.
    """
    def verify_product():
        # Try to construct product
        try:
            P = category.product([X, Y])
            return P
        except NotImplementedError:
            return None
    
    def extract_witness(P):
        """Extract the actual product data."""
        return {
            'product_object': P,
            'projections': [P.projection(0), P.projection(1)],
            'universal_morphism': lambda W, f, g: P.universal_morphism(W, [f, g])
        }
    
    return UniversalPropertyWitness("product", verify_product, extract_witness)
```

---

## 4. Design Patterns for SageMath

### **1. Structured Universal Properties**
Based on HoTT3's approach, we should structure universal properties as:

```python
class UniversalProperty:
    """Base class for universal properties with witness extraction."""
    
    def __init__(self, diagram, category):
        self.diagram = diagram
        self.category = category
        self._limit_data = None
        self._colimit_data = None
    
    def has_limit(self):
        """Boolean check: does limit exist?"""
        return self._compute_limit() is not None
    
    def limit(self):
        """Extract limit object and cone."""
        limit_data = self._compute_limit()
        if limit_data is None:
            raise ValueError("Limit does not exist")
        return limit_data
    
    def _compute_limit(self):
        """Override in subclasses."""
        if self._limit_data is None:
            self._limit_data = self._try_compute_limit()
        return self._limit_data
    
    def _try_compute_limit(self):
        """Attempt to compute limit, return None if doesn't exist."""
        raise NotImplementedError
```

### **2. Equivalence-Based Characterizations**
```python
def characterize_via_hom_equivalence(universal_construction):
    """
    Many universal constructions can be characterized by
    equivalences of hom-sets or mapping spaces.
    """
    def hom_equiv_condition(test_object):
        # Left side: morphisms to/from the universal object
        left_hom = universal_construction.hom_space(test_object)
        
        # Right side: structured morphisms satisfying conditions
        right_hom = universal_construction.structured_morphisms(test_object)
        
        # The universal property is that these are equivalent
        return left_hom.is_equivalent_to(right_hom)
    
    return hom_equiv_condition
```

### **3. Coherence Management**
```python
class CoherentUniversalProperty:
    """
    Universal property with explicit coherence conditions.
    
    Manages both the basic universal property and additional
    coherence data needed for good computational behavior.
    """
    def __init__(self, basic_property, coherence_conditions=None):
        self.basic = basic_property
        self.coherence = coherence_conditions or []
    
    def verify_coherence(self):
        """Check all coherence conditions."""
        return all(cond.verify() for cond in self.coherence)
    
    def canonical_witness(self):
        """
        Extract canonical witness satisfying all coherence conditions.
        
        This is inspired by HoTT's insight that witnesses are
        essentially unique when they exist.
        """
        witness = self.basic.witness()
        for cond in self.coherence:
            witness = cond.make_coherent(witness)
        return witness
```

---

## 5. Integration with Our Existing Framework

### **Enhanced Cone/Cocone with Witnesses**
```python
class WitnessCone(Cone):
    """
    Cone with explicit universal property witnesses.
    """
    def __init__(self, diagram, apex, projections, universal_property_witness=None):
        super().__init__(diagram, apex, projections)
        self.universal_witness = universal_property_witness
    
    def is_limit(self):
        """Check if this cone is a limit."""
        if self.universal_witness is None:
            # Fall back to traditional verification
            return super().is_limit()
        return self.universal_witness.exists()
    
    def universal_morphism(self, other_cone):
        """Extract the universal morphism."""
        if self.universal_witness is None:
            raise NotImplementedError("No universal property witness provided")
        return self.universal_witness.extract_morphism(other_cone)
```

### **Category Enhancement**
```python
class CategoryWithUniversalProperties(Category):
    """
    Category enhanced with universal property management.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._universal_property_cache = {}
    
    def universal_property(self, construction_type, *args):
        """
        Get universal property witness for given construction.
        """
        key = (construction_type, args)
        if key not in self._universal_property_cache:
            self._universal_property_cache[key] = self._compute_universal_property(
                construction_type, *args
            )
        return self._universal_property_cache[key]
    
    def _compute_universal_property(self, construction_type, *args):
        """Override in concrete categories."""
        if construction_type == "product":
            return self._compute_product_property(*args)
        elif construction_type == "pullback":
            return self._compute_pullback_property(*args)
        # etc.
        raise NotImplementedError(f"Universal property {construction_type} not implemented")
```

---

## 6. Key Takeaways for Implementation

1. **Witness-Carrying Design**: Store explicit witnesses for universal properties, not just boolean existence
2. **Equivalence Characterizations**: Use equivalences of mapping spaces to characterize universal properties
3. **Coherence Management**: Track coherence conditions explicitly for computational reliability
4. **Contractible Choices**: Exploit the fact that universal property witnesses are essentially unique
5. **Multiple Characterizations**: Provide different interfaces (computational vs. proof-relevant) for different use cases

This approach gives us both mathematical rigor and computational efficiency, learning from HoTT's sophisticated treatment of universal properties and equivalences!