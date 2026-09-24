r"""Archive reconciliation for the K3 lattice's even-unimodular model.

The archived source cites the classification of indefinite even unimodular
lattices: the K3 lattice has signature ``(3,19)`` and is represented by
``U^3 + E8(-1)^2`` in the repository's sign convention.  The test below uses
a genuinely regrouped orthogonal sum, so the final assertion is an isometry
statement and not construction identity.
"""

from dzack_research.preamble.all import *


def test_k3_lattice_is_the_even_unimodular_signature_3_19_model() -> None:
    k3 = Lattices.LK3
    signature = k3.signature_pair()

    assert k3.module_rank() == 22
    assert signature.first() == 3
    assert signature.second() == 19
    assert k3.is_even()
    assert k3.is_unimodular()

    regrouped = (Lattices.U + Lattices.E8) + (Lattices.U + Lattices.E8) + Lattices.U
    assert regrouped is not k3
    assert regrouped.is_isometric(k3) is True
