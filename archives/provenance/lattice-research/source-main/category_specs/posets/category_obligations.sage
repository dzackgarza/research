import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.cat import Cat
from category_specs.posets import Posets
from category_specs.posets.homsets import PosetAutCategory, PosetEndCategory, PosetHomCategory
from category_specs.posets.subcategories.constructions.objects_over import _ObjectsOver
from category_specs.posets.subcategories.constructions.objects_under import _ObjectsUnder
from category_specs.posets.subcategories.finite import _FinitePosets
from category_specs.posets.subcategories.finite_join_semilattice import _FiniteJoinSemilatticePosets
from category_specs.posets.subcategories.finite_meet_semilattice import _FiniteMeetSemilatticePosets
from category_specs.utils import assert_category_statements


P = Posets()
PC = P.Constructors()
diamond_elements = [0, 1, 2, 3]
diamond_covers = {0: [1, 2], 1: [3], 2: [3], 3: []}
diamond_cover_list = [[1, 2], [3], [3], []]
diamond_relations = [(0, 1), (0, 2), (1, 3), (2, 3)]
diamond_digraph = DiGraph(diamond_covers)
chain_elements = [0, 1, 2]


def diamond_le(a, b):
    return (a | b) == b


def chain_covers_predicate(a, b):
    return b == a + 1


def raw_diamond_poset():
    return Poset(diamond_covers)


diamond_poset = PC.Poset(upper_covers_dict=diamond_covers)
diamond_lattice = PC.LatticePoset(upper_covers=diamond_cover_list)


def abstract_method_has_name(method, name):
    return method.__name__ == name


CATEGORY_STATEMENTS = (
    ("Posets() is an object of Cat()", lambda _: P in Cat()),
    ("Posets().Finite() is an object of Cat()", lambda _: P.Finite() in Cat()),
    ("Posets().Finite() refines the finite poset category", lambda _: issubclass(P.Finite().__class__, _FinitePosets)),
    ("Posets().MeetSemilattice() is an object of Cat()", lambda _: P.MeetSemilattice() in Cat()),
    ("Posets().MeetSemilattice().Finite() is an object of Cat()", lambda _: P.MeetSemilattice().Finite() in Cat()),
    ("Posets().JoinSemilattice() is an object of Cat()", lambda _: P.JoinSemilattice() in Cat()),
    ("Posets().JoinSemilattice().Finite() is an object of Cat()", lambda _: P.JoinSemilattice().Finite() in Cat()),
    ("Posets().Lattice() is an object of Cat()", lambda _: P.Lattice() in Cat()),
    ("Posets().Lattice().Finite() is an object of Cat()", lambda _: P.Lattice().Finite() in Cat()),
    ("Posets().Finite() is a subcategory of Posets()", lambda _: P.Finite().is_subcategory(P)),
    ("Posets().MeetSemilattice() is a subcategory of Posets()", lambda _: P.MeetSemilattice().is_subcategory(P)),
    ("Posets().JoinSemilattice() is a subcategory of Posets()", lambda _: P.JoinSemilattice().is_subcategory(P)),
    ("Posets().Lattice() is a subcategory of Posets()", lambda _: P.Lattice().is_subcategory(P)),
    (
        "Posets().Lattice() is a subcategory of Posets().MeetSemilattice()",
        lambda _: P.Lattice().is_subcategory(P.MeetSemilattice()),
    ),
    (
        "Posets().Lattice() is a subcategory of Posets().JoinSemilattice()",
        lambda _: P.Lattice().is_subcategory(P.JoinSemilattice()),
    ),
    (
        "Posets().MeetSemilattice().Finite() is a subcategory of Posets().MeetSemilattice()",
        lambda _: P.MeetSemilattice().Finite().is_subcategory(P.MeetSemilattice()),
    ),
    (
        "Posets().JoinSemilattice().Finite() is a subcategory of Posets().JoinSemilattice()",
        lambda _: P.JoinSemilattice().Finite().is_subcategory(P.JoinSemilattice()),
    ),
    ("Posets().Lattice().Finite() is a subcategory of Posets().Lattice()", lambda _: P.Lattice().Finite().is_subcategory(P.Lattice())),
    ("Posets().Subobjects() is an object of Cat()", lambda _: P.Subobjects() in Cat()),
    ("Posets().Quotients() is an object of Cat()", lambda _: P.Quotients() in Cat()),
    ("Posets().Subquotients() is an object of Cat()", lambda _: P.Subquotients() in Cat()),
    ("Posets().CartesianProducts() is an object of Cat()", lambda _: P.CartesianProducts() in Cat()),
    ("Posets().HomCategory() is an object of Cat()", lambda _: P.HomCategory() in Cat()),
    ("Poset(hasse_digraph=...) refines to finite posets", lambda _: PC.Poset(hasse_digraph=diamond_digraph) in P.Finite()),
    (
        "Poset(elements=..., relations=...) refines to finite posets",
        lambda _: PC.Poset(elements=diamond_elements, relations=diamond_relations) in P.Finite(),
    ),
    (
        "Poset(elements=..., covers=...) refines to finite posets",
        lambda _: PC.Poset(elements=diamond_elements, covers=diamond_relations) in P.Finite(),
    ),
    ("Poset(elements=..., order_predicate=...) refines to finite posets", lambda _: PC.Poset(elements=diamond_elements, order_predicate=diamond_le) in P.Finite()),
    (
        "Poset(elements=..., cover_predicate=...) refines to finite posets",
        lambda _: PC.Poset(elements=chain_elements, cover_predicate=chain_covers_predicate) in P.Finite(),
    ),
    ("Poset(upper_covers_dict=...) refines to finite posets", lambda _: PC.Poset(upper_covers_dict=diamond_covers) in P.Finite()),
    ("Poset(upper_covers=...) refines to finite posets", lambda _: PC.Poset(upper_covers=diamond_cover_list) in P.Finite()),
    ("Poset(existing=...) refines to finite posets", lambda _: PC.Poset(existing=raw_diamond_poset()) in P.Finite()),
    ("Poset(existing=spec-owned poset) stays inside the category constructor surface", lambda _: PC.Poset(existing=diamond_poset) in P.Finite()),
    (
        "MeetSemilattice(hasse_digraph=...) refines to finite meet-semilattices",
        lambda _: PC.MeetSemilattice(hasse_digraph=diamond_digraph) in P.MeetSemilattice().Finite(),
    ),
    (
        "MeetSemilattice(elements=..., relations=...) refines to finite meet-semilattices",
        lambda _: PC.MeetSemilattice(elements=diamond_elements, relations=diamond_relations) in P.MeetSemilattice().Finite(),
    ),
    (
        "MeetSemilattice(elements=..., covers=...) refines to finite meet-semilattices",
        lambda _: PC.MeetSemilattice(elements=diamond_elements, covers=diamond_relations) in P.MeetSemilattice().Finite(),
    ),
    (
        "MeetSemilattice(elements=..., order_predicate=...) refines to finite meet-semilattices",
        lambda _: PC.MeetSemilattice(elements=diamond_elements, order_predicate=diamond_le) in P.MeetSemilattice().Finite(),
    ),
    (
        "MeetSemilattice(elements=..., cover_predicate=...) refines to finite meet-semilattices",
        lambda _: PC.MeetSemilattice(elements=chain_elements, cover_predicate=chain_covers_predicate) in P.MeetSemilattice().Finite(),
    ),
    (
        "MeetSemilattice(upper_covers_dict=...) refines to finite meet-semilattices",
        lambda _: PC.MeetSemilattice(upper_covers_dict=diamond_covers) in P.MeetSemilattice().Finite(),
    ),
    (
        "MeetSemilattice(upper_covers=...) refines to finite meet-semilattices",
        lambda _: PC.MeetSemilattice(upper_covers=diamond_cover_list) in P.MeetSemilattice().Finite(),
    ),
    (
        "MeetSemilattice(existing=...) refines to finite meet-semilattices",
        lambda _: PC.MeetSemilattice(existing=raw_diamond_poset()) in P.MeetSemilattice().Finite(),
    ),
    (
        "MeetSemilattice(existing=spec-owned poset) stays inside the category constructor surface",
        lambda _: PC.MeetSemilattice(existing=diamond_poset) in P.MeetSemilattice().Finite(),
    ),
    (
        "JoinSemilattice(hasse_digraph=...) refines to finite join-semilattices",
        lambda _: PC.JoinSemilattice(hasse_digraph=diamond_digraph) in P.JoinSemilattice().Finite(),
    ),
    (
        "JoinSemilattice(elements=..., relations=...) refines to finite join-semilattices",
        lambda _: PC.JoinSemilattice(elements=diamond_elements, relations=diamond_relations) in P.JoinSemilattice().Finite(),
    ),
    (
        "JoinSemilattice(elements=..., covers=...) refines to finite join-semilattices",
        lambda _: PC.JoinSemilattice(elements=diamond_elements, covers=diamond_relations) in P.JoinSemilattice().Finite(),
    ),
    (
        "JoinSemilattice(elements=..., order_predicate=...) refines to finite join-semilattices",
        lambda _: PC.JoinSemilattice(elements=diamond_elements, order_predicate=diamond_le) in P.JoinSemilattice().Finite(),
    ),
    (
        "JoinSemilattice(elements=..., cover_predicate=...) refines to finite join-semilattices",
        lambda _: PC.JoinSemilattice(elements=chain_elements, cover_predicate=chain_covers_predicate) in P.JoinSemilattice().Finite(),
    ),
    (
        "JoinSemilattice(upper_covers_dict=...) refines to finite join-semilattices",
        lambda _: PC.JoinSemilattice(upper_covers_dict=diamond_covers) in P.JoinSemilattice().Finite(),
    ),
    (
        "JoinSemilattice(upper_covers=...) refines to finite join-semilattices",
        lambda _: PC.JoinSemilattice(upper_covers=diamond_cover_list) in P.JoinSemilattice().Finite(),
    ),
    (
        "JoinSemilattice(existing=...) refines to finite join-semilattices",
        lambda _: PC.JoinSemilattice(existing=raw_diamond_poset()) in P.JoinSemilattice().Finite(),
    ),
    (
        "JoinSemilattice(existing=spec-owned poset) stays inside the category constructor surface",
        lambda _: PC.JoinSemilattice(existing=diamond_poset) in P.JoinSemilattice().Finite(),
    ),
    (
        "LatticePoset(hasse_digraph=...) refines to finite lattices",
        lambda _: PC.LatticePoset(hasse_digraph=diamond_digraph) in P.Lattice().Finite(),
    ),
    (
        "LatticePoset(elements=..., relations=...) refines to finite lattices",
        lambda _: PC.LatticePoset(elements=diamond_elements, relations=diamond_relations) in P.Lattice().Finite(),
    ),
    (
        "LatticePoset(elements=..., covers=...) refines to finite lattices",
        lambda _: PC.LatticePoset(elements=diamond_elements, covers=diamond_relations) in P.Lattice().Finite(),
    ),
    ("LatticePoset(elements=..., order_predicate=...) refines to finite lattices", lambda _: PC.LatticePoset(elements=diamond_elements, order_predicate=diamond_le) in P.Lattice().Finite()),
    (
        "LatticePoset(elements=..., cover_predicate=...) refines to finite lattices",
        lambda _: PC.LatticePoset(elements=chain_elements, cover_predicate=chain_covers_predicate) in P.Lattice().Finite(),
    ),
    ("LatticePoset(upper_covers_dict=...) refines to finite lattices", lambda _: PC.LatticePoset(upper_covers_dict=diamond_covers) in P.Lattice().Finite()),
    ("LatticePoset(upper_covers=...) refines to finite lattices", lambda _: PC.LatticePoset(upper_covers=diamond_cover_list) in P.Lattice().Finite()),
    ("LatticePoset(existing=...) refines to finite lattices", lambda _: PC.LatticePoset(existing=raw_diamond_poset()) in P.Lattice().Finite()),
    (
        "LatticePoset(existing=spec-owned poset) stays inside the category constructor surface",
        lambda _: PC.LatticePoset(existing=diamond_poset) in P.Lattice().Finite(),
    ),
    (
        "finite diamond poset has the expected top and bottom",
        lambda _: diamond_poset.bottom() == 0
        and diamond_poset.top() == 3
        and diamond_poset.has_bottom()
        and diamond_poset.has_top()
        and diamond_poset.is_bounded(),
    ),
    (
        "finite diamond poset has the expected extremal elements",
        lambda _: diamond_poset.minimal_elements() == [0] and diamond_poset.maximal_elements() == [3],
    ),
    (
        "finite diamond poset exposes cover relations through list and iterator surfaces",
        lambda _: diamond_poset.cover_relations() == [[0, 1], [0, 2], [1, 3], [2, 3]]
        and list(diamond_poset.cover_relations_iterator()) == [[0, 1], [0, 2], [1, 3], [2, 3]],
    ),
    (
        "finite diamond poset exposes reverse comparisons and lower covers",
        lambda _: diamond_poset.ge(3, 1) and diamond_poset.gt(3, 1) and diamond_poset.lower_covers(3) == [1, 2],
    ),
    (
        "finite diamond poset generates order ideals and filters",
        lambda _: diamond_poset.order_ideal([1]) == [0, 1] and diamond_poset.order_filter([1]) == [1, 3],
    ),
    (
        "finite diamond poset intervals distinguish open and closed intervals",
        lambda _: diamond_poset.closed_interval(0, 3) == [0, 1, 2, 3]
        and diamond_poset.interval(0, 3) == [0, 1, 2, 3]
        and diamond_poset.open_interval(0, 3) == [1, 2],
    ),
    (
        "finite diamond poset height and width certificates recover chains and antichains",
        lambda _: diamond_poset.height_certificate() == (3, [0, 1, 3])
        and diamond_poset.width_certificate() == (2, [1, 2]),
    ),
    (
        "finite diamond poset is ranked and semilattice-certified",
        lambda _: diamond_poset.is_ranked()
        and diamond_poset.meet_semilattice_certificate() == (True, None)
        and diamond_poset.join_semilattice_certificate() == (True, None),
    ),
    (
        "finite diamond poset enumerates chains antichains and linear extensions",
        lambda _: [0, 1, 3] in list(diamond_poset.chains())
        and [1, 2] in list(diamond_poset.antichains())
        and [list(extension) for extension in diamond_poset.linear_extensions()] == [[0, 1, 2, 3], [0, 2, 1, 3]],
    ),
    (
        "poset Hom and morphism surfaces own order-preserving predicates",
        lambda _: abstract_method_has_name(PosetHomCategory.ElementMethods.is_order_preserving, "is_order_preserving")
        and abstract_method_has_name(PosetHomCategory.ElementMethods.is_order_embedding, "is_order_embedding"),
    ),
    (
        "poset End and Aut surfaces own base-poset and automorphism predicates",
        lambda _: abstract_method_has_name(PosetEndCategory.ParentMethods.base_poset, "base_poset")
        and PosetAutCategory.ElementMethods().is_order_automorphism(),
    ),
    (
        "poset objects-over and objects-under surfaces own structure-poset maps",
        lambda _: abstract_method_has_name(_ObjectsOver.ParentMethods.structure_poset, "structure_poset")
        and abstract_method_has_name(_ObjectsUnder.ParentMethods.structure_poset, "structure_poset"),
    ),
    (
        "finite diamond lattice complements pair opposite atoms",
        lambda _: diamond_lattice.complements() == {0: [3], 1: [2], 2: [1], 3: [0]}
        and diamond_lattice.complements(1) == [2],
    ),
    (
        "finite diamond lattice exposes meet and join semilattice extremal elements",
        lambda _: diamond_lattice.atoms() == [1, 2] and diamond_lattice.coatoms() == [1, 2],
    ),
    (
        "finite diamond lattice exposes meet and join operation matrices",
        lambda _: diamond_lattice.meet_matrix()[1, 2] == 0 and diamond_lattice.join_matrix()[1, 2] == 3,
    ),
    (
        "finite diamond lattice exposes meet and join subsemilattice constructors",
        lambda _: diamond_lattice.pseudocomplement(1) == 2
        and diamond_lattice.submeetsemilattice([0, 1, 3]).cardinality() == 3
        and diamond_lattice.subjoinsemilattice([0, 1, 3]).cardinality() == 3,
    ),
    (
        "finite meet and join semilattice categories own the expected method surfaces",
        lambda _: abstract_method_has_name(_FiniteMeetSemilatticePosets.ParentMethods.atoms, "atoms")
        and abstract_method_has_name(_FiniteMeetSemilatticePosets.ParentMethods.meet_matrix, "meet_matrix")
        and abstract_method_has_name(_FiniteJoinSemilatticePosets.ParentMethods.coatoms, "coatoms")
        and abstract_method_has_name(_FiniteJoinSemilatticePosets.ParentMethods.join_matrix, "join_matrix"),
    ),
    (
        "finite diamond lattice atomic coatomic complemented and distributive certificates are positive",
        lambda _: diamond_lattice.atomic_certificate() == (True, None)
        and diamond_lattice.coatomic_certificate() == (True, None)
        and diamond_lattice.complemented_certificate() == (True, None)
        and diamond_lattice.distributive_certificate() == (True, None),
    ),
    (
        "finite diamond lattice modular and semidistributive surfaces are positive",
        lambda _: diamond_lattice.are_modular_elements([1, 2])
        and diamond_lattice.modular_certificate() == (True, None)
        and diamond_lattice.modular_elements_certificate([1, 2]) == (True, None)
        and diamond_lattice.is_semidistributive(),
    ),
    (
        "finite diamond lattice sublattice and congruence constructions have expected sizes",
        lambda _: diamond_lattice.sublattice([0, 1, 3]).cardinality() == 3
        and diamond_lattice.sublattices_lattice().cardinality() == 13
        and diamond_lattice.congruence_generated_by([[0, 1]]) == SetPartition([[0, 1], [2, 3]])
        and diamond_lattice.congruence_lattice().cardinality() == 4,
    ),
)

assert_category_statements(CATEGORY_STATEMENTS)
