r"""Exercise declared vocabulary that had no caller anywhere in the corpus:
each method below is public DSL surface whose only prior witness was its
definition. Every assertion is a real mathematical fact, not a smoke call.

- ``O(A2) -> O(q_{A2})``: A_{A2} = Z/3 with q = 2/3, so O(q) = {±1} has order
  2, the representation is onto, and the stable kernel O(A2)# = ker has index
  2 in the order-12 group O(A2) = W(A2) × {±1}.
- ``H^perp`` for the trivial isotropic subgroup is the whole group.
- A2's genus contains a single isometry class (unique in its genus).
"""
from __future__ import annotations

from sage.all import ZZ

from sage_lattice_category_spike.lattice_categories import Lattice


def test_discriminant_representation_and_stable_kernel_split_O_A2():
    O = Lattice("A2").isometry_group()
    representation = O.discriminant_representation()
    kernel = O.stable_kernel()
    assert O.order() == 12
    assert representation.order() == 2
    assert kernel.order() == 6
    # first isomorphism theorem, numerically: |O| = |image| * |kernel|
    assert representation.order() * kernel.order() == O.order()


def test_orthogonal_submodule_of_trivial_isotropic_subgroup_is_everything():
    discriminant = Lattice("A2").discriminant_group()
    (trivial_subgroup,) = discriminant.isotropic_subgroups()
    assert trivial_subgroup.invariants() == ()
    assert trivial_subgroup.orthogonal_submodule().invariants() == discriminant.invariants() == (3,)


def test_A2_is_unique_in_its_genus():
    assert Lattice("A2").genus().is_unique_class()
