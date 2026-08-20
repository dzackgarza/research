r"""Finite-group representations on finitely generated free modules."""

from typing import TYPE_CHECKING
from dzack_research.preamble.lexicon import Element
if TYPE_CHECKING:
    from sage.categories.groups import Group
    from sage.categories.groups import GroupElement
    from sage.categories.modules import Module
    from sage.structure.element import ModuleElement
    from sage.structure.element import Vector
    from sage.structure.parent import ElementConstructorInput, MembershipInput

from sage.rings.number_field.number_field import CyclotomicField
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import FramingMorphism
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import GroupAction
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleAutomorphism
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
from sage.matrix.special import identity_matrix
from sage.arith.functions import lcm
if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
    from sage.rings.ring import Field
    from sage.categories.homset import Homset
    from sage.rings.ring import Ring
    from sage.structure.element import RingElement

from typing import Protocol, Self, TYPE_CHECKING

from sage.misc.cachefunc import cached_method
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import Category
from dzack_research.preamble.owned_category_bases import HomsetsCategory
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.structure.element import Element as SageElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, richcmp

from dzack_research.preamble.categories.sets.cardinals import Cardinal
from dzack_research.preamble.categories.modules.group_modules.characters import Character
from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import MorphismMatrix
from dzack_research.preamble.categories.sets.owned_sets import Sets
from dzack_research.preamble.categories.sets.underlying_sets import (
    UnderlyingSet,
    UnderlyingSets,
)

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleAutomorphismGroup
    from dzack_research.preamble.owned_category import ConstructionData

    # The admissible ways to name an equivariant map, in the order the
    # constructors match them: the generator morphism itself, a finite
    # assignment of generator images, or those images in the framing's order.
    EquivariantAssignment = SetMorphism | dict | list | tuple

    class GroupModuleParent(Protocol):
        r"""What a parent placed in ``GroupModules(R, G)`` supplies.

        Category placement, not the constructing class, is what gives an
        object these; ``GroupModule`` is one such parent and the group
        lattices are others.
        """

        def base_ring(self) -> "Ring": ...
        def rank(self) -> "Cardinal": ...
        def group(self) -> "Group": ...
        def action_matrix(self, element: "Element") -> MorphismMatrix: ...
        def Hom(self, codomain: "Module", category: "Category | None" = ...) -> "Homset": ...


class GroupModules(Category):
    r"""The category of \(R[G]\)-modules for the specified \(R\) and \(G\)."""

    @staticmethod
    def __classcall__(cls: type["GroupModules"], base_ring: "Ring", group: "Group") -> "GroupModules":
        # One category per ring and group, named the way a module reports
        # its base: callers reach here both from a module and from the
        # engine's own \(\ZZ\), and those two must not name two categories
        # with disjoint memberships.
        # Local: a module-level import would close a cycle; the module is built by the time this runs.
        from dzack_research.preamble.categories.rings.rings import owned_ring_view

        category: "GroupModules" = Category.__classcall__(
            cls, owned_ring_view(base_ring), group
        )
        return category

    def __init__(self, base_ring: "Ring", group: "Group") -> None:
        # No finiteness requirement.  R[G]-Mod is defined for every group;
        # what the preamble can *check* about a morphism depends on whether
        # G produces generators, and that is recorded per morphism rather
        # than shutting the category itself against infinite groups.
        self._base_ring = base_ring
        self._group = group
        Category.__init__(self)

    def base_ring(self) -> "Ring":
        return self._base_ring

    def acting_group(self) -> "Group":
        return self._group

    def _repr_object_names(self) -> str:
        return f"{self._base_ring}[{self._group}]-modules"

    def super_categories(self) -> list:
        # Local: a module-level import would close a cycle; the module is built by the time this runs.
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import FinitelyGeneratedFreeModules

        return [FinitelyGeneratedFreeModules(self._base_ring)]

    def is_semisimple(self) -> bool:
        r"""Return whether \(R[G]\)-Mod is semisimple.

        Maschke's theorem: this holds exactly when \(|G|\) is invertible in
        \(R\).  Stating it on the category is what makes it a theorem the
        code can consult; buried in a method as ``base_ring is ZZ`` it is an
        unnamed hypothesis that happens to be checked in one place.

        \(\mathbb Z[G]\) is *not* semisimple for any nontrivial \(G\), which
        is why an isotypic decomposition over \(\mathbb Z\) is an inclusion
        of finite index and not an isomorphism.

        This is Maschke's theorem and not the statement that \(R\) splits
        \(G\): semisimplicity says the components exhaust \(M\), and says
        nothing about whether the simple factors are absolutely irreducible.
        \(\mathbb Q[G]\) is semisimple and splits almost no \(G\).  That
        second statement is :meth:`is_split`.
        """
        base_ring = self.base_ring()
        if not base_ring.is_field():
            return False
        characteristic = base_ring.characteristic()
        semisimple: bool = (
            characteristic == 0 or self._group.order() % characteristic != 0
        )
        return semisimple

    def splitting_field(self) -> "Field":
        r"""Return \(K=\mathbb Q(\zeta_n)\), a field that *splits* \(G\).

        Not the fraction field.  A character takes its values in the \(n\)th
        cyclotomic field for \(n\) the exponent of \(G\), so a field omitting
        those values is one over which the absolutely irreducible characters
        are not even functions.  Over \(\mathbb Z\) the fraction field
        \(\mathbb Q\) is such a field for every \(G\) of exponent above 2.

        Two theorems are in play and only one of them is Maschke's.  \(K[G]\)
        is semisimple for *any* field of characteristic zero, which is what
        :meth:`is_semisimple` reports.  That its simple factors are matrix
        algebras -- that the absolutely irreducible characters are the
        characters of \(K\)-representations -- is the extra demand that \(K\)
        be a splitting field, and Brauer's theorem says \(\mathbb Q(\zeta_n)\)
        is one.

        The exponent divides the order, and \(\mathbb Q(\zeta_{|G|})\)
        contains \(\mathbb Q(\zeta_n)\), so the order is a number the group
        states and \(\mathbb Q(\zeta_{|G|})\) splits \(G\) either way.
        """
        order = self._group.order()
        fraction_field = self.base_ring().fraction_field()
        # Q(zeta_1) and Q(zeta_2) *are* Q, presented as degree-one number
        # fields; naming the fraction field itself keeps the rational case in
        # the ring the module already has, and covers a base ring whose
        # fraction field is larger than Q.
        field = fraction_field if order <= 2 else CyclotomicField(order)
        assert field.has_coerce_map_from(fraction_field), (
            f"{field} does not contain {fraction_field}: the field splitting "
            "G over this base ring is their composite, which is not formed here"
        )
        return field

    def is_split(self) -> bool:
        r"""Return whether \(R\) splits \(G\), so that \(R[G]\) is split.

        Brauer's theorem names one splitting field, ``splitting_field()``;
        \(R\) splits \(G\) when its fraction field already contains that one.
        The consequence is which characters index a decomposition: over a
        splitting field the absolutely irreducible characters do, and over a
        field that is not -- \(\mathbb Q\), for every \(G\) of exponent above
        2 -- the \(F\)-irreducible ones do, and the absolutely irreducible
        ones index components that have no \(R\)-form.
        """
        splits: bool = self.base_ring().fraction_field().has_coerce_map_from(
            self.splitting_field()
        )
        return splits

    class ParentMethods:
        r"""One $R[G]$-module: a finite free $M$, and an action $G\to Aut_R(M)$."""

        # The two halves of the pair $(M,\rho)$, and the same $\rho$ recorded
        # through the element wrapping so it moves this parent's own elements.
        _module: "Module"
        _action: GroupAction
        _acting_automorphisms: GroupAction

        def __init__(
            self: Self,
            module: "Module",
            action: GroupAction,
            **rest: "ConstructionData",
        ) -> None:
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import FinitelyGeneratedFreeModules
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import framing_morphism
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import group_action_homset

            assert module in FinitelyGeneratedFreeModules(module.base_ring()), (
                "an R[G]-module is constructed from an actual finite framed "
                "free module"
            )
            assert isinstance(action, GroupAction) and action.module() is module, (
                "the action must be a morphism into the supplied module's Aut "
                "homset"
            )
            # A group module IS the pair $(M,\rho)$, and both halves arrive as
            # constructor arguments.  They are stored before anything else so
            # that identity -- hash, equality, repr -- is answerable from the
            # first moment the object exists, including while construction is
            # still running and Sage's caches hash it.
            self._module = module
            self._action = action
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
                    underlying_module_generator_morphism(element_of_S)
                ),
            )
            self._free_module_generator_morphism = lifted_module_generator_morphism
            self._framing_morphism = framing_morphism(
                source,
                self,
                lifted_module_generator_morphism,
            )
            automorphisms = self.Aut()
            values = {
                element: automorphisms(
                    {
                        element_of_S: self._over(
                            action(element)(
                                underlying_module_generator_morphism(element_of_S)
                            )
                        )
                        for element_of_S in module.module_generating_set()
                    }
                )
                for element in action.domain()
            }
            # $\rho$ lands in $Aut(M)$, whose automorphisms move elements of
            # $M$.  This module's elements wrap those, so the same $\rho$ is
            # also recorded through the wrapping, to act on them.  Derived,
            # under its own name: ``_action`` is the constructor's $\rho$ and
            # never changes, because the hash is taken from it.
            self._acting_automorphisms = group_action_homset(action.domain(), self)(values)

        def framing_morphism(self: Self) -> FramingMorphism:
            return self._framing_morphism

        def rank(self: Self) -> "Cardinal":
            return self._module.rank()

        def zero(self: Self) -> "Element":
            return self._over(self._module.zero())

        def _over(self: Self, element: "Element") -> "Element":
            wrapped: "Element" = self.element_class(self, element)
            return wrapped

        def _from_coordinates(self: Self, coordinates: "Vector") -> "Element":
            return self._over(self._module._from_coordinates(coordinates))

        def _element_constructor_(
            self: Self,
            element: "ElementConstructorInput",
        ) -> "Element":
            # Conversion, not just recognition: coordinate data converts through
            # the module's own coordinate route; an element of this parent passes
            # through unchanged.
            if isinstance(element, SageElement) and element.parent() is self:
                return element
            assert isinstance(element, (tuple, list, SageElement)), (
                f"{element} is neither an element of {self} nor coordinate "
                "data for one"
            )
            return self._over(self._module(element))

        def __contains__(self: Self, element: "MembershipInput") -> bool:
            return isinstance(element, SageElement) and element.parent() is self

        def __hash__(self: Self) -> int:
            return hash((type(self), self._module, self._action))

        def __eq__(self: Self, other: "MembershipInput") -> bool:
            return (
                type(other) is type(self)
                and self._module == other._module
                and self._action == other._action
            )

        def _repr_(self: Self) -> str:
            return f"{self._module} with an action of {self.group()}"

        def forget_action(self: Self) -> "Module":
            return self._module

        def action(self: Self) -> GroupAction:
            return self._action

        def group(self: Self) -> "Group":
            return self.action().domain()

        def action_of(self: Self, element: "Element") -> ModuleAutomorphism:
            return self._acting_automorphisms(element)

        def action_matrix(self: Self, element: "Element") -> MorphismMatrix:
            return self.action_of(element).matrix()

        def character(self: "GroupModuleParent") -> Character:
            r"""Return \(\chi_\rho:g\mapsto\operatorname{tr}\rho(g)\).

            The character *of the representation*, and the only place the
            module enters character theory: ``group().irreducible_characters()``
            asks \(G\) alone, from the group and nothing else, and this asks
            the composite.  It is a class function because the trace is a
            conjugation invariant, so its values on class representatives
            determine it.

            \(\rho\) need not be faithful.  When it has a kernel, \(\chi_\rho\)
            is inflated from a character of the proper quotient \(\rho(G)\) and
            its inner products are taken over \(|G|\) -- which is precisely the
            statement lost when the acting group is recovered from the action
            matrices instead of being named.
            """
            group = self.group()
            class_function = group.character(
                [
                    self.action_matrix(element).trace()
                    for element in group.conjugacy_classes_representatives()
                ]
            )
            assert self.rank() == class_function.degree(), (
                f"chi_rho(1) is {class_function.degree()} and the module has "
                f"rank {self.rank()}: the traces were written against the "
                "wrong conjugacy classes"
            )
            return Character(class_function)

        def Hom(self: Self, codomain: "Module", category: "Category | None" = None) -> "Homset":
            if codomain in GroupModules(self.base_ring(), self.group()):
                return group_module_homset(self, codomain)
            return Parent.Hom(self, codomain, category)

        def act(self: Self, element: "Element", vector_: "ModuleElement") -> "ModuleElement":
            moved: "ModuleElement" = self.action_of(element)(vector_)
            return moved

        def is_invariant(self: Self, vector_: "ModuleElement") -> bool:
            r"""Return whether \(g\cdot v=v\) for every \(g\in G\).

            Decided on generators: the elements fixing \(v\) form a
            subgroup, so it contains \(G\) as soon as it contains a
            generating set.  Ranging over \(G\) needs it finite and does
            more work when it is.
            """
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.group.groups import refine_group

            return all(
                self.act(generator, vector_) == vector_
                for generator in refine_group(self.group()).group_generators()
            )

        def subobject_on(self: Self, module_generators: "OrderedSet") -> "Subobject":
            return _group_subobject(self, module_generators)

        def hom(self: "GroupModuleParent", images: "EquivariantAssignment", codomain: "Module | None" = None) -> "ModuleMorphism":
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.modules.framed.framed_modules import _finite_module_generator_assignment

            match images:
                case SetMorphism():
                    assert isinstance(images.codomain(), UnderlyingSets.ParentMethods), (
                        "a generator morphism lands in the underlying set of "
                        "its module codomain"
                    )
                    target = images.codomain().structured_parent()
                    assignment: "EquivariantAssignment" = images
                case dict() if images:
                    target = next(iter(images.values())).parent()
                    assignment = images
                case dict():
                    assert codomain is not None, (
                        "an empty assignment requires its codomain"
                    )
                    target = codomain
                    assignment = images
                case list() | tuple():
                    target, assignment = _finite_module_generator_assignment(
                        self,
                        images,
                        codomain,
                    )
                case _:
                    assert False, (
                        "an equivariant homomorphism is specified by a "
                        "generator morphism, a finite assignment, or an "
                        "ordered list of images"
                    )
            assert target.group() == self.group(), (
                "an equivariant map uses the same acting group on both sides"
            )
            return self.Hom(target)(assignment)

        @cached_method
        def isotypic_decomposition(self: Self) -> "Subobject":
            return _isotypic_decomposition(self)

        def isotypic_component(self: Self, character: Character) -> "Subobject":
            return self.isotypic_decomposition().summand(character)

        def module_invariants(self: Self) -> "Subobject":
            r"""Return \(M^G=\{v:gv=v\}\hookrightarrow M\).

            Named beside ``module_coinvariants`` for the same reason that one
            is: the unqualified ``invariants`` already names the invariant
            factors of a finitely presented module, a different object
            entirely, and the qualifier is how the two are told apart in one
            namespace.
            """
            return _group_subobject(self, _invariant_generators(self))

        def module_coinvariants(self: Self) -> "Module":
            return _module_coinvariants(self)

    class ElementMethods:
        r"""An element of an $R[G]$-module, and its image after forgetting $G$."""

        def __init__(
            self: Self,
            parent: Parent,
            element: "Element",
            **rest: "ConstructionData",
        ) -> None:
            assert element.parent() is parent.forget_action(), (
                f"{element} is not an element of {parent.forget_action()}"
            )
            self._underlying = element
            super().__init__(parent, **rest)

        def forget_action(self: Self) -> "Element":
            return self._underlying

        def coefficients(self: Self) -> dict:
            return dict(self._underlying.coefficients())

        def underlying_set_element(self: Self) -> "Element":
            r"""Recover the element of \(S\) defining a canonical generator."""
            return self._underlying.underlying_set_element()

        def _coordinates(self: Self) -> "Vector":
            coordinates: "Vector" = self._underlying._coordinates()
            return coordinates

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
            return richcmp(self._underlying, other._underlying, op)

        def __eq__(self: Self, other: "MembershipInput") -> bool:
            # Identification across parents is a stated morphism, never coercion
            # (AGENTS.md: coercion must not erase the element/image distinction),
            # so equality outside this parent is plain False and Sage's
            # conversion fallback never consults a constructor.
            if not (
                isinstance(other, SageElement)
                and other.parent() is self.parent()
            ):
                return False
            return bool(richcmp(self._underlying, other._underlying, op_EQ))

        def __ne__(self: Self, other: "MembershipInput") -> bool:
            return not self.__eq__(other)

        def __hash__(self: Self) -> int:
            return hash((id(self.parent()), self._underlying))

        def _repr_(self: Self) -> str:
            return repr(self._underlying)

    class Homsets(HomsetsCategory):
        r"""The equivariant maps between two modules for one $G$."""

        class ParentMethods:
            r"""The homset of equivariant maps between two modules for one \(G\)."""

            def __init__(
                self,
                domain: "Module",
                codomain: "Module",
                **rest: "ConstructionData",
            ) -> None:
                assert codomain in GroupModules(domain.base_ring(), domain.group()), (
                    "the codomain is not a module for the stated ring and group"
                )
                assert domain.group() == codomain.group(), (
                    "an equivariant homset has one specified acting group"
                )
                super().__init__(domain=domain, codomain=codomain, **rest)

            def _element_constructor_(self, images: "EquivariantAssignment | ModuleMorphism") -> ModuleMorphism:
                morphism: ModuleMorphism
                match images:
                    case ModuleMorphism():
                        assert images.parent() is self, (
                            "an existing equivariant morphism belongs to its own homset"
                        )
                        return images
                    case SetMorphism() | dict():
                        morphism = ModuleMorphism(self, images)
                    case _:
                        assert False, (
                            "an equivariant morphism is specified by its generator "
                            "morphism or finite generator assignment"
                        )
                assert all(
                    morphism(
                        self.domain().act(
                            group_element,
                            self.domain().module_generator(element_of_S),
                        )
                    )
                    == self.codomain().act(
                        group_element,
                        morphism(self.domain().module_generator(element_of_S)),
                    )
                    for group_element in self.domain().group()
                    for element_of_S in self.domain().module_generating_set()
                ), "the proposed map is not equivariant"
                return morphism

            def _repr_(self) -> str:
                return (
                    f"Hom_{self.domain().group()}("
                    f"{self.domain()}, {self.codomain()})"
                )

def group_module_homset(domain: "Module", codomain: "Module") -> Parent:
    r"""Return the canonical equivariant homset of two \(G\)-modules."""
    cache = domain.__dict__.setdefault("_group_module_homsets", {})
    homset: Parent | None = cache.get(codomain)
    if homset is None:
        homset = object_of(
            GroupModules(domain.base_ring(), domain.group()).Homsets(),
            domain=domain,
            codomain=codomain,
        )
        cache[codomain] = homset
    return homset


def GroupModule(module: "Module", action: GroupAction) -> Parent:
    r"""Return the finite free module $M$ acted on by $G$ through ``action``."""
    return object_of(
        GroupModules(module.base_ring(), action.domain()),
        module=module,
        action=action,
    )


def _is_group_module(module: "Module") -> bool:
    r"""Whether ``module`` is an object of a category of $R[G]$-modules."""
    return any(
        isinstance(part, GroupModules)
        for part in module.category().all_super_categories()
    )


def _invariant_generators(module: "Module") -> list:
    r"""Return generators of \(M^G=\{v:gv=v\ \forall g\}\) written in \(M\).

    A morphism's matrix has the images of the generators as its rows, so a
    coefficient row \(v\) is carried to \(v\rho(g)\) and invariance is the
    *left* condition \(v(\rho(g)-1)=0\).  The conditions for the several \(g\)
    hold at once exactly on the left kernel of the blocks written side by
    side, which is the right kernel of the transposed blocks stacked -- the
    shape in which the seam offers a nullspace.  Reading the right kernel of
    the untransposed blocks instead answers for the dual representation, whose
    invariants have the same rank and are different vectors.

    The subtraction happens on the underlying matrices.  A difference of two
    morphism matrices is the matrix of a difference of morphisms, since
    \(\operatorname{End}(M)\) is an abelian group; a difference of a morphism
    matrix and a bare array is not, and the identity here is a bare array.
    """
    # Local: a module-level import would close a cycle; the module is built by the time this runs.
    from dzack_research.preamble.categories.rings.rings import engine_ring

    assert module.group() in Sets().Finite(), (
        "computing invariants imposes one condition per group element, so "
        f"it requires a finite group; {module.group()} is not known to be one"
    )
    identity = identity_matrix(engine_ring(module.base_ring()), module.rank())
    constraints = MorphismMatrix(
        matrix(
            engine_ring(module.base_ring()),
            [
                row
                for element in module.group()
                for row in (
                    module.action_matrix(element)._sage_matrix() - identity
                ).transpose().rows()
            ],
        )
    )
    generators = [
        module._from_coordinates(row)
        for row in constraints._right_kernel_matrix().rows()
    ]
    assert all(module.is_invariant(generator) for generator in generators), (
        "the solved constraint system produced a vector the group moves"
    )
    return generators


def _module_coinvariants(module: "Module") -> "Module":
    # Local: a module-level import would close a cycle; the module is built by the time this runs.
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModule
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _independent_module_generators
    from dzack_research.preamble.categories.sets.sets import finite_ordered_set

    relations = _independent_module_generators(
        module,
        [
        module.act(group_element, generator) - generator
        for group_element in module.group()
        for generator in module.module_generators()
        ],
    )
    relation_module = BasedFreeModule(
        module.base_ring(),
        finite_ordered_set(tuple(relations)),
    )
    presentation = (
        relation_module.Hom(module)(
            {relation: relation for relation in relation_module.module_generating_set()}
        )
        if relations
        else relation_module.Hom(module).zero()
    )
    return FinitelyPresentedModule(presentation)


def _base_field_automorphisms(category: GroupModules) -> tuple:
    r"""Return \(\operatorname{Gal}(K/F)\) for \(F\) the fraction field of \(R\).

    The absolutely irreducible characters are permuted by the automorphisms of
    the splitting field that fix the field \(M\)'s coefficients are written
    over, which is to say the automorphisms fixing \(F\) pointwise, which is
    to say fixing its generators.  Taking all of
    \(\operatorname{Gal}(K/\mathbb Q)\) instead would merge orbits that \(F\)
    already separates whenever \(F\) is larger than \(\mathbb Q\).
    """
    # Local: a module-level import would close a cycle; the module is built by the time this runs.
    from dzack_research.preamble.categories.rings.rings import own_ring

    field = category.splitting_field()
    base_field = category.base_ring().fraction_field()
    return tuple(
        automorphism
        for automorphism in field.galois_group()
        if all(
            automorphism(field(generator)) == field(generator)
            for generator in own_ring(base_field).algebra_generators()
        )
    )


def _index_characters(module: "Module") -> tuple:
    r"""Return the characters indexing the isotypic decomposition of \(M\).

    Over a base ring that splits \(G\) these are the absolutely irreducible
    characters.  Over one that does not -- \(\mathbb Z\), for every \(G\) of
    exponent above 2 -- they are the \(F\)-irreducible characters: the sums
    over the orbits of \(\operatorname{Gal}(K/F)\) acting on the absolutely
    irreducible ones.

    Which set indexes the decomposition is a statement about \(M_\chi\) and
    not a presentation choice.  \(M_\chi=M\cap(M\otimes K)_\chi\) is nonzero
    only when the \(\chi\)-component has an \(R\)-form, and an absolutely
    irreducible \(\chi\) with irrational values has none: its component is
    defined over \(K\) and moved by \(\operatorname{Gal}(K/F)\), so it meets
    \(M\) in \(0\).  The orbit sum is the character that group fixes, and its
    component is the one that is nonzero whenever \(\chi\) occurs, saturated
    in \(M\), and whose sum over the index set has finite index in \(M\) --
    which is the statement the decomposition makes.  Indexing by the
    absolutely irreducible characters instead leaves every component but the
    rational ones zero and the sum far from \(M\).

    A Galois orbit is read off the values, which are what a character is: two
    absolutely irreducible characters are conjugate exactly when the sets of
    value families of their orbits agree, so that set is the key the orbits
    are collected under.  GAP supplies the character table and Sage the
    automorphisms of \(K\); neither the table nor the action is written here.
    """
    characters = tuple(
        Character(class_function)
        for class_function in module.group().irreducible_characters()
    )
    category = module.category()
    if category.is_split():
        return characters
    field = category.splitting_field()
    automorphisms = _base_field_automorphisms(category)
    orbits: dict = {}
    for character in characters:
        orbit = frozenset(
            tuple(
                automorphism(field(value))
                for value in character.class_values()
            )
            for automorphism in automorphisms
        )
        orbits.setdefault(orbit, []).append(character)
    return tuple(
        sum(conjugates[1:], conjugates[0]) for conjugates in orbits.values()
    )


def _isotypic_projector(module: "Module", character: Character) -> "ModuleMorphism":
    r"""Return \(p_\chi=\frac{\deg\psi}{|G|}\sum_g\chi(g^{-1})\rho(g)\).

    An idempotent endomorphism of \(M\otimes F\) -- and an endomorphism is a
    morphism, so it is returned as one.  Its matrix is the private means of
    writing it down: a caller holding the matrix has to know which of its row
    and column spaces is the image, and the morphism knows.  Over \(R\) itself
    the projector need not have entries, which is the whole reason for the
    base change.

    \(\psi\) is an absolutely irreducible constituent of \(\chi\).  For an
    absolutely irreducible \(\chi\) that is \(\chi\) and this is the classical
    formula.  For an \(F\)-irreducible \(\chi\) the constituents are one
    Galois orbit, all of one degree, and \(p_\chi\) is the sum of their
    projectors: the sum over the orbit is therefore taken on the
    *coefficients*, where it is \(\chi(g^{-1})\) itself, and not on the
    matrices, where each term separately would ask \(F\) for a value it does
    not have.

    This one routine is not delegated, and the divergence is deliberate.
    Sage's ``invariant.py`` writes the same operator transposed and with
    \(\chi(g)\) where \(\chi(g^{-1})\) belongs; the two departures cancel for
    a permutation action and do not cancel in general.  Upstream also leaves
    the \(1/|G|\) to surface as a bare type error over a ring where it does
    not exist, instead of stating the hypothesis.  Everything the projector
    consumes -- the character table, the degrees, the values -- is still
    GAP's.

    \(F=\operatorname{Frac}(R)\) and not the splitting field \(K\).  What a
    projector asks of its coefficient field is that its coefficients lie
    there, and the coefficient of \(\rho(g)\) in \(p_\chi\) is a value of the
    *indexing* character.  ``_index_characters`` chooses characters whose
    values lie in \(F\), so \(K\) is where the character table is read and
    never where the projector is written.
    """
    extended = module.vector_space()
    field = extended.base_ring()
    group = module.group()
    constituents = character.irreducible_constituents()
    assert constituents, "the zero class function affords no representation"
    assert all(value in field for value in character.class_values()), (
        f"{character} takes values outside {field}, so the component it names "
        f"has no {module.base_ring()}-form and does not index a decomposition "
        "over this ring"
    )
    # Galois conjugates share a degree, so any one constituent states it.
    degree = constituents[0].degree()
    entries = (field(degree) / field(group.order())) * sum(
        field(character(element.inverse()))
        * module.action_matrix(element).change_ring(field)._sage_matrix()
        for element in group
    )
    assert entries * entries == entries, (
        "the projector for this character is not idempotent: its constituents "
        "are not a single Galois orbit of absolutely irreducible characters"
    )
    return extended.hom(
        [extended._from_coordinates(row) for row in entries.rows()],
        extended,
    )


def _isotypic_component(module: "Module", character: Character) -> "Subobject":
    r"""Return \(M_\chi=M\cap(M\otimes F)_\chi\hookrightarrow M\).

    The *kernel* of \(N(p_\chi-1)\), for \(N\) clearing the denominators of
    \(p_\chi\).  A vector of \(M\) lies in the \(\chi\)-part of \(M\otimes F\)
    exactly when \(p_\chi\) fixes it, which is exactly when \(N(p_\chi-1)\)
    kills it; \(N\ne0\) changes no solution, and it is what makes the
    endomorphism one of \(M\) rather than of \(M\otimes F\).

    Taking a kernel is what makes the component saturated, and for free: over
    a PID \(kv\) is killed exactly when \(v\) is.  So no call site here clears
    a denominator on a generator or saturates a span afterwards.
    ``Subobjects.saturation`` is still the definition of the primitive closure
    and is simply not what computes this one.

    \(N(p_\chi-1)\) is equivariant: \(p_\chi\) is the action of a *central*
    element of \(F[G]\) and commutes with every \(\rho(g)\).  That is what the
    equivariant homset checks on construction, and it is why the kernel is a
    submodule for \(G\) and not merely for \(R\).  A character that does not
    occur in \(M\) gives the zero submodule rather than a failure.
    """
    # Local: a module-level import would close a cycle; the module is built by the time this runs.
    from dzack_research.preamble.categories.rings.rings import engine_ring

    projector = _isotypic_projector(module, character).matrix()
    difference = projector._sage_matrix() - identity_matrix(
        projector.base_ring(), module.rank()
    )
    scale = lcm([entry.denominator() for entry in difference.list()])
    integral = (scale * difference).change_ring(engine_ring(module.base_ring()))
    return module.hom(
        [module._from_coordinates(row) for row in integral.rows()],
        module,
    ).kernel()


def _restricted_action_automorphisms(
    module: "Module",
    submodule: "Module",
    module_generators: list,
) -> list:
    # Local: a module-level import would close a cycle; the module is built by the time this runs.
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector
    from dzack_research.preamble.categories.rings.rings import engine_ring

    if not module_generators:
        return [submodule.Aut().one() for _ in module.group().group_generators()]
    # The linear system is solved over a field, and which field that is, is a
    # fact about the base ring rather than about which base ring it happens to
    # be: a field is its own fraction field, so naming the fraction field says
    # it once for every R.  The solution is asserted back into R below.
    field = module.base_ring().fraction_field()
    inclusion_matrix = matrix(
        field,
        [_coordinate_vector(generator) for generator in module_generators],
    )
    def restricted_automorphism(group_element: "GroupElement") -> "ModuleAutomorphism":
        images = matrix(
            field,
            [
                _coordinate_vector(module.act(group_element, generator))
                for generator in module_generators
            ],
        )
        coefficients = (
            inclusion_matrix.transpose()
            .solve_right(images.transpose())
            .transpose()
        )
        assert coefficients * inclusion_matrix == images, (
            "the proposed submodule is not stable under the action"
        )
        assert all(
            entry in submodule.base_ring() for entry in coefficients.list()
        ), "the restricted action is not defined over the base ring"
        coefficients = coefficients.change_ring(engine_ring(submodule.base_ring()))
        return submodule.Aut()(
            {
                label: submodule._from_coordinates(row)
                for label, row in zip(
                    submodule.module_generating_set(),
                    coefficients.rows(),
                )
            }
        )

    return [
        restricted_automorphism(group_element)
        for group_element in module.group().group_generators()
    ]


def _equivariant_hom(domain: "Module", codomain: "Module", images: "EquivariantAssignment") -> "ModuleMorphism":
    match images:
        case dict():
            assignment = images
        case list() | tuple():
            assert len(images) == domain.number_of_module_generators(), (
                "the number of images does not match the generating set"
            )
            assignment = dict(
                zip(
                    domain.module_generating_set(),
                    images,
                    strict=True,
                )
            )
        case _:
            assert False, (
                "an equivariant homomorphism is specified by a finite "
                "assignment or an ordered list of images"
            )
    return domain.Hom(codomain)(assignment)


def _group_subobject(module: "Module", module_generators: "OrderedSet") -> "Subobject":
    # Local: a module-level import would close a cycle; the module is built by the time this runs.
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _independent_module_generators
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import group_action_homset
    from dzack_research.preamble.categories.sets.sets import finite_ordered_set

    module_generators = tuple(module_generators)
    assert all(generator in module for generator in module_generators), (
        "a subobject is generated by elements of this group module"
    )
    module_generators = _independent_module_generators(module, module_generators)
    labels = finite_ordered_set(tuple(module_generators))
    free = BasedFreeModule(
        module.base_ring(),
        labels,
    )
    restricted = _restricted_action_automorphisms(module, free, module_generators)
    action = group_action_homset(module.group(), free)(restricted)
    submodule = GroupModule(free, action)
    return Subobject(
        _equivariant_hom(
            submodule,
            module,
            tuple(labels),
        )
    )


def _isotypic_sum(
    summed: "Subobject",
    components: "OrderedSet",
    characters: "OrderedSet",
) -> "Subobject":
    r"""Return \(\bigoplus_\chi M_\chi\hookrightarrow M\), decomposed.

    One object answers both of the questions a caller has, because they are
    one statement.  As a subobject it carries the inclusion into \(M\), and
    with it ``index()``; as a direct sum it carries the summands indexed by
    the characters, so ``summand(chi)`` is the \(\chi\)-component.  The two
    are structure on the same object and not two objects.

    The summands and their index set are the data ``DirectSumObjects``
    declares -- the same two names its own constructor sets -- and not a
    private ledger: the inclusion is the subobject's morphism, and the index
    is computed from it rather than stored.
    """
    # Local: a module-level import would close a cycle; the module is built by the time this runs.
    from dzack_research.preamble.categories.abstract_categories.direct_sum_objects import DirectSumObjects
    from dzack_research.preamble.refine import refine

    summed._summands = tuple(components)
    summed._summand_index_set = characters
    # Both categories are named: ``refine`` installs the methods of the
    # category it is given, so refining into the direct-sum structure alone
    # would take the inclusion and the index away with it.
    # refine rebuilds the class from the categories named here, so the
    # object's own category must be one of them or its module methods go.
    return refine(summed, [summed.category(), DirectSumObjects()])


def _isotypic_decomposition(module: "Module") -> "Subobject":
    r"""Return \(\bigoplus_\chi M_\chi\) together with how it sits in \(M\).

    One statement at two strengths, and so one object.  The sum of the
    isotypic components is a submodule of \(M\) of finite index, indexed by
    the characters ``_index_characters`` names; when \(R[G]\) is semisimple
    that index is 1 and the inclusion is an isomorphism.  Maschke's theorem is
    therefore an assertion *about* this object, not a second kind of object: a
    caller asking for the \(\chi\)-component asks the same way in either case,
    and reads ``index()`` when it wants to know which case it is in.

    The index set is where the base ring is heard from.  Over a splitting
    field it is the absolutely irreducible characters; over \(\mathbb Z\) it
    is the \(\mathbb Q\)-irreducible ones, and the finite-index statement
    above is true of that index set and false of the other.

    The coproduct is not the object to return.  Its coapex would be \(M\) --
    the shared codomain of the components' inclusions -- so refining it would
    declare \(M\) to *be* \(\bigoplus_\chi M_\chi\), which is exactly the
    isomorphism that fails over \(\mathbb Z\), and would leave the inclusion
    of the sum with nowhere to live but a private field.
    """
    # Local: a module-level import would close a cycle; the module is built by the time this runs.
    from dzack_research.preamble.categories.sets.sets import finite_ordered_set

    characters = _index_characters(module)
    components = tuple(
        _isotypic_component(module, character) for character in characters
    )
    summed = _group_subobject(
        module,
        [
            generator
            for component in components
            for generator in component.embedded_module_generators()
        ],
    )
    if module.category().is_semisimple():
        # Maschke, asserted of the object it is about: the components exhaust
        # M, which is the index being 1 and nothing else.
        assert summed.index() == 1, (
            "over a semisimple group algebra the isotypic components must "
            f"exhaust the module, but their sum has index {summed.index()}"
        )
    return _isotypic_sum(summed, components, finite_ordered_set(characters))
