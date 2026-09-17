"""Algebras over an owned base ring, with identities represented as refinements."""

from sage.categories.category_with_axiom import all_axioms
from sage.categories.commutative_algebras import (
    CommutativeAlgebras as SageCommutativeAlgebras,
)
from sage.categories.map import Map
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.rings import Rings as SageRings
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.unknown import Unknown

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
    _category_homset,
)
from dzack_research.preamble.categories.abstract_categories.products import (
    _finite_factor_family,
    _two_factors_of,
)
from dzack_research.preamble.categories.algebras.associative_algebra_morphisms import (
    AssociativeAlgebraHomset,
)
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    BilinearMap,
    FramedModules,
    MatrixEndomorphismSpaces,
    Modules,
    TensorProductModules,
)

from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedFields,
    OwnedRings,
    PrincipalIdealDomains,
    _engine_element,
    _engine_ring,
    _own_ring,
    _owned_ring,
    _OwnedRingElement,
    _OwnedRingParent,
)
from dzack_research.preamble.categories.sets.cardinals import aleph0
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import EnumeratedSets, Sets
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom
from dzack_research.preamble.refine import refine

if "Lie" not in all_axioms:
    all_axioms.add("Lie")

# Qualified as Sage qualifies ``FinitelyGeneratedAsMagma``: an axiom name is
# global and propagates to every declared supercategory defining it, and a
# finitely presented algebra is not a finitely presented module.
if "FinitelyPresentedAsAlgebra" not in all_axioms:
    all_axioms.add("FinitelyPresentedAsAlgebra")


class AlgebraHomCategoryConstruction(HomCategoryConstruction):
    r"""The fixed-endpoint Hom categories of associative unital ``R``-algebras.

    The domain settles which Hom parent an algebra takes -- a presented
    algebra and a free one carry their maps differently -- so the class is
    named here and the Hom family builds it.  Naming the class rather than
    building the object is what lets a subcategory that states no morphisms of
    its own reuse the parent above it instead of interning a second one.
    """

    def fixed_category_class_for(self, domain, codomain):
        return domain._algebra_homset_class()


class MultiplicativeAlgebraMorphism(Morphism):
    r"""An ``R``-linear map \(f\colon A\to B\) with \(f\,m_A = m_B\,(f\otimes f)\).

    The datum is the linear map.  Multiplicativity is one equation between
    two module morphisms out of \(A\otimes_R A\), asked of the module Hom,
    which decides it on a chosen finite presentation of \(A\otimes_R A\) and
    answers ``Unknown`` otherwise.  A ``False`` answer refuses the map; an
    ``Unknown`` one is recorded as the hypothesis the arrow is stated under,
    never replaced by a finite-framing assertion (``CON-16``, ``DEV-52``).
    """

    def __init__(self, parent, underlying_morphism) -> None:
        Morphism.__init__(self, parent)
        domain = self.domain()
        codomain = self.codomain()
        module_hom = domain.module_category().Mor(domain, codomain)
        underlying_morphism = module_hom(underlying_morphism)
        source_multiplication = domain.multiplication_morphism()
        target_multiplication = codomain.multiplication_morphism()
        tensor_square = underlying_morphism.tensor_product_map(
            underlying_morphism,
            source=source_multiplication.domain(),
            target=target_multiplication.domain(),
        )
        preserved = underlying_morphism * source_multiplication == target_multiplication * tensor_square
        match preserved:
            case True:
                pass
            case False:
                raise ValueError("the stated map does not preserve multiplication")
            case _:
                preserved = Unknown
        self._underlying_morphism = underlying_morphism
        self._tensor_square_morphism = tensor_square
        self._preserves_multiplication = preserved

    def underlying_morphism(self):
        r"""The linear map this algebra morphism is, in the module Hom."""
        return self._underlying_morphism

    def tensor_square_morphism(self):
        r"""\(f\otimes f\colon A\otimes_R A\to B\otimes_R B\)."""
        return self._tensor_square_morphism

    def is_multiplicative(self):
        r"""``True`` when \(f\,m_A = m_B\,(f\otimes f)\) was decided, else ``Unknown``.

        The equation is asked once, at construction, of the module Hom out of
        \(A\otimes_R A\); a map that answered ``False`` was never constructed.
        """
        return self._preserves_multiplication

    def corestrict_to_center(self):
        r"""Factor this algebra morphism through the represented centre of its codomain."""
        return _corestrict_algebra_morphism_to_center(self)

    @cached_method
    def cokernel(self):
        r"""Return the algebra cokernel as quotient by the generated algebra ideal.

        The underlying module image need not itself be an ideal.  This is the
        essential distinction from the module cokernel; for Lie algebras it is
        the quotient by the Lie ideal generated by the image.
        """
        image = self.underlying_morphism().image()
        return self.codomain().quotient_by_generated_algebra_ideal(image)

    @cached_method
    def cokernel_projection(self):
        r"""Return the multiplication-preserving quotient map to ``coker(self)``."""
        quotient = self.cokernel()
        category = self.parent().hom_family().base_category()
        return category.Mor(self.codomain(), quotient)(quotient.algebra_quotient_projection())

    def _call_(self, element):
        return self.codomain()(self.underlying_morphism()(self.domain()(element)))

    def __eq__(self, other) -> bool:
        if not isinstance(other, MultiplicativeAlgebraMorphism):
            return False
        return self.parent() is other.parent() and self.underlying_morphism() == other.underlying_morphism()

    def __ne__(self, other) -> bool:
        return not self == other

    __hash__ = None

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        category = self.parent().hom_family().base_category()
        return category.Mor(
            other.domain(),
            self.codomain(),
        )(self.underlying_morphism() * other.underlying_morphism())


class MultiplicativeAlgebraHomset(CategoricalHomset):
    r"""``Hom_{R-Alg}(A, B)``: the linear maps preserving the multiplication."""

    Element = MultiplicativeAlgebraMorphism

    def __call__(self, underlying_morphism):
        return self._element_constructor_(underlying_morphism)

    def _element_constructor_(self, underlying_morphism):
        # The one boundary admitting foreign data: an arrow of another algebra
        # Hom with these endpoints is admitted by the linear map it is.
        if isinstance(underlying_morphism, MultiplicativeAlgebraMorphism):
            if underlying_morphism.parent() is self:
                return underlying_morphism
            underlying_morphism = underlying_morphism.underlying_morphism()
        return self.element_class(self, underlying_morphism)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom-set")
        algebra = self.domain()
        return self(algebra.module_category().Mor(algebra, algebra).identity())

    def _repr_(self):
        return f"Mor_Alg({self.domain()}, {self.codomain()})"


class UnitalMultiplicativeAlgebraMorphism(MultiplicativeAlgebraMorphism):
    r"""A multiplicative linear map that also preserves the selected unit."""

    def __init__(self, parent, underlying_morphism) -> None:
        super().__init__(parent, underlying_morphism)
        if self(self.domain().one()) != self.codomain().one():
            raise ValueError("the stated map does not preserve the unit")


class UnitalMultiplicativeAlgebraHomset(MultiplicativeAlgebraHomset):
    r"""The fixed Hom of represented associative unital algebras."""

    Element = UnitalMultiplicativeAlgebraMorphism

    def _repr_(self):
        return f"Mor_UnitalAlg({self.domain()}, {self.codomain()})"


class GeneralAlgebraHomCategoryConstruction(HomCategoryConstruction):
    r"""The Hom of the algebra node: linear maps preserving the multiplication."""

    FixedCategoryClass = MultiplicativeAlgebraHomset


class UnitalGeneralAlgebraHomCategoryConstruction(HomCategoryConstruction):
    r"""The unit-preserving common Hom of possibly nonassociative unital algebras."""

    FixedCategoryClass = UnitalMultiplicativeAlgebraHomset


def _scalar_module(ring):
    r"""\(U_R(R)\): the ring as the module over itself, the domain of every unit map."""
    ring = _owned_ring(ring)
    return Algebras(ring).underlying_module()(ring)


def _unit_morphism_from_element(module, unit, ring):
    r"""Return the linear map ``U_R(R) -> module`` determined by ``1 |-> unit``."""
    ring = _owned_ring(ring)
    scalar_module = _scalar_module(ring)
    return ModuleMorphism(
        scalar_module.module_category().Mor(scalar_module, module),
        lambda scalar: module.scalar_multiple(ring(scalar), unit),
        elementwise=True,
    )


def _unit_morphism_of(unit_morphism, module, ring):
    r"""Admit ``eta: U_R(R) -> module`` as the unit datum of an algebra on ``module``."""
    scalar_module = _scalar_module(ring)
    assert unit_morphism.domain() is scalar_module, "the unit morphism starts at U_R(R)"
    assert unit_morphism.codomain() is module, (
        "the unit morphism lands in the module the multiplication is stated on"
    )
    return unit_morphism


def _unit_equations_hold(algebra):
    r"""Decide \(1\cdot x = x = x\cdot 1\) on a finite module framing, else ``Unknown``.

    Both sides are linear in \(x\), so agreement on a module generating set
    is agreement everywhere; an infinite framing leaves the equations
    ``Unknown`` rather than enumerated.
    """
    match algebra.is_framed_module():
        case True:
            labels = algebra.module_generating_set()
        case _:
            return Unknown
    if not labels.cardinality().is_finite():
        return Unknown
    unit = algebra.one()
    multiplication = algebra.multiplication_morphism()
    tensor = multiplication.domain()
    for label in labels:
        element = algebra.module_generator(label)
        left = multiplication(tensor.pure_tensor(unit, element))
        right = multiplication(tensor.pure_tensor(element, unit))
        if left != element or right != element:
            return False
    return True


class _CommutativeUnitalAlgebraSubcategoryMethods:
    r"""Constructions that require commutative associative unital algebras."""

    def spectrum(self):
        r"""``Spec_R : CAlg_R^op -> AffSch_R``, the affine spectrum functor."""
        from dzack_research.preamble.categories.schemes.affine_spec import (
            _affine_spec_functor,
        )

        return _affine_spec_functor(self.base_ring())

    def de_rham(self):
        r"""``DR_R : CAlg_R -> SCDGA_R``, the algebraic de Rham functor."""
        from dzack_research.preamble.categories.functors.de_rham import (
            _de_rham_functor,
        )

        return _de_rham_functor(self.base_ring())

    def de_rham_adjunction(self):
        r"""Return the algebraic de Rham/degree-zero adjunction over this base."""
        from dzack_research.preamble.categories.functors.de_rham import (
            _de_rham_adjunction,
        )

        return _de_rham_adjunction(self.base_ring())

    def de_rham_cohomology(self, degree):
        r"""Return ``H^degree_dR(-/R)`` on this commutative algebra category."""
        from dzack_research.preamble.categories.functors.cohomology import (
            _de_rham_cohomology_functor,
        )

        return _de_rham_cohomology_functor(self.base_ring(), degree)

    def de_rham_cohomology_algebra(self):
        r"""Return the graded algebraic de Rham cohomology functor ``H^*_dR``."""
        from dzack_research.preamble.categories.functors.cohomology import (
            _de_rham_cohomology_algebra_functor,
        )

        return _de_rham_cohomology_algebra_functor(self.base_ring())

    def coproduct(self, factors):
        r"""Return the represented two-factor tensor-product coproduct."""
        left, right = _two_factors_of(factors, name="Coproduct factors")
        return self._categorical_coproduct(left, right)

    def _categorical_coproduct(self, left, right):
        operation = getattr(left, "_commutative_algebra_coproduct", None)
        if operation is None:
            operation = getattr(right, "_commutative_algebra_coproduct", None)
        assert operation is not None, (
            "commutative-algebra coproduct requires a represented coproduct backend on one selected factor"
        )
        return operation(left, right)

    def _categorical_coproduct_morphism(
        self,
        left_morphism,
        right_morphism,
        source,
        target,
    ):
        return source.from_cocone(
            target.left_coproduct_map() * left_morphism,
            target.right_coproduct_map() * right_morphism,
        )

    def pushout(self, left_leg, right_leg):
        r"""Return the pushout of a represented commutative-algebra span."""
        assert left_leg.domain() is right_leg.domain(), "a span has one common domain"
        return self._categorical_pushout(left_leg, right_leg)

    def _categorical_pushout(self, left_morphism, right_morphism):
        left = left_morphism.codomain()
        right = right_morphism.codomain()
        operation = getattr(left, "_commutative_algebra_pushout", None)
        if operation is None:
            operation = getattr(right, "_commutative_algebra_pushout", None)
        assert operation is not None, (
            "commutative-algebra pushout requires a represented pushout backend on one selected factor"
        )
        return operation(left_morphism, right_morphism)


class _CommutativeUnitalAlgebraParentMethods:
    def is_commutative(self) -> bool:
        return True

    def kahler_differentials(self):
        r"""Return ``Omega^1_{A/R}`` for this commutative ``R``-algebra."""
        from dzack_research.preamble.categories.algebras.kahler_differentials import (
            KahlerDifferentialModules,
        )

        return KahlerDifferentialModules(self)(self)

    def de_rham_algebra(self):
        r"""Return the algebraic de Rham algebra ``Omega^*_{A/R}``."""
        from dzack_research.preamble.categories.algebras.de_rham_algebras import (
            DeRhamAlgebras,
        )

        return DeRhamAlgebras(self.base_ring())(self)

    def _quotient_by_algebra_elements(self, elements):
        r"""Return ``A/(f_1,...,f_r)`` through the selected ring presentation."""
        from dzack_research.preamble.categories.algebras.free_algebras import (
            _quotient_by_algebra_elements_backend,
        )

        return _quotient_by_algebra_elements_backend(self, elements)

    def quotient_by_relations(
        self,
        relations,
        *,
        _extra_categories=(),
        _extra_construction_data=None,
        _free_source_module=None,
    ):
        r"""Return the selected finite-presentation quotient by ``relations``."""
        category = AlgebrasWithChosenFinitePresentation(self.base_ring())
        return category._call_(
            self,
            relations,
            extra_categories=_extra_categories,
            extra_construction_data=_extra_construction_data,
            free_source_module=_free_source_module,
        )


class _AlgebraTensorSquareFunctor(Functor):
    r"""The diagonal tensor-square endofunctor on modules over a commutative ring."""

    def __init__(self, base_ring) -> None:
        self._base_ring = _owned_ring(base_ring)
        modules = Modules(self._base_ring)
        super().__init__(modules, modules)

    def base_ring(self):
        return self._base_ring

    def _apply_object(self, module):
        return Modules(self.base_ring()).tensor_product((module, module))

    def _apply_morphism(self, morphism):
        return morphism.tensor_product_map(
            morphism,
            source=self(morphism.domain()),
            target=self(morphism.codomain()),
        )

    def _repr_(self) -> str:
        return f"Tensor-square endofunctor on {self.domain()}"


@cached_function(key=lambda base_ring: id(_owned_ring(base_ring)))
def _algebra_tensor_square_functor(base_ring):
    ring = _owned_ring(base_ring)
    assert ring in OwnedRings().Commutative(), (
        "the represented algebra tensor-square functor requires a commutative base ring; "
        "noncommutative bases require a selected bimodule tensor product"
    )
    return _AlgebraTensorSquareFunctor(ring)


class Algebras(OwnedCategoryOverBaseRing):
    r"""``R``-modules equipped with one bilinear multiplication.

    This is the algebra node.  Its datum is a morphism
    \(m:A\otimes_R A\to A\); associativity, a chosen two-sided unit,
    commutativity, and the Lie identities are refinements above this node.
    """

    def an_object(self):
        r"""The base ring itself, an algebra over itself."""
        return self.base_ring()

    @classmethod
    def _repr_object_names(cls):
        return "algebras"

    def super_categories(self):
        return [Modules(self.base_ring())]

    def underlying_module(self):
        r"""Return the forgetful functor ``Alg_R -> Mod_R`` from this category."""
        from dzack_research.preamble.categories.functors.algebra_modules import (
            _algebra_underlying_module_functor,
        )

        return _algebra_underlying_module_functor(self.base_ring(), self)

    class SubcategoryMethods:
        def underlying_module(self):
            r"""Return the forgetful functor from this refined algebra category."""
            from dzack_research.preamble.categories.functors.algebra_modules import (
                _algebra_underlying_module_functor,
            )

            return _algebra_underlying_module_functor(self.base_ring(), self)

        def base_change_adjunction(self, ring_map):
            r"""Return ``S tensor_R - -| Res_f`` on associative unital algebras."""
            ordinary = Algebras(self.base_ring()).Associative().Unital()
            if not self.is_subcategory(ordinary):
                raise TypeError(
                    "algebra scalar change is represented on associative unital algebras"
                )
            if _owned_ring(ring_map.domain()) is not self.base_ring():
                raise ValueError("the scalar map has the wrong source ring")
            from dzack_research.preamble.categories.functors.algebra_scalar_change import (
                _algebra_base_change_adjunction,
            )

            return _algebra_base_change_adjunction(ring_map)

        def scalar_extension(self, ring_map):
            r"""Return scalar extension along ``ring_map`` from this algebra category."""
            return self.base_change_adjunction(ring_map).left_adjoint()

        def restriction_of_scalars(self, ring_map):
            r"""Return scalar restriction along ``ring_map`` into this algebra category."""
            if _owned_ring(ring_map.codomain()) is not self.base_ring():
                raise ValueError("the scalar map has the wrong target ring")
            source = Algebras(ring_map.domain()).Associative().Unital()
            return source.base_change_adjunction(ring_map).right_adjoint()

        def Associative(self):
            r"""Return the refinement satisfying ``(xy)z=x(yz)``."""
            return self._with_axiom("Associative")

        def Unital(self):
            r"""Return the refinement equipped with a two-sided unit."""
            return self._with_axiom("Unital")

        def Commutative(self):
            r"""Return the refinement satisfying ``xy=yx``."""
            return self._with_axiom("Commutative")

        def Lie(self):
            r"""Return the refinement whose selected multiplication is a Lie bracket."""
            return self._with_axiom("Lie")

    def Mor(self, domain, codomain):
        r"""Return the unique Hom-set ``Hom_{R-Alg}(domain,codomain)``."""
        if domain not in self or codomain not in self:
            raise TypeError("an R-algebra Hom requires two R-algebras")
        return self.HomCategory().Of(domain, codomain)

    _HomCategory = GeneralAlgebraHomCategoryConstruction

    class ElementMethods:
        def _mul_(self, other):
            r"""``x * y`` is the stated multiplication evaluated on \(x\otimes y\).

            A realization that states its product itself -- an engine ring, a
            graded module with its own ``multiply`` -- has no stated
            multiplication morphism at this node yet and keeps its own
            product; the constructor threads the datum through the root, so
            that arm closes as the engine realizations are routed through it.
            """
            match self.parent()._preamble_multiplication_morphism:
                case None:
                    return super()._mul_(other)
                case multiplication:
                    return multiplication(multiplication.domain().pure_tensor(self, other))

    class ParentMethods:
        # The defining datum of the node, established by the one constructor
        # ``Algebras(R)(M, m)``: the module \(M\) the multiplication was
        # stated on, and that multiplication read on this algebra.  ``None``
        # is the state of a realization that has not been routed through the
        # constructor (an engine ring placed here by adoption, a graded module
        # with a hand-written product); every accessor below derives from the
        # realization's own product what such an object did not state.
        _preamble_unformed_module = None
        _preamble_multiplication_morphism = None

        def __init__(self, unformed_module=None, multiplication=None, **rest) -> None:
            r"""Establish \((M, m)\) on this algebra.

            The module data are threaded by the levels below; this level
            stores the module the multiplication was stated on and, once the
            object exists, reads \(m\colon M\otimes_R M\to M\) on itself.
            """
            assert (unformed_module is None) == (multiplication is None), (
                "an algebra is stated on a module together with its multiplication"
            )
            self._preamble_unformed_module = unformed_module
            super().__init__(**rest)
            match multiplication:
                case None:
                    return
                case _:
                    self._preamble_multiplication_morphism = self._multiplication_read_on_this_algebra(multiplication)

        def unformed_module(self):
            r"""The module \(M\) this algebra was stated on, retained as data.

            The forgetful functor is the identity on the object; this is the
            constructor's retained input, and elements of it are read on this
            algebra by their coordinates in the common framing.  An algebra
            realized directly, not on a retained module, is its own module.
            """
            match self._preamble_unformed_module:
                case None:
                    return self
                case module:
                    return module

        def _read_in_this_algebra(self, element):
            r"""An element of ``unformed_module()`` with the same coordinates in this algebra."""
            module = self.unformed_module()
            if module is self:
                return self(element)
            return self.linear_combination(module.framing_coefficients(module(element)))

        @cached_method
        def _linear_map_from_unformed_module(self):
            r"""The linear map \(M\to A\) sending each module generator to its namesake."""
            module = self.unformed_module()
            return module.module_category().Mor(module, self)(self.module_generator)

        @cached_method
        def _linear_map_onto_unformed_module(self):
            r"""The linear map \(A\to M\) sending each module generator to its namesake."""
            module = self.unformed_module()
            return self.module_category().Mor(self, module)(module.module_generator)

        def _multiplication_read_on_this_algebra(self, multiplication):
            r"""\(m\colon A\otimes_R A\to A\) from \(m\colon M\otimes_R M\to M\).

            Both sides are bilinear, so the multiplication is determined by
            its values on pairs of module generators, and those are the stated
            values read on this algebra.
            """
            module = self.unformed_module()
            stated_tensor = multiplication.domain()
            tensor = _algebra_tensor_square_functor(self.algebra_base_ring())(self)
            return tensor.from_bilinear(
                BilinearMap(
                    self,
                    self,
                    self,
                    lambda left, right: self._read_in_this_algebra(
                        multiplication(
                            stated_tensor.pure_tensor(
                                module.module_generator(left),
                                module.module_generator(right),
                            )
                        )
                    ),
                )
            )

        def base_ring(self):
            return self.algebra_base_ring()

        def affine_equation_family(self, relative_variables, equations):
            r"""Return the relative affine family defined over this parameter algebra."""
            from dzack_research.preamble.categories.schemes.families import (
                RelativeAffineFamily,
            )

            return RelativeAffineFamily(self, relative_variables, equations)

        def restrict_scalars(self, ring_map):
            r"""Return this algebra with scalars restricted along ``ring_map``."""
            from dzack_research.preamble.categories.algebras.restricted_scalars import (
                _restrict_algebra_scalars,
            )

            return _restrict_algebra_scalars(self, ring_map)

        def derivations(self, target_module=None):
            r"""Return ``Der_R(self, M)`` for the selected ``self``-module ``M``."""
            from dzack_research.preamble.categories.algebras.derivations import (
                _derivations,
            )

            if target_module is None:
                target_module = self.regular_module()
            return _derivations(self, target_module)

        def vector_fields(self):
            r"""Return ``Der_R(self,self)`` with values in the regular module."""
            return self.derivations(self.regular_module())

        def is_algebra(self) -> bool:
            return True

        def is_framed_algebra(self) -> bool:
            return False

        def is_commutative(self):
            r"""Whether the multiplication commutes, decided on a finite module framing.

            Commutativity is a property of the multiplication before it is a
            category refinement, and both sides of \(xy = yx\) are bilinear,
            so a finite module generating set decides it.  An algebra with no
            finite framing answers ``Unknown`` rather than enumerating; the
            ``Commutative`` axiom answers ``True`` by placement.
            """
            match self.is_framed_module():
                case True:
                    labels = self.module_generating_set()
                case _:
                    return Unknown
            if not labels.cardinality().is_finite():
                return Unknown
            return _multiplication_is_commutative(self.multiplication_morphism())

        def product(self, left, right):
            r"""Evaluate this algebra's multiplication on two elements."""
            return self(left) * self(right)

        def algebra_base_ring(self):
            r"""The scalar ring this algebra is an algebra over.

            Every route that builds an algebra states the ring it is an
            algebra over -- the module level threads it to the host as the
            base, and a ring the preamble adopts declares the ring its engine
            presents it over -- so the answer is read off the construction.
            A ring presented over nothing smaller is an algebra over itself.
            """
            host_base = self.base()
            match host_base:
                case None:
                    return self
                case _ if host_base is self:
                    return self
                case _:
                    return _own_ring(host_base)

        def underlying_module(self):
            r"""This algebra under the forgetful functor ``Alg_R -> Mod_R`` of its category."""
            return Algebras(self.base_ring()).underlying_module()(self)

        @cached_method
        def multiplication_morphism(self):
            r"""The multiplication \(m\colon A\otimes_R A\to A\) as an \(R\)-module morphism.

            Centrality of the image of \(R\) is exactly \(R\)-bilinearity of
            the product, so \(m\) is the unique factorization of
            \((a,b)\mapsto ab\) through the tensor product.  An algebra built
            by the constructor states \(m\); a realization that states its
            product itself determines \(m\) on pairs of module generators, by
            bilinearity, and needs a module framing to do so.
            """
            match self._preamble_multiplication_morphism:
                case None:
                    assert self.is_framed_module(), (
                        f"the multiplication morphism of {self} is read off a module framing, and this realization states none"
                    )
                    tensor = _algebra_tensor_square_functor(self.algebra_base_ring())(self)
                    return tensor.from_bilinear(
                        BilinearMap(
                            self,
                            self,
                            self,
                            lambda left, right: self.module_generator(left) * self.module_generator(right),
                        )
                    )
                case multiplication:
                    return multiplication

        @cached_method
        def algebra_structure_morphism(self):
            r"""The structure morphism \(\rho\) of this \(R\)-algebra.

            Over commutative \(R\), \(\rho\) is the scalar action of the
            module: \(\rho(r)\) is multiplication by \(r\), an additive
            endomorphism commuting with left and right multiplication by
            bilinearity of the product, so it lands in the centroid of
            \(A\).  On the unital associative refinement the centroid is the
            centre through \(\varphi\mapsto\varphi(1)\), and \(\rho\) is the
            ring map \(R\to Z(A)\), \(r\mapsto r\cdot 1\): a theorem-backed
            specialization computed here from the unit, never a datum of the
            refinement.
            """
            base = self.algebra_base_ring()
            match self:
                case _ if self in Algebras(base).Associative().Unital():
                    center = self.ring_center()
                    unit_morphism = self.unit_morphism()
                    scalars = _scalar_module(base)
                    return base.Mor(center)(
                        lambda scalar: center(self(unit_morphism(scalars(base(scalar))))),
                    )
                case _:
                    return self.scalar_action()

        def Mor(self, codomain, category=None):
            base = self.base_ring()
            if category is None and base is self and self in OwnedRings():
                return OwnedRings.ParentMethods.Mor(self, codomain)
            algebras = Algebras(base)
            ordinary = algebras.Associative().Unital()
            if category is None:
                if self in ordinary and codomain in ordinary:
                    return ordinary.Mor(self, codomain)
                return algebras.Mor(self, codomain)
            if category.is_subcategory(ordinary):
                return ordinary.Mor(self, codomain)
            if category.is_subcategory(algebras):
                return algebras.Mor(self, codomain)
            return _category_homset(category, self, codomain)

        @cached_method
        def center(self):
            r"""The centre \(Z(A)\), an algebra when associativity closes it under the product.

            An element commutes with all of \(A\) exactly when it commutes
            with a module generating set, so \(Z(A)\) is the wide equalizer
            of the pairs (left multiplication by \(b\), right multiplication
            by \(b\)) over that set, computed in \(R\)-modules.  For an
            associative \(A\) the centre is closed under the product and is
            the commutative algebra stated on that submodule; it is unital
            when \(A\) is, with the same unit.
            """
            ring = self.base_ring()
            multiplication = self.multiplication_morphism()
            tensor = multiplication.domain()
            labels = self.module_generating_set()
            assert labels.cardinality().is_finite(), "the centre is computed here from a finite module generating set"
            endomorphisms = self.module_category().Mor(self, self)

            def commutation_equalizer(label):
                element = self.module_generator(label)
                left = endomorphisms({other: multiplication(tensor.pure_tensor(self.module_generator(other), element)) for other in labels})
                right = endomorphisms({other: multiplication(tensor.pure_tensor(element, self.module_generator(other))) for other in labels})
                return Modules(ring).equalizer(left, right)

            equalizers = iter(labels)
            center = commutation_equalizer(next(equalizers))
            for label in equalizers:
                center = center.intersection(commutation_equalizer(label))
            if self not in Algebras(ring).Associative():
                return center

            inclusion = center.inclusion()
            center_tensor = Modules(ring).tensor_product((center, center))
            center_multiplication = center_tensor.from_bilinear(
                BilinearMap(
                    center,
                    center,
                    center,
                    lambda left, right: inclusion.lift(
                        multiplication(
                            tensor.pure_tensor(
                                inclusion(center.module_generator(left)),
                                inclusion(center.module_generator(right)),
                            )
                        )
                    ),
                )
            )
            placement = [Algebras(ring).Associative(), Algebras(ring).Commutative()]
            construction_data = {}
            if self in Algebras(ring).Unital():
                placement.append(Algebras(ring).Unital())
                construction_data["unit_morphism"] = _unit_morphism_from_element(
                    center,
                    inclusion.lift(self.one()),
                    ring,
                )
            return _algebra_on_module(
                center,
                center_multiplication,
                placement=tuple(placement),
                construction_data=construction_data,
            )

        def center_inclusion(self):
            r"""The inclusion \(Z(A)\hookrightarrow A\) of this algebra, constructed as a centre.

            The centre is stated on a submodule of \(A\); its inclusion is
            that submodule's, read from this algebra.
            """
            module = self.unformed_module()
            assert module in ModuleSubobjects(self.base_ring()), (
                f"{self} was not constructed as the centre of an algebra: it is not stated on a submodule"
            )
            return module.inclusion() * self._linear_map_onto_unformed_module()

        def algebra_ideal_generated_by(self, subobject):
            r"""Return the algebra ideal generated by one represented submodule.

            In the supported finite-dimensional regime, the ideal generated by
            ``I`` is obtained by repeatedly adjoining all left and right products
            of ambient module generators with generators of the current
            submodule.  Over a field the resulting ascending chain of subspaces
            stabilizes after at most ``dim(A)`` strict enlargements, so the
            closure is an exact computation rather than a heuristic search.
            """

            ring = self.base_ring()
            assert ring in OwnedFields(), (
                "algebra-ideal closure is represented here for finite-dimensional algebras over fields"
            )
            if subobject.inclusion().codomain() is not self:
                raise ValueError("an algebra ideal generator must be a submodule of the algebra")
            ambient_labels = self.module_generating_set()
            assert ambient_labels.cardinality().is_finite(), (
                "algebra-ideal closure requires a finite selected module framing"
            )

            subobjects = Modules(ring).Subobjects(self)
            current = subobject
            while True:
                products = []
                inclusion = current.inclusion()
                for ideal_label in current.module_generating_set():
                    ideal_element = inclusion(current.module_generator(ideal_label))
                    for ambient_label in ambient_labels:
                        ambient_element = self.module_generator(ambient_label)
                        products.append(self.product(ambient_element, ideal_element))
                        products.append(self.product(ideal_element, ambient_element))

                if not products:
                    return current
                enlarged = current.sum(self.subobject_on(products))
                if subobjects.leq(enlarged, current):
                    return current
                current = enlarged

        def quotient_by_algebra_ideal(self, ideal):
            r"""Return ``A/I`` with the multiplication induced from ``A``.

            The supplied submodule must already be an algebra ideal.  The
            module cokernel provides the quotient module and projection; the
            multiplication on quotient generators is the image of the product
            of their selected lifts.  Associative, commutative, and Lie
            identities descend through quotients, and the image of the unit
            is the unit of the quotient, so those placements are stated with
            the construction rather than reverified coordinatewise.
            """
            ring = self.base_ring()
            if ideal.inclusion().codomain() is not self:
                raise ValueError("an algebra quotient requires an ideal in the algebra")
            projection = ideal.inclusion().cokernel_projection()
            quotient_module = projection.codomain()
            quotient_tensor = Modules(ring).tensor_product((quotient_module, quotient_module))
            multiplication = quotient_tensor.from_bilinear(
                BilinearMap(
                    quotient_module,
                    quotient_module,
                    quotient_module,
                    lambda left, right: projection(
                        self.product(
                            self.module_generator(left),
                            self.module_generator(right),
                        )
                    ),
                )
            )
            placement = [
                axiom
                for axiom in (
                    Algebras(ring).Associative(),
                    Algebras(ring).Commutative(),
                    Algebras(ring).Lie(),
                )
                if self in axiom
            ]
            construction_data = {}
            if self in Algebras(ring).Unital():
                placement.append(Algebras(ring).Unital())
                construction_data["unit_morphism"] = _unit_morphism_from_element(
                    quotient_module,
                    projection(self.one()),
                    ring,
                )
            quotient = _algebra_on_module(
                quotient_module,
                multiplication,
                placement=tuple(placement),
                construction_data=construction_data,
            )
            quotient._preamble_algebra_quotient_projection = quotient._linear_map_from_unformed_module() * projection
            quotient._preamble_algebra_quotient_ideal = ideal
            return quotient

        def quotient_by_generated_algebra_ideal(self, subobject):
            r"""Return the quotient by the algebra ideal generated by ``subobject``."""
            ideal = self.algebra_ideal_generated_by(subobject)
            return self.quotient_by_algebra_ideal(ideal)

        def algebra_quotient_projection(self):
            selected = self.__dict__.get("_preamble_algebra_quotient_projection")
            if selected is None:
                raise TypeError("this algebra was not constructed as a represented algebra quotient")
            return selected

        def algebra_quotient_ideal(self):
            selected = self.__dict__.get("_preamble_algebra_quotient_ideal")
            if selected is None:
                raise TypeError("this algebra was not constructed as a represented algebra quotient")
            return selected

        def _Hom_(self, codomain, category=None):
            if category is not None and not category.is_subcategory(Algebras(self.base_ring())):
                raise TypeError("this is not an algebra homset category")
            ordinary = Algebras(self.base_ring()).Associative().Unital()
            if self in ordinary and codomain in ordinary:
                return ordinary.Mor(self, codomain)
            return Algebras(self.base_ring()).Mor(self, codomain)

    def _call_(self, module, multiplication=None):
        r"""The algebra stated on ``module`` by ``multiplication``: the one entry (``CON-16``).

        ``Algebras(R)(M, m)`` builds the algebra on the data of \(M\) and
        retains \(M\) as ``unformed_module()``; ``Algebras(R)(m)`` reads
        \(M\) off the codomain of \(m\).
        """
        if multiplication is None:
            multiplication = module
            module = multiplication.codomain()
        return _algebra_on_module(module, multiplication)

    class Associative(CategoryWithAxiom):
        r"""Algebras whose selected multiplication is associative."""

        _HomCategory = GeneralAlgebraHomCategoryConstruction

        class SubcategoryMethods:
            def Unital(self):
                r"""Return the associative refinement with a two-sided unit."""
                return self._with_axiom("Unital")

            def commutator_lie_algebra(self):
                r"""Return the functor sending ``m`` to the Lie product ``m-m tau``."""
                from dzack_research.preamble.categories.functors.commutator_lie_algebras import (
                    _commutator_lie_algebra_functor,
                )

                return _commutator_lie_algebra_functor(self.base_ring())

        @classmethod
        def _repr_object_names(cls):
            return "associative algebras"

        def _call_(self, module, multiplication=None):
            r"""The associative algebra on ``(M, m)``, or an algebra proved associative."""
            if multiplication is None and module in Algebras(self.base_ring()):
                return refine(module, self)
            if multiplication is None:
                multiplication = module
                module = multiplication.codomain()
            return _algebra_on_module(module, multiplication, placement=(self,))

        class Unital(CategoryWithAxiom):
            r"""Associative unital algebras: the ring objects among algebras."""

            @classmethod
            def _repr_object_names(cls):
                return "algebras"

            def extra_super_categories(self):
                return [
                    Algebras(self.base_ring()).Unital(),
                    OwnedRings(),
                ]

            _HomCategory = AlgebraHomCategoryConstruction

            class SubcategoryMethods:
                def FinitelyPresentedAsAlgebra(self):
                    r"""Return the refinement whose objects admit a finite algebra presentation."""
                    return self._with_axiom("FinitelyPresentedAsAlgebra")

            class FinitelyPresentedAsAlgebra(CategoryWithAxiom):
                r"""Algebras that admit a finite algebra presentation.

                A property: the presentation exists and none is chosen.
                ``AlgebrasWithChosenFinitePresentation`` is the data category.
                """

                @classmethod
                def _repr_object_names(cls):
                    return "finitely presented algebras"

                def an_object(self):
                    r"""``R[x]/(x^2)``, the dual numbers: one generator and one relation."""
                    presentation = self.base_ring().free_module(("x",)).symmetric_algebra()
                    return presentation.quotient_by_relations(("x^2",))

                class ParentMethods:
                    def is_finitely_presented(self) -> bool:
                        return True

            def _call_(self, module, multiplication=None, unit=None):
                r"""The associative unital algebra on ``(M, m, eta)``, ``eta: U_R(R) -> M`` its unit."""
                return _unital_algebra_on_module(self, module, multiplication, unit)

            class Commutative(CategoryWithAxiom):
                r"""Commutative associative unital ``R``-algebras."""

                _HomCategory = AlgebraHomCategoryConstruction
                SubcategoryMethods = _CommutativeUnitalAlgebraSubcategoryMethods
                ParentMethods = _CommutativeUnitalAlgebraParentMethods

                @classmethod
                def _repr_object_names(cls):
                    return "commutative algebras"

                def an_object(self):
                    modules = Modules(self.base_ring())
                    return modules.symmetric_algebra()(modules.an_object())

            class ParentMethods:
                def _algebra_homset_class(self):
                    r"""The Hom parent an algebra with this domain takes.

                    An algebra stated on a retained module states its maps as
                    linear maps preserving the multiplication.  An engine
                    realization not yet routed through the constructor states
                    them on its algebra generators, in the engine.
                    """
                    match self._preamble_unformed_module:
                        case None:
                            return AlgebraHomset
                        case _:
                            return UnitalMultiplicativeAlgebraHomset

                def algebra_homset(self, hom_family, codomain):
                    return self._algebra_homset_class()(hom_family, self, codomain)

    class Lie(CategoryWithAxiom):
        r"""Algebras whose selected bilinear multiplication satisfies the Lie identities.

        No associativity or unit is implied: the multiplication at this node
        is the bracket itself.  Consequently the ordinary algebra Hom already
        has the correct morphisms, namely the linear maps preserving that
        multiplication.
        """

        _HomCategory = GeneralAlgebraHomCategoryConstruction

        @classmethod
        def _repr_object_names(cls):
            return "Lie algebras"

        def an_object(self):
            r"""``gl_2(R)``: the two-by-two matrix algebra under the commutator."""
            ring = self.base_ring()
            return Algebras(ring).Associative().commutator_lie_algebra()(
                MatrixAlgebras(ring).an_object()
            )

        def _call_(self, module, multiplication=None):
            r"""The Lie algebra on ``(M, m)``, ``m`` its bracket, or an algebra proved Lie."""
            if multiplication is None and module in Algebras(self.base_ring()):
                return refine(module, self)
            if multiplication is None:
                multiplication = module
                module = multiplication.codomain()
            return _algebra_on_module(module, multiplication, placement=(self,))

        class ParentMethods:
            def bracket(self, left, right):
                return self.product(left, right)

    class Unital(CategoryWithAxiom):
        r"""Algebras with a two-sided unit, without associativity.

        The unit is unique when it exists, so this is a property; the unit
        morphism \(\eta\colon U_R(R)\to M\), \(r\mapsto r\cdot 1\), is the
        witness the constructor takes, verified on a finite module framing
        and recorded ``Unknown`` otherwise.
        """

        _HomCategory = UnitalGeneralAlgebraHomCategoryConstruction

        @classmethod
        def _repr_object_names(cls):
            return "unital algebras"

        def _call_(self, module, multiplication=None, unit=None):
            r"""The unital algebra on ``(M, m, eta)``, ``eta: U_R(R) -> M`` its unit."""
            return _unital_algebra_on_module(self, module, multiplication, unit)

        class ParentMethods:
            # The unit witness \(\eta\colon U_R(R)\to M\) and the unit itself,
            # \(\eta(1)\) read on this algebra.  ``None`` is the state of a
            # realization that presents its unit itself (an engine ring) and
            # has not been routed through the constructor.
            _preamble_algebra_unit_morphism = None
            _preamble_algebra_unit = None
            _preamble_unit_equations_hold = None

            def __init__(self, unit_morphism=None, **rest) -> None:
                self._preamble_algebra_unit_morphism = unit_morphism
                super().__init__(**rest)
                match unit_morphism:
                    case None:
                        return
                    case _:
                        base = self.algebra_base_ring()
                        self._preamble_algebra_unit = self._read_in_this_algebra(
                            unit_morphism(_scalar_module(base)(base.one()))
                        )
                        held = _unit_equations_hold(self)
                        assert held is not False, (
                            f"the stated unit of {self} fails a unit equation on a module generator"
                        )
                        self._preamble_unit_equations_hold = held

            def unit_equations_hold(self):
                r"""``True`` when \(1x = x = x1\) was decided on a finite framing, else ``Unknown``."""
                match self._preamble_unit_equations_hold:
                    case None:
                        return Unknown
                    case held:
                        return held

            @cached_method
            def one(self):
                match self._preamble_algebra_unit:
                    case None:
                        return super().one()
                    case unit:
                        return self(unit)

            @cached_method
            def unit_morphism(self):
                r"""\(\eta\colon U_R(R)\to A\), \(r\mapsto r\cdot 1\), with this algebra as codomain."""
                base = self.algebra_base_ring()
                scalars = _scalar_module(base)
                stated = self._preamble_algebra_unit_morphism
                match stated:
                    case None:
                        # The realization presents its scalars itself: an
                        # engine ring converts a scalar to r*1 through the ring
                        # map its engine states.
                        def image(scalar):
                            return self(scalar)
                    case _ if stated.codomain() is self:
                        return stated
                    case _:
                        def image(scalar):
                            return self._read_in_this_algebra(stated(scalar))
                return ModuleMorphism(
                    scalars.module_category().Mor(scalars, self),
                    image,
                    elementwise=True,
                    verify_linearity=False,
                )

    class Commutative(CategoryWithAxiom):
        r"""Algebras whose selected multiplication is commutative."""

        @classmethod
        def _repr_object_names(cls):
            return "commutative algebras"

        def an_object(self):
            r"""A commutative product supplied by an ordinary commutative ring."""
            return Algebras(self.base_ring()).Associative().Unital().Commutative().an_object()

        class ParentMethods:
            def is_commutative(self) -> bool:
                return True


# ``Lie`` is an owned algebra axiom not known to Sage's global axiom registry.
# Register the nested refinement explicitly so ``Algebras(R).Lie()`` is a
# category-with-axiom rather than an inference through Sage's built-in names.
Algebras.__dict__["Lie"]._base_category_class_and_axiom = (Algebras, "Lie")

FinitelyPresentedAlgebras = Algebras.Associative.Unital.FinitelyPresentedAsAlgebra


class FramedAlgebras(OwnedCategoryOverBaseRing):
    r"""Algebras carrying a chosen algebra generating set."""

    def an_object(self):
        r"""The polynomial algebra on one generator, framed by it."""
        modules = Modules(self.base_ring())
        return modules.symmetric_algebra()(modules.an_object())

    @classmethod
    def _repr_object_names(cls):
        return "framed algebras"

    def super_categories(self):
        return [Algebras(self.base_ring()).Associative().Unital()]

    class ParentMethods:
        def is_framed_algebra(self) -> bool:
            return True

        def cardinality(self):
            base_cardinality = self.base_ring().cardinality()
            generator_cardinality = self.algebra_generating_set().cardinality()
            if generator_cardinality.is_countable():
                if base_cardinality.is_finite() or base_cardinality.is_countable():
                    return aleph0
                return base_cardinality
            return super().cardinality()

        def algebra_generating_set(self):
            return self._preamble_algebra_generating_set

        @cached_method
        def algebra_generators(self):

            return indexed_family(
                self.algebra_generating_set(),
                self.algebra_generator,
                name=f"Algebra generators of {self}",
            )

        def algebra_generator(self, label):
            labels = self.algebra_generating_set()
            if label not in labels:
                raise ValueError(f"{label!r} is not an algebra-generator label")
            return self._preamble_algebra_generator_values[label]

        def finite_algebra_generators(self):
            r"""Return the selected algebra generators as a finite ordered family."""
            labels = self.algebra_generating_set()
            assert labels.cardinality().is_finite(), (
                f"finite_algebra_generators requires a finite chosen algebra generating set on {self}"
            )
            return FiniteOrderedSets().from_indexed(
                labels,
                self.algebra_generator,
                name=f"Selected algebra generators of {self}",
            )

        @cached_method
        def algebra_generator_morphism(self):
            r"""Return the selected map from generator labels into the algebra."""
            return SetMorphism(
                Sets().Mor(self.algebra_generating_set(), self),
                self.algebra_generator,
            )

        def number_of_algebra_generators(self):
            return self.algebra_generating_set().cardinality()

        def product_on_algebra_generators(self, left, right):
            return self.algebra_generator(left) * self.algebra_generator(right)

        def is_central(self, element):
            r"""Decide centrality from the selected algebra generating family."""
            if element not in self:
                return False
            return all(element * self.algebra_generator(label) == self.algebra_generator(label) * element for label in self.algebra_generating_set())


class MatrixAlgebras(OwnedCategoryOverBaseRing):
    r"""Finite matrix endomorphism Hom objects with their canonical algebra structure."""

    def an_object(self):
        r"""``End_R(Free_R([2]))``, the two-by-two matrix algebra."""
        from dzack_research.preamble.categories.sets.set_categories import (
            finite_ordinal_set,
        )

        ring = self.base_ring()
        plane = Sets().free_module(ring)(finite_ordinal_set(2))
        return Modules(ring).Mor(plane, plane)

    @classmethod
    def _repr_object_names(cls):
        return "matrix algebras"

    def super_categories(self):
        if self.base_ring() not in OwnedRings().Commutative():
            raise TypeError("the canonical R-algebra structure on End_R(F) needs commutative R")
        return [
            MatrixEndomorphismSpaces(self.base_ring()),
            FramedAlgebras(self.base_ring()),
        ]

    # M_n(R) is unital, so a morphism of matrix algebras preserves the unit.
    # The associative Hom that arrives from the endomorphism spaces below does
    # not ask that, and this says which of the two the category means.
    _HomCategory = AlgebraHomCategoryConstruction

    class ParentMethods:
        def algebra_base_ring(self):
            return self._preamble_base_ring

        def is_commutative(self) -> bool:
            r"""``M_n(R)`` commutes exactly when ``n <= 1``.

            This category is over a commutative ring, so the only obstruction
            is the size of the matrices.  Rank one gives ``R`` itself and rank
            zero the zero ring; from rank two the matrix units ``e_{12}`` and
            ``e_{21}`` fail to commute.
            """
            return self.nrows() <= 1

        @cached_method
        def _ring_morphism_defining_algebra_structure(self):

            ring = self.base_ring()
            center = self.ring_center()
            identity = self.identity()
            return ring.Mor(center)(
                lambda scalar: center(self.scalar_multiple(scalar, identity)),
            )

        def algebra_generating_set(self):
            return self.module_generating_set()

        def algebra_generator(self, label):
            label = self.algebra_generating_set()(label)
            return self.matrix_unit(label[0], label[1])


def _refine_matrix_algebra(homset):
    r"""Return a square matrix Hom after requiring constructor-time algebra placement."""

    ring = homset.base_ring()
    if homset not in MatrixEndomorphismSpaces(ring):
        return homset
    if ring not in OwnedRings().Commutative():
        return homset
    if homset not in MatrixAlgebras(ring):
        raise TypeError("a finite-free endomorphism Hom over a commutative ring must be constructed in its canonical matrix-algebra category")
    return homset


class _SelectedFiniteAlgebraPresentation:
    r"""The chosen polynomial presentation defining a presented algebra.

    The presenting algebra, relation family, defining ideal, quotient map, and
    selected lift are one mathematical choice.  Keep them together so the
    chosen-presentation category does not infer that choice from unrelated
    private attributes on its objects.
    """

    def __init__(
        self,
        presentation_ring,
        relations,
        presentation_ideal,
        lift_to_presentation,
    ) -> None:
        self._presentation_ring = presentation_ring
        self._relations = relations
        self._presentation_ideal = presentation_ideal
        self._lift_to_presentation = lift_to_presentation
        self._presentation_morphism = None

    def presentation_ring(self):
        return self._presentation_ring

    def relations(self):
        return self._relations

    def presentation_ideal(self):
        return self._presentation_ideal

    def lift(self, element):
        return self._lift_to_presentation(element)

    def set_presentation_morphism(self, morphism) -> None:
        if self._presentation_morphism is not None and self._presentation_morphism is not morphism:
            raise ValueError("the selected algebra presentation already has its quotient morphism")
        self._presentation_morphism = morphism

    def presentation_morphism(self):
        assert self._presentation_morphism is not None, (
            "the selected algebra presentation must acquire its quotient morphism during construction"
        )
        return self._presentation_morphism


class AlgebrasWithChosenFinitePresentation(OwnedCategoryOverBaseRing):
    r"""Finitely presented algebras carrying one selected finite presentation."""

    def an_object(self):
        r"""``R[x]/(x^2)``, the dual numbers: one generator and one relation."""
        presentation = self.base_ring().free_module(("x",)).symmetric_algebra()
        return presentation.quotient_by_relations(("x^2",))

    @classmethod
    def _repr_object_names(cls):
        return "algebras with a chosen finite presentation"

    def super_categories(self):
        return [
            Algebras(self.base_ring()).Associative().Unital().FinitelyPresentedAsAlgebra(),
            FramedAlgebras(self.base_ring()),
        ]

    def _call_(
        self,
        presentation_ring,
        relations,
        *,
        extra_categories=(),
        extra_construction_data=None,
        free_source_module=None,
    ):
        r"""Construct an algebra from its selected finite polynomial presentation."""
        if presentation_ring.base_ring() is not self.base_ring():
            raise ValueError("a chosen algebra presentation stays over its stated scalar base")
        from dzack_research.preamble.categories.algebras.free_algebras import (
            _finitely_presented_algebra_from_data,
        )

        return _finitely_presented_algebra_from_data(
            presentation_ring,
            relations,
            _extra_categories=tuple(extra_categories),
            _extra_construction_data=extra_construction_data,
            _free_source_module=free_source_module,
        )

    class ParentMethods:
        def _algebra_homset_class(self):
            return PresentedAlgebraHomset

        def selected_algebra_presentation(self):
            r"""Return the one chosen polynomial-presentation datum for this algebra."""
            return self._selected_algebra_presentation

        def presentation_ring(self):
            return self.selected_algebra_presentation().presentation_ring()

        def _has_selected_exact_coefficient_presentation(self) -> bool:
            return True

        def _exact_coefficient_presentation_ring(self):
            return self.presentation_ring()

        def _exact_coefficient_presentation_relations(self):
            return self.relations()

        def _lift_coefficient_to_presentation(self, value):
            return self.lift_to_presentation(self(value))

        def _descend_coefficient_from_presentation(self, value):
            return self(value)

        def relations(self):
            return self.selected_algebra_presentation().relations()

        def presentation_ideal(self):
            return self.selected_algebra_presentation().presentation_ideal()

        def presentation(self):
            return self.presentation_ring(), self.relations()

        def _represented_structure_morphism_kernel_is_zero(self) -> bool:
            r"""Decide whether the selected scalar map has zero kernel by elimination.

            For ``A = R[x_1,...,x_n]/I`` the kernel of ``R -> A`` is
            ``I cap R``.  When the selected computation ring is the relative
            polynomial ring itself, or its canonical flattening, eliminate the
            algebra variables and ask the established polynomial-ideal backend
            for this intersection.
            """

            presentation = self.presentation_ring()
            presentation_engine = _engine_ring(presentation)
            algebra_engine = _engine_ring(self)
            try:
                cover = algebra_engine.cover_ring()
                defining_ideal = algebra_engine.defining_ideal()
            except (
                AttributeError,
                NotImplementedError,
                TypeError,
                ValueError,
            ) as error:
                raise AssertionError(
                    "the selected algebra presentation requires a quotient-cover elimination backend"
                ) from error

            if cover is presentation_engine:
                algebra_variables = tuple(presentation_engine.gens())
            else:
                flattening_factory = getattr(
                    presentation_engine,
                    "flattening_morphism",
                    None,
                )
                assert callable(flattening_factory), (
                    "the selected relative presentation requires a canonical polynomial flattening"
                )
                flattening = flattening_factory()
                assert flattening.codomain() is cover, (
                    "the selected quotient cover must be the codomain of the canonical presentation flattening"
                )
                algebra_variables = tuple(flattening(generator) for generator in presentation_engine.gens())

            try:
                scalar_kernel = defining_ideal.elimination_ideal(algebra_variables)
            except (
                AttributeError,
                NotImplementedError,
                TypeError,
                ValueError,
            ) as error:
                raise AssertionError(
                    "the selected polynomial presentation backend must eliminate the algebra variables"
                ) from error
            return bool(scalar_kernel.is_zero())

        def is_torsion_free(self) -> bool:
            r"""Decide torsion-freeness in the supported integral PID-algebra regime.

            If ``R`` and ``A`` are domains, then the ``R``-module ``A`` is
            torsion-free exactly when the unital structure map ``R -> A`` is
            injective: a nonzero scalar in the kernel kills ``1_A``, while an
            injective scalar map and absence of zero divisors make multiplication
            by every nonzero scalar injective.
            """

            base = self.base_ring()
            if bool(_engine_ring(base).is_field()):
                return True
            assert base in PrincipalIdealDomains(), (
                "the represented algebra torsion-freeness criterion requires a PID base"
            )
            assert bool(self.is_integral_domain()), (
                "the represented PID-algebra torsion criterion requires an integral target"
            )
            return self._represented_structure_morphism_kernel_is_zero()

        def _represented_primitive_hypersurface_relative_dimension(self) -> int:
            r"""Return the common fibre dimension for a primitive hypersurface presentation."""

            relations = self.relations()
            assert relations.cardinality().is_finite() and int(relations.cardinality()) == 1, (
                "the represented relative-dimension criterion requires one defining equation"
            )
            labels = self.presentation_ring().algebra_generating_set()
            assert labels.cardinality().is_finite(), (
                "the represented hypersurface criterion requires finitely many relative variables"
            )
            variable_count = int(labels.cardinality())
            assert variable_count > 0, (
                "the represented hypersurface criterion requires a positive relative affine dimension"
            )

            relation_index = next(iter(relations.index_set()))
            relation = relations.value(relation_index)
            presentation = self.presentation_ring()
            presentation_engine = _engine_ring(presentation)
            backend_relation = presentation_engine(_engine_element(presentation, relation))
            coefficient_ideal = self.base_ring().ideal(*tuple(self.base_ring()._from_engine_element(coefficient) for coefficient in backend_relation.coefficients()))
            assert coefficient_ideal == self.base_ring().ideal(self.base_ring().one()), (
                "the represented hypersurface relative-dimension criterion requires a primitive defining equation"
            )
            return variable_count - 1

        def algebra_presentation_morphism(self):
            return self.selected_algebra_presentation().presentation_morphism()

        def lift_to_presentation(self, element):
            return self.selected_algebra_presentation().lift(element)

        def presentation_normal_form_terms(self, element):
            r"""Return the selected reduced presentation representative as owned monomial terms.

            The chosen finite presentation fixes a polynomial representative
            for every quotient element.  Its computational normal form is
            private; this method raises that representative to a finite mapping
            from owned presentation monomials to owned scalar coefficients.
            """
            presentation = self.presentation_ring()
            representative = self.lift_to_presentation(self(element))
            backend = _engine_element(presentation, representative)
            labels = tuple(presentation.algebra_generating_set())
            base = self.base_ring()
            engine_base = _engine_ring(base)
            terms = {}
            for exponent, coefficient in backend.monomial_coefficients().items():
                try:
                    powers = tuple(int(value) for value in exponent)
                except TypeError:
                    powers = (int(exponent),)
                monomial = presentation.one()
                for label, power in zip(labels, powers, strict=True):
                    if power:
                        monomial *= presentation.algebra_generator(label) ** power
                terms[monomial] = base._from_engine_element(engine_base(coefficient))
            return terms

        def base_change(self, ring_map):
            r"""Extend this chosen commutative presentation along ``ring_map``."""
            assert self in Algebras(self.base_ring()).Associative().Unital().Commutative(), (
                "base change of a chosen algebra presentation is currently represented for commutative algebras"
            )
            from dzack_research.preamble.categories.algebras.free_algebras import (
                _base_change_commutative_presentation,
            )

            return _base_change_commutative_presentation(self, ring_map)

        def _commutative_algebra_coproduct(self, left, right):
            operation = getattr(
                self,
                "_preamble_commutative_algebra_coproduct_backend",
                None,
            )
            assert operation is not None, (
                "this selected presentation requires a represented commutative-algebra coproduct backend"
            )
            return operation(left, right)

        def _commutative_algebra_pushout(self, left_map, right_map):
            operation = getattr(
                self,
                "_preamble_commutative_algebra_pushout_backend",
                None,
            )
            assert operation is not None, (
                "this selected presentation requires a represented commutative-algebra pushout backend"
            )
            return operation(left_map, right_map)


class CommutativeAlgebraCoproducts(OwnedCategoryOverBaseRing):
    r"""Commutative ``R``-algebras equipped as selected binary coproducts."""

    def an_object(self):
        r"""``R[x] \otimes_R R[y]``, the coproduct of two polynomial algebras."""

        ring = self.base_ring()
        return Algebras(ring).Associative().Unital().Commutative().coproduct((ring.free_module(("x",)).symmetric_algebra(), ring.free_module(("y",)).symmetric_algebra()))

    def super_categories(self):
        return [Algebras(self.base_ring()).Associative().Unital().Commutative()]

    class ParentMethods:
        def coproduct_factors(self):
            r"""Return the family of factors, indexed by the product's own index set."""

            return _finite_factor_family(self._preamble_coproduct_factors, name="Coproduct factors")

        tensor_factors = coproduct_factors

        @cached_method
        def coproduct_injection(self, index):
            index = int(index)
            if index not in (0, 1):
                raise IndexError("a binary coproduct has two injections")
            factor = self.coproduct_factors()[index]
            tag = "left" if index == 0 else "right"
            return factor.Mor(self)({label: self.algebra_generator((tag, label)) for label in factor.algebra_generating_set()})

        def coproduct_injections(self):
            return tuple(self.coproduct_injection(index) for index in range(2))

        def left_coproduct_map(self):
            return self.coproduct_injection(0)

        def right_coproduct_map(self):
            return self.coproduct_injection(1)

        def from_cocone(self, left_map, right_map):
            left, right = self.coproduct_factors()
            if left_map.domain() is not left or right_map.domain() is not right:
                raise ValueError("the cocone maps have the wrong factor domains")
            if left_map.codomain() is not right_map.codomain():
                raise ValueError("the cocone maps must have one common codomain")
            target = left_map.codomain()
            images = {
                **{("left", label): left_map(left.algebra_generator(label)) for label in left.algebra_generating_set()},
                **{("right", label): right_map(right.algebra_generator(label)) for label in right.algebra_generating_set()},
            }
            return self.Mor(target)(images)

        tensor_map = from_cocone


class CommutativeAlgebraPushouts(OwnedCategoryOverBaseRing):
    r"""Commutative ``R``-algebras equipped as selected pushouts of one span."""

    def an_object(self):
        r"""``R[x] \otimes_{R[t]} R[y]`` for ``t`` sent to ``x`` and to ``y``.

        The pushout of the span whose legs are the two isomorphisms
        \(R[t]\to R[x]\) and \(R[t]\to R[y]\).
        """

        ring = self.base_ring()
        common = ring.free_module(("t",)).symmetric_algebra()
        left = ring.free_module(("x",)).symmetric_algebra()
        right = ring.free_module(("y",)).symmetric_algebra()
        return Algebras(ring).Associative().Unital().Commutative().pushout(
            common.Mor(left)({"t": left.algebra_generator("x")}),
            common.Mor(right)({"t": right.algebra_generator("y")}),
        )

    def super_categories(self):
        return [Algebras(self.base_ring()).Associative().Unital().Commutative()]

    class ParentMethods:
        def pushout_span(self):
            return self._preamble_pushout_span

        @cached_method
        def pushout_maps(self):
            coproduct = self._preamble_pushout_coproduct
            quotient_map = coproduct.Mor(self)({label: self.algebra_generator(label) for label in coproduct.algebra_generating_set()})
            return tuple(quotient_map * injection for injection in coproduct.coproduct_injections())

        def left_pushout_map(self):
            return self.pushout_maps()[0]

        def right_pushout_map(self):
            return self.pushout_maps()[1]

        def from_pushout_cocone(self, left_map, right_map):
            source_map, target_map = self.pushout_span()
            left_factor = source_map.codomain()
            right_factor = target_map.codomain()
            if left_map.domain() is not left_factor or right_map.domain() is not right_factor:
                raise ValueError("the pushout cocone has the wrong factor domains")
            if left_map.codomain() is not right_map.codomain():
                raise ValueError("the pushout cocone maps require one common codomain")
            common_source = source_map.domain()
            for label in common_source.algebra_generating_set():
                element = common_source.algebra_generator(label)
                if left_map(source_map(element)) != right_map(target_map(element)):
                    raise ValueError("the cocone does not agree on the common algebra")
            target = left_map.codomain()
            images = {
                **{("left", label): left_map(left_factor.algebra_generator(label)) for label in left_factor.algebra_generating_set()},
                **{("right", label): right_map(right_factor.algebra_generator(label)) for label in right_factor.algebra_generating_set()},
            }
            return self.Mor(target)(images)


class AlgebraMorphism(Morphism):
    r"""An ``R``-algebra morphism specified by the images of algebra generators."""

    def __init__(self, parent, images) -> None:
        Morphism.__init__(self, parent)
        domain = self.domain()
        codomain = self.codomain()
        engine_domain = _engine_ring(domain)
        engine_codomain = _engine_ring(codomain)
        framed_domain = domain in FramedAlgebras(domain.base_ring())
        self._engine_morphism = None
        self._element_function = None

        if isinstance(images, ModuleMorphism):
            if images.domain() is not domain or images.codomain() is not codomain:
                raise ValueError("an adopted module morphism must have the owned algebra homset's exact domain and codomain")

            labels = domain.module_generating_set()
            size = labels.cardinality()
            assert size.is_finite(), (
                "verification that an adopted module morphism is multiplicative requires a finite module generating set"
            )
            if images(domain.one()) != codomain.one():
                raise ValueError("an algebra morphism must preserve the unit")
            for left_label in labels:
                left = domain.module_generator(left_label)
                for right_label in labels:
                    right = domain.module_generator(right_label)
                    if images(left * right) != images(left) * images(right):
                        raise ValueError("the adopted module morphism is not multiplicative on the selected module generators")
            self._element_function = images
            if framed_domain:
                algebra_labels = domain.algebra_generating_set()
                self._generator_images = indexed_family(
                    algebra_labels,
                    lambda label: codomain(images(domain.algebra_generator(label))),
                    name="Generator images",
                )
            else:
                self._generator_images = None
            return
        if isinstance(images, Map):
            if images.domain() is domain and images.codomain() is codomain:
                self._element_function = images
                if framed_domain:
                    labels = domain.algebra_generating_set()
                    self._generator_images = indexed_family(
                        labels,
                        lambda label: codomain(images(domain.algebra_generator(label))),
                        name="Generator images",
                    )
                else:
                    self._generator_images = None
                return
            if images.domain() is not engine_domain or images.codomain() is not engine_codomain:
                raise ValueError("an algebra morphism datum must have either the owned endpoints or their private engine endpoints")
            self._engine_morphism = images
            if framed_domain:
                labels = domain.algebra_generating_set()
                self._generator_images = indexed_family(
                    labels,
                    lambda label: codomain(images(engine_domain(domain.algebra_generator(label)))),
                    name="Generator images",
                )
            else:
                self._generator_images = None
            return
        assert framed_domain, (
            "an algebra morphism from an unframed domain must be supplied as an exact engine ring morphism"
        )
        labels = domain.algebra_generating_set()
        if isinstance(images, IndexedFamily):
            source_indices = images.index_set()
            self._generator_images = indexed_family(
                labels,
                lambda label: codomain(images[source_indices(label)]),
                name="Generator images",
            )
        elif isinstance(images, dict):
            if not labels.cardinality().is_finite():
                raise TypeError("dictionary algebra-generator syntax requires a finite framing; use a callable or indexed family for an infinite framing")
            missing = [label for label in labels if label not in images]
            if missing:
                raise ValueError(f"algebra-generator assignment omits {missing}")
            self._generator_images = indexed_family(
                labels,
                lambda label: codomain(images[label]),
                name="Generator images",
            )
        elif isinstance(images, (tuple, list)):
            size = labels.cardinality()
            if not size.is_finite():
                raise TypeError("sequence algebra-generator syntax requires a finite framing; use a callable or indexed family for an infinite framing")
            values = tuple(images)
            if len(values) != int(size.finite_value()):
                raise ValueError("the number of algebra-generator images must equal the framing size")
            if labels not in EnumeratedSets():
                raise TypeError("sequence algebra-generator syntax requires a ranked framing")
            self._generator_images = indexed_family(
                labels,
                lambda label: codomain(values[int(labels.ranking_map()(label))]),
                name="Generator images",
            )
        elif callable(images):
            self._generator_images = indexed_family(
                labels,
                lambda label: codomain(images(label)),
                name="Generator images",
            )
        else:
            raise TypeError("an algebra morphism is specified on the algebra generating set")

        assert engine_domain in SageRings() and engine_codomain in SageRings(), (
            "generator-defined maps at this generic algebra-Hom boundary require native Sage ring endpoints; "
            "owned-only maps use the free or chosen-presentation Hom categories"
        )
        self._engine_morphism = _engine_algebra_morphism_from_generator_images(
            domain,
            codomain,
            self._generator_images,
        )

    def __call__(self, element):
        r"""Apply this owned algebra morphism to an engine-backed facade element."""
        return self._call_(element)

    def _call_(self, element):
        r"""Apply the algebra map in its represented realization."""
        if self._element_function is not None:
            return self.codomain()(self._element_function(self.domain()(element)))
        engine_morphism = self._engine_morphism_crossing()
        source = _engine_ring(self.domain())
        return self.codomain()(engine_morphism(source(element)))

    def _engine_morphism_crossing(self):
        r"""Return the private engine morphism when this map has one.

        Protected contract for bridge consumers that must construct a native
        Sage object.  An algebra morphism represented entirely in the owned
        universe deliberately has no such engine morphism.
        """
        if self._engine_morphism is not None:
            return self._engine_morphism
        return _engine_algebra_morphism(self)

    def algebra_generator_morphism(self):
        assert self._generator_images is not None, (
            "algebra_generator_morphism requires a selected algebra generating family on the domain"
        )
        return SetMorphism(
            Sets().Mor(self.domain().algebra_generating_set(), self.codomain()),
            self._generator_images.value,
        )

    def algebra_generator_images(self):
        assert self._generator_images is not None, (
            "algebra_generator_images requires a selected algebra generating family on the domain"
        )
        return self._generator_images

    def corestrict_to_center(self):
        r"""Factor this algebra morphism through the represented centre of its codomain."""
        return _corestrict_algebra_morphism_to_center(self)

    def _richcmp_(self, other, op):
        r"""Decide equality from the source's chosen algebra generating set.

        Two algebra morphisms agree exactly when they agree on generators, so
        this is decidable when the source is framed and not otherwise.
        """
        from sage.structure.richcmp import op_EQ, op_NE

        if op not in (op_EQ, op_NE):
            return NotImplemented
        if not isinstance(other, AlgebraMorphism) or other.parent() is not self.parent():
            return op == op_NE
        if self is other:
            return op == op_EQ
        domain = self.domain()
        if domain not in FramedAlgebras(domain.base_ring()):
            return Unknown
        equal = self.algebra_generator_images() == other.algebra_generator_images()
        if equal is Unknown:
            return Unknown
        return equal if op == op_EQ else not equal

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        if not isinstance(other, AlgebraMorphism):
            compose = getattr(other, "_postcompose_algebra_morphism", None)
            return NotImplemented if compose is None else compose(self)
        if self._engine_morphism is not None and other._engine_morphism is not None:
            composed_engine = self._engine_morphism * other._engine_morphism
            return Algebras(other.domain().base_ring()).Associative().Unital().Mor(other.domain(), self.codomain())(composed_engine)
        if other.domain() in FramedAlgebras(other.domain().base_ring()):
            return (Algebras(other.domain().base_ring()).Associative().Unital().Mor(other.domain(), self.codomain()))(
                lambda label: self(other(other.domain().algebra_generator(label)))
            )

        if other.domain() in FramedModules(other.domain().base_ring()):
            source = other.domain()
            target = self.codomain()
            module_map = source.module_category().Mor(source, target)(
                lambda label: self(other(source.module_generator(label)))
            )
            return Algebras(source.base_ring()).Associative().Unital().Mor(
                source,
                target,
            )(module_map)
        return (
            Algebras(other.domain().base_ring())
            .Associative()
            .Unital()
            .Mor(other.domain(), self.codomain())(
                SetMorphism(
                    Sets().Mor(other.domain(), self.codomain()),
                    lambda element: self(other(element)),
                )
            )
        )


class PresentedAlgebraMorphism(Morphism):
    r"""A map from an algebra with a chosen finite presentation.

    The map is defined on the presentation algebra, its selected relations are
    checked once, and evaluation descends by the chosen quotient projection.
    No Sage target-ring protocol is involved.
    """

    def __init__(self, parent, images) -> None:
        Morphism.__init__(self, parent)
        domain = self.domain()
        labels = domain.algebra_generating_set()
        size = labels.cardinality()
        if not size.is_finite():
            raise ValueError("a chosen finite algebra presentation must have a finite framing")
        if isinstance(images, IndexedFamily):
            source_indices = images.index_set()
            selected = indexed_family(
                labels,
                lambda label: self.codomain()(images[source_indices(label)]),
                name="Generator images",
            )
        elif isinstance(images, dict):
            missing = [label for label in labels if label not in images]
            if missing:
                raise ValueError(f"algebra-generator assignment omits {missing}")
            selected = indexed_family(
                labels,
                lambda label: self.codomain()(images[label]),
                name="Generator images",
            )
        elif isinstance(images, (tuple, list)):
            values = tuple(images)
            if len(values) != int(size.finite_value()):
                raise ValueError("the number of algebra-generator images must equal the framing size")
            selected = indexed_family(
                labels,
                lambda label: self.codomain()(values[int(labels.ranking_map()(label))]),
                name="Generator images",
            )
        elif callable(images):
            selected = indexed_family(
                labels,
                lambda label: self.codomain()(images(label)),
                name="Generator images",
            )
        else:
            raise TypeError("a presented-algebra morphism is specified on its algebra generators")
        self._generator_images = selected
        self._presentation_map = Algebras(domain.presentation_ring().base_ring()).Associative().Unital().Mor(domain.presentation_ring(), self.codomain())(selected)
        zero = self.codomain().zero()
        for relation in domain.relations():
            if self._presentation_map(relation) != zero:
                raise ValueError("relations do not all map to zero under the stated algebra-generator images")

    def algebra_generator_morphism(self):
        return SetMorphism(
            Sets().Mor(self.domain().algebra_generating_set(), self.codomain()),
            self._generator_images.value,
        )

    def algebra_generator_images(self):
        return self._generator_images

    def corestrict_to_center(self):
        r"""Factor this algebra morphism through the represented centre of its codomain."""
        return _corestrict_algebra_morphism_to_center(self)

    def _call_(self, element):
        return self._presentation_map(self.domain().lift_to_presentation(element))

    def __call__(self, element):
        return self._call_(element)

    def _richcmp_(self, other, op):
        r"""Decide equality on the chosen algebra generators of the source.

        A morphism out of a presented algebra is determined by the images of
        those generators: its map from the presentation algebra is determined
        there, and the quotient projection is surjective.
        """
        from sage.structure.richcmp import op_EQ, op_NE

        if op not in (op_EQ, op_NE):
            return NotImplemented
        if not isinstance(other, PresentedAlgebraMorphism) or other.parent() is not self.parent():
            return op == op_NE
        if self is other:
            return op == op_EQ
        equal = self._generator_images == other._generator_images
        return equal if op == op_EQ else not equal

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        if other.domain() not in FramedAlgebras(other.domain().base_ring()):
            return NotImplemented
        return (Algebras(other.domain().base_ring()).Associative().Unital().Mor(other.domain(), self.codomain()))(
            lambda label: self(other(other.domain().algebra_generator(label)))
        )


class _AlgebraHomsetCommonMethods:
    r"""Shared equality protocol for represented algebra Hom parents."""

    def _from_degree_preserving_generator_map(self, images):
        r"""Construct from a structurally degree-preserving generator map."""
        return self(images)


def _corestrict_algebra_morphism_to_center(morphism):
    r"""Return the unique represented ring-map factor ``A -> Z(B)`` of ``morphism``.

    The source must carry a chosen algebra generating family, because centrality
    is verified on that family.  Scalars already land centrally because
    ``morphism`` is an algebra map, so checking the selected algebra generators
    proves that its whole image lies in ``Z(B)``.  The factor is returned in the
    owned ring Hom category, matching the mathematical codomain ``ring_center``
    rather than requiring that the predicate centre carry a second algebra
    presentation.
    """
    domain = morphism.domain()
    codomain = morphism.codomain()
    base = domain.base_ring()
    assert domain in FramedAlgebras(base), (
        "corestriction to the centre requires a chosen algebra generating set of the source"
    )
    labels = domain.algebra_generating_set()
    assert labels.cardinality().is_finite(), (
        "corestriction to the centre requires finitely many selected algebra generators"
    )
    center = codomain.ring_center()
    for label in labels:
        image = morphism(domain.algebra_generator(label))
        if image not in center:
            raise ValueError(f"the image of algebra generator {label} is not central in {codomain}")
    return domain.Mor(center)(lambda element: center(morphism(element)))


class PresentedAlgebraHomset(_AlgebraHomsetCommonMethods, CategoricalHomset):
    Element = PresentedAlgebraMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        CategoricalHomset.__init__(
            self,
            hom_family,
            domain,
            codomain,
        )

    def _element_constructor_(self, images):
        return self.element_class(self, images)

    @cached_method
    def identity(self):
        r"""Return the identity of this endomorphism Hom.

        The identity of an object needs no framing: an unframed algebra such as
        the integers regarded over themselves has no algebra generating set,
        and its identity is still the identity.  A Hom object has one identity,
        so this is cached.
        """
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined on an endomorphism homset")
        domain = self.domain()
        if domain in FramedAlgebras(domain.base_ring()):
            return self(lambda label: domain.algebra_generator(label))
        engine = _engine_ring(domain)
        return self(engine.hom(engine))


class AlgebraHomset(_AlgebraHomsetCommonMethods, CategoricalHomset):
    Element = AlgebraMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        CategoricalHomset.__init__(
            self,
            hom_family,
            domain,
            codomain,
        )

    def _element_constructor_(self, images):
        return self.element_class(self, images)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined on an endomorphism homset")
        algebra = self.domain()
        return self(algebra.module_category().Mor(algebra, algebra).identity())

    def _repr_(self):
        return f"Mor_Alg({self.domain()}, {self.codomain()})"


class _OwnedAlgebraElement(_OwnedRingElement):
    r"""Engine-backed owned algebra element with ring multiplication syntax."""

    def __mul__(self, other):
        return _OwnedRingElement.__mul__(self, other)

    def __rmul__(self, other):
        return _OwnedRingElement.__rmul__(self, other)


class _OwnedAlgebraParent(_OwnedRingParent):
    r"""One ring read as an algebra through one specified scalar map."""

    Element = _OwnedAlgebraElement

    def __init__(
        self,
        engine,
        base_ring,
        labels,
        structure_map=None,
        generator_values=None,
        *,
        categories=(),
        construction_data=(),
    ) -> None:
        base = _owned_ring(base_ring)
        for name, value in construction_data:
            setattr(self, name, value)
        self._algebra_structure_construction = AlgebraStructureConstruction(base, structure_map)
        self._preamble_algebra_generating_set = None if labels is None else finite_ordered_set(labels)
        placement = [Algebras(base).Associative().Unital(), OwnedAlgebras(base)]
        if engine in SageCommutativeAlgebras(_engine_ring(base)):
            placement.append(Algebras(base).Associative().Unital().Commutative())
        if labels is not None:
            placement.append(FramedAlgebras(base))
        placement.extend(categories)
        _OwnedRingParent.__init__(
            self,
            engine,
            base=base,
            category=Cat().meet(tuple(placement)),
        )
        if labels is None:
            if generator_values is not None:
                raise ValueError("an unframed algebra cannot carry framed generator values")
            self._preamble_algebra_generator_values = None
            if self.is_commutative() is True:
                refine(self, [Algebras(self).Associative().Unital().Commutative()])
            return

        selected_labels = self._preamble_algebra_generating_set
        label_size = selected_labels.cardinality()
        if not label_size.is_finite():
            raise TypeError("an engine-backed framed algebra requires a finite backend generator set")

        if generator_values is None:

            def value(label):
                position = int(selected_labels.ranking_map()(label))
                return self._from_engine_element(engine.gen(position))
        else:
            if hasattr(generator_values, "index_set") and callable(getattr(generator_values, "value", None)):
                if generator_values.cardinality() != label_size:
                    raise ValueError("the number of algebra-generator values must equal the framing size")

                def value(label):
                    return self(generator_values.value(selected_labels.ranking_map()(label)))
            elif callable(generator_values):

                def value(label):
                    raw = generator_values(label)
                    return raw if getattr(raw, "parent", lambda: None)() is self else self._from_engine_element(raw)
            elif isinstance(generator_values, (tuple, list)):
                if len(generator_values) != int(label_size.finite_value()):
                    raise ValueError("the number of algebra-generator values must equal the framing size")
                # Explicit finite ingress is parsed by position; the Python
                # sequence is not retained as the mathematical family.
                by_position = {position: generator_values[position] for position in range(len(generator_values))}

                def value(label):
                    raw = by_position[int(selected_labels.ranking_map()(label))]
                    return raw if getattr(raw, "parent", lambda: None)() is self else self._from_engine_element(raw)
            else:
                raise TypeError("algebra-generator values are a callable/indexed family or explicit finite ingress")

        self._preamble_algebra_generator_values = indexed_family(
            selected_labels,
            value,
            name=f"Algebra generator values of {self}",
        )
        if self.is_commutative() is True:
            refine(self, [Algebras(self).Associative().Unital().Commutative()])


@cached_function
def _owned_algebra_view(
    engine,
    base_ring,
    labels=None,
    categories=(),
    construction_data=(),
):
    base = _owned_ring(base_ring)
    return _OwnedAlgebraParent(
        engine,
        base,
        labels,
        categories=tuple(categories),
        construction_data=tuple(construction_data),
    )


def _refine_algebra(
    algebra,
    base_ring,
    labels=None,
    *categories,
    construction_data=(),
):
    r"""Construct an owned algebra view with its selected categories present."""
    base = _owned_ring(base_ring)
    return _owned_algebra_view(
        _engine_ring(algebra),
        base,
        labels,
        tuple(categories),
        tuple(construction_data),
    )


@cached_function(key=lambda ring, structure_map: (id(ring), id(structure_map)))
def _algebra_structure_view(ring, structure_map):
    r"""Return ``ring`` read as an algebra through the explicit map ``R -> ring``.

    The view is a scalar-structure object, not a second authoritative ring.
    Its elements use the same private computation ring while its owned algebra
    structure morphism has the exact supplied source and the view itself as
    codomain.  This is the construction needed when a ring acquires a new
    scalar structure by a universal property, for example an overlap
    localization regarded as an algebra over the overlap section ring.
    """
    selected_ring = _own_ring(ring)
    if structure_map.codomain() is not selected_ring:
        raise ValueError("an algebra-structure view requires a ring map into the selected ring")
    base = _own_ring(structure_map.domain())
    view = _OwnedAlgebraParent(_engine_ring(selected_ring), base, None)
    view.algebra_structure_construction().set_structure_map(
        base.Mor(view)(lambda scalar: view(structure_map(base(scalar))))
    )
    view._preamble_algebra_structure_ring = selected_ring
    return view


def _unit_from_multiplication(multiplication):
    from sage.matrix.constructor import matrix as sage_matrix
    from sage.modules.free_module_element import vector as sage_vector

    module = multiplication.codomain()
    tensor_square = multiplication.domain()
    labels = module.module_generating_set()
    size = labels.cardinality()
    if not size.is_finite():
        raise TypeError("a unit is recovered from a finite module generating set")
    ring = module.base_ring()
    engine = _engine_ring(ring)
    rank = int(size.finite_value())

    # Private finite linear-system serialization.  The mathematical basis stays
    # the owned ordered framing ``labels``; only this backend array is concrete.
    system_entries = [[engine.zero() for _ in range(rank)] for _ in range(rank * rank)]
    target_entries = [engine.zero() for _ in range(rank * rank)]
    for right_index in range(rank):
        right_label = labels[right_index]
        target_entries[right_index * rank + right_index] = engine.one()
        for left_index in range(rank):
            left_label = labels[left_index]
            product = multiplication(
                tensor_square.pure_tensor(
                    module.module_generator(left_label),
                    module.module_generator(right_label),
                )
            )
            coefficients = module.framing_coefficients(product)
            for out_index in range(rank):
                out_label = labels[out_index]
                system_entries[right_index * rank + out_index][left_index] = _engine_element(ring, coefficients.get(out_label, ring.zero()))
    system = sage_matrix(engine, rank * rank, rank, system_entries)
    target = sage_vector(engine, target_entries)
    try:
        coefficients = system.solve_right(target)
    except (ValueError, ArithmeticError) as error:
        raise TypeError("the multiplication morphism has no left unit") from error
    unit = module.linear_combination({labels[index]: ring._from_engine_element(engine(coefficients[index])) for index in range(rank) if coefficients[index]})
    for label in labels:
        generator = module.module_generator(label)
        if multiplication(tensor_square.pure_tensor(generator, unit)) != generator:
            raise TypeError("the multiplication morphism has no two-sided unit")
    return unit


def _multiplication_is_commutative(multiplication) -> bool:
    module = multiplication.codomain()
    tensor = multiplication.domain()
    labels = module.module_generating_set()
    for left in labels:
        for right in labels:
            left_element = module.module_generator(left)
            right_element = module.module_generator(right)
            if multiplication(tensor.pure_tensor(left_element, right_element)) != multiplication(tensor.pure_tensor(right_element, left_element)):
                return False
    return True



@cached_function
def _own_algebra(structure_map):
    r"""Return the algebra object presented by the supplied ring map."""
    if not isinstance(structure_map, Map):
        raise TypeError("an algebra is presented by a ring map")
    base = _owned_ring(structure_map.domain())
    engine = _engine_ring(structure_map.codomain())
    algebra = _OwnedAlgebraParent(engine, base, None, structure_map)
    return algebra


def _engine_algebra_morphism_from_generator_images(domain, codomain, generator_images):
    r"""Realize a framed owned algebra map in Sage when both engines exist.

    This is a private bridge boundary.  The mathematical datum is the owned
    generator map; Sage receives only engine endpoints and engine elements.
    """
    engine_domain = _engine_ring(domain)
    engine_codomain = _engine_ring(codomain)
    assert engine_domain in SageRings() and engine_codomain in SageRings(), (
        "the private Sage algebra-morphism realization requires native Sage ring endpoints"
    )
    labels = domain.algebra_generating_set()
    assert labels.cardinality().is_finite(), (
        "the private Sage algebra-morphism realization requires a finite generator framing"
    )

    base = domain.base_ring()
    engine_base = _engine_ring(base)
    target_structure = codomain._ring_morphism_defining_algebra_structure()

    def engine_base_image(scalar):
        owned_scalar = base._from_engine_element(engine_base(scalar))
        return _engine_element(codomain, target_structure(owned_scalar))

    if codomain is base and engine_codomain is engine_base:
        # An R-algebra morphism A -> R is over the literal identity of R.
        # Keep that theorem visible to Sage's quotient-Hom verifier instead of
        # wrapping id_R as an opaque set map whose multiplicativity Sage cannot
        # certify when checking the defining relations.
        base_map = engine_base.hom(engine_base)
    else:
        native_base_map = engine_codomain.coerce_map_from(engine_base)
        if native_base_map is not None:
            try:
                determining_scalars = (
                    engine_base.one(),
                    *tuple(engine_base.gens()),
                )
                native_matches_owned = all(native_base_map(scalar) == engine_base_image(scalar) for scalar in determining_scalars)
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                native_matches_owned = False
        else:
            native_matches_owned = False
        base_map = (
            native_base_map
            if native_matches_owned
            else SetMorphism(
                engine_base.Hom(engine_codomain),
                engine_base_image,
            )
        )
    engine_generator_images = {label: _engine_element(codomain, codomain(image)) for label, image in generator_images.items()}

    scalar_labels_method = getattr(domain, "restricted_scalar_generator_labels", None)
    algebra_labels_method = getattr(domain, "restricted_algebra_generator_labels", None)
    if scalar_labels_method is not None and algebra_labels_method is not None:
        scalar_labels = tuple(domain.restricted_scalar_generator_labels())
        algebra_labels = tuple(domain.restricted_algebra_generator_labels())
        extension_engine = _engine_ring(domain.extension_ring())
        extension_map = _engine_morphism_from_generator_images(
            extension_engine,
            engine_codomain,
            [engine_generator_images[("scalar", label)] for label in scalar_labels],
            base_map,
        )
        return _engine_morphism_from_generator_images(
            engine_domain,
            engine_codomain,
            [engine_generator_images[("algebra", label)] for label in algebra_labels],
            extension_map,
        )

    if domain in AlgebrasWithChosenFinitePresentation(base):
        try:
            engine_labels = tuple(engine_domain.gens())
            selected_size = int(labels.cardinality().finite_value())
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            engine_labels = ()
            selected_size = -1
        if engine_labels and len(engine_labels) != selected_size:
            # A maintained private realization may introduce coefficient or
            # inverse variables that are not algebra generators of the owned
            # presentation.  Recover the image of each such engine generator
            # by lifting it through the selected presentation and evaluating
            # that lift under the actual R-algebra map.  This preserves the
            # chosen presentation while supplying Sage the complete generator
            # family its quotient engine requires.
            presentation = domain.presentation_ring()
            presentation_engine = _engine_ring(presentation)
            presentation_map = _engine_morphism_from_generator_images(
                presentation_engine,
                engine_codomain,
                [engine_generator_images[label] for label in labels],
                base_map,
            )
            private_images = []
            for engine_generator in engine_labels:
                owned_generator = domain._from_engine_element(engine_generator)
                selected_lift = domain.lift_to_presentation(owned_generator)
                private_images.append(presentation_map(_engine_element(presentation, selected_lift)))
            return engine_domain.hom(
                private_images,
                engine_codomain,
            )

    return _engine_morphism_from_generator_images(
        engine_domain,
        engine_codomain,
        [engine_generator_images[label] for label in labels],
        base_map,
    )


def _engine_algebra_morphism(morphism):
    r"""Return a private Sage realization of an owned algebra morphism.

    Bridge consumers such as affine ``Spec`` use this function.  It is not a
    public method on the mathematical morphism.
    """
    if isinstance(morphism, AlgebraMorphism) and morphism._engine_morphism is not None:
        return morphism._engine_morphism
    domain = morphism.domain()
    assert domain in FramedAlgebras(domain.base_ring()), (
        "a private Sage realization of an owned algebra morphism requires a selected algebra generating family"
    )
    images = {label: morphism(domain.algebra_generator(label)) for label in domain.algebra_generating_set()}
    return _engine_algebra_morphism_from_generator_images(domain, morphism.codomain(), images)


def _engine_morphism_from_generator_images(engine_domain, engine_codomain, images, base_map):
    r"""Construct a native Sage ring morphism at the engine boundary."""
    assert engine_domain in SageRings() and engine_codomain in SageRings(), (
        "a native engine ring morphism requires native Sage ring endpoints"
    )
    return engine_domain.hom(
        [engine_codomain(image) for image in images],
        engine_codomain,
        base_map=base_map,
    )


__all__ = [
    "AlgebraHomset",
    "AlgebraMorphism",
    "Algebras",
    "AlgebrasWithChosenFinitePresentation",
    "AlgebrasWithChosenMultiplication",
    "AssociativeAlgebrasWithChosenMultiplication",
    "CommutativeAlgebraCoproducts",
    "CommutativeAlgebraPushouts",
    "FinitelyPresentedAlgebras",
    "FramedAlgebras",
    "OwnedAlgebras",
]
