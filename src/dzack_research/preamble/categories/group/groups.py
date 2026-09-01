"""Owned categories of groups and their standard constructor catalogue."""

from functools import wraps

from sage.categories.category import Category
from sage.categories.finite_groups import FiniteGroups as SageFiniteGroups
from sage.categories.groups import Groups as SageGroups
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.rings import Rings
from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups
from sage.groups.abelian_gps.abelian_group import (
    AbelianGroup_class,
    AbelianGroup_subgroup,
)
from sage.groups.finitely_presented import FinitelyPresentedGroup
from sage.groups.free_group import FreeGroup_class
from sage.groups.libgap_wrapper import ParentLibGAP
from sage.groups.matrix_gps.coxeter_group import CoxeterMatrixGroup
from sage.groups.matrix_gps.finitely_generated import FinitelyGeneratedMatrixGroup_generic
from sage.groups.matrix_gps.finitely_generated_gap import FinitelyGeneratedMatrixGroup_gap
from sage.groups.matrix_gps.named_group import NamedMatrixGroup_generic
from sage.groups.matrix_gps.named_group_gap import NamedMatrixGroup_gap
from sage.groups.perm_gps.permgroup import (
    PermutationGroup_generic,
    PermutationGroup_subgroup,
)
from sage.groups.perm_gps.permgroup_named import AlternatingGroup, SymmetricGroup
from sage.libs.gap.libgap import libgap
from sage.misc.cachefunc import cached_method
from sage.misc.unknown import Unknown
from sage.rings.infinity import infinity
from sage.rings.integer_ring import ZZ
from sage.structure.parent import Parent
from sage.structure.element import RingElement

from dzack_research.preamble.categories.group.magmas import Monoids
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.refine import hook_post_init, refine


def _finiteness(group):
    """Return True/False when Sage's category already decides finiteness."""
    if group in SageFiniteGroups():
        return True
    if group.category().is_subcategory(SageGroups().Infinite()):
        return False
    return Unknown


def _finite_ordered_set(elements):
    return finite_ordered_set(elements)


def _unique_nonidentity_generators(group):
    identity = group.one()
    return _finite_ordered_set(
        generator for generator in group.gens() if generator != identity
    )


def _owned_group_constructor(constructor):
    @wraps(constructor)
    def construct(*args, **kwargs):
        return refine_group(constructor(*args, **kwargs))
    return staticmethod(construct)


def _group_over_ring(constructor, degree, ring, *args, **kwargs):
    from dzack_research.preamble.categories.rings import engine_ring

    return refine_group(constructor(degree, engine_ring(ring), *args, **kwargs))


def _GL(degree, ring, var="a"):
    from sage.groups.matrix_gps.catalog import GL
    return _group_over_ring(GL, degree, ring, var=var)


def _SL(degree, ring, var="a"):
    from sage.groups.matrix_gps.catalog import SL
    return _group_over_ring(SL, degree, ring, var=var)


def _Sp(degree, ring, var="a", invariant_form=None):
    from sage.groups.matrix_gps.catalog import Sp
    return _group_over_ring(Sp, degree, ring, var=var, invariant_form=invariant_form)


def _GU(degree, ring, var="a", invariant_form=None):
    from sage.groups.matrix_gps.catalog import GU
    return _group_over_ring(GU, degree, ring, var=var, invariant_form=invariant_form)


def _SU(degree, ring, var="a", invariant_form=None):
    from sage.groups.matrix_gps.catalog import SU
    return _group_over_ring(SU, degree, ring, var=var, invariant_form=invariant_form)


def _GO(degree, ring, e=0, var="a", invariant_form=None):
    from sage.groups.matrix_gps.catalog import GO
    return _group_over_ring(GO, degree, ring, e=e, var=var, invariant_form=invariant_form)


def _SO(degree, ring, e=None, var="a", invariant_form=None):
    from sage.groups.matrix_gps.catalog import SO
    return _group_over_ring(SO, degree, ring, e=e, var=var, invariant_form=invariant_form)


def _Affine(degree, ring):
    from sage.groups.affine_gps.catalog import Affine
    return _group_over_ring(Affine, degree, ring)


def _Euclidean(degree, ring):
    from sage.groups.affine_gps.catalog import Euclidean
    return _group_over_ring(Euclidean, degree, ring)


def _Heisenberg(degree=1, ring=0):
    from sage.groups.matrix_gps.catalog import Heisenberg
    from dzack_research.preamble.categories.rings import engine_ring

    scalar_ring = ring if ring == 0 else engine_ring(ring)
    return refine_group(Heisenberg(degree, scalar_ring))


def _SemimonomialTransformation(ring, degree):
    from sage.groups.misc_gps.misc_groups_catalog import SemimonomialTransformation
    from dzack_research.preamble.categories.rings import engine_ring

    return refine_group(SemimonomialTransformation(engine_ring(ring), degree))


def _SmallGroup(order, index):
    from sage.groups.perm_gps.permgroup import PermutationGroup
    model = libgap.SmallGroup(order, index).IsomorphismPermGroup().Image()
    return refine_group(PermutationGroup(gap_group=model))


def _Coxeter(data, implementation="reflection", base_ring=None, index_set=None):
    from sage.groups.misc_gps.misc_groups_catalog import CoxeterGroup
    from dzack_research.preamble.categories.rings import engine_ring

    scalar_ring = None if base_ring is None else engine_ring(base_ring)
    return refine_group(
        CoxeterGroup(
            data,
            implementation=implementation,
            base_ring=scalar_ring,
            index_set=index_set,
        )
    )


def _native_supergroup(group):
    match group:
        case PermutationGroup_subgroup() | AbelianGroup_subgroup():
            return refine_group(group.ambient_group())
        case _:
            return group


class SubgroupInclusion(SetMorphism):
    def is_injective(self):
        return True


def _group_inclusion_image(subgroup, containing_group, element):
    if element.parent() is containing_group:
        return element
    if isinstance(subgroup, AbelianGroup_subgroup):
        image = containing_group.one()
        for generator, exponent in zip(subgroup.gens(), element.exponents(), strict=True):
            image *= containing_group(generator) ** exponent
        return image
    return containing_group(element)


def _canonical_subgroup_inclusion(subgroup):
    containing_group = subgroup.supergroup()
    return SubgroupInclusion(
        Hom(subgroup, containing_group, SageGroups()),
        lambda element: _group_inclusion_image(subgroup, containing_group, element),
    )


class OwnedGroups(Category):
    """Groups whose notebook-facing group interface is owned by the preamble."""

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

    def homset(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a group Hom requires two owned groups")
        from dzack_research.preamble.categories.group.group_morphisms import group_homset

        return group_homset(domain, codomain)

    @classmethod
    def _repr_object_names(cls):
        return "groups"

    def super_categories(self):
        return [SageGroups(), Monoids()]

    class ParentMethods:
        def is_finitely_generated(self):
            if self in OwnedFinitelyGeneratedGroups():
                return True
            if _finiteness(self) is True or self.is_arithmetic_group() is True:
                return True
            return Unknown

        def is_finitely_presented(self):
            return True if self in OwnedFinitelyPresentedGroups() else Unknown

        def is_arithmetic_group(self):
            if isinstance(self, NamedMatrixGroup_generic) and self.base_ring() is ZZ:
                return True
            return Unknown

        def supergroup(self):
            return _native_supergroup(self)

        def inclusion(self):
            return _canonical_subgroup_inclusion(self)

        def End(self):
            from dzack_research.preamble.categories.group.group_morphisms import group_homset
            return group_homset(self, self)

        @cached_method
        def Aut(self):
            from dzack_research.preamble.categories.group.group_morphisms import GroupAutomorphismGroup
            automorphisms = GroupAutomorphismGroup(self)
            categories = [OwnedGroups()]
            if _finiteness(self) is True:
                categories.append(OwnedFiniteGroups())
            refine(automorphisms, categories)
            return automorphisms

        def is_isomorphic_to(self, other):
            if _finiteness(self) is not True or _finiteness(other) is not True:
                return Unknown
            found = _gap_model(self).IsomorphismGroups(_gap_model(other))
            return str(found) != "fail"


class OwnedFinitelyGeneratedGroups(Category):
    """Groups admitting some finite generating set."""

    @classmethod
    def _repr_object_names(cls):
        return "finitely generated groups"

    def super_categories(self):
        return [OwnedGroups()]

    class ParentMethods:
        def is_finitely_generated(self):
            return True


class GroupsWithChosenFiniteGeneratingSet(Category):
    """Finitely generated groups carrying a chosen finite generating set."""

    def super_categories(self):
        return [OwnedFinitelyGeneratedGroups()]

    class ParentMethods:
        @cached_method
        def group_generators(self):
            return _unique_nonidentity_generators(self)

        def number_of_group_generators(self):
            return ZZ(self.group_generators().cardinality())

        def conjugation_morphism(self):
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


class OwnedFinitelyPresentedGroups(Category):
    """Finitely presented groups, as a property of the group."""

    @classmethod
    def _repr_object_names(cls):
        return "finitely presented groups"

    def super_categories(self):
        return [OwnedFinitelyGeneratedGroups()]

    class ParentMethods:
        def is_finitely_presented(self):
            return True


class GroupsWithChosenFinitePresentation(Category):
    """Groups carrying a chosen finite presentation."""

    def super_categories(self):
        return [OwnedFinitelyPresentedGroups(), GroupsWithChosenFiniteGeneratingSet()]

    class ParentMethods:
        def presenting_free_group(self):
            free, _ = _presentation_of(self)
            return refine_group(free)

        @cached_method
        def defining_relations(self):
            _, relations = _presentation_of(self)
            return _finite_ordered_set(relations)


class _AbelianEndomorphismElement(RingElement):
    """Storage for one endomorphism; the operations live on its category."""

    def __init__(self, parent, mapping):
        self._mapping = mapping
        RingElement.__init__(self, parent)


class AbelianGroupEndomorphismRings(Category):
    """Endomorphism rings of abelian groups."""

    def super_categories(self):
        return [Rings()]

    class ElementMethods:
        def __call__(self, element):
            return self._mapping(element)

        def _add_(self, other):
            return self.parent()(
                lambda element: self.parent()._sum_values(
                    self(element), other(element)
                )
            )

        def _neg_(self):
            return self.parent()(
                lambda element: self.parent()._negative_value(self(element))
            )

        def _mul_(self, other):
            return self.parent()(lambda element: self(other(element)))

    class ParentMethods:
        def domain(self):
            return self._group

        def codomain(self):
            return self._group

        def _sum_values(self, left, right):
            return left + right if self._additive else left * right

        def _negative_value(self, value):
            return -value if self._additive else value ** -1

        def _identity_value(self):
            return self._group.zero() if self._additive else self._group.one()

        def _element_constructor_(self, mapping):
            return self.element_class(self, mapping)

        def one(self):
            return self(lambda element: element)

        def zero(self):
            return self(lambda element: self._identity_value())

        def _repr_(self):
            return f"Endomorphism ring of {self._group}"


class _AbelianEndomorphismRingParent(Parent):
    Element = _AbelianEndomorphismElement

    def __init__(self, group):
        self._group = group
        self._additive = group.category().is_subcategory(CommutativeAdditiveGroups())
        Parent.__init__(self, category=AbelianGroupEndomorphismRings())
        refine(self, AbelianGroupEndomorphismRings())


class OwnedAbelianGroups(Category):
    @classmethod
    def _repr_object_names(cls):
        return "abelian groups"

    def super_categories(self):
        return [OwnedGroups(), SageGroups().Commutative()]

    class ParentMethods:
        @cached_method
        def endomorphism_ring(self):
            return _AbelianEndomorphismRingParent(self)

        @cached_method
        def scalar_action(self):
            endomorphisms = self.endomorphism_ring()
            additive = self.category().is_subcategory(CommutativeAdditiveGroups())

            def multiple(exponent, element):
                return exponent * element if additive else element ** exponent

            return SetMorphism(
                Hom(ZZ, endomorphisms, Rings()),
                lambda exponent: endomorphisms(
                    lambda element: multiple(exponent, element)
                ),
            )

        def scalar_multiple(self, exponent, element):
            return self.scalar_action()(ZZ(exponent))(element)


class OwnedFiniteGroups(Category):
    @classmethod
    def _repr_object_names(cls):
        return "finite groups"

    def super_categories(self):
        return [OwnedFinitelyPresentedGroups(), SageFiniteGroups()]

    class ParentMethods:
        def is_finite(self):
            return True

        def conjugacy_classes_representatives(self):
            from dzack_research.preamble.categories.group.group_morphisms import _element_from_engine
            return tuple(
                _element_from_engine(self, conjugacy_class.Representative())
                for conjugacy_class in _gap_model(self).ConjugacyClasses()
            )


class OwnedFiniteAbelianGroups(Category):
    @classmethod
    def _repr_object_names(cls):
        return "finite abelian groups"

    def super_categories(self):
        return [OwnedFiniteGroups(), OwnedAbelianGroups()]


def coxeter_presentation(coxeter_matrix, names=None):
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
            relations.append((generators[i] * generators[j]) ** ZZ(bond))
    return free, tuple(relations)


def _presentation_of(group):
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
            presented = group.as_permutation_group().as_finitely_presented_group()
            return presented.free_group(), tuple(presented.relations())
        case _:
            raise NotImplementedError(f"{group} does not supply chosen finite-presentation data")


def _gap_model(group):
    from dzack_research.preamble.categories.group.group_morphisms import GroupAutomorphismGroup
    match group:
        case GroupAutomorphismGroup():
            return group._libgap_()
        case PermutationGroup_generic():
            return libgap(group)
        case ParentLibGAP():
            return group.gap()
        case AbelianGroup_class():
            if _finiteness(group) is not True:
                raise NotImplementedError("GAP normalization of this abelian group requires finiteness")
            return libgap(group.permutation_group())
        case CoxeterMatrixGroup():
            free, relations = coxeter_presentation(group.coxeter_matrix())
            return libgap(free / list(relations))
        case NamedMatrixGroup_generic() | FinitelyGeneratedMatrixGroup_generic():
            if _finiteness(group) is not True:
                raise NotImplementedError("GAP permutation normalization requires finiteness")
            return libgap(group.as_permutation_group())
        case _:
            raise NotImplementedError(f"{group} has no GAP model in this engine")


def _is_abelian_witness(group):
    if group.category().is_subcategory(SageGroups().Commutative()):
        return True
    if isinstance(group, (AbelianGroup_class, AbelianGroup_subgroup)):
        return True
    if _finiteness(group) is True:
        try:
            return bool(_gap_model(group).IsAbelian())
        except NotImplementedError:
            return False
    return False


def _has_chosen_generators(group):
    return isinstance(
        group,
        (
            PermutationGroup_generic,
            AbelianGroup_class,
            FreeGroup_class,
            FinitelyPresentedGroup,
            FinitelyGeneratedMatrixGroup_generic,
            FinitelyGeneratedMatrixGroup_gap,
            CoxeterMatrixGroup,
        ),
    )


def _has_chosen_presentation(group):
    if isinstance(group, (FreeGroup_class, FinitelyPresentedGroup, CoxeterMatrixGroup)):
        return True
    if _finiteness(group) is True and isinstance(
        group,
        (PermutationGroup_generic, AbelianGroup_class, NamedMatrixGroup_generic, NamedMatrixGroup_gap),
    ):
        return True
    return False


def _is_finitely_generated_witness(group):
    return _finiteness(group) is True or _has_chosen_generators(group) or (
        isinstance(group, NamedMatrixGroup_generic) and group.base_ring() is ZZ
    )


def _is_finitely_presented_witness(group):
    return _finiteness(group) is True or isinstance(
        group, (FreeGroup_class, FinitelyPresentedGroup, CoxeterMatrixGroup, AbelianGroup_class)
    )


def refine_group(group):
    """Place a Sage group in every owned category its construction witnesses."""
    categories = [OwnedGroups()]
    finite = _finiteness(group) is True
    abelian = _is_abelian_witness(group)
    if finite and abelian:
        categories.append(OwnedFiniteAbelianGroups())
    elif finite:
        categories.append(OwnedFiniteGroups())
    elif abelian:
        categories.append(OwnedAbelianGroups())
    if not finite and _is_finitely_generated_witness(group):
        categories.append(OwnedFinitelyGeneratedGroups())
    if not finite and _is_finitely_presented_witness(group):
        categories.append(OwnedFinitelyPresentedGroups())
    if _has_chosen_generators(group):
        categories.append(GroupsWithChosenFiniteGeneratingSet())
    if _has_chosen_presentation(group):
        categories.append(GroupsWithChosenFinitePresentation())
    return refine(group, categories)


_GROUP_CONSTRUCTIONS = (
    NamedMatrixGroup_generic,
    NamedMatrixGroup_gap,
    FinitelyGeneratedMatrixGroup_generic,
    FinitelyGeneratedMatrixGroup_gap,
    PermutationGroup_generic,
    SymmetricGroup,
    AlternatingGroup,
    FreeGroup_class,
    FinitelyPresentedGroup,
    AbelianGroup_class,
)
_GROUPS_INSTALLED = False


def _finish_group_refinement(group):
    refine_group(group)


def install_groups():
    global _GROUPS_INSTALLED
    if _GROUPS_INSTALLED:
        return
    for construction in _GROUP_CONSTRUCTIONS:
        hook_post_init(construction, OwnedGroups(), after=_finish_group_refinement)
    _GROUPS_INSTALLED = True


Groups = groups = OwnedGroups
FinitelyGeneratedGroups = OwnedFinitelyGeneratedGroups
FinitelyPresentedGroups = OwnedFinitelyPresentedGroups
FiniteGroups = OwnedFiniteGroups
AbelianGroups = OwnedAbelianGroups
FiniteAbelianGroups = OwnedFiniteAbelianGroups

install_groups()
