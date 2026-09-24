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
from sage.structure.element import Element, MultiplicativeGroupElement, RingElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    CategoryPacketMethods,
    EndCategoryConstruction,
    MorCategoryConstruction,
    IsoCategoryConstruction,
    _category_mor_parent,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
    OwnedParameterizedCategory,
    _fix_selected_framing,
)
from dzack_research.preamble.categories.group.magmas import (
    AdditiveGroups,
    Monoids,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    MatrixSpaces,
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
from dzack_research.preamble.categories.sets.set_categories import FiniteSets, Sets, finite_ordinal_set
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom
from dzack_research.preamble.refine import realize_owned_category, refine

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
# ``_from_subgroup_engine(engine_element)``.  Implementers:
# :class:`_GroupEngine`, selected privately at ``OwnedGroups``, and the
# lattice orthogonal group and torsion-form orthogonal group on their Mor
# parents.  Callers: the adapters in this section and the class-function,
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
    r"""Return ``True``/``False`` when Sage's category already decides finiteness, else ``Unknown``."""
    if engine in SageFiniteGroups():
        return True
    if engine.category().is_subcategory(SageGroups().Infinite()):
        return False
    return Unknown


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
    match group:
        case _ if group in GroupAutomorphismGroups():
            return group._subgroup_from_engine(gap_subgroup)
        case _:
            engine = _engine_group(group)
            match engine:
                case PermutationGroup_generic() | ParentLibGAP():
                    return _transported_subgroup(group, engine._subgroup_constructor(gap_subgroup))
                case _:
                    assert False, f"a GAP subgroup cannot be read as a subgroup of {group}: this is possible only for permutation groups and GAP-based groups"


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
    return subgroup.supergroup()._to_engine(element) in _engine_group(subgroup)


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

    A Galois group acts on its field by automorphisms; any other permutation
    group acts on the points it permutes, and fixes every other point.
    """
    engine = _engine_group(group)
    match engine:
        case SageGaloisGroup():
            field = _own_ring(engine.number_field())
            assert point in field, f"{group} acts on the field {field} by automorphisms, but {point} is not an element of {field}"
            return _owned_engine_element(field, backend_element.as_mor()(_engine_element(field, point)))
        case PermutationGroup_generic():
            engine_point = _engine_point(engine, point)
            if engine_point not in engine.domain():
                return point
            return _owned_point(backend_element(engine_point))
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
        case FreeGroup_class() | FinitelyPresentedGroup():
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
        case FreeGroup_class() | FinitelyPresentedGroup():
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


class _SelectedGroupPresentation:
    r"""The chosen free source and relators defining one presented group."""

    def __init__(self, free_group, relations) -> None:
        self._free_group = free_group
        self._relations = relations

    def free_group(self):
        return self._free_group

    def relations(self):
        return self._relations


def _group_framing_morphism(group, source, labels, generator_morphism):
    r"""Realize one selected set-of-generators map as the induced group morphism."""
    assert source.free_basis() is labels, (
        f"the free group {source} does not have {labels} as its free basis, so it cannot map onto {group} by sending the free generators to the elements indexed by {labels}"
    )
    return source.Mor(group)(generator_morphism)


def _fix_selected_group_framing(group, *, free_basis=None) -> None:
    r"""Retain one chosen free-source epimorphism."""
    if free_basis is not None:
        source = group
        labels = free_basis
        generator_morphism = Sets().Mor(labels, group)(group.free_generator)
        _fix_selected_framing(
            group,
            OwnedGroups(),
            source,
            labels,
            lambda: generator_morphism,
            lambda: _group_framing_morphism(
                group, source, labels, generator_morphism
            ),
        )
        return

    generators = _engine_generators(group)
    source = Groups.Free(index_set=generators)
    generator_morphism = Sets().Mor(generators, group)(lambda generator: group(generator))
    _fix_selected_framing(
        group,
        OwnedGroups(),
        source,
        generators,
        lambda: generator_morphism,
        lambda: _group_framing_morphism(
            group, source, generators, generator_morphism
        ),
    )


def _fix_selected_group_presentation(group, source, relations) -> None:
    r"""Install one constructor-selected presentation and its exact framing."""
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
    _fix_selected_framing(
        group,
        OwnedGroups(),
        source,
        labels,
        lambda: generator_morphism,
        lambda: _group_framing_morphism(group, source, labels, generator_morphism),
    )
    group._selected_group_presentation = _SelectedGroupPresentation(
        source,
        finite_ordered_set(tuple(relations)),
    )


def _engine_quotient_by_relators(group, relators):
    r"""Return ``G / <<relators>>`` computed from the engine's presentation."""
    engine = _engine_group(group)
    match engine:
        case FreeGroup_class():
            return _own_group(engine.quotient([group._to_engine(group(relator)) for relator in relators]))
        case FinitelyPresentedGroup():
            # G = F/R and G/<<S>> = F/<<R, S>>, with S lifted to words in F.
            free = engine.free_group()
            relations = list(engine.relations()) + [free(group._to_engine(group(relator)).Tietze()) for relator in relators]
            return _own_group(free.quotient(relations))
        case _:
            assert False, f"the quotient of {group} by the normal closure of {relators} cannot be computed: this is available only for free groups and finitely presented groups"


def _engine_abelianity(engine):
    r"""Whether the engine's structure decides its group abelian, else ``Unknown``.

    ``F_0`` and ``F_1`` are abelian; ``F_n`` for ``n >= 2`` contains two
    noncommuting free generators.  This reads the rank of the represented
    free group and performs no search.
    """
    match engine:
        case FreeGroup_class():
            return engine.ngens() <= 1
        case _:
            return Unknown


# Witnesses read off an engine for the placement of the group it realizes.
# Each is a positive witness: ``False`` means the engine supplied none, never
# that the property fails.


def _is_arithmetic_witness(engine) -> bool:
    match engine:
        case NamedMatrixGroup_generic():
            return engine.base_ring() is ZZ
        case _:
            return False


def _is_abelian_witness(engine) -> bool:
    if engine.category().is_subcategory(SageGroups().Commutative()):
        return True
    match engine:
        case AbelianGroup_class() | AbelianGroup_subgroup():
            return True
        case FreeGroup_class():
            return engine.ngens() <= 1
        case FinitelyPresentedGroup():
            # A bare finite presentation is not a cheap abelianity certificate:
            # Sage/GAP may launch a coset-table computation to decide it.
            return False
        case _ if _engine_finiteness(engine) is True:
            return bool(engine.is_abelian())
        case _:
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


def _is_finitely_generated_witness(engine) -> bool:
    return _engine_finiteness(engine) is True or _has_chosen_generators(engine) or _is_arithmetic_witness(engine)


def _is_finitely_presented_witness(engine) -> bool:
    match engine:
        case FreeGroup_class() | FinitelyPresentedGroup() | CoxeterMatrixGroup() | AbelianGroup_class():
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
        (_has_chosen_generators(engine), OwnedGroups().Framed()),
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
                return value in self.supergroup() and _engine_subgroup_admits(self, value)
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
            case _ if self in GroupsWithChosenFiniteGeneratingSet() and self in OwnedFiniteGroups():
                return f"Group of order {self.cardinality()} generated by {self.group_generators()}"
            case _ if self in GroupsWithChosenFiniteGeneratingSet():
                return f"Group generated by {self.group_generators()}"
            case _:
                return f"Group in {self.category()}"

    def _latex_(self):
        if self._description is not None:
            escaped = self._description.replace("_", r"\_")
            return rf"\text{{{escaped}}}"
        match self:
            case _ if self in GroupsWithChosenFiniteGeneratingSet():
                count = self.group_generators().cardinality()
                return rf"\langle g_1,\ldots,g_{{{count}}}\rangle"
            case _:
                return r"\mathrm{Group}"

    def is_abelian(self):
        match self:
            case _ if self in OwnedAbelianGroups():
                return True
            case _ if self in OwnedFiniteGroups():
                return bool(_gap_model(self).IsAbelian())
            case _:
                return _engine_abelianity(self._engine)

    def is_arithmetic_group(self):
        return True if _is_arithmetic_witness(self._engine) else Unknown


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
        return not self == other

    def __hash__(self):
        return hash((id(self.parent()), self._backend()))

    def is_one(self):
        return bool(self._backend() == _engine_group(self.parent()).one())

    def order(self):
        r"""The order of this element: an integer when finite, else the cardinality of ``<g>``."""
        backend_order = self._backend().order()
        if backend_order == infinity:
            return aleph(0)
        return _owned_engine_element(ZZ, ZZ(backend_order))

    multiplicative_order = order

    def _repr_(self):
        if self.is_one():
            return "1"
        text = _engine_element_text(self.parent(), self._backend())
        if text:
            return text
        return f"element of {self.parent()} of order {self.order()}"

    def _latex_(self):
        if self.is_one():
            return "1"
        text = _engine_element_latex(self.parent(), self._backend())
        if text:
            return text
        return rf"\text{{element of }}{latex(self.parent())}"


def _owned_group(group):
    r"""Return ``group`` after asserting that it is already a preamble group."""
    assert group in OwnedGroups(), f"{group} is not a group of the preamble's category of groups"
    return group


@cached_function(
    key=lambda group, refinements, description, free_basis, presentation_source_group: (
        id(group),
        refinements,
        description,
        id(free_basis),
        id(presentation_source_group),
    )
)
def _own_group(
    group,
    refinements=(),
    description=None,
    free_basis=None,
    presentation_source_group=None,
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
    framing rather than retained a second time.  Sage groups compare
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
                source_engine, backend_relations = _chosen_engine_presentation(group)
                presentation_source = None if source_engine is None else _own_group(source_engine)
                relation_source = presentation_source
                if relation_source is None:
                    owned_relations = finite_ordered_set(())
                else:
                    owned_relations = finite_ordered_set(
                        tuple(
                            relation_source._from_engine(relation)
                            for relation in backend_relations
                        )
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
                    **presentation_data,
                )
            else:
                owned = _object_of(
                    Cat().meet(
                        (*placement, GroupsWithChosenFreeBasis(), OwnedGroups().Framed())
                    ),
                    _engine=(OwnedGroups(), _GroupEngine, _GroupElement),
                    engine=group,
                    description=description,
                    free_basis=free_basis,
                    **presentation_data,
                )
            if free_basis is not None and not _has_chosen_presentation(group):
                _fix_selected_group_framing(owned, free_basis=free_basis)
            elif not _has_chosen_presentation(group) and _has_chosen_generators(group):
                _fix_selected_group_framing(owned)
            return owned


def _transported_subgroup(group, engine_subgroup):
    r"""Return the subgroup of ``group`` computed by ``engine_subgroup``."""
    return _object_of(
        Cat().meet((_owned_group_category(engine_subgroup), Subgroups(group))),
        _engine=(OwnedGroups(), _GroupEngine, _GroupElement),
        engine=engine_subgroup,
        supergroup=group,
    )


def _generated_subgroup(group, engine_subgroup, generators):
    r"""Return the subgroup of ``group`` generated by ``generators``, computed by ``engine_subgroup``."""
    return _object_of(
        Cat().meet(
            (
                _owned_group_category(engine_subgroup),
                GeneratedSubgroups(group),
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
        case Morphism() if (
            hasattr(value.parent(), "base_ring")
            and value.parent() in MatrixSpaces(value.parent().base_ring())
        ):
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

    scalar_ring = ring if ring == 0 else _engine_ring(ring)
    return _own_group(Heisenberg(_group_constructor_argument(degree), scalar_ring))


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


def _Coxeter(data, implementation="reflection", base_ring=None, index_set=None):
    from sage.groups.misc_gps.misc_groups_catalog import CoxeterGroup

    scalar_ring = None if base_ring is None else _engine_ring(base_ring)
    return _own_group(
        CoxeterGroup(
            data,
            implementation=implementation,
            base_ring=scalar_ring,
            index_set=index_set,
        )
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
    assert bool(normal_subgroup.IsNormal(group_model)), (
        f"the quotient of {group} by {normal_subgroup} is not a group: {normal_subgroup} is not a normal subgroup of {group}"
    )
    gap_projection = libgap.NaturalMorphismByNormalSubgroup(
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


class SubgroupInclusion(SetMorphism):
    def is_injective(self):
        return True

    def factor_through_or_none(self, target_inclusion):
        r"""Return the subgroup factor, or None when represented containment fails."""
        if target_inclusion.codomain() is not self.codomain():
            raise ValueError(f"the inclusion of {self.domain()} cannot factor through the inclusion of {target_inclusion.domain()}: they are subgroups of different groups, {self.codomain()} and {target_inclusion.codomain()}")
        source = self.domain()
        target = target_inclusion.domain()
        if source is target:
            return source.Mor(target).identity()
        match source:
            case _ if source in GeneratedSubgroups(self.codomain()):
                witnesses = source.selected_subgroup_generators()
            case _ if source in OwnedFiniteGroups():
                witnesses = source
            case _:
                assert source in GeneratedSubgroups(self.codomain()), (
                    f"cannot decide whether {source} is contained in {target}: {source} has no chosen generating set "
                    f"and is not known to be finite"
                )
        if not all(element in target for element in witnesses):
            return None
        return source.Mor(target)(lambda element: target(element))

    def factor_through(self, target_inclusion):
        factor = self.factor_through_or_none(target_inclusion)
        if factor is None:
            raise ValueError(f"the inclusion of {self.domain()} does not factor through {target_inclusion.domain()}: {self.domain()} is not contained in {target_inclusion.domain()}")
        return factor

    @cached_method
    def _cokernel_data(self):
        r"""Return the quotient by the normal closure of this subgroup image."""
        subgroup = self.domain()
        ambient = self.codomain()
        assert ambient in OwnedFiniteGroups(), (
            f"the cokernel of the inclusion {subgroup} -> {ambient} is computed here only for finite groups, "
            f"and {ambient} is not known to be finite"
        )
        from dzack_research.preamble.categories.group.predicate_subgroups import (
            KernelSubgroups,
            PredicateSubgroups,
        )

        match subgroup:
            case _ if subgroup in KernelSubgroups(ambient):
                subgroup_model = (
                    subgroup.kernel_morphism()._gap_morphism_crossing().Kernel()
                )
            case _:
                assert subgroup not in PredicateSubgroups(ambient), (
                    f"the cokernel of the inclusion {subgroup} -> {ambient} cannot be computed: {subgroup} is defined "
                    f"by a predicate, and is computable here only when it is the kernel of a group homomorphism"
                )
                subgroup_model = _gap_model(subgroup)
        normal_closure = libgap.NormalClosure(_gap_model(ambient), subgroup_model)
        return _finite_group_quotient_by_gap_normal_subgroup(
            ambient,
            normal_closure,
        )

    def cokernel(self):
        return self._cokernel_data()[0]

    def cokernel_projection(self):
        return self._cokernel_data()[1]


def _canonical_subgroup_inclusion(subgroup):
    r"""The inclusion ``H -> G`` of a subgroup whose elements are elements of ``G``."""
    containing_group = subgroup.supergroup()
    return subgroup.Mor(containing_group)._from_realization_rule(
        lambda mor: SubgroupInclusion(mor, containing_group)
    )


class IndexedFreeGroupMorphism(Morphism):
    r"""A morphism out of the free group on a chosen set.

    The universal property of the free group ``F(S)`` makes a group morphism
    ``F(S) -> H`` the same datum as a set map ``S -> H``, which is what this
    morphism stores; it is evaluated on reduced words.  The free group on an
    arbitrary set has no elementwise GAP model, so no GAP morphism is used.
    """

    def __init__(self, parent, generator_morphism) -> None:
        Morphism.__init__(self, parent)
        self._generator_morphism = generator_morphism

    def generator_morphism(self):
        return self._generator_morphism

    def _call_(self, element):
        codomain = self.codomain()
        return reduce(
            mul,
            (
                self.generator_morphism()(index) ** sign
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
                lambda index: morphism(self.generator_morphism()(index))
            )
        )

    def _composition(self, right):
        r"""``self ∘ right`` for a group morphism ``right`` out of a free group, read on its basis.

        Sage's ``Map.__mul__`` has checked that ``right`` is a map into this
        morphism's domain.
        """
        source = right.domain()
        if source not in GroupsWithChosenFreeBasis() or not right.parent().mor_family().base_category().is_subcategory(OwnedGroups()):
            return NotImplemented
        return source.Mor(self.codomain())(
            Sets().Mor(source.free_basis(), self.codomain())(
                lambda index: self(right(source.free_generator(index)))
            )
        )


class _GroupMorRealizationMixin:
    def _from_realization_rule(self, rule):
        r"""Realize a specialized group arrow through this canonical Mor parent."""
        morphism = rule(self)
        assert morphism.parent() is self, (
            f"the rule produced {morphism}, which is not a homomorphism in {self}; it lies in {morphism.parent()}"
        )
        return morphism


class IndexedFreeGroupMor(_GroupMorRealizationMixin, CategoricalMor):
    """The canonical Mor object out of the free group on a chosen set."""

    Element = IndexedFreeGroupMorphism

    def __init__(self, mor_family, domain, codomain) -> None:
        category = Monoids() if domain is codomain else None
        CategoricalMor.__init__(
            self,
            mor_family,
            domain,
            codomain,
            category=category,
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
            case _:
                raise TypeError(f"{images!r} cannot define a homomorphism {self.domain()} -> {self.codomain()}: give the images of the free basis {indices} as a map, a function, or a dictionary")
        return self.element_class(self, generator_morphism)

    def cardinality(self):
        r"""A homomorphism from F(S) is exactly a function S -> H."""
        return cardinal(self.codomain().cardinality()) ** cardinal(self.domain().free_basis().cardinality())

    def _repr_(self):
        return f"Mor({self.domain()}, {self.codomain()})"


class GroupMorphism(Morphism):
    r"""An owned group morphism computed by a private GAP homomorphism."""

    def __init__(self, parent, gap_homomorphism, check=True) -> None:
        Morphism.__init__(self, parent)
        if check:
            assert gap_homomorphism.Source() == _gap_model(self.domain()), (
                f"the GAP homomorphism is not a homomorphism out of {self.domain()}: its source differs from {self.domain()}"
            )
            assert gap_homomorphism.Range() == _gap_model(self.codomain()), (
                f"the GAP homomorphism is not a homomorphism into {self.codomain()}: its range differs from {self.codomain()}"
            )
        self._gap_homomorphism = gap_homomorphism

    def _gap_morphism_crossing(self):
        r"""Return the private GAP realization to the group computation owner."""
        return self._gap_homomorphism

    def __eq__(self, other):
        r"""Decide equality on the generators of the source's GAP model."""
        if not isinstance(other, Morphism) or other.parent() is not self.parent():
            return False
        if self is other:
            return True
        source = self.domain()
        return all(
            self(_element_from_engine(source, generator)) == other(_element_from_engine(source, generator))
            for generator in _gap_model(source).GeneratorsOfGroup()
        )

    def __ne__(self, other):
        return not self == other

    def _composition(self, right):
        r"""``self ∘ right`` for a group morphism ``right``, computed on the generators of its source.

        Sage's ``Map.__mul__`` has checked that ``right`` is a map into this
        morphism's domain; a map outside the group Mor is not composed here.
        """
        source = right.domain()
        if source not in OwnedGroups() or not right.parent().mor_family().base_category().is_subcategory(OwnedGroups()):
            return NotImplemented
        if source in GroupsWithChosenFreeBasis():
            return right.postcompose(self)
        backend_generators = _gap_model(source).GeneratorsOfGroup()
        return source.Mor(self.codomain())(
            tuple(
                self(right(_element_from_engine(source, generator)))
                for generator in backend_generators
            )
        )

    def _call_(self, element):
        model = _element_to_engine(self.domain(), element)
        if self.parent()._is_twisted():
            model = model.Inverse()
        return _element_from_engine(
            self.codomain(),
            self._gap_morphism_crossing().Image(model),
        )

    def lift(self, element):
        r"""Return one preimage of ``element``."""
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
        return _subgroup_from_gap(
            self.codomain(),
            self._gap_morphism_crossing().Image(),
        )

    @cached_method
    def _cokernel_data(self):
        r"""Return the quotient of the codomain by the normal closure of the image."""
        codomain = self.codomain()
        assert codomain in OwnedFiniteGroups(), (
            f"the cokernel of {self} is computed here only when the codomain is finite, and {codomain} is not known to be finite"
        )
        normal_closure = libgap.NormalClosure(
            _gap_model(codomain),
            self._gap_morphism_crossing().Image(),
        )
        return _finite_group_quotient_by_gap_normal_subgroup(
            codomain,
            normal_closure,
        )

    def cokernel(self):
        return self._cokernel_data()[0]

    def cokernel_projection(self):
        return self._cokernel_data()[1]

    def is_injective(self):
        return bool(self._gap_morphism_crossing().IsInjective())

    def is_surjective(self):
        return bool(self._gap_morphism_crossing().IsSurjective())


class GroupMor(_GroupMorRealizationMixin, CategoricalMor):
    """The canonical owned ``Mor(G,H)``."""

    Element = GroupMorphism

    @staticmethod
    def __classcall__(cls, family, domain, codomain):
        return typecall(cls, family, domain, codomain)

    def __init__(self, mor_family, domain, codomain, *, category=None):
        placement = []
        if domain is codomain:
            placement.append(Monoids())
        if category is not None:
            placement.append(category)
        CategoricalMor.__init__(
            self,
            mor_family,
            domain,
            codomain,
            category=Cat().meet(tuple(placement)) if placement else None,
        )

    @cached_method
    def _is_twisted(self) -> bool:
        r"""Whether exactly one endpoint multiplies as its engine reversed.

        Then an owned morphism ``Phi`` is an engine anti-morphism; it is
        represented by the engine morphism ``phi(x) = Phi(x^-1)``, and read
        back through inverses.  Asked only where a GAP morphism is evaluated,
        so both endpoints are engine-realized there.
        """
        return _law_reversed(self.domain()) != _law_reversed(self.codomain())

    def _element_constructor_(self, images, check=True, **_options):
        match images:
            case dict():
                return self._from_group_generator_images(images, check=check)
            case GapElement():
                return self._from_gap_homomorphism(images, check=check)
            case Morphism() if images.parent() is self:
                return images
            case tuple() | list():
                return self._from_gap_generator_images(images, check=check)
        raise TypeError(f"unable to convert {images!r} to an element of {self}")

    def _from_finite_elementwise_rule(self, function):
        r"""Admit an elementwise group map by exhaustive verification on a finite domain.

        This is the finite analogue of specifying a map on chosen generators:
        when no framing has been selected, the multiplication table itself is
        a finite determining family.  The resulting arrow is still an element
        of this Mor object; finite enumeration is only its admission algorithm.
        """
        domain = self.domain()
        assert domain.is_finite() is True, (
            f"a function on elements defines a homomorphism {domain} -> {self.codomain()} here only when {domain} is "
            f"finite, so that the homomorphism law can be checked on all pairs of elements; {domain} is not known to be finite"
        )
        morphism = _ElementwiseGroupMorphism(self, function)
        assert all(
            morphism(left * right) == morphism(left) * morphism(right)
            for left in domain
            for right in domain
        ), f"the function does not define a homomorphism {domain} -> {self.codomain()}: it does not preserve multiplication"
        return morphism

    def _from_gap_homomorphism(self, gap_homomorphism, check=True):
        if check:
            assert gap_homomorphism.Source() == _gap_model(self.domain()), (
                f"the GAP homomorphism is not a homomorphism out of {self.domain()}: its source differs from {self.domain()}"
            )
            assert gap_homomorphism.Range() == _gap_model(self.codomain()), (
                f"the GAP homomorphism is not a homomorphism into {self.codomain()}: its range differs from {self.codomain()}"
            )
        return self.element_class(self, gap_homomorphism, check=False)

    def _from_engine_generator_images(self, generator_models, image_models, check=True):
        source = _gap_model(self.domain())
        target = _gap_model(self.codomain())
        if self._is_twisted():
            image_models = [model.Inverse() for model in image_models]
        if not check:
            engine = libgap.GroupHomomorphismByImagesNC(source, target, generator_models, image_models)
            return self.element_class(self, engine, check=False)
        engine = libgap.GroupHomomorphismByImages(source, target, generator_models, image_models)
        if engine.is_bool():
            raise ValueError(f"the given images do not define a homomorphism {self.domain()} -> {self.codomain()}: they do not satisfy the relations of {self.domain()}")
        return self.element_class(self, engine, check=False)

    def _from_group_generator_images(self, images, check=True):
        domain = self.domain()
        codomain = self.codomain()
        if domain not in OwnedGroups().Framed():
            raise TypeError(
                f"a homomorphism out of {domain} cannot be given by images of generators: {domain} has no chosen generating set"
            )
        generators = domain.group_generators()
        if not (all(generator in images for generator in generators) and all(key in generators for key in images)):
            raise ValueError(f"the dictionary does not define a homomorphism out of {domain}: its keys must be exactly the chosen generators {generators} of {domain}, but they are {tuple(images)}")
        return self._from_engine_generator_images(
            [_element_to_engine(domain, generator) for generator in generators],
            [_element_to_engine(codomain, codomain(images[generator])) for generator in generators],
            check=check,
        )

    def _from_gap_generator_images(self, images, check=True):
        r"""Images listed in the order of the GAP model's own generators."""
        codomain = self.codomain()
        return self._from_engine_generator_images(
            list(_gap_model(self.domain()).GeneratorsOfGroup()),
            [_element_to_engine(codomain, codomain(image)) for image in images],
            check=check,
        )

    @cached_method
    def cardinality(self):
        r"""Return the exact number of homomorphisms between finite endpoints."""
        domain = self.domain()
        codomain = self.codomain()
        assert domain in OwnedFiniteGroups() and codomain in OwnedFiniteGroups(), (
            f"the number of homomorphisms {domain} -> {codomain} is computed here only when both groups are finite, "
            f"and {domain} or {codomain} is not known to be finite"
        )
        homomorphisms = libgap.AllHomomorphisms(
            _gap_model(domain),
            _gap_model(codomain),
        )
        return cardinal(int(homomorphisms.Length()))

    def _repr_(self):
        return f"Mor({self.domain()}, {self.codomain()})"


class GroupAutomorphism(GroupMorphism):
    def _composition(self, right):
        r"""Compose automorphisms inside their represented automorphism group."""
        if right.parent() is self.parent():
            return self.parent()(
                right._gap_morphism_crossing() * self._gap_morphism_crossing(),
                check=False,
            )
        return super()._composition(right)


class GroupAutomorphismGroups(OwnedCategory):
    r"""Automorphism groups ``Aut(G)`` computed by GAP, and their subgroups.

    The datum is the group ``G`` whose automorphisms are the elements, held by
    the Mor object, together with the GAP subgroup of ``Aut(G)`` when the
    object is a proper subgroup.
    """

    def super_categories(self):
        return [OwnedGroups()]

    class ParentMethods:
        @cached_method
        def _libgap_(self):
            if self._engine_subgroup is not None:
                return self._engine_subgroup
            return _automorphism_gap_model(self.domain())

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
            return self._supergroup

        def cardinality(self):
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
            return super().cardinality()

        def _repr_(self):
            if self._engine_subgroup is not None:
                return f"Subgroup of Aut({self.domain()})"
            return f"Aut({self.domain()})"

    class ElementMethods:
        def inverse(self):
            return self.parent()(
                self._gap_morphism_crossing().InverseGeneralMapping(),
                check=False,
            )

        def _composition_(self, right, mor):
            assert right.parent() is self.parent(), f"cannot compose {self} with {right}: they are automorphisms of different groups, in {self.parent()} and {right.parent()}"
            return self.parent()(
                right._gap_morphism_crossing() * self._gap_morphism_crossing(),
                check=False,
            )


class GroupAutomorphismGroup(GroupMor):
    Element = GroupAutomorphism

    @staticmethod
    def __classcall__(cls, mor_family, group, engine_subgroup=None, supergroup=None):
        return typecall(cls, mor_family, group, engine_subgroup=engine_subgroup, supergroup=supergroup)

    def __init__(self, mor_family, group, engine_subgroup=None, supergroup=None):
        self._engine_subgroup = engine_subgroup
        self._supergroup = self if supergroup is None else supergroup
        categories = [GroupAutomorphismGroups()]
        if group.is_finite() is True:
            categories.extend((OwnedFiniteGroups(), OwnedGroups().Framed()))
        GroupMor.__init__(
            self,
            mor_family,
            group,
            group,
            category=Cat().meet(tuple(categories)),
        )
        if group.is_finite() is True:
            backend_generators = tuple(self._libgap_().GeneratorsOfGroup())
            generators = finite_ordered_set(
                tuple(self(generator, check=False) for generator in backend_generators)
            )
            source = Groups.Free(index_set=generators)
            generator_morphism = Sets().Mor(generators, self)(lambda generator: generator)
            _fix_selected_framing(
                self,
                OwnedGroups(),
                source,
                generators,
                lambda: generator_morphism,
                lambda: _group_framing_morphism(
                    self, source, generators, generator_morphism
                ),
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
        return supers

    def identity(self):
        return self(libgap.IdentityMapping(_gap_model(self.domain())), check=False)

    one = identity
    identity_automorphism = identity

    def _element_constructor_(self, images, check=True, **options):
        match images:
            case GapElement():
                automorphism = self.element_class(self, images, check=False)
            case _:
                automorphism = super()._element_constructor_(images, check=check, **options)
        if check and not bool(
            automorphism._gap_morphism_crossing().IsBijective()
        ):
            raise ValueError(f"{images} does not define an element of {self}: the homomorphism is not bijective")
        return automorphism

    def _subgroup_from_engine(self, engine_subgroup):
        return GroupAutomorphismGroup(
            self.mor_family(),
            self.domain(),
            engine_subgroup=engine_subgroup,
            supergroup=self,
        )


class GeneralGroupMor(_GroupMorRealizationMixin, CategoricalMor):
    r"""The owned group Mor for endpoints without a selected GAP realization.

    Specialized morphism constructions (for example profinite restriction maps
    and characters) parent their arrows here directly.  This Mor does not
    manufacture a group map from arbitrary literals when no representation-
    specific constructor has been selected.
    """

    Element = Morphism

    def __init__(self, mor_family, domain, codomain) -> None:
        category = Monoids() if domain is codomain else None
        CategoricalMor.__init__(
            self, mor_family, domain, codomain, category=category
        )

    def _element_constructor_(self, datum):
        match datum:
            case Morphism() if datum.parent() is self:
                return datum
            case _:
                assert False, (
                    f"{datum} cannot be made a homomorphism {self.domain()} -> {self.codomain()}: homomorphisms "
                    f"between these groups are constructed only by specific constructions (restriction maps, characters)"
                )

    def identity(self):
        assert self.domain() is self.codomain(), f"there is no identity homomorphism {self.domain()} -> {self.codomain()}: the domain and codomain differ"
        domain = self.domain()
        return _ElementwiseGroupMorphism(self, lambda element: domain(element))


class _ElementwiseGroupMorphism(Morphism):
    r"""Private elementwise realization used only when the group law supplies the map."""

    def __init__(self, parent, function) -> None:
        self._function = function
        Morphism.__init__(self, parent)

    def _call_(self, element):
        return self.codomain()(self._function(self.domain()(element)))

    def _in_mor(self, mor):
        return _ElementwiseGroupMorphism(mor, self._function)


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

        def FinitelyGeneratedAsMagma(self) -> Category:
            r"""Return this category with the axiom that some finite subset generates."""
            return self._with_axiom("FinitelyGeneratedAsMagma")

        def FinitelyGenerated(self) -> Category:
            r"""Sage's shorthand for :meth:`FinitelyGeneratedAsMagma`."""
            return self.FinitelyGeneratedAsMagma()

        def FinitelyPresentedAsGroup(self) -> Category:
            r"""Return this category with the axiom that some finite presentation exists."""
            return self._with_axiom("FinitelyPresentedAsGroup")

        def FinitelyPresented(self) -> Category:
            r"""Shorthand for :meth:`FinitelyPresentedAsGroup`."""
            return self.FinitelyPresentedAsGroup()

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

            embeddings = tuple(
                libgap.Embedding(coproduct_engine, position)
                for position in range(1, len(labels) + 1)
            )
            target_category = OwnedGroups()
            diagram = _discrete_diagram(family, target_category)

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

        def cyclic_subgroup(self):
            r"""Return the literal cyclic subgroup generated by this element."""
            from dzack_research.preamble.categories.group.cyclic_subgroups import (
                CyclicGroups,
            )

            return CyclicGroups()(self)

    class ParentMethods:
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

        def is_finite(self):
            return Unknown

        def is_abelian(self):
            match self:
                case _ if self in OwnedAbelianGroups():
                    return True
                case _ if self in OwnedFiniteGroups():
                    return all(left * right == right * left for left in self for right in self)
                case _:
                    return Unknown

        def is_finitely_generated(self):
            if self in OwnedGroups().FinitelyGeneratedAsMagma():
                return True
            return Unknown

        def is_finitely_presented(self):
            return True if self in OwnedGroups().FinitelyPresentedAsGroup() else Unknown

        def is_arithmetic_group(self):
            return Unknown

        def cardinality(self):
            if self in OwnedFiniteGroups():
                return cardinal(_finite_order(self))
            if self in GroupsWithChosenFreeBasis():
                basis_cardinality = self.free_basis().cardinality()
                if basis_cardinality == cardinal(0):
                    return cardinal(1)
                return Cardinalities().supremum(aleph(0), basis_cardinality)
            if self in OwnedInfiniteGroups() and self in OwnedGroups().FinitelyGeneratedAsMagma():
                return aleph(0)
            assert False, (
                f"the cardinality of {self} is not computed here: it is computed only for finite groups, free groups, "
                f"and infinite finitely generated groups, and {self} is not known to be any of these; "
                f"{self} is in {self.category()}"
            )

        def order(self):
            r"""The set cardinality, read as an integer when finite."""
            size = cardinal(self.cardinality())
            match size.is_finite():
                case True:
                    return _own_ring(ZZ)(int(size.finite_value()))
                case False:
                    return size

        def order_is_invertible_in(self, ring) -> bool:
            r"""Return whether ``|G|`` is a unit in ``ring`` for this finite group."""
            assert self in OwnedFiniteGroups(), (
                f"cannot decide whether the order of {self} is a unit in {ring}: {self} is not known to be finite"
            )
            return bool(ring(int(self.order())).is_unit())

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
            """
            if generators is None:
                assert self in OwnedGroups().Framed(), (
                    f"the image of {self} under {image} cannot be enumerated: {self} has no chosen generating set; "
                    f"pass generators explicitly"
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
            image_bound = int(image_bound)
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

        @cached_method
        def center(self):
            r"""Return the center as an owned subgroup in the represented finite case."""
            assert self in OwnedFiniteGroups(), (
                f"the center of {self} is computed here only for finite groups, and {self} is not known to be finite"
            )
            return _subgroup_from_gap(self, _gap_model(self).Center())

        @cached_method
        def commutator_subgroup(self):
            r"""Return ``[G,G]`` as the represented derived subgroup when finite."""
            assert self in OwnedFiniteGroups(), (
                f"the commutator subgroup of {self} is computed here only for finite groups, and {self} is not known to be finite"
            )
            return _subgroup_from_gap(self, _gap_model(self).DerivedSubgroup())

        derived_subgroup = commutator_subgroup

        @cached_method
        def subgroups(self):
            r"""Return the represented subgroups as an owned finite ordered set.

            GAP owns exact subgroup enumeration for finite groups whose elements
            are represented by its group model.  Each enumerated subgroup is
            raised through the existing transported-subgroup constructor, so the
            ambient group and canonical inclusion remain the same owned data used
            by ``subgroup(...)`` and the subgroup categories.
            """
            assert self in OwnedFiniteGroups(), (
                f"the subgroups of {self} are listed here only for finite groups, and {self} is not known to be finite"
            )
            return finite_ordered_set(
                tuple(
                    _subgroup_from_gap(self, subgroup)
                    for subgroup in _gap_model(self).AllSubgroups()
                )
            )

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
            if self.is_finite() is not True or other.is_finite() is not True:
                return Unknown
            found = _gap_model(self).IsomorphismGroups(_gap_model(other))
            return str(found) != "fail"

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
            def is_abelian(self):
                return True

            @cached_method
            def endomorphism_ring(self):
                r"""The ring ``End(A)`` of group endomorphisms, under pointwise sum and composition."""
                return _object_of(AbelianGroupEndomorphismRings(), group=self)

            @cached_method
            def scalar_action(self):

                integers = _own_ring(ZZ)
                endomorphisms = self.endomorphism_ring()
                additive = self.category().is_subcategory(AdditiveGroups().AdditiveCommutative())

                def multiple(exponent, element):
                    return exponent * element if additive else element ** int(exponent)

                return integers.Mor(endomorphisms)(
                    lambda exponent: endomorphisms(lambda element: multiple(exponent, element)),
                )

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
            def is_finite(self):
                return True

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

            @cached_method
            def conjugation_g_set(self):
                r"""The finite ``G``-set ``G`` under conjugation."""
                from dzack_research.preamble.categories.group.g_sets import FiniteGSets

                points = finite_ordered_set(tuple(self))
                return FiniteGSets(self)(
                    points,
                    lambda group_element, point: group_element * point * group_element.inverse(),
                )

            @cached_method
            def conjugacy_classes(self):
                r"""The orbit set of the conjugation action of this finite group."""
                return self.conjugation_g_set().orbits()

            def conjugacy_class(self, representative):
                r"""The actual conjugacy orbit of ``representative``."""
                return self.conjugacy_classes().orbit_of(self(representative))

            def class_function(self, codomain, values, *, representatives=None):
                r"""Return the class function on this finite group with the stated values."""
                from dzack_research.preamble.categories.group.class_functions import (
                    _finite_group_class_function,
                )

                return _finite_group_class_function(
                    self,
                    codomain,
                    values,
                    representatives=representatives,
                )

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
                        self.character_set()(
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
                candidate = self.character_set()(
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
                return self.character_set()(
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

            def left_cosets(self, subgroup):
                r"""Return the set of left cosets ``gH``, each an ordered set of elements."""
                return _engine_cosets(self, subgroup, "left")

            def right_cosets(self, subgroup):
                r"""Return the set of right cosets ``Hg``, each an ordered set of elements."""
                return _engine_cosets(self, subgroup, "right")

    class Infinite(CategoryWithAxiom):
        @classmethod
        def _repr_object_names(cls):
            return "infinite groups"

        class ParentMethods:
            def is_finite(self):
                return False

    class Framed(CategoryWithAxiom):
        r"""Groups carrying the global selected-framing datum in ``Grp``."""

        class ParentMethods:
            def group_generators(self):
                return self.selected_framing_generators(
                    OwnedGroups(),
                    name="Group generators",
                )

            def number_of_group_generators(self):
                return self.selected_framing_generator_count(OwnedGroups())

            def conjugation_morphism(self):
                r"""The morphism ``G -> Aut(G)`` stated on the selected framing generators."""
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

    class FinitelyGeneratedAsMagma(CategoryWithAxiom):
        r"""Groups admitting some finite generating set."""

        def an_object(self):
            r"""The cyclic group of order two."""
            return OwnedGroups().C(2)

        @classmethod
        def _repr_object_names(cls):
            return "finitely generated groups"

        class ParentMethods:
            def is_finitely_generated(self):
                return True

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

        class ParentMethods:
            def is_finitely_presented(self):
                return True

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
                    presentation_source_group=self,
                )



class TopologicalGroups(OwnedCategory):
    r"""Owned groups equipped with a represented compatible topology."""

    def super_categories(self):
        return [OwnedGroups()]

    class ParentMethods:
        def is_topological_group(self) -> bool:
            return True


def GroupsWithChosenFiniteGeneratingSet():
    r"""The global ``Framed`` axiom specialized to owned groups."""
    return OwnedGroups().Framed()


class GroupsWithChosenFreeBasis(OwnedCategory):
    r"""Free groups carrying the chosen set they are free on.

    The datum is the basis ``S``: the group is the free group ``F(S)``, and
    its morphisms out are determined by set maps out of ``S``.
    """

    def super_categories(self):
        return [OwnedGroups()]

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
        def natural_points(self):
            r"""The finite set the group permutes."""
            return finite_ordered_set(tuple(_owned_point(point) for point in _engine_group(self).domain()))

        def action_on(self, points):
            r"""The ``G``-set on ``points`` with the natural action ``g . x = g(x)``."""
            from dzack_research.preamble.categories.group.g_sets import FiniteGSets

            return FiniteGSets(self)(points, lambda group_element, point: group_element(point))

        def natural_g_set(self):
            r"""The natural ``G``-set on the points the group permutes."""
            return self.action_on(self.natural_points())

        def orbit(self, point):
            r"""The orbit ``G . point`` of the natural action."""
            engine = _engine_group(self)
            return finite_ordered_set(tuple(_owned_point(image) for image in engine.orbit(_engine_point(engine, point))))

        def orbits(self, points=None):
            r"""The orbit set of the natural action on ``points`` (all natural points by default)."""
            g_set = self.natural_g_set() if points is None else self.action_on(points)
            return g_set.orbits()

        def stabilizer(self, point):
            r"""The subgroup ``G_x`` fixing ``point``, computed by the permutation engine."""
            engine = _engine_group(self)
            engine_point = _engine_point(engine, point)
            return _subgroup_from_gap(
                self,
                libgap.Stabilizer(_gap_model(self), libgap(engine_point), libgap.OnPoints),
            )

        def is_transitive(self) -> bool:
            r"""Whether the natural action has one orbit."""
            return bool(_engine_group(self).is_transitive())


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
            OwnedGroups().Framed(),
        ]

    class ParentMethods:
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
                if selected_source_group not in OwnedGroups().Framed():
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
            selected = self.__dict__.get("_selected_group_presentation")
            assert selected is not None, (
                f"{self} has no chosen finite presentation, so it has no presenting free group"
            )
            assert selected.free_group() is self.selected_framing_source(OwnedGroups()), (
                f"the presentation of {self} is on the free group {selected.free_group()}, but the chosen generating set "
                f"of {self} is indexed by a different free group; the two must agree"
            )
            return selected.free_group()

        def defining_relations(self):
            r"""The chosen relators, as elements of the presenting free group."""
            selected = self.__dict__.get("_selected_group_presentation")
            assert selected is not None, (
                f"{self} has no chosen finite presentation, so it has no defining relations"
            )
            return selected.relations()

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
            return OwnedGroups().Core().Mor(self, source)(forward, inverse)

        def quotient_by_relators(self, relators):
            r"""Return ``G / <<relators>>``, the quotient by the normal closure of ``relators``."""
            return _engine_quotient_by_relators(self, relators)


class AbelianGroupEndomorphismRings(OwnedCategory):
    r"""The rings ``End(A)`` of endomorphisms of an abelian group ``A``.

    The datum is the group ``A``.  Addition is pointwise, in the group law of
    ``A`` written additively or multiplicatively, and multiplication is
    composition.
    """

    def super_categories(self):
        return [OwnedRings()]

    class ParentMethods:
        def __init__(self, group, **rest) -> None:
            self._group = group
            super().__init__(**rest)

        def domain(self):
            return self._group

        def codomain(self):
            return self._group

        def _is_additive(self) -> bool:
            return self._group.category().is_subcategory(AdditiveGroups().AdditiveCommutative())

        def _sum_values(self, left, right):
            return left + right if self._is_additive() else left * right

        def _negative_value(self, value):
            return -value if self._is_additive() else value**-1

        def _identity_value(self):
            return self._group.zero() if self._is_additive() else self._group.one()

        def _element_constructor_(self, mapping):
            return self.element_class(self, mapping)

        def one(self):
            return self(lambda element: element)

        def zero(self):
            return self(lambda element: self._identity_value())

        def is_commutative(self):
            r"""``End(A)`` commutes when ``A`` is cyclic; a group on one generator is, and otherwise this is not decided here."""
            if self._group not in OwnedGroups().Framed():
                return Unknown
            generators = self._group.group_generators().cardinality()
            if generators.is_finite() and int(generators.finite_value()) <= 1:
                return True
            return Unknown

        def _repr_(self):
            return f"Endomorphism ring of {self._group}"

    class ElementMethods(RingElement):
        r"""One endomorphism, given by its map on the elements of ``A``."""

        def __init__(self, parent, mapping) -> None:
            RingElement.__init__(self, parent)
            self._mapping = mapping

        def __call__(self, element):
            return self._mapping(element)

        def _add_(self, other):
            return self.parent()(lambda element: self.parent()._sum_values(self(element), other(element)))

        def _neg_(self):
            return self.parent()(lambda element: self.parent()._negative_value(self(element)))

        def _mul_(self, other):
            return self.parent()(lambda element: self(other(element)))


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


class GeneratedSubgroups(OwnedParameterizedCategory):
    r"""Subgroups equipped with the selected family used to generate them.

    The map from the free group on that family is the selected framing
    epimorphism. Its generator images are the supplied ambient elements,
    not a new generating family chosen by the engine.
    """

    @staticmethod
    def __classcall__(cls, supergroup):
        return OwnedParameterizedCategory.__classcall__(cls, _owned_group(supergroup))

    def parameter_category(self):
        return OwnedGroups()

    def an_object(self):
        return self.base().subgroup(())

    def super_categories(self):
        return [Subgroups(self.base()), OwnedGroups().Framed()]

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
            _fix_selected_framing(
                self,
                OwnedGroups(),
                source,
                labels,
                generator_morphism,
                lambda: _group_framing_morphism(
                    self, source, labels, generator_morphism
                ),
            )

        def selected_subgroup_generators(self):
            return self._selected_subgroup_generators


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
