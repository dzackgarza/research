r"""polyhedral_common routes, run against the real programs.

The ``py_polyhedral`` wrapper writes the matrix files the programs read and
resolves each program from ``PATH`` at call time.  These tests exercise that
boundary through the capability layer and through the owned orthogonal group,
and where a program is not on ``PATH`` they assert the stated absence and the
command that provisions it.  Nothing here substitutes another engine.
"""

import pytest
from py_polyhedral.binaries import binary_available

from dzack_research.preamble.all import Lattices, ZZ
from dzack_research.preamble.engine_capabilities import (
    EngineCapabilityUnavailable,
    engine_capabilities,
)

_HYPERBOLIC_PLANE_GRAM = [[0, 1], [1, 0]]

# Every polyhedral_common program the preamble reaches for, with the capability
# under which the layer offers it.  The last two are the programs upstream does
# not build; they are registered so that asking for them states that.
_ROUTES = (
    ("lattice.indefinite_automorphism_group", "INDEF_FORM_AutomorphismGroup"),
    ("lattice.indefinite_isometry_witness", "INDEF_FORM_TestEquivalence"),
    ("lattice.indefinite_vector_isometry_witness", "INDEF_FORM_TestEquivalenceVector"),
    ("lattice.indefinite_orbit_representative", "INDEF_FORM_GetOrbitRepresentative"),
    ("lattice.indefinite_isotropic_subspace_orbits", "INDEF_FORM_GetOrbit_IsotropicKplane"),
    (
        "lattice.indefinite_isotropic_subspace_stabilizer",
        "INDEF_FORM_StabilizerIsotropicPlane",
    ),
    ("lattice.indefinite_vector_stabilizer", "INDEF_FORM_StabilizerVector"),
    (
        "lattice.indefinite_isotropic_subspace_isometry_witness",
        "INDEF_FORM_TestEquivalenceIsotropicKplane",
    ),
)


def test_every_polyhedral_operation_is_offered_by_the_capability_layer() -> None:
    for capability, _binary in _ROUTES:
        assert "polyhedral-common-via-py-polyhedral" in engine_capabilities.provider_names(
            capability
        ), f"{capability} is not offered by the ordered capability layer"


def test_an_unbuilt_program_refuses_with_the_reason_it_cannot_be_provisioned() -> None:
    # INDEF_FORM_StabilizerVector is named by the wrapper but has no driver in
    # polyhedral_common's src_indefinite, so no build makes it available.  The
    # refusal has to say that rather than advise an impossible install, and it
    # carries the port's absence too, since the port is the first provider.
    assert not binary_available("INDEF_FORM_StabilizerVector")

    with pytest.raises(EngineCapabilityUnavailable) as refusal:
        engine_capabilities.compute(
            "lattice.indefinite_vector_stabilizer",
            _HYPERBOLIC_PLANE_GRAM,
            [1, 0],
        )

    absence = refusal.value.absent
    assert tuple(entry.provider for entry in absence) == (
        "sage-indefinite-port",
        "polyhedral-common-via-py-polyhedral",
    )
    assert "port of INDEF_FORM_StabilizerVector" in absence[0].provisioning
    assert "builds no program of this name" in absence[1].provisioning


def test_isometry_witnesses_of_the_hyperbolic_plane() -> None:
    # b(x,y) = x1 y2 + x2 y1 on U.  Pulling U back along diag(1,-1) gives
    # [[0,-1],[-1,0]], so the two are isometric.  The determinant of the Gram
    # matrix is an isometry invariant, and det(U) = -1 while det(U(2)) = -4,
    # so U and U(2) are not.  The wrapper returns the witness rows when the
    # forms are equivalent and None when they are not.
    if not binary_available("INDEF_FORM_TestEquivalence"):
        with pytest.raises(EngineCapabilityUnavailable) as refusal:
            engine_capabilities.compute(
                "lattice.indefinite_isometry_witness",
                _HYPERBOLIC_PLANE_GRAM,
                _HYPERBOLIC_PLANE_GRAM,
            )
        # The port is the first provider, so polyhedral_common's remedy is second.
        assert "make -C src_indefinite" in refusal.value.absent[1].provisioning
        return

    witness = engine_capabilities.compute(
        "lattice.indefinite_isometry_witness",
        _HYPERBOLIC_PLANE_GRAM,
        [[0, -1], [-1, 0]],
    )
    assert witness is not None

    assert (
        engine_capabilities.compute(
            "lattice.indefinite_isometry_witness",
            _HYPERBOLIC_PLANE_GRAM,
            [[0, 2], [2, 0]],
        )
        is None
    )


def test_the_owned_orthogonal_group_of_the_hyperbolic_plane() -> None:
    # Solving M^t G M = G over ZZ for G = [[0,1],[1,0]]: the equations are
    # ac = bd = 0 and ad + bc = 1, whose only integral solutions are ±1 and
    # ±(the swap of e and f).  So O(U) is the Klein four-group, which no
    # single element generates.
    lattice = Lattices(ZZ)("U")
    e, f = lattice.module_generators()

    if not binary_available("INDEF_FORM_AutomorphismGroup"):
        with pytest.raises(EngineCapabilityUnavailable) as refusal:
            engine_capabilities.compute(
                "lattice.indefinite_automorphism_group",
                _HYPERBOLIC_PLANE_GRAM,
            )
        # The port is the first provider, so polyhedral_common's remedy is second.
        assert "make -C src_indefinite" in refusal.value.absent[1].provisioning
        return

    generators = lattice.O().group_generators()
    assert generators.cardinality() >= 2

    images = [(generator(e), generator(f)) for generator in generators]
    orthogonal_group = [(e, f), (-e, -f), (f, e), (-f, -e)]
    for image in images:
        assert image in orthogonal_group
    assert any(image in ((f, e), (-f, -e)) for image in images)
