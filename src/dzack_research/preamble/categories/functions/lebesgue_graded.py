r"""Lebesgue spaces as an \(M\)-graded module, and the two products.

The underlying graded module is \(\bigoplus_s L^{1/s}\), indexed by Hölder
degree \(s=1/p\). Restricting the index monoid restricts the module. Each
product is extra structure interned from a morphism of the tensor square:

- Pointwise multiplication is graded over \(([0,\infty],+)\). The unit
  piece is \(L^\infty\). This is a unital \(\mathbb R\)-algebra.
- Convolution is graded over \(([0,1],\oplus)\) with \(s\oplus t=s+t-1\).
  The identity degree is \(L^1\). On \(\mathbb R\) there is no convolution
  unit in \(L^1\), so this is an associative algebra, not a unital one.

The integral pairing of either algebra is the composite
\(B=\varepsilon\circ m\), where \(m\) is the interned multiplication and
\(\varepsilon=\iota\circ\pi_1\) integrates the degree-\(1\) piece \(L^1\).
That \(\varepsilon\) is \(\mathbb R\)-linear, not an algebra morphism. The
graded augmentation of the pointwise algebra is the projection onto the
unit piece \(A\to L^\infty=A_u\).
"""

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from sage.categories.map import Map
from sage.categories.morphism import Morphism, SetMorphism
from dzack_research.preamble.categories.sets.set_categories import Sets
from sage.misc.cachefunc import cached_function
from sage.rings.infinity import Infinity
from sage.structure.element import ModuleElement, parent as element_parent
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.symbolic.ring import SR

from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    AlgebrasWithChosenMultiplication,
    AssociativeAlgebras,
    AssociativeAlgebrasWithChosenMultiplication,
    CommutativeAlgebras,
)
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.forms.forms import Pairings
from dzack_research.preamble.categories.functions.real_functions import (
    Lp,
    _integrability,
    _is_lebesgue_space,
    _l2_pairing,
)
from dzack_research.preamble.categories.modules.graded_modules import GradedModules
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _engine_ring,
    _owned_ring,
)
from dzack_research.preamble.refine import refine
from dzack_research.preamble.rings.real import RR
from dzack_research.preamble.rings.nonnegative_reals import NonNegativeReals
from dzack_research.preamble.rings.unit_interval import UnitInterval


def _real_ring():
    return _owned_ring(RR)


def _holder_degree(space):
    exponent = space.integrability_exponent()
    if exponent is Infinity:
        return NonNegativeReals.zero()
    return ~NonNegativeReals(exponent)


def _lebesgue_exponent(degree):
    value = degree.as_extended_real()
    if value is Infinity:
        raise TypeError(f"degree {degree} is ∞, so the graded piece would be L^0")
    if value == 0:
        return Infinity
    return _integrability(RR.one() / RR(value))


def _convolve_formulas(left, right):
    x = left.parent().indeterminate()
    dummy = SR.symbol()
    formula = left.expression().subs({x: x - dummy}) * right.expression().subs({x: dummy})
    return formula.integrate(dummy, -Infinity, Infinity)


def _pointwise_piece_product(left, right, degree):
    return Lp(_lebesgue_exponent(degree))(left.expression() * right.expression())


def _convolution_piece_product(left, right, degree):
    return Lp(_lebesgue_exponent(degree))(_convolve_formulas(left, right))


def _compose_morphisms(left, right):
    r"""The composite \(left\circ right\)."""
    if right.codomain() is not left.domain():
        raise TypeError(
            f"cannot compose: the codomain of {right} is not the domain of {left}"
        )
    return SetMorphism(
        Sets().Mor(right.domain(), left.codomain()),
        lambda value, left=left, right=right: left(right(value)),
    )


class LebesgueGradedModules(OwnedCategoryOverBaseRing):
    r"""Graded modules whose homogeneous pieces are Lebesgue spaces \(L^{1/s}\)."""

    @classmethod
    def _repr_object_names(cls):
        return "Lebesgue graded modules"

    def super_categories(self):
        return [Modules(self.base_ring())]

    class ParentMethods:
        def algebra_from_multiplication(self, multiplication, *, unital=True):
            r"""Equip this graded Lebesgue module with its represented product."""
            return intern_graded_lebesgue_algebra(
                multiplication,
                self.base_ring(),
                unital,
            )

        def degree_projection(self, degree):
            r"""The projection \(\pi_s\colon N\to L^{1/s}\) onto a homogeneous piece."""
            degree = self.grading_monoid()(degree)
            piece = self.graded_piece(degree)
            return SetMorphism(
                Sets().Mor(self, piece),
                lambda element, parent=self, degree=degree: parent(
                    element
                ).homogeneous_component(degree),
            )

        def integration_of_degree_one(self):
            r"""Integration \(\iota\colon L^1\to\mathbb R\) of the degree-\(1\) piece."""
            return integration_morphism(self.graded_piece(self.grading_monoid()(1)))

        def integral_form(self):
            r"""The linear form \(\varepsilon=\iota\circ\pi_1\colon N\to\mathbb R\).

            This is not an algebra morphism. It integrates the degree-\(1\)
            piece and vanishes on the complementary summands.
            """
            degree_one = self.grading_monoid()(1)
            return _compose_morphisms(
                self.integration_of_degree_one(),
                self.degree_projection(degree_one),
            )

        def unit_piece_projection(self):
            r"""The graded augmentation \(A\to A_u\), for a unital graded algebra.

            Convolution \(L^1(\mathbb R)\) is not unital, so it does not
            supply this morphism.
            """
            ring = self.base_ring()
            match self:
                case _ if self in Algebras(ring):
                    return self.degree_projection(
                        self.grading_monoid().monoidal_unit()
                    )
                case _:
                    raise TypeError(
                        f"{self} is not a unital algebra; "
                        "the unit-piece projection is the graded augmentation "
                        "of a unital graded algebra"
                    )

        def integral_pairing_morphism(self):
            r"""The pairing \(B=\varepsilon\circ m\colon A\otimes_{\mathbb R}A\to\mathbb R\)."""
            ring = self.base_ring()
            match self:
                case _ if self in AssociativeAlgebrasWithChosenMultiplication(ring):
                    multiplication = self.multiplication_morphism()
                    return _compose_morphisms(self.integral_form(), multiplication)
                case _:
                    raise TypeError(
                        f"{self} has no chosen multiplication morphism"
                    )

        def integral_pairing(self):
            r"""The pairing \(B\) as an element of \(\operatorname{Hom}(A\otimes A,\mathbb R)\)."""
            composite = self.integral_pairing_morphism()
            multiplication = self.multiplication_morphism()
            tensor = multiplication.domain()
            return Pairings(self, self, RR)(
                lambda left, right, composite=composite, tensor=tensor: composite(
                    tensor.pure_tensor(left, right)
                )
            )


class GradedTensorProductModules(OwnedCategoryOverBaseRing):
    r"""Tensor squares of Lebesgue graded modules.

    Elements are finite sums of homogeneous pure tensors. This is not the
    finitely presented tensor product: the summands \(L^{1/s}\) are not
    finitely presented \(\mathbb R\)-modules.
    """

    @classmethod
    def _repr_object_names(cls):
        return "graded tensor products of Lebesgue modules"

    def super_categories(self):
        return [Modules(self.base_ring())]

    class ParentMethods:
        def tensor_factors(self):
            return self._preamble_tensor_factors

        def tensor_factor(self, index):
            return self.tensor_factors()[index]

        def pure_tensor(self, left_element, right_element):
            r"""Return the image of \((left, right)\) under \(\otimes\)."""
            left_module, right_module = self.tensor_factors()
            left_element = left_module(left_element)
            right_element = right_module(right_element)
            summands = tuple(
                (
                    left_degree,
                    right_degree,
                    left_element.homogeneous_component(left_degree),
                    right_element.homogeneous_component(right_degree),
                )
                for left_degree in left_element._degrees()
                for right_degree in right_element._degrees()
            )
            return self.element_class(self, summands)


class LebesgueModuleMorphism(Morphism):
    r"""An \(R\)-linear map specified by its action on elements."""

    def __init__(self, parent, evaluate) -> None:
        Morphism.__init__(self, parent)
        self._evaluate = evaluate

    def _call_(self, element):
        if element_parent(element) is not self.domain():
            element = self.domain()(element)
        return self._evaluate(element)

    def then(self, other):
        r"""Return ``other ∘ self``."""
        return _compose_morphisms(other, self)

    def __mul__(self, other):
        if not isinstance(other, Map) or other.codomain() is not self.domain():
            return NotImplemented
        return _compose_morphisms(self, other)

    def _composition_(self, right, homset):
        return homset(lambda value, left=self, right=right: left(right(value)))


class LebesgueModuleHomset(CategoricalHomset):
    Element = LebesgueModuleMorphism

    def __init__(self, domain, codomain) -> None:
        CategoricalHomset.__init__(
            self,
            HomCategoryConstruction(Modules(domain.base_ring())),
            domain,
            codomain,
        )

    def _element_constructor_(self, evaluate):
        return self.element_class(self, evaluate)

    def _repr_(self):
        return f"Hom({self.domain()}, {self.codomain()})"


def lebesgue_module_homset(domain, codomain) -> LebesgueModuleHomset:
    return LebesgueModuleHomset(domain, codomain)


def integration_morphism(space):
    r"""Integration \(\iota\colon L^1(\mathbb R)\to\mathbb R\), \(\iota(f)=\int f\)."""

    def evaluate(function, space=space):
        function = space(function)
        if function == space.zero():
            return RR.zero()
        return RR(_l2_pairing(function, space.one()))

    return SetMorphism(Sets().Mor(space, RR), evaluate)


class _GradedLebesgueElement(ModuleElement):
    r"""A finitely supported family of homogeneous Lebesgue classes."""

    def __init__(self, parent, components) -> None:
        ModuleElement.__init__(self, parent)
        self._components = {
            parent.grading_monoid()(degree): function
            for degree, function in components.items()
            if function != function.parent().zero()
        }

    def homogeneous_component(self, degree):
        degree = self.parent().grading_monoid()(degree)
        return self._components.get(degree, self.parent().graded_piece(degree).zero())

    def _degrees(self):
        return self._components.keys()

    def _richcmp_(self, other, op):
        from sage.structure.richcmp import op_EQ, op_NE

        if op not in (op_EQ, op_NE):
            return NotImplemented
        equal = self._components.keys() == other._components.keys() and all(
            self.homogeneous_component(degree).expression()
            == other.homogeneous_component(degree).expression()
            for degree in self._degrees()
        )
        return equal if op == op_EQ else not equal

    def _add_(self, other):
        degrees = {*self._degrees(), *other._degrees()}
        return self.parent()._from_components(
            {
                degree: self.homogeneous_component(degree)
                + other.homogeneous_component(degree)
                for degree in degrees
            }
        )

    def _neg_(self):
        return self.parent()._from_components(
            {degree: -function for degree, function in self._components.items()}
        )

    def _lmul_(self, scalar):
        return self.parent()._from_components(
            {degree: scalar * function for degree, function in self._components.items()}
        )

    def _repr_(self) -> str:
        if not self._components:
            return "0"
        return " + ".join(
            f"({function} in {function.parent()})"
            for function in self._components.values()
        )


class _GradedTensorSquareElement(ModuleElement):
    r"""A finite sum of homogeneous pure tensors."""

    def __init__(self, parent, summands) -> None:
        ModuleElement.__init__(self, parent)
        self._summands = tuple(summands)

    def summands(self):
        return self._summands

    def _add_(self, other):
        return self.parent().element_class(
            self.parent(), self._summands + other._summands
        )

    def _neg_(self):
        return self.parent().element_class(
            self.parent(),
            tuple(
                (left_degree, right_degree, -left_function, right_function)
                for left_degree, right_degree, left_function, right_function in self._summands
            ),
        )

    def _lmul_(self, scalar):
        return self.parent().element_class(
            self.parent(),
            tuple(
                (left_degree, right_degree, scalar * left_function, right_function)
                for left_degree, right_degree, left_function, right_function in self._summands
            ),
        )

    def _repr_(self) -> str:
        if not self._summands:
            return "0"
        return " + ".join(
            f"({left_function} ⊗ {right_function})"
            for _left_degree, _right_degree, left_function, right_function in self._summands
        )


class GradedTensorSquare(UniqueRepresentation, Parent):
    r"""The tensor square \(N\otimes_{\mathbb R} N\) of a Lebesgue graded module."""

    Element = _GradedTensorSquareElement

    def __init__(self, module) -> None:
        self._preamble_tensor_factors = (module, module)
        ring = _real_ring()
        Parent.__init__(self, base=_engine_ring(ring), category=Modules(ring))
        refine(self, GradedTensorProductModules(ring))

    def _repr_(self) -> str:
        left, _right = self.tensor_factors()
        return f"{left} ⊗ {left}"

    def _from_summands(self, summands):
        return self.element_class(self, tuple(summands))

    def zero(self):
        return self.element_class(self, ())

    def _an_element_(self):
        return self.zero()


def _lebesgue_multiplication(module, piece_product):
    tensor = GradedTensorSquare(module)

    def evaluate(element, module=module, piece_product=piece_product):
        components = {}
        for left_degree, right_degree, left_function, right_function in element.summands():
            degree = module.combine_degrees(left_degree, right_degree)
            product = piece_product(left_function, right_function, degree)
            components[degree] = (
                components.get(degree, module.graded_piece(degree).zero()) + product
            )
        return module._from_components(components)

    return lebesgue_module_homset(tensor, module)(evaluate)


def _transport_multiplication(multiplication, algebra):
    module = multiplication.codomain()
    tensor = GradedTensorSquare(algebra)
    module_tensor = multiplication.domain()

    def evaluate(
        element,
        algebra=algebra,
        multiplication=multiplication,
        module_tensor=module_tensor,
    ):
        product = multiplication(module_tensor._from_summands(element.summands()))
        return algebra._from_components(
            {degree: product.homogeneous_component(degree) for degree in product._degrees()}
        )

    return lebesgue_module_homset(tensor, algebra)(evaluate)


class _LebesgueAlgebraFromMultiplication(Parent):
    r"""A Lebesgue graded module interned on a chosen multiplication morphism."""

    Element = _GradedLebesgueElement

    def __init__(self, module) -> None:
        ring = _real_ring()
        self._preamble_algebra_base_ring = ring
        Parent.__init__(self, base=_engine_ring(ring), category=Modules(ring))
        refine(
            self,
            [LebesgueGradedModules(ring), GradedModules(ring, module.grading_monoid())],
        )

    def _repr_(self) -> str:
        ring = self._preamble_algebra_base_ring
        match self:
            case _ if self in Algebras(ring):
                return "graded Lebesgue algebra"
            case _:
                return "Lebesgue convolution algebra"

    def _latex_(self) -> str:
        ring = self._preamble_algebra_base_ring
        match self:
            case _ if self in Algebras(ring):
                return r"\bigoplus_s L^{1/s}(\mathbb{R})"
            case _:
                return r"\bigoplus_{s\in[0,1]} L^{1/s}(\mathbb{R})"

    def graded_piece(self, degree):
        r"""The homogeneous summand \(L^{1/s}\) in the interned grading."""
        return Lp(_lebesgue_exponent(self.grading_monoid()(degree)))

    def _from_components(self, components):
        return self.element_class(self, components)

    def _element_constructor_(self, value):
        if element_parent(value) is self:
            return value
        value_parent = element_parent(value)
        if _is_lebesgue_space(value_parent):
            degree = self.grading_monoid()(_holder_degree(value_parent).as_extended_real())
            return self._from_components({degree: value})
        ring = self._preamble_algebra_base_ring
        match self:
            case _ if self in Algebras(ring):
                return self._from_components(
                    {
                        self.grading_monoid().monoidal_unit(): Lp(Infinity)(value),
                    }
                )
            case _:
                raise TypeError(f"{value} is not a Lebesgue class of exponent at least 1")

    def zero(self):
        return self._from_components({})

    def _an_element_(self):
        return self.zero()


class GradedLebesgueModule(UniqueRepresentation, Parent):
    r"""The \(M\)-graded module \(\bigoplus_{s\in M} L^{1/s}\).

    The monoid \(M\) supplies the index of Hölder degrees. The full
    family uses \(([0,\infty],+)\); convolution uses \(([0,1],\oplus)\).
    """

    Element = _GradedLebesgueElement

    def __init__(self, grading_monoid) -> None:
        ring = _real_ring()
        self._preamble_algebra_base_ring = ring
        Parent.__init__(self, base=_engine_ring(ring), category=Modules(ring))
        refine(
            self,
            [LebesgueGradedModules(ring), GradedModules(ring, grading_monoid)],
        )

    def _repr_(self) -> str:
        return f"graded Lebesgue module over {self.grading_monoid()}"

    def _latex_(self) -> str:
        return r"\bigoplus_s L^{1/s}(\mathbb{R})"

    def graded_piece(self, degree):
        r"""The homogeneous summand \(L^{1/s}\) in Hölder degree \(s\)."""
        return Lp(_lebesgue_exponent(self.grading_monoid()(degree)))

    def _from_components(self, components):
        return self.element_class(self, components)

    def _element_constructor_(self, value):
        if element_parent(value) is self:
            return value
        value_parent = element_parent(value)
        if _is_lebesgue_space(value_parent):
            degree = self.grading_monoid()(_holder_degree(value_parent).as_extended_real())
            return self._from_components({degree: value})
        raise TypeError(f"{value} is not a Lebesgue class in {self}")

    def zero(self):
        return self._from_components({})

    def _an_element_(self):
        return self.zero()


def intern_graded_lebesgue_algebra(multiplication, ring, unital):
    r"""Intern a Lebesgue graded module on a morphism of its tensor square."""
    module = multiplication.codomain()
    if module not in LebesgueGradedModules(ring):
        raise TypeError(
            "this internment presents a Lebesgue graded module by a "
            "morphism of its tensor square"
        )
    algebra = _LebesgueAlgebraFromMultiplication(module)
    algebra._preamble_multiplication_morphism = _transport_multiplication(
        multiplication, algebra
    )
    algebra._preamble_algebra_base_ring = ring
    monoid = module.grading_monoid()
    match unital:
        case True:
            unit_degree = monoid.monoidal_unit()
            algebra._preamble_algebra_unit = algebra._from_components(
                {unit_degree: algebra.graded_piece(unit_degree).one()}
            )
            return refine(
                algebra,
                [
                    AlgebrasWithChosenMultiplication(ring),
                    GradedAlgebras(ring, monoid),
                    CommutativeAlgebras(ring),
                    LebesgueGradedModules(ring),
                    GradedModules(ring, monoid),
                ],
            )
        case False:
            return refine(
                algebra,
                [
                    AssociativeAlgebrasWithChosenMultiplication(ring),
                    AssociativeAlgebras(ring),
                    LebesgueGradedModules(ring),
                    GradedModules(ring, monoid),
                ],
            )


@cached_function
def graded_lebesgue_algebra():
    r"""The pointwise algebra \(\bigoplus_s L^{1/s}\), interned from its product."""
    ring = _real_ring()
    module = GradedLebesgueModule(NonNegativeReals)
    return GradedAlgebras(ring, NonNegativeReals)(
        _lebesgue_multiplication(module, _pointwise_piece_product)
    )


@cached_function
def lebesgue_convolution_algebra():
    r"""The convolution algebra \(\bigoplus_{s\in[0,1]} L^{1/s}\), interned from its product."""
    ring = _real_ring()
    module = GradedLebesgueModule(UnitInterval)
    return AssociativeAlgebras(ring)(
        _lebesgue_multiplication(module, _convolution_piece_product)
    )
