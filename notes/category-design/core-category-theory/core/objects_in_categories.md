<!--
Origin: gitclones/Coxeter/implementation/planning/core/objects_in_categories.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Objects in Categories: Monoid, Group, and Ring Objects

This file defines the general notion of algebraic objects (monoids, groups, rings) internal to arbitrary monoidal categories.

## General Pattern

Given a monoidal category (C, ⊗, I), we can define algebraic structures as objects with appropriate morphisms satisfying coherence diagrams.

## Monoid Objects

```python
class MonoidObjects(CategoryWithAxiom):
    """
    The category of monoid objects in a monoidal category.
    
    A monoid object in a monoidal category (C, ⊗, I) is an object M
    together with:
    - Multiplication: μ: M ⊗ M → M
    - Unit: η: I → M
    
    satisfying associativity and unit axioms via commutative diagrams.
    
    EXAMPLES::
    
        sage: # Classical example: Monoids in Set
        sage: from sage.categories.sets_cat import Sets
        sage: MonoidObjects(Sets())
        Category of monoids
        
        sage: # Ring as monoid object in Ab
        sage: from sage.categories.abelian_groups import AbelianGroups
        sage: MonoidObjects(AbelianGroups())
        Category of rings  # (unital, possibly non-commutative)
        
        sage: # R-algebra as monoid object in R-Mod
        sage: from sage.categories.modules import Modules
        sage: MonoidObjects(Modules(ZZ))
        Category of algebras over Integer Ring
        
        sage: # Hopf algebra as monoid object in tensor category
        sage: from sage.categories.coalgebras import Coalgebras
        sage: MonoidObjects(Coalgebras(QQ))
        Category of bialgebras over Rational Field
    """
    
    def __init__(self, ambient_category):
        """
        Initialize the category of monoid objects.
        
        INPUT:
        - ambient_category -- a monoidal category
        
        EXAMPLES::
        
            sage: C = MonoidObjects(VectorSpaces(QQ))
            sage: C.ambient_category()
            Category of vector spaces over Rational Field
        """
        if not hasattr(ambient_category, 'tensor_product'):
            raise ValueError(f"{ambient_category} must be a monoidal category")
        self._ambient = ambient_category
        super().__init__()
    
    def super_categories(self):
        """
        Monoid objects form a subcategory of the ambient category.
        
        EXAMPLES::
        
            sage: MonoidObjects(Modules(ZZ)).super_categories()
            [Category of modules over Integer Ring]
        """
        return [self._ambient]
    
    def _repr_(self):
        """
        String representation.
        
        EXAMPLES::
        
            sage: MonoidObjects(Sets())
            Category of monoids
            
            sage: MonoidObjects(Modules(QQ))
            Category of algebras over Rational Field
        """
        # Special cases for common categories
        if self._ambient == Sets():
            return "Category of monoids"
        elif self._ambient in Modules:
            R = self._ambient.base_ring()
            return f"Category of algebras over {R}"
        elif self._ambient == AbelianGroups():
            return "Category of rings"
        else:
            return f"Category of monoid objects in {self._ambient}"
    
    class ParentMethods:
        """
        Methods for monoid objects.
        """
        
        def multiplication(self):
            """
            Return the multiplication morphism μ: M ⊗ M → M.
            
            EXAMPLES::
            
                sage: # For an R-algebra
                sage: A = PolynomialRing(QQ, 'x')
                sage: mu = A.multiplication()
                sage: # mu(x ⊗ x) = x²
                
                sage: # For a monoid in Set
                sage: M = SymmetricGroup(3)
                sage: mu = M.multiplication()
                sage: # mu(g, h) = g * h
            """
            raise NotImplementedError
        
        def unit(self):
            """
            Return the unit morphism η: I → M.
            
            The unit I is the tensor unit of the ambient category.
            
            EXAMPLES::
            
                sage: # For an R-algebra, I = R
                sage: A = MatrixSpace(QQ, 2)
                sage: eta = A.unit()
                sage: eta(1)  # 1 ∈ QQ maps to identity matrix
                [1 0]
                [0 1]
                
                sage: # For a monoid in Set, I = {*}
                sage: M = Integers(12)
                sage: eta = M.unit()
                sage: eta(*)  # The unique element of I maps to 0
                0
            """
            raise NotImplementedError
        
        def is_associative(self):
            """
            Verify the associativity axiom.
            
            Checks that the following diagram commutes:
            
            (M⊗M)⊗M --μ⊗id--> M⊗M
                |                 |
                α                 μ
                |                 |
                v                 v
            M⊗(M⊗M) --id⊗μ--> M⊗M --μ--> M
            
            EXAMPLES::
            
                sage: R.<x,y> = PolynomialRing(QQ)
                sage: R.is_associative()
                True  # Polynomial multiplication is associative
            """
            raise NotImplementedError
        
        def is_unital(self):
            """
            Verify the unit axioms.
            
            Checks that these diagrams commute:
            
            Left unit:             Right unit:
            I⊗M --η⊗id--> M⊗M     M⊗I --id⊗η--> M⊗M
             |              |       |              |
             λ              μ       ρ              μ
             |              |       |              |
             v              v       v              v
             M <-----------M        M <-----------M
                    id                     id
            
            EXAMPLES::
            
                sage: A = GroupAlgebra(SymmetricGroup(3), QQ)
                sage: A.is_unital()
                True  # Has multiplicative identity
            """
            raise NotImplementedError
    
    class ElementMethods:
        """
        Methods for elements of monoid objects.
        """
        
        def __mul__(self, other):
            """
            Multiplication using the monoid structure.
            
            EXAMPLES::
            
                sage: # In an R-algebra
                sage: R.<x> = PolynomialRing(ZZ)
                sage: x * x
                x^2
                
                sage: # In a monoid
                sage: G = SymmetricGroup(3)
                sage: g, h = G.gens()
                sage: g * h != h * g  # Non-commutative
                True
            """
            M = self.parent()
            tensor = M.tensor_product(M)
            mu = M.multiplication()
            return mu(tensor(self, other))
    
    class Commutative(CategoryWithAxiom):
        """
        The axiom for commutative monoid objects.
        
        The multiplication satisfies μ ∘ β = μ where β is the braiding.
        """
        
        def extra_super_categories(self):
            """
            Commutative monoids require a braided ambient category.
            
            EXAMPLES::
            
                sage: C = MonoidObjects(Modules(ZZ)).Commutative()
                sage: C
                Category of commutative algebras over Integer Ring
            """
            # Only makes sense if ambient is braided
            if not hasattr(self.base_category()._ambient, 'braiding'):
                raise ValueError("Commutativity requires braided ambient category")
            return []


## Group Objects

```python
class GroupObjects(MonoidObjects):
    """
    The category of group objects in a monoidal category.
    
    A group object is a monoid object G with an inverse morphism
    ι: G → G such that μ(id ⊗ ι) = η ∘ ε and μ(ι ⊗ id) = η ∘ ε
    where ε: G → I is the counit.
    
    EXAMPLES::
    
        sage: # Classical example: Groups in Set
        sage: GroupObjects(Sets())
        Category of groups
        
        sage: # Group objects in finite sets = finite groups
        sage: GroupObjects(FiniteSets())
        Category of finite groups
        
        sage: # Hopf algebras are group objects in certain tensor categories
        sage: # (when they have antipode)
    """
    
    def _repr_(self):
        """
        String representation.
        
        EXAMPLES::
        
            sage: GroupObjects(Sets())
            Category of groups
            
            sage: GroupObjects(FiniteSets())
            Category of finite groups
        """
        if self._ambient == Sets():
            return "Category of groups"
        elif self._ambient == FiniteSets():
            return "Category of finite groups"
        else:
            return f"Category of group objects in {self._ambient}"
    
    class ParentMethods:
        """
        Methods for group objects.
        """
        
        def inverse_morphism(self):
            """
            Return the inverse morphism ι: G → G.
            
            EXAMPLES::
            
                sage: G = SymmetricGroup(3)
                sage: iota = G.inverse_morphism()
                sage: g = G.an_element()
                sage: iota(g) == g.inverse()
                True
            """
            raise NotImplementedError
        
        def is_group_object(self):
            """
            Verify the group object axioms.
            
            Checks:
            1. Is a monoid object
            2. Inverse axioms hold
            
            EXAMPLES::
            
                sage: GL3 = GeneralLinearGroup(3, QQ)
                sage: GL3.is_group_object()
                True
            """
            if not self.is_associative() or not self.is_unital():
                return False
            # Check inverse axioms
            # ...
            return True


## Ring Objects

```python
class RingObjects(CategoryWithAxiom):
    """
    The category of ring objects in a monoidal category.
    
    A ring object in a monoidal category (C, ⊗, I) is:
    - An abelian group object in C (with addition +)
    - A monoid object in C (with multiplication ×)
    - Distributivity of × over +
    
    The classical case: Ring objects in (Ab, ⊗_Z, Z) are ordinary rings.
    
    EXAMPLES::
    
        sage: # Ring objects in Ab = ordinary rings
        sage: RingObjects(AbelianGroups())
        Category of rings
        
        sage: # Ring objects in R-Mod = R-algebras
        sage: RingObjects(Modules(ZZ))
        Category of algebras over Integer Ring
        
        sage: # Ring objects in Vect_k = k-algebras  
        sage: RingObjects(VectorSpaces(QQ))
        Category of algebras over Rational Field
    """
    
    def __init__(self, ambient_category):
        """
        Initialize the category of ring objects.
        
        The ambient category must be additive (have biproducts).
        
        EXAMPLES::
        
            sage: C = RingObjects(Modules(ZZ))
            sage: C
            Category of algebras over Integer Ring
        """
        # Ring objects need additive structure
        if not hasattr(ambient_category, 'direct_sum'):
            raise ValueError(f"{ambient_category} must be an additive category")
        self._ambient = ambient_category
        super().__init__()
    
    def _repr_(self):
        """
        String representation.
        
        EXAMPLES::
        
            sage: RingObjects(AbelianGroups())
            Category of rings
            
            sage: RingObjects(Modules(QQ))
            Category of algebras over Rational Field
        """
        if self._ambient == AbelianGroups():
            return "Category of rings"
        elif self._ambient in Modules:
            R = self._ambient.base_ring()
            return f"Category of algebras over {R}"
        else:
            return f"Category of ring objects in {self._ambient}"
    
    class ParentMethods:
        """
        Methods for ring objects.
        """
        
        def addition(self):
            """
            Return the addition morphism +: R ⊕ R → R.
            
            Here ⊕ is the biproduct (direct sum) in the category.
            
            EXAMPLES::
            
                sage: R = PolynomialRing(QQ, 'x')
                sage: add = R.addition()
                sage: # add(x ⊕ x²) = x + x²
            """
            raise NotImplementedError
        
        def multiplication(self):
            """
            Return the multiplication morphism ×: R ⊗ R → R.
            
            EXAMPLES::
            
                sage: R = MatrixSpace(QQ, 2)
                sage: mult = R.multiplication()
                sage: # mult(A ⊗ B) = A * B (matrix multiplication)
            """
            raise NotImplementedError
        
        def zero(self):
            """
            Return the zero morphism 0: I → R.
            
            EXAMPLES::
            
                sage: R = PolynomialRing(ZZ, 'x')
                sage: zero = R.zero()
                sage: zero(1)  # 1 ∈ ZZ maps to 0 ∈ R[x]
                0
            """
            raise NotImplementedError
        
        def unit(self):
            """
            Return the multiplicative unit morphism 1: I → R.
            
            EXAMPLES::
            
                sage: R = Integers(12)
                sage: one = R.unit()
                sage: one(1)  # 1 ∈ ZZ maps to 1 ∈ Z/12Z
                1
            """
            raise NotImplementedError
        
        def is_distributive(self):
            """
            Verify distributivity of multiplication over addition.
            
            Checks both left and right distributivity.
            
            EXAMPLES::
            
                sage: R = PolynomialRing(QQ, ['x', 'y'])
                sage: R.is_distributive()
                True
            """
            raise NotImplementedError
    
    class Commutative(CategoryWithAxiom):
        """
        The axiom for commutative ring objects.
        """
        pass


## Concrete Examples

### Example 1: R-Algebras as Monoid Objects in R-Mod

```python
def RAlgebras(R):
    """
    The category of R-algebras as monoid objects in R-modules.
    
    An R-algebra is precisely a monoid object in (R-Mod, ⊗_R, R).
    
    EXAMPLES::
    
        sage: from sage.categories.algebras import Algebras
        sage: A1 = Algebras(QQ)
        sage: A2 = MonoidObjects(Modules(QQ))
        sage: A1 is A2
        True  # They are the same category!
        
        sage: # Concrete algebra
        sage: M = MatrixSpace(QQ, 2)
        sage: M in MonoidObjects(Modules(QQ))
        True
        
        sage: # Check structure maps
        sage: mu = M.multiplication()  # μ: M ⊗_QQ M → M
        sage: eta = M.unit()           # η: QQ → M
        
        sage: # Multiplication of matrices
        sage: A = M([[1, 2], [3, 4]])
        sage: B = M([[5, 6], [7, 8]])
        sage: mu(A.tensor(B)) == A * B
        True
        
        sage: # Unit is identity matrix
        sage: eta(1) == M.identity_matrix()
        True
    """
    return MonoidObjects(Modules(R))


### Example 2: Lie Algebras as Objects with Bracket

```python
class LieAlgebraObjects(CategoryWithAxiom):
    """
    Lie algebra objects in a symmetric monoidal category.
    
    A Lie algebra object is an object L with a morphism
    [,]: L ⊗ L → L (the Lie bracket) satisfying:
    - Antisymmetry: [,] ∘ β = -[,]
    - Jacobi identity (as a commutative diagram)
    
    EXAMPLES::
    
        sage: # Classical Lie algebras
        sage: LieAlgebraObjects(VectorSpaces(QQ))
        Category of Lie algebras over Rational Field
        
        sage: # Lie algebra objects in supermodules = super Lie algebras
        sage: LieAlgebraObjects(SuperModules(QQ))
        Category of super Lie algebras over Rational Field
    """
    pass


### Example 3: Hopf Algebras as Group Objects

```python
class HopfAlgebraObjects(GroupObjects):
    """
    Hopf algebras as group objects in the category of coalgebras.
    
    A Hopf algebra is:
    - A bialgebra (monoid object in coalgebras)
    - With antipode S: H → H (giving group structure)
    
    EXAMPLES::
    
        sage: # Group algebra is a Hopf algebra
        sage: G = SymmetricGroup(3)
        sage: H = GroupAlgebra(G, QQ)
        sage: H in HopfAlgebraObjects(Coalgebras(QQ))
        True
        
        sage: # Check antipode
        sage: S = H.antipode()
        sage: g = G.an_element()
        sage: S(g) == g.inverse()
        True
    """
    pass
```

## Coherence Diagrams

### Associativity for Monoid Objects
```
(M⊗M)⊗M ----μ⊗id----> M⊗M
    |                    |
    α                    μ
    |                    |
    v                    v
M⊗(M⊗M) ----id⊗μ----> M⊗M ----μ----> M
```

### Unit Laws for Monoid Objects
```
Left unit:               Right unit:
I⊗M --η⊗id--> M⊗M       M⊗I --id⊗η--> M⊗M
 |              |         |              |
 λ              μ         ρ              μ
 |              |         |              |
 v              v         v              v
 M <---------- M          M <---------- M
       id                        id
```

### Distributivity for Ring Objects
```
Left distributivity:
R⊗(R⊕R) --id⊗+-> R⊗R --×-> R
    |                         ^
    ≅                         |
    |                         +
    v                         |
(R⊗R)⊕(R⊗R) --×⊕×-> R⊕R ----+

Right distributivity is similar.
```

## Key Insights

1. **Unification**: Algebras, rings, groups all arise as "objects with structure" in appropriate categories

2. **Internalization**: We can define algebraic structures internal to any category with enough structure

3. **Examples Everywhere**:
   - Monoid objects in (Set, ×, 1) = monoids
   - Monoid objects in (Ab, ⊗, Z) = rings  
   - Monoid objects in (R-Mod, ⊗_R, R) = R-algebras
   - Group objects in (Top, ×, pt) = topological groups

4. **Coherence is Key**: The diagrams ensure the algebraic laws hold categorically

This approach beautifully unifies many mathematical structures under a single framework!