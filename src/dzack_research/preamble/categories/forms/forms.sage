r"""Bilinear and quadratic forms as native Sage morphisms."""


from collections.abc import Callable
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.structure.parent import ElementConstructorInput, MembershipInput
from dzack_research.preamble.lexicon import Element
if TYPE_CHECKING:
    from sage.categories.modules import Module

from sage.misc.cachefunc import cached_function
from sage.rings.integer import Integer
from sage.categories.homset import Homset
from sage.categories.homset import Hom
from sage.categories.morphism import Morphism, SetMorphism
from sage.structure.element import ModuleElement
from dzack_research.preamble.categories.sets.underlying_sets import UnderlyingSet
from sage.matrix.constructor import matrix
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

# The graded module functors a form is a morphism out of live at the tensor
# node: a form has no say in what a tensor or divided square is, it only
# consumes them as domains.  ``tensors`` loads before this module.
from dzack_research.preamble.categories.modules.tensors import (
    DividedSquare,
    TensorSquare,
    divided_square_element,
)


def _framing_rank(module_generating_set: "OrderedSet") -> Integer:
    size = module_generating_set.cardinality()
    if isinstance(size, Cardinal):
        assert size.is_finite(), "a Gram matrix requires a finite framing set"
        rank: Integer = size.finite_value()
        return rank
    assert size in SageZZ, "a Gram matrix requires a finite framing set"
    return SageZZ(size)


def _is_framed(module: "Module") -> bool:
    r"""Return whether ``module`` carries a framing \(F_R(S)\to M\).

    Being framed is category membership and is asked of the category, not of
    the object's attributes: the framing is the datum the graded module
    functors at the tensor node run on.
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
    # Local: the tensor node imports this module, so a module-level import
    # here would close that cycle; it is built by the time a form is evaluated.
    from dzack_research.preamble.categories.modules.tensors import divided_square_of

    module = divided_square_of(morphism.domain())
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

    def __contains__(self, form: "Morphism") -> bool:
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

    def __contains__(self, form: "Morphism") -> bool:
        return (
            isinstance(form, QuadraticFormMorphism)
            and form.parent() is self
        )

    def _repr_(self) -> str:
        return (
            f"Quadratic forms on {self.module()} with values in "
            f"{self.codomain()}"
        )


@cached_function
def BilinearForms(module: "Module", value_module: "Module") -> BilinearFormHomset:
    r"""Return the canonical homset of bilinear forms on ``module``."""
    return BilinearFormHomset(module, value_module)


@cached_function
def QuadraticForms(module: "Module", value_module: "Module") -> QuadraticFormHomset:
    r"""Return the canonical homset of quadratic forms on ``module``."""
    return QuadraticFormHomset(module, value_module)


def _underlying_element(element: "Element") -> "Element":
    # Local: form_modules imports this module, so a module-level import here
    # would close that cycle; it is built by the time this function runs.
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModules

    match element:
        case Element() if element.parent() in FormModules(element.parent().base_ring()):
            return element.underlying_element()
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
        assert isinstance(left, Element) and isinstance(right, Element), (
            "a bilinear form pairs elements"
        )
        # Membership, not parent identity: the domain of the form is
        # ``self.module()``, and being an element of it is what the question
        # asks.  The two agree for a module whose members answer to it, and
        # part company for a facade, whose members answer to its host --
        # so identity would refuse elements that are in the domain.  An
        # element of a module *enriched* over this one (a formed module's
        # element over its underlying module) is not in this domain and
        # reaches it through the forgetful map, which is what
        # ``FormedModules.ElementMethods.b`` applies before calling here.
        assert all(
            element in self.module()
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
        r"""Return $\operatorname{polar}(\operatorname{diag}(b))=2b$.

        The polar form of the norm $q(x)=b(x,x)$: the bilinear expansion
        $q(x+y)-q(x)-q(y)=2b(x,y)$ (FOUNDATIONS Lemma 17.2, following the
        polarization convention of Nik80 §2°), valued where $b$ is.  Not
        $b$ itself: as previously written this method was the identity
        under a false name (TODO 2026-08-14), and the finite quadratic
        case (FOUNDATIONS Def 25.4) reads the same factor of two through
        the canonical $\times 2$ isomorphism
        $\mathbb Q/\mathbb Z\to\mathbb Q/2\mathbb Z$.
        """
        assert self._gram_matrix is not None, (
            f"{self.module()} has no finite generating set, so its polar "
            "form has no Gram matrix; polarize the pairing instead"
        )
        return BilinearForms(self.module(), self.codomain())(
            2 * self._gram_matrix
        )

    def on_module(self, module: "Module") -> "BilinearFormMorphism":
        assert self._gram_matrix is not None, (
            f"{self.module()} has no finite generating set, so its form has "
            "no Gram matrix; the form is its pairing"
        )
        return BilinearForms(module, self.codomain())(self._gram_matrix)

    def reduced(self, value_module: "Module") -> "BilinearFormMorphism":
        assert self._gram_matrix is not None, (
            f"{self.module()} has no finite generating set, so its form has "
            "no Gram matrix; the form is its pairing"
        )
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
        matrix_of_map = morphism.matrix()._sage_matrix()
        domain = morphism.domain()
        return BilinearForms(domain, self.codomain())(
            GramMatrix(
                matrix_of_map
                * self._gram_matrix
                * matrix_of_map.transpose()
            )
        )

    def descends_along(
        self, morphism: "ModuleMorphism", value_projection: "Morphism"
    ) -> bool:
        r"""Whether this form descends to \(\operatorname{coker}(f)\).

        For \(f:N\hookrightarrow M\) with \(M\) this form's module, the
        induced form on \(M/N\) valued in \(W'\) exists exactly when every
        pairing of \(f(N)\) against \(M\) lies in
        \(\ker(\pi:W\twoheadrightarrow W')\) -- the target quotient's defining
        submodule, read off ``value_projection`` as the values it kills.
        """
        domain, codomain = morphism.domain(), morphism.codomain()
        # The compatibility the pairing loop below silently assumes: the
        # inclusion lands in this form's module, which is where both the
        # images of N and the generating family of M are paired.
        assert codomain is self.module(), (
            f"the inclusion lands in {codomain}, but this form pairs "
            f"elements of {self.module()}"
        )
        assert value_projection.domain() is self.codomain(), (
            f"the value projection starts at {value_projection.domain()}, "
            f"but this form takes values in {self.codomain()}"
        )
        target_zero = value_projection.codomain().zero()
        return all(
            value_projection(
                self(
                    _underlying_element(morphism(domain.module_generator(label))),
                    _underlying_element(codomain.module_generator(target_label)),
                )
            )
            == target_zero
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
        assert isinstance(element, Element), (
            "a quadratic form is evaluated on an element"
        )
        # Membership, for the reason given on the bilinear ``__call__``.
        assert element in self.module(), (
            f"{element} is not an element of {self.module()}"
        )
        coordinates = _coordinate_vector(element)
        return self.codomain()(
            coordinates * self._lift_matrix * coordinates
        )

    def norm(self, element: "Element") -> "Element":
        return self(element)

    def lift_form(self) -> BilinearFormMorphism:
        r"""Return the symmetric bilinear lift, valued where its entries live."""
        return BilinearForms(self.module(), self._lift_matrix.base_ring())(
            self._lift_matrix
        )

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
        matrix_of_map = morphism.matrix()._sage_matrix()
        domain = morphism.domain()
        return QuadraticForms(domain, self.codomain())(
            matrix_of_map
            * self._lift_matrix
            * matrix_of_map.transpose()
        )

    def descends_along(
        self, morphism: "ModuleMorphism", value_projection: "Morphism"
    ) -> bool:
        r"""Whether this quadratic form descends to \(\operatorname{coker}(f)\).

        Nikulin's two conditions: the polar pairings of \(f(N)\) against
        \(M\) descend along the polar quotient of ``value_projection``'s
        target, and the values \(q(f(N))\) lie in
        \(\ker(\pi:W\twoheadrightarrow W')\), read off ``value_projection``
        as the values it kills.
        """
        from sage.groups.additive_abelian.qmodnz import QmodnZ

        quadratic_target = value_projection.codomain()
        assert isinstance(quadratic_target, QmodnZ), (
            "halving the value modulus is defined here only for Q/nZ"
        )
        polar_target = QmodnZ(quadratic_target.n / 2)
        polar_projection = polar_target.coerce_map_from(
            value_projection.domain()
        )
        if not self.lift_form().descends_along(morphism, polar_projection):
            return False
        assert value_projection.domain() is self.codomain(), (
            f"the value projection starts at {value_projection.domain()}, "
            f"but this form takes values in {self.codomain()}"
        )
        target_zero = quadratic_target.zero()
        return all(
            value_projection(
                self(_underlying_element(morphism(morphism.domain().module_generator(label))))
            )
            == target_zero
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
