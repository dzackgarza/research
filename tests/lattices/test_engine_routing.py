r"""The lattice morphism layer reaches polyhedral_common through the capability layer.

Every indefinite route in :mod:`lattice_morphisms` asks the capability layer
for its operation, so an unprovisioned program arrives as a stated absence
naming the capability and its remedy, never as an import or file error raised
by the wrapper.  ``INDEF_FORM_StabilizerVector`` is the sharpest specimen:
the routine exists in ``CombinedAlgorithms.h`` but polyhedral_common compiles
no driver of that name, so its absence is permanent and the refusal a caller
meets is always the layer's.
"""

import pytest

from dzack_research.preamble.all import ZZ, Lattices
from dzack_research.preamble.engine_capabilities import (
    EngineCapabilityUnavailable,
    engine_capabilities,
)

_CAPABILITY = "lattice.indefinite_vector_stabilizer"
_POLYHEDRAL_PROVIDER = "polyhedral-common-via-py-polyhedral"


def test_the_indefinite_vector_stabilizer_states_its_absence_through_the_layer() -> None:
    assert _POLYHEDRAL_PROVIDER in engine_capabilities.provider_names(_CAPABILITY)

    plane = Lattices(ZZ)("U")
    assert not plane.is_definite()

    with pytest.raises(EngineCapabilityUnavailable) as refusal:
        plane.O().vector_stabilizer_generators(plane.module_generator(0))

    assert refusal.value.capability == _CAPABILITY
    assert _POLYHEDRAL_PROVIDER in tuple(
        absence.provider for absence in refusal.value.absent
    )
