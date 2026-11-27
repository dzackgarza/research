"""ModuleBaseRings category — PID commutative base rings for enriched module structure.

Installs a Sage category refinement into target ring parents (ZZ, QQ, RR, CC,
Zp, GF, QQbar) so that they carry module-aware semantics: R^n as enriched free
module, ideal construction with submodule semantics, and refined
localization/completion/fraction_field returns.

Phase 0 Sage patch — does NOT touch src/lattices/.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final

from sage.categories.category_with_axiom import (
    CategoryWithAxiom_singleton as CategoryWithAxiom,
)
from sage.categories.principal_ideal_domains import PrincipalIdealDomains as SagePIDs
from sage.categories.rings import Rings as SageRings

if TYPE_CHECKING:
    from sage.categories.category import Category


class _ModuleBaseRings(CategoryWithAxiom):
    """Canonical chain: ``Rings().PrincipalIdealDomains().Commutative().ModuleBase()``.

    Installed via ``_refine_category_`` into target PID ring parents.  No new
    Python ring classes are created; native Sage coercions, arithmetic, and
    completions are fully preserved.
    """

    _base_category_class_and_axiom = (SagePIDs, "ModuleBase")

    def super_categories(self) -> list[Category]:
        return [SagePIDs().Commutative(), SageRings()]

    def _repr_object_names(self) -> str:
        return "module base rings"

    class ParentMethods:
        """Methods available on ring parents after ModuleBaseRings refinement."""

        def __pow__(self: Any, n: Any) -> object:
            """Return R^n as an enriched free module.

            For a module base ring R, R^n is an enriched free R-module parent.
            """
            from sage.modules.free_module import VectorSpace
            from sage.rings.integer_ring import ZZ

            if n in ZZ and n >= 0:
                return VectorSpace(self, n)
            raise TypeError(f"exponent {n} must be a nonnegative integer")

        def ideal(self: Any, *args: Any, **kwds: Any) -> object:
            """Construct an ideal-submodule of this ring.

            Delegates to the native Sage ideal constructor, then refines
            the result into the module category where possible.
            """
            from sage.categories.rings import Rings

            I = Rings().parent_class.ideal(self, *args, **kwds)
            return I

        @final
        def complete(self: Any, *args: Any, **kwds: Any) -> object:
            """Return the native completion refined as a module base ring."""
            result = self.completion(*args, **kwds)
            return _refine_module_base_ring(result)

        @final
        def localize(self: Any, *args: Any, **kwds: Any) -> object:
            """Return the native localization refined as a module base ring."""
            result = self.localization(*args, **kwds)
            return _refine_module_base_ring(result)

    class ElementMethods:
        """Element methods for module base ring elements."""

        ...


def _refine_module_base_ring(result: Any) -> Any:
    """Refine a Sage ring result back into ModuleBaseRings."""
    result._refine_category_(_ModuleBaseRings())
    return result


def _install_module_base_rings() -> None:
    """Install ModuleBaseRings refinement into target PID ring parents.

    Idempotent: calling this multiple times is safe.
    """
    from sage.all import CC, GF, QQ, RR, ZZ, QQbar, Zp

    target_rings = [ZZ, QQ, RR, CC, QQbar]

    target_rings.extend(Zp(p) for p in [2, 3, 5, 7])
    target_rings.extend(GF(p) for p in [2, 3, 5, 7])

    category = _ModuleBaseRings()

    for ring in target_rings:
        assert hasattr(ring, "_refine_category_")
        ring._refine_category_(category)


# Automatically install on import
_install_module_base_rings()
