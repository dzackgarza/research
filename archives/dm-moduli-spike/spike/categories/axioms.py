r"""Category axioms for structure morphisms over a base scheme.

Refinements such as ``DeligneMumfordStacks(S).Smooth().Proper()`` are theorem-backed
joins. Membership ``X in C.Proper()`` checks that ``X.declared_axioms()`` contains
``Proper`` — it does **not** recompute properness from equations or atlases.
Constructors of concrete parents are responsible for declaring only axioms that
the literature / theorem establishes for that object.
"""

from __future__ import annotations

from sage.categories.category import Category
from sage.structure.unique_representation import UniqueRepresentation

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

    _axioms: frozenset[str]

    def _with_axiom(self, name: str) -> Category:
        if name not in _AXIOM_NAMES:
            raise ValueError(f"unknown geometric axiom {name!r}")
        axioms = frozenset(self._axioms) | {name}
        return AxiomRefinement(self._base_category_for_axioms(), axioms)

    def _base_category_for_axioms(self) -> ModuliCategory:
        assert isinstance(self, ModuliCategory), f"_AxiomMixin requires ModuliCategory; found {type(self)!r}; owned boundary=_AxiomMixin._base_category_for_axioms"
        return self

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
        return frozenset(self._axioms)


class AxiomRefinement(ModuliCategory, _AxiomMixin):
    r"""Join of a geometric category with a finite set of structure-morphism axioms."""

    @staticmethod
    def __classcall_private__(cls: type, *args: object, **kwargs: object) -> AxiomRefinement:
        from .._typing_utils import as_frozenset

        assert len(args) == 2 and not kwargs, (
            f"AxiomRefinement(base_category, axioms); found args={args!r} kwargs={kwargs!r}; owned boundary=AxiomRefinement.__classcall_private__"
        )
        base_category, axioms_arg = args
        assert isinstance(base_category, ModuliCategory), f"expected ModuliCategory; found {type(base_category)!r}"
        axioms = as_frozenset(axioms_arg)
        result = UniqueRepresentation.__classcall__(cls, base_category, axioms)
        assert isinstance(result, AxiomRefinement), f"classcall must return AxiomRefinement; found {type(result)!r}"
        return result

    def __init__(self, base_category: ModuliCategory, axioms: frozenset[str]) -> None:
        self._base_category = base_category
        ModuliCategory.__init__(self, base_category.base_scheme())
        self._axioms = axioms

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
        assert hasattr(obj, "declared_axioms"), (
            f"axiom membership requires declared_axioms; found {type(obj)!r}; "
            f"object={obj!r}; owned boundary=AxiomRefinement.__contains__; "
            "declare axioms on GeometricObject (or equivalent) before membership checks"
        )
        declared = obj.declared_axioms()
        return self._axioms <= frozenset(declared)
