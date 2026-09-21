r"""Archive reconciliation for lattice embedding mors.

The archived ``EmbeddingHomsets`` category has become the canonical
``L.Emb(M)`` Mor parent.  Its elements are still form-preserving injective
lattice morphisms; there is no detached embedding wrapper around a second map.
"""

import pytest

from dzack_research.preamble.all import ZZ, Lattices


def test_embedding_mor_owns_the_actual_form_preserving_arrow() -> None:
    source = Lattices(ZZ)("A1")
    target = Lattices(ZZ)([[-2, 0], [0, -2]])
    source_root = source.basis_vector(0)
    target_root = target.basis_vector(0)
    mor = source.Emb(target)

    embedding = mor((target_root,))

    assert embedding.parent() is mor
    assert embedding.domain() is source
    assert embedding.codomain() is target
    assert embedding.is_injective()
    assert embedding(source_root) == target_root
    assert embedding(source_root).q() == source_root.q()
    assert mor(embedding) is embedding


def test_embedding_mor_rejects_a_form_preserving_but_noninjective_zero_map() -> None:
    source = Lattices(ZZ)([[0]])
    target = Lattices(ZZ)([[0, 0], [0, 0]])

    with pytest.raises(ValueError):
        source.Emb(target)((target.zero(),))
