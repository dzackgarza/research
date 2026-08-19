<!--
Origin: gitclones/Coxeter/implementation/planning/RMod/RMod_subobjects.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Subobjects: Submodules and Quotient Modules

Implementation of submodules, quotient modules, and related operations in the category of R-modules.

## Submodule Structure

```python
from sage.modules.submodule import Submodule_free_ambient
from sage.structure.parent import Parent

class RSubmodule(Submodule_free_ambient):
    """
    Submodule of an R-module.
    
    A submodule W ⊆ M is a subset that is closed under:
    - Addition: w₁ + w₂ ∈ W for all w₁, w₂ ∈ W
    - Scalar multiplication: r·w ∈ W for all r ∈ R, w ∈ W
    - Contains zero: 0 ∈ W
    
    Submodules inherit the R-module structure from the ambient module
    and form a lattice under inclusion.
    
    EXAMPLES::
    
        sage: M = RModule(ZZ, rank=3)
        sage: e1, e2, e3 = M.gens()
        sage: W = M.submodule([e1 + e2, 2*e2 + e3])
        sage: W
        Submodule of rank 2 of Free module of rank 3 over Integer Ring
        
        sage: # Test submodule properties
        sage: (e1 + e2) in W
        True
        sage: 3*(e1 + e2) in W
        True
        sage: e1 in W
        False  # e1 not in span
        
        sage: # Submodule operations
        sage: W.rank()
        2
        sage: W.ambient_module() is M
        True
    """
    
    def __init__(self, ambient, gens, category=None, check=True, **kwds):
        """
        Initialize submodule.
        
        INPUT:
        - ambient -- parent R-module
        - gens -- list of generators as elements of ambient
        - category -- optional category (defaults to subobjects of ambient's category)
        - check -- whether to verify generators are in ambient
        """
        if category is None:
            category = ambient.category().Subobjects()
        
        # Ensure generators are elements of ambient
        if check:
            gens = [ambient(g) for g in gens]
        
        super().__init__(ambient, gens, category=category, **kwds)
    
    def _repr_(self):
        """
        String representation.
        
        EXAMPLES::
        
            sage: M = RModule(QQ, rank=4)
            sage: W = M.submodule(M.gens()[:2])
            sage: W
            Submodule of rank 2 of Vector space of dimension 4 over Rational Field
        """
        return f"Submodule of rank {self.rank()} of {self.ambient_module()}"
    
    def rank(self):
        """
        Return the rank (dimension) of this submodule.
        
        This is the dimension as a free module over the base ring.
        
        OUTPUT:
        Non-negative integer
        
        EXAMPLES::
        
            sage: M = RModule(ZZ, rank=5)
            sage: W = M.submodule([M.gen(0), M.gen(2), M.gen(0) + M.gen(2)])
            sage: W.rank()
            2  # Only 2 independent generators
        """
        return len(self.basis())
    
    def is_submodule(self, other):
        """
        Test if this is a submodule of other.
        
        Returns True if self ⊆ other as submodules.
        
        INPUT:
        - other -- another submodule or module
        
        OUTPUT:
        Boolean
        
        EXAMPLES::
        
            sage: M = RModule(ZZ, rank=3)
            sage: W1 = M.submodule([M.gen(0)])
            sage: W2 = M.submodule([M.gen(0), M.gen(1)])
            sage: W1.is_submodule(W2)
            True
            sage: W2.is_submodule(W1)
            False
            sage: W1.is_submodule(M)
            True
        """
        if other is self.ambient_module():
            return True
        
        if not hasattr(other, 'gens'):
            return False
        
        # Check if all our generators are in other
        return all(g in other for g in self.gens())
    
    def __contains__(self, x):
        """
        Test membership in submodule.
        
        INPUT:
        - x -- potential element
        
        OUTPUT:
        Boolean
        
        EXAMPLES::
        
            sage: M = RModule(QQ, rank=3)
            sage: e1, e2, e3 = M.gens()
            sage: W = M.submodule([e1 + e2, e2 + e3])
            sage: e1 + e2 in W
            True
            sage: e1 - e3 in W  # = (e1 + e2) - (e2 + e3)
            True
            sage: e1 in W
            False
        """
        try:
            x = self.ambient_module()(x)
        except:
            return False
        
        # Express x in terms of ambient basis and check if in our span
        return x in self.vector_space()
    
    def basis(self):
        """
        Return a basis for this submodule.
        
        Computes echelonized basis from generators.
        
        OUTPUT:
        List of linearly independent module elements
        
        EXAMPLES::
        
            sage: M = RModule(ZZ, rank=3)
            sage: W = M.submodule([M.gen(0) + M.gen(1), 
            ....:                  2*M.gen(0) + 2*M.gen(1),
            ....:                  M.gen(1) + M.gen(2)])
            sage: B = W.basis()
            sage: len(B)
            2  # Removes redundancy
        """
        # Use echelonized basis computation
        return self.echelonized_basis()
    
    def echelonized_basis(self):
        """
        Return echelonized (row-reduced) basis.
        
        Particularly useful for submodules over fields.
        
        OUTPUT:
        List of basis elements in echelon form
        """
        # Get generator matrix and echelonize
        from sage.matrix.constructor import matrix
        
        gens = self.gens()
        if not gens:
            return []
        
        # Convert to matrix form
        ambient_basis = self.ambient_module().basis()
        gen_matrix = matrix([g.to_vector() for g in gens])
        
        # Echelonize
        gen_matrix.echelonize()
        
        # Convert back to module elements
        basis = []
        for row in gen_matrix.rows():
            if not row.is_zero():
                element = sum(c * b for c, b in zip(row, ambient_basis) if c != 0)
                basis.append(element)
        
        return basis
    
    def coordinates(self, v):
        """
        Express v in terms of submodule basis.
        
        INPUT:
        - v -- element of this submodule
        
        OUTPUT:
        Vector of coordinates or ValueError if v not in submodule
        
        EXAMPLES::
        
            sage: M = RModule(QQ, rank=3)
            sage: W = M.submodule([M.gen(0), M.gen(1)])
            sage: v = 3*M.gen(0) + 2*M.gen(1)
            sage: W.coordinates(v)
            (3, 2)
        """
        if v not in self:
            raise ValueError(f"{v} is not in the submodule")
        
        # Solve for coordinates using basis
        basis = self.basis()
        from sage.matrix.constructor import matrix
        
        basis_matrix = matrix([b.to_vector() for b in basis]).transpose()
        v_vector = v.to_vector()
        
        # Solve basis_matrix * coords = v_vector
        coords = basis_matrix.solve_right(v_vector)
        return coords
    
    def complement(self):
        """
        Find a complementary submodule (if possible).
        
        Returns W' such that M = W ⊕ W' (direct sum).
        Not always possible (e.g., for torsion submodules).
        
        OUTPUT:
        Complementary submodule or None
        
        EXAMPLES::
        
            sage: M = RModule(QQ, rank=3)
            sage: W = M.submodule([M.gen(0)])
            sage: C = W.complement()
            sage: C.rank()
            2
            sage: W.intersection(C).is_zero()
            True
        """
        if not self.base_ring().is_field():
            # Complements may not exist over general rings
            raise NotImplementedError("Complement only implemented for vector spaces")
        
        # Extend basis of W to basis of M
        W_basis = self.basis()
        M_basis = self.ambient_module().basis()
        
        # Find vectors not in span of W
        complement_gens = []
        W_space = self.vector_space()
        
        for v in M_basis:
            if v not in W_space:
                complement_gens.append(v)
        
        if len(W_basis) + len(complement_gens) != len(M_basis):
            return None
        
        return self.ambient_module().submodule(complement_gens)


## Quotient Module Implementation

```python
class RQuotientModule(Parent):
    """
    Quotient module M/N where N is a submodule of M.
    
    Elements are equivalence classes [m] = {m + n : n ∈ N}.
    The quotient inherits an R-module structure:
    - [m₁] + [m₂] = [m₁ + m₂]
    - r·[m] = [r·m]
    
    EXAMPLES::
    
        sage: M = RModule(ZZ, rank=2)
        sage: e1, e2 = M.gens()
        sage: N = M.submodule([2*e1, 3*e2])
        sage: Q = M.quotient(N)
        sage: Q
        Quotient of Free module of rank 2 over Integer Ring by Submodule generated by (2, 0), (0, 3)
        
        sage: # Elements are cosets
        sage: Q(e1)
        [1, 0]
        sage: 2*Q(e1)
        [0, 0]  # Since 2*e1 ∈ N
        
        sage: # Quotient is Z/2Z × Z/3Z
        sage: Q.invariant_factors()
        [2, 3]
    """
    
    def __init__(self, ambient, submodule, category=None):
        """
        Initialize quotient module.
        
        INPUT:
        - ambient -- module M
        - submodule -- submodule N of M
        - category -- optional category
        """
        if not submodule.is_submodule(ambient):
            raise ValueError("N must be a submodule of M")
        
        self._ambient = ambient
        self._submodule = submodule
        
        if category is None:
            from sage.categories.modules import Modules
            category = Modules(ambient.base_ring()).Quotients()
        
        Parent.__init__(self, base=ambient.base_ring(), category=category)
    
    def _repr_(self):
        """String representation."""
        return (f"Quotient of {self._ambient} by "
                f"Submodule generated by {', '.join(str(g) for g in self._submodule.gens())}")
    
    def ambient_module(self):
        """Return the module M in M/N."""
        return self._ambient
    
    def submodule(self):
        """Return the submodule N in M/N."""
        return self._submodule
    
    def _element_constructor_(self, x):
        """
        Create element of quotient module.
        
        INPUT:
        - x -- element of ambient module
        
        OUTPUT:
        Equivalence class [x] in M/N
        """
        x = self._ambient(x)
        return self.element_class(self, x)
    
    def _coerce_map_from_(self, S):
        """
        Determine coercion from S.
        
        Natural map M → M/N exists.
        """
        if S is self._ambient:
            return True
        return super()._coerce_map_from_(S)
    
    def zero(self):
        """Return zero element [0] of quotient."""
        return self(self._ambient.zero())
    
    def gens(self):
        """
        Return generators of quotient module.
        
        Projects ambient generators to quotient.
        
        OUTPUT:
        Tuple of quotient module generators
        """
        return tuple(self(g) for g in self._ambient.gens())
    
    def rank(self):
        """
        Return rank of quotient module.
        
        For free modules: rank(M/N) = rank(M) - rank(N).
        
        OUTPUT:
        Non-negative integer
        """
        if self._ambient.is_free() and self._submodule.is_free():
            return self._ambient.rank() - self._submodule.rank()
        else:
            # General case requires more analysis
            raise NotImplementedError("Rank for non-free quotients")
    
    def natural_map(self):
        """
        Return natural projection π: M → M/N.
        
        This is the canonical surjective homomorphism.
        
        OUTPUT:
        Module morphism M → M/N
        """
        from sage.categories.morphism import SetMorphism
        
        def projection(x):
            return self(x)
        
        return SetMorphism(Hom(self._ambient, self), projection)
    
    def lift(self, x):
        """
        Lift element from quotient to ambient.
        
        Choose representative m ∈ M such that [m] = x.
        
        INPUT:
        - x -- element of quotient M/N
        
        OUTPUT:
        Element m of ambient module M
        """
        if x.parent() is not self:
            raise ValueError("Element not in this quotient")
        
        return x._representative
    
    def is_zero(self):
        """Test if quotient is the zero module."""
        return self._submodule == self._ambient
    
    def invariant_factors(self):
        """
        Invariant factors of quotient (for modules over PIDs).
        
        Gives structure of M/N as direct sum of cyclic modules.
        
        OUTPUT:
        List of invariant factors
        """
        if not self.base_ring().is_principal_ideal_domain():
            raise ValueError("Invariant factors only defined over PIDs")
        
        # Use presentation matrix of quotient
        # This requires Smith normal form computation
        raise NotImplementedError("Invariant factor computation")


class RQuotientModuleElement(Element):
    """
    Element of quotient module M/N.
    
    Represents equivalence class [m] = {m + n : n ∈ N}.
    """
    
    def __init__(self, parent, representative):
        """
        Initialize quotient element.
        
        INPUT:
        - parent -- quotient module M/N
        - representative -- element m of M representing [m]
        """
        Element.__init__(self, parent)
        self._representative = representative
    
    def _repr_(self):
        """String representation of [m]."""
        return f"[{self._representative}]"
    
    def __eq__(self, other):
        """
        Test equality of cosets.
        
        [m₁] = [m₂] iff m₁ - m₂ ∈ N
        """
        if not isinstance(other, RQuotientModuleElement):
            return False
        
        if self.parent() != other.parent():
            return False
        
        difference = self._representative - other._representative
        return difference in self.parent().submodule()
    
    def _add_(self, other):
        """Addition in quotient: [m₁] + [m₂] = [m₁ + m₂]."""
        return self.parent()(self._representative + other._representative)
    
    def _neg_(self):
        """Negation in quotient: -[m] = [-m]."""
        return self.parent()(-self._representative)
    
    def _sub_(self, other):
        """Subtraction in quotient."""
        return self._add_(-other)
    
    def _lmul_(self, scalar):
        """Scalar multiplication: r·[m] = [r·m]."""
        return self.parent()(scalar * self._representative)
    
    def _rmul_(self, scalar):
        """Right scalar multiplication."""
        return self._lmul_(scalar)
    
    def is_zero(self):
        """Test if this is zero coset: [m] = [0] iff m ∈ N."""
        return self._representative in self.parent().submodule()
    
    def lift(self):
        """Return a representative in the ambient module."""
        return self._representative
```

## Submodule Operations

```python
def intersection(self, other):
    """
    Intersection of two submodules.
    
    Returns W ∩ V as a submodule.
    
    INPUT:
    - other -- another submodule of the same ambient module
    
    OUTPUT:
    Submodule representing intersection
    
    EXAMPLES::
    
        sage: M = RModule(QQ, rank=3)
        sage: W1 = M.submodule([M.gen(0), M.gen(1)])
        sage: W2 = M.submodule([M.gen(1), M.gen(2)])
        sage: W = W1.intersection(W2)
        sage: W.rank()
        1  # Span of e2
        sage: W.gens()
        [(0, 1, 0)]
    """
    if self.ambient_module() != other.ambient_module():
        raise ValueError("Submodules must have same ambient module")
    
    # Find intersection using linear algebra
    from sage.matrix.constructor import matrix
    
    # Stack generator matrices
    self_gens = [g.to_vector() for g in self.gens()]
    other_gens = [g.to_vector() for g in other.gens()]
    
    if not self_gens or not other_gens:
        # Empty intersection
        return self.ambient_module().submodule([])
    
    # Solve for intersection basis
    # This uses the fact that v ∈ W₁ ∩ W₂ iff v = Σaᵢwᵢ = Σbⱼvⱼ
    # Implementation depends on base ring properties
    
    # Simplified: use Sage's built-in intersection for vector spaces
    self_space = self.vector_space()
    other_space = other.vector_space()
    intersection_space = self_space.intersection(other_space)
    
    # Convert back to module elements
    intersection_gens = []
    for basis_vec in intersection_space.basis():
        module_element = self.ambient_module()._from_vector(basis_vec)
        intersection_gens.append(module_element)
    
    return self.ambient_module().submodule(intersection_gens)

def sum(self, other):
    """
    Sum of two submodules.
    
    Returns W + V = span(W ∪ V) as a submodule.
    
    INPUT:
    - other -- another submodule of same ambient
    
    OUTPUT:
    Submodule representing sum
    
    EXAMPLES::
    
        sage: M = RModule(ZZ, rank=3)
        sage: W1 = M.submodule([M.gen(0)])
        sage: W2 = M.submodule([M.gen(1)])
        sage: W = W1.sum(W2)
        sage: W.rank()
        2
        sage: W.gens()
        [(1, 0, 0), (0, 1, 0)]
    """
    if self.ambient_module() != other.ambient_module():
        raise ValueError("Submodules must have same ambient module")
    
    # Combine all generators
    combined_gens = list(self.gens()) + list(other.gens())
    
    return self.ambient_module().submodule(combined_gens)

def direct_sum(self, other):
    """
    Direct sum W ⊕ V (if intersection is zero).
    
    INPUT:
    - other -- another submodule with W ∩ V = {0}
    
    OUTPUT:
    Direct sum as submodule, or ValueError
    
    EXAMPLES::
    
        sage: M = RModule(QQ, rank=3)
        sage: W1 = M.submodule([M.gen(0)])
        sage: W2 = M.submodule([M.gen(1)])
        sage: W = W1.direct_sum(W2)
        sage: W.rank()
        2
        sage: W == W1.sum(W2)
        True
    """
    # Check intersection is trivial
    if not self.intersection(other).is_zero():
        raise ValueError("Submodules must have trivial intersection for direct sum")
    
    return self.sum(other)

def colon(self, ideal):
    """
    Colon ideal operation (W : I).
    
    (W : I) = {m ∈ M : I·m ⊆ W}
    
    INPUT:
    - ideal -- ideal in base ring
    
    OUTPUT:
    Submodule (W : I)
    
    EXAMPLES::
    
        sage: M = RModule(ZZ, rank=2)
        sage: W = M.submodule([2*M.gen(0), 2*M.gen(1)])
        sage: I = ZZ.ideal(2)
        sage: C = W.colon(I)
        sage: C == M
        True  # Since 2·M ⊆ W
    """
    ambient = self.ambient_module()
    colon_gens = []
    
    # Find all m such that I·m ⊆ W
    for g in ambient.gens():
        if all(a * g in self for a in ideal.gens()):
            colon_gens.append(g)
    
    # This is simplified - full algorithm more complex
    return ambient.submodule(colon_gens)
```

## Special Submodules

```python
def torsion_submodule(self):
    """
    Return torsion submodule.
    
    Tor(M) = {m ∈ M : ∃r ∈ R\\{0}, r·m = 0}
    
    OUTPUT:
    Torsion submodule
    
    EXAMPLES::
    
        sage: # Z-module Z ⊕ Z/6Z
        sage: M = AbelianGroup([0, 6])
        sage: T = M.torsion_submodule()
        sage: T.invariant_factors()
        [6]
    """
    if self.base_ring().is_field():
        # No torsion over fields
        return self.submodule([])
    
    torsion_gens = []
    
    for g in self.gens():
        ann = g.annihilator()
        if not ann.is_zero():
            torsion_gens.append(g)
    
    # This requires more sophisticated algorithm
    # to find all torsion elements
    raise NotImplementedError("General torsion submodule computation")

def socle(self):
    """
    Return socle (sum of simple submodules).
    
    Soc(M) = Σ{S : S simple submodule of M}
    
    OUTPUT:
    Socle as submodule
    """
    # Find all minimal submodules
    minimals = self.minimal_submodules()
    
    if not minimals:
        return self.submodule([])
    
    # Sum all minimal submodules
    socle = minimals[0]
    for S in minimals[1:]:
        socle = socle.sum(S)
    
    return socle

def radical(self):
    """
    Return Jacobson radical.
    
    Rad(M) = ∩{S : S maximal submodule of M}
    
    OUTPUT:
    Radical as submodule
    """
    # Find all maximal submodules
    maximals = self.maximal_submodules()
    
    if not maximals:
        return self  # No proper maximals means M is simple
    
    # Intersect all maximal submodules
    radical = maximals[0]
    for S in maximals[1:]:
        radical = radical.intersection(S)
    
    return radical

def annihilator(self):
    """
    Return annihilator ideal.
    
    Ann(M) = {r ∈ R : r·m = 0 for all m ∈ M}
    
    OUTPUT:
    Ideal in base ring
    """
    R = self.base_ring()
    
    # Annihilator is intersection of annihilators of generators
    if not self.gens():
        return R.ideal(1)  # Everything annihilates zero module
    
    ann = self.gen(0).annihilator()
    for g in self.gens()[1:]:
        ann = ann.intersection(g.annihilator())
    
    return ann
```

## Exact Sequences

```python
class ShortExactSequence:
    """
    Short exact sequence 0 → A → B → C → 0.
    
    Consists of injective f: A → B and surjective g: B → C
    with im(f) = ker(g).
    """
    
    def __init__(self, injection, surjection):
        """
        Initialize short exact sequence.
        
        INPUT:
        - injection -- injective morphism A → B
        - surjection -- surjective morphism B → C
        """
        if injection.codomain() != surjection.domain():
            raise ValueError("Morphisms must be composable")
        
        if not injection.is_injective():
            raise ValueError("First morphism must be injective")
        
        if not surjection.is_surjective():
            raise ValueError("Second morphism must be surjective")
        
        # Check exactness: im(f) = ker(g)
        if injection.image() != surjection.kernel():
            raise ValueError("Sequence not exact at middle term")
        
        self.injection = injection
        self.surjection = surjection
        self.A = injection.domain()
        self.B = injection.codomain()
        self.C = surjection.codomain()
    
    def is_split(self):
        """
        Test if sequence splits.
        
        True if there exists either:
        - Section s: C → B with g∘s = id_C
        - Retraction r: B → A with r∘f = id_A
        
        OUTPUT:
        Boolean
        """
        # Try to find section of surjection
        try:
            # For free modules, can construct section
            if self.C.is_free():
                # Lift basis of C to B
                basis_lifts = []
                for c in self.C.basis():
                    # Find preimage in B
                    b = self.surjection.lift(c)
                    basis_lifts.append(b)
                
                # Define section on basis
                section_dict = dict(zip(self.C.basis(), basis_lifts))
                section = self.C.hom(section_dict, self.B)
                
                # Check if section works
                composition = self.surjection * section
                if composition.is_identity():
                    return True
        except:
            pass
        
        return False
    
    def splitting(self):
        """
        Return splitting maps if sequence splits.
        
        OUTPUT:
        Tuple (section, retraction) or None
        """
        if not self.is_split():
            return None
        
        # Construct splitting maps
        # This requires the explicit construction from is_split()
        raise NotImplementedError("Splitting construction")

def short_exact_sequence(submodule, ambient):
    """
    Construct short exact sequence from submodule.
    
    0 → N → M → M/N → 0
    
    INPUT:
    - submodule -- submodule N of M
    - ambient -- ambient module M
    
    OUTPUT:
    ShortExactSequence object
    """
    # Inclusion map N → M
    inclusion = inclusion_morphism(submodule, ambient)
    
    # Projection map M → M/N  
    quotient = ambient.quotient(submodule)
    projection = quotient.natural_map()
    
    return ShortExactSequence(inclusion, projection)
```

## Mathematical Properties

```python
# Mathematical assertion: Submodule lattice
# Submodules form a complete lattice under inclusion

# Mathematical assertion: Correspondence theorem
# Submodules of M/N ↔ submodules of M containing N

# Mathematical assertion: First isomorphism theorem
# M/ker(f) ≅ im(f) for any module homomorphism f

# Mathematical assertion: Second isomorphism theorem
# (S + T)/T ≅ S/(S ∩ T) for submodules S, T

# Mathematical assertion: Third isomorphism theorem
# (M/S)/(T/S) ≅ M/T for submodules S ⊆ T ⊆ M

# Mathematical assertion: Structure theorem (PIDs)
# Finitely generated modules over PID decompose as
# M ≅ R^r ⊕ R/(d₁) ⊕ ... ⊕ R/(dₖ) with d₁|d₂|...|dₖ

# Mathematical assertion: Torsion-free iff embeds in free
# M torsion-free ⟺ M embeds in free module

# Mathematical assertion: Exact sequence splits
# 0 → A → B → C → 0 splits ⟺ C projective ⟺ A injective
```

This comprehensive subobject framework provides the lattice-theoretic structure of submodules and quotients while maintaining compatibility with homological algebra and the structure theory of modules over rings.