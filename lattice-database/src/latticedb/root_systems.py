"""The irreducible reduced root systems: the Gram matrix of a base, and the number of roots.

A type is a letter `A` to `G` and a rank. The simple roots `alpha_1, ..., alpha_n`
are numbered as SageMath's `CartanMatrix` numbers them, and the form is the
one with `(alpha, alpha) = 2` for a short root `alpha`: the Gram matrix of the
simple roots is `CartanMatrix(type).symmetrized_matrix()`, and the number of
roots is `2 * len(RootSystem(type).ambient_space().positive_roots())`.
`B1`, `C1`, `C2`, `D1`, `D2` and `D3` are not types here: they are `A1`, `A1`,
`B2`, no root system, `A1 + A1` and `A3`.
"""

import re
from fractions import Fraction

TYPE_PATTERN = r"^(A[1-9]\d*|B[2-9]|B[1-9]\d+|C[3-9]|C[1-9]\d+|D[4-9]|D[1-9]\d+|E[678]|F4|G2)$"


def is_type(root_type: str) -> bool:
    """Whether the string names a type: `D3` and `E9` do not."""
    return re.match(TYPE_PATTERN, root_type) is not None


def _parts(root_type: str) -> tuple[str, int]:
    assert is_type(root_type), f"{root_type} is not the type of an irreducible reduced root system"
    return root_type[0], int(root_type[1:])


def _diagram(letter: str, rank: int) -> tuple[list[int], list[tuple[int, int]]]:
    """Return `(alpha_i, alpha_i)` for each `i`, and the pairs `(i, j)` with `(alpha_i, alpha_j) != 0`, from 0."""
    chain = [(i, i + 1) for i in range(rank - 1)]
    match letter:
        case "A":
            return [2] * rank, chain
        case "B":
            return [4] * (rank - 1) + [2], chain
        case "C":
            return [2] * (rank - 1) + [4], chain
        case "D":
            return [2] * rank, [*chain[:-1], (rank - 3, rank - 1)]
        case "E":
            return [2] * rank, [(0, 2), (1, 3), *((i, i + 1) for i in range(2, rank - 1))]
        case "F":
            return [4, 4, 2, 2], chain
        case "G":
            return [2, 6], chain
    raise AssertionError(letter)


def simple_root_gram(root_type: str) -> tuple[tuple[int, ...], ...]:
    """Return the components `(alpha_i, alpha_j)`.

    Two simple roots that are not orthogonal have
    `(alpha_i, alpha_j) = -max((alpha_i, alpha_i), (alpha_j, alpha_j)) / 2`:
    the Cartan integer `2 (alpha_i, alpha_j) / (alpha, alpha)` is `-1` for the
    longer root `alpha` of the two.
    """
    letter, rank = _parts(root_type)
    norms, edges = _diagram(letter, rank)
    gram = [[norms[i] if i == j else 0 for j in range(rank)] for i in range(rank)]
    for i, j in edges:
        gram[i][j] = gram[j][i] = -max(norms[i], norms[j]) // 2
    return tuple(tuple(row) for row in gram)


def root_count(root_type: str) -> int:
    """Return the number of roots."""
    letter, rank = _parts(root_type)
    match letter:
        case "A":
            return rank * (rank + 1)
        case "B" | "C":
            return 2 * rank * rank
        case "D":
            return 2 * rank * (rank - 1)
        case "E":
            return {6: 72, 7: 126, 8: 240}[rank]
        case "F":
            return 48
        case "G":
            return 12
    raise AssertionError(letter)


def root_lattice(root_type: str) -> tuple[str, int, Fraction]:
    """Return `(letter, rank, k)` such that the lattice `Q` that the simple roots generate is isometric to the standard lattice of that letter and rank with the form `k b`.

    The letter is `A`, `D`, `E` or `I`; `I` is the lattice `I_{n,0}`: the
    module `Z^n` with the Euclidean form `sum_i x_i y_i`. In the realisations
    of SageMath's `RootSystem(type).ambient_space()`, with the form scaled so
    that a short root has norm 2:

    - `B_n`: the roots are the `e_i` and the `e_i + e_j`, `e_i - e_j`, and they
      generate `Z^n`; `(e_i, e_i) = 1`, so `Q = I_{n,0}(2)`.
    - `C_n`: the roots are the `2 e_i` and the `e_i + e_j`, `e_i - e_j`, and
      they generate `D_n`; `D_3 = A_3`.
    - `F_4`: the roots are those of `B_4` and the `(e_1 + e_2 + e_3 + e_4) / 2`
      with signs, and they generate the dual lattice of `D_4`, which is
      isometric to `D_4(1/2)`; a short root has norm 1 there, so `Q = D_4`.
    - `G_2`: each long root is a sum of short roots, and the short roots are
      a root system of type `A_2`.
    """
    letter, rank = _parts(root_type)
    match letter:
        case "B":
            return "I", rank, Fraction(2)
        case "C":
            return ("A", 3, Fraction(1)) if rank == 3 else ("D", rank, Fraction(1))
        case "F":
            return "D", 4, Fraction(1)
        case "G":
            return "A", 2, Fraction(1)
    return letter, rank, Fraction(1)
