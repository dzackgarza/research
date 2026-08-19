<!--
Origin: gitclones/Coxeter/tmp_restore/docs/api-planning/categories/bilinear_Rmod/symmetric_Rmod/nondegenerate_lattices/definite_lattices/negative_definite_lattices/negative_definite_lattices.md
Copied 2026-08-20 by the Coxeter-corpora enrichment migration
(PLAN-coxeter-deletion-audit-registry). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences are listed in the INDEX.md of this corpus.
-->

# Interface: NegativeDefiniteLattices

Negative definite lattices inherit all methods from `DefiniteLattices` and add:

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