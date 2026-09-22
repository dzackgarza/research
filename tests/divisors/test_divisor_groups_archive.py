r"""Archive reconciliation for the five divisor-group role categories."""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    AffineSpaces,
    CartierDivisorGroups,
    Cat,
    ClassGroups,
    DivisorGroups,
    FormalDivisorGroups,
    PicardGroups,
    Set,
    WeilDivisorGroups,
)

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/categories/divisors/divisor_groups.sage",
        "live_owner": "src/dzack_research/preamble/categories/divisors/divisor_groups.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/categories/divisors/cartier_divisor_groups.sage",
        "live_owner": "src/dzack_research/preamble/categories/divisors/cartier_divisor_groups.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/categories/divisors/weil_divisor_groups.sage",
        "live_owner": "src/dzack_research/preamble/categories/divisors/divisor_groups.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/categories/divisors/picard_groups.sage",
        "live_owner": "src/dzack_research/preamble/categories/divisors/divisor_groups.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/categories/divisors/class_groups.sage",
        "live_owner": "src/dzack_research/preamble/categories/divisors/divisor_groups.py",
        "disposition": "reconciled-live-owner",
    },
)


def test_divisor_roles_preserve_the_archived_module_distinctions() -> None:
    primes = Set(("D0", "D1"))
    free = ZZ.free_module(primes)

    divisors = DivisorGroups()(free)
    weil = WeilDivisorGroups()(free)
    line = AffineSpaces(QQ)(1)
    cartier = CartierDivisorGroups().of_scheme(line)
    picard = PicardGroups()(free)
    classes = ClassGroups()(free)

    assert divisors in DivisorGroups()
    assert weil in WeilDivisorGroups()
    assert weil in DivisorGroups()
    assert cartier in CartierDivisorGroups()
    assert picard in PicardGroups()
    assert classes in ClassGroups()
    for category in (
        DivisorGroups(),
        WeilDivisorGroups(),
        CartierDivisorGroups(),
        PicardGroups(),
        ClassGroups(),
    ):
        assert category in Cat()
        assert category.category() is Cat()
    assert divisors.module_generating_set() == free.module_generating_set()
    assert weil.module_generating_set() == free.module_generating_set()
    assert cartier.divisor_scheme() is line
    assert cartier.quotient_sheaf() is line.cartier_divisor_sheaf()
    assert picard.module_generating_set() == free.module_generating_set()
    assert classes.module_generating_set() == free.module_generating_set()


def test_formal_divisor_keeps_support_and_combines_repeated_terms() -> None:
    divisor = FormalDivisorGroups(ZZ).from_terms(
        ((ZZ(2), "D0"), (ZZ(-1), "D1"), (ZZ(3), "D0")),
    )
    group = divisor.parent()

    assert group in FormalDivisorGroups(ZZ)
    assert tuple(group.components(divisor)) == ("D0", "D1")
    terms = tuple(group.terms(divisor).items())
    assert terms == (("D0", ZZ(5)), ("D1", ZZ(-1)))
    assert group.divisor_repr(divisor) == "5*D0 - 1*D1"
