r"""Owned categories of groups."""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dzack_research.preamble.categories.sets.cardinals import Cardinal
    from dzack_research.preamble.lexicon import CartanType, Group, GroupElement, Matrix, Ring
    from dzack_research.preamble.lexicon import OrderedSet, Set

if TYPE_CHECKING:
    from typing import Callable
    from sage.rings.integer import Integer

from dzack_research.preamble.categories.sets.owned_sets import Sets, placement_of
if TYPE_CHECKING:
    from sage.categories.morphism import Morphism

from typing import Self

from sage.misc.cachefunc import cached_method
from sage.categories.category import Category
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups
from sage.categories.finite_groups import FiniteGroups as SageFiniteGroups
from sage.categories.groups import Groups as SageGroups
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.rings import Rings
from sage.groups.abelian_gps.abelian_group import AbelianGroup_class
from sage.groups.finitely_presented import FinitelyPresentedGroup
from sage.groups.free_group import FreeGroup_class
from sage.groups.matrix_gps.named_group import NamedMatrixGroup_generic
from sage.groups.matrix_gps.named_group_gap import NamedMatrixGroup_gap
from sage.groups.perm_gps.permgroup import PermutationGroup_generic
from sage.groups.perm_gps.permgroup_named import AlternatingGroup
from sage.groups.perm_gps.permgroup_named import SymmetricGroup
from sage.misc.unknown import Unknown
from dzack_research.preamble.categories.rings.rings import ℤ
from sage.rings.integer_ring import ZZ as SageZZ
from sage.categories.sets_cat import Sets as SageSets
from sage.sets.totally_ordered_finite_set import TotallyOrderedFiniteSet
from sage.structure.element import Element, RingElement
from sage.structure.parent import Parent


if TYPE_CHECKING:
    from typing import Protocol

    class GroupParent(Protocol):
        r"""What a group parent has from its placement: an identity, supplied
        by Sage's ``Groups().ParentMethods``."""

        def one(self) -> "GroupElement": ...


def _owned_group_constructor(
    constructor: "Callable[..., Group]",
) -> "staticmethod[..., Group]":
    r"""Return Sage's constructor with its result refined as a group here."""
    from functools import wraps

    @wraps(constructor)
    def construct(*arguments: object, **keywords: object) -> "Group":
        return refine_group(constructor(*arguments, **keywords))

    return staticmethod(construct)


def _group_over_engine_ring(
    constructor: "Callable[..., Group]",
    degree: "Integer",
    ring: "Ring",
    *arguments: object,
    **keywords: object,
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


def _engine_answer(
    group: "Group", question: str
) -> "bool | Integer | Unknown":
    r"""Return the engine's answer to ``question``, or ``Unknown``.

    Asked of the class Sage built rather than of ``group`` when the owned
    category supplies the public method.  Asking the object in that case
    would find the method that called this one.

    Sage says "I cannot decide" in two ways -- no such method, and a method
    that raises ``NotImplementedError`` -- and neither is mathematics.  Both
    become ``Unknown``, which carries the same information as a value.  Any
    other exception is a defect and is left to raise.

    ``super`` and not the class, because what is wanted is a *bound* answer:
    a cached method reached through its class is a descriptor and not a
    function of the group.
    """
    try:
        match group.category().is_subcategory(OwnedGroups()):
            case True:
                answer = getattr(
                    super(OwnedGroups.ParentMethods, group), question
                )
            case False:
                answer = getattr(group, question)
    except AttributeError:
        return Unknown
    try:
        return answer()
    except NotImplementedError:
        return Unknown


def _finiteness(group: "Group") -> "bool | Unknown":
    r"""Return whether ``group`` is finite, as a value.

    The group's own answer wherever it has one, so a category that decides
    finiteness -- ``LatticeIsometries`` puts the question to GAP -- is the one
    that answers.  A group placed in no owned category has not got
    :meth:`OwnedGroups.ParentMethods.is_finite` yet, which is why the decline
    is caught here too.
    """
    try:
        return group.is_finite()
    except NotImplementedError:
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
        return [SageSets()]

    class ParentMethods:
        def group_generators(self: Self) -> "OrderedSet":
            r"""Return \(S\), the images in \(G\) of the generating morphism.

            Honest elements of this group, and an ordered set of them: the
            enumeration the group lists them in is the order, and it is
            placed rather than rebuilt, which would discard it.  Finiteness
            is not part of it -- a group is not finitely generated by being
            a group -- so an infinite generating set survives being asked.

            Dropping the identity needs the set enumerated, so it happens at
            the category of finitely generated groups and not here.
            """
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.refine import refine

            family: "Set" = SageGroups().ParentMethods.group_generators(self)
            if family.category().is_subcategory(Sets().TotallyOrdered()):
                return family
            return refine(family, placement_of(family).TotallyOrdered())

        def number_of_group_generators(self: Self) -> "Cardinal":
            r"""Return \(|S|\), which is a cardinal and may be infinite."""
            return self.group_generators().cardinality()

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
            if self.has_computed_group_generators() is True:
                return True
            if self.group_generators_are_computable() is True:
                return True
            if self.is_arithmetic_group() is True:
                return True
            return Unknown

        def is_finite(self: Self) -> "bool | Unknown":
            r"""Return whether \(|G|\) is finite, as a value.

            A group placed in the finite groups category is finite, and that
            is the end of the question -- the placement is the statement, and
            a group carrying it needs no procedure run over it.  Sage's own
            procedure computes the order to decide, which for such a group is
            asking the cardinality to decide its own finiteness.

            Otherwise the group is asked.  A procedure that declines to decide
            is saying it does not know, which is what ``Unknown`` is for:
            ``Sp_4(\ZZ)`` reaches here, and the exception Sage raises instead
            says nothing about the group.
            """
            if self in OwnedFiniteGroups() or self in SageFiniteGroups():
                return True
            return _engine_answer(self, "is_finite")

        def ngens(self: Self) -> "Integer | Unknown":
            r"""Return the size of the generating set the engine holds.

            Sage answers for a group whose generators it can produce and
            raises ``AttributeError`` for one it cannot, so a caller has to
            catch to learn that nobody knows the generators.  That is the
            same fact ``Unknown`` states as a value.

            The preamble's own word is
            :meth:`number_of_group_generators`, which says which structure is
            generated; this spelling is kept because it is the one Sage's
            callers already type.
            """
            return _engine_answer(self, "ngens")

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

        def group_generators_are_computable(self: Self) -> "bool | Unknown":
            r"""Return whether some algorithm produces a generating set.

            Asked of this object's resolution order with the owned categories'
            own answer discounted.  ``OwnedGroups`` gives *every* group it
            holds a ``group_generators`` that reads the group's ``gens``, so
            asking the object whether the method is there finds the
            preamble's own and says yes about a group -- \(SO_3(\QQ)\) --
            whose generating set nobody can produce.  What is left is the
            engine's method, or a category that computes one, as
            ``LatticeIsometries`` does from the Gram matrix.

            True does not promise the computation is cheap -- ``O(L)`` for a
            definite lattice is computable and slow.  It promises only that
            asking is meaningful.  Absence is ``Unknown``: no algorithm in
            this engine is not the same as no algorithm.
            """
            generic = (
                OwnedGroups.ParentMethods,
                OwnedFinitelyGeneratedGroups.ParentMethods,
            )
            for holder in type(self).__mro__:
                if holder in generic:
                    continue
                if "group_generators" in vars(holder) or "gens" in vars(holder):
                    return True
            return Unknown

        def has_computed_group_generators(self: Self) -> "bool | Unknown":
            r"""Return whether a generating set is already in hand.

            The one case that is free.  A group given by generators and
            relations, or carved out of \(GL_n(R)\) on stated matrices,
            answers ``True`` and no computation follows.
            """
            for stored in ("_group_generators", "_gens"):
                if self.__dict__.get(stored) is not None:
                    return True
            return Unknown


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

        def group_generators(self: "GroupParent") -> TotallyOrderedFiniteSet:
            r"""Return \(S\), which the axiom makes a *finite* ordered set.

            The same generating set, with the finiteness the axiom supplies.
            The enumeration is handed over as the order rather than re-sorted,
            so a family indexed \(1,\dots,n\) keeps its indexing.

            The identity is dropped, which is only possible where the set can
            be enumerated: \(\langle S\rangle=\langle S\setminus\{1\}\rangle\)
            for every \(S\), so it never generates anything, and the trivial
            group is generated by \(\emptyset\) rather than by \(\{1\}\).
            """
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set

            identity = self.one()
            stored = self.__dict__.get("_group_generators")
            match stored:
                case None:
                    generators = SageGroups().ParentMethods.group_generators(
                        self
                    )
                    nonidentity = tuple(
                        generator
                        for generator in generators
                        if generator != identity
                    )
                case _:
                    nonidentity = tuple(
                        generator
                        for generator in stored
                        if not generator.is_identity()
                    )
            generating_set: TotallyOrderedFiniteSet = finite_ordered_set(nonidentity)
            return generating_set

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
        case NamedMatrixGroup_generic() | NamedMatrixGroup_gap():
            presented = (
                group.as_permutation_group().as_finitely_presented_group()
            )
            return presented.free_group(), tuple(presented.relations())
        case _:
            assert False, (
                f"{group} does not supply finite-presentation data"
            )


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
            free_group, _ = _presentation_of(self)
            # Finitely generated with no probe needed: the alphabet is finite
            # by construction, and it is the surjection's own generating set.
            if not free_group.category().is_subcategory(
                OwnedFinitelyGeneratedGroups()
            ):
                free_group._refine_category_(OwnedFinitelyGeneratedGroups())
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


class AbelianGroupEndomorphism(Element):
    r"""An endomorphism of an abelian group.

    A map, held as one.  Images of a generating set would be a presentation,
    and endomorphisms are wanted here for groups that have no distinguished
    one -- a permutation group has no coordinates to read an exponent off.
    """

    if TYPE_CHECKING:
        # The parent of an endomorphism is the endomorphism ring, which is
        # what makes the ring's own operations reachable from an element.
        def parent(self) -> "AbelianGroupEndomorphismRing": ...

    def __init__(
        self, parent: "Parent", mapping: "Callable[[GroupElement], GroupElement]"
    ) -> None:
        Element.__init__(self, parent)
        self._mapping = mapping

    def __call__(self, element: "GroupElement") -> "GroupElement":
        return self._mapping(element)

    def _add_(self, other: "AbelianGroupEndomorphism") -> "AbelianGroupEndomorphism":
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

    def _neg_(self) -> "AbelianGroupEndomorphism":
        return self.parent()(
            lambda element: self.parent()._negative_value(self(element))
        )

    def _mul_(self, other: "AbelianGroupEndomorphism") -> "AbelianGroupEndomorphism":
        r"""Return the composite \(f\circ g\), the ring's multiplication."""
        return self.parent()(lambda element: self(other(element)))


if TYPE_CHECKING:
    EndomorphismRingParent = Parent[AbelianGroupEndomorphism]
else:
    # ``Parent`` is a cython extension type and is not subscriptable at
    # runtime; the element binding is for the checker.
    EndomorphismRingParent = Parent


class AbelianGroupEndomorphismRing(EndomorphismRingParent):
    r"""\(\operatorname{End}(A)\) for \(A\) abelian, as a ring.

    Endomorphisms of any group compose, so they always form a monoid; they
    add only when the target is abelian.  So this is a ring precisely for the
    groups this category holds, and Sage builds no such ring for them --
    ``End(AbelianGroup([3]))`` is not in ``Rings()`` and declines to construct
    a morphism from generator images at all.
    """

    Element = AbelianGroupEndomorphism

    def __init__(self, group: "Group") -> None:
        assert group.is_abelian(), (
            f"{group} is not abelian, so its endomorphisms do not add"
        )
        self._group = group
        self._additive = _uses_additive_notation(group)
        Parent.__init__(self, category=Rings())

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
    ) -> AbelianGroupEndomorphism:
        endomorphism: AbelianGroupEndomorphism = self.element_class(self, mapping)
        return endomorphism

    def one(self) -> AbelianGroupEndomorphism:
        return self(lambda element: element)

    def zero(self) -> AbelianGroupEndomorphism:
        return self(lambda element: self._identity_value())

    def __hash__(self) -> int:
        return hash((type(self), self._group))

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, AbelianGroupEndomorphismRing)
            and type(other) is type(self)
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
        def endomorphism_ring(self: Self) -> AbelianGroupEndomorphismRing:
            r"""Return \(\operatorname{End}(A)\), a ring because \(A\) is abelian."""
            return AbelianGroupEndomorphismRing(self)

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
        return [OwnedFinitelyPresentedGroups()]

    class ParentMethods:
        def is_finite(self: Self) -> bool:
            r"""Return ``True`` because membership states this property."""
            return True


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
    return _engine_answer(group, "is_abelian") is True


def _record_group_notation(group: "Group") -> None:
    r"""Record how Sage writes the group law before category refinement."""
    group._preamble_uses_additive_notation = group.category().is_subcategory(
        CommutativeAdditiveGroups()
    )


def _uses_additive_notation(group: "Group") -> bool:
    r"""Return whether this realization writes the group law additively."""
    recorded = group.__dict__.get("_preamble_uses_additive_notation")
    if recorded is not None:
        additive: bool = recorded
        return additive
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

    if "_preamble_uses_additive_notation" not in group.__dict__:
        _record_group_notation(group)
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
    if not finite and OwnedGroups.ParentMethods.is_finitely_generated(group) is True:
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
_GROUP_CONSTRUCTIONS = (
    NamedMatrixGroup_generic,
    NamedMatrixGroup_gap,
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
            before=_record_group_notation,
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
