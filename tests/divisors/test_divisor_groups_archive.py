r"""Archive reconciliation for the five divisor-group role categories."""

from dzack_research.preamble.all import (
    Cat,
    ZZ,
    CartierDivisorGroup,
    CartierDivisorGroups,
    ClassGroup,
    ClassGroups,
    DivisorGroup,
    DivisorGroups,
    FormalDivisor,
    FormalDivisorGroups,
    FreeModuleOn,
    PicardGroup,
    PicardGroups,
    Set,
    WeilDivisorGroup,
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
        "live_owner": "src/dzack_research/preamble/categories/divisors/divisor_groups.py",
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
    free = FreeModuleOn(ZZ, primes)

    divisors = DivisorGroup(free)
    weil = WeilDivisorGroup(free)
    cartier = CartierDivisorGroup(free)
    picard = PicardGroup(free)
    classes = ClassGroup(free)

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
    assert cartier.module_generating_set() == free.module_generating_set()
    assert picard.module_generating_set() == free.module_generating_set()
    assert classes.module_generating_set() == free.module_generating_set()


def test_formal_divisor_keeps_support_and_combines_repeated_terms() -> None:
    divisor = FormalDivisor(
        ZZ,
        ((ZZ(2), "D0"), (ZZ(-1), "D1"), (ZZ(3), "D0")),
    )
    group = divisor.parent()

    assert group in FormalDivisorGroups(ZZ)
    assert group.components(divisor) == ("D0", "D1")
    terms = tuple(group.terms(divisor))
    assert terms == ((ZZ(5), "D0"), (ZZ(-1), "D1"))
    assert group.divisor_repr(divisor) == "5*D0 - 1*D1"
