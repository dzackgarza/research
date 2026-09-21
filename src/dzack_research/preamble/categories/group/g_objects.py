r"""Internal group objects and external abstract-group actions.

For a category ``C`` with represented finite products, ``Grp(C)`` is the
category of internal group objects: an object ``G`` of ``C`` with multiplication,
unit, and inverse morphisms satisfying the group diagrams.  Actions of such an
internal group are morphisms ``G x X -> X`` satisfying the action diagrams.

This is distinct from an action of an external abstract group:

For a group ``G`` and a category ``C``, a ``G``-action on an object ``X`` of
``C`` is a functor ``BG -> C`` selecting ``X``; equivalently a group morphism
``G -> Aut_C(X)`` (lean-categories FOUNDATIONS, Definition 34.1).  A morphism
of ``G``-objects is a morphism of ``C`` commuting with the two actions, so
``Mor_G(X, Y)`` is the fixed locus of ``G`` acting on ``Mor_C(X, Y)`` by
conjugation.  The forgetful functor to ``C`` is evaluation at the one object
of ``BG``.

The category of ``G``-sets is ``GObjects(G, Sets())``.  ``Modules(R[G])`` is
equivalent to ``GObjects(G, Modules(R))``, and an ``R[G]``-module is not an
object of it by inheritance: ``Modules(R[G]).restriction_along_group_inclusion()``
sends an ``R[G]``-module to its action ``G -> Aut_R(M)``,
``Modules(R[G]).linearization()`` extends a ``G``-action ``R``-linearly, and
``Modules(R[G]).linearization_equivalence()`` is the adjunction between them.
The generic constructor takes the actual functor ``BG -> C``.  Represented
specializations may retain their concrete underlying object, but expose that
same functor through ``action_functor()``; their private elementwise action
data are only a realization of the categorical action.
"""

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method
from sage.misc.unknown import Unknown
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    CategoryPacketMethods,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.categories.group.groups import (
    GroupsWithChosenFiniteGeneratingSet,
    GroupsWithChosenFinitePresentation,
    OwnedFiniteGroups,
    _owned_group,
)
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import _object_of


def _verify_relators(action, group, endomorphisms) -> None:
    r"""Check the represented action law without manufacturing presentation data.

    An action is a left action: ``rho(s_1 s_2) = rho(s_1) rho(s_2)``, the
    product of the matrices acting on an ordered basis.  A function on the
    generators extends to a group morphism exactly when every defining
    relator, composed in that order, is the identity.  When no presentation
    has been selected but the group is finite, the same claim is decided
    directly on all pairs.  Finite presentability alone never triggers a
    presentation search.
    """
    if group in GroupsWithChosenFinitePresentation():
        # Private serialization: Tietze letters index the chosen generators in
        # their recorded order, and a negative letter names an inverse.
        generators = tuple(group.group_generators())
        identity = endomorphisms.identity()
        for relator in group.defining_relations():
            composite = identity
            for letter in relator.Tietze():
                generator = generators[abs(int(letter)) - 1]
                composite = composite * action(
                    generator if int(letter) > 0 else ~generator
                )
            assert composite == identity, (
                f"the generator images do not satisfy the relator {relator}, "
                f"so they define no left action of {group}"
            )
        return
    if group in OwnedFiniteGroups():
        for left in group:
            for right in group:
                assert action(left * right) == action(left) * action(right), (
                    f"the stated maps do not define a left action of {group}"
                )


def _product_projections(construction):
    return tuple(
        construction.structure_morphism(index)
        for index in construction.diagram().domain().objects()
    )


def _factor_selected_product(construction, source, legs):
    legs = tuple(legs)
    diagram = construction.diagram()
    cone = diagram.ProductCones().cone(
        source,
        lambda index: legs[int(index.value())],
    )
    return construction.factor(cone).apex_map()


def _terminal_map(category, source):
    return _factor_selected_product(
        category.product_construction(()),
        source,
        (),
    )


class InternalGroupObjectMorphism(Morphism):
    r"""A morphism of internal group objects preserving all group structure."""

    def __init__(self, parent, arrow) -> None:
        Morphism.__init__(self, parent)
        self._arrow = arrow

    def underlying_arrow(self):
        return self._arrow

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        return self.parent().hom_family().Of(
            other.domain(),
            self.codomain(),
        )(
            self.underlying_arrow() * other.underlying_arrow()
        )

    def _repr_(self):
        return f"Internal-group morphism induced by {self.underlying_arrow()}"


class InternalGroupObjectHomset(CategoricalHomset):
    r"""Morphisms in the category of internal group objects."""

    Element = InternalGroupObjectMorphism

    def underlying_homset(self):
        category = self.domain().underlying_category()
        return category.Mor(
            self.domain().underlying_object(),
            self.codomain().underlying_object(),
        )

    def _element_constructor_(self, arrow):
        source = self.domain()
        target = self.codomain()
        arrow = self.underlying_homset()(arrow)

        source_square = source.square_construction()
        target_square = target.square_construction()
        first, second = _product_projections(source_square)
        arrow_times_arrow = _factor_selected_product(
            target_square,
            source_square.object(),
            (arrow * first, arrow * second),
        )
        if (
            arrow * source.multiplication()
            != target.multiplication() * arrow_times_arrow
        ):
            raise ValueError(
                "the underlying morphism does not preserve internal-group multiplication"
            )
        if arrow * source.unit_morphism() != target.unit_morphism():
            raise ValueError(
                "the underlying morphism does not preserve the internal-group unit"
            )
        if (
            arrow * source.inverse_morphism()
            != target.inverse_morphism() * arrow
        ):
            raise ValueError(
                "the underlying morphism does not preserve internal-group inversion"
            )
        return self.element_class(self, arrow)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an internal-group endomorphism Hom")
        return self(self.underlying_homset().identity())


class InternalGroupObjectHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return InternalGroupObjectHomset


class InternalGroupObjects(CategoryPacketMethods, OwnedCategory):
    r"""Internal group objects in a category with represented finite products.

    The data are an object G of C and owned C-morphisms m:GxG->G,
    e:1->G, and i:G->G satisfying the group diagrams.  This is distinct
    from GObjects: an action of an external abstract group is a functor BG->C.
    """

    @staticmethod
    def __classcall__(cls, category):
        return Category.__classcall__(cls, category)

    def __init__(self, category) -> None:
        self._underlying_category = category
        OwnedCategory.__init__(self)

    def underlying_category(self):
        return self._underlying_category

    def super_categories(self):
        return [Objects()]

    def _repr_object_names(self):
        return f"internal group objects in {self.underlying_category()}"

    _HomCategory = InternalGroupObjectHomCategoryConstruction

    def _call_(self, underlying_object, multiplication, unit, inverse):
        return _object_of(
            self,
            _engine=(self, _InternalGroupObjectEngine, None),
            underlying_object=underlying_object,
            multiplication=multiplication,
            unit=unit,
            inverse=inverse,
        )

    def an_object(self):
        category = self.underlying_category()
        terminal = category.product_construction(())
        underlying = terminal.object()
        square = category.product_construction((underlying, underlying))
        multiplication = _terminal_map(category, square.object())
        identity = category.Mor(underlying, underlying).identity()
        return self(underlying, multiplication, identity, identity)


class _InternalGroupObjectEngine:
    def __init__(self, underlying_object, multiplication, unit, inverse, **rest) -> None:
        category = rest["category"].underlying_category()
        if underlying_object not in category:
            raise TypeError("an internal group object must be an object of its underlying category")
        self._underlying_object = underlying_object
        self._square_construction = category.product_construction(
            (underlying_object, underlying_object)
        )
        self._terminal_construction = category.product_construction(())
        self._multiplication = category.Mor(
            self._square_construction.object(),
            underlying_object,
        )(multiplication)
        self._unit = category.Mor(
            self._terminal_construction.object(),
            underlying_object,
        )(unit)
        self._inverse = category.Mor(
            underlying_object,
            underlying_object,
        )(inverse)
        super().__init__(**rest)
        self._verify_group_diagrams()

    def underlying_category(self):
        return self.category().underlying_category()

    def underlying_object(self):
        return self._underlying_object

    def square_construction(self):
        return self._square_construction

    def terminal_construction(self):
        return self._terminal_construction

    def multiplication(self):
        return self._multiplication

    def unit_morphism(self):
        return self._unit

    def inverse_morphism(self):
        return self._inverse

    def _verify_group_diagrams(self):
        category = self.underlying_category()
        group = self.underlying_object()
        multiplication = self.multiplication()
        square = self.square_construction()
        triple = category.product_construction((group, group, group))
        first, second, third = _product_projections(triple)

        first_pair = _factor_selected_product(
            square,
            triple.object(),
            (first, second),
        )
        second_pair = _factor_selected_product(
            square,
            triple.object(),
            (second, third),
        )
        first_product = multiplication * first_pair
        second_product = multiplication * second_pair
        multiply_first = multiplication * _factor_selected_product(
            square,
            triple.object(),
            (first_product, third),
        )
        multiply_second = multiplication * _factor_selected_product(
            square,
            triple.object(),
            (first, second_product),
        )
        if multiply_first != multiply_second:
            raise ValueError("internal-group multiplication is not associative")

        identity = category.Mor(group, group).identity()
        unit_on_group = self.unit_morphism() * _terminal_map(category, group)
        left_unit = multiplication * _factor_selected_product(
            square,
            group,
            (unit_on_group, identity),
        )
        right_unit = multiplication * _factor_selected_product(
            square,
            group,
            (identity, unit_on_group),
        )
        if left_unit != identity or right_unit != identity:
            raise ValueError("internal-group multiplication does not satisfy the unit laws")

        inverse = self.inverse_morphism()
        left_inverse = multiplication * _factor_selected_product(
            square,
            group,
            (inverse, identity),
        )
        right_inverse = multiplication * _factor_selected_product(
            square,
            group,
            (identity, inverse),
        )
        if left_inverse != unit_on_group or right_inverse != unit_on_group:
            raise ValueError("internal-group inverse does not satisfy the inverse laws")

    def actions(self):
        return InternalGroupActions(self)

    def Mor(self, target):
        return self.category().Mor(self, target)

    def _repr_(self):
        return f"Internal group object on {self.underlying_object()}"


class InternalGroupActionMorphism(Morphism):
    r"""An equivariant morphism between actions of one internal group object."""

    def __init__(self, parent, arrow) -> None:
        Morphism.__init__(self, parent)
        self._arrow = arrow

    def underlying_arrow(self):
        return self._arrow

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        return self.parent().hom_family().Of(
            other.domain(),
            self.codomain(),
        )(
            self.underlying_arrow() * other.underlying_arrow()
        )


class InternalGroupActionHomset(CategoricalHomset):
    Element = InternalGroupActionMorphism

    def underlying_homset(self):
        category = self.domain().group_object().underlying_category()
        return category.Mor(
            self.domain().underlying_object(),
            self.codomain().underlying_object(),
        )

    def _element_constructor_(self, arrow):
        source = self.domain()
        target = self.codomain()
        arrow = self.underlying_homset()(arrow)
        source_product = source.action_product_construction()
        target_product = target.action_product_construction()
        group_leg, point_leg = _product_projections(source_product)
        identity_times_arrow = _factor_selected_product(
            target_product,
            source_product.object(),
            (group_leg, arrow * point_leg),
        )
        if (
            arrow * source.action_morphism()
            != target.action_morphism() * identity_times_arrow
        ):
            raise ValueError("the underlying morphism is not equivariant for the internal-group actions")
        return self.element_class(self, arrow)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an internal-action endomorphism Hom")
        return self(self.underlying_homset().identity())


class InternalGroupActionHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return InternalGroupActionHomset


class InternalGroupActions(CategoryPacketMethods, OwnedCategory):
    r"""Actions of one internal group object by morphisms GxX->X."""

    @staticmethod
    def __classcall__(cls, group_object):
        return Category.__classcall__(cls, group_object)

    def __init__(self, group_object) -> None:
        self._group_object = group_object
        OwnedCategory.__init__(self)

    def group_object(self):
        return self._group_object

    def super_categories(self):
        return [Objects()]

    def _repr_object_names(self):
        return f"objects acted on by {self.group_object()}"

    _HomCategory = InternalGroupActionHomCategoryConstruction

    def _call_(self, underlying_object, action_morphism):
        return _object_of(
            self,
            _engine=(self, _InternalGroupActionEngine, None),
            underlying_object=underlying_object,
            action_morphism=action_morphism,
        )

    def an_object(self):
        category = self.group_object().underlying_category()
        terminal = category.product_construction(()).object()
        action_product = category.product_construction(
            (self.group_object().underlying_object(), terminal)
        )
        _group_projection, point_projection = _product_projections(action_product)
        return self(terminal, point_projection)


class _InternalGroupActionEngine:
    def __init__(self, underlying_object, action_morphism, **rest) -> None:
        group = rest["category"].group_object()
        category = group.underlying_category()
        if underlying_object not in category:
            raise TypeError("an internal group acts on an object of its underlying category")
        self._underlying_object = underlying_object
        self._action_product_construction = category.product_construction(
            (group.underlying_object(), underlying_object)
        )
        self._action_morphism = category.Mor(
            self._action_product_construction.object(),
            underlying_object,
        )(action_morphism)
        super().__init__(**rest)
        self._verify_action_diagrams()

    def group_object(self):
        return self.category().group_object()

    def underlying_object(self):
        return self._underlying_object

    def action_product_construction(self):
        return self._action_product_construction

    def action_morphism(self):
        return self._action_morphism

    def _verify_action_diagrams(self):
        group = self.group_object()
        category = group.underlying_category()
        group_object = group.underlying_object()
        acted = self.underlying_object()
        action = self.action_morphism()
        group_times_acted = self.action_product_construction()
        triple = category.product_construction((group_object, group_object, acted))
        first, second, point = _product_projections(triple)

        multiplied = group.multiplication() * _factor_selected_product(
            group.square_construction(),
            triple.object(),
            (first, second),
        )
        via_multiplication = action * _factor_selected_product(
            group_times_acted,
            triple.object(),
            (multiplied, point),
        )
        inner_action = action * _factor_selected_product(
            group_times_acted,
            triple.object(),
            (second, point),
        )
        via_action = action * _factor_selected_product(
            group_times_acted,
            triple.object(),
            (first, inner_action),
        )
        if via_multiplication != via_action:
            raise ValueError("the internal-group action is not associative")

        identity = category.Mor(acted, acted).identity()
        unit_on_acted = group.unit_morphism() * _terminal_map(category, acted)
        via_unit = action * _factor_selected_product(
            group_times_acted,
            acted,
            (unit_on_acted, identity),
        )
        if via_unit != identity:
            raise ValueError("the internal-group unit does not act as the identity")

    def Mor(self, target):
        return self.category().Mor(self, target)


def Grp(category):
    r"""Return the category of internal group objects in category."""
    return InternalGroupObjects(category)


class EquivariantMorphism(Morphism):
    r"""A morphism of ``C`` between two ``G``-objects that commutes with the actions."""

    def __init__(self, parent, arrow) -> None:
        Morphism.__init__(self, parent)
        self._arrow = arrow

    def underlying_arrow(self):
        r"""Return the same morphism read in the underlying category."""
        return self._arrow

    def natural_transformation(self):
        r"""Return the corresponding natural transformation between action functors."""
        from dzack_research.preamble.categories.functors.core import NaturalTransformation

        return NaturalTransformation(
            self.domain().action_functor(),
            self.codomain().action_functor(),
            lambda _obj: self.underlying_arrow(),
        ).morphism()

    def _call_(self, element):
        return self._arrow(element)

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        homset = self.parent().hom_family().Of(other.domain(), self.codomain())
        return homset._from_equivariant_arrow(self.underlying_arrow() * other.underlying_arrow())

    def __eq__(self, other) -> bool:
        r"""Equal when the underlying morphisms of ``C`` are; ``other`` may be either."""
        match other:
            case EquivariantMorphism():
                other = other.underlying_arrow()
        return self.underlying_arrow() == other

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        return hash((id(self.parent()), id(self)))

    def _repr_(self) -> str:
        return f"Equivariant {self.underlying_arrow()}"


class ExternalInternalActionComparison(SageObject):
    r"""Comparison of an external Set-action with its internal-group action."""

    def __init__(self, external_object, internal_group, internal_action) -> None:
        self._external_object = external_object
        self._internal_group = internal_group
        self._internal_action = internal_action

    def external_object(self):
        return self._external_object

    def internal_group_object(self):
        return self._internal_group

    def internal_action(self):
        return self._internal_action


class GObjectHomset(CategoricalHomset):
    r"""The represented ``Mor_G(X, Y)``: the equivariant morphisms of ``C``.

    Equivariance is decided on a determining family of the acting group:
    selected generators when present, or every element when the group is
    represented as finite.
    """

    Element = EquivariantMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        assert domain.acting_group() is codomain.acting_group(), "equivariant morphisms require one acting group"
        CategoricalHomset.__init__(self, hom_family, domain, codomain)

    def underlying_homset(self):
        r"""Return ``Mor_C(U(X), U(Y))``, where equivariant maps live.

        A concrete ``G``-object need not itself be an object of ``C``: an
        ``R[G]``-module, for example, reaches ``Mod_R`` by restriction of
        scalars.  Evaluation of the represented action functor is the common
        forgetful construction for both generic functor-category objects and
        concrete specializations, so use that rather than treating the acted
        wrapper as its own underlying object.
        """
        category = self.hom_family().base_category()
        forget = category.forgetful_functor()
        source = forget(self.domain())
        target = forget(self.codomain())
        return category.underlying_category().Mor(source, target)

    def is_equivariant(self, arrow):
        r"""Decide ``f rho_X(g) = rho_Y(g) f`` on a determining family of ``G``."""
        group = self.domain().acting_group()
        arrow = self.underlying_homset()(arrow)
        match group:
            case _ if group in GroupsWithChosenFiniteGeneratingSet():
                determining = group.group_generators()
            case _ if group.is_finite() is True:
                determining = group
            case _:
                return Unknown
        return all(
            arrow * self.domain().action_of(element)
            == self.codomain().action_of(element) * arrow
            for element in determining
        )

    def _from_equivariant_arrow(self, arrow):
        r"""Wrap an arrow whose equivariance follows from its construction."""
        return self.element_class(self, arrow)

    def _element_constructor_(self, datum):
        arrow = self.underlying_homset()(datum)
        if self.is_equivariant(arrow) is not True:
            raise ValueError(f"{arrow} does not commute with the {self.domain().acting_group()}-actions")
        return self._from_equivariant_arrow(arrow)

    def identity(self):
        assert self.domain() is self.codomain(), "identity belongs to an endomorphism Hom-set"
        return self._from_equivariant_arrow(self.underlying_homset().identity())

    def _repr_(self) -> str:
        return f"Mor_{self.domain().acting_group()}({self.domain()}, {self.codomain()})"


class GObjectHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return GObjectHomset


class GObjects(CategoryPacketMethods, OwnedCategory):
    r"""The category of objects of ``C`` with a chosen ``G``-action."""

    @staticmethod
    def __classcall__(cls, group, category):
        return Category.__classcall__(cls, _owned_group(group), category)

    def __init__(self, group, category) -> None:
        self._group = group
        self._category = category
        OwnedCategory.__init__(self)

    def acting_group(self):
        return self._group

    def underlying_category(self):
        r"""Return ``C``, the codomain of the forgetful functor."""
        return self._category

    def super_categories(self):
        return [self.underlying_category()]

    def _repr_object_names(self):
        return f"{self.acting_group()}-objects in {self.underlying_category()._repr_object_names()}"

    _HomCategory = GObjectHomCategoryConstruction

    def functor_category(self):
        r"""Return the represented functor category ``[BG,C]``."""
        return Cat().Mor(
            self.acting_group().classifying_category(),
            self.underlying_category(),
        )

    def __contains__(self, candidate) -> bool:
        if candidate in self.functor_category():
            return True
        return super().__contains__(candidate)

    def _call_(self, action_functor):
        r"""Construct a ``G``-object from an actual functor ``BG -> C``."""
        return self.functor_category().object(action_functor)

    def Mor(self, source, target):
        r"""Equivariant morphisms, as natural transformations on generic actions."""
        functors = self.functor_category()
        if source in functors and target in functors:
            return functors.Mor(source, target)
        return CategoryPacketMethods.Mor(self, source, target)

    def forgetful_functor(self):
        r"""Evaluation at the unique object, ``GObjects(G,C) -> C``."""
        from dzack_research.preamble.categories.functors.group_actions import (
            ForgetGroupActionFunctor,
        )

        return ForgetGroupActionFunctor(self.acting_group(), self.underlying_category())

    def internal_action_comparison(self, acted_object):
        r"""Compare an external action with an internal action when the constant group exists.

        The represented comparison is currently supplied for Set, where an
        abstract group is itself an internal group object on its underlying set.
        Finite products alone do not construct a constant group object in an
        arbitrary category, so no conversion is inferred outside this regime.
        """
        if self.underlying_category() is not Sets():
            raise TypeError(
                "comparison with an internal action requires a represented constant internal group object; the current generic construction supplies it only in Set"
            )
        if acted_object not in self:
            raise TypeError("the compared object must carry this external group action")

        group = self.acting_group()
        product = Sets().product((group, group))
        multiplication = Sets().Mor(product, group)(
            lambda pair: pair[0] * pair[1]
        )
        terminal = Sets().product(())
        unit = Sets().Mor(terminal, group)(lambda _point: group.one())
        inverse = Sets().Mor(group, group)(lambda element: ~element)
        internal_group = Grp(Sets())(
            group,
            multiplication,
            unit,
            inverse,
        )

        underlying = self.forgetful_functor()(acted_object)
        action_product = Sets().product((group, underlying))
        functor = (
            acted_object
            if acted_object in self.functor_category()
            else acted_object.action_functor()
        )
        classifying = functor.domain()
        point = classifying.an_object()
        arrows = classifying.Mor(point, point)
        action = Sets().Mor(action_product, underlying)(
            lambda pair: functor(arrows(pair[0]))(pair[1])
        )
        internal_action = internal_group.actions()(underlying, action)
        return ExternalInternalActionComparison(
            acted_object,
            internal_group,
            internal_action,
        )

    def transport(self, functor):
        r"""Postcompose actions by ``functor: C -> D``."""
        from dzack_research.preamble.categories.functors.group_actions import (
            TransportGroupActionFunctor,
        )

        assert functor.domain() == self.underlying_category(), "transport must start in the underlying category"
        return TransportGroupActionFunctor(self.acting_group(), functor)

    def restriction(self, group_morphism):
        r"""Return ``phi^*: GObjects(G, C) -> GObjects(H, C)`` for ``phi: H -> G``.

        Restriction along a group morphism is the reindexing functor
        ``BH -> BG -> C``; it is defined for every ``phi``, not only for the
        inclusion of a subgroup.
        """
        from dzack_research.preamble.categories.functors.group_actions import (
            RestrictionOfGroupActionFunctor,
        )

        assert group_morphism.codomain() is self.acting_group(), f"{group_morphism} does not land in {self.acting_group()}, so it restricts no action of that group"
        return RestrictionOfGroupActionFunctor(
            group_morphism,
            self.underlying_category(),
        )

    def affine_quotient_functor(self):
        r"""Return ``(-)/G: GObjects(G, Sch_R) -> AffSch_R``.

        The quotient of one affine action and its universal property are owned
        by the affine specialization; the functor adds the action on
        equivariant morphisms, which that universal property determines.
        """
        from dzack_research.preamble.categories.schemes.quotients import (
            AffineQuotientFunctor,
        )
        from dzack_research.preamble.categories.schemes.schemes import (
            Schemes,
        )

        category = self.underlying_category()
        match category:
            case Schemes():
                return AffineQuotientFunctor(self.acting_group(), category.base_ring())
            case other:
                assert False, f"the affine quotient functor is a construction on schemes; {other} has no owned quotient by a group action"

    def an_object(self):
        r"""The trivial action on an object of the underlying category."""
        from dzack_research.preamble.categories.group.g_sets import FiniteGSets
        from dzack_research.preamble.categories.modules.pure.modules import Modules
        from dzack_research.preamble.categories.schemes.schemes import AffineGSchemes, Schemes

        category = self.underlying_category()
        sample = category.an_object()
        match category:
            case _ if category is Sets():
                return FiniteGSets(self.acting_group()).trivial(sample)
            case Schemes():
                return AffineGSchemes(self.acting_group(), category.base_ring()).an_object()
        assert category.is_subcategory(Modules(category.base_ring())), f"no owned constructor equips an object of {category} with a group action"
        ring = category.base_ring()
        group = self.acting_group()
        trivial = Modules(ring).trivial_action(group)(sample)
        return Modules(ring[group]).restriction_along_group_inclusion()(trivial)

    class ParentMethods:
        def __init__(self, acting_group, action, underlying_category, **rest) -> None:
            self._acting_group = acting_group
            self._action_datum = action
            self._underlying_category = underlying_category
            super().__init__(**rest)

        def acting_group(self):
            return self._acting_group

        def underlying_category(self):
            r"""Return the category in which this object is acted on."""
            return self._underlying_category

        @cached_method
        def action_functor(self):
            r"""Return this represented action as the actual functor ``BG -> C``."""
            from dzack_research.preamble.categories.functors.group_actions import (
                GroupActionFunctor,
            )

            endomorphisms = self.underlying_category().Mor(self, self)
            datum = self._action_datum
            functor = GroupActionFunctor(
                self.acting_group(),
                self.underlying_category(),
                self,
                lambda group_element: endomorphisms(datum(group_element)),
            )
            action = Sets().Mor(self.acting_group(), endomorphisms)(
                lambda group_element: functor(
                    functor.domain().Mor(
                        functor.domain().an_object(),
                        functor.domain().an_object(),
                    )(group_element)
                )
            )
            _verify_relators(action, self.acting_group(), endomorphisms)
            return functor

        @cached_method
        def action(self):
            r"""Return the chosen action as the set morphism ``G -> Mor_C(X, X)``.

            Its values are automorphisms of ``X`` in ``C``, and the action is
            a left action: ``rho(s_1 s_2) = rho(s_1) rho(s_2)``.  The generator
            images are checked against the group's chosen relators once, here.
            """
            endomorphisms = self.underlying_category().Mor(self, self)
            functor = self.action_functor()
            classifying = functor.domain()
            point = classifying.an_object()
            arrows = classifying.Mor(point, point)
            return Sets().Mor(self.acting_group(), endomorphisms)(lambda group_element: functor(arrows(group_element)))

        @cached_method
        def action_of(self, group_element):
            r"""Return the automorphism of ``X`` in ``C`` induced by ``group_element``."""
            assert group_element in self.acting_group(), f"{group_element} is not an element of {self.acting_group()}"
            return self.action()(group_element)

        def act(self, group_element, element):
            r"""Return ``group_element . element``."""
            assert element in self, f"{element} is not an element of {self}"
            return self.action_of(group_element)(element)

        def restrict_action(self, group_morphism):
            r"""Return this object acted on by ``H`` through ``phi: H -> G``."""
            category = GObjects(self.acting_group(), self.underlying_category())
            return category.restriction(group_morphism)(self)

        def _cyclic_restriction(self, group_element):
            r"""Return this object acted on by the cyclic subgroup ``<g> <= G``."""

            from dzack_research.preamble.categories.schemes.schemes import Schemes

            match self.underlying_category():
                case Schemes():
                    return self.restrict_action(
                        group_element.cyclic_subgroup().inclusion()
                    )
                case other:
                    assert False, (
                        f"the fixed locus of a single group element is constructed for schemes; {other} supplies no owned equalizer of an automorphism with the identity"
                    )

        def fixed_subobject_of(self, group_element):
            r"""Return ``X^g``, the equalizer of ``rho(g)`` and the identity of ``X``.

            A point fixed by ``g`` is fixed by every power of ``g``, so
            ``X^g = X^{<g>}``: the equalizer of one automorphism with the
            identity is the common fixed locus of the cyclic subgroup that
            automorphism generates, and that common fixed locus is what the
            specialization constructs.
            """
            return self._cyclic_restriction(group_element).fixed_subscheme()

        def nontrivial_stabilizer_subscheme(self):
            r"""Return the locus of points fixed by some nonidentity element.

            This is the union of the ``X^g`` over ``g != 1``, and a union of
            closed subschemes is cut out by the intersection of their ideals.
            The action is free exactly when this subscheme is empty, and the
            quotient morphism is ramified exactly over its image, which is
            where a quotient singularity of the orbit space can appear.
            """
            group = self.acting_group()
            assert group.is_finite() is True, f"the union of the fixed loci of {group} is taken over its nonidentity elements, which requires a group decided finite"
            identity = group.one()
            ideal = None
            for group_element in group:
                if group_element == identity:
                    continue
                fixed = self._cyclic_restriction(group_element).fixed_ideal()
                ideal = fixed if ideal is None else ideal.intersection(fixed)
            if ideal is None:
                ideal = self.coordinate_algebra().ideal(self.coordinate_algebra().one())
            return self.closed_subscheme(tuple(ideal.ideal_generators()))

        def action_is_free(self):
            r"""Decide whether the identity is the only element with a fixed point.

            This is strictly stronger than ``X^G`` being empty.  ``X^G`` is the
            intersection of the ``X^g``, so one element acting without fixed
            points already empties it while other elements keep theirs; the
            quotient is then still not a torsor over its image, and the
            hypotheses of free quotients do not apply.  Freeness asks the
            question of every nonidentity element separately.

            ``X^g`` is empty exactly when its ideal is the unit ideal.  For an
            acting group not decided finite the answer is ``Unknown``: the
            question is one condition per element and no owned criterion
            replaces it.
            """
            group = self.acting_group()
            if group.is_finite() is not True:
                return Unknown
            identity = group.one()
            for group_element in group:
                if group_element == identity:
                    continue
                restricted = self._cyclic_restriction(group_element)
                unit = restricted.coordinate_algebra().one()
                if not restricted.fixed_ideal().contains_ambient_element(unit):
                    return False
            return True

        def is_invariant(self, element):
            r"""Decide ``g . element = element`` on a determining family of the acting group."""
            group = self.acting_group()
            match group:
                case _ if group in GroupsWithChosenFiniteGeneratingSet():
                    determining = group.group_generators()
                case _ if group.is_finite() is True:
                    determining = group
                case _:
                    return Unknown
            return all(self.act(group_element, element) == element for group_element in determining)


__all__ = [
    "EquivariantMorphism",
    "ExternalInternalActionComparison",
    "GObjectHomset",
    "GObjects",
    "Grp",
    "InternalGroupActionMorphism",
    "InternalGroupActions",
    "InternalGroupObjectMorphism",
    "InternalGroupObjects",
]
