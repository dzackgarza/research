r"""Named integral lattices and primitive embeddings used by the research layer."""

from collections.abc import Mapping
from functools import cache

from sage.combinat.root_system.cartan_type import CartanType
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.lattices import (
    Lattices,
    register_indecomposable,
    register_indecomposable_gram,
    signature_pair,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.set_categories import NN
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.tensors.tensor import tensor

ZZ = _own_ring(SageZZ)


def _gram_from_engine_matrix(engine_matrix):
    r"""Cross one private Sage Gram matrix into the public tensor layer."""
    rows = int(engine_matrix.nrows())
    columns = int(engine_matrix.ncols())
    return tensor(
        ZZ,
        (),
        (rows, columns),
        [
            [ZZ._from_engine_element(SageZZ(engine_matrix[i, j])) for j in range(columns)]
            for i in range(rows)
        ],
    )


def _block_gram(*grams):
    r"""Return the orthogonal direct sum of finite Gram tensors."""
    ranks = tuple(int(gram.tensor_shape()[0]) for gram in grams)
    total = sum(ranks)
    values = [[ZZ.zero() for _ in range(total)] for _ in range(total)]
    offset = 0
    for gram, rank in zip(grams, ranks, strict=True):
        shape = gram.tensor_shape()
        if (
            gram.tensor_valence() != (NN**2)((0, 2))
            or shape[0] != rank
            or shape[1] != rank
        ):
            raise TypeError("a catalogue Gram block is a square type-(0,2) tensor")
        for i in range(rank):
            for j in range(rank):
                values[offset + i][offset + j] = ZZ(gram[i, j])
        offset += rank
    return tensor(ZZ, (), (total, total), values)


def _named_lattice(gram, names):
    return Lattices(ZZ)(gram, names=names)


_C = Lattices(ZZ)
_U = _C("U")
_E8 = _C("E8")
_Ug = _U.gram_tensor()
_E8g = _E8.gram_tensor()
_rank_one_2 = tensor(ZZ, (), (1, 1), [[2]])
_rank_one_m2 = tensor(ZZ, (), (1, 1), [[-2]])
_rank_one_m4 = tensor(ZZ, (), (1, 1), [[-4]])


class NamedLattices:
    Zero = _C(0)
    Z = _C(1)
    Z_2 = Z.twist(2)
    U = _U
    H = U
    U_2 = U.twist(2)
    H_2 = U_2
    E8 = _E8
    E8_2 = E8.twist(2)
    E10 = U + E8
    E10_2 = U_2 + E8_2

    Sdp = U_2
    SEn = E10_2

    Tco = _C(
        _block_gram(
            _rank_one_2,
            2 * _Ug,
            2 * _E8g,
        ),
        names="h,ep,fp,a1,a2,a3,a4,a5,a6,a7,a8",
    )
    Sco = _C(
        _block_gram(
            _rank_one_m2,
            2 * _Ug,
            2 * _E8g,
        )
    )
    TEn = _C(
        _block_gram(_Ug, 2 * _Ug, 2 * _E8g),
        names="e,f,ep,fp,a1,a2,a3,a4,a5,a6,a7,a8",
    )
    TdP = _C(
        _block_gram(_Ug, 2 * _Ug, _E8g, _E8g),
        names=("e,f,ep,fp,a1,a2,a3,a4,a5,a6,a7,a8,b1,b2,b3,b4,b5,b6,b7,b8"),
    )
    L_20_2_0 = TdP
    LK3 = _C(
        _block_gram(_Ug, _Ug, _Ug, _E8g, _E8g),
        names=("e1,f1,e2,f2,e3,f3,a1,a2,a3,a4,a5,a6,a7,a8,b1,b2,b3,b4,b5,b6,b7,b8"),
    )
    LK3_2 = _C(_block_gram(_rank_one_m2, _Ug, _Ug, _E8g, _E8g))
    LK3_4 = _C(_block_gram(_rank_one_m4, _Ug, _Ug, _E8g, _E8g))
    LpNik = _C(_block_gram(_Ug, _Ug, _Ug, 2 * _E8g))
    LmNik = E8_2

    Mukai = _C(_block_gram(_Ug, _Ug, _Ug, _Ug, _E8g, _E8g))
    MukaiExtended = _C(_block_gram(_Ug, _Ug, _Ug, _Ug, _Ug, _E8g, _E8g))
    MukaiAbelian = _C(_block_gram(_Ug, _Ug, _Ug, _Ug))
    MukaiAbelianExtended = _C(_block_gram(_Ug, _Ug, _Ug, _Ug, _Ug))
    U_E8_2 = U + E8_2

    BogachevKolpakovNonReflective = _C([[3, 7, 49], [7, 0, 0], [49, 0, 49]]).twist(-1)
    BogachevKolpakovWithoutRoots = _C([[0, 0, 49], [0, 49, 7], [49, 7, 3]]).twist(-1)


NamedLattices.A1 = _C("A1")
NamedLattices.D4 = _C("D4")
NamedLattices.D6 = _C("D6")
NamedLattices.D8 = _C("D8")
NamedLattices.E7 = _C("E7")
NamedLattices.Z_m2 = NamedLattices.Z.twist(-2)


for _name, _value in vars(NamedLattices).items():
    if not _name.startswith("_") and _value in _C:
        setattr(Lattices, _name, _value)


# Exact Gram-block names used by the represented direct-sum decomposition.
# A1 and D2 are intentionally omitted: they are scalar twists of rank-one
# blocks and should display as I_{0,1}(2), not as competing root names.
register_indecomposable_gram("I_{1,0}", tensor(ZZ, (), (1, 1), [[1]]))
register_indecomposable_gram("I_{0,1}", tensor(ZZ, (), (1, 1), [[-1]]))
for _rank in range(2, 22):
    register_indecomposable_gram(
        f"A_{{{_rank}}}",
        -_gram_from_engine_matrix(CartanType(["A", _rank]).cartan_matrix()),
    )
for _rank in range(3, 23):
    register_indecomposable_gram(
        f"D_{{{_rank}}}",
        -_gram_from_engine_matrix(CartanType(["D", _rank]).cartan_matrix()),
    )
for _rank in (6, 7, 8):
    register_indecomposable_gram(
        f"E_{{{_rank}}}",
        -_gram_from_engine_matrix(CartanType(["E", _rank]).cartan_matrix()),
    )
register_indecomposable("U", NamedLattices.U)


# Nikulin, Math. USSR-Izv. 14 (1980), DOI
# 10.1070/IM1980v014n01ABEH001060; the 75 K3-involution types are displayed
# in Alexeev--Engel--Han, arXiv:2208.10383, Figure 1.
_TWO_ELEMENTARY_RECIPES = {
    (1, 1, 1): (("Z_2", 1),),
    (2, 0, 0): (("U", 1),),
    (2, 2, 0): (("U_2", 1),),
    (2, 2, 1): (("Z_2", 1), ("Z_m2", 1)),
    (3, 1, 1): (("U", 1), ("A1", 1)),
    (3, 3, 1): (("U_2", 1), ("A1", 1)),
    (4, 2, 1): (("U", 1), ("A1", 2)),
    (4, 4, 1): (("U_2", 1), ("A1", 2)),
    (5, 3, 1): (("U", 1), ("A1", 3)),
    (5, 5, 1): (("U_2", 1), ("A1", 3)),
    (6, 2, 0): (("U", 1), ("D4", 1)),
    (6, 4, 0): (("U_2", 1), ("D4", 1)),
    (6, 4, 1): (("U", 1), ("A1", 4)),
    (6, 6, 1): (("U_2", 1), ("A1", 4)),
    (7, 3, 1): (("U", 1), ("D4", 1), ("A1", 1)),
    (7, 5, 1): (("U_2", 1), ("A1", 1), ("D4", 1)),
    (7, 7, 1): (("U_2", 1), ("A1", 5)),
    (8, 2, 1): (("U", 1), ("D6", 1)),
    (8, 4, 1): (("U_2", 1), ("D6", 1)),
    (8, 6, 1): (("U_2", 1), ("A1", 2), ("D4", 1)),
    (8, 8, 1): (("U_2", 1), ("A1", 6)),
    (9, 1, 1): (("U", 1), ("E7", 1)),
    (9, 3, 1): (("U_2", 1), ("E7", 1)),
    (9, 5, 1): (("U_2", 1), ("A1", 1), ("D6", 1)),
    (9, 7, 1): (("U", 1), ("A1", 7)),
    (9, 9, 1): (("U_2", 1), ("A1", 7)),
    (10, 0, 0): (("E10", 1),),
    (10, 2, 0): (("U", 1), ("D8", 1)),
    (10, 2, 1): (("U", 1), ("E7", 1), ("A1", 1)),
    (10, 4, 0): (("U_2", 1), ("D8", 1)),
    (10, 4, 1): (("U", 1), ("D6", 1), ("A1", 2)),
    (10, 6, 0): (("U_2", 1), ("D4", 2)),
    (10, 6, 1): (("U_2", 1), ("D6", 1), ("A1", 2)),
    (10, 8, 0): (("U", 1), ("E8_2", 1)),
    (10, 8, 1): (("U", 1), ("A1", 8)),
    (10, 10, 0): (("E10_2", 1),),
    (10, 10, 1): (("U_2", 1), ("A1", 8)),
    (11, 1, 1): (("U", 1), ("E8", 1), ("A1", 1)),
    (11, 3, 1): (("U", 1), ("D8", 1), ("A1", 1)),
    (11, 5, 1): (("U", 1), ("D6", 1), ("A1", 3)),
    (11, 7, 1): (("U_2", 1), ("D6", 1), ("A1", 3)),
    (11, 9, 1): (("U", 1), ("A1", 1), ("E8_2", 1)),
    (11, 11, 1): (("U_2", 1), ("A1", 1), ("E8_2", 1)),
    (12, 2, 1): (("U", 1), ("E8", 1), ("A1", 2)),
    (12, 4, 1): (("U", 1), ("D8", 1), ("A1", 2)),
    (12, 6, 1): (("U_2", 1), ("D4", 1), ("D6", 1)),
    (12, 8, 1): (("U_2", 1), ("D6", 1), ("A1", 4)),
    (12, 10, 1): (("U", 1), ("A1", 2), ("E8_2", 1)),
    (13, 3, 1): (("U", 1), ("E7", 1), ("D4", 1)),
    (13, 5, 1): (("U_2", 1), ("D4", 1), ("E7", 1)),
    (13, 7, 1): (("U", 1), ("D6", 1), ("A1", 5)),
    (13, 9, 1): (("U_2", 1), ("D6", 1), ("A1", 5)),
    (14, 2, 0): (("U", 1), ("D4", 1), ("E8", 1)),
    (14, 4, 0): (("U", 1), ("D4", 1), ("D8", 1)),
    (14, 4, 1): (("U", 1), ("D6", 2)),
    (14, 6, 0): (("U_2", 1), ("D4", 1), ("D8", 1)),
    (14, 6, 1): (("U_2", 1), ("D6", 2)),
    (14, 8, 1): (("U_2", 1), ("D6", 1), ("D4", 1), ("A1", 2)),
    (15, 3, 1): (("U", 1), ("E7", 1), ("D6", 1)),
    (15, 5, 1): (("U_2", 1), ("D6", 1), ("E7", 1)),
    (15, 7, 1): (("U_2", 1), ("D8", 1), ("D4", 1), ("A1", 1)),
    (16, 2, 1): (("U", 1), ("D6", 1), ("E8", 1)),
    (16, 4, 1): (("U", 1), ("D6", 1), ("D8", 1)),
    (16, 6, 1): (("U_2", 1), ("D6", 1), ("D8", 1)),
    (17, 1, 1): (("U", 1), ("E7", 1), ("E8", 1)),
    (17, 3, 1): (("U", 1), ("D8", 1), ("E7", 1)),
    (17, 5, 1): (("U_2", 1), ("D8", 1), ("E7", 1)),
    (18, 0, 0): (("U", 1), ("E8", 2)),
    (18, 2, 0): (("U", 1), ("D8", 1), ("E8", 1)),
    (18, 2, 1): (("U", 1), ("E8", 1), ("E7", 1), ("A1", 1)),
    (18, 4, 0): (("U", 1), ("D8", 2)),
    (18, 4, 1): (("U_2", 1), ("E8", 1), ("E7", 1), ("A1", 1)),
    (19, 1, 1): (("U", 1), ("E8", 2), ("A1", 1)),
    (19, 3, 1): (("U_2", 1), ("E8", 2), ("A1", 1)),
    (20, 2, 1): (("U", 1), ("E8", 2), ("A1", 2)),
}


def _orthogonal_sum(recipe):
    result = None
    for name, multiplicity in recipe:
        block = getattr(NamedLattices, name)
        for _index in range(multiplicity):
            result = block if result is None else result + block
    return NamedLattices.Zero if result is None else result


@cache
def _two_elementary_lattice(key):
    return _orthogonal_sum(_TWO_ELEMENTARY_RECIPES[key])


class _TwoElementaryTable(Mapping):
    r"""Lazy read-only form of the 75-row Nikulin table."""

    def __getitem__(self, key):
        key = tuple(SageZZ(entry) for entry in key)
        if key not in _TWO_ELEMENTARY_RECIPES:
            raise KeyError(key)
        return _two_elementary_lattice(key)

    def __iter__(self):
        return iter(_TWO_ELEMENTARY_RECIPES)

    def __len__(self):
        return len(_TWO_ELEMENTARY_RECIPES)


TwoElementary = _TwoElementaryTable()


def _sum_spec(*parts):
    return ("sum", parts)


def _glue_spec(coefficients, *parts):
    return ("glue", parts, tuple(coefficients))


_NEGATIVE_TWO_ELEMENTARY_SPECS = {
    (0, 0, 0): (_sum_spec(),),
    (1, 1, 1): (_sum_spec("A1"),),
    (2, 2, 1): (_sum_spec(("A1", 2)),),
    (3, 3, 1): (_sum_spec(("A1", 3)),),
    (4, 2, 0): (_sum_spec("D4"),),
    (4, 4, 1): (_sum_spec(("A1", 4)),),
    (5, 3, 1): (_sum_spec("D4", "A1"),),
    (5, 5, 1): (_sum_spec(("A1", 5)),),
    (6, 2, 1): (_sum_spec("D6"),),
    (6, 4, 1): (_sum_spec("D4", ("A1", 2)),),
    (6, 6, 1): (_sum_spec(("A1", 6)),),
    (7, 1, 1): (_sum_spec("E7"),),
    (7, 3, 1): (_sum_spec("D6", "A1"),),
    (7, 5, 1): (_sum_spec("D4", ("A1", 3)),),
    (7, 7, 1): (_sum_spec(("A1", 7)),),
    (8, 0, 0): (_sum_spec("E8"),),
    (8, 2, 0): (_sum_spec("D8"),),
    (8, 2, 1): (_sum_spec("E7", "A1"),),
    (8, 4, 0): (_sum_spec(("D4", 2)),),
    (8, 4, 1): (_sum_spec("D6", ("A1", 2)),),
    (8, 6, 0): (_glue_spec([1, 1, 1, 1, 1, 1, 1, 1], ("A1", 8)),),
    (8, 6, 1): (_sum_spec("D4", ("A1", 4)),),
    (8, 8, 0): (_sum_spec("E8_2"),),
    (8, 8, 1): (_sum_spec(("A1", 8)),),
    (9, 1, 1): (_sum_spec("E8", "A1"),),
    (9, 3, 1): (
        _sum_spec("E7", ("A1", 2)),
        _sum_spec("D8", "A1"),
    ),
    (9, 5, 1): (
        _sum_spec("D6", ("A1", 3)),
        _sum_spec(("D4", 2), "A1"),
    ),
    (9, 7, 1): (
        _glue_spec([0, 1, 1, 1, 1, 1, 1, 1, 1], ("A1", 9)),
        _sum_spec(("A1", 5), "D4"),
    ),
    (9, 9, 1): (
        _sum_spec(("A1", 9)),
        _sum_spec("A1", "E8_2"),
    ),
    (10, 2, 1): (
        _sum_spec("D10"),
        _sum_spec("E8", ("A1", 2)),
    ),
    (10, 4, 1): (
        _sum_spec("E7", ("A1", 3)),
        _sum_spec("D8", ("A1", 2)),
        _sum_spec("D6", "D4"),
    ),
    (10, 6, 1): (
        _sum_spec(("D4", 2), ("A1", 2)),
        _glue_spec(
            [1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
            ("A1", 6),
            "D4",
        ),
        _sum_spec("D6", ("A1", 4)),
    ),
    (10, 8, 1): (
        _sum_spec("D4", ("A1", 6)),
        _glue_spec(
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            ("A1", 10),
        ),
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
            "A3",
            ("E7", 1, 2),
        ),
    ),
    (11, 3, 1): (
        _sum_spec("D10", "A1"),
        _sum_spec("E8", ("A1", 3)),
        _sum_spec("E7", "D4"),
    ),
    (11, 5, 1): (
        _sum_spec("D6", "D4", "A1"),
        _sum_spec("D8", ("A1", 3)),
        _sum_spec("E7", ("A1", 4)),
        _glue_spec(
            [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
            "D6",
            ("A1", 5),
        ),
    ),
    (11, 7, 1): (
        _sum_spec("D6", ("A1", 5)),
        _glue_spec(
            [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
            ("A1", 7),
            "D4",
        ),
        _sum_spec(("D4", 2), ("A1", 3)),
        _glue_spec(
            [1, 2, 0, 1, 2, 1, 0, 2, 0, 1, 2],
            "A5",
            ("E6", 1, 2),
        ),
    ),
    (12, 2, 0): (
        _sum_spec("E8", "D4"),
        _sum_spec("D12"),
    ),
    (12, 4, 0): (
        _glue_spec(
            [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
            "E7",
            ("A1", 5),
        ),
        _sum_spec("D8", "D4"),
    ),
    (12, 4, 1): (
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
            "D8",
            ("A1", 4),
        ),
        _sum_spec("E8", ("A1", 4)),
        _sum_spec(("D6", 2)),
        _sum_spec("D10", ("A1", 2)),
        _sum_spec("E7", "D4", "A1"),
    ),
    (12, 6, 0): (
        _sum_spec(("D4", 3)),
        _glue_spec(
            [1, 0, 2, 0, 1, 2, 1, 0, 2, 0, 1, 2],
            "E6",
            ("E6", 1, 2),
        ),
        _glue_spec(
            [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            "D6",
            ("A1", 6),
        ),
    ),
    (12, 6, 1): (
        _glue_spec(
            [1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
            "D6",
            ("A1", 6),
        ),
        _sum_spec("E7", ("A1", 5)),
        _glue_spec(
            [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
            ("D4", 2),
            ("A1", 4),
        ),
        _sum_spec("D8", ("A1", 4)),
        _sum_spec("D6", "D4", ("A1", 2)),
        _glue_spec(
            [3, 2, 1, 0, 3, 2, 1, 2, 0, 2, 1, 3],
            "A7",
            ("D5", 1, 2),
        ),
    ),
    (13, 3, 1): (
        _sum_spec("D12", "A1"),
        _sum_spec("E7", "D6"),
        _sum_spec("E8", "D4", "A1"),
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
            "D10",
            ("A1", 3),
        ),
    ),
    (13, 5, 1): (
        _sum_spec("D8", "D4", "A1"),
        _sum_spec("E7", "D4", ("A1", 2)),
        _sum_spec(("D6", 2), "A1"),
        _glue_spec(
            [0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
            "E7",
            ("A1", 6),
        ),
        _glue_spec(
            [1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
            "D6",
            "D4",
            ("A1", 3),
        ),
        _sum_spec("D10", ("A1", 3)),
        _sum_spec("E8", ("A1", 5)),
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1],
            "D8",
            ("A1", 5),
        ),
        _glue_spec(
            [3, 1, 4, 2, 0, 3, 1, 4, 2, 1, 2, 3, 4],
            "A9",
            ("A4", 1, 2),
        ),
    ),
    (14, 2, 1): (
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1],
            "D12",
            ("A1", 2),
        ),
        _sum_spec("D14"),
        _sum_spec("E8", "D6"),
        _sum_spec(("E7", 2)),
    ),
    (14, 4, 1): (
        _glue_spec(
            [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
            ("D6", 2),
            ("A1", 2),
        ),
        _sum_spec("E8", "D4", ("A1", 2)),
        _sum_spec("E7", "D6", "A1"),
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
            "D10",
            ("A1", 4),
        ),
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
            "D8",
            "D4",
            ("A1", 2),
        ),
        _glue_spec(
            [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
            "E7",
            "D4",
            ("A1", 3),
        ),
        _sum_spec("D12", ("A1", 2)),
        _sum_spec("D10", "D4"),
        _sum_spec("D8", "D6"),
        _glue_spec(
            [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 2, 4, 3],
            "A11",
            ("A2", 1, 2),
            ("A1", 1, 2),
        ),
    ),
    (15, 1, 1): (
        _sum_spec("E8", "E7"),
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            "D14",
            "A1",
        ),
    ),
    (15, 3, 1): (
        _sum_spec(("E7", 2), "A1"),
        _sum_spec("D8", "E7"),
        _sum_spec("D14", "A1"),
        _sum_spec("E8", "D6", "A1"),
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
            "D12",
            ("A1", 3),
        ),
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1],
            "D10",
            "D4",
            "A1",
        ),
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1],
            "D8",
            "D6",
            "A1",
        ),
        _glue_spec(
            [0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
            "E7",
            "D6",
            ("A1", 2),
        ),
        _glue_spec(
            [8, 2, 10, 4, 12, 6, 0, 8, 2, 10, 4, 12, 6, 7, 5],
            "A13",
            ("A1", 1, 2),
            "N14",
        ),
    ),
    (16, 0, 0): (
        _sum_spec(("E8", 2)),
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            "D16",
        ),
    ),
    (16, 2, 0): (
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1],
            ("D8", 2),
        ),
        _glue_spec(
            [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
            ("E7", 2),
            ("A1", 2),
        ),
        _sum_spec("E8", "D8"),
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1],
            "D12",
            "D4",
        ),
        _sum_spec("D16"),
        _glue_spec(
            [3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 2],
            "A15",
            ("A1", 1, 2),
        ),
    ),
    (16, 2, 1): (
        _sum_spec("E8", "E7", "A1"),
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
            "D8",
            "E7",
            "A1",
        ),
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
            "D10",
            "D6",
        ),
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
            "D14",
            ("A1", 2),
        ),
        _glue_spec(
            [7, 6, 5, 4, 3, 2, 1, 0, 7, 6, 5, 4, 3, 2, 1, 3],
            "A15",
            "N8",
        ),
    ),
    (17, 1, 1): (
        _sum_spec(("E8", 2), "A1"),
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
            "D16",
            "A1",
        ),
        _glue_spec(
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
            "D10",
            "E7",
        ),
        _glue_spec(
            [2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1],
            "A17",
        ),
    ),
}


@cache
def _negative_block(name, twist=1):
    if name.startswith("N") and name[1:].isdigit():
        # ``rank_one_negative(d)`` in the archived catalogue means
        # ``<-2d>``, not ``<-d>``.
        block = _C([[-2 * SageZZ(name[1:])]])
    elif hasattr(NamedLattices, name):
        block = getattr(NamedLattices, name)
    else:
        block = _C(name)
    return block if twist == 1 else block.twist(SageZZ(twist))


def _negative_sum(parts):
    result = None
    for part in parts:
        if isinstance(part, str):
            name, multiplicity, twist = part, 1, 1
        elif len(part) == 2:
            name, multiplicity = part
            twist = 1
        else:
            name, multiplicity, twist = part
        block = _negative_block(name, twist)
        for _copy in range(multiplicity):
            result = block if result is None else result + block
    return NamedLattices.Zero if result is None else result


@cache
def _negative_two_elementary_row(key):
    values = []
    for spec in _NEGATIVE_TWO_ELEMENTARY_SPECS[key]:
        kind, parts, *rest = spec
        lattice = _negative_sum(parts)
        if kind == "glue":
            coefficients = rest[0]
            labels = tuple(lattice.module_generating_set())
            if len(coefficients) != len(labels):
                raise RuntimeError(f"glue vector for {key} has length {len(coefficients)}, not lattice rank {len(labels)}")
            vector = lattice.linear_combination({label: coefficient for label, coefficient in zip(labels, coefficients, strict=True) if coefficient})
            discriminant_class = vector.divided_discriminant_class()
            if lattice.discriminant_module().q(discriminant_class) != 0:
                raise ValueError(f"the recorded glue class for {key} is not isotropic")
            inclusion = lattice.overlattice(discriminant_class)
            lattice = inclusion.codomain()
            lattice._catalogue_glue_inclusion = inclusion
        values.append(lattice)
    return tuple(values)


class _NegativeDefTwoElementaryTable(Mapping):
    def __getitem__(self, key):
        key = tuple(SageZZ(entry) for entry in key)
        if key not in _NEGATIVE_TWO_ELEMENTARY_SPECS:
            raise KeyError(key)
        return _negative_two_elementary_row(key)

    def __iter__(self):
        return iter(_NEGATIVE_TWO_ELEMENTARY_SPECS)

    def __len__(self):
        return len(_NEGATIVE_TWO_ELEMENTARY_SPECS)


NegativeDefTwoElementary = _NegativeDefTwoElementaryTable()


def validate_negative_def_two_elementary_table():
    r"""Validate the signature and discriminant invariants of every listed class."""
    for key in NegativeDefTwoElementary:
        rank, _length, _delta = key
        for lattice in NegativeDefTwoElementary[key]:
            if lattice.signature_pair() != signature_pair(0, rank):
                raise AssertionError(f"{key} contains a lattice of signature {lattice.signature_pair()}")
            actual = lattice.two_elementary_invariants()
            if actual != key:
                raise AssertionError(f"{key} contains a lattice with invariants {actual}")
            inclusion = getattr(lattice, "_catalogue_glue_inclusion", None)
            if inclusion is not None:
                source = inclusion.domain()
                index = SageZZ(inclusion.index())
                if index <= 1:
                    raise AssertionError(f"{key} records a trivial glue inclusion")
                if abs(source.determinant()) != (
                    index**2 * abs(lattice.determinant())
                ):
                    raise AssertionError(f"{key} violates det(R)=[L:R]^2 det(L)")
                reduction = lattice.lll_reduction()
                witness = reduction.isometry
                if lattice.gram_tensor().pullback(witness) != reduction.reduced.gram_tensor():
                    raise AssertionError(f"{key} has an invalid isometry witness")
    return True


def validate_two_elementary_table():
    r"""Validate every row against its signature and Nikulin invariants."""
    if len(TwoElementary) != 75:
        raise AssertionError(f"Nikulin's table has 75 rows, not {len(TwoElementary)}")
    for key in TwoElementary:
        rank, _a, _delta = key
        lattice = TwoElementary[key]
        if lattice.signature_pair() != signature_pair(1, rank - 1):
            raise AssertionError(
                f"{key} has signature {lattice.signature_pair()}, "
                f"not {signature_pair(1, rank - 1)}"
            )
        actual = lattice.two_elementary_invariants()
        if actual != key:
            raise AssertionError(f"{key} is represented by a lattice with invariants {actual}")
    return True


@cache
def _two_elementary_blocks():
    blocks = (
        NamedLattices.A1,
        NamedLattices.D4,
        NamedLattices.D6,
        NamedLattices.D8,
        NamedLattices.E7,
        NamedLattices.E8,
        NamedLattices.E8_2,
        NamedLattices.Z_2,
        NamedLattices.U,
        NamedLattices.U_2,
    )
    return tuple(
        (
            block,
            block.signature_pair().first(),
            block.signature_pair().second(),
            block.discriminant_length(),
            block.delta(),
        )
        for block in blocks
    )


def two_elementary_orthogonal_sums(target_signature, a, delta):
    r"""Return block-orthogonal realizations of the stated 2-elementary invariants."""
    positive_target = int(target_signature.first())
    negative_target = int(target_signature.second())
    target_a = int(a)
    target_delta = int(delta)
    if min(positive_target, negative_target, target_a) < 0:
        raise ValueError("signature indices and discriminant length are nonnegative")
    if positive_target + negative_target == 0:
        raise ValueError("the zero lattice is not a nonempty block sum")
    if target_delta not in (0, 1):
        raise ValueError("Nikulin's delta is zero or one")

    block_data = _two_elementary_blocks()
    realizations = []

    def extend(index, positive, negative, length, realized_delta, counts):
        if length > positive + negative:
            return
        if index == len(block_data):
            if positive == negative == length == 0 and realized_delta == target_delta:
                recipe = tuple(
                    (
                        next(name for name, specimen in vars(NamedLattices).items() if specimen is block),
                        count,
                    )
                    for (block, *_invariants), count in zip(block_data, counts, strict=True)
                    if count
                )
                realizations.append(_orthogonal_sum(recipe))
            return
        _block, block_positive, block_negative, block_length, block_delta = block_data[index]
        count = 0
        while count * block_positive <= positive and count * block_negative <= negative and count * block_length <= length and (count == 0 or block_delta <= target_delta):
            extend(
                index + 1,
                positive - count * block_positive,
                negative - count * block_negative,
                length - count * block_length,
                max(realized_delta, block_delta) if count else realized_delta,
                counts + (count,),
            )
            count += 1

    extend(
        0,
        positive_target,
        negative_target,
        target_a,
        0,
        (),
    )
    return finite_ordered_set(tuple(realizations))


def signature_orthogonal_sums(target_signature, blocks):
    r"""Enumerate multisets of the supplied blocks with the target signature."""
    positive_target = int(target_signature.first())
    negative_target = int(target_signature.second())
    if min(positive_target, negative_target) < 0:
        raise ValueError("signature indices are nonnegative")
    if positive_target + negative_target == 0:
        raise ValueError("the zero lattice is not a nonempty block sum")
    block_data = tuple(
        (block, int(block.signature_pair().first()), int(block.signature_pair().second()))
        for block in blocks
    )
    if any(positive + negative == 0 for _block, positive, negative in block_data):
        raise ValueError("rank-zero blocks make multiset enumeration unbounded")
    realizations = []

    def extend(index, positive, negative, selected):
        if index == len(block_data):
            if positive == negative == 0:
                result = None
                for (block, _p, _q), count in zip(block_data, selected, strict=True):
                    for _copy in range(count):
                        result = block if result is None else result + block
                realizations.append(result)
            return
        _block, block_positive, block_negative = block_data[index]
        count = 0
        while count * block_positive <= positive and count * block_negative <= negative:
            extend(
                index + 1,
                positive - count * block_positive,
                negative - count * block_negative,
                selected + (count,),
            )
            count += 1

    extend(0, positive_target, negative_target, ())
    return finite_ordered_set(tuple(realizations))


_TCO_GENS = tuple(NamedLattices.Tco.module_generators())
_TEN_GENS = tuple(NamedLattices.TEn.module_generators())
_TDP_GENS = tuple(NamedLattices.TdP.module_generators())
_LK3_GENS = tuple(NamedLattices.LK3.module_generators())


class Involutions:
    r"""Named involutions of the K3 lattice in its displayed block framing."""

    I_dP = NamedLattices.LK3.Aut()(
        (
            *(-generator for generator in _LK3_GENS[0:2]),
            *_LK3_GENS[4:6],
            *_LK3_GENS[2:4],
            *(-generator for generator in _LK3_GENS[6:22]),
        )
    )
    I_En = NamedLattices.LK3.Aut()(
        (
            *(-generator for generator in _LK3_GENS[0:2]),
            *_LK3_GENS[4:6],
            *_LK3_GENS[2:4],
            *_LK3_GENS[14:22],
            *_LK3_GENS[6:14],
        )
    )
    I_Nik = NamedLattices.LK3.Aut()(
        (
            *_LK3_GENS[0:6],
            *(-generator for generator in _LK3_GENS[14:22]),
            *(-generator for generator in _LK3_GENS[6:14]),
        )
    )


class Embeddings:
    E8_2_into_TdP = NamedLattices.E8_2.Emb(NamedLattices.TdP)(tuple(_TDP_GENS[4 + index] + _TDP_GENS[12 + index] for index in range(8)))

    TCo_into_TEn = NamedLattices.Tco.Emb(NamedLattices.TEn)(
        (
            _TEN_GENS[0] + _TEN_GENS[1],
            _TEN_GENS[2],
            _TEN_GENS[3],
            *_TEN_GENS[4:12],
        )
    )

    TEn_into_TdP = NamedLattices.TEn.Emb(NamedLattices.TdP)(
        (
            _TDP_GENS[0],
            _TDP_GENS[1],
            _TDP_GENS[2],
            _TDP_GENS[3],
            *tuple(_TDP_GENS[4 + index] + _TDP_GENS[12 + index] for index in range(8)),
        )
    )

    TdP_into_LK3 = NamedLattices.TdP.Emb(NamedLattices.LK3)(
        (
            _LK3_GENS[0],
            _LK3_GENS[1],
            _LK3_GENS[2] - _LK3_GENS[4],
            _LK3_GENS[3] - _LK3_GENS[5],
            *_LK3_GENS[6:14],
            *(-generator for generator in _LK3_GENS[14:22]),
        )
    )

    TEn_into_LK3 = TdP_into_LK3 * TEn_into_TdP

    _u_e8_generators = tuple(NamedLattices.U_E8_2.module_generators())
    U_E8_2_into_TEn = NamedLattices.U_E8_2.Emb(NamedLattices.TEn)(
        (
            _TEN_GENS[0] + _TEN_GENS[2] + _TEN_GENS[3] - _TEN_GENS[4],
            _TEN_GENS[1] + _TEN_GENS[2] + _TEN_GENS[3] - _TEN_GENS[4],
            _TEN_GENS[2] - _TEN_GENS[3],
            _TEN_GENS[5],
            _TEN_GENS[3] + _TEN_GENS[6],
            *_TEN_GENS[7:12],
        )
    )


__all__ = [
    "Embeddings",
    "Involutions",
    "NamedLattices",
    "NegativeDefTwoElementary",
    "TwoElementary",
    "signature_orthogonal_sums",
    "two_elementary_orthogonal_sums",
    "validate_negative_def_two_elementary_table",
    "validate_two_elementary_table",
]
