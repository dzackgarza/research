r"""Modules equipped with a bilinear or quadratic form."""


from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ as SageZZ
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.modules import Module
    from sage.structure.element import Vector
    from sage.structure.parent import ElementConstructorInput, MembershipInput

from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import FramingMorphism
from sage.matrix.matrix0 import Matrix
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
from dzack_research.preamble.categories.modules.framed.framed_modules import FramedModules
from sage.categories.category import Category as SageCategory
from sage.categories.modules import Modules
if TYPE_CHECKING:
    from sage.categories.category import Category
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
    from sage.rings.ring import Ring
    from sage.structure.element import RingElement

from dzack_research.preamble.categories.rings.rings import OwnedBaseRing
from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.owned_category import object_of
from typing import Protocol, Self, TYPE_CHECKING, TypeAlias

from sage.categories.homset import Hom
from sage.misc.cachefunc import cached_method
from sage.categories.morphism import Morphism, SetMorphism
from sage.rings.integer import Integer
from sage.structure.element import Element, ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp
from dzack_research.preamble.lexicon import GramMatrix
from dzack_research.preamble.categories.modules.pure.modules import Modules as OwnedModules

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
    # map) that a formed module is equipped with.  Not an element of
    # ``FormModules.Homsets``, which is a map *between* two formed modules.
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

        _framing_morphism: FramingMorphism

        def _form_morphism(self) -> "Form": ...
        def base_ring(self) -> "Ring": ...
        def form(self) -> "Form": ...
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

        def dual_module(self) -> "Module": ...
        def correlation_morphism(self) -> ModuleMorphism: ...

    class FormedElement(Protocol):
        r"""What an element of a formed module offers."""

        def parent(self) -> Parent: ...
        def underlying_element(self) -> "UnderlyingElement": ...
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


class FormModules(OwnedCategoryOverBaseRing):
    r"""Modules over \(R\) equipped with a form."""

    @staticmethod
    def __classcall_private__(
        cls: type["FormModules"],
        base_ring: "Ring",
    ) -> "FormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        category: FormModules = super().__classcall__(cls, engine_ring(base_ring))
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
            super().__init__(**rest)
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
                        morphism.domain(), morphism.codomain()
                    )(scalar * morphism.lift_form().gram_matrix())
                case _:
                    rescaled = BilinearForms(
                        morphism.domain(), morphism.codomain()
                    )(scalar * morphism.gram_matrix())
            return FormModule(rescaled)

        def framing_morphism(self: "FormedParent") -> "FramingMorphism":
            r"""Return the framing \(F_R(S)\to M\)."""
            return self._framing_morphism

        def value_module(self: "FormedParent") -> "Module":
            return self.form().codomain()

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
                module=self,
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
            changed_tensor = tensor.base_changed(changed_form)
            return changed_form.raise_index(changed_tensor, slot)

        def lower_index(
            self: "FormedParent",
            tensor: "TensorElement",
            slot: Integer = 0,
        ) -> "TensorElement":
            r"""Lower one upper index using this form."""
            return tensor.lower_index(self, slot)

        def _Hom_(
            self: Self,
            codomain: "Module",
            category: "Category | None" = None,
        ) -> Parent:
            r"""Return the form-preserving homset, or Sage's for a plain codomain.

            Built by ``Hom(X, Y, C)`` with ``C`` the category of the
            *objects*, which is the constructor of every owned homset: Sage's
            ``Homset.__init__`` is what places the result in ``C.Homsets()``
            or ``C.Endsets()``, so handing it ``C.Homsets()`` would place the
            homset in the homsets of the homsets and its morphisms would
            never reach ``FormModules.Homsets.ElementMethods``.
            """
            if category is None and codomain in FormModules(self.base_ring()):
                category = FormModules(self.base_ring())
            homset: Parent = super()._Hom_(codomain, category)
            return homset

        def Aut(self: "FormedParent") -> Parent:
            r"""Return $\operatorname{Aut}(M)$ when its endset category proves it.

            A general form-preserving endomorphism need not be invertible.
            A narrower category can identify its endset with its automorphism
            group only after its hypotheses prove that every such endomorphism
            is a unit.  Integral nondegenerate lattices do this in their endset;
            discriminant forms construct their finite orthogonal groups
            separately.
            """
            # Local: importing the group node here would close a cycle, and a
            # specialised endset is built by the time automorphisms are asked for.
            from dzack_research.preamble.categories.group.groups import OwnedGroups

            endomorphisms = self.Hom(self)
            assert endomorphisms in OwnedGroups(), (
                "Aut(M) requires a category whose endset consists exactly of "
                "invertible form-preserving endomorphisms"
            )
            return endomorphisms

        def hom(
            self: "FormedParent",
            images: "GeneratorAssignment",
            codomain: "Module | None" = None,
        ) -> "Morphism":
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
                    target = (
                        codomain
                        if codomain is not None
                        else next(iter(images.values())).parent()
                    )
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
            assert is_form_morphism(morphism), (
                f"{target} is a formed module, so its homset builds form "
                f"morphisms; got {morphism}"
            )
            return morphism

        def _refine_from_form(self: Self) -> None:
            r"""Place this object in the subcategories its form puts it in.

            Called once the construction has returned, never from inside it.
            Which subcategories a formed module belongs to is read off the
            form -- bilinear or quadratic, symmetric, free, torsion, integral
            -- so it is a consequence of the datum rather than a step in
            establishing it.  It is also the only order Sage's identity
            caching admits: ``UniqueRepresentation.__classcall__`` requires
            the object it caches to still be an instance of the class it
            asked for, and refinement rebuilds that class.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.forms.forms import BilinearFormMorphism
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import FinitelyGeneratedFreeModules
            from dzack_research.preamble.categories.modules.pure.finitely_generated.finitely_generated_modules import FinitelyGeneratedModules
            from dzack_research.preamble.categories.modules.pure.free_modules import FreeModules
            from dzack_research.preamble.categories.modules.group_modules.group_lattices import GroupLattices
            from dzack_research.preamble.categories.forms.forms import QuadraticFormMorphism
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModules
            from dzack_research.preamble.categories.modules.pure.torsion_modules import TorsionModules
            from dzack_research.preamble.categories.modules.framed.formed.torsionform.torsion_modules_with_form import TorsionModulesWithForm
            from dzack_research.preamble.categories.modules.group_modules.group_lattices import _action_preserves_form
            from dzack_research.preamble.categories.modules.group_modules.group_modules import _is_group_module
            from dzack_research.preamble.categories.rings.rings import engine_ring
            from dzack_research.preamble.refine import refine
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import refine_one_lattice
            module = self
            base_ring = module.base_ring()
            free = module in FreeModules(base_ring)
            finitely_generated = module in FinitelyGeneratedModules(base_ring)
            zero = finitely_generated and module.is_zero()
            torsion = (
                module in TorsionModules(base_ring)
                or zero
            )
            finite_torsion = torsion and finitely_generated
            # ``TorsionModulesWithForm`` sits under the finitely *presented*
            # torsion modules, which consume a chosen presentation.  Being
            # torsion does not supply one: the zero module is torsion and is
            # built free, framed by the empty set and presented by nothing, so
            # admitting it there would place an object in a category whose
            # defining datum it does not have.  It is refined into the torsion
            # property category below instead.
            presented_finite_torsion = (
                finite_torsion
                and engine_ring(base_ring) is SageZZ
                and module in FinitelyPresentedModules(base_ring)
            )
            bilinear = isinstance(self._form, BilinearFormMorphism)
            quadratic = isinstance(self._form, QuadraticFormMorphism)
            symmetric_bilinear = (
                bilinear
                and self._form.gram_matrix().is_symmetric()
            )
            match (bilinear, quadratic, free, presented_finite_torsion):
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
            match (torsion, presented_finite_torsion):
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
                and engine_ring(self._form.codomain()) is SageZZ
            ):
                refine_one_lattice(self)
                if (
                    _is_group_module(module)
                    and _action_preserves_form(self)
                ):
                    refine(self, GroupLattices(module.group()))

        def _over(self: Self, element: "UnderlyingElement") -> "Element":
            r"""Return this module's element reading ``element``'s coordinates.

            \(M\) and this module are the free module on one framing set over
            one ring: equipping \(M\)'s form built a second object of that
            category, and the isomorphism between the two is the identity on
            the framing, hence the identity on coordinates.  Nothing is
            wrapped -- the element is this module's own, made the way this
            module makes elements.
            """
            formed: "Element" = self._from_coordinates(element._coordinates())
            return formed

        def _repr_(self: Self) -> str:
            return (
                f"{type(self._form).__name__} on the module with values in "
                f"{self.value_module()}"
            )

    class ElementMethods:
        r"""An element of a formed module: the form is on the parent.

        A formed module *is* a module, so its elements are that module's own
        and this level adds no datum to them.  Addition, negation, scaling,
        comparison, coordinates and coefficients are all answered by the
        module level the formed module is constructed through; what is
        declared here is what the *form* gives an element -- its norm, the
        pairing with another element, the subobject it spans.
        """

        def underlying_element(self: Self) -> "UnderlyingElement":
            r"""Return this element read in the module the form is written on.

            The action on elements of the functor forgetting the form.  The
            two modules are framed by one set, so the arrow is the identity
            on coordinates; what changes is which parent the element answers
            to, and the form is a morphism out of \(M\), so it is evaluated
            on \(M\)'s elements.
            """
            module: "Module" = self.parent().form().module()
            underlying: "UnderlyingElement" = module._from_coordinates(
                self._coordinates()
            )
            return underlying

        def b(self: "FormedElement", other: "Element") -> "Element":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.forms.forms import QuadraticFormMorphism
            from dzack_research.preamble.categories.forms.forms import _underlying_element
            assert other.parent() is self.parent(), (
                "a form pairs two elements of one formed module"
            )
            form = self.parent().form()
            if isinstance(form, QuadraticFormMorphism):
                value: "Element" = form.b(
                    _underlying_element(self),
                    _underlying_element(other),
                )
                return value
            value = form(_underlying_element(self), _underlying_element(other))
            return value

        def norm(self: "FormedElement") -> "Element":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.forms.forms import QuadraticFormMorphism
            from dzack_research.preamble.categories.forms.forms import _underlying_element
            form = self.parent().form()
            underlying = _underlying_element(self)
            if isinstance(form, QuadraticFormMorphism):
                value: "Element" = form(underlying)
                return value
            value = form.norm(underlying)
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
                    return self._lmul_(scalar)
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


    class Homsets(OwnedModules.Homsets):
        r"""The form-preserving maps between two formed modules.

        The homset is the parent and the morphism is its element, so this is
        where both live.  The level below is the owned ``Sets().Homsets()``,
        which supplies Sage's ``Homset`` and ``Morphism``; nothing here names
        a base.
        """

        class ParentMethods:
            r"""$\operatorname{Hom}(M, N)$ of two modules with a form."""

            def __init__(
                self,
                domain: "Module",
                codomain: "Module",
                **rest: "ConstructionData",
            ) -> None:
                assert domain.base_ring() == codomain.base_ring(), (
                    "form morphisms require the same module base ring"
                )
                super().__init__(
                    domain=domain,
                    codomain=codomain,
                    **rest,
                )
            def _element_constructor_(
                self, images: "GeneratorAssignment | ModuleMorphism"
            ) -> "Morphism":
                # Local: a module-level import here would close a cycle; by call time this module is built.
                from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

                if isinstance(images, list | tuple):
                    assert len(images) == self.domain().number_of_module_generators(), (
                        "the number of images does not match the domain framing"
                    )
                    images = dict(
                        zip(self.domain().module_generating_set(), images)
                    )
                module_homset_for_forms = module_homset(self.domain(), self.codomain())
                match images:
                    case Morphism():
                        module_morphism = images
                        assert module_morphism.parent() is module_homset_for_forms, (
                            "the module morphism belongs to a different homset"
                        )
                    case SetMorphism() | dict():
                        module_morphism = module_homset_for_forms(images)
                    case _ if callable(images):
                        module_morphism = module_homset_for_forms(images)
                    case _:
                        assert False, (
                            "a form morphism is specified by its generator morphism"
                        )
                morphism: "Morphism" = self.element_class(self, module_morphism)
                return morphism

            def _repr_(self) -> str:
                return (
                    f"Form-preserving morphisms from {self.domain()} to "
                    f"{self.codomain()}"
                )

        class ElementMethods:
            r"""A morphism whose underlying module map preserves the form."""

            def __init__(
                self,
                parent: Parent,
                module_morphism: ModuleMorphism,
            ) -> None:
                super().__init__(parent)
                self._generator_morphism = (
                    module_morphism.module_generator_morphism()
                )
                # $f$ preserves the form when $f^*b_N = b_M$, which is an
                # equation between two forms *on one module*.  The pullback is
                # written on the morphism's domain; the domain's own form is
                # written on the module the form classifies, one level of
                # enrichment below.  So the domain's form is read on the
                # module the pullback lives on before the two are compared.
                pulled_back = parent.codomain().form().pullback(module_morphism)
                expected_form = parent.domain().form().on_module(
                    pulled_back.module()
                )
                if pulled_back.codomain() is not expected_form.codomain():
                    pulled_back = pulled_back.reduced(expected_form.codomain())
                assert expected_form == pulled_back, (
                    "the module morphism does not preserve the stated form"
                )

            def _domain_module_generating_set(self) -> "OrderedSet":
                return self.domain().module_generating_set()

            def module_generator_morphism(self) -> SetMorphism:
                return self._generator_morphism

            def orthogonal_complement(self) -> "Subobject":
                from dzack_research.preamble.utilities import zipsum

                codomain = self.codomain()
                assert not codomain.is_torsion(), (
                    "orthogonal complement is defined here in a free codomain"
                )
                gram = codomain.gram_matrix()
                pairing = (
                    gram
                    * self.matrix().transpose()
                )
                return codomain.subobject_on(
                    [
                        zipsum(
                            row,
                            codomain.module_generators(),
                            codomain.zero(),
                        )
                        for row in pairing.left_kernel_matrix().rows()
                    ]
                )

            def then(self, other: "Morphism") -> "Morphism":
                assert other.domain() is self.codomain(), (
                    "the codomain of the first map is not the domain of the second"
                )
                module_generator_morphism = self.module_generator_morphism()
                composite: "Morphism" = self.domain().Hom(other.codomain())(
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

            def __mul__(self, other: "ElementConstructorInput") -> "Morphism":
                assert (
                    isinstance(other, Morphism)
                    and other.parent() is self.parent()
                ), "composition here is internal to one endomorphism homset"
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

            def _repr_type(self) -> str:
                return "Form"

class BilinearFormModules(OwnedCategoryOverBaseRing):
    r"""Modules whose form is bilinear."""

    @staticmethod
    def __classcall_private__(
        cls: type["BilinearFormModules"],
        base_ring: "Ring",
    ) -> "BilinearFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        category: BilinearFormModules = super().__classcall__(cls, engine_ring(base_ring))
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
        base_ring: "Ring",
    ) -> "SymmetricBilinearFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        category: SymmetricBilinearFormModules = super().__classcall__(
            cls, engine_ring(base_ring)
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
        base_ring: "Ring",
    ) -> "QuadraticFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        category: QuadraticFormModules = super().__classcall__(cls, engine_ring(base_ring))
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
        base_ring: "Ring",
    ) -> "FreeFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        category: FreeFormModules = super().__classcall__(cls, engine_ring(base_ring))
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
            return Subobject(sub.Hom(self)(images))

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
            label: "Element" = self.underlying_element().underlying_set_element()
            return label


class FinitelyGeneratedFormModules(OwnedCategoryOverBaseRing):
    r"""Form modules whose chosen framing set is finite."""

    @staticmethod
    def __classcall_private__(
        cls: type["FinitelyGeneratedFormModules"],
        base_ring: "Ring",
    ) -> "FinitelyGeneratedFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        category: FinitelyGeneratedFormModules = super().__classcall__(
            cls, engine_ring(base_ring)
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
        ) -> "Morphism":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.framed_modules import _finite_module_generator_assignment
            match images:
                case dict():
                    return super().hom(images, codomain)
                case list() | tuple():
                    target, assignment = _finite_module_generator_assignment(
                        self,
                        images,
                        codomain,
                    )
                    morphism = self.Hom(target)(assignment)
                    assert is_form_morphism(morphism), (
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
        base_ring: "Ring",
    ) -> "FinitelyGeneratedFreeFormModules":
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        category: FinitelyGeneratedFreeFormModules = super().__classcall__(
            cls, engine_ring(base_ring)
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
    r"""Return the formed object one form morphism classifies.

    The form is the datum, and \(M\) is recovered from it: the form's domain
    is \(T^2M\) or \(\Lambda^2M\), so the module it is written on is
    ``form.domain()``. Nothing passes \(M\) alongside the form, which could
    only disagree with it.

    The object is built in \(M\)'s own category enriched by the form, so it
    **is** a module rather than one that holds a module.  A framed \(M\)
    hands its framing set up as the module level's datum; an unframed one has
    none to hand, which is what ``FormModules`` means by not requiring a
    framing.

    \(M\)'s *structure* is what is inherited, not \(M\)'s arrows.  A module
    that is a subobject, a kernel or a graded piece of something is placed in
    a slice category by that arrow, and the formed module has no such arrow:
    it is a new object, and the only morphism it comes with is the form.  So
    the arrows are forgotten.  Ordinary category construction preserves the
    framing, freeness, finite generation, and underlying-set construction.
    """
    # Local: the slice family reaches this module through the subobject
    # constructor, so a module-level import here would close that cycle.
    from dzack_research.preamble.categories.abstract_categories.slice_categories import (
        with_chosen_arrows_forgotten,
    )

    module = form.module()
    category = SageCategory.join(
        [
            with_chosen_arrows_forgotten(module.category()),
            FormModules(module.base_ring()),
        ]
    )
    # The formed object is built in \(M\)'s categories, so it is built from
    # \(M\)'s data: the levels of that chain declare exactly one datum each,
    # and a presented module is presented by its own presentation while a
    # framed one is framed by its own framing set.
    # Local: the presented and group nodes reach this module, so a module-level
    # import here would close that cycle; both are built by the time a form is
    # equipped.
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModules
    from dzack_research.preamble.categories.modules.framed.framed_modules import FramedModules
    from dzack_research.preamble.categories.modules.group_modules.group_modules import GroupModules

    # One datum per level, and the highest level that declares one supplies
    # what the levels under it need.  A group module supplies its action and
    # framing.  The new object is then built through the same module chain.
    # $R[G]$-Mod is named by its group, and only a module carrying an action
    # can say which group that is, so the module is asked for it first.
    # Being a $G$-module is category membership, so it is read off the
    # categories the module is in.  Asked by attribute instead, the question
    # was whether the name ``group`` resolves -- which any object may answer
    # for reasons of its own, and which no longer names the group when the
    # module carries the action without exposing it.
    group_module_category = next(
        (member for member in module.categories() if isinstance(member, GroupModules)),
        None,
    )
    data: dict[str, "ConstructionData"] = {"form": form}
    if group_module_category is not None:
        data["action"] = module.action()
        data["module_generating_set"] = module.module_generating_set()
    elif module in FinitelyPresentedModules(module.base_ring()):
        data["presentation"] = module.presentation()
    elif module in FramedModules(module.base_ring()):
        data["module_generating_set"] = module.module_generating_set()
    formed = object_of(category, **data)
    # The form is re-read on the object it is the form *of*.  It arrives here
    # written on $M$, because $L$ did not exist when it was stated; but $L$ is
    # $M$ with that form, so a form of $L$ that its own elements cannot be fed
    # to is a form of something else.
    formed._form = form.on_module(formed)
    formed._refine_from_form()
    return formed


def is_form_morphism(morphism: "MembershipInput") -> bool:
    r"""Whether ``morphism`` is an element of a form-preserving homset.

    Being form-preserving is not a class but a homset: such a morphism is an
    element of ``Hom`` taken in :class:`FormModules`, so this asks its parent.
    """
    if not isinstance(morphism, Morphism):
        return False
    return morphism.parent() in FormModules(
        morphism.domain().base_ring()
    ).Homsets()



def correlation_of(lattice: Parent) -> Morphism:
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
    assert is_form_morphism(correlation), (
        f"{dual} is a formed module, so its homset builds form morphisms; "
        f"got {correlation}"
    )
    return correlation
