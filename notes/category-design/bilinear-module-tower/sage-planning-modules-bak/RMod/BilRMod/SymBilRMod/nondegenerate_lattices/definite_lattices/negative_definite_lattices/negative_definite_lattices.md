<!--
Origin: gitclones/Coxeter-v2/archive/cold_storage_pre_integration/background-research/sage-planning/modules_bak/RMod/BilRMod/SymBilRMod/nondegenerate_lattices/definite_lattices/negative_definite_lattices/negative_definite_lattices.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Interface: NegativeDefiniteLattices

Negative definite lattices inherit all methods from `DefiniteLattices` and add:

## Mathematical Test Assertions

```python
# Mathematical assertion: Negative definite lattices have all negative eigenvalues
# sage: R = RootSystem(['E', 8])
# sage: G = -R.cartan_matrix()  # Our convention: Gram = -Cartan for simply-laced
# sage: all(e < 0 for e in G.eigenvalues())
# True  # E₈ is negative definite (elliptic type) - Bourbaki Ch VI §4

# Mathematical assertion: Elliptic = finite Coxeter groups (Humphreys, Ch 2)
# sage: R = RootSystem(['F', 4])
# sage: W = R.root_system().weyl_group()
# sage: W.order() < infinity and all(e < 0 for e in (-R.cartan_matrix()).eigenvalues())
# True  # F₄ has order 1152, negative definite Gram matrix

# Mathematical assertion: Compact fundamental domains for elliptic types
# sage: # All finite Coxeter groups have compact fundamental domains
# sage: # This is equivalent to negative definiteness under our convention
# sage: for ct in [['A', 5], ['D', 6], ['E', 7]]:
# ...     R = RootSystem(ct)
# ...     G = -R.cartan_matrix()
# ...     if not all(e < 0 for e in G.eigenvalues()):
# ...         print(f"Failed for {ct}")
# # (No output - all finite types are negative definite)

# Mathematical assertion: Root systems of finite type have finitely many roots
# sage: R = RootSystem(['E', 6])
# sage: roots = R.root_lattice().roots()
# sage: len(roots) == 72  # E₆ has exactly 72 roots
# True  # Conway & Sloane, Sphere Packings Ch. 4

# Mathematical assertion: Connection to Lie algebras - dimension formula
# sage: R = RootSystem(['G', 2])
# sage: dim = R.cartan_type().rank() + len(R.root_lattice().roots())
# sage: dim == 14  # dim(G₂) = rank + |roots| = 2 + 12 = 14
# True  # Humphreys, Introduction to Lie Algebras Ch. 3

# Mathematical assertion: Negative definite ⟺ positive definite of opposite form
# sage: R = RootSystem(['B', 4])
# sage: G_neg = -R.cartan_matrix()  # Our negative definite convention
# sage: G_pos = -G_neg  # Standard positive definite convention
# sage: all(e < 0 for e in G_neg.eigenvalues()) and all(e > 0 for e in G_pos.eigenvalues())
# True  # Sign conventions are dual (Vinberg, Hyperbolic Reflection Groups)

# Mathematical assertion: Exceptional E₈ is even unimodular of rank 8
# sage: R = RootSystem(['E', 8])
# sage: G = -R.cartan_matrix()
# sage: abs(G.determinant()) == 1  # Unimodular
# True  # E₈ is the unique even unimodular lattice in dimension 8 (Conway & Sloane Ch. 4)

# Mathematical assertion: No null vectors in negative definite lattices
# sage: # For v ≠ 0 in a negative definite lattice, ⟨v,v⟩ < 0
# sage: R = RootSystem(['A', 7])
# sage: G = -R.cartan_matrix()
# sage: 0 not in G.eigenvalues()  # No zero eigenvalue means no null vectors
# True  # Definite lattices have trivial radical (Serre, Course in Arithmetic)
```

## Elliptic Properties

```python
def is_elliptic(self):
    r"""
    Always returns True for negative definite lattices.
    
    NOTE: Coxeter-specific properties like Coxeter numbers are only 
    available for objects in CoxeterLattices() & NegativeDefiniteLattices().
    """
    return True
```

## Algebraic Geometry Applications

```python
def intersection_form(self):
    r"""
    Interpret this as an intersection form on an algebraic surface.
    
    Negative definite lattices arise as intersection forms on
    exceptional divisors of resolutions of singularities.
    """

def canonical_class_square(self):
    r"""
    Return K² where K is the canonical class.
    
    For lattices arising from algebraic surfaces, this is an
    important invariant.
    """

def blowup_graph(self):
    r"""
    Return the dual graph if this arises from a configuration of curves.
    
    For ADE singularities, this recovers the Dynkin diagram.
    """
```

## Note on Coxeter Structure

When a negative definite lattice also admits a Coxeter system embedding, 
the combined object in CoxeterLattices() & NegativeDefiniteLattices() 
provides additional methods including:

- dynkin_type(), coxeter_number(), exponents()
- highest_root(), root_poset(), weyl_group()  
- mckay_quiver(), preprojective_algebra() (for ADE types)

These are available through SageMath's automatic category joining mechanism.