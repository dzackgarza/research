r"""Modules equipped with a bilinear or quadratic form."""


from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ as SageZZ
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.modules import Module
    from sage.structure.element import Vector
    from sage.structure.parent import ElementConstructorInput, MembershipInput

from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import FramingMorphism
from sage.categories.groups import Groups
from sage.matrix.matrix0 import Matrix
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
from dzack_research.preamble.categories.modules.framed.framed_modules import FramedModules
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
from dzack_research.preamble.owned_category import object_of
from typing import Protocol, Self, TYPE_CHECKING, TypeAlias

from sage.categories.homset import Hom, Homset
from sage.misc.cachefunc import cached_method
from sage.categories.morphism import Morphism, SetMorphism
from sage.rings.integer import Integer
from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet
from sage.structure.element import Element, ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp
from dzack_research.preamble.lexicon import GramMatrix
from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import MorphismMatrix
from dzack_research.preamble.categories.sets.cardinals import Cardinal

from dzack_research.preamble.categories.sets.owned_sets import placement_of
from dzack_research.preamble.categories.sets.owned_sets import Sets
from dzack_research.preamble.categories.sets.underlying_sets import (
    UnderlyingSet,
    UnderlyingSets,
)

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet

    from dzack_research.preamble.owned_category import ConstructionData

    from collections.abc import Callable

    from dzack_research.preamble.categories.forms.forms import BilinearFormMorphism
    from dzack_research.preamble.categories.forms.forms import QuadraticFormMorphism
    from dzack_research.preamble.categories.modules.tensors import TensorElement

    # The form itself: the morphism out of $M\otimes_R M$ (or the quadratic
    # map) that a formed module is equipped with.  Not ``FormMorphism``
    # below, which is a map *between* two formed modules.
    Form: TypeAlias = BilinearFormMorphism | QuadraticFormMorphism

    # How a map out of a formed module may be named: an assignment on the
    # framing labels, the generator morphism itself, or a function on the
    # framing set.
    GeneratorAssignment: TypeAlias = SetMorphism | dict | Callable

    class FormedParent(Protocol):
        r"""What an object of these categories offers.

        Structural rather than a class, for the reason the categories
        themselves are: what makes an object formed is the carried data and
        its placement, so a ring equipped as its own rank-one lattice
        answers these too and is no instance of ``FormModule``.
        """

        _module: "Module"
        _framing_morphism: FramingMorphism

        def _form_morphism(self) -> "Form": ...
        def base_ring(self) -> "Ring": ...
        def form(self) -> "Form": ...
        def forget_form(self) -> "Module": ...
        def value_module(self) -> "Module": ...
        def gram_matrix(self) -> GramMatrix: ...
        def vector_space(self) -> "FormedParent": ...
        def module_generating_set(self) -> "OrderedSet": ...
        def module_generators(self) -> tuple: ...
        def module_generator_morphism(self) -> SetMorphism: ...
        def zero(self) -> "Element": ...
        def is_torsion(self) -> bool: ...
        def raise_index(
            self,
            tensor: "TensorElement",
            slot: Integer = ...,
        ) -> "TensorElement": ...
        def _sub_form_module(
            self,
            gram: Matrix,
            module_generating_set: "OrderedSet",
        ) -> Parent: ...
        def Hom(
            self,
            codomain: "Module",
            category: "Category | None" = ...,
        ) -> Homset: ...

    class FiniteFreeFormedParent(FormedParent, Protocol):
        r"""What the finitely generated free formed surface adds.

        Separate from ``FormedParent`` because these are not questions every
        formed module can answer: the dual and the correlation morphism are
        built from a finite basis.
        """

        _preamble_Aut: "ModuleAutomorphismGroup"

        def dual_module(self) -> "Module": ...
        def correlation_morphism(self) -> ModuleMorphism: ...

    class FormedElement(Protocol):
        r"""What an element of a formed module offers."""

        def parent(self) -> Parent: ...
        def forget_form(self) -> "UnderlyingElement": ...
        def b(self, other: "Element") -> "Element": ...
        def span(self) -> "Subobject": ...
        def _coordinates(self) -> "Vector": ...

    class UnderlyingElement(Protocol):
        r"""An element of the module a formed module is built on."""

        def parent(self) -> "Parent": ...
        def coefficients(self) -> dict: ...
        def underlying_set_element(self) -> "Element": ...
        def __add__(self, other: "UnderlyingElement") -> "UnderlyingElement": ...
        def __sub__(self, other: "UnderlyingElement") -> "UnderlyingElement": ...
        def __neg__(self) -> "UnderlyingElement": ...
        def __rmul__(self, factor: "Element") -> "UnderlyingElement": ...


def _finite_rank(module_generating_set: TotallyOrderedFiniteSet) -> Integer:
    size = module_generating_set.cardinality()
    if isinstance(size, Cardinal):
        assert size.is_finite(), "a finitely generated form module has finite rank"
        rank: Integer = size.finite_value()
        return rank
    return Integer(size)


class FormModules(OwnedCategoryOverBaseRing):
    r"""Modules over \(R\) equipped with a form."""

    @staticmethod
    def __classcall_private__(
        cls: type["FormModules"],
        base_ring: "Ring | None" = None,
    ) -> "FormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        category: FormModules = super().__classcall__(
            cls, SageZZ if base_ring is None else engine_ring(base_ring)
        )
        return category

    @classmethod
    def _repr_object_names(cls) -> str:
        return "form modules"

    def super_categories(self) -> list:
        r"""A formed module is a module with a form.  It need not be framed.

        A framing is what a *presentation* of the form needs -- a Gram matrix
        is written against chosen generators -- and ``forms.sage`` says so
        itself: an unframed module states its pairing on \(U(M)\times U(M)\)
        instead, which by the universal property of the tensor product is the
        same datum.  Requiring a framing here made that unreachable, because
        ``_is_framed`` asks category *membership*, so a formed module was
        reported framed and then asked for a framing datum it had never been
        given.  Modules that do carry one are placed in the framed nodes by
        their own constructors and keep everything they had.
        """
        from dzack_research.preamble.categories.modules.pure.modules import (
            Modules as OwnedModules,
        )

        return [OwnedModules(self.base_ring())]

    class ParentMethods(OwnedBaseRing):
        r"""One formed module: the module, and the form morphism on it."""

        def __init__(
            self: Self,
            form: "Form",
            **rest: "ConstructionData",
        ) -> None:
            r"""Equip the module ``form`` is defined on with that form.

            The form is this level's datum.  In the bilinear case it lives in
            $\operatorname{Hom}_R(M\otimes_R M, W)$ for the value module $W$.
            It is a map, not a matrix; a Gram matrix is what a *finitely
            generated* one can be written as.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.forms.forms import BilinearFormMorphism
            from dzack_research.preamble.categories.forms.forms import QuadraticFormMorphism
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import framing_morphism
            match form:
                case BilinearFormMorphism() | QuadraticFormMorphism():
                    pass
                case _:
                    assert False, (
                        "a formed module requires a bilinear or quadratic "
                        "form morphism"
                    )
            module = form.module()
            self._form = form
            self._module = module
            super().__init__(base=module.base_ring(), **rest)
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

        def _form_morphism(self: "FormedParent") -> "Form":
            r"""Return the morphism this object's form *is*.

            A construction that reaches this category another way -- a ring
            equipped as its own rank-one lattice, a subobject -- states its
            own form here.
            """
            return self._form

        def form(self: "FormedParent") -> "Form":
            r"""Return the form morphism classifying this object."""
            return self._form_morphism()

        def forget_form(self: "FormedParent") -> "Module":
            r"""Return the underlying module, forgetting the form."""
            return self._module

        def twist(self: "FormedParent", scalar: "RingElement") -> Parent:
            r"""Return $M(s)$: the same underlying module, the form rescaled by ``scalar``.

            The general notion, stated where any formed module can answer it:
            rescaling the classifying form morphism by a scalar of the value
            module's ring of operators.  Negation, $-q$ via ``twist(-1)``, is
            the case MM09's negation rules classify (Zotero ACX7WF7L).
            Refinements whose objects carry more construction data -- lattices,
            discriminant forms -- restate this with their own constructors so
            the twist stays in its category.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.forms.forms import BilinearForms, QuadraticForms
            from dzack_research.preamble.categories.forms.forms import QuadraticFormMorphism
            morphism = self._form_morphism()
            match morphism:
                case QuadraticFormMorphism():
                    # The lift is what records a quadratic form, and
                    # ``lift_form`` is where it is read off.
                    rescaled = QuadraticForms(
                        morphism.module(), morphism.value_module()
                    )(scalar * morphism.lift_form().gram_matrix())
                case _:
                    rescaled = BilinearForms(
                        morphism.module(), morphism.value_module()
                    )(scalar * morphism.gram_matrix())
            return FormModule(rescaled)

        def framing_morphism(self: "FormedParent") -> "FramingMorphism":
            r"""Return the framing \(F_R(S)\to M\)."""
            return self._framing_morphism

        def value_module(self: "FormedParent") -> "Module":
            return self.form().value_module()

        def gram_matrix(self: "FormedParent") -> GramMatrix:
            return self.form().gram_matrix()

        def gram_tensor(self: "FormedParent") -> "TensorElement":
            r"""Return the form as a type-$(0,2)$ tensor.

            What the Gram matrix *is*: twice covariant, because the form eats
            two vectors.  The matrix is its components in this module's
            framing, so this reads them off rather than computing anything
            new -- and a reader who wants the valence gets it from the object
            instead of from a convention about which index is which.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.tensors import tensor

            gram_tensor: "TensorElement" = tensor(
                self.base_ring(),
                [list(row) for row in self.gram_matrix().rows()],
                valence=(0, 2),
                module=self.forget_form(),
            )
            return gram_tensor

        def raise_index(
            self: "FormedParent",
            tensor: "TensorElement",
            slot: Integer = 0,
        ) -> "TensorElement":
            r"""Raise one lower index using this form."""
            return tensor.raise_index(self, slot)

        def raise_index_over_fraction_field(
            self: "FormedParent",
            tensor: "TensorElement",
            slot: Integer = 0,
        ) -> "TensorElement":
            r"""Raise one lower index after extension to the fraction field."""
            changed_form = self.vector_space()
            changed_tensor = tensor.base_changed(changed_form.forget_form())
            return changed_form.raise_index(changed_tensor, slot)

        def lower_index(
            self: "FormedParent",
            tensor: "TensorElement",
            slot: Integer = 0,
        ) -> "TensorElement":
            r"""Lower one upper index using this form."""
            return tensor.lower_index(self, slot)

        def is_torsion_free(self: "FormedParent") -> bool:
            return bool(self.forget_form().is_torsion_free())

        def is_torsion(self: "FormedParent") -> bool:
            return bool(self.forget_form().is_torsion())

        def Hom(
            self: Self,
            codomain: "Module",
            category: "Category | None" = None,
        ) -> "FormHomset | Homset":
            # The union is the honest return: the formed branch builds a
            # FormHomset (its ends are the FormedParent protocol, not a
            # nominal Parent), the fallback delegates to Parent.Hom.
            if codomain in FormModules(self.base_ring()):
                cache: dict["Module", "FormHomset"] = self.__dict__.setdefault(
                    "_form_module_homsets", {}
                )
                homset = cache.get(codomain)
                if homset is None:
                    homset = FormHomset(
                        self,
                        codomain,
                        FormModules(self.base_ring()),
                    )
                    cache[codomain] = homset
                return homset
            plain_homset: "Homset" = Parent.Hom(self, codomain, category)
            return plain_homset

        def Aut(self: "FormedParent") -> "FormAutomorphismGroup":
            r"""Return $\operatorname{Aut}(M)$, the form-preserving units of
            $\operatorname{End}(M)$.

            Sited beside ``Hom``, on the general formed node, for the same
            reason: a lattice's $\operatorname{Aut}$ is $O(L)$ and belongs in
            the isometry node, and a refinement only reaches its own
            statement first when it is a subcategory of the one the general
            statement sits on.  On a node incomparable with the lattice
            categories -- finite free formed modules, say -- it would shadow
            them instead, leaving the join's linearization to decide which
            $\operatorname{Aut}$ a lattice answers.

            The group is built from a finite framing, which
            ``FormAutomorphismGroup`` asserts: a formed module without one
            has the operation named here and its hypothesis stated there.
            """
            cached = self.__dict__.get("_preamble_Aut")
            if cached is None:
                cached = FormAutomorphismGroup(self)
                self._preamble_Aut = cached
            return cached

        def hom(
            self: "FormedParent",
            images: "GeneratorAssignment",
            codomain: "Module | None" = None,
        ) -> "FormMorphism":
            assignment: "GeneratorAssignment"
            match images:
                case SetMorphism():
                    assert isinstance(images.codomain(), UnderlyingSets.ParentMethods), (
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
            morphism = self.Hom(target)(assignment)
            assert isinstance(morphism, FormMorphism), (
                f"{target} is a formed module, so its homset builds form "
                f"morphisms; got {morphism}"
            )
            return morphism

        def _refine_from_form(self: Self) -> None:
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.forms.forms import BilinearFormMorphism
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import FinitelyGeneratedFreeModules
            from dzack_research.preamble.categories.modules.pure.finitely_generated.finitely_generated_modules import FinitelyGeneratedModules
            from dzack_research.preamble.categories.modules.pure.free_modules import FreeModules
            from dzack_research.preamble.categories.modules.group_modules.group_lattices import GroupLattices
            from dzack_research.preamble.categories.forms.forms import QuadraticFormMorphism
            from dzack_research.preamble.categories.modules.pure.torsion_modules import TorsionModules
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import TorsionModulesWithForm
            from dzack_research.preamble.categories.modules.group_modules.group_lattices import _action_preserves_form
            from dzack_research.preamble.categories.modules.group_modules.group_lattices import _install_group_lattice_structure
            from dzack_research.preamble.categories.modules.group_modules.group_modules import _is_group_module
            from dzack_research.preamble.categories.rings.rings import engine_ring
            from dzack_research.preamble.refine import refine
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import refine_one_lattice
            module = self._module
            # Equipping a module with a form leaves its elements alone, so the
            # underlying set -- and every placement that set determines -- is the
            # module's own.
            refine(self, placement_of(module))
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
                    _is_group_module(module)
                    and _action_preserves_form(self)
                ):
                    refine(self, GroupLattices(module.group()))
                    _install_group_lattice_structure(self)

        def _element_constructor_(self: Self, element: "ElementConstructorInput") -> "Element":
            assert isinstance(element, Element) and element.parent() is self, (
                f"{element} is not an element of {self}"
            )
            return element

        def __contains__(self: Self, element: "MembershipInput") -> bool:
            # ``in`` is asked of an arbitrary value: the question membership
            # answers is whether that value is one of ours.
            return isinstance(element, Element) and element.parent() is self

        def _over(self: Self, element: "UnderlyingElement") -> "Element":
            formed: "Element" = self.element_class(self, element)
            return formed

        def zero(self: Self) -> "Element":
            return self._over(self._module.zero())

        def _repr_(self: Self) -> str:
            return (
                f"{type(self._form).__name__} on {self._module} with values in "
                f"{self.value_module()}"
            )

    class ElementMethods:
        r"""An element of a formed module, and its image after forgetting the form."""

        def __init__(
            self: Self,
            parent: Parent,
            element: "UnderlyingElement",
            **rest: "ConstructionData",
        ) -> None:
            assert element.parent() is parent.forget_form(), (
                f"{element} is not an element of {parent.forget_form()}"
            )
            self._underlying = element
            super().__init__(parent, **rest)

        def forget_form(self: Self) -> "UnderlyingElement":
            return self._underlying

        def coefficients(self: Self) -> dict["Element", "RingElement"]:
            return dict(self._underlying.coefficients())

        def _add_(self: Self, other: Self) -> "Element":
            return self.parent()._over(self._underlying + other._underlying)

        def _sub_(self: Self, other: Self) -> "Element":
            return self.parent()._over(self._underlying - other._underlying)

        def _neg_(self: Self) -> "Element":
            return self.parent()._over(-self._underlying)

        def _lmul_(self: Self, factor: "RingElement") -> "Element":
            return self.parent()._over(factor * self._underlying)

        _rmul_ = _lmul_

        def _richcmp_(self: Self, other: Self, op: int) -> bool:
            return bool(richcmp(self._underlying, other._underlying, op))

        def __hash__(self: Self) -> int:
            return hash((id(self.parent()), self._underlying))

        def _repr_(self: Self) -> str:
            return repr(self._underlying)

        def _coordinates(self: "FormedElement") -> "Vector":
            coordinates: "Vector" = self.forget_form()._coordinates()
            return coordinates

        def b(self: "FormedElement", other: "Element") -> "Element":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.forms.forms import _forget_form_element
            assert other.parent() is self.parent(), (
                "a form pairs two elements of one formed module"
            )
            value: "Element" = self.parent().form().b(
                _forget_form_element(self),
                _forget_form_element(other),
            )
            return value

        def norm(self: "FormedElement") -> "Element":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.forms.forms import _forget_form_element
            value: "Element" = self.parent().form().norm(
                _forget_form_element(self)
            )
            return value

        def is_isotropic(self: "FormedElement") -> bool:
            r"""Return whether the norm of $x$ is $0$ in the value module.

            The norm is the form's own: $b(x,x)$ for a bilinear form and
            $q(x)$ for a quadratic one, which differ exactly where isotropy
            definitions differ (characteristic $2$), so asking the form's
            norm asks the right question in both.  Isotropy of a *subobject*
            is a different statement -- the form vanishing on all of
            $S\times S$ -- and is asked of the subobject, not of a spanning
            element.
            """
            return bool(self.norm().is_zero())

        def is_orthogonal_to(self: "FormedElement", other: "Element") -> bool:
            r"""Return whether $b(x,y)=0$ in the value module.

            Left orthogonality: $x$ in the first argument, ``other`` in the
            second.  For a form that is not symmetric this relation is not
            symmetric -- $b(x,y)=0$ says nothing about $b(y,x)$ -- so the
            method states its argument order and a caller who means the
            two-sided relation asks both ways.
            """
            return bool(self.b(other).is_zero())

        def represents(self: "FormedElement", value: "Element") -> bool:
            r"""Return whether the norm of $x$ equals ``value`` in the value module.

            The statement about one element, on the form's own norm --
            $b(x,x)$ for a bilinear form, $q(x)$ for a quadratic one.
            Whether the *module* represents a value -- $\exists x$ of norm
            $k$ -- is an existence question over an infinite set and lives
            where it is decidable: on definite lattices
            ``vectors_of_square`` answers it, and the indefinite case is the
            stated adelic gap recorded there.
            """
            return bool(self.norm() == self.parent().value_module()(value))

        def span(self: "FormedElement") -> "Subobject":
            return self.parent().subobject_on([self])

        def isotropic_reduction(self: "FormedElement") -> "Module":
            return self.span().isotropic_reduction()

        def __mul__(self: "FormedElement", other: "Element | RingElement") -> "Element":
            match other:
                case Element() if other.parent() is self.parent():
                    return self.b(other)
                case scalar if scalar in self.parent().base_ring():
                    return self.parent()._over(scalar * self.forget_form())
                case _:
                    assert False, (
                        f"{other} is neither an element of {self.parent()} nor "
                        f"a scalar of {self.parent().base_ring()}"
                    )

        def __truediv__(self: "FormedElement", divisor: "RingElement") -> "Element":
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
            quotient: "Element" = zipsum(
            tuple(coefficient_ring(entry) for entry in coordinates),
            self.parent().module_generators(),
            self.parent().zero(),
            )
            return quotient


class BilinearFormModules(OwnedCategoryOverBaseRing):
    r"""Modules whose form is bilinear."""

    @staticmethod
    def __classcall_private__(
        cls: type["BilinearFormModules"],
        base_ring: "Ring | None" = None,
    ) -> "BilinearFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        category: BilinearFormModules = super().__classcall__(
            cls, SageZZ if base_ring is None else engine_ring(base_ring)
        )
        return category

    @classmethod
    def _repr_object_names(cls) -> str:
        return "modules with a bilinear form"

    def super_categories(self) -> list:
        return [FormModules(self.base_ring())]


class SymmetricBilinearFormModules(OwnedCategoryOverBaseRing):
    r"""Modules equipped with a symmetric bilinear form."""

    @staticmethod
    def __classcall_private__(
        cls: type["SymmetricBilinearFormModules"],
        base_ring: "Ring | None" = None,
    ) -> "SymmetricBilinearFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        category: SymmetricBilinearFormModules = super().__classcall__(
            cls, SageZZ if base_ring is None else engine_ring(base_ring)
        )
        return category

    @classmethod
    def _repr_object_names(cls) -> str:
        return "modules with a symmetric bilinear form"

    def super_categories(self) -> list:
        return [BilinearFormModules(self.base_ring())]


class QuadraticFormModules(OwnedCategoryOverBaseRing):
    r"""Modules whose form is quadratic."""

    @staticmethod
    def __classcall_private__(
        cls: type["QuadraticFormModules"],
        base_ring: "Ring | None" = None,
    ) -> "QuadraticFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        category: QuadraticFormModules = super().__classcall__(
            cls, SageZZ if base_ring is None else engine_ring(base_ring)
        )
        return category

    @classmethod
    def _repr_object_names(cls) -> str:
        return "modules with a quadratic form"

    def super_categories(self) -> list:
        return [FormModules(self.base_ring())]


class FreeFormModules(OwnedCategoryOverBaseRing):
    r"""Form modules whose image after forgetting the form is free."""

    @staticmethod
    def __classcall_private__(
        cls: type["FreeFormModules"],
        base_ring: "Ring | None" = None,
    ) -> "FreeFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        category: FreeFormModules = super().__classcall__(
            cls, SageZZ if base_ring is None else engine_ring(base_ring)
        )
        return category

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

        def rank(self: "FormedParent") -> "Cardinal":
            rank: "Cardinal" = self.forget_form().rank()
            return rank

        def subobject_on(
            self: "FormedParent",
            module_generators: "OrderedSet",
        ) -> "Subobject":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _independent_module_generators
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set
            module_generators = tuple(module_generators)
            assert all(generator in self for generator in module_generators), (
                "a subobject is generated by elements of this formed module"
            )
            module_generators = _independent_module_generators(self, module_generators)
            gram = matrix(
                [[left.b(right) for right in module_generators] for left in module_generators]
            )
            labels = finite_ordered_set(tuple(module_generators))
            sub = self._sub_form_module(gram, labels)
            images = {generator: generator for generator in labels}
            return Subobject(
                FormHomset(
                    sub,
                    self,
                    FormModules(self.base_ring()),
                )(images)
            )

        def _sub_form_module(
            self: "FormedParent",
            gram: Matrix,
            module_generating_set: "OrderedSet",
        ) -> Parent:
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
            from dzack_research.preamble.categories.forms.forms import BilinearForm
            module = BasedFreeModule(
                self.base_ring(),
                module_generating_set,
            )
            # ``BilinearForm`` builds the formed module the form classifies.
            sub_form_module: Parent = BilinearForm(
                module, self.value_module(), gram
            )
            return sub_form_module

    class ElementMethods:
        def underlying_set_element(self: "FormedElement") -> "Element":
            r"""Recover the element of \(S\) defining a canonical generator."""
            label: "Element" = self.forget_form().underlying_set_element()
            return label


class FinitelyGeneratedFormModules(OwnedCategoryOverBaseRing):
    r"""Form modules whose chosen framing set is finite."""

    @staticmethod
    def __classcall_private__(
        cls: type["FinitelyGeneratedFormModules"],
        base_ring: "Ring | None" = None,
    ) -> "FinitelyGeneratedFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        category: FinitelyGeneratedFormModules = super().__classcall__(
            cls, SageZZ if base_ring is None else engine_ring(base_ring)
        )
        return category

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

        def number_of_module_generators(self: "FormedParent") -> Integer:
            return _finite_rank(self.module_generating_set())

        def scale_submodule(self: "FormedParent") -> "Subobject":
            r"""Return $\mathfrak s(L)\subseteq W$: the image of the form.

            The construction is the same for every value module: $b$ is a
            morphism into $W$, and the scale is the $R$-submodule of $W$ it
            generates -- its image.  Nothing here assumes $W$ is a ring; a
            discriminant form's scale is a $\mathbb Z$-submodule of
            $\mathbb Q/\mathbb Z$, and $\mathbb Z\subset\mathbb Q$ is not an
            ideal of anything.

            One specialization is then a theorem, not the definition: when
            $W=R$ as a module over itself, its submodules *are* its ideals,
            and the image is the ideal generated by the Gram entries -- the
            classical scale $\mathfrak s(L)$ of O'Meara §82:8.  That case is
            presented as the native ideal.  Every other value module presents
            the image by its own subobject machinery.
            """
            value_module = self.value_module()
            if value_module is self.base_ring():
                # Specialization, derived: a submodule of R over R is an ideal.
                scale: "Subobject" = value_module.ideal(
                    [entry for row in self.gram_matrix().rows() for entry in row]
                )
                return scale
            return self.form().image()

        def is_integral(self: "FormedParent") -> bool:
            r"""Return whether the form's values are integral.

            Integrality has one a priori meaning: a ring morphism $R\to S$
            makes "integral over $R$" a property of elements of $S$.  A
            value *ring* $W$ is a $\mathbb Z$-algebra along
            $\mathbb Z\to W$, so the question is integrality over
            $\mathbb Z$ -- membership in $\mathcal O_K$ when $W$ is a
            number field, since $\mathcal O_K$ *is* the integral closure of
            $\mathbb Z$ there; and outright for a finite ring, whose every
            element satisfies the monic relation $x^n=x^m$.

            A value module with no ring structure -- $\mathbb Q/2\mathbb Z$,
            a framed module -- carries no such morphism, so nothing in it is
            integral over anything: the answer is ``False`` and the object
            routes past the ``Integral`` axiom.  Not an error, just a
            different category.
            """
            from sage.categories.rings import Rings

            value_module = self.value_module()
            if value_module not in Rings():
                return False
            if value_module.is_finite():
                return True
            return all(
                bool(entry.is_integral())
                for row in self.gram_matrix().rows()
                for entry in row
            )

        def hom(
            self: "FormedParent",
            images: "GeneratorAssignment | list | tuple",
            codomain: "Module | None" = None,
        ) -> "FormMorphism":
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
                    morphism = self.Hom(target)(assignment)
                    assert isinstance(morphism, FormMorphism), (
                        f"{target} is a formed module, so its homset builds "
                        f"form morphisms; got {morphism}"
                    )
                    return morphism
                case _:
                    assert False, (
                        "a homomorphism is specified by a finite assignment "
                        "or an ordered list of images"
                    )


class FinitelyGeneratedFreeFormModules(OwnedCategoryOverBaseRing):
    r"""Finite free modules equipped with a form."""

    @staticmethod
    def __classcall_private__(
        cls: type["FinitelyGeneratedFreeFormModules"],
        base_ring: "Ring | None" = None,
    ) -> "FinitelyGeneratedFreeFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        category: FinitelyGeneratedFreeFormModules = super().__classcall__(
            cls, SageZZ if base_ring is None else engine_ring(base_ring)
        )
        return category

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
        # ---- the radical, and the predicates the axioms gate on ----
        #
        # Sited here, on the finitely generated *free* formed surface, and
        # not inside any axiom category: the axioms' gates ask candidates
        # these questions, so a candidate must be able to answer before it
        # is admitted anywhere.  A degenerate form module answers
        # ``is_nondegenerate() == False`` from right here.

        @cached_method
        def dual_module(self: "FiniteFreeFormedParent") -> "Module":
            r"""Return $\operatorname{Hom}(L,R)$, free on the dual basis.

            The dual as a *module*, which every finite free module has:
            $\operatorname{Hom}$ into $R$ of a free module of rank $n$ is
            free of rank $n$, with no condition on the form.  It carries no
            form -- the one on $L^\vee$ is $G^{-1}$, and that is where
            nondegeneracy is needed.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule

            dual_module: "Module" = BasedFreeModule(
                self.base_ring(), self.module_generating_set()
            )
            return dual_module

        @cached_method
        def correlation_morphism(self: "FiniteFreeFormedParent") -> ModuleMorphism:
            r"""Return $c: L\to\operatorname{Hom}(L,R)$, $v\mapsto b(v,-)$.

            Always defined, and the map the radical and nondegeneracy are
            about: $b(v,-)$ is a functional on $L$ whatever the form does,
            and its matrix in the dual basis is $G$.  The domain is this
            module -- a formed module *is* a module, and $c$ leaves from it,
            not from some stored carrier.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
            from dzack_research.preamble.utilities import zipsum

            dual_module = self.dual_module()
            assignment = dict(
                zip(
                    self.module_generating_set(),
                    (
                        zipsum(
                            row,
                            dual_module.module_generators(),
                            dual_module.zero(),
                        )
                        for row in self.gram_matrix().rows()
                    ),
                )
            )
            homset = module_homset(self, dual_module)
            return homset.zero() if not assignment else homset(assignment)

        @cached_method
        def radical(self: "FiniteFreeFormedParent") -> "Subobject":
            r"""Return $\operatorname{rad}(L)=\ker(c)$, as a subobject.

            $\{v: b(v,w)=0 \text{ for all } w\}$ is by definition the set of
            $v$ killed by $v\mapsto b(v,-)$, so the radical is that map's
            kernel and is computed as one -- not as a Gram-matrix kernel that
            happens to agree with it.
            """
            return self.correlation_morphism().kernel()

        def radical_quotient(self: "FiniteFreeFormedParent") -> Parent:
            r"""Return $L/\operatorname{rad}(L)$ with the descended form.

            The radical is isotropic ($b$ vanishes on it by definition) and
            $\operatorname{rad}(L)^{\perp}=L$ (everything pairs to zero with
            the radical), so the nondegenerate quotient *is* the isotropic
            reduction $S^{\perp}/S$ of the radical subobject -- one owned
            construction, no second quotient machinery.
            """
            return self.radical().isotropic_reduction()

        def is_nondegenerate(self: "FiniteFreeFormedParent") -> bool:
            r"""Return whether $\operatorname{rad}(L)=0$, i.e. $c$ is injective.

            Asked of the correlation morphism itself: $\ker c=0$ *is*
            injectivity of $c$, so the question is decided on the arrow
            without constructing the kernel object.  That is what lets the
            axiom gate and lattice-birth routing ask it of every candidate
            -- including the radical's own submodule as it is built --
            without a construction asking for itself.  :meth:`radical`
            still constructs $\ker c$ as an honest subobject for whoever
            wants the object rather than the answer.
            """
            return bool(self.correlation_morphism().is_injective())


def FormModule(form: "Form") -> Parent:
    r"""Return the formed object one form morphism classifies."""
    return object_of(FormModules(form.module().base_ring()), form=form)


# ``Homset`` is generic in its morphism type; the runtime class is not
# subscriptable, so the binding goes through a TYPE_CHECKING-only alias.
# The ends bind to a phantom NOMINAL type: a form homset's ends really are
# Parents (the protocol alone is not, so it cannot sit under Parent.Hom's
# declared Homset return), and they carry the formed surface — stated once
# by inheriting the protocol.
if TYPE_CHECKING:

    class FormedModule(Parent, FormedParent):
        r"""A Parent that offers the formed surface (type-only)."""

    _FormHomsetBase = Homset["FormMorphism", "FormedModule", "FormedModule"]
else:
    _FormHomsetBase = Homset


class FormHomset(_FormHomsetBase):
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

    def _element_constructor_(self, images: "GeneratorAssignment | ModuleMorphism") -> "FormMorphism":
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

    def __contains__(self, morphism: "MembershipInput") -> bool:
        # ``in`` is asked of an arbitrary value.
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

    if TYPE_CHECKING:
        # Built only by ``FormHomset._element_constructor_``, so that homset
        # is the parent.
        def parent(self) -> FormHomset: ...

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
        generator_morphism: SetMorphism = self._module_morphism.module_generator_morphism()
        return generator_morphism

    def matrix(self) -> MorphismMatrix:
        return self._module_morphism.matrix()

    def _call_(self, element: "ElementConstructorInput") -> "Element":
        # Sage calls a morphism on an arbitrary value and lets the underlying
        # map decide; the parameter is unrestricted for that reason.
        image: "Element" = self._module_morphism(element)
        return image

    def lift(self, element: "Element") -> "ModuleElement":
        lifted: "ModuleElement" = self._module_morphism.lift(element)
        return lifted

    def kernel(self) -> "Subobject":
        return self._module_morphism.kernel()

    def cokernel(self) -> "FinitelyPresentedModule":
        return self._module_morphism.cokernel()

    def image(self) -> "Subobject":
        return self._module_morphism.image()

    def is_injective(self) -> bool:
        return bool(self._module_morphism.is_injective())

    def index(self) -> "Integer":
        index: "Integer" = self._module_morphism.index()
        return index

    def orthogonal_complement(self) -> "Subobject":
        return self._module_morphism.orthogonal_complement()

    def then(self, other: "FormMorphism") -> "FormMorphism":
        assert other.domain() is self.codomain(), (
            "the codomain of the first map is not the domain of the second"
        )
        module_generator_morphism = self.module_generator_morphism()
        composite: "FormMorphism" = self.domain().Hom(other.codomain())(
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
        return composite

    def __mul__(self, other: "ElementConstructorInput") -> "FormMorphism":
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

    def __eq__(self, other: "MembershipInput") -> bool:
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

    def _element_constructor_(
        self,
        images: "GeneratorAssignment | ModuleMorphism",
    ) -> FormMorphism:
        morphism = FormHomset._element_constructor_(self, images)
        determinant = morphism.matrix().det()
        assert determinant.is_unit(), (
            f"the determinant {determinant} is not a unit"
        )
        return morphism

    def one(self) -> FormMorphism:
        return self(self.domain().module_generator_morphism())

    def __contains__(self, morphism: "MembershipInput") -> bool:
        # ``in`` is asked of an arbitrary value.
        return (
            isinstance(morphism, FormMorphism)
            and morphism.parent() is self
        )


def correlation_of(lattice: Parent) -> FormMorphism:
    r"""Return \(c:L\to L^\vee\), \(v\mapsto b(v,-)\)."""
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.utilities import zipsum
    dual = lattice.dual_lattice()
    correlation = lattice.Hom(dual)(
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
    assert isinstance(correlation, FormMorphism), (
        f"{dual} is a formed module, so its homset builds form morphisms; "
        f"got {correlation}"
    )
    return correlation
