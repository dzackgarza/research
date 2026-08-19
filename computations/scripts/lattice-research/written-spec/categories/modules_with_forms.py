r"""
Modules With Forms

Top-level category scaffold for finitely generated modules over a
commutative PID `R` equipped with a primary bilinear or quadratic form.

The first-pass front door is intentionally narrow: generic objects in this
category are `R`-valued or `K = Frac(R)`-valued. Quotient-valued codomains
such as `K/R` and `K/2R` are introduced by explicit categorical descent on
real kernel/image/cokernel objects.
"""
# ****************************************************************************
#  Copyright (C) 2026  The research project authors
#
#  Distributed under the terms of the GNU General Public License (GPL)
# ****************************************************************************

from sage.categories.cartesian_product import CartesianProductsCategory
from sage.categories.category_types import Category_module
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.dual import DualObjectsCategory
from sage.categories.homsets import HomsetsCategory
from sage.categories.modules import Modules
from sage.categories.tensor import TensorProductsCategory
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method


class ModulesWithForms(Category_module):
    r"""
    Category of finitely generated `R`-modules equipped with a form.

    Objects may be mixed modules `M = F \oplus T`. The category therefore
    owns the generic parent, element, morphism, and homset scaffolding
    needed before promotion into free, torsion, lattice, or discriminant
    meets.
    """

    def super_categories(self):
        r"""Return the immediate super categories."""
        return [Modules(self.base_ring()).FinitelyPresented()]

    def additional_structure(self):
        r"""
        Return ``self``.

        A module morphism between two objects with forms is not
        automatically form-preserving, so the form data is genuine
        additional structure.
        """
        return self

    class SubcategoryMethods:
        r"""Methods available on subcategories of ``ModulesWithForms(R)``."""

        @cached_method
        def base_ring(self):
            r"""Return the base ring for ``self``."""
            for category in self.super_categories():
                if hasattr(category, "base_ring"):
                    return category.base_ring()
            raise AttributeError(f"no super category of {self} has a base_ring")

        @cached_method
        def Bilinear(self):
            r"""Return the bilinear refinement."""
            return self._with_axiom("Bilinear")

        @cached_method
        def Quadratic(self):
            r"""Return the quadratic refinement."""
            return self._with_axiom("Quadratic")

        @cached_method
        def Free(self):
            r"""Return the free refinement."""
            return self._with_axiom("Free")

        @cached_method
        def Torsion(self):
            r"""Return the torsion refinement."""
            return self._with_axiom("Torsion")

        @cached_method
        def NonDegenerate(self):
            r"""Return the nondegenerate refinement."""
            return self._with_axiom("NonDegenerate")

        @cached_method
        def Integral(self):
            r"""Return the `R`-valued refinement."""
            return self._with_axiom("Integral")

        @cached_method
        def Rational(self):
            r"""Return the `K = Frac(R)`-valued refinement."""
            return self._with_axiom("Rational")

        @cached_method
        def TensorProducts(self):
            r"""Return the tensor-product construction category."""
            return TensorProductsCategory.category_of(self)

        @cached_method
        def CartesianProducts(self):
            r"""Return the Cartesian-product construction category."""
            return CartesianProductsCategory.category_of(self)

        @cached_method
        def DualObjects(self):
            r"""Return the dual-object construction category."""
            return DualObjectsCategory.category_of(self)

        dual = DualObjects

    class ParentMethods:
        r"""Generic parent-level interface for modules with forms."""

        @abstract_method
        def form(self):
            r"""Return the primary form carried by ``self``."""

        @abstract_method
        def gens(self):
            r"""Return the canonical generators of ``self``."""

        @abstract_method
        def zero(self):
            r"""Return the additive identity."""

        @abstract_method
        def base_ring(self):
            r"""Return the base PID `R`."""

        @abstract_method
        def free_part(self):
            r"""Return the free summand as an actual category object."""

        @abstract_method
        def torsion_part(self):
            r"""Return the torsion summand as an actual category object."""

        @abstract_method
        def Hom(self, other):
            r"""Return the hom space in ``ModulesWithForms(R)``."""

        @abstract_method
        def dual(self):
            r"""Return the categorical dual object."""

        @abstract_method
        def span(self, elements):
            r"""Return the subobject generated by ``elements``."""

        @abstract_method
        def cardinality(self):
            r"""Return the cardinality of the underlying set."""

        def End(self):
            r"""Return the endomorphism space of ``self``."""
            return self.Hom(self)

    class ElementMethods:
        r"""Generic element-level interface for modules with forms."""

        @abstract_method
        def to_vector(self):
            r"""Return coordinates with respect to ``parent().gens()``."""

        def span(self):
            r"""Return the span of ``self``."""
            return self.parent().span([self])

    class MorphismMethods:
        r"""Generic morphism-level interface for modules with forms."""

        @abstract_method
        def domain(self):
            r"""Return the domain of the morphism."""

        @abstract_method
        def codomain(self):
            r"""Return the codomain of the morphism."""

        @abstract_method
        def __call__(self, value):
            r"""Evaluate the morphism on ``value``."""

        @abstract_method
        def to_matrix(self):
            r"""Return the matrix of the morphism in canonical generators."""

        @abstract_method
        def kernel(self):
            r"""Return the actual kernel object with descended form data."""

        @abstract_method
        def image(self):
            r"""Return the actual image object with descended form data."""

        @abstract_method
        def cokernel(self):
            r"""Return the actual cokernel object with descended form data."""

        @abstract_method
        def is_form_preserving(self):
            r"""Return whether the morphism preserves the primary form."""

        def is_bijective(self):
            r"""Return whether the morphism is both injective and surjective."""
            return self.is_injective() and self.is_surjective()

    class Homsets(HomsetsCategory):
        r"""Hom-set category for modules with forms."""

        def extra_super_categories(self):
            r"""A hom set of modules with forms is an `R`-module."""
            return [Modules(self.base_category().base_ring())]

        def base_ring(self):
            r"""Return the base ring of the hom-set category."""
            return self.base_category().base_ring()

        class ParentMethods:
            r"""Generic parent-level interface for hom sets."""

            @cached_method
            def base_ring(self):
                r"""Return the base ring from the domain."""
                return self.domain().base_ring()

            @abstract_method
            def element_from_dict(self, mapping):
                r"""Construct a morphism from a generator-image dict."""

            @abstract_method
            def element_from_matrix(self, matrix_data):
                r"""Construct a morphism from matrix data."""

            @abstract_method
            def element_from_images(self, images):
                r"""Construct a morphism from images of generators."""

            @abstract_method
            def __contains__(self, value):
                r"""Return whether ``value`` is a morphism in this hom set."""

    class Bilinear(CategoryWithAxiom_over_base_ring):
        r"""Axiom for objects whose primary form is bilinear."""

        class ParentMethods:
            r"""Additional parent-level interface for bilinear objects."""

            @abstract_method
            def bilinear_form(self):
                r"""Return the bilinear form on ``self``."""

            def form(self):
                r"""Return the primary form on ``self``."""
                return self.bilinear_form()

            def b(self, left, right):
                r"""Evaluate the bilinear form."""
                return self.bilinear_form().evaluate(left, right)

            def gram_matrix(self):
                r"""Return the Gram matrix of the bilinear form."""
                return self.bilinear_form().gram_matrix()

            @abstract_method
            def radical(self):
                r"""Return the radical of ``self``."""

        class ElementMethods:
            r"""Additional element-level interface for bilinear objects."""

            def b(self, other):
                r"""Evaluate the bilinear product with ``other``."""
                return self.parent().b(self, other)

            def q(self):
                r"""Return the diagonal bilinear value `b(self, self)`."""
                return self.parent().b(self, self)

            def is_isotropic(self):
                r"""Return whether ``self`` is isotropic."""
                return self.q() == 0

        class MorphismMethods:
            r"""Additional morphism-level interface for bilinear objects."""

            def is_isometry(self):
                r"""Return whether the morphism preserves the bilinear form."""
                return self.is_form_preserving()

    class Quadratic(CategoryWithAxiom_over_base_ring):
        r"""Axiom for objects whose primary form is quadratic."""

        class ParentMethods:
            r"""Additional parent-level interface for quadratic objects."""

            @abstract_method
            def quadratic_form(self):
                r"""Return the quadratic form on ``self``."""

            def form(self):
                r"""Return the primary form on ``self``."""
                return self.quadratic_form()

            @abstract_method
            def associated_bilinear_object(self):
                r"""Return the same carrier with its polar bilinear form."""

            def polar_bilinear_form(self):
                r"""Return the polar bilinear form."""
                return self.quadratic_form().polar_bilinear_form()

        class ElementMethods:
            r"""Additional element-level interface for quadratic objects."""

            def q(self):
                r"""Evaluate the quadratic form on ``self``."""
                return self.parent().quadratic_form().evaluate(self)

    class Free(CategoryWithAxiom_over_base_ring):
        r"""Axiom for finite free carriers."""

    class Torsion(CategoryWithAxiom_over_base_ring):
        r"""Axiom for finite torsion carriers."""

    class NonDegenerate(CategoryWithAxiom_over_base_ring):
        r"""Axiom for nondegenerate forms."""

    class Integral(CategoryWithAxiom_over_base_ring):
        r"""Axiom for `R`-valued forms."""

    class Rational(CategoryWithAxiom_over_base_ring):
        r"""Axiom for `K = Frac(R)`-valued forms."""

    class CartesianProducts(CartesianProductsCategory):
        r"""Category of Cartesian products of modules with forms."""

        def extra_super_categories(self):
            r"""A Cartesian product of modules with forms is again such an object."""
            return [self.base_category()]

    class TensorProducts(TensorProductsCategory):
        r"""Category of tensor products of modules with forms."""

        def extra_super_categories(self):
            r"""A tensor product of modules with forms stays in the base category."""
            return [self.base_category()]

        class ParentMethods:
            r"""Parent-level interface for tensor-product objects."""

            @abstract_method
            def tensor_factors(self):
                r"""Return the tensor factors."""
