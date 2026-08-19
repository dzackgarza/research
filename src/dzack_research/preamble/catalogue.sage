r"""Named integral lattices used by the preamble.

Root lattices use the negative-definite convention.

Coordinates are data, not elements: a tuple/list/vector never counts as a
lattice element by itself. Build an element only by extracting
``module_generators()`` and summing ``coefficient * generator``.

The named specimens (``Lattices.E8``, ``Lattices.U``, ...) live on the
``Lattices`` category itself, defined inline in ``lattices.sage`` -- this
module only holds what is catalogue-specific: the ``TwoElementary`` and
``NegativeDefTwoElementary`` tables, the named involutions and embeddings, and
the ``register_indecomposable`` calls.  Call :meth:`Lattices.install` (``init.sage``
does this) to bind specimens and the $\Lambda_{K3}$ module_generators into the
session namespace.

``TwoElementary`` is Nikulin's table of 75 even indefinite 2-elementary
lattices of signature $(1,r-1)$, keyed by $(r,a,\delta)$.

``NegativeDefTwoElementary`` is Alexeev--Engel Table 2, keyed by the
negative-definite quotient's own $(r,a,\delta)$ invariants.
"""

from dzack_research.preamble.utilities import zipsum
from dzack_research.preamble.categories.rings.rings import install_session_rings
from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import (
    IntegralLattices,
    register_indecomposable,
    _integral_lattice_with_names,
)
from sage.matrix.constructor import matrix
from sage.sets.integer_range import IntegerRange
from sage.structure.parent import Parent
from sage.rings.integer_ring import ZZ as SageZZ

import sys as _sys

# ``install.sage`` imports this file as a module, so by the time a session or
# a test ``load``s it the catalogue is already built.  Running the body again
# would rebuild every specimen a second time (a different object, failing
# every identity check, and paying the whole construction twice).  A second
# load re-exports what the module holds, exactly as ``install.sage`` does for
# the categories.
_built = _sys.modules.get("dzack_research.preamble.catalogue")

if _built is not None and vars(_built) is not globals():
    globals().update(
        {
            _name: _value
            for _name, _value in vars(_built).items()
            if not _name.startswith("_")
        }
    )
else:
    # The preamble's own constructor, installed over Sage's name.  Sage's
    # function of this name returns a submodule of a base-changed module over
    # $\mathbb Q$, which is outside the owned categories -- so a lattice built
    # through it answers Sage's ``discriminant_group`` rather than this
    # preamble's, and takes no ``names=``, which is what the
    # ``L.<e,f> = ...`` sugar passes.
    IntegralLattice = _integral_lattice_with_names

    __all__ = [
        "Embeddings",
        "Involutions",
        "Lattices",
        "NegativeDefTwoElementary",
        "TwoElementary",
    ]

    from dzack_research.preamble.categories.modules.framed.formed.lattices import (
        Lattices,
    )

    # Named specimens, attached directly onto ``Lattices`` (which declares them
    # as ``ClassVar`` for the type checker).  Building them here -- not in
    # ``lattices.sage`` -- avoids importing the constructor across the
    # ``integral_lattices`` -> ``lattices`` edge at module load.  Root lattices
    # use the negative-definite convention.
    _with = _integral_lattice_with_names

    Lattices.Zero = _with(matrix(SageZZ, 0, 0, []))
    Lattices.Z = _with(matrix(SageZZ, [1]))
    Lattices.Z_2 = Lattices.Z.twist(2)

    Lattices.H = _with("H")
    Lattices.H_2 = Lattices.H.twist(2)
    Lattices.U = Lattices.H
    Lattices.U_2 = Lattices.H_2

    # The named root lattices arrive negative definite from the single
    # construction site (``_gram_from_name`` applies the AG convention to
    # the root realization); nothing here re-twists them.
    for _rank in range(1, 22):
        setattr(Lattices, f"A{_rank}", _with(f"A{_rank}"))
    for _rank in range(2, 23):
        setattr(Lattices, f"D{_rank}", _with(f"D{_rank}"))

    Lattices.E6 = _with("E6")
    Lattices.E7 = _with("E7")
    Lattices.E8 = _with("E8")
    Lattices.E8_2 = Lattices.E8.twist(2)

    Lattices.E10 = Lattices.U + Lattices.E8
    Lattices.E10_2 = Lattices.U_2 + Lattices.E8_2

    Lattices.Sdp = Lattices.U_2
    Lattices.SEn = Lattices.E10_2
    Lattices.Tco = Lattices.Z_2 + Lattices.U_2 + Lattices.E8_2
    Lattices.Sco = Lattices.Z_2.twist(-1) + Lattices.U_2 + Lattices.E8_2
    Lattices.LpNik = Lattices.U**3 + Lattices.E8_2
    Lattices.LmNik = Lattices.E8_2
    Lattices.LK3_2 = Lattices.Z.twist(-2) + Lattices.U**2 + Lattices.E8**2
    Lattices.LK3_4 = Lattices.Z.twist(-4) + Lattices.U**2 + Lattices.E8**2

    # Named bases -- matching the old init.sage session.  The ``L.<generators> =``
    # sugar only injected the generator names into the builder's local scope; the
    # lattice is the object bound here.
    Lattices.LK3 = (Lattices.U**3).direct_sum([Lattices.E8**2])
    Lattices.TEn = Lattices.U.direct_sum([Lattices.E10_2])
    Lattices.TdP = Lattices.U.direct_sum([Lattices.U_2, Lattices.E8, Lattices.E8])
    Lattices.L_20_2_0 = Lattices.TdP

    # Registry of specimens, what ``Lattices.namespace`` and ``Lattices.install``
    # read -- not a scan for attributes that look like lattices.
    Lattices._specimens = {
        _name: _value
        for _name, _value in vars(Lattices).items()
        if not _name.startswith("_")
        and isinstance(_value, Parent)
        and _value in IntegralLattices()
    }

    # Names for the blocks a decomposition can actually produce.  Matching is
    # Gram equality, so only indecomposable lattices belong here: everything
    # else splits on construction and is named through its own summands.
    #
    # $I_{p,q}$ and $II_{p,q}$ take priority, but they contribute only these
    # two entries.  Both families are unique only when indefinite, and an
    # indefinite unimodular lattice decomposes ($I_{p,q}=\langle1\rangle^p
    # \oplus\langle-1\rangle^q$, and $II_{p,q}\cong U^a\oplus E_8^b$ by Milnor),
    # so it never reaches a block.  What survives is rank one, and registering
    # it here is what makes the twist search print $\langle-2\rangle$ as
    # $I_{0,1}(2)$.
    register_indecomposable("I_{1,0}", Lattices.IPQ(1, 0))
    register_indecomposable("I_{0,1}", Lattices.IPQ(0, 1))

    # $A_1$ and $D_2$ are deliberately not searched: $A_1$ is $I_{0,1}(2)$, and
    # $D_2$ is $\langle-2\rangle^2$, which decomposes before any lookup runs.
    # $U$ and $E_8$ are $II_{1,1}$ and $II_{0,8}$, but keep their own names,
    # which say more than the signature does.
    for _rank in IntegerRange(2, 22):
        register_indecomposable(f"A_{{{_rank}}}", Lattices.root_lattice("A", _rank))
    for _rank in IntegerRange(3, 23):
        register_indecomposable(f"D_{{{_rank}}}", Lattices.root_lattice("D", _rank))
    for _rank in (6, 7, 8):
        register_indecomposable(f"E_{{{_rank}}}", Lattices.root_lattice("E", _rank))
    register_indecomposable("U", Lattices.U)


    # Nikulin's 75 even indefinite 2-elementary lattices of signature $(1,r-1)$,
    # keyed by $(r,a,\delta)$.  Source: Nikulin (1979); Alexeev–Engel–et al.,
    # arXiv:2208.10383 Fig. 1.  Plain root-lattice entries from Table 2 supply
    # additional hyperbolic models via ``U`` or ``U(2)`` direct sums.  Starred
    # glued-overlattice entries are intentionally not encoded here.
    #
    # Classification check used by this catalogue: Nikulin's uniqueness theorem is
    # for indefinite even 2-elementary lattices.  Thus a candidate below is the
    # unique isometry class once the full lattice, not just the Table 2 definite
    # root piece, is verified to have signature $(1,r-1)$ and invariants
    # $(r,a,\delta)$ matching its key.  Definite Table 2 root pieces alone are not
    # uniqueness certificates; a definite genus may contain multiple isometry
    # classes.
    TwoElementary = {
            (1, 1, 1): Lattices.Z.twist(2),
            (2, 0, 0): Lattices.U,
            (2, 2, 0): Lattices.U_2,
            (2, 2, 1): Lattices.Z.twist(2) + Lattices.Z.twist(-2),
            (3, 1, 1): Lattices.U + Lattices.A1,
            (3, 3, 1): Lattices.U_2 + Lattices.A1,
            (4, 2, 1): Lattices.U + Lattices.A1**2,
            (4, 4, 1): Lattices.U_2 + Lattices.A1**2,
            (5, 3, 1): Lattices.U + Lattices.A1**3,
            (5, 5, 1): Lattices.U_2 + Lattices.A1**3,
            (6, 2, 0): Lattices.U + Lattices.D4,
            (6, 4, 0): Lattices.U_2 + Lattices.D4,
            (6, 4, 1): Lattices.U + Lattices.A1**4,
            (6, 6, 1): Lattices.U_2 + Lattices.A1**4,
            (7, 3, 1): Lattices.U + Lattices.D4 + Lattices.A1,
            (7, 5, 1): Lattices.U_2 + Lattices.A1 + Lattices.D4,
            (7, 7, 1): Lattices.U_2 + Lattices.A1**5,
            (8, 2, 1): Lattices.U + Lattices.D6,
            (8, 4, 1): Lattices.U_2 + Lattices.D6,
            (8, 6, 1): Lattices.U_2 + Lattices.A1**2 + Lattices.D4,
            (8, 8, 1): Lattices.U_2 + Lattices.A1**6,
            (9, 1, 1): Lattices.U + Lattices.E7,
            (9, 3, 1): Lattices.U_2 + Lattices.E7,
            (9, 5, 1): Lattices.U_2 + Lattices.A1 + Lattices.D6,
            (9, 7, 1): Lattices.U + Lattices.A1**7,
            (9, 9, 1): Lattices.U_2 + Lattices.A1**7,
            (10, 0, 0): Lattices.E10,
            (10, 2, 0): Lattices.U + Lattices.D8,
            (10, 2, 1): Lattices.U + Lattices.E7 + Lattices.A1,
            (10, 4, 0): Lattices.U_2 + Lattices.D8,
            (10, 4, 1): Lattices.U + Lattices.D6 + Lattices.A1**2,
            (10, 6, 0): Lattices.U_2 + Lattices.D4**2,
            (10, 6, 1): Lattices.U_2 + Lattices.D6 + Lattices.A1**2,
            (10, 8, 0): Lattices.U + Lattices.E8_2,
            (10, 8, 1): Lattices.U + Lattices.A1**8,
            (10, 10, 0): Lattices.E10_2,
            (10, 10, 1): Lattices.U_2 + Lattices.A1**8,
            (11, 1, 1): Lattices.U + Lattices.E8 + Lattices.A1,
            (11, 3, 1): Lattices.U + Lattices.D8 + Lattices.A1,
            (11, 5, 1): Lattices.U + Lattices.D6 + Lattices.A1**3,
            (11, 7, 1): Lattices.U_2 + Lattices.D6 + Lattices.A1**3,
            (11, 9, 1): Lattices.U + Lattices.A1 + Lattices.E8_2,
            (11, 11, 1): Lattices.U_2 + Lattices.A1 + Lattices.E8_2,
            (12, 2, 1): Lattices.U + Lattices.E8 + Lattices.A1**2,
            (12, 4, 1): Lattices.U + Lattices.D8 + Lattices.A1**2,
            (12, 6, 1): Lattices.U_2 + Lattices.D4 + Lattices.D6,
            (12, 8, 1): Lattices.U_2 + Lattices.D6 + Lattices.A1**4,
            (12, 10, 1): Lattices.U + Lattices.A1**2 + Lattices.E8_2,
            (13, 3, 1): Lattices.U + Lattices.E7 + Lattices.D4,
            (13, 5, 1): Lattices.U_2 + Lattices.D4 + Lattices.E7,
            (13, 7, 1): Lattices.U + Lattices.D6 + Lattices.A1**5,
            (13, 9, 1): Lattices.U_2 + Lattices.D6 + Lattices.A1**5,
            (14, 2, 0): Lattices.U + Lattices.D4 + Lattices.E8,
            (14, 4, 0): Lattices.U + Lattices.D4 + Lattices.D8,
            (14, 4, 1): Lattices.U + Lattices.D6**2,
            (14, 6, 0): Lattices.U_2 + Lattices.D4 + Lattices.D8,
            (14, 6, 1): Lattices.U_2 + Lattices.D6**2,
            (14, 8, 1): Lattices.U_2 + Lattices.D6 + Lattices.D4 + Lattices.A1**2,
            (15, 3, 1): Lattices.U + Lattices.E7 + Lattices.D6,
            (15, 5, 1): Lattices.U_2 + Lattices.D6 + Lattices.E7,
            (15, 7, 1): Lattices.U_2 + Lattices.D8 + Lattices.D4 + Lattices.A1,
            (16, 2, 1): Lattices.U + Lattices.D6 + Lattices.E8,
            (16, 4, 1): Lattices.U + Lattices.D6 + Lattices.D8,
            (16, 6, 1): Lattices.U_2 + Lattices.D6 + Lattices.D8,
            (17, 1, 1): Lattices.U + Lattices.E7 + Lattices.E8,
            (17, 3, 1): Lattices.U + Lattices.D8 + Lattices.E7,
            (17, 5, 1): Lattices.U_2 + Lattices.D8 + Lattices.E7,
            (18, 0, 0): Lattices.U + Lattices.E8**2,
            (18, 2, 0): Lattices.U + Lattices.D8 + Lattices.E8,
            (18, 2, 1): Lattices.U + Lattices.E8 + Lattices.E7 + Lattices.A1,
            (18, 4, 0): Lattices.U + Lattices.D8**2,
            (18, 4, 1): Lattices.U_2 + Lattices.E8 + Lattices.E7 + Lattices.A1,
            (19, 1, 1): Lattices.U + Lattices.E8**2 + Lattices.A1,
            (19, 3, 1): Lattices.U_2 + Lattices.E8**2 + Lattices.A1,
            (20, 2, 1): Lattices.U + Lattices.E8**2 + Lattices.A1**2,
    }


    # Alexeev--Engel Table 2: even negative-definite 2-elementary lattices
    # appearing at 1-cusps, keyed by the table's own $(r,a,\delta)$ invariants.
    #
    # Theory: if an even overlattice $\overline R$ of an even lattice $R$ is
    # obtained by gluing, the gluing datum is a totally isotropic subgroup
    # $H \subset A_R$ of the discriminant quadratic module.  Then
    # $A_{\overline R} \simeq H^\perp/H$, so
    # $|A_{\overline R}| = |A_R|/|H|^2$.  The subgroup $H$ is not part of AE's
    # table data and need not be unique.  The row determines the lattice only up
    # to isometry, by the displayed root sublattice $R$ together with the listed
    # $(r,a,\delta)$ invariants.
    #
    # Production method for the starred rows: enumerate totally isotropic
    # subgroups $H \subset A_R$ of the forced order, construct the corresponding
    # overlattices, keep those with the keyed invariants and the displayed
    # $(-2)$-root sublattice, and verify that all surviving choices are isometric
    # via the exact positive-definite form test on $-\mathrm{Gram}$.  The vectors
    # below are one representative choice from that single isometry class; they
    # are not parsed from the AE labels.
    NegativeDefTwoElementary = {
            (0, 0, 0): [_integral_lattice_with_names(matrix(SageZZ, 0, 0, []))],
            (1, 1, 1): [Lattices.A1],
            (2, 2, 1): [Lattices.A1**2],
            (3, 3, 1): [Lattices.A1**3],
            (4, 2, 0): [Lattices.D4],
            (4, 4, 1): [Lattices.A1**4],
            (5, 3, 1): [Lattices.D4 + Lattices.A1],
            (5, 5, 1): [Lattices.A1**5],
            (6, 2, 1): [Lattices.D6],
            (6, 4, 1): [Lattices.D4 + Lattices.A1**2],
            (6, 6, 1): [Lattices.A1**6],
            (7, 1, 1): [Lattices.E7],
            (7, 3, 1): [Lattices.D6 + Lattices.A1],
            (7, 5, 1): [Lattices.D4 + Lattices.A1**3],
            (7, 7, 1): [Lattices.A1**7],
            (8, 0, 0): [Lattices.E8],
            (8, 2, 0): [Lattices.D8],
            (8, 2, 1): [Lattices.E7 + Lattices.A1],
            (8, 4, 0): [Lattices.D4**2],
            (8, 4, 1): [Lattices.D6 + Lattices.A1**2],
            (8, 6, 0): [
                (_L := Lattices.A1**8).glue(zipsum(
                [1, 1, 1, 1, 1, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
            ],
            (8, 6, 1): [Lattices.D4 + Lattices.A1**4],
            (8, 8, 0): [Lattices.E8_2],
            (8, 8, 1): [Lattices.A1**8],
            (9, 1, 1): [Lattices.E8 + Lattices.A1],
            (9, 3, 1): [Lattices.E7 + Lattices.A1**2, Lattices.D8 + Lattices.A1],
            (9, 5, 1): [Lattices.D6 + Lattices.A1**3, Lattices.D4**2 + Lattices.A1],
            (9, 7, 1): [
                (_L := Lattices.A1**9).glue(zipsum(
                [0, 1, 1, 1, 1, 1, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                Lattices.A1**5 + Lattices.D4,
            ],
            (9, 9, 1): [Lattices.A1**9, Lattices.A1 + Lattices.E8_2],
            (10, 2, 1): [Lattices.D10, Lattices.E8 + Lattices.A1**2],
            (10, 4, 1): [
                Lattices.E7 + Lattices.A1**3,
                Lattices.D8 + Lattices.A1**2,
                Lattices.D6 + Lattices.D4,
            ],
            (10, 6, 1): [
                Lattices.D4**2 + Lattices.A1**2,  # AE label: D_4^2 A_1^2*
                (_L := Lattices.A1**6 + Lattices.D4).glue(zipsum(
                [1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                Lattices.D6 + Lattices.A1**4,
            ],
            (10, 8, 1): [
                Lattices.D4 + Lattices.A1**6,  # AE label: D_4 A_1^6*
                (_L := Lattices.A1**10).glue(zipsum(
                [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                (_L := Lattices.A3 + Lattices.E7.twist(2)).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
            ],
            (11, 3, 1): [
                Lattices.D10 + Lattices.A1,
                Lattices.E8 + Lattices.A1**3,
                Lattices.E7 + Lattices.D4,
            ],
            (11, 5, 1): [
                Lattices.D6 + Lattices.D4 + Lattices.A1,
                Lattices.D8 + Lattices.A1**3,
                Lattices.E7 + Lattices.A1**4,
                (_L := Lattices.D6 + Lattices.A1**5).glue(zipsum(
                [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
            ],
            (11, 7, 1): [
                Lattices.D6 + Lattices.A1**5,
                (_L := Lattices.A1**7 + Lattices.D4).glue(zipsum(
                [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                Lattices.D4**2 + Lattices.A1**3,
                (_L := Lattices.A5 + Lattices.E6.twist(2)).glue(zipsum(
                [1, 2, 0, 1, 2, 1, 0, 2, 0, 1, 2],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
            ],
            (12, 2, 0): [Lattices.E8 + Lattices.D4, Lattices.D12],
            (12, 4, 0): [
                (_L := Lattices.E7 + Lattices.A1**5).glue(zipsum(
                [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                Lattices.D8 + Lattices.D4,
            ],
            (12, 4, 1): [
                (_L := Lattices.D8 + Lattices.A1**4).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                Lattices.E8 + Lattices.A1**4,
                Lattices.D6**2,
                Lattices.D10 + Lattices.A1**2,
                Lattices.E7 + Lattices.D4 + Lattices.A1,
            ],
            (12, 6, 0): [
                Lattices.D4**3,
                (_L := Lattices.E6 + Lattices.E6.twist(2)).glue(zipsum(
                [1, 0, 2, 0, 1, 2, 1, 0, 2, 0, 1, 2],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                (_L := Lattices.D6 + Lattices.A1**6).glue(zipsum(
                [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
            ],
            (12, 6, 1): [
                (_L := Lattices.D6 + Lattices.A1**6).glue(zipsum(
                [1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                Lattices.E7 + Lattices.A1**5,
                (_L := Lattices.D4**2 + Lattices.A1**4).glue(zipsum(
                [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                Lattices.D8 + Lattices.A1**4,
                Lattices.D6 + Lattices.D4 + Lattices.A1**2,
                (_L := Lattices.A7 + Lattices.D5.twist(2)).glue(zipsum(
                [3, 2, 1, 0, 3, 2, 1, 2, 0, 2, 1, 3],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
            ],
            (13, 3, 1): [
                Lattices.D12 + Lattices.A1,
                Lattices.E7 + Lattices.D6,
                Lattices.E8 + Lattices.D4 + Lattices.A1,
                (_L := Lattices.D10 + Lattices.A1**3).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
            ],
            (13, 5, 1): [
                Lattices.D8 + Lattices.D4 + Lattices.A1,
                Lattices.E7 + Lattices.D4 + Lattices.A1**2,
                Lattices.D6**2 + Lattices.A1,
                (_L := Lattices.E7 + Lattices.A1**6).glue(zipsum(
                [0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                (_L := Lattices.D6 + Lattices.D4 + Lattices.A1**3).glue(zipsum(
                [1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                Lattices.D10 + Lattices.A1**3,
                Lattices.E8 + Lattices.A1**5,
                (_L := Lattices.D8 + Lattices.A1**5).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                (_L := Lattices.A9 + Lattices.A4.twist(2)).glue(zipsum(
                [3, 1, 4, 2, 0, 3, 1, 4, 2, 1, 2, 3, 4],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
            ],
            (14, 2, 1): [
                (_L := Lattices.D12 + Lattices.A1**2).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                Lattices.D14,
                Lattices.E8 + Lattices.D6,
                Lattices.E7**2,
            ],
            (14, 4, 1): [
                (_L := Lattices.D6**2 + Lattices.A1**2).glue(zipsum(
                [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                Lattices.E8 + Lattices.D4 + Lattices.A1**2,
                Lattices.E7 + Lattices.D6 + Lattices.A1,
                (_L := Lattices.D10 + Lattices.A1**4).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                (_L := Lattices.D8 + Lattices.D4 + Lattices.A1**2).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                (_L := Lattices.E7 + Lattices.D4 + Lattices.A1**3).glue(zipsum(
                [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                Lattices.D12 + Lattices.A1**2,
                Lattices.D10 + Lattices.D4,
                Lattices.D8 + Lattices.D6,
                (_L := Lattices.A11 + (Lattices.A2 + Lattices.A1).twist(2)).glue(zipsum(
                [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 2, 4, 3],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
            ],
            (15, 1, 1): [
                Lattices.E8 + Lattices.E7,
                (_L := Lattices.D14 + Lattices.A1).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
            ],
            (15, 3, 1): [
                Lattices.E7**2 + Lattices.A1,
                Lattices.D8 + Lattices.E7,
                Lattices.D14 + Lattices.A1,
                Lattices.E8 + Lattices.D6 + Lattices.A1,
                (_L := Lattices.D12 + Lattices.A1**3).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                (_L := Lattices.D10 + Lattices.D4 + Lattices.A1).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                (_L := Lattices.D8 + Lattices.D6 + Lattices.A1).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                (_L := Lattices.E7 + Lattices.D6 + Lattices.A1**2).glue(zipsum(
                [0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                # AE label: A_{13} A_1(2)^
                (_L := Lattices.A13 + Lattices.A1.twist(2) + Lattices.rank_one_negative(14)).glue(zipsum(
                [8, 2, 10, 4, 12, 6, 0, 8, 2, 10, 4, 12, 6, 7, 5],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
            ],
            (16, 0, 0): [
                Lattices.E8**2,
                (_L := Lattices.D16).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
            ],
            (16, 2, 0): [
                (_L := Lattices.D8**2).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                (_L := Lattices.E7**2 + Lattices.A1**2).glue(zipsum(
                [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                Lattices.E8 + Lattices.D8,
                (_L := Lattices.D12 + Lattices.D4).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                Lattices.D16,
                (_L := Lattices.A15 + Lattices.A1.twist(2)).glue(zipsum(
                [3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 2],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
            ],
            (16, 2, 1): [
                Lattices.E8 + Lattices.E7 + Lattices.A1,
                (_L := Lattices.D8 + Lattices.E7 + Lattices.A1).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                (_L := Lattices.D10 + Lattices.D6).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                (_L := Lattices.D14 + Lattices.A1**2).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                # AE label: A_{15}^
                (_L := Lattices.A15 + Lattices.rank_one_negative(8)).glue(zipsum(
                [7, 6, 5, 4, 3, 2, 1, 0, 7, 6, 5, 4, 3, 2, 1, 3],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
            ],
            (17, 1, 1): [
                Lattices.E8**2 + Lattices.A1,
                (_L := Lattices.D16 + Lattices.A1).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                (_L := Lattices.D10 + Lattices.E7).glue(zipsum(
                [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
                (_L := Lattices.A17).glue(zipsum(
                [2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1],
                _L.module_generators(),
                _L.zero(),
            ).primitive_dual_in_discriminant_quadratic_form()),
            ],
    }


    class Involutions:
        r"""Named automorphisms of $\Lambda_{K3}$ from its direct-sum decomposition."""

        v, uu, up, ea, ep = Lattices.LK3.summands()

        I_dP = Lattices.LK3.Aut()(
            {
                v: tuple(-image for image in v.embedded_module_generators()),
                uu: up,
                up: uu,
                ea: tuple(-image for image in ea.embedded_module_generators()),
                ep: tuple(-image for image in ep.embedded_module_generators()),
            }
        )
        I_En = Lattices.LK3.Aut()(
            {
                v: tuple(-image for image in v.embedded_module_generators()),
                uu: up,
                up: uu,
                ea: ep,
                ep: ea,
            }
        )
        I_Nik = Lattices.LK3.Aut()(
            {
                v: v,
                uu: uu,
                up: up,
                ea: tuple(-image for image in ep.embedded_module_generators()),
                ep: tuple(-image for image in ea.embedded_module_generators()),
            }
        )


    class Embeddings:
        r"""Primitive embeddings
        $T_{\mathrm{Co}}\hookrightarrow T_{\mathrm{En}}
        \hookrightarrow T_{\mathrm{dP}}\hookrightarrow\Lambda_{K3}$.
        """

        c1, c2, c3 = Lattices.Tco.summands()
        e1, e2, e3 = Lattices.TEn.summands()
        d1, d2, d3, d4 = Lattices.TdP.summands()
        E8_2_into_TdP = Lattices.E8_2.Hom(Lattices.TdP)(
            tuple(
                left + right
                for left, right in zip(d3.embedded_module_generators(), d4.embedded_module_generators())
            )
        )
        TCo_into_TEn = Lattices.Tco.Hom(Lattices.TEn)(
            {
                c1: e1.embedded_module_generators()[0] + e1.embedded_module_generators()[1],
                c2: e2,
                c3: e3,
            }
        )
        TEn_into_TdP = Lattices.TEn.Hom(Lattices.TdP)(
            {
                e1: d1,
                e2: d2,
                e3: tuple(
                    left + right
                    for left, right in zip(d3.embedded_module_generators(), d4.embedded_module_generators())
                ),
            }
        )
        # $T=(L^G)^{\perp}$ for $G=\langle\iota\rangle$ acting by its inclusion.
        TEn_into_LK3 = Lattices.LK3.coinvariant_lattice(
            Involutions.I_En.cyclic_subgroup().inclusion()
        )
        TdP_into_LK3 = Lattices.LK3.coinvariant_lattice(
            Involutions.I_dP.cyclic_subgroup().inclusion()
        )
