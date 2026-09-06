r"""sage-indefinite-port routes, run against the real package.

The port carries the ``INDEF_FORM_*`` kernels onto the owned formed-lattice
category, so it is the first provider of every indefinite-lattice capability
and polyhedral_common is the next entry in the same ordered layer.  These
tests exercise that order and the one operation the port exposes today, and
where the port is not installed they assert the stated absence and the command
that provisions it.  Nothing here substitutes another engine.
"""

from importlib.util import find_spec

import pytest

from dzack_research.preamble.all import Lattices, ZZ
from dzack_research.preamble.engine_capabilities import (
    EngineCapabilityUnavailable,
    engine_capabilities,
)

_PORT_PACKAGE = "sage_indefinite_port"
_PORT_PROVIDER = "sage-indefinite-port"
_POLYHEDRAL_PROVIDER = "polyhedral-common-via-py-polyhedral"

# The capabilities polyhedral_common also realizes.  The port is replacing it,
# so the port answers first and polyhedral_common is the layer's next entry.
_SHARED_CAPABILITIES = (
    "lattice.indefinite_automorphism_group",
    "lattice.indefinite_isometry_witness",
    "lattice.indefinite_vector_isometry_witness",
    "lattice.indefinite_orbit_representative",
    "lattice.indefinite_isotropic_subspace_orbits",
    "lattice.indefinite_isotropic_subspace_stabilizer",
    "lattice.indefinite_vector_stabilizer",
    "lattice.indefinite_isotropic_subspace_isometry_witness",
)

# The doubled hyperbolic plane U(2).  Its Gram matrix has eigenvalues 2 and -2,
# so the signature is (1, 1) with no radical; b(x, x) = 4ab is even; the signed
# discriminant is (-1)^{2.1/2} det = -(-4) = 4; and the correlation morphism
# L -> Hom(L, ZZ) has matrix [[0,2],[2,0]], whose cokernel L^vee / L is
# (ZZ/2)^2, so the invariant factors are (2, 2).
_DOUBLED_HYPERBOLIC_PLANE_GRAM = [[0, 2], [2, 0]]


def test_the_layer_offers_the_port_before_polyhedral_common() -> None:
    for capability in _SHARED_CAPABILITIES:
        assert engine_capabilities.provider_names(capability) == (
            _PORT_PROVIDER,
            _POLYHEDRAL_PROVIDER,
        ), f"{capability} does not reach the port before polyhedral_common"

    # polyhedral_common exposes the invariant only as a size_t hash inside its
    # own kernels, so the prefilter is the port's alone.
    assert engine_capabilities.provider_names(
        "lattice.indefinite_isometry_prefilter"
    ) == (_PORT_PROVIDER,)


def test_the_invariant_prefilter_of_the_doubled_hyperbolic_plane() -> None:
    lattice = Lattices(ZZ)(_DOUBLED_HYPERBOLIC_PLANE_GRAM)

    if find_spec(_PORT_PACKAGE) is None:
        with pytest.raises(EngineCapabilityUnavailable) as refusal:
            engine_capabilities.compute(
                "lattice.indefinite_isometry_prefilter",
                lattice,
            )
        absence = refusal.value.absent
        assert tuple(entry.provider for entry in absence) == (_PORT_PROVIDER,)
        assert "sage -pip install --no-deps -e" in absence[0].provisioning
        return

    prefilter = engine_capabilities.compute(
        "lattice.indefinite_isometry_prefilter",
        lattice,
    )
    assert prefilter.rank == 2
    assert prefilter.signature == (1, 1, 0)
    assert prefilter.parity == "even"
    assert prefilter.discriminant == 4
    assert prefilter.discriminant_elementary_divisors == (2, 2)
