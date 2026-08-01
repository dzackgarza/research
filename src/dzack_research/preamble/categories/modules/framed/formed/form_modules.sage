r"""Modules equipped with a bilinear or quadratic form."""

from typing import Any

from sage.categories.category_types import Category_over_base_ring
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.categories.sets_cat import Sets as SageSets
from sage.matrix.matrix0 import Matrix
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp


class FormModules(Category_over_base_ring):
    r"""Modules over \(R\) equipped with a form."""

    @staticmethod
    def __classcall_private__(cls, base_ring=None):
        return super().__classcall__(cls, ZZ if base_ring is None else base_ring)

    @classmethod
    def _repr_object_names(cls) -> str:
        return "form modules"

    def super_categories(self) -> list:
        return [Modules(self.base_ring()).Framed()]

    class ParentMethods:
        def value_module(self: Any) -> Any:
            return self.form().value_module()

        def gram_matrix(self: Any) -> Matrix:
            return self.form().gram_matrix()

        def is_torsion_free(self: Any) -> bool:
            return self.forget_form().is_torsion_free()

        def is_torsion(self: Any) -> bool:
            return self.forget_form().is_torsion()

        def linear_combination(self: Any, coefficients: Any) -> Any:
            match coefficients:
                case dict():
                    return _combination(self, coefficients)
                case _:
                    raise TypeError(
                        "a form module with an arbitrary framing accepts a "
                        "finite dictionary of label-coefficient pairs"
                    )

        def Hom(self, codomain: Any) -> "FormHomset":
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

        def hom(self: Any, images: Any, codomain: Any = None) -> "FormMorphism":
            match images:
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
                    raise TypeError(
                        "a map from an arbitrarily framed form module is "
                        "specified by a dictionary or a function on its frame"
                    )
            return self.Hom(target)(assignment)

    class ElementMethods:
        def _coordinates(self: Any) -> Any:
            return _coordinate_vector(self.forget_form())

        def b(self: Any, other: Any) -> Any:
            assert other.parent() is self.parent(), (
                "a form pairs two elements of one formed module"
            )
            return self.parent().form().b(
                _forget_form_element(self),
                _forget_form_element(other),
            )

        def norm(self: Any) -> Any:
            return self.parent().form().norm(
                _forget_form_element(self)
            )

        def span(self: Any) -> Any:
            return self.parent().subobject_on([self])

        def isotropic_reduction(self: Any) -> Any:
            return self.span().isotropic_reduction()

        def __mul__(self: Any, other: Any) -> Any:
            match other:
                case Element() if other.parent() is self.parent():
                    return self.b(other)
                case _:
                    assert other in self.parent().base_ring(), (
                        f"{other} is not a scalar of {self.parent().base_ring()}"
                    )
                    return self.parent()._over(
                        other * _formed_element_representation(self)
                    )

        def __truediv__(self: Any, divisor: Any) -> Any:
            assert not self.parent().is_torsion(), (
                "division is not single-valued in a torsion module"
            )
            coordinates = self._coordinates() / divisor
            assert all(
                entry in self.parent().base_ring() for entry in coordinates
            ), "the quotient is not an element of this module"
            return self.parent().linear_combination(coordinates)


class BilinearFormModules(Category_over_base_ring):
    r"""Modules whose form is bilinear."""

    @staticmethod
    def __classcall_private__(cls, base_ring=None):
        return super().__classcall__(cls, ZZ if base_ring is None else base_ring)

    @classmethod
    def _repr_object_names(cls) -> str:
        return "modules with a bilinear form"

    def super_categories(self) -> list:
        return [FormModules(self.base_ring())]


class SymmetricBilinearFormModules(Category_over_base_ring):
    r"""Modules equipped with a symmetric bilinear form."""

    @staticmethod
    def __classcall_private__(cls, base_ring=None):
        return super().__classcall__(cls, ZZ if base_ring is None else base_ring)

    @classmethod
    def _repr_object_names(cls) -> str:
        return "modules with a symmetric bilinear form"

    def super_categories(self) -> list:
        return [BilinearFormModules(self.base_ring())]


class QuadraticFormModules(Category_over_base_ring):
    r"""Modules whose form is quadratic."""

    @staticmethod
    def __classcall_private__(cls, base_ring=None):
        return super().__classcall__(cls, ZZ if base_ring is None else base_ring)

    @classmethod
    def _repr_object_names(cls) -> str:
        return "modules with a quadratic form"

    def super_categories(self) -> list:
        return [FormModules(self.base_ring())]


class FreeFormModules(Category_over_base_ring):
    r"""Form modules whose image after forgetting the form is free."""

    @staticmethod
    def __classcall_private__(cls, base_ring=None):
        return super().__classcall__(cls, ZZ if base_ring is None else base_ring)

    @classmethod
    def _repr_object_names(cls) -> str:
        return "free form modules"

    def super_categories(self) -> list:
        return [
            FormModules(self.base_ring()),
            FramedFreeModules(self.base_ring()),
        ]

    class ParentMethods:
        def rank(self: Any) -> Any:
            return self.forget_form().rank()

        def basis(self: Any) -> Any:
            return self.gens()

        def monomial(self: Any, label: Any) -> Any:
            return self.generator(label)

        def subobject_on(self: Any, generators: Any) -> Any:
            generators = tuple(generators)
            assert all(generator.parent() is self for generator in generators), (
                "a subobject is generated by elements of this formed module"
            )
            generators = _independent_generators(self, generators)
            gram = matrix(
                [[left.b(right) for right in generators] for left in generators]
            )
            labels = finite_ordered_set(tuple(generators))
            sub = self._sub_form_module(gram, labels)
            images = {generator: generator for generator in labels}
            return Subobject(sub.Hom(self)(images))

        def _sub_form_module(
            self: Any,
            gram: Matrix,
            generating_set: Any,
        ) -> Any:
            module = BasedFreeModule(
                self.base_ring(),
                generating_set,
            )
            return BilinearForm(module, self.value_module(), gram)


class FinitelyGeneratedFormModules(Category_over_base_ring):
    r"""Form modules whose chosen framing set is finite."""

    @staticmethod
    def __classcall_private__(cls, base_ring=None):
        return super().__classcall__(cls, ZZ if base_ring is None else base_ring)

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely generated form modules"

    def super_categories(self) -> list:
        return [
            FormModules(self.base_ring()),
            FinitelyGeneratedModules(self.base_ring()),
        ]

    class ParentMethods:
        def ngens(self: Any) -> int:
            return int(self.generating_set().cardinality())

        def linear_combination(self: Any, coefficients: Any) -> Any:
            return _combination(self, coefficients)

        def hom(self: Any, images: Any, codomain: Any = None) -> "FormMorphism":
            match images:
                case dict():
                    return FormModules.ParentMethods.hom(
                        self,
                        images,
                        codomain,
                    )
                case _:
                    images = tuple(images)
                    assert len(images) == self.ngens(), (
                        "the number of images does not match the framing set"
                    )
                    if images:
                        target = images[0].parent()
                    else:
                        assert codomain is not None, (
                            "an empty assignment requires its codomain"
                        )
                        target = codomain
                    return self.Hom(target)(
                        dict(zip(self.generating_set(), images))
                    )


class FinitelyGeneratedFreeFormModules(Category_over_base_ring):
    r"""Finite free modules equipped with a form."""

    @staticmethod
    def __classcall_private__(cls, base_ring=None):
        return super().__classcall__(cls, ZZ if base_ring is None else base_ring)

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely generated free form modules"

    def super_categories(self) -> list:
        return [
            FreeFormModules(self.base_ring()),
            FinitelyGeneratedFormModules(self.base_ring()),
            FinitelyGeneratedFreeModules(self.base_ring()),
        ]

    class ParentMethods:
        def Aut(self: Any) -> Any:
            cached = self.__dict__.get("_preamble_Aut")
            if cached is None:
                cached = FormAutomorphismGroup(self)
                self._preamble_Aut = cached
            return cached


class FormModuleElement(Element):
    r"""An element of a formed module and its image after forgetting the form."""

    def __init__(self, parent: Any, element: Any) -> None:
        Element.__init__(self, parent)
        assert element.parent() is parent.forget_form(), (
            f"{element} is not an element of {parent.forget_form()}"
        )
        self._underlying = element

    def forget_form(self) -> Any:
        return self._underlying

    def _add_(self, other: Any) -> "FormModuleElement":
        return self.parent()._over(self._underlying + other._underlying)

    def _sub_(self, other: Any) -> "FormModuleElement":
        return self.parent()._over(self._underlying - other._underlying)

    def _neg_(self) -> "FormModuleElement":
        return self.parent()._over(-self._underlying)

    def _lmul_(self, factor: Any) -> "FormModuleElement":
        return self.parent()._over(factor * self._underlying)

    _rmul_ = _lmul_

    def _richcmp_(self, other: Any, op: int) -> bool:
        return richcmp(self._underlying, other._underlying, op)

    def __hash__(self) -> int:
        return hash((id(self.parent()), self._underlying))

    def _repr_(self) -> str:
        return repr(self._underlying)


def _formed_element_representation(element: Any) -> Any:
    r"""Forget exactly the form structure represented by ``element``."""
    match element:
        case FormModuleElement():
            return element.forget_form()
        case _:
            raise TypeError(f"{element} is not an element of a formed module")


class FormModule(Parent):
    r"""The formed object classified by one form morphism."""

    Element = FormModuleElement

    def __init__(self, form: Any) -> None:
        match form:
            case BilinearFormMorphism() | QuadraticFormMorphism():
                pass
            case _:
                raise TypeError(
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
        labels = module.generating_set()
        source = module.framing_morphism().domain()
        match labels in SageSets().Finite():
            case True:
                images = {
                    label: self._over(module.generator(label))
                    for label in labels
                }
            case False:
                images = lambda label: self._over(module.generator(label))
        self._framing_morphism = framing_morphism(source, self, images)
        self._refine_from_form()

    def _refine_from_form(self) -> None:
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
        owned_finite_torsion = finite_torsion and base_ring is ZZ
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
            and base_ring is ZZ
            and free
            and self._form.value_module() is ZZ
        ):
            refine_one_lattice(self)
            _decompose_lattice(self)
            if (
                isinstance(module, GroupModule)
                and _action_preserves_form(self)
            ):
                refine(self, GroupLattices(module.group()))
                _install_group_lattice_structure(self)

    def form(self) -> Any:
        return self._form

    def forget_form(self) -> Any:
        return self._module

    def framing_morphism(self) -> FramingMorphism:
        return self._framing_morphism

    def monomial(self, label: Any) -> FormModuleElement:
        return self.generator(label)

    def _element_constructor_(self, element: Any) -> FormModuleElement:
        assert isinstance(element, FormModuleElement) and element.parent() is self, (
            f"{element} is not an element of {self}"
        )
        return element

    def __contains__(self, element: Any) -> bool:
        return (
            isinstance(element, FormModuleElement)
            and element.parent() is self
        )

    def _over(self, element: Any) -> FormModuleElement:
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

    def __init__(self, domain: Any, codomain: Any, category: Any) -> None:
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

    def _element_constructor_(self, images: Any) -> "FormMorphism":
        match images:
            case ModuleMorphism():
                module_morphism = images
                assert module_morphism.parent() is self._module_homset, (
                    "the module morphism belongs to a different homset"
                )
            case dict():
                module_morphism = self._module_homset(images)
            case _ if callable(images):
                module_morphism = self._module_homset(images)
            case _:
                raise TypeError(
                    "a form morphism is specified by a dictionary or "
                    "function on the domain framing"
                )
        return FormMorphism(self, module_morphism)

    def __contains__(self, morphism: Any) -> bool:
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
        assert parent.domain().form() == pulled_back, (
            "the module morphism does not preserve the stated form"
        )
        self._module_morphism = module_morphism

    def module_morphism(self) -> ModuleMorphism:
        return self._module_morphism

    def matrix(self) -> Matrix:
        return self._module_morphism.matrix()

    def _call_(self, element: Any) -> Any:
        return self._module_morphism(element)

    def lift(self, element: Any) -> Any:
        return self._module_morphism.lift(element)

    def kernel(self) -> Any:
        return self._module_morphism.kernel()

    def cokernel(self) -> Any:
        return self._module_morphism.cokernel()

    def image(self) -> Any:
        return self._module_morphism.image()

    def is_injective(self) -> bool:
        return self._module_morphism.is_injective()

    def index(self) -> Any:
        return self._module_morphism.index()

    def orthogonal_complement(self) -> Any:
        return self._module_morphism.orthogonal_complement()

    def then(self, other: "FormMorphism") -> "FormMorphism":
        assert other.domain() is self.codomain(), (
            "the codomain of the first map is not the domain of the second"
        )
        return self.domain().Hom(other.codomain())(
            {
                label: other(self(self.domain().generator(label)))
                for label in self.domain().generating_set()
            }
        )

    def __mul__(self, other: Any) -> "FormMorphism":
        assert (
            isinstance(other, FormMorphism)
            and other.parent() is self.parent()
        ), "composition here is internal to one automorphism homset"
        return self.parent()(
            {
                label: self(other(self.domain().generator(label)))
                for label in self.domain().generating_set()
            }
        )

    def __eq__(self, other: Any) -> bool:
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
        return self._module_morphism._repr_defn()


class FormAutomorphismGroup(FormHomset):
    r"""The invertible form-preserving endomorphisms of a finite free object."""

    def __init__(self, formed_module: Any) -> None:
        assert formed_module in FinitelyGeneratedFreeFormModules(
            formed_module.base_ring()
        ), "form automorphisms here require a finite free module"
        FormHomset.__init__(
            self,
            formed_module,
            formed_module,
            FormModules(formed_module.base_ring()),
        )

    def _element_constructor_(self, images: Any) -> FormMorphism:
        morphism = FormHomset._element_constructor_(self, images)
        determinant = morphism.matrix().det()
        assert determinant.is_unit(), (
            f"the determinant {determinant} is not a unit"
        )
        return morphism

    def one(self) -> FormMorphism:
        return self(
            {
                label: self.domain().generator(label)
                for label in self.domain().generating_set()
            }
        )

    def __contains__(self, morphism: Any) -> bool:
        return (
            isinstance(morphism, FormMorphism)
            and morphism.parent() is self
        )


def correlation_of(lattice: Any) -> FormMorphism:
    r"""Return \(c:L\to L^\vee\), \(v\mapsto b(v,-)\)."""
    dual = lattice.dual()
    return lattice.Hom(dual)(
        {
            label: dual.linear_combination(row)
            for label, row in zip(
                lattice.generating_set(),
                lattice.gram_matrix().rows(),
            )
        }
    )
