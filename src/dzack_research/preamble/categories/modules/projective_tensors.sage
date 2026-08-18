r"""Type-$(p,q)$ projective tensors on a module and Bilinear Form Tensors.

Mathematical Framework
======================
A projective tensor of valence $(p, q)$ on an $R$-module $M$ is a multilinear
geometric datum with components in Sage's native projective line:

.. MATH::

    \mathbb{P}^1(R) = \operatorname{ProjectiveSpace}(R, 1)

In standard homogeneous coordinates $(x : y)$:
- Affine chart $U_1 = \{ y \neq 0 \}$: $(r : 1)$ represents the finite scalar $r = x/y \in R$.
- Infinity chart $U_0 = \{ y = 0 \}$: $(1 : 0)$ represents $\infty$.

Mathematical Comparison: Supported vs. Excluded Operations
=========================================================

1. Operations That Make Mathematical Sense (Supported):
-------------------------------------------------------
- **Evaluation / Pairing**:
  Evaluation on basis elements $e_i, e_j$ directly produces homogeneous coordinates
  $B(e_i, e_j) \in \mathbb{P}^1(R)$.
- **Pullback along Module Homomorphisms**:
  For a linear morphism $f \colon N \to M$, the pullback $f^* B$ is well-defined on basis
  elements: $(f^* B)(v, w) = B(f(v), f(w))$.
- **Subdiagram / Submodule Restriction**:
  For an index subset $J \subseteq I$, restriction $(B|_J)_{ij} = B_{ij}$ preserves all
  homogeneous coordinates and reflection geometry.
- **Projective Basis Scaling**:
  Scaling basis elements $e_i \mapsto \lambda_i e_i$ with $\lambda_i \in R^\times$ acts
  projectively on entries: $B_{ij} \mapsto (\lambda_i \lambda_j x_{ij} : y_{ij})$.
- **Vinberg Invariant Extraction**:
  For reflection groups and Coxeter geometry, the normalized angle ratio:

  .. MATH::

      t(r_i, r_j) = \left( 4\,b(r_i, r_j)^2 \;:\; b(r_i, r_i)\,b(r_j, r_j) \right) \in \mathbb{P}^1(R)

  is an absolute projective invariant classifying mirror geometry into elliptic ($t < 4$),
  parabolic/parallel ($t = 4$), and hyperbolic/divergent ($t > 4$).
- **Conversion to Coxeter Matrix and Diagram**:
  Direct conversion to Sage's :class:`CoxeterMatrix` and :class:`FiniteCoxeterDiagram`.
- **Affine Chart Projection**:
  Isomorphism to :class:`GramMatrix` when all entries lie in the affine chart $y \neq 0$.

2. Operations That Are Mathematically Excluded:
----------------------------------------------
- **Global Addition ($T_1 + T_2$)**:
  $\mathbb{P}^1(R)$ is a projective scheme, not an $R$-module. Homogeneous addition
  $(x_1 : y_1) + (x_2 : y_2) = (x_1 y_2 + x_2 y_1 : y_1 y_2)$ yields indeterminate $(0 : 0)$
  when $y_1 = y_2 = 0$ (e.g. $(1 : 0) + (-1 : 0)$). Projective tensors do not form an $R$-module.
- **Uncontracted Matrix-Matrix Multiplication ($B_1 \cdot B_2$)**:
  Bilinear forms are $(0, 2)$-tensors ($V^* \otimes V^*$). Multiplying two $(0, 2)$-tensors
  is meaningless without an explicit metric contraction $V \cong V^*$.
- **General Multi-Slot Contractions / Traces**:
  Full contractions $\sum_k T^i_{\dots k \dots} S^{\dots k \dots}_j$ require summing products
  of projective coordinates, which is undefined without choosing specific global sections of line bundles.

EXAMPLES::

    sage: from dzack_research.preamble.categories.modules.projective_tensors import BilinearFormTensor, bilinear_form_tensor
    sage: from sage.rings.integer_ring import ZZ
    sage: from sage.rings.infinity import infinity
    sage: B = bilinear_form_tensor(ZZ, [[-2, 1, 0], [1, -2, infinity], [0, infinity, -2]])
    sage: B[0, 1]
    (1 : 1)
    sage: B[1, 2]
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
# 1. Projective Line Helper using Sage's native ProjectiveSpace
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
# 2. Projective Tensor Base Class
# ---------------------------------------------------------------------------


class ProjectiveTensor(Parent):
    r"""
    A type-$(p, q)$ tensor on a module $M$ with components in Sage's native :class:`ProjectiveSpace`.
    """

    def __init__(
        self,
        module: object,
        valence: tuple[int, int],
        entries: dict[tuple[int, ...], SchemeMorphism_point_projective_ring],
    ) -> None:
        self._module = module
        self._valence = tuple(valence)
        self._projective_space = ProjectiveSpace(module.base_ring(), 1, "x,y")
        self._entries = dict(entries)
        Parent.__init__(self, base=module.base_ring(), category=Objects())

    def module(self) -> object:
        r"""Return $M$, the module on which the tensor is defined."""
        return self._module

    def valence(self) -> tuple[int, int]:
        r"""Return $(p, q)$ indicating $p$ contravariant and $q$ covariant slots."""
        return self._valence

    def degree(self) -> int:
        r"""Return $p + q$, the total number of tensor indices."""
        return sum(self._valence)

    def projective_space(self) -> ProjectiveSpace:
        r"""Return the ambient projective space $\mathbb{P}^1(R)$."""
        return self._projective_space

    def __getitem__(self, index: tuple[int, ...] | int) -> SchemeMorphism_point_projective_ring:
        r"""Return component at multi-index as a ProjectivePoint."""
        idx = index if isinstance(index, tuple) else (index,)
        assert len(idx) == self.degree(), (
            f"Expected index of length {self.degree()}, got {len(idx)}"
        )
        return self._entries.get(idx, self._projective_space([0, 1]))

    def components(self) -> dict[tuple[int, ...], SchemeMorphism_point_projective_ring]:
        r"""Return dictionary of non-zero multi-index components."""
        return dict(self._entries)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ProjectiveTensor):
            return False
        return (
            self._module == other._module
            and self._valence == other._valence
            and self._entries == other._entries
        )


# ---------------------------------------------------------------------------
# 3. Bilinear Form Tensor ((0, 2)-Tensor with entries in P^1(R))
# ---------------------------------------------------------------------------


class BilinearFormTensor(ProjectiveTensor):
    r"""
    A symmetric bilinear $(0, 2)$-tensor $B \colon M \times M \to \mathbb{P}^1(R)$
    using Sage's native :class:`ProjectiveSpace`.

    Mathematical Foundations:
    -------------------------
    - Evaluates pairs of module elements / roots into $\mathbb{P}^1(R)$.
    - Encodes reflection geometry and Vinberg projective ratios:

      .. MATH::

          t(r_i, r_j) = \left( 4\,b(r_i, r_j)^2 \;:\; b(r_i, r_i)\,b(r_j, r_j) \right) \in \mathbb{P}^1(R)

    - Direct mapping to Coxeter matrices and diagrams:
      - $t = (0 : 1) \implies m = 2$ (orthogonal)
      - $t = (1 : 1) \implies m = 3$ (single bond)
      - $t = (2 : 1) \implies m = 4$ (double bond)
      - $t = (3 : 1) \implies m = 6$ (triple bond)
      - $t = (4 : 1) \implies m = \infty$ (parabolic / parallel mirrors)
      - $t = (k : 1)$ ($k > 4$) $\implies m = \infty$ (hyperbolic / divergent mirrors)
      - $t = (1 : 0) \implies \infty$ (infinite limit)
    """

    def __init__(
        self,
        module: object,
        entries: dict[tuple[int, int], SchemeMorphism_point_projective_ring],
        names: Sequence[str] | None = None,
    ) -> None:
        rank = module.rank() if hasattr(module, "rank") else len(module.module_generating_set())
        self._rank = int(rank)
        self._names = tuple(names) if names is not None else tuple(f"e_{i}" for i in range(self._rank))

        # Enforce symmetry
        sym_entries = {}
        for (i, j), pt in entries.items():
            sym_entries[(i, j)] = pt
            sym_entries[(j, i)] = pt

        ProjectiveTensor.__init__(self, module, (0, 2), sym_entries)

    def rank(self) -> int:
        r"""Return the rank / dimension of the underlying module."""
        return self._rank

    def variable_names(self) -> tuple[str, ...]:
        r"""Return variable/basis names."""
        return self._names

    def is_symmetric(self) -> bool:
        r"""Return True (bilinear form tensors are symmetric)."""
        return True

    def vinberg_ratio(self, i: int, j: int) -> SchemeMorphism_point_projective_ring:
        r"""
        Return the Vinberg projective angle invariant $t(e_i, e_j) \in \mathbb{P}^1(R)$:

        .. MATH::

            t(e_i, e_j) = \left( 4\,B(e_i, e_j)^2 \;:\; B(e_i, e_i)\,B(e_j, e_j) \right)
        """
        b_ij = self[i, j]
        b_ii = self[i, i]
        b_jj = self[j, j]

        # b_ij = (x_ij : y_ij), etc.
        x_ij, y_ij = b_ij[0], b_ij[1]
        x_ii, y_ii = b_ii[0], b_ii[1]
        x_jj, y_jj = b_jj[0], b_jj[1]

        # If any component is at infinity (y == 0)
        if y_ij == 0:
            return self._projective_space([1, 0])
        if y_ii == 0 or y_jj == 0:
            return self._projective_space([0, 1])

        # Exact homogeneous formula: 4 b_ij^2 / (b_ii b_jj)
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
        Return standard Sage Matrix when all entries are finite ($y \neq 0$).
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

    def subdiagram(self, indices: Sequence[int]) -> "BilinearFormTensor":
        r"""Return the induced sub-form tensor on the specified basis subset."""
        idx_list = list(indices)
        n_sub = len(idx_list)
        sub_entries = {}
        for new_i, old_i in enumerate(idx_list):
            for new_j, old_j in enumerate(idx_list):
                sub_entries[(new_i, new_j)] = self[old_i, old_j]
        sub_names = tuple(self._names[i] for i in idx_list)
        sub_module = FreeModule(self.base_ring(), n_sub)
        return BilinearFormTensor(sub_module, sub_entries, names=sub_names)

    def is_elliptic(self, indices: Sequence[int] | None = None) -> bool:
        r"""Check if the form tensor (or subdiagram) is elliptic (positive definite)."""
        target = self if indices is None else self.subdiagram(indices)
        if not target.is_all_finite():
            return False
        gram = target.to_gram_matrix()
        return gram.is_positive_definite()

    def is_parabolic(self, indices: Sequence[int] | None = None) -> bool:
        r"""Check if the form tensor (or subdiagram) is parabolic (positive semi-definite with rank n-1)."""
        target = self if indices is None else self.subdiagram(indices)
        if not target.is_all_finite():
            return False
        try:
            gram = target.to_gram_matrix()
            return gram.is_positive_semidefinite() and gram.rank() == target.rank() - 1
        except ValueError:
            return False

    def is_hyperbolic(self, indices: Sequence[int] | None = None) -> bool:
        r"""Check if the form tensor (or subdiagram) is hyperbolic (signature (n-1, 1))."""
        target = self if indices is None else self.subdiagram(indices)
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
        return f"Bilinear Form Tensor of rank {n} over {self.base_ring()}:\n{grid_repr}"

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
# 4. Constructor Functions
# ---------------------------------------------------------------------------


def bilinear_form_tensor(
    base_ring: object,
    components: Sequence[Sequence[object]],
    module: object = None,
    names: Sequence[str] | None = None,
) -> BilinearFormTensor:
    r"""
    Construct a BilinearFormTensor with components in $\mathbb{P}^1(R)$.

    EXAMPLES::

        sage: from dzack_research.preamble.categories.modules.projective_tensors import bilinear_form_tensor
        sage: from sage.rings.integer_ring import ZZ
        sage: from sage.rings.infinity import infinity
        sage: B = bilinear_form_tensor(ZZ, [[-2, 1], [1, -2]])
        sage: B[0, 0]
        (-2 : 1)
        sage: B_hyp = bilinear_form_tensor(ZZ, [[-2, infinity], [infinity, -2]])
        sage: B_hyp[0, 1]
        (1 : 0)
    """
    return projective_tensor(base_ring, components, valence=(0, 2), module=module, names=names)


def projective_tensor(
    base_ring: object,
    components: Sequence[Sequence[object]] | Sequence[object],
    valence: tuple[int, int] = (0, 2),
    module: object = None,
    names: Sequence[str] | None = None,
) -> ProjectiveTensor:
    r"""
    Construct a projective tensor with components in Sage's native :class:`ProjectiveSpace`.

    EXAMPLES::

        sage: from dzack_research.preamble.categories.modules.projective_tensors import projective_tensor
        sage: from sage.rings.integer_ring import ZZ
        sage: from sage.rings.infinity import infinity
        sage: B = projective_tensor(ZZ, [[-2, 1], [1, -2]])
        sage: B[0, 0]
        (-2 : 1)
    """
    assert isinstance(components, (list, tuple)), "Components must be a list or tuple"
    n_rows = len(components)

    if module is None:
        module = FreeModule(base_ring, n_rows)

    P1 = ProjectiveSpace(base_ring, 1, "x,y")

    if valence == (0, 2):
        entries = {}
        for i in range(n_rows):
            row = components[i]
            assert len(row) == n_rows, f"Row {i} has length {len(row)}, expected {n_rows}"
            for j in range(n_rows):
                val = row[j]
                entries[(i, j)] = to_projective_point(P1, val)
        return BilinearFormTensor(module, entries, names=names)

    # General (p, q) projective tensor
    entries_gen = {}
    for i, row in enumerate(components):
        if isinstance(row, (list, tuple)):
            for j, val in enumerate(row):
                entries_gen[(i, j)] = to_projective_point(P1, val)
        else:
            entries_gen[(i,)] = to_projective_point(P1, row)

    return ProjectiveTensor(module, valence, entries_gen)
