r"""Combinatorial Coxeter-Vinberg matrices and projective tensors.

Mathematical Distinction: Tensors vs. Coxeter-Vinberg Matrices
==============================================================
A fundamental distinction exists between geometric tensors and Coxeter-Vinberg matrices:

1. **Bilinear Form / Gram Matrix (Tensor)**:
   - A bilinear form $b \colon V \times V \to R$ is a genuine **$(0, 2)$-tensor** ($B \in \operatorname{Sym}^2(V^*)$).
   - In hyperbolic geometry ($\mathbb{H}^n$), the inner product $b(v, w)$ between root vectors
     is **always a finite scalar**:
     - Intersecting mirrors ($m < \infty$): $b(v_i, v_j) = -\cos(\pi/m) \in (-1, 0]$.
     - Parallel mirrors ($m = \infty$, cusp): $b(v_i, v_j) = -1$.
     - Ultraparallel mirrors ($m = \infty$, distance $d > 0$): $b(v_i, v_j) = -\cosh(d) < -1$.
   - The value $b(v, w) = \infty$ never occurs in the hyperbolic metric.

2. **Combinatorial Coxeter-Vinberg Matrix (Not a Tensor)**:
   - The matrix $M = (m_{ij})$ encodes the **group-theoretic relation exponents**:
     $$(s_i s_j)^{m_{ij}} = 1, \quad m_{ij} \in \{1, 2, 3, \ldots, \infty\}$$
   - It is a **combinatorial presentation object**, not a tensor:
     it does not transform under linear change of basis by congruence $P^T M P$.
   - The symbol $\infty$ denotes an infinite cyclic subgroup $\langle s_i s_j \rangle \cong \mathbb{Z}$
     (no relation between $s_i$ and $s_j$), not an infinite metric distance or infinite inner product.
   - The normalized angle ratio:

     .. MATH::

         t(r_i, r_j) = \left[ 4\,b(r_i, r_j)^2 \;:\; b(r_i, r_i)\,b(r_j, r_j) \right] \in \mathbb{P}^1(R)

     is a projective invariant in Sage's native $\mathbb{P}^1(R)$ classifying mirror pairs into:
     - $t = (0 : 1) \implies m = 2$ (orthogonal)
     - $t = (1 : 1) \implies m = 3$ (single bond)
     - $t = (2 : 1) \implies m = 4$ (double bond)
     - $t = (3 : 1) \implies m = 6$ (triple bond)
     - $t = (4 : 1) \implies m = \infty$ (parabolic / parallel mirrors)
     - $t = (k : 1)$ ($k > 4$) $\implies m = \infty$ (hyperbolic / divergent mirrors)
     - $t = (1 : 0) \implies \infty$ (isotropic root limit)

EXAMPLES::

    sage: from dzack_research.preamble.categories.modules.projective_tensors import CombinatorialCoxeterVinbergMatrix, combinatorial_coxeter_vinberg_matrix
    sage: from sage.rings.integer_ring import ZZ
    sage: from sage.rings.infinity import infinity
    sage: M = combinatorial_coxeter_vinberg_matrix(ZZ, [[-2, 1, 0], [1, -2, infinity], [0, infinity, -2]])
    sage: M.coxeter_matrix()
    [ 1  3  2]
    [ 3  1 -1]
    [ 2 -1  1]
    sage: M.vinberg_ratio(1, 2)
    (1 : 0)
"""

from collections.abc import Sequence
from typing import TYPE_CHECKING

from sage.categories.objects import Objects
from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix
from sage.matrix.constructor import matrix
from sage.modules.free_module import FreeModule
from sage.rings.infinity import Infinity, PlusInfinity, infinity
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ as SageZZ
from sage.schemes.projective.projective_point import SchemeMorphism_point_projective_ring
from sage.schemes.projective.projective_space import ProjectiveSpace
from sage.structure.parent import Parent

if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.coxeter_diagrams import (
        FiniteCoxeterDiagram,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        ModuleMorphism,
    )
    from dzack_research.preamble.lexicon import GramMatrix


# ---------------------------------------------------------------------------
# 1. Projective Space Helper using Sage's native ProjectiveSpace
# ---------------------------------------------------------------------------


def to_projective_point(P1: ProjectiveSpace, val: object) -> SchemeMorphism_point_projective_ring:
    r"""Coerce a value or coordinate pair into a point in Sage's native ProjectiveSpace."""
    if isinstance(val, SchemeMorphism_point_projective_ring) and val.scheme() == P1:
        return val
    ring = P1.base_ring()
    if val is infinity or val is Infinity or isinstance(val, PlusInfinity) or str(val) in ("+Infinity", "oo", "infinity", "inf"):
        return P1([ring.one(), ring.zero()])
    elif isinstance(val, (tuple, list)) and len(val) == 2:
        return P1([ring(val[0]), ring(val[1])])
    else:
        return P1([ring(val), ring.one()])


# ---------------------------------------------------------------------------
# 2. Combinatorial Coxeter-Vinberg Matrix
# ---------------------------------------------------------------------------


class CombinatorialCoxeterVinbergMatrix(Parent):
    r"""
    A Combinatorial Coxeter-Vinberg matrix encoding reflection relations and Vinberg invariants.

    Mathematical Properties:
    ------------------------
    - Encodes group presentation exponents $m_{ij} \in \{1, 2, 3, \ldots, \infty\}$.
    - Evaluates Vinberg projective ratios $t(r_i, r_j) \in \mathbb{P}^1(R)$.
    - This is a combinatorial presentation matrix, NOT a bilinear tensor.
    """

    def __init__(
        self,
        base_ring: object,
        entries: dict[tuple[int, int], SchemeMorphism_point_projective_ring],
        rank: int,
        names: Sequence[str] | None = None,
    ) -> None:
        self._rank = int(rank)
        self._names = tuple(names) if names is not None else tuple(f"e_{i}" for i in range(self._rank))
        self._projective_space = ProjectiveSpace(base_ring, 1, "x,y")

        # Enforce symmetry
        sym_entries = {}
        for (i, j), pt in entries.items():
            sym_entries[(i, j)] = pt
            sym_entries[(j, i)] = pt
        self._entries = sym_entries

        Parent.__init__(self, base=base_ring, category=Objects())

    def rank(self) -> int:
        r"""Return the number of generators / rank."""
        return self._rank

    def variable_names(self) -> tuple[str, ...]:
        r"""Return generator names."""
        return self._names

    def projective_space(self) -> ProjectiveSpace:
        r"""Return the ambient projective space $\mathbb{P}^1(R)$."""
        return self._projective_space

    def __getitem__(self, index: tuple[int, int] | int) -> SchemeMorphism_point_projective_ring:
        r"""Return the entry at (i, j) as a projective point."""
        idx = index if isinstance(index, tuple) else (index, index)
        assert len(idx) == 2, f"Expected 2D index, got {len(idx)}"
        return self._entries.get(idx, self._projective_space([0, 1]))

    def entries(self) -> dict[tuple[int, int], SchemeMorphism_point_projective_ring]:
        r"""Return all matrix entries."""
        return dict(self._entries)

    def vinberg_ratio(self, i: int, j: int) -> SchemeMorphism_point_projective_ring:
        r"""
        Return the Vinberg projective angle invariant $t(e_i, e_j) \in \mathbb{P}^1(R)$:

        .. MATH::

            t(e_i, e_j) = \left[ 4\,b(e_i, e_j)^2 \;:\; b(e_i, e_i)\,b(e_j, e_j) \right]
        """
        b_ij = self[i, j]
        b_ii = self[i, i]
        b_jj = self[j, j]

        x_ij, y_ij = b_ij[0], b_ij[1]
        x_ii, y_ii = b_ii[0], b_ii[1]
        x_jj, y_jj = b_jj[0], b_jj[1]

        if y_ij == 0:
            return self._projective_space([1, 0])
        if y_ii == 0 or y_jj == 0:
            return self._projective_space([0, 1])

        num = 4 * (x_ij ** 2) * y_ii * y_jj
        den = (y_ij ** 2) * x_ii * x_jj
        return self._projective_space([num, den])

    def coxeter_order(self, i: int, j: int) -> object:
        r"""Return the Coxeter bond order $m_{ij} \in \{1, 2, 3, 4, 6, \infty\}$."""
        if i == j:
            return Integer(1)
        t = self.vinberg_ratio(i, j)
        if t[1] == 0:
            return infinity
        val = t[0] / t[1]
        if val == 0:
            return Integer(2)
        elif val == 1:
            return Integer(3)
        elif val == 2:
            return Integer(4)
        elif val == 3:
            return Integer(6)
        elif val >= 4:
            return infinity
        return infinity

    def coxeter_matrix(self) -> CoxeterMatrix:
        r"""Return the Coxeter matrix as a native Sage :class:`CoxeterMatrix`."""
        n = self._rank
        cox_entries = [
            [self.coxeter_order(i, j) for j in range(n)]
            for i in range(n)
        ]
        return CoxeterMatrix(cox_entries)

    def is_all_finite(self) -> bool:
        r"""Return True if all entries lie in the affine chart $y \neq 0$."""
        return all(pt[1] != 0 for pt in self._entries.values())

    def to_gram_matrix(self) -> matrix:
        r"""
        Return standard Sage Gram Matrix when all entries are finite ($y \neq 0$).
        """
        if not self.is_all_finite():
            raise ValueError("Cannot convert to Gram matrix: contains infinite entries (1 : 0)")
        n = self._rank
        ring = self.base_ring()
        mat_data = [
            [ring(self[i, j][0] / self[i, j][1]) for j in range(n)]
            for i in range(n)
        ]
        return matrix(ring, n, n, mat_data)

    def submatrix(self, indices: Sequence[int]) -> "CombinatorialCoxeterVinbergMatrix":
        r"""Return the submatrix on the specified generator subset."""
        idx_list = list(indices)
        n_sub = len(idx_list)
        sub_entries = {}
        for new_i, old_i in enumerate(idx_list):
            for new_j, old_j in enumerate(idx_list):
                sub_entries[(new_i, new_j)] = self[old_i, old_j]
        sub_names = tuple(self._names[i] for i in idx_list)
        return CombinatorialCoxeterVinbergMatrix(self.base_ring(), sub_entries, n_sub, names=sub_names)

    def is_elliptic(self, indices: Sequence[int] | None = None) -> bool:
        r"""Check if the system (or sub-system) is elliptic (positive definite)."""
        target = self if indices is None else self.submatrix(indices)
        if not target.is_all_finite():
            return False
        gram = target.to_gram_matrix()
        return gram.is_positive_definite()

    def is_parabolic(self, indices: Sequence[int] | None = None) -> bool:
        r"""Check if the system (or sub-system) is parabolic (positive semi-definite with rank n-1)."""
        target = self if indices is None else self.submatrix(indices)
        if not target.is_all_finite():
            return False
        try:
            gram = target.to_gram_matrix()
            return gram.is_positive_semidefinite() and gram.rank() == target.rank() - 1
        except ValueError:
            return False

    def is_hyperbolic(self, indices: Sequence[int] | None = None) -> bool:
        r"""Check if the system (or sub-system) is hyperbolic (signature (n-1, 1))."""
        target = self if indices is None else self.submatrix(indices)
        try:
            gram = target.to_gram_matrix()
            return not gram.is_positive_semidefinite() and gram.det() < 0
        except ValueError:
            return True

    def _repr_(self) -> str:
        n = self._rank
        grid_rows = []
        for i in range(n):
            row_str = "  ".join(str(self[i, j]) for j in range(n))
            grid_rows.append(f"[{row_str}]")
        grid_repr = "\n".join(grid_rows)
        return f"Combinatorial Coxeter-Vinberg Matrix of rank {n} over {self.base_ring()}:\n{grid_repr}"

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
# 3. Constructor Function
# ---------------------------------------------------------------------------


def combinatorial_coxeter_vinberg_matrix(
    base_ring: object,
    components: Sequence[Sequence[object]],
    names: Sequence[str] | None = None,
) -> CombinatorialCoxeterVinbergMatrix:
    r"""
    Construct a CombinatorialCoxeterVinbergMatrix with entries in $\mathbb{P}^1(R)$.

    EXAMPLES::

        sage: from dzack_research.preamble.categories.modules.projective_tensors import combinatorial_coxeter_vinberg_matrix
        sage: from sage.rings.integer_ring import ZZ
        sage: from sage.rings.infinity import infinity
        sage: M = combinatorial_coxeter_vinberg_matrix(ZZ, [[-2, 1, 0], [1, -2, infinity], [0, infinity, -2]])
        sage: M[0, 0]
        (-2 : 1)
        sage: M[1, 2]
        (1 : 0)
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

    return CombinatorialCoxeterVinbergMatrix(base_ring, entries, n_rows, names=names)
