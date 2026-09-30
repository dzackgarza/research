"""Write the seed corpus `lattices/<TAG>.md`: about ten lattices of each rank from 1 to 20.

Usage, from `lattice-database/`: just seed

The script constructs each lattice in SageMath, computes every recorded
invariant from the components `b(e_i, e_j)` of its Gram tensor, and writes one
Markdown file with YAML front matter. It refuses to run when `lattices/`
already holds records, because tags are permanent after the first corpus.

Conventions of PARI/GP that the script relies on (checked on `Z^2` and `E8`):
`qfminim()` returns the number of minimal vectors, both signs counted, and
the minimum; `qfrep(B)` returns, for k = 1..B, half the number of vectors
with `b(x, x) = k`; `qfauto()[0]` is the order of the isometry group;
`qfsolve()` returns a vector when the form is isotropic and a prime otherwise.
"""

import json
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from cypari2.handle_error import PariError
from cysignals.alarm import AlarmInterrupt, alarm, cancel_alarm
from sage.all import QQ, ZZ, CartanMatrix, Graph, QuadraticForm, block_diagonal_matrix, identity_matrix, latex, lcm, matrix, pari, span
from sage.quadratic_forms.genera.genus import Genus
from sage.version import version as SAGE_VERSION

CORPUS = Path("lattices")
CATALOGUE = Path("scripts/nebe_sloane")
COMPUTED_WITH = f"SageMath {SAGE_VERSION}, PARI/GP"
AUTOMORPHISM_SECONDS = 120
THETA_SECONDS = 30
ALEXEEV = {
    "citation": 'V. Alexeev, "Reflective hyperbolic 2-elementary lattices, K3 surfaces and hyperkahler manifolds", arXiv:2209.09110v4, Theorem 1.1.',
    "url": "https://arxiv.org/abs/2209.09110v4",
}
NOT_REFLECTIVE = {(17, 5, 1), (18, 4, 1), (19, 3, 1)}
"""Alexeev, Theorem 1.1: on the line r + a = 22, exactly these even hyperbolic 2-elementary lattices are not reflective."""


class Flow(list):
    """A list that YAML writes on one line."""


yaml.add_representer(Flow, lambda dumper, data: dumper.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=True))


@dataclass(frozen=True)
class Piece:
    """A lattice with a name: `gram` holds the components of its Gram tensor, `glossary` explains the symbols in its name."""

    name: str
    latex: str
    gram: matrix
    glossary: tuple[str, ...]


@dataclass
class Candidate:
    piece: Piece
    aliases: list[str] = field(default_factory=list)
    families: list[str] = field(default_factory=list)
    references: list[dict[str, str]] = field(default_factory=list)
    source: str = "Constructed in SageMath. The invariants were computed from the Gram tensor."
    url: str | None = None
    notes: list[str] = field(default_factory=list)
    reflective: bool | None = None


def rational(value) -> int | str:
    value = QQ(value)
    return int(value) if value.denominator() == 1 else f"{value.numerator()}/{value.denominator()}"


def root(letter: str, n: int) -> Piece:
    text = f"$X_n$, for $X$ one of $A$, $D$, $E$, is the root lattice of that type: $e_1, \\dots, e_n$ is a basis of simple roots, numbered as SageMath's `CartanMatrix` numbers them, and $b(e_i, e_j)$ is the entry $(i, j)$ of the Cartan matrix."
    return Piece(f"{letter}{n}", f"{letter}_{{{n}}}", matrix(QQ, CartanMatrix([letter, n])), (text,))


def affine(letter: str, n: int) -> Piece:
    text = (
        f"$\\widetilde{{{letter}}}_{{{n}}}$ is the root lattice of the affine root system of that type: the basis is a basis of simple roots, "
        "numbered as SageMath's `CartanMatrix` numbers them, and $b(e_i, e_j)$ is the entry $(i, j)$ of the affine Cartan matrix."
    )
    return Piece(f"affine {letter}{n}", f"\\widetilde{{{letter}}}_{{{n}}}", matrix(QQ, CartanMatrix([letter, n, 1])), (text,))


def rank_one(value) -> Piece:
    text = "$\\langle a \\rangle$ is the lattice of rank 1 with basis $e$ and $b(e, e) = a$."
    return Piece(f"<{QQ(value)}>", f"\\langle {latex(QQ(value))} \\rangle", matrix(QQ, [[value]]), (text,))


U = Piece("U", "U", matrix(QQ, [[0, 1], [1, 0]]), ("$U$ is the lattice with basis $e, f$ and $b(e, e) = b(f, f) = 0$, $b(e, f) = 1$.",))


def scaled(piece: Piece, factor: int) -> Piece:
    text = "$L(k)$ is the module $L$ with the form $k b$."
    return Piece(f"{piece.name}({factor})", f"{piece.latex}({factor})", factor * piece.gram, (*piece.glossary, text))


def dual_lattice(piece: Piece) -> Piece:
    text = (
        "$L^*$ is the dual lattice $\\{x \\in L \\otimes \\mathbb{Q} : b(x, y) \\in \\mathbb{Z} \\text{ for all } y \\in L\\}$ with the form $b$. "
        "Its basis is $e_1^*, \\dots, e_n^*$ with $b(e_i^*, e_j) = \\delta_{ij}$."
    )
    return Piece(f"{piece.name}*", f"{piece.latex}^{{*}}", piece.gram.inverse(), (*piece.glossary, text))


def orthogonal_sum(*terms: tuple[Piece, int]) -> Piece:
    text = "The basis of an orthogonal sum is the union of the bases of the summands, in the order written."
    name = " + ".join(piece.name if count == 1 else f"{piece.name}^{count}" for piece, count in terms)
    tex = " \\oplus ".join(piece.latex if count == 1 else f"{piece.latex}^{{{count}}}" for piece, count in terms)
    gram = block_diagonal_matrix([piece.gram for piece, count in terms for _ in range(count)], subdivide=False)
    glossary = tuple(dict.fromkeys(sentence for piece, _ in terms for sentence in piece.glossary))
    return Piece(name, tex, gram, (*glossary, text))


def standard(n: int) -> Piece:
    text = "$\\mathbb{Z}^n$ has the basis $e_1, \\dots, e_n$ with $b(e_i, e_j) = \\delta_{ij}$."
    return Piece(f"Z^{n}", f"\\mathbb{{Z}}^{{{n}}}", identity_matrix(QQ, n), (text,))


def odd_unimodular(p: int, q: int) -> Piece:
    text = "$\\mathrm{I}_{p,q}$ is the orthogonal sum of $p$ copies of $\\langle 1 \\rangle$ and $q$ copies of $\\langle -1 \\rangle$."
    gram = block_diagonal_matrix(identity_matrix(QQ, p), -identity_matrix(QQ, q), subdivide=False)
    return Piece(f"I_{{{p},{q}}}", f"\\mathrm{{I}}_{{{p},{q}}}", gram, (text,))


def d_plus(n: int) -> Piece:
    text = (
        "$D_n^+$ is the lattice in $\\mathbb{Q}^n$, with the standard form, that $D_n = \\{x \\in \\mathbb{Z}^n : x_1 + \\dots + x_n \\text{ even}\\}$ "
        "and the vector $(\\tfrac{1}{2}, \\dots, \\tfrac{1}{2})$ generate. The basis is an LLL-reduced basis."
    )
    rows = [[int(j == i) - int(j == i + 1) for j in range(n)] for i in range(n - 1)] + [[0] * (n - 2) + [1, 1], [QQ(1) / 2] * n]
    basis = span(rows, ZZ).basis_matrix()
    gram = basis * basis.transpose()
    change = gram.LLL_gram()
    return Piece(f"D{n}+", f"D_{{{n}}}^{{+}}", (change.transpose() * gram * change).change_ring(QQ), (text,))


def best_root(n: int) -> Piece:
    return root("E", n) if n in (6, 7, 8) else root("D", n) if n >= 4 else root("A", n)


def catalogue(entry: str, name: str, tex: str, aliases: list[str], families: list[str]) -> Candidate:
    data = json.loads((CATALOGUE / f"{entry}.json").read_text())
    gram = matrix(QQ, data["gram_tensor"])
    count, least = pari(gram.change_ring(ZZ)).qfminim()[:2]
    assert (gram.det(), int(least), int(count)) == (data["determinant"], data["minimal_norm"], data["kissing_number"]), f"{entry}: the catalogue values differ"
    notes = [f"The catalogue entry gives this reference text: {' '.join(data['references'])}"] if data["references"] else []
    return Candidate(
        Piece(name, tex, gram, (f"The components $b(e_i, e_j)$ are those of the section `GRAM` of the entry `{entry}` of the Catalogue of Lattices.",)),
        aliases=aliases,
        families=["nebe-sloane-catalogue", *families],
        references=[{"citation": f"G. Nebe and N. J. A. Sloane, Catalogue of Lattices, entry {entry}.", "url": data["url"]}],
        source=f"Catalogue of Lattices (G. Nebe, N. J. A. Sloane), entry {entry}. The invariants were computed again from the Gram tensor.",
        url=data["url"],
        notes=notes,
    )


def two_elementary_invariants(gram: matrix) -> tuple[int, int, int]:
    """`(r, a, delta)` of an even 2-elementary lattice: rank, rank of the discriminant group over Z/2, and coparity.

    Coparity is 0 when `b(x, x)` is an integer for every `x` in the dual lattice (Alexeev, section 2: `L^*(2)` is even).
    `b(x, x) = sum_i c_i^2 b(e_i^*, e_i^*) + 2 sum_{i<j} c_i c_j b(e_i^*, e_j^*)` and `2 b(e_i^*, e_j^*)` is an integer, so the diagonal decides.
    """
    divisors = [d for d in gram.change_ring(ZZ).elementary_divisors() if d != 1]
    assert all(d == 2 for d in divisors) and all(x % 2 == 0 for x in gram.diagonal()), "not an even 2-elementary lattice"
    return gram.nrows(), len(divisors), int(any(x not in ZZ for x in gram.inverse().diagonal()))


def alexeev(triple: tuple[int, int, int], *terms: tuple[Piece, int]) -> Candidate:
    piece = orthogonal_sum(*terms)
    assert two_elementary_invariants(piece.gram) == triple, f"{piece.name} does not have the invariants {triple}"
    reflective = triple not in NOT_REFLECTIVE
    notes = [
        f"This is the even hyperbolic 2-elementary lattice with invariants $(r, a, \\delta) = {triple}$: $r$ is the rank, the discriminant group is "
        "$(\\mathbb{Z}/2)^a$, and $\\delta = 0$ exactly when $b(x, x)$ is an integer for every $x$ in the dual lattice. "
        "An indefinite even 2-elementary lattice is determined by its signature and $(r, a, \\delta)$ (Nikulin; see the reference).",
        f"The lattice is on the line $r + a = 22$, and it is {'reflective' if reflective else 'not reflective'} (Alexeev, Theorem 1.1).",
    ]
    return Candidate(piece, aliases=[f"(r, a, delta) = {triple}"], families=["r-plus-a-22"], references=[ALEXEEV], notes=notes, reflective=reflective)


def candidates() -> list[Candidate]:
    a1m, d4m, e7m, e8m = scaled(root("A", 1), -1), scaled(root("D", 4), -1), scaled(root("E", 7), -1), scaled(root("E", 8), -1)
    found = [
        Candidate(rank_one(1), aliases=["Z", "I_1"], families=["diagonal"]),
        Candidate(rank_one(2), aliases=["A1"], families=["root-lattice"]),
        Candidate(rank_one(3)),
        Candidate(rank_one(4), aliases=["A1(2)"]),
        Candidate(rank_one(6)),
        Candidate(rank_one(QQ(1) / 2), aliases=["A1*"], families=["dual-root-lattice"]),
        Candidate(rank_one(-1), aliases=["I_{0,1}"], families=["diagonal"]),
        Candidate(rank_one(-2), aliases=["A1(-1)"]),
        Candidate(rank_one(-4)),
        Candidate(rank_one(0)),
    ]
    sums: dict[int, list[list[tuple[str, int, int]]]] = {
        2: [[("A", 1, 2)]],
        3: [[("A", 1, 3)], [("A", 2, 1), ("A", 1, 1)]],
        4: [[("A", 2, 2)], [("A", 1, 4)]],
        5: [[("A", 3, 1), ("A", 2, 1)], [("D", 4, 1), ("A", 1, 1)]],
        6: [[("A", 2, 3)], [("A", 3, 2)]],
        7: [[("D", 4, 1), ("A", 3, 1)], [("E", 6, 1), ("A", 1, 1)]],
        8: [[("D", 4, 2)], [("E", 7, 1), ("A", 1, 1)]],
        9: [[("E", 8, 1), ("A", 1, 1)]],
        10: [[("E", 8, 1), ("A", 2, 1)]],
        11: [[("E", 8, 1), ("A", 3, 1)]],
        12: [[("E", 8, 1), ("D", 4, 1)], [("E", 6, 2)]],
        13: [[("E", 8, 1), ("D", 5, 1)]],
        14: [[("E", 8, 1), ("E", 6, 1)], [("E", 7, 2)]],
        15: [[("E", 8, 1), ("E", 7, 1)]],
        16: [[("E", 8, 2)]],
        17: [[("E", 8, 2), ("A", 1, 1)]],
        18: [[("E", 8, 2), ("A", 2, 1)]],
        19: [[("E", 8, 2), ("A", 3, 1)]],
        20: [[("E", 8, 2), ("D", 4, 1)]],
    }
    even_unimodular = {2: (1, 0), 4: (2, 0), 6: (3, 0), 8: (4, 0), 10: (1, 1), 12: (2, 1), 14: (3, 1), 16: (4, 1), 18: (1, 2), 20: (2, 2)}
    affine_types = {2: ("A", 1), 3: ("A", 2), 4: ("A", 3), 5: ("D", 4), 6: ("D", 5), 7: ("E", 6), 8: ("E", 7), 9: ("E", 8)}
    anisotropic = {2: [(1, 1), (-2, 1)], 3: [(1, 2), (-3, 1)], 4: [(1, 3), (-7, 1)]}
    specials: dict[int, list[Candidate]] = {
        2: [Candidate(scaled(U, 2)), Candidate(orthogonal_sum((rank_one(2), 1), (rank_one(-2), 1)))],
        3: [Candidate(orthogonal_sum((scaled(U, 2), 1), (rank_one(-2), 1)))],
        4: [Candidate(orthogonal_sum((U, 1), (scaled(U, 2), 1))), Candidate(orthogonal_sum((scaled(U, 2), 2)))],
        7: [catalogue("KAPPA7", "K7", "K_{7}", ["KAPPA7"], [])],
        8: [Candidate(scaled(root("E", 8), 2)), catalogue("KAPPA8", "K8", "K_{8}", ["KAPPA8"], [])],
        9: [catalogue("KAPPA9", "K9", "K_{9}", ["KAPPA9"], [])],
        10: [Candidate(orthogonal_sum((U, 1), (scaled(root("E", 8), -2), 1))), Candidate(orthogonal_sum((scaled(U, 2), 1), (scaled(root("E", 8), -2), 1)))],
        11: [alexeev((11, 11, 1), (rank_one(2), 1), (a1m, 10))],
        12: [
            catalogue("K12", "K12", "K_{12}", ["Coxeter-Todd lattice"], []),
            Candidate(d_plus(12)),
            alexeev((12, 10, 1), (U, 1), (a1m, 10)),
            Candidate(orthogonal_sum((U, 2), (scaled(root("E", 8), -2), 1))),
        ],
        13: [alexeev((13, 9, 1), (U, 1), (d4m, 1), (a1m, 7))],
        14: [alexeev((14, 8, 0), (scaled(U, 2), 1), (d4m, 3)), alexeev((14, 8, 1), (U, 1), (d4m, 2), (a1m, 4))],
        15: [alexeev((15, 7, 1), (U, 1), (e7m, 1), (a1m, 6))],
        16: [
            catalogue("BW16", "BW16", "BW_{16}", ["Barnes-Wall lattice"], []),
            Candidate(d_plus(16)),
            alexeev((16, 6, 1), (U, 1), (e8m, 1), (a1m, 6)),
        ],
        17: [alexeev((17, 5, 1), (U, 1), (e8m, 1), (d4m, 1), (a1m, 3))],
        18: [alexeev((18, 4, 0), (U, 1), (e8m, 1), (d4m, 2)), alexeev((18, 4, 1), (U, 1), (e8m, 1), (scaled(root("D", 6), -1), 1), (a1m, 2))],
        19: [alexeev((19, 3, 1), (U, 1), (e8m, 1), (e7m, 1), (a1m, 2))],
        20: [Candidate(d_plus(20)), alexeev((20, 2, 1), (U, 1), (e8m, 2), (a1m, 2))],
    }
    for n in range(2, 21):
        found.append(Candidate(standard(n), aliases=[f"I_{{{n},0}}"], families=["diagonal"]))
        found.append(Candidate(root("A", n), families=["root-lattice"]))
        if n >= 4:
            found.append(Candidate(root("D", n), families=["root-lattice"]))
        if n in (6, 7, 8):
            found.append(Candidate(root("E", n), families=["root-lattice"]))
        if n >= 9:
            found.append(catalogue(f"LAMBDA{n}", f"Lambda{n}", f"\\Lambda_{{{n}}}", [f"LAMBDA{n}"], ["laminated"]))
        found.extend(specials.get(n, []))
        found.append(Candidate(odd_unimodular(1, n - 1), families=["diagonal"]))
        hyperbolic_root = root("E", n - 2) if n in (8, 9) else root("D", n - 2) if n >= 6 else root("A", n - 2)
        if n >= 3:
            found.append(Candidate(orthogonal_sum((U, 1), (scaled(hyperbolic_root, -1), 1))))
        if n in even_unimodular:
            planes, e8s = even_unimodular[n]
            terms = [(U, planes)] + ([(e8m, e8s)] if e8s else [])
            piece = orthogonal_sum(*terms) if len(terms) > 1 or planes > 1 else U
            found.append(Candidate(piece, aliases=[f"II_{{{planes},{planes + 8 * e8s}}}"], families=["even-unimodular"]))
        found.append(Candidate(dual_lattice(root("A", n)), families=["dual-root-lattice"]))
        if n >= 4:
            found.append(Candidate(dual_lattice(root("D", n)), families=["dual-root-lattice"]))
        if n in (6, 7):
            found.append(Candidate(dual_lattice(root("E", n)), families=["dual-root-lattice"]))
        for parts in sums[n]:
            found.append(Candidate(orthogonal_sum(*((root(letter, index), count) for letter, index, count in parts)), families=["root-lattice-sum"]))
        found.append(Candidate(scaled(best_root(n), -1)))
        if n >= 4:
            found.append(Candidate(odd_unimodular(2, n - 2), families=["diagonal"]))
        if n in affine_types:
            found.append(Candidate(affine(*affine_types[n]), families=["affine-root-lattice"]))
        if n in anisotropic:
            found.append(Candidate(orthogonal_sum(*((rank_one(value), count) for value, count in anisotropic[n]))))
    return found


def within(seconds: int, compute):
    """The value of `compute()`, or `None` when PARI needs more than the time limit or more than its stack."""
    try:
        alarm(seconds)
        value = compute()
        cancel_alarm()
        return value
    except AlarmInterrupt:
        return None
    except PariError as error:
        cancel_alarm()
        assert "the PARI stack overflows" in error.errtext(), error
        return None


def genus_symbol(gram: matrix) -> str:
    """`I` or `II`, the signature, and SageMath's p-adic symbols at the primes that divide twice the determinant. A unimodular lattice has only the first part."""
    genus = Genus(gram)
    p, q = genus.signature_pair()
    head = f"{'II' if genus.is_even() else 'I'}_{{{p},{q}}}"
    if abs(gram.det()) == 1:
        return head
    local = "; ".join(f"{symbol.prime()}: {str(symbol).split(':', 1)[1].strip()}" for symbol in genus.local_symbols())
    return f"{head} ({local})"


def root_components(gram: matrix) -> Flow:
    """Irreducible components of the root system of the vectors with `b(x, x) = 2`, for a positive definite integer-valued form."""
    short = pari(gram).qfminim(2, None, 0)[2].sage()
    roots = [column for column in short.columns() if column * gram * column == 2]
    graph = Graph([list(range(len(roots))), lambda i, j: i != j and roots[i] * gram * roots[j] != 0])
    names = []
    for component in graph.connected_components():
        rank, count = matrix(ZZ, [roots[i] for i in component]).rank(), 2 * len(component)
        kind = (
            f"A{rank}" if count == rank * (rank + 1) else f"D{rank}" if rank >= 4 and count == 2 * rank * (rank - 1) else f"E{rank}" if (rank, count) in ((6, 72), (7, 126), (8, 240)) else None
        )
        assert kind is not None, f"no irreducible simply laced root system has rank {rank} and {count} roots"
        names.append(kind)
    return Flow(sorted(names, key=lambda kind: (-int(kind[1:]), kind[0])))


def theta_bound(rank: int, minimum: int) -> int:
    return max(minimum, 12 if rank <= 4 else 8 if rank <= 8 else 6 if rank <= 12 else 4)


def invariants(gram: matrix) -> dict:
    n_plus, n_minus, n_zero = (int(value) for value in QuadraticForm(QQ, 2 * gram).signature_vector())
    determinant = gram.det()
    definite = n_zero == 0 and (n_plus == 0 or n_minus == 0)
    indefinite = n_plus > 0 and n_minus > 0
    definiteness = (
        "indefinite"
        if indefinite
        else ("positive_definite" if n_plus else "negative_definite")
        if definite
        else "positive_semidefinite"
        if n_plus
        else "negative_semidefinite"
        if n_minus
        else "zero"
    )
    record: dict = {"signature": Flow([n_plus, n_minus]), "determinant": rational(determinant), "definiteness": definiteness}
    integer_valued = all(value in ZZ for value in gram.list())
    scale = lcm([value.denominator() for value in gram.list()])
    if integer_valued:
        integers = gram.change_ring(ZZ)
        record["integral"] = {"parity": "even" if all(value % 2 == 0 for value in integers.diagonal()) else "odd"}
        if determinant != 0:
            record["integral"]["discriminant_group"] = Flow(int(abs(d)) for d in integers.elementary_divisors() if abs(d) > 1)
            record["integral"]["genus_symbol"] = genus_symbol(integers)
    if definite:
        sign = 1 if n_plus else -1
        form = pari((sign * scale * gram).change_ring(ZZ))
        count, least = form.qfminim()[:2]
        block: dict = {"minimum": rational(QQ(int(least)) / scale), "kissing_number": int(count)}
        order = within(AUTOMORPHISM_SECONDS, lambda: int(form.qfauto()[0]))
        if order is not None:
            block["automorphism_group_order"] = order
        if integer_valued:
            positive = (sign * gram).change_ring(ZZ)
            halves = within(THETA_SECONDS, lambda: [int(value) for value in pari(positive).qfrep(theta_bound(gram.nrows(), int(least)))])
            if halves is not None:
                block["theta_series"] = Flow([1, *(2 * value for value in halves)])
            block["root_system"] = root_components(positive) if int(least) <= 2 else Flow()
        record["definite"] = block
    if indefinite:
        record["indefinite"] = {"isotropic": n_zero > 0 or str(pari((scale * gram).change_ring(ZZ)).qfsolve().type()) == "t_COL"}
    return record


def same_lattice(first: matrix, second: matrix) -> bool:
    """Whether two candidates are known to be isometric: definite forms by PARI's `qfisom`, indefinite integral forms by equality of genus."""
    if first == second:
        return True
    if first.nrows() != second.nrows() or first.det() != second.det() or first.det() == 0:
        return False
    signatures = [QuadraticForm(QQ, 2 * gram).signature_vector() for gram in (first, second)]
    if signatures[0] != signatures[1]:
        return False
    scales = [lcm([value.denominator() for value in gram.list()]) for gram in (first, second)]
    if scales[0] != scales[1]:
        return False
    n_plus, n_minus, _ = signatures[0]
    if n_plus == 0 or n_minus == 0:
        sign = 1 if n_plus else -1
        return bool(pari((sign * scales[0] * first).change_ring(ZZ)).qfisom(pari((sign * scales[0] * second).change_ring(ZZ))))
    return scales[0] == 1 and Genus(first.change_ring(ZZ)) == Genus(second.change_ring(ZZ))


def main() -> None:
    CORPUS.mkdir(exist_ok=True)
    assert not any(CORPUS.iterdir()), "lattices/ already holds records; tags are permanent, so the seed does not write over a corpus"
    kept: list[Candidate] = []
    for candidate in candidates():
        twin = next((other for other in kept if same_lattice(other.piece.gram, candidate.piece.gram)), None)
        if twin is None:
            kept.append(candidate)
        else:
            twin.aliases.extend(name for name in (candidate.piece.name, *candidate.aliases) if name not in twin.aliases)
            print(f"{candidate.piece.name} is {twin.piece.name}")
    kept.sort(key=lambda candidate: candidate.piece.gram.nrows())
    tags = {candidate.piece.name: f"{index:04d}" for index, candidate in enumerate(kept, start=1)}
    for candidate in kept:
        piece = candidate.piece
        related = []
        for other in kept:
            if other is candidate or other.piece.gram.nrows() != piece.gram.nrows() or piece.gram.det() == 0:
                continue
            if other.piece.gram == -piece.gram:
                related.append({"tag": tags[other.piece.name], "relation": "The same module with the form \\(-b\\)."})
            elif other.piece.gram == piece.gram.inverse():
                related.append({"tag": tags[other.piece.name], "relation": "The dual lattice, in the basis dual to the basis of this record."})
            elif other.piece.gram == 2 * piece.gram:
                related.append({"tag": tags[other.piece.name], "relation": "The same module with the form \\(2b\\)."})
            elif 2 * other.piece.gram == piece.gram:
                related.append({"tag": tags[other.piece.name], "relation": "The same module with the form \\(\\tfrac{1}{2} b\\)."})
        record: dict = {
            "tag": tags[piece.name],
            "name": piece.name,
            "latex": piece.latex,
            "aliases": Flow(candidate.aliases),
            "rank": int(piece.gram.nrows()),
            "gram_tensor": [Flow(rational(value) for value in row) for row in piece.gram.rows()],
            **invariants(piece.gram),
            "families": Flow(candidate.families),
            "related": related,
            "references": candidate.references,
            "provenance": {"source": candidate.source, **({"url": candidate.url} if candidate.url else {}), "computed_with": COMPUTED_WITH},
        }
        if candidate.reflective is not None:
            record["hyperbolic"] = {"reflective": candidate.reflective}
        prose = "\n\n".join([" ".join(piece.glossary), *candidate.notes])
        text = "---\n" + yaml.dump(record, sort_keys=False, allow_unicode=True, width=100000) + "---\n\n" + prose + "\n"
        (CORPUS / f"{tags[piece.name]}.md").write_text(text)
        print(tags[piece.name], piece.name)


if __name__ == "__main__":
    main()
