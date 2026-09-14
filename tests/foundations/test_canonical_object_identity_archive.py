r"""Archive reconciliation for canonical identity of finite enumerations.

The historical implementation identified an arbitrary ordered enumeration with
the finite ordinal carrying the same displayed values.  The live owner keeps a
labelled set distinct from its counting ordinal, but the canonical-object
invariant survives where it mathematically belongs: every finite enumeration
of the same cardinality reaches one interned ordinal.
"""

from dzack_research.preamble.all import Sets
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.set_categories import (
    counting_ordinal,
    finite_ordinal_set,
)


def test_three_point_counting_ordinal_is_one_canonical_object() -> None:
    letters = finite_ordered_set(("a", "b", "c"))
    primes = finite_ordered_set((2, 3, 5))
    ordinal = Sets.Δ[2]

    assert finite_ordinal_set(3) is ordinal
    assert counting_ordinal(letters) is ordinal
    assert counting_ordinal(primes) is ordinal
