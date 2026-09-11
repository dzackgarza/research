# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/limits/cat_w_product.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Product Category Factory for Cat_w.

Given categories C, D, ... this module provides:
- ProductCategory: C × D × ... as a category
- ProductObject: (c, d, ...) where c ∈ Ob(C), d ∈ Ob(D), ...
- ProductMorphism: (f, g, ...) where f ∈ Mor(C), g ∈ Mor(D), ...
- Product versions of Hom, End, Aut built from factor constructions

Key insight: All product constructions delegate to factor constructions
via projection, then wrap results in product wrappers.
"""

from __future__ import annotations

from src.local_typing import *
from dataclasses import dataclass, field
from itertools import product as cartesian_product

from src._types import CategoryABCs


# =============================================================================
# Product Cell Types
# =============================================================================


@dataclass(frozen=True)
class ProductObject(CategoryABCs.Object):
    """
    An object in a product category C × D × ...
    
    Wraps a tuple of objects (c, d, ...) from the factor categories.
    """
    _components: tuple[CategoryABCs.Object, ...]
    _factors: tuple[CategoryABCs.Category, ...] = field(repr=False)
    
    def project(self, i: int) -> CategoryABCs.Object:
        """Project to the i-th component object."""
        return self._components[i]
    
    def __iter__(self) -> Iterator[CategoryABCs.Object]:
        return iter(self._components)
    
    def __len__(self) -> int:
        return len(self._components)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ProductObject):
            return NotImplemented
        return self._components == other._components
    
    def __hash__(self) -> int:
        return hash(self._components)


@dataclass(frozen=True)
class ProductMorphism(CategoryABCs.Morphism):
    """
    A morphism in a product category C × D × ...
    
    Wraps a tuple of morphisms (f, g, ...) from the factor categories.
    Morphism (f, g): (c1, d1) → (c2, d2) where f: c1→c2 and g: d1→d2.
    """
    _components: tuple[CategoryABCs.Morphism, ...]
    _factors: tuple[CategoryABCs.Category, ...] = field(repr=False)
    
    def project(self, i: int) -> CategoryABCs.Morphism:
        """Project to the i-th component morphism."""
        return self._components[i]
    
    def source(self) -> ProductObject:
        """Source is product of component sources."""
        return ProductObject(
            tuple(f.source() for f in self._components),
            self._factors
        )
    
    def target(self) -> ProductObject:
        """Target is product of component targets."""
        return ProductObject(
            tuple(f.target() for f in self._components),
            self._factors
        )
    
    def __iter__(self) -> Iterator[CategoryABCs.Morphism]:
        return iter(self._components)
    
    def __len__(self) -> int:
        return len(self._components)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ProductMorphism):
            return NotImplemented
        return self._components == other._components
    
    def __hash__(self) -> int:
        return hash(self._components)


# =============================================================================
# Product Hom-Set
# =============================================================================


@dataclass
class ProductHomC_xy(CategoryABCs.HomC_xy):
    """
    Hom_{C×D}((c1,d1), (c2,d2)) = Hom_C(c1,c2) × Hom_D(d1,d2).
    
    Objects are ProductMorphisms; built from factor hom-sets.
    """
    _source: ProductObject
    _target: ProductObject
    _factor_homs: tuple[CategoryABCs.HomC_xy, ...]
    _factors: tuple[CategoryABCs.Category, ...]
    
    def domain(self) -> ProductObject:
        return self._source
    
    def codomain(self) -> ProductObject:
        return self._target
    
    def objects(self) -> Iterator[ProductMorphism]:
        """Morphisms (c1,d1) → (c2,d2) = product of factor hom-sets."""
        for combo in cartesian_product(*(h.objects() for h in self._factor_homs)):
            yield ProductMorphism(combo, self._factors)
    
    def amb(self) -> ProductHomC:
        """Ambient ProductHomC."""
        # Would need reference to containing ProductHomC
        raise NotImplementedError


@dataclass
class ProductEndC_x(CategoryABCs.EndC_x):
    """
    End_{C×D}((c,d)) = End_C(c) × End_D(d).
    """
    _object: ProductObject
    _factor_ends: tuple[CategoryABCs.EndC_x, ...]
    _factors: tuple[CategoryABCs.Category, ...]
    
    def object(self) -> ProductObject:
        return self._object
    
    def objects(self) -> Iterator[ProductMorphism]:
        """Endomorphisms on (c,d) = product of factor endomorphism sets."""
        for combo in cartesian_product(*(e.objects() for e in self._factor_ends)):
            yield ProductMorphism(combo, self._factors)


@dataclass
class ProductAutC_x(CategoryABCs.AutC_x):
    """
    Aut_{C×D}((c,d)) = Aut_C(c) × Aut_D(d).
    """
    _object: ProductObject
    _factor_auts: tuple[CategoryABCs.AutC_x, ...]
    _factors: tuple[CategoryABCs.Category, ...]
    
    def object(self) -> ProductObject:
        return self._object
    
    def objects(self) -> Iterator[ProductMorphism]:
        """Automorphisms on (c,d) = product of factor automorphism sets."""
        for combo in cartesian_product(*(a.objects() for a in self._factor_auts)):
            yield ProductMorphism(combo, self._factors)


# =============================================================================
# Product HomC (category of hom-sets)
# =============================================================================


@dataclass
class ProductHomC(CategoryABCs.HomC):
    """
    HomC for product category C × D.
    
    Objects are ProductHomC_xy instances.
    """
    _factors: tuple[CategoryABCs.Category, ...]
    _factor_homCs: tuple[CategoryABCs.HomC, ...]
    
    def objects(self) -> Iterator[ProductHomC_xy]:
        """All Hom_{C×D}(x,y) for pairs of product objects."""
        # This would iterate over cartesian product of factor hom-sets
        # Implementation depends on how factor categories enumerate objects
        raise NotImplementedError("Iteration over all hom-sets requires object enumeration")
    
    def object_from_domain_and_codomain(
        self, 
        domain: ProductObject, 
        codomain: ProductObject
    ) -> ProductHomC_xy:
        """Construct Hom_{C×D}(x, y)."""
        factor_homs = tuple(
            self._factor_homCs[i].object_from_domain_and_codomain(
                domain.project(i), 
                codomain.project(i)
            )
            for i in range(len(self._factors))
        )
        return ProductHomC_xy(domain, codomain, factor_homs, self._factors)


# =============================================================================
# Product Category
# =============================================================================


@dataclass
class ProductCategory(CategoryABCs.Category):
    """
    Product category C × D × ...
    
    - Objects: tuples (c, d, ...) where c ∈ Ob(C), d ∈ Ob(D), ...
    - Morphisms: tuples (f, g, ...) where f ∈ Mor(C), g ∈ Mor(D), ...
    - Composition: componentwise
    - Identity: (id_c, id_d, ...)
    """
    _factors: tuple[CategoryABCs.Category, ...]
    
    # Declared types for signature verification
    Object: ClassVar[type] = ProductObject
    Morphism: ClassVar[type] = ProductMorphism
    
    def factors(self) -> tuple[CategoryABCs.Category, ...]:
        """The factor categories."""
        return self._factors
    
    def objects(self) -> Iterator[ProductObject]:
        """Objects = cartesian product of factor objects."""
        for combo in cartesian_product(*(f.objects() for f in self._factors)):
            yield ProductObject(combo, self._factors)
    
    def morphisms(self) -> Iterator[ProductMorphism]:
        """Morphisms = cartesian product of factor morphisms."""
        for combo in cartesian_product(*(f.morphisms() for f in self._factors)):
            yield ProductMorphism(combo, self._factors)
    
    def identity(self, obj: ProductObject) -> ProductMorphism:
        """Identity on (c, d, ...) = (id_c, id_d, ...)."""
        return ProductMorphism(
            tuple(
                self._factors[i].identity(obj.project(i))
                for i in range(len(self._factors))
            ),
            self._factors
        )
    
    def compose(
        self, 
        f: ProductMorphism, 
        g: ProductMorphism
    ) -> ProductMorphism:
        """Compose componentwise: (f1, f2, ...) ∘ (g1, g2, ...) = (f1∘g1, f2∘g2, ...)."""
        return ProductMorphism(
            tuple(
                self._factors[i].compose(f.project(i), g.project(i))
                for i in range(len(self._factors))
            ),
            self._factors
        )
    
    def hom_C(self, x: ProductObject, y: ProductObject) -> ProductHomC_xy:
        """Hom_{C×D}(x, y) = Hom_C(x1, y1) × Hom_D(x2, y2) × ..."""
        factor_homs = tuple(
            self._factors[i].hom_C(x.project(i), y.project(i))
            for i in range(len(self._factors))
        )
        return ProductHomC_xy(x, y, factor_homs, self._factors)
    
    def end_C(self, x: ProductObject) -> ProductEndC_x:
        """End_{C×D}(x) = End_C(x1) × End_D(x2) × ..."""
        factor_ends = tuple(
            self._factors[i].end_C(x.project(i))
            for i in range(len(self._factors))
        )
        return ProductEndC_x(x, factor_ends, self._factors)
    
    def aut_C(self, x: ProductObject) -> ProductAutC_x:
        """Aut_{C×D}(x) = Aut_C(x1) × Aut_D(x2) × ..."""
        factor_auts = tuple(
            self._factors[i].aut_C(x.project(i))
            for i in range(len(self._factors))
        )
        return ProductAutC_x(x, factor_auts, self._factors)


# =============================================================================
# Factory Function
# =============================================================================


def product_category(*factors: CategoryABCs.Category) -> ProductCategory:
    """
    Construct the product category C × D × ... from factor categories.
    
    Usage:
        C_times_D = product_category(C, D)
        obj = ProductObject((c, d), (C, D))
        mor = ProductMorphism((f, g), (C, D))
    """
    return ProductCategory(factors)


# =============================================================================
# Semantic Exports
# =============================================================================

# Factory
make_product = product_category

# Types
ProductCategoryType = ProductCategory
ProductObjectType = ProductObject
ProductMorphismType = ProductMorphism
ProductHomType = ProductHomC_xy
ProductEndType = ProductEndC_x
ProductAutType = ProductAutC_x
