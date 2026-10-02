"""The genus invariants of integral lattices, computed by SageMath: run by `latticedb certify` under `sage -python`.

Reads from standard input a JSON object `{"seconds": s, "lattices": [{"tag", "gram", "sign", "fields"}, ...]}`,
where `sign` is 1 for a positive definite lattice, -1 for a negative definite one and 0 otherwise, and
`fields` names the values to compute among `genus_symbol`, `genus_class_count`, `spinor_genus_count`, `spinor_genera`, `hyperbolic_index`,
`automorphism_group_order` and `primitive_orbits`. Writes one JSON line per lattice to standard output, as soon as it is
computed: the tag, the version of SageMath as `by`, and each value of `fields`. A value that is not
computed within `s` seconds is null.

The module imports SageMath and nothing of `latticedb`, whose environment does not have SageMath.
"""

import json
import sys
from collections.abc import Callable, Mapping, Sequence, Sized
from functools import partial
from itertools import chain, combinations
from typing import TypedDict

from cysignals.alarm import alarm, cancel_alarm
from cysignals.signals import AlarmInterrupt
from sage.all import QQ, ZZ, Integer, gcd, matrix, pari
from sage.groups.fqf_orthogonal import FqfIsometry
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.matrix.special import block_diagonal_matrix
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
from sage.modules.torsion_quadratic_module import TorsionQuadraticModuleElement
from sage.quadratic_forms.binary_qf import BinaryQF
from sage.quadratic_forms.genera.genus import Genus, genera
from sage.quadratic_forms.quadratic_form import QuadraticForm
from sage.quadratic_forms.quadratic_form__neighbors import neighbor_iteration
from sage.sets.primes import Primes
from sage.version import version


class Request(TypedDict):
    tag: str
    gram: list[list[int]]
    sign: int
    fields: list[str]


def symbol(gram: Matrix_integer_dense) -> str:
    """`I` or `II` with the signature pair, then, when the determinant is not 1 or -1, the local symbol at each prime of twice the determinant as SageMath prints it."""
    genus = Genus(gram)
    positive, negative = genus.signature_pair()
    head = f"{'II' if genus.is_even() else 'I'}_{{{positive},{negative}}}"
    if abs(gram.det()) == 1:
        return head
    local = [f"{local_symbol.prime()}: {repr(local_symbol).split(':', 1)[1].strip()}" for local_symbol in genus.local_symbols()]
    return f"{head} ({'; '.join(local)})"


def class_count(gram: Matrix_integer_dense) -> int:
    """The number of isometry classes in the genus of `gram`.

    `representatives(backend="sage")` avoids Magma, which SageMath calls by default for a definite form of rank more than 6.
    For an indefinite binary form it lists every reduced form of each cycle, so the forms are counted up to improper equivalence.
    """
    representatives = Genus(gram).representatives(backend="sage")
    if gram.nrows() != 2 or gram.det() > 0:
        return len(representatives)
    classes: list[BinaryQF] = []
    for form in (BinaryQF(r[0, 0], 2 * r[0, 1], r[1, 1]) for r in representatives):
        if not any(form.is_equivalent(other, proper=False) for other in classes):
            classes.append(form)
    return len(classes)


def spinor_genus_count(gram: Matrix_integer_dense) -> int:
    """The number of spinor genera in the genus of a Gram matrix of rank at least 3.

    `spinor_generators(proper=False)` adds a prime p only when its spinor operator is not in the subgroup that the spinor kernel and
    the operators already chosen generate, so the operators of the primes are independent in the quotient, an elementary abelian 2-group.
    """
    count: int = 2 ** len(Genus(gram).spinor_generators(proper=False))
    return count


def _neighbour(form: QuadraticForm[Integer], p: Integer) -> QuadraticForm[Integer]:
    # From no previous vector, the search returns the first primitive vector of (Z/pZ)^n with Q(v) = 0 mod p, and None only when there is none.
    vector = form.find_primitive_p_divisible_vector__next(p)
    assert vector is not None, f"the form has no primitive vector of norm divisible by {p}"
    return form.find_p_neighbor_from_vec(p, vector)


def spinor_genera(gram: Matrix_integer_dense, sign: int) -> list[int]:
    """The number of classes in each spinor genus of the genus of a Gram matrix of rank at least 3: that of `gram` first, then the others in decreasing order.

    An indefinite genus has one class in each spinor genus (SPLAG, Chapter 15, Theorem 14). For a definite one, M is a p-neighbour of L when
    [L : L n M] = [M : L n M] = p, so its spinor genus is that of L times the spinor operator of p (SPLAG, Chapter 15, Theorem 15).
    A product of neighbours at the primes of `spinor_generators` reaches each spinor genus once; the p-neighbours at a prime p in the spinor kernel
    stay in the spinor genus. The neighbours are found by `algorithm="orbits"`, which computes every neighbour up to the isometries of the form,
    and the masses 1/|O(M)| of the classes found must add up to the mass of the genus, so that no class is missing.
    `_improper_spinor_kernel` is the method of SageMath that gives the spinor kernel.
    """
    genus = Genus(gram)
    count = spinor_genus_count(gram)
    if sign == 0:
        return [1] * count
    spinor_operators, kernel = genus._improper_spinor_kernel()
    primes = genus.spinor_generators(proper=False)
    # A Hessian matrix of SageMath is twice the Gram matrix of its form, so an odd Gram matrix is doubled.
    form = QuadraticForm(ZZ, (sign if genus.is_even() else 2 * sign) * gram)
    p = ZZ(2)
    while p.divides(genus.determinant()) or spinor_operators.delta(p) not in kernel:
        p = Primes().next(p)
    classes: list[list[QuadraticForm[Integer]]] = []
    for chosen in chain.from_iterable(combinations(primes, size) for size in range(len(primes) + 1)):
        seed = form
        for q in chosen:
            seed = _neighbour(seed, q)
        classes.append(neighbor_iteration([seed], int(p), algorithm="orbits", max_classes=10**6))
    mass = sum(QQ(1) / found.number_of_automorphisms() for spinor_genus in classes for found in spinor_genus)
    assert mass == form.conway_mass(), f"the classes found in the spinor genera of {gram.list()} have mass {mass}, and the genus {form.conway_mass()}"
    return [len(classes[0]), *sorted((len(spinor_genus) for spinor_genus in classes[1:]), reverse=True)]


def hyperbolic_index(gram: Matrix_integer_dense) -> int:
    """The largest n with L isometric to U^n + L', for the hyperbolic plane U.

    A lattice U + L' of rank at least 3 is alone in its genus (Nikulin 1980, Theorem 1.13.1*), and the
    even unimodular lattice of signature (n, n) is U^n. So L is isometric to U^n + L' for some L' exactly
    when the genus of L is the sum of the genus of U^n and a genus of signature (p - n, q - n) and
    determinant (-1)^n det(L), with the parity of L.
    """
    genus = Genus(gram)
    positive, negative = genus.signature_pair()
    plane = matrix(ZZ, [[0, 1], [1, 0]])
    for n in range(min(positive, negative), 0, -1):
        planes = Genus(block_diagonal_matrix([plane] * n))
        if (positive, negative) == (n, n):
            if genus == planes:
                return n
            continue
        complements = genera((positive - n, negative - n), (-1) ** n * gram.det(), even=genus.is_even())
        if any(complement.direct_sum(planes) == genus for complement in complements):
            return n
    return 0


ORBIT_NORM_BOUND = 4
"""The series of orbits of primitive vectors are computed through the coefficients of z^4 and w^4."""

Series = dict[str, int | list[int]]
"""The coefficients of a series F_{L,Gamma}: `constant`, and the lists `z` and `w` of the coefficients of z^n and w^n for n = 1, 2, ..."""

Value = int | str | list[int] | dict[str, Series]


def _discriminant_actions(gram: Matrix_integer_dense, generators: list[Matrix_integer_dense]) -> tuple[list[int], list[Matrix_integer_dense]]:
    """The invariant factors d_i > 1 of A_L, and for each isometry g the matrix by which it acts on A_L in the coordinates of these factors.

    With L* = G^{-1} Z^n, multiplication by G identifies L*/L with Z^n / G Z^n, and g acts there by G g G^{-1} = g^{-T}.
    For U G V = D in Smith form, the coordinates of y in Z^n / G Z^n are the entries of U y modulo the diagonal of D.
    """
    smith, left, _ = gram.smith_form()
    kept = [index for index in range(gram.nrows()) if abs(smith[index, index]) > 1]
    factors = [abs(int(smith[index, index])) for index in kept]
    # U and the isometries g are unimodular, so their inverses are integer matrices.
    left_inverse = left.inverse_of_unit()
    actions = []
    for g in generators:
        action = left * g.inverse_of_unit().transpose() * left_inverse
        actions.append(action.matrix_from_rows_and_columns(kept, kept))
    return factors, actions


def _orbit_counts(vectors: Matrix_integer_dense, generators: list[Matrix_integer_dense], quotient: list[list[int]], size: int) -> list[int]:
    """For each column x of `vectors`, a label of the orbit of (x, 1), where the orbits are those of the group on (column, element of the image Q).

    `quotient[k][q]` is the index of the product of the image of generator k with the element of index q of Q, for q = 0, ..., size - 1.
    For a surjection phi: G -> Q with kernel H, the H-orbits on X correspond to the G-orbits on X x Q through
    x -> (x, 1): the G-orbit of (x, 1) meets X x {1} in the H-orbit of x, and every G-orbit meets X x {1}.
    """
    columns = {tuple(column): index for index, column in enumerate(vectors.columns())}
    parent = list(range(len(columns) * size))

    def root(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    for g, multiply in zip(generators, quotient, strict=True):
        images = [columns[tuple(column)] for column in (g * vectors).columns()]
        for x, image in enumerate(images):
            for q in range(size):
                a, b = root(x * size + q), root(image * size + multiply[q])
                if a != b:
                    parent[a] = b
    return [root(x * size) for x in range(len(columns))]


def _closure(identity: tuple[int, ...], generators: Sequence[Callable[[tuple[int, ...]], tuple[int, ...]]]) -> list[tuple[int, ...]]:
    """The elements of the group generated by `generators`, as the orbit of `identity` under them."""
    found = {identity: None}
    frontier = [identity]
    while frontier:
        element = frontier.pop()
        for generator in generators:
            image = generator(element)
            if image not in found:
                found[image] = None
                frontier.append(image)
    return list(found)


def primitive_orbits(gram: Matrix_integer_dense, sign: int) -> dict[str, Series]:
    """The series F_{L,Gamma} through z^4 and w^4: of a definite lattice by its vectors, of an even indefinite one that contains U^2 from A_L."""
    return _definite_orbits(gram, sign) if sign != 0 else _hyperbolic_orbits(gram)


def _hyperbolic_orbits(gram: Matrix_integer_dense) -> dict[str, Series]:
    """The series F_{L,Gamma} of an even lattice L = U^2 + L_1, for the eight groups Gamma.

    `latticedb certify` asks for it only when L is even and contains U^2. A primitive vector v of norm n gives
    alpha = v / div(v) + L, of order div(v) with q_L(alpha) = n / div(v)^2 in Q/2Z; S_n is the set of the alpha of order d
    with q_L(alpha) = n / d^2. The SO~+(L)-orbits of primitive vectors of norm n correspond to S_n (Gritsenko, Hulek and
    Sankaran 2009, Proposition 3.3(i)), and SO~+(L) is normal in O(L). So c_Gamma(n) is the number of orbits on S_n of the
    image of Gamma in O(q_L): the trivial group for the four groups in O~(L), and O(q_L) for the four others (theory/orbits.md).
    """
    lattice = IntegralLattice(gram)
    assert lattice.is_even(), "the series of an indefinite lattice is computed only for an even one"
    discriminant = lattice.discriminant_group()
    elements = list(discriminant)
    classes = {n: [alpha for alpha in elements if alpha.q() == QQ(n) / alpha.order() ** 2] for n in range(-ORBIT_NORM_BOUND, ORBIT_NORM_BOUND + 1)}
    generators = discriminant.orthogonal_group().gens()
    orbits = {n: _orbits(alphas, generators) for n, alphas in classes.items()}
    series: dict[str, Mapping[int, Sized]] = {
        "Otilde": classes,
        "SOtilde": classes,
        "Otilde+": classes,
        "SOtilde+": classes,
        "O": orbits,
        "SO": orbits,
        "O+": orbits,
        "SO+": orbits,
    }
    return {
        group: {
            "constant": len(counted[0]),
            "z": [len(counted[n]) for n in range(1, ORBIT_NORM_BOUND + 1)],
            "w": [len(counted[-n]) for n in range(1, ORBIT_NORM_BOUND + 1)],
        }
        for group, counted in series.items()
    }


def _orbits(elements: list[TorsionQuadraticModuleElement], generators: tuple[FqfIsometry, ...]) -> list[list[TorsionQuadraticModuleElement]]:
    """The orbits on `elements`, a set that the group generated by `generators` preserves."""
    found: list[list[TorsionQuadraticModuleElement]] = []
    seen: set[TorsionQuadraticModuleElement] = set()
    for start in elements:
        if start in seen:
            continue
        orbit = [start]
        seen.add(start)
        for element in orbit:
            for generator in generators:
                image = generator(element)
                if image not in seen:
                    seen.add(image)
                    orbit.append(image)
        found.append(orbit)
    return found


def _definite_orbits(gram: Matrix_integer_dense, sign: int) -> dict[str, Series]:
    """The series F_{L,Gamma} of a definite lattice through z^4 and w^4, for the eight groups Gamma.

    `gram` is positive definite: the Gram matrix of L, or of L(-1) when `sign` is -1. PARI's `qfauto` gives generators g of O(L)
    with g^T G g = G, acting on column vectors, and `qfminim` the vectors x with x^T G x <= 4 up to sign.
    SO(L) is the kernel of det, O~(L) the kernel of the action on A_L, and SO~(L) the kernel of both.
    The real spinor norm of a reflection in w is -b(w, w)/2 modulo squares (Dawes 2022, (4)); on a positive definite lattice it is -1,
    so O+ = SO, and on a negative definite lattice it is 1, so O+ = O.
    """
    generators = [matrix(ZZ, g) for g in pari(gram).qfauto()[1]]
    half = matrix(ZZ, pari(gram).qfminim(ORBIT_NORM_BOUND)[2]).columns()
    primitive = [x for x in half if gcd(list(x)) == 1]
    vectors = matrix(ZZ, primitive + [-x for x in primitive]).transpose() if primitive else matrix(ZZ, gram.nrows(), 0)
    norms = [int(x * gram * x) for x in vectors.columns()]
    factors, actions = _discriminant_actions(gram, generators)
    determinants = [int(g.det()) for g in generators]
    order = len(factors)
    counts: dict[str, list[int]] = {}
    for group, (with_determinant, with_discriminant) in {"O": (False, False), "SO": (True, False), "Otilde": (False, True), "SOtilde": (True, True)}.items():
        identity = (1, *(int(i == j) for i in range(order) for j in range(order))) if with_discriminant else (1,)
        moves = [partial(_quotient_action, actions[k], factors, determinants[k], with_determinant, with_discriminant) for k in range(len(generators))]
        elements = _closure(identity, moves)
        index = {element: position for position, element in enumerate(elements)}
        quotient = [[index[move(element)] for element in elements] for move in moves]
        roots = _orbit_counts(vectors, generators, quotient, len(elements))
        counts[group] = [len({roots[x] for x in range(len(norms)) if norms[x] == n}) for n in range(1, ORBIT_NORM_BOUND + 1)]
    zeros = [0] * ORBIT_NORM_BOUND
    plus = {"O+": "SO", "SO+": "SO", "Otilde+": "SOtilde", "SOtilde+": "SOtilde"} if sign > 0 else {"O+": "O", "SO+": "SO", "Otilde+": "Otilde", "SOtilde+": "SOtilde"}
    counts |= {group: counts[source] for group, source in plus.items()}
    return {group: {"constant": 0, "z": values if sign > 0 else zeros, "w": zeros if sign > 0 else values} for group, values in counts.items()}


def _quotient_action(
    action: Matrix_integer_dense, factors: list[int], determinant: int, with_determinant: bool, with_discriminant: bool, element: tuple[int, ...]
) -> tuple[int, ...]:
    """Left multiplication by the image of an isometry on an element (det, the columns of an endomorphism of A_L) of the image Q."""
    sign_part = element[0] * determinant if with_determinant else 1
    if not with_discriminant:
        return (sign_part,)
    order = len(factors)
    current = matrix(ZZ, order, order, list(element[1:])).transpose()
    product = action * current
    return (sign_part, *(int(product[i, j]) % factors[i] for j in range(order) for i in range(order)))


def within(seconds: int, compute: Callable[[], Value]) -> Value | None:
    """The value of `compute`, or None when it takes more than `seconds` seconds."""
    alarm(seconds)
    # SageMath interrupts a computation only by raising AlarmInterrupt in it.
    try:
        value = compute()
    except AlarmInterrupt:
        return None
    cancel_alarm()
    return value


def automorphism_group_order(gram: Matrix_integer_dense) -> int:
    """The order of O(L) of a positive definite Gram matrix, by `qfauto` of PARI/GP."""
    return int(pari(gram).qfauto()[0])


def main() -> None:
    task = json.load(sys.stdin)
    seconds: int = task["seconds"]
    lattices: list[Request] = task["lattices"]
    for lattice in lattices:
        gram = matrix(ZZ, lattice["gram"])
        positive = gram if lattice["sign"] >= 0 else -gram
        computations: dict[str, Callable[[], Value]] = {
            "genus_symbol": partial(symbol, gram),
            "genus_class_count": partial(class_count, gram),
            "spinor_genus_count": partial(spinor_genus_count, gram),
            "spinor_genera": partial(spinor_genera, gram, lattice["sign"]),
            "hyperbolic_index": partial(hyperbolic_index, gram),
            "automorphism_group_order": partial(automorphism_group_order, positive),
            "primitive_orbits": partial(primitive_orbits, positive, lattice["sign"]),
        }
        line: dict[str, Value | None] = {"tag": lattice["tag"], "by": f"SageMath {version}"}
        for field in lattice["fields"]:
            line[field] = within(seconds, computations[field])
        print(json.dumps(line), flush=True)


if __name__ == "__main__":
    main()
