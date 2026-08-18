r"""Type-$(p,q)$ projective tensors on a module and projective bilinear forms.

Mathematical Framework
======================
A projective tensor of valence $(p, q)$ on an $R$-module $M$ is a multilinear
geometric datum with components in the projective line:

.. MATH::

    \mathbb{P}^1(R) = \mathbb{P}(R^2) = \{ [x : y] \mid (x, y) \in R^2 \setminus \{(0, 0)\} \} / R^\times

In standard homogeneous coordinates:
- Affine chart $U_1 = \{ y \neq 0 \}$: $[r : 1]$ represents the finite scalar $r = x/y \in R$.
- Infinity chart $U_0 = \{ y = 0 \}$: $[1 : 0]$ represents $\infty$.

Over the integers $R = \mathbb{Z}$, every rational $p/q \in \mathbb{Q}$ in lowest terms
identifies with the unimodular pair $[p : q] \in \mathbb{P}^1(\mathbb{Z})$ where $\gcd(p, q) = 1$,
and $[1 : 0]$ represents $\infty$.

Mathematical Comparison: Supported vs. Excluded Operations
=========================================================

1. Operations That Make Mathematical Sense (Supported):
-------------------------------------------------------
- **Evaluation / Pairing**:
  Evaluation on basis elements $e_i, e_j$ directly produces homogeneous coordinates
  $B(e_i, e_j) = [x_{ij} : y_{ij}] \in \mathbb{P}^1(R)$.
- **Pullback along Module Homomorphisms**:
  For a linear morphism $f \colon N \to M$, the pullback $f^* B$ is well-defined on basis
  elements: $(f^* B)(v, w) = B(f(v), f(w))$.
- **Subdiagram / Submodule Restriction**:
  For an index subset $J \subseteq I$, restriction $(B|_J)_{ij} = B_{ij}$ preserves all
  homogeneous coordinates and reflection geometry.
- **Projective Basis Scaling**:
  Scaling basis elements $e_i \mapsto \lambda_i e_i$ with $\lambda_i \in R^\times$ acts
  projectively on entries: $B_{ij} \mapsto [\lambda_i \lambda_j x_{ij} : y_{ij}]$.
- **Vinberg Invariant Extraction**:
  For reflection groups and Coxeter geometry, the normalized angle ratio:

  .. MATH::

      t(r_i, r_j) = \left[ 4\,b(r_i, r_j)^2 \;:\; b(r_i, r_i)\,b(r_j, r_j) \right] \in \mathbb{P}^1(R)

  is an absolute projective invariant classifying mirror geometry into elliptic ($t < 4$),
  parabolic/parallel ($t = 4$), and hyperbolic/divergent ($t > 4$).
- **Conversion to Coxeter Matrix and Diagram**:
  Direct conversion to Sage's :class:`CoxeterMatrix` and :class:`FiniteCoxeterDiagram`.
- **Affine Chart Projection**:
  Isomorphism to :class:`GramMatrix` when all entries lie in the affine chart $y \neq 0$.

2. Operations That Are Mathematically Excluded:
----------------------------------------------
- **Global Addition ($T_1 + T_2$)**:
  $\mathbb{P}^1(R)$ is a geometric scheme, not an $R$-module. Homogeneous addition
  $[x_1 : y_1] + [x_2 : y_2] = [x_1 y_2 + x_2 y_1 : y_1 y_2]$ yields indeterminate $[0 : 0]$
  when $y_1 = y_2 = 0$ (e.g. $[1 : 0] + [-1 : 0]$). Projective tensors do not form an $R$-module.
- **Uncontracted Matrix-Matrix Multiplication ($B_1 \cdot B_2$)**:
  Bilinear forms are $(0, 2)$-tensors ($V^* \otimes V^*$). Multiplying two $(0, 2)$-tensors
  is meaningless without an explicit metric contraction $V \cong V^*$.
- **General Multi-Slot Contractions / Traces**:
  Full contractions $\sum_k T^i_{\dots k \dots} S^{\dots k \dots}_j$ require summing products
  of projective coordinates, which is undefined without choosing specific global sections of line bundles.

EXAMPLES::

    sage: from dzack_research.preamble.categories.modules.projective_tensors import ProjectiveBilinearForm, projective_point, projective_tensor
    sage: from sage.rings.integer_ring import ZZ
    sage: from sage.rings.infinity import infinity
    sage: B = projective_tensor(ZZ, [[-2, 1, 0], [1, -2, infinity], [0, infinity, -2]])
    sage: B[0, 1]
    (1 : 1)
    sage: B[1, 2]
    (1 : 0)
    sage: B[1, 2].is_infinity()
    True
"""

from collections.abc import Callable, Hashable, Iterable, Iterator, Mapping, Sequence
from typing import ClassVar, NamedTuple, Optional, Self, TYPE_CHECKING, Union

from sage.categories.category import Category
from sage.categories.sets_cat import Sets
from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix
from sage.matrix.constructor import matrix
from sage.misc.cachefunc import cached_method
from sage.modules.free_module import FreeModule
from sage.rings.infinity import Infinity, PlusInfinity, infinity
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational import Rational
from sage.rings.rational_field import QQ as SageQQ
from sage.structure.element import Element, ModuleElement
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.coxeter_diagrams import (
        FiniteCoxeterDiagram,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        ModuleMorphism,
    )
    from dzack_research.preamble.lexicon import GramMatrix, OrderedSet


# ---------------------------------------------------------------------------
# 1. Projective Point on P^1(R)
# ---------------------------------------------------------------------------


class ProjectivePoint(Element):
    r"""
    A homogeneous point $[x : y] \in \mathbb{P}^1(R)$.

    Attributes:
        x: Numerator coordinate.
        y: Denominator coordinate ($y = 0 \iff \infty$).
    """

    def __init__(self, parent: "ProjectiveLine", x: object, y: object = 1) -> None:
        Element.__init__(self, parent)
        ring = parent.base_ring()
        if x is infinity or x is Infinity or isinstance(x, PlusInfinity) or str(x) in ("+Infinity", "oo", "infinity", "inf"):
            self._x = ring.one()
            self._y = ring.zero()
        elif isinstance(x, ProjectivePoint):
            self._x = ring(x.x())
            self._y = ring(x.y())
        elif isinstance(x, (tuple, list)) and len(x) == 2:
            self._x = ring(x[0])
            self._y = ring(x[1])
        else:
            if y is infinity or y is Infinity or isinstance(y, PlusInfinity) or str(y) in ("+Infinity", "oo", "infinity", "inf"):
                self._x = ring.zero()
                self._y = ring.one()
            else:
                if ring is SageZZ and isinstance(x, (int, Integer)) and isinstance(y, (int, Integer)):
                    ix = Integer(x)
                    iy = Integer(y)
                    if ix == 0 and iy == 0:
                        raise ValueError("Projective coordinates (0, 0) are undefined")
                    g = ix.gcd(iy)
                    if iy < 0 or (iy == 0 and ix < 0):
                        g = -g
                    self._x = ring(ix // g)
                    self._y = ring(iy // g)
                else:
                    self._x = ring(x)
                    self._y = ring(y)
                    if self._x == 0 and self._y == 0:
                        raise ValueError("Projective coordinates (0, 0) are undefined")

    def x(self) -> object:
        r"""Return the first homogeneous coordinate $x$."""
        return self._x

    def y(self) -> object:
        r"""Return the second homogeneous coordinate $y$."""
        return self._y

    def is_infinity(self) -> bool:
        r"""Return True if this is the point at infinity $[1 : 0]$ ($y = 0$)."""
        return self._y == self.parent().base_ring().zero()

    def is_finite(self) -> bool:
        r"""Return True if this point lies in the affine patch $y \neq 0$."""
        return not self.is_infinity()

    def affine_value(self) -> object:
        r"""
        Return $x/y$ as an element of the fraction field, or raise ValueError if infinite.
        """
        if self.is_infinity():
            raise ValueError("Point is at infinity [1 : 0] and has no finite affine value")
        return self._x / self._y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ProjectivePoint):
            try:
                other_pt = self.parent()(other)
                return self._x * other_pt._y == self._y * other_pt._x
            except Exception:
                return False
        return self._x * other._y == self._y * other._x

    def __hash__(self) -> int:
        return hash((self._x, self._y))

    def _repr_(self) -> str:
        return f"({self._x} : {self._y})"

    def _latex_(self) -> str:
        if self.is_infinity():
            return r"\infty"
        if self._y == 1:
            return str(self._x)
        return rf"\left[{self._x} : {self._y}\right]"

    def _repr_latex_(self) -> str:
        return "$\\displaystyle " + self._latex_() + "$"


class ProjectiveLine(UniqueRepresentation, Parent):
    r"""
    The projective line $\mathbb{P}^1(R)$ over a commutative ring $R$.
    """

    Element = ProjectivePoint

    def __init__(self, base_ring: object) -> None:
        self._base_ring = base_ring
        Parent.__init__(self, base=base_ring, category=Sets())

    def _element_constructor_(self, x: object, y: object = 1) -> ProjectivePoint:
        return self.element_class(self, x, y)

    def infinity(self) -> ProjectivePoint:
        r"""Return the point at infinity $[1 : 0]$."""
        return self(1, 0)

    def point(self, x: object, y: object = 1) -> ProjectivePoint:
        r"""Construct a point $[x : y] \in \mathbb{P}^1(R)$."""
        return self(x, y)

    def _repr_(self) -> str:
        return f"Projective Line P^1({self.base_ring()})"


def projective_point(base_ring: object, x: object, y: object = 1) -> ProjectivePoint:
    r"""Construct a point $[x : y] \in \mathbb{P}^1(R)$."""
    return ProjectiveLine(base_ring)(x, y)


# ---------------------------------------------------------------------------
# 2. Projective Tensor Base Class
# ---------------------------------------------------------------------------


class ProjectiveTensor(Parent):
    r"""
    A type-$(p, q)$ tensor on a module $M$ with components in $\mathbb{P}^1(R)$.
    """

    def __init__(
        self,
        module: object,
        valence: tuple[int, int],
        entries: dict[tuple[int, ...], ProjectivePoint],
    ) -> None:
        self._module = module
        self._valence = tuple(valence)
        self._projective_line = ProjectiveLine(module.base_ring())
        self._entries = dict(entries)
        Parent.__init__(self, base=module.base_ring(), category=Sets())

    def module(self) -> object:
        r"""Return $M$, the module on which the tensor is defined."""
        return self._module

    def valence(self) -> tuple[int, int]:
        r"""Return $(p, q)$ indicating $p$ contravariant and $q$ covariant slots."""
        return self._valence

    def degree(self) -> int:
        r"""Return $p + q$, the total number of tensor indices."""
        return sum(self._valence)

    def projective_line(self) -> ProjectiveLine:
        r"""Return the ambient projective line $\mathbb{P}^1(R)$."""
        return self._projective_line

    def __getitem__(self, index: tuple[int, ...] | int) -> ProjectivePoint:
        r"""Return component at multi-index as a ProjectivePoint."""
        idx = index if isinstance(index, tuple) else (index,)
        assert len(idx) == self.degree(), (
            f"Expected index of length {self.degree()}, got {len(idx)}"
        )
        return self._entries.get(idx, self._projective_line(0, 1))

    def components(self) -> dict[tuple[int, ...], ProjectivePoint]:
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
# 3. Projective Bilinear Form Tensor ((0, 2)-Form)
# ---------------------------------------------------------------------------


class ProjectiveBilinearForm(ProjectiveTensor):
    r"""
    A symmetric bilinear $(0, 2)$-tensor $B \colon M \times M \to \mathbb{P}^1(R)$.

    Mathematical Foundations:
    -------------------------
    - Evaluates pairs of module elements / roots into $\mathbb{P}^1(R)$.
    - Encodes reflection geometry and Vinberg projective ratios:

      .. MATH::

          t(r_i, r_j) = \left[ 4\,b(r_i, r_j)^2 \;:\; b(r_i, r_i)\,b(r_j, r_j) \right] \in \mathbb{P}^1(R)

    - Direct mapping to Coxeter matrices and diagrams:
      - $t = [0 : 1] \implies m = 2$ (orthogonal)
      - $t = [1 : 1] \implies m = 3$ (single bond)
      - $t = [2 : 1] \implies m = 4$ (double bond)
      - $t = [3 : 1] \implies m = 6$ (triple bond)
      - $t = [4 : 1] \implies m = \infty$ (parabolic / parallel mirrors)
      - $t = [k : 1]$ ($k > 4$) $\implies m = \infty$ (hyperbolic / divergent mirrors)
      - $t = [1 : 0] \implies \infty$ (infinite limit)
    """

    def __init__(
        self,
        module: object,
        entries: dict[tuple[int, int], ProjectivePoint],
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
        r"""Return True (projective bilinear forms are symmetric)."""
        return True

    def vinberg_ratio(self, i: int, j: int) -> ProjectivePoint:
        r"""
        Return the Vinberg projective angle invariant $t(e_i, e_j) \in \mathbb{P}^1(R)$:

        .. MATH::

            t(e_i, e_j) = \left[ 4\,B(e_i, e_j)^2 \;:\; B(e_i, e_i)\,B(e_j, e_j) \right]
        """
        b_ij = self[i, j]
        b_ii = self[i, i]
        b_jj = self[j, j]

        # If any component is at infinity
        if b_ij.is_infinity():
            return self._projective_line.infinity()
        if b_ii.is_infinity() or b_jj.is_infinity():
            return self._projective_line(0, 1)

        # Exact homogeneous formula
        # b_ij = x_ij / y_ij, b_ii = x_ii / y_ii, b_jj = x_jj / y_jj
        # 4 b_ij^2 / (b_ii b_jj) = (4 x_ij^2 y_ii y_jj) / (y_ij^2 x_ii x_jj)
        num = 4 * (b_ij.x() ** 2) * b_ii.y() * b_jj.y()
        den = (b_ij.y() ** 2) * b_ii.x() * b_jj.x()
        return self._projective_line(num, den)

    def coxeter_order(self, i: int, j: int) -> object:
        r"""Return the Coxeter bond order $m_{ij} \in \{1, 2, 3, 4, 6, \infty\}$."""
        if i == j:
            return Integer(1)
        t = self.vinberg_ratio(i, j)
        if t.is_infinity():
            return infinity
        if t.y() == 0:
            return infinity
        val = t.affine_value()
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
        return all(pt.is_finite() for pt in self._entries.values())

    def to_gram_matrix(self) -> matrix:
        r"""
        Return standard Sage Matrix when all entries are finite ($y \neq 0$).
        """
        if not self.is_all_finite():
            raise ValueError("Cannot convert to Gram matrix: contains infinite entries [1 : 0]")
        n = self._rank
        ring = self.base_ring()
        mat_data = [
            [ring(self[i, j].affine_value()) for j in range(n)]
            for i in range(n)
        ]
        return matrix(ring, n, n, mat_data)

    def subdiagram(self, indices: Sequence[int]) -> "ProjectiveBilinearForm":
        r"""Return the induced sub-form on the specified basis subset."""
        idx_list = list(indices)
        n_sub = len(idx_list)
        sub_entries = {}
        for new_i, old_i in enumerate(idx_list):
            for new_j, old_j in enumerate(idx_list):
                sub_entries[(new_i, new_j)] = self[old_i, old_j]
        sub_names = tuple(self._names[i] for i in idx_list)
        sub_module = FreeModule(self.base_ring(), n_sub)
        return ProjectiveBilinearForm(sub_module, sub_entries, names=sub_names)

    def is_elliptic(self, indices: Sequence[int] | None = None) -> bool:
        r"""Check if the form (or subdiagram) is elliptic (positive definite)."""
        target = self if indices is None else self.subdiagram(indices)
        if not target.is_all_finite():
            return False
        gram = target.to_gram_matrix()
        return gram.is_positive_definite()

    def is_parabolic(self, indices: Sequence[int] | None = None) -> bool:
        r"""Check if the form (or subdiagram) is parabolic (positive semi-definite with rank n-1)."""
        target = self if indices is None else self.subdiagram(indices)
        if not target.is_all_finite():
            return False
        try:
            gram = target.to_gram_matrix()
            return gram.is_positive_semidefinite() and gram.rank() == target.rank() - 1
        except ValueError:
            return False

    def is_hyperbolic(self, indices: Sequence[int] | None = None) -> bool:
        r"""Check if the form (or subdiagram) is hyperbolic (signature (n-1, 1))."""
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
        return f"Projective Bilinear Form of rank {n} over {self.base_ring()}:\n{grid_repr}"

    def _latex_(self) -> str:
        n = self._rank
        rows_latex = []
        for i in range(n):
            row_latex = " & ".join(self[i, j]._latex_() for j in range(n))
            rows_latex.append(row_latex)
        mat_latex = r" \\ ".join(rows_latex)
        return rf"\begin{{pmatrix}} {mat_latex} \end{{pmatrix}}"

    def _repr_latex_(self) -> str:
        return "$\\displaystyle " + self._latex_() + "$"


# ---------------------------------------------------------------------------
# 4. Constructor Function
# ---------------------------------------------------------------------------


def projective_tensor(
    base_ring: object,
    components: Sequence[Sequence[object]] | Sequence[object],
    valence: tuple[int, int] = (0, 2),
    module: object = None,
    names: Sequence[str] | None = None,
) -> ProjectiveTensor:
    r"""
    Construct a projective tensor with components in $\mathbb{P}^1(R)$.

    EXAMPLES::

        sage: from dzack_research.preamble.categories.modules.projective_tensors import projective_tensor
        sage: from sage.rings.integer_ring import ZZ
        sage: from sage.rings.infinity import infinity
        sage: B = projective_tensor(ZZ, [[-2, 1], [1, -2]])
        sage: B[0, 0]
        (-2 : 1)
        sage: B_hyp = projective_tensor(ZZ, [[-2, infinity], [infinity, -2]])
        sage: B_hyp[0, 1]
        (1 : 0)
        sage: B_hyp[0, 1].is_infinity()
        True
    """
    assert isinstance(components, (list, tuple)), "Components must be a list or tuple"
    n_rows = len(components)

    if module is None:
        module = FreeModule(base_ring, n_rows)

    p_line = ProjectiveLine(base_ring)

    if valence == (0, 2):
        entries = {}
        for i in range(n_rows):
            row = components[i]
            assert len(row) == n_rows, f"Row {i} has length {len(row)}, expected {n_rows}"
            for j in range(n_rows):
                val = row[j]
                if isinstance(val, ProjectivePoint):
                    entries[(i, j)] = val
                else:
                    entries[(i, j)] = p_line(val)
        return ProjectiveBilinearForm(module, entries, names=names)

    # General (p, q) projective tensor
    entries_gen = {}
    for i, row in enumerate(components):
        if isinstance(row, (list, tuple)):
            for j, val in enumerate(row):
                entries_gen[(i, j)] = p_line(val)
        else:
            entries_gen[(i,)] = p_line(row)

    return ProjectiveTensor(module, valence, entries_gen)
