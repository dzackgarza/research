"""Mathematical facts for the root lattices A_2 and E_8, computed through the lattice
category constructor.

Citation standard (see vault memory `What A Test Cites`): every expected value cites a
Zotero item key + the item's text/markdown extraction attachment key + the specific line
in that workstation extraction. Resolve/verify over SSH to ``$PDF_SSH_HOST`` against the
workstation Zotero API ``http://127.0.0.1:23119/api/users/0`` (the public proxy 400s by
design). Sources used here, verified on the workstation 2026-06-18:

  - Conway & Sloane, "Sphere Packings, Lattices and Groups" (1999):
      item D5P2XVRN, markdown extraction TCJKXU3D
      :4379  "The glue group is L*/L, of order det L"   (glue group = discriminant group)
      :4655  for A_n: "Glue group: cyclic C_{n+1}" and "The norm of [i] is i j/(n+1)"
      :4682  the A_2 entry: "Glue group = C_3"
    A_2 (n=2): glue group C_3 = Z/3; glue vector [1] has i=1, j=2, norm 1*2/3 = 2/3 in Q/2Z.
  - Nikulin, "Integer Symmetric Bilinear Forms and Some of Their Geometric
    Applications" (1979):
      item F3PXZC9K, markdown extraction HNJV2SEU
      :121   "U and E_8 ... the even unimodular lattices of signatures (1,1) and (0,8)"

Each test is a real mathematical computation; it passes only when the backend recovers the
cited value, and is red while the backend is incomplete. It never asserts software
properties (raises, non-None, type, source-string).
"""

from __future__ import annotations

import importlib

from sage.all import ZZ

importlib.import_module("category_specs")
Lattices = importlib.import_module("category_specs.lattices").Lattices


def _ctor():
    return Lattices(ZZ).Constructors()


class TestA2:
    """A_2 root lattice. Source: Conway-Sloane 1999, item D5P2XVRN / extraction TCJKXU3D."""

    def test_discriminant_group_is_cyclic_order_three(self) -> None:
        # TCJKXU3D:4682 "Glue group = C_3"; :4379 glue group = L*/L; :4655 norm [1]=2/3.
        D = _ctor().IntegralLattice(cartan_type="A2").discriminant_group()
        assert D.cardinality() == 3
        assert D.gens()[0].q() == ZZ(2) / ZZ(3)

    def test_is_not_unimodular(self) -> None:
        # TCJKXU3D:4682 glue group C_3 is nontrivial (det = 3), so A_2 is not unimodular.
        assert _ctor().IntegralLattice(cartan_type="A2").is_unimodular() is False

    def test_inclusion_into_dual_is_not_an_isomorphism(self) -> None:
        # TCJKXU3D:4379 the canonical L -> L* has cokernel the glue group L*/L; for A_2
        # that is C_3 (nontrivial), so the inclusion is not an isomorphism.
        L = _ctor().IntegralLattice(cartan_type="A2")
        iota = L.inclusion_morphism()
        assert iota.domain() == L
        assert iota.codomain() == L.dual_lattice()
        assert iota.is_isomorphism() is False


class TestE8:
    """E_8 root lattice. Source: Nikulin 1979, item F3PXZC9K / extraction HNJV2SEU."""

    def test_is_even_unimodular(self) -> None:
        # HNJV2SEU:121 "U and E_8 ... the even unimodular lattices of signatures (1,1), (0,8)".
        assert _ctor().IntegralLattice(cartan_type="E8").is_unimodular() is True

    def test_discriminant_group_is_trivial(self) -> None:
        # Unimodular (HNJV2SEU:121) => discriminant group L*/L is trivial
        # (TCJKXU3D:4379: glue group has order det L = 1).
        assert _ctor().IntegralLattice(cartan_type="E8").discriminant_group().cardinality() == 1

    def test_inclusion_into_dual_is_an_isomorphism(self) -> None:
        # E_8 = E_8* (unimodular, HNJV2SEU:121), so the canonical inclusion is an isomorphism.
        assert _ctor().IntegralLattice(cartan_type="E8").inclusion_morphism().is_isomorphism() is True
