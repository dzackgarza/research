r"""The forgetful functor \(U\colon R\text{-}\mathbf{Alg}\to R\text{-}\mathbf{Mod}\).

An algebra carries an underlying \(R\)-module, but the algebra category is not
identified with a subcategory of modules.  An exact equipped algebra returns
the supplied module literally; a legacy parent with independent module
placement returns that module object; otherwise this owner supplies one
realization module on the same algebra elements and scalar action.

An algebra that carries a module framing is that framed module.  A free
construction carries none: \(T_R(M)\) and \(\operatorname{Sym}_R(M)\) have one
homogeneous module generator for each word or monomial, in every degree, so
their underlying module is the finite-support direct sum of their own graded
pieces.  A polynomial ring named by its variables is the second of these, on
the free module on those names, and is summed the same way.
"""

from sage.misc.cachefunc import cached_function
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import ModuleElement
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    AlgebrasWithChosenFinitePresentation,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    SymmetricAlgebras,
    TensorAlgebras,
)
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.modules.graded_direct_sums import (
    GradedDirectSumModule,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FramedModules,
    Modules,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _engine_element,
    _engine_ring,
    _owned_ring,
)
from dzack_research.preamble.owned_category import object_of


from dzack_research.preamble.categories.modules.tensor_products import (
    _flatten_tensor_label,
    _nested_tensor_label,
)


class _UnderlyingAlgebraModules(OwnedCategoryOverBaseRing):
    r"""Realization modules for legacy algebras with no independent module placement."""

    def super_categories(self):
        return [Modules(self.base_ring())]

    class ParentMethods:
        def __init__(self, algebra, **rest) -> None:
            self._realized_algebra = algebra
            category = rest.get("category")
            if category is None:
                raise TypeError("an underlying algebra module requires its module category")
            super().__init__(base_ring=category.base_ring(), **rest)

        def realized_object(self):
            return self._realized_algebra

        def realize(self, element):
            element = self(element)
            return element.underlying_element()

        def from_realization(self, element):
            return self(element)

        def _element_constructor_(self, element):
            if getattr(element, "parent", lambda: None)() is self:
                return element
            underlying = getattr(element, "underlying_element", None)
            if callable(underlying):
                element = underlying()
            return self.element_class(self, self.realized_object()(element))

        def __contains__(self, element) -> bool:
            return getattr(element, "parent", lambda: None)() is self

        def zero(self):
            return self(self.realized_object().zero())

        def _owned_scalar_multiple(self, scalar, element):
            algebra = self.realized_object()
            ordinary = Algebras(self.base_ring()).Associative().Unital()
            if algebra not in ordinary:
                raise NotImplementedError(
                    "a legacy nonunital algebra needs an explicit represented scalar-action module"
                )
            structure = algebra.algebra_structure_morphism()
            scalar_image = algebra(structure(self.base_ring()(scalar)))
            return self(
                scalar_image * algebra(self.realize(element))
            )

        def _repr_(self):
            return f"Underlying {self.base_ring()}-module of {self.realized_object()}"

    class ElementMethods(ModuleElement):
        r"""One legacy algebra element read in its forgetful module."""

        def __init__(self, parent, underlying_element) -> None:
            ModuleElement.__init__(self, parent)
            self._underlying_element = underlying_element

        def underlying_element(self):
            return self._underlying_element

        def _add_(self, other):
            parent = self.parent()
            return parent(
                self.underlying_element() + parent.realize(other)
            )

        def _sub_(self, other):
            parent = self.parent()
            return parent(
                self.underlying_element() - parent.realize(other)
            )

        def _neg_(self):
            return self.parent()(-self.underlying_element())

        def _lmul_(self, scalar):
            return self.parent().scalar_multiple(scalar, self)

        def _rmul_(self, scalar):
            return self.parent().scalar_multiple(scalar, self)

        def _acted_upon_(self, actor, self_on_left):
            _ = self_on_left
            try:
                scalar = self.parent().base_ring()(actor)
            except (TypeError, ValueError):
                return None
            return self.parent().scalar_multiple(scalar, self)

        def _richcmp_(self, other, op):
            if getattr(other, "parent", lambda: None)() is not self.parent():
                return NotImplemented
            if op == op_EQ:
                return self.underlying_element() == other.underlying_element()
            if op == op_NE:
                return self.underlying_element() != other.underlying_element()
            return NotImplemented

        def _repr_(self):
            return repr(self.underlying_element())


@cached_function(key=lambda algebra, ring: (id(algebra), id(ring)))
def _legacy_algebra_underlying_module(algebra, ring):
    return object_of(
        _UnderlyingAlgebraModules(ring),
        algebra=algebra,
    )


def _monomial_exponents(exponents):
    r"""Return one monomial's exponent as multiplicities in variable order.

    Private backend serialization.  Sage writes the exponent of a monomial in
    a single variable as a bare integer and of a monomial in several variables
    as a tuple of them.  Both record the same multiplicity function on the
    variables, and the code that reads it wants the second spelling.
    """
    return (exponents,) if exponents in SageZZ else exponents


def _free_algebra_underlying_module(algebra, ring):
    source = algebra.free_source_module()
    tensor_flavored = algebra in TensorAlgebras(ring)
    realization_maps = {}

    def piece(degree):
        return algebra.graded_piece(degree)

    def generator_word(degree, label):
        if degree == 0:
            return algebra.one()
        if degree == 1:
            return algebra.algebra_generator(label)
        if tensor_flavored:
            factors = (
                algebra.algebra_generator(source_label)
                for source_label in _flatten_tensor_label(label, degree)
            )
        else:
            factors = (
                algebra.algebra_generator(source_label)
                for source_label in label
            )
        result = algebra.one()
        for factor in factors:
            result *= factor
        return result

    def realization_map(degree):
        degree = int(degree)
        cached = realization_maps.get(degree)
        if cached is not None:
            return cached
        homogeneous_piece = piece(degree)
        realized = module_homset(homogeneous_piece, algebra)(
            lambda label: generator_word(degree, label)
        )
        realization_maps[degree] = realized
        return realized

    direct_sum = None

    def realize_generator(degree, label):
        homogeneous_piece = piece(degree)
        return realization_map(degree)(homogeneous_piece.module_generator(label))

    def from_realization(element):
        coefficients_by_degree = {}
        source_labels = source.module_generating_set()


        if algebra in AlgebrasWithChosenFinitePresentation(algebra.base_ring()):
            presentation = algebra.presentation_ring()
            presented = algebra.lift_to_presentation(element)
        else:
            presentation = algebra
            presented = algebra(element)
        backend = _engine_element(presentation, presented)
        engine = _engine_ring(presentation)

        if tensor_flavored:
            def source_label(generator):
                position = next(
                    index
                    for index, candidate in enumerate(engine.monoid().gens())
                    if candidate == generator
                )
                return source_labels[position]

            def tensor_term(item):
                monomial, coefficient = item
                degree = sum(int(exponent) for _generator, exponent in monomial)
                word = (
                    source_label(generator)
                    for generator, exponent in monomial
                    for _ in range(int(exponent))
                )
                return (
                    degree,
                    _nested_tensor_label(source, word),
                    algebra.base_ring()._from_engine_element(
                        _engine_ring(algebra.base_ring())(coefficient)
                    ),
                )

            terms = (
                tensor_term(item)
                for item in engine(backend).monomial_coefficients().items()
            )
        else:
            def symmetric_term(item):
                exponents, coefficient = item
                multiplicities = {
                    source_labels[position]: int(exponent)
                    for position, exponent in enumerate(
                        _monomial_exponents(exponents)
                    )
                    if exponent
                }
                degree = sum(multiplicities.values())
                if degree == 0:
                    label = 0
                elif degree == 1:
                    label = next(iter(multiplicities))
                else:
                    label = piece(degree).module_generating_set().from_multiplicities(
                        multiplicities
                    )
                return (
                    degree,
                    label,
                    algebra.base_ring()._from_engine_element(
                        _engine_ring(algebra.base_ring())(coefficient)
                    ),
                )

            terms = (symmetric_term(item) for item in engine(backend).dict().items())

        for degree, label, coefficient in terms:
            degree_coefficients = coefficients_by_degree.setdefault(degree, {})
            degree_coefficients[label] = degree_coefficients.get(
                label, algebra.base_ring().zero()
            ) + coefficient
        return direct_sum.from_components(
            {
                degree: piece(degree).linear_combination(coefficients)
                for degree, coefficients in coefficients_by_degree.items()
            }
        )

    direct_sum = GradedDirectSumModule(
        algebra.base_ring(),
        piece,
        name=f"Underlying graded module of {algebra}",
        realize_generator=realize_generator,
        realized_object=algebra,
        from_realization=from_realization,
    )
    return direct_sum


class UnderlyingAlgebraModuleMorphism(ModuleMorphism):
    r"""An algebra morphism read as its underlying linear map.

    \(U\) changes neither an element nor its image; it changes which
    operations the map answers to.  So this is constructed as an ordinary
    module morphism, on the framing of its domain when there is one and
    elementwise otherwise, and the kernel, cokernel, matrix and composites of
    the module level are then computed from the algebra morphism rather than
    from state a bare ``Morphism`` never established.

    Linearity is not re-established here.  An \(R\)-algebra morphism is
    \(R\)-linear by definition of the structure map, so the module level is
    told the theorem rather than asked to test it.
    """

    def __init__(self, parent, algebra_morphism) -> None:
        self._algebra_morphism = algebra_morphism
        domain = parent.domain()
        if domain.is_framed():
            super().__init__(
                parent,
                lambda label: self._underlying_image(domain.module_generator(label)),
                verify_linearity=False,
            )
            return
        super().__init__(
            parent,
            self._underlying_image,
            elementwise=True,
            verify_linearity=False,
        )

    def _underlying_image(self, element):
        r"""Return the image of one element under the algebra morphism.

        The underlying module of an algebra is either the algebra itself or a
        graded module that realizes it.  Which one is settled by comparing the
        endpoints of this morphism with the endpoints of the algebra morphism
        it comes from, so nothing is asked what class it belongs to.
        """
        source = self.domain()
        target = self.codomain()
        algebra_domain = self._algebra_morphism.domain()
        algebra_codomain = self._algebra_morphism.codomain()
        argument = element if source is algebra_domain else source.realize(element)
        image = self._algebra_morphism(argument)
        if target is algebra_codomain:
            return image
        return target.from_realization(image)

    def algebra_morphism(self):
        return self._algebra_morphism


class AlgebraUnderlyingModuleFunctor(Functor):
    r"""\(U\colon\mathbf{Alg}_R\to\mathbf{Mod}_R\)."""

    def __init__(self, base_ring, algebra_category=None) -> None:
        self._base_ring = _owned_ring(base_ring)
        domain = (
            Algebras(self._base_ring) if algebra_category is None else algebra_category
        )
        assert domain.is_subcategory(Algebras(self._base_ring)), (
            f"the underlying-module functor starts on a category of {self._base_ring}-algebras"
        )
        super().__init__(domain, Modules(self._base_ring))

    def base_ring(self):
        return self._base_ring

    def _apply_object(self, algebra):
        r"""Return the underlying \(R\)-module of one algebra.

        An equipped algebra retains its exact carrier, and that carrier is the
        answer.  Legacy engine-backed algebra parents can already carry their
        represented module structure directly; returning those parents here is
        the action of this functor, not an assertion that the algebra category
        is a subcategory of modules.

        A free construction \(T_R(M)\) or \(\operatorname{Sym}_R(M)\) has no
        finite framing: it has one homogeneous module generator for each word
        or monomial, in every degree.  Its underlying module is therefore
        stated as the finite-support sum of its own graded pieces -- the
        module it realizes, not a second model of it.  This covers a
        polynomial ring named by its variables too, since \(R[x_1,\dots,x_n]\)
        is \(\operatorname{Sym}_R\) of the free module on those names, so the
        graded pieces are there to be summed whichever route built it.

        Every remaining legacy algebra is represented by an unframed module
        realization on the same algebra elements and the algebra's selected
        scalar action.  This is a genuine object of ``Modules(R)``; the
        algebra parent is not silently treated as a module merely because it
        once lay under a category-inclusion edge.
        """
        ring = self.base_ring()
        target_object = getattr(algebra, "target_object", None)
        arrow = getattr(algebra, "arrow", None)
        if callable(target_object) and callable(arrow):
            carrier = target_object()
            structure = arrow()
            if carrier in Modules(ring) and structure.codomain() is carrier:
                return carrier
        if algebra in Modules(ring):
            return algebra
        if algebra in FramedModules(ring):
            return algebra
        match algebra:
            case _ if algebra in TensorAlgebras(ring):
                return _free_algebra_underlying_module(algebra, ring)
            case _ if algebra in SymmetricAlgebras(ring):
                return _free_algebra_underlying_module(algebra, ring)
            case _:
                return _legacy_algebra_underlying_module(algebra, ring)

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        right = getattr(morphism, "right", None)
        if callable(right):
            underlying = right()
            if underlying.domain() is source and underlying.codomain() is target:
                return underlying
        return UnderlyingAlgebraModuleMorphism(
            module_homset(source, target),
            morphism,
        )

    def _repr_(self):
        return f"Underlying-module functor on {self.base_ring()}-algebras"


@cached_function
def algebra_underlying_module_functor(
    base_ring,
    algebra_category=None,
) -> AlgebraUnderlyingModuleFunctor:
    return AlgebraUnderlyingModuleFunctor(base_ring, algebra_category)


__all__ = [
    "AlgebraUnderlyingModuleFunctor",
    "UnderlyingAlgebraModuleMorphism",
    "algebra_underlying_module_functor",
]
