r"""Owned groups with private Sage/GAP realizations.

Catalogue constructors cross their mathematical arguments at the engine
boundary and construct at OwnedGroups(), with the properties the native
construction proves.  A free basis belongs to GroupsWithChosenFreeBasis;
a subgroup retains its ambient group at Subgroups(G).  Engine classes are
private implementations selected at those owners, not new category nodes.
"""

from functools import reduce, wraps
from itertools import combinations
from operator import mul

from sage.categories.category import Category
from sage.categories.category_with_axiom import all_axioms
from sage.categories.finite_groups import FiniteGroups as SageFiniteGroups
from sage.categories.groups import Groups as SageGroups
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.objects import Objects
from sage.groups.abelian_gps.abelian_group import (
    AbelianGroup_class,
    AbelianGroup_subgroup,
)
from sage.groups.finitely_presented import FinitelyPresentedGroup
from sage.groups.free_group import FreeGroup_class
from sage.groups.indexed_free_group import IndexedFreeGroup
from sage.groups.libgap_group import GroupLibGAP
from sage.groups.libgap_wrapper import ParentLibGAP
from sage.groups.matrix_gps.coxeter_group import CoxeterMatrixGroup
from sage.groups.matrix_gps.finitely_generated import (
    FinitelyGeneratedMatrixGroup_generic,
)
from sage.groups.matrix_gps.finitely_generated_gap import (
    FinitelyGeneratedMatrixGroup_gap,
)
from sage.groups.matrix_gps.matrix_group import MatrixGroup_generic
from sage.groups.matrix_gps.named_group import NamedMatrixGroup_generic
from sage.groups.matrix_gps.named_group_gap import NamedMatrixGroup_gap
from sage.groups.perm_gps.permgroup import (
    PermutationGroup_generic,
    PermutationGroup_subgroup,
)
from sage.libs.gap.element import GapElement
from sage.libs.gap.libgap import libgap
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.classcall_metaclass import typecall
from sage.misc.latex import latex
from sage.misc.unknown import Unknown
from sage.rings.infinity import infinity
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.rings.number_field.galois_group import GaloisGroup_v2 as SageGaloisGroup
from sage.rings.rational_field import QQ
from sage.structure.element import Element, MultiplicativeGroupElement
from sage.structure.element import parent as element_parent
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE, richcmp
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    CategoryPacketMethods,
    EndCategoryConstruction,
    MorCategoryConstruction,
    MorCategories,
    IsoCategoryConstruction,
    _category_mor_parent,
    _distinct_supercategories,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
    OwnedParameterizedCategory,
    _fix_selected_resolution,
)
from dzack_research.preamble.categories.group.magmas import (
    AdditiveGroups,
    Monoids,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphismMethods,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    MatrixSpaces,
    ModuleMorphism,
    _engine_matrix,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedRings,
    _engine_element,
    _engine_ring,
    _own_ring,
    _owned_ring,
)
from dzack_research.preamble.categories.sets.cardinals import (
    Cardinalities,
    aleph,
    cardinal,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.set_categories import EnumeratedSets, FiniteSets, OwnedSetMorphism, Sets, finite_ordinal_set
from dzack_research.preamble.logic import AtomicProposition, conjunction, negation
from dzack_research.preamble.owned_category import (
    _implementation_with_engine,
    _object_of,
)
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom
from dzack_research.preamble.refine import RealizationHook, realize_owned_category, refine
from dzack_research.preamble.validation import validator

# Finite generation reuses Sage's axiom for it, ``FinitelyGeneratedAsMagma``.
# Finite presentation is qualified as Sage qualifies that one: an axiom name
# is global, and ``FinitelyPresented`` is Sage's module axiom.
if "FinitelyPresentedAsGroup" not in all_axioms:
    all_axioms.add("FinitelyPresentedAsGroup")

# --------------------------------------------------------------------------
# Engine crossings.
#
# Protected contract (``OWN-05``).  A group realized by an engine supplies
# ``_engine_group()``, ``_to_engine(element)`` and
# ``_from_engine(engine_element)``; a group whose subgroups are generated in
# its engine also supplies ``_engine_subgroup_from_generators(generators)``,
# ``_to_subgroup_engine(element, engine_subgroup)`` and
# ``_from_subgroup_engine(engine_element)``. Membership uses
# ``_engine_subgroup_contains(element, engine_subgroup)`` and returns a
# Boolean without requiring an engine for the full containing group. Implementers:
# :class:`_GroupEngine`, selected privately at ``OwnedGroups``; the
# group-automorphism, lattice orthogonal-group and torsion-form
# orthogonal-group Mor parents; and predicate subgroups of a finite group,
# realized as the engine subgroup on their elements.  Callers: the adapters in this section and the class-function,
# character and ``G``-set adapters of this package.  Inputs and outputs are
# owned elements on one side and the engine's elements on the other; a
# crossing and its inverse compose to the identity on owned elements.  The
# contract is invoked through :func:`_engine_group` and the functions below,
# which are its dispatchers; a group supplying no engine realization fails at
# the dispatcher, which is the computational frontier of every engine-backed
# operation.
#
# Every function in this section is an engine adapter (``OWN-06``): it is the
# one site inspecting the engine's representation type for the operation it
# names.
# --------------------------------------------------------------------------


def _engine_group(group):
    r"""Return the engine realizing ``group`` (the protected contract's dispatcher)."""
    return group._engine_group()


def _engine_finiteness(engine):
    r"""Return ``True``/``False`` when Sage's category states finiteness, else ``None``.

    ``None`` means that the engine's category states neither, so the engine
    supplies no witness either way.
    """
    if engine in SageFiniteGroups():
        return True
    if engine.category().is_subcategory(SageGroups().Infinite()):
        return False
    return None


def _gap_model(group):
    r"""Return the GAP group modelling ``group``."""
    match group:
        case _ if group in GroupAutomorphismGroups():
            return group._libgap_()
        case _:
            return _gap_model_of_engine(_engine_group(group))


def _gap_model_of_engine(engine):
    r"""Return the GAP group modelling one engine group."""
    match engine:
        case PermutationGroup_generic() | FreeGroup_class() | FinitelyPresentedGroup():
            return libgap(engine)
        case ParentLibGAP():
            return engine.gap()
        case AbelianGroup_class():
            assert _engine_finiteness(engine) is True, (
                f"{engine} cannot be handed to GAP: an abelian group given by its invariants is converted "
                f"through its permutation representation, which requires the group to be finite"
            )
            return libgap(engine.permutation_group())
        case CoxeterMatrixGroup():
            free, relations = _coxeter_presentation(engine.coxeter_matrix())
            return libgap(free / list(relations))
        case NamedMatrixGroup_generic() | FinitelyGeneratedMatrixGroup_generic():
            assert _engine_finiteness(engine) is True, (
                f"{engine} cannot be handed to GAP: a matrix group is converted through its permutation "
                f"representation, which requires the group to be finite"
            )
            return libgap(engine.as_permutation_group())
        case _:
            assert False, f"{engine} cannot be handed to GAP: no conversion to a GAP group is available for groups of type {type(engine).__name__}"


def _automorphism_gap_model(group):
    r"""Return GAP's automorphism group of ``group``.

    ``Aut(G)`` exists for every group; the available GAP algorithm
    (``AutomorphismGroup``) computes it for finite groups only.
    """
    assert group.is_finite() is True, (
        f"Aut({group}) exists, but it is computed here only by GAP's algorithm for finite groups, "
        f"and {group} is not known to be finite"
    )
    return libgap.AutomorphismGroup(_gap_model(group))


def _encodes_elements_in_gap(engine) -> bool:
    r"""Whether ``engine`` identifies its elements one by one with GAP elements."""
    match engine:
        case PermutationGroup_generic() | ParentLibGAP() | FreeGroup_class() | FinitelyPresentedGroup():
            return True
        case _:
            return False


class _AdditiveGroupForGroupExp(Parent):
    r"""The Sage additive-parent interface required by ``sage.groups.group_exp``.

    Operations and elements are those of the given owned abelian group;
    this private parent supplies Sage's runtime category to GroupExp.
    """

    def __init__(self, additive_group):
        from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups

        self._additive_group = additive_group
        Parent.__init__(self, category=CommutativeAdditiveGroups(), facade=additive_group)

    def _element_constructor_(self, value):
        return self._additive_group(value)

    def __contains__(self, value):
        return value in self._additive_group

    def zero(self):
        return self._additive_group.zero()

    def _repr_(self):
        return repr(self._additive_group)


@cached_function
def _additive_group_exponential(additive_group):
    r"""Realize multiplicative notation by Sage's maintained ``GroupExp`` functor.

    The adapter owns the two crossings; both public endpoints and every
    value of the identification are owned objects. Sage reference:
    ``sage.groups.group_exp.GroupExp``.
    """
    from sage.groups.group_exp import GroupExp

    engine = GroupExp()(_AdditiveGroupForGroupExp(additive_group))
    # The selected additive law proves exp(a)exp(b) = exp(b)exp(a).
    group = _own_group(engine, refinements=(OwnedGroups().Commutative(),))
    forward = Sets().Mor(additive_group, group)(
        lambda element: group._from_engine(engine._element_constructor_(element))
    )
    backward = Sets().Mor(group, additive_group)(
        lambda element: additive_group(group._to_engine(element).value)
    )
    # GroupExp wraps an additive element; reading its value reverses that
    # constructor. This inverse pair belongs to the notation-change functor.
    return Sets().Core().Mor(additive_group, group)._from_known_inverse_pair(forward, backward)


def _element_to_engine(group, element):
    r"""Return the GAP element modelling ``element`` of ``group``."""
    match group:
        case _ if group in GroupAutomorphismGroups():
            return element.gap()
        case _:
            assert _encodes_elements_in_gap(_engine_group(group)), (
                f"an element of {group} cannot be passed to GAP: the elements of {group} are not "
                f"represented as permutations, words, or GAP group elements"
            )
            return group._to_engine(group(element)).gap()


def _element_from_engine(group, gap_element):
    r"""Return the element of ``group`` modelled by ``gap_element``."""
    match group:
        case _ if group in GroupAutomorphismGroups():
            return group(gap_element, check=False)
        case _:
            engine = _engine_group(group)
            assert _encodes_elements_in_gap(engine), (
                f"a GAP element cannot be read as an element of {group}: the elements of {group} are not "
                f"represented as permutations, words, or GAP group elements"
            )
            return group._from_engine(engine(gap_element))


def _matrix_group_element_matrix(group, element):
    r"""Return the private exact matrix of one owned matrix-group element.

    Protected group contract (\`OWN-05\`--\`OWN-07\`).  The permitted
    external caller is the Eichler determinant-model lattice adapter for its
    represented \`SL_2(ZZ)\` action.  The group owner validates and lowers the
    owned element; only the exact matrix required by that adapter crosses, and
    its entries are immediately raised into the lattice's owned scalar ring.
    """
    represented = group._to_engine(group(element))
    matrix = getattr(represented, "matrix", None)
    assert callable(matrix), f"{element} has no matrix: {group} is not a matrix group"
    return matrix()


def _subgroup_from_gap(group, gap_subgroup):
    r"""Return the owned subgroup of ``group`` modelled by the GAP subgroup.

    Uses Sage's private ``_subgroup_constructor`` of
    ``sage.groups.perm_gps.permgroup.PermutationGroup_generic`` and
    ``sage.groups.libgap_wrapper.ParentLibGAP``, which builds the engine
    subgroup of a GAP subgroup without re-reading its generators; no public
    Sage operation constructs a subgroup from a GAP subgroup object.
    """
    engine = _engine_group(group)
    match engine:
        case PermutationGroup_generic() | ParentLibGAP():
            return _transported_subgroup(group, engine._subgroup_constructor(gap_subgroup))
        case _:
            assert False, f"{group} does not construct subgroups from GAP data in this engine"


def _finite_order(group):
    r"""Return the order of a finite group as an owned integer."""
    match group:
        case _ if group in GroupAutomorphismGroups():
            backend_order = _gap_model(group).Size().sage()
        case _:
            backend_order = _engine_group(group).order()
    return _owned_engine_element(ZZ, ZZ(backend_order))


def _finite_group_morphism_kernel_cardinality(morphism):
    r"""Return the exact kernel order without exporting the GAP morphism."""
    return cardinal(
        int(morphism._gap_morphism_crossing().Kernel().Size())
    )


def _finite_group_morphism_kernel_is_abelian(morphism) -> bool:
    r"""Decide kernel abelianity without exporting the GAP morphism."""
    return bool(morphism._gap_morphism_crossing().Kernel().IsAbelian())


def _conjugacy_class_elements(group, representative):
    r"""Return the elements of the conjugacy class of ``representative`` in the finite ``group``."""
    engine = _engine_group(group)
    return tuple(
        group._from_engine(engine_element)
        for engine_element in engine.conjugacy_class(group._to_engine(representative))
    )


def _conjugacy_class_size(group, representative):
    r"""Return the size |G : C_G(g)| of the conjugacy class of ``representative``, a count used as an integer scalar."""
    return int(
        libgap.ConjugacyClass(
            _gap_model(group),
            _element_to_engine(group, representative),
        ).Size()
    )


def _engine_generated_subgroup(engine, engine_generators):
    r"""Return the engine's subgroup generated by engine elements."""
    match engine:
        case PermutationGroup_generic() | MatrixGroup_generic() | AbelianGroup_class() | ParentLibGAP():
            return engine.subgroup(list(engine_generators))
        case _:
            assert False, f"the subgroup of {engine} generated by given elements cannot be computed: this is available only for permutation, matrix, abelian and GAP-based groups"


def _engine_subgroup_admits(subgroup, element) -> bool:
    r"""Whether the engine subgroup computing ``subgroup`` contains ``element``.

    This is the private engine-membership adapter (``OWN-06``): cross the
    owned element once through its containing group, then ask the represented
    engine subgroup whether that engine element belongs to it.  Membership is
    therefore a predicate, not exception-driven control flow.
    """
    return subgroup.supergroup()._engine_subgroup_contains(element, _engine_group(subgroup))


def _engine_cosets(group, subgroup, side):
    r"""Return the cosets of ``subgroup`` on ``side``, each an ordered set of elements."""
    engine = _engine_group(group)
    assert _encodes_as_permutations(engine), (
        f"the cosets of {subgroup} in {group} cannot be listed: cosets are enumerated only in permutation groups, "
        f"and {group} is not a permutation group"
    )
    # The owned coset gH = {g h} is {h *_engine g} when the engine law is
    # the owned law reversed: the engine's coset on the other side.
    engine_side = {"left": "right", "right": "left"}[side] if _law_reversed(group) else side
    backend_cosets = engine.cosets(_engine_group(subgroup), side=engine_side)
    coset_positions = Sets.Δ[len(backend_cosets) - 1]

    def own_coset(backend_members):
        member_positions = Sets.Δ[len(backend_members) - 1]
        return FiniteOrderedSets().from_indexed(
            member_positions,
            lambda member_position: group._from_engine(backend_members[int(member_position)]),
            name="Coset elements",
        )

    # Each coset is one object: build them once, so a coset read back from a
    # representative is the coset the family already holds.
    owned_cosets = tuple(own_coset(backend_members) for backend_members in backend_cosets)
    return FiniteOrderedSets().from_indexed(
        coset_positions,
        lambda position: owned_cosets[int(position)],
        name=f"{side.capitalize()} cosets",
    )


def _encodes_as_permutations(engine) -> bool:
    r"""Whether ``engine`` is a Sage permutation group."""
    match engine:
        case PermutationGroup_generic():
            return True
        case _:
            return False


def _engine_generators(group):
    r"""Return the engine's chosen generators of ``group``.

    For a group encoded by words, the chosen generators are the images of
    the presentation's free basis, one per word position whether or not it
    is trivial in the group: deciding that a word is trivial is the word
    problem, and the positions are what a word's letters index.  Any other
    engine's generators are read without the identity.
    """
    engine = _engine_group(group)
    backend_generators = tuple(engine.gens())
    if _encodes_as_words(engine):
        from dzack_research.preamble.categories.sets.finite_families import finite_family

        return finite_family(tuple(group._from_engine(generator) for generator in backend_generators))
    owned_generators = finite_ordered_set(tuple(group._from_engine(generator) for generator in backend_generators))
    identity = group.one()
    return owned_generators.filtered(
        lambda generator: generator != identity,
        name="Chosen group generators",
    )


def _engine_basis_label(basis, label):
    r"""Return the engine's index of a point of an owned free basis.

    A finite basis is encoded by the positions of its enumeration, an owned
    ring by its engine elements, and any other set by its own points; these
    are the index sets :func:`_free_group_constructor` hands the engine.
    """
    match basis:
        case _ if basis in FiniteSets():
            assert label in basis, f"{label!r} is not a free generator: it is not an element of the free basis {basis}"
            return next(position for position, candidate in enumerate(basis) if candidate == label)
        case _ if basis in OwnedRings():
            return _engine_element(basis, label)
        case _:
            return label


def _owned_basis_label(basis, engine_label):
    r"""Return the point of an owned free basis indexed by the engine label."""
    match basis:
        case _ if basis in FiniteSets():
            return next(candidate for position, candidate in enumerate(basis) if position == int(engine_label))
        case _ if basis in OwnedRings():
            return _owned_engine_element(basis, engine_label)
        case _:
            return engine_label


def _free_generator(group, index):
    r"""Return the free generator of ``group`` indexed by a point of its free basis."""
    basis = group.free_basis()
    label = index if index in basis else basis(index)
    return group._from_engine(_engine_group(group).gen(_engine_basis_label(basis, label)))


def _reduced_word_data(group, element):
    r"""Read private reduced-word coordinates in the owned multiplication order.

    Sage's finite FreeGroup uses signed positions (Tietze); IndexedFreeGroup
    uses basis labels with exponents.  Both represent finite words, including
    when the generating set is infinite.  This coordinate data is private to
    the free-group owner; public words are families of owned signed generators.
    """
    basis = group.free_basis()
    backend = group._to_engine(group(element))
    match _engine_group(group):
        case FreeGroup_class():
            letters = tuple(
                (_owned_basis_label(basis, abs(letter) - 1), 1 if letter > 0 else -1)
                for letter in backend.Tietze()
            )
        case IndexedFreeGroup():
            letters = tuple(
                (_owned_basis_label(basis, index), exponent)
                for index, exponent in backend.to_word_list()
            )
    return letters[::-1] if _law_reversed(group) else letters


def _free_group_conjugacy(group, source, target) -> bool:
    r"""Whether ``source`` and ``target`` are conjugate in the free group ``group``.

    Sage decides it: ``is_conjugate`` of an element of a finite-rank
    ``FreeGroup`` (``ElementLibGAP.is_conjugate``) is GAP's
    ``IsConjugate``, which dispatches to the FGA package's
    ``RepresentativeActionOp`` for conjugation of elements in a free group
    (``fga/lib/ReprAct.gi``); it compares cyclically reduced words up to
    cyclic permutation.  ``IndexedFreeGroup`` has no such method, so both
    engines are read through their reduced words.  The two words use finitely many
    letters ``S'`` of the basis ``S``, and the retraction ``F(S) -> F(S')``
    sending the other letters to ``1`` fixes ``F(S')``, so they are
    conjugate in ``F(S)`` exactly when they are conjugate in ``F(S')``.
    That finite-rank free group is the one the question is asked in,
    whatever the cardinality of ``S``.  The words are read in the owned
    order; conjugacy is the same relation under the engine's reversed
    product, since reversal is an anti-automorphism.
    """
    from sage.groups.free_group import FreeGroup

    words = tuple(_reduced_word_data(group, element) for element in (source, target))
    positions = {}
    for word in words:
        for label, _ in word:
            positions.setdefault(label, len(positions) + 1)
    finite_rank = FreeGroup(max(len(positions), 1))
    finite_source, finite_target = (
        finite_rank(
            [
                positions[label] if exponent > 0 else -positions[label]
                for label, exponent in word
                for _ in range(abs(int(exponent)))
            ]
        )
        for word in words
    )
    return bool(finite_source.is_conjugate(finite_target))


def _reduced_word_syllables(group, element):
    r"""Return the reduced word as syllables ``(s, e)``: a basis point and its nonzero exponent.

    Consecutive letters on the same basis point merge into one syllable, so
    both engines give the same syllables for the same element.
    """
    syllables = []
    for label, exponent in _reduced_word_data(group, element):
        if syllables and syllables[-1][0] == label:
            syllables[-1] = (label, syllables[-1][1] + int(exponent))
        else:
            syllables.append((label, int(exponent)))
    return tuple(syllables)


def _reduced_word(group, element):
    r"""Return the reduced word as an owned finite family of signed generators."""
    from dzack_research.preamble.categories.sets.finite_families import finite_family

    letters = []
    for index, exponent in _reduced_word_data(group, element):
        exponent = int(exponent)
        assert exponent != 0, f"the reduced word of {element} in {group} has a letter {index} with exponent 0; a reduced word has only nonzero exponents"
        generator = _free_generator(group, index)
        letter = generator if exponent > 0 else ~generator
        letters.extend(letter for _ in range(abs(exponent)))
    return finite_family(letters, name="Reduced group word")


def _law_reversed(group) -> bool:
    r"""Whether the owned product of ``group`` is its engine's product reversed.

    The owned product is composition of the maps a group's elements act as.
    Matrix engines already multiply as such maps on column vectors.  Sage's
    permutation groups and GAP's word and automorphism groups multiply left
    to right, ``(g h)(x) = h(g(x))``, so their owned product is reversed.
    """
    match group:
        case _ if group in GroupAutomorphismGroups():
            return True
        case _:
            return _engine_law_reversed(_engine_group(group))


def _engine_law_reversed(engine) -> bool:
    match engine:
        case CoxeterMatrixGroup() | NamedMatrixGroup_generic() | FinitelyGeneratedMatrixGroup_generic():
            return False
        case PermutationGroup_generic() | FreeGroup_class() | FinitelyPresentedGroup() | IndexedFreeGroup() | AbelianGroup_class() | ParentLibGAP():
            return True
        case _:
            return False


def _engine_generator_epimorphism(group, generators):
    r"""GAP's epimorphism ``F(S) ->> G`` onto the chosen generators ``generators`` of ``group``.

    Engine adapter (``OWN-06``).  ``PreImagesRepresentative`` of the result
    writes an element of ``group`` as a word in ``generators``; free
    generator ``i`` of ``F(S)`` is sent to the ``i``-th of ``generators``.
    """
    models = libgap([_element_to_engine(group, generator) for generator in generators])
    # A map induced by generator images is defined on all of G only when
    # these elements generate G. In particular GroupHomomorphismByImagesNC
    # does not certify surjectivity or even its own homomorphism law.
    if libgap.Subgroup(_gap_model(group), models) != _gap_model(group):
        raise ValueError(
            f"the selected generators do not generate the source group {group}"
        )
    free = libgap.FreeGroup(models.Length())
    return libgap.GroupHomomorphismByImagesNC(
        free,
        _gap_model(group),
        free.GeneratorsOfGroup(),
        models,
    )


def _engine_generator_relators(group, epimorphism):
    r"""Relators of ``group`` as words in the generators that ``epimorphism`` hits.

    Engine adapter (``OWN-06``).  The words generate the kernel of the
    epimorphism ``F(S) ->> G`` as a normal subgroup; letter ``i`` of each
    word is generator ``i`` of ``epimorphism``.
    """
    generator_models = epimorphism.MappingGeneratorsImages()[1]
    return libgap.IsomorphismFpGroupByGenerators(
        _gap_model(group),
        generator_models,
    ).Range().RelatorsOfFpGroup()


def _engine_word_letters(group, word):
    r"""The letters ``(position, sign)`` of a GAP word in chosen generators of ``group``.

    Engine adapter (``OWN-06``).  The letters are in the owned multiplication
    order of ``group``; positions count from zero.
    """
    letters = tuple(
        (abs(int(letter)) - 1, 1 if letter > 0 else -1)
        for letter in word.LetterRepAssocWord().sage()
    )
    return letters[::-1] if _law_reversed(group) else letters


def _integer_engine_point(point):
    r"""An owned integer as the engine's integer; any other point unchanged."""
    integers = _own_ring(ZZ)
    return _engine_element(integers, integers(point)) if point in integers else point


def _engine_point(engine, point):
    r"""Cross an owned point into the domain of a Sage permutation group."""
    engine_point = _integer_engine_point(point)
    return engine_point if engine_point in engine.domain() else point


def _owned_point(point):
    r"""Read a point of a Sage permutation group's domain as an owned point."""
    match point:
        case Integer():
            return _owned_engine_element(ZZ, point)
        case _:
            return point


def _engine_element_action(group, backend_element, point):
    r"""Apply an engine element to a point.

    A Galois group acts on its field by automorphisms; a permutation
    group acts on the points of its selected permutation domain.
    """
    engine = _engine_group(group)
    match engine:
        case SageGaloisGroup():
            field = _own_ring(engine.number_field())
            assert point in field, f"{group} acts on the field {field} by automorphisms, but {point} is not an element of {field}"
            return _owned_engine_element(field, backend_element.as_hom()(_engine_element(field, point)))
        case PermutationGroup_generic():
            return group._permutation_point_action(backend_element, point)
        case _:
            assert False, f"an element of {group} cannot be applied to {point}: {group} is neither a permutation group nor a Galois group, so it has no action on points"


def _engine_word(group, backend_element):
    r"""Return the word of an engine element in the chosen generators, as signed generator positions."""
    engine = _engine_group(group)
    assert _encodes_as_words(engine), (
        f"an element of {group} cannot be written as a word in the generators: {group} is neither a free group "
        f"nor a finitely presented group"
    )
    word = tuple(int(letter) for letter in backend_element.Tietze())
    return word[::-1] if _law_reversed(group) else word


def _encodes_as_words(engine) -> bool:
    r"""Whether ``engine`` encodes its elements as words in its chosen generators."""
    match engine:
        case FreeGroup_class() | FinitelyPresentedGroup():
            return True
        case _:
            return False


def _engine_element_text(group, backend_element) -> str:
    r"""Return the owned notation for an engine element, or the empty string."""
    engine = _engine_group(group)
    match engine:
        case FinitelyPresentedGroup():
            return " ".join(
                f"g_{abs(letter)}" if letter > 0 else f"g_{abs(letter)}^-1"
                for letter in _engine_word(group, backend_element)
            )
        case PermutationGroup_generic():
            cycles = tuple(tuple(cycle) for cycle in backend_element.cycle_tuples())
            return "".join("(" + " ".join(map(str, cycle)) + ")" for cycle in cycles)
        case _:
            return ""


def _engine_element_latex(group, backend_element) -> str:
    r"""Return the owned LaTeX for an engine element, or the empty string."""
    match _engine_group(group):
        case FinitelyPresentedGroup():
            return " ".join(
                rf"g_{{{abs(letter)}}}" if letter > 0 else rf"g_{{{abs(letter)}}}^{{-1}}"
                for letter in _engine_word(group, backend_element)
            )
        case _:
            return ""


def _chosen_engine_presentation(engine):
    r"""Return the free source and backend relators already defining ``engine``."""
    match engine:
        case FreeGroup_class():
            return None, ()
        case FinitelyPresentedGroup():
            return engine.free_group(), tuple(engine.relations())
        case CoxeterMatrixGroup():
            free, relations = _coxeter_presentation(engine.coxeter_matrix())
            return free, relations
        case _:
            raise TypeError(f"{engine} is not given by a finite presentation: it is neither a free group, a finitely presented group, nor a Coxeter group")


def _computed_finitely_presented_engine(group):
    r"""Compute one maintained finitely presented model of ``group``."""
    engine = _engine_group(group)
    match engine:
        case PermutationGroup_generic():
            return engine.as_finitely_presented_group()
        case AbelianGroup_class():
            return engine.permutation_group().as_finitely_presented_group()
        case FinitelyGeneratedMatrixGroup_gap() if _engine_finiteness(engine) is True:
            return engine.as_permutation_group().as_finitely_presented_group()
        case NamedMatrixGroup_generic() | NamedMatrixGroup_gap():
            return engine.as_permutation_group().as_finitely_presented_group()
        case _:
            assert False, f"no finite presentation of {group} can be computed: this is available only for permutation groups, finite abelian groups, and finite matrix groups"


def _group_generating_epimorphism(group, source, labels, generator_morphism):
    r"""Return the group morphism ``F(S) -> group`` induced by a map of the free basis ``S`` into ``group``."""
    assert source.free_basis() is labels, (
        f"the free group {source} does not have {labels} as its free basis, so it cannot map onto {group} by sending the free generators to the elements indexed by {labels}"
    )
    return source.Mor(group)(generator_morphism)


def _fix_selected_group_resolution_data(
    group,
    source,
    labels,
    generator_morphism,
    *,
    replace=False,
) -> None:
    r"""Retain one explicit free-group augmentation as truncation-zero data."""
    _fix_selected_resolution(
        group,
        OwnedGroups(),
        lambda: _selected_group_resolution(group, source, labels, generator_morphism),
        replace=replace,
    )


def _fix_selected_group_resolution_on(group, generating_set, *, replace=False) -> None:
    r"""Retain the free-group augmentation on a generating subset computed at first read.

    ``generating_set`` is a zero-argument computation of a subset ``S`` of
    ``group``.  Fixing the datum computes nothing: ``S``, the free group
    ``F(S)`` and the augmentation ``F(S) -> group`` induced by the inclusion
    ``S -> group`` are built when the selected resolution is first read.
    """

    def selected_resolution():
        generators = generating_set()
        source = Groups.Free(index_set=generators)
        inclusion = Sets().Mor(generators, group)(lambda generator: generator)
        return _selected_group_resolution(group, source, generators, inclusion)

    _fix_selected_resolution(group, OwnedGroups(), selected_resolution, replace=replace)


def _selected_group_resolution(group, source, labels, generator_morphism):
    r"""The truncation-zero free-group resolution ``source -> group`` on ``labels``."""
    from dzack_research.preamble.categories.abstract_categories.resolutions import (
        Resolutions,
    )

    augmentation = _group_generating_epimorphism(group, source, labels, generator_morphism)
    free = GroupsWithChosenFreeBasis()
    return Resolutions(OwnedGroups(), free, 0, free).selected_degree_zero(
        group,
        source,
        augmentation,
        generating_set=labels,
        generator_morphism=generator_morphism,
    )


def _fix_selected_group_resolution(group, *, free_basis=None) -> None:
    r"""Retain one chosen degree-zero free-group resolution."""
    if free_basis is not None:
        source = group
        labels = free_basis
        generator_morphism = Sets().Mor(labels, group)(group.free_generator)
        _fix_selected_group_resolution_data(
            group, source, labels, generator_morphism
        )
        return

    generators = _engine_generators(group)
    source = Groups.Free(index_set=generators)
    generator_morphism = Sets().Mor(generators, group)(lambda generator: group(generator))
    _fix_selected_group_resolution_data(
        group, source, generators, generator_morphism
    )


def _fix_selected_group_presentation(group, source, relations) -> None:
    r"""Install one constructor-selected presentation as a truncation-one resolution."""
    labels = source.free_basis()
    generators = _engine_generators(group)
    assert generators.cardinality() == labels.cardinality(), (
        f"{group} has {generators.cardinality()} generators, but the presentation on {source} has "
        f"{labels.cardinality()} free generators; a presentation must send each free generator to one generator"
    )
    ranking = labels.ranking_map()
    generator_morphism = Sets().Mor(labels, group)(
        lambda label: generators[int(ranking(label))]
    )
    selected_relations = finite_ordered_set(tuple(relations))

    def selected_resolution():
        relation_labels = finite_ordinal_set(int(selected_relations.cardinality()))
        degree_one_labels = finite_ordered_set(
            tuple(("generator", label) for label in labels)
            + tuple(("relation", index) for index in relation_labels)
        )
        degree_one = Groups.Free(index_set=degree_one_labels)
        relation_source = Groups.Free(index_set=relation_labels)

        def first_face_value(tagged):
            match tagged[0]:
                case "generator":
                    return source.free_generator(tagged[1])
                case "relation":
                    return source.one()

        def second_face_value(tagged):
            match tagged[0]:
                case "generator":
                    return source.free_generator(tagged[1])
                case "relation":
                    return selected_relations[int(tagged[1])]

        first_face = degree_one.Mor(source)(
            Sets().Mor(degree_one_labels, source)(first_face_value)
        )
        second_face = degree_one.Mor(source)(
            Sets().Mor(degree_one_labels, source)(second_face_value)
        )
        degeneracy = source.Mor(degree_one)(
            Sets().Mor(labels, degree_one)(
                lambda label: degree_one.free_generator(("generator", label))
            )
        )
        augmentation = _group_generating_epimorphism(
            group, source, labels, generator_morphism
        )
        return OwnedGroups().FinitelyPresentedAsGroup().resolution_category().selected_presentation(
            group,
            source,
            degree_one,
            augmentation,
            first_face,
            second_face,
            degeneracy,
            generating_set=labels,
            generator_morphism=generator_morphism,
            relation_source=relation_source,
            relations=selected_relations,
        )

    _fix_selected_resolution(
        group,
        OwnedGroups(),
        selected_resolution,
        replace=True,
    )


def _engine_quotient_by_relators(group, relators, *, quotient_category=None):
    r"""Return ``G / <<relators>>`` with its actual quotient presentation.

    A selected free-quotient category is passed into the *same* owned
    construction that receives the quotient engine. Re-wrapping an already
    owned group is not a change of its category, so that intermediate
    owned realization must not replace the selected quotient constructor.
    """
    engine = _engine_group(group)
    match engine:
        case FreeGroup_class():
            quotient = engine.quotient([group._to_engine(group(relator)) for relator in relators])
            if quotient_category is None:
                return _own_group(quotient)
            return _own_group(
                quotient,
                refinements=(quotient_category,),
                presentation_source_group=group,
                chosen_presentation=(group, quotient_category.relators()),
            )
        case FinitelyPresentedGroup():
            # G = F/R and G/<<S>> = F/<<R, S>>, with S lifted to words in F.
            free = engine.free_group()
            relations = list(engine.relations()) + [free(group._to_engine(group(relator)).Tietze()) for relator in relators]
            return _own_group(free.quotient(relations))
        case _:
            assert False, f"the quotient of {group} by the normal closure of {relators} cannot be computed: this is available only for free groups and finitely presented groups"


def _engine_abelianity(engine):
    r"""Whether the engine's structure decides its group abelian, else ``None``.

    ``F_0`` and ``F_1`` are abelian; ``F_n`` for ``n >= 2`` contains two
    noncommuting free generators.  This reads the rank of the represented
    free group and performs no search.  ``None`` means that the engine's
    structure supplies no witness either way.
    """
    match engine:
        case FreeGroup_class():
            return engine.ngens() <= 1
        case _:
            return None


# Witnesses read off an engine for the placement of the group it realizes.
# Each is a positive witness: ``False`` means the engine supplied none, never
# that the property fails.


def _is_abelian_witness(engine) -> bool:
    if engine.category().is_subcategory(SageGroups().Commutative()):
        return True
    match engine:
        case AbelianGroup_class() | AbelianGroup_subgroup():
            return True
        case FreeGroup_class():
            return engine.ngens() <= 1
        case IndexedFreeGroup():
            # A free group is abelian exactly when its rank is at most one;
            # Sage implements no is_abelian for the rank-zero indexed one.
            return bool(engine.indices().cardinality() <= 1)
        case FinitelyPresentedGroup():
            # A bare finite presentation is not a cheap abelianity certificate:
            # Sage/GAP may launch a coset-table computation to decide it.
            return False
        case _:
            # Finite order is not a certificate of commutativity. In
            # particular Sage's Coxeter matrix groups may advertise finite
            # order while their is_abelian() algorithm is unavailable.
            # Membership in the commutative refinement requires a witness,
            # not an eager general-purpose group computation at ingress.
            return False


def _has_chosen_generators(engine) -> bool:
    match engine:
        case PermutationGroup_generic() | AbelianGroup_class() | FreeGroup_class() | FinitelyPresentedGroup() | FinitelyGeneratedMatrixGroup_generic() | FinitelyGeneratedMatrixGroup_gap() | CoxeterMatrixGroup():
            return True
        case _:
            return False


def _has_chosen_presentation(engine) -> bool:
    match engine:
        case FreeGroup_class() | FinitelyPresentedGroup() | CoxeterMatrixGroup():
            return True
        case _:
            return False


def _is_finite_rank_free(engine) -> bool:
    r"""Whether ``engine`` is a free group on a finite set: finitely generated and presented with no relations."""
    match engine:
        case FreeGroup_class():
            return True
        case IndexedFreeGroup():
            return bool(engine.indices().is_finite())
        case _:
            return False


def _is_finitely_generated_witness(engine) -> bool:
    return (
        _engine_finiteness(engine) is True
        or _has_chosen_generators(engine)
        or _is_finite_rank_free(engine)
    )


def _is_finitely_presented_witness(engine) -> bool:
    match engine:
        case FinitelyPresentedGroup() | CoxeterMatrixGroup() | AbelianGroup_class():
            return True
        case _ if _is_finite_rank_free(engine):
            return True
        case _:
            return _engine_finiteness(engine) is True


def _owned_group_category(engine) -> Category:
    r"""Return the category an engine-realized group is constructed in.

    The placement adapter: the one site reading an engine's representation
    type to decide which owned categories the group it realizes belongs to.
    A chosen free basis is a datum its constructor supplies, so that
    placement is made by :func:`_own_group`, not here.
    """
    finiteness = _engine_finiteness(engine)
    witnessed = (
        (True, OwnedGroups()),
        (finiteness is True, OwnedGroups().Finite()),
        (finiteness is False, OwnedGroups().Infinite()),
        (_is_abelian_witness(engine), OwnedGroups().Commutative()),
        (_is_finitely_generated_witness(engine), OwnedGroups().FinitelyGeneratedAsMagma()),
        (_is_finitely_presented_witness(engine), OwnedGroups().FinitelyPresentedAsGroup()),
        (_has_chosen_presentation(engine), GroupsWithChosenFinitePresentation()),
        (_encodes_as_permutations(engine), PermutationGroups()),
    )
    return Cat().meet(tuple(category for holds, category in witnessed if holds))


# --------------------------------------------------------------------------
# The private group realization.
# --------------------------------------------------------------------------


class _GroupEngine:
    r"""Private Sage/GAP realization selected by the OwnedGroups entry.

    The represented group retains its engine, not a second category node.
    Subgroups retain their containing group at Subgroups(G); the crossing
    keeps their elements in that containing group.  The native catalogue
    continues to supply permutation, matrix, word and other group engines.
    """

    def __init__(self, engine, description=None, **rest) -> None:
        self._engine = engine
        self._description = description
        super().__init__(**rest)

    def _engine_group(self):
        return self._engine

    def _to_engine(self, element):
        supergroup = self.supergroup()
        if supergroup is not self:
            return supergroup._to_subgroup_engine(element, self._engine)
        assert element in self, f"{element} is not an element of the group {self}"
        return element._backend()

    def _from_engine(self, engine_element):
        supergroup = self.supergroup()
        if supergroup is not self:
            return supergroup._from_subgroup_engine(engine_element)
        return self.element_class(self, self._engine(engine_element))

    def _engine_subgroup_from_generators(self, generators):
        return _engine_generated_subgroup(
            self._engine,
            [self._to_engine(generator) for generator in generators],
        )

    def _to_subgroup_engine(self, element, engine_subgroup):
        return engine_subgroup(self._to_engine(element))

    def _engine_subgroup_contains(self, element, engine_subgroup):
        return self._to_engine(element) in engine_subgroup

    def _from_subgroup_engine(self, engine_element):
        return self._from_engine(engine_element)

    def __call__(self, value):
        return self._element_constructor_(value)

    def _element_constructor_(self, value):
        r"""Admit an element of this group, of another owned group, or a literal.

        The boundary admitting foreign values: a raw engine element is
        refused, an element of another owned group crosses through that
        group's engine crossing, and a literal is read by the engine.
        """
        supergroup = self.supergroup()
        if supergroup is not self:
            element = supergroup(value)
            if element not in self:
                raise ValueError(f"{element} is not in {self}")
            return element
        if value in self:
            return value
        if isinstance(value, Element) and value.parent() in OwnedGroups():
            return self._from_engine(value.parent()._to_engine(value))
        if isinstance(value, SageObject):
            raise TypeError(f"{value} cannot be made an element of {self}: it is a Sage object, not an element of a preamble group")
        return self._from_engine(value)

    def __contains__(self, value) -> bool:
        r"""Test group elements, not categorical objects of a mixed Mor parent."""
        match value:
            case Element() if self.supergroup() is self:
                return value.parent() is self
            case Element():
                if value not in self.supergroup():
                    return False
                if self in GeneratedSubgroups(self.supergroup()) and self.supergroup().is_finite() is not True:
                    decision = self.membership_decision(value)
                    if decision is True:
                        return True
                    raise TypeError(f"membership of {value} in {self} is undecided; supply a word witness to membership_decision")
                return _engine_subgroup_admits(self, value)
            case _:
                return False

    def __iter__(self):
        return (self._from_engine(element) for element in self._engine)

    def one(self):
        return self._from_engine(self._engine.one())

    def _repr_(self):
        if self._description is not None:
            return self._description
        supergroup = self.supergroup()
        if supergroup is not self:
            return f"Subgroup of {supergroup}"
        match self:
            case _ if self.has_selected_group_resolution() and self in OwnedFiniteGroups():
                return f"Group of order {self.cardinality()} generated by {self.group_generators()}"
            case _ if self.has_selected_group_resolution():
                return f"Group generated by {self.group_generators()}"
            case _:
                return f"Group in {self.category()}"

    def _latex_(self):
        if self._description is not None:
            escaped = self._description.replace("_", r"\_")
            return rf"\text{{{escaped}}}"
        match self:
            case _ if self.has_selected_group_resolution() and self.group_generators().index_set() in FiniteSets():
                generators = ", ".join(latex(value) for value in self.group_generators().values())
                return rf"\langle {generators}\rangle"
            case _:
                return r"\mathrm{Group}"

    def _abelianity_decision(self):
        engine_decision = _engine_abelianity(self._engine)
        match self:
            case _ if self in OwnedFiniteGroups():
                return bool(_gap_model(self).IsAbelian())
            case _ if engine_decision is not None:
                return engine_decision
            case _:
                return AtomicProposition("is_abelian", self)

    def _arithmeticity_decision(self):
        return AtomicProposition("is_arithmetic_group", self)


class _GroupElement(MultiplicativeGroupElement):
    r"""An element represented privately by its Sage/GAP group element."""

    def __init__(self, parent, backend_element) -> None:
        MultiplicativeGroupElement.__init__(self, parent)
        self._backend_element = backend_element

    def _backend(self):
        return self._backend_element

    def _mul_(self, other):
        r"""``self * other`` is the composition ``self ∘ other``.

        A group acts on the left: ``rho(g h) = rho(g) rho(h)``, the product
        of the matrices acting on an ordered basis.  Sage's permutation
        groups and GAP's word groups multiply left to right,
        ``(g h)(x) = h(g(x))``, so for those engines the owned product is
        the engine product reversed.
        """
        parent = self.parent()
        left, right = self._backend(), other._backend()
        if _law_reversed(parent):
            left, right = right, left
        return parent._from_engine(left * right)

    def __call__(self, point):
        r"""Apply this element to a point of the set it acts on."""
        return _engine_element_action(self.parent(), self._backend(), point)

    def _invert_(self):
        return self.parent()._from_engine(~self._backend())

    def __invert__(self):
        return self._invert_()

    def __pow__(self, exponent, modulus=None):
        if modulus is not None:
            return NotImplemented
        return self.parent()._from_engine(self._backend() ** int(exponent))

    def _richcmp_(self, other, op):
        if other not in self.parent():
            return NotImplemented
        return richcmp(self._backend(), other._backend(), op)

    def __eq__(self, other):
        return other in self.parent() and self._backend() == other._backend()

    def __ne__(self, other):
        return negation(self == other)

    def __hash__(self):
        return hash((id(self.parent()), self._backend()))

    def is_one(self):
        return self == self.parent().one()

    def order(self):
        r"""The order of this element: an integer when finite, else the cardinality of ``<g>``."""
        backend_order = self._backend().order()
        if backend_order == infinity:
            return aleph(0)
        return _owned_engine_element(ZZ, ZZ(backend_order))

    multiplicative_order = order

    def _cyclic_subgroup_cardinality_decision(self):
        r"""Supply the cardinality of the generated subgroup from the selected engine order."""
        return cardinal(self.order())

    def _repr_(self):
        if self.is_one():
            return "1"
        text = _engine_element_text(self.parent(), self._backend())
        if text:
            return text
        return f"group element of order {self.order()}"

    def _latex_(self):
        if self.is_one():
            return "1"
        text = _engine_element_latex(self.parent(), self._backend())
        if text:
            return text
        return rf"\text{{group element of order }}{latex(self.order())}"


def _owned_group(group):
    r"""Return ``group`` after asserting that it is already a preamble group."""
    assert group in OwnedGroups(), f"{group} is not a group of the preamble's category of groups"
    return group


def _finite_if_bounded_by(group):
    r"""The finite-group placement of a group whose order is at most ``|group|``.

    A subgroup ``H <= G`` and a quotient ``G/N`` of a finite group are finite
    by Lagrange's theorem, ``|G| = |H| [G : H] = |N| |G/N|``, and a chosen
    presentation of ``G`` presents a group isomorphic to ``G``.  So a
    construction of one of these from ``group`` is placed in finite groups at
    construction when ``group`` is, by that theorem, and no order is computed.
    """
    match group:
        case _ if group in OwnedFiniteGroups():
            return (OwnedFiniteGroups(),)
        case _:
            return ()


def _group_mor_placement(domain, codomain, *categories, pointwise=True):
    r"""The placement of ``Mor(G, H)``, the homomorphisms ``G -> H``, at construction.

    A homomorphism ``G -> H`` is a function ``G -> H``, so ``Mor(G, H)`` is a
    subset of ``H^G``: a set, and a finite set of at most ``|H|^|G|``
    elements when ``G`` and ``H`` are finite.  ``Mor(G, G)`` is a monoid under
    composition. If ``H`` is abelian, its pointwise law makes the full
    ``Mor(G,H)`` an abelian group. On the unrestricted diagonal this is
    the endomorphism ring. A restriction such as ``Aut(G)`` supplies
    ``pointwise=False``: sums of automorphisms need not be invertible.
    No homomorphism is counted here; cardinality is computed when asked.
    """
    match domain, codomain:
        case _ if domain in OwnedFiniteGroups() and codomain in OwnedFiniteGroups():
            sets = FiniteSets()
        case _:
            sets = Sets()
    monoids = (Monoids(),) if domain is codomain else ()
    enrichment = ()
    if pointwise and codomain in OwnedGroups().Commutative():
        from dzack_research.preamble.categories.group.additive_mors import AdditiveMorGroups

        enrichment = (
            AbelianGroupEndomorphismRings()
            if domain is codomain else AdditiveMorGroups(),
        )
    return Cat().meet((sets, *monoids, *enrichment, *categories))


@cached_function(
    key=lambda group, refinements, description, free_basis, presentation_source_group, symmetric_points=None, chosen_presentation=None, coxeter_matrix=None, linear_data=None: (
        id(group),
        refinements,
        description,
        id(free_basis),
        id(presentation_source_group),
        id(symmetric_points),
        # Temporary containers do not define construction identity. Keep
        # the actual relation words in the key: their object ids can be
        # reused while the cached group is still alive, whereas the words
        # themselves encode the normal subgroup being imposed.
        None if chosen_presentation is None else (
            chosen_presentation[0],
            tuple(chosen_presentation[1]),
        ),
        id(coxeter_matrix),
        None if linear_data is None else (id(linear_data[0]), linear_data[1]),
    )
)
def _own_group(
    group,
    refinements=(),
    description=None,
    free_basis=None,
    presentation_source_group=None,
    symmetric_points=None,
    chosen_presentation=None,
    coxeter_matrix=None,
    linear_data=None,
):
    r"""Return the owned group realized by the Sage group ``group``.

    The engine adapter through which every engine-realized group enters.  It
    computes the placement the engine witnesses, adds the ``refinements`` a
    construction has proved about the group and, when a free basis was
    chosen, the free-basis data subcategory, and calls the one constructor
    entry of that category.  A Sage subgroup engine enters as a subgroup of
    the owned group realized by its containing engine group.

    Identity is by construction on the defining data (``OWN-10``): the engine
    object, the proved refinements, the catalogue notation, the chosen free
    basis, and—when this is a computed presented model—the exact source group.
    Its comparison images are derived from that source group's selected
    group resolution rather than retained a second time.  Sage groups compare
    structurally, so the engine enters the key by identity, and the cache keeps
    the engine alive while its owned group is.
    """
    if group in OwnedGroups():
        return group
    assert group in SageGroups(), f"{group} is not a group"
    if free_basis is None and isinstance(group, FreeGroup_class):
        free_basis = finite_ordinal_set(int(group.ngens()))
    match group:
        case PermutationGroup_subgroup() | AbelianGroup_subgroup():
            return _transported_subgroup(_own_group(group.ambient_group()), group)
        case ParentLibGAP() if group.ambient() is not group:
            return _transported_subgroup(_own_group(group.ambient()), group)
        case _:
            placement = (_owned_group_category(group), *refinements)
            presentation_data = {}
            if _has_chosen_presentation(group):
                if chosen_presentation is not None:
                    presentation_source, chosen_relations = chosen_presentation
                    owned_relations = finite_ordered_set(chosen_relations)
                else:
                    source_engine, backend_relations = _chosen_engine_presentation(group)
                    presentation_source = None if source_engine is None else _own_group(source_engine)
                    if presentation_source is None:
                        owned_relations = finite_ordered_set(())
                    else:
                        owned_relations = finite_ordered_set(
                            tuple(presentation_source._from_engine(relation) for relation in backend_relations)
                        )
                presentation_data = {
                    "group_presentation_source": presentation_source,
                    "group_presentation_relations": owned_relations,
                    "presentation_source_group": presentation_source_group,
                }
            if free_basis is None:
                owned = _object_of(
                    Cat().meet(placement),
                    _engine=(OwnedGroups(), _GroupEngine, _GroupElement),
                    engine=group,
                    description=description,
                    **({"symmetric_points": symmetric_points} if symmetric_points is not None else {}),
                    **({"selected_coxeter_matrix": coxeter_matrix} if coxeter_matrix is not None else {}),
                    **({"selected_linear_data": linear_data} if linear_data is not None else {}),
                    **presentation_data,
                )
            else:
                owned = _object_of(
                    Cat().meet(
                        (*placement, GroupsWithChosenFreeBasis())
                    ),
                    _engine=(OwnedGroups(), _GroupEngine, _GroupElement),
                    engine=group,
                    description=description,
                    **({"symmetric_points": symmetric_points} if symmetric_points is not None else {}),
                    **({"selected_coxeter_matrix": coxeter_matrix} if coxeter_matrix is not None else {}),
                    **({"selected_linear_data": linear_data} if linear_data is not None else {}),
                    free_basis=free_basis,
                    **presentation_data,
                )
            if free_basis is not None and not _has_chosen_presentation(group):
                _fix_selected_group_resolution(owned, free_basis=free_basis)
            elif not _has_chosen_presentation(group) and _has_chosen_generators(group):
                _fix_selected_group_resolution(owned)
            return owned


def _transported_subgroup(group, engine_subgroup):
    r"""Return the subgroup of ``group`` computed by ``engine_subgroup``."""
    subgroup = _object_of(
        Cat().meet(
            (
                _owned_group_category(engine_subgroup),
                Subgroups(group),
                *_finite_if_bounded_by(group),
            )
        ),
        _engine=(OwnedGroups(), _GroupEngine, _GroupElement),
        engine=engine_subgroup,
        supergroup=group,
    )
    if _is_finitely_generated_witness(engine_subgroup):
        _fix_selected_group_resolution(subgroup)
    return subgroup


def _generated_subgroup(group, engine_subgroup, generators):
    r"""Return the subgroup of ``group`` generated by ``generators``, computed by ``engine_subgroup``."""
    return _object_of(
        Cat().meet(
            (
                _owned_group_category(engine_subgroup),
                GeneratedSubgroups(group),
                *_finite_if_bounded_by(group),
            )
        ),
        _engine=(OwnedGroups(), _GroupEngine, _GroupElement),
        engine=engine_subgroup,
        supergroup=group,
        selected_subgroup_generators=generators,
    )


def _engine_subgroup(group, generators):
    r"""Return the subgroup of ``group`` generated by ``generators``."""
    selected = finite_ordered_set(tuple(group(generator) for generator in generators))
    return _generated_subgroup(
        group,
        group._engine_subgroup_from_generators(selected),
        selected,
    )


class _SubgroupCollection(Sets().ObjectType):
    r"""The set of represented subgroups of one owned group.

    A point is an object of ``Subgroups(G)``, hence retains its inclusion into
    ``G``.  This set is defined for every represented group.  When ``G`` is
    placed among finite groups, GAP supplies an exact enumeration; that
    enumeration is computational structure on the same set, not its definition.
    """

    def __init__(self, group) -> None:
        assert group in OwnedGroups(), (
            f"the subgroup collection is defined for a group, but {group} is not an owned group"
        )
        self._group = group
        match group:
            case _ if group in OwnedFiniteGroups():
                placement = FiniteSets()
            case _:
                placement = Sets()
        super().__init__(category=placement, facade=True)

    def __contains__(self, candidate) -> bool:
        r"""Whether ``candidate`` is a represented subgroup of the ambient group."""
        return candidate in Subgroups(self._group)

    is_parent_of = __contains__

    def _element_constructor_(self, candidate):
        if candidate not in self:
            raise ValueError(
                f"{candidate!r} is not a represented subgroup of {self._group}"
            )
        return candidate

    def __iter__(self):
        r"""Enumerate this set when the ambient represented group is finite."""
        group = self._group
        match group:
            case _ if group in OwnedFiniteGroups():
                return (
                    _subgroup_from_gap(group, subgroup)
                    for subgroup in _gap_model(group).AllSubgroups()
                )
            case _:
                assert False, (
                    f"cannot list all subgroups of {group}: its subgroup collection is defined as a set, "
                    "but exact enumeration is installed only for finite represented groups"
                )

    def _repr_(self) -> str:
        return f"Subgroups of {self._group}"


# --------------------------------------------------------------------------
# Constructor catalogue.
# --------------------------------------------------------------------------


def _group_constructor_argument(value):
    r"""Lower one catalogue argument to the engine constructor's input.

    Literal ingress adapter (``OWN-06``): an owned ring becomes its engine
    ring, an element of an owned group its GAP element, an element of an
    owned ring its engine element, an owned matrix its engine matrix; tuples,
    lists and dictionaries are lowered entrywise, and any other literal is
    already the engine's input.
    """
    match value:
        case tuple():
            return tuple(_group_constructor_argument(entry) for entry in value)
        case list():
            return [_group_constructor_argument(entry) for entry in value]
        case dict():
            return {_group_constructor_argument(key): _group_constructor_argument(entry) for key, entry in value.items()}
        case Parent() if value in OwnedRings():
            return _engine_ring(value)
        case Element() if value.parent() in OwnedGroups():
            return _element_to_engine(value.parent(), value)
        case Element() if value.parent() in OwnedRings():
            return _engine_element(value.parent(), value)
        case ModuleMorphismMethods() if value.parent() in MatrixSpaces(value.domain().base_ring()):
            return _engine_matrix(value)
        case _:
            return value


def _catalogue_group_description(constructor, arguments):
    r"""Return owned mathematical notation for standard catalogue constructors."""
    first = arguments[0] if arguments else None
    match constructor.__name__:
        case "CyclicPermutationGroup" if first is not None:
            return f"Cyclic group C_{first} of order {first}"
        case "SymmetricGroup" if first is not None:
            return f"Symmetric group S_{first}"
        case "AlternatingGroup" if first is not None:
            return f"Alternating group A_{first}"
        case "DihedralGroup" if first is not None:
            return f"Dihedral group D_{first}"
        case "QuaternionGroup":
            return "Quaternion group Q_8"
        case "KleinFourGroup":
            return "Klein four group C_2 x C_2"
        case _:
            return None


def _lowered_arguments(args, kwargs):
    return (
        tuple(_group_constructor_argument(argument) for argument in args),
        {name: _group_constructor_argument(argument) for name, argument in kwargs.items()},
    )


def _owned_group_constructor(constructor):
    @wraps(constructor)
    def construct(*args, **kwargs):
        engine_args, engine_kwargs = _lowered_arguments(args, kwargs)
        return _own_group(
            constructor(*engine_args, **engine_kwargs),
            description=_catalogue_group_description(constructor, args),
        )

    return staticmethod(construct)


def _nilpotent_group_constructor(*args, **kwargs):
    from sage.groups.lie_gps.catalog import Nilpotent as SageNilpotent

    engine_args, engine_kwargs = _lowered_arguments(args, kwargs)
    return _own_group(SageNilpotent(*engine_args, **engine_kwargs))


def _free_group_constructor(n=None, names="x", index_set=None, abelian=False, **kwds):
    r"""The free group of rank ``n``, or the free group on the owned set ``index_set``.

    On an owned set the free basis is construction data of the group.  The
    engine is handed the positions of a finite basis, the engine ring of an
    owned ring, and any other set as it is; :func:`_engine_basis_label`
    reads a basis point in the same encoding.
    """
    from sage.groups.misc_gps.misc_groups_catalog import Free as SageFree

    engine_kwds = {name: _group_constructor_argument(value) for name, value in kwds.items()}
    engine_rank = None if n is None else _group_constructor_argument(n)
    engine_names = _group_constructor_argument(names)
    if index_set is None:
        return _own_group(SageFree(engine_rank, engine_names, index_set=None, abelian=abelian, **engine_kwds))
    assert index_set in Sets(), f"the free group on {index_set} cannot be formed: its index set must be a set of the preamble's category of sets"
    match index_set:
        case _ if index_set in FiniteSets():
            engine_index_set = tuple(range(int(cardinal(index_set.cardinality()).finite_value())))
        case _:
            engine_index_set = _group_constructor_argument(index_set)
    return _own_group(
        SageFree(engine_rank, engine_names, index_set=engine_index_set, abelian=abelian, **engine_kwds),
        free_basis=None if abelian else index_set,
    )


def _group_over_ring(constructor, degree, ring, *args, **kwargs):
    # Matrix and affine group degrees are discrete structural parameters.
    # The shared adapter must not ask an engine to interpret a fractional
    # rank, independently of which named group family is being constructed.
    if degree not in ZZ or degree != ZZ(degree):
        raise ValueError("a group degree must be an integer")
    engine_args, engine_kwargs = _lowered_arguments(args, kwargs)
    return _own_group(
        constructor(
            _group_constructor_argument(degree),
            _engine_ring(_owned_ring(ring)),
            *engine_args,
            **engine_kwargs,
        )
    )


def _GL(degree, ring, var="a"):
    from sage.groups.matrix_gps.catalog import GL

    return _group_over_ring(GL, degree, ring, var=var)


def _SL(degree, ring, var="a"):
    from sage.groups.matrix_gps.catalog import SL

    # Do not allow a nonintegral rank through either the arithmetic witness
    # or the generic engine adapter. This is a defining group parameter,
    # not an approximate numerical argument to be rounded or truncated.
    if degree not in ZZ or degree != ZZ(degree):
        raise ValueError("SL_n(R) requires an integral rank")
    if degree < 1:
        raise ValueError("SL_n(R) requires a positive rank")
    # The arithmetic refinement is specific to the actual integral rank
    # two group. Truncating first would incorrectly identify SL_(5/2)(ZZ)
    # with SL_2(ZZ), bypassing the engine's rank admission.
    if degree == 2 and _owned_ring(ring) is ZZ:
        # The standard integral modular group is arithmetic by its
        # defining integral matrix realization; the axiom does not follow
        # for arbitrary named matrix groups from their engine type alone.
        return _own_group(
            SL(2, _engine_ring(ZZ), var=var),
            refinements=(OwnedGroups().Arithmetic(), OwnedGroups().FinitelyGeneratedAsMagma()),
        )
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

    return _own_group(
        Heisenberg(
            _group_constructor_argument(degree),
            _group_constructor_argument(ring),
        )
    )


def _SemimonomialTransformation(ring, degree):
    from sage.groups.misc_gps.misc_groups_catalog import SemimonomialTransformation

    return _own_group(SemimonomialTransformation(_engine_ring(ring), _group_constructor_argument(degree)))


def _SmallGroup(order, index):
    from sage.groups.perm_gps.permgroup import PermutationGroup

    model = (
        libgap.SmallGroup(
            _group_constructor_argument(order),
            _group_constructor_argument(index),
        )
        .IsomorphismPermGroup()
        .Image()
    )
    return _own_group(PermutationGroup(gap_group=model))


def _Coxeter(data, implementation="reflection", base_ring=None, index_set=None, *, refinements=(), selected_matrix=None):
    from sage.groups.misc_gps.misc_groups_catalog import CoxeterGroup

    from dzack_research.preamble.categories.coxeter_diagrams import _engine_coxeter_matrix_of
    from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily

    match data:
        case IndexedFamily():
            # The owned Coxeter matrix m: V x V -> Card, lowered to Sage's matrix on V.
            data = _engine_coxeter_matrix_of(data)
    scalar_ring = None if base_ring is None else _engine_ring(base_ring)
    return _own_group(
        CoxeterGroup(
            data,
            implementation=implementation,
            base_ring=scalar_ring,
            index_set=index_set,
        ),
        refinements=refinements,
        coxeter_matrix=selected_matrix,
    )


# --------------------------------------------------------------------------
# Subgroup inclusions and the Mor packet.
# --------------------------------------------------------------------------


def _finite_group_quotient_by_gap_normal_subgroup(group, normal_subgroup):
    r"""Raise ``G/N`` and its quotient map from GAP for a represented finite group."""
    from sage.groups.perm_gps.permgroup import PermutationGroup

    assert group in OwnedFiniteGroups(), (
        f"the quotient of {group} by a normal subgroup is computed here only for finite groups, "
        f"and {group} is not known to be finite"
    )
    group_model = _gap_model(group)
    # GAP's IsNormal(G, U) asks whether G normalizes U.
    assert bool(group_model.IsNormal(normal_subgroup)), (
        f"the quotient of {group} by {normal_subgroup} is not a group: {normal_subgroup} is not a normal subgroup of {group}"
    )
    gap_projection = libgap.NaturalHomomorphismByNormalSubgroup(
        group_model,
        normal_subgroup,
    )
    gap_quotient = gap_projection.Image()
    permutation_isomorphism = gap_quotient.IsomorphismPermGroup()
    permutation_model = permutation_isomorphism.Image()
    quotient = _own_group(PermutationGroup(gap_group=permutation_model))
    projection = group.Mor(quotient)(
        gap_projection * permutation_isomorphism
    )
    return quotient, projection


class _AbelianSubgroupQuotientElement(MultiplicativeGroupElement):
    r"""A coset in ``A/H`` represented by one element of the abelian group ``A``."""

    def __init__(self, parent, representative) -> None:
        MultiplicativeGroupElement.__init__(self, parent)
        self._representative = parent.supergroup()(representative)

    def representative(self):
        return self._representative

    def _mul_(self, other):
        return self.parent()(self.representative() * other.representative())

    def _invert_(self):
        return self.parent()(~self.representative())

    def __invert__(self):
        return self._invert_()

    def is_one(self) -> bool:
        return self.representative() in self.parent().subgroup()

    def __eq__(self, other):
        return (
            isinstance(other, _AbelianSubgroupQuotientElement)
            and other.parent() is self.parent()
            and self.representative() * ~other.representative()
            in self.parent().subgroup()
        )

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        r"""A quotient class has no canonical representative in the general predicate case."""
        return hash(id(self.parent()))

    def _repr_(self):
        return f"[{self.representative()}]"


class _AbelianSubgroupQuotientGroup:
    r"""The represented quotient ``A/H`` for a subgroup of an owned abelian group."""

    def __init__(self, subgroup, **rest) -> None:
        ambient = subgroup.supergroup()
        assert ambient in OwnedAbelianGroups(), (
            f"the quotient {ambient}/{subgroup} is constructed here from subgroup membership because the ambient "
            f"group is abelian, but {ambient} is not represented as abelian"
        )
        self._subgroup = subgroup
        super().__init__(**rest)

    def subgroup(self):
        return self._subgroup

    def supergroup(self):
        return self._subgroup.supergroup()

    def __call__(self, representative):
        return self._element_constructor_(representative)

    def _element_constructor_(self, representative):
        if isinstance(representative, _AbelianSubgroupQuotientElement) and representative.parent() is self:
            return representative
        return self.element_class(self, self.supergroup()(representative))

    def __contains__(self, element) -> bool:
        return isinstance(element, _AbelianSubgroupQuotientElement) and element.parent() is self

    def one(self):
        return self(self.supergroup().one())

    @cached_method
    def quotient_projection(self):
        r"""Return the canonical group morphism ``A -> A/H``."""
        return self.supergroup().Mor(self)(lambda element: self(element))

    def _repr_(self):
        return f"{self.supergroup()} / {self.subgroup()}"


def _abelian_subgroup_quotient(subgroup):
    r"""Construct ``A/H`` from represented membership in ``H <= A`` for abelian ``A``."""
    return _object_of(
        Cat().meet((AbelianGroups(), *_finite_if_bounded_by(subgroup.supergroup()))),
        _engine=(OwnedGroups(), _AbelianSubgroupQuotientGroup, _AbelianSubgroupQuotientElement),
        subgroup=subgroup,
    )


def _canonical_subgroup_inclusion(subgroup):
    r"""The inclusion ``H -> G`` of a subgroup whose elements are elements of ``G``."""
    return subgroup.Mor(subgroup.supergroup())._from_subgroup_inclusion()


class GroupMorphism:
    r"""A group morphism, given by generator images, an elementwise rule or a GAP homomorphism.

    Images of the chosen generators of the domain are the defining datum of
    a morphism out of a presented group: a GAP homomorphism into the
    codomain's engine is then computed on the first request.

    The inclusion ``H -> G`` of a subgroup sends ``h`` to ``h``.  Its
    construction gives two premises, which are stored and never checked:
    the arrow is injective (``injectivity_decision``), and its image is the
    domain ``H`` itself (``subgroup_of_codomain``).
    """

    def __init__(self, parent, realization, *, injectivity_decision=None, subgroup_of_codomain=False) -> None:
        self._injectivity_premise = injectivity_decision
        self._subgroup_premise = subgroup_of_codomain
        self._gap_homomorphism = None
        self._generator_images = None
        match realization:
            case GapElement():
                # Endpoint agreement is part of the datum of every Mor,
                # independently of optional homomorphism-law checking.
                # Without this, a GAP map between different groups could
                # be installed in Mor(G,H) when check=False (the default).
                if (
                    realization.Source() != _gap_model(parent.domain())
                    or realization.Range() != _gap_model(parent.codomain())
                ):
                    raise ValueError(
                        f"the supplied GAP group map does not have the selected endpoints "
                        f"{parent.domain()} and {parent.codomain()}"
                    )
                # check=False suppresses optional mathematical validation,
                # not the requirement that a supplied GAP realization be a
                # map on the *whole* source satisfying its group law.
                generators, images = realization.MappingGeneratorsImages()
                if libgap.Subgroup(realization.Source(), generators) != realization.Source():
                    raise ValueError("the supplied GAP map's generators do not generate its source")
                checked = libgap.GroupHomomorphismByImages(
                    realization.Source(), realization.Range(), generators, images
                )
                if checked.is_bool():
                    raise ValueError("the supplied GAP map does not satisfy the source relations")
                # The checked map, not the unchecked supplied realization,
                # is the mathematical arrow represented by these images.
                self._gap_homomorphism = checked
                evaluator = self._evaluate_gap
            case dict():
                self._generator_images = realization
                evaluator = self._evaluate_generator_word
            case _ if callable(realization):
                evaluator = realization
            case _:
                raise TypeError(
                    f"a group morphism {parent.domain()} -> {parent.codomain()} needs generator images, an "
                    f"elementwise map or a GAP homomorphism, but got {realization!r}"
                )
        super().__init__(
            parent,
            evaluator,
            injectivity_decision=injectivity_decision,
            submonoid_of_codomain=subgroup_of_codomain,
        )

    def __call__(self, element, *args, **kwargs):
        r"""Evaluate this group map on an admitted point of its source.

        The fixed source supplies membership, and the homomorphism datum
        supplies membership of the image. Subgroup and submonoid facades
        retain their ambient representatives: evaluation normalizes those
        representatives without asking their defining predicate again.
        Other endpoints keep their ordinary element-constructor ingress.
        """
        normalize = _GroupMorRealizationMixin._normalize_admitted_element
        point = normalize(self.domain(), element)
        return normalize(self.codomain(), self._owned_function(point, *args, **kwargs))

    def _pointwise_mor(self):
        r"""The full group Mor containing this arrow's pointwise arithmetic.

        An abelian target is necessary for the uniform homomorphism law.
        A restriction such as automorphisms keeps its composition, while
        addition and negation land in the canonical full Mor.
        """
        from dzack_research.preamble.categories.group.additive_mors import AdditiveMorGroups

        if self.codomain() not in OwnedGroups().Commutative():
            raise TypeError(f"pointwise abelian arithmetic is not defined for maps into {self.codomain()}")
        parent = self.parent()
        if parent in AdditiveMorGroups():
            return parent
        return OwnedGroups().Mor(self.domain(), self.codomain())

    def __add__(self, other):
        from dzack_research.preamble.categories.group.additive_mors import AdditiveMorGroups

        return AdditiveMorGroups.ElementMethods._add_(self, other)

    _add_ = __add__

    def __neg__(self):
        from dzack_research.preamble.categories.group.additive_mors import AdditiveMorGroups

        return AdditiveMorGroups.ElementMethods.__neg__(self)

    _neg_ = __neg__

    def __sub__(self, other):
        from dzack_research.preamble.categories.group.additive_mors import AdditiveMorGroups

        return AdditiveMorGroups.ElementMethods.__sub__(self, other)

    def __rmul__(self, scalar):
        from dzack_research.preamble.categories.group.additive_mors import AdditiveMorGroups

        return AdditiveMorGroups.ElementMethods.__rmul__(self, scalar)

    @cached_method
    def _engine_generator_epimorphism(self):
        r"""GAP's ``F(S) ->> G`` onto the generators whose images define this morphism."""
        return _engine_generator_epimorphism(self.domain(), tuple(self._generator_images))

    def _product_of_generator_images(self, word):
        r"""``phi(w)`` for a GAP word ``w`` in the chosen generators, multiplied in the codomain."""
        images = tuple(self._generator_images.values())
        return reduce(
            mul,
            (
                images[position] if sign > 0 else ~images[position]
                for position, sign in _engine_word_letters(self.domain(), word)
            ),
            self.codomain().one(),
        )

    def _evaluate_generator_word(self, element):
        r"""``rho(g) = phi(w)`` for a word ``w`` in the chosen generators with ``pi(w) = g``.

        The universal property of the presentation ``pi: F(S) ->> G``: the
        generator images define ``phi: F(S) -> H``, and ``rho`` is the
        morphism with ``rho . pi = phi``.  The word is computed in the
        domain's engine; the images are multiplied in the codomain.
        """
        word = self._engine_generator_epimorphism().PreImagesRepresentative(
            _element_to_engine(self.domain(), element)
        )
        return self._product_of_generator_images(word)

    @validator
    def validate_homomorphism(self) -> None:
        r"""Raise ``ValueError`` unless ``f(xy) = f(x) f(y)`` (``OWN-22``).

        Generator images define a homomorphism exactly when every relator of
        the presentation by those generators maps to the identity.  A GAP
        realization is a map between the engine models of the two
        endpoints, and its generator images must satisfy the relations of
        the source.  An elementwise rule on a finite source is decided on
        all pairs of elements.
        """
        domain = self.domain()
        codomain = self.codomain()
        match self._generator_images, self._gap_homomorphism:
            case dict(), _:
                if domain in GroupsWithChosenFinitePresentation():
                    # The selected finite presentation already gives the
                    # complete relation family for the generator map.
                    # Use its actual free-source Mor rather than asking GAP
                    # to rediscover relations in an unrelated generating
                    # presentation of the same group.
                    source = domain.presenting_free_group()
                    labels = source.free_basis()
                    projection = domain.quotient_projection()
                    projected = tuple(projection(source.free_generator(label)) for label in labels)
                    # Checking the relators of F only certifies the map on
                    # the images of F's generators. If the Mor's selected
                    # generating family contains additional elements, their
                    # independently supplied images are not constrained by
                    # that check. Use the engine presentation in that case.
                    if (
                        all(generator in self._generator_images for generator in projected)
                        and all(generator in projected for generator in self._generator_images)
                    ):
                        free_map = source.Mor(codomain)(
                            Sets().Mor(labels, codomain)(
                                lambda label: self._generator_images[projection(source.free_generator(label))]
                            )
                        )
                        if any(free_map(relation) != codomain.one() for relation in domain.defining_relations()):
                            raise ValueError(
                                f"the given images do not define a homomorphism {domain} -> {codomain}: "
                                "they do not satisfy the chosen presentation relations"
                            )
                        return
                relators = _engine_generator_relators(domain, self._engine_generator_epimorphism())
                if not all(
                    self._product_of_generator_images(relator) == codomain.one()
                    for relator in relators
                ):
                    raise ValueError(
                        f"the given images do not define a homomorphism {domain} -> {codomain}: they do not "
                        f"satisfy the relations of {domain}"
                    )
            case None, None:
                assert domain.is_finite() is True, (
                    f"whether {self} preserves multiplication is decided here on all pairs of elements, so "
                    f"{domain} must be finite, and it is not known to be"
                )
                if not all(
                    self(left * right) == self(left) * self(right)
                    for left in domain
                    for right in domain
                ):
                    raise ValueError(
                        f"the function does not define a homomorphism {domain} -> {codomain}: it does not "
                        f"preserve multiplication"
                    )
            case None, engine:
                if engine.Source() != _gap_model(domain):
                    raise ValueError(
                        f"the GAP homomorphism is not a homomorphism out of {domain}: its source differs from {domain}"
                    )
                if engine.Range() != _gap_model(codomain):
                    raise ValueError(
                        f"the GAP homomorphism is not a homomorphism into {codomain}: its range differs from {codomain}"
                    )
                generators, images = engine.MappingGeneratorsImages()
                if libgap.Subgroup(engine.Source(), generators) != engine.Source():
                    raise ValueError(
                        f"the supplied GAP morphism does not specify images for generators of all of {domain}"
                    )
                if libgap.GroupHomomorphismByImages(engine.Source(), engine.Range(), generators, images).is_bool():
                    raise ValueError(
                        f"the given images do not define a homomorphism {domain} -> {codomain}: they do not "
                        f"satisfy the relations of {domain}"
                    )

    def _gap_morphism_crossing(self):
        r"""Return the private GAP realization to the group computation owner.

        A morphism given by generator images computes it on the first
        request. An elementwise rule can supply those images when its
        source has a selected finite generating set. The endpoint engines
        are requested only for this GAP computation, never for evaluating
        or composing the underlying rule.
        """
        if self._gap_homomorphism is None:
            images = self._generator_images
            if images is None:
                source = self.domain()
                assert source.has_selected_group_resolution() and source.group_generating_set() in FiniteSets(), (
                    f"cannot compute with {self} through GAP: this elementwise group morphism "
                    "has no selected finite source generating set from which to compute generator images"
                )
                images = {generator: self(generator) for generator in source.group_generators()}
            codomain = self.codomain()
            self._gap_homomorphism = self.parent()._engine_homomorphism(
                [_element_to_engine(self.domain(), generator) for generator in images],
                [_element_to_engine(codomain, image) for image in images.values()],
            )
        return self._gap_homomorphism

    def _richcmp_(self, other, op):
        r"""Compare group maps on finite determining data in their common Mor.

        The set-arrow host selects the common Mor before reaching this
        supplier. A different, weaker Mor parent is not a proof that two
        maps differ. Without finite determining data, retain the inherited
        equality proposition instead of traversing an arbitrary free basis.
        """
        if op not in (op_EQ, op_NE):
            return NotImplemented
        if self is other:
            return op == op_EQ
        source = self.domain()
        match source:
            case _ if (
                source.has_selected_group_resolution()
                and source.group_generating_set() in FiniteSets()
            ):
                equal = conjunction(
                    self(generator) == other(generator)
                    for generator in source.group_generators()
                )
            case _:
                return super()._richcmp_(other, op)
        return equal if op == op_EQ else negation(equal)

    def _composition(self, right):
        r"""Compose group maps through their retained rules on elements.

        A free source uses its basis universal property. Otherwise the
        composite rule is retained in the ordinary group Mor, whose
        admitted-point contract preserves intermediate membership premises.
        In particular an automorphism followed by a group map need
        not be an automorphism. No generating resolution or GAP realization
        is needed to compose admitted maps. A weaker right factor composes
        in the inherited weaker Mor.
        """
        source = right.domain()
        if (
            source not in OwnedGroups()
            or right.parent() not in MorCategories()
            or not right.parent().mor_family().base_category().is_subcategory(OwnedGroups())
        ):
            return super()._composition(right)
        if right.parent() is self.parent() and self.parent() in AbelianGroupEndomorphismRings():
            return self.parent()._compose_endomorphisms(self, right)
        if source in GroupsWithChosenFreeBasis():
            return right.postcompose(self)
        if (
            source.has_selected_group_resolution()
            and source.group_generating_set() in FiniteSets()
            and (right._gap_homomorphism is not None or right._generator_images is not None)
        ):
            return source.Mor(self.codomain())(
                {generator: self(right(generator)) for generator in source.group_generators()}
            )
        return OwnedGroups().Mor(source, self.codomain())._from_elementwise_rule(
            lambda element: self(right(element))
        )

    def _evaluate_gap(self, element):
        model = _element_to_engine(self.domain(), element)
        if self.parent()._is_twisted():
            model = model.Inverse()
        return _element_from_engine(
            self.codomain(),
            self._gap_morphism_crossing().Image(model),
        )

    def lift(self, element):
        r"""Return one preimage of ``element``.

        The inclusion of a subgroup ``H`` sends ``h`` to ``h``, so the
        preimage of an element of ``H`` is that element.
        """
        if self._subgroup_premise:
            assert element in self.domain(), f"{element} is not in the image of {self}"
            return self.domain()(element)
        engine_element = _element_to_engine(self.codomain(), element)
        gap_morphism = self._gap_morphism_crossing()
        assert engine_element in gap_morphism.Image(), (
            f"{element} is not in the image of {self}"
        )
        preimage = gap_morphism.PreImagesRepresentative(engine_element)
        if self.parent()._is_twisted():
            preimage = preimage.Inverse()
        return _element_from_engine(self.domain(), preimage)

    def preimage_subgroup(
        self,
        subgroup,
        *,
        predicate=None,
        description=None,
        character_data=None,
        character_data_complete=None,
    ):
        r"""Return the inverse image of ``subgroup`` under this group morphism."""
        from dzack_research.preamble.categories.group.predicate_subgroups import (
            PreimageSubgroups,
        )

        return PreimageSubgroups(self.domain())(
            self,
            subgroup,
            predicate=predicate,
            description=description,
            character_data=character_data,
            character_data_complete=character_data_complete,
        )

    def kernel(self):
        from dzack_research.preamble.categories.group.predicate_subgroups import (
            KernelSubgroups,
        )

        return KernelSubgroups(self.domain())(self)

    def image(self):
        r"""``f(G)``; the image of the inclusion of a subgroup ``H`` is ``H``."""
        if self._subgroup_premise:
            return self.domain()
        return _subgroup_from_gap(
            self.codomain(),
            self._gap_morphism_crossing().Image(),
        )

    def _image_model(self):
        r"""The GAP model of ``f(G)`` inside the model of a finite codomain."""
        if not self._subgroup_premise:
            if self._gap_homomorphism is not None or self._generator_images is not None:
                return self._gap_morphism_crossing().Image()
            return _gap_model(self.image())
        from dzack_research.preamble.categories.group.predicate_subgroups import (
            KernelSubgroups,
        )

        subgroup = self.domain()
        match subgroup:
            case _ if subgroup in KernelSubgroups(self.codomain()):
                return subgroup.kernel_morphism()._gap_morphism_crossing().Kernel()
            case _:
                return _gap_model(subgroup)

    def is_normal(self):
        r"""Whether this is a normal monomorphism: injective, with image normal in the codomain.

        For the inclusion of ``H`` in ``G`` this is ``g H g^{-1} = H`` for
        every ``g`` in ``G``, decided for a finite ``G`` by GAP's
        ``IsNormal``.  ``G/H`` is a group, and ``H -> G -> G/H`` exact,
        exactly when this holds; otherwise :meth:`cokernel` is ``G`` modulo
        the normal closure of the image.
        """
        codomain = self.codomain()
        injective = self.is_injective()
        if injective is False:
            return False
        match codomain:
            case _ if codomain in OwnedAbelianGroups():
                return injective
            case _ if codomain in OwnedFiniteGroups():
                if injective is not True:
                    return AtomicProposition("is_normal", self)
                return bool(_gap_model(codomain).IsNormal(self._image_model()))
            case _:
                assert False, (
                    f"whether {self} is a normal monomorphism is defined for every group morphism, but the "
                    "current preamble decides it only into finite or abelian represented groups"
                )

    def factor_through_or_none(self, target_inclusion):
        r"""The factor ``m = n . k`` of this monomorphism ``m`` through ``n``, or None.

        ``k(a) = n^{-1}(m(a))`` exists exactly when ``m(A)`` lies in
        ``n(B)``; containment is decided on the chosen generators of a
        generated subgroup ``A``, or on the elements of a finite ``A``.
        """
        if target_inclusion.codomain() is not self.codomain():
            raise ValueError(f"{self} cannot factor through {target_inclusion}: their codomains {self.codomain()} and {target_inclusion.codomain()} differ")
        assert self.is_injective() is True and target_inclusion.is_injective() is True, (
            f"factoring {self} through {target_inclusion} is defined here for monomorphisms, and one of them is not known to be injective"
        )
        source = self.domain()
        target = target_inclusion.domain()
        if source is target and self is target_inclusion:
            return source.Mor(target).identity()
        match source:
            case _ if source in GeneratedSubgroups(self.codomain()):
                witnesses = source.selected_subgroup_generators()
            case _ if source in OwnedFiniteGroups():
                witnesses = source
            case _:
                assert False, (
                    f"cannot decide whether the image of {self} lies in the image of {target_inclusion}: {source} "
                    f"has no chosen generating set and is not known to be finite"
                )
        target_image = target_inclusion.image()
        if not all(self(element) in target_image for element in witnesses):
            return None
        return source.Mor(target)(lambda element: target_inclusion.lift(self(element)))

    def factor_through(self, target_inclusion):
        factor = self.factor_through_or_none(target_inclusion)
        if factor is None:
            raise ValueError(f"{self} does not factor through {target_inclusion}: its image is not contained in the image of {target_inclusion}")
        return factor

    @cached_method
    def coset_cokernel(self):
        r"""Return ``G'/f(G)`` as the pointed transitive left ``G'``-set of image cosets."""
        return self.codomain().left_cosets(self.image())

    def coset_cokernel_projection(self):
        r"""Return the equivariant projection ``G' -> G'/f(G)`` of left ``G'``-sets."""
        return self.coset_cokernel().projection()

    @cached_method
    def _cokernel_data(self):
        r"""Return the quotient of the codomain by the normal closure of the image.

        A finite codomain is quotiented by GAP, which realizes the quotient
        as a finite group with its own engine.  An abelian codomain not
        known to be finite is quotiented through membership in a subgroup
        whose inclusion this is, since every subgroup of it is normal.
        """
        codomain = self.codomain()
        match codomain:
            case _ if codomain in OwnedFiniteGroups():
                normal_closure = libgap.NormalClosure(
                    _gap_model(codomain),
                    self._image_model(),
                )
                return _finite_group_quotient_by_gap_normal_subgroup(
                    codomain,
                    normal_closure,
                )
            case _ if codomain in OwnedAbelianGroups() and self._subgroup_premise:
                quotient = _abelian_subgroup_quotient(self.domain())
                return quotient, quotient.quotient_projection()
            case _:
                assert False, (
                    f"the cokernel of {self} exists, but it is computed here only into a finite group, or "
                    f"for the inclusion of a subgroup of an abelian group"
                )

    def cokernel(self):
        return self._cokernel_data()[0]

    def cokernel_projection(self):
        return self._cokernel_data()[1]

    def is_injective(self):
        if self._injectivity_premise is not None:
            return self._injectivity_premise
        if self._gap_homomorphism is not None or self._generator_images is not None:
            return bool(self._gap_morphism_crossing().IsInjective())
        return Sets().Mor(self.domain(), self.codomain())(self.__call__).is_injective()

    def is_surjective(self):
        if self._subgroup_premise and self.domain() is self.codomain():
            return True
        if self._gap_homomorphism is not None or self._generator_images is not None:
            return bool(self._gap_morphism_crossing().IsSurjective())
        return Sets().Mor(self.domain(), self.codomain())(self.__call__).is_surjective()

    def inverse(self):
        r"""The inverse of a decided bijective group morphism, in the group Mor.

        A bijective homomorphism has a homomorphic inverse: applying the
        forward map to ``f^-1(x) f^-1(y)`` gives ``xy``. The selected group
        realization supplies lifts; for an elementwise map the set owner
        supplies its finite inverse algorithm and its named frontier.
        """
        assert self.is_injective() is True and self.is_surjective() is True, (
            f"the inverse of {self} is defined as a group morphism when it is bijective, "
            "but injectivity and surjectivity have not both been decided"
        )
        if self.domain() is self.codomain() and self is self.parent().identity():
            return self
        if (
            self._subgroup_premise
            or self._gap_homomorphism is not None
            or self._generator_images is not None
        ):
            rule = self.lift
        else:
            rule = Sets().Mor(self.domain(), self.codomain())(self.__call__).inverse()
        return OwnedGroups().Mor(self.codomain(), self.domain())._from_elementwise_rule(rule)

    def as_isomorphism(self):
        r"""Retain this inverse pair as an arrow of ``core(Grp)``."""
        return OwnedGroups().Core().Mor(self.domain(), self.codomain())._from_known_inverse_pair(
            self, self.inverse()
        )


class IndexedFreeGroupMorphism(GroupMorphism):
    r"""A morphism out of the free group on a chosen set.

    The universal property of the free group ``F(S)`` makes a group morphism
    ``F(S) -> H`` the same datum as a set map ``S -> H``, which is what this
    morphism stores; it is evaluated on reduced words.  The free group on an
    arbitrary set has no elementwise GAP model, so no GAP morphism is used.
    """

    def __init__(self, parent, generator_morphism, **premises) -> None:
        self._generator_morphism = generator_morphism
        super().__init__(parent, self._evaluate_reduced_word, **premises)

    def generator_morphism(self):
        return self._generator_morphism

    def _admitted_generator_image(self, index):
        r"""Evaluate the retained basis map with its supplied range premise.

        The free-group extension already receives a map from its basis into
        the target group. At this protected realization boundary, the owned
        set map's retained evaluator supplies that map's values without a
        second predicate-target admission. A supplied native set map keeps
        its own evaluator. The common group-arrow normalization then keeps
        the target's actual ambient representation.
        """
        index = self.domain().free_basis()(index)
        morphism = self.generator_morphism()
        image = morphism._owned_function(index) if isinstance(morphism, OwnedSetMorphism) else morphism(index)
        return _GroupMorRealizationMixin._normalize_admitted_element(self.codomain(), image)

    @validator
    def validate_homomorphism(self) -> None:
        r"""The free extension preserves multiplication by reduction of words.

        Its defining datum is a set map from the selected basis to a
        group. Cancelling adjacent inverse letters does not change its
        value, so the product-of-images rule is a homomorphism for every
        basis, including an infinite one. There are no relators to decide.
        """
        return None

    def image(self):
        r"""Image subgroup generated by the images of the selected free basis.

        This uses the free-group universal map, not a GAP model of its
        potentially infinite source.

        EXAMPLES::

            sage: F, C = Groups.Free(1), Groups.C(4)
            sage: label = next(iter(F.free_basis()))
            sage: t = C.group_generators()[0]
            sage: f = F.Mor(C)({label: t*t})
            sage: f.image().cardinality() == 2
            True
            sage: f(F.group_generators()[0]) in f.image()
            True
        """
        if self._subgroup_premise:
            return self.domain()
        basis = self.domain().free_basis()
        assert basis in FiniteSets(), (
            f"the image of {self} is a subgroup of {self.codomain()}, but this construction "
            "lists its generators only when the selected free basis is finite"
        )
        return self.codomain().subgroup(tuple(self._admitted_generator_image(label) for label in basis))

    def _evaluate_reduced_word(self, element):
        codomain = self.codomain()
        return reduce(
            mul,
            (
                self._admitted_generator_image(index) ** sign
                for index, sign in _reduced_word_data(self.domain(), element)
            ),
            codomain.one(),
        )

    def postcompose(self, morphism):
        assert morphism.domain() is self.codomain(), (
            f"cannot compose {morphism} after {self}: the codomain {self.codomain()} is not the domain {morphism.domain()}"
        )
        indices = self.domain().free_basis()
        return self.domain().Mor(morphism.codomain())(
            Sets().Mor(indices, morphism.codomain())(
                lambda index: morphism(self._admitted_generator_image(index))
            )
        )


class _GroupMorRealizationMixin:
    @staticmethod
    def _normalize_admitted_element(endpoint, element):
        r"""Normalize a group-arrow point through its declared facade ambient.

        Protected evaluation contract (OWN-05), shared by GroupMorphism
        and the defining subgroup inclusion. The point is already admitted
        in the source, or its membership is supplied by the defining map's
        range law. This is not a constructor for new subgroup members.
        A point already parented by the current endpoint is retained before
        following any ambient datum: a subgroup may own its elements.
        The existing submonoid realization explicitly retains its ambient
        monoid; Subgroups retains its ambient group. Follow these actual
        facade data, including nested facades, then use ordinary ingress in
        the representing ambient parent. No predicate truth is inferred.
        """
        from dzack_research.preamble.categories.group.submonoids import _SubmonoidEngine

        while True:
            if element_parent(element) is endpoint:
                return element
            if isinstance(endpoint, _SubmonoidEngine):
                endpoint = endpoint.ambient_monoid()
                continue
            if endpoint in OwnedGroups():
                ambient = endpoint.supergroup()
                if ambient is not endpoint and endpoint in Subgroups(ambient):
                    endpoint = ambient
                    continue
            return endpoint(element)

    def _from_elementwise_rule(self, function):
        r"""Retain an admitted group map by its rule on elements (``OWN-22``).

        The multiplication-preserving law is construction data, not a
        request for a GAP model or a generating resolution. A free-source
        realization reads this same rule on its selected free generators.
        """
        return self.element_class(self, function)

    def elementwise(self, function):
        r"""Retain an admitted homomorphism on elements in this exact Mor.

        This is the shared pointwise-arithmetic constructor contract. A
        free source still uses its existing basis realization through
        ``_from_elementwise_rule``; no second group-map engine is created.
        """
        if not callable(function):
            raise TypeError(f"a morphism in {self} needs a function on elements")
        return self._from_elementwise_rule(function)

    def _apply_pointwise_scalar(self, scalar, element):
        r"""The integer action on the multiplicatively written abelian target.

        Only the additive Mor enrichment calls this selected action.
        Exact owned-integer ingress precedes the native exponent spelling.
        """
        return element ** int(self.base_ring()(scalar))

    def _scalar_identity(self, scalar):
        from dzack_research.preamble.categories.group.additive_mors import _ScalarIdentityEvaluation

        if self.domain() is not self.codomain():
            raise ValueError(f"a scalar multiple of the identity needs equal endpoints, but got {self}")
        scalar = self.base_ring()(scalar)
        if (scalar == self.base_ring().one()) is True:
            return self._from_subgroup_inclusion()
        return self.elementwise(_ScalarIdentityEvaluation(self, scalar))

    def _compose_endomorphisms(self, left, right):
        return self._pointwise_endomorphism_composite(left, right)

    def _owned_scalar_multiple(self, scalar, morphism):
        return self._pointwise_scalar_multiple(scalar, morphism)

    @cached_method
    def identity(self):
        r"""The identity as an arrow of this generated group-Mor type."""
        if self.domain() is not self.codomain():
            raise ValueError(
                f"there is no identity homomorphism {self.domain()} -> {self.codomain()}: "
                "the endpoints differ"
            )
        return self._from_subgroup_inclusion()

    @cached_method
    def _is_twisted(self) -> bool:
        r"""Whether exactly one endpoint reverses multiplication in its engine.

        An owned map ``Phi`` is then represented by the engine homomorphism
        ``phi(x) = Phi(x^-1)``. This computation asks the endpoint engines
        only when a GAP morphism is constructed or evaluated.
        """
        return _law_reversed(self.domain()) != _law_reversed(self.codomain())

    def _engine_homomorphism(self, generator_models, image_models):
        r"""GAP's checked homomorphism on a generating family of the source."""
        source = _gap_model(self.domain())
        target = _gap_model(self.codomain())
        if len(generator_models) != len(image_models):
            raise ValueError("the engine group morphism requires one image per generator")
        if libgap.Subgroup(source, libgap(generator_models)) != source:
            raise ValueError("the engine morphism generators do not generate its source group")
        if self._is_twisted():
            image_models = [model.Inverse() for model in image_models]
        checked = libgap.GroupHomomorphismByImages(source, target, generator_models, image_models)
        if checked.is_bool():
            raise ValueError("the engine morphism images do not satisfy the source relations")
        return checked

    def _from_realization_engine(self, engine, *args, **kwargs):
        r"""Insert one private realization behind the generated group-arrow type.

        Protected construction contract under OWN-05. A specialized group
        map construction supplies its engine and fixed-endpoint data.
        In particular UnitGroupFunctor supplies _UnitGroupMorphism and an
        admitted monoid arrow f: M -> N, with this Mor's literal endpoints
        M.unit_group() and N.unit_group(). Its evaluator returns f(u) on an
        admitted source unit; the monoid-map laws establish membership in
        the target unit group without a second predicate admission. The
        declared group-arrow input supplies source-unit membership too;
        evaluation uses f's ordinary ambient ingress without reconstructing
        either unit-group predicate facade. This retains the intermediate
        unit premise when two induced maps are applied successively.
        The generated GroupMor arrow and its actual endpoints are retained.
        """
        realized_type = _implementation_with_engine(
            self.element_class,
            GroupMorphism,
            engine,
        )
        return realized_type(self, *args, **kwargs)

    @cached_method
    def _from_subgroup_inclusion(self):
        r"""The inclusion ``H -> G`` of the domain, a subgroup of the codomain, sending ``h`` to ``h``.

        The construction gives the arrow's injectivity and its image ``H``
        as premises; neither is checked.
        """
        codomain = self.codomain()
        return self.element_class(
            self,
            lambda element: self._normalize_admitted_element(codomain, element),
            injectivity_decision=True,
            subgroup_of_codomain=True,
        )

    def _from_realization_rule(self, rule):
        r"""Realize a specialized group arrow through this canonical Mor parent."""
        morphism = rule(self)
        assert morphism.parent() is self, (
            f"the rule produced {morphism}, which is not a homomorphism in {self}; it lies in {morphism.parent()}"
        )
        return morphism


class IndexedFreeGroupMor(_GroupMorRealizationMixin, CategoricalMor):
    """The canonical Mor object out of the free group on a chosen set."""

    ElementMethods = IndexedFreeGroupMorphism

    def __init__(self, mor_family, domain, codomain) -> None:
        self._preamble_base_ring = _own_ring(ZZ)
        CategoricalMor.__init__(
            self,
            mor_family,
            domain,
            codomain,
            category=_group_mor_placement(domain, codomain),
        )
        realize_owned_category(self)

    def _element_constructor_(self, images, **_options):
        r"""The morphism ``F(S) -> H`` determined by the images of the basis ``S``.

        The images are a set morphism ``S -> H``, a function on ``S``, or, for
        a finite ``S``, a dictionary naming every basis point.
        """
        indices = self.domain().free_basis()
        set_mor = Sets().Mor(indices, self.codomain())
        match images:
            case SetMorphism():
                assert images.domain() is indices and images.codomain() is self.codomain(), (
                    f"{images} cannot define a homomorphism {self.domain()} -> {self.codomain()}: a homomorphism out of a "
                    f"free group is a map from the free basis {indices} to {self.codomain()}, but {images} is a map "
                    f"{images.domain()} -> {images.codomain()}"
                )
                generator_morphism = images
            case dict():
                assert indices in FiniteSets(), (
                    f"a dictionary cannot define a homomorphism out of {self.domain()}: its free basis {indices} is not "
                    f"known to be finite; give a map from {indices} to {self.codomain()} instead"
                )
                assert all(index in images for index in indices), (
                    f"the dictionary does not define a homomorphism out of {self.domain()}: it must give an image for every "
                    f"element of the free basis {indices}, but it has keys {tuple(images)}"
                )
                generator_morphism = set_mor(images.__getitem__)
            case _ if callable(images):
                generator_morphism = set_mor(images)
            case _ if self in AbelianGroupEndomorphismRings():
                return self._scalar_identity(images)
            case _:
                raise TypeError(f"{images!r} cannot define a homomorphism {self.domain()} -> {self.codomain()}: give the images of the free basis {indices} as a map, a function, or a dictionary")
        return self.element_class(self, generator_morphism)

    def _from_elementwise_rule(self, function):
        r"""Restrict an admitted elementwise rule to the selected free basis."""
        domain = self.domain()
        return self(
            Sets().Mor(domain.free_basis(), self.codomain())(
                lambda index: function(domain.free_generator(index))
            )
        )

    @cached_method
    def _from_subgroup_inclusion(self):
        r"""The inclusion ``F(S) -> G`` of a free subgroup, given by the images ``s -> s`` of its free basis."""
        domain = self.domain()
        codomain = self.codomain()
        return self.element_class(
            self,
            Sets().Mor(domain.free_basis(), codomain)(
                lambda index: self._normalize_admitted_element(codomain, domain.free_generator(index))
            ),
            injectivity_decision=True,
            subgroup_of_codomain=True,
        )

    def _cardinality_decision(self):
        r"""A homomorphism from F(S) is exactly a function S -> H."""
        return cardinal(self.codomain().cardinality()) ** cardinal(self.domain().free_basis().cardinality())

    def _repr_(self):
        return f"Mor({self.domain()}, {self.codomain()})"


class GroupMor(_GroupMorRealizationMixin, CategoricalMor):
    """The canonical owned ``Mor(G,H)``."""

    ElementMethods = GroupMorphism

    @staticmethod
    def __classcall__(cls, family, domain, codomain):
        return typecall(cls, family, domain, codomain)

    def __init__(self, mor_family, domain, codomain, *, category=None, pointwise=True):
        self._preamble_base_ring = _own_ring(ZZ)
        CategoricalMor.__init__(
            self,
            mor_family,
            domain,
            codomain,
            category=_group_mor_placement(
                domain, codomain, *(() if category is None else (category,)),
                pointwise=pointwise,
            ),
        )

    def _element_constructor_(self, images, *, check=False, **_options):
        match images:
            case dict():
                morphism = self._from_group_generator_images(images)
                # Generator-image data need to kill all defining relations
                # before they describe any morphism G -> H. Unlike a
                # pointwise callable, an invalid generator assignment is
                # not even a map on the presented quotient. Enforce this
                # regardless of the optional check flag.
                morphism.validate_homomorphism(check=True)
            case GapElement():
                morphism = self.element_class(self, images)
            case Morphism() if images.parent() is self:
                return images
            case tuple() | list():
                morphism = self._from_gap_generator_images(images)
            case _ if callable(images):
                morphism = self._from_elementwise_rule(images)
            case _ if self in AbelianGroupEndomorphismRings():
                morphism = self._scalar_identity(images)
            case _:
                raise TypeError(f"unable to convert {images!r} to an element of {self}")
        morphism.validate_homomorphism(check=check)
        return morphism

    def _from_engine_generator_images(self, generator_models, image_models):
        # This ingress is also used by product/coproduct constructions,
        # bypassing _from_gap_generator_images. A truncated image family
        # must never be passed to GroupHomomorphismByImagesNC.
        if len(generator_models) != len(image_models):
            raise ValueError(
                f"the engine morphism from {self.domain()} has {len(generator_models)} "
                f"selected generators but {len(image_models)} images"
            )
        return self.element_class(self, self._engine_homomorphism(generator_models, image_models))

    def _from_group_generator_images(self, images):
        r"""The morphism out of a presented group given by the images of its chosen generators.

        The images are the defining datum; construction stores them in the
        order of the chosen generators and computes nothing in the codomain.
        """
        domain = self.domain()
        codomain = self.codomain()
        if not domain.has_selected_group_resolution():
            raise TypeError(
                f"a homomorphism out of {domain} cannot be given by images of generators: {domain} has no chosen generating set"
            )
        generators = domain.group_generators()
        if not (all(generator in images for generator in generators) and all(key in generators for key in images)):
            raise ValueError(f"the dictionary does not define a homomorphism out of {domain}: its keys must be exactly the chosen generators {generators} of {domain}, but they are {tuple(images)}")
        return self.element_class(
            self,
            {generator: codomain(images[generator]) for generator in generators},
        )

    def _from_gap_generator_images(self, images):
        r"""Images listed in the order of the GAP model's own generators."""
        codomain = self.codomain()
        generators = list(_gap_model(self.domain()).GeneratorsOfGroup())
        if len(images) != len(generators):
            raise ValueError(
                f"the engine presentation of {self.domain()} has {len(generators)} generators, "
                f"but {len(images)} images were supplied"
            )
        return self._from_engine_generator_images(
            generators,
            [_element_to_engine(codomain, codomain(image)) for image in images],
        )

    @cached_method
    def _cardinality_decision(self):
        r"""Return the cardinality of the represented homomorphism object."""
        domain = self.domain()
        codomain = self.codomain()
        match (domain, codomain):
            case (source, target) if source in OwnedFiniteGroups() and target in OwnedFiniteGroups():
                homomorphisms = libgap.AllHomomorphisms(
                    _gap_model(source),
                    _gap_model(target),
                )
                return cardinal(int(homomorphisms.Length()))
            case _:
                return None

    def _repr_(self):
        return f"Mor({self.domain()}, {self.codomain()})"


class GroupAutomorphismMethods:
    def inverse(self):
        r"""Invert inside this represented automorphism group."""
        return self.parent()(
            self._gap_morphism_crossing().InverseGeneralMapping(),
            check=False,
        )

    @validator
    def validate_bijectivity(self) -> None:
        r"""Raise ``ValueError`` unless this endomorphism is bijective (``OWN-22``)."""
        if not bool(self._gap_morphism_crossing().IsBijective()):
            raise ValueError(f"{self} does not define an element of {self.parent()}: the homomorphism is not bijective")

    def _composition(self, right):
        r"""Compose automorphisms inside their represented automorphism group."""
        if right.parent() is self.parent():
            return self.parent()(
                right._gap_morphism_crossing() * self._gap_morphism_crossing(),
                check=False,
            )
        return super()._composition(right)


class GroupAutomorphism(GroupAutomorphismMethods, GroupMorphism):
    r"""Compatibility shell for GAP-backed group automorphisms."""


class GroupAutomorphismGroups(OwnedCategory):
    r"""Canonical automorphism groups ``Aut(G)`` computed by GAP.

    The datum is the group ``G`` whose automorphisms are the elements. A
    proper subgroup is instead an object of ``Subgroups(Aut(G))``, so it
    retains its inclusion without becoming another fixed ``Iso(G,G)``.
    """

    def an_object(self):
        r"""The automorphism group of the cyclic group of order two."""
        return Groups.C(2).Aut()

    def super_categories(self):
        return [OwnedGroups()]

    class ParentMethods:
        @cached_method
        def _libgap_(self):
            return _automorphism_gap_model(self.domain())

        @cached_method
        def _engine_group(self):
            r"""Return the private Sage wrapper of GAP's automorphism group."""
            return GroupLibGAP(self._libgap_())

        def _to_engine(self, automorphism):
            r"""Lower an owned automorphism through the group-engine contract."""
            if not self.accepts(automorphism):
                raise ValueError("the engine crossing requires an automorphism of this group")
            return self._engine_group()(automorphism._gap_morphism_crossing())

        def _from_engine(self, engine_automorphism):
            r"""Raise one private engine element as an ambient automorphism."""
            return self(engine_automorphism.gap(), check=False)

        def _engine_subgroup_from_generators(self, generators):
            return _engine_generated_subgroup(
                self._engine_group(),
                [self._to_engine(generator) for generator in generators],
            )

        def _to_subgroup_engine(self, automorphism, engine_subgroup):
            return engine_subgroup(self._to_engine(automorphism))

        def _engine_subgroup_contains(self, automorphism, engine_subgroup):
            return self._to_engine(automorphism) in engine_subgroup

        def _from_subgroup_engine(self, engine_automorphism):
            return self(engine_automorphism.gap(), check=False)

        def one(self):
            return self(libgap.IdentityMapping(_gap_model(self.domain())), check=False)

        def __iter__(self):
            r"""Enumerate automorphisms when the underlying group is finite."""
            assert self.domain().is_finite() is True, (
                f"the elements of Aut({self.domain()}) are listed here only when {self.domain()} is finite, "
                f"and {self.domain()} is not known to be finite"
            )
            return (
                self(backend, check=False)
                for backend in self._libgap_().Elements()
            )

        def supergroup(self):
            return self

        def _cardinality_decision(self):
            r"""``|Aut(G)|``: from GAP for finite ``G``, from the rank for a free ``G``.

            ``Aut(F_0)`` is trivial, ``Aut(F_1) = C_2``, and ``Aut(F_n)`` for
            ``2 <= n < infinity`` is countably infinite; the rank of a free
            group is the cardinality of its chosen basis.
            """
            domain = self.domain()
            if domain in OwnedFiniteGroups():
                return cardinal(_finite_order(self))
            if domain in GroupsWithChosenFreeBasis() and domain.free_basis().cardinality().is_finite():
                match int(domain.free_basis().cardinality().finite_value()):
                    case 0:
                        return cardinal(1)
                    case 1:
                        return cardinal(2)
                    case _:
                        return aleph(0)
            return super()._cardinality_decision()

        def _repr_(self):
            return f"Aut({self.domain()})"

    class ElementMethods:
        def _composition_(self, right, mor):
            assert right.parent() is self.parent(), f"cannot compose {self} with {right}: they are automorphisms of different groups, in {self.parent()} and {right.parent()}"
            return self.parent()(
                right._gap_morphism_crossing() * self._gap_morphism_crossing(),
                check=False,
            )


class GroupAutomorphismGroup(GroupMor):
    ElementMethods = GroupAutomorphismMethods

    @staticmethod
    def __classcall__(cls, mor_family, group):
        return typecall(cls, mor_family, group)

    def __init__(self, mor_family, group):
        categories = [GroupAutomorphismGroups()]
        if group.is_finite() is True:
            categories.append(OwnedFiniteGroups())
        GroupMor.__init__(
            self,
            mor_family,
            group,
            group,
            category=Cat().meet(tuple(categories)),
            pointwise=False,
        )
        if group.is_finite() is True:
            backend_generators = tuple(self._libgap_().GeneratorsOfGroup())
            generators = finite_ordered_set(
                tuple(self(generator, check=False) for generator in backend_generators)
            )
            source = Groups.Free(index_set=generators)
            generator_morphism = Sets().Mor(generators, self)(lambda generator: generator)
            _fix_selected_group_resolution_data(
                self, source, generators, generator_morphism
            )

    def super_categories(self):
        packet = self.base_category().category_packet()
        group = self.domain()
        supers = [
            packet.Mors().Of(group, group),
            packet.Monos().Of(group, group),
            packet.Epis().Of(group, group),
        ]
        supers.extend(superpacket.Isos().Of(group, group) for superpacket in packet.super_packets() if group in superpacket.C())
        if self.aut_family() is not None:
            supers.append(packet.Ends().Of(group))
            supers.extend(superpacket.Auts().Of(group) for superpacket in packet.super_packets() if group in superpacket.C())
        return _distinct_supercategories(supers)

    def identity(self):
        return self(libgap.IdentityMapping(_gap_model(self.domain())), check=False)

    one = identity
    identity_automorphism = identity

    def _element_constructor_(self, images, *, check=False, **options):
        automorphism = super()._element_constructor_(images, check=check, **options)
        automorphism.validate_bijectivity(check=check)
        return automorphism

class GeneralGroupMor(_GroupMorRealizationMixin, CategoricalMor):
    r"""The owned group Mor for endpoints without a selected GAP realization.

    Specialized constructions (for example profinite restriction maps and
    characters) parent their arrows here directly. An admitted elementwise
    homomorphism also supplies all data needed for a group arrow; evaluating
    or composing that rule does not require a GAP realization.
    """

    ElementMethods = GroupMorphism

    def __init__(self, mor_family, domain, codomain) -> None:
        self._preamble_base_ring = _own_ring(ZZ)
        CategoricalMor.__init__(
            self, mor_family, domain, codomain, category=_group_mor_placement(domain, codomain)
        )

    def _element_constructor_(self, datum):
        match datum:
            case Morphism() if datum.parent() is self:
                return datum
            case _ if callable(datum):
                return self._from_elementwise_rule(datum)
            case _ if self in AbelianGroupEndomorphismRings():
                return self._scalar_identity(datum)
            case _:
                raise TypeError(
                    f"a group morphism {self.domain()} -> {self.codomain()} needs an admitted "
                    f"elementwise homomorphism or a specialized realization, but got {datum!r}"
                )


class GroupMorCategoryConstruction(MorCategoryConstruction):
    r"""The represented Mor categories of owned groups."""

    def Of(self, domain, codomain=None):
        if codomain is None:
            codomain = domain
        if domain not in self.base_category() or codomain not in self.base_category():
            raise TypeError(f"the homomorphisms {domain} -> {codomain} cannot be formed: both must be groups of {self.base_category()}")
        cached = self._cached_between(domain, codomain)
        if cached is not None:
            return cached
        from dzack_research.preamble.categories.group.profinite.profinite_groups import (
            ProfiniteGroups,
        )

        match domain:
            case _ if domain in GroupsWithChosenFreeBasis():
                result = IndexedFreeGroupMor(self, domain, codomain)
            case _ if domain in ProfiniteGroups():
                result = GeneralGroupMor(self, domain, codomain)
            case _:
                result = GroupMor(self, domain, codomain)
        return self._remember_between(domain, codomain, result)


class GroupEndCategoryConstruction(EndCategoryConstruction):
    r"""Endomorphism monoids of groups, on the same underlying set as ``Mor(G,G)``."""

    def Of(self, obj, codomain=None):
        if codomain is not None and codomain is not obj:
            raise ValueError(f"End({obj}) cannot have codomain {codomain}: an endomorphism has equal domain and codomain")
        if obj not in self.base_category():
            raise TypeError(f"End({obj}) cannot be formed here: {obj} is not a group of {self.base_category()}")
        cached = self._cached_between(obj, obj)
        if cached is not None:
            return cached
        endomorphisms = self.base_category().Mor(obj, obj)
        endomorphisms.attach_end_family(self)
        return self._remember_between(obj, obj, endomorphisms)


class GroupIsoCategoryConstruction(IsoCategoryConstruction):
    r"""Group isomorphisms, using the maintained automorphism group on the diagonal."""

    def Of(self, domain, codomain=None):
        if codomain is None:
            codomain = domain
        if domain is not codomain:
            return super().Of(domain, codomain)

        # A free group on a set has no GAP elementwise model, so its
        # automorphism group has no stronger computational parent than the
        # generic Iso object.
        if domain in GroupsWithChosenFreeBasis():
            return super().Of(domain, codomain)

        cached = self._cached_between(domain, domain)
        if cached is not None:
            return cached
        result = GroupAutomorphismGroup(self, domain)
        return self._remember_between(domain, domain, result)


# --------------------------------------------------------------------------
# The owned categories.
# --------------------------------------------------------------------------


class OwnedGroups(CategoryPacketMethods, OwnedCategory):
    """Groups whose notebook-facing group interface is owned by the preamble."""

    from sage.groups.abelian_gps.abelian_group import AbelianGroup as _SageAbelianGroup
    from sage.groups.misc_gps.misc_groups_catalog import (
        Artin as _SageArtin,
    )
    from sage.groups.misc_gps.misc_groups_catalog import (
        Braid as _SageBraid,
    )
    from sage.groups.misc_gps.misc_groups_catalog import (
        Cactus as _SageCactus,
    )
    from sage.groups.misc_gps.misc_groups_catalog import (
        Free as _SageFree,
    )
    from sage.groups.misc_gps.misc_groups_catalog import (
        PureCactus as _SagePureCactus,
    )
    from sage.groups.misc_gps.misc_groups_catalog import (
        ReflectionGroup as _SageReflection,
    )
    from sage.groups.misc_gps.misc_groups_catalog import (
        RightAngledArtin as _SageRightAngledArtin,
    )
    from sage.groups.misc_gps.misc_groups_catalog import (
        WeylGroup as _SageWeyl,
    )
    from sage.groups.perm_gps.permgroup_named import (
        AlternatingGroup as _SageAlternatingGroup,
    )
    from sage.groups.perm_gps.permgroup_named import (
        CyclicPermutationGroup as _SageCyclicGroup,
    )
    from sage.groups.perm_gps.permgroup_named import (
        DiCyclicGroup as _SageDiCyclicGroup,
    )
    from sage.groups.perm_gps.permgroup_named import (
        DihedralGroup as _SageDihedralGroup,
    )
    from sage.groups.perm_gps.permgroup_named import (
        KleinFourGroup as _SageKleinFourGroup,
    )
    from sage.groups.perm_gps.permgroup_named import (
        QuaternionGroup as _SageQuaternionGroup,
    )
    from sage.groups.perm_gps.permgroup_named import (
        SymmetricGroup as _SageSymmetricGroup,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        PGL as _SagePGL,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        PGU as _SagePGU,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        PSL as _SagePSL,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        PSU as _SagePSU,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        ComplexReflection as _SageComplexReflection,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        Janko as _SageJanko,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        Mathieu as _SageMathieu,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        PSp as _SagePSp,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        RubiksCube as _SageRubiksCube,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        Suzuki as _SageSuzuki,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        SuzukiSporadic as _SageSuzukiSporadic,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        Transitive as _SageTransitive,
    )

    def an_object(self):
        r"""The cyclic group of order two.

        The smallest group that is not the trivial one, so a construction over an
        arbitrary group is exercised on a group with a non-identity element.
        """
        return self.C(2)

    C = _owned_group_constructor(_SageCyclicGroup)
    S = _owned_group_constructor(_SageSymmetricGroup)
    A = _owned_group_constructor(_SageAlternatingGroup)
    D = _owned_group_constructor(_SageDihedralGroup)
    Dic = _owned_group_constructor(_SageDiCyclicGroup)
    Q = _owned_group_constructor(_SageQuaternionGroup)
    V4 = _owned_group_constructor(_SageKleinFourGroup)
    Abelian = _owned_group_constructor(_SageAbelianGroup)
    Free = staticmethod(_free_group_constructor)
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
    Nilpotent = staticmethod(_nilpotent_group_constructor)
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

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError(f"the homomorphisms {domain} -> {codomain} cannot be formed: both must be objects of {self}")
        return self.MorCategory().Of(domain, codomain)

    def group_algebra(self, base_ring):
        r"""The functor \(R[-]\colon \mathbf{Grp}\to\mathbf{Alg}_R\)."""
        from dzack_research.preamble.categories.algebras.group_algebras import (
            _GroupAlgebraFunctor,
        )

        return _GroupAlgebraFunctor(base_ring)

    _MorCategory = GroupMorCategoryConstruction
    _EndCategory = GroupEndCategoryConstruction
    _IsoCategory = GroupIsoCategoryConstruction

    @classmethod
    def _repr_object_names(cls):
        return "groups"

    def super_categories(self):
        return [Monoids()]

    class SubcategoryMethods:
        r"""Constructions this category owns, reachable from any subcategory."""

        def FinitelyPresentedAsGroup(self) -> Category:
            r"""Return this category with the axiom that some finite presentation exists."""
            return self._with_axiom("FinitelyPresentedAsGroup")

        # Functors out of ``Grp``, each spelled as a method of this, their
        # domain category, and named by the construction it performs.

        def _categorical_product_construction(self, factors):
            r"""Return the selected finite product of represented finite groups.

            GAP's ``DirectProduct`` supplies the product group and its canonical
            projections.  The owned object is raised through the ordinary group
            constructor, so finiteness, commutativity, permutation realization,
            and presentation structure are recovered from that one product rather
            than attached after construction.
            """
            from sage.groups.perm_gps.permgroup import PermutationGroup

            from dzack_research.preamble.categories.abstract_categories.products import (
                SelectedLimitConstruction,
                _discrete_diagram,
                _finite_factor_family,
            )

            family = _finite_factor_family(factors, name="Group product factors")
            assert family.cardinality() != cardinal(0), (
                "the product of an empty family of groups (the trivial group) is not computed here; give at least one factor"
            )
            if any(factor not in self for factor in family):
                raise TypeError(f"the product of {family} cannot be formed in {self}: some factor is not an object of {self}")
            assert all(factor in OwnedFiniteGroups() for factor in family), (
                f"the product of {family} is computed here only for finite groups, and some factor is not known to be finite"
            )
            labels = tuple(family.index_set())
            engines = tuple(_gap_model(family[label]) for label in labels)
            product_engine = libgap.DirectProduct(*engines)
            product = _own_group(PermutationGroup(gap_group=product_engine))
            if product not in self:
                raise ArithmeticError(
                    f"the direct product {product} of {family} is not an object of {self}, although every factor is"
                )

            diagram = _discrete_diagram(family, self)

            def projection(label):
                position = labels.index(label) + 1
                return product.Mor(family[label])(
                    libgap.Projection(product_engine, position)
                )

            universal_cone = (diagram).ProductCones().cone(
                product,
                lambda index: projection(index.value()),
            )

            def factorizer(cone):
                apex = cone.apex()
                source_engine = _gap_model(apex)
                source_generators = tuple(source_engine.GeneratorsOfGroup())
                images = []
                for source_generator in source_generators:
                    owned_generator = _element_from_engine(apex, source_generator)
                    image = product_engine.One()
                    for position, label in enumerate(labels, start=1):
                        leg = cone.structure_morphism(diagram.domain()(label))
                        factor = family[label]
                        factor_image = leg(owned_generator)
                        image *= libgap.Embedding(product_engine, position).Image(
                            _element_to_engine(factor, factor_image)
                        )
                    images.append(image)
                return apex.Mor(product)._from_engine_generator_images(
                    source_generators,
                    images,
                )

            return SelectedLimitConstruction(diagram, universal_cone, factorizer)

        def _categorical_coproduct_construction(self, factors):
            r"""Return the selected finite coproduct of represented finite groups.

            In ``Grp`` the coproduct is the free product.  GAP supplies finite
            presentation isomorphisms for the represented finite factors, the
            maintained ``FreeProduct`` construction, and its canonical factor
            embeddings.  The result is raised as one owned finitely presented
            group; no GAP group or mapping crosses the public boundary.
            """
            from dzack_research.preamble.categories.abstract_categories.products import (
                SelectedColimitConstruction,
                _discrete_diagram,
                _finite_factor_family,
            )

            family = _finite_factor_family(factors, name="Group coproduct factors")
            assert family.cardinality() != cardinal(0), (
                "the coproduct of an empty family of groups (the trivial group) is not computed here; give at least one factor"
            )
            if any(factor not in self for factor in family):
                raise TypeError(f"the coproduct of {family} cannot be formed in {self}: some factor is not an object of {self}")
            assert all(factor in OwnedFiniteGroups() for factor in family), (
                f"the free product of {family} is computed here only for finite factors, and some factor is not known to be finite"
            )

            labels = tuple(family.index_set())
            presentation_isomorphisms = tuple(
                _gap_model(family[label]).IsomorphismFpGroup() for label in labels
            )
            presented_factors = tuple(
                isomorphism.Image() for isomorphism in presentation_isomorphisms
            )
            coproduct_engine = libgap.FreeProduct(*presented_factors)
            # A free product with two nontrivial factors contains an element of
            # infinite order (a product of nontrivial elements of two factors),
            # so it is infinite; with at most one it is that factor.  This is
            # proved here and enters as construction data of the coproduct.
            nontrivial_factors = sum(
                1 for label in labels if int(family[label].order()) > 1
            )
            size = OwnedInfiniteGroups() if nontrivial_factors >= 2 else OwnedFiniteGroups()
            coproduct = _own_group(coproduct_engine.sage(), refinements=(size,))
            assert coproduct in self, (
                f"the group free product {coproduct} of {family} is not an object of {self}; "
                "this inherited construction supplies a coproduct only when that free product "
                "lies in the requested category"
            )

            embeddings = tuple(
                libgap.Embedding(coproduct_engine, position)
                for position in range(1, len(labels) + 1)
            )
            diagram = _discrete_diagram(family, self)

            def injection(label):
                position = labels.index(label)
                return family[label].Mor(coproduct)(
                    presentation_isomorphisms[position] * embeddings[position]
                )

            universal_cocone = (diagram).CoproductCocones().cocone(
                coproduct,
                lambda index: injection(index.value()),
            )

            def factorizer(cocone):
                apex = cocone.apex()
                generator_models = []
                image_models = []
                for position, label in enumerate(labels):
                    factor = family[label]
                    leg = cocone.costructure_morphism(diagram.domain()(label))
                    isomorphism = presentation_isomorphisms[position]
                    embedding = embeddings[position]
                    for presented_generator in presented_factors[
                        position
                    ].GeneratorsOfGroup():
                        generator_models.append(
                            embedding.Image(presented_generator)
                        )
                        factor_generator = isomorphism.PreImagesRepresentative(
                            presented_generator
                        )
                        image_models.append(
                            _element_to_engine(
                                apex,
                                leg(_element_from_engine(factor, factor_generator)),
                            )
                        )
                return coproduct.Mor(apex)._from_engine_generator_images(
                    generator_models,
                    image_models,
                )

            return SelectedColimitConstruction(
                diagram,
                universal_cocone,
                factorizer,
            )

        def abelianization(self):
            r"""``(-)^ab : Grp -> Ab``, the abelianization functor.

            A group is sent to its quotient by the derived subgroup, and a
            group morphism to the morphism the universal property of that
            quotient determines.  Left adjoint of the inclusion of abelian
            groups; the adjunction is ``abelianization_adjunction``.
            """
            from dzack_research.preamble.categories.functors.abelianization import (
                _abelianization_functor,
            )

            return _abelianization_functor()

        def abelianization_adjunction(self):
            r"""``(-)^ab -| i`` between ``Grp`` and ``Ab``.

            An adjunction is a method of its left adjoint's domain category,
            and ``(-)^ab`` is the left adjoint.  Its unit at ``G`` is the
            quotient projection onto ``G/[G,G]``, and its counit identifies an
            abelian group with its own abelianization.
            """
            from dzack_research.preamble.categories.functors.abelianization import (
                _abelianization_adjunction,
            )

            return _abelianization_adjunction()

        def underlying_set(self):
            r"""``U : Grp -> Set``, the underlying-set functor.

            The right adjoint of the free-group functor spelled on ``Set``.
            On an object it is the identity: a group already is a set object,
            and forgetting the multiplication removes structure, not elements.
            """
            from dzack_research.preamble.categories.functors.free_groups import (
                _group_underlying_set_functor,
            )

            return _group_underlying_set_functor()

    class ElementMethods:
        def inverse(self):
            r"""Return the group inverse."""
            return ~self

        def _unit_decision(self):
            r"""Every group element has its group inverse as a two-sided inverse."""
            return True

        def _unit_inverse_decision(self):
            r"""Supply the monoid unit inverse through this group's inverse operation."""
            return self.inverse()

        def _regularity_decision(self):
            r"""Supply multiplicative cancellation from the group inverse.

            Left translation by x has inverse left translation by x^-1,
            and the same holds for right translation. Both are bijective.
            """
            return True

        def cyclic_subgroup(self):
            r"""Return the literal cyclic subgroup generated by this element."""
            from dzack_research.preamble.categories.group.cyclic_subgroups import (
                CyclicGroups,
            )

            return CyclicGroups()(self)

        def _cyclic_subgroup_cardinality_decision(self):
            r"""Protected cardinality computation for this element's cyclic subgroup.

            ``CyclicGroups`` calls this only when cardinality, finiteness or
            a finite enumeration is requested.  A selected element
            realization returns the cardinality supplied by its order
            algorithm, or ``None`` when that computation is unavailable.
            Constructing the cyclic subgroup needs no order decision.
            """
            return None

    class ParentMethods:
        @RealizationHook
        def _engine_group(self):
            r"""The selected group engine, when a realization supplies one (``OWN-05``)."""
            assert False, (
                f"computation with {self} through a group engine requires a selected realization; "
                "this group supplies none"
            )

        @RealizationHook
        def _engine_subgroup_from_generators(self, generators):
            r"""The selected subgroup-generation algorithm, when supplied (``OWN-05``)."""
            assert False, (
                f"the subgroup of {self} generated by {generators} is defined, but no "
                "group-engine subgroup construction is selected for this group"
            )

        def has_selected_group_resolution(self) -> bool:
            return self.has_selected_resolution(OwnedGroups())

        def group_generators_are_computable(self) -> bool:
            r"""Whether this object supplies its selected algebraic generator family.

            This reports the retained group-resolution datum, not the logical
            existence of a finite or enumerable generating set, and it runs
            no search for a presentation. A topological generating family
            alone supplies no such datum: the Frobenius of an absolute
            Galois group of a finite field generates a dense subgroup, not
            the whole abstract group.
            """
            return self.has_selected_group_resolution()

        def has_computed_group_generators(self) -> bool:
            r"""Whether selected algebraic generator data have already been fixed.

            This capability reports the retained resolution selection;
            its generator family may be realized lazily, and this method
            does not ask whether that computation has run. It neither
            enumerates the indexing set nor asserts finiteness. Without
            selected algebraic data the answer is False, including when
            only topological generators have been supplied.
            """
            return self.has_selected_group_resolution()

        def has_selected_finite_group_generating_set(self) -> bool:
            r"""Whether the selected group resolution has finitely many degree-zero generators."""
            match self.has_selected_group_resolution():
                case False:
                    return False
                case True:
                    return bool(
                        self.selected_group_resolution()
                        .generating_set()
                        .cardinality()
                        .is_finite()
                    )

        def selected_group_resolution(self):
            return self.selected_resolution(OwnedGroups())

        def group_generating_set(self):
            return self.selected_group_resolution().generating_set()

        def group_generator_morphism(self):
            return self.selected_group_resolution().generator_morphism()

        def group_generator(self, label):
            return self.selected_group_resolution().generator(label)

        def group_generators(self):
            return self.selected_group_resolution().generators(
                name="Group generators"
            )

        def invariant_overlattice(self, lattice):
            r"""Return the least integral invariant overlattice for this rational orthogonal action.

            The group must be a retained subgroup of the orthogonal group
            of the chosen rational span. For a nondegenerate lattice L,
            every integral overlattice is contained in L-sharp and hence
            in ``(1/abs(det L))*L``. This finite bound makes orbit-span
            closure terminate even for an infinite finitely generated group.
            A degenerate L requires a finite group for this realization.
            """
            from dzack_research.preamble.categories.functors.group_actions import GroupActionFunctor
            from dzack_research.preamble.categories.group.g_objects import GObjects
            from dzack_research.preamble.categories.modules.orbit_spans import OrbitSpanLattices
            from dzack_research.preamble.categories.modules.pure.modules import Modules, ModulesOverIntegralDomains

            ring = lattice.base_ring()
            if ring is not _own_ring(ZZ):
                raise TypeError("an integral invariant overlattice requires a lattice over ZZ")
            if not lattice.module_rank().is_finite():
                raise NotImplementedError("the invariant overlattice construction requires finite rank")
            field_map = ring.fraction_field_map()
            rational = lattice.base_change(field_map)
            seed = ModulesOverIntegralDomains(ring)(lattice).generic_fibre_map()
            ambient = seed.codomain()
            group = self
            group_inclusion = OwnedGroups().Mor(self, self).identity()
            while group.supergroup() is not group:
                inclusion = group.inclusion()
                group_inclusion = OwnedGroups().Mor(group, inclusion.codomain())(inclusion) * group_inclusion
                group = group.supergroup()
            if group is not rational.Aut():
                raise ValueError("the group must be included in the orthogonal group of this rational span")
            restrict = Modules(field_map.codomain()).restriction_of_scalars(field_map)
            action = GroupActionFunctor(
                self, Modules(ring), ambient,
                lambda g: restrict(Modules(field_map.codomain()).Mor(rational, rational)(group_inclusion(g))),
            )
            determinant = abs(lattice.determinant())
            bound = None
            if determinant != ring.zero():
                inverse = field_map.codomain().one() / field_map(determinant)
                containing = ambient.subobject_on(tuple(
                    ambient(rational.scalar_multiple(inverse, seed(v).underlying_element()))
                    for v in lattice.module_generators()
                ))
                bound = containing.inclusion()
            construction = GObjects(self, Modules(ring)).orbit_generated_submodule(
                action, seed, containing=bound
            )
            return OrbitSpanLattices(ring)(construction, rational)

        def number_of_group_generators(self):
            return self.selected_group_resolution().generator_count()

        def conjugation_morphism(self):
            r"""The morphism ``G -> Aut(G)`` stated on the selected generators."""
            match self:
                case _ if self in OwnedFiniteGroups():
                    automorphisms = self.Aut()
                    model = _gap_model(self)
                    images = {
                        generator: automorphisms(
                            libgap.ConjugatorAutomorphism(
                                model,
                                _element_to_engine(self, generator),
                            )
                        )
                        for generator in self.group_generators()
                    }
                    return self.Mor(automorphisms)(images)
                case _:
                    assert False, (
                        f"the conjugation morphism {self} -> Aut({self}) is defined for every group, but the "
                        "current preamble computes it only for finite represented groups; a general "
                        "automorphism-group/conjugation construction is still missing"
                    )

        @cached_method
        def classifying_category(self):
            r"""Return ``BG``, with one object and this group's elements as arrows."""
            from dzack_research.preamble.categories.group.classifying_categories import (
                ClassifyingCategory,
            )

            return ClassifyingCategory(self)

        def Mor(self, codomain, category=None):
            groups = OwnedGroups()
            if category is None or category.is_subcategory(groups):
                return groups.Mor(self, codomain)
            return _category_mor_parent(category, self, codomain)

        def _Hom_(self, codomain, category=None):
            groups = OwnedGroups()
            if codomain in groups and (category is None or category.is_subcategory(groups)):
                return groups.Mor(self, codomain)
            raise TypeError(f"the homomorphisms {self} -> {codomain} in {category} are not group homomorphisms: {codomain} must be a group and {category} a category of groups")

        def _finiteness_decision(self):
            match self:
                case _ if self in OwnedFiniteGroups():
                    return True
                case _ if self in OwnedInfiniteGroups():
                    return False
                case _:
                    return AtomicProposition("is_finite", self)

        def is_abelian(self):
            match self:
                case _ if self in OwnedAbelianGroups():
                    return True
                case _:
                    return self._abelianity_decision()

        def _abelianity_decision(self):
            match self:
                case _ if self in OwnedFiniteGroups():
                    return conjunction(left * right == right * left for left in self for right in self)
                case _:
                    return AtomicProposition("is_abelian", self)

        def _commutativity_decision(self):
            r"""Commutativity of the group law is abelianity: the magma predicate asks ``is_abelian``."""
            return self._abelianity_decision()

        def is_finitely_generated(self):
            r"""Finite group generation, equivalently finite generation of its magma.

            From group generators S, the finite set S union S^-1 union {1}
            generates the magma. Conversely a magma generating set also
            generates the group. No selected group generators are changed.
            """
            return self.is_finitely_generated_as_magma()

        @RealizationHook
        def _finite_magma_generation_decision(self):
            r"""Supply the common magma predicate through the existing group decision."""
            return self._finite_generation_decision()

        def _finite_generation_decision(self):
            return AtomicProposition("is_finitely_generated", self)

        def is_finitely_presented_as_group(self):
            match self.is_finitely_generated():
                case False:
                    return False
                case _ if self in OwnedGroups().FinitelyPresentedAsGroup():
                    return True
                case _:
                    return AtomicProposition("is_finitely_presented_as_group", self)

        def is_arithmetic_group(self):
            if self in OwnedGroups().Arithmetic():
                return True
            return self._arithmeticity_decision()

        def _arithmeticity_decision(self):
            return AtomicProposition("is_arithmetic_group", self)

        def is_topological_group(self):
            r"""Whether a compatible group topology is part of the selected structure.

            Absence of a topological-group category placement does not prove
            that no compatible topology is carried by the represented group.

            EXAMPLES::

                sage: from dzack_research.preamble.categories.group.groups import OwnedGroups, TopologicalGroups
                sage: from dzack_research.preamble.logic import AtomicProposition
                sage: topological = TopologicalGroups().an_object()
                sage: topological.is_topological_group()
                True
                sage: underlying = OwnedGroups().C(2)
                sage: undecided = underlying.is_topological_group()
                sage: isinstance(undecided, AtomicProposition)
                True
            """
            match self:
                case _ if self in TopologicalGroups():
                    return True
                case _:
                    return AtomicProposition("is_topological_group", self)

        def _cardinality_decision(self):
            r"""``|G|``, from what the group's own data determine.

            A finite group is counted by its engine.  A free group on a basis
            ``S`` is trivial for empty ``S`` and otherwise has
            ``max(aleph_0, |S|)`` elements, its reduced words.  An infinite
            finitely generated group is a quotient of a free group of finite
            rank, so it is countably infinite.  A subcategory whose datum
            determines more supplies its own answer.
            """
            match self:
                case _ if self in OwnedFiniteGroups():
                    return cardinal(_finite_order(self))
                case _ if self in GroupsWithChosenFreeBasis():
                    basis_cardinality = self.free_basis().cardinality()
                    if basis_cardinality == cardinal(0):
                        return cardinal(1)
                    return Cardinalities().supremum(aleph(0), basis_cardinality)
                case _ if self in OwnedInfiniteGroups() and self in OwnedGroups().FinitelyGeneratedAsMagma():
                    return aleph(0)
                case _:
                    assert False, (
                        f"cannot compute the cardinality of the group {self}: it is not known to be finite, "
                        f"it has no chosen free basis, and it is not known to be infinite and finitely "
                        f"generated (it is in {self.category()})"
                    )

        def order(self):
            r"""The set cardinality, read as an integer when finite."""
            size = cardinal(self.cardinality())
            match size.is_finite():
                case True:
                    return _own_ring(ZZ)(int(size.finite_value()))
                case False:
                    return size

        def quotient_by_relators(self, relators):
            r"""Return ``G / <<relators>>``, the quotient by their normal closure."""
            match self:
                case _ if isinstance(_engine_group(self), FreeGroup_class):
                    # The free source and the caller's chosen relators
                    # define this quotient. Preserve them at the family
                    # constructor rather than discarding them on ingress.
                    return FreeGroupQuotients(self, relators)()
                case _ if self in GroupsWithChosenFinitePresentation():
                    return _engine_quotient_by_relators(self, relators)
                case _:
                    assert False, (
                        f"the quotient of {self} by the normal closure of {relators} is defined for every group, "
                        "but the current preamble computes it only for groups with a chosen finite presentation"
                    )

        def finite_image_lifts(
            self,
            image,
            *,
            generators=None,
            multiply=None,
            image_bound=None,
        ):
            r"""Retain one source lift above every element of a finite generated image.

            This is the Cayley-graph image algorithm for a group map whose
            source generators are represented.  ``image`` may be an owned
            group morphism or another exact represented homomorphism.  When
            its codomain is an owned finite group, that cardinality is the
            termination bound; a finite quotient represented by another
            exact multiplication law supplies ``multiply`` and
            ``image_bound`` explicitly.

            Supplying ``generators`` asks for the image of the subgroup they
            generate, while the retained witnesses remain elements of
            ``self``.  The consistency check on every newly retained word
            makes this operation unsuitable for an arbitrary nonhomomorphic
            callback: it is the owner for finite group images with lifts, not
            a generic graph traversal.

            The image-size bound must be integral; truncating a rational
            bound would silently change the contract of the finite search.
            """
            if generators is None:
                assert self.has_selected_group_resolution() and self.has_selected_finite_group_generating_set(), (
                    f"the image of {self} under {image} cannot be enumerated: {self} has no selected finite "
                    "generating set; pass a finite generating family explicitly"
                )
                generators = tuple(self.group_generators())
            else:
                generators = tuple(generators)
                assert all(generator in self for generator in generators), (
                    f"the image under {image} cannot be enumerated from {generators}: not every one of them is an element of {self}"
                )

            if multiply is None:
                multiply = lambda left, right: left * right
            if image_bound is None:
                codomain = image.codomain()
                assert codomain in OwnedFiniteGroups(), (
                    f"the image of {self} under {image} cannot be enumerated: its codomain {codomain} is not known to be finite; "
                    f"pass image_bound, a bound on the order of the image"
                )
                image_bound = int(codomain.cardinality())
            original_bound = image_bound
            image_bound = int(image_bound)
            if image_bound != original_bound:
                raise ValueError("the finite-image cardinality bound must be an integer")
            if image_bound < 1:
                raise ValueError(f"image_bound = {image_bound} is not a bound on the order of the image of {self}: every image contains the identity, so its order is at least 1")

            identity = self.one()
            identity_image = image(identity)
            witnesses = {identity_image: identity}
            steps = tuple(
                (image(word), word)
                for generator in generators
                for word in (generator, ~generator)
            )
            frontier = [identity_image]
            while frontier:
                current_image = frontier.pop()
                current_witness = witnesses[current_image]
                for step_image, step_witness in steps:
                    candidate_image = multiply(step_image, current_image)
                    if candidate_image in witnesses:
                        continue
                    candidate_witness = step_witness * current_witness
                    if image(candidate_witness) != candidate_image:
                        raise ArithmeticError(
                            f"{image} is not a homomorphism on {self}: the element {candidate_witness} maps to "
                            f"{image(candidate_witness)}, but the product of the images of its factors is {candidate_image}"
                        )
                    witnesses[candidate_image] = candidate_witness
                    frontier.append(candidate_image)
                    if len(witnesses) > image_bound:
                        raise ArithmeticError(
                            f"the image of {self} under {image} has more than image_bound = {image_bound} elements"
                        )
            return witnesses

        def subgroup(self, generators):
            return _engine_subgroup(self, generators)

        def predicate_subgroup(
            self,
            predicate,
            description,
            *,
            character_data=None,
            character_data_complete=None,
        ):
            r"""Return the subgroup of elements satisfying ``predicate``."""
            from dzack_research.preamble.categories.group.predicate_subgroups import (
                PredicateSubgroups,
            )

            return PredicateSubgroups(self)(
                predicate,
                description,
                character_data=character_data,
                character_data_complete=character_data_complete,
            )

        def centralizer(self, element):
            r"""Return the subgroup of elements commuting with ``element``."""
            from dzack_research.preamble.categories.group.predicate_subgroups import (
                CentralizerSubgroups,
            )

            return CentralizerSubgroups(self)(element)

        @RealizationHook
        def _normalizer_construction(self, subgroup):
            r"""Supply a selected construction of ``N_self(subgroup)``, or None.

            Protected construction contract under OWN-05. Only normalizer
            calls this hook, after subgroup admission. A more specific
            category may return its normalizer with its retained subgroup
            data; None selects the general predicate stabilizer. An
            undecided normality predicate does not select the whole group.
            """
            return None

        def normalizer(self, subgroup):
            r"""Return ``N_G(H) = {g in G : g H g^-1 = H}``, the stabilizer of ``H`` under conjugation."""
            assert subgroup is self or subgroup in self.subgroups(), f"{subgroup} is not a subgroup of {self}"
            from dzack_research.preamble.categories.group.predicate_subgroups import (
                StabilizerSubgroups,
            )

            selected = self._normalizer_construction(subgroup)
            if selected is not None:
                return selected

            def normalizes(group_element):
                if subgroup is self or (group_element == self.one()) is True or self.is_abelian() is True:
                    return True
                if subgroup.has_selected_group_resolution() and subgroup.has_selected_finite_group_generating_set():
                    generators = tuple(subgroup.group_generators())
                    inverse = group_element.inverse()
                    return conjunction(
                        subgroup.is_parent_of(conjugator * generator * inverse_conjugator)
                        for conjugator, inverse_conjugator in (
                            (group_element, inverse), (inverse, group_element)
                        )
                        for generator in generators
                    )
                if subgroup in OwnedFiniteGroups():
                    inverse = group_element.inverse()
                    return conjunction(
                        subgroup.is_parent_of(group_element * element * inverse)
                        for element in subgroup
                    )
                return AtomicProposition("normalizes", group_element, subgroup)

            return StabilizerSubgroups(self)(
                subgroup,
                "conjugation",
                normalizes,
                description=f"normalizer of {subgroup} in {self}",
            )

        @RealizationHook
        def _conjugacy_decision(self, source, target):
            r"""Protected decision whether ``target = g source g^-1`` for some ``g``.

            ``conjugation_g_set`` is the only caller, after equality and
            commutativity have not decided it.  A category whose objects
            supply a procedure answers ``True`` or ``False``; ``Unknown``
            means that no procedure decides it.
            """
            return Unknown

        @cached_method
        def conjugation_g_set(self):
            r"""Return ``G`` with its conjugation action ``g.x = g x g^-1``.

            Two elements are conjugate when one is the other; in an abelian
            group exactly then.  A finite group decides the relation from
            its orbits; elsewhere the procedure its category supplies
            decides it, or it is undecided.  The stabilizer of ``x`` is its
            centralizer.
            """
            from dzack_research.preamble.categories.group.g_sets import (
                FiniteGSets,
                _g_set_on_points,
            )

            def conjugate(group_element, point):
                return group_element * point * group_element.inverse()

            match self:
                case _ if self in OwnedFiniteGroups():
                    return FiniteGSets(self)(finite_ordered_set(tuple(self)), conjugate)
                case _:

                    def conjugacy(source, target):
                        equal = source == target
                        if equal is True:
                            return True
                        if self.is_abelian() is True:
                            return equal
                        return self._conjugacy_decision(source, target)

                    return _g_set_on_points(
                        self, self, conjugate, conjugacy, self.centralizer
                    )

        @cached_method
        def conjugacy_classes(self):
            r"""Return the orbit set ``G / G`` of the conjugation action."""
            return self.conjugation_g_set().orbits()

        def conjugacy_class(self, representative):
            r"""Return the conjugacy orbit of ``representative``."""
            return self.conjugacy_classes().orbit_of(self(representative))

        @RealizationHook
        def _conjugate_subgroup_construction(self, group_element, subgroup):
            r"""Supply a selected ``g H g^-1`` construction, or None.

            Protected construction contract under OWN-05. Only
            conjugate_subgroup calls this hook, with admitted ``g`` and
            ``H``. A more specific category retains any defining data of
            its conjugated subgroup; None selects the general predicate
            construction. The public operation is owned by groups.
            """
            return None

        def conjugate_subgroup(self, group_element, subgroup):
            r"""Return ``g H g^-1``, the image of ``H`` under conjugation by ``g``."""
            assert group_element in self, f"{group_element} is not an element of {self}"
            assert subgroup is self or subgroup in self.subgroups(), f"{subgroup} is not a subgroup of {self}"
            if subgroup is self:
                return self
            selected = self._conjugate_subgroup_construction(group_element, subgroup)
            if selected is not None:
                return selected
            inverse = group_element.inverse()
            return self.predicate_subgroup(
                lambda element: subgroup.is_parent_of(inverse * element * group_element),
                description=f"conjugate of {subgroup} by {group_element}",
            )

        @RealizationHook
        def _subgroup_conjugacy_decision(self, left, right):
            r"""Protected decision whether ``right = g left g^-1`` for some ``g``.

            ``subgroup_conjugation_g_set`` is the only caller.  A category
            whose objects supply a procedure answers ``True`` or ``False``;
            ``Unknown`` means that no procedure decides it.
            """
            return Unknown

        @cached_method
        def subgroup_conjugation_g_set(self):
            r"""The set of subgroups of ``G`` with the conjugation action ``g.H = g H g^-1``.

            The stabilizer of ``H`` is its normalizer.
            """
            from dzack_research.preamble.categories.group.g_sets import _g_set_on_points

            return _g_set_on_points(
                self,
                self.subgroups(),
                self.conjugate_subgroup,
                self._subgroup_conjugacy_decision,
                self.normalizer,
            )

        def left_cosets(self, subgroup):
            r"""Return the represented left-coset space ``G/H``."""
            from dzack_research.preamble.categories.group.g_sets import _left_coset_g_set
            return _left_coset_g_set(self, subgroup)

        def right_cosets(self, subgroup):
            r"""Return the represented right-coset space ``H\\G``."""
            match self:
                case _ if self in OwnedFiniteGroups():
                    return _engine_cosets(self, subgroup, "right")
                case _:
                    assert False, (
                        f"the right cosets of {subgroup} in {self} are defined, but the current "
                        "preamble materializes coset spaces only for finite represented groups"
                    )

        @cached_method
        @RealizationHook
        def _center_construction(self):
            r"""Supply the magma center as a group and its literal inclusion.

            Every group element is nuclear by associativity, so the magma
            center is exactly the subgroup of elements commuting with every
            group element.  The common ``Magmas`` owner projects this one
            cached construction onto its center and inclusion.
            """
            match self:
                case _ if self in OwnedAbelianGroups():
                    return self, OwnedGroups().Mor(self, self).identity()
                case _ if self in OwnedFiniteGroups():
                    center = _subgroup_from_gap(self, _gap_model(self).Center())
                    return center, center.inclusion()
                case _:
                    assert False, (
                        f"the center Z({self}) is defined for every group, but the current preamble computes it "
                        "only for abelian or finite represented groups; no general center algorithm is installed"
                    )

        @cached_method
        def commutator_subgroup(self):
            r"""Return the derived subgroup ``[G,G]``."""
            match self:
                case _ if self in OwnedFiniteGroups():
                    return _subgroup_from_gap(self, _gap_model(self).DerivedSubgroup())
                case _:
                    assert False, (
                        f"the commutator subgroup [{self},{self}] is defined for every group, but the current "
                        "preamble computes it only for finite represented groups; the presentation route is "
                        "still missing"
                    )

        def derived_subgroup(self, *args, **kwargs):
            return self.commutator_subgroup(*args, **kwargs)

        @cached_method
        def subgroups(self):
            r"""Return the set of represented subgroups of this group.

            Its points are objects of ``Subgroups(self)``, so every point
            retains its inclusion into this group.  Finite represented groups
            additionally enumerate this same set exactly through GAP.
            """
            return _SubgroupCollection(self)

        def supergroup(self):
            r"""The group this one was constructed as a subgroup of; a group that is not is its own.

            ``Subgroups(G)`` and the automorphism-group constructions state
            the containing group as construction data and answer it there.
            """
            return self

        def inclusion(self):
            return _canonical_subgroup_inclusion(self)

        def End(self):
            return OwnedGroups().End(self)

        @cached_method
        def Aut(self):
            return OwnedGroups().Aut(self)

        def is_isomorphic_to(self, other):
            match (self, other):
                case (left, right) if left in OwnedFiniteGroups() and right in OwnedFiniteGroups():
                    found = _gap_model(left).IsomorphismGroups(_gap_model(right))
                    return str(found) != "fail"
                case _:
                    assert False, (
                        f"whether {self} is isomorphic to {other} is defined for every pair of groups, but the "
                        "current preamble decides it only for finite represented groups"
                    )

    class Commutative(CategoryWithAxiom):
        def an_object(self):
            r"""The cyclic group of order two."""
            return OwnedGroups().C(2)

        @classmethod
        def _repr_object_names(cls):
            return "abelian groups"

        class ElementMethods:
            def __rmul__(self, exponent):
                r"""Return the canonical integer multiple of an abelian-group element."""
                return self.parent().scalar_multiple(exponent, self)

        class ParentMethods:
            @cached_method
            def endomorphism_ring(self):
                r"""The ring ``End(A)`` of group endomorphisms, under pointwise sum and composition."""
                return AbelianGroupEndomorphismRings()(self)

            @cached_method
            def scalar_action(self):

                integers = _own_ring(ZZ)
                endomorphisms = self.endomorphism_ring()
                return integers.Mor(endomorphisms)(endomorphisms._scalar_identity)

            def scalar_multiple(self, exponent, element):

                return self.scalar_action()(_own_ring(ZZ)(exponent))(element)

    class Finite(CategoryWithAxiom):
        def an_object(self):
            r"""The cyclic group of order two."""
            return OwnedGroups().C(2)

        @classmethod
        def _repr_object_names(cls):
            return "finite groups"

        def extra_super_categories(self) -> list[Category]:
            r"""The multiplication table is a finite presentation."""
            return [OwnedGroups().FinitelyPresentedAsGroup()]

        class ParentMethods:
            def conjugate_subgroup(self, group_element, subgroup):
                r"""Return ``g H g^-1``; GAP's ``ConjugateSubgroup(H, x)`` is ``x^-1 H x``."""
                assert group_element in self, f"{group_element} is not an element of {self}"
                assert subgroup in self.subgroups(), f"{subgroup} is not a subgroup of {self}"
                return _subgroup_from_gap(
                    self,
                    libgap.ConjugateSubgroup(
                        _gap_model(subgroup),
                        _element_to_engine(self, group_element.inverse()),
                    ),
                )

            def _subgroup_conjugacy_decision(self, left, right) -> bool:
                r"""GAP's ``IsConjugate`` decides conjugacy of subgroups of a finite group."""
                return bool(
                    libgap.IsConjugate(_gap_model(self), _gap_model(left), _gap_model(right))
                )

            def order_is_invertible_in(self, ring) -> bool:
                r"""Return whether the finite order ``|G|`` is a unit in ``ring``."""
                return bool(ring(int(self.order())).is_unit())

            def conjugacy_classes_representatives(self):
                classes = _gap_model(self).ConjugacyClasses()
                return FiniteOrderedSets().from_indexed(
                    Sets.Δ[len(classes) - 1],
                    lambda position: _element_from_engine(
                        self,
                        classes[int(position)].Representative(),
                    ),
                    name="Conjugacy-class representatives",
                )

            def class_function(self, codomain, values, *, representatives=None):
                r"""The conjugacy-invariant map on the classes of the given representatives.

                A class function is constant on conjugacy classes, so it is
                the map from the union of those classes into ``A``, sending
                each member to its class value. If the representatives cover
                all of ``G``, its domain is exactly ``G``. A proper union,
                such as the ``p``-regular locus of a Brauer character, is
                an owned subset of ``G``, not a partial map with domain ``G``.
                The representatives default to the group's entire conjugacy
                class framing.
                """
                if representatives is None:
                    representatives = self.conjugacy_classes_representatives()
                if representatives not in FiniteOrderedSets():
                    representatives = finite_ordered_set(tuple(representatives))
                supplied = tuple(codomain(value) for value in values)
                if len(supplied) != int(representatives.cardinality()):
                    raise ValueError(
                        f"cannot build a class function on {self} from {len(supplied)} values: a class "
                        f"function takes one value per given conjugacy class, and {representatives.cardinality()} "
                        f"classes were given"
                    )
                table = {
                    element: value
                    for representative, value in zip(representatives, supplied, strict=True)
                    for element in _conjugacy_class_elements(self, representative)
                }
                # The domain carries its inclusion into G as selected set data.
                domain = (
                    self if len(table) == int(self.order())
                    else self.condition_set(lambda element: element in table)
                )

                def value_of_class(element):
                    return table[element]

                return Sets().Mor(domain, codomain)(value_of_class)

            @cached_method
            def character_set(self):
                r"""Return the owned set ``Char(self)`` of ordinary characters."""
                from dzack_research.preamble.categories.group.characters import (
                    _character_set,
                )

                return _character_set(self)

            @cached_method
            def irreducible_characters(self):
                r"""The complex irreducible characters, as elements of ``Char(G)``.

                Values lie in the cyclotomic field of the group's exponent
                and are read on the chosen conjugacy-class representatives,
                in the order GAP's ``Irr`` lists them.
                """
                from dzack_research.preamble.categories.rings.number_fields import (
                    CyclotomicField,
                )

                gap_group = _gap_model(self)
                exponent = int(gap_group.Exponent())
                field = CyclotomicField(exponent)
                engine_field = _engine_ring(field)
                representatives = self.conjugacy_classes_representatives()
                # One class-function object per character: the set is the
                # index of isotypic components and is compared by identity.
                return finite_ordered_set(
                    tuple(
                        self.character_set()._from_known_character(
                            self.class_function(
                                field,
                                tuple(
                                    _owned_engine_element(field, engine_field(value.sage()))
                                    for value in character.List()
                                ),
                                representatives=representatives,
                            )
                        )
                        for character in gap_group.Irr()
                    )
                )

            def character(self, values):
                r"""Return the ordinary character with the stated class values.

                Values are indexed by this group's selected conjugacy-class
                representatives and live in the same cyclotomic coefficient
                field as :meth:`irreducible_characters`.  The values define an
                ordinary character exactly when every inner product with an
                irreducible character is a nonnegative integer and the class
                function is the sum of the irreducibles with those
                multiplicities.  The result is the owned character, an element
                of ``Char(G)``, whose value family is a class function on ``G``.
                """
                from dzack_research.preamble.categories.rings.number_fields import (
                    CyclotomicField,
                )

                gap_group = _gap_model(self)
                field = CyclotomicField(int(gap_group.Exponent()))
                representatives = self.conjugacy_classes_representatives()
                supplied = tuple(values)
                if len(supplied) != int(representatives.cardinality()):
                    raise ValueError(
                        f"{supplied} cannot be the values of a character of {self}: a character takes one value on each of "
                        f"the {representatives.cardinality()} conjugacy classes, but {len(supplied)} values were given"
                    )
                candidate = self.character_set()._from_known_character(
                    self.class_function(
                        field,
                        tuple(field(value) for value in supplied),
                        representatives=representatives,
                    )
                )
                integers = _own_ring(ZZ)
                irreducibles = self.irreducible_characters()
                inner_products = tuple(
                    candidate._inner_product(irreducible) for irreducible in irreducibles
                )
                if any(inner_product not in integers for inner_product in inner_products):
                    raise ValueError(
                        f"the class function with values {supplied} is not a character of {self}: its inner products "
                        f"with the irreducible characters are {inner_products}, and not all are integers"
                    )
                multiplicities = tuple(integers(inner_product) for inner_product in inner_products)
                if any(multiplicity < integers.zero() for multiplicity in multiplicities):
                    raise ValueError(
                        f"the class function with values {supplied} is not a character of {self}: its multiplicities "
                        f"{multiplicities} on the irreducible characters are not all nonnegative"
                    )
                if any(
                    sum(
                        (
                            multiplicity * irreducible(representative)
                            for multiplicity, irreducible in zip(multiplicities, irreducibles, strict=True)
                        ),
                        field.zero(),
                    )
                    != field(expected)
                    for representative, expected in zip(representatives, supplied, strict=True)
                ):
                    raise ValueError(
                        f"the class function with values {supplied} is not a character of {self}: it is not the sum of "
                        f"the irreducible characters with multiplicities {multiplicities}"
                    )
                return candidate

            @cached_method
            def trivial_character(self):
                r"""Return the degree-one trivial ordinary character of ``self``.

                Its values live in the same cyclotomic field selected for the
                ordinary irreducible characters of this group, so it is an
                element of the same owned character set and composes with the
                existing character arithmetic without a separate value model.
                """
                from dzack_research.preamble.categories.rings.number_fields import (
                    CyclotomicField,
                )

                gap_group = _gap_model(self)
                field = CyclotomicField(int(gap_group.Exponent()))
                representatives = self.conjugacy_classes_representatives()
                return self.character_set()._from_known_character(
                    self.class_function(
                        field,
                        tuple(field.one() for _representative in representatives),
                        representatives=representatives,
                    )
                )

            @cached_method
            def character_table(self):
                r"""The character table: rows the irreducible characters, columns the classes.

                A square matrix over the cyclotomic field of the group's
                exponent, the row and column orders being those of
                ``irreducible_characters()`` and
                ``conjugacy_classes_representatives()``.
                """
                characters = self.irreducible_characters()
                size = int(characters.cardinality())
                field = characters[0].codomain()
                return field.matrix_space(size, size).from_rows(tuple(tuple(character.values()) for character in characters))

    class Infinite(CategoryWithAxiom):
        @classmethod
        def _repr_object_names(cls):
            return "infinite groups"

    class Arithmetic(CategoryWithAxiom):
        r"""Groups with a supplied arithmeticity witness."""

        def an_object(self):
            return OwnedGroups().SL(2, ZZ)

        @classmethod
        def _repr_object_names(cls):
            return "arithmetic groups"

    class FinitelyGeneratedAsMagma(CategoryWithAxiom):
        r"""Groups admitting some finite generating set."""

        def an_object(self):
            r"""The cyclic group of order two."""
            return OwnedGroups().C(2)

        @classmethod
        def _repr_object_names(cls):
            return "finitely generated groups"

        @cached_method
        def resolution_category(self):
            from dzack_research.preamble.categories.abstract_categories.resolutions import (
                Resolutions,
            )

            free = GroupsWithChosenFreeBasis()
            finite_free = Cat().meet(
                (free, OwnedGroups().FinitelyGeneratedAsMagma())
            )
            return Resolutions(OwnedGroups(), free, 0, finite_free)

        @cached_method
        def resolution_classifier(self):
            return self.resolution_category().target_functor()

    class FinitelyPresentedAsGroup(CategoryWithAxiom):
        r"""Groups admitting some finite presentation."""

        def an_object(self):
            r"""The cyclic group of order two."""
            return OwnedGroups().C(2)

        @classmethod
        def _repr_object_names(cls):
            return "finitely presented groups"

        def extra_super_categories(self) -> list[Category]:
            r"""The generating set of a finite presentation is finite."""
            return [OwnedGroups().FinitelyGeneratedAsMagma()]

        @cached_method
        def resolution_category(self):
            from dzack_research.preamble.categories.abstract_categories.resolutions import (
                Resolutions,
            )

            free = GroupsWithChosenFreeBasis()
            finite_free = Cat().meet(
                (free, OwnedGroups().FinitelyGeneratedAsMagma())
            )
            return Resolutions(OwnedGroups(), free, 1, finite_free)

        @cached_method
        def resolution_classifier(self):
            return self.resolution_category().target_functor()

        class ParentMethods:
            @cached_method
            def presentation(self):
                r"""Return one selected finite-presentation model of this group.

                Finite presentability is only the existence property.  This is
                the explicit property-to-data crossing: an object that already
                carries selected presentation data is returned unchanged;
                otherwise the maintained presentation algorithm constructs a
                separate presented group.  That object retains this exact group
                and the comparison morphism back to it, so selecting a
                presentation never mutates the source group.
                """
                if self in GroupsWithChosenFinitePresentation():
                    return self
                presented_engine = _computed_finitely_presented_engine(self)
                return _own_group(
                    presented_engine,
                    refinements=_finite_if_bounded_by(self),
                    presentation_source_group=self,
                )



class TopologicalGroups(OwnedCategory):
    r"""Owned groups equipped with a represented compatible topology."""

    def an_object(self):
        r"""The procyclic absolute Galois group of ``GF(2)``."""
        from dzack_research.preamble.categories.group.profinite.profinite_groups import (
            ProfiniteGroups,
        )

        return ProfiniteGroups().an_object()

    def super_categories(self):
        return [OwnedGroups()]

    class ParentMethods:
        @RealizationHook
        def _topological_generating_family(self):
            r"""Supply a selected family whose generated subgroup is dense.

            Protected value contract of ``TopologicalGroups``. The sole
            caller is ``topological_group_generators``. A more specific
            category or realization may retain a distinguished family;
            ``None`` leaves the public operation to its general construction.
            A supplied family need not generate the whole abstract group.
            """
            return None

        @cached_method
        def topological_group_generators(self):
            r"""Return a selected family generating a dense subgroup.

            Retain a distinguished family when one is supplied. Otherwise
            select the identity family ``(g)_{g in G}``: its values generate
            ``G`` itself, so their subgroup is dense in every group topology.
            This family retains the actual group as its index set and reads
            a value only at a supplied point; it does not enumerate ``G`` or
            claim finite generation. Neither case selects an algebraic group
            resolution.
            """
            selected = self._topological_generating_family()
            if selected is not None:
                return selected
            from dzack_research.preamble.categories.sets.indexed_families import (
                indexed_family,
            )

            return indexed_family(
                self,
                lambda element: element,
                name="Topological group generators",
            )

        def topological_generating_family(self):
            r"""Return the same selected family as ``topological_group_generators``."""
            return self.topological_group_generators()

        def is_profinite(self):
            r"""Whether this topological group is profinite, or the proposition that it is."""
            from dzack_research.preamble.categories.group.profinite.profinite_groups import (
                ProfiniteGroups,
            )

            return True if self in ProfiniteGroups() else AtomicProposition("is_profinite", self)


class GroupsWithChosenFreeBasis(OwnedCategory):
    r"""Free groups carrying the chosen set they are free on.

    The datum is the basis ``S``: the group is the free group ``F(S)``, and
    its morphisms out are determined by set maps out of ``S``.
    """

    def an_object(self):
        r"""The free group on one chosen generator."""
        return Groups.Free(1)

    def super_categories(self):
        return [OwnedGroups()]

    class ElementMethods:
        def _repr_(self):
            r"""The reduced word in the free generators ``g_s``, ``s`` a point of the free basis."""
            syllables = _reduced_word_syllables(self.parent(), self)
            if not syllables:
                return "1"
            return " ".join(f"g_{label}" if exponent == 1 else f"g_{label}^{exponent}" for label, exponent in syllables)

        def _latex_(self):
            r"""The reduced word in the free generators ``g_s``, ``s`` a point of the free basis."""
            syllables = _reduced_word_syllables(self.parent(), self)
            if not syllables:
                return "1"
            return " ".join(
                rf"g_{{{latex(label)}}}" if exponent == 1 else rf"g_{{{latex(label)}}}^{{{exponent}}}"
                for label, exponent in syllables
            )

    class ParentMethods:
        def __init__(self, free_basis, **rest) -> None:
            self._free_basis = free_basis
            super().__init__(**rest)

        def free_basis(self):
            r"""Return the set ``S`` this group is the free group on."""
            return self._free_basis

        def free_generator(self, index):
            r"""Return the free generator indexed by a point of the free basis."""
            return _free_generator(self, index)

        def reduced_word(self, element):
            r"""Return the reduced word as an owned finite family of signed generators."""
            return _reduced_word(self, element)

        def _conjugacy_decision(self, source, target) -> bool:
            r"""Conjugacy in a free group is decided by cyclic reduction of reduced words."""
            return _free_group_conjugacy(self, source, target)


class PermutationGroups(OwnedCategory):
    """Groups carrying a chosen faithful action on a finite set of points.

    A data subcategory: the natural action on the points is the chosen datum,
    and the methods below consume it.  Elements act on the left, so
    ``(g h)(x) = g(h(x))``.
    """

    def an_object(self):
        r"""The symmetric group on two points."""
        return OwnedGroups().S(2)

    @classmethod
    def _repr_object_names(cls):
        return "permutation groups"

    def super_categories(self):
        return [OwnedGroups()]

    class ElementMethods:
        def sign(self):
            r"""The sign of this element as a permutation of the natural points."""
            return _owned_engine_element(ZZ, ZZ(self.parent()._to_engine(self).sign()))

    class ParentMethods:
        def _permutation_point_action(self, backend_element, point):
            engine = _engine_group(self)
            engine_point = _engine_point(engine, point)
            if engine_point not in engine.domain():
                raise ValueError(
                    f"{point} is outside the selected permutation domain {self.natural_points()}"
                )
            return _owned_point(backend_element(engine_point))

        def natural_points(self):
            r"""The finite set the group permutes."""
            return finite_ordered_set(tuple(_owned_point(point) for point in _engine_group(self).domain()))

        def action_on(self, points):
            r"""The natural ``G``-set on the selected permutation domain.

            A different point set requires an independently specified action;
            restricting or extending the engine's action is not automatic.
            """
            from dzack_research.preamble.categories.group.g_sets import FiniteGSets
            assert points == self.natural_points(), (
                "the natural permutation action is defined only on its selected domain; "
                "specify a separate group action for another point set"
            )
            return FiniteGSets(self)(points, lambda group_element, point: group_element(point))

        @cached_method
        def natural_g_set(self):
            r"""The natural ``G``-set on the points the group permutes."""
            return self.action_on(self.natural_points())

        def natural_permutation_representation(self):
            r"""The group morphism expressing the selected faithful action.

            Its defining datum belongs to the natural G-set, so this returns
            that object's retained Mor rather than constructing a second
            homomorphism from the backend permutation labels.
            """
            return self.natural_g_set().permutation_representation()

        def orbit(self, point):
            r"""The orbit ``G . point`` of the natural action."""
            action = self.natural_g_set()
            return action.orbits().orbit_of(point).points()

        def orbits(self, points=None):
            r"""The orbit set of the natural action on ``points`` (all natural points by default)."""
            g_set = self.natural_g_set() if points is None else self.action_on(points)
            return g_set.orbits()

        def stabilizer(self, point):
            r"""The subgroup ``G_x`` fixing ``point`` in the natural action."""
            return self.natural_g_set().stabilizer(point)

        def is_transitive(self) -> bool:
            r"""Whether the natural action has one orbit."""
            return self.natural_g_set().is_transitive_action()


class SymmetricGroups(OwnedParameterizedCategory):
    r"""Full permutation groups of a chosen finite enumerated set."""

    def __init__(self, points):
        super().__init__(points)
        assert points in FiniteSets(), (
            "a category of finite full symmetric groups requires a finite "
            "point set; an infinite symmetric group is not a finite group"
        )

    def parameter_category(self):
        return EnumeratedSets()

    def super_categories(self):
        categories = [PermutationGroups(), OwnedGroups().Finite()]
        # For at most two points S_n is trivial or cyclic of order two;
        # for three points the transpositions (12) and (23) fail to
        # commute. The axiom is determined by the chosen point set.
        if cardinal(self.parameter().cardinality()).finite_value() <= 2:
            categories.append(OwnedGroups().Commutative())
        return categories

    def an_object(self):
        return self()

    def _call_(self):
        from sage.groups.perm_gps.permgroup_named import SymmetricGroup

        points = self.parameter()
        return _own_group(
            SymmetricGroup(int(cardinal(points.cardinality()).finite_value())),
            refinements=(self,), symmetric_points=points,
        )

    class ParentMethods:
        def __init__(self, symmetric_points=None, **rest):
            self._symmetric_points = symmetric_points
            super().__init__(**rest)

        def _permutation_point_action(self, backend_element, point):
            points = self.natural_points()
            if point not in points:
                raise ValueError(
                    f"{point} is outside the selected permutation domain {points}"
                )
            ranking = points.ranking_map()
            position = int(ranking(points(point))) + 1
            # The inverse of the selected ranking map is the mathematical
            # unranking operation, even when the enumeration is not stored
            # as a Python tuple or has a nontrivial selected order.
            return ranking.inverse()(int(backend_element(position)) - 1)

        def natural_points(self):
            return self._symmetric_points

        @cached_method
        def action_on(self, points):
            r"""The selected permutation action is on its actual point set.

            A different set needs a separately specified action morphism;
            applying the Sage ordinal permutation directly to its labels
            is not a group action on those labels.
            """
            assert points is self.natural_points(), (
                "the full symmetric group's selected action is on its defining "
                "point set; specify a group action to act on another set"
            )
            from dzack_research.preamble.categories.group.g_sets import FiniteGSets

            # The common PermutationGroups natural_g_set is the owner of
            # the canonical action. Its constructor dispatches here, where
            # the selected labelled point action is supplied by g(x).
            return FiniteGSets(self)(points, lambda element, point: element(point))


class GeneralLinearGroups(OwnedCategory):
    r"""Automorphism groups of the chosen standard free module ``R^n``."""

    def __init__(self, ring, degree):
        self._coefficient_ring = _owned_ring(ring)
        # An integral rank is part of the defining free-module datum.
        # Casting first would silently identify GL_(3/2)(R) with GL_1(R).
        assert degree in ZZ and degree == ZZ(degree), (
            "GL_n(R) requires an integral rank"
        )
        self._degree = int(degree)
        assert self._degree >= 0, "GL_n(R) requires a nonnegative rank"
        super().__init__()

    def coefficient_ring(self):
        return self._coefficient_ring

    def degree(self):
        return self._degree

    def super_categories(self):
        # GL_0(R) is trivial, and GL_1(R)=R^× is abelian for commutative R.
        # Neither statement licenses commutativity of the unit group of an
        # arbitrary noncommutative ring.
        abelian = (
            self.degree() == 0
            or (self.degree() == 1 and self.coefficient_ring() in OwnedRings().Commutative())
        )
        refinements = [OwnedGroups().Commutative()] if abelian else []
        # GL_n(R) is a subset of the finite matrix set R^(n*n) whenever
        # R is finite; rank zero is the trivial group over any ring.
        # For rank one, the group is R^× rather than all of R. In
        # particular ZZ^× = {1,-1} despite ZZ being infinite. Do not
        # infer infinitude merely from the coefficient set.
        if (
            self.degree() == 0
            or self.coefficient_ring().is_finite() is True
            or (self.degree() == 1 and self.coefficient_ring() is ZZ)
        ):
            return [OwnedGroups().Finite(), *refinements]
        # For any infinite coefficient ring and n >= 2, the elementary
        # transvections I + r E_12 give an injection of its underlying set
        # into GL_n(R). The rank-one case instead detects the unit group,
        # which need not be infinite (e.g. ZZ^×).
        if self.degree() >= 2 and self.coefficient_ring().is_finite() is False:
            return [OwnedGroups().Infinite(), *refinements]
        # An infinite field has infinitely many nonzero units. Their
        # diagonal matrices give an infinite subgroup even in rank one;
        # this implication does not extend to arbitrary infinite rings.
        if (
            self.degree() >= 1
            and self.coefficient_ring().is_field() is True
            and self.coefficient_ring().is_finite() is False
        ):
            return [OwnedGroups().Infinite(), *refinements]
        return [OwnedGroups(), *refinements]

    def an_object(self):
        return self()

    def _call_(self):
        from sage.groups.matrix_gps.catalog import GL

        ring = self.coefficient_ring()
        return _own_group(
            GL(self.degree(), _engine_ring(ring)),
            refinements=(self,), linear_data=(ring, self.degree()),
        )

    class ParentMethods:
        def __init__(self, selected_linear_data=None, **rest):
            self._selected_linear_data = selected_linear_data
            super().__init__(**rest)

        def coefficient_ring(self):
            return self._selected_linear_data[0]

        def degree(self):
            return self._selected_linear_data[1]

class CoxeterGroups(OwnedCategory):
    r"""The Coxeter group defined by the actual selected Coxeter matrix."""

    def __init__(self, coxeter_matrix):
        from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix
        from dzack_research.preamble.categories.coxeter_diagrams import _engine_coxeter_matrix_of
        from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily

        # Category placement asserts that the datum is a Coxeter matrix,
        # not merely a square array. Validate that law at category ingress,
        # retaining the caller's exact datum for its mathematical identity.
        self._engine_coxeter_matrix = (
            _engine_coxeter_matrix_of(coxeter_matrix)
            if isinstance(coxeter_matrix, IndexedFamily)
            else CoxeterMatrix(coxeter_matrix)
        )
        self._coxeter_matrix = coxeter_matrix
        super().__init__()

    def coxeter_matrix(self):
        # The retained datum may be a mutable list. A category cannot
        # continue to claim a different Coxeter matrix after its defining
        # representation was selected; this check belongs on the category
        # accessor too, not only on its group constructor and group accessor.
        from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix
        from dzack_research.preamble.categories.coxeter_diagrams import _engine_coxeter_matrix_of
        from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily

        current = (
            _engine_coxeter_matrix_of(self._coxeter_matrix)
            if isinstance(self._coxeter_matrix, IndexedFamily)
            else CoxeterMatrix(self._coxeter_matrix)
        )
        if current != self._engine_coxeter_matrix:
            raise ValueError("the chosen Coxeter matrix changed after category construction")
        return self._coxeter_matrix

    def super_categories(self):
        # Check that the retained defining data have not been mutated.
        self.coxeter_matrix()
        # Sage's CoxeterMatrix owns the diagram classification, including
        # reducible systems, exceptional finite types and affine systems.
        # Its is_finite() returns True for certified finite type and False
        # otherwise; False need not certify infinitude (unknown type).
        finite = self._engine_coxeter_matrix.is_finite()
        indices = tuple(self._engine_coxeter_matrix.index_set())
        commutative = all(
            self._engine_coxeter_matrix[left, right] == 2
            for left, right in combinations(indices, 2)
        )
        categories = [OwnedGroups().FinitelyPresentedAsGroup()]
        if finite is True:
            categories.append(OwnedGroups().Finite())
        elif (
            self._engine_coxeter_matrix.is_affine() is True
            or any(self._engine_coxeter_matrix[left, right] in (-1, infinity)
                   for left, right in combinations(indices, 2))
            or any(
                sum((QQ(1) / ZZ(self._engine_coxeter_matrix[left, right])
                     for left, right in combinations(triple, 2)), QQ(0)) <= 1
                for triple in combinations(indices, 3)
                if all(self._engine_coxeter_matrix[left, right] > 0
                       for left, right in combinations(triple, 2))
            )
        ):
            # These are positive witnesses for infinite standard parabolic
            # subsystems; the negative answer from is_finite() alone is not.
            categories.append(OwnedGroups().Infinite())
        if commutative:
            # Commuting Coxeter involutions give (C2)^rank, including
            # the empty diagram. This also independently proves finiteness.
            categories.extend((OwnedGroups().Commutative(), OwnedGroups().Finite()))
        return _distinct_supercategories(categories)

    def an_object(self):
        return self()

    def _call_(self):
        # The Coxeter matrix realization exposes the Coxeter presentation
        # and its generating reflections at the existing engine adapter.
        # The catalogue's default reflection realization need not carry
        # those presentation data even when the abstract group is the same.
        # Validate through the category's mathematical datum accessor.
        selected_matrix = self.coxeter_matrix()
        return _Coxeter(
            self._engine_coxeter_matrix, implementation="matrix",
            refinements=(self,), selected_matrix=selected_matrix,
        )

    class ParentMethods:
        def __init__(self, selected_coxeter_matrix=None, **rest):
            self._selected_coxeter_matrix = selected_coxeter_matrix
            super().__init__(**rest)

        def coxeter_matrix(self):
            r"""The chosen Coxeter datum, provided it still defines this group.

            The engine was constructed from a matrix snapshot. A caller can
            subsequently mutate a list used as the chosen matrix; returning
            that altered list as the group's defining matrix would assert a
            different Coxeter presentation without changing the group.
            """
            from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix
            from dzack_research.preamble.categories.coxeter_diagrams import _engine_coxeter_matrix_of
            from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily

            chosen = self._selected_coxeter_matrix
            current = (
                _engine_coxeter_matrix_of(chosen)
                if isinstance(chosen, IndexedFamily)
                else CoxeterMatrix(chosen)
            )
            if current != _engine_group(self).coxeter_matrix():
                raise ValueError("the chosen Coxeter matrix changed after group construction")
            return self._selected_coxeter_matrix


class FreeGroupQuotients(OwnedCategory):
    r"""Groups presented by a chosen free group and finite relators."""

    def __init__(self, free_group, relators):
        self._free_group = _owned_group(free_group)
        # Check the mathematical finite-generation requirement before
        # requiring Sage's finite-rank FreeGroup_class engine. Indexed free
        # groups on infinite bases use a different backend representation.
        if self._free_group in GroupsWithChosenFreeBasis():
            if self._free_group.free_basis() not in FiniteSets():
                raise ValueError("a finite group presentation requires a finite free basis")
        assert isinstance(_engine_group(self._free_group), FreeGroup_class), (
            "a free-group quotient requires an actual free group, not merely "
            "a group equipped with a chosen generating set"
        )
        assert self._free_group in GroupsWithChosenFreeBasis(), (
            "the free source must retain its chosen free basis"
        )
        # A finite relator family alone does not give a finite presentation:
        # the free generating set must also be finite. In particular a
        # quotient of F(NN) by finitely many relations is not thereby an
        # object of GroupsWithChosenFinitePresentation().
        self._relators = tuple(self._free_group(relator) for relator in relators)
        super().__init__()

    def free_group(self):
        return self._free_group

    def relators(self):
        return self._relators

    def super_categories(self):
        return [GroupsWithChosenFinitePresentation()]

    def an_object(self):
        return self()

    def _call_(self):
        source = self.free_group()
        return _engine_quotient_by_relators(source, self.relators(), quotient_category=self)

class GroupsWithChosenFinitePresentation(OwnedCategory):
    """Finitely presented groups with a chosen finite presentation."""

    def an_object(self):
        r"""The cyclic group of order two, with its chosen presentation."""
        free = Groups.Free(1)
        generator = next(iter(free.group_generators()))
        return free.quotient_by_relators((generator * generator,))

    def super_categories(self):
        return [
            OwnedGroups().FinitelyPresentedAsGroup(),
        ]

    class ParentMethods:
        def descend_homomorphism(self, source_map):
            r"""The unique descent of a map killing the chosen presentation relations.

            Every chosen presentation gives ``F -> G`` and the same
            universal property, regardless of which engine built ``G``.
            """
            projection = self.quotient_projection()
            source = projection.domain()
            if source_map.domain() is not source:
                raise ValueError("presentation descent requires the chosen free-group source")
            target = source_map.codomain()
            if any(source_map(relator) != target.one() for relator in self.defining_relations()):
                raise ValueError("the map does not kill all defining relators")
            # The presentation projection, rather than an identity test on
            # enumeration objects, determines the generator correspondence.
            # Different but isomorphic index presentations still define the
            # same universal factorization when their projection is chosen.
            labels = source.free_basis()
            generator_images = {}
            for label in labels:
                generator = source.free_generator(label)
                image = projection(generator)
                target_image = source_map(generator)
                # A presentation may have redundant generators. Distinct
                # free generators can project to the same group element;
                # the induced map must assign equal values to both, rather
                # than silently retaining the last dictionary entry.
                if image in generator_images and generator_images[image] != target_image:
                    raise ValueError(
                        "the proposed descent assigns incompatible images to equal quotient generators"
                    )
                generator_images[image] = target_image
            if not all(generator in generator_images for generator in self.group_generators()):
                raise ValueError("the chosen presentation projection does not cover the quotient generators")
            # The quotient's engine generator presentation may differ from
            # its chosen free-source presentation. Validate the induced
            # images against the former as well: a mere dictionary of
            # images does not by itself establish a group homomorphism.
            descended = self.Mor(target)(
                generator_images, check=True
            )
            # The factorization equation is a statement about actual Mor
            # composition, not just the engine's chosen presentation.
            # It suffices to check it on the chosen free basis: the
            # presenting group is free on precisely those generators.
            if any(
                descended(projection(source.free_generator(label)))
                != source_map(source.free_generator(label))
                for label in labels
            ):
                raise ValueError(
                    "the represented quotient generators do not implement "
                    "the selected presentation projection"
                )
            return descended

        def quotient_projection(self):
            r"""The presentation epimorphism from the selected free group.

            Every group with a chosen finite presentation carries this
            arrow, not only quotients constructed by FreeGroupQuotients.
            Its actual endpoints and images belong to the selected
            presentation resolution.
            """
            return self.selected_group_resolution().augmentation()

        def __init__(
            self,
            group_presentation_source=None,
            group_presentation_relations=None,
            presentation_source_group=None,
            **rest,
        ) -> None:
            super().__init__(**rest)
            if group_presentation_relations is None:
                raise ValueError(f"{self} cannot be given a finite presentation without its relators; pass the relators")
            source = self if group_presentation_source is None else group_presentation_source
            _fix_selected_group_presentation(
                self,
                source,
                group_presentation_relations,
            )
            selected_source_group = self if presentation_source_group is None else presentation_source_group
            if selected_source_group is self:
                pass
            else:
                if not selected_source_group.has_selected_group_resolution():
                    raise ValueError(
                        f"{self} cannot be a finite presentation of {selected_source_group}: "
                        f"{selected_source_group} has no chosen generating set to match the presentation's generators"
                    )
                presented_generators = tuple(self.group_generators())
                source_generators = tuple(selected_source_group.group_generators())
                if len(source_generators) != len(presented_generators):
                    raise ValueError(
                        f"{self} cannot be a finite presentation of {selected_source_group}: it has "
                        f"{len(presented_generators)} generators, but {selected_source_group} has {len(source_generators)} chosen generators"
                    )
            self._presentation_source_group = selected_source_group

        def presenting_free_group(self):
            selected = self.selected_group_resolution()
            match selected.truncation():
                case 1:
                    return selected.level(0)
                case _:
                    raise TypeError(
                        f"{self} has no chosen finite presentation: its selected group resolution "
                        f"is truncated in degree {selected.truncation()}"
                    )

        def defining_relations(self):
            r"""The chosen relators, as elements of the presenting free group."""
            selected = self.selected_group_resolution()
            match selected.truncation():
                case 1:
                    return selected.relations()
                case _:
                    raise TypeError(
                        f"{self} has no chosen finite presentation: its selected group resolution "
                        f"is truncated in degree {selected.truncation()}"
                    )

        def presentation_source_group(self):
            r"""Return the exact group for which this presentation was selected."""
            return self._presentation_source_group

        @cached_method
        def presentation_isomorphism(self):
            r"""Return the canonical isomorphism from this presented model to its source group."""
            source = self.presentation_source_group()
            if source is self:
                return OwnedGroups().Core().Mor(self, self).identity()
            source_generators = tuple(source.group_generators())
            forward = self.Mor(source)(source_generators)
            inverse = source.Mor(self)(
                dict(
                    zip(
                        source_generators,
                        (forward.lift(generator) for generator in source_generators),
                        strict=True,
                    )
                )
            )
            return OwnedGroups().Core().Mor(self, source)._from_known_inverse_pair(forward, inverse)

class AbelianGroupEndomorphismRings(OwnedCategory):
    r"""The rings ``End(A)`` of endomorphisms of an abelian group ``A``.

    The datum is an abelian group ``A`` in either notation. Its canonical
    endomorphism Mor is the carrier, with its actual maps and endpoints.
    The pointwise abelian law and composition form the already owned
    endomorphism algebra over ``ZZ``; this category owns only the group
    construction and its selected cyclic commutativity decision.
    """

    def an_object(self):
        r"""The endomorphism ring of the additive group of the integers."""
        return self(AdditiveGroups().an_object())

    def _call_(self, group):
        r"""Enrich the actual ``End(A)`` in the notation already carried by A.

        For an additive group, including the additive group of any ring,
        the canonical additive Mor supplies all group homomorphisms;
        no linearity over that ring is imposed. Multiplicative notation
        uses the canonical group Mor. Both branches retain literal
        endpoints and reuse the existing End packet's cached object.
        """
        if group in AdditiveGroups().AdditiveCommutative():
            endomorphisms = AdditiveGroups().AdditiveCommutative().End(group)
        elif group in OwnedGroups().Commutative():
            endomorphisms = OwnedGroups().End(group)
        else:
            raise TypeError(f"an endomorphism ring needs an abelian group, but got {group}")
        if endomorphisms not in self:
            refine(endomorphisms, self)
        return endomorphisms

    def super_categories(self):
        from dzack_research.preamble.categories.group.additive_mors import AdditiveEndomorphismRings

        return [AdditiveEndomorphismRings(_own_ring(ZZ))]

    class ParentMethods:
        def _commutativity_decision(self):
            r"""``End(A)`` commutes when ``A`` is cyclic.

            A group on one generator is cyclic; otherwise the answer is the
            proposition that ``End(A)`` is commutative.
            """
            undecided = AtomicProposition("is_commutative", self)
            group = self.domain()
            if group is _own_ring(ZZ):
                return True
            if group not in OwnedGroups() or not group.has_selected_group_resolution():
                return undecided
            generators = group.group_generators().cardinality()
            if generators.is_finite() and int(generators.finite_value()) <= 1:
                return True
            return undecided

        def _repr_(self):
            return f"Endomorphism ring of {self.domain()}"


class Subgroups(OwnedParameterizedCategory):
    r"""Groups represented as a specified subgroup of one ambient owned group.

    The datum is the containing group ``G``; the subgroup's elements are
    elements of ``G``, so the inclusion is the identity on elements.
    """

    @staticmethod
    def __classcall__(cls, supergroup):
        return OwnedParameterizedCategory.__classcall__(cls, _owned_group(supergroup))

    def parameter_category(self):
        r"""A subgroup is a subgroup of one group, so the parameter is a group."""
        return OwnedGroups()

    def an_object(self):
        r"""The trivial subgroup, generated by nothing."""
        return self.supergroup().subgroup(())

    def supergroup(self):
        return self.base()

    def super_categories(self):
        return [OwnedGroups()]

    @classmethod
    def _repr_object_names(cls):
        return "subgroups"

    class ParentMethods:
        def __init__(self, supergroup, **rest) -> None:
            self._supergroup = supergroup
            super().__init__(facade=supergroup, **rest)

        def supergroup(self):
            return self._supergroup

        @cached_method
        def inclusion(self):
            return _canonical_subgroup_inclusion(self)

        def index(self):
            r"""``[G : H]``, the cardinality of the left-coset space ``G/H``."""
            return self.supergroup().left_cosets(self).cardinality()

        def image_under(self, morphism, *, index_bound=None, ambient_generators=None):
            r"""Image subgroup along a map of the specified ambient group.

            The image is generated by mapped subgroup generators, including
            Schreier generators of represented finite-index preimages. A
            general predicate alone does not supply a generating family.
            An explicit finite-index bound enables the predicate subgroup's
            coset-enumeration route even without a quotient morphism.
            ``ambient_generators`` supplies generators of the whole ambient
            group when its selected resolution is unavailable.

            EXAMPLES::

                sage: A, B = Groups.C(4), Groups.C(2)
                sage: a, b = A.group_generators()[0], B.group_generators()[0]
                sage: f = A.Mor(B)({a: b})
                sage: A.subgroup((a*a,)).image_under(f).cardinality() == 1
                True
                sage: f.preimage_subgroup(B.subgroup(())).image_under(f).cardinality() == 1
                True
                sage: G = Groups.S(3)
                sage: t = G((1, 2))
                sage: f = G.Mor(G)({g: g for g in G.group_generators()})
                sage: P = f.preimage_subgroup(G.subgroup((t,)))
                sage: P.image_under(f).cardinality() == 2 and t in P.image_under(f)
                True
                sage: H = G.subgroup((t,))
                sage: P = G.predicate_subgroup(lambda g: g in H, "transposition subgroup")
                sage: P.image_under(f, index_bound=3).cardinality() == 2
                True
                sage: F, C = Groups.Free(1), Groups.C(2)
                sage: h = C.group_generators()[0]
                sage: reduction = F.Mor(C)({next(iter(F.free_basis())): h})
                sage: parity = F.predicate_subgroup(lambda g: reduction(g) == C.one(), "parity kernel")
                sage: parity.image_under(reduction, index_bound=2).cardinality() == 1
                True
            """
            if morphism.domain() is not self.supergroup():
                raise ValueError("a subgroup image requires a morphism of its containing group")
            match self:
                case _ if self in GeneratedSubgroups(self.supergroup()):
                    generators = self.selected_subgroup_generators()
                case _ if self in OwnedFiniteGroups():
                    generators = tuple(self)
                case _ if hasattr(self, "schreier_generators"):
                    generators = self.schreier_generators(generators=ambient_generators)
                case _ if index_bound is not None and hasattr(self, "finite_index_schreier_generators"):
                    generators = self.finite_index_schreier_generators(index_bound=index_bound, generators=ambient_generators)
                case _:
                    raise ValueError("the subgroup image needs a generating family or a finite-index Schreier construction")
            return morphism.codomain().subgroup(tuple(morphism(g) for g in generators))


class GeneratedSubgroups(OwnedParameterizedCategory):
    r"""Subgroups equipped with the selected family used to generate them.

    The map from the free group on that set is the selected generating
    epimorphism. Its generator images are the supplied elements of the
    supergroup, not a new generating set chosen by the engine.
    """

    @staticmethod
    def __classcall__(cls, supergroup):
        return OwnedParameterizedCategory.__classcall__(cls, _owned_group(supergroup))

    def parameter_category(self):
        return OwnedGroups()

    def an_object(self):
        return self.base().subgroup(())

    def super_categories(self):
        return [Subgroups(self.base())]

    @classmethod
    def _repr_object_names(cls):
        return "generated subgroups"

    class ParentMethods:
        def __init__(self, selected_subgroup_generators, **rest) -> None:
            self._selected_subgroup_generators = selected_subgroup_generators
            super().__init__(**rest)
            labels = selected_subgroup_generators
            source = Groups.Free(index_set=labels)
            generator_morphism = Sets().Mor(labels, self)(lambda generator: self(generator))
            _fix_selected_group_resolution_data(
                self, source, labels, generator_morphism
            )

        def selected_subgroup_generators(self):
            return self._selected_subgroup_generators

        def membership_decision(self, candidate, *, word=None):
            r"""Membership certified by a word in the selected free generators.

            When no word is supplied, a general infinite matrix-subgroup
            membership question remains an unevaluated proposition.
            """
            ambient = self.supergroup()
            if candidate not in ambient:
                return False
            if word is not None:
                free = self.selected_group_resolution().level(0)
                labels = self.selected_subgroup_generators()
                generating_map = free.Mor(ambient)(
                    Sets().Mor(labels, ambient)(lambda generator: generator)
                )
                product = generating_map(free(word))
                if product == candidate:
                    return True
                if ambient.is_finite() is True:
                    return _engine_subgroup_admits(self, candidate)
                return AtomicProposition("is_member", candidate, self)
            if candidate == ambient.one() or any(
                candidate == generator or candidate == ~generator
                for generator in self.selected_subgroup_generators()
            ):
                return True
            if ambient.is_finite() is True:
                return _engine_subgroup_admits(self, candidate)
            return AtomicProposition("is_member", candidate, self)


def _coxeter_presentation(coxeter_matrix, names=None):
    r"""The Coxeter presentation ``<s_i | (s_i s_j)^{m_ij} = 1>`` of a Coxeter matrix.

    A pair with ``m_ij = infinity`` (encoded ``-1`` by Sage) imposes no relation.
    """
    from sage.groups.free_group import FreeGroup

    indices = tuple(coxeter_matrix.index_set())
    free = FreeGroup(len(indices) if names is None else names)
    generators = free.gens()
    squares = tuple(generator**2 for generator in generators)
    bonds = (
        (i, j, coxeter_matrix[indices[i], indices[j]])
        for i, j in combinations(range(len(indices)), 2)
    )
    braids = tuple(
        (generators[i] * generators[j]) ** ZZ(bond)
        for i, j, bond in bonds
        if bond is not infinity and bond != -1
    )
    return free, squares + braids


Groups = groups = OwnedGroups


def FinitelyGeneratedGroups():
    r"""The category of finitely generated groups."""
    return OwnedGroups().FinitelyGeneratedAsMagma()


def FinitelyPresentedGroups():
    r"""The category of finitely presented groups."""
    return OwnedGroups().FinitelyPresentedAsGroup()


def FiniteGroups():
    r"""The category of finite groups."""
    return OwnedGroups().Finite()


def InfiniteGroups():
    r"""The category of infinite groups."""
    return OwnedGroups().Infinite()


def AbelianGroups():
    r"""The category of abelian groups."""
    return OwnedGroups().Commutative()


def FiniteAbelianGroups():
    r"""The category of finite abelian groups.

    One category cut out by two axioms, not a third class beside them.
    """
    return OwnedGroups().Commutative().Finite()


OwnedFiniteGroups = FiniteGroups
OwnedInfiniteGroups = InfiniteGroups
OwnedAbelianGroups = AbelianGroups
OwnedFiniteAbelianGroups = FiniteAbelianGroups
OwnedFinitelyGeneratedGroups = FinitelyGeneratedGroups
OwnedFinitelyPresentedGroups = FinitelyPresentedGroups
