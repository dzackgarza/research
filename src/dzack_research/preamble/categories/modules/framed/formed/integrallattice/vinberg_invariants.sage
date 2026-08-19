r"""Combinatorial Vinberg invariant matrices, projective reflection geometry, and X_ref validation.

Mathematical Framework
======================
Let $V$ be a free module or vector space equipped with a symmetric bilinear form $b$.
For any pair of non-isotropic vectors $v_i, v_j \in V$, the **Vinberg invariant** is the
normalized projective ratio:

.. MATH::

    t(v_i, v_j) = \left[\, 4\,b(v_i, v_j)^2 \;:\; b(v_i, v_i)\,b(v_j, v_j) \,\right] \in \mathbb{P}^1(R)

where $\mathbb{P}^1(R) = \operatorname{ProjectiveSpace}(R, 1)$ is Sage's native projective line.

The Reflection Cosine Set ($X_{\mathrm{ref}}$)
==============================================
The set of reflection cosines:

.. MATH::

    X_{\mathrm{ref}} = \left\{ \cos\left(\frac{\pi}{n}\right) \;\middle|\; n \in \mathbb{Z}_{\ge 1} \right\} \;\subset\; \overline{\mathbb{Q}} \cap [-1, 1)

is defined via exact algebraic geometry without enumeration or floating-point rounding.

Exact Algebraic Characterization (No Rounding)
-----------------------------------------------
For any real algebraic candidate $x \in [-1, 1)$:
1. Construct the algebraic number:

   .. MATH::

       \zeta = x + i \sqrt{1 - x^2} \in \overline{\mathbb{Q}}

2. Compute its exact multiplicative order $k = \operatorname{multiplicative\_order}(\zeta)$.
3. $x \in X_{\mathrm{ref}}$ if and only if $k = 2n$ is an even integer and $\zeta^n = -1$.
   In this case, the exact Coxeter exponent is $n = k / 2$.

EXAMPLES::

    sage: from dzack_research.preamble.categories.modules.framed.formed.integrallattice.vinberg_invariants import (
    ...       CombinatorialVinbergInvariantMatrix,
    ...       ReflectionCosineSet, X_ref,
    ...       vinberg_invariant_matrix_from_gram
    ...   )
    sage: from sage.rings.integer_ring import ZZ
    sage: from sage.matrix.constructor import matrix
    sage: from sage.functions.other import sqrt

    # 1. Exact algebraic membership:
    sage: 1/2 in X_ref
    True
    sage: X_ref.index_of(1/2)
    3
    sage: (1 + sqrt(5))/4 in X_ref
    True
    sage: X_ref.index_of((1 + sqrt(5))/4)
    5
    sage: 1/3 in X_ref
    False

TODOs & Architectural Roadmap
=============================
- [ ] Generalize to combinatorial intersection matrices for arbitrary hyperplane arrangements
      in an ambient space (not just reflection hyperplanes).
- [ ] Formalize "Hyperplane arrangement in an ambient space" as a first-class category.
- [ ] Make crystallographic, non-crystallographic, and hyperbolic properties axiomatic
      refinements of reflection arrangements.
- [ ] Ensure all root lattice objects in the preamble can canonically produce their associated
      CombinatorialVinbergInvariantMatrix / hyperplane arrangement.
- [ ] Make the Gram tensor reconstruction return an entire abstract root lattice parent
      instead of just the bare Gram matrix.
- [ ] Rename `gram_matrix` to `gram_tensor` across the entire preamble codebase.
"""

from collections.abc import Mapping, Sequence
from itertools import combinations
import math
from typing import TYPE_CHECKING

from sage.categories.category import Category
from sage.categories.objects import Objects
from sage.categories.sets_cat import Sets
from sage.combinat.posets.posets import Poset
from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix as SageCoxeterMatrix
from sage.functions.other import sqrt
from sage.functions.trig import cos
from sage.graphs.graph import Graph
from sage.matrix.constructor import matrix
from sage.matrix.matrix0 import Matrix
from sage.rings.infinity import Infinity, PlusInfinity, infinity
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.imaginary_unit import I
from sage.rings.qqbar import QQbar
from sage.rings.rational_field import QQ as SageQQ
from sage.schemes.projective.projective_point import SchemeMorphism_point_projective_ring
from sage.schemes.projective.projective_space import ProjectiveSpace
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

if TYPE_CHECKING:
    from sage.graphs.digraph import DiGraph
    from sage.rings.qqbar import AlgebraicNumber
    from sage.rings.ring import Ring
    from sage.structure.parent import MembershipInput
    from sage.symbolic.expression import Expression
    from dzack_research.preamble.lexicon import Element
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.coxeter_diagrams import (
        FiniteCoxeterDiagram,
    )

    # A vertex of a projective weighted graph is named by a label; the
    # constructors accept either the label or its index.
    VertexLabel = str | int | Integer
    # What a point of P^1(R) may be handed over as: a scalar (read as
    # [x : 1]), infinity (read as [1 : 0]), a coordinate pair, or a point
    # already in the projective space.
    ProjectivePointDatum = (
        Element
        | int
        | PlusInfinity
        | tuple
        | list
        | SchemeMorphism_point_projective_ring
    )


# ---------------------------------------------------------------------------
# 1. Reflection Cosine Set X_ref (Exact Algebraic Implementation)
# ---------------------------------------------------------------------------


class ReflectionCosineSet(UniqueRepresentation, Parent):
    r"""
    The infinite set of reflection cosines:
        X_ref = { cos(pi/n) | n in ZZ_{>=1} } subset QQbar cap [-1, 1)

    Membership is computed algebraically via roots of unity in QQbar without rounding.
    """

    def __init__(self) -> None:
        Parent.__init__(self, category=Sets().Infinite())

    def _repr_(self) -> str:
        return "Set of reflection cosines { cos(pi/n) | n in ZZ_{>=1} }"

    def _exact_n(self, x: "AlgebraicNumber | Element") -> Integer | None:
        r"""
        Return the exact integer n >= 1 such that x = cos(pi/n), or None if x not in X_ref.
        """
        x_alg = QQbar(x)

        if x_alg == -1:
            return Integer(1)
        if x_alg <= -1 or x_alg >= 1:
            return None

        zeta = x_alg + QQbar(I) * QQbar(sqrt(1 - x_alg**2))
        order = zeta.multiplicative_order()
        if order is not infinity and order % 2 == 0:
            n = Integer(order // 2)
            if zeta**n == -1:
                return n
        return None

    def __contains__(self, x: "AlgebraicNumber | Element") -> bool:
        return self._exact_n(x) is not None

    def __getitem__(self, n: int | Integer) -> "Expression":
        r"""Return cos(pi/n) for n >= 1."""
        n_int = Integer(n)
        assert n_int >= 1, "Index must be an integer n >= 1"
        return cos(SageQQ.pi() / n_int) if hasattr(SageQQ, "pi") else cos(SageZZ(1) * SageQQ(1) / n_int)

    def index_of(self, x: "AlgebraicNumber | Element") -> Integer:
        r"""Return the exact integer n such that x = cos(pi/n)."""
        n = self._exact_n(x)
        assert n is not None, (
            f"{x} is not an algebraic reflection cosine in X_ref"
        )
        return n


# Singleton instance
X_ref = ReflectionCosineSet()


# ---------------------------------------------------------------------------
# 2. Categories of Projective Weighted Graphs and Arrangements
# ---------------------------------------------------------------------------


class ProjectiveWeightedGraphs(Category):
    r"""Category of finite directed graphs with node and edge weights in P^1(R)."""

    def _repr_object_names(self) -> str:
        return "projective weighted graphs"

    def super_categories(self) -> list[Category]:
        return [Sets().Finite()]

    def Symmetric(self) -> "SymmetricProjectiveWeightedGraphs":
        return SymmetricProjectiveWeightedGraphs(self)

    class ParentMethods:
        r"""Universal methods and predicates for all projective weighted graphs."""

        def _get_n_and_verts(self) -> tuple[int, tuple[str, ...]]:
            n = self.num_vertices() if hasattr(self, "num_vertices") else self.rank()
            verts = self.vertices() if hasattr(self, "vertices") else tuple(str(v) for v in range(n))
            return n, verts

        def is_symmetric(self) -> bool:
            r"""Return True if the directed edge weights are symmetric."""
            n, verts = self._get_n_and_verts()
            for i in range(n):
                for j in range(i + 1, n):
                    u, v = verts[i], verts[j]
                    w1 = self.edge_weight(u, v) if hasattr(self, "edge_weight") else self[i, j]
                    w2 = self.edge_weight(v, u) if hasattr(self, "edge_weight") else self[j, i]
                    if w1[0] * w2[1] != w2[0] * w1[1]:
                        return False
            return True

        def is_coxeter(self) -> bool:
            r"""Return True if node weights are (4 : 1) and off-diagonal weights satisfy reflection angles."""
            if not self.is_symmetric():
                return False
            n, verts = self._get_n_and_verts()
            for i in range(n):
                u = verts[i]
                diag = self.vertex_weight(u) if hasattr(self, "vertex_weight") else self[i, i]
                if diag[0] * 1 != 4 * diag[1]:
                    return False
                for j in range(i + 1, n):
                    v = verts[j]
                    wt = self.edge_weight(u, v) if hasattr(self, "edge_weight") else self[i, j]
                    if wt[1] == 0:
                        continue
                    ratio = wt[0] / wt[1]
                    if ratio >= 4:
                        continue
                    if ratio < 0 or (sqrt(ratio) / 2 not in X_ref):
                        return False
            return True

        def is_crystallographic(self) -> bool:
            r"""Return True if all finite Coxeter bonds belong to {2, 3, 4, 6}.

            A property the diagram either has or lacks, decided on the bonds.
            The Schläfli entry $-\cos(\pi/m)$ is irrational for $m=4,6$, and
            the way to a lattice there is to rescale a *root* -- which moves
            the diagonal too, taking $B_2$ to Gram $((2,-2),(-2,4))$ -- never
            to multiply one off-diagonal entry by a constant.  That is not a
            change of basis and does not yield an integral matrix.
            """
            if not self.is_coxeter():
                return False
            n, verts = self._get_n_and_verts()
            for i in range(n):
                for j in range(i + 1, n):
                    m = self.coxeter_order(i, j) if hasattr(self, "coxeter_order") else None
                    if m is not None and m is not infinity:
                        if m not in (2, 3, 4, 6):
                            return False
            return True

        def is_simply_laced(self) -> bool:
            r"""Return True if all finite Coxeter bonds belong to {2, 3} (types A, D, E)."""
            if not self.is_coxeter():
                return False
            n, verts = self._get_n_and_verts()
            for i in range(n):
                for j in range(i + 1, n):
                    m = self.coxeter_order(i, j) if hasattr(self, "coxeter_order") else None
                    if m is not None and m is not infinity:
                        if m not in (2, 3):
                            return False
            return True

        def is_elliptic(self, indices: Sequence[int] | None = None) -> bool:
            r"""Check if the system (or sub-system) is elliptic (positive definite Schläfli matrix)."""
            if not self.is_symmetric():
                return False
            S = self.schlafli_matrix(indices=indices)
            return bool(S.is_positive_definite())

        def is_parabolic(self, indices: Sequence[int] | None = None) -> bool:
            r"""Check if the system (or sub-system) is parabolic (positive semi-definite with corank 1)."""
            if not self.is_symmetric():
                return False
            S = self.schlafli_matrix(indices=indices)
            if S.nrows() == 0:
                return False
            return bool(S.is_positive_semidefinite() and S.rank() == S.nrows() - 1)

        def is_hyperbolic(self, indices: Sequence[int] | None = None) -> bool:
            r"""Check if the system (or sub-system) is hyperbolic (signature (n-1, 1)).

            Sound on Schläfli matrices, and only there: $\det<0$ says the
            number of negative eigenvalues is *odd*, so on an arbitrary
            symmetric matrix this would also admit signature $(n-3,3)$.  What
            excludes that here is the Schläfli domain -- diagonal $1$, entries
            $-\cos(\pi/m)\in(-1,0]$, hence trace $n$ against a bounded spectral
            radius.  Do not lift this test to a general Gram matrix; ask
            ``signature_pair`` there.
            """
            if not self.is_symmetric():
                return False
            S = self.schlafli_matrix(indices=indices)
            if S.nrows() == 0:
                return False
            return bool(not S.is_positive_semidefinite() and (S.det() < 0))

        def is_compact_hyperbolic(self, indices: Sequence[int] | None = None) -> bool:
            r"""Check if the system is compact hyperbolic (Lannér simplex: hyperbolic with all proper minors elliptic)."""
            if not self.is_hyperbolic(indices=indices):
                return False
            n, verts = self._get_n_and_verts()
            target_indices = list(range(n)) if indices is None else list(indices)
            k = len(target_indices)
            for size in range(1, k):
                for subset in combinations(target_indices, size):
                    if not self.is_elliptic(indices=subset):
                        return False
            return True

        def is_paracompact_hyperbolic(self, indices: Sequence[int] | None = None) -> bool:
            r"""Check if the system is paracompact hyperbolic (hyperbolic and contains at least one parabolic minor)."""
            if not self.is_hyperbolic(indices=indices):
                return False
            n, verts = self._get_n_and_verts()
            target_indices = list(range(n)) if indices is None else list(indices)
            k = len(target_indices)
            for size in range(1, k):
                for subset in combinations(target_indices, size):
                    if self.is_parabolic(indices=subset):
                        return True
            return False

        def subdiagram_poset(self) -> Poset:
            r"""Return the Boolean inclusion poset of all induced subdiagram objects."""
            n, verts = self._get_n_and_verts()
            subdiagrams = [
                self.subdiagram(s) for size in range(n + 1) for s in combinations(range(n), size)
            ]

            def leq(D1: Parent, D2: Parent) -> bool:
                v1 = getattr(D1, "vertices", None) or getattr(D1, "variable_names", None)
                v2 = getattr(D2, "vertices", None) or getattr(D2, "variable_names", None)
                names1 = set(v1()) if v1 is not None else set()
                names2 = set(v2()) if v2 is not None else set()
                return names1.issubset(names2)

            return Poset((subdiagrams, leq))

        def parabolic_subdiagram_poset(self) -> Poset:
            r"""Return the induced subposet of parabolic subdiagram objects."""
            if not self.is_symmetric():
                return Poset(([], lambda a, b: True))
            full_P = self.subdiagram_poset()
            parabolics = [
                D for D in full_P
                if (D.num_vertices() if hasattr(D, "num_vertices") else D.rank()) > 0 and D.is_parabolic()
            ]
            return full_P.subposet(parabolics)

        def maximal_parabolic_subdiagram_poset(self) -> Poset:
            r"""Return the subposet of maximal parabolic subdiagram objects."""
            p_poset = self.parabolic_subdiagram_poset()
            max_elems = p_poset.maximal_elements()
            return p_poset.subposet(max_elems)

        def elliptic_subdiagram_poset(self) -> Poset:
            r"""Return the induced subposet of elliptic subdiagram objects.

            The elliptic subdiagrams form an order ideal in
            :meth:`subdiagram_poset`: a subdiagram's Schläfli matrix is a
            principal submatrix -- the Gram matrix of the restricted form --
            and a positive definite form restricts positive definite
            (equivalently, Cauchy interlacing bounds each eigenvalue of a
            principal submatrix below by one of the full matrix).  So every
            subdiagram of an elliptic diagram is elliptic, and an
            enumeration may prune every superdiagram of a non-elliptic
            subdiagram.
            """
            if not self.is_symmetric():
                return Poset(([], lambda a, b: True))
            full_P = self.subdiagram_poset()
            elliptics = [D for D in full_P if D.is_elliptic()]
            return full_P.subposet(elliptics)

        def maximal_elliptic_subdiagram_poset(self) -> Poset:
            r"""Return the subposet of maximal elliptic subdiagram objects.

            Maximality is among *all* elliptic subdiagrams, disconnected ones
            included; a caller wanting the maximal connected ones filters
            with ``is_connected()``.
            """
            e_poset = self.elliptic_subdiagram_poset()
            max_elems = e_poset.maximal_elements()
            return e_poset.subposet(max_elems)

        def hyperbolic_subdiagram_poset(self) -> Poset:
            r"""Return the induced subposet of hyperbolic subdiagram objects."""
            if not self.is_symmetric():
                return Poset(([], lambda a, b: True))
            full_P = self.subdiagram_poset()
            hyperbolics = [
                D for D in full_P
                if (D.num_vertices() if hasattr(D, "num_vertices") else D.rank()) > 0 and D.is_hyperbolic()
            ]
            return full_P.subposet(hyperbolics)

        def find_all_parabolics(self) -> list[Parent]:
            r"""Find all parabolic subdiagram objects."""
            return list(self.parabolic_subdiagram_poset())

        def find_maximal_parabolics(self) -> list[Parent]:
            r"""Find all maximal parabolic subdiagram objects."""
            return self.parabolic_subdiagram_poset().maximal_elements()


class SymmetricProjectiveWeightedGraphs(Category):
    r"""Category of symmetric projective weighted graphs (undirected / symmetric intersection matrices)."""

    def __init__(self, base_category: Category | None = None) -> None:
        self._base = base_category if base_category is not None else ProjectiveWeightedGraphs()
        Category.__init__(self)

    def _repr_object_names(self) -> str:
        return "symmetric projective weighted graphs"

    def super_categories(self) -> list[Category]:
        return [self._base]

    def Coxeter(self) -> Category:
        r"""Return the category of Coxeter diagrams (symmetric projective weighted graphs with reflection angles)."""
        from dzack_research.preamble.categories.modules.framed.formed.integrallattice.coxeter_diagrams import (
            CoxeterDiagrams,
        )
        return CoxeterDiagrams()

    class ParentMethods:
        r"""Methods for symmetric projective weighted graphs and combinatorial intersection matrices."""

        def schlafli_matrix(self, indices: Sequence[int] | None = None) -> Matrix:
            r"""
            Reconstruct the Schläfli matrix $S = (s_{ij})$ where $s_{ii} = 1$ and $s_{ij} = -\sqrt{t_{ij}}/2$.
            """
            n = self.num_vertices() if hasattr(self, "num_vertices") else self.rank()
            idx_list = list(range(n)) if indices is None else list(indices)
            k = len(idx_list)
            verts = self.vertices() if hasattr(self, "vertices") else tuple(str(v) for v in range(n))
            S_mat = [[SageQQ.zero() for _ in range(k)] for _ in range(k)]

            for i_idx, i in enumerate(idx_list):
                S_mat[i_idx][i_idx] = SageQQ.one()
                for j_idx in range(i_idx + 1, k):
                    j = idx_list[j_idx]
                    u, v = verts[i], verts[j]
                    pt = self.edge_weight(u, v) if hasattr(self, "edge_weight") else self[i, j]
                    assert pt[1] != 0, (
                        "Cannot reconstruct finite Schläfli entry from "
                        "infinite ratio [1 : 0]"
                    )
                    t_val = pt[0] / pt[1]
                    val = -sqrt(t_val) / 2
                    S_mat[i_idx][j_idx] = val
                    S_mat[j_idx][i_idx] = val

            return matrix(S_mat)

        def gram_tensor(
            self,
            root_norms: "Sequence[Element] | Element | int" = -2,
            indices: Sequence[int] | None = None,
        ) -> Matrix:
            r"""
            Reconstruct the Gram matrix $G = (b(v_i, v_j))$ given diagonal root norms $q_i = b(v_i, v_i)$.
            """
            n = self.num_vertices() if hasattr(self, "num_vertices") else self.rank()
            idx_list = list(range(n)) if indices is None else list(indices)
            k = len(idx_list)
            verts = self.vertices() if hasattr(self, "vertices") else tuple(str(v) for v in range(n))

            ring = self.base_ring()
            if isinstance(root_norms, Sequence):
                assert len(root_norms) == k, f"Expected {k} root norms, got {len(root_norms)}"
                norms = [ring(q) for q in root_norms]
            else:
                norms = [ring(root_norms)] * k

            G_mat = [[ring.zero() for _ in range(k)] for _ in range(k)]
            for i_idx, i in enumerate(idx_list):
                G_mat[i_idx][i_idx] = norms[i_idx]
                for j_idx in range(i_idx + 1, k):
                    j = idx_list[j_idx]
                    u, v = verts[i], verts[j]
                    pt = self.edge_weight(u, v) if hasattr(self, "edge_weight") else self[i, j]
                    assert pt[1] != 0, (
                        "Cannot reconstruct finite Gram entry from infinite "
                        "Vinberg ratio [1 : 0]"
                    )
                    t_val = pt[0] / pt[1]
                    val_sq = t_val * norms[i_idx] * norms[j_idx] / 4
                    root = sqrt(val_sq)
                    val = ring(root) if root in ring else root
                    G_mat[i_idx][j_idx] = val
                    G_mat[j_idx][i_idx] = val

            return matrix(G_mat)


# ---------------------------------------------------------------------------
# 3. Helper: Coerce to Projective Space Point in P^1(R)
# ---------------------------------------------------------------------------


def to_projective_point(P1: ProjectiveSpace, val: "ProjectivePointDatum") -> SchemeMorphism_point_projective_ring:
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
# 4. Combinatorial Vinberg Invariant Matrix
# ---------------------------------------------------------------------------


class CombinatorialVinbergInvariantMatrix(Parent):
    r"""
    A Combinatorial Vinberg Invariant Matrix $T = (t_{ij}) \in \mathbb{P}^1(R)^{n \times n}$.

    Encodes the normalized projective angles, mirror distances, and parabolic classifications
    of a reflection group natively without relying on Sage's flawed CoxeterMatrix.
    """

    def __init__(
        self,
        base_ring: "Ring",
        entries: dict[tuple[int, int], SchemeMorphism_point_projective_ring],
        rank: int,
        names: Sequence[str] | None = None,
        category: Category | None = None,
    ) -> None:
        cat = category if category is not None else ProjectiveWeightedGraphs().Symmetric()
        Parent.__init__(self, base=base_ring, category=cat)
        self._rank = int(rank)
        self._projective_space = ProjectiveSpace(base_ring, 1, "x,y")
        self._names = tuple(names) if names is not None else tuple(f"v_{i}" for i in range(self._rank))

        # Enforce symmetry and diagonal = (4 : 1)
        sym_entries = {}
        for i in range(self._rank):
            sym_entries[(i, i)] = self._projective_space([4, 1])
        for (i, j), pt in entries.items():
            if i != j:
                sym_entries[(i, j)] = pt
                sym_entries[(j, i)] = pt
        self._entries = sym_entries

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

    def __eq__(self, other: "MembershipInput") -> bool:
        r"""Return True if other is a CombinatorialVinbergInvariantMatrix with equal projective entries."""
        if not isinstance(other, CombinatorialVinbergInvariantMatrix):
            return False
        if self._rank != other._rank:
            return False
        n = self._rank
        for i in range(n):
            for j in range(n):
                pt1, pt2 = self[i, j], other[i, j]
                if pt1[0] * pt2[1] != pt2[0] * pt1[1]:
                    return False
        return True

    def __ne__(self, other: "MembershipInput") -> bool:
        return not (self == other)

    def is_infinity(self, i: int, j: int) -> bool:
        r"""Return True if $t_{ij} = \infty$ (denominator coordinate is 0)."""
        return self[i, j][1] == 0

    def affine_ratio(self, i: int, j: int) -> "Element | PlusInfinity":
        r"""Return the affine scalar $t_{ij} = x/y$ if finite, else infinity."""
        pt = self[i, j]
        if pt[1] == 0:
            return infinity
        return pt[0] / pt[1]

    def coxeter_order(self, i: int, j: int) -> "Integer | PlusInfinity":
        r"""
        Return the exact Coxeter bond exponent $m_{ij} \in \{1, 2, 3, \ldots, \infty\}$.

        Uses exact algebraic verification via $X_{\mathrm{ref}}$ (no numerical rounding).
        """
        if i == j:
            return Integer(1)
        pt = self[i, j]
        if pt[1] == 0:
            return infinity
        ratio = pt[0] / pt[1]
        if ratio >= 4:
            return infinity
        assert ratio >= 0, (
            f"Negative Vinberg invariant t[{i},{j}] = {ratio} is invalid"
        )

        cos_theta = sqrt(ratio) / 2
        n = X_ref._exact_n(cos_theta)
        assert n is not None, (
            f"Vinberg invariant t[{i},{j}] = {ratio} corresponds to "
            f"non-Coxeter angle (cos = {cos_theta})"
        )
        return n

    def is_valid(self) -> bool:
        r"""Return True if all entries represent valid Coxeter/Vinberg invariants.

        The same conditions :meth:`coxeter_order` asserts, computed as the
        predicate they are: an entry is valid when it is infinite, at least
        four, or a nonnegative ratio whose half square root is a reflection
        cosine.
        """
        n = self._rank
        for i in range(n):
            for j in range(i + 1, n):
                pt = self[i, j]
                if pt[1] == 0:
                    continue
                ratio = pt[0] / pt[1]
                if ratio >= 4:
                    continue
                if ratio < 0 or sqrt(ratio) / 2 not in X_ref:
                    return False
        return True

    def to_sage_coxeter_matrix(self) -> SageCoxeterMatrix:
        r"""Export to Sage's native :class:`CoxeterMatrix` (optional adapter)."""
        n = self._rank
        raw_entries = [
            [self.coxeter_order(i, j) for j in range(n)]
            for i in range(n)
        ]
        return SageCoxeterMatrix(raw_entries)

    def __hash__(self) -> int:
        canon_entries = tuple(
            sorted((k, (pt[0] / pt[1], 1) if pt[1] != 0 else (1, 0)) for k, pt in self._entries.items())
        )
        return hash((self.__class__, self._names, self._rank, canon_entries))

    def subdiagram(self, indices: Sequence[int | str]) -> "CombinatorialVinbergInvariantMatrix":
        r"""Return the induced subdiagram on the specified vertex indices or names."""
        name_to_idx = {name: i for i, name in enumerate(self._names)}
        idx_list = [name_to_idx[str(x)] if str(x) in name_to_idx else int(x) for x in indices]
        n_sub = len(idx_list)
        sub_entries = {}
        for new_i, old_i in enumerate(idx_list):
            for new_j, old_j in enumerate(idx_list):
                sub_entries[(new_i, new_j)] = self[old_i, old_j]
        sub_names = tuple(self._names[i] for i in idx_list)
        return CombinatorialVinbergInvariantMatrix(self.base_ring(), sub_entries, n_sub, names=sub_names)

    def submatrix(self, indices: Sequence[int | str]) -> "CombinatorialVinbergInvariantMatrix":
        r"""Alias for :meth:`subdiagram`."""
        return self.subdiagram(indices)

    def to_digraph(self) -> "ProjectiveWeightedDiGraph":
        r"""Construct a ProjectiveWeightedDiGraph with node and edge weights in P^1(R)."""
        return ProjectiveWeightedDiGraph.from_combinatorial_matrix(self)

    def graph(self) -> Graph:
        r"""Construct a Sage Graph representing the Coxeter diagram."""
        G = Graph()
        G.add_vertices(range(self._rank))
        for i in range(self._rank):
            for j in range(i + 1, self._rank):
                m = self.coxeter_order(i, j)
                if m > 2 or m is infinity:
                    G.add_edge(i, j, m)
        return G

    def tikz(self, title: str = "", labels: Sequence[str] | None = None) -> str:
        r"""Generate standalone LaTeX TikZ markup for the Coxeter diagram."""
        n = self._rank
        if labels is None:
            labels = [f"\\alpha_{{{i+1}}}" for i in range(n)]

        if n <= 4:
            pos = [(2 * i, 0) for i in range(n)]
        else:
            angles = [2 * math.pi * i / n for i in range(n)]
            pos = [(3 * math.cos(a), 3 * math.sin(a)) for a in angles]

        tikz = ["\\begin{tikzpicture}[scale=1.2]"]
        tikz.append("\\tikzstyle{vertex}=[circle,draw,minimum size=8mm,inner sep=2pt,fill=white]")

        for i in range(n):
            x, y = pos[i]
            tikz.append(f"\\node[vertex] (n{i}) at ({float(x):.2f},{float(y):.2f}) {{${labels[i]}$}};")

        for i in range(n):
            for j in range(i + 1, n):
                m = self.coxeter_order(i, j)
                if m == 3:
                    tikz.append(f"\\draw (n{i}) -- (n{j});")
                elif m == 4:
                    tikz.append(f"\\draw[double,double distance=1.5pt] (n{i}) -- (n{j});")
                elif m == 5:
                    tikz.append(f"\\draw[decorate,decoration={{zigzag,segment length=4mm,amplitude=1mm}}] (n{i}) -- (n{j});")
                elif m == 6:
                    tikz.append(f"\\draw[double,double distance=3pt] (n{i}) -- (n{j});")
                    tikz.append(f"\\draw (n{i}) -- (n{j});")
                elif m is infinity:
                    tikz.append(f"\\draw[dashed,thick] (n{i}) -- (n{j});")
                elif m > 6:
                    tikz.append(f"\\draw (n{i}) -- (n{j}) node[midway,above] {{\\small {m}}};")

        if title:
            avg_x = sum(p[0] for p in pos) / n
            tikz.append(f"\\node at ({avg_x:.2f},2.5) {{\\Large \\textbf{{{title}}}}};")

        tikz.append("\\end{tikzpicture}")
        return "\n".join(tikz)

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
# 4. Constructor Functions
# ---------------------------------------------------------------------------


def vinberg_invariant_matrix_from_gram(
    G: Matrix,
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
    base_ring: "Ring",
    components: "Sequence[Sequence[ProjectivePointDatum]]",
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


# ---------------------------------------------------------------------------
# 5. Projective Weighted Directed Graphs (Node and Edge Weights in P^1(R))
# ---------------------------------------------------------------------------


class ProjectiveWeightedDiGraph(Parent):
    r"""
    A Directed Graph with both node weights and edge weights in $\mathbb{P}^1(R)$.

    Bidirectionally dual to :class:`CombinatorialVinbergInvariantMatrix`:
    - Node weights correspond to diagonal invariants $t_{ii} \in \mathbb{P}^1(R)$.
    - Directed edge weights correspond to off-diagonal invariants $t_{ij} \in \mathbb{P}^1(R)$.
    """

    def __init__(
        self,
        base_ring: "Ring",
        vertices: "Sequence[VertexLabel]",
        vertex_weights: "Mapping[VertexLabel, ProjectivePointDatum] | Sequence[ProjectivePointDatum] | None" = None,
        edges: "Sequence[tuple[VertexLabel, VertexLabel, ProjectivePointDatum]] | None" = None,
        category: Category | None = None,
    ) -> None:
        cat = category if category is not None else ProjectiveWeightedGraphs()
        Parent.__init__(self, base=base_ring, category=cat)
        self._projective_space = ProjectiveSpace(base_ring, 1, "x,y")
        self._vertices = tuple(str(v) for v in vertices)
        self._v_to_idx = {v: i for i, v in enumerate(self._vertices)}

        # 1. Initialize vertex weights
        v_weights = {}
        if isinstance(vertex_weights, Mapping):
            for v in self._vertices:
                wt = vertex_weights.get(v, vertex_weights.get(self._v_to_idx[v], [4, 1]))
                v_weights[v] = to_projective_point(self._projective_space, wt)
        elif isinstance(vertex_weights, Sequence):
            for i, v in enumerate(self._vertices):
                wt = vertex_weights[i] if i < len(vertex_weights) else [4, 1]
                v_weights[v] = to_projective_point(self._projective_space, wt)
        else:
            for v in self._vertices:
                v_weights[v] = self._projective_space([4, 1])
        self._vertex_weights = v_weights

        # 2. Initialize directed edge weights
        e_weights = {}
        if edges is not None:
            for e in edges:
                u_str, v_str = str(e[0]), str(e[1])
                wt = to_projective_point(self._projective_space, e[2])
                e_weights[(u_str, v_str)] = wt
        self._edge_weights = e_weights

    def vertices(self) -> tuple[str, ...]:
        r"""Return the tuple of vertex labels."""
        return self._vertices

    def num_vertices(self) -> int:
        r"""Return the number of vertices."""
        return len(self._vertices)

    def vertex_weight(self, v: "VertexLabel") -> SchemeMorphism_point_projective_ring:
        r"""Return the weight of vertex $v$ in $\mathbb{P}^1(R)$."""
        v_str = str(v)
        return self._vertex_weights.get(v_str, self._projective_space([4, 1]))

    def edge_weight(self, u: "VertexLabel", v: "VertexLabel") -> SchemeMorphism_point_projective_ring:
        r"""Return the directed edge weight $(u \to v)$ in $\mathbb{P}^1(R)$."""
        u_str, v_str = str(u), str(v)
        return self._edge_weights.get((u_str, v_str), self._projective_space([0, 1]))

    def edges(self) -> list[tuple[str, str, SchemeMorphism_point_projective_ring]]:
        r"""Return all directed edges with non-zero weight."""
        result = []
        for (u, v), wt in self._edge_weights.items():
            if wt[0] != 0:  # Non-zero projective point
                result.append((u, v, wt))
        return result

    def __eq__(self, other: "MembershipInput") -> bool:
        r"""Return True if other is a ProjectiveWeightedDiGraph with equal vertices and weights."""
        if not isinstance(other, ProjectiveWeightedDiGraph):
            return False
        if self._vertices != other._vertices:
            return False
        for v in self._vertices:
            pt1, pt2 = self.vertex_weight(v), other.vertex_weight(v)
            if pt1[0] * pt2[1] != pt2[0] * pt1[1]:
                return False
        for u in self._vertices:
            for v in self._vertices:
                pt1, pt2 = self.edge_weight(u, v), other.edge_weight(u, v)
                if pt1[0] * pt2[1] != pt2[0] * pt1[1]:
                    return False
        return True

    def __ne__(self, other: "MembershipInput") -> bool:
        return not (self == other)

    def __hash__(self) -> int:
        v_wts = tuple(
            sorted((v, (wt[0] / wt[1], 1) if wt[1] != 0 else (1, 0)) for v, wt in self._vertex_weights.items())
        )
        e_wts = tuple(
            sorted((k, (wt[0] / wt[1], 1) if wt[1] != 0 else (1, 0)) for k, wt in self._edge_weights.items())
        )
        return hash((self.__class__, self._vertices, v_wts, e_wts))

    def subdiagram(self, vertices: Sequence[str | int]) -> "ProjectiveWeightedDiGraph":
        r"""Return the induced subdiagram (subgraph) on the specified vertex subset."""
        target_v = tuple(str(self._vertices[v]) if isinstance(v, (int, Integer)) else str(v) for v in vertices)
        v_set = set(target_v)
        sub_v_weights = {v: self.vertex_weight(v) for v in target_v}
        sub_edges = [
            (u, v, wt) for (u, v), wt in self._edge_weights.items()
            if u in v_set and v in v_set and wt[0] != 0
        ]
        return ProjectiveWeightedDiGraph(
            self.base_ring(), target_v, vertex_weights=sub_v_weights, edges=sub_edges
        )

    def subgraph(self, vertices: Sequence[str | int]) -> "ProjectiveWeightedDiGraph":
        r"""Alias for :meth:`subdiagram`."""
        return self.subdiagram(vertices)

    def to_combinatorial_matrix(self) -> CombinatorialVinbergInvariantMatrix:
        r"""
        Convert to the dual CombinatorialVinbergInvariantMatrix.
        """
        n = len(self._vertices)
        entries = {}
        for i, u in enumerate(self._vertices):
            entries[(i, i)] = self.vertex_weight(u)
            for j, v in enumerate(self._vertices):
                if i != j:
                    wt_uv = self.edge_weight(u, v)
                    wt_vu = self.edge_weight(v, u)
                    wt = wt_uv if wt_uv[0] != 0 else wt_vu
                    entries[(i, j)] = wt
        return CombinatorialVinbergInvariantMatrix(
            self.base_ring(), entries, n, names=self._vertices
        )

    def to_vinberg_matrix(self) -> CombinatorialVinbergInvariantMatrix:
        r"""Alias for :meth:`to_combinatorial_matrix`."""
        return self.to_combinatorial_matrix()

    @classmethod
    def from_combinatorial_matrix(
        cls, T: CombinatorialVinbergInvariantMatrix
    ) -> "ProjectiveWeightedDiGraph":
        r"""
        Construct a ProjectiveWeightedDiGraph from a CombinatorialVinbergInvariantMatrix.
        """
        ring = T.base_ring()
        verts = list(T.variable_names())
        n = T.rank()
        v_weights = {verts[i]: T[i, i] for i in range(n)}
        edges = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    wt = T[i, j]
                    if wt[0] != 0:
                        edges.append((verts[i], verts[j], wt))
        return cls(ring, verts, vertex_weights=v_weights, edges=edges)

    def underlying_digraph(self) -> "DiGraph":
        r"""Construct a native Sage DiGraph carrying the projective weights as attributes."""
        from sage.graphs.digraph import DiGraph
        D = DiGraph(multiedges=False)
        for v in self._vertices:
            D.add_vertex(v)
            D.set_vertex(v, self.vertex_weight(v))
        for u, v, wt in self.edges():
            D.add_edge(u, v, wt)
        return D

    def _repr_(self) -> str:
        return (
            f"Projective Weighted DiGraph on {self.num_vertices()} vertices over {self.base_ring()}:\n"
            f"  Vertices: {self._vertices}\n"
            f"  Edges: {[(u, v, str(wt)) for u, v, wt in self.edges()]}"
        )


def projective_weighted_digraph(
    base_ring: "Ring",
    vertices: "Sequence[VertexLabel]",
    vertex_weights: "Mapping[VertexLabel, ProjectivePointDatum] | Sequence[ProjectivePointDatum] | None" = None,
    edges: "Sequence[tuple[VertexLabel, VertexLabel, ProjectivePointDatum]] | None" = None,
) -> ProjectiveWeightedDiGraph:
    r"""Construct a ProjectiveWeightedDiGraph."""
    return ProjectiveWeightedDiGraph(
        base_ring, vertices, vertex_weights=vertex_weights, edges=edges
    )

