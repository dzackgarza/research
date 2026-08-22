r"""Native homsets and morphisms for the owned module categories.

A map from a framed module is declared by a set morphism from its generating
set to the underlying set of the codomain.  Its parent is the canonical homset
of the named domain and codomain.  Construction checks every relation of a
presented domain, so membership in a homset is parenthood and nothing else.
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Callable

from dzack_research.preamble.utilities import zipsum
if TYPE_CHECKING:
    from sage.categories.groups import Group
    from sage.categories.modules import Module
    from dzack_research.preamble.lexicon import ModuleElement
    from sage.structure.element import Vector

from sage.categories.groups import Groups
from sage.categories.modules import Modules
from dzack_research.preamble.categories.modules.pure.modules import Modules as OwnedModules
from dzack_research.preamble.owned_category_bases import Category, Category_over_base_ring
from dzack_research.preamble.categories.sets.sets import finite_ordered_set
from dzack_research.preamble.refine import refine
if TYPE_CHECKING:
    from typing import Protocol
    from sage.categories.category import Category
    from dzack_research.preamble.categories.sets.sets import Set
    from dzack_research.preamble.categories.modules.framed.framed_modules import FramedModuleParent
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
    class AutomorphismModuleParent(FramedModuleParent, Protocol):
        def Aut(self) -> "ModuleAutomorphismGroup": ...

    class FramedAutomorphismSubgroup(Protocol):
        def domain(self) -> AutomorphismModuleParent: ...
        def is_finite(self) -> bool: ...
        def group_generators(self) -> TotallyOrderedFiniteSet[ModuleAutomorphism]: ...

from collections.abc import Iterator
from typing import TYPE_CHECKING

from sage.misc.cachefunc import cached_function, cached_method
from sage.categories.homset import Hom, Homset
from dzack_research.preamble.owned_category import object_of
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.rings import Rings
from sage.matrix.constructor import matrix
from sage.matrix.matrix0 import Matrix
from sage.modules.free_module_element import FreeModuleElement, vector
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet
from sage.structure.element import Element, MultiplicativeGroupElement, RingElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.sets.cardinals import Cardinal, cardinal
from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import (
    matrix_group,
    row_normal_form,
)
from dzack_research.preamble.categories.modules.group_modules.characters import Character
from dzack_research.preamble.categories.sets.owned_sets import Sets

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet
    from sage.rings.infinity import PlusInfinity
    from sage.rings.ring import Ring
    from sage.structure.parent import ElementConstructorInput

    # The three admissible ways to name a module morphism, in the order
    # ``ModuleMorphism.__init__`` matches them: the generator morphism itself,
    # a finite dictionary of generator images, or any function on the
    # generating set.  Type-only: nothing constructs it.
    type ModuleMorphismAssignment = dict[
        ElementConstructorInput,
        ElementConstructorInput,
    ]
    type ModuleMorphismData = (
        SetMorphism[Element, ModuleElement]
        | ModuleMorphismAssignment
        | Callable[[Element], ModuleElement]
    )

    # A homset is a parent whose elements are its morphisms.  The runtime
    # class is a Cython extension type and cannot be subscripted, so the
    # binding goes through an alias, per the note in
    # ``typings/sage/structure/parent.pyi``.
    GroupActionHomsetBase = Homset["GroupAction"]
else:
    GroupActionHomsetBase = Homset


@cached_function
def module_homset(domain: "Module", codomain: "Module") -> Parent:
    r"""Return the canonical module homset after forgetting extra structure.

    ``Hom(X, Y, C)`` with ``C`` the category of the *objects*: Sage's
    ``Homset.__init__`` is what places the result in ``C.Homsets()`` or
    ``C.Endsets()``, so handing it ``C.Homsets()`` places the homset in the
    homsets of the homsets and its morphisms reach none of the homset
    methods.
    """
    homset: Parent = Hom(domain, codomain, OwnedModules(domain.base_ring()))
    return homset


def _module_morphism(domain: "Module", codomain: "Module", images: "ModuleMorphismData") -> "ModuleMorphism":
    r"""Construct a module morphism through its canonical homset."""
    return module_homset(domain, codomain)(images)


def _one_sided_inverse_matrix(forward: "Matrix", left: bool) -> "Matrix":
    r"""Return $X$ with $FX=I$ (``left=True``) or $XF=I$ (``left=False``).

    Smith normal form gives $D=UFV$, so $X=VD^{+}U$ with $D^{+}$ the
    diagonal of unit inverses -- integral over the base ring exactly when
    the relevant invariant factors are units, which the caller's split
    criterion guarantees and this helper re-asserts, along with the
    inverse identity itself.
    """
    smith, row_transform, column_transform = forward.smith_form()
    required = forward.nrows() if left else forward.ncols()
    diagonal = [
        smith[index, index]
        for index in range(min(smith.nrows(), smith.ncols()))
    ]
    assert len(diagonal) >= required and all(
        entry.is_unit() for entry in diagonal[:required]
    ), "a split morphism has unit invariant factors"
    pseudo_inverse = matrix(
        forward.base_ring(),
        forward.ncols(),
        forward.nrows(),
        {
            (index, index): diagonal[index].inverse_of_unit()
            for index in range(required)
        },
    )
    candidate = column_transform * pseudo_inverse * row_transform
    identity_check = (
        forward * candidate if left else candidate * forward
    )
    assert identity_check.is_one(), (
        "the Smith-form one-sided inverse does not compose to the identity"
    )
    return candidate


def endomorphism_ring(module: "Module") -> Parent:
    r"""Return \(\operatorname{End}_R(M)\): the endset, as a ring.

    Multiplication is composition and addition is pointwise, so the endset
    of \(M\) in \(R\text{-Mod}\) is a ring.  This is the codomain of the
    structure morphism \(\rho:S\to\operatorname{End}(M)\) that *is* an
    \(S\)-module structure on \(M\), which is why it must be a ring and not
    merely a monoid.

    Taken in \(R\text{-Mod}\), never in a category of form-bearing modules:
    isometries do not add, so form-preserving endomorphisms are not an
    abelian group.  A form-bearing \(S\)-module is one whose \(\rho\) happens
    to land in the subgroup preserving the form, not one whose endomorphism
    ring was formed somewhere else.
    """
    endset: Parent = refine(module_homset(module, module), Rings())
    return endset


def _coordinate_vector(element: "Element") -> FreeModuleElement:
    r"""Return finite coordinates in the element's declared framing.

    Asked of the element.  A module whose category gives its elements a finite
    ordered framing answers this; one without such a framing has no answer.
    """
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import FinitelyGeneratedFreeModules
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModules

    assert (
        element.parent() in FinitelyGeneratedFreeModules(element.parent().base_ring())
        or element.parent() in FinitelyPresentedModules(element.parent().base_ring())
    ), (
        f"{element} is not in a finite free or presented module with a matrix "
        "coordinate vector"
    )
    coordinates: FreeModuleElement = element._coordinates()
    return coordinates


def _coefficients(element: "Element") -> dict[ElementConstructorInput, RingElement]:
    r"""Return the finite coefficient function of a framed-module element.

    Asked of the element, whose own category names its generators.
    """
    from dzack_research.preamble.categories.modules.framed.framed_modules import FramedModules

    assert element.parent() in FramedModules(element.parent().base_ring()), (
        f"{element} is not an element of an owned framed module"
    )
    coefficient_function: dict[ElementConstructorInput, RingElement] = dict(
        element.coefficients()
    )
    return coefficient_function


def _is_presented(module: "Module") -> bool:
    r"""Whether ``module`` carries a chosen finite presentation."""
    # Local: at module level this closes an import cycle; the presented
    # category is built by the time a morphism asks about its ends.
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import FinitelyPresentedModules

    return module in FinitelyPresentedModules(module.base_ring())


def _is_torsion(module: "Module") -> bool:
    return _is_presented(module) and module.is_torsion()


def _independent_module_generators(
    module: "FramedModuleParent",
    module_generators: "OrderedSet[ModuleElement]",
) -> list[ModuleElement]:
    r"""Return a basis of the submodule spanned by finite input.

    Each input element has finite support in the framing.  Independence is
    therefore a finite computation on the union of those supports, even when
    the module's full framing is infinite.
    """
    # Local: at module level this closes an import cycle; the ring module is
    # built by the time generators are reduced.
    from dzack_research.preamble.categories.rings.rings import engine_ring

    module_generators = list(module_generators)
    if not module_generators:
        return []
    coefficient_functions = [_coefficients(generator) for generator in module_generators]
    support = tuple(
        dict.fromkeys(
            label
            for coefficients in coefficient_functions
            for label in coefficients
        )
    )
    ring = engine_ring(module.base_ring())
    rows = matrix(
        ring,
        [
            [coefficients.get(label, module.base_ring().zero()) for label in support]
            for coefficients in coefficient_functions
        ],
    )
    independent = row_normal_form(rows).rows()
    return [
        zipsum(
            row,
            (module.module_generator(label) for label in support),
            module.zero(),
        )
        for row in independent
    ]


def _expand_subobject_dict(
    parent: Parent,
    images: "ModuleMorphismAssignment",
) -> dict[ElementConstructorInput, ModuleElement]:
    r"""Expand a summand-level assignment onto the domain's framed labels.

    Both sides are ordered generating sets. A key is a framed module (which
    contributes its own labels), an element of the domain (which resolves to
    the label naming it), or a label. A value is a framed module -- a
    subobject included -- whose module generators are the images in order, an
    ordered enumeration of elements, or, when the source has rank one, a
    single element.
    """
    # Local: at module level these close an import cycle; the framed and
    # subobject modules are built by the time an assignment is expanded.
    from dzack_research.preamble.categories.modules.framed.framed_modules import FramedModules
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobjects

    domain = parent.domain()
    codomain = parent.codomain()
    module_generating_set = domain.module_generating_set()
    if set(images) == set(module_generating_set):
        return dict(images)

    label_of = {
        domain.module_generator(label): label
        for label in module_generating_set
    }

    expanded = {}
    for key, val in images.items():
        match key:
            case _ if key in FramedModules(domain.base_ring()):
                sources = tuple(key.module_generating_set())
            case Element() if key in label_of:
                sources = (label_of[key],)
            case _:
                sources = (key,)

        match val:
            case _ if val in Subobjects():
                # A subobject's own generators are abstract -- e_0 has
                # coordinates of length rank(S).  What lands in the codomain
                # is their image f(e_i), whose coordinates have the
                # codomain's rank.  These are not the same family.
                targets = tuple(val.embedded_module_generators())
            case _ if val in FramedModules(codomain.base_ring()):
                targets = tuple(val.module_generators())
            case list() | tuple():
                targets = tuple(val)
            case _:
                assert len(sources) == 1, (
                    "one target element requires a rank-one source"
                )
                targets = (val,)

        assert len(sources) == len(targets), (
            f"subobject {key} has {len(sources)} generators, but image has "
            f"{len(targets)}"
        )
        for source, target in zip(sources, targets, strict=True):
            expanded[source] = (
                target
                if isinstance(target, Element) and target.parent() is codomain
                else codomain(target)
            )

    assert set(expanded) == set(module_generating_set), (
        "the assignment must name exactly every element of the generating "
        f"set; got {set(expanded)} vs {set(module_generating_set)}"
    )
    return expanded


class ModuleMorphism(Morphism):
    r"""The linear extension of a morphism \(S\to U(N)\)."""

    def __init__(
        self,
        parent: Parent,
        images: "ModuleMorphismData",
    ) -> None:
        Morphism.__init__(self, parent)
        module_generating_set = self._domain_module_generating_set()
        set_homset = Hom(
            module_generating_set,
            parent.codomain(),
            Sets(),
        )
        match images:
            case SetMorphism():
                assert images.parent() is set_homset, (
                    "the generator morphism must belong to "
                    f"{set_homset}, got {images.parent()}"
                )
                module_generator_morphism = images
            case dict():
                assert module_generating_set in Sets().Finite(), (
                    "a dictionary specifies a morphism only for a finite "
                    "generating set; use a set morphism on the generating set"
                )
                values = _expand_subobject_dict(parent, images)
                assert all(
                    image.parent() == parent.codomain()
                    for image in values.values()
                ), "every specified generator image must belong to the codomain"
                module_generator_morphism = SetMorphism(
                    set_homset,
                    values.__getitem__,
                )
            case _ if callable(images):
                module_generator_morphism = SetMorphism(set_homset, images)
            case _:
                assert False, (
                    "a module morphism is the linear extension of a set "
                    "morphism from the domain's generating set"
                )
        self._generator_morphism = module_generator_morphism
        self._check_relations()

    def _domain_module_generating_set(self) -> "OrderedSet":
        return self.domain().module_generating_set()

    def _check_relations(self) -> None:
        # Local: at module level this closes an import cycle; the presented
        # category is built by the time relations are checked.
        domain = self.domain()
        if not _is_presented(domain):
            return
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import _presentation_matrix

        module_generating_set = tuple(self.domain().module_generating_set())
        zero = self.codomain().zero()
        assert all(
            zipsum(
            relation,
            module_generating_set,
            zero,
            term=lambda coefficient, element_of_S: coefficient
                    * self._module_generator_image(element_of_S),
        )
            == zero
            for relation in _presentation_matrix(domain).rows()
        ), "the assignment does not kill every relation"

    def module_generator_morphism(self) -> SetMorphism[Element, ModuleElement]:
        r"""Return the set morphism whose linear extension is this morphism."""
        return self._generator_morphism

    def _call_(self, element: "ElementConstructorInput") -> "Element":
        r"""Evaluate the linear extension on a module element."""
        from sage.structure.element import Element

        assert isinstance(element, Element), f"{element} is not an element"
        source = element
        if source.parent() is not self.domain():
            assert source.parent() == self.domain(), (
                f"{source} is not an element of {self.domain()}"
            )
            source = sum(
                (
                    coefficient * self.domain().module_generator(label)
                    for label, coefficient in _coefficients(source).items()
                ),
                self.domain().zero(),
            )
        return sum(
            (
                coefficient * self._generator_morphism(element_of_S)
                for element_of_S, coefficient in _coefficients(source).items()
            ),
            self.codomain().zero(),
        )

class FramingMorphism(ModuleMorphism):
    r"""A declared epimorphism \(F_R(S)\twoheadrightarrow M\).

    Surjectivity is part of the construction datum.  It is not replaced by an
    enumeration algorithm, since \(S\) may be a membership-only set.
    """

    def __init__(
        self,
        parent: Parent,
        images: "ModuleMorphismData",
    ) -> None:
        # Local: at module level this closes an import cycle; the free-module
        # category is built by the time a framing is declared.
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules

        assert parent.domain() in FramedFreeModules(
            parent.domain().base_ring()
        ), "the source of a framing is a free module on a specified set"
        ModuleMorphism.__init__(self, parent, images)

    def _domain_module_generating_set(self) -> "OrderedSet":
        return self.domain().module_generator_morphism().domain()


class SubFramingMorphism(ModuleMorphism):
    r"""\(F_R(\iota)\) for an injection \(\iota:T\hookrightarrow S\) of framings.

    Injectivity is part of the construction datum, the way surjectivity is for
    :class:`FramingMorphism` above, and for the same reason: an injection of
    sets is split, \(F_R(-)\) is a left adjoint and carries the splitting, so
    the morphism is a split monomorphism -- and \(T\) may be infinite, as the
    degree-two piece of an algebra on countably many generators is, in which
    case no enumeration of images decides anything.

    The caller supplies \(\iota\) and states by choosing this class that it is
    injective.  Sited here rather than as a field written onto whatever
    morphism arrived: a class says what the morphism *is*, and the general
    route below is a matrix of images and its normal form, which the tensor
    square of every lattice would otherwise pay.
    """

    def is_injective(self) -> bool:
        return True

    def is_in_image(self, element: Element) -> bool:
        r"""Return whether ``element`` is supported on the source framing."""
        if element.parent() is not self.codomain():
            return False
        source_labels = self.domain().module_generating_set()
        return all(label in source_labels for label in _coefficients(element))

    def lift(self, element: Element) -> Element:
        r"""Return the unique source element mapped to ``element``."""
        assert self.is_in_image(element), (
            f"{element} is not in the image of {self}"
        )
        domain = self.domain()
        return sum(
            (
                coefficient * domain.module_generator(label)
                for label, coefficient in _coefficients(element).items()
            ),
            domain.zero(),
        )


def framing_morphism(
    domain: "Module",
    codomain: "Module",
    images: "ModuleMorphismData",
) -> FramingMorphism:
    r"""Construct the declared framing epimorphism in its canonical homset."""
    return FramingMorphism(module_homset(domain, codomain), images)


class ModuleAutomorphism(ModuleMorphism):
    r"""An invertible endomorphism of a finitely generated free module."""

    def __init__(
        self,
        parent: "ModuleAutomorphismGroup",
        images: "ModuleMorphismData",
    ) -> None:
        ModuleMorphism.__init__(self, parent, images)
        refine(self, parent.category())
        assert self.domain() is self.codomain(), (
            "an automorphism is an endomorphism"
        )
        determinant = self.matrix().det()
        assert determinant.is_unit(), (
            f"the determinant {determinant} is not a unit"
        )

    def __mul__(self, other: ElementConstructorInput) -> "ModuleAutomorphism":
        assert (
            isinstance(other, ModuleAutomorphism)
            and other.parent() is self.parent()
        ), "composition here is internal to one automorphism group"
        return self.parent()(
            SetMorphism(
                Hom(
                    self.domain().module_generating_set(),
                    self.codomain(),
                    Sets(),
                ),
                lambda element_of_S: self(
                    other.module_generator_morphism()(element_of_S)
                ),
            )
        )

    def _richcmp_(self, other: ElementConstructorInput, op: int) -> bool:
        assert op in (op_EQ, op_NE), (
            "module automorphisms only have equality comparisons"
        )
        equal = (
            isinstance(other, ModuleAutomorphism)
            and other.parent() is self.parent()
            and all(
                self.module_generator_morphism()(label)
                == other.module_generator_morphism()(label)
                for label in self.domain().module_generating_set()
            )
        )
        return equal if op == op_EQ else not equal

    def inverse(self) -> "ModuleAutomorphism":
        # The engine view of the actual base ring: an automorphism's inverse
        # matrix lives over the module's own ring, not over Z regardless.
        from dzack_research.preamble.categories.rings.rings import engine_ring
        inverse_matrix = self.matrix().inverse().change_ring(
            engine_ring(self.domain().base_ring())
        )
        images = [
            zipsum(
            row,
            self.domain().module_generators(),
            self.domain().zero(),
        )
            for row in inverse_matrix.rows()
        ]
        return self.parent()(
            dict(zip(self.domain().module_generating_set(), images))
        )

    def cyclic_subgroup(
        self,
    ) -> "ModuleAutomorphismGroup":
        return self.parent().subgroup_on({self})

    def _libgap_(self) -> "GapElement":
        r"""Return this automorphism inside its group's GAP model.

        A character is a function on a group, and when the group is a literal
        subgroup of \(\operatorname{Aut}(M)\) its elements are these
        automorphisms; declaring where they sit in GAP is what makes GAP's
        characters functions on them rather than on a parallel set of
        matrices a caller would have to translate for.  This is the
        conversion protocol ``ClassFunction`` evaluates through.
        """
        return self.parent()._defining_matrix_group()(self.matrix()).gap()


class AutomorphismSubgroup:
    r"""A subgroup of \(\operatorname{Aut}(M)\).

    A subgroup generated by named automorphisms is a group in its own right,
    and it is the \(G\) of one of the two ways a representation is built here:
    the caller names elements of \(\operatorname{Aut}(M)\), \(G\) is what they
    generate, and \(\rho\) is the inclusion.  The other way names an abstract
    \(G\) and a \(\rho\) whose well-definedness the action constructor checks
    against \(G\)'s relations; both reach character theory the same way, by
    asking \(G\) for its characters and the module for \(\operatorname{tr}
    \rho(-)\).  So this class answers the questions a finite group answers.

    The elements here *are* automorphisms. Their matrices generate a matrix
    group isomorphic to this group: what is modelled below is this group and
    not the image of any \(\rho\).  An action's matrices generate \(\rho(G)\),
    a proper quotient of \(G\) whenever \(\rho\) has a kernel, whose character
    theory is a different one -- which is why no model is ever built from an
    action.  The full \(\operatorname{Aut}(M)\) is the automorphism group,
    the codomain \(\rho\) maps into and generally
    infinite, and the finiteness assertion is what separates the two.

    A mixin because the two automorphism groups that take this role --
    \(\operatorname{Aut}_R(M)\) and \(O(L)\) -- sit in unrelated homset
    hierarchies and the group surface is the same in both.
    """

    if TYPE_CHECKING:
        # What this mixin requires of whichever homset it is mixed into: the
        # module it is the automorphisms of, whether it is a literal finite
        # subgroup, that subgroup's generators, and its elements.  Declared,
        # never defined -- the host supplies every one.
        def is_finite(self) -> bool: ...
        def group_generators(self) -> TotallyOrderedFiniteSet["ModuleAutomorphism"]: ...
        def __iter__(self) -> Iterator["ModuleAutomorphism"]: ...

    def _subgroup_inclusion(self: "FramedAutomorphismSubgroup") -> "GroupAction":
        r"""Construct the canonical inclusion \(\rho:G\hookrightarrow\operatorname{Aut}(M)\).

        A subgroup of \(\operatorname{Aut}(M)\) determines one
        representation with no choice left to anyone: \(G\) is these elements
        and \(\rho\) sends each to itself.  So the arrow is named here, by the
        group whose data alone decides it, and a module never assembles a
        \(\rho\) for a caller who handed it an automorphism.

        Faithful, because it is an inclusion.  A caller who means an abstract
        \(G\), or a \(\rho\) with a kernel, constructs both in
        ``group_action_homset(G, M)`` instead; this is the case where that
        homset's element is already determined.

        The images are re-expressed in \(\operatorname{Aut}(M)\) because the
        generators' parent is this subgroup, and \(\rho\) is an arrow *into*
        the automorphism group.
        """
        module = self.domain()
        return AutomorphismSubgroupInclusion(group_action_homset(self, module))

    def automorphism_subgroup_inclusion(
        self: "FramedAutomorphismSubgroup",
    ) -> "GroupAction":
        r"""Return the faithful action that includes this subgroup in \(\operatorname{Aut}(M)\)."""
        return AutomorphismSubgroupInclusion(
            group_action_homset(self, self.domain(), self.supergroup())
        )

    def automorphism_subgroup_identity(
        self: "FramedAutomorphismSubgroup",
    ) -> ModuleAutomorphism:
        r"""Return the identity in the containing automorphism group."""
        return self.supergroup().one()

    def automorphism_subgroup_element(
        self: "FramedAutomorphismSubgroup",
        datum: "ElementConstructorInput",
    ) -> ModuleAutomorphism:
        r"""Return ``datum`` as an automorphism in this subgroup."""
        automorphism = self.supergroup()(datum)
        assert automorphism in self, f"{automorphism} is not in {self}"
        return automorphism

    @cached_method
    def _defining_matrix_group(self) -> "Group":
        r"""Return the GAP-backed matrix model of this group.

        The generators' matrices are used here once, to hand GAP a group it
        can compute conjugacy classes and a character table for.  Every method
        below translates GAP's answers back into this group's own elements, so
        no caller ever holds a matrix group.
        """
        assert self.is_finite(), (
            "this computation requires a finite subgroup, not the full "
            "automorphism group"
        )
        return matrix_group(
            (
                generator.matrix()
                for generator in self.group_generators()
            )
        )

    @cached_method
    def _by_matrix(self) -> dict[Matrix, ModuleAutomorphism]:
        r"""Index this group's own elements by their matrices."""
        indexed = {}
        for element in self:
            coordinates = matrix(element.matrix())
            coordinates.set_immutable()
            indexed[coordinates] = element
        return indexed

class ModuleAutomorphismGroups(Category_over_base_ring):
    r"""$\operatorname{Aut}_R(M)$, and its finitely generated subgroups.

    The group of units of $\operatorname{End}_R(M)$, which is a ring, so it is
    a different object from the endset and has a node of its own.  It is
    built over the module homsets, which is where its elements and its two
    ends come from.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "module automorphism groups"

    def super_categories(self) -> list:
        return [OwnedModules(self.base_ring()).Homsets()]

    class ParentMethods(AutomorphismSubgroup):
        r"""The automorphism group, or a finite subgroup with the same elements."""

        Element = ModuleAutomorphism

        def conjugacy_classes_representatives(
            self,
        ) -> tuple[ModuleAutomorphism, ...]:
            r"""Return this group's representatives in character-table order."""
            by_matrix = self._by_matrix()
            representatives = []
            engine_group = self._defining_matrix_group()
            for representative in engine_group.conjugacy_classes_representatives():
                coordinates = matrix(representative.matrix())
                coordinates.set_immutable()
                representatives.append(by_matrix.get(coordinates))
            representatives = tuple(representatives)
            assert all(
                representative is not None for representative in representatives
            ), "the matrix model does not present this automorphism subgroup"
            return representatives

        def irreducible_characters(self) -> tuple[Character, ...]:
            r"""Return the absolutely irreducible characters of this group."""
            engine_group = self._defining_matrix_group()
            return tuple(
                Character(
                    class_function,
                    self,
                    element_argument=lambda element: engine_group(element.matrix()),
                )
                for class_function in engine_group.irreducible_characters()
            )

        def character(self, values: "OrderedSet") -> Character:
            r"""Return the character with the stated conjugacy-class values."""
            class_function = self._defining_matrix_group().character(list(values))
            return Character(
                class_function,
                self,
                element_argument=lambda element: self._defining_matrix_group()(element.matrix()),
            )

        def trivial_character(self) -> Character:
            r"""Return the trivial character of this group."""
            class_function = self._defining_matrix_group().trivial_character()
            return Character(
                class_function,
                self,
                element_argument=lambda element: self._defining_matrix_group()(element.matrix()),
            )

        if TYPE_CHECKING:
            # The elements here are automorphisms, narrower than the module
            # morphisms the module homsets bind.  The conversion is provided by
            # this homset's element constructor.
            def __call__(
                self,
                x: ElementConstructorInput = ...,
                *args: ElementConstructorInput,
                **kwds: ElementConstructorInput,
            ) -> ModuleAutomorphism: ...

        def __init__(
            self,
            module: "Module",
            group_generators: "OrderedSet | None" = None,
            **rest: "ModuleMorphismData",
        ) -> None:
            rest["category"] = OwnedModules(module.base_ring())
            super().__init__(domain=module, codomain=module, **rest)
            from dzack_research.preamble.categories.group.groups import OwnedGroups

            refine(
                self,
                [ModuleAutomorphismGroups(module.base_ring()), OwnedGroups()],
            )
            self._supergroup = self
            self._group_generators = None
            self._elements = None
            if group_generators is not None:
                supplied = tuple(group_generators)
                assert supplied, "a generated subgroup needs at least one generator"
                assert all(
                    isinstance(generator, ModuleAutomorphism)
                    for generator in supplied
                ), "subgroup generators must be module automorphisms"
                self._group_generators = tuple(
                    self(generator.module_generator_morphism())
                    for generator in supplied
                )
                self._elements = self._close()

        def supergroup(self) -> "Group":
            return self._supergroup

        def _element_constructor_(
            self,
            images: "ModuleMorphismData",
        ) -> ModuleAutomorphism:
            return ModuleAutomorphism(self, images)

        def one(
            self,
        ) -> ModuleAutomorphism:
            return self(self.domain().module_generator_morphism())

        def subgroup_on(
            self,
            group_generators: "Set",
        ) -> "ModuleAutomorphismGroup":
            r"""Return the subgroup generated by a *set* of automorphisms."""
            assert all(generator in self for generator in group_generators), (
                "each subgroup generator must belong to this automorphism group"
            )
            subgroup = ModuleAutomorphismGroup(self.domain(), group_generators)
            subgroup._supergroup = self
            # Local: a module-level import would close a cycle; the module is
            # built by the time this runs.
            from dzack_research.preamble.categories.group.groups import OwnedGroups

            return refine(subgroup, OwnedGroups().Subobjects())

        def group_generators(
            self,
        ) -> "OrderedSet[ModuleAutomorphism]":
            generators: "OrderedSet[ModuleAutomorphism]" = (
                finite_ordered_set(())
                if self._group_generators is None
                else finite_ordered_set(self._group_generators)
            )
            return generators

        def is_finite(self) -> bool:
            return self._elements is not None

        def order(self) -> "Cardinal":
            r"""Return \(|G|\), the cardinality of this group.

            A cardinality, not an integer: \(\operatorname{Aut}(M)\) for a free
            \(M\) of rank \(\ge 2\) over \(\mathbb Z\) is
            \(\mathrm{GL}_n(\mathbb Z)\), which is infinite.  Refusing to answer
            there would be assuming finiteness of a group that simply is not
            finite; the order is \(\aleph_0\) and saying so costs nothing.
            """
            if self._elements is None:
                return Sets.ℵ[0]
            return cardinal(len(self._elements))

        def __iter__(self) -> Iterator[ModuleAutomorphism]:
            assert self._elements is not None, (
                "the full automorphism group is not enumerable"
            )
            return iter(self._elements)

        def __contains__(self, element: ElementConstructorInput) -> bool:
            return (
                isinstance(element, ModuleAutomorphism)
                and element.parent() is self
            )

        def _close(
            self,
        ) -> tuple[ModuleAutomorphism, ...]:
            identity = self.one()
            elements = set((identity,))
            frontier = [identity]
            steps = 0
            assert self._group_generators is not None
            while frontier:
                current = frontier.pop()
                for generator in self._group_generators:
                    for factor in (generator, generator.inverse()):
                        candidate = current * factor
                        if candidate in elements:
                            continue
                        elements.add(candidate)
                        frontier.append(candidate)
                        steps += 1
                        assert steps <= 100000, (
                            "the proposed subgroup has not closed after 100000 elements"
                        )
            return tuple(elements)

        def _repr_(self) -> str:
            if self.is_finite():
                return f"Subgroup of Aut({self.domain()}) of order {self.order()}"
            return f"Aut({self.domain()})"

def ModuleAutomorphismGroup(
    module: "Module",
    group_generators: "OrderedSet | None" = None,
) -> Parent:
    r"""Return $\operatorname{Aut}_R(M)$, or the subgroup ``group_generators`` spans."""
    return object_of(
        ModuleAutomorphismGroups(module.base_ring()),
        module=module,
        group_generators=group_generators,
    )


class GroupAction(Morphism):
    r"""Construction class for \(\rho:G\to\operatorname{Aut}_R(M)\)."""

    if TYPE_CHECKING:
        def parent(self) -> "GroupActionHomset": ...


class GroupActionHomsets(Category):
    r"""Homsets \(\operatorname{Hom}(G,\operatorname{Aut}_R(M))\)."""

    def super_categories(self) -> list:
        from dzack_research.preamble.categories.group.groups import OwnedGroups

        return [OwnedGroups().Homsets()]

    class ParentMethods:
        def module(self) -> "Module":
            r"""Return the module acted on by this homset's codomain."""
            return self.codomain().domain()

        def __call__(self, images: "OrderedSet | dict") -> "GroupAction":
            return self._element_constructor_(images)

        def _element_constructor_(self, images: "OrderedSet | dict") -> "GroupAction":
            match images:
                case dict():
                    return self.element_class(self, images)
                case _:
                    values = self._values_on_generators(tuple(images))
                    return self.element_class(self, values)

        def _values_on_generators(
            self,
            images: "OrderedSet[ModuleAutomorphism]",
        ) -> dict[MultiplicativeGroupElement, ModuleAutomorphism]:
            r"""Extend generator images across a finite group."""
            group = self.domain()
            assert group.is_finite(), (
                "extension from generator images requires a finite group"
            )
            automorphisms = self.codomain()
            generators = tuple(group.group_generators())
            assert len(images) == len(generators), (
                f"{group} has {len(generators)} generators, got {len(images)} images"
            )
            assert all(image in automorphisms for image in images), (
                "each image belongs to the stated automorphism group"
            )
            values = {group.one(): automorphisms.one()}
            frontier = [group.one()]
            while frontier:
                current = frontier.pop()
                for generator, image in zip(generators, images, strict=True):
                    product = current * generator
                    candidate = values[current] * image
                    if product in values:
                        assert values[product] == candidate, (
                            "the images do not respect the relations of the group"
                        )
                    else:
                        values[product] = candidate
                        frontier.append(product)
            return values

        def __contains__(self, action: "ElementConstructorInput") -> bool:
            return isinstance(action, GroupAction) and action.parent() is self

    class ElementMethods:
        def __init__(
            self,
            parent: "GroupActionHomset",
            values: dict[MultiplicativeGroupElement, ModuleAutomorphism],
        ) -> None:
            super().__init__(parent)
            group = parent.domain()
            automorphisms = parent.codomain()
            values = {
                group_element: (
                    value
                    if value in automorphisms
                    else automorphisms(value.module_generator_morphism())
                )
                for group_element, value in values.items()
            }
            assert all(value in automorphisms for value in values.values()), (
                "each action value belongs to the stated automorphism group"
            )
            from dzack_research.preamble.categories.group.groups import OwnedFinitelyGeneratedGroups

            if group in OwnedFinitelyGeneratedGroups():
                assert set(group.group_generators()) <= set(values), (
                    "the action names the image of each group generator"
                )
            self._values = dict(values)

        def _call_(self, element: "ElementConstructorInput") -> ModuleAutomorphism:
            r"""Return \(\rho(g)\) where the defining assignment names it."""
            assert element in self.values(), (
                f"the action has no stated value at {element}; computing one "
                f"requires a word for it in {self.domain()}"
            )
            return self.values()[element]

        def values(
            self,
        ) -> dict[MultiplicativeGroupElement, ModuleAutomorphism]:
            r"""Return the defining values of this action."""
            return dict(self._values)

        def is_injective(self) -> bool:
            r"""Return whether the stated values define a faithful action."""
            values = self.values()
            return len(set(values.values())) == len(values)

        def __eq__(self, other: "ElementConstructorInput") -> bool:
            return (
                isinstance(other, GroupAction)
                and self.domain() == other.domain()
                and self.codomain() == other.codomain()
                and self.values() == other.values()
            )

        def __hash__(self) -> int:
            return hash((type(self), self.domain(), self.codomain()))


class GroupActionHomset(GroupActionHomsetBase):
    r"""Homomorphisms from a group to the automorphisms of one module."""

    Element = GroupAction

    if TYPE_CHECKING:
        # An action goes from a group to the automorphism group of the
        # module; ``Homset`` states only that both are parents.  Declared,
        # never defined: the inherited implementations are the ones that run.
        def domain(self) -> "Group": ...
        def codomain(self) -> "ModuleAutomorphismGroup": ...

    def __init__(
        self,
        group: "Group",
        module: "Module",
        automorphism_group: "Parent | None" = None,
    ) -> None:
        from dzack_research.preamble.categories.group.groups import refine_group

        group = refine_group(group)
        if automorphism_group is None:
            automorphism_group = module.Aut()
        assert automorphism_group.domain() is module, (
            "the automorphism group must act on the stated module"
        )
        Homset.__init__(
            self,
            group,
            automorphism_group,
            category=Groups(),
            check=False,
        )
        refine(self, GroupActionHomsets())


def group_action_homset(
    group: "Group",
    module: "Module",
    automorphism_group: "Parent | None" = None,
) -> GroupActionHomset:
    r"""Return \(\operatorname{Hom}(G,\operatorname{Aut}_R(M))\)."""
    return GroupActionHomset(group, module, automorphism_group)


class AutomorphismSubgroupInclusion(GroupAction):
    r"""The canonical monomorphism from a subgroup into \(\operatorname{Aut}(M)\)."""

    def __init__(self, parent: GroupActionHomset) -> None:
        Morphism.__init__(self, parent)

    def _call_(self, element: ElementConstructorInput) -> ModuleAutomorphism:
        assert element in self.domain(), f"{element} is not in {self.domain()}"
        module = self.codomain().domain()
        return self.codomain()(
            {
                label: element(module.module_generator(label))
                for label in module.module_generating_set()
            }
        )

    def is_injective(self) -> bool:
        return True

    def values(self) -> dict[MultiplicativeGroupElement, ModuleAutomorphism]:
        return {
            group_generator: self(group_generator)
            for group_generator in self.domain().group_generators()
        }

    def __eq__(self, other: ElementConstructorInput) -> bool:
        return (
            isinstance(other, AutomorphismSubgroupInclusion)
            and other.parent() is self.parent()
        )

    def __hash__(self) -> int:
        return hash((type(self), id(self.parent())))


def _solve_left_integrally(
    system: Matrix, target: "Vector", ring: "Ring"
) -> "Vector":
    r"""Return a solution of \(aS=t\) over ``ring``, or fail.

    The caller hands over a morphism matrix -- the matrix of the morphism
    being lifted along, stacked with the codomain's relations -- the
    coordinate vector of the element to hit (not the module it lies in), and
    the engine view of the domain's base ring, which is where the Smith form
    and the divisibility questions live: over a field every nonzero pivot
    divides, over \(\mathbb Z\) divisibility is the integrality condition.
    """
    # The Smith factors act here on coordinate vectors, not on framings: a
    # morphism matrix times a vector is not a morphism matrix, so this solve
    # runs on coordinate vectors in the module's base ring.
    smith, left, right = system.transpose().smith_form()
    shifted = left * vector(ring, target)
    width = smith.ncols()
    solution = [ring.zero()] * width
    for index, value in enumerate(shifted):
        divisor = smith[index, index] if index < width else ring.zero()
        assert divisor != 0 or value == 0, (
            f"no solution: row {index} is zero but asks for {value}"
        )
        if divisor != 0:
            assert divisor.divides(value), (
                f"no solution over {ring}: row {index} asks for "
                f"{value}/{divisor}"
            )
            solution[index] = ring(value / divisor)
    return right * vector(ring, solution)
