r"""Coble-surface lattice data recovered from the research log.

Two configurations from the ``Coble Lattice Invariants`` notebook
(``archives/notebooks/``), re-expressed on the owned catalogue surface:

* Coble's $0$-cusp candidates: seventeen isotropic vectors of
  $T_{\mathrm{Co}}$, the Coble analogue of the Sterk cusp list
  (:mod:`~dzack_research.preamble.sterk`), transported to $T_{\mathrm{En}}$
  and $T_{\mathrm{dP}}$ through the owned embedding chain
  :attr:`Embeddings.TCo_into_TEn` and :attr:`Embeddings.TEn_into_TdP` --
  the arrows the notebook wrote out by hand ($h\mapsto e+f$, then
  $a_i\mapsto a_i+b_i$).

* An eleven-root Coxeter configuration in the Nikulin $(10,10,1)$ lattice,
  extracted in the notebook as the invariant lattice of an involution of
  the $22$ roots $v_1,\ldots,v_{22}$ of :meth:`Sterk.roots_18_2_0` in
  $T_{\mathrm{dP}}$ -- named for the Nikulin invariants
  $(r,a,\delta)=(18,2,0)$ -- namely the involution swapping
  $v_1\ldots v_8$ with $v_9\ldots v_{16}$ and $v_{17},v_{18}$ with
  $v_{19},v_{20}$, which is the exchange of the two $E_8$ blocks of
  $T_{\mathrm{dP}}$.

Corrections recorded at this landing (2026-08-20 migration):

* The notebook's ``divisibility(v, L)`` took the *minimum* of the nonzero
  pairings where the divisibility is their gcd, so its tabulated values are
  upper bounds, not divisibilities.  Nothing of that table is carried here;
  the owned ``div`` (``integral_lattices.sage``) answers from the
  definition.

* The notebook's printed ten-root Gram matrix and its printed
  change-of-basis witness came from different execution states of one
  session: no orientation of the asserted congruence holds between the two
  prints as printed.  They are reconciled by the root reindexing
  $[0,1,9,5,4,6,2,7,8,3]$, under which the configuration recorded below
  reproduces the printed Gram exactly.  Every vector below was re-verified
  by exact integer arithmetic at migration, independent of the session.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
    from dzack_research.preamble.lexicon import ModuleElement

from dzack_research.preamble.catalogue import Embeddings, Lattices, TwoElementary
from dzack_research.preamble.categories.modules.framed.formed.integrallattice.coxeter_diagrams import FiniteCoxeterDiagram
from dzack_research.preamble.utilities import zipsum

__all__ = [
    "Coble",
]


class Coble:
    r"""Coble cusp candidates and the invariant rank-$10$ root configuration.

    Embeddings of the Coble/Enriques/del Pezzo chain are
    :attr:`Embeddings`, not methods here.
    """

    @staticmethod
    def isotropic_vectors() -> dict[str, "ModuleElement"]:
        r"""Return the seventeen recorded isotropic vectors of $T_{\mathrm{Co}}$.

        The Coble cusp candidates, written over the basis
        $h, e', f', a_1, \ldots, a_8$ of
        $T_{\mathrm{Co}} = \langle2\rangle \oplus U(2) \oplus E_8(2)$ and
        asserted isotropic at construction.  Divisibilities are questions
        for the owned ``div``, per the correction in the module docstring.
        """
        Tco = Lattices.Tco
        generators = list(Tco.module_generators())
        h = generators[0]
        ep, fp = generators[1], generators[2]
        a = {index: generators[2 + index] for index in range(1, 9)}
        vectors = {
            "w1": ep,
            "w2": fp,
            "w3": 2 * h + a[1] + a[2],
            "w4": ep + fp + a[1],
            "w5": 2 * h - fp - a[1] - a[6] - a[7] - a[8],
            "w6": 8 * ep + fp + a[4] - 2 * a[5] - a[8],
            "w7": 2 * h + ep - a[1] - a[2],
            "w8": 2 * h + ep - a[2] - a[3],
            "w9": 2 * h - a[1] + a[2] - a[3],
            "w10": 2 * ep + fp - a[1] - a[8],
            "w11": 5 * ep + fp + a[2] + 2 * a[3],
            "w12": 2 * h + a[1] - a[4],
            "w13": 2 * h + a[2] - a[5],
            "w14": 2 * h + a[3] - a[6],
            "w15": 2 * h + a[4] - a[7],
            "w16": 2 * h + a[5] - a[8],
            "w17": 2 * h - a[6] - a[8],
        }
        assert len(vectors) == 17
        for name, vector_ in vectors.items():
            assert vector_.q() == 0, f"{name} is not isotropic: q = {vector_.q()}"
        return vectors

    @staticmethod
    def isotropic_vectors_in_TEn() -> dict[str, "ModuleElement"]:
        r"""Return the cusp candidates as elements of $T_{\mathrm{En}}$.

        The images under :attr:`Embeddings.TCo_into_TEn` -- the arrow whose
        $\langle2\rangle$ block lands diagonally in $U$ ($h\mapsto e+f$),
        which is the substitution the notebook performed by hand.
        """
        return {
            name: Embeddings.TCo_into_TEn(vector_)
            for name, vector_ in Coble.isotropic_vectors().items()
        }

    @staticmethod
    def isotropic_vectors_in_TdP() -> dict[str, "ModuleElement"]:
        r"""Return the cusp candidates as elements of $T_{\mathrm{dP}}$.

        The chain $T_{\mathrm{Co}}\hookrightarrow T_{\mathrm{En}}
        \hookrightarrow T_{\mathrm{dP}}$, the second arrow placing $E_8(2)$
        diagonally in $E_8\oplus E_8$ ($a_i\mapsto a_i+b_i$, the notebook's
        hand substitution).
        """
        return {
            name: Embeddings.TEn_into_TdP(vector_)
            for name, vector_ in Coble.isotropic_vectors_in_TEn().items()
        }

    @staticmethod
    def rank_ten_coxeter_roots() -> tuple[
        "FormModule",
        tuple["ModuleElement", ...],
    ]:
        r"""Return the eleven-root configuration in the Nikulin $(10,10,1)$
        lattice, with the lattice.

        The notebook extracted a rank-$10$ lattice as the invariant lattice
        of the block-exchange involution of the $22$ roots of
        :meth:`Sterk.roots_18_2_0`, found its induced roots (eleven of square $-2$ and
        $-4$, after primitivizing and doubling the square $-1$ images), and
        identified the lattice with the $(10,10,1)$ class by an explicit
        engine isometry witness onto $U(2)\oplus A_1^{8}$ -- the catalogue's
        own spelling of that Nikulin row (its invariant-level comparison
        target $\langle2\rangle\oplus\langle-2\rangle\oplus E_8(2)$ is the
        same class by Nikulin uniqueness).

        Recorded here are the eleven roots transported through that witness
        into ``TwoElementary[(10, 10, 1)]``, re-verified exactly at
        migration: the squares are eight $-4$ and two $-2$ among the first
        ten plus a $-4$ eleventh, every pairing is $0$ or $2$, the first ten
        are a $\mathbb Z$-basis of the lattice (the coordinate matrix is
        unimodular), and the eleventh root -- the registry's
        $-b_0+b_1+b_2+2b_4+b_5-b_6-b_7-2b_8-2b_9$ over the
        $A_1^{8}\oplus U(2)$ order -- pairs $2$ with exactly one of them.
        Reflection integrality is automatic: every Gram entry of a
        $2$-elementary even lattice here is even, so square $-4$ vectors
        satisfy the criterion ``reflection`` asserts.
        """
        lattice = TwoElementary[(10, 10, 1)]
        generators = lattice.module_generators()
        zero = lattice.zero()
        # Coordinates over the catalogue order (U(2) pair first, then the
        # eight A_1 generators); data, not elements, so each row is read
        # through the module generators.
        coordinate_rows = (
            (0, 0, 1, 0, 0, 0, 0, 0, -1, 0),
            (0, 0, 0, -1, 0, 0, 0, 0, 0, -1),
            (2, 1, 1, -1, 0, 0, -1, -1, 1, 1),
            (0, 0, -1, 0, 0, 0, 0, -1, 0, 0),
            (0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
            (0, 0, 0, 0, -1, 0, 0, 1, 0, 0),
            (0, 0, 0, 1, 0, 0, 0, 0, 1, 0),
            (-2, -1, -1, 1, 1, 0, 0, 1, -1, -1),
            (-2, -1, -1, 0, 1, -1, 1, 1, -1, 0),
            (-1, 0, 0, 0, 0, 0, 1, 0, 0, 0),
            (-2, -2, -1, 1, 1, 0, 2, 1, -1, -1),
        )
        roots = tuple(
            zipsum(row, generators, zero) for row in coordinate_rows
        )
        assert len(roots) == 11
        for index, root in enumerate(roots, start=1r):
            square = root.q()
            assert square in (-2, -4), (
                f"rank-ten configuration root {index} has square {square}"
            )
        return lattice, roots

    @staticmethod
    def rank_ten_diagram() -> FiniteCoxeterDiagram:
        r"""Return the eleven-vertex rooted Coxeter diagram of
        :meth:`rank_ten_coxeter_roots`.

        Bonds derived from the root Gram data by the owned edge table:
        pairing $2$ between square $-4$ roots is a single bond ($m=3$),
        between a $-2$ and a $-4$ root a double bond ($m=4$).
        """
        _lattice, roots = Coble.rank_ten_coxeter_roots()
        return FiniteCoxeterDiagram.from_roots(
            roots,
            names=tuple(f"r_{index + 1}" for index in range(len(roots))),
        )
