r"""Algebras over a commutative ring, their axioms, and their data subcategories.

Let \(R\) be a commutative ring.  An \(R\)-algebra is an \(R\)-module \(M\)
together with an \(R\)-bilinear multiplication, that is an \(R\)-linear map
\(m\colon M\otimes_R M\to M\) (Bourbaki, *Algebra* III §1.1).  The pair
\((M, m)\) is the whole structure.  The structure morphism \(\rho\) is the
scalar action of \(M\); associativity, a unit, commutativity and the Lie
identities are axioms above the root, and a Lie bracket is the multiplication
of its algebra.

``Algebras(R)(M, m)`` is the one entry (``CON-16``).  Every other route -- an
axiom entry, the centre, a quotient, the commutator Lie algebra, a group
algebra -- computes \((M, m)\) and reaches the same construction,
:func:`_algebra_on_module`.
"""

import itertools
from functools import reduce

from sage.categories.category_with_axiom import all_axioms
from sage.categories.commutative_algebras import (
    CommutativeAlgebras as SageCommutativeAlgebras,
)
from sage.categories.map import Map
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.rings import Rings as SageRings
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.unknown import Unknown
from sage.structure.element import parent as element_parent

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
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FramedFreeModules,
)
from dzack_research.preamble.categories.modules.general_modules import GeneralModules
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    BilinearMap,
    FramedModules,
    MatrixEndomorphismSpaces,
    Modules,
    ModulesWithChosenFinitePresentation,
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
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import EnumeratedSets, Sets
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom
from dzack_research.preamble.refine import refine

if "Lie" not in all_axioms:
    all_axioms.add("Lie")

# Qualified as Sage qualifies ``FinitelyGeneratedAsMagma``: an axiom name is
# global and propagates to every declared supercategory defining it, and a
# finitely presented algebra is not a finitely presented module.
if "FinitelyPresentedAsAlgebra" not in all_axioms:
    all_axioms.add("FinitelyPresentedAsAlgebra")


# ---------------------------------------------------------------------------
# The algebra Hom: linear maps preserving the multiplication.
# ---------------------------------------------------------------------------


class MultiplicativeAlgebraMorphism(Morphism):
    r"""An algebra morphism: an ``R``-linear \(f\colon A\to B\) with \(f\,m_A = m_B\,(f\otimes f)\).

    The datum is the linear map, an element of the module Hom.  The defining
    equation is one equation between two module morphisms out of
    \(A\otimes_R A\), asked of the module Hom: it decides on a chosen finite
    presentation of \(A\otimes_R A\) and answers ``Unknown`` otherwise.  A map
    for which it answers ``False`` is refused; ``Unknown`` is recorded as the
    hypothesis the arrow is stated under (``CON-16``, ``DEV-52``).
    """

    def __init__(self, parent, underlying_morphism) -> None:
        Morphism.__init__(self, parent)
        domain = self.domain()
        codomain = self.codomain()
        linear = domain.module_category().Mor(domain, codomain)(underlying_morphism)
        source_multiplication = domain.multiplication_morphism()
        target_multiplication = codomain.multiplication_morphism()
        tensor_square = linear.tensor_product_map(
            linear,
            source=source_multiplication.domain(),
            target=target_multiplication.domain(),
        )
        preserved = linear * source_multiplication == target_multiplication * tensor_square
        assert preserved is not False, "the stated linear map does not preserve the multiplication"
        self._underlying_morphism = linear
        self._tensor_square_morphism = tensor_square
        self._preserves_multiplication = preserved

    def underlying_morphism(self):
        r"""The linear map this algebra morphism is, in the module Hom."""
        return self._underlying_morphism

    def tensor_square_morphism(self):
        r"""\(f\otimes f\colon A\otimes_R A\to B\otimes_R B\)."""
        return self._tensor_square_morphism

    def is_multiplicative(self):
        r"""``True`` when \(f\,m_A = m_B\,(f\otimes f)\) was decided, ``Unknown`` when it is the stated hypothesis."""
        return self._preserves_multiplication

    def corestrict_to_center(self):
        r"""Factor this algebra morphism through the represented centre of its codomain."""
        return _corestrict_algebra_morphism_to_center(self)

    @cached_method
    def cokernel(self):
        r"""The algebra cokernel: the quotient by the ideal the image generates.

        The image of the underlying linear map need not be an ideal, which is
        the difference from the module cokernel; for Lie algebras it is the
        quotient by the Lie ideal the image generates.
        """
        image = self.underlying_morphism().image()
        return self.codomain().quotient_by_generated_algebra_ideal(image)

    @cached_method
    def cokernel_projection(self):
        r"""The multiplication-preserving quotient map onto ``coker(self)``."""
        quotient = self.cokernel()
        category = self.parent().homset_category()
        return category.Mor(self.codomain(), quotient)(quotient.algebra_quotient_projection())

    def _call_(self, element):
        return self.codomain()(self.underlying_morphism()(self.domain()(element)))

    def __eq__(self, other) -> bool:
        match element_parent(other):
            case parent if parent is self.parent():
                return self.underlying_morphism() == other.underlying_morphism()
            case _:
                return False

    def __ne__(self, other) -> bool:
        return not self == other

    __hash__ = None

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        category = self.parent().homset_category()
        forget = Algebras(self.domain().algebra_base_ring()).underlying_module()
        return category.Mor(other.domain(), self.codomain())(self.underlying_morphism() * forget(other))


class MultiplicativeAlgebraHomset(CategoricalHomset):
    r"""``Hom_{R-Alg}(A, B)``: the linear maps preserving the multiplication."""

    Element = MultiplicativeAlgebraMorphism

    def __call__(self, datum):
        return self._element_constructor_(datum)

    def _element_constructor_(self, datum):
        # The one boundary admitting data this Hom did not build.  An arrow of
        # an algebra Hom with these endpoints is admitted by the linear map the
        # forgetful functor reads it as; any other datum states the linear map.
        parent = element_parent(datum)
        if parent is self:
            return datum
        algebras = Algebras(self.domain().algebra_base_ring())
        match parent:
            case CategoricalHomset() if parent.homset_category().is_subcategory(algebras):
                datum = algebras.underlying_module()(datum)
            case _:
                pass
        return self.element_class(self, datum)

    def identity(self):
        assert self.domain() is self.codomain(), "the identity is an endomorphism"
        algebra = self.domain()
        return self(algebra.module_category().Mor(algebra, algebra).identity())

    def _repr_(self):
        return f"Mor_Alg({self.domain()}, {self.codomain()})"


class UnitalMultiplicativeAlgebraMorphism(MultiplicativeAlgebraMorphism):
    r"""A morphism of unital algebras: multiplicative and \(f(1) = 1\)."""

    def __init__(self, parent, underlying_morphism) -> None:
        super().__init__(parent, underlying_morphism)
        assert self(self.domain().one()) == self.codomain().one(), "the stated linear map does not preserve the unit"


class UnitalMultiplicativeAlgebraHomset(MultiplicativeAlgebraHomset):
    r"""``Hom`` of unital algebras: the multiplicative linear maps preserving the unit."""

    Element = UnitalMultiplicativeAlgebraMorphism

    def _repr_(self):
        return f"Mor_UnitalAlg({self.domain()}, {self.codomain()})"


class AlgebraHomCategoryConstruction(HomCategoryConstruction):
    r"""The fixed-endpoint Hom categories of ``R``-algebras: linear maps preserving the multiplication.

    An axiom that adds no condition on morphisms -- associativity,
    commutativity, the Lie identities -- shares this Hom object.
    """

    FixedCategoryClass = MultiplicativeAlgebraHomset


class UnitalAlgebraHomCategoryConstruction(HomCategoryConstruction):
    r"""The fixed-endpoint Hom categories of unital ``R``-algebras: the unit is preserved too.

    The domain names the parent realizing this Hom.  An algebra stated by
    ``(M, m)`` takes the linear maps preserving product and unit; a data
    subcategory whose objects state their maps on further data -- algebra
    generators, a chosen presentation -- names its realization of the same
    morphisms.
    """

    def fixed_category_class_for(self, domain, codomain):
        return domain._algebra_homset_class()


# ---------------------------------------------------------------------------
# Units and the tensor square.
# ---------------------------------------------------------------------------


def _scalar_module(ring):
    r"""\(U_R(R)\): the ring as the module over itself, the domain of every unit map."""
    ring = _owned_ring(ring)
    return Algebras(ring).underlying_module()(ring)


def _unit_morphism_from_element(module, unit, ring):
    r"""The linear map ``U_R(R) -> module`` determined by ``1 |-> unit``."""
    ring = _owned_ring(ring)
    scalar_module = _scalar_module(ring)
    return ModuleMorphism(
        scalar_module.module_category().Mor(scalar_module, module),
        lambda scalar: module.scalar_multiple(ring(scalar), unit),
        elementwise=True,
    )


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


# ---------------------------------------------------------------------------
# Identities of a multiplication, decided on module generators.
# ---------------------------------------------------------------------------


def _product_on(multiplication):
    r"""``(x, y) |-> m(x (x) y)`` for ``m: M (x)_R M -> M``."""
    tensor = multiplication.domain()

    def product(left, right):
        return multiplication(tensor.pure_tensor(left, right))

    return product


def _decide_on_module_generators(module, identity, arity):
    r"""Decide an ``R``-multilinear identity on tuples of module generators of ``module``.

    Both sides of every identity decided here are ``R``-multilinear in their
    arguments, so agreement on each tuple of module generators is agreement on
    all of ``module``.  A module stating no finite framing leaves the identity
    ``Unknown``: it is not enumerated (``DEV-52``).
    """
    ring = module.base_ring()
    match module:
        case _ if module in FramedModules(ring) and module.module_generating_set().cardinality().is_finite():
            labels = module.module_generating_set()
            return all(
                identity(*(module.module_generator(label) for label in labels_tuple))
                for labels_tuple in itertools.product(labels, repeat=arity)
            )
        case _:
            return Unknown


def _associativity(multiplication):
    product = _product_on(multiplication)
    return lambda x, y, z: product(product(x, y), z) == product(x, product(y, z))


def _commutativity(multiplication):
    product = _product_on(multiplication)
    return lambda x, y: product(x, y) == product(y, x)


def _alternation(multiplication):
    r"""``[x, x] = 0`` on generators and ``[x, y] + [y, x] = 0`` on pairs: alternation of a bilinear map."""
    product = _product_on(multiplication)
    zero = multiplication.codomain().zero()
    return lambda x, y: product(x, x) == zero and product(x, y) + product(y, x) == zero


def _jacobi_identity(multiplication):
    product = _product_on(multiplication)
    zero = multiplication.codomain().zero()
    return lambda x, y, z: product(x, product(y, z)) + product(y, product(z, x)) + product(z, product(x, y)) == zero


def _two_sided_unit(multiplication, unit):
    product = _product_on(multiplication)
    return lambda x: product(unit, x) == x and product(x, unit) == x


def _assert_decided(held, statement, module):
    r"""An axiom entry places an algebra only on an identity it decided to hold."""
    assert held is not False, f"{statement} fails for the stated multiplication on {module}"
    assert held is True, (
        f"{statement} of the stated multiplication on {module} is undecided: "
        "the module states no finite framing on which to decide it"
    )


# ---------------------------------------------------------------------------
# The category of algebras.
# ---------------------------------------------------------------------------


class Algebras(OwnedCategoryOverBaseRing):
    r"""Algebras over a commutative ring ``R``: an ``R``-module with an ``R``-bilinear multiplication.

    The defining datum is the pair ``(M, m)``, ``m: M (x)_R M -> M``, and
    ``Algebras(R)(M, m)`` is the one entry.  The algebra is built on the data
    of ``M``, retains ``M`` as ``unformed_module()`` and ``m`` as
    ``multiplication()``, and its elements pass to and from ``M`` by
    coercion.  A unit, associativity, commutativity and the Lie identities are
    axioms above this node.
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
            r"""Return the refinement with a two-sided unit."""
            return self._with_axiom("Unital")

        def Commutative(self):
            r"""Return the refinement satisfying ``xy=yx``."""
            return self._with_axiom("Commutative")

        def Lie(self):
            r"""Return the refinement whose multiplication is a Lie bracket."""
            return self._with_axiom("Lie")

    def Mor(self, domain, codomain):
        r"""Return the unique Hom-set ``Hom_{R-Alg}(domain,codomain)``."""
        if domain not in self or codomain not in self:
            raise TypeError("an R-algebra Hom requires two R-algebras")
        return self.HomCategory().Of(domain, codomain)

    _HomCategory = AlgebraHomCategoryConstruction

    def _call_(self, module, multiplication):
        r"""The algebra on ``M`` with multiplication ``m: M (x)_R M -> M``: the one entry.

        No identity of ``m`` is assumed or placed here; the axiom entries
        ``Associative()``, ``Unital()``, ``Commutative()`` and ``Lie()`` place
        an algebra on the identities they decide.
        """
        assert module.base_ring() is self.base_ring(), f"an algebra over {self.base_ring()} is stated on a module over it"
        return _algebra_on_module(module, multiplication, placement=(self,))

    class ElementMethods:
        def _mul_(self, other):
            r"""``x * y`` is the multiplication evaluated on ``x (x) y`` in the module it is stated on.

            Elements pass to that module and back by coercion.
            """
            algebra = self.parent()
            module = algebra.unformed_module()
            product = _product_on(algebra.multiplication())
            return algebra(product(module(self), module(other)))

    class ParentMethods:
        def __init__(self, unformed_module, multiplication, **rest) -> None:
            r"""Retain the defining datum ``(M, m)``; the levels below build the module on the data of ``M``."""
            self._preamble_unformed_module = unformed_module
            self._preamble_multiplication = multiplication
            super().__init__(**rest)

        def unformed_module(self):
            r"""The module ``M`` this algebra is built on, retained by ``Algebras(R)(M, m)``."""
            return self._preamble_unformed_module

        def _element_of_unformed_module(self, element):
            r"""The element of :meth:`unformed_module` on the data of ``element``.

            ``Algebras(R)(M, m)`` builds on the framing of ``M`` when ``M``
            has one, so an element reads there with the same coefficients;
            otherwise it builds on the underlying additive group of ``M``, and
            an element reads there as its underlying additive element.
            """
            module = self.unformed_module()
            match self:
                case _ if self in FramedModules(self.algebra_base_ring()):
                    return module.linear_combination(self.framing_coefficients(element))
                case _:
                    return module(self._underlying_additive_element(element))

        def _element_from_unformed_module(self, element):
            r"""The element of this algebra on the data of an element of :meth:`unformed_module`."""
            module = self.unformed_module()
            match self:
                case _ if self in FramedModules(self.algebra_base_ring()):
                    return self.linear_combination(module.framing_coefficients(element))
                case _:
                    return self(module.underlying_additive_group()(element))

        def multiplication(self):
            r"""The multiplication ``m: M (x)_R M -> M`` this algebra was stated with."""
            return self._preamble_multiplication

        @cached_method
        def multiplication_morphism(self):
            r"""The multiplication read on this algebra, ``A (x)_R A -> A``.

            Elements of this algebra and of ``M`` pass by coercion, so on two
            module generators ``a, b`` of ``A`` the map is
            ``A(m(M(a) (x) M(b)))``, and bilinearity determines the rest.  The
            module layer represents maps out of ``A (x)_R A`` on module
            generators, so this reads the framing of ``A``.
            """
            ring = self.algebra_base_ring()
            assert self in FramedModules(ring), (
                f"the multiplication of {self} is read on A (x) A through a module framing of A, and {self} states none"
            )
            module = self.unformed_module()
            product = _product_on(self.multiplication())
            tensor = _algebra_tensor_square_functor(ring)(self)
            return tensor.from_bilinear(
                BilinearMap(
                    self,
                    self,
                    self,
                    lambda left, right: self(
                        product(
                            module(self.module_generator(left)),
                            module(self.module_generator(right)),
                        )
                    ),
                )
            )

        @cached_method
        def algebra_structure_morphism(self):
            r"""The structure morphism \(\rho\) of this \(R\)-algebra.

            Over commutative \(R\), \(\rho\colon R\to\operatorname{End}(A)\) is
            the scalar action of the underlying module: \(\rho(r)\) commutes
            with left and right multiplication by bilinearity, so it lies in
            the centroid of \(A\).  On a unital associative algebra the
            centroid is the centre through \(\varphi\mapsto\varphi(1)\), and
            the structure morphism is the ring map \(R\to Z(A)\),
            \(r\mapsto\rho(r)(1)\), computed here from \(\rho\).
            """
            ring = self.algebra_base_ring()
            rho = self.scalar_action()
            match self:
                case _ if self in Algebras(ring).Associative().Unital():
                    center = self.ring_center()
                    unit = self._underlying_additive_element(self.one())
                    return ring.Mor(center)(
                        lambda scalar: center(self(rho(ring(scalar))(unit))),
                    )
                case _:
                    return rho

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
            r"""Whether ``xy = yx``: decided on module generators of ``M`` against ``m``, else ``Unknown``.

            Commutativity is a property of the multiplication before it is a
            refinement; the ``Commutative`` axiom answers ``True`` by placement.
            """
            multiplication = self.multiplication()
            return _decide_on_module_generators(
                self.unformed_module(),
                _commutativity(multiplication),
                2,
            )

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
            return Algebras(self.algebra_base_ring()).underlying_module()(self)

        def Mor(self, codomain, category=None):
            base = self.algebra_base_ring()
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
            r"""The centre \(Z(A)=\{z : zx = xz\ \text{for all}\ x\}\).

            Left and right multiplication by \(b\) are \(R\)-linear, so
            \(Z(A)\) is the intersection, over the module generators \(b\) of
            \(A\), of the equalizers of \(x\mapsto xb\) and \(x\mapsto bx\),
            computed in \(R\)-modules.  For an associative \(A\) the centre is
            closed under the product and is the commutative associative algebra
            on that submodule; otherwise it is the submodule.
            """
            ring = self.algebra_base_ring()
            labels = self.module_generating_set()
            assert labels.cardinality().is_finite(), (
                f"the centre of {self} is computed as a finite intersection of equalizers over its module generators, and its module framing is infinite"
            )
            endomorphisms = self.module_category().Mor(self, self)
            modules = Modules(ring)

            def commutation_equalizer(label):
                element = self.module_generator(label)
                left = endomorphisms(lambda other: self.module_generator(other) * element)
                right = endomorphisms(lambda other: element * self.module_generator(other))
                return modules.equalizer(left, right)

            identity = endomorphisms.identity()
            submodule = reduce(
                lambda central, label: central.intersection(commutation_equalizer(label)),
                labels,
                modules.equalizer(identity, identity),
            )
            match self:
                case _ if self in Algebras(ring).Associative():
                    return _center_algebra(self, submodule)
                case _:
                    return submodule

        def center_inclusion(self):
            r"""The inclusion \(Z(A)\hookrightarrow A\).

            The centre of an associative algebra is built on a submodule of
            \(A\): an element of the centre passes to that submodule by
            coercion and then along the submodule's inclusion.
            """
            center = self.center()
            match center:
                case _ if center in Algebras(self.algebra_base_ring()):
                    submodule = center.unformed_module()
                    inclusion = submodule.inclusion()
                    return center.module_category().Mor(center, self).elementwise(
                        lambda element: inclusion(submodule(element)),
                        verify_linearity=False,
                    )
                case _:
                    return center.inclusion()

        def algebra_ideal_generated_by(self, subobject):
            r"""The two-sided algebra ideal generated by a submodule ``I``.

            The ideal is the smallest submodule containing ``I`` and closed
            under left and right multiplication by module generators of
            \(A\).  Starting from ``I``, adjoin the products of the generators
            of the current submodule with the module generators of \(A\) on
            both sides.  Over a field a strictly ascending chain of subspaces
            of a finite-dimensional algebra has at most ``dim A`` steps, so
            the closure is reached exactly.
            """
            ring = self.algebra_base_ring()
            assert ring in OwnedFields(), (
                "algebra-ideal closure is represented here for finite-dimensional algebras over fields"
            )
            assert subobject.inclusion().codomain() is self, "an algebra ideal is generated by a submodule of the algebra"
            ambient_labels = self.module_generating_set()
            assert ambient_labels.cardinality().is_finite(), (
                "algebra-ideal closure requires a finite module framing of the algebra"
            )
            subobjects = Modules(ring).Subobjects(self)
            current = subobject
            while True:
                inclusion = current.inclusion()
                products = tuple(
                    product
                    for ideal_label in current.module_generating_set()
                    for ambient_label in ambient_labels
                    for product in (
                        self.product(self.module_generator(ambient_label), inclusion(current.module_generator(ideal_label))),
                        self.product(inclusion(current.module_generator(ideal_label)), self.module_generator(ambient_label)),
                    )
                )
                if not products:
                    return current
                enlarged = current.sum(self.subobject_on(products))
                if subobjects.leq(enlarged, current):
                    return current
                current = enlarged

        def quotient_by_algebra_ideal(self, ideal):
            r"""``A/I`` for a two-sided ideal ``I`` of ``A``.

            The module cokernel of ``I -> A`` is the quotient module; it is
            presented on the module generators of ``A``, each generator of
            ``A/I`` being the image of the generator of ``A`` of the same
            name.  The product of two such images is the image of the product
            of the generators, well defined because ``I`` is an ideal.
            Associativity, commutativity, the Lie identities and a unit
            descend to quotients, so they are stated with the construction.
            """
            ring = self.algebra_base_ring()
            assert ideal.inclusion().codomain() is self, "an algebra quotient is taken by an ideal of the algebra"
            projection = ideal.inclusion().cokernel_projection()
            quotient_module = projection.codomain()
            tensor = _algebra_tensor_square_functor(ring)(quotient_module)
            multiplication = tensor.from_bilinear(
                BilinearMap(
                    quotient_module,
                    quotient_module,
                    quotient_module,
                    lambda left, right: projection(
                        self.product(self.module_generator(left), self.module_generator(right))
                    ),
                )
            )
            algebras = Algebras(ring)
            descended = tuple(
                axiom
                for axiom in (algebras.Associative(), algebras.Commutative(), algebras.Lie())
                if self in axiom
            )
            match self:
                case _ if self in algebras.Unital():
                    return _algebra_on_module(
                        quotient_module,
                        multiplication,
                        placement=(*descended, algebras.Unital()),
                        unit=projection(self.one()),
                    )
                case _:
                    return _algebra_on_module(quotient_module, multiplication, placement=descended)

        def quotient_by_generated_algebra_ideal(self, subobject):
            r"""The quotient by the algebra ideal generated by ``subobject``."""
            ideal = self.algebra_ideal_generated_by(subobject)
            return self.quotient_by_algebra_ideal(ideal)

        def algebra_quotient_projection(self):
            r"""The projection ``A -> A/I`` of an algebra built as ``A.quotient_by_algebra_ideal(I)``, as a linear map.

            That algebra is built on the module cokernel of ``I -> A``, which
            retains its projection; the projection passes to this algebra by
            coercion.
            """
            projection = self.unformed_module().cokernel_projection()
            ambient = projection.domain()
            return ambient.module_category().Mor(ambient, self).elementwise(
                lambda element: self(projection(element)),
                verify_linearity=False,
            )

        def algebra_quotient_ideal(self):
            r"""The ideal ``I`` of an algebra built as ``A.quotient_by_algebra_ideal(I)``: the kernel of its projection."""
            return self.unformed_module().cokernel_projection().kernel()

        def _Hom_(self, codomain, category=None):
            if category is not None and not category.is_subcategory(Algebras(self.algebra_base_ring())):
                raise TypeError("this is not an algebra homset category")
            ordinary = Algebras(self.algebra_base_ring()).Associative().Unital()
            if self in ordinary and codomain in ordinary:
                return ordinary.Mor(self, codomain)
            return Algebras(self.algebra_base_ring()).Mor(self, codomain)

    class Associative(CategoryWithAxiom):
        r"""Algebras whose multiplication is associative."""

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

        def _call_(self, module, multiplication):
            r"""The associative algebra on ``(M, m)``: ``(xy)z = x(yz)`` decided on module generators of ``M``."""
            _assert_decided(
                _decide_on_module_generators(module, _associativity(multiplication), 3),
                "associativity",
                module,
            )
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

            _HomCategory = UnitalAlgebraHomCategoryConstruction

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

            def _call_(self, module, multiplication, unit):
                r"""The associative unital algebra on ``(M, m)`` with unit ``1 in M``, both identities decided on module generators."""
                _assert_decided(
                    _decide_on_module_generators(module, _associativity(multiplication), 3),
                    "associativity",
                    module,
                )
                _assert_decided(
                    _decide_on_module_generators(module, _two_sided_unit(multiplication, module(unit)), 1),
                    "the two unit equations",
                    module,
                )
                return _algebra_on_module(module, multiplication, placement=(self,), unit=module(unit))

            class Commutative(CategoryWithAxiom):
                r"""Commutative associative unital ``R``-algebras."""

                _HomCategory = UnitalAlgebraHomCategoryConstruction
                SubcategoryMethods = _CommutativeUnitalAlgebraSubcategoryMethods
                ParentMethods = _CommutativeUnitalAlgebraParentMethods

                @classmethod
                def _repr_object_names(cls):
                    return "commutative algebras"

                def an_object(self):
                    modules = Modules(self.base_ring())
                    return modules.symmetric_algebra()(modules.an_object())

                def _call_(self, module, multiplication, unit):
                    r"""The commutative associative unital algebra on ``(M, m)`` with unit ``1 in M``, each identity decided on module generators."""
                    for held, statement in (
                        (_decide_on_module_generators(module, _associativity(multiplication), 3), "associativity"),
                        (_decide_on_module_generators(module, _commutativity(multiplication), 2), "commutativity"),
                        (_decide_on_module_generators(module, _two_sided_unit(multiplication, module(unit)), 1), "the two unit equations"),
                    ):
                        _assert_decided(held, statement, module)
                    return _algebra_on_module(module, multiplication, placement=(self,), unit=module(unit))

    class Lie(CategoryWithAxiom):
        r"""Algebras whose bilinear multiplication is a Lie bracket: alternating and satisfying the Jacobi identity.

        No associativity or unit is implied: the multiplication at this node
        is the bracket itself, so the algebra Hom already has the right
        morphisms, the linear maps preserving it.
        """

        @classmethod
        def _repr_object_names(cls):
            return "Lie algebras"

        def an_object(self):
            r"""``gl_2(R)``: the two-by-two matrix algebra under the commutator."""
            ring = self.base_ring()
            return Algebras(ring).Associative().commutator_lie_algebra()(
                MatrixAlgebras(ring).an_object()
            )

        def _call_(self, module, multiplication):
            r"""The Lie algebra on ``(M, m)``, ``m`` its bracket: alternation and the Jacobi identity decided on module generators."""
            _assert_decided(
                _decide_on_module_generators(module, _alternation(multiplication), 2),
                "alternation",
                module,
            )
            _assert_decided(
                _decide_on_module_generators(module, _jacobi_identity(multiplication), 3),
                "the Jacobi identity",
                module,
            )
            return _algebra_on_module(module, multiplication, placement=(self,))

        class ParentMethods:
            def bracket(self, left, right):
                return self.product(left, right)

    class Unital(CategoryWithAxiom):
        r"""Algebras with a two-sided unit, without associativity.

        The unit is unique when it exists, so this is a property.  Its
        witness, the unit ``1`` of ``M``, is decided against the
        multiplication by the entry that states it, or supplied by the
        theorem of the construction that builds the algebra, and is retained
        by the construction.
        """

        _HomCategory = UnitalAlgebraHomCategoryConstruction

        @classmethod
        def _repr_object_names(cls):
            return "unital algebras"

        def _call_(self, module, multiplication, unit):
            r"""The unital algebra on ``(M, m)`` with unit ``1 in M``, the unit equations decided on module generators."""
            _assert_decided(
                _decide_on_module_generators(module, _two_sided_unit(multiplication, module(unit)), 1),
                "the two unit equations",
                module,
            )
            return _algebra_on_module(module, multiplication, placement=(self,), unit=module(unit))

        class ParentMethods:
            def __init__(self, unit, **rest) -> None:
                r"""Retain the unit, an element of the module the multiplication is stated on."""
                self._preamble_algebra_unit = unit
                super().__init__(**rest)

            @cached_method
            def one(self):
                r"""The unit, read on this algebra by coercion from the unit of ``M``."""
                return self(self._preamble_algebra_unit)

            @cached_method
            def unit_morphism(self):
                r"""\(\eta\colon U_R(R)\to A\), \(r\mapsto\rho(r)(1)\)."""
                return _unit_morphism_from_element(self, self.one(), self.algebra_base_ring())

            def _algebra_homset_class(self):
                r"""A unital algebra stated by ``(M, m)`` takes the multiplicative unit-preserving linear maps."""
                return UnitalMultiplicativeAlgebraHomset

    class Commutative(CategoryWithAxiom):
        r"""Algebras whose multiplication is commutative."""

        @classmethod
        def _repr_object_names(cls):
            return "commutative algebras"

        def an_object(self):
            r"""A commutative product supplied by an ordinary commutative ring."""
            return Algebras(self.base_ring()).Associative().Unital().Commutative().an_object()

        def _call_(self, module, multiplication):
            r"""The commutative algebra on ``(M, m)``: ``xy = yx`` decided on module generators of ``M``."""
            _assert_decided(
                _decide_on_module_generators(module, _commutativity(multiplication), 2),
                "commutativity",
                module,
            )
            return _algebra_on_module(module, multiplication, placement=(self,))

        class ParentMethods:
            def is_commutative(self) -> bool:
                return True


# ``Lie`` is an owned algebra axiom not known to Sage's global axiom registry.
# Register the nested refinement explicitly so ``Algebras(R).Lie()`` is a
# category-with-axiom rather than an inference through Sage's built-in names.
Algebras.__dict__["Lie"]._base_category_class_and_axiom = (Algebras, "Lie")

FinitelyPresentedAlgebras = Algebras.Associative.Unital.FinitelyPresentedAsAlgebra


# ---------------------------------------------------------------------------
# The construction behind every entry.
# ---------------------------------------------------------------------------


def _algebra_on_module(module, multiplication, *, placement, unit=None, construction_data=None):
    r"""Build the algebra on the data of ``M`` with multiplication ``m``: the realization of ``Algebras(R)(M, m)``.

    Declared owner: the ``Algebras(R)`` entry and its axiom entries, and the
    constructions that compute ``(M, m)`` -- the centre, quotients, the
    commutator Lie algebra, group algebras, graded algebras -- call this and
    nothing else (``OWN-13``).

    The algebra's module structure is the defining datum of ``M``, read from
    the most specific module construction ``M`` carries: a chosen finite
    presentation (a finitely generated framed free module is one), a framed
    free module on its labels, or otherwise the datum of every ``R``-module,
    its additive group with the scalar action ``rho_M``.  ``M`` is retained
    as ``unformed_module()`` and ``m`` as ``multiplication()``; elements pass
    to and from ``M`` by coercion at the module level of that construction,
    and no map identifying the two is built.

    ``placement`` lists the categories the caller established for ``(M, m)``:
    an identity an axiom entry decided, or the theorem of a construction,
    cited where it is called.  ``unit``, an element of ``M``, is required
    exactly when the placement is unital.  ``construction_data`` carries the
    datum of a data category in ``placement``.
    """
    ring = module.base_ring()
    tensor = multiplication.domain()
    assert tensor in TensorProductModules(ring) and all(factor is module for factor in tensor.tensor_factors()), (
        f"the multiplication of an algebra on {module} is a linear map out of its tensor square"
    )
    assert multiplication.codomain() is module, f"the multiplication of an algebra on {module} lands in it"
    multiplication = module.module_category().Mor(tensor, module)(multiplication)
    categories = (Algebras(ring), *placement)
    data = {
        "unformed_module": module,
        "multiplication": multiplication,
        **(construction_data or {}),
    }
    match Cat().meet(categories):
        case category if category.is_subcategory(Algebras(ring).Unital()):
            assert unit is not None, "a unital algebra is stated with its unit"
            data["unit"] = module(unit)
        case _:
            assert unit is None, "a unit is stated only with a unital placement"
    match module:
        case _ if module in ModulesWithChosenFinitePresentation(ring):
            return module._same_presentation_module(
                module.module_generating_set(),
                _extra_categories=categories,
                _extra_construction_data=data,
            )
        case _ if module in FramedFreeModules(ring):
            return module._fresh_free_module_on(
                module.module_generating_set(),
                _extra_categories=categories,
                _extra_construction_data=data,
            )
        case _:
            return _object_of(
                Cat().meet((GeneralModules(ring), *categories)),
                base_ring=ring,
                rho=module.scalar_action(),
                verify=False,
                **data,
            )


def _center_algebra(algebra, submodule):
    r"""The centre of an associative algebra, built through the one construction on its central submodule.

    The centre of an associative algebra is a commutative associative
    subalgebra, and contains the unit when there is one (Bourbaki, *Algebra*
    III §1.7): that is the placement.  Its multiplication is the product of
    the algebra read back along the inclusion, which is injective, so
    ``lift`` recovers each product.
    """
    ring = algebra.algebra_base_ring()
    inclusion = submodule.inclusion()
    tensor = _algebra_tensor_square_functor(ring)(submodule)
    multiplication = tensor.from_bilinear(
        BilinearMap(
            submodule,
            submodule,
            submodule,
            lambda left, right: inclusion.lift(
                inclusion(submodule.module_generator(left)) * inclusion(submodule.module_generator(right))
            ),
        )
    )
    algebras = Algebras(ring)
    match algebra:
        case _ if algebra in algebras.Unital():
            return _algebra_on_module(
                submodule,
                multiplication,
                placement=(algebras.Associative().Unital().Commutative(),),
                unit=inclusion.lift(algebra.one()),
            )
        case _:
            return _algebra_on_module(
                submodule,
                multiplication,
                placement=(algebras.Associative(), algebras.Commutative()),
            )


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

        def _algebra_homset_class(self):
            r"""A framed algebra states its morphisms on its algebra generators."""
            return AlgebraHomset

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
    _HomCategory = UnitalAlgebraHomCategoryConstruction

    class ParentMethods:
        def algebra_base_ring(self):
            r"""``R`` for ``End_R(F)``: the base ring of the Hom module this algebra is."""
            return self.base_ring()

        def is_commutative(self) -> bool:
            r"""``M_n(R)`` commutes exactly when ``n <= 1``.

            This category is over a commutative ring, so the only obstruction
            is the size of the matrices.  Rank one gives ``R`` itself and rank
            zero the zero ring; from rank two the matrix units ``e_{12}`` and
            ``e_{21}`` fail to commute.
            """
            return self.nrows() <= 1

        def one(self):
            r"""The unit of ``End_R(F)``: the identity, the unit of composition."""
            return self.identity()

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

    def _lmul_(self, scalar):
        r"""``r * a = (r * 1) a``, with ``r * 1`` given by the realization's scalar structure.

        This realizes the scalar action of the underlying module.  The
        structure morphism of the algebra is computed from that action at the
        root, so it is not read back here.
        """
        parent = self.parent()
        return parent(parent._realized_scalar_structure(parent.base_ring()(scalar))) * self


class _OwnedAlgebraParent(_OwnedRingParent):
    r"""One ring read as an algebra through one specified scalar map."""

    Element = _OwnedAlgebraElement

    def __init__(
        self,
        engine,
        base_ring,
        labels,
        scalar_structure=None,
        generator_values=None,
        *,
        categories=(),
        construction_data=(),
    ) -> None:
        r"""Realize a ring as an algebra over ``base_ring`` on a private engine.

        Declared engine adapter (``OWN-06``) for the algebras the preamble
        adopts from Sage.  ``scalar_structure`` is the ring map
        ``base_ring -> A``, ``r |-> r * 1``, that realizes the scalar action
        of the underlying module; without one it is the engine's own map from
        its scalars.
        """
        base = _owned_ring(base_ring)
        for name, value in construction_data:
            setattr(self, name, value)
        self._realized_scalar_structure = (lambda scalar: self(scalar)) if scalar_structure is None else scalar_structure
        self._preamble_algebra_generating_set = None if labels is None else finite_ordered_set(labels)
        placement = [Algebras(base).Associative().Unital()]
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
    view = _OwnedAlgebraParent(
        _engine_ring(selected_ring),
        base,
        None,
        scalar_structure=lambda scalar: structure_map(base(scalar)),
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


@cached_function
def _own_algebra(structure_map):
    r"""Return the codomain of the ring map ``R -> A`` read as an ``R``-algebra through it."""
    if not isinstance(structure_map, Map):
        raise TypeError("an algebra is presented by a ring map")
    base = _owned_ring(structure_map.domain())
    engine = _engine_ring(structure_map.codomain())
    return _OwnedAlgebraParent(engine, base, None, scalar_structure=structure_map)


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
    target_structure = codomain.algebra_structure_morphism()

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
    "CommutativeAlgebraCoproducts",
    "CommutativeAlgebraPushouts",
    "FinitelyPresentedAlgebras",
    "FramedAlgebras",
    "MatrixAlgebras",
    "MultiplicativeAlgebraHomset",
    "UnitalMultiplicativeAlgebraHomset",
]
