r"""Category axioms for structure morphisms over a base scheme.

Refinements such as ``DeligneMumfordStacks(S).Smooth().Proper()`` are theorem-backed
joins: constructors of concrete parents declare membership; there is no equation-level
decision procedure for properness.
"""

from __future__ import annotations

from sage.categories.category import Category

from .foundation import ModuliCategory


_AXIOM_NAMES = (
    "FiniteType",
    "Separated",
    "Proper",
    "Smooth",
    "Projective",
    "Normal",
    "Reduced",
    "Integral",
    "Connected",
    "Nodal",
)


class _AxiomMixin:
    r"""Mixin providing geometric axiom refinements on :class:`ModuliCategory`."""

    def _with_axiom(self, name: str) -> Category:
        if name not in _AXIOM_NAMES:
            raise ValueError(f"unknown geometric axiom {name!r}")
        axioms = frozenset(getattr(self, "_axioms", ())) | {name}
        return AxiomRefinement(self._base_category_for_axioms(), axioms)

    def _base_category_for_axioms(self) -> ModuliCategory:
        return self  # type: ignore[return-value]

    def FiniteType(self) -> Category:
        return self._with_axiom("FiniteType")

    def Separated(self) -> Category:
        return self._with_axiom("Separated")

    def Proper(self) -> Category:
        return self._with_axiom("Proper")

    def Smooth(self) -> Category:
        return self._with_axiom("Smooth")

    def Projective(self) -> Category:
        return self._with_axiom("Projective")

    def Normal(self) -> Category:
        return self._with_axiom("Normal")

    def Reduced(self) -> Category:
        return self._with_axiom("Reduced")

    def Integral(self) -> Category:
        return self._with_axiom("Integral")

    def Connected(self) -> Category:
        return self._with_axiom("Connected")

    def Nodal(self) -> Category:
        return self._with_axiom("Nodal")

    def axioms(self) -> frozenset[str]:
        return frozenset(getattr(self, "_axioms", ()))


class AxiomRefinement(ModuliCategory, _AxiomMixin):
    r"""Join of a geometric category with a finite set of structure-morphism axioms."""

    @staticmethod
    def __classcall_private__(cls, base_category: ModuliCategory, axioms: frozenset[str] | set[str]) -> AxiomRefinement:
        axioms = frozenset(axioms)
        return super().__classcall__(cls, base_category, axioms)

    def __init__(self, base_category: ModuliCategory, axioms: frozenset[str]) -> None:
        self._base_category = base_category
        self._axioms = axioms
        ModuliCategory.__init__(self, base_category.base_scheme())

    def _base_category_for_axioms(self) -> ModuliCategory:
        return self._base_category

    def super_categories(self) -> list[Category]:
        return [self._base_category]

    def _repr_object_names(self) -> str:
        base = self._base_category._repr_object_names()
        ax = ".".join(sorted(self._axioms))
        return f"{base} with axioms {ax}"

    def __contains__(self, obj: object) -> bool:
        if obj not in self._base_category:
            return False
        declared = getattr(obj, "declared_axioms", lambda: frozenset())()
        return self._axioms <= frozenset(declared)
