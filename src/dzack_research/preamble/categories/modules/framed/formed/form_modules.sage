r"""Modules equipped with a bilinear or quadratic form."""


from sage.rings.integer_ring import ZZ as SageZZ
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage_lattice_category_spike.lexicon import Lattice
    from sage_lattice_category_spike.lexicon import Module
    from sage_lattice_category_spike.lexicon import Vector

from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import FramingMorphism
from sage.categories.groups import Groups
from sage.matrix.constructor import Matrix
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
from sage.categories.modules import Modules
if TYPE_CHECKING:
    from sage.categories.category import Category
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleAutomorphismGroup
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
    from sage.rings.ring import Ring
    from sage.structure.element import RingElement

from dzack_research.preamble.categories.rings.rings import OwnedBaseRing
from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from typing import Any, Self, TYPE_CHECKING

from sage.categories.homset import Hom, Homset
from sage.categories.morphism import Morphism, SetMorphism
from sage.rings.integer import Integer
from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet
from sage.structure.element import Element, ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp
from sage_lattice_category_spike.lexicon import GramMatrix, MorphismMatrix
from sage_lattice_category_spike.objects.cardinals import Cardinal

from sage_lattice_category_spike.objects.sets import Sets
from sage_lattice_category_spike.objects.underlying_sets import UnderlyingSet

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from sage_lattice_category_spike.lexicon import OrderedSet


def _finite_rank(module_generating_set: TotallyOrderedFiniteSet) -> Integer:
    size = module_generating_set.cardinality()
    if isinstance(size, Cardinal):
        assert size.is_finite(), "a finitely generated form module has finite rank"
        return size.finite_value()
    return Integer(size)


class FormModules(OwnedCategoryOverBaseRing):
    r"""Modules over \(R\) equipped with a form."""

    @staticmethod
    def __classcall_private__(cls: type, base_ring: "Ring" = None) -> "FormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        return super().__classcall__(
            cls, SageZZ if base_ring is None else engine_ring(base_ring)
        )

    @classmethod
    def _repr_object_names(cls) -> str:
        return "form modules"

    def super_categories(self) -> list:
        return [Modules(self.base_ring()).Framed()]

    class ParentMethods:

        # Read off the carried data, so what makes an object formed is the
        # data and its placement -- not which class constructed it.  A ring
        # equipped as its own rank-one lattice answers these too.
        def form(self: Self) -> "FormMorphism":
            r"""Return the form morphism classifying this object."""
            return self._form

        def forget_form(self: Self) -> "Module":
            r"""Return the underlying module, forgetting the form."""
            return self._module

        def framing_morphism(self: Self) -> "FramingMorphism":
            r"""Return the framing \(F_R(S)\to M\)."""
            return self._framing_morphism

        def value_module(self: Self) -> "Module":
            return self.form().value_module()

        def gram_matrix(self: Self) -> GramMatrix:
            return self.form().gram_matrix()

        def is_torsion_free(self: Self) -> bool:
            return bool(self.forget_form().is_torsion_free())

        def is_torsion(self: Self) -> bool:
            return bool(self.forget_form().is_torsion())

        def Hom(self: Self, codomain: "Module", category: "Category" = None) -> "Homset":
            if codomain in FormModules(self.base_ring()):
                cache = self.__dict__.setdefault("_form_module_homsets", {})
                homset = cache.get(codomain)
                if homset is None:
                    homset = FormHomset(
                        self,
                        codomain,
                        FormModules(self.base_ring()),
                    )
                    cache[codomain] = homset
                return homset
            return Parent.Hom(self, codomain, category)

        def hom(self: Self, images: dict, codomain: "Module" = None) -> "FormMorphism":
            match images:
                case SetMorphism():
                    assert isinstance(images.codomain(), UnderlyingSet), (
                        "a generator morphism lands in the underlying set of "
                        "its module codomain"
                    )
                    target = images.codomain().structured_parent()
                    assignment = images
                case dict() if images:
                    target = next(iter(images.values())).parent()
                    assignment = images
                case dict():
                    assert codomain is not None, (
                        "an empty assignment requires its codomain"
                    )
                    target = codomain
                    assignment = images
                case _ if callable(images):
                    assert codomain is not None, (
                        "a function on an arbitrary framing requires its codomain"
                    )
                    target = codomain
                    assignment = images
                case _:
                    assert False, (
                        "a map from an arbitrarily framed form module is "
                        "specified by a finite assignment or a function on "
                        "its generating set"
                    )
            return self.Hom(target)(assignment)

    class ElementMethods:

        def _coordinates(self: Self) -> "Vector":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector
            return _coordinate_vector(self.forget_form())

        def b(self: Self, other: "Element") -> "Element":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.forms.forms import _forget_form_element
            assert other.parent() is self.parent(), (
                "a form pairs two elements of one formed module"
            )
            return self.parent().form().b(
                _forget_form_element(self),
                _forget_form_element(other),
            )

        def norm(self: Self) -> "Element":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.forms.forms import _forget_form_element
            return self.parent().form().norm(
                _forget_form_element(self)
            )

        def span(self: Self) -> "Subobject":
            return self.parent().subobject_on([self])

        def isotropic_reduction(self: Self) -> "Module":
            return self.span().isotropic_reduction()

        def __mul__(self: Self, other: object) -> "Element":
            match other:
                case Element() if other.parent() is self.parent():
                    return self.b(other)
                case scalar if scalar in self.parent().base_ring():
                    return self.parent()._over(
                        scalar * _formed_element_representation(self)
                    )
                case _:
                    assert False, (
                        f"{other} is neither an element of {self.parent()} nor "
                        f"a scalar of {self.parent().base_ring()}"
                    )

        def __truediv__(self: Self, divisor: "RingElement") -> "Element":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.utilities import zipsum
            assert not self.parent().is_torsion(), (
                "division is not single-valued in a torsion module"
            )
            coordinates = self._coordinates() / divisor
            coefficient_ring = self.parent().base_ring()
            assert all(
                entry in coefficient_ring for entry in coordinates
            ), "the quotient is not an element of this module"
            return zipsum(
            tuple(coefficient_ring(entry) for entry in coordinates),
            self.parent().module_generators(),
            self.parent().zero(),
            )


class BilinearFormModules(OwnedCategoryOverBaseRing):
    r"""Modules whose form is bilinear."""

    @staticmethod
    def __classcall_private__(cls: type, base_ring: "Ring" = None) -> "BilinearFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        return super().__classcall__(
            cls, SageZZ if base_ring is None else engine_ring(base_ring)
        )

    @classmethod
    def _repr_object_names(cls) -> str:
        return "modules with a bilinear form"

    def super_categories(self) -> list:
        return [FormModules(self.base_ring())]


class SymmetricBilinearFormModules(OwnedCategoryOverBaseRing):
    r"""Modules equipped with a symmetric bilinear form."""

    @staticmethod
    def __classcall_private__(cls: type, base_ring: "Ring" = None) -> "SymmetricBilinearFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        return super().__classcall__(
            cls, SageZZ if base_ring is None else engine_ring(base_ring)
        )

    @classmethod
    def _repr_object_names(cls) -> str:
        return "modules with a symmetric bilinear form"

    def super_categories(self) -> list:
        return [BilinearFormModules(self.base_ring())]


class QuadraticFormModules(OwnedCategoryOverBaseRing):
    r"""Modules whose form is quadratic."""

    @staticmethod
    def __classcall_private__(cls: type, base_ring: "Ring" = None) -> "QuadraticFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        return super().__classcall__(
            cls, SageZZ if base_ring is None else engine_ring(base_ring)
        )

    @classmethod
    def _repr_object_names(cls) -> str:
        return "modules with a quadratic form"

    def super_categories(self) -> list:
        return [FormModules(self.base_ring())]


class FreeFormModules(OwnedCategoryOverBaseRing):
    r"""Form modules whose image after forgetting the form is free."""

    @staticmethod
    def __classcall_private__(cls: type, base_ring: "Ring" = None) -> "FreeFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        return super().__classcall__(
            cls, SageZZ if base_ring is None else engine_ring(base_ring)
        )

    @classmethod
    def _repr_object_names(cls) -> str:
        return "free form modules"

    def super_categories(self) -> list:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
        return [
            FormModules(self.base_ring()),
            FramedFreeModules(self.base_ring()),
        ]

    class ParentMethods:

        def rank(self: Self) -> "Cardinal":
            return self.forget_form().rank()

        def subobject_on(self: Self, module_generators: "OrderedSet") -> "Subobject":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _independent_module_generators
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set
            module_generators = tuple(module_generators)
            assert all(generator.parent() is self for generator in module_generators), (
                "a subobject is generated by elements of this formed module"
            )
            module_generators = _independent_module_generators(self, module_generators)
            gram = matrix(
                [[left.b(right) for right in module_generators] for left in module_generators]
            )
            labels = finite_ordered_set(tuple(module_generators))
            sub = self._sub_form_module(gram, labels)
            images = {generator: generator for generator in labels}
            return Subobject(sub.Hom(self)(images))

        def _sub_form_module(
            self: Self,
            gram: Matrix,
            module_generating_set: "OrderedSet",
        ) -> "FormMorphism":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
            from dzack_research.preamble.categories.forms.forms import BilinearForm
            module = BasedFreeModule(
                self.base_ring(),
                module_generating_set,
            )
            return BilinearForm(module, self.value_module(), gram)

    class ElementMethods:
        def underlying_set_element(self: Self) -> "Element":
            r"""Recover the element of \(S\) defining a canonical generator."""
            return self.forget_form().underlying_set_element()


class FinitelyGeneratedFormModules(OwnedCategoryOverBaseRing):
    r"""Form modules whose chosen framing set is finite."""

    @staticmethod
    def __classcall_private__(cls: type, base_ring: "Ring" = None) -> "FinitelyGeneratedFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        return super().__classcall__(
            cls, SageZZ if base_ring is None else engine_ring(base_ring)
        )

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely generated form modules"

    def super_categories(self) -> list:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.pure.finitely_generated.finitely_generated_modules import FinitelyGeneratedModules
        return [
            FormModules(self.base_ring()),
            FinitelyGeneratedModules(self.base_ring()),
        ]

    class ParentMethods:

        def number_of_module_generators(self: Self) -> Integer:
            return _finite_rank(self.module_generating_set())

        def hom(self: Self, images: dict, codomain: "Module" = None) -> "FormMorphism":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.framed_modules import _finite_module_generator_assignment
            match images:
                case dict():
                    return FormModules.ParentMethods.hom(
                        self,
                        images,
                        codomain,
                    )
                case list() | tuple():
                    target, assignment = _finite_module_generator_assignment(
                        self,
                        images,
                        codomain,
                    )
                    return self.Hom(target)(assignment)
                case _:
                    assert False, (
                        "a homomorphism is specified by a finite assignment "
                        "or an ordered list of images"
                    )


class FinitelyGeneratedFreeFormModules(OwnedCategoryOverBaseRing):
    r"""Finite free modules equipped with a form."""

    @staticmethod
    def __classcall_private__(cls: type, base_ring: "Ring" = None) -> "FinitelyGeneratedFreeFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        return super().__classcall__(
            cls, SageZZ if base_ring is None else engine_ring(base_ring)
        )

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely generated free form modules"

    def super_categories(self) -> list:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import FinitelyGeneratedFreeModules
        return [
            FreeFormModules(self.base_ring()),
            FinitelyGeneratedFormModules(self.base_ring()),
            FinitelyGeneratedFreeModules(self.base_ring()),
        ]

    class ParentMethods:
        def Aut(self: Self) -> "ModuleAutomorphismGroup":
            cached = self.__dict__.get("_preamble_Aut")
            if cached is None:
                cached = FormAutomorphismGroup(self)
                self._preamble_Aut = cached
            return cached


class FormModuleElement(ModuleElement):
    r"""An element of a formed module and its image after forgetting the form."""


    def __init__(self, parent: "Parent", element: "Element") -> None:
        ModuleElement.__init__(self, parent)
        assert element.parent() is parent.forget_form(), (
            f"{element} is not an element of {parent.forget_form()}"
        )
        self._underlying = element

    def forget_form(self) -> "Module":
        return self._underlying

    def coefficients(self) -> dict[Any, Any]:
        return dict(self._underlying.coefficients())

    def _add_(self: "FormModuleElement", other: "FormModuleElement") -> "FormModuleElement":
        return self.parent()._over(self._underlying + other._underlying)

    def _sub_(self: "FormModuleElement", other: "FormModuleElement") -> "FormModuleElement":
        return self.parent()._over(self._underlying - other._underlying)

    def _neg_(self: "FormModuleElement") -> "FormModuleElement":
        return self.parent()._over(-self._underlying)

    def _lmul_(self: "FormModuleElement", factor: "RingElement") -> "FormModuleElement":
        return self.parent()._over(factor * self._underlying)

    _rmul_ = _lmul_

    def _richcmp_(self: "FormModuleElement", other: object, op: int) -> bool:
        return bool(richcmp(self._underlying, other._underlying, op))

    def __hash__(self) -> int:
        return hash((id(self.parent()), self._underlying))

    def _repr_(self) -> str:
        return repr(self._underlying)


def _formed_element_representation(element: "Element") -> "Element":
    r"""Forget exactly the form structure represented by ``element``."""
    match element:
        case FormModuleElement():
            return element.forget_form()
        case _:
            assert False, f"{element} is not an element of a formed module"


class FormModule(OwnedBaseRing, Parent):
    r"""The formed object classified by one form morphism."""

    Element = FormModuleElement

    def __init__(self, form: "FormMorphism") -> None:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.forms.forms import BilinearFormMorphism
        from dzack_research.preamble.categories.forms.forms import QuadraticFormMorphism
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import framing_morphism
        match form:
            case BilinearFormMorphism() | QuadraticFormMorphism():
                pass
            case _:
                assert False, (
                    "FormModule requires a bilinear or quadratic form morphism"
                )
        module = form.module()
        self._form = form
        self._module = module
        Parent.__init__(
            self,
            base=module.base_ring(),
            category=FormModules(module.base_ring()),
        )
        source = module.framing_morphism().domain()
        underlying_module_generator_morphism = module.module_generator_morphism()
        lifted_module_generator_morphism = SetMorphism(
            Hom(
                underlying_module_generator_morphism.domain(),
                UnderlyingSet(self),
                Sets(),
            ),
            lambda element_of_S: self._over(
                underlying_module_generator_morphism._call_(element_of_S)
            ),
        )
        self._free_module_generator_morphism = lifted_module_generator_morphism
        self._framing_morphism = framing_morphism(
            source,
            self,
            lifted_module_generator_morphism,
        )
        self._refine_from_form()

    def _refine_from_form(self) -> None:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.forms.forms import BilinearFormMorphism
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import FinitelyGeneratedFreeModules
        from dzack_research.preamble.categories.modules.pure.finitely_generated.finitely_generated_modules import FinitelyGeneratedModules
        from dzack_research.preamble.categories.modules.pure.free_modules import FreeModules
        from dzack_research.preamble.categories.modules.group_modules.group_lattices import GroupLattices
        from dzack_research.preamble.categories.modules.group_modules.group_modules import GroupModule
        from dzack_research.preamble.categories.forms.forms import QuadraticFormMorphism
        from dzack_research.preamble.categories.modules.pure.torsion_modules import TorsionModules
        from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import TorsionModulesWithForm
        from dzack_research.preamble.categories.modules.group_modules.group_lattices import _action_preserves_form
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import _decompose_lattice
        from dzack_research.preamble.categories.modules.group_modules.group_lattices import _install_group_lattice_structure
        from dzack_research.preamble.categories.rings.rings import engine_ring
        from dzack_research.preamble.refine import refine
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import refine_one_lattice
        module = self._module
        base_ring = module.base_ring()
        free = module in FreeModules(base_ring)
        finitely_generated = module in FinitelyGeneratedModules(base_ring)
        zero = finitely_generated and module.is_zero()
        torsion = (
            module in TorsionModules(base_ring)
            or zero
        )
        finite_torsion = torsion and finitely_generated
        owned_finite_torsion = finite_torsion and engine_ring(base_ring) is SageZZ
        bilinear = isinstance(self._form, BilinearFormMorphism)
        quadratic = isinstance(self._form, QuadraticFormMorphism)
        symmetric_bilinear = (
            bilinear
            and self._form.gram_matrix().is_symmetric()
        )
        match (bilinear, quadratic, free, owned_finite_torsion):
            case (True, False, True, True):
                refine(
                    self,
                    [
                        BilinearFormModules(base_ring),
                        FreeFormModules(base_ring),
                        TorsionModulesWithForm(base_ring),
                    ],
                )
            case (True, False, True, False):
                refine(
                    self,
                    [
                        BilinearFormModules(base_ring),
                        FreeFormModules(base_ring),
                    ],
                )
            case (True, False, False, True):
                refine(
                    self,
                    [
                        BilinearFormModules(base_ring),
                        TorsionModulesWithForm(base_ring),
                    ],
                )
            case (True, False, False, False):
                refine(self, BilinearFormModules(base_ring))
            case (False, True, True, False):
                refine(
                    self,
                    [
                        QuadraticFormModules(base_ring),
                        FreeFormModules(base_ring),
                    ],
                )
            case (False, True, True, True):
                refine(
                    self,
                    [
                        QuadraticFormModules(base_ring),
                        FreeFormModules(base_ring),
                        TorsionModulesWithForm(base_ring),
                    ],
                )
            case (False, True, False, True):
                refine(
                    self,
                    [
                        QuadraticFormModules(base_ring),
                        TorsionModulesWithForm(base_ring),
                    ],
                )
            case (False, True, False, False):
                refine(self, QuadraticFormModules(base_ring))
            case _:
                assert False, (
                    "a form has exactly one of the bilinear and quadratic kinds"
                )
        match (bilinear, symmetric_bilinear):
            case (True, True):
                refine(self, SymmetricBilinearFormModules(base_ring))
            case (True, False) | (False, False):
                pass
            case _:
                assert False, "only a bilinear form can be symmetric bilinear"
        match (torsion, owned_finite_torsion):
            case (True, False):
                refine(self, TorsionModules(base_ring))
            case (True, True) | (False, False):
                pass
            case _:
                assert False, "owned finite torsion implies torsion"
        match (
            module in FinitelyGeneratedFreeModules(base_ring),
            finitely_generated,
        ):
            case (True, True):
                refine(
                    self,
                    [
                        FinitelyGeneratedFormModules(base_ring),
                        FinitelyGeneratedFreeFormModules(base_ring),
                    ],
                )
            case (False, True):
                refine(self, FinitelyGeneratedFormModules(base_ring))
            case (False, False):
                pass
            case _:
                assert False, (
                    "a finitely generated free module is finitely generated"
                )
        if (
            symmetric_bilinear
            and engine_ring(base_ring) is SageZZ
            and free
            and engine_ring(self._form.value_module()) is SageZZ
        ):
            refine_one_lattice(self)
            if (
                isinstance(module, GroupModule)
                and _action_preserves_form(self)
            ):
                refine(self, GroupLattices(module.group()))
                _install_group_lattice_structure(self)

    def _element_constructor_(self, element: FormModuleElement) -> FormModuleElement:
        assert isinstance(element, FormModuleElement) and element.parent() is self, (
            f"{element} is not an element of {self}"
        )
        return element

    def __contains__(self, element: "Element") -> bool:
        return (
            isinstance(element, FormModuleElement)
            and element.parent() is self
        )

    def _over(self, element: "Element") -> FormModuleElement:
        return self.element_class(self, element)


    def zero(self) -> FormModuleElement:
        return self._over(self._module.zero())

    def _repr_(self) -> str:
        return (
            f"{type(self._form).__name__} on {self._module} with values in "
            f"{self.value_module()}"
        )


class FormHomset(Homset):
    r"""The homset of form-preserving morphisms between formed modules."""

    def __init__(self, domain: "Module", codomain: "Module", category: "Category") -> None:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
        assert domain.base_ring() == codomain.base_ring(), (
            "form morphisms require the same module base ring"
        )
        Homset.__init__(
            self,
            domain,
            codomain,
            category=category,
            base=domain.base_ring(),
            check=False,
        )
        self._module_homset = module_homset(domain, codomain)

    def _element_constructor_(self, images: dict) -> "FormMorphism":
        match images:
            case ModuleMorphism():
                module_morphism = images
                assert module_morphism.parent() is self._module_homset, (
                    "the module morphism belongs to a different homset"
                )
            case SetMorphism() | dict():
                module_morphism = self._module_homset(images)
            case _ if callable(images):
                module_morphism = self._module_homset(images)
            case _:
                assert False, (
                    "a form morphism is specified by its generator morphism"
                )
        return FormMorphism(self, module_morphism)

    def __contains__(self, morphism: "Morphism") -> bool:
        return (
            isinstance(morphism, FormMorphism)
            and morphism.parent() is self
        )

    def _repr_(self) -> str:
        return (
            f"Form-preserving morphisms from {self.domain()} to "
            f"{self.codomain()}"
        )


class FormMorphism(Morphism):
    r"""A morphism whose underlying module map preserves the form."""

    def __init__(self, parent: FormHomset, module_morphism: ModuleMorphism) -> None:
        Morphism.__init__(self, parent)
        pulled_back = parent.codomain().form().pullback(module_morphism)
        expected_form = parent.domain().form()
        if pulled_back.codomain() is not expected_form.codomain():
            pulled_back = pulled_back.reduced(expected_form.codomain())
        assert parent.domain().form() == pulled_back, (
            "the module morphism does not preserve the stated form"
        )
        self._module_morphism = module_morphism

    def module_morphism(self) -> ModuleMorphism:
        return self._module_morphism

    def module_generator_morphism(self) -> SetMorphism:
        return self._module_morphism.module_generator_morphism()

    def matrix(self) -> MorphismMatrix:
        return self._module_morphism.matrix()

    def _call_(self, element: "Element") -> "Element":
        return self._module_morphism(element)

    def lift(self, element: "Element") -> "ModuleElement":
        return self._module_morphism.lift(element)

    def kernel(self) -> "Subobject":
        return self._module_morphism.kernel()

    def cokernel(self) -> "FinitelyPresentedModule":
        return self._module_morphism.cokernel()

    def image(self) -> "Subobject":
        return self._module_morphism.image()

    def is_injective(self) -> bool:
        return bool(self._module_morphism.is_injective())

    def index(self) -> "Integer":
        return self._module_morphism.index()

    def orthogonal_complement(self) -> "Subobject":
        return self._module_morphism.orthogonal_complement()

    def then(self, other: "FormMorphism") -> "FormMorphism":
        assert other.domain() is self.codomain(), (
            "the codomain of the first map is not the domain of the second"
        )
        module_generator_morphism = self.module_generator_morphism()
        return self.domain().Hom(other.codomain())(
                SetMorphism(
                    Hom(
                        module_generator_morphism.domain(),
                        UnderlyingSet(other.codomain()),
                        Sets(),
                    ),
                    lambda element_of_S: other(
                        module_generator_morphism._call_(element_of_S)
                    ),
                )
            )

    def __mul__(self, other: object) -> "FormMorphism":
        assert (
            isinstance(other, FormMorphism)
            and other.parent() is self.parent()
        ), "composition here is internal to one automorphism homset"
        module_generator_morphism = other.module_generator_morphism()
        return self.parent()(
                SetMorphism(
                    Hom(
                        module_generator_morphism.domain(),
                        UnderlyingSet(self.codomain()),
                        Sets(),
                    ),
                    lambda element_of_S: self(
                        module_generator_morphism._call_(element_of_S)
                    ),
                )
            )

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, FormMorphism)
            and self.parent() is other.parent()
            and self._module_morphism == other._module_morphism
        )

    def __hash__(self) -> int:
        return hash((id(self.parent()), self._module_morphism))

    def _repr_type(self) -> str:
        return "Form"

    def _repr_defn(self) -> str:
        return str(self._module_morphism._repr_defn())


class FormAutomorphismGroup(FormHomset):
    r"""The invertible form-preserving endomorphisms of a finite free object."""

    def __init__(self, formed_module: "Module") -> None:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.refine import refine
        assert formed_module in FinitelyGeneratedFreeFormModules(
            formed_module.base_ring()
        ), "form automorphisms here require a finite free module"
        FormHomset.__init__(
            self,
            formed_module,
            formed_module,
            FormModules(formed_module.base_ring()),
        )
        # \(\operatorname{Aut}\) in formed modules is a group, so that is the
        # placement.  Not the module-homset category as well: that carries
        # the additive axioms of \(\operatorname{End}\), which is a ring --
        # whereas \(\operatorname{Aut}\) is its group of units, closed under
        # composition and inverse and not under addition.  Declaring both
        # makes this object an additive *and* multiplicative semigroup, and
        # constructions keyed on that, \(R[G]\) among them, rightly refuse it
        # as ambiguous.  The homset surface comes from the class it subclasses.
        refine(self, [Groups()])

    def _element_constructor_(self, images: dict) -> FormMorphism:
        morphism = FormHomset._element_constructor_(self, images)
        determinant = morphism.matrix().det()
        assert determinant.is_unit(), (
            f"the determinant {determinant} is not a unit"
        )
        return morphism

    def one(self) -> FormMorphism:
        return self(self.domain().module_generator_morphism())

    def __contains__(self, morphism: "Morphism") -> bool:
        return (
            isinstance(morphism, FormMorphism)
            and morphism.parent() is self
        )


def correlation_of(lattice: "Lattice") -> FormMorphism:
    r"""Return \(c:L\to L^\vee\), \(v\mapsto b(v,-)\)."""
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.utilities import zipsum
    dual = lattice.dual_lattice()
    return lattice.Hom(dual)(
            {
                label: zipsum(
                row,
                dual.module_generators(),
                dual.zero(),
            )
                for label, row in zip(
                    lattice.module_generating_set(),
                    lattice.gram_matrix().rows(),
                )
            }
        )
