r"""Primitive ``(-2)`` roots in the K3 lattice and their complements.

The archived known-mathematics suite records the Nikulin complement statement
for a primitive root ``r`` in the K3 lattice: ``<r>`` has Gram ``[-2]`` and
its orthogonal complement has signature ``(3,18)``, discriminant group
``ZZ/2``, and discriminant form anti-isometric to that of ``<r>``.  This is a
different primitive-complement specimen from the positive-square polarization
cases: the signature changes on the opposite side.
"""

from dzack_research.preamble.all import Lattices


def test_primitive_k3_root_has_the_nikulin_complement_discriminant_form() -> None:
    k3 = Lattices.LK3
    e, f = tuple(k3.module_generators())[:2]
    root = k3.subobject_on((e - f,))
    complement = root.orthogonal_complement()

    assert root.is_primitive()
    assert root.gram_matrix().determinant() == -2
    assert root.signature_pair() == (0, 1)

    assert complement.module_rank() == 21
    assert complement.signature_pair() == (3, 18)
    assert complement.is_even()
    assert abs(complement.gram_matrix().determinant()) == 2
    assert tuple(complement.discriminant_group().invariants()) == (2,)
    assert complement.discriminant_group().is_anti_isometric(
        root.discriminant_group()
    )
