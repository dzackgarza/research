<!--
Origin: gitclones/Coxeter-v2/archive/cold_storage_pre_integration/background-research/sage-planning/modules_bak/RMod/RMod_constructions.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# User Interface: Intelligent Bilinear Module Factory

## Primary Constructor

```python
def BilinearModule(matrix, base_ring=None, check=True):
    r"""
    Intelligent constructor that automatically determines the appropriate 
    subcategory based on matrix properties.
    
    .. NOTE:: **ℤ-First API Design**
    
       The ``base_ring`` parameter defaults to ``None``, which automatically
       selects ``ZZ`` for integer lattices. This follows the ℤ-first principle:
       most Coxeter systems and root lattices work over the integers, so this
       should be the easiest case. Users only need to specify ``base_ring``
       for advanced use cases requiring number fields or other rings.
    
    .. WARNING:: **Sign Convention**

       This framework operates with a **negative definite** sign convention
       for elliptic (definite) and parabolic (semi-definite) lattices,
       aligning with practices in algebraic geometry. This constructor will
       **automatically convert** positive definite or positive semi-definite
       input matrices by multiplying them by -1. For example, the A2 Cartan
       matrix `[[2, -1], [-1, 2]]` will be stored internally as
       `[[-2, 1], [1, -2]]`.
    
    Analyzes the input matrix and creates the most specialized object possible:
    
    1. **Matrix Structure Analysis**:
       - General matrix → FreeBilinearModule
       - Symmetric matrix → SymmetricBilinearModule (or more specialized)
       - Skew-symmetric matrix → SkewSymmetricBilinearModule
    
    2. **For Symmetric Matrices, Signature Analysis**:
       - Nondegenerate (det ≠ 0) → Lattice (with signature-based subtype)
       - Degenerate (det = 0) → DegenerateLattice (with signature-based subtype)
    
    3. **Signature-Based Subtypes**:
       - (0, n, 0): Negative definite → EllipticLattice
       - (n, 0, 0): Positive definite → EllipticLattice (converted to negative definite)
       - (p, q, 0) with p,q ≥ 1: Mixed signature → HyperbolicLattice
       - (0, n-1, 1): Negative semidefinite → ParabolicLattice  
       - (n-1, 0, 1): Positive semidefinite → ParabolicLattice (converted to negative)
       - Other signatures → IndefiniteLattice or DegenerateLattice
    
    INPUT:
    
    - ``matrix`` -- n×n matrix defining the bilinear form
    - ``base_ring`` -- (default: None, auto-selects ZZ) base ring for coordinates
    - ``check`` -- (default: True) perform automatic analysis and validation
    
    OUTPUT:
    
    Most specialized subcategory object based on matrix properties
    
    SIMPLE USAGE EXAMPLES::
    
        sage: # ℤ-first: Simple integer lattices (most common case)
        sage: A2_gram = matrix([[-2, 1], [1, -2]])
        sage: L = BilinearModule(A2_gram)  # base_ring=ZZ automatically
        sage: L.base_ring()
        Integer Ring
        
        sage: # Hyperbolic lattice over ℤ
        sage: hyperbolic_gram = matrix([[-2, 3], [3, -2]])
        sage: H = BilinearModule(hyperbolic_gram)
        sage: H.signature()
        (1, 1, 0)
        
        sage: # Advanced: Explicit field for non-crystallographic types
        sage: K.<phi> = NumberField(x^2 - x - 1)  # Golden ratio field
        sage: H3_gram = matrix(K, [[-2, 1], [1, -2/phi]])
        sage: L_H3 = BilinearModule(H3_gram, base_ring=K)
        sage: L_H3.base_ring()
        Number Field in phi with defining polynomial x^2 - x - 1
    
    DETAILED EXAMPLES::
    
        sage: # General bilinear form (not symmetric) → FreeBilinearModule
        sage: B = matrix([[1, 2], [3, 4]])
        sage: M = BilinearModule(B)
        sage: type(M).__name__
        'FreeBilinearModule'
        sage: v, w = M([1, 0]), M([0, 1])
        sage: v * w != w * v  # Non-symmetric
        True
        
        sage: # Skew-symmetric matrix → SkewSymmetricBilinearModule  
        sage: S = matrix([[0, 1], [-1, 0]])
        sage: M2 = BilinearModule(S)
        sage: type(M2).__name__
        'SkewSymmetricBilinearModule'
        
        sage: # Symmetric, negative definite → EllipticLattice
        sage: G1 = matrix([[-2, 1], [1, -2]])
        sage: L1 = BilinearModule(G1)
        sage: type(L1).__name__
        'EllipticLattice'
        sage: L1.is_elliptic()
        True
        sage: L1.signature()
        (0, 2, 0)
        
        sage: # Symmetric, positive definite → EllipticLattice (converted)
        sage: G2 = matrix([[2, -1], [-1, 2]])
        sage: L2 = BilinearModule(G2)
        sage: type(L2).__name__
        'EllipticLattice'
        sage: L2.gram()  # Internally converted to negative definite
        [-2  1]
        [ 1 -2]
        
        sage: # Symmetric, indefinite → HyperbolicLattice
        sage: G3 = matrix([[-2, 3], [3, -2]]) 
        sage: L3 = BilinearModule(G3)
        sage: type(L3).__name__
        'HyperbolicLattice' 
        sage: L3.signature()
        (1, 1, 0)
        
        sage: # Symmetric, degenerate, negative semidefinite → ParabolicLattice
        sage: G4 = matrix([[-2, 1, 1], [1, -2, 1], [1, 1, -2]])
        sage: L4 = BilinearModule(G4)
        sage: type(L4).__name__
        'ParabolicLattice'
        sage: L4.is_parabolic()
        True
        sage: L4.signature()
        (0, 2, 1)
        
        sage: # Symmetric, general indefinite → IndefiniteLattice
        sage: G5 = matrix([[-2, 3, 0], [3, -2, 3], [0, 3, -2]])
        sage: L5 = BilinearModule(G5)
        sage: type(L5).__name__
        'IndefiniteLattice'
    
    ALGORITHM:
    
    The factory performs the following analysis::
    
        def BilinearModule(matrix, base_ring=None, check=True):
            # Step 0: Default base_ring selection
            if base_ring is None:
                base_ring = ZZ  # ℤ-first default for integer lattices
            # Step 1: Analyze matrix structure
            if not matrix.is_symmetric():
                if matrix.is_skew_symmetric():
                    return SkewSymmetricBilinearModule(matrix, base_ring)
                else:
                    return FreeBilinearModule(matrix, base_ring)
            
            # Step 2: Symmetric case - analyze signature
            signature = matrix.signature()  # (pos, neg, zero)
            determinant = matrix.determinant()
            
            # Step 3: Dispatch based on degeneracy and signature
            if determinant != 0:
                # Nondegenerate case
                return _create_lattice_by_signature(matrix, signature, base_ring)
            else:
                # Degenerate case  
                return _create_degenerate_lattice_by_signature(matrix, signature, base_ring)
    """
```

## API Design Philosophy

### ℤ-First Pattern

The `BilinearModule` factory follows a **ℤ-first** design pattern where the most common use case (integer lattices) requires minimal syntax:

```python
# SIMPLE: Most Coxeter lattices work over ℤ
L = BilinearModule(gram_matrix)                    # Automatic ZZ

# ADVANCED: When you need specific rings/fields  
L = BilinearModule(gram_matrix, base_ring=K)       # Explicit field
```

### When to Specify base_ring

- **Default (None)**: Integer gram matrices → automatic ZZ selection
- **Number fields**: Non-crystallographic types (H₃, H₄, I₂(p))
- **Rational fields**: When working with fractional coordinates
- **Finite fields**: For reduction/counting problems

### SageMath Category Framework Integration

The factory leverages SageMath's sophisticated category framework with automatic category joining:

**Automatic Category Joins:**
```python
# These are computed automatically by SageMath:
CoxeterLattices() & Lattices().Elliptic()    = EllipticCoxeterLattices()
CoxeterLattices() & Lattices().Hyperbolic()  = HyperbolicCoxeterLattices() 
CoxeterLattices() & DegenerateLattices().Parabolic() = ParabolicCoxeterLattices()
```

**Factory Dispatch Logic:**
1. **Matrix Analysis**: Symmetric, skew-symmetric, or general
2. **Signature Detection**: (p,q,r) classification for symmetric matrices  
3. **Category Assignment**: Most specialized applicable category
4. **Structure Discovery**: Additional properties trigger category joins

## Coxeter Structure Constructors

These functions create CoxeterLattices which combine lattice structure with Coxeter system embeddings:

```python
# In sage.modules.coxeter_lattices.factory:

def CoxeterLattice(lattice=None, coxeter_system=None, **kwargs):
    r"""
    Construct a Coxeter lattice (L, C) where C embeds into L.
    
    This is the primary constructor for objects in the CoxeterLattices category.
    Automatically detects lattice signature and creates appropriate combined type.
    
    INPUT:
    - lattice: Ambient lattice L (optional, can be computed from simple_roots)
    - coxeter_system: CoxeterSystem C = (Φ, ι) with ι: ⟨Φ⟩_R ↪ L
    - Alternatively, provide simple_roots to auto-construct both
    
    OUTPUT: 
    CoxeterLattice object with both lattice and Coxeter system structure
    
    RAISES:
    - ValueError: If provided lattice and coxeter_system are inconsistent
    """
    if lattice is None and 'simple_roots' in kwargs:
        # Construct both lattice and Coxeter system from simple roots
        simple_roots = kwargs['simple_roots']
        gram_matrix = compute_gram_matrix(simple_roots)
        lattice = BilinearModule(gram_matrix)  # Auto-detects signature
        coxeter_system = CoxeterSystem(simple_roots, lattice)
    
    # CRITICAL: Validate consistency if both lattice and coxeter_system are provided
    if lattice is not None and coxeter_system is not None:
        if lattice is not coxeter_system.ambient_lattice():
            raise ValueError(
                "The provided lattice is not the same object as the Coxeter system's "
                "ambient lattice. The CoxeterSystem embedding ι: ⟨Φ⟩_R ↪ L must "
                "target the provided lattice L. Consider using CoxeterLattice with "
                "only one argument to avoid this inconsistency."
            )
    
    # Create combined object via category joining
    base_category = lattice.category()
    combined_category = Category.join([base_category, CoxeterLattices()])
    return combined_category(lattice, coxeter_system)

def CoxeterLattice_from_cartan_type(cartan_type, ambient_lattice=None):
    r"""
    Construct CoxeterLattice from Cartan type.
    
    Creates both the CoxeterSystem and appropriate lattice automatically.
    
    INPUT:
    - cartan_type: Cartan type like 'A3', ['B', 4], etc.
    - ambient_lattice: Choice of ambient lattice ('weight', 'root', 'ambient')
    """
    coxeter_system = CoxeterSystem.from_cartan_type(cartan_type, ambient_lattice)
    lattice = coxeter_system.ambient_lattice()
    return CoxeterLattice(lattice, coxeter_system)

def CoxeterLattice_from_coxeter_matrix(coxeter_matrix):
    r"""
    Construct CoxeterLattice from Coxeter matrix.
    
    Creates the minimal lattice embedding for the given Coxeter matrix.
    """
    coxeter_system = CoxeterSystem.from_coxeter_matrix(coxeter_matrix)
    lattice = coxeter_system.ambient_lattice()
    return CoxeterLattice(lattice, coxeter_system)

def CoxeterLattice_from_simple_roots(simple_roots, ambient_lattice=None):
    r"""
    Construct CoxeterLattice from simple roots.
    
    INPUT:
    - simple_roots: List of vectors defining the simple root system
    - ambient_lattice: Optional ambient lattice (default: span of roots)
    """
    if ambient_lattice is None:
        gram_matrix = compute_gram_matrix(simple_roots)
        ambient_lattice = BilinearModule(gram_matrix)
    
    coxeter_system = CoxeterSystem(simple_roots, ambient_lattice)
    return CoxeterLattice(ambient_lattice, coxeter_system)
```

## Mathematical Test Assertions

### Factory Correctness for Root Lattices

```python
# Mathematical assertion 1: Factory creates correct elliptic lattice structures
# sage: R = RootSystem(['A', 3])
# sage: L = R.root_lattice()  # Factory method from RootSystem
# sage: L.rank()
# 3
# sage: L.is_elliptic()  # Must be finite type
# True
# sage: L.gram_matrix().is_symmetric()
# True

# Mathematical assertion 2: Factory respects weight lattice containment
# sage: R = RootSystem(['B', 2])
# sage: WL = R.weight_lattice()  # Factory creates weight lattice
# sage: RL = R.root_lattice()    # Factory creates root lattice  
# sage: all(RL(alpha) in WL for alpha in R.roots())  # Root lattice embeds in weight lattice
# True
# sage: WL.index(RL) == R.cartan_matrix().det()  # Index equals determinant of Cartan matrix
# True

# Mathematical assertion 3: Factory conversion preserves bilinear structure
# sage: R = RootSystem(['C', 3])
# sage: AL = R.ambient_lattice()  # Factory creates ambient space
# sage: RL = R.root_lattice()     # Factory creates root lattice
# sage: alpha = R.simple_roots()[0]
# sage: beta = R.simple_roots()[1]
# sage: AL(alpha).inner_product(AL(beta)) == RL(alpha).inner_product(RL(beta))
# True

# Mathematical assertion 4: Factory validates Coxeter matrix consistency
# sage: M = matrix([[1, 3, 2], [3, 1, 3], [2, 3, 1]])  # A3 Coxeter matrix
# sage: C = CoxeterLattice_from_coxeter_matrix(M)  # Factory method
# sage: C.coxeter_system().coxeter_matrix() == M
# True
# sage: all(C.reflection(i).order() == (2 if M[i,i] == 1 else infinity) for i in range(3))
# True

# Mathematical assertion 5: Factory produces canonical forms
# sage: gram_positive = matrix([[2, -1], [-1, 2]])  # Positive definite
# sage: L = BilinearModule(gram_positive)  # Factory auto-converts
# sage: L.gram_matrix() == -gram_positive  # Converted to negative definite canonical form
# True
# sage: L.is_elliptic()  # Correctly classified despite sign change
# True
```