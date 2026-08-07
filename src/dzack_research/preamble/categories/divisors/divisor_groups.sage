r"""Divisor groups as framed free \(\mathbb Z\)-modules."""

from sage.categories.category import Category


def DivisorGroup(module: "Module") -> "Module":
    r"""Refine the declared free module of divisors."""
    assert module in FramedFreeModules(ZZ), (
        "a divisor group is constructed from its actual set of prime divisors"
    )
    return refine(module, DivisorGroups())


class DivisorGroups(Category):
    r"""Free abelian groups on specified prime divisors."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "divisor groups"

    def super_categories(self) -> list:
        return [FramedFreeModules(ZZ)]
