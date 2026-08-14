r"""Bilinear and quadratic forms as native Sage morphisms."""


from sage.rings.rational_field import QQ as SageQQ
from collections.abc import Callable
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.structure.parent import ElementConstructorInput, MembershipInput
from dzack_research.preamble.lexicon import Element
if TYPE_CHECKING:
    from sage.categories.modules import Module
    from sage.categories.rings import Ring

if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism

from sage.rings.integer import Integer
from sage.categories.homset import Homset
from sage.categories.homset import Hom
from sage.categories.morphism import Morphism, SetMorphism
from sage.structure.element import ModuleElement
from dzack_research.preamble.categories.sets.underlying_sets import UnderlyingSet
from sage.matrix.matrix0 import Matrix
from sage.structure.parent import Parent
from dzack_research.preamble.lexicon import GramMatrix
from dzack_research.preamble.categories.sets.cardinals import Cardinal
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.sets.owned_sets import Sets


if TYPE_CHECKING:
    Pairing = Callable[[Element, Element], Element]
    # The two ways one bilinear form is handed over: written down on a
    # framing, as a Gram matrix, or stated as the pairing it is.  A Gram
    # matrix is a ``NewType`` over ``Matrix``, which is the spelling here.
    FormDatum = Matrix | Pairing

    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        ModuleMorphism,
    )

    # What the graded constructions ask of the algebra they are cut out of,
    # and what the piece they return records.  Declared for the checker
    # only: at runtime the objects are the free algebra and the module the
    # constructions actually build.

    class _GradedAlgebra(Parent):
        r"""A free algebra read one degree at a time."""

        def zero(self) -> "Element": ...
        def one(self) -> "Element": ...
        def algebra_generator(self, label: "Element") -> "Element": ...
        def divided_square(self, element: "Element") -> "Element": ...
        def monomial_system(self) -> "Parent": ...
        def graded_piece(self, degree: "Integer | int") -> "_GradedPiece": ...
        def graded_piece_monomials(
            self, degree: "Integer | int"
        ) -> "OrderedSet | tuple": ...
        def ideal_generators_in_degree(
            self, relations: tuple, degree: "Integer | int"
        ) -> tuple: ...

    class _GradedPiece(Parent):
        r"""One graded piece \(A[n]\), marked with the module and the degree
        it was built from -- which is what lets a later call recognize it as
        the tensor, symmetric, alternating or divided power of that module."""

        _tensor_power_of: "Module"
        _tensor_power_degree: int
        _symmetric_power_of: "Module"
        _symmetric_power_degree: int
        _alternating_power_of: "Module"
        _alternating_power_degree: int
        _divided_power_of: "Module"
        _divided_power_degree: int
        _tensor_square_of: "Module"
        _divided_square_of: "Module"

        def zero(self) -> "Element": ...
        def base_ring(self) -> "Ring": ...
        def module_generating_set(self) -> "OrderedSet": ...
        def module_generators(self) -> "OrderedSet": ...


def _framing_rank(module_generating_set: "OrderedSet") -> Integer:
    size = module_generating_set.cardinality()
    if isinstance(size, Cardinal):
        assert size.is_finite(), "a Gram matrix requires a finite framing set"
        rank: Integer = size.finite_value()
        return rank
    assert size in SageZZ, "a Gram matrix requires a finite framing set"
    return SageZZ(size)


def _degree_construction(
    module: "Module",
    algebra_constructor: "Callable[[Ring, OrderedSet], _GradedAlgebra]",
    cache_key: str,
    degree: "Integer | int",
) -> "_GradedPiece":
    r"""Return one graded construction induced by a module presentation."""
    degree = int(degree)
    assert degree >= 0, "a graded degree is nonnegative"
    cache = module.__dict__.setdefault("_degree_constructions", {})
    cached: "_GradedPiece | None" = cache.get((cache_key, degree))
    if cached is not None:
        return cached

    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

    algebra = algebra_constructor(
        module.base_ring(), module.module_generating_set()
    )
    piece: "_GradedPiece" = algebra.graded_piece(degree)
    relations = module.relation_matrix()._sage_matrix()
    match relations.nrows():
        case 0:
            cache[(cache_key, degree)] = piece
            return piece
        case _:
            pass

    labels = tuple(module.module_generating_set())
    algebra_relations = tuple(
        sum(
            (
                coefficient * algebra.algebra_generator(label)
                for coefficient, label in zip(row, labels)
            ),
            algebra.zero(),
        )
        for row in relations.rows()
    )
    degree_relations = algebra.ideal_generators_in_degree(
        algebra_relations,
        degree,
    )
    monomials = tuple(
        next(iter(generator.coefficients()))
        for generator in algebra.graded_piece_monomials(degree)
    )
    relation_vectors = tuple(
        piece([
            relation.coefficients().get(monomial, module.base_ring().zero())
            for monomial in monomials
        ])
        for relation in degree_relations
    )
    relation_module = BasedFreeModule(
        module.base_ring(), Sets.Δ[len(relation_vectors) - 1]
    )
    presentation = module_homset(relation_module, piece)(
        dict(zip(relation_module.module_generating_set(), relation_vectors))
    )
    result: "_GradedPiece" = FinitelyPresentedModule(presentation)
    cache[(cache_key, degree)] = result
    return result


def TensorPower(module: "Module", degree: "Integer | int") -> "_GradedPiece":
    r"""Return \(T(M)[n]=M^{\otimes n}\)."""
    from dzack_research.preamble.categories.algebras.framed_free_algebras import TensorAlgebraOn

    power = _degree_construction(module, TensorAlgebraOn, "tensor", degree)
    power._tensor_power_of = module
    power._tensor_power_degree = int(degree)
    return power


def SymmetricPower(module: "Module", degree: "Integer | int") -> "_GradedPiece":
    r"""Return \(\operatorname{Sym}(M)[n]=\operatorname{Sym}^nM\)."""
    from dzack_research.preamble.categories.algebras.framed_free_algebras import FreeAlgebraOn

    power = _degree_construction(module, FreeAlgebraOn, "symmetric", degree)
    power._symmetric_power_of = module
    power._symmetric_power_degree = int(degree)
    return power


def AlternatingPower(module: "Module", degree: "Integer | int") -> "_GradedPiece":
    r"""Return \(\Lambda(M)[n]=\Lambda^nM\)."""
    from dzack_research.preamble.categories.algebras.framed_free_algebras import AlternatingAlgebraOn

    power = _degree_construction(module, AlternatingAlgebraOn, "alternating", degree)
    power._alternating_power_of = module
    power._alternating_power_degree = int(degree)
    return power


def DividedPower(module: "Module", degree: "Integer | int") -> "_GradedPiece":
    r"""Return \(\Gamma(M)[n]=\Gamma^nM\)."""
    from dzack_research.preamble.categories.algebras.framed_free_algebras import DividedPowerAlgebraOn

    power = _degree_construction(module, DividedPowerAlgebraOn, "divided", degree)
    power._divided_power_of = module
    power._divided_power_degree = int(degree)
    return power


def TensorSquare(module: "Module") -> "_GradedPiece":
    r"""Return \(T(M)[2]=M\otimes_RM\)."""
    square = TensorPower(module, 2)
    square._tensor_square_of = module
    return square


def _is_framed(module: "Module") -> bool:
    r"""Return whether ``module`` carries a framing \(F_R(S)\to M\).

    Being framed is category membership and is asked of the category, not of
    the object's attributes: the framing is the datum the monomial
    constructions above run on.
    """
    # Local: the framed node is loaded before this one, and importing it at
    # module level here would close a cycle through the form modules.
    from dzack_research.preamble.categories.modules.framed.framed_modules import FramedModules

    framed: bool = module in FramedModules(module.base_ring())
    return framed


def _bilinear_form_domain(module: "Module") -> Parent:
    r"""Return the object a bilinear form on \(M\) is a morphism out of.

    \(T^2(M)=M\otimes_RM\) exists for every \(R\)-module, and
    :func:`TensorSquare` is one *presentation* of it -- the monomial one, cut
    out of the tensor algebra on a framing, so it is available exactly when
    \(M\) is framed.  An unframed module has no presentation to build it
    from, so the form is handed over as the bilinear pairing on
    \(U(M)\times U(M)\); by the universal property of the tensor product that
    is the same datum as the morphism out of \(M\otimes_RM\), which is why
    nothing is lost by siting the unframed form on the product of sets.
    """
    # Local: the product node is loaded before this one; see above.
    from dzack_research.preamble.categories.abstract_categories.products import CartesianProductOfSets

    if _is_framed(module):
        return TensorSquare(module)
    pairs: Parent = CartesianProductOfSets((module, module))
    return pairs


def DividedSquare(module: "Module") -> "_GradedPiece":
    r"""Return \(\Gamma(M)[2]=\Gamma^2M\)."""
    square = DividedPower(module, 2)
    square._divided_square_of = module
    return square


def divided_square_element(module: "Module", element: "Element") -> "Element":
    r"""Return \(\gamma_2(x)\in\Gamma^2M\)."""
    from dzack_research.preamble.categories.algebras.framed_free_algebras import DividedPowerAlgebraOn
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector
    from dzack_research.preamble.utilities import zipsum

    assert element.parent() is module, f"{element} is not an element of {module}"
    labels = tuple(module.module_generating_set())
    coordinates = _coordinate_vector(element)
    algebra = DividedPowerAlgebraOn(module.base_ring(), module.module_generating_set())
    degree_one = sum(
        (
            coefficient * algebra.algebra_generator(label)
            for coefficient, label in zip(coordinates, labels)
        ),
        algebra.zero(),
    )
    divided = algebra.divided_square(degree_one)
    square = DividedSquare(module)
    coefficients = divided.coefficients()
    return zipsum(
        (
            coefficients.get(label, module.base_ring().zero())
            for label in square.module_generating_set()
        ),
        square.module_generators(),
        square.zero(),
    )


def _element_of_degree_piece(
    piece: "_GradedPiece", algebra_element: "Element"
) -> "Element":
    r"""Read a homogeneous algebra element in its graded-piece module."""
    from dzack_research.preamble.utilities import zipsum

    coefficients = algebra_element.coefficients()
    ring = piece.base_ring()
    return zipsum(
        (coefficients.get(label, ring.zero()) for label in piece.module_generating_set()),
        piece.module_generators(),
        piece.zero(),
    )


def divided_power_invariant_inclusion(
    module: "Module",
    degree: "Integer | int",
) -> "Morphism":
    r"""Return \(\Gamma^nM\to M^{\otimes n}\) by summing each word orbit."""
    from itertools import permutations
    from dzack_research.preamble.categories.algebras.framed_free_algebras import DividedPowerAlgebraOn
    from dzack_research.preamble.categories.algebras.framed_free_algebras import TensorAlgebraOn
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

    degree = int(degree)
    divided = DividedPowerAlgebraOn(module.base_ring(), module.module_generating_set())
    tensor = TensorAlgebraOn(module.base_ring(), module.module_generating_set())
    tensor_generators = {
        label: tensor.algebra_generator(label)
        for label in module.module_generating_set()
    }

    def invariant(monomial: "Element") -> "Element":
        factors = tuple(divided.monomial_system().factors(monomial))
        word = tuple(
            label
            for label, exponent in factors
            for _ in range(exponent)
        )
        assert len(word) == degree, f"{monomial} does not have degree {degree}"
        image = tensor.zero()
        for permuted_word in set(permutations(word)):
            term = tensor.one()
            for label in permuted_word:
                term *= tensor_generators[label]
            image += term
        return _element_of_degree_piece(TensorPower(module, degree), image)

    source = DividedPower(module, degree)
    target = TensorPower(module, degree)
    inclusion: "Morphism" = module_homset(source, target)(
        {monomial: invariant(monomial) for monomial in source.module_generating_set()}
    )
    return inclusion


def tensor_power_polarization(module: "Module", degree: "Integer | int") -> "Morphism":
    r"""Return \(M^{\otimes n}\to\Gamma^nM\), sending a word to its product."""
    from dzack_research.preamble.categories.algebras.framed_free_algebras import DividedPowerAlgebraOn
    from dzack_research.preamble.categories.algebras.framed_free_algebras import TensorAlgebraOn
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

    degree = int(degree)
    tensor = TensorAlgebraOn(module.base_ring(), module.module_generating_set())
    divided = DividedPowerAlgebraOn(module.base_ring(), module.module_generating_set())
    divided_generators = {
        label: divided.algebra_generator(label)
        for label in module.module_generating_set()
    }

    def polarized(monomial: "Element") -> "Element":
        factors = tuple(tensor.monomial_system().factors(monomial))
        assert len(factors) == degree, f"{monomial} does not have degree {degree}"
        image = divided.one()
        for label, _ in factors:
            image *= divided_generators[label]
        return _element_of_degree_piece(DividedPower(module, degree), image)

    source = TensorPower(module, degree)
    target = DividedPower(module, degree)
    polarization: "Morphism" = module_homset(source, target)(
        {monomial: polarized(monomial) for monomial in source.module_generating_set()}
    )
    return polarization


def tensor_power_permutation(
    module: "Module",
    degree: "Integer | int",
    positions: tuple[int, ...],
) -> "Morphism":
    r"""Return the permutation of tensor factors specified by ``positions``."""
    from dzack_research.preamble.categories.algebras.framed_free_algebras import TensorAlgebraOn
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

    degree = int(degree)
    assert tuple(sorted(positions)) == tuple(range(degree)), (
        f"{positions} is not a permutation of {tuple(range(degree))}"
    )
    algebra = TensorAlgebraOn(module.base_ring(), module.module_generating_set())
    generators = {
        label: algebra.algebra_generator(label)
        for label in module.module_generating_set()
    }
    power = TensorPower(module, degree)

    def permuted(monomial: "Element") -> "Element":
        word = tuple(
            label for label, _ in algebra.monomial_system().factors(monomial)
        )
        image = algebra.one()
        for position in positions:
            image *= generators[word[position]]
        return _element_of_degree_piece(power, image)

    permutation: "Morphism" = module_homset(power, power)(
        {monomial: permuted(monomial) for monomial in power.module_generating_set()}
    )
    return permutation


def divided_square_invariant_inclusion(module: "Module") -> "Morphism":
    r"""Return \(\Gamma^2M\to M^{\otimes2}\)."""
    return divided_power_invariant_inclusion(module, 2)


def tensor_square_polarization(module: "Module") -> "Morphism":
    r"""Return the polarization map \(M^{\otimes2}\to\Gamma^2M\)."""
    return tensor_power_polarization(module, 2)


class QuadraticMapMorphism(SetMorphism):
    r"""A set map recorded with its quadratic source and value module."""

    # Bound by :func:`QuadraticMap`, which is the only thing that builds one:
    # a quadratic map is the pair (function, the two modules it runs between).
    _quadratic_module: "Module"
    _quadratic_value_module: "Module"

    if TYPE_CHECKING:
        # The values lie in a module, which is what lets the polarization
        # below subtract them; a set map in general promises no more than
        # elements.
        def __call__(
            self,
            x: "ElementConstructorInput",
            *args: "ElementConstructorInput",
            **kwds: "ElementConstructorInput",
        ) -> "Element": ...


def QuadraticMap(
    module: "Module",
    value_module: "Module",
    function: "Callable[[Element], Element]",
) -> QuadraticMapMorphism:
    r"""Return a quadratic map \(M\to W\) supplied by its value function."""
    quadratic = QuadraticMapMorphism(
        Hom(
            UnderlyingSet(module),
            UnderlyingSet(value_module),
            Sets(),
        ),
        function,
    )
    quadratic._quadratic_module = module
    quadratic._quadratic_value_module = value_module
    return quadratic


def classifying_morphism(quadratic: QuadraticMapMorphism) -> "Morphism":
    r"""Return the unique linear map \(\Gamma^2M\to W\) classifying \(q\)."""
    from dzack_research.preamble.categories.algebras.framed_free_algebras import DividedPowerAlgebraOn
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

    module = quadratic._quadratic_module
    value_module = quadratic._quadratic_value_module
    square = DividedSquare(module)
    algebra = DividedPowerAlgebraOn(module.base_ring(), module.module_generating_set())
    module_generators = {
        label: module.module_generator(label)
        for label in module.module_generating_set()
    }

    def image_of_monomial(monomial: "Element") -> "Element":
        factors = tuple(algebra.monomial_system().factors(monomial))
        match factors:
            case ((label, 2),):
                return quadratic(module_generators[label])
            case ((left, 1), (right, 1)):
                x = module_generators[left]
                y = module_generators[right]
                return quadratic(x + y) - quadratic(x) - quadratic(y)
            case _:
                assert False, f"{monomial} is not a divided monomial of degree two"

    classifier: "Morphism" = module_homset(square, value_module)(
        {
            monomial: image_of_monomial(monomial)
            for monomial in square.module_generating_set()
        }
    )
    return classifier


def quadratic_map_from_morphism(morphism: "Morphism") -> SetMorphism:
    r"""Evaluate \(f:\Gamma^2M\to W\) on \(\gamma_2(x)\)."""
    square = morphism.domain()
    module = square.__dict__.get("_divided_square_of")
    assert module is not None, "the morphism domain must be a divided square"
    return QuadraticMap(
        module,
        morphism.codomain(),
        lambda element: morphism(divided_square_element(module, element)),
    )


class BilinearFormHomset(Homset):
    r"""The homset of bilinear forms on \(M\) with values in \(W\).

    Two presentations of one homset, because
    \(\operatorname{Hom}(M\otimes_RM,W)\) and the bilinear maps
    \(U(M)\times U(M)\to W\) are the same set: a framed \(M\) has the tensor
    square built, and an unframed one is paired on the product of sets, which
    :func:`_bilinear_form_domain` decides.
    """

    def __init__(self, module: "Module", value_module: "Module") -> None:
        self._module = module
        Homset.__init__(
            self,
            _bilinear_form_domain(module),
            value_module,
            category=Sets(),
        )

    if TYPE_CHECKING:
        # Conversion into this homset builds the form ``_element_constructor_``
        # below builds; Sage routes ``__call__`` there.
        def __call__(
            self,
            x: "ElementConstructorInput" = ...,
            *args: "ElementConstructorInput",
            **kwds: "ElementConstructorInput",
        ) -> "BilinearFormMorphism": ...

    def module(self) -> "Module":
        return self._module

    def _element_constructor_(self, datum: "FormDatum") -> "BilinearFormMorphism":
        return BilinearFormMorphism(self, datum)

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
        self._module = module
        Homset.__init__(
            self,
            DividedSquare(module),
            value_module,
            category=Sets(),
        )

    if TYPE_CHECKING:
        # Conversion into this homset builds the form ``_element_constructor_``
        # below builds.
        def __call__(
            self,
            x: "ElementConstructorInput" = ...,
            *args: "ElementConstructorInput",
            **kwds: "ElementConstructorInput",
        ) -> "QuadraticFormMorphism": ...

    def module(self) -> "Module":
        r"""Return \(M\), which the domain is the divided square of."""
        return self._module

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
    homsets: dict = module.__dict__.setdefault("_form_homsets", {})
    return homsets


def BilinearForms(module: "Module", value_module: "Module") -> BilinearFormHomset:
    r"""Return the canonical homset of bilinear forms on ``module``."""
    key = ("bilinear", value_module)
    cache = _form_homset_cache(module)
    if key not in cache:
        cache[key] = BilinearFormHomset(module, value_module)
    forms: BilinearFormHomset = cache[key]
    return forms


def QuadraticForms(module: "Module", value_module: "Module") -> QuadraticFormHomset:
    r"""Return the canonical homset of quadratic forms on ``module``."""
    key = ("quadratic", value_module)
    cache = _form_homset_cache(module)
    if key not in cache:
        cache[key] = QuadraticFormHomset(module, value_module)
    forms: QuadraticFormHomset = cache[key]
    return forms


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


def _value_submodule(
    form: "BilinearFormMorphism | QuadraticFormMorphism",
) -> Parent:
    r"""Return the submodule of \(W\) generated by ``form``'s values.

    One reading for both kinds of form, because it is one statement: the
    domain is generated by the family the Gram matrix is indexed on, so the
    image of the morphism is generated by the entries of that matrix.  The
    value module presents the submodule and carries the inclusion; nothing
    here decides what a submodule of \(W\) looks like.

    Sage supplies a generic ``image`` to every morphism, which answers with a
    formal image *set* -- a thing with no module structure, no inclusion and
    no cardinality.  Declaring the form's own image is what keeps the scale
    of a discriminant form a submodule of \(\mathbb Q/\mathbb Z\).
    """
    value_module = form.codomain()
    submodule: Parent = value_module.subobject_on(
        [value for row in form.values_matrix() for value in row]
    )
    return submodule


class BilinearFormMorphism(Morphism):
    r"""A bilinear form on \(M\), given by a Gram matrix or by its pairing."""

    if TYPE_CHECKING:
        # The parent is the homset of forms on one module, which is where
        # ``module`` below is read from.
        def parent(self) -> BilinearFormHomset: ...

        # Which of the two the form was given by is what it keeps: the
        # pairing, or the matrix -- never both, and never neither.
        _pairing: "Pairing | None"
        _gram_matrix: "Matrix | None"

    def __init__(self, parent: BilinearFormHomset, datum: "FormDatum") -> None:
        Morphism.__init__(self, parent)
        # A form is its pairing.  A Gram matrix is how a *finitely generated*
        # one can be written down -- it is a presentation, not the form -- so
        # a module without a finite generating set states the pairing itself.
        # Bilinearity is not checkable for such a pairing and is trusted; the
        # matrix route is checked as before.
        if callable(datum) and not isinstance(datum, Matrix):
            self._pairing = datum
            self._gram_matrix = None
            return
        self._pairing = None
        module = parent.module()
        assert _is_framed(module), (
            f"{module} has no framing, so a form on it has no Gram matrix to "
            "be given by; state the pairing instead"
        )
        gram: "Matrix" = datum if isinstance(datum, Matrix) else matrix(datum)
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
        r"""Return the matrix of the form in the module's framing.

        Only a finitely generated module has one: the entries are the
        pairings of a finite generating family, and there is no such family
        to run over otherwise.
        """
        assert self._gram_matrix is not None, (
            f"{self.module()} has no finite generating set, so its form has "
            "no Gram matrix; the form is its pairing"
        )
        return GramMatrix(self._gram_matrix)

    def __call__(
        self,
        x: "ElementConstructorInput",
        *args: "ElementConstructorInput",
        **kwds: "ElementConstructorInput",
    ) -> "Element":
        # Local: the morphism node imports this module, so a module-level
        # import would close that cycle; it is built by call time.
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector

        assert len(args) == 1 and not kwds, (
            "a bilinear form is evaluated on the two elements it pairs"
        )
        left, right = x, args[0]
        # Finitely presented quotient elements are ModuleElements; the
        # parent-identity assert below is the real mathematical precondition.
        assert isinstance(left, Element) and isinstance(right, Element), (
            "a bilinear form pairs elements"
        )
        assert all(
            element.parent() is self.module()
            for element in (left, right)
        ), f"the form pairs elements of {self.module()}"
        if self._pairing is not None:
            return self.codomain()(self._pairing(left, right))
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

        assert self._gram_matrix is not None, (
            f"{self.module()} has no finite generating set, so this form has "
            "no matrix of entries to carry along the ring map"
        )
        value_ring = module.base_ring()
        return BilinearForms(module, value_ring)(
            self._gram_matrix.change_ring(engine_ring(value_ring))
        )

    def pullback(self, morphism: "ModuleMorphism") -> "BilinearFormMorphism":
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

    def descends_along(self, morphism: "ModuleMorphism") -> bool:
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
        assert self._gram_matrix is not None, (
            f"{self.module()} has no finite generating set, so this form has "
            "no finite family of values to tabulate"
        )
        return tuple(
            tuple(self.codomain()(entry) for entry in row)
            for row in self._gram_matrix.rows()
        )

    def image(self) -> Parent:
        r"""Return the submodule of \(W\) the form's values generate.

        \(M\) is generated by the \(e_i\), so \(M\otimes_RM\) is generated by
        the \(e_i\otimes e_j\), and the image of a linear map is generated by
        its values on a generating family.  Those values are the entries of
        the Gram matrix, which is why the matrix is enough and no basis of
        \(W\) is consulted.
        """
        return _value_submodule(self)

    def __eq__(self, other: "MembershipInput") -> bool:
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
        if self._gram_matrix is None:
            return "the pairing it is given by"
        return repr(self._gram_matrix)


class QuadraticFormMorphism(Morphism):
    if TYPE_CHECKING:
        # The parent is the homset of quadratic forms on one module.
        def parent(self) -> QuadraticFormHomset: ...

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
        return self.parent().module()

    def value_module(self) -> "Module":
        return self.codomain()

    def __call__(
        self,
        x: "ElementConstructorInput",
        *args: "ElementConstructorInput",
        **kwds: "ElementConstructorInput",
    ) -> "Element":
        # Local: the morphism node imports this module, so a module-level
        # import would close that cycle; it is built by call time.
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector

        assert not args and not kwds, (
            "a quadratic form is evaluated on one element"
        )
        element = x
        # Finitely presented quotient elements are ModuleElements; the
        # parent-identity assert below carries the mathematics.
        assert isinstance(element, Element), (
            "a quadratic form is evaluated on an element"
        )
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

    def pullback(self, morphism: "ModuleMorphism") -> "QuadraticFormMorphism":
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

    def descends_along(self, morphism: "ModuleMorphism") -> bool:
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

    def image(self) -> Parent:
        r"""Return the submodule of \(W\) the form's values generate.

        \(\Gamma^2M\) is generated by the \(\gamma_2(e_i)\) and the products
        \(e_ie_j\) for \(i<j\); this morphism takes the value \(q(e_i)\) on
        the first and \(2b(e_i,e_j)\) on the second, which are exactly the
        entries of :meth:`gram_matrix`.  So the same reading as the bilinear
        case applies to the matrix that records a quadratic form.
        """
        return _value_submodule(self)

    def __eq__(self, other: "MembershipInput") -> bool:
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


def BilinearForm(
    module: "Module", value_module: "Module", gram_matrix: "GramMatrix"
) -> Parent:
    r"""Construct the formed module classified by a bilinear form."""
    # Local: form_modules imports this module, so a module-level import here
    # would close that cycle; it is built by the time this function runs.
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule

    formed: Parent = FormModule(
        BilinearForms(module, value_module)(gram_matrix)
    )
    return formed


def QuadraticForm(
    module: "Module", value_module: "Module", gram_matrix: "GramMatrix"
) -> Parent:
    r"""Construct the formed module classified by a quadratic form."""
    # Local: form_modules imports this module, so a module-level import here
    # would close that cycle; it is built by the time this function runs.
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule

    formed: Parent = FormModule(
        QuadraticForms(module, value_module)(gram_matrix)
    )
    return formed
