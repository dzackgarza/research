r"""Exact pairings and bilinear or quadratic forms on framed modules.

A pairing is an element of \(\operatorname{Hom}_R(X\otimes_R Y,W)\).  A
bilinear form is the diagonal \(X=Y\).  The active module layer does not
materialize a general tensor-product parent yet, so the pairing stores that
universal datum directly: its left and right modules, value module, and
either its evaluation or its values on the chosen framings.  Nothing pretends
that a set product is the tensor product merely to satisfy a Sage ``Homset``
constructor.
"""

from sage.categories.rings import Rings as SageRings
from sage.categories.sets_cat import Sets
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import Element
from sage.structure.parent import Parent

from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.rings import engine_ring


def _finite_framing(module) -> tuple:
    labels = module.module_generating_set()
    try:
        finite = labels.cardinality() in SageZZ
    except AttributeError:
        finite = False
    if not finite:
        raise TypeError("a coordinate Gram presentation requires a finite module framing")
    return tuple(labels)


def _coerce_value(value_module, value):
    if value_module in SageRings():
        return engine_ring(value_module)(value)
    return value_module(value)


def _coordinate_values(form, left, right):
    left_module = form.left_module()
    right_module = form.right_module()
    if left.parent() is not left_module or right.parent() is not right_module:
        raise TypeError(f"the pairing takes an element of {left_module} and an element of {right_module}")
    left_coefficients = module_coefficients(left, left_module)
    right_coefficients = module_coefficients(right, right_module)
    zero = form.codomain().zero()
    total = zero
    for left_label, left_coefficient in left_coefficients.items():
        for right_label, right_coefficient in right_coefficients.items():
            total += left_coefficient * right_coefficient * form._gram_entry(left_label, right_label)
    return _coerce_value(form.codomain(), total)


class _FormSpace(Parent):
    Element = Element

    def __init__(self, module, value_module) -> None:
        self._module = module
        self._value_module = value_module
        Parent.__init__(self, category=Sets())

    def module(self):
        return self._module

    def left_module(self):
        return self._module

    def right_module(self):
        return self._module

    def codomain(self):
        return self._value_module


class BilinearFormMorphism(Element):
    r"""An exact bilinear form ``M x M -> W``.

    This represents the corresponding linear morphism ``M tensor M -> W``;
    the tensor-product parent itself is intentionally not fabricated.
    """

    def __init__(self, parent, datum) -> None:
        Element.__init__(self, parent)
        self._pairing = None
        self._labels = None
        self._label_positions = None
        self._gram = None
        if callable(datum) and not hasattr(datum, "rows"):
            self._pairing = datum
            return
        labels = _finite_framing(parent.module())
        rows = tuple(tuple(row) for row in (datum.rows() if hasattr(datum, "rows") else datum))
        if len(rows) != len(labels) or any(len(row) != len(labels) for row in rows):
            raise ValueError(f"the Gram presentation must have shape {len(labels)} x {len(labels)}")
        self._labels = labels
        self._label_positions = {label: position for position, label in enumerate(labels)}
        self._gram = tuple(tuple(_coerce_value(parent.codomain(), entry) for entry in row) for row in rows)

    def module(self):
        return self.parent().module()

    def left_module(self):
        return self.parent().left_module()

    def right_module(self):
        return self.parent().right_module()

    def codomain(self):
        return self.parent().codomain()

    def _gram_entry(self, left_label, right_label):
        if self._gram is None:
            raise TypeError("this form is represented by its pairing, not a Gram array")
        i = self._label_positions[left_label]
        j = self._label_positions[right_label]
        return self._gram[i][j]

    def __call__(self, left, right):
        if self._pairing is not None:
            if left.parent() is not self.module() or right.parent() is not self.module():
                raise TypeError(f"the form pairs elements of {self.module()}")
            return _coerce_value(self.codomain(), self._pairing(left, right))
        return _coordinate_values(self, left, right)

    def norm(self, element):
        return self(element, element)

    def values_matrix(self):
        if self._gram is None:
            raise TypeError("a form supplied only by a pairing has no finite values matrix")
        return self._gram

    def gram_tensor(self):
        r"""Return the scalar-valued Gram tensor in the selected framing."""
        if self._gram is None:
            raise TypeError("a form supplied only by a pairing has no finite Gram tensor")
        if self.codomain() not in SageRings():
            raise TypeError("a Gram tensor here requires scalar-valued form entries")
        from dzack_research.preamble.tensors import tensor

        rank = len(self._gram)
        return tensor(self.codomain(), (), (rank, rank), self._gram)

    def polar_form(self):
        r"""Return the polar form of ``q(x)=b(x,x)``, namely ``2b``."""
        return BilinearForms(self.module(), self.codomain())(lambda left, right: 2 * self(left, right))

    def pullback(self, morphism):
        if morphism.codomain() is not self.module():
            raise ValueError("the pullback map must land in the form's module")
        forms = BilinearForms(morphism.domain(), self.codomain())
        if self._gram is None:
            return forms(lambda left, right: self(morphism(left), morphism(right)))
        generators = tuple(morphism.domain().module_generators())
        return forms([[self(morphism(left), morphism(right)) for right in generators] for left in generators])

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, BilinearFormMorphism):
            return False
        if self.module() is not other.module() or self.codomain() is not other.codomain():
            return False
        assert self.module().module_generating_set().cardinality() in SageZZ
        generators = tuple(self.module().module_generators())
        return all(self(left, right) == other(left, right) for left in generators for right in generators)

    def _repr_(self):
        return f"Bilinear form on {self.module()} with values in {self.codomain()}"


class BilinearFormSpace(_FormSpace):
    Element = BilinearFormMorphism

    def _element_constructor_(self, datum):
        if isinstance(datum, BilinearFormMorphism) and datum.parent() is self:
            return datum
        return self.element_class(self, datum)

    def _repr_(self):
        return f"Bilinear forms on {self.module()} with values in {self.codomain()}"


class QuadraticFormMorphism(Element):
    r"""An exact quadratic form on a framed module."""

    def __init__(self, parent, datum) -> None:
        Element.__init__(self, parent)
        self._value_map = None
        self._lift = None
        if callable(datum) and not hasattr(datum, "rows"):
            self._value_map = datum
            return
        lift = BilinearForms(parent.module(), parent.codomain())(datum)
        gram = lift.values_matrix()
        if any(gram[i][j] != gram[j][i] for i in range(len(gram)) for j in range(len(gram))):
            raise ValueError("the bilinear lift of a quadratic form must be symmetric")
        self._lift = lift

    def module(self):
        return self.parent().module()

    def codomain(self):
        return self.parent().codomain()

    def __call__(self, element):
        if element.parent() is not self.module():
            raise TypeError(f"the quadratic form is defined on {self.module()}")
        if self._value_map is not None:
            return _coerce_value(self.codomain(), self._value_map(element))
        return self._lift(element, element)

    def lift_form(self):
        if self._lift is None:
            raise TypeError("a quadratic form supplied by its value map has no chosen bilinear lift")
        return self._lift

    def polar_form(self):
        return BilinearForms(self.module(), self.codomain())(lambda left, right: self(left + right) - self(left) - self(right))

    def b(self, left, right):
        return self.polar_form()(left, right)

    def values_matrix(self):
        generators = tuple(self.module().module_generators())
        return tuple(
            tuple(self(generator_left + generator_right) - self(generator_left) - self(generator_right) for generator_right in generators) for generator_left in generators
        )

    def pullback(self, morphism):
        if morphism.codomain() is not self.module():
            raise ValueError("the pullback map must land in the form's module")
        forms = QuadraticForms(morphism.domain(), self.codomain())
        if self._lift is None:
            return forms(lambda element: self(morphism(element)))
        generators = tuple(morphism.domain().module_generators())
        return forms([[self._lift(morphism(left), morphism(right)) for right in generators] for left in generators])

    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, QuadraticFormMorphism):
            return False
        if self.module() is not other.module() or self.codomain() is not other.codomain():
            return False
        assert self.module().module_generating_set().cardinality() in SageZZ
        generators = tuple(self.module().module_generators())
        probes = generators + tuple(left + right for i, left in enumerate(generators) for right in generators[i + 1 :])
        return all(self(element) == other(element) for element in probes)

    def _repr_(self):
        return f"Quadratic form on {self.module()} with values in {self.codomain()}"


class QuadraticFormSpace(_FormSpace):
    Element = QuadraticFormMorphism

    def _element_constructor_(self, datum):
        if isinstance(datum, QuadraticFormMorphism) and datum.parent() is self:
            return datum
        return self.element_class(self, datum)

    def _repr_(self):
        return f"Quadratic forms on {self.module()} with values in {self.codomain()}"


class PairingMorphism(Element):
    r"""An exact pairing \(X\times Y\to W\), i.e. a map \(X\otimes_R Y\to W\)."""

    def __init__(self, parent, datum) -> None:
        Element.__init__(self, parent)
        self._pairing = None
        self._left_labels = None
        self._right_labels = None
        self._gram = None
        if callable(datum) and not hasattr(datum, "rows"):
            self._pairing = datum
            return
        left_labels = _finite_framing(parent.left_module())
        right_labels = _finite_framing(parent.right_module())
        rows = tuple(tuple(row) for row in (datum.rows() if hasattr(datum, "rows") else datum))
        if len(rows) != len(left_labels) or any(len(row) != len(right_labels) for row in rows):
            raise ValueError(f"the pairing presentation must have shape {len(left_labels)} x {len(right_labels)}")
        self._left_labels = left_labels
        self._right_labels = right_labels
        self._gram = tuple(tuple(_coerce_value(parent.codomain(), entry) for entry in row) for row in rows)

    def left_module(self):
        return self.parent().left_module()

    def right_module(self):
        return self.parent().right_module()

    def codomain(self):
        return self.parent().codomain()

    def _gram_entry(self, left_label, right_label):
        if self._gram is None:
            raise TypeError("this pairing is represented by its evaluation, not a values array")
        i = self._left_labels.index(left_label)
        j = self._right_labels.index(right_label)
        return self._gram[i][j]

    def __call__(self, left, right):
        if self._pairing is not None:
            if left.parent() is not self.left_module() or right.parent() is not self.right_module():
                raise TypeError(f"the pairing takes an element of {self.left_module()} and an element of {self.right_module()}")
            return _coerce_value(self.codomain(), self._pairing(left, right))
        return _coordinate_values(self, left, right)

    def values_matrix(self):
        if self._gram is None:
            raise TypeError("a pairing supplied only by evaluation has no finite values matrix")
        return self._gram

    def _repr_(self):
        return f"Pairing {self.left_module()} ⊗ {self.right_module()} -> {self.codomain()}"


class PairingSpace(Parent):
    Element = PairingMorphism

    def __init__(self, left_module, right_module, value_module) -> None:
        self._left_module = left_module
        self._right_module = right_module
        self._value_module = value_module
        Parent.__init__(self, category=Sets())

    def left_module(self):
        return self._left_module

    def right_module(self):
        return self._right_module

    def module(self):
        if self._left_module is not self._right_module:
            raise TypeError("a pairing of two modules is not a form on one module")
        return self._left_module

    def codomain(self):
        return self._value_module

    def _element_constructor_(self, datum):
        if isinstance(datum, PairingMorphism) and datum.parent() is self:
            return datum
        return self.element_class(self, datum)

    def _repr_(self):
        return f"Pairings {self.left_module()} ⊗ {self.right_module()} -> {self.codomain()}"


_PAIRING_SPACE_CACHE = {}
_BILINEAR_FORM_SPACE_CACHE = {}
_QUADRATIC_FORM_SPACE_CACHE = {}


def _identity_cached_space(cache, objects, constructor):
    r"""Cache a typed space only when its argument objects are identical.

    Sage parents that are equal as computational quotients can still carry
    different selected mathematical structure.  The domain/codomain of a
    form is part of its type, so equality is not an admissible cache key.
    Repeated calls on the very same objects should nevertheless return the
    same Hom/form space, as ordinary category syntax expects.
    """
    key = tuple(id(obj) for obj in objects)
    cached = cache.get(key)
    if cached is not None and all(cached_object is requested_object for cached_object, requested_object in zip(cached[:-1], objects, strict=True)):
        return cached[-1]
    space = constructor(*objects)
    cache[key] = (*objects, space)
    return space


def Pairings(left_module, right_module, value_module):
    r"""Return \(\operatorname{Hom}_R(X\otimes_R Y,W)\)."""
    if left_module is right_module:
        return BilinearForms(left_module, value_module)
    return _identity_cached_space(
        _PAIRING_SPACE_CACHE,
        (left_module, right_module, value_module),
        PairingSpace,
    )


def BilinearForms(module, value_module) -> BilinearFormSpace:
    return _identity_cached_space(
        _BILINEAR_FORM_SPACE_CACHE,
        (module, value_module),
        BilinearFormSpace,
    )


def QuadraticForms(module, value_module) -> QuadraticFormSpace:
    return _identity_cached_space(
        _QUADRATIC_FORM_SPACE_CACHE,
        (module, value_module),
        QuadraticFormSpace,
    )


def BilinearForm(module, value_module, datum):
    r"""Return the module ``module`` equipped with the stated bilinear form."""
    from dzack_research.preamble.categories.modules.framed.formed import FormModule

    return FormModule(BilinearForms(module, value_module)(datum))


def QuadraticForm(module, value_module, datum):
    r"""Return the module ``module`` equipped with the stated quadratic form."""
    from dzack_research.preamble.categories.modules.framed.formed import FormModule

    return FormModule(QuadraticForms(module, value_module)(datum))


QuadraticMapMorphism = QuadraticFormMorphism
BilinearFormHomset = BilinearFormSpace
QuadraticFormHomset = QuadraticFormSpace


def QuadraticMap(module, value_module, function):
    r"""Return the represented quadratic map ``module -> value_module``."""
    return QuadraticForms(module, value_module)(function)


def classifying_morphism(quadratic):
    r"""Return the unique linear map ``Gamma^2(M) -> W`` classifying ``quadratic``."""
    from dzack_research.preamble.categories.modules.quadratic_square import DividedSquare

    square = DividedSquare(quadratic.module())
    return square.from_quadratic(quadratic, quadratic.codomain())


def quadratic_map_from_morphism(module, morphism):
    r"""Recover the quadratic map classified by ``morphism: Gamma^2(M) -> W``."""
    from dzack_research.preamble.categories.modules.quadratic_square import DividedSquare

    square = DividedSquare(module)
    if morphism.domain() is not square:
        raise ValueError("the classifier morphism has the wrong divided-square domain")
    return QuadraticMap(
        module,
        morphism.codomain(),
        lambda element: morphism(square.quadratic(element)),
    )
