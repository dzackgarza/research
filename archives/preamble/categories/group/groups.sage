r"""Owned categories of groups."""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.structure.parent import ElementConstructorInput, MembershipInput
    from dzack_research.preamble.categories.sets.cardinals import Cardinal
    from sage.categories.groups import Group, GroupElement
    from sage.categories.rings import Ring
    from dzack_research.preamble.lexicon import CartanType, Matrix
    from dzack_research.preamble.lexicon import OrderedSet

if TYPE_CHECKING:
    from typing import Callable
    from sage.rings.integer import Integer
    from dzack_research.preamble.owned_category import ConstructionData

from dzack_research.preamble.categories.sets.owned_sets import Sets
if TYPE_CHECKING:
    from sage.categories.morphism import Morphism
    from sage.libs.gap.element import GapElement
    from dzack_research.preamble.categories.group.group_morphisms import (
        GroupAutomorphismGroup,
        GroupHomomorphism,
        GroupHomset,
    )

from typing import Self

from sage.misc.cachefunc import cached_method
from dzack_research.preamble.owned_category_bases import (
    Category,
    HomCategoryConstruction,
    SubobjectsCategory,
)
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups
from sage.categories.finite_groups import FiniteGroups as SageFiniteGroups
from sage.categories.groups import Groups as SageGroups
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.rings import Rings
from sage.groups.abelian_gps.abelian_group import AbelianGroup_class
from sage.groups.abelian_gps.element_base import AbelianGroupElementBase
from sage.groups.finitely_presented import FinitelyPresentedGroup
from sage.groups.free_group import FreeGroup_class
from sage.groups.libgap_wrapper import ParentLibGAP
from sage.groups.matrix_gps.finitely_generated import (
    FinitelyGeneratedMatrixGroup_generic,
)
from sage.groups.matrix_gps.finitely_generated_gap import (
    FinitelyGeneratedMatrixGroup_gap,
)
from sage.groups.matrix_gps.coxeter_group import CoxeterMatrixGroup
from sage.groups.matrix_gps.named_group import NamedMatrixGroup_generic
from sage.groups.matrix_gps.named_group_gap import NamedMatrixGroup_gap
from sage.groups.perm_gps.permgroup import PermutationGroup_generic
from sage.groups.perm_gps.permgroup_named import AlternatingGroup
from sage.groups.perm_gps.permgroup_named import SymmetricGroup
from sage.libs.gap.libgap import libgap
from sage.misc.unknown import Unknown
from dzack_research.preamble.categories.rings.rings import OwnedRings, ℤ
from dzack_research.preamble.owned_category import object_of
from sage.rings.infinity import infinity
from sage.rings.integer_ring import ZZ as SageZZ
from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet
from sage.structure.element import Element, RingElement
from sage.structure.parent import Parent


class SubgroupInclusion(SetMorphism):
    r"""The canonical inclusion homomorphism \(H\hookrightarrow G\)."""

    def is_injective(self) -> bool:
        return True


def _group_inclusion_image(
    subgroup: "Group",
    containing_group: "Group",
    element: "GroupElement",
) -> "GroupElement":
    r"""Return the element as an element of the containing group."""
    if element.parent() is containing_group:
        return element
    if isinstance(element, AbelianGroupElementBase):
        image = containing_group.one()
        for group_generator, exponent in zip(
            subgroup.gens(),
            element.exponents(),
            strict=True,
        ):
            image *= group_generator**exponent
        return image
    return containing_group(element)


def _canonical_subgroup_inclusion(subgroup: "Group") -> SetMorphism:
    r"""Return \(\iota:H\hookrightarrow G\), the arrow \(H\) is a subgroup by.

    One implementation for the two levels that name it: the owned groups node,
    where every group has it and a group naming no containing group is a
    subgroup of itself by the identity, and the subobject construction, where
    it is the datum the construction is about.  A group whose presentation
    determines its own arrow -- a subgroup of \(\operatorname{Aut}(M)\), whose
    inclusion *is* the representation \(\rho\) -- names it and that one is
    returned.
    """
    containing_group = subgroup.supergroup()
    if hasattr(subgroup, "automorphism_subgroup_inclusion"):
        return subgroup.automorphism_subgroup_inclusion()
    # In the owned category, because both ends are owned groups: an object
    # reached only through the owned tree -- a predicate subgroup among them --
    # is in no Sage group category at all, and asking for the homset there
    # refuses it.
    return SubgroupInclusion(
        Hom(subgroup, containing_group, OwnedGroups()),
        lambda element: _group_inclusion_image(
            subgroup,
            containing_group,
            element,
        ),
    )


if TYPE_CHECKING:
    from typing import Protocol

    class GroupParent(Protocol):
        r"""What a group parent has from its placement: an identity, supplied
        by Sage's ``Groups().ObjectType``."""

        _group_generators: "OrderedSet"

        def one(self) -> "GroupElement": ...


def _owned_group_constructor(
    constructor: "Callable[..., Group]",
) -> "staticmethod[..., Group]":
    r"""Return Sage's constructor with its result refined as a group here."""
    from functools import wraps

    @wraps(constructor)
    def construct(
        *arguments: "ElementConstructorInput",
        **keywords: "ElementConstructorInput",
    ) -> "Group":
        return refine_group(constructor(*arguments, **keywords))

    return staticmethod(construct)


def _group_over_engine_ring(
    constructor: "Callable[..., Group]",
    degree: "Integer",
    ring: "Ring",
    *arguments: "ElementConstructorInput",
    **keywords: "ElementConstructorInput",
) -> "Group":
    r"""Construct through Sage using the engine view of the scalar ring."""
    from dzack_research.preamble.categories.rings.rings import engine_ring

    return refine_group(
        constructor(degree, engine_ring(ring), *arguments, **keywords)
    )


def _GL(degree: "Integer", ring: "Ring", var: str = "a") -> "Group":
    r"""Return \(GL_{\mathrm{degree}}(\mathrm{ring})\)."""
    from sage.groups.matrix_gps.catalog import GL
    return _group_over_engine_ring(GL, degree, ring, var=var)


def _SL(degree: "Integer", ring: "Ring", var: str = "a") -> "Group":
    r"""Return \(SL_{\mathrm{degree}}(\mathrm{ring})\)."""
    from sage.groups.matrix_gps.catalog import SL
    return _group_over_engine_ring(SL, degree, ring, var=var)


def _Sp(
    degree: "Integer",
    ring: "Ring",
    var: str = "a",
    invariant_form: "Matrix | None" = None,
) -> "Group":
    r"""Return the symplectic group over ``ring`` in the selected degree."""
    from sage.groups.matrix_gps.catalog import Sp
    return _group_over_engine_ring(
        Sp, degree, ring, var=var, invariant_form=invariant_form
    )


def _GU(
    degree: "Integer",
    ring: "Ring",
    var: str = "a",
    invariant_form: "Matrix | None" = None,
) -> "Group":
    r"""Return the general unitary group over ``ring`` in the selected degree."""
    from sage.groups.matrix_gps.catalog import GU
    return _group_over_engine_ring(
        GU, degree, ring, var=var, invariant_form=invariant_form
    )


def _SU(
    degree: "Integer",
    ring: "Ring",
    var: str = "a",
    invariant_form: "Matrix | None" = None,
) -> "Group":
    r"""Return the special unitary group over ``ring`` in the selected degree."""
    from sage.groups.matrix_gps.catalog import SU
    return _group_over_engine_ring(
        SU, degree, ring, var=var, invariant_form=invariant_form
    )


def _GO(
    degree: "Integer",
    ring: "Ring",
    e: "Integer" = 0,
    var: str = "a",
    invariant_form: "Matrix | None" = None,
) -> "Group":
    r"""Return the general orthogonal group over ``ring`` in the selected degree."""
    from sage.groups.matrix_gps.catalog import GO
    return _group_over_engine_ring(
        GO, degree, ring, e=e, var=var, invariant_form=invariant_form
    )


def _SO(
    degree: "Integer",
    ring: "Ring",
    e: "Integer | None" = None,
    var: str = "a",
    invariant_form: "Matrix | None" = None,
) -> "Group":
    r"""Return the special orthogonal group over ``ring`` in the selected degree."""
    from sage.groups.matrix_gps.catalog import SO
    return _group_over_engine_ring(
        SO, degree, ring, e=e, var=var, invariant_form=invariant_form
    )


def _Affine(degree: "Integer", ring: "Ring") -> "Group":
    r"""Return the affine group over ``ring`` in the selected degree."""
    from sage.groups.affine_gps.catalog import Affine
    return _group_over_engine_ring(Affine, degree, ring)


def _Euclidean(degree: "Integer", ring: "Ring") -> "Group":
    r"""Return the Euclidean group over ``ring`` in the selected degree."""
    from sage.groups.affine_gps.catalog import Euclidean
    return _group_over_engine_ring(Euclidean, degree, ring)


def _SemimonomialTransformation(ring: "Ring", degree: "Integer") -> "Group":
    r"""Return the semimonomial transformation group over ``ring``."""
    from dzack_research.preamble.categories.rings.rings import engine_ring
    from sage.groups.misc_gps.misc_groups_catalog import SemimonomialTransformation

    return refine_group(SemimonomialTransformation(engine_ring(ring), degree))


def _Heisenberg(degree: "Integer" = 1, ring: "Ring | Integer" = 0) -> "Group":
    r"""Return the Heisenberg group over ``ring`` in the selected degree."""
    from dzack_research.preamble.categories.rings.rings import engine_ring
    from sage.groups.matrix_gps.catalog import Heisenberg

    scalar_ring = ring if ring == 0 else engine_ring(ring)
    return refine_group(Heisenberg(degree, scalar_ring))


def _SmallGroup(order: "Integer", index: "Integer") -> "Group":
    r"""Return the group ``SmallGroup(order, index)`` of GAP's small-groups library.

    The library (Besche--Eick--O'Brien, reached through GAP's ``SmallGroup``)
    catalogues the groups of each admitted order up to isomorphism, and
    ``index`` selects one isomorphism class; GAP validates both arguments.
    GAP hands back a pc-presented model, which is normalized here to a
    permutation group through ``IsomorphismPermGroup`` -- so the intake
    models the catalogued group up to isomorphism, the same contract as the
    normalizing arms of ``_gap_model``.
    """
    from sage.groups.perm_gps.permgroup import PermutationGroup

    permutation_model = libgap.SmallGroup(order, index).IsomorphismPermGroup().Image()
    return refine_group(PermutationGroup(gap_group=permutation_model))


def _Coxeter(
    data: "CartanType | Matrix | str",
    implementation: str = "reflection",
    base_ring: "Ring | None" = None,
    index_set: "OrderedSet | None" = None,
) -> "Group":
    r"""Return the Coxeter group for ``data`` through Sage's constructor."""
    from dzack_research.preamble.categories.rings.rings import engine_ring
    from sage.groups.misc_gps.misc_groups_catalog import CoxeterGroup

    scalar_ring = None if base_ring is None else engine_ring(base_ring)
    return refine_group(
        CoxeterGroup(
            data,
            implementation=implementation,
            base_ring=scalar_ring,
            index_set=index_set,
        )
    )


def _finiteness(group: "Group") -> "bool | Unknown":
    r"""Return whether ``group`` is finite, as a value.

    The group's own answer wherever it has one, so a category that decides
    finiteness -- ``LatticeIsometries`` puts the question to GAP -- is the one
    that answers.  A group placed in no owned category has not got
    :meth:`OwnedGroups.ObjectType.is_finite` yet, which is why the decline
    is caught here too.
    """
    if group in SageFiniteGroups() or group in OwnedFiniteGroups():
        return True
    return Unknown


class OwnedGroups(Category):
    r"""Groups whose notebook-facing methods are owned by the preamble.

    This category does not choose additive or multiplicative notation.  Sage's
    ``Groups`` category is a category of multiplicatively written groups, while
    a module is an additively written group.  Both are groups.  Each concrete
    realization keeps its notation and supplies its operation there.

    The class is also the flat catalogue of standard groups.  Tab completion
    on ``Groups.`` shows the available families.  The constructors ``C(n)``,
    ``S(n)``, ``A(n)``, and ``D(n)`` return \(C_n\), \(S_n\), \(A_n\), and
    \(D_n\), where \(|D_n|=2n\).  Matrix groups keep their standard names and
    signatures, such as ``GL(n, R)`` and ``Sp(n, R)``.
    """

    from sage.groups.lie_gps.catalog import Nilpotent as _SageNilpotent
    from sage.groups.misc_gps.misc_groups_catalog import (
        Artin as _SageArtin,
        Braid as _SageBraid,
        Cactus as _SageCactus,
        Free as _SageFree,
        PureCactus as _SagePureCactus,
        ReflectionGroup as _SageReflection,
        RightAngledArtin as _SageRightAngledArtin,
        WeylGroup as _SageWeyl,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        ComplexReflection as _SageComplexReflection,
        Janko as _SageJanko,
        Mathieu as _SageMathieu,
        PGL as _SagePGL,
        PGU as _SagePGU,
        PSL as _SagePSL,
        PSp as _SagePSp,
        PSU as _SagePSU,
        RubiksCube as _SageRubiksCube,
        Suzuki as _SageSuzuki,
        SuzukiSporadic as _SageSuzukiSporadic,
        Transitive as _SageTransitive,
    )
    from sage.groups.perm_gps.permgroup_named import (
        AlternatingGroup as _SageAlternatingGroup,
        CyclicPermutationGroup as _SageCyclicGroup,
        DiCyclicGroup as _SageDiCyclicGroup,
        DihedralGroup as _SageDihedralGroup,
        KleinFourGroup as _SageKleinFourGroup,
        QuaternionGroup as _SageQuaternionGroup,
        SymmetricGroup as _SageSymmetricGroup,
    )
    from sage.groups.abelian_gps.abelian_group import AbelianGroup as _SageAbelianGroup

    C = _owned_group_constructor(_SageCyclicGroup)
    S = _owned_group_constructor(_SageSymmetricGroup)
    A = _owned_group_constructor(_SageAlternatingGroup)
    D = _owned_group_constructor(_SageDihedralGroup)
    Dic = _owned_group_constructor(_SageDiCyclicGroup)
    Q = _owned_group_constructor(_SageQuaternionGroup)
    V4 = _owned_group_constructor(_SageKleinFourGroup)

    Abelian = _owned_group_constructor(_SageAbelianGroup)
    Free = _owned_group_constructor(_SageFree)
    Artin = _owned_group_constructor(_SageArtin)
    Braid = _owned_group_constructor(_SageBraid)
    Cactus = _owned_group_constructor(_SageCactus)
    PureCactus = _owned_group_constructor(_SagePureCactus)
    Coxeter = staticmethod(_Coxeter)
    Weyl = _owned_group_constructor(_SageWeyl)
    Reflection = _owned_group_constructor(_SageReflection)
    RightAngledArtin = _owned_group_constructor(_SageRightAngledArtin)

    GL = staticmethod(_GL)
    SL = staticmethod(_SL)
    Sp = staticmethod(_Sp)
    GU = staticmethod(_GU)
    SU = staticmethod(_SU)
    GO = staticmethod(_GO)
    SO = staticmethod(_SO)
    Heisenberg = staticmethod(_Heisenberg)
    SemimonomialTransformation = staticmethod(_SemimonomialTransformation)

    Affine = staticmethod(_Affine)
    Euclidean = staticmethod(_Euclidean)
    Nilpotent = _owned_group_constructor(_SageNilpotent)
    SmallGroup = staticmethod(_SmallGroup)

    ComplexReflection = _owned_group_constructor(_SageComplexReflection)
    Mathieu = _owned_group_constructor(_SageMathieu)
    Janko = _owned_group_constructor(_SageJanko)
    Suzuki = _owned_group_constructor(_SageSuzuki)
    SuzukiSporadic = _owned_group_constructor(_SageSuzukiSporadic)
    PGL = _owned_group_constructor(_SagePGL)
    PSL = _owned_group_constructor(_SagePSL)
    PSp = _owned_group_constructor(_SagePSp)
    PGU = _owned_group_constructor(_SagePGU)
    PSU = _owned_group_constructor(_SagePSU)
    Transitive = _owned_group_constructor(_SageTransitive)
    RubiksCube = _owned_group_constructor(_SageRubiksCube)

    @classmethod
    def _repr_object_names(cls) -> str:
        return "groups"

    def super_categories(self) -> list:
        # Seated over the owned Monoids node (user ruling 2026-08-19): a
        # group is a monoid with inverses, and the owned operation spine
        # Magmas -> Semigroups -> Monoids in ``magmas.sage`` is where
        # operation-level declarations file.  ``Sets()`` stays reachable
        # through the spine.
        from dzack_research.preamble.categories.group.magmas import Monoids as OwnedMonoids

        # Sage's ``Groups()`` beside the spine, the way the spine itself seats
        # each owned node over Sage's (``Monoids -> [SageMonoids(), ...]``).
        # Without it an owned group was a Sage *monoid* and not a Sage group,
        # so $O(L)$ -- which is one -- failed ``in Groups()`` while answering
        # its order.
        return [SageGroups(), OwnedMonoids()]

    class ParentMethods:
        def _subgroup_inclusion(self: Self) -> SetMorphism:
            r"""Construct the inclusion from this subgroup's containing group."""
            return _canonical_subgroup_inclusion(self)

        def is_finitely_generated(self: Self) -> "bool | Unknown":
            r"""Return whether \(G\) admits a finite generating set.

            Total: ``True``, ``False``, or ``Unknown``, never an exception.
            Sage answers this with two different exception types -- no such
            method, and a method that declines to decide -- and neither
            carries mathematics, so callers would have to catch to learn
            what is true.

            Layered, because no single signal is sound.  Sage's
            ``FinitelyGenerated`` is a declaration rather than a decision, so
            its ``True`` is evidence and its ``False`` is not: the free group
            on two generators stands outside it.  A finite group generates
            itself.  Failing both, the group is asked, and if it cannot say,
            the answer is ``Unknown``.
            """
            if self in SageGroups().FinitelyGenerated():
                return True
            if _finiteness(self) is True:
                return True
            if self.is_arithmetic_group() is True:
                return True
            return Unknown

        def is_arithmetic_group(self: Self) -> "bool | Unknown":
            r"""Return whether \(G\) is the \(\ZZ\)-points of an algebraic group.

            Arithmetic groups are finitely generated -- Borel and
            Harish-Chandra -- and that theorem is the only evidence available
            for \(Sp_{2n}(\ZZ)\), whose generating set Hua and Reiner exhibit
            and Sage cannot produce.

            The witness is a *named* classical group, one carrying a degree
            and a ring rather than a list of generators, whose scalars are the
            integers: \(SL_n\), \(GL_n\), \(Sp_{2n}\) and \(O(q)\) over
            \(\ZZ\) are each the integral points of a linear algebraic group
            defined over \(\QQ\).  Over any other ring the construction says
            nothing -- \(SO_3(\QQ)\) is not arithmetic and not finitely
            generated -- so the answer is ``Unknown`` and not ``False``: a
            group Sage built some other way may be arithmetic, and nothing
            here decides it.
            """
            if (
                isinstance(self, NamedMatrixGroup_generic)
                and self.base_ring() is SageZZ
            ):
                return True
            return Unknown

        def End(self: Self) -> "GroupHomset":
            r"""Return \(\operatorname{End}(G)=\operatorname{Hom}(G,G)\).

            The endset, which is where \(\operatorname{Aut}(G)\) comes from:
            an automorphism is an invertible endomorphism, so the group is
            the units of this monoid.  Sited here and not built here -- an
            endset is the homset whose two objects coincide, and asking for
            it any other way would produce a second object with the same
            elements.

            Reached through the owned homset constructor rather than by
            re-routing ``Hom`` on this category: the owned module tree seats
            its finitely presented torsion modules in the abelian-groups
            node, and those objects' ``Hom`` is the module homset their own
            categories supply.  The group placement adds group vocabulary; it
            never re-routes module morphisms.
            """
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.group.group_morphisms import (
                group_homset,
            )

            return group_homset(self, self)

        @cached_method
        def Aut(self: Self) -> "GroupAutomorphismGroup":
            r"""Return \(\operatorname{Aut}(G)\), the units of \(\operatorname{End}(G)\).

            One object, reached one way, and cached on the parent so a
            generating set computed once stays computed.
            \(\operatorname{Aut}(G)\) exists for every group; what some
            groups lack is an algorithm, and that absence is stated where it
            is met, at the engine.

            Finiteness is claimed exactly when the group itself is decidably
            finite: an automorphism permutes the underlying finite set, so
            \(\operatorname{Aut}(G)\le\operatorname{Sym}(G)\) is finite with
            \(G\).  Nothing stronger is claimed -- finite presentation of
            \(\operatorname{Aut}(F_2)\) is a theorem this method does not
            state.
            """
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.group.group_morphisms import (
                GroupAutomorphismGroup,
            )
            from dzack_research.preamble.refine import refine

            automorphisms = GroupAutomorphismGroup(self)
            placements: list[Category] = [OwnedGroups()]
            if _finiteness(self) is True:
                placements.append(OwnedFiniteGroups())
            refine(automorphisms, placements)
            return automorphisms

        def is_isomorphic_to(self: Self, other: "Group") -> "bool | Unknown":
            r"""Return whether \(G\cong H\) as groups, as a value.

            One spelling across every owned presentation: two finite groups
            given as permutation groups, finitely presented groups, abelian
            groups, or matrix groups are compared through their GAP models,
            so the question does not depend on which constructor built each
            side.  Decided by GAP's ``IsomorphismGroups``, which searches for
            an isomorphism and answers ``fail`` when none exists -- a
            decision procedure for finite groups, and the same engine Sage's
            ``PermutationGroup_generic.is_isomorphic`` calls.

            Groups not decidably finite answer ``Unknown``: the isomorphism
            problem for finitely presented groups is undecidable
            (Adian--Rabin), so no loop or bounded probe stands in for the
            missing algorithm, and ``Unknown`` is not ``False`` -- nothing
            here decides the infinite case either way.
            """
            if _finiteness(self) is not True or _finiteness(other) is not True:
                return Unknown
            found = _gap_model(self).IsomorphismGroups(_gap_model(other))
            return str(found) != "fail"

    class _HomCategory(HomCategoryConstruction):
        r"""Homsets of groups and their homomorphisms."""

        class ElementMethods:
            def image(self: "GroupHomomorphism") -> "Group":
                r"""Return \(\operatorname{im}(f)\leq H\)."""
                from dzack_research.preamble.categories.group.group_morphisms import (
                    GroupAutomorphismGroup,
                )

                engine_image = self.gap().Image()
                codomain = self.codomain()
                match codomain:
                    case GroupAutomorphismGroup():
                        return codomain._subgroup_from_engine(engine_image)
                    case _:
                        subgroup: "Group" = codomain._subgroup_constructor(
                            engine_image
                        )
                        return subgroup

    class Subobjects(SubobjectsCategory):
        r"""Subgroups: a group \(H\) and a monomorphism \(\iota:H\hookrightarrow G\).

        \(G\) is ``inclusion().codomain()``, so no subgroup records it a
        second time.  What this level states past the bare subobject is that
        \(\iota\) is a homomorphism: \(H\) is closed under the operation and
        under inverses, and \(1_H=1_G\).  That is why the arrow alone decides
        membership, and why nothing has to be enumerated to get it.

        Order, finite generation and a generating set are no part of being a
        subgroup and are not asserted here.  A subgroup of \(O(L)\) is the
        case that forbids asserting them: computing a generating set of
        \(O(L)\) for a common indefinite \(L\) runs for days, while deciding
        \(f\in H\) is always available.

        The axiom subcategories -- :class:`OwnedFinitelyGeneratedGroups`,
        :class:`OwnedFinitelyPresentedGroups`, :class:`OwnedFiniteGroups` --
        declare no ``Subobjects`` of their own and must not.  Each reaches
        this one through ``super_categories()``, which is the whole
        statement: an axiom is a property of the group already there, so a
        subgroup of a finite group is a subgroup that is finite, not a second
        construction.
        """

        class ParentMethods:
            def inclusion(self: Self) -> SetMorphism:
                r"""Return \(\iota:H\hookrightarrow G\), the datum of this level.

                Named here and not left to the owned groups node above:
                :class:`SubobjectsCategory` declares ``inclusion`` abstract,
                and a construction category's own declaration precedes its
                supercategory's implementation, so a subgroup would answer
                nothing for the one arrow it is defined by.  The owned groups
                node keeps the same arrow for a group reached outside this
                construction, and both call one implementation.
                """
                return self._subgroup_inclusion()


class OwnedFinitelyGeneratedGroups(Category):
    r"""Groups admitting a surjection \(F(S)\twoheadrightarrow G\), \(S\) finite.

    Finite generation is witnessed by such a surjection.  It is not witnessed
    by an arbitrary stored list of elements.  The kernel of this surjection
    occurs in the definition of finite presentation.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely generated groups"

    def super_categories(self) -> list:
        return [OwnedGroups()]

    class ParentMethods:
        def is_finitely_generated(self: Self) -> bool:
            r"""Return ``True`` because membership states this property."""
            return True

        def group_generators(self: "GroupParent") -> "OrderedSet":
            r"""Return the finite generating set supplied by the construction."""
            return self._group_generators

        def number_of_group_generators(self: "GroupParent") -> "Cardinal":
            r"""Return the cardinality of the specified finite generating set."""
            from dzack_research.preamble.categories.sets.cardinals import cardinal

            return cardinal(self.group_generators().cardinality())

        def conjugation_morphism(self: "GroupParent") -> "GroupHomomorphism":
            r"""Return the conjugation representation on the specified generators."""
            from dzack_research.preamble.categories.group.group_morphisms import (
                _element_to_engine,
                group_homset,
            )

            automorphisms = self.Aut()
            model = _gap_model(self)
            images = {
                generator: automorphisms(
                    libgap.ConjugatorAutomorphism(
                        model, _element_to_engine(self, generator)
                    )
                )
                for generator in self.group_generators()
            }
            return group_homset(self, automorphisms)(images)

def coxeter_presentation(
    coxeter_matrix: "Matrix",
    names: "OrderedSet | None" = None,
) -> tuple:
    r"""Return \((F, R)\) for \(\langle s_i \mid s_i^2,\ (s_is_j)^{m_{ij}}\rangle\).

    The Coxeter presentation of the group a Coxeter matrix describes: one
    involution per index, and a braid relation for each finite bond.  A bond
    \(m_{ij}=\infty\) contributes no relation, which is what leaves the two
    involutions of the infinite dihedral group unrelated.

    Sage writes \(\infty\) two ways.  A matrix read off a Cartan type carries
    \(-1\); one built from roots carries ``infinity``.  Both name the bond.
    """
    from sage.groups.free_group import FreeGroup

    indices = tuple(coxeter_matrix.index_set())
    free = FreeGroup(len(indices) if names is None else names)
    generators = free.gens()
    relations = [generator**2 for generator in generators]
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            bond = coxeter_matrix[indices[i], indices[j]]
            if bond is infinity or bond == -1:
                continue
            relations.append((generators[i] * generators[j]) ** SageZZ(bond))
    return free, tuple(relations)


def _presentation_of(group: "Group") -> tuple:
    r"""Return \((F(S), R)\) for a finitely presented group.

    Each realization of \(C_2\) is a finitely presented group.  Each one has
    generators and relations to supply.  This function only records where
    each Sage type stores that data.  A type that cannot supply the data is
    rejected here.

    This function is the private boundary to Sage's representation-specific
    presentation algorithms.  It returns presentation data.  It does not
    return another public group that callers must use instead of ``group``.
    """
    match group:
        case FreeGroup_class():
            return group, ()
        case FinitelyPresentedGroup():
            return group.free_group(), tuple(group.relations())
        case PermutationGroup_generic():
            presented = group.as_finitely_presented_group()
            return presented.free_group(), tuple(presented.relations())
        case AbelianGroup_class():
            presented = group.permutation_group().as_finitely_presented_group()
            return presented.free_group(), tuple(presented.relations())
        case CoxeterMatrixGroup():
            return coxeter_presentation(group.coxeter_matrix())
        case NamedMatrixGroup_generic() | NamedMatrixGroup_gap():
            presented = (
                group.as_permutation_group().as_finitely_presented_group()
            )
            return presented.free_group(), tuple(presented.relations())
        case _:
            assert False, (
                f"{group} does not supply finite-presentation data"
            )


def _gap_model(group: "Group") -> "GapElement":
    r"""Return the GAP group the engine computes with for ``group``.

    Sibling of :func:`_presentation_of`, and the same kind of boundary: this
    function only records how each Sage type reaches a GAP-computable form.
    A type that cannot supply one is rejected here, with the gap stated.

    The permutation-normalization arms (``AbelianGroup_class`` and the
    generic matrix groups) model the group only up to isomorphism -- the
    correspondence between elements is forgotten -- so they support the
    group-level questions and leave element-level transport a stated gap
    (``_element_to_engine`` in ``group_morphisms``).  Normalizing an
    infinite group would not terminate, so those arms are gated on decidable
    finiteness rather than run silently.
    """
    # Local: a module-level import would close a cycle; the module is built by the time this runs.
    from dzack_research.preamble.categories.group.group_morphisms import (
        GroupAutomorphismGroup,
    )

    match group:
        case GroupAutomorphismGroup():
            return group._libgap_()
        case PermutationGroup_generic():
            return libgap(group)
        case ParentLibGAP():
            return group.gap()
        case AbelianGroup_class():
            assert _finiteness(group) is True, (
                f"normalizing {group} to a permutation model requires "
                "finiteness, which the group cannot decide"
            )
            return libgap(group.permutation_group())
        case CoxeterMatrixGroup():
            # Its Coxeter presentation, which is a GAP-backed group.  Sage's
            # matrix realization is not: it has no ``as_permutation_group``,
            # and its ``_libgap_`` falls through to converting the repr.  The
            # presentation is also the group's own definition, so nothing is
            # normalized away by taking it -- over a number field there is no
            # matrix model GAP could hold in any case.
            free, relations = coxeter_presentation(group.coxeter_matrix())
            return libgap(free / list(relations))
        case NamedMatrixGroup_generic() | FinitelyGeneratedMatrixGroup_generic():
            assert _finiteness(group) is True, (
                f"normalizing {group} to a permutation model requires "
                "finiteness, which the group cannot decide"
            )
            return libgap(group.as_permutation_group())
        case _:
            assert False, f"{group} has no GAP model in this engine"


class OwnedFinitelyPresentedGroups(Category):
    r"""Finitely generated groups whose defining surjection has
    kernel normally generated by finitely many relators.

    Strictly stronger than finite generation: there are finitely generated
    groups admitting no finite presentation.  Strictly weaker than finiteness:
    \(O(L)\) for indefinite \(L\) is finitely presented and infinite.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely presented groups"

    def super_categories(self) -> list:
        return [OwnedFinitelyGeneratedGroups()]

    class ParentMethods:
        def is_finitely_presented(self: Self) -> bool:
            r"""Return ``True`` because membership states this property."""
            return True

        def presenting_free_group(self: Self) -> "Group":
            r"""Return \(F(S)\), the free group the relations are words in."""
            from dzack_research.preamble.refine import refine

            free_group, _ = _presentation_of(self)
            # Finitely generated with no probe needed: the alphabet is finite
            # by construction, and it is the surjection's own generating set.
            if not free_group.category().is_subcategory(
                OwnedFinitelyGeneratedGroups()
            ):
                refine(free_group, OwnedFinitelyGeneratedGroups())
            return free_group

        def defining_relations(self: Self) -> "OrderedSet":
            r"""Return the relations of this group's presentation.

            The relations normally generate the kernel of \(F(S)\twoheadrightarrow G\),
            so they are a set of words in \(F(S)\) -- not the words themselves
            repeated, and not an ordering the presentation depends on.
            """
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set

            _, relations = _presentation_of(self)
            return finite_ordered_set(relations)


class AbelianGroupEndomorphismRings(Category):
    r"""\(\operatorname{End}(A)\) for \(A\) abelian, as a ring.

    Endomorphisms of any group compose, so they always form a monoid; they
    add only when the target is abelian.  So this is a ring precisely for the
    groups the abelian node holds, and Sage builds no such ring for them --
    ``End(AbelianGroup([3]))`` is not in ``Rings()`` and declines to construct
    a morphism from generator images at all.

    The group is the datum this level introduces.  Everything the
    endomorphism ring *is* as a ring it reaches through :class:`OwnedRings`.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "endomorphism rings of abelian groups"

    def super_categories(self) -> list:
        return [OwnedRings()]

    class ElementMethods:
        r"""An endomorphism of an abelian group.

        A map, held as one.  Images of a generating set would be a
        presentation, and endomorphisms are wanted here for groups that have
        no distinguished one -- a permutation group has no coordinates to
        read an exponent off.
        """

        def __init__(
            self,
            parent: "Parent",
            mapping: "Callable[[GroupElement], GroupElement]",
        ) -> None:
            self._mapping = mapping
            super().__init__(parent)

        def __call__(self, element: "GroupElement") -> "GroupElement":
            return self._mapping(element)

        def _add_(self: Self, other: Self) -> Self:
            r"""Return \(f+g:x\mapsto f(x)g(x)\).

            A homomorphism exactly because the target is abelian:
            \((f+g)(xy)=f(x)f(y)g(x)g(y)\), and the middle pair commutes past
            each other to give \((f+g)(x)(f+g)(y)\).  This is the whole reason
            the endomorphism ring is a ring, and the reason it is built here.
            """
            return self.parent()(
                lambda element: self.parent()._sum_values(
                    self(element), other(element)
                )
            )

        def _neg_(self: Self) -> Self:
            return self.parent()(
                lambda element: self.parent()._negative_value(self(element))
            )

        def _mul_(self: Self, other: Self) -> Self:
            r"""Return the composite \(f\circ g\), the ring's multiplication."""
            return self.parent()(lambda element: self(other(element)))

    class ParentMethods:
        def __init__(
            self, group: "Group", **rest: "ConstructionData"
        ) -> None:
            assert group.is_abelian(), (
                f"{group} is not abelian, so its endomorphisms do not add"
            )
            self._group = group
            self._additive = _uses_additive_notation(group)
            super().__init__(**rest)

        def _sum_values(
            self, left: "GroupElement", right: "GroupElement"
        ) -> "GroupElement":
            match self._additive:
                case True:
                    return left + right
                case False:
                    return left * right

        def _negative_value(self, value: "GroupElement") -> "GroupElement":
            match self._additive:
                case True:
                    return -value
                case False:
                    return value ** -1

        def _identity_value(self) -> "GroupElement":
            match self._additive:
                case True:
                    return self._group.zero()
                case False:
                    return self._group.one()

        def domain(self) -> "Group":
            return self._group

        def codomain(self) -> "Group":
            return self._group

        def _element_constructor_(
            self, mapping: "Callable[[GroupElement], GroupElement]"
        ) -> "Element":
            endomorphism: "Element" = self.ElementType(self, mapping)
            return endomorphism

        def one(self) -> "Element":
            return self(lambda element: element)

        def zero(self) -> "Element":
            return self(lambda element: self._identity_value())

        def __hash__(self) -> int:
            return hash((type(self), self._group))

        def __eq__(self, other: "MembershipInput") -> bool:
            return (
                type(other) is type(self)
                and self._group == other._group
            )

        def _repr_(self) -> str:
            return f"Endomorphism ring of {self._group}"


class OwnedAbelianGroups(Category):
    r"""Abelian groups.

    This is \(\mathbb Z\text{-Mod}\).  A Sage realization can write its group
    law additively or multiplicatively.  In the second notation, scalar
    multiplication by \(n\) is the \(n\)-th power map.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "abelian groups"

    def super_categories(self) -> list:
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return [OwnedGroups(), Modules(ℤ)]

    class ParentMethods:
        @cached_method
        def endomorphism_ring(self: Self) -> "Parent":
            r"""Return \(\operatorname{End}(A)\), a ring because \(A\) is abelian."""
            return object_of(AbelianGroupEndomorphismRings(), group=self)

        @cached_method
        def _ring_morphism_defining_module_action(self: Self) -> "Morphism":
            r"""Return the unique \(\rho:\mathbb Z\to\operatorname{End}(A)\).

            \(\mathbb Z\) is initial in rings, so there is exactly one ring
            morphism out of it into any ring, and \(\operatorname{End}(A)\) is
            a ring.  That is the whole content of
            \(\mathrm{Ab}\cong\mathbb Z\text{-Mod}\): the action exists and
            nothing about it is chosen.  It sends \(n\) to the \(n\)-th power
            map, which is what \(\rho(n)=n\cdot 1\) unwinds to.
            """
            endomorphisms = self.endomorphism_ring()
            additive = _uses_additive_notation(self)

            def multiple(
                exponent: "RingElement", element: "GroupElement"
            ) -> "GroupElement":
                match additive:
                    case True:
                        return exponent * element
                    case False:
                        return element ** exponent

            # \(\ZZ\) named as the session names it: \(\rho\)'s domain is the
            # ring of scalars a notebook asks about, and no arithmetic runs on
            # it here -- the action is a map of sets on the nose.
            return SetMorphism(
                Hom(ℤ, endomorphisms, Rings()),
                lambda exponent: endomorphisms(
                    lambda element: multiple(exponent, element)
                ),
            )


class OwnedFiniteGroups(Category):
    r"""Finite groups whose notebook-facing methods are owned by the preamble."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finite groups"

    def super_categories(self) -> list:
        return [OwnedFinitelyPresentedGroups(), Sets().Finite()]

    class ParentMethods:
        def conjugacy_classes_representatives(self: Self) -> tuple:
            r"""Return this finite group's conjugacy-class representatives."""
            from dzack_research.preamble.categories.group.group_morphisms import (
                _element_from_engine,
            )

            return tuple(
                _element_from_engine(self, conjugacy_class.Representative())
                for conjugacy_class in _gap_model(self).ConjugacyClasses()
            )

        def irreducible_characters(self: Self) -> tuple:
            r"""Return the absolutely irreducible characters of this group."""
            from sage.groups.class_function import ClassFunction
            from dzack_research.preamble.categories.modules.group_modules.characters import Character

            return tuple(
                Character(ClassFunction(self, engine_character), self)
                for engine_character in _gap_model(self).Irr()
            )

        def character(self: Self, values: "OrderedSet") -> "Character":
            r"""Return the character with the stated conjugacy-class values."""
            from sage.groups.class_function import ClassFunction
            from dzack_research.preamble.categories.modules.group_modules.characters import Character

            class_function = ClassFunction(self, list(values))
            return Character(class_function, self)

        def trivial_character(self: Self) -> "Character":
            r"""Return the trivial character."""
            from sage.groups.class_function import ClassFunction
            from dzack_research.preamble.categories.modules.group_modules.characters import Character

            class_function = ClassFunction(
                self,
                _gap_model(self).TrivialCharacter(),
            )
            return Character(class_function, self)


class OwnedFiniteAbelianGroups(Category):
    r"""Finite abelian groups, in either additive or multiplicative notation."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finite abelian groups"

    def super_categories(self) -> list:
        return [OwnedFiniteGroups(), OwnedAbelianGroups()]


def _answers_abelian(group: "Group") -> bool:
    r"""Return whether ``group`` decides commutativity.

    Sage's free groups raise rather than answer, and a free group of rank one
    is abelian -- so a group declining the question is not a group that is
    nonabelian.  Placing on a witness and not on a default is the difference.
    """
    return group.category().is_subcategory(SageGroups().Commutative())


def _uses_additive_notation(group: "Group") -> bool:
    r"""Return whether this realization writes the group law additively."""
    written_additively: bool = group.category().is_subcategory(
        CommutativeAdditiveGroups()
    )
    return written_additively


def refine_group(group: "Group") -> "Group":
    r"""Put ``group`` in every owned category witnessed by its structure.

    The parent stays the same.  Refinement adds mathematical properties and
    their methods.  It does not construct a second group.
    """
    from dzack_research.preamble.refine import refine

    if group.category().is_subcategory(OwnedGroups()):
        return group
    categories = tuple(
        category
        for category in _group_categories(group)
    )
    refine(group, categories)
    return group


def _group_categories(group: "Group") -> list[Category]:
    r"""Return the owned categories ``group``'s presentation witnesses.

    Each axiom is claimed only when the group carries the witness the
    definition asks for, never when a theorem would be needed:

    * finitely generated -- a finite generating set, which *is* the surjection
      \(F(S)\twoheadrightarrow G\);
    * finitely presented -- a finite presentation, or finiteness, whose
      multiplication table is one;
    * abelian -- commutativity, as decided by the group.

    A group that answers none of these is still a group, and is placed as one.
    """
    categories: list[Category] = [OwnedGroups()]
    finite = _finiteness(group) is True
    abelian = _answers_abelian(group)
    match (finite, abelian):
        case (True, True):
            categories.append(OwnedFiniteAbelianGroups())
        case (True, False):
            categories.append(OwnedFiniteGroups())
        case (False, True) | (False, False):
            pass
    # The probe, not ``ngens`` directly: a group that cannot answer must not
    # take the placement down with it, and Unknown is the honest outcome for
    # one whose generators nobody knows how to produce.
    if not finite and OwnedGroups.ObjectType.is_finitely_generated(group) is True:
        categories.append(OwnedFinitelyGeneratedGroups())
    if not finite and isinstance(group, (FinitelyPresentedGroup, FreeGroup_class)):
        categories.append(OwnedFinitelyPresentedGroups())
    if abelian and not finite:
        categories.append(OwnedAbelianGroups())
    return categories


# The Sage constructors a session builds groups with.  Each is the outermost
# ``__init__`` of its family, so the instance is complete when the hook runs.
# The classical groups have two: a GAP-backed one is not built by running the
# generic constructor and then adding GAP, so neither reaches the other.
#
# The two matrix groups *given by* a finite list of generating matrices are the
# exception, and are listed by that base class rather than by the families that
# build on it.  The construction is the witness -- the group is the one those
# matrices generate -- so every such family is finitely generated for the same
# reason, and each of them (Weyl, Coxeter, a bare ``MatrixGroup``) delegates to
# this constructor as its last statement, leaving the instance complete.
_GROUP_CONSTRUCTIONS = (
    NamedMatrixGroup_generic,
    NamedMatrixGroup_gap,
    FinitelyGeneratedMatrixGroup_generic,
    FinitelyGeneratedMatrixGroup_gap,
    PermutationGroup_generic,
    SymmetricGroup,
    AlternatingGroup,
    FreeGroup_class,
    AbelianGroup_class,
)


def _witnesses_finite_generation(group: "Group") -> bool:
    r"""Return whether ``group``'s own structure establishes finite generation."""
    return group.is_finitely_generated() is True


def _witnesses_finiteness(group: "Group") -> bool:
    return _finiteness(group) is True


def _witnesses_finite_presentation(group: "Group") -> bool:
    return _witnesses_finiteness(group) or isinstance(group, FreeGroup_class)


def _witnesses_commutativity(group: "Group") -> bool:
    return _answers_abelian(group)


def _witnesses_finite_abelian(group: "Group") -> bool:
    return _witnesses_finiteness(group) and _answers_abelian(group)


_GROUPS_INSTALLED = False


def install_groups() -> None:
    r"""Refine every group a session constructs into the owned categories.

    Construction *is* intake here: once the preamble is loaded the session is
    inside its universe, and a group built in that session is a group the
    preamble may be asked about.  Sage's classes offer no other moment --
    the interesting groups are built on demand, and none of them passes
    through a preamble constructor first.

    Two registrations, in this order, because the second's evidence lives on
    the first: the owned group category supplies ``is_finitely_generated``, and
    only a group that answers it with ``True`` carries the axiom.  A group
    that cannot say stays outside and answers ``Unknown``, which is the whole
    difference between this and a declaration.
    """
    global _GROUPS_INSTALLED
    # Local: a module-level import would close a cycle; the module is built by the time this runs.
    from dzack_research.preamble.refine import hook_post_init

    if _GROUPS_INSTALLED:
        return
    for construction in _GROUP_CONSTRUCTIONS:
        hook_post_init(
            construction,
            OwnedGroups(),
        )
        hook_post_init(
            construction,
            OwnedFinitelyGeneratedGroups(),
            predicate=_witnesses_finite_generation,
        )
        hook_post_init(
            construction,
            OwnedFinitelyPresentedGroups(),
            predicate=_witnesses_finite_presentation,
        )
        hook_post_init(
            construction,
            OwnedFiniteGroups(),
            predicate=_witnesses_finiteness,
        )
        hook_post_init(
            construction,
            OwnedAbelianGroups(),
            predicate=_witnesses_commutativity,
        )
        hook_post_init(
            construction,
            OwnedFiniteAbelianGroups(),
            predicate=_witnesses_finite_abelian,
        )
    _GROUPS_INSTALLED = True


install_groups()
