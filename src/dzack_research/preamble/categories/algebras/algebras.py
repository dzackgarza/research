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
from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
    _category_mor_parent,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    _fix_selected_framing,
)
from dzack_research.preamble.categories.abstract_categories.products import (
    _finite_factor_family,
    _two_factors_of,
)
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.group.magmas import AdditiveGroups
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FramedFreeModules,
)
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
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
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


class _StructuredAlgebraModuleTransportMorphism(ModuleMorphism):
    r"""An existing module map read between algebra objects built on those modules."""

    def __init__(self, parent, underlying_morphism, action) -> None:
        self._underlying_morphism = underlying_morphism
        super().__init__(parent, action, elementwise=True)

    def _elementwise_linearity_derivation(self):
        return self._underlying_morphism.linearity_decision()


if "Lie" not in all_axioms:
    all_axioms.add("Lie")

# Qualified as Sage qualifies ``FinitelyGeneratedAsMagma``: an axiom name is
# global and propagates to every declared supercategory defining it, and a
# finitely presented algebra is not a finitely presented module.
if "FinitelyPresentedAsAlgebra" not in all_axioms:
    all_axioms.add("FinitelyPresentedAsAlgebra")


# ---------------------------------------------------------------------------
# The algebra Mor: linear maps preserving the multiplication.
# ---------------------------------------------------------------------------


class MultiplicativeAlgebraMorphism(Morphism):
    r"""An algebra morphism: an ``R``-linear \(f\colon A\to B\) with \(f\,m_A = m_B\,(f\otimes f)\).

    The datum is the linear map, an element of the module Mor.  The defining
    equation is one equation between two module morphisms out of
    \(A\otimes_R A\), asked of the module Mor: its finite generating data
    decide the equation when value equality is decided; otherwise it answers
    ``Unknown``.  A map
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
        assert preserved is not False, (
            f"{underlying_morphism} is not an algebra morphism {domain} -> {codomain}: it does not "
            "preserve the multiplication, f(xy) != f(x) f(y)"
        )
        self._underlying_morphism = linear
        self._tensor_square_morphism = tensor_square
        self._underlying_linearity = linear.linearity_decision()
        self._preserves_multiplication = preserved

    def underlying_morphism(self):
        r"""The linear map this algebra morphism is, in the module Mor."""
        return self._underlying_morphism

    def tensor_square_morphism(self):
        r"""\(f\otimes f\colon A\otimes_R A\to B\otimes_R B\)."""
        return self._tensor_square_morphism

    def linearity_decision(self):
        r"""Return the retained linearity decision of the underlying module map."""
        return self._underlying_linearity

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
        category = self.parent().mor_category()
        return category.Mor(self.codomain(), quotient)(quotient.algebra_quotient_projection())

    def _call_(self, element):
        return self.codomain()(self.underlying_morphism()(self.domain()(element)))

    def __eq__(self, other) -> bool:
        match element_parent(other):
            case parent if parent is self.parent():
                return self.underlying_morphism() == other.underlying_morphism()
            case _:
                return False

    def __ne__(self, other):
        equal = self == other
        return Unknown if equal is Unknown else not equal

    __hash__ = None

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        category = self.parent().mor_category()
        forget = Algebras(self.domain().algebra_base_ring()).underlying_module()
        return category.Mor(other.domain(), self.codomain())(self.underlying_morphism() * forget(other))


class MultiplicativeAlgebraMor(CategoricalMor):
    r"""``Hom_{R-Alg}(A, B)``: the linear maps preserving the multiplication."""

    Element = MultiplicativeAlgebraMorphism

    def __call__(self, datum):
        return self._element_constructor_(datum)

    def _element_constructor_(self, datum):
        # The one boundary admitting data this Mor did not build.  An arrow of
        # an algebra Mor with these endpoints is admitted by the linear map the
        # forgetful functor reads it as; any other datum states the linear map.
        parent = element_parent(datum)
        if parent is self:
            return datum
        algebras = Algebras(self.domain().algebra_base_ring())
        match parent:
            case CategoricalMor() if parent.mor_category().is_subcategory(algebras):
                datum = algebras.underlying_module()(datum)
            case _:
                pass
        return self.element_class(self, datum)

    def identity(self):
        assert self.domain() is self.codomain(), (
            f"the identity morphism exists only on Mor(A, A), but this is Mor({self.domain()}, {self.codomain()})"
        )
        algebra = self.domain()
        return self(algebra.module_category().Mor(algebra, algebra).identity())

    def _repr_(self):
        return f"Mor_Alg({self.domain()}, {self.codomain()})"


class UnitalMultiplicativeAlgebraMorphism(MultiplicativeAlgebraMorphism):
    r"""A morphism of unital algebras: multiplicative and \(f(1) = 1\)."""

    def __init__(self, parent, underlying_morphism) -> None:
        super().__init__(parent, underlying_morphism)
        self._preserves_unit = self(self.domain().one()) == self.codomain().one()
        assert self._preserves_unit is not False, (
            f"{underlying_morphism} is not a unital algebra morphism {self.domain()} -> {self.codomain()}: "
            "it does not send 1 to 1"
        )

    def preserves_unit(self):
        r"""The decision of the unit equation, or ``Unknown`` for its stated hypothesis."""
        return self._preserves_unit


class UnitalMultiplicativeAlgebraMor(MultiplicativeAlgebraMor):
    r"""``Mor`` of unital algebras: the multiplicative linear maps preserving the unit."""

    Element = UnitalMultiplicativeAlgebraMorphism

    def _repr_(self):
        return f"Mor_UnitalAlg({self.domain()}, {self.codomain()})"


def _algebra_from_native_ring(algebra, product, unit, scalar_action, *, module_basis=None):
    r"""Compute (M,m) from a native ring and enter the ordinary algebra constructor.

    The native unit is needed by the coefficient arithmetic of a self-based
    ring, so the unit owner records it before constructing its regular module.
    Modules(R) constructs the specified action and, over R itself, its actual
    rank-one framing. The tensor owner classifies the primitive bilinear
    product. Only then does _algebra_on_module construct the algebra datum.
    Nothing in this route substitutes a bare binary function for m.
    """
    from dzack_research.preamble.categories.modules.native_modules import _RingModulePresentation

    ring = algebra.algebra_base_ring()
    Algebras.Unital.ParentMethods._retain_unit(algebra, unit)
    presentation = _RingModulePresentation(algebra, ring, product, unit, scalar_action, basis=module_basis)
    module = Modules(ring)(presentation)
    category = Algebras(ring).Associative().Unital()
    law_decisions = {"associativity": True, "unit": True}
    if algebra.is_commutative() is True:
        category = category.Commutative()
        law_decisions["commutativity"] = True
    # The ring's own product is its algebra structure (OWN-22): no map out of
    # the tensor square is built here; `multiplication()` builds it when asked.
    Algebras.ParentMethods._retain_algebra_law_decisions(module, law_decisions)
    Algebras.Unital.ParentMethods._retain_unit(module, module(unit))
    selected_category = Cat().meet((Algebras(ring), category))
    match module in selected_category:
        case True:
            return module
        case False:
            return refine(module, selected_category)


class AlgebraMorCategoryConstruction(MorCategoryConstruction):
    r"""The fixed-endpoint Mor categories of ``R``-algebras: linear maps preserving the multiplication.

    An axiom that adds no condition on morphisms -- associativity,
    commutativity, the Lie identities -- shares this Mor object.
    """

    FixedCategoryClass = MultiplicativeAlgebraMor


class UnitalAlgebraMorCategoryConstruction(MorCategoryConstruction):
    r"""The fixed-endpoint Mor categories of unital ``R``-algebras: the unit is preserved too.

    The domain names the parent realizing this Mor.  An algebra stated by
    ``(M, m)`` takes the linear maps preserving product and unit; a data
    subcategory whose objects state their maps on further data -- algebra
    generators, a chosen presentation -- names its realization of the same
    morphisms.
    """

    def fixed_category_class_for(self, domain, codomain):
        return domain._algebra_mor_class()


# ---------------------------------------------------------------------------
# Units and the tensor square.
# ---------------------------------------------------------------------------


def _scalar_module(ring):
    r"""\(U_R(R)\): the ring as the module over itself, the domain of every unit map."""
    ring = _owned_ring(ring)
    match ring.base_ring() is ring:
        case True:
            return ring
        case False:
            return OwnedRings().Mor(ring, ring).identity().as_algebra()


class _AlgebraUnitModuleMorphism(ModuleMorphism):
    r"""The linear unit map ``R -> A`` determined by the module scalar action."""

    def _elementwise_linearity_derivation(self):
        return True


def _unit_morphism_from_element(module, unit, ring):
    r"""The linear map ``U_R(R) -> module`` determined by ``1 |-> unit``."""
    ring = _owned_ring(ring)
    scalar_module = _scalar_module(ring)
    return _AlgebraUnitModuleMorphism(
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
            f"no construction of the coproduct {left} (x) {right} of commutative algebras is available for "
            "either factor"
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
        assert left_leg.domain() is right_leg.domain(), (
            f"a pushout needs a span B <- A -> C, but {left_leg} starts at {left_leg.domain()} and "
            f"{right_leg} starts at {right_leg.domain()}"
        )
        return self._categorical_pushout(left_leg, right_leg)

    def _categorical_pushout(self, left_morphism, right_morphism):
        left = left_morphism.codomain()
        right = right_morphism.codomain()
        operation = getattr(left, "_commutative_algebra_pushout", None)
        if operation is None:
            operation = getattr(right, "_commutative_algebra_pushout", None)
        assert operation is not None, (
            f"no construction of the pushout of {left_morphism} and {right_morphism} in commutative "
            "algebras is available for either target"
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
        _generating_module=None,
    ):
        r"""Return the selected finite-presentation quotient by ``relations``."""
        category = AlgebrasWithChosenFinitePresentation(self.base_ring())
        return category._call_(
            self,
            relations,
            extra_categories=_extra_categories,
            extra_construction_data=_extra_construction_data,
            generating_module=_generating_module,
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
        f"the tensor square of algebras over {ring} is defined here only for a commutative ring, "
        f"but {ring} is not known to be commutative"
    )
    return _AlgebraTensorSquareFunctor(ring)


# ---------------------------------------------------------------------------
# Identities of a multiplication, decided on module generators.
# ---------------------------------------------------------------------------


def _product_on(multiplication):
    r"""``(x, y) |-> m(x, y)`` for ``m`` in ``M.bilinear_forms(M)``.

    That space is ``Hom_R(M (x)_R M, M)`` where the tensor square is
    represented, whose arrows evaluate on two elements through the pure
    tensor, and the bilinear maps ``M x M -> M`` otherwise; both evaluate on
    two elements of ``M``.
    """
    return lambda left, right: multiplication(left, right)


def _all_identity_decisions(decisions):
    r"""Conjoin decisions without treating an undecided equality as false."""
    result = True
    for decision in decisions:
        if decision is False:
            return False
        if decision is not True:
            result = Unknown
    return result


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
            return _all_identity_decisions(
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
    return lambda x, y: _all_identity_decisions((
        product(x, x) == zero, product(x, y) + product(y, x) == zero,
    ))


def _jacobi_identity(multiplication):
    product = _product_on(multiplication)
    zero = multiplication.codomain().zero()
    return lambda x, y, z: product(x, product(y, z)) + product(y, product(z, x)) + product(z, product(x, y)) == zero


def _two_sided_unit(multiplication, unit):
    product = _product_on(multiplication)
    return lambda x: _all_identity_decisions((product(unit, x) == x, product(x, unit) == x))


def _assert_not_refuted(held, statement, module):
    r"""Reject a disproved law; otherwise construct under the stated law.

    An axiom constructor states its identities as hypotheses on the supplied
    multiplication.  Finitary data can decide them; an undecided computation
    does not imply that the algebra has no such structure (``CON-16``).
    """
    assert held is not False, f"{statement} fails for the stated multiplication on {module}"


def _root_algebra_law_decisions(algebra):
    r"""Return the retained premises supporting the root algebra axioms of ``algebra``."""
    ring = algebra.algebra_base_ring()
    algebras = Algebras(ring)
    decisions = {}
    for category, accessors in (
        (algebras.Associative(), (("associativity", algebra.associativity_decision),)),
        (algebras.Unital(), (("unit", algebra.unit_laws_decision),)),
        (algebras.Commutative(), (("commutativity", algebra.commutativity_decision),)),
        (
            algebras.Lie(),
            (
                ("alternation", algebra.alternation_decision),
                ("jacobi", algebra.jacobi_decision),
            ),
        ),
    ):
        match algebra in category:
            case True:
                decisions.update((law, accessor()) for law, accessor in accessors)
            case False:
                pass
    return decisions



# ---------------------------------------------------------------------------
# The category of algebras.
# ---------------------------------------------------------------------------


def _algebra_structure_morphism(algebra):
    r"""Return the scalar structure map determined by an algebra's retained module action."""
    ring = algebra.algebra_base_ring()
    if ring is algebra:
        return ring.Mor(ring, category=OwnedRings()).identity()
    rho = algebra.scalar_action()
    match algebra:
        case _ if algebra in Algebras(ring).Associative().Unital():
            center = algebra.ring_center()
            unit = algebra._underlying_additive_element(algebra.one())
            return ring.Mor(center, category=OwnedRings())(
                lambda scalar: center(algebra(rho(ring(scalar))(unit))),
            )
        case _:
            return rho


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
                    f"scalar change of algebras is defined here on associative unital algebras, but {self} is "
                    f"not a subcategory of {ordinary}"
                )
            if _owned_ring(ring_map.domain()) is not self.base_ring():
                raise ValueError(
                    f"scalar change along {ring_map} for algebras over {self.base_ring()} needs a ring map "
                    f"starting at {self.base_ring()}, but it starts at {ring_map.domain()}"
                )
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
                raise ValueError(
                    f"restriction of scalars along {ring_map} into algebras over {self.base_ring()} needs a ring "
                    f"map ending at {self.base_ring()}, but it ends at {ring_map.codomain()}"
                )
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
        r"""Return the unique Mor object ``Hom_{R-Alg}(domain,codomain)``."""
        if domain not in self or codomain not in self:
            raise TypeError(
                f"a morphism of algebras in {self} needs two algebras in it, but got {domain} and {codomain}"
            )
        return self.MorCategory().Of(domain, codomain)

    _MorCategory = AlgebraMorCategoryConstruction

    def _call_(self, module, multiplication):
        r"""The algebra on ``M`` with multiplication ``m: M (x)_R M -> M``: the one entry.

        No identity of ``m`` is assumed or placed here; the axiom entries
        ``Associative()``, ``Unital()``, ``Commutative()`` and ``Lie()`` place
        an algebra on the identities they decide.
        """
        assert module.base_ring() is self.base_ring(), (
            f"an algebra over {self.base_ring()} is built on a module over {self.base_ring()}, but {module} "
            f"is a module over {module.base_ring()}"
        )
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
        def _refined_specialized_algebra(
            self,
            base_ring,
            labels,
            categories,
            construction_data,
        ):
            r"""Internal refinement hook for a specialized algebra realization.

            Protected Algebras constructor contract under OWN-05.  The sole
            caller is _refine_algebra.  A specialized algebra owner may return
            the owned algebra preserving its defining representation while
            adding the requested labels, categories, and construction data;
            the default returns None.  No engine handle is exchanged.  This
            hook exists because representation-preserving reconstruction is a
            constructor responsibility, not an ordinary mathematical
            operation on an already constructed algebra.
            """
            _ = (base_ring, labels, categories, construction_data)
            return None

        def __init__(self, unformed_module=None, multiplication=None, *, algebra_law_decisions=None,
                     _engine_product=None, _engine_scalar_action=None, _native_unit_factory=None, **rest) -> None:
            r"""Construct the algebra from its exact module and tensor multiplication.

            Native cooperative realizations supply primitive ring operations;
            after the lower constructor finishes they compute the same module
            and tensor datum through the owners used by every ordinary entry.
            """
            self._preamble_algebra_law_decisions = dict(
                vars(self).get("_preamble_algebra_law_decisions", {})
            )
            if algebra_law_decisions is not None:
                self._retain_algebra_law_decisions(algebra_law_decisions)
            match _engine_product:
                case None:
                    assert unformed_module is not None and multiplication is not None, (
                        "an algebra needs its module and its multiplication M (x) M -> M, but one of them is missing"
                    )
                    self._retain_algebra_datum(unformed_module, multiplication)
                    super().__init__(**rest)
                case product:
                    assert unformed_module is None and multiplication is None, (
                        "an algebra computed by a computer-algebra system cannot also be given a module and a "
                        "multiplication"
                    )
                    assert callable(product) and callable(_engine_scalar_action) and callable(_native_unit_factory)
                    super().__init__(**rest)
                    _algebra_from_native_ring(self, product, _native_unit_factory(self), _engine_scalar_action)

        def _retain_algebra_law_decisions(self, decisions):
            r"""Retain the exact admission decision supporting each algebra axiom placement."""
            retained = dict(vars(self).get("_preamble_algebra_law_decisions", {}))
            for law, decision in dict(decisions).items():
                assert decision is True or decision is Unknown, (
                    f"the {law} law of an algebra is recorded only as True or Unknown, but got {decision}"
                )
                previous = retained.get(law)
                if previous is True:
                    continue
                if previous is Unknown and decision is Unknown:
                    continue
                retained[law] = decision
            self._preamble_algebra_law_decisions = retained

        def associativity_decision(self):
            r"""Return the retained decision supporting associative placement, else ``Unknown``."""
            return self._preamble_algebra_law_decisions.get("associativity", Unknown)

        def unit_laws_decision(self):
            r"""Return the retained decision supporting the selected two-sided unit, else ``Unknown``."""
            return self._preamble_algebra_law_decisions.get("unit", Unknown)

        def commutativity_decision(self):
            r"""Return the retained decision supporting commutative placement, else ``Unknown``."""
            return self._preamble_algebra_law_decisions.get("commutativity", Unknown)

        def alternation_decision(self):
            r"""Return the retained decision supporting alternation of a Lie bracket, else ``Unknown``."""
            return self._preamble_algebra_law_decisions.get("alternation", Unknown)

        def jacobi_decision(self):
            r"""Return the retained decision supporting the Jacobi identity, else ``Unknown``."""
            return self._preamble_algebra_law_decisions.get("jacobi", Unknown)

        def _retain_algebra_datum(self, module, multiplication):
            r"""Retain the root constructor's already validated (M,m) once.

            Called by this level's constructor and by _algebra_on_module when
            the canonical native realization is the already constructed M.
            Both callers supply an actual tensor morphism. A second product
            never mutates an existing algebra.
            """
            previous = vars(self).get("_preamble_multiplication")
            if previous is not None:
                assert previous is multiplication and self._preamble_unformed_module is module, (
                    f"the multiplication of an algebra cannot be replaced: it already has {previous} on "
                    f"{self._preamble_unformed_module}"
                )
                return
            self._preamble_unformed_module = module
            self._preamble_multiplication = multiplication

        def unformed_module(self):
            r"""The module ``M`` this algebra is built on: the ``M`` of ``Algebras(R)(M, m)``, or the algebra itself when it realizes its own module."""
            native = self._native_module_presentation()
            if native is not None:
                return native.module()
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
            r"""The multiplication ``m: M (x)_R M -> M`` this algebra was stated with, an element of ``M.bilinear_forms(M)``.

            A ring that is its own algebra is stated by its product, not by a
            map out of a tensor product (``OWN-22``), so for it the map is
            built from that product here, when it is asked for.
            """
            stated = vars(self).get("_preamble_multiplication")
            if stated is not None:
                return stated
            native = self._native_module_presentation()
            assert native is not None, f"{self} was constructed without a multiplication"
            return native.multiplication()

        @cached_method
        def multiplication_morphism(self):
            r"""The linear classifier ``A tensor_R A -> A`` of the product.

            The module tensor owner supplies the universal map for both
            framed and unframed modules.  Transport of the product from the
            retained module is bilinear because the element crossings preserve
            that module's addition and scalar action.
            """
            ring = self.algebra_base_ring()
            module = self.unformed_module()
            product = _product_on(self.multiplication())
            tensor = _algebra_tensor_square_functor(ring)(self)
            return tensor.from_bilinear_map(
                self, lambda left, right: self(product(module(left), module(right))),
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
            return _algebra_structure_morphism(self)

        def affine_equation_family(self, relative_variables, equations):
            r"""Return the relative affine family defined over this parameter algebra."""
            from dzack_research.preamble.categories.schemes.families import (
                _relative_affine_family,
            )

            return _relative_affine_family(self, relative_variables, equations)

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
            r"""The scalar ring established by this algebra's module constructor."""
            return self.base_ring()

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
            return _category_mor_parent(category, self, codomain)

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
                f"the centre of {self} is computed from its module generators, which needs finitely many, "
                f"but it has {labels.cardinality()}"
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
                    return _StructuredAlgebraModuleTransportMorphism(
                        center.module_category().Mor(center, self),
                        inclusion,
                        lambda element: inclusion(submodule(element)),
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
                f"the ideal of {self} generated by {subobject} is computed here only for finite-dimensional "
                f"algebras over a field, but {ring} is not a field"
            )
            assert subobject.inclusion().codomain() is self, (
                f"the ideal of {self} generated by a submodule needs a submodule of {self}, but {subobject} "
                f"is a submodule of {subobject.inclusion().codomain()}"
            )
            ambient_labels = self.module_generating_set()
            assert ambient_labels.cardinality().is_finite(), (
                f"the ideal of {self} generated by {subobject} needs finitely many module generators of "
                f"{self}, but it has {ambient_labels.cardinality()}"
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
            assert ideal.inclusion().codomain() is self, (
                f"the quotient of {self} needs an ideal of {self}, but {ideal} is an ideal of "
                f"{ideal.inclusion().codomain()}"
            )
            projection = ideal.inclusion().cokernel_projection()
            quotient_module = projection.codomain()
            multiplication = BilinearMap(
                quotient_module,
                quotient_module,
                quotient_module,
                lambda left, right: projection(
                    self.product(self.module_generator(left), self.module_generator(right))
                ),
            )
            algebras = Algebras(ring)
            descended = tuple(
                axiom
                for axiom in (algebras.Associative(), algebras.Commutative(), algebras.Lie())
                if self in axiom
            )
            law_decisions = _root_algebra_law_decisions(self)
            match self:
                case _ if self in algebras.Unital():
                    return _algebra_on_module(
                        quotient_module,
                        multiplication,
                        placement=(*descended, algebras.Unital()),
                        unit=projection(self.one()),
                        law_decisions=law_decisions,
                    )
                case _:
                    return _algebra_on_module(
                        quotient_module,
                        multiplication,
                        placement=descended,
                        law_decisions=law_decisions,
                    )

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
            return _StructuredAlgebraModuleTransportMorphism(
                ambient.module_category().Mor(ambient, self),
                projection,
                lambda element: self(projection(element)),
            )

        def algebra_quotient_ideal(self):
            r"""The ideal ``I`` of an algebra built as ``A.quotient_by_algebra_ideal(I)``: the kernel of its projection."""
            return self.unformed_module().cokernel_projection().kernel()

        def _Hom_(self, codomain, category=None):
            if category is not None and not category.is_subcategory(Algebras(self.algebra_base_ring())):
                raise TypeError(
                    f"{category} is not a category of algebras over {self.algebra_base_ring()}, so Mor({self}, "
                    f"{codomain}) cannot be formed in it"
                )
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
            associativity = _decide_on_module_generators(
                module, _associativity(multiplication), 3
            )
            _assert_not_refuted(associativity, "associativity", module)
            return _algebra_on_module(
                module,
                multiplication,
                placement=(self,),
                law_decisions={"associativity": associativity},
            )

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

            _MorCategory = UnitalAlgebraMorCategoryConstruction

            class SubcategoryMethods:
                def FinitelyPresentedAsAlgebra(self):
                    r"""Return the refinement whose objects admit a finite algebra presentation."""
                    return self._with_axiom("FinitelyPresentedAsAlgebra")

            class Framed(CategoryWithAxiom):
                r"""Associative unital algebras carrying the global framing datum."""

                class ParentMethods:
                    def __init__(
                        self,
                        algebra_generating_family=None,
                        algebra_framing_source=None,
                        algebra_framing_owner=None,
                        **rest,
                    ) -> None:
                        super().__init__(**rest)
                        if algebra_generating_family is None:
                            return
                        associative = Algebras(self.base_ring()).Associative().Unital()
                        owner = algebra_framing_owner
                        if owner is None:
                            owner = (
                                associative.Commutative()
                                if self in associative.Commutative()
                                else associative
                            )
                        self._algebra_framing_owner = owner
                        labels = algebra_generating_family.index_set()
                        values = algebra_generating_family.map(self)
                        if algebra_framing_source is None:
                            module = self.base_ring().free_module(labels)
                            match owner is associative:
                                case True:
                                    source = module.tensor_algebra()
                                case False:
                                    source = module.symmetric_algebra()
                        else:
                            source = algebra_framing_source
                        generator_morphism = Sets().Mor(labels, self)(values.value)
                        _fix_selected_framing(
                            self,
                            owner,
                            source,
                            labels,
                            lambda: generator_morphism,
                            lambda: source.Mor(self)(generator_morphism),
                        )

                    def algebra_framing_owner(self):
                        owner = self.__dict__.get("_algebra_framing_owner")
                        assert owner is not None, (
                            f"{self} has no chosen generating set as an algebra"
                        )
                        return owner

                    def algebra_generating_set(self):
                        return self.selected_framing_generating_set(self.algebra_framing_owner())

                    def algebra_generator_morphism(self):
                        return self.selected_framing_generator_morphism(self.algebra_framing_owner())

                    def algebra_generator(self, label):
                        return self.selected_framing_generator(self.algebra_framing_owner(), label)

                    def algebra_generators(self):
                        return self.selected_framing_generators(
                            self.algebra_framing_owner(),
                            name="Algebra generators",
                        )

                    def number_of_algebra_generators(self):
                        return self.selected_framing_generator_count(self.algebra_framing_owner())

                    def _algebra_mor_class(self):
                        r"""A framed algebra states its morphisms on its selected generators."""
                        return AlgebraMor

                    def finite_algebra_generators(self):
                        r"""Return the selected algebra generators as a finite ordered family."""
                        labels = self.algebra_generating_set()
                        assert labels.cardinality().is_finite(), (
                            f"{self} has no finite chosen set of algebra generators: it has {labels.cardinality()}"
                        )
                        return FiniteOrderedSets().from_indexed(
                            labels,
                            self.algebra_generator,
                            name=f"Selected algebra generators of {self}",
                        )

                    def product_on_algebra_generators(self, left, right):
                        return self.algebra_generator(left) * self.algebra_generator(right)

                    def is_central(self, element):
                        r"""Decide centrality from the selected algebra framing."""
                        if element not in self:
                            return False
                        return all(
                            element * self.algebra_generator(label)
                            == self.algebra_generator(label) * element
                            for label in self.algebra_generating_set()
                        )

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
                associativity = _decide_on_module_generators(
                    module, _associativity(multiplication), 3
                )
                unit_laws = _decide_on_module_generators(
                    module,
                    _two_sided_unit(multiplication, module(unit)),
                    1,
                )
                _assert_not_refuted(associativity, "associativity", module)
                _assert_not_refuted(unit_laws, "the two unit equations", module)
                return _algebra_on_module(
                    module,
                    multiplication,
                    placement=(self,),
                    unit=module(unit),
                    law_decisions={
                        "associativity": associativity,
                        "unit": unit_laws,
                    },
                )

            class Commutative(CategoryWithAxiom):
                r"""Commutative associative unital ``R``-algebras."""

                _MorCategory = UnitalAlgebraMorCategoryConstruction
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
                    decisions = {
                        "associativity": _decide_on_module_generators(
                            module, _associativity(multiplication), 3
                        ),
                        "commutativity": _decide_on_module_generators(
                            module, _commutativity(multiplication), 2
                        ),
                        "unit": _decide_on_module_generators(
                            module,
                            _two_sided_unit(multiplication, module(unit)),
                            1,
                        ),
                    }
                    for law, statement in (
                        ("associativity", "associativity"),
                        ("commutativity", "commutativity"),
                        ("unit", "the two unit equations"),
                    ):
                        held = decisions[law]
                        _assert_not_refuted(held, statement, module)
                    return _algebra_on_module(
                        module,
                        multiplication,
                        placement=(self,),
                        unit=module(unit),
                        law_decisions=decisions,
                    )

    class Lie(CategoryWithAxiom):
        r"""Algebras whose bilinear multiplication is a Lie bracket: alternating and satisfying the Jacobi identity.

        No associativity or unit is implied: the multiplication at this node
        is the bracket itself, so the algebra Mor already has the right
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
            alternation = _decide_on_module_generators(
                module, _alternation(multiplication), 2
            )
            jacobi = _decide_on_module_generators(
                module, _jacobi_identity(multiplication), 3
            )
            _assert_not_refuted(alternation, "alternation", module)
            _assert_not_refuted(jacobi, "the Jacobi identity", module)
            return _algebra_on_module(
                module,
                multiplication,
                placement=(self,),
                law_decisions={"alternation": alternation, "jacobi": jacobi},
            )

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

        _MorCategory = UnitalAlgebraMorCategoryConstruction

        @classmethod
        def _repr_object_names(cls):
            return "unital algebras"

        def _call_(self, module, multiplication, unit):
            r"""The unital algebra on ``(M, m)`` with unit ``1 in M``, the unit equations decided on module generators."""
            unit_laws = _decide_on_module_generators(
                module,
                _two_sided_unit(multiplication, module(unit)),
                1,
            )
            _assert_not_refuted(unit_laws, "the two unit equations", module)
            return _algebra_on_module(
                module,
                multiplication,
                placement=(self,),
                unit=module(unit),
                law_decisions={"unit": unit_laws},
            )

        class ParentMethods:
            def __init__(self, unit=None, *, _engine_unit=None, **rest) -> None:
                match _engine_unit:
                    case None:
                        assert unit is not None, (
                            "a unital algebra needs its unit element, but none was given"
                        )
                        self._retain_unit(unit)
                        super().__init__(**rest)
                    case unit_factory:
                        assert unit is None and callable(unit_factory)
                        super().__init__(_native_unit_factory=unit_factory, **rest)

            def _retain_unit(self, unit):
                r"""The one unit datum, including self-based coefficient construction."""
                previous = vars(self).get("_preamble_algebra_unit")
                assert previous is None or previous is unit or (previous == unit) is True, (
                    f"the unit of an algebra cannot be replaced: it already has unit {previous}, not {unit}"
                )
                self._preamble_algebra_unit = unit

            @cached_method
            def one(self):
                r"""The unit, read on this algebra by coercion from the unit of ``M``."""
                return self(self._preamble_algebra_unit)

            @cached_method
            def unit_morphism(self):
                r"""\(\eta\colon U_R(R)\to A\), \(r\mapsto\rho(r)(1)\)."""
                return _unit_morphism_from_element(self, self.one(), self.algebra_base_ring())

            def _algebra_mor_class(self):
                r"""A unital algebra stated by ``(M, m)`` takes the multiplicative unit-preserving linear maps."""
                return UnitalMultiplicativeAlgebraMor

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
            commutativity = _decide_on_module_generators(
                module, _commutativity(multiplication), 2
            )
            _assert_not_refuted(commutativity, "commutativity", module)
            return _algebra_on_module(
                module,
                multiplication,
                placement=(self,),
                law_decisions={"commutativity": commutativity},
            )

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


def _algebra_on_module(
    module,
    multiplication,
    *,
    placement,
    unit=None,
    construction_data=None,
    law_decisions=None,
):
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
    datum of a data category in ``placement``.  ``law_decisions`` carries the
    exact ``True``/``Unknown`` premises supporting axiom placements.
    """
    ring = module.base_ring()
    tensor = multiplication.domain()
    assert tensor in TensorProductModules(ring) and tensor.tensor_factors().index_set().cardinality() == 2 and all(factor is module for factor in tensor.tensor_factors()), (
        f"the multiplication of an algebra on {module} must be a linear map {module} (x) {module} -> "
        f"{module}, but {multiplication} starts at {tensor}"
    )
    assert all(category.is_subcategory(Algebras(ring)) for category in placement), (
        f"an algebra on the {ring}-module {module} must be placed in categories of algebras over "
        f"{ring}, but got {placement}"
    )
    assert multiplication.codomain() is module, (
        f"the multiplication of an algebra on {module} must end at {module}, but {multiplication} "
        f"ends at {multiplication.codomain()}"
    )
    multiplication = module.module_category().Mor(tensor, module)(multiplication)
    categories = (Algebras(ring), *placement)
    selected_category = Cat().meet(categories)
    law_decisions = dict(law_decisions or {})
    for decision in law_decisions.values():
        assert decision is True or decision is Unknown, (
            f"an algebra law is recorded only as True or Unknown, but got {decision}"
        )
    for required_category, required_laws in (
        (Algebras(ring).Associative(), ("associativity",)),
        (Algebras(ring).Unital(), ("unit",)),
        (Algebras(ring).Commutative(), ("commutativity",)),
        (Algebras(ring).Lie(), ("alternation", "jacobi")),
    ):
        match selected_category.is_subcategory(required_category):
            case True:
                missing = tuple(law for law in required_laws if law not in law_decisions)
                assert not missing, (
                    f"placing an algebra on {module} in {selected_category} needs a decision for each of the "
                    f"laws {missing}, but none was recorded"
                )
            case False:
                pass
    data = {
        "unformed_module": module,
        "multiplication": multiplication,
        "algebra_law_decisions": law_decisions,
        **(construction_data or {}),
    }
    match selected_category:
        case category if category.is_subcategory(Algebras(ring).Unital()):
            assert unit is not None, (
                f"an algebra on {module} placed in {selected_category} is unital, so it needs its unit "
                "element, but none was given"
            )
            data["unit"] = module(unit)
        case _:
            assert unit is None, (
                f"a unit {unit} was given for an algebra on {module}, but {selected_category} is not a "
                "category of unital algebras"
            )
    native = Modules.ParentMethods._native_module_presentation(module)
    if native is not None and construction_data is None and multiplication is native.multiplication():
        # This is the original ring product on its constructed module, not an
        # alternative multiplication admitted merely because M is a ring.
        Algebras.ParentMethods._retain_algebra_datum(module, module, multiplication)
        Algebras.ParentMethods._retain_algebra_law_decisions(
            module, law_decisions
        )
        if unit is not None:
            Algebras.Unital.ParentMethods._retain_unit(module, module(unit))
        match module in selected_category:
            case True:
                return module
            case False:
                return refine(module, selected_category)
    return module._module_with_structure(categories, data)


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
    multiplication = BilinearMap(
        submodule,
        submodule,
        submodule,
        lambda left, right: inclusion.lift(
            inclusion(submodule.module_generator(left)) * inclusion(submodule.module_generator(right))
        ),
    )
    algebras = Algebras(ring)
    law_decisions = {
        "associativity": algebra.associativity_decision(),
        "commutativity": True,
    }
    match algebra:
        case _ if algebra in algebras.Unital():
            law_decisions["unit"] = algebra.unit_laws_decision()
            return _algebra_on_module(
                submodule,
                multiplication,
                placement=(algebras.Associative().Unital().Commutative(),),
                unit=inclusion.lift(algebra.one()),
                law_decisions=law_decisions,
            )
        case _:
            return _algebra_on_module(
                submodule,
                multiplication,
                placement=(algebras.Associative(), algebras.Commutative()),
                law_decisions=law_decisions,
            )


def FramedAlgebras(base_ring):
    r"""The global ``Framed`` axiom specialized to associative unital algebras."""
    return Algebras(base_ring).Associative().Unital().Framed()


class MatrixAlgebras(OwnedCategoryOverBaseRing):
    r"""Finite matrix endomorphism Mor objects with their canonical algebra structure."""

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
            raise TypeError(
                f"End_R(F) is an R-algebra only for commutative R, but {self.base_ring()} is not known to be "
                "commutative"
            )
        return [
            MatrixEndomorphismSpaces(self.base_ring()),
            FramedAlgebras(self.base_ring()),
        ]

    # M_n(R) is unital, so a morphism of matrix algebras preserves the unit.
    # The associative Mor that arrives from the endomorphism spaces below does
    # not ask that, and this says which of the two the category means.
    _MorCategory = UnitalAlgebraMorCategoryConstruction

    class ParentMethods:
        def __init_extra__(self) -> None:
            r"""Retain the canonical matrix-unit algebra framing at refinement."""
            owner = Algebras(self.base_ring()).Associative().Unital()
            if owner in self.__dict__.get("_selected_framings", {}):
                return
            labels = self.module_generating_set()
            generator_morphism = Sets().Mor(labels, self)(
                lambda label: self.matrix_unit(label[0], label[1])
            )
            source = self.base_ring().free_module(labels).tensor_algebra()
            self._algebra_framing_owner = owner
            _fix_selected_framing(
                self,
                owner,
                source,
                labels,
                lambda: generator_morphism,
                lambda: source.Mor(self)(generator_morphism),
            )

        def algebra_base_ring(self):
            r"""``R`` for ``End_R(F)``: the base ring of the Mor module this algebra is."""
            return self.base_ring()

        def is_commutative(self) -> bool:
            r"""``M_n(R)`` commutes exactly when ``n <= 1``.

            This category is over a commutative ring, so the only obstruction
            is the size of the matrices.  Rank one gives ``R`` itself and rank
            zero the zero ring; from rank two the matrix units ``e_{12}`` and
            ``e_{21}`` fail to commute.
            """
            return self.base_ring().one() == self.base_ring().zero() or self.nrows() <= 1

        def one(self):
            r"""The unit of ``End_R(F)``: the identity, the unit of composition."""
            return self.identity()

def _refine_matrix_algebra(mor):
    r"""Return a square matrix Mor after requiring constructor-time algebra placement."""

    ring = mor.base_ring()
    if mor not in MatrixEndomorphismSpaces(ring):
        return mor
    if ring not in OwnedRings().Commutative():
        return mor
    if mor not in MatrixAlgebras(ring):
        raise TypeError(
            f"End({mor.domain()}) over the commutative ring {ring} must be constructed as a matrix algebra, "
            f"but {mor} is not in {MatrixAlgebras(ring)}"
        )
    return mor


class _SelectedFiniteAlgebraPresentation:
    r"""The chosen polynomial presentation defining a presented algebra.

    The presenting algebra, relation family, defining ideal, quotient map, and
    selected lift are one mathematical choice.  The quotient-map realization
    is fixed at construction and may be evaluated later; its cache is not a
    second mathematical datum.  Keep them together so the
    chosen-presentation category does not infer that choice from unrelated
    private attributes on its objects.
    """

    def __init__(
        self,
        presentation_ring,
        relations,
        presentation_ideal,
        lift_to_presentation,
        presentation_morphism_factory,
    ) -> None:
        self._presentation_ring = presentation_ring
        self._relations = relations
        self._presentation_ideal = presentation_ideal
        self._lift_to_presentation = lift_to_presentation
        if not callable(presentation_morphism_factory):
            raise TypeError(
                f"writing an algebra as R[x_1, ..., x_n]/I needs a function producing its quotient map, "
                f"but {presentation_morphism_factory!r} is not callable"
            )
        self._presentation_morphism_factory = presentation_morphism_factory
        self._realized_presentation_morphism = None

    def presentation_ring(self):
        return self._presentation_ring

    def relations(self):
        return self._relations

    def presentation_ideal(self):
        return self._presentation_ideal

    def lift(self, element):
        return self._lift_to_presentation(element)

    def presentation_morphism(self):
        morphism = self._realized_presentation_morphism
        if morphism is None:
            morphism = self._presentation_morphism_factory()
            if morphism.domain() is not self.presentation_ring():
                raise ValueError(
                    f"the quotient map R[x_1, ..., x_n] -> R[x_1, ..., x_n]/I must start at {self.presentation_ring()}, but it "
                    f"starts at {morphism.domain()}"
                )
            self._realized_presentation_morphism = morphism
        return morphism


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
            Algebras(self.base_ring()).Associative().Unital().Commutative().Framed(),
        ]

    def _call_(
        self,
        presentation_ring,
        relations,
        *,
        extra_categories=(),
        extra_construction_data=None,
        generating_module=None,
    ):
        r"""Construct an algebra from its selected finite polynomial presentation."""
        if presentation_ring.base_ring() is not self.base_ring():
            raise ValueError(
                f"an algebra over {self.base_ring()} given by generators and relations needs a polynomial ring "
                f"over {self.base_ring()}, but {presentation_ring} is over {presentation_ring.base_ring()}"
            )
        from dzack_research.preamble.categories.algebras.free_algebras import (
            _finitely_presented_algebra_from_data,
        )

        return _finitely_presented_algebra_from_data(
            presentation_ring,
            relations,
            _extra_categories=tuple(extra_categories),
            _extra_construction_data=extra_construction_data,
            _generating_module=generating_module,
        )

    class ParentMethods:
        def _algebra_mor_class(self):
            return PresentedAlgebraMor

        def selected_algebra_presentation(self):
            r"""Return the one chosen polynomial-presentation datum for this algebra."""
            selected = self._selected_algebra_presentation
            assert selected.presentation_ring() is self.selected_framing_source(
                self.algebra_framing_owner()
            ), (
                f"{self} must be written as a quotient of the free algebra on its chosen generators, "
                f"but its polynomial ring is {selected.presentation_ring()}"
            )
            return selected

        def presentation_ring(self):
            return self.selected_algebra_presentation().presentation_ring()

        def generating_module(self):
            r"""Return the exact module on which the selected free algebra is built."""
            generating = self.presentation_ring().generating_module()
            assert generating.module_generating_set() == self.algebra_generating_set(), (
                f"the generators {generating.module_generating_set()} of the polynomial ring of {self} differ "
                f"from its chosen algebra generators {self.algebra_generating_set()}"
            )
            return generating

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
            labels = finite_ordered_set(("presentation_ring", "relations"))
            values = {
                "presentation_ring": self.presentation_ring(),
                "relations": self.relations(),
            }
            return indexed_family(
                labels,
                values.__getitem__,
                name="Selected finite algebra presentation data",
            )

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
                    f"cannot decide whether {self.base_ring()} -> {self} is injective: {self} is not given as a "
                    "quotient of a polynomial ring in which the relations can be eliminated"
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
                    f"cannot decide whether {self.base_ring()} -> {self} is injective: its polynomial ring "
                    f"{presentation} over a non-polynomial base has no flattening to a polynomial ring"
                )
                flattening = flattening_factory()
                assert flattening.codomain() is cover, (
                    f"cannot decide whether {self.base_ring()} -> {self} is injective: the flattening of "
                    f"{presentation} ends at {flattening.codomain()}, not at {cover}"
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
                    f"cannot decide whether {self.base_ring()} -> {self} is injective: the variables of "
                    f"{presentation} could not be eliminated from the relations"
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
                f"torsion-freeness of {self} is decided here only over a principal ideal domain, but "
                f"{base} is not known to be one"
            )
            assert bool(self.is_integral_domain()), (
                f"torsion-freeness of {self} over the principal ideal domain {base} is decided here only when "
                f"{self} is an integral domain"
            )
            return self._represented_structure_morphism_kernel_is_zero()

        def _represented_primitive_hypersurface_relative_dimension(self) -> int:
            r"""Return the common fibre dimension for a primitive hypersurface presentation."""

            relations = self.relations()
            assert relations.cardinality().is_finite() and int(relations.cardinality()) == 1, (
                f"the relative dimension of {self} is computed here only for one defining equation, but it has "
                f"{relations.cardinality()}"
            )
            labels = self.presentation_ring().algebra_generating_set()
            assert labels.cardinality().is_finite(), (
                f"the relative dimension of {self} needs finitely many variables, but it has {labels.cardinality()}"
            )
            variable_count = int(labels.cardinality())
            assert variable_count > 0, (
                f"the relative dimension of the hypersurface {self} needs at least one variable, but it has none"
            )

            relation_index = next(iter(relations.index_set()))
            relation = relations.value(relation_index)
            presentation = self.presentation_ring()
            presentation_engine = _engine_ring(presentation)
            backend_relation = presentation_engine(_engine_element(presentation, relation))
            coefficient_ideal = self.base_ring().ideal(*tuple(_owned_engine_element(self.base_ring(), coefficient) for coefficient in backend_relation.coefficients()))
            assert coefficient_ideal == self.base_ring().ideal(self.base_ring().one()), (
                f"the relative dimension of the hypersurface {self} is computed here only when its equation "
                f"{relation} is primitive, i.e. its coefficients generate the unit ideal of {self.base_ring()}"
            )
            return variable_count - 1

        def algebra_presentation_morphism(self):
            selected = self.selected_algebra_presentation().presentation_morphism()
            assert selected is self.selected_framing_morphism(
                self.algebra_framing_owner()
            ), (
                f"the quotient map R[x_1, ..., x_n] -> {self} is not its chosen surjection from the free algebra"
            )
            return selected

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
                terms[monomial] = _owned_engine_element(base, engine_base(coefficient))
            return terms

        def base_change(self, ring_map):
            r"""Extend this chosen commutative presentation along ``ring_map``."""
            assert self in Algebras(self.base_ring()).Associative().Unital().Commutative(), (
                f"base change of {self} along {ring_map} is computed here only for a commutative algebra"
            )
            from dzack_research.preamble.categories.algebras.free_algebras import (
                _base_change_commutative_presentation,
            )

            return _base_change_commutative_presentation(self, ring_map)

        def _commutative_algebra_coproduct(self, left, right):
            r"""Evaluate the selected binary-coproduct construction on this object.

            Protected algebra-construction contract under OWN-05--07. The sole
            external caller role is ``Algebras._categorical_coproduct`` after
            it has selected one of the two operands as the construction owner.
            The installed callable returns an owned algebra and its owned
            injections; no engine algebra or presentation storage crosses this
            method.
            """
            operation = getattr(
                self,
                "_preamble_commutative_algebra_coproduct_backend",
                None,
            )
            assert operation is not None, (
                f"no construction of the coproduct {left} (x) {right} of commutative algebras is available for {self}"
            )
            return operation(left, right)

        def _commutative_algebra_pushout(self, left_map, right_map):
            r"""Evaluate the selected commutative-algebra pushout on this object.

            Protected algebra-construction contract under OWN-05--07. The sole
            external caller role is ``Algebras._categorical_pushout`` once an
            operand has supplied the represented construction. The result and
            its structure maps are owned algebraic objects; private
            presentation data remain inside the construction implementation.
            """
            operation = getattr(
                self,
                "_preamble_commutative_algebra_pushout_backend",
                None,
            )
            assert operation is not None, (
                f"no construction of the pushout of {left_map} and {right_map} in commutative algebras is "
                f"available for {self}"
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
                raise IndexError(
                    f"a coproduct of two algebras has injections 0 and 1, but got index {index}"
                )
            factor = self.coproduct_factors()[index]
            tag = "left" if index == 0 else "right"
            return factor.Mor(self)({label: self.algebra_generator((tag, label)) for label in factor.algebra_generating_set()})

        def coproduct_injections(self):
            factors = self.coproduct_factors()
            return indexed_family(
                factors.index_set(),
                self.coproduct_injection,
                name="Coproduct injections",
            )

        def left_coproduct_map(self):
            return self.coproduct_injection(0)

        def right_coproduct_map(self):
            return self.coproduct_injection(1)

        def from_cocone(self, left_map, right_map):
            left, right = self.coproduct_factors()
            if left_map.domain() is not left or right_map.domain() is not right:
                raise ValueError(
                    f"the maps out of the coproduct {self} must start at its factors {left} and {right}, but they "
                    f"start at {left_map.domain()} and {right_map.domain()}"
                )
            if left_map.codomain() is not right_map.codomain():
                raise ValueError(
                    f"the maps out of the coproduct {self} must end at one algebra, but they end at "
                    f"{left_map.codomain()} and {right_map.codomain()}"
                )
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
            return coproduct.coproduct_injections().map(
                lambda injection: quotient_map * injection,
                name="Pushout structure maps",
            )

        def left_pushout_map(self):
            return self.pushout_maps()[0]

        def right_pushout_map(self):
            return self.pushout_maps()[1]

        def from_pushout_cocone(self, left_map, right_map):
            source_map, target_map = self.pushout_span()
            left_factor = source_map.codomain()
            right_factor = target_map.codomain()
            if left_map.domain() is not left_factor or right_map.domain() is not right_factor:
                raise ValueError(
                    f"the maps out of the pushout {self} must start at {left_factor} and {right_factor}, but they "
                    f"start at {left_map.domain()} and {right_map.domain()}"
                )
            if left_map.codomain() is not right_map.codomain():
                raise ValueError(
                    f"the maps out of the pushout {self} must end at one algebra, but they end at "
                    f"{left_map.codomain()} and {right_map.codomain()}"
                )
            common_source = source_map.domain()
            for label in common_source.algebra_generating_set():
                element = common_source.algebra_generator(label)
                if left_map(source_map(element)) != right_map(target_map(element)):
                    raise ValueError(
                        f"the maps {left_map} and {right_map} do not agree on the common algebra "
                        f"{common_source}: they differ on its generator {element}"
                    )
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
                raise ValueError(
                    f"cannot view the module map {images} as an algebra morphism {domain} -> {codomain}: it is a "
                    f"map {images.domain()} -> {images.codomain()}"
                )

            labels = domain.module_generating_set()
            size = labels.cardinality()
            assert size.is_finite(), (
                f"checking that {images} is multiplicative needs finitely many module generators of {domain}, "
                f"but it has {size}"
            )
            if images(domain.one()) != codomain.one():
                raise ValueError(
                    f"{images} is not a unital algebra morphism: it sends 1 to {images(domain.one())}, not to "
                    f"{codomain.one()}"
                )
            for left_label in labels:
                left = domain.module_generator(left_label)
                for right_label in labels:
                    right = domain.module_generator(right_label)
                    if images(left * right) != images(left) * images(right):
                        raise ValueError(
                            f"{images} is not an algebra morphism: f({left} * {right}) != f({left}) * f({right})"
                        )
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
                raise ValueError(
                    f"cannot view {images} as an algebra morphism {domain} -> {codomain}: it is a map "
                    f"{images.domain()} -> {images.codomain()}"
                )
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
            f"{domain} has no chosen algebra generators, so a morphism out of it must be given as a ring "
            f"map, not as {images!r}"
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
                raise TypeError(
                    f"a dictionary of generator images needs finitely many algebra generators of {domain}, but it "
                    f"has {labels.cardinality()}; give a function or an indexed family"
                )
            missing = [label for label in labels if label not in images]
            if missing:
                raise ValueError(
                    f"the images of the algebra generators of {domain} must be given for every generator, but "
                    f"{missing} are missing"
                )
            self._generator_images = indexed_family(
                labels,
                lambda label: codomain(images[label]),
                name="Generator images",
            )
        elif isinstance(images, (tuple, list)):
            size = labels.cardinality()
            if not size.is_finite():
                raise TypeError(
                    f"a list of generator images needs finitely many algebra generators of {domain}, but it has "
                    f"{size}; give a function or an indexed family"
                )
            values = tuple(images)
            if len(values) != int(size.finite_value()):
                raise ValueError(
                    f"{domain} has {size} algebra generators, but {len(values)} images were given"
                )
            if labels not in EnumeratedSets():
                raise TypeError(
                    f"a list of generator images needs the algebra generators of {domain} in a fixed order, but "
                    f"{labels} is not ordered"
                )
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
            raise TypeError(
                f"a morphism {domain} -> {codomain} of algebras is given by the images of the algebra "
                f"generators, but got {images!r}"
            )

        assert engine_domain in SageRings() and engine_codomain in SageRings(), (
            f"a morphism {domain} -> {codomain} given by generator images is computed only between rings "
            "that Sage can compute with; use the category of free algebras or of algebras given by "
            "generators and relations"
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
            f"{self} has no images of algebra generators: its domain {self.domain()} has no chosen "
            "algebra generators"
        )
        return SetMorphism(
            Sets().Mor(self.domain().algebra_generating_set(), self.codomain()),
            self._generator_images.value,
        )

    def algebra_generator_images(self):
        assert self._generator_images is not None, (
            f"{self} has no images of algebra generators: its domain {self.domain()} has no chosen "
            "algebra generators"
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
            raise ValueError(
                f"an algebra given by generators and relations needs finitely many generators, but "
                f"{domain} has {size}"
            )
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
                raise ValueError(
                    f"the images of the algebra generators of {domain} must be given for every generator, but "
                    f"{missing} are missing"
                )
            selected = indexed_family(
                labels,
                lambda label: self.codomain()(images[label]),
                name="Generator images",
            )
        elif isinstance(images, (tuple, list)):
            values = tuple(images)
            if len(values) != int(size.finite_value()):
                raise ValueError(
                    f"{domain} has {size} algebra generators, but {len(values)} images were given"
                )
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
            raise TypeError(
                f"a morphism out of {domain} is given by the images of its algebra generators, but got {images!r}"
            )
        self._generator_images = selected
        self._presentation_map = Algebras(domain.presentation_ring().base_ring()).Associative().Unital().Mor(domain.presentation_ring(), self.codomain())(selected)
        zero = self.codomain().zero()
        for relation in domain.relations():
            if self._presentation_map(relation) != zero:
                raise ValueError(
                    f"the generator images do not define a morphism out of {domain}: the relation {relation} is "
                    f"sent to {self._presentation_map(relation)}, not to 0"
                )

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


class _AlgebraMorCommonMethods:
    r"""Shared equality protocol for represented algebra Mor parents."""

    def _from_degree_preserving_generator_map(self, images):
        r"""Construct from a structurally degree-preserving generator map."""
        return self(images)


def _corestrict_algebra_morphism_to_center(morphism):
    r"""Return the unique represented ring-map factor ``A -> Z(B)`` of ``morphism``.

    The source must carry a chosen algebra generating family, because centrality
    is verified on that family.  Scalars already land centrally because
    ``morphism`` is an algebra map, so checking the selected algebra generators
    proves that its whole image lies in ``Z(B)``.  The factor is returned in the
    owned ring Mor category, matching the mathematical codomain ``ring_center``
    rather than requiring that the predicate centre carry a second algebra
    presentation.
    """
    domain = morphism.domain()
    codomain = morphism.codomain()
    base = domain.base_ring()
    assert domain in FramedAlgebras(base), (
        f"the corestriction of {morphism} to the centre of {codomain} needs chosen algebra generators "
        f"of {domain}"
    )
    labels = domain.algebra_generating_set()
    assert labels.cardinality().is_finite(), (
        f"the corestriction of {morphism} to the centre of {codomain} needs finitely many algebra "
        f"generators of {domain}, but it has {labels.cardinality()}"
    )
    center = codomain.ring_center()
    for label in labels:
        image = morphism(domain.algebra_generator(label))
        if image not in center:
            raise ValueError(
                f"{morphism} does not land in the centre of {codomain}: the image {image} of the generator "
                f"{label} is not central"
            )
    return domain.Mor(center)(lambda element: center(morphism(element)))


class PresentedAlgebraMor(_AlgebraMorCommonMethods, CategoricalMor):
    Element = PresentedAlgebraMorphism

    def __init__(self, mor_family, domain, codomain) -> None:
        CategoricalMor.__init__(
            self,
            mor_family,
            domain,
            codomain,
        )

    def _element_constructor_(self, images):
        return self.element_class(self, images)

    @cached_method
    def identity(self):
        r"""Return the identity of this endomorphism Mor.

        The identity of an object needs no framing: an unframed algebra such as
        the integers regarded over themselves has no algebra generating set,
        and its identity is still the identity.  A Mor object has one identity,
        so this is cached.
        """
        if self.domain() is not self.codomain():
            raise ValueError(
                f"the identity morphism exists only on Mor(A, A), but this is Mor({self.domain()}, {self.codomain()})"
            )
        domain = self.domain()
        if domain in FramedAlgebras(domain.base_ring()):
            return self(lambda label: domain.algebra_generator(label))
        engine = _engine_ring(domain)
        return self(engine.hom(engine))


class AlgebraMor(_AlgebraMorCommonMethods, CategoricalMor):
    Element = AlgebraMorphism

    def __init__(self, mor_family, domain, codomain) -> None:
        CategoricalMor.__init__(
            self,
            mor_family,
            domain,
            codomain,
        )

    def _element_constructor_(self, images):
        return self.element_class(self, images)

    def _from_constructed_element_map(self, evaluator):
        r"""Construct an algebra map whose supplying construction proves the algebra laws.

        This protected route is for canonical maps such as the factorial
        comparison ``Gamma(M) -> Sym(M)``.  It retains the ordinary algebra-Mor
        parent and an actual owned set map; arbitrary user element functions do
        not enter through this route.
        """
        if not callable(evaluator):
            raise TypeError(
                f"a morphism {self.domain()} -> {self.codomain()} needs a map on elements, but {evaluator!r} "
                "is not callable"
            )
        represented = SetMorphism(
            Sets().Mor(self.domain(), self.codomain()),
            lambda element: self.codomain()(evaluator(self.domain()(element))),
        )
        return self.element_class(self, represented)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"the identity morphism exists only on Mor(A, A), but this is Mor({self.domain()}, {self.codomain()})"
            )
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
        law_decisions=(),
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
        selected_labels = None if labels is None else finite_ordered_set(labels)
        associative = Algebras(base).Associative().Unital()
        framing_owner = associative
        placement = [associative]
        if engine in SageCommutativeAlgebras(_engine_ring(base)):
            framing_owner = associative.Commutative()
            placement.append(framing_owner)
        if labels is not None:
            placement.append(framing_owner.Framed())
        placement.extend(categories)
        retained_laws = {"associativity": True, "unit": True}
        if framing_owner is not associative:
            retained_laws["commutativity"] = True
        retained_laws.update(dict(law_decisions))
        _OwnedRingParent.__init__(
            self,
            engine,
            base=base,
            category=Cat().meet(tuple(placement)),
        )
        Algebras.ParentMethods._retain_algebra_law_decisions(
            self, retained_laws
        )
        if labels is None:
            if generator_values is not None:
                raise ValueError(
                    f"the algebra {engine} over {base_ring} has no chosen generators, so it cannot be given "
                    "generator values"
                )
            return

        label_size = selected_labels.cardinality()
        if not label_size.is_finite():
            raise TypeError(
                f"the algebra {engine} over {base_ring} needs finitely many generators, but has {label_size}"
            )

        if generator_values is None:

            def value(label):
                position = int(selected_labels.ranking_map()(label))
                return self._from_engine_element(engine.gen(position))
        else:
            if hasattr(generator_values, "index_set") and callable(getattr(generator_values, "value", None)):
                if generator_values.cardinality() != label_size:
                    raise ValueError(
                        f"the algebra {engine} has {label_size} generators, but {generator_values.cardinality()} "
                        "generator values were given"
                    )

                def value(label):
                    return self(generator_values.value(selected_labels.ranking_map()(label)))
            elif callable(generator_values):

                def value(label):
                    raw = generator_values(label)
                    return raw if getattr(raw, "parent", lambda: None)() is self else self._from_engine_element(raw)
            elif isinstance(generator_values, (tuple, list)):
                if len(generator_values) != int(label_size.finite_value()):
                    raise ValueError(
                        f"the algebra {engine} has {label_size} generators, but {len(generator_values)} generator "
                        "values were given"
                    )
                # Explicit finite ingress is parsed by position; the Python
                # sequence is not retained as the mathematical family.
                by_position = {position: generator_values[position] for position in range(len(generator_values))}

                def value(label):
                    raw = by_position[int(selected_labels.ranking_map()(label))]
                    return raw if getattr(raw, "parent", lambda: None)() is self else self._from_engine_element(raw)
            else:
                raise TypeError(
                    f"generator values of the algebra {engine} are given by a function, an indexed family, or a "
                    f"list, but got {generator_values!r}"
                )

        generator_morphism = Sets().Mor(selected_labels, self)(value)
        self._algebra_framing_owner = framing_owner
        selected_presentation = self.__dict__.get("_selected_algebra_presentation")
        if selected_presentation is not None:
            source = selected_presentation.presentation_ring()

            def framing_morphism():
                return selected_presentation.presentation_morphism()

        elif self.__dict__.get("_native_free_flavor") is not None:
            source = self

            def framing_morphism():
                return source.Mor(self)(generator_morphism)

        else:
            generating_module = base.free_module(selected_labels)
            match framing_owner is associative:
                case True:
                    source = generating_module.tensor_algebra()
                case False:
                    source = generating_module.symmetric_algebra()

            def framing_morphism():
                return source.Mor(self)(generator_morphism)

        _fix_selected_framing(
            self,
            framing_owner,
            source,
            selected_labels,
            lambda: generator_morphism,
            framing_morphism,
        )



@cached_function
def _owned_algebra_view(
    engine,
    base_ring,
    labels=None,
    categories=(),
    construction_data=(),
    law_decisions=(),
):
    base = _owned_ring(base_ring)
    return _OwnedAlgebraParent(
        engine,
        base,
        labels,
        categories=tuple(categories),
        construction_data=tuple(construction_data),
        law_decisions=tuple(law_decisions),
    )


def _refine_algebra(
    algebra,
    base_ring,
    labels=None,
    *categories,
    construction_data=(),
):
    r"""Construct an owned algebra view with its selected categories present.

    Native representation boundary: a free polynomial/word realization
    retains its exact generating module and monomial frame when a further
    construction (for example a coproduct) adds its datum.  An unchanged
    view is the existing object.  Other scalar structures retain their own
    native algebra constructor, without assuming a monomial basis.
    """
    base = _owned_ring(base_ring)
    specialized = algebra._refined_specialized_algebra(
        base,
        labels,
        tuple(categories),
        tuple(construction_data),
    )
    if specialized is not None:
        return specialized
    return _owned_algebra_view(
        _engine_ring(algebra),
        base,
        labels,
        tuple(categories),
        tuple(construction_data),
    )


class _ScalarAlgebraEngine:
    r"""Native ring conversion for an algebra built on a scalar-action module.

    Engine adapter (``OWN-06``).  The module owner supplies all arithmetic and
    the algebra root supplies multiplication.  This class only reads native
    ring data and translates elements between that realization and the exact
    module used at the algebra entry.
    """

    def __init__(self, native_ring, **rest) -> None:
        self._native_ring = native_ring
        self._preamble_engine_ring = _engine_ring(native_ring)
        super().__init__(**rest)

    def _element_constructor_(self, value):
        source = element_parent(value)
        if source is self:
            return value
        if source in Modules(self.base_ring()) and self._built_on_the_same_data(source):
            return super()._element_constructor_(value)
        module_value = self.unformed_module()(self._native_ring(value))
        return super()._element_constructor_(module_value)

    def _from_engine_element(self, value):
        return self(_owned_engine_element(self._native_ring, value))

    def _engine_element(self, value):
        module_element = self.unformed_module()(self(value))
        return _engine_element(self._native_ring, module_element.underlying_element())

    def _repr_(self):
        return f"{self._native_ring} as an algebra over {self.base_ring()}"


@cached_function(key=lambda ring, structure_map: (id(ring), id(structure_map)))
def _algebra_structure_view(ring, structure_map):
    r"""The R-algebra defined by the central ring map ``R -> ring``.

    First construct its R-module from the additive group and the given scalar
    action.  The product of the original ring is R-bilinear because the scalar
    image is central.  Classify it at the tensor owner and supply that module,
    classifier and unit to the single algebra entry.  Native conversion is a
    private realization of this result, not a second algebra constructor.
    """
    from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring_category

    selected_ring = _own_ring(ring)
    assert structure_map.codomain() is selected_ring, (
        f"the structure map R -> A of an algebra must end at A = {selected_ring}, but {structure_map} "
        f"ends at {structure_map.codomain()}"
    )
    base = _own_ring(structure_map.domain())
    assert base in OwnedRings().Commutative(), (
        f"{selected_ring} is an algebra over {base} through {structure_map} only if {base} is "
        "commutative, and it is not known to be"
    )
    center = selected_ring.ring_center()

    def scalar_action(scalar, element):
        central_scalar = center(structure_map(base(scalar)))
        return selected_ring(central_scalar) * selected_ring(element)

    additive_group = selected_ring.underlying_additive_group()
    additive_endomorphisms = AdditiveGroups().AdditiveCommutative().End(additive_group)
    rho = base.Mor(additive_endomorphisms, category=OwnedRings())(
        lambda scalar: additive_endomorphisms.elementwise(
            lambda element: scalar_action(scalar, element)
        )
    )
    module = Modules(base)(rho)
    tensor = Modules(base).tensor_product((module, module))
    multiplication = tensor.from_bilinear_map(
        module, lambda left, right: module(left.underlying_element() * right.underlying_element()),
    )
    algebras = Algebras(base).Associative().Unital()
    law_decisions = {"associativity": True, "unit": True}
    if selected_ring in OwnedRings().Commutative():
        algebras = algebras.Commutative()
        law_decisions["commutativity"] = True
    category = Cat().meet((
        algebras, _owned_ring_category(_engine_ring(selected_ring), scalar_base=base),
    ))
    return _algebra_on_module(
        module, multiplication, placement=(category,),
        unit=module(selected_ring.one()),
        construction_data={
            "_engine": (Algebras(base), _ScalarAlgebraEngine, None),
            "native_ring": selected_ring,
        },
        law_decisions=law_decisions,
    )


def _unit_from_multiplication(multiplication):
    from sage.matrix.constructor import matrix as sage_matrix
    from sage.modules.free_module_element import vector as sage_vector

    module = multiplication.codomain()
    tensor_square = multiplication.domain()
    labels = module.module_generating_set()
    size = labels.cardinality()
    if not size.is_finite():
        raise TypeError(
            f"the unit of the algebra with multiplication {multiplication} is computed from finitely many "
            f"module generators of {module}, but it has {size}"
        )
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
        raise TypeError(
            f"the multiplication {multiplication} on {module} has no left unit"
        ) from error
    unit = module.linear_combination({labels[index]: _owned_engine_element(ring, engine(coefficients[index])) for index in range(rank) if coefficients[index]})
    for label in labels:
        generator = module.module_generator(label)
        if multiplication(tensor_square.pure_tensor(generator, unit)) != generator:
            raise TypeError(
                f"the multiplication {multiplication} on {module} has no two-sided unit: the left unit {unit} "
                f"fails on the generator {generator}"
            )
    return unit


@cached_function
def _own_algebra(structure_map):
    r"""Return the codomain of the ring map ``R -> A`` read as an ``R``-algebra through it."""
    if not isinstance(structure_map, Map):
        raise TypeError(
            f"an algebra is given by its structure map R -> A, but {structure_map!r} is not a ring map"
        )
    base = _owned_ring(structure_map.domain())
    if (
        structure_map.codomain() is base
        and base.base_ring() is base
        and structure_map is base.Mor(base).identity()
    ):
        # The existing regular scalar structure is literally id_R.  Creating
        # another engine view here would replace its exact ring endpoint.
        placement = Algebras(base).Associative().Unital()
        if base in OwnedRings().Commutative():
            placement = placement.Commutative()
        match base in placement:
            case True:
                return base
            case False:
                return refine(base, placement)
    return _algebra_structure_view(structure_map.codomain(), structure_map)


def _engine_algebra_morphism_from_generator_images(domain, codomain, generator_images):
    r"""Realize a framed owned algebra map in Sage when both engines exist.

    This is a private bridge boundary.  The mathematical datum is the owned
    generator map; Sage receives only engine endpoints and engine elements.
    """
    engine_domain = _engine_ring(domain)
    engine_codomain = _engine_ring(codomain)
    assert engine_domain in SageRings() and engine_codomain in SageRings(), (
        f"a morphism {domain} -> {codomain} given by generator images is computed only between rings "
        "Sage can compute with"
    )
    labels = domain.algebra_generating_set()
    assert labels.cardinality().is_finite(), (
        f"a morphism out of {domain} given by generator images needs finitely many algebra generators, "
        f"but it has {labels.cardinality()}"
    )

    base = domain.base_ring()
    engine_base = _engine_ring(base)
    target_structure = codomain.algebra_structure_morphism()

    def engine_base_image(scalar):
        owned_scalar = _owned_engine_element(base, engine_base(scalar))
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
                owned_generator = _owned_engine_element(domain, engine_generator)
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
        f"cannot compute with the algebra morphism {morphism}: its domain {domain} has no chosen "
        "algebra generators"
    )
    images = {label: morphism(domain.algebra_generator(label)) for label in domain.algebra_generating_set()}
    return _engine_algebra_morphism_from_generator_images(domain, morphism.codomain(), images)


def _engine_morphism_from_generator_images(engine_domain, engine_codomain, images, base_map):
    r"""Construct a native Sage ring morphism at the engine boundary."""
    assert engine_domain in SageRings() and engine_codomain in SageRings(), (
        f"a ring morphism given by generator images needs rings Sage can compute with, but got "
        f"{engine_domain} and {engine_codomain}"
    )
    return engine_domain.hom(
        [engine_codomain(image) for image in images],
        engine_codomain,
        base_map=base_map,
    )


__all__ = [
    "AlgebraMor",
    "AlgebraMorphism",
    "Algebras",
    "AlgebrasWithChosenFinitePresentation",
    "CommutativeAlgebraCoproducts",
    "CommutativeAlgebraPushouts",
    "FinitelyPresentedAlgebras",
    "FramedAlgebras",
    "MatrixAlgebras",
    "MultiplicativeAlgebraMor",
    "UnitalMultiplicativeAlgebraMor",
]
