r"""Exact pairings and quadratic forms through their universal module objects.

Whenever the relevant universal object is represented, a pairing is literally an
element of ``Hom_R(X tensor_R Y, W)`` and a quadratic map is literally an element
of ``Hom_R(Gamma^2(M), W)``.  Only modules for which those universal objects are
not represented retain an extensional callable form object; that fallback never
pretends to be a second Hom implementation and has no coordinate presentation.
"""

from sage.misc.cachefunc import cached_function
from sage.categories.sets_cat import Sets
from sage.structure.element import Element
from sage.structure.parent import Parent

from dzack_research.preamble.categories.sets.indexed_families import (
    coerce_family_value as _coerce_value,
    coordinate_family as _coordinate_family,
    coordinate_family_from_function as _coordinate_family_from_function,
    coordinate_pair as _coordinate_pair,
    finite_framing as _finite_framing,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
)
from dzack_research.preamble.refine import refine


class BilinearFormHoms(OwnedCategoryOverBaseRing):
    r"""Diagonal pairing Hom objects carrying the bilinear-form operations."""

    @classmethod
    def _repr_object_names(cls):
        return "bilinear-form Hom objects"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import (
            InternalHomModules,
        )

        return [InternalHomModules(self.base_ring())]

    class ElementMethods:
        def gram_tensor(self):
            if self.left_module() is not self.right_module():
                raise TypeError("a Gram tensor requires a diagonal bilinear form")
            if self.codomain() not in OwnedRings():
                raise TypeError("a Gram tensor here requires scalar-valued form entries")
            from dzack_research.preamble.categories.sets.cardinals import cardinal
            from dzack_research.preamble.tensors.tensor import tensor

            labels = self.left_module().module_generating_set()
            size = cardinal(labels.cardinality())
            if not size.is_finite():
                raise TypeError("a form supplied only by a pairing has no finite Gram tensor")
            rank = int(size.finite_value())
            return tensor(
                self.codomain(),
                (),
                (rank, rank),
                (
                    self._gram_entry(labels.unrank(i), labels.unrank(j))
                    for i in range(rank)
                    for j in range(rank)
                ),
            )

        def pullback(self, morphism):
            if morphism.codomain() is not self.module():
                raise ValueError("the pullback map must land in the form's module")
            from dzack_research.preamble.categories.abstract_categories.constructions import TensorProduct
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_homset,
            )

            source = TensorProduct(morphism.domain(), morphism.domain())
            induced = module_homset(source, self.domain())(
                lambda pair: self.domain().pure_tensor(
                    morphism(
                        morphism.domain().module_generator(pair.component(0))
                    ),
                    morphism(
                        morphism.domain().module_generator(pair.component(1))
                    ),
                )
            )
            return BilinearForms(morphism.domain(), self.codomain())(self * induced)


def _value_module_over(value_module, ring) -> bool:
    from dzack_research.preamble.categories.modules.pure.modules import Modules

    return value_module in Modules(ring)


class _CallableForm(Element):
    r"""Extensional form data used only when no universal classifier is represented."""

    def __init__(self, parent, datum) -> None:
        Element.__init__(self, parent)
        self._evaluation = None
        self._lift_evaluation = None
        from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily

        coordinate_datum = (
            isinstance(datum, IndexedFamily)
            or hasattr(datum, "rows")
            or (
                isinstance(datum, (tuple, list))
                and all(isinstance(row, (tuple, list)) for row in datum)
            )
        )
        if coordinate_datum:
            left_labels = _finite_framing(parent.left_module())
            right_labels = _finite_framing(parent.right_module())
            values = _coordinate_family(
                left_labels,
                right_labels,
                parent.codomain(),
                datum,
                name=f"Callable {parent.kind()} coordinate input",
            )

            def bilinear(left, right):
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                    module_coefficients,
                )

                left_coefficients = module_coefficients(left, parent.left_module())
                right_coefficients = module_coefficients(right, parent.right_module())
                result = parent.codomain().zero()
                for left_label, left_coefficient in left_coefficients.items():
                    for right_label, right_coefficient in right_coefficients.items():
                        scalar = left_coefficient * right_coefficient
                        if scalar:
                            result += scalar * _coordinate_pair(
                                values, left_label, right_label
                            )
                return result

            if parent.kind() == "quadratic":
                size = int(left_labels.cardinality())
                for i in range(size):
                    for j in range(i + 1, size):
                        left = left_labels.unrank(i)
                        right = left_labels.unrank(j)
                        if _coordinate_pair(values, left, right) != _coordinate_pair(
                            values, right, left
                        ):
                            raise ValueError(
                                "the bilinear lift of a quadratic form must be symmetric"
                            )
                self._lift_evaluation = bilinear
                self._evaluation = lambda element: bilinear(element, element)
            else:
                self._evaluation = bilinear
            return

        if not callable(datum):
            raise TypeError(
                "an unrepresented form is supplied by callable evaluation or finite coordinate ingress"
            )
        self._evaluation = datum

    def left_module(self):
        return self.parent().left_module()

    def right_module(self):
        return self.parent().right_module()

    def module(self):
        if self.parent().kind() == "quadratic":
            return self.left_module()
        if self.left_module() is not self.right_module():
            raise TypeError("a pairing of distinct modules is not a form on one module")
        return self.left_module()

    def codomain(self):
        return self.parent().codomain()

    def __call__(self, *arguments):
        if self.parent().kind() == "quadratic":
            if len(arguments) != 1:
                raise TypeError("a quadratic map takes one module element")
            element = arguments[0]
            if element not in self.module():
                raise TypeError(f"the quadratic form is defined on {self.module()}")
            return _coerce_value(self.codomain(), self._evaluation(element))
        if len(arguments) != 2:
            raise TypeError("a pairing takes two module elements")
        left, right = arguments
        if left not in self.left_module() or right not in self.right_module():
            raise TypeError(
                f"the pairing takes an element of {self.left_module()} and {self.right_module()}"
            )
        return _coerce_value(self.codomain(), self._evaluation(left, right))

    def norm(self, element):
        if self.parent().kind() != "bilinear" or self.left_module() is not self.right_module():
            raise TypeError("a norm here requires a bilinear form on one module")
        return self(element, element)

    def coordinate_values(self):
        if self.parent().kind() != "bilinear":
            raise TypeError("quadratic forms have lift coordinates, not bilinear coordinates")
        labels = _finite_framing(self.module())
        return _coordinate_family_from_function(
            labels,
            labels,
            self.codomain(),
            lambda left_label, right_label: self(
                self.module().module_generator(left_label),
                self.module().module_generator(right_label),
            ),
            name="Extensional bilinear coordinate values",
        )

    def lift_coordinate_values(self):
        if self.parent().kind() != "quadratic" or self._lift_evaluation is None:
            raise TypeError(
                "an extensional callable quadratic form has no chosen bilinear coordinate lift"
            )
        labels = _finite_framing(self.module())
        return _coordinate_family_from_function(
            labels,
            labels,
            self.codomain(),
            lambda left_label, right_label: self._lift_evaluation(
                self.module().module_generator(left_label),
                self.module().module_generator(right_label),
            ),
            name="Extensional quadratic-lift coordinate values",
        )

    def lift_pairing(self, left, right):
        if self.parent().kind() != "quadratic" or self._lift_evaluation is None:
            raise TypeError("this quadratic form has no chosen bilinear lift")
        return _coerce_value(self.codomain(), self._lift_evaluation(left, right))

    def gram_tensor(self):
        from dzack_research.preamble.categories.rings.ring_foundation import OwnedRings
        from dzack_research.preamble.tensors.tensor import tensor

        if self.codomain() not in OwnedRings():
            raise TypeError("a Gram tensor here requires scalar-valued form entries")
        values = (
            self.lift_coordinate_values()
            if self.parent().kind() == "quadratic"
            else self.coordinate_values()
        )
        labels = _finite_framing(self.module())
        rank = int(labels.cardinality())
        return tensor(
            self.codomain(),
            (),
            (rank, rank),
            (
                _coordinate_pair(values, labels.unrank(i), labels.unrank(j))
                for i in range(rank)
                for j in range(rank)
            ),
        )

    def polar_form(self):
        if self.parent().kind() == "quadratic":
            return BilinearForms(self.module(), self.codomain())(
                lambda left, right: self(left + right) - self(left) - self(right)
            )
        if self.left_module() is not self.right_module():
            raise TypeError("polar form syntax requires a bilinear form on one module")
        return BilinearForms(self.module(), self.codomain())(
            lambda left, right: 2 * self(left, right)
        )

    def b(self, left, right):
        if self.parent().kind() == "quadratic":
            return self.polar_form()(left, right)
        return self(left, right)

    def pullback(self, morphism):
        if morphism.codomain() is not self.module():
            raise ValueError("the pullback map must land in the form's module")
        if self.parent().kind() == "quadratic":
            return QuadraticMap(
                morphism.domain(),
                self.codomain(),
                lambda element: self(morphism(element)),
            )
        return BilinearForms(morphism.domain(), self.codomain())(
            lambda left, right: self(morphism(left), morphism(right))
        )

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, _CallableForm) or other.parent() is not self.parent():
            return False
        if self._evaluation is other._evaluation:
            return True
        raise NotImplementedError("equality of arbitrary callable forms is not decidable")

    def __ne__(self, other):
        return not self.__eq__(other)

    def _repr_(self):
        return f"Extensional {self.parent().kind()} form with values in {self.codomain()}"


class _CallableFormSpace(Parent):
    Element = _CallableForm

    def __init__(self, left_module, right_module, value_module, kind) -> None:
        self._left_module = left_module
        self._right_module = right_module
        self._value_module = value_module
        self._kind = kind
        Parent.__init__(self, category=Sets())

    def left_module(self):
        return self._left_module

    def right_module(self):
        return self._right_module

    def module(self):
        if self.kind() == "quadratic" or self.left_module() is self.right_module():
            return self.left_module()
        raise TypeError("a pairing of distinct modules is not a form on one module")

    def codomain(self):
        return self._value_module

    def kind(self):
        return self._kind

    def _element_constructor_(self, datum):
        if isinstance(datum, _CallableForm) and datum.parent() is self:
            return datum
        return self.element_class(self, datum)


@cached_function(key=lambda left_module, right_module, value_module, kind: (id(left_module), id(right_module), id(value_module), kind))
def _callable_form_space(left_module, right_module, value_module, kind):
    space = _CallableFormSpace(left_module, right_module, value_module, kind)
    return space


def is_bilinear_form(form) -> bool:
    if isinstance(form, _CallableForm):
        return form.parent().kind() == "bilinear" and form.left_module() is form.right_module()
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        TensorProductModuleMorphism,
    )

    return (
        isinstance(form, TensorProductModuleMorphism)
        and form.left_module() is form.right_module()
    )


def is_quadratic_form(form) -> bool:
    if isinstance(form, _CallableForm):
        return form.parent().kind() == "quadratic"
    from dzack_research.preamble.categories.modules.powers import (
        QuadraticModuleMorphism,
    )

    return isinstance(form, QuadraticModuleMorphism)


def Pairings(left_module, right_module, value_module):
    r"""Return ``Hom_R(X tensor_R Y,W)`` whenever that universal object exists."""
    if left_module is right_module:
        return BilinearForms(left_module, value_module)
    from dzack_research.preamble.categories.abstract_categories.constructions import TensorProduct
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

    if _value_module_over(value_module, left_module.base_ring()):
        try:
            tensor_product = TensorProduct(left_module, right_module)
        except NotImplementedError:
            pass
        else:
            return module_homset(tensor_product, value_module)
    return _callable_form_space(left_module, right_module, value_module, "bilinear")


def BilinearForms(module, value_module):
    r"""Return ``Hom_R(M tensor_R M,W)`` whenever that universal object exists."""
    from dzack_research.preamble.categories.abstract_categories.constructions import TensorProduct
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

    if _value_module_over(value_module, module.base_ring()):
        try:
            tensor_product = TensorProduct(module, module)
        except NotImplementedError:
            pass
        else:
            return refine(
                module_homset(tensor_product, value_module),
                BilinearFormHoms(module.base_ring()),
            )
    return _callable_form_space(module, module, value_module, "bilinear")


def QuadraticForms(module, value_module):
    r"""Return ``Hom_R(Gamma^2(M),W)`` whenever the divided square is represented."""
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
    from dzack_research.preamble.categories.modules.powers import DividedSquare

    if _value_module_over(value_module, module.base_ring()):
        try:
            square = DividedSquare(module)
        except NotImplementedError:
            pass
        else:
            return module_homset(square, value_module)
    return _callable_form_space(module, module, value_module, "quadratic")


from dzack_research.preamble.categories.modules.powers import (
    QuadraticModuleHomset as QuadraticFormHomset,
    QuadraticModuleMorphism as QuadraticFormMorphism,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    TensorProductModuleHomset as BilinearFormHomset,
    TensorProductModuleMorphism as BilinearFormMorphism,
    TensorProductModuleMorphism as PairingMorphism,
)

QuadraticMapMorphism = QuadraticFormMorphism


def QuadraticMap(module, value_module, function):
    r"""Return the quadratic map ``module -> value_module`` via its classifier."""
    forms = QuadraticForms(module, value_module)
    constructor = getattr(forms, "from_quadratic_map", None)
    return forms(function) if constructor is None else constructor(function)


def classifying_morphism(quadratic):
    r"""Return the unique linear map ``Gamma^2(M) -> W`` classifying ``quadratic``."""
    from dzack_research.preamble.categories.modules.powers import (
        QuadraticModuleMorphism,
    )
    from dzack_research.preamble.categories.modules.powers import DividedSquare

    if isinstance(quadratic, QuadraticModuleMorphism):
        return quadratic
    square = DividedSquare(quadratic.module())
    return square.from_quadratic(quadratic, quadratic.codomain())


def quadratic_map_from_morphism(module, morphism):
    r"""Recover the quadratic map classified by ``morphism: Gamma^2(M) -> W``."""
    from dzack_research.preamble.categories.modules.powers import DividedSquare
    from dzack_research.preamble.categories.modules.powers import (
        QuadraticModuleMorphism,
    )

    square = DividedSquare(module)
    if morphism.domain() is not square:
        raise ValueError("the classifier morphism has the wrong divided-square domain")
    if isinstance(morphism, QuadraticModuleMorphism):
        return morphism
    return QuadraticMap(
        module,
        morphism.codomain(),
        lambda element: morphism(square.quadratic(element)),
    )
