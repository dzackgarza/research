"""Modules graded by a monoid."""

from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.parent import Parent
from sage.categories.morphism import Morphism

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleHomset,
    ModuleMorphism,
    _ModuleHomsetCommonMethods,
    _initialize_module_hom_parent,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    LinearEndCategoryConstruction,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _own_ring,
)
from dzack_research.preamble.categories.group.magmas import (
    AdditiveMonoids,
    Monoids,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FramedModules,
    Modules,
)


def normalize_grading_monoid(monoid: Parent | None) -> Parent:
    r"""Return the owned grading monoid, defaulting to \(\mathbb{Z},+\)."""
    return _own_ring(SageZZ) if monoid is None else monoid


def require_grading_monoid(monoid: Parent | None) -> Parent:
    monoid = normalize_grading_monoid(monoid)
    if monoid not in Monoids() and monoid not in AdditiveMonoids():
        raise TypeError(f"{monoid} is not a monoid in the owned category graph")
    return monoid


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
                source_homogeneous = source.is_homogeneous()
                source_degree = source.degree()
            except AttributeError:
                continue
            if not source_homogeneous:
                raise ValueError("a selected graded-module generator is not homogeneous")
            image = self(source)
            if image == self.codomain().zero():
                continue
            try:
                target_homogeneous = image.is_homogeneous()
                target_degree = image.degree()
            except AttributeError as error:
                raise ValueError("a graded-module map has a nonhomogeneous target carrier") from error
            if not target_homogeneous or target_degree != source_degree:
                raise ValueError("a graded-module morphism must preserve degree")

    def __mul__(self, other):
        if not isinstance(other, GradedModuleMorphism):
            return super().__mul__(other)
        if other.codomain() is not self.domain():
            return NotImplemented
        return graded_module_homset(other.domain(), self.codomain()).elementwise(
            lambda element: self(other(element))
        )


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


def graded_module_homset(domain, codomain) -> GradedModuleHomset:
    ring = domain.base_ring()
    if codomain.base_ring() is not ring:
        raise ValueError("graded-module morphisms require one base ring")
    monoid = require_grading_monoid(domain.grading_monoid())
    if require_grading_monoid(codomain.grading_monoid()) != monoid:
        raise ValueError("graded-module morphisms require one grading monoid")
    return GradedModules(ring, monoid).Mor(domain, codomain)
