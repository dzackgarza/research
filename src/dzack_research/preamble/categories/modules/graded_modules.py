"""Modules graded by a monoid."""

from sage.misc.cachefunc import cached_function
from sage.rings.infinity import Infinity as _Infinity
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.group.magmas import (
    AdditiveMonoids,
    Monoids,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    _initialize_module_mor_parent,
    _ModuleMorCommonMethods,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FramedModules,
    LinearEndCategoryConstruction,
    Modules,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    Zmod,
    _own_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets


def _normalize_grading_monoid(monoid: Parent | None) -> Parent:
    r"""Return the owned grading monoid, defaulting to \(\mathbb{Z},+\)."""
    return _own_ring(SageZZ) if monoid is None else monoid


def _require_grading_monoid(monoid: Parent | None) -> Parent:
    monoid = _normalize_grading_monoid(monoid)
    if monoid not in Monoids() and monoid not in AdditiveMonoids():
        raise TypeError(f"{monoid} is not a monoid in the owned category graph")
    return monoid


def _grading_identity(monoid: Parent | None):
    r"""Return the identity degree of the selected grading monoid."""
    monoid = _require_grading_monoid(monoid)
    if monoid in AdditiveMonoids():
        return monoid.zero()
    return monoid.one()


class _ParityKey:
    r"""A chosen parity morphism as a category parameter.

    A chosen morphism has identity semantics as a parameter of a categorical
    construction, as a functor does; the key is interned on that identity.
    """

    def __init__(self, morphism) -> None:
        self._morphism = morphism

    def morphism(self):
        return self._morphism


@cached_function(key=lambda parity: id(parity))
def _parity_key(parity):
    return _ParityKey(parity)


@cached_function
def _integer_parity():
    r"""The reduction ``ZZ -> ZZ/2``, the canonical parity of the integer grading."""
    integers = _own_ring(SageZZ)
    parity_target = Zmod(2)
    return integers.Mor(parity_target)(parity_target)


@cached_function
def _two_parity():
    r"""The identity of ``ZZ/2``, the canonical parity of a grading by ``ZZ/2``."""
    two = Zmod(2)
    return two.Mor(two)(lambda degree: degree)


def _grading_parity(grading_monoid, parity=None):
    r"""Return the parity homomorphism ``M -> ZZ/2`` of the grading, or ``None``.

    The parity is part of the grading datum: a monoid admits many
    homomorphisms to ``ZZ/2``, so it is chosen and stated with the monoid.
    ``ZZ`` is graded with reduction mod 2 and ``ZZ/2`` with the identity unless
    another is stated; every other monoid records the parity it is given and
    none otherwise, and a construction that reads the parity (the Koszul sign
    of a supercommutative product) refuses a grading that recorded none.
    """
    parity_target = Zmod(2)
    if parity is None:
        if grading_monoid is _own_ring(SageZZ):
            return _integer_parity()
        if grading_monoid is parity_target:
            return _two_parity()
        return None
    assert parity.domain() is grading_monoid, (
        "the parity homomorphism is defined on the grading monoid"
    )
    assert parity.codomain() is parity_target, (
        f"a parity is a monoid morphism into {parity_target}"
    )
    return parity


def _concentrated_graded_module(base_ring, grading_monoid=None):
    r"""Return a rank-one graded module concentrated in the identity degree."""
    monoid = _require_grading_monoid(grading_monoid)
    return base_ring._fresh_free_module_on(
        Sets.Δ[0],
        _extra_categories=(GradedModules(base_ring, monoid),),
        _extra_construction_data={
            "concentrated_degree": _grading_identity(monoid),
        },
    )


def _represented_homogeneous_degree_or_none(element):
    r"""Return a represented homogeneous degree, or ``None`` when no degree view is selected."""
    parent = element.parent()
    selected = parent.__dict__.get("_preamble_concentrated_degree")
    if selected is not None:
        if element == parent.zero():
            raise ValueError("zero has no selected homogeneous degree here")
        return selected
    homogeneous_function = getattr(element, "is_homogeneous", None)
    degree_function = getattr(element, "degree", None)
    match callable(homogeneous_function) and callable(degree_function):
        case False:
            return None
        case True:
            pass
    if not homogeneous_function():
        raise ValueError("the graded-module element is not homogeneous")
    return degree_function()


def _selected_homogeneous_degree(element):
    r"""Return one represented homogeneous degree without imposing one element API."""
    degree = _represented_homogeneous_degree_or_none(element)
    assert degree is not None, (
        "this graded-module element has no represented homogeneous degree"
    )
    return degree


class GradedModuleMorphism(ModuleMorphism):
    r"""A degree-zero morphism of graded modules."""

    def __init__(self, parent, images, *, elementwise=False) -> None:
        self._underlying_linearity_premise = (
            images if isinstance(images, ModuleMorphism) else None
        )
        if self._underlying_linearity_premise is None:
            ModuleMorphism.__init__(self, parent, images, elementwise=elementwise)
        else:
            ModuleMorphism.__init__(
                self,
                parent,
                lambda element: images(element),
                elementwise=True,
            )
        if self.linearity_decision() is not True:
            raise ValueError("a graded-module morphism requires an established underlying linear map")
        self._check_selected_degrees()

    def _elementwise_linearity_derivation(self):
        premise = self._underlying_linearity_premise
        if premise is None:
            return super()._elementwise_linearity_derivation()
        return premise.linearity_decision()

    def _check_selected_degrees(self) -> None:

        domain = self.domain()
        if domain not in FramedModules(domain.base_ring()):
            return
        labels = domain.module_generating_set()
        if not labels.cardinality().is_finite():
            return
        for label in labels:
            source = domain.module_generator(label)
            source_degree = _represented_homogeneous_degree_or_none(source)
            if source_degree is None:
                continue
            image = self(source)
            if image == self.codomain().zero():
                continue
            target_degree = _represented_homogeneous_degree_or_none(image)
            if target_degree is None:
                raise ValueError("a graded-module map has an image with no represented homogeneous degree")
            if target_degree != source_degree:
                raise ValueError("a graded-module morphism must preserve degree")

    def __mul__(self, other):
        if not isinstance(other, GradedModuleMorphism):
            return super().__mul__(other)
        if other.codomain() is not self.domain():
            return NotImplemented
        domain = other.domain()
        indices = domain.grading_index_set()
        return _CompositeGradedModuleMorphism(
            GradedModules(domain.base_ring(), indices).Mor(domain, self.codomain()),
            self,
            other,
        )


class _CompositeGradedModuleMorphism(GradedModuleMorphism):
    r"""Composition of degree-zero graded maps, linear by composition."""

    def __init__(self, parent, left, right) -> None:
        self._left_factor = left
        self._right_factor = right
        super().__init__(parent, lambda element: left(right(element)), elementwise=True)

    def _elementwise_linearity_derivation(self):
        return True


class GradedModuleMor(_ModuleMorCommonMethods, CategoricalMor):
    Element = GradedModuleMorphism

    def __init__(self, mor_family, domain, codomain) -> None:
        indices = domain.grading_index_set()
        assert indices is codomain.grading_index_set(), "graded-module arrows use the same indexing set"
        assert indices is mor_family.base_category().grading_index_set(), "the graded-module arrow category uses those indices"
        _initialize_module_mor_parent(self, mor_family, domain, codomain)

    def _element_constructor_(self, images):
        if isinstance(images, ModuleMorphism):
            if images.domain() is not self.domain() or images.codomain() is not self.codomain():
                raise ValueError("the module morphism has the wrong graded-module endpoints")
            if isinstance(images, GradedModuleMorphism) and images.parent() is self:
                return images
            return self.element_class(self, images)
        return super()._element_constructor_(images)



class GradedModuleMorCategoryConstruction(MorCategoryConstruction):
    def fixed_category_class(self):
        return GradedModuleMor


class GradedModules(OwnedCategoryOverBaseRing):
    r"""Modules with a direct-sum decomposition indexed by a set.

    Mathlib CategoryTheory/GradedObject defines I-graded objects for any type I,
    with componentwise arrows and a total coproduct.  Multiplying degrees
    requires a monoid; shifts and parity require their additional data.
    The default indexing set is the additive group of integers.
    """

    def an_object(self):
        indices = self.grading_index_set()
        match indices:
            case _ if indices in Monoids() or indices in AdditiveMonoids():
                return _concentrated_graded_module(self.base_ring(), indices)
            case _:
                from dzack_research.preamble.categories.sets.indexed_families import indexed_family

                zero = self.base_ring().free_module(0)
                return self(indexed_family(indices, lambda _: zero))

    @staticmethod
    def __classcall__(cls, base_ring, grading_monoid=None, parity=None):
        r"""``GradedModules(R, M, parity)``: the grading is ``M`` with its parity ``M -> ZZ/2``.

        The parity is canonical for ``ZZ`` (reduction) and ``ZZ/2`` (the
        identity) and stated explicitly for any other monoid; see
        :func:`_grading_parity`.
        """
        monoid = _normalize_grading_monoid(grading_monoid)
        assert monoid in Sets(), "a grading is indexed by an owned set"
        selected_parity = _grading_parity(monoid, parity)
        return OwnedCategoryOverBaseRing.__classcall__(
            cls,
            base_ring,
            monoid,
            None if selected_parity is None else _parity_key(selected_parity),
        )

    def __init__(self, base_ring, grading_monoid: Parent, parity_key) -> None:
        self._grading_index_set = grading_monoid
        self._parity_key = parity_key
        super().__init__(base_ring)

    def _call_(self, pieces, *, placements=(), **construction_data):
        r"""The graded direct sum of the supplied family of R-modules."""
        from dzack_research.preamble.categories.modules.graded_direct_sums import _direct_sum_of_modules

        return _direct_sum_of_modules(
            self.base_ring(), self.grading_index_set(), pieces,
            extra_categories=placements, construction_data=construction_data,
        )

    def grading_index_set(self) -> Parent:
        return self._grading_index_set

    def grading_monoid(self) -> Parent:
        return _require_grading_monoid(self.grading_index_set())

    def parity_homomorphism(self):
        r"""Return the stated parity ``M -> ZZ/2`` of the grading."""
        assert self._parity_key is not None, (
            f"{self.grading_index_set()} is an indexing set with no canonical parity "
            f"homomorphism to {Zmod(2)}; state the parity with the grading"
        )
        return self._parity_key.morphism()

    def _repr_object_names(self) -> str:
        monoid = self.grading_index_set()
        if monoid is _own_ring(SageZZ):
            names = "graded modules"
        else:
            names = f"modules graded by {monoid}"
        return f"{names} over {self.base()}"

    def _make_named_class_key(self, name):
        return (super()._make_named_class_key(name), self.grading_index_set(), self._parity_key)

    def super_categories(self):

        return [Modules(self.base_ring())]

    _MorCategory = GradedModuleMorCategoryConstruction
    _EndCategory = LinearEndCategoryConstruction

    class ParentMethods:
        def is_graded(self) -> bool:
            return True

        def grading_index_set(self):
            for category in self.category().all_super_categories(proper=False):
                try:
                    return category.grading_index_set()
                except AttributeError:
                    continue
            raise TypeError(f"{self} has no selected grading index set")

        def grading_monoid(self):
            return _require_grading_monoid(self.grading_index_set())

        def parity_homomorphism(self):
            r"""Return the parity ``M -> ZZ/2`` stated with this module's grading."""
            for cat in self.category().all_super_categories(proper=False):
                try:
                    parity = cat.parity_homomorphism
                except AttributeError:
                    continue
                return parity()
            raise TypeError(f"{self} is not in a graded module category")

        def combine_degrees(self, left, right):
            r"""The monoid product of two degrees.

            Additive monoids use \(+\); otherwise the monoid operation is
            multiplication.  A set grading alone supplies no such operation.
            """
            monoid = self.grading_monoid()
            left = monoid(left)
            right = monoid(right)
            if monoid in AdditiveMonoids():
                return left + right
            return left * right

        def concentrated_degree(self):
            selected = self.__dict__.get("_preamble_concentrated_degree")
            if selected is None:
                raise TypeError(f"{self} is not represented as a concentrated graded module")
            return selected

        def degree_on_module_generator(self, module_generator):
            r"""Return the selected degree of one homogeneous framing generator.

            A graded object whose grading is read from a framing supplies this
            operation.  Construction-specific parents such as free graded
            algebras override it; a merely category-placed object with no
            represented grading on its framing refuses rather than guessing.
            """
            selected = self.__dict__.get("_preamble_degree_on_module_generator")
            assert selected is not None, (
                f"{self} has no represented degree on its selected module framing"
            )
            return selected(module_generator)

        def module_generators_of_degree(self, degree):
            r"""Return the selected framing generators lying in ``degree``."""
            if self not in FramedModules(self.base_ring()):
                raise TypeError("graded-piece generators require a framed graded module")
            labels = self.module_generating_set()
            assert labels.cardinality().is_finite() is True, (
                "generic degree-piece filtering requires a finite selected framing; "
                "an infinite graded construction supplies its intrinsic graded_piece instead"
            )
            return finite_ordered_set(
                tuple(
                    self.module_generator(label)
                    for label in labels
                    if self.degree_on_module_generator(self.module_generator(label)) == degree
                )
            )

        def graded_piece(self, degree):
            r"""Return the represented degree piece as a subobject of this module.

            This is the generic framing-derived fallback.  Constructions with
            a more intrinsic degree-piece owner, such as tensor or symmetric
            powers, override this method and remain authoritative.
            """
            if self not in FramedModules(self.base_ring()):
                raise TypeError("a generic graded piece requires a framed graded module")
            return self.subobject_on(self.module_generators_of_degree(degree))

    class ElementMethods:
        def degree(self):
            r"""Return the largest degree occurring in the selected finite support.

            The zero element has degree ``-Infinity``.
            """
            parent = self.parent()
            if parent.grading_monoid() is not _own_ring(SageZZ):
                raise TypeError("top degree is represented here only for the integer grading")
            support = parent.framing_coefficients(self)
            if not support:
                return -_Infinity
            return max(
                parent.degree_on_module_generator(parent.module_generator(label))
                for label in support
            )

        def is_homogeneous(self) -> bool:
            r"""Whether all nonzero framing terms lie in one degree."""
            parent = self.parent()
            degrees = {
                parent.degree_on_module_generator(parent.module_generator(label))
                for label in parent.framing_coefficients(self).index_set()
            }
            return len(degrees) <= 1

        def homogeneous_components(self):
            r"""Return the degree-indexed nonzero homogeneous components."""
            parent = self.parent()
            components = {}
            for label, coefficient in parent.framing_coefficients(self).items():
                generator = parent.module_generator(label)
                degree = parent.degree_on_module_generator(generator)
                component = components.get(degree, parent.zero())
                components[degree] = component + parent.scalar_multiple(
                    coefficient, generator
                )
            return components

        def truncate(self, degree):
            r"""Return the sum of homogeneous terms of degree strictly below ``degree``."""
            parent = self.parent()
            if parent.grading_monoid() is not _own_ring(SageZZ):
                raise TypeError("degree truncation is represented here only for the integer grading")
            result = parent.zero()
            for label, coefficient in parent.framing_coefficients(self).items():
                generator = parent.module_generator(label)
                if parent.degree_on_module_generator(generator) < degree:
                    result += parent.scalar_multiple(coefficient, generator)
            return result
