r"""Cartier divisors as global sections of the Cartier quotient sheaf.

For a scheme ``X`` let ``K_X`` be the sheaf of total quotient rings.  A
Cartier divisor is, by definition, a global section of

``K_X^* / O_X^*``.

The quotient-sheaf convention is Stacks Project, Tag 02AQ.  A represented
finite-atlas lift of such a section consists of local equations ``f_i`` in the
total quotient rings of the affine charts, with ``f_i/f_j`` a regular unit on
every overlap.  Those lifts are presentations of elements of ``CDiv(X)``;
they are not a second kind of Cartier-divisor object.
"""

from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.unknown import Unknown
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import parent as element_parent
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.modules.general_modules import GeneralModules
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
    OwnedNoetherianRings,
    OwnedRings,
    _own_ring,
)
from dzack_research.preamble.categories.schemes.gluing import FiniteAffineAtlases
from dzack_research.preamble.categories.schemes.ringed_spaces import SheafObjects
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.owned_category_bases import Category


def _integers():
    return _own_ring(SageZZ)


class _TotalQuotientSheafEngine:
    r"""Private realization of the meromorphic-function sheaf ``K_X``.

    In general ``K_X`` is the sheaf associated to
    ``U |-> S(U)^(-1) O_X(U)``, where ``S(U)`` consists of sections whose germ
    is a nonzerodivisor at every point.  On a locally Noetherian scheme this
    sheaf already has ``K_X(U)=Q(O_X(U))`` for every affine open ``U`` (Stacks,
    Tags 01X1 and 02OV).  The latter is the represented computational regime
    used by the finite-atlas lift below.
    """

    def __init__(self, scheme, **rest) -> None:
        self._scheme = scheme
        super().__init__(**rest)

    def scheme(self):
        return self._scheme

    def sections_on_affine(self, affine_open):
        r"""Return ``K_X(U)=Q(O_X(U))`` in the represented Noetherian regime."""
        ring = affine_open.coordinate_algebra()
        assert ring in OwnedNoetherianRings(), (
            "the affine total-quotient formula for K_X is used only in the represented Noetherian regime"
        )
        return ring.total_quotient_ring()

    def _repr_(self):
        return f"Total quotient sheaf on {self.scheme()}"


class _UnitSheafEngine:
    r"""Private realization of the sheaf of units of a represented ring sheaf."""

    def __init__(self, ring_sheaf, **rest) -> None:
        self._ring_sheaf = ring_sheaf
        super().__init__(**rest)

    def ring_sheaf(self):
        return self._ring_sheaf

    def scheme(self):
        return self.ring_sheaf().scheme()

    def _repr_(self):
        return f"Unit sheaf of {self.ring_sheaf()}"


class _RegularUnitSheafEngine:
    r"""Private realization of ``O_X^*`` without requiring an affine ``O_X`` engine."""

    def __init__(self, scheme, **rest) -> None:
        self._scheme = scheme
        super().__init__(**rest)

    def scheme(self):
        return self._scheme

    def _repr_(self):
        return f"Regular unit sheaf O^* on {self.scheme()}"


class _CartierDivisorQuotientSheafEngine:
    r"""Private realization of the quotient sheaf ``K_X^* / O_X^*``."""

    def __init__(self, numerator_sheaf, denominator_sheaf, **rest) -> None:
        self._numerator_sheaf = numerator_sheaf
        self._denominator_sheaf = denominator_sheaf
        assert numerator_sheaf.scheme() is denominator_sheaf.scheme(), (
            "a quotient of unit sheaves is formed on one scheme"
        )
        super().__init__(**rest)

    def scheme(self):
        return self.numerator_sheaf().scheme()

    def numerator_sheaf(self):
        r"""The sheaf ``K_X^*``."""
        return self._numerator_sheaf

    def denominator_sheaf(self):
        r"""The subsheaf ``O_X^*``."""
        return self._denominator_sheaf

    @cached_method
    def global_sections(self):
        r"""Return ``Gamma(X, K_X^*/O_X^*) = CDiv(X)``."""
        return CartierDivisorGroups()(self)

    def _repr_(self):
        return f"Cartier quotient sheaf K^*/O^* on {self.scheme()}"


@cached_function(key=lambda scheme: id(scheme))
def _total_quotient_sheaf(scheme):
    sheaves = SheafObjects(scheme)
    return _object_of(
        sheaves,
        _engine=(sheaves, _TotalQuotientSheafEngine, None),
        scheme=scheme,
    )


@cached_function(key=lambda ring_sheaf: id(ring_sheaf))
def _unit_sheaf(ring_sheaf):
    sheaves = SheafObjects(ring_sheaf.scheme())
    return _object_of(
        sheaves,
        _engine=(sheaves, _UnitSheafEngine, None),
        ring_sheaf=ring_sheaf,
    )


@cached_function(key=lambda scheme: id(scheme))
def _regular_unit_sheaf(scheme):
    sheaves = SheafObjects(scheme)
    return _object_of(
        sheaves,
        _engine=(sheaves, _RegularUnitSheafEngine, None),
        scheme=scheme,
    )


@cached_function(key=lambda scheme: id(scheme))
def _cartier_divisor_quotient_sheaf(scheme):
    r"""Return the represented quotient sheaf ``K_X^*/O_X^*``."""
    sheaves = SheafObjects(scheme)
    total_quotient_units = _unit_sheaf(_total_quotient_sheaf(scheme))
    regular_units = _regular_unit_sheaf(scheme)
    return _object_of(
        sheaves,
        _engine=(sheaves, _CartierDivisorQuotientSheafEngine, None),
        numerator_sheaf=total_quotient_units,
        denominator_sheaf=regular_units,
    )


def _total_quotient_pullback(ring_morphism, rational_section):
    r"""Pull a represented total-quotient section along an affine open map.

    The currently represented finite-atlas computation uses a localization
    realization of the source total quotient ring.  The public Cartier group
    is not restricted by this computational case; this is only the adapter
    used to verify one finite-atlas lift.
    """
    source = ring_morphism.domain()
    target = ring_morphism.codomain()
    source_total = source.total_quotient_ring()
    target_total = target.total_quotient_ring()
    rational_section = source_total(rational_section)
    match source_total in LocalizationRings():
        case True:
            match target in OwnedRings().Commutative().NoZeroDivisors():
                case True:
                    target_map = target.fraction_field_map()
                case False:
                    target_map = target.total_quotient_map()
            numerator = target_map(ring_morphism(source(rational_section.numerator())))
            denominator = target_map(
                ring_morphism(source(rational_section.denominator()))
            )
            assert denominator.is_unit(), (
                "an affine-open restriction sends a represented total-quotient denominator to a unit"
            )
            return target_total(numerator * denominator.inverse_of_unit())
        case False:
            raise AssertionError(
                "finite-atlas Cartier restriction currently requires the source total quotient ring to have a localization realization"
            )


def _regular_unit_ratio(ring, left, right):
    r"""Whether ``left/right`` is represented by a unit of ``ring``."""
    total = ring.total_quotient_ring()
    ratio = total(left) * total(right).inverse_of_unit()
    match ratio in ring:
        case True:
            return bool(ring(ratio).is_unit())
        case False:
            return False


class _CartierSectionClass:
    r"""One class in ``Gamma(X,K_X^*/O_X^*)`` with a represented expression."""

    def __init__(
        self,
        parent,
        kind,
        *,
        atlas=None,
        local_equations=None,
        transition_units=None,
        left=None,
        right=None,
        operand=None,
        scalar=None,
    ) -> None:
        self._kind = kind
        self._atlas = atlas
        self._local_equations = local_equations
        self._transition_units = transition_units
        self._left = left
        self._right = right
        self._operand = operand
        self._scalar = scalar
        super().__init__(parent)

    def is_finite_atlas_presentation(self):
        return self._kind == "finite_atlas"

    def gluing_datum(self):
        assert self.is_finite_atlas_presentation(), (
            "this represented Cartier section is not presently stored by one finite atlas"
        )
        return self._atlas

    def local_equation(self, index):
        atlas = self.gluing_datum()
        return self._local_equations[atlas.normalize_chart_index(index)]

    def transition_unit(self, source_index, target_index):
        atlas = self.gluing_datum()
        source_index = atlas.normalize_chart_index(source_index)
        target_index = atlas.normalize_chart_index(target_index)
        pair = next(
            pair
            for pair in atlas.transition_index_set()
            if {pair[0], pair[1]} == {source_index, target_index}
        )
        unit = self._transition_units[pair]
        match pair == (source_index, target_index):
            case True:
                return unit
            case False:
                reverse = atlas.transition_between(source_index, target_index).forward()
                return reverse.coordinate_algebra_morphism()(unit.inverse_of_unit())

    def _richcmp_(self, other, op):
        match op in (op_EQ, op_NE):
            case False:
                return NotImplemented
            case True:
                pass
        match element_parent(other) is self.parent():
            case False:
                return op == op_NE
            case True:
                pass
        decision = self.parent().equal(self, other)
        match op == op_EQ or decision is Unknown:
            case True:
                return decision
            case False:
                return not decision

    __hash__ = None

    def _repr_(self):
        match self._kind:
            case "zero":
                return "0"
            case "finite_atlas":
                return (
                    f"Cartier section on {self.parent().scheme()} "
                    "from finite-atlas local equations"
                )
            case "sum":
                return f"({self._left}) + ({self._right})"
            case "negation":
                return f"-({self._operand})"
            case "multiple":
                return f"{self._scalar}*({self._operand})"


class _CartierSectionClasses:
    r"""The underlying set of global Cartier-quotient sections.

    Finite-atlas lifts are identified when their local equations differ by
    chartwise regular units.  For distinct represented atlases, equality may
    remain ``Unknown`` until a common refinement is available; this does not
    change the section represented by either lift.
    """

    def __init__(self, quotient_sheaf, **rest) -> None:
        self._quotient_sheaf = quotient_sheaf
        super().__init__(**rest)

    def quotient_sheaf(self):
        return self._quotient_sheaf

    def scheme(self):
        return self.quotient_sheaf().scheme()

    def __contains__(self, value):
        return element_parent(value) is self

    def __call__(self, value):
        match element_parent(value) is self:
            case True:
                return value
            case False:
                raise TypeError("a Cartier section class requires a represented global section")

    @cached_method
    def zero(self):
        return self.element_class(self, "zero")

    def finite_atlas(self, atlas, local_equations):
        match atlas in FiniteAffineAtlases(self.scheme()):
            case True:
                pass
            case False:
                raise TypeError(
                    "finite-atlas Cartier equations require a finite affine atlas of this scheme"
                )
        supplied = dict(local_equations)
        assert set(supplied) == set(atlas.chart_indices()), (
            "a Cartier datum requires one local equation on every atlas chart"
        )
        equations = {}
        for index in atlas.chart_indices():
            ring = atlas.chart(index).coordinate_algebra()
            assert ring in OwnedNoetherianRings(), (
                "the represented finite-atlas lift computes K_X on Noetherian affine charts"
            )
            total = self.quotient_sheaf().numerator_sheaf().ring_sheaf().sections_on_affine(
                atlas.chart(index)
            )
            equation = total(supplied[index])
            assert equation.is_unit(), (
                "a Cartier local equation is a unit of the chart's total quotient ring"
            )
            equations[index] = equation
        equations = finite_indexed_family(
            atlas.chart_index_set(),
            equations.__getitem__,
            name="Finite-atlas Cartier local equations",
        )
        transitions = {
            pair: self._transition_unit(atlas, equations, *pair)
            for pair in atlas.transition_index_set()
        }
        return self.element_class(
            self,
            "finite_atlas",
            atlas=atlas,
            local_equations=equations,
            transition_units=transitions,
        )

    def _restricted_equation(self, atlas, equations, source_index, target_index):
        overlap = atlas.overlap(source_index, target_index)
        restriction = overlap.inclusion().coordinate_algebra_morphism()
        return _total_quotient_pullback(restriction, equations[source_index])

    def _transition_unit(self, atlas, equations, source_index, target_index):
        source_equation = self._restricted_equation(
            atlas,
            equations,
            source_index,
            target_index,
        )
        target_equation = self._restricted_equation(
            atlas,
            equations,
            target_index,
            source_index,
        )
        transition = atlas.transition_between(source_index, target_index).forward()
        target_on_source = _total_quotient_pullback(
            transition.coordinate_algebra_morphism(),
            target_equation,
        )
        overlap_ring = atlas.overlap(source_index, target_index).coordinate_algebra()
        overlap_total = overlap_ring.total_quotient_ring()
        ratio = overlap_total(source_equation) * overlap_total(
            target_on_source
        ).inverse_of_unit()
        assert ratio in overlap_ring, (
            "Cartier local equations must have a regular ratio on every overlap"
        )
        unit = overlap_ring(ratio)
        assert unit.is_unit(), (
            "Cartier local equations must differ by a unit on every overlap"
        )
        return unit

    def add(self, left, right):
        left = self(left)
        right = self(right)
        match (left._kind, right._kind):
            case ("zero", _):
                return right
            case (_, "zero"):
                return left
            case ("finite_atlas", "finite_atlas") if left._atlas is right._atlas:
                atlas = left._atlas
                equations = {
                    index: left.local_equation(index) * right.local_equation(index)
                    for index in atlas.chart_indices()
                }
                return self.finite_atlas(atlas, equations)
            case _:
                return self.element_class(self, "sum", left=left, right=right)

    def negate(self, value):
        value = self(value)
        match value._kind:
            case "zero":
                return value
            case "finite_atlas":
                atlas = value._atlas
                return self.finite_atlas(
                    atlas,
                    {
                        index: value.local_equation(index).inverse_of_unit()
                        for index in atlas.chart_indices()
                    },
                )
            case "negation":
                return value._operand
            case _:
                return self.element_class(self, "negation", operand=value)

    def scale(self, scalar, value):
        scalar = _integers()(scalar)
        value = self(value)
        exponent = int(scalar)
        match exponent:
            case 0:
                return self.zero()
            case 1:
                return value
            case _ if value._kind == "finite_atlas":
                atlas = value._atlas
                return self.finite_atlas(
                    atlas,
                    {
                        index: value.local_equation(index) ** exponent
                        for index in atlas.chart_indices()
                    },
                )
            case _:
                return self.element_class(
                    self,
                    "multiple",
                    operand=value,
                    scalar=scalar,
                )

    def _finite_atlas_is_zero(self, value):
        atlas = value._atlas
        return all(
            _regular_unit_ratio(
                atlas.chart(index).coordinate_algebra(),
                value.local_equation(index),
                atlas.chart(index).coordinate_algebra().one(),
            )
            for index in atlas.chart_indices()
        )

    def _same_atlas_equal(self, left, right):
        atlas = left._atlas
        return all(
            _regular_unit_ratio(
                atlas.chart(index).coordinate_algebra(),
                left.local_equation(index),
                right.local_equation(index),
            )
            for index in atlas.chart_indices()
        )

    def equal(self, left, right):
        left = self(left)
        right = self(right)
        match (left._kind, right._kind):
            case _ if left is right:
                return True
            case ("zero", "zero"):
                return True
            case ("zero", "finite_atlas"):
                return self._finite_atlas_is_zero(right)
            case ("finite_atlas", "zero"):
                return self._finite_atlas_is_zero(left)
            case ("finite_atlas", "finite_atlas") if left._atlas is right._atlas:
                return self._same_atlas_equal(left, right)
            case ("sum", "sum"):
                left_decision = self.equal(left._left, right._left)
                right_decision = self.equal(left._right, right._right)
                match (left_decision, right_decision):
                    case (True, True):
                        return True
                    case (False, _) | (_, False):
                        return False
                    case _:
                        return Unknown
            case ("negation", "negation"):
                return self.equal(left._operand, right._operand)
            case ("multiple", "multiple") if left._scalar == right._scalar:
                return self.equal(left._operand, right._operand)
            case _:
                return Unknown

    def _repr_(self):
        return f"Global sections of {self.quotient_sheaf()}"


@cached_function(key=lambda quotient_sheaf: id(quotient_sheaf))
def _cartier_section_classes(quotient_sheaf):
    return _object_of(
        Sets(),
        _engine=(Sets(), _CartierSectionClasses, _CartierSectionClass),
        quotient_sheaf=quotient_sheaf,
    )


class CartierDivisorGroups(Category):
    r"""The groups ``CDiv(X)=Gamma(X,K_X^*/O_X^*)`` of Cartier divisors.

    The defining datum of an object is the quotient sheaf
    ``K_X^*/O_X^*``.  Since every abelian group is canonically a ``ZZ``-module,
    the group is represented through ``GeneralModules(ZZ)`` without choosing a
    framing or presentation.

    Unverified specimen: a finite-atlas local equation is an element of the
    one owned Cartier divisor group::

        sage: from dzack_research.preamble.all import QQ, ProjectiveSpaces
        sage: line = ProjectiveSpaces(QQ)(1)
        sage: atlas = line.standard_affine_atlas()
        sage: left = atlas.chart(0).coordinate_algebra()
        sage: right = atlas.chart(1).coordinate_algebra()
        sage: x0_over_x1 = right.algebra_generator("x0_over_x1")
        sage: cartier = CartierDivisorGroups().of_scheme(line)
        sage: point = cartier.finite_atlas_section(
        ....:     atlas, {0: left.one(), 1: x0_over_x1}
        ....: )
        sage: point in cartier
        True
        sage: point.parent() is cartier
        True
        sage: cartier.quotient_sheaf().global_sections() is cartier
        True
    """

    @classmethod
    def _repr_object_names(cls):
        return "Cartier divisor groups"

    def super_categories(self):
        return [GeneralModules(_integers())]

    def an_object(self):
        from dzack_research.preamble.categories.divisors.divisor_groups import (
            _affine_line_over_rationals,
        )

        return self.of_scheme(_affine_line_over_rationals())

    def of_scheme(self, scheme):
        r"""Return ``CDiv(X)`` for ``scheme = X``."""
        return _cartier_divisor_quotient_sheaf(scheme).global_sections()

    def _call_(self, quotient_sheaf):
        r"""Construct the global-section group of ``K_X^*/O_X^*``."""
        scheme = quotient_sheaf.scheme()
        assert quotient_sheaf is _cartier_divisor_quotient_sheaf(scheme), (
            "the Cartier divisor group is constructed from the represented quotient sheaf K_X^*/O_X^*"
        )
        sections = _cartier_section_classes(quotient_sheaf)
        return _object_of(
            self,
            cartier_divisor_sheaf=quotient_sheaf,
            base_ring=_integers(),
            underlying_set=sections,
            addition=sections.add,
            zero=sections.zero(),
            negation=sections.negate,
            scalar_action=sections.scale,
            verify=False,
        )

    class ParentMethods:
        def __init__(self, cartier_divisor_sheaf, **rest) -> None:
            self._cartier_divisor_sheaf = cartier_divisor_sheaf
            super().__init__(**rest)

        def quotient_sheaf(self):
            r"""The sheaf ``K_X^*/O_X^*`` whose global sections form this group."""
            return self._cartier_divisor_sheaf

        def divisor_scheme(self):
            r"""The scheme ``X`` in ``CDiv(X)``."""
            return self.quotient_sheaf().scheme()

        def finite_atlas_section(self, atlas, local_equations):
            r"""Construct the section represented by ``(U_i,f_i)`` on ``atlas``."""
            section = self.underlying_set().finite_atlas(atlas, local_equations)
            return self(section)

    class ElementMethods:
        def gluing_datum(self):
            r"""The finite atlas of this represented local-equation lift."""
            return self.underlying_element().gluing_datum()

        def local_equation(self, index):
            r"""The chosen local lift ``f_i`` on one chart."""
            return self.underlying_element().local_equation(index)

        def transition_unit(self, source_index, target_index):
            r"""The regular unit ``f_i/f_j`` on the selected overlap."""
            return self.underlying_element().transition_unit(source_index, target_index)

        def associated_invertible_sheaf(self):
            r"""Return ``O_X(D)`` from the transition units of this finite-atlas lift."""
            from dzack_research.preamble.categories.divisors.invertible_sheaves import (
                _finite_atlas_invertible_sheaf,
            )

            atlas = self.gluing_datum()
            units = {
                pair: self.transition_unit(*pair)
                for pair in atlas.transition_index_set()
            }
            return _finite_atlas_invertible_sheaf(
                atlas,
                units,
                associated_divisor=self,
            )

        line_bundle = associated_invertible_sheaf


__all__ = ["CartierDivisorGroups"]
