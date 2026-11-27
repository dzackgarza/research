"""
Backend methods for lattice isometry and Nikulin invariants.

The backend first screens lattices through exact necessary conditions ordered
from cheap global invariants to more expensive local and adelic checks:
rank, signature, determinant, discriminant-group structure, discriminant-form
isomorphism, rational isometry, small-prime local isometry, and genus.
Only lattices that survive this obstruction ladder are sent to a full exact
isometry route.

Definite lattices then defer to Sage's quadratic-form equivalence. Indefinite
even two-elementary lattices use the signature plus Nikulin's ``(r, a,
delta)`` classification invariants. The remaining indefinite cases delegate to
Mathieu Dutour Sikiric's ``INDEF_FORM_TestEquivalence`` C++ binary (from
``polyhedral_common``) via subprocess, and require an exact witness matrix
before returning ``True``.

The binary lives at ``src/external/bin/INDEF_FORM_TestEquivalence`` inside
this repository.  See ``src/external/README.md`` for installation instructions.

Sources:
- Repo theory note: ``theory/foundations/reflective-two-elementary-lattices.md``, section ``Nikulin classification``
- Expository source used in the repo's notation: Alexeev--Engel--Garza--Schaffler,
  ``§9.2``
- Primary source: V. V. Nikulin, ``Integer Symmetric Bilinear Forms and Some of
  Their Geometric Applications`` (1979), Theorem ``1.14.2``
- Backend research note: ``theory/backends/indefinite-isometry.md``
- Upstream software:
  `MathieuDutSik/polyhedral_common`, ``src_indefinite/INDEF_FORM_TestEquivalence``
"""

from __future__ import annotations

from sage.all import ZZ, IntegralLattice
from src.backends.external.py_polyhedral import indefinite_form_test_equivalence


class LatticeIsometryBackend:
    def is_isometric(self, left, right):
        """
        Return the lattice isometry predicate on the routes implemented here.

        The route first applies exact early obstructions in increasing cost:
        rank, signature, determinant, rational isometry, small-prime local
        isometry at ``2, 3, 5``, discriminant-group structure,
        discriminant-form isomorphism, and genus equality. Surviving definite
        lattices defer to Sage, surviving indefinite even ``2``-elementary
        lattices use Nikulin's classification by ``(r, a, delta)``, and the
        remaining indefinite cases delegate to the Dutour `Indefinite.jl`
        witness search recorded in ``theory/backends/indefinite-isometry.md``.
        """
        assert left.base_ring() is ZZ
        assert right.base_ring() is ZZ
        left_discriminant_group = left.discriminant_group()
        right_discriminant_group = right.discriminant_group()
        match left, right:
            case _ if left.rank() != right.rank():
                return False
            case _ if left.signature_pair() != right.signature_pair():
                return False
            case _ if left.determinant() != right.determinant():
                return False
            case _ if not left_discriminant_group.isomorphic_as_groups(right_discriminant_group):
                return False
            case _ if not left_discriminant_group.is_isometric_to(right_discriminant_group):
                return False
            case _ if not left.is_rationally_isometric_to(right):
                return False
            case _ if not all(left.is_locally_isometric_to(right, p) for p in (2, 3, 5)):
                return False
            case _ if not left.is_in_same_genus_as(right):
                return False
            case _ if self._is_definite(left):
                return self._isometric_definite(left, right)
            case _ if self._supports_nikulin_classification(left) and self._supports_nikulin_classification(right):
                return self._isometric_indefinite_two_elementary(left, right)
            case _:
                return self._isometric_indefinite_general(left, right)

    def nikulin_invariants(self, lattice):
        """
        Return Nikulin's triple ``(r, a, delta)`` for the lattice.
        """
        invariants = lattice.nikulin_invariants()
        assert all(invariant in ZZ for invariant in invariants)
        return invariants

    def _supports_nikulin_classification(self, lattice):
        positive_rank, negative_rank = lattice.signature_pair()
        assert lattice.base_ring() is ZZ
        return (
            lattice.is_even() and bool(positive_rank) and bool(negative_rank) and lattice.discriminant_group().is_p_elementary(2)
        )

    def _is_definite(self, lattice):
        positive_rank, negative_rank = lattice.signature_pair()
        assert lattice.base_ring() is ZZ
        return (not positive_rank) or (not negative_rank)

    def _positive_definite_copy(self, lattice):
        positive_rank, negative_rank = lattice.signature_pair()
        assert self._is_definite(lattice)
        return lattice._sage_like() if not negative_rank else IntegralLattice(-lattice.inner_product_matrix())

    def _isometric_definite(self, left, right):
        left_positive = self._positive_definite_copy(left)
        right_positive = self._positive_definite_copy(right)
        assert self._is_definite(left_positive)
        return left_positive.quadratic_form().is_globally_equivalent_to(right_positive.quadratic_form())

    def _isometric_indefinite_two_elementary(self, left, right):
        """
        Nikulin branch for even indefinite ``2``-elementary lattices.

        Sources:
        - ``theory/foundations/reflective-two-elementary-lattices.md``, section ``Nikulin classification``
        - Alexeev--Engel--Garza--Schaffler, ``§9.2``
        - Nikulin (1979), Theorem ``1.14.2``
        """
        assert self._supports_nikulin_classification(left)
        assert self._supports_nikulin_classification(right)
        return self.nikulin_invariants(left) == self.nikulin_invariants(right)

    def _isometric_indefinite_general(self, left, right):
        """
        General indefinite branch via Dutour's ``INDEF_FORM_TestEquivalence``.

        Writes both Gram matrices to temp files, invokes the C++ binary, reads
        back the witness matrix (a Python literal), and verifies it over ``ZZ``.

        Sources:
        - ``theory/backends/indefinite-isometry.md``
        - `MathieuDutSik/polyhedral_common`, ``src_indefinite/``
        """
        cache_key = (self._gram_key(left), self._gram_key(right))
        cache = self.__dict__.setdefault("_isometry_cache", {})
        if cache_key not in cache:
            cache[cache_key] = self._compute_general_indefinite_isometry(left, right)
        return cache[cache_key]

    def _compute_general_indefinite_isometry(self, left, right):
        M1 = left.inner_product_matrix()
        M2 = right.inner_product_matrix()
        witness_data = indefinite_form_test_equivalence(M1.rows(), M2.rows())
        if witness_data is None:
            return False
        from sage.all import matrix

        n, m = left.rank(), right.rank()
        witness = matrix(ZZ, n, m, [ZZ(x) for row in witness_data for x in row])
        assert witness * M1 * witness.transpose() == M2
        return True

    def _gram_key(self, lattice):
        return tuple(tuple(str(entry) for entry in row) for row in lattice.inner_product_matrix().rows())


ISOMETRY_BACKEND = LatticeIsometryBackend()
