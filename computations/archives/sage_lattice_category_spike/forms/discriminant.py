r"""HELD remainder: the spike's genus surface (W2 absorption round, 2026-08-19).

Everything else in this module -- the discriminant element/subgroup/action
classes, the closure helpers, the ``TorsionQuadraticForm`` factory -- was
dispositioned in the W2 absorption round: preamble-stands entries retired,
spike-lands entries re-expressed on the preamble's torsionform categories.

The genus surface below is deliberately NOT absorbed and NOT deleted:
FOUNDATIONS Part VI is silent on the genus (and its Status-and-scope list
retracts one genus position without ratifying a replacement), while project
memory holds the adelic frame (genus equality = adelic isometry, local
invariants as methods on the completed lattices ``L (x) ZZ_p``), which this
(signature, discriminant-form) parameterization does not implement.  It waits
on the user's ruling about the genus home; its input type (the retired
synthetic discriminant form) is gone, so it is reference material, not
runnable code.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from sage.rings.integer_ring import ZZ
from sage.structure.parent import Parent

from ..lexicon import Genus

if TYPE_CHECKING:
    from ..lexicon import (
        DiscriminantForm,
        DiscriminantSubgroup,
        Integer,
        Lattice,
        Rational,
        SageGenus,
        SageLocalGenusSymbol,
        SignaturePair,
    )


class SyntheticGenus(Genus, Parent):
    r"""The genus of a nondegenerate integral lattice, as a category-backed parent:
    the finite set of isometry classes sharing this signature and discriminant form
    (Nikulin 1.10.1). Its cardinality is the class number; iterating yields one
    representative lattice per class. Parity is the ``Even`` axiom, acquired as
    output from the discriminant form."""

    def __init__(self, discriminant_group: DiscriminantSubgroup, signature_pair: SignaturePair) -> None:
        from ..objects.categories import Genera

        self._discriminant_group = discriminant_group
        self._signature_pair = (ZZ(signature_pair[0]), ZZ(signature_pair[1]))
        # Parity is a property of the discriminant form (output), never an input:
        # an even genus has a discriminant quadratic form of value modulus 2.
        self._even = bool(discriminant_group._quadratic_modulus() == 2)
        category = Genera(ZZ).Even() if self._even else Genera(ZZ)
        Parent.__init__(self, base=ZZ, category=category)

    # cardinality/__iter__ are the class-number/representatives rollup on
    # the Genus base (CP3 routing) — no leaf spellings here.

    def discriminant_form(self) -> DiscriminantForm:
        return self._discriminant_group

    def signature_pair(self) -> tuple[Any, Any]:
        return self._signature_pair

    def signature(self) -> SignaturePair:
        return self._signature_pair[0] - self._signature_pair[1]

    def is_even(self) -> bool:
        return self._even

    def brown_invariant(self) -> Integer:
        return self.discriminant_form().brown_invariant()

    def _sage_engine(self) -> SageGenus:
        r"""Ephemeral Sage genus symbol built from this genus's own data
        (discriminant-form Gram + signature) through the torsion-module constructor."""
        from sage.modules.torsion_quadratic_module import TorsionQuadraticForm

        form = self.discriminant_form()
        sage_form = TorsionQuadraticForm(form.gram_matrix_quadratic())
        assert sage_form.cardinality() == form.cardinality(), (
            "the ephemeral Sage TorsionQuadraticModule must carry the whole discriminant group to "
            "present the genus; "
            f"synthetic cardinality={form.cardinality()}, Sage cardinality={sage_form.cardinality()}"
        )
        return sage_form.genus(self.signature_pair())

    def det(self) -> Rational:
        return ZZ(self._sage_engine().determinant())

    def dim(self) -> Integer:
        return ZZ(self._sage_engine().dimension())

    def representative(self) -> Lattice:
        r"""A lattice in this genus: Sage's genus machinery returns an integer
        Gram matrix, converted into an owned synthetic lattice."""
        from ..objects.categories import Lattices

        return Lattices(ZZ).from_gram_matrix(self._sage_engine().representative(), label="genus_representative")

    def representatives(self) -> tuple[Any, ...]:
        r"""One lattice per isometry class in this genus, from Sage's genus
        enumeration (computed exactly where Sage's engines compute it)."""
        from ..objects.categories import Lattices

        return tuple(Lattices(ZZ).from_gram_matrix(gram, label=f"genus_class_{index}") for index, gram in enumerate(self._sage_engine().representatives()))

    def class_number(self) -> Integer:
        r"""``h(genus)`` = the number of isometry classes, counted from the
        enumerated representatives."""
        return ZZ(len(self._sage_engine().representatives()))

    def is_unique_class(self) -> bool:
        r"""Whether the genus contains a single isometry class (the regime
        where genus equality decides isometry)."""
        return bool(self.class_number() == 1)

    def local_symbol(self, p: Integer) -> SageLocalGenusSymbol:
        r"""The p-adic symbol at ``p`` (spec 3.5): the
        returned object is Sage's local genus symbol."""
        return self._sage_engine().local_symbol(ZZ(p))

    def local_symbols(self) -> tuple[Any, ...]:
        r"""All local symbols from Sage's genus machinery (spec 3.5)."""
        return tuple(self._sage_engine().local_symbols())

    # ---- per-prime symbol extraction (gap-ledger G2, round-2 ruling) --------
    # Convenience access over Genus_Symbol_p_adic_ring, sufficient to state
    # Nikulin-type local conditions per prime: the Conway-Sloane Jordan-
    # constituent tuples, and the local determinant/rank/excess/level data.
    # At p = 2 the constituent tuples carry five entries
    # [scale-valuation, rank, det-class, type II/I, oddity] — the p = 2
    # complication Nik80 section 1.8 tracks; at odd p they carry three.

    def local_symbol_tuples(self, p: Integer) -> tuple[tuple[Any, ...], ...]:
        r"""The CANONICAL Conway-Sloane symbol tuples of the Jordan
        constituents at ``p`` (Sage's ``canonical_symbol``), as a tuple of
        integer tuples. Canonical, not raw: the raw 2-adic constituent data is
        presentation-dependent (equal genera can print different det classes
        and oddities pre-canonicalization), so only the canonical form is
        usable per-prime data."""
        return tuple(tuple(ZZ(entry) for entry in constituent) for constituent in self.local_symbol(p).canonical_symbol())

    def local_determinant(self, p: Integer) -> Rational:
        r"""Determinant datum of the ``p``-adic symbol (Sage's local ``determinant``)."""
        return ZZ(self.local_symbol(p).determinant())

    def local_rank(self, p: Integer) -> Integer:
        r"""Dimension of the ``p``-adic symbol."""
        return ZZ(self.local_symbol(p).dimension())

    def local_excess(self, p: Integer) -> Integer:
        r"""The p-excess (Conway-Sloane Ch. 15 section 7.5; at ``p = 2`` this is
        the oddity), from Sage's local symbol."""
        return self.local_symbol(p).excess()

    def local_level(self, p: Integer) -> Rational:
        r"""Level of the ``p``-adic symbol."""
        return ZZ(self.local_symbol(p).level())

    def is_locally_even(self, p: Integer) -> bool:
        r"""Whether the ``p``-adic symbol is of even type (Sage ``is_even``)."""
        return bool(self.local_symbol(p).is_even())

    def __eq__(self, other: object) -> bool:
        # spec section 5: genus equality IS local-symbol equality (computed by
        # Sage: genus symbols compare by signature + local symbols)
        if not isinstance(other, SyntheticGenus):
            return False
        if self.signature_pair() != other.signature_pair() or self.is_even() != other.is_even():
            return False
        return bool(self._sage_engine() == other._sage_engine())

    def __ne__(self, other: object) -> bool:
        # Coherent inequality: on Sage Element subclasses a Python-level
        # __eq__ shadows only ==, while != would fall through to cython
        # richcmp (id-based or coercion) and disagree or raise (#226).
        return not self == other

    def __hash__(self) -> int:
        # Consistent with __eq__: a genus is fixed by its signature, parity, and
        # discriminant form (Nikulin 1.10.1), so equal genera share these.
        return hash((self._signature_pair, self._even, tuple(self.discriminant_form().invariants())))

    def __repr__(self) -> str:
        return f"Synthetic genus with signature {self.signature_pair()} and discriminant invariants {self.discriminant_form().invariants()}"
