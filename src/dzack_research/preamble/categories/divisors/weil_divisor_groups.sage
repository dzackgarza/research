r"""Weil divisor groups."""

from sage.categories.category import Category


def WeilDivisorGroup(module: "Module") -> "Module":
    r"""Refine the free module on the actual codimension-one subvarieties."""
    assert module in FramedFreeModules(ZZ), (
        "WeilDiv(X) is free on its specified set of prime divisors"
    )
    return refine(module, WeilDivisorGroups())


class WeilDivisorGroups(Category):
    r"""Free abelian groups on codimension-one subvarieties."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "Weil divisor groups"

    def super_categories(self) -> list:
        return [DivisorGroups()]
