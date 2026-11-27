"""Ring and ideal categories used by the module redesign.

``ModuleBaseRings`` is a refinement category sitting below Sage's
``Rings().PrincipalIdealDomains().Commutative()``.  Ring parents opt in by
having their category refined (``R._refine_category_(ModuleBaseRings())``);
``Modules(R)`` performs this lazily and ``refinement.install()`` seeds the
common base rings eagerly and wraps constructors so freshly-minted rings are
also refined.

Ideals of a refined ring are the same Sage ideal parents as before, additionally
refined into ``ModuleBaseIdeals(R)`` and ``Modules(R).RIdeals()``.  Per the
design axiom *ideals simply ARE R-submodules of R*, ``Modules(R).RIdeals()`` is
the canonical category of ideals of R; ``ModuleBaseIdeals`` is a thin
Sage-interop bridge.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, final

from sage.categories.category import Category
from sage.categories.category_singleton import Category_singleton
from sage.categories.category_types import Category_ideal
from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.principal_ideal_domains import PrincipalIdealDomains
from sage.misc.abstract_method import abstract_method
from sage.rings.integer import Integer

from .sage_modules import Modules

if TYPE_CHECKING:
    from .types import (
        CompleteRing,
        FreeModule,
        Ideal,
        LocalRing,
        Ring,
        RingElement,
        RModule,
    )

Names = str | tuple[str, ...] | None


class ModuleBaseIdeals(Category_ideal):
    r"""
    Sage-interop bridge category for ideals of a refined module base ring.

    The canonical categorical home for ideals of ``R`` is
    ``Modules(R).RIdeals()`` (per the axiom *ideals ARE R-submodules of R*).
    ``ModuleBaseIdeals(R)`` is an additional refinement layer attached to the
    existing ``Ideal_generic`` / ``Ideal_pid`` parents so Sage's ``Ideals(R)``
    hierarchy continues to work unchanged.
    """

    def super_categories(self) -> list[Category]:
        from sage.categories.commutative_ring_ideals import CommutativeRingIdeals
        R = self.ring()
        return [CommutativeRingIdeals(R), Modules(R).RIdeals()]

    @classmethod
    def from_ideal(cls, sage_ideal) -> Ideal:
        r"""Return ``sage_ideal``, after a best-effort category refinement.

        Sage ideals are ``MonoidElement`` instances with a hardcoded
        ``.category()`` returning ``Ideals(R)``; ``_refine_category_`` is
        only available on ``Parent`` objects.  If the refinement path is
        available (on a future ``Parent``-backed ideal), it is applied;
        otherwise this is a no-op and the ideal is returned unchanged.
        """
        refine = getattr(sage_ideal, "_refine_category_", None)
        if refine is not None:
            R = sage_ideal.ring()
            try:
                refine([cls(R), Modules(R).RIdeals()])
            except Exception:
                pass
        return sage_ideal

    def _repr_object_names(self) -> str:
        return "module-base ideals"

    class ParentMethods:
        @final
        def ideal(self):
            r"""Return the underlying Sage ideal (self)."""
            return self

    class ElementMethods:
        pass

    class MorphismMethods:
        pass


class ModuleBaseRings(Category_singleton):
    r"""
    Subcategory of ``Rings().PrincipalIdealDomains().Commutative()`` whose
    ring parents produce objects in the redesigned module surface.

    Existing ring parents join this category via
    ``ring._refine_category_(ModuleBaseRings())``.  The ``ParentMethods``
    overrides below are *trivial glue*: each calls ``super().method(...)`` and
    then refines the returned parent into the appropriate module/ring
    subcategory.  Anything non-trivial is ``@abstract_method`` so the
    implementation backlog is enumerated precisely.
    """

    @final
    def super_categories(self) -> list[Category]:
        return [PrincipalIdealDomains()]

    @final
    def additional_structure(self):
        return None

    @final
    def _repr_object_names(self) -> str:
        return "commutative PID base rings for finitely presented modules"

    # ------------------------------------------------------------------
    # Subcategories
    # ------------------------------------------------------------------

    class Local(CategoryWithAxiom):
        r"""Local rings in the module surface (e.g. ``Zp(p)``)."""

        @final
        def super_categories(self) -> list[Category]:
            from sage.categories.local_rings import LocalRings as SageLocalRings
            return [ModuleBaseRings(), SageLocalRings()]

        @final
        def _repr_object_names(self) -> str:
            return "local rings for finitely presented modules"

        class ParentMethods:
            @abstract_method
            def maximal_ideal(self) -> Ideal: ...

        class ElementMethods:
            pass

        class MorphismMethods:
            pass

    class Complete(CategoryWithAxiom):
        r"""Complete rings in the module surface (e.g. ``Zp(p)``)."""

        @final
        def super_categories(self) -> list[Category]:
            # No intersection with Sage's CompleteDiscreteValuationRings is
            # declared here; ``_refine_category_`` on a specific ``Zp(p)``
            # parent pulls the DVR hierarchy in via the join.
            return [ModuleBaseRings()]

        @final
        def _repr_object_names(self) -> str:
            return "complete rings for finitely presented modules"

        class ParentMethods:
            pass

        class ElementMethods:
            pass

        class MorphismMethods:
            pass

    # Field() is inherited from Rings().PrincipalIdealDomains().Commutative()
    # via the axiom system.  No explicit subcategory needed here.

    # ------------------------------------------------------------------
    # ParentMethods — concrete super+refine glue.
    # ------------------------------------------------------------------

    class ParentMethods:
        # Super+refine glue.  Python's built-in ``super()`` does not work in
        # category ``ParentMethods`` because Sage injects these methods into a
        # dynamically-generated ``parent_class`` that is not in the defining
        # MRO.  We therefore delegate by explicit reference to the canonical
        # ``sage.categories.rings.Rings.ParentMethods`` functions.

        # @override Rings.ParentMethods.ideal
        def ideal(self, *args, **kwds) -> Ideal:
            r"""Delegate to Sage, then refine into ``ModuleBaseIdeals`` and
            ``Modules(R).RIdeals()``.
            """
            from sage.categories.rings import Rings as _Rings
            result = _Rings.ParentMethods.ideal(self, *args, **kwds)
            return ModuleBaseIdeals.from_ideal(result)

        # @override Rings.ParentMethods.__mul__
        def __mul__(self, generator: RingElement) -> Ideal:
            r"""``R * g`` is the principal ideal ``(g)``."""
            return self.ideal(generator)

        def __rmul__(self, generator: RingElement) -> Ideal:
            r"""``g * R`` is the principal ideal ``(g)``."""
            return self.ideal(generator)

        # @override Rings.ParentMethods.quotient
        def quotient(
            self,
            modulus: RingElement | Ideal,
            names: Names = None,
            **kwds,
        ) -> RModule:
            r"""Delegate to Sage, then refine the result into ``Modules(self)``."""
            from sage.categories.rings import Rings as _Rings
            result = _Rings.ParentMethods.quotient(
                self, modulus, names=names, **kwds
            )
            try:
                result._refine_category_(Modules(self))
            except Exception:
                pass
            return result

        def quo(
            self,
            modulus: RingElement | Ideal,
            names: Names = None,
            **kwds,
        ) -> RModule:
            return self.quotient(modulus, names=names, **kwds)

        @final
        def quotient_ring(
            self,
            modulus: RingElement | Ideal,
            names: Names = None,
            **kwds,
        ) -> RModule:
            return self.quotient(modulus, names=names, **kwds)

        @final
        def __truediv__(
            self,
            modulus: RingElement | Ideal,
        ) -> RModule:
            return self.quotient(modulus)

        # @override Rings.ParentMethods.__pow__
        def __pow__(self, n: Integer) -> FreeModule:
            r"""``R ** n`` is the free rank-``n`` R-module.

            The ``FreeModule`` / ``MatrixSpace`` constructors are already
            wrapped by ``refinement.install()`` to refine the result into
            ``Modules(R).Free()``; we simply call them here.
            """
            if isinstance(n, tuple):
                from sage.matrix.matrix_space import MatrixSpace
                return MatrixSpace(self, *n)
            from sage.modules.free_module import FreeModule
            return FreeModule(self, n)

        # @override Ring.free_module — deprecated wrapper kept for legacy callers
        @final
        def free_module(self, base=None, basis=None, map=True):
            r"""Deprecated: use ``R ** 1``."""
            import warnings
            warnings.warn(
                "Ring.free_module() is deprecated; use R ** 1 instead.",
                DeprecationWarning,
                stacklevel=2,
            )
            return self.__pow__(1)

        # @override Rings.ParentMethods.localization
        def localization(
            self, *extra_units: RingElement, **kwds
        ) -> LocalRing:
            from sage.categories.rings import Rings as _Rings
            result = _Rings.ParentMethods.localization(self, *extra_units, **kwds)
            try:
                result._refine_category_(ModuleBaseRings().Local())
            except Exception:
                pass
            return result

        # ``completion`` / ``fraction_field`` / ``derivation_module`` are not
        # overridden here: results are refined lazily the moment they appear
        # as a ``base_ring`` to ``Modules(R)`` via
        # ``refinement.ensure_refined`` in ``Modules.__classcall_private__``.

        # ---- genuinely abstract ----

        @abstract_method
        def unit_ideal(self) -> Ideal: ...

        @abstract_method
        def nilradical(self) -> Ideal: ...

    class ElementMethods:
        r"""Element-level contract.

        ``parent``, ``_repr_``, ``_latex_`` are Sage ``Element`` intrinsics
        and are *not* restated as abstract here.
        """

        def principal_ideal(self) -> Ideal:
            r"""Sugar for ``self.parent().ideal(self)``."""
            return self.parent().ideal(self)

    class MorphismMethods:
        pass


# --- Seed enrollment + constructor hooks -------------------------------------
# Deferred to ``refinement.install()``; runs once at package import time.

from . import refinement as _refinement  # noqa: E402

_refinement.install()
