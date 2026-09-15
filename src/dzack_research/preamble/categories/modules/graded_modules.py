"""Modules graded by a monoid."""

from sage.rings.infinity import Infinity as _Infinity
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.group.magmas import (
    AdditiveMonoids,
    Monoids,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreshFreeModuleOn,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    _initialize_module_hom_parent,
    _ModuleHomsetCommonMethods,
    module_coefficients,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FramedModules,
    LinearEndCategoryConstruction,
    Modules,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _own_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets


def normalize_grading_monoid(monoid: Parent | None) -> Parent:
    r"""Return the owned grading monoid, defaulting to \(\mathbb{Z},+\)."""
    return _own_ring(SageZZ) if monoid is None else monoid


def require_grading_monoid(monoid: Parent | None) -> Parent:
    monoid = normalize_grading_monoid(monoid)
    if monoid not in Monoids() and monoid not in AdditiveMonoids():
        raise TypeError(f"{monoid} is not a monoid in the owned category graph")
    return monoid


def grading_identity(monoid: Parent | None):
    r"""Return the identity degree of the selected grading monoid."""
    monoid = require_grading_monoid(monoid)
    if monoid in AdditiveMonoids():
        return monoid.zero()
    return monoid.one()


def concentrated_graded_module(base_ring, grading_monoid=None):
    r"""Return a rank-one graded module concentrated in the identity degree."""
    monoid = require_grading_monoid(grading_monoid)
    return FreshFreeModuleOn(
        base_ring,
        Sets.Δ[0],
        _extra_categories=(GradedModules(base_ring, monoid),),
        _extra_construction_data={
            "concentrated_degree": grading_identity(monoid),
        },
    )


def _selected_homogeneous_degree(element):
    r"""Return one represented homogeneous degree without imposing one element API."""
    parent = element.parent()
    selected = parent.__dict__.get("_preamble_concentrated_degree")
    if selected is not None:
        if element == parent.zero():
            raise ValueError("zero has no selected homogeneous degree here")
        return selected
    try:
        homogeneous = element.is_homogeneous()
        degree = element.degree()
    except AttributeError as error:
        raise NotImplementedError(
            "this graded-module element has no represented homogeneous degree"
        ) from error
    if not homogeneous:
        raise ValueError("the graded-module element is not homogeneous")
    return degree


class GradedModuleMorphism(ModuleMorphism):
    r"""A degree-zero morphism of graded modules."""

    def __init__(self, parent, images, *, elementwise=False) -> None:
        ModuleMorphism.__init__(self, parent, images, elementwise=elementwise)
        self._check_selected_degrees()

    def _check_selected_degrees(self) -> None:

        domain = self.domain()
        if domain not in FramedModules(domain.base_ring()):
            return
        for label in domain.module_generating_set():
            source = domain.module_generator(label)
            try:
                source_degree = _selected_homogeneous_degree(source)
            except NotImplementedError:
                continue
            image = self(source)
            if image == self.codomain().zero():
                continue
            try:
                target_degree = _selected_homogeneous_degree(image)
            except NotImplementedError as error:
                raise ValueError("a graded-module map has a nonhomogeneous image") from error
            if target_degree != source_degree:
                raise ValueError("a graded-module morphism must preserve degree")

    def __mul__(self, other):
        if not isinstance(other, GradedModuleMorphism):
            return super().__mul__(other)
        if other.codomain() is not self.domain():
            return NotImplemented
        domain = other.domain()
        monoid = require_grading_monoid(domain.grading_monoid())
        return GradedModules(domain.base_ring(), monoid).Mor(
            domain, self.codomain()
        ).elementwise(lambda element: self(other(element)))


class GradedModuleHomset(_ModuleHomsetCommonMethods, CategoricalHomset):
    Element = GradedModuleMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        source_monoid = require_grading_monoid(domain.grading_monoid())
        target_monoid = require_grading_monoid(codomain.grading_monoid())
        packet_monoid = hom_family.base_category().grading_monoid()
        if source_monoid != target_monoid:
            raise ValueError("graded-module morphisms require one grading monoid")
        if source_monoid != packet_monoid:
            raise ValueError("the graded-module Hom packet has the wrong grading monoid")
        _initialize_module_hom_parent(self, hom_family, domain, codomain)



class GradedModuleHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return GradedModuleHomset


class GradedModules(OwnedCategoryOverBaseRing):
    r"""Modules graded by a monoid.

    Let \(M\) be a monoid and \(R\) a ring. An \(M\)-graded \(R\)-module is
    an \(R\)-module \(N\) together with a direct-sum decomposition
    \(N = \bigoplus_{m \in M} N_m\). This is the nLab graded module over an
    ungraded ring (an \(M\)-graded object of \(\mathbf{Mod}_R\)).

    The default monoid is \(\mathbb{Z}\) (additive), which is Sage's graded
    module axiom. An \(M\)-graded algebra is an \(M\)-graded module whose
    product sends \(N_m \times N_{m'}\) into \(N_{mm'}\).
    """

    def an_object(self):
        r"""The rank-one module concentrated in the identity degree."""
        return concentrated_graded_module(self.base_ring(), self.grading_monoid())

    @staticmethod
    def __classcall__(cls, base_ring, grading_monoid=None):
        monoid = require_grading_monoid(grading_monoid)
        return OwnedCategoryOverBaseRing.__classcall__(cls, base_ring, monoid)

    def __init__(self, base_ring, grading_monoid: Parent) -> None:
        self._grading_monoid = grading_monoid
        super().__init__(base_ring)

    def grading_monoid(self) -> Parent:
        return self._grading_monoid

    def _repr_object_names(self) -> str:
        monoid = self.grading_monoid()
        if monoid is _own_ring(SageZZ):
            names = "graded modules"
        else:
            names = f"modules graded by {monoid}"
        return f"{names} over {self.base()}"

    def _make_named_class_key(self, name):
        return (super()._make_named_class_key(name), self.grading_monoid())

    def super_categories(self):

        return [Modules(self.base_ring())]

    _HomCategory = GradedModuleHomCategoryConstruction
    _EndCategory = LinearEndCategoryConstruction

    class ParentMethods:
        def is_graded(self) -> bool:
            return True

        def grading_monoid(self):
            for cat in self.category().all_super_categories(proper=False):
                try:
                    monoid = cat.grading_monoid()
                except AttributeError:
                    continue
                return monoid
            raise TypeError(f"{self} is not in a graded module category")

        def combine_degrees(self, left, right):
            r"""The monoid product of two degrees.

            Additive monoids use \(+\); otherwise the monoid operation is
            multiplication, so a monoid whose identity is not \(0\) (Young's
            \(s\oplus t=s+t-1\), identity \(1\)) is encoded as a Sage monoid.
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
            if selected is None:
                raise NotImplementedError(
                    f"{self} has no represented degree on its selected module framing"
                )
            return selected(module_generator)

        def module_generators_of_degree(self, degree):
            r"""Return the selected framing generators lying in ``degree``."""
            if self not in FramedModules(self.base_ring()):
                raise TypeError("graded-piece generators require a framed graded module")
            labels = self.module_generating_set()
            if labels.cardinality().is_finite() is not True:
                raise NotImplementedError(
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
            support = module_coefficients(self, parent)
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
                for label in module_coefficients(self, parent)
            }
            return len(degrees) <= 1

        def homogeneous_components(self):
            r"""Return the degree-indexed nonzero homogeneous components."""
            parent = self.parent()
            components = {}
            for label, coefficient in module_coefficients(self, parent).items():
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
            for label, coefficient in module_coefficients(self, parent).items():
                generator = parent.module_generator(label)
                if parent.degree_on_module_generator(generator) < degree:
                    result += parent.scalar_multiple(coefficient, generator)
            return result
