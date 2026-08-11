r"""Bilinear and quadratic forms as native Sage morphisms."""


from sage.rings.rational_field import QQ as SageQQ
from typing import TYPE_CHECKING
from sage_lattice_category_spike.lexicon import Element
if TYPE_CHECKING:
    from sage_lattice_category_spike.lexicon import Module

if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism

from sage.rings.integer import Integer
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.matrix.matrix0 import Matrix
from sage.structure.parent import Parent
from sage_lattice_category_spike.lexicon import GramMatrix
from sage_lattice_category_spike.objects.cardinals import Cardinal
from sage.rings.integer_ring import ZZ as SageZZ

from sage_lattice_category_spike.objects.sets import Sets


if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from sage_lattice_category_spike.lexicon import OrderedSet


def _framing_rank(module_generating_set: "OrderedSet") -> Integer:
    size = module_generating_set.cardinality()
    if isinstance(size, Cardinal):
        assert size.is_finite(), "a Gram matrix requires a finite framing set"
        return size.finite_value()
    assert size in SageZZ, "a Gram matrix requires a finite framing set"
    return SageZZ(size)


class TensorSquare(Parent):
    r"""The formal tensor square \(M\otimes_R M\), as a morphism domain."""

    def __init__(self, module: "Module") -> None:
        self._module = module
        Parent.__init__(self, category=Sets())

    def module(self) -> "Module":
        return self._module

    def __eq__(self, other: object) -> bool:
        return isinstance(other, TensorSquare) and self._module is other._module

    def __hash__(self) -> int:
        return hash((TensorSquare, id(self._module)))

    def _repr_(self) -> str:
        return f"Tensor square of {self._module}"


class DividedSquare(Parent):
    r"""The divided square \(\Gamma^2 M\), as a morphism domain.

    A quadratic form is not a morphism of modules: \(q(rx)=r^2q(x)\), so it
    does not lie in \(\operatorname{Hom}_R(M,W)\).  What it *is* is a morphism
    out of the divided square, \(\Gamma^2M\to W\), the way a bilinear form is
    one out of \(M\otimes_R M\).  Evaluating \(q\) at \(x\) means applying
    it to \(\gamma_2(x)\).

    Formal, like ``TensorSquare`` beside it: what the preamble needs of it is
    that a form has an honest domain, not that its elements are constructed.
    """

    def __init__(self, module: "Module") -> None:
        self._module = module
        Parent.__init__(self, category=Sets())

    def module(self) -> "Module":
        return self._module

    def __eq__(self, other: object) -> bool:
        return isinstance(other, DividedSquare) and self._module is other._module

    def __hash__(self) -> int:
        return hash((DividedSquare, id(self._module)))

    def _repr_(self) -> str:
        return f"Divided square of {self._module}"


class BilinearFormHomset(Homset):
    r"""The homset of bilinear forms \(M\otimes_RM\to W\)."""

    def __init__(self, module: "Module", value_module: "Module") -> None:
        self._module = module
        Homset.__init__(
            self,
            TensorSquare(module),
            value_module,
            category=Sets(),
        )

    def module(self) -> "Module":
        return self._module

    def _element_constructor_(self, gram: "GramMatrix") -> "BilinearFormMorphism":
        return BilinearFormMorphism(self, gram)

    def __contains__(self, form: "FormMorphism") -> bool:
        return (
            isinstance(form, BilinearFormMorphism)
            and form.parent() is self
        )

    def _repr_(self) -> str:
        return (
            f"Bilinear forms on {self._module} with values in "
            f"{self.codomain()}"
        )


class QuadraticFormHomset(Homset):
    r"""The homset of quadratic forms, \(\Gamma^2M\to W\)."""

    def __init__(self, module: "Module", value_module: "Module") -> None:
        Homset.__init__(
            self,
            DividedSquare(module),
            value_module,
            category=Sets(),
        )

    def module(self) -> "Module":
        r"""Return \(M\), which the domain is the divided square of."""
        return self.domain().module()

    def _element_constructor_(self, gram: "GramMatrix") -> "QuadraticFormMorphism":
        return QuadraticFormMorphism(self, gram)

    def __contains__(self, form: "FormMorphism") -> bool:
        return (
            isinstance(form, QuadraticFormMorphism)
            and form.parent() is self
        )

    def _repr_(self) -> str:
        return (
            f"Quadratic forms on {self.module()} with values in "
            f"{self.codomain()}"
        )


def _form_homset_cache(module: "Module") -> dict:
    return module.__dict__.setdefault("_form_homsets", {})


def BilinearForms(module: "Module", value_module: "Module") -> BilinearFormHomset:
    r"""Return the canonical homset of bilinear forms on ``module``."""
    key = ("bilinear", value_module)
    cache = _form_homset_cache(module)
    if key not in cache:
        cache[key] = BilinearFormHomset(module, value_module)
    return cache[key]


def QuadraticForms(module: "Module", value_module: "Module") -> QuadraticFormHomset:
    r"""Return the canonical homset of quadratic forms on ``module``."""
    key = ("quadratic", value_module)
    cache = _form_homset_cache(module)
    if key not in cache:
        cache[key] = QuadraticFormHomset(module, value_module)
    return cache[key]


def _forget_form_element(element: "Element") -> "Element":
    # Local: form_modules imports this module, so a module-level import here
    # would close that cycle; it is built by the time this function runs.
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModuleElement

    match element:
        case FormModuleElement():
            return element.forget_form()
        case Element():
            return element
        case _:
            assert False, f"{element!r} is not a module element"


class BilinearFormMorphism(Morphism):
    r"""A morphism \(M\otimes_RM\to W\), recorded on a finite framing."""

    def __init__(self, parent: BilinearFormHomset, gram: "GramMatrix") -> None:
        Morphism.__init__(self, parent)
        gram = gram if isinstance(gram, Matrix) else matrix(gram)
        module = parent.module()
        size = _framing_rank(module.module_generating_set())
        assert gram.nrows() == size and gram.ncols() == size, (
            f"the Gram matrix is {gram.nrows()}x{gram.ncols()} but the "
            f"framing set has cardinality {size}"
        )
        assert all(entry in parent.codomain() for entry in gram.list()), (
            f"the form does not take values in {parent.codomain()}"
        )
        self._gram_matrix = gram

    def module(self) -> "Module":
        return self.parent().module()

    def value_module(self) -> "Module":
        return self.codomain()

    def gram_matrix(self) -> GramMatrix:
        return GramMatrix(self._gram_matrix)

    def __call__(self, left: "Element", right: "Element") -> "Element":
        # Local: the morphism node imports this module, so a module-level
        # import would close that cycle; it is built by call time.
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector

        assert all(
            element.parent() is self.module()
            for element in (left, right)
        ), f"the form pairs elements of {self.module()}"
        return self.codomain()(
            _coordinate_vector(left)
            * self._gram_matrix
            * _coordinate_vector(right)
        )

    def b(self, left: "Element", right: "Element") -> "Element":
        return self(left, right)

    def norm(self, element: "Element") -> "Element":
        return self(element, element)

    def polar_form(self) -> "BilinearFormMorphism":
        return self

    def on_module(self, module: "Module") -> "BilinearFormMorphism":
        return BilinearForms(module, self.codomain())(self._gram_matrix)

    def reduced(self, value_module: "Module") -> "BilinearFormMorphism":
        return BilinearForms(self.module(), value_module)(self._gram_matrix)

    def base_changed(self, module: "Module") -> "BilinearFormMorphism":
        r"""Return this form on ``module``, valued in ``module``'s base ring.

        The transport of a form along a ring map \(f:R\to S\).  The entries do
        not change -- they are carried by \(f\) -- and what changes is the ring
        they are read in, which is the ring the pairings of \(M\otimes_RS\)
        take their values in.
        """
        # Local: importing the ring node here would close a cycle, and the
        # module is built by the time this method runs.
        from dzack_research.preamble.categories.rings.rings import engine_ring

        value_ring = module.base_ring()
        return BilinearForms(module, value_ring)(
            self._gram_matrix.change_ring(engine_ring(value_ring))
        )

    def pullback(self, morphism: "Morphism") -> "BilinearFormMorphism":
        # Local: the morphism node imports this module, so a module-level
        # import would close that cycle; it is built by call time.
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _underlying_module

        matrix_of_map = morphism.matrix()._sage_matrix()
        domain = _underlying_module(morphism.domain())
        return BilinearForms(domain, self.codomain())(
            GramMatrix(
                matrix_of_map
                * self._gram_matrix
                * matrix_of_map.transpose()
            )
        )

    def descends_along(self, morphism: "Morphism") -> bool:
        return all(
            self(
                _forget_form_element(morphism(domain.module_generator(label))),
                _forget_form_element(codomain.module_generator(target_label)),
            )
            in SageZZ
            for domain, codomain in [(morphism.domain(), morphism.codomain())]
            for label in domain.module_generating_set()
            for target_label in codomain.module_generating_set()
        )

    def values_matrix(self) -> tuple:
        return tuple(
            tuple(self.codomain()(entry) for entry in row)
            for row in self._gram_matrix.rows()
        )

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, BilinearFormMorphism)
            and self.parent() is other.parent()
            and self.values_matrix() == other.values_matrix()
        )

    def __hash__(self) -> int:
        return hash((id(self.parent()), self.values_matrix()))

    def _repr_type(self) -> str:
        return "Bilinear form"

    def _repr_defn(self) -> str:
        return repr(self._gram_matrix)


class QuadraticFormMorphism(Morphism):
    r"""A quadratic form \(\Gamma^2M\to W\), recorded by its diagonal lift.

    Evaluated at an element of \(M\): \(q(x)\) is this morphism applied to
    \(\gamma_2(x)\), and writing it that way is what keeps a quadratic form
    a morphism without pretending it is linear on \(M\).
    """

    def __init__(self, parent: QuadraticFormHomset, gram: "GramMatrix") -> None:
        Morphism.__init__(self, parent)
        gram = gram if isinstance(gram, Matrix) else matrix(gram)
        size = _framing_rank(parent.module().module_generating_set())
        assert gram.is_symmetric(), (
            "the diagonal lift of a quadratic form is symmetric"
        )
        assert gram.nrows() == size and gram.ncols() == size, (
            f"the Gram matrix is {gram.nrows()}x{gram.ncols()} but the "
            f"framing set has cardinality {size}"
        )
        assert all(entry in parent.codomain() for entry in gram.list()), (
            f"the form does not take values in {parent.codomain()}"
        )
        self._lift_matrix = gram

    def module(self) -> "Module":
        return self.domain().module()

    def value_module(self) -> "Module":
        return self.codomain()

    def __call__(self, element: "Element") -> "Element":
        # Local: the morphism node imports this module, so a module-level
        # import would close that cycle; it is built by call time.
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector

        assert element.parent() is self.module(), (
            f"{element} is not an element of {self.module()}"
        )
        coordinates = _coordinate_vector(element)
        return self.codomain()(
            coordinates * self._lift_matrix * coordinates
        )

    def norm(self, element: "Element") -> "Element":
        return self(element)

    def lift_form(self) -> BilinearFormMorphism:
        return BilinearForms(self.module(), SageQQ)(self._lift_matrix)

    def _polar_value_module(self) -> "Module":
        from sage.groups.additive_abelian.qmodnz import QmodnZ

        assert isinstance(self.codomain(), QmodnZ), (
            "halving the value modulus is defined here only for Q/nZ"
        )
        return QmodnZ(self.codomain().n / 2)

    def polar_form(self) -> BilinearFormMorphism:
        return BilinearForms(
            self.module(),
            self._polar_value_module(),
        )(self._lift_matrix)

    def b(self, left: "Element", right: "Element") -> "Element":
        return self.polar_form()(left, right)

    def gram_matrix(self) -> GramMatrix:
        size = self._lift_matrix.nrows()
        upper = matrix(
            self._lift_matrix.base_ring(),
            [
                [
                    self._lift_matrix[row, column]
                    if row == column
                    else 2 * self._lift_matrix[row, column]
                    if row < column
                    else self._lift_matrix.base_ring().zero()
                    for column in range(size)
                ]
                for row in range(size)
            ],
        )
        upper.subdivide(*self._lift_matrix.subdivisions())
        return GramMatrix(upper)

    def on_module(self, module: "Module") -> "QuadraticFormMorphism":
        return QuadraticForms(module, self.codomain())(self._lift_matrix)

    def base_changed(self, module: "Module") -> "QuadraticFormMorphism":
        r"""Return this form on ``module``, valued in ``module``'s base ring.

        A quadratic form is transported by its lift, which is the matrix that
        records it, so the transport is the bilinear one on that matrix.
        """
        # Local: importing the ring node here would close a cycle, and the
        # module is built by the time this method runs.
        from dzack_research.preamble.categories.rings.rings import engine_ring

        value_ring = module.base_ring()
        return QuadraticForms(module, value_ring)(
            self._lift_matrix.change_ring(engine_ring(value_ring))
        )

    def pullback(self, morphism: "Morphism") -> "QuadraticFormMorphism":
        # Local: the morphism node imports this module, so a module-level
        # import would close that cycle; it is built by call time.
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _underlying_module

        matrix_of_map = morphism.matrix()._sage_matrix()
        domain = _underlying_module(morphism.domain())
        return QuadraticForms(domain, self.codomain())(
            matrix_of_map
            * self._lift_matrix
            * matrix_of_map.transpose()
        )

    def descends_along(self, morphism: "Morphism") -> bool:
        if not self.lift_form().descends_along(morphism):
            return False
        return all(
            self(_forget_form_element(morphism(morphism.domain().module_generator(label))))
            == self.codomain().zero()
            for label in morphism.domain().module_generating_set()
        )

    def values_matrix(self) -> tuple:
        return tuple(
            tuple(self.codomain()(entry) for entry in row)
            for row in self.gram_matrix().rows()
        )

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, QuadraticFormMorphism)
            and self.parent() is other.parent()
            and self.values_matrix() == other.values_matrix()
        )

    def __hash__(self) -> int:
        return hash((id(self.parent()), self.values_matrix()))

    def _repr_type(self) -> str:
        return "Quadratic form"

    def _repr_defn(self) -> str:
        return repr(self.gram_matrix())


def BilinearForm(module: "Module", value_module: "Module", gram_matrix: "GramMatrix") -> "BilinearFormMorphism":
    r"""Construct the formed module classified by a bilinear form."""
    # Local: form_modules imports this module, so a module-level import here
    # would close that cycle; it is built by the time this function runs.
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule

    return FormModule(BilinearForms(module, value_module)(gram_matrix))


def QuadraticForm(module: "Module", value_module: "Module", gram_matrix: "GramMatrix") -> "QuadraticFormMorphism":
    r"""Construct the formed module classified by a quadratic form."""
    # Local: form_modules imports this module, so a module-level import here
    # would close that cycle; it is built by the time this function runs.
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule

    return FormModule(QuadraticForms(module, value_module)(gram_matrix))
