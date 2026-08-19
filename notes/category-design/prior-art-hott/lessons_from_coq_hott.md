<!--
Origin: gitclones/Coxeter/research/explorations/implementation-notes/lessons_from_coq_hott.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of this
corpus.
-->

# Lessons from Coq-HoTT Category Theory Implementation

After exploring the Coq-HoTT library's category theory implementation, here are key insights we can apply to our SageMath categorical framework.

---

## 1. Core Category Structure

### **Coq-HoTT Approach**
```coq
Record PreCategory :=
  Build_PreCategory' {
      object :> Type;
      morphism : object -> object -> Type;
      identity : forall x, morphism x x;
      compose : forall s d d', morphism d d' -> morphism s d -> morphism s d';
      
      (* Laws with redundant versions for judgmental equality *)
      associativity : ...;
      associativity_sym : ...;  (* Symmetrized version *)
      left_identity : ...;
      right_identity : ...;
      identity_identity : ...;  (* id ∘ id = id *)
      
      (* Truncation level *)
      trunc_morphism :: forall s d, IsHSet (morphism s d)
  }.
```

### **Key Insights**
1. **Explicit morphism types**: They use `morphism : object -> object -> Type` rather than a single morphism type with domain/codomain methods
2. **Redundant laws**: They include symmetric versions of laws (e.g., both directions of associativity) for better computational behavior
3. **Truncation levels**: Explicit tracking of h-levels (set-truncation for hom-sets)

### **Adaptation for SageMath**
```python
class Category:
    def objects(self):
        """Return collection of objects."""
        raise NotImplementedError
    
    def hom(self, X, Y):
        """Return hom-set Hom(X,Y) as a Parent."""
        raise NotImplementedError
    
    def compose(self, f, g):
        """Compose morphisms where cod(g) = dom(f)."""
        # Could cache compositions for efficiency
        return f * g
    
    def identity(self, X):
        """Return identity morphism on X."""
        return self.hom(X, X).identity()
```

---

## 2. Limits as Kan Extensions

### **Coq-HoTT Approach**
```coq
(* Diagonal functor *)
Definition diagonal_functor : Functor (1 -> C) (D -> C)
  := @pullback_along _ D 1 C (Functors.to_terminal _).

(* Limit as right Kan extension *)
Definition IsLimit
  := @IsRightKanExtensionAlong _ D 1 C (Functors.to_terminal _) F.

(* Colimit as left Kan extension *)  
Definition IsColimit
  := @IsLeftKanExtensionAlong _ D 1 C (Functors.to_terminal _) F.
```

### **Key Insights**
1. **Unifying perspective**: Limits/colimits are special cases of Kan extensions
2. **Diagonal functor**: Central role of Δ: C → C^D sending X to constant functor
3. **Terminal category**: Using the terminal category 1 to express limits cleanly

### **Adaptation for SageMath**
```python
def diagonal_functor(C, D):
    """
    The diagonal functor Δ: C → Fun(D,C).
    
    Sends each object X to the constant functor Δ_X: D → C.
    """
    class DiagonalFunctor(Functor):
        def _call_on_objects(self, X):
            return ConstantFunctor(D, C, X)
        
        def _call_on_morphisms(self, f):
            # Natural transformation between constant functors
            return ConstantNaturalTransformation(f)
    
    return DiagonalFunctor(C, FunctorCategory(D, C))

# Then limits are universal cones
def limit(diagram):
    """
    Limit of F: D → C is terminal object in category of cones.
    
    Equivalently, it's the right Kan extension of F along ! : D → 1.
    """
    pass
```

---

## 3. Universal Properties via Comma Categories

### **Coq-HoTT Approach**
```coq
(* Initial morphism from X to U as initial object in (X ↓ U) *)
Definition IsInitialMorphism (Ap : object (X / U)) :=
  IsInitialObject (X / U) Ap.

(* Terminal morphism from U to X as terminal object in (U ↓ X) *)
Definition IsTerminalMorphism (Ap : object (U / X)) :=
  IsTerminalObject (U / X) Ap.
```

### **Key Insights**
1. **Comma categories**: Universal properties expressed as initial/terminal objects in comma categories
2. **Duality**: Terminal morphisms in C are initial morphisms in C^op
3. **Clean abstraction**: Reduces universal properties to initial/terminal objects

### **Adaptation for SageMath**
```python
class CommaCategoryObject:
    """Object in comma category."""
    def __init__(self, source_obj, target_obj, morphism):
        self.source = source_obj
        self.target = target_obj  
        self.morphism = morphism

def is_initial_morphism(X, U, A, phi):
    """
    Check if φ: X → U(A) is initial morphism from X to U.
    
    This means (A, φ) is initial in comma category (X ↓ U).
    """
    comma_obj = CommaCategoryObject(X, A, phi)
    comma_cat = CommaCategory(ConstantFunctor(X), U)
    return comma_cat.is_initial(comma_obj)
```

---

## 4. Explicit Introduction/Elimination Rules

### **Coq-HoTT Approach**
```coq
(* Explicit builders with clear universal property *)
Definition Build_IsInitialMorphism
           (A : D) 
           (p : morphism C X (U A))
           (UniversalProperty
            : forall (A' : D) (p' : morphism C X (U A')),
                Contr { m : morphism D A A' | U _1 m o p = p' })
: IsInitialMorphism Ap.

(* Clear projections for elimination *)
Definition IsInitialMorphism_object (M : IsInitialMorphism Ap) : D.
Definition IsInitialMorphism_morphism (M : IsInitialMorphism Ap) : morphism C X (U _).
Definition IsInitialMorphism_property (M : IsInitialMorphism Ap) : ....
```

### **Key Insights**
1. **Explicit interfaces**: Clear introduction (Build_) and elimination functions
2. **Contractible types**: Using HoTT's Contr for uniqueness
3. **Abstraction barriers**: Hiding implementation details while preserving computation

### **Adaptation for SageMath**
```python
class InitialMorphism:
    """
    Initial morphism from X to functor U.
    
    Encapsulates the universal property with clear interface.
    """
    def __init__(self, X, U, A, morphism, verify=True):
        self.source = X
        self.functor = U
        self.object = A
        self.morphism = morphism  # X → U(A)
        
        if verify:
            self._verify_universal_property()
    
    def _verify_universal_property(self):
        """Check this satisfies the initial property."""
        # Would need to check uniqueness of factorizations
        pass
    
    def factor_through(self, Y, f):
        """
        Given f: X → U(Y), find unique g: A → Y with U(g) ∘ φ = f.
        """
        # Implementation of universal property
        pass
```

---

## 5. Design Principles to Adopt

### **1. Separation of Concerns**
- Core definitions (PreCategory) separate from derived notions
- Universal properties as separate layer built on top
- Clear abstraction boundaries

### **2. Computational Efficiency**
- Include redundant laws for better reduction behavior
- Cache frequently used compositions
- Avoid recomputing universal properties

### **3. Proof-Relevant Design**
- Keep track of witnesses to universal properties
- Make uniqueness data accessible when needed
- Allow both existence checks and witness extraction

### **4. Systematic Duality**
- Implement concepts to work cleanly with opposite categories
- Use op-op = id systematically
- Design APIs to be self-dual where possible

---

## 6. Practical Implementation Strategy

Based on Coq-HoTT's architecture, here's a suggested implementation order:

1. **Core Categories**
   - Basic category with objects() and hom() methods
   - Comma categories as fundamental construction
   - Opposite categories with clean duality

2. **Universal Properties**
   - Initial/terminal objects in arbitrary categories  
   - Universal morphisms via comma categories
   - Build specialized APIs on top (products, pullbacks, etc.)

3. **Limits/Colimits**
   - Implement as Kan extensions for theoretical cleanliness
   - Add optimized special cases for efficiency
   - Use diagram categories from our earlier work

4. **Higher Structure**
   - Natural transformations with proper coherence
   - 2-categorical structure where needed
   - Adjunctions as next major abstraction

The Coq-HoTT approach shows that building from universal properties and comma categories gives a very clean, modular design that naturally captures all the standard constructions.