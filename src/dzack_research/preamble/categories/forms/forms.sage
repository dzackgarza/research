r"""Bilinear and quadratic forms as native Sage morphisms."""

from typing import Any

from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.matrix.matrix0 import Matrix
from sage.structure.parent import Parent

from sage_lattice_category_spike.objects.sets import Sets


class TensorSquare(Parent):
    r"""The formal tensor square \(M\otimes_R M\), as a morphism domain."""

    def __init__(self, module: Any) -> None:
        self._module = module
        Parent.__init__(self, category=Sets())

    def module(self) -> Any:
        return self._module

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, TensorSquare) and self._module is other._module

    def __hash__(self) -> int:
        return hash((TensorSquare, id(self._module)))

    def _repr_(self) -> str:
        return f"Tensor square of {self._module}"


class BilinearFormHomset(Homset):
    r"""The homset of bilinear forms \(M\otimes_RM\to W\)."""

    def __init__(self, module: Any, value_module: Any) -> None:
        self._module = module
        Homset.__init__(
            self,
            TensorSquare(module),
            value_module,
            category=Sets(),
            check=False,
        )

    def module(self) -> Any:
        return self._module

    def _element_constructor_(self, gram: Any) -> "BilinearFormMorphism":
        return BilinearFormMorphism(self, gram)

    def __contains__(self, form: Any) -> bool:
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
    r"""The homset of quadratic forms \(M\to W\)."""

    def __init__(self, module: Any, value_module: Any) -> None:
        Homset.__init__(
            self,
            module,
            value_module,
            category=Sets(),
            check=False,
        )

    def module(self) -> Any:
        return self.domain()

    def _element_constructor_(self, gram: Any) -> "QuadraticFormMorphism":
        return QuadraticFormMorphism(self, gram)

    def __contains__(self, form: Any) -> bool:
        return (
            isinstance(form, QuadraticFormMorphism)
            and form.parent() is self
        )

    def _repr_(self) -> str:
        return (
            f"Quadratic forms on {self.domain()} with values in "
            f"{self.codomain()}"
        )


def _form_homset_cache(module: Any) -> dict:
    return module.__dict__.setdefault("_form_homsets", {})


def BilinearForms(module: Any, value_module: Any) -> BilinearFormHomset:
    r"""Return the canonical homset of bilinear forms on ``module``."""
    key = ("bilinear", value_module)
    cache = _form_homset_cache(module)
    if key not in cache:
        cache[key] = BilinearFormHomset(module, value_module)
    return cache[key]


def QuadraticForms(module: Any, value_module: Any) -> QuadraticFormHomset:
    r"""Return the canonical homset of quadratic forms on ``module``."""
    key = ("quadratic", value_module)
    cache = _form_homset_cache(module)
    if key not in cache:
        cache[key] = QuadraticFormHomset(module, value_module)
    return cache[key]


def _forget_form_element(element: Any) -> Any:
    match element:
        case FormModuleElement():
            return element.forget_form()
        case Element():
            return element
        case _:
            raise TypeError(f"{element!r} is not a module element")


class BilinearFormMorphism(Morphism):
    r"""A morphism \(M\otimes_RM\to W\), recorded on a finite framing."""

    def __init__(self, parent: BilinearFormHomset, gram: Any) -> None:
        Morphism.__init__(self, parent)
        gram = gram if isinstance(gram, Matrix) else matrix(gram)
        module = parent.module()
        size = module.generating_set().cardinality()
        assert size in ZZ, "a Gram matrix requires a finite framing set"
        assert gram.nrows() == size and gram.ncols() == size, (
            f"the Gram matrix is {gram.nrows()}x{gram.ncols()} but the "
            f"framing set has cardinality {size}"
        )
        assert all(entry in parent.codomain() for entry in gram.list()), (
            f"the form does not take values in {parent.codomain()}"
        )
        self._gram_matrix = gram

    def module(self) -> Any:
        return self.parent().module()

    def value_module(self) -> Any:
        return self.codomain()

    def gram_matrix(self) -> Matrix:
        return self._gram_matrix

    def __call__(self, left: Any, right: Any) -> Any:
        assert all(
            element.parent() is self.module()
            for element in (left, right)
        ), f"the form pairs elements of {self.module()}"
        return self.codomain()(
            _coordinate_vector(left)
            * self._gram_matrix
            * _coordinate_vector(right)
        )

    def b(self, left: Any, right: Any) -> Any:
        return self(left, right)

    def norm(self, element: Any) -> Any:
        return self(element, element)

    def polar_form(self) -> "BilinearFormMorphism":
        return self

    def on_module(self, module: Any) -> "BilinearFormMorphism":
        return BilinearForms(module, self.codomain())(self._gram_matrix)

    def reduced(self, value_module: Any) -> "BilinearFormMorphism":
        return BilinearForms(self.module(), value_module)(self._gram_matrix)

    def pullback(self, morphism: Any) -> "BilinearFormMorphism":
        matrix_of_map = morphism.matrix()
        domain = _underlying_module(morphism.domain())
        return BilinearForms(domain, self.codomain())(
            matrix_of_map
            * self._gram_matrix
            * matrix_of_map.transpose()
        )

    def descends_along(self, morphism: Any) -> bool:
        return all(
            self(
                _forget_form_element(morphism(domain.generator(label))),
                _forget_form_element(codomain.generator(target_label)),
            )
            in ZZ
            for domain, codomain in [(morphism.domain(), morphism.codomain())]
            for label in domain.generating_set()
            for target_label in codomain.generating_set()
        )

    def values_matrix(self) -> tuple:
        return tuple(
            tuple(self.codomain()(entry) for entry in row)
            for row in self._gram_matrix.rows()
        )

    def __eq__(self, other: Any) -> bool:
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
    r"""A quadratic morphism \(q:M\to W\), recorded by its diagonal lift."""

    def __init__(self, parent: QuadraticFormHomset, gram: Any) -> None:
        Morphism.__init__(self, parent)
        gram = gram if isinstance(gram, Matrix) else matrix(gram)
        size = parent.domain().generating_set().cardinality()
        assert size in ZZ, "a Gram matrix requires a finite framing set"
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

    def module(self) -> Any:
        return self.domain()

    def value_module(self) -> Any:
        return self.codomain()

    def __call__(self, element: Any) -> Any:
        assert element.parent() is self.domain(), (
            f"{element} is not an element of {self.domain()}"
        )
        coordinates = _coordinate_vector(element)
        return self.codomain()(
            coordinates * self._lift_matrix * coordinates
        )

    def norm(self, element: Any) -> Any:
        return self(element)

    def lift_form(self) -> BilinearFormMorphism:
        return BilinearForms(self.domain(), QQ)(self._lift_matrix)

    def _polar_value_module(self) -> Any:
        from sage.groups.additive_abelian.qmodnz import QmodnZ

        assert isinstance(self.codomain(), QmodnZ), (
            "halving the value modulus is defined here only for Q/nZ"
        )
        return QmodnZ(QQ(self.codomain().n) / 2)

    def polar_form(self) -> BilinearFormMorphism:
        return BilinearForms(
            self.domain(),
            self._polar_value_module(),
        )(self._lift_matrix)

    def b(self, left: Any, right: Any) -> Any:
        return self.polar_form()(left, right)

    def gram_matrix(self) -> Matrix:
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
        return upper

    def on_module(self, module: Any) -> "QuadraticFormMorphism":
        return QuadraticForms(module, self.codomain())(self._lift_matrix)

    def pullback(self, morphism: Any) -> "QuadraticFormMorphism":
        matrix_of_map = morphism.matrix()
        domain = _underlying_module(morphism.domain())
        return QuadraticForms(domain, self.codomain())(
            matrix_of_map
            * self._lift_matrix
            * matrix_of_map.transpose()
        )

    def descends_along(self, morphism: Any) -> bool:
        if not self.lift_form().descends_along(morphism):
            return False
        return all(
            self(_forget_form_element(morphism(morphism.domain().generator(label))))
            == self.codomain().zero()
            for label in morphism.domain().generating_set()
        )

    def values_matrix(self) -> tuple:
        return tuple(
            tuple(self.codomain()(entry) for entry in row)
            for row in self.gram_matrix().rows()
        )

    def __eq__(self, other: Any) -> bool:
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


def BilinearForm(module: Any, value_module: Any, gram_matrix: Any) -> Any:
    r"""Construct the formed module classified by a bilinear form."""
    return FormModule(BilinearForms(module, value_module)(gram_matrix))


def QuadraticForm(module: Any, value_module: Any, gram_matrix: Any) -> Any:
    r"""Construct the formed module classified by a quadratic form."""
    return FormModule(QuadraticForms(module, value_module)(gram_matrix))
