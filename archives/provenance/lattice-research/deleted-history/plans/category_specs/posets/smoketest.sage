import sys
from pathlib import Path

THIS_FILE = Path(__file__).resolve()
sys.path.insert(0, str(THIS_FILE.parent.parent.parent))

from category_specs.cat import Cat
from category_specs.posets import Posets
from category_specs.utils import assert_smoke_statements


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


def diamond_covers_predicate(a, b):
    return a != b and diamond_le(b, a) and bin(a ^ b).count("1") == 1


def chain_covers_predicate(a, b):
    return b == a + 1


def raw_diamond_poset():
    return Poset(diamond_covers)

SMOKE_STATEMENTS = (
    ("Posets() is an object of Cat()", lambda _: P in Cat()),
    ("Posets().Finite() is an object of Cat()", lambda _: P.Finite() in Cat()),
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
    ("from_digraph(...) refines to finite posets", lambda _: PC.from_digraph(diamond_digraph, cover_relations=True) in P.Finite()),
    (
        "from_relations(...) refines to finite posets",
        lambda _: PC.from_relations(diamond_elements, diamond_relations, cover_relations=True) in P.Finite(),
    ),
    ("from_order_predicate(...) refines to finite posets", lambda _: PC.from_order_predicate(diamond_elements, diamond_le) in P.Finite()),
    (
        "from_cover_predicate(...) refines to finite posets",
        lambda _: PC.from_cover_predicate(chain_elements, chain_covers_predicate) in P.Finite(),
    ),
    ("from_upper_covers_dict(...) refines to finite posets", lambda _: PC.from_upper_covers_dict(diamond_covers) in P.Finite()),
    ("from_upper_covers(...) refines to finite posets", lambda _: PC.from_upper_covers(diamond_cover_list) in P.Finite()),
    ("from_existing(...) refines to finite posets", lambda _: PC.from_existing(raw_diamond_poset()) in P.Finite()),
    (
        "meet_semilattice_from_digraph(...) refines to finite meet-semilattices",
        lambda _: PC.meet_semilattice_from_digraph(diamond_digraph, cover_relations=True) in P.MeetSemilattice().Finite(),
    ),
    (
        "meet_semilattice_from_relations(...) refines to finite meet-semilattices",
        lambda _: PC.meet_semilattice_from_relations(diamond_elements, diamond_relations, cover_relations=True) in P.MeetSemilattice().Finite(),
    ),
    (
        "meet_semilattice_from_order_predicate(...) refines to finite meet-semilattices",
        lambda _: PC.meet_semilattice_from_order_predicate(diamond_elements, diamond_le) in P.MeetSemilattice().Finite(),
    ),
    (
        "meet_semilattice_from_cover_predicate(...) refines to finite meet-semilattices",
        lambda _: PC.meet_semilattice_from_cover_predicate(chain_elements, chain_covers_predicate) in P.MeetSemilattice().Finite(),
    ),
    (
        "meet_semilattice_from_upper_covers_dict(...) refines to finite meet-semilattices",
        lambda _: PC.meet_semilattice_from_upper_covers_dict(diamond_covers) in P.MeetSemilattice().Finite(),
    ),
    (
        "meet_semilattice_from_upper_covers(...) refines to finite meet-semilattices",
        lambda _: PC.meet_semilattice_from_upper_covers(diamond_cover_list) in P.MeetSemilattice().Finite(),
    ),
    (
        "meet_semilattice_from_existing(...) refines to finite meet-semilattices",
        lambda _: PC.meet_semilattice_from_existing(raw_diamond_poset()) in P.MeetSemilattice().Finite(),
    ),
    (
        "join_semilattice_from_digraph(...) refines to finite join-semilattices",
        lambda _: PC.join_semilattice_from_digraph(diamond_digraph, cover_relations=True) in P.JoinSemilattice().Finite(),
    ),
    (
        "join_semilattice_from_relations(...) refines to finite join-semilattices",
        lambda _: PC.join_semilattice_from_relations(diamond_elements, diamond_relations, cover_relations=True) in P.JoinSemilattice().Finite(),
    ),
    (
        "join_semilattice_from_order_predicate(...) refines to finite join-semilattices",
        lambda _: PC.join_semilattice_from_order_predicate(diamond_elements, diamond_le) in P.JoinSemilattice().Finite(),
    ),
    (
        "join_semilattice_from_cover_predicate(...) refines to finite join-semilattices",
        lambda _: PC.join_semilattice_from_cover_predicate(chain_elements, chain_covers_predicate) in P.JoinSemilattice().Finite(),
    ),
    (
        "join_semilattice_from_upper_covers_dict(...) refines to finite join-semilattices",
        lambda _: PC.join_semilattice_from_upper_covers_dict(diamond_covers) in P.JoinSemilattice().Finite(),
    ),
    (
        "join_semilattice_from_upper_covers(...) refines to finite join-semilattices",
        lambda _: PC.join_semilattice_from_upper_covers(diamond_cover_list) in P.JoinSemilattice().Finite(),
    ),
    (
        "join_semilattice_from_existing(...) refines to finite join-semilattices",
        lambda _: PC.join_semilattice_from_existing(raw_diamond_poset()) in P.JoinSemilattice().Finite(),
    ),
    (
        "lattice_from_digraph(...) refines to finite lattices",
        lambda _: PC.lattice_from_digraph(diamond_digraph, cover_relations=True) in P.Lattice().Finite(),
    ),
    (
        "lattice_from_relations(...) refines to finite lattices",
        lambda _: PC.lattice_from_relations(diamond_elements, diamond_relations, cover_relations=True) in P.Lattice().Finite(),
    ),
    ("lattice_from_order_predicate(...) refines to finite lattices", lambda _: PC.lattice_from_order_predicate(diamond_elements, diamond_le) in P.Lattice().Finite()),
    (
        "lattice_from_cover_predicate(...) refines to finite lattices",
        lambda _: PC.lattice_from_cover_predicate(chain_elements, chain_covers_predicate) in P.Lattice().Finite(),
    ),
    ("lattice_from_upper_covers_dict(...) refines to finite lattices", lambda _: PC.lattice_from_upper_covers_dict(diamond_covers) in P.Lattice().Finite()),
    ("lattice_from_upper_covers(...) refines to finite lattices", lambda _: PC.lattice_from_upper_covers(diamond_cover_list) in P.Lattice().Finite()),
    ("lattice_from_existing(...) refines to finite lattices", lambda _: PC.lattice_from_existing(raw_diamond_poset()) in P.Lattice().Finite()),
)

assert_smoke_statements(SMOKE_STATEMENTS)
