r"""Combinatorial Vinberg invariant matrices and projective reflection geometry.

Mathematical Framework
======================
Let $V$ be a free module or vector space equipped with a symmetric bilinear form $b$.
For any pair of non-isotropic vectors $v_i, v_j \in V$, the **Vinberg invariant** is the
normalized projective ratio:

.. MATH::

    t(v_i, v_j) = \left[\, 4\,b(v_i, v_j)^2 \;:\; b(v_i, v_i)\,b(v_j, v_j) \,\right] \in \mathbb{P}^1(R)

where $\mathbb{P}^1(R) = \operatorname{ProjectiveSpace}(R, 1)$ is Sage's native projective line.

Properties of the Vinberg Invariant Matrix $T = (t_{ij})$:
----------------------------------------------------------
1. **Diagonal**: $t_{ii} = [4 : 1] = 4$.
2. **Off-Diagonal Values in $\mathbb{P}^1(R)$**:
   - $t_{ij} = (0 : 1) = 0 \iff m_{ij} = 2$ (orthogonal mirrors, $\theta = \pi/2$).
   - $t_{ij} = (1 : 1) = 1 \iff m_{ij} = 3$ (single bond, $\theta = \pi/3$).
   - $t_{ij} = (2 : 1) = 2 \iff m_{ij} = 4$ (double bond, $\theta = \pi/4$).
   - $t_{ij} = (3 : 1) = 3 \iff m_{ij} = 6$ (triple bond, $\theta = \pi/6$).
   - $t_{ij} = (4 : 1) = 4 \iff m_{ij} = \infty$ (parabolic / parallel mirrors meeting at $\partial\mathbb{H}^n$).
   - $t_{ij} = (k : 1)$ ($k > 4$) $\iff m_{ij} = \infty$ (hyperbolic / ultraparallel mirrors at distance $d > 0$).
   - $t_{ij} = (1 : 0) = \infty \iff$ isotropic root limit ($b(v_i, v_i) = 0$).

Bidirectional Reconstruction
============================
- **Gram Tensor $G$**: Given diagonal root norms $q_i = b(v_i, v_i)$ (default: $q_i = -2$):

  .. MATH::

      G_{ii} = q_i, \qquad G_{ij} = \frac{\sqrt{t_{ij} \cdot q_i \, q_j}}{2}

- **Schläfli Matrix $S$**: For unit normals ($q_i = 1$):

  .. MATH::

      S_{ii} = 1, \qquad S_{ij} = -\frac{\sqrt{t_{ij}}}{2}

- **Coxeter Bond Orders $m_{ij}$**: Directly mapped from $t_{ij}$.

EXAMPLES::

    sage: from dzack_research.preamble.categories.modules.projective_tensors import (
    ...       CombinatorialVinbergInvariantMatrix,
    ...       combinatorial_vinberg_invariant_matrix,
    ...       vinberg_invariant_matrix_from_gram
    ...   )
    sage: from sage.rings.integer_ring import ZZ
    sage: from sage.matrix.constructor import matrix

    # 1. Construct from a finite Gram tensor of simple roots:
    sage: G = matrix(ZZ, [
    ...       [-2,  1,  0],
    ...       [ 1, -2,  2],
    ...       [ 0,  2, -2]
    ...   ])
    sage: T = vinberg_invariant_matrix_from_gram(G)
    sage: T[0, 1]
    (1 : 1)
    sage: T[1, 2]
    (4 : 1)
    sage: T.coxeter_order(1, 2)
    +Infinity

    # 2. Reconstruct the Gram tensor from T:
    sage: G_rec = T.gram_tensor(root_norms=[-2, -2, -2])
    sage: G_rec == G
    True

    # 3. Reconstruct the Schläfli matrix:
    sage: S = T.schlafli_matrix()
    sage: S[0, 1]
    -1/2
    sage: S[1, 2]
    -1
"""

from collections.abc import Sequence
from typing import TYPE_CHECKING

from sage.categories.objects import Objects
from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix as SageCoxeterMatrix
from sage.functions.other import sqrt
from sage.matrix.constructor import matrix
from sage.modules.free_module import FreeModule
from sage.rings.infinity import Infinity, PlusInfinity, infinity
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.rings.real_mpfr import RR as SageRR
from sage.schemes.projective.projective_point import SchemeMorphism_point_projective_ring
from sage.schemes.projective.projective_space import ProjectiveSpace
from sage.structure.parent import Parent

if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.coxeter_diagrams import (
        FiniteCoxeterDiagram,
    )


# ---------------------------------------------------------------------------
# 1. Helper: Coerce to Projective Space Point in P^1(R)
# ---------------------------------------------------------------------------


def to_projective_point(P1: ProjectiveSpace, val: object) -> SchemeMorphism_point_projective_ring:
    r"""Coerce a scalar, infinity, or coordinate pair into a point in Sage's native ProjectiveSpace."""
    if isinstance(val, SchemeMorphism_point_projective_ring) and val.scheme() == P1:
        return val
    ring = P1.base_ring()
    if val is infinity or val is Infinity or isinstance(val, PlusInfinity) or str(val) in ("+Infinity", "oo", "infinity", "inf", "-1"):
        return P1([ring.one(), ring.zero()])
    elif isinstance(val, (tuple, list)) and len(val) == 2:
        return P1([ring(val[0]), ring(val[1])])
    else:
        return P1([ring(val), ring.one()])


# ---------------------------------------------------------------------------
# 2. Combinatorial Vinberg Invariant Matrix
# ---------------------------------------------------------------------------


class CombinatorialVinbergInvariantMatrix(Parent):
    r"""
    A Combinatorial Vinberg Invariant Matrix $T = (t_{ij}) \in \mathbb{P}^1(R)^{n \times n}$.

    Encodes the normalized projective angles and mirror distances of a reflection group.
    """

    def __init__(
        self,
        base_ring: object,
        entries: dict[tuple[int, int], SchemeMorphism_point_projective_ring],
        rank: int,
        names: Sequence[str] | None = None,
    ) -> None:
        self._rank = int(rank)
        self._projective_space = ProjectiveSpace(base_ring, 1, "x,y")
        self._names = tuple(names) if names is not None else tuple(f"v_{i}" for i in range(self._rank))

        # Enforce symmetry and diagonal = 4
        sym_entries = {}
        for i in range(self._rank):
            sym_entries[(i, i)] = self._projective_space([4, 1])
        for (i, j), pt in entries.items():
            if i != j:
                sym_entries[(i, j)] = pt
                sym_entries[(j, i)] = pt
        self._entries = sym_entries

        Parent.__init__(self, base=base_ring, category=Objects())

    def rank(self) -> int:
        r"""Return the number of vertices / generators."""
        return self._rank

    def variable_names(self) -> tuple[str, ...]:
        r"""Return vertex / generator names."""
        return self._names

    def projective_space(self) -> ProjectiveSpace:
        r"""Return the ambient projective space $\mathbb{P}^1(R)$."""
        return self._projective_space

    def __getitem__(self, index: tuple[int, int] | int) -> SchemeMorphism_point_projective_ring:
        r"""Return the Vinberg invariant $t_{ij} \in \mathbb{P}^1(R)$."""
        idx = index if isinstance(index, tuple) else (index, index)
        if idx[0] == idx[1]:
            return self._projective_space([4, 1])
        return self._entries.get(idx, self._projective_space([0, 1]))

    def entries(self) -> dict[tuple[int, int], SchemeMorphism_point_projective_ring]:
        r"""Return the dictionary of entries."""
        return dict(self._entries)

    def is_infinity(self, i: int, j: int) -> bool:
        r"""Return True if $t_{ij} = \infty$ (denominator coordinate is 0)."""
        return self[i, j][1] == 0

    def affine_ratio(self, i: int, j: int) -> object:
        r"""Return the affine scalar $t_{ij} = x/y$ if finite, else infinity."""
        pt = self[i, j]
        if pt[1] == 0:
            return infinity
        return pt[0] / pt[1]

    def coxeter_order(self, i: int, j: int) -> object:
        r"""Return the Coxeter bond exponent $m_{ij} \in \{1, 2, 3, 4, 6, \infty\}$."""
        if i == j:
            return Integer(1)
        pt = self[i, j]
        if pt[1] == 0:
            return infinity
        ratio = pt[0] / pt[1]
        if ratio == 0:
            return Integer(2)
        elif ratio == 1:
            return Integer(3)
        elif ratio == 2:
            return Integer(4)
        elif ratio == 3:
            return Integer(6)
        elif ratio >= 4:
            return infinity
        return infinity

    def to_sage_coxeter_matrix(self) -> SageCoxeterMatrix:
        r"""Export to Sage's native :class:`CoxeterMatrix`."""
        n = self._rank
        raw_entries = [
            [self.coxeter_order(i, j) for j in range(n)]
            for i in range(n)
        ]
        return SageCoxeterMatrix(raw_entries)

    def gram_tensor(self, root_norms: Sequence[object] | object = -2) -> matrix:
        r"""
        Reconstruct the Gram matrix $G = (b(v_i, v_j))$ given diagonal root norms $q_i = b(v_i, v_i)$.

        Args:
            root_norms: A sequence of diagonal norms $(q_1, \dots, q_n)$, or a scalar (default: -2).
        """
        n = self._rank
        if isinstance(root_norms, (int, Integer)):
            norms = [self.base_ring()(root_norms)] * n
        elif isinstance(root_norms, Sequence):
            assert len(root_norms) == n, f"Expected {n} root norms, got {len(root_norms)}"
            norms = [self.base_ring()(q) for q in root_norms]
        else:
            norms = [self.base_ring()(-2)] * n

        ring = self.base_ring()
        G_mat = [[ring.zero() for _ in range(n)] for _ in range(n)]

        for i in range(n):
            G_mat[i][i] = norms[i]
            for j in range(i + 1, n):
                pt = self[i, j]
                if pt[1] == 0:
                    raise ValueError(f"Cannot reconstruct finite Gram entry G[{i},{j}] from infinite Vinberg ratio [1 : 0]")
                t_val = pt[0] / pt[1]
                # G_ij = sqrt(t_ij * q_i * q_j) / 2
                val_sq = t_val * norms[i] * norms[j] / 4
                try:
                    val = ring(sqrt(val_sq))
                except Exception:
                    val = sqrt(val_sq)
                G_mat[i][j] = val
                G_mat[j][i] = val

        return matrix(G_mat)

    def schlafli_matrix(self) -> matrix:
        r"""
        Reconstruct the Schläfli matrix $S = (s_{ij})$ where $s_{ii} = 1$ and $s_{ij} = -\sqrt{t_{ij}}/2$.
        """
        n = self._rank
        S_mat = [[SageQQ.zero() for _ in range(n)] for _ in range(n)]

        for i in range(n):
            S_mat[i][i] = SageQQ.one()
            for j in range(i + 1, n):
                pt = self[i, j]
                if pt[1] == 0:
                    raise ValueError(f"Cannot reconstruct finite Schläfli entry from infinite ratio [1 : 0]")
                t_val = pt[0] / pt[1]
                val = -sqrt(t_val) / 2
                S_mat[i][j] = val
                S_mat[j][i] = val

        return matrix(S_mat)

    def submatrix(self, indices: Sequence[int]) -> "CombinatorialVinbergInvariantMatrix":
        r"""Return the induced sub-invariant matrix on the specified vertex subset."""
        idx_list = list(indices)
        n_sub = len(idx_list)
        sub_entries = {}
        for new_i, old_i in enumerate(idx_list):
            for new_j, old_j in enumerate(idx_list):
                sub_entries[(new_i, new_j)] = self[old_i, old_j]
        sub_names = tuple(self._names[i] for i in idx_list)
        return CombinatorialVinbergInvariantMatrix(self.base_ring(), sub_entries, n_sub, names=sub_names)

    def is_elliptic(self, indices: Sequence[int] | None = None) -> bool:
        r"""Check if the system (or sub-system) is elliptic (positive definite Schläfli matrix)."""
        target = self if indices is None else self.submatrix(indices)
        try:
            S = target.schlafli_matrix()
            return S.is_positive_definite()
        except ValueError:
            return False

    def is_parabolic(self, indices: Sequence[int] | None = None) -> bool:
        r"""Check if the system (or sub-system) is parabolic (positive semidefinite with rank n-1)."""
        target = self if indices is None else self.submatrix(indices)
        try:
            S = target.schlafli_matrix()
            return S.is_positive_semidefinite() and S.rank() == target.rank() - 1
        except ValueError:
            return False

    def is_hyperbolic(self, indices: Sequence[int] | None = None) -> bool:
        r"""Check if the system (or sub-system) is hyperbolic (signature (n-1, 1))."""
        target = self if indices is None else self.submatrix(indices)
        try:
            S = target.schlafli_matrix()
            return not S.is_positive_semidefinite() and S.det() < 0
        except ValueError:
            return True

    def _repr_(self) -> str:
        n = self._rank
        grid_rows = []
        for i in range(n):
            row_str = "  ".join(str(self[i, j]) for j in range(n))
            grid_rows.append(f"[{row_str}]")
        grid_repr = "\n".join(grid_rows)
        return f"Combinatorial Vinberg Invariant Matrix of rank {n} over {self.base_ring()}:\n{grid_repr}"

    def _latex_(self) -> str:
        n = self._rank
        rows_latex = []
        for i in range(n):
            row_latex = " & ".join(
                r"\infty" if self[i, j][1] == 0 else str(self[i, j][0] / self[i, j][1])
                for j in range(n)
            )
            rows_latex.append(row_latex)
        mat_latex = r" \\ ".join(rows_latex)
        return rf"\begin{{pmatrix}} {mat_latex} \end{{pmatrix}}"

    def _repr_latex_(self) -> str:
        return "$\\displaystyle " + self._latex_() + "$"


# ---------------------------------------------------------------------------
# 3. Constructor Functions
# ---------------------------------------------------------------------------


def vinberg_invariant_matrix_from_gram(
    G: matrix,
    names: Sequence[str] | None = None,
) -> CombinatorialVinbergInvariantMatrix:
    r"""
    Construct a CombinatorialVinbergInvariantMatrix from any finite Gram matrix $G$.

    Formula:
        $t_{ij} = [4\,G_{ij}^2 : G_{ii}\,G_{jj}] \in \mathbb{P}^1(R)$
    """
    n = G.nrows()
    ring = G.base_ring()
    P1 = ProjectiveSpace(ring, 1, "x,y")
    entries = {}

    for i in range(n):
        for j in range(i + 1, n):
            g_ij = G[i, j]
            g_ii = G[i, i]
            g_jj = G[j, j]

            if g_ij == 0:
                pt = P1([ring.zero(), ring.one()])  # (0 : 1)
            else:
                num = 4 * (g_ij ** 2)
                den = g_ii * g_jj
                if den == 0:
                    pt = P1([ring.one(), ring.zero()])  # (1 : 0)
                else:
                    pt = P1([ring(num), ring(den)])
            entries[(i, j)] = pt
            entries[(j, i)] = pt

    return CombinatorialVinbergInvariantMatrix(ring, entries, n, names=names)


def combinatorial_vinberg_invariant_matrix(
    base_ring: object,
    components: Sequence[Sequence[object]],
    names: Sequence[str] | None = None,
) -> CombinatorialVinbergInvariantMatrix:
    r"""
    Construct a CombinatorialVinbergInvariantMatrix from a nested matrix of $t_{ij}$ values.
    """
    assert isinstance(components, (list, tuple)), "Components must be a list or tuple"
    n_rows = len(components)
    P1 = ProjectiveSpace(base_ring, 1, "x,y")
    entries = {}

    for i in range(n_rows):
        row = components[i]
        assert len(row) == n_rows, f"Row {i} has length {len(row)}, expected {n_rows}"
        for j in range(n_rows):
            val = row[j]
            entries[(i, j)] = to_projective_point(P1, val)

    return CombinatorialVinbergInvariantMatrix(base_ring, entries, n_rows, names=names)
