r"""Lattices over integral domains."""

from __future__ import annotations

from abc import abstractmethod
from typing import final

from sage.misc.lazy_import import LazyImport

from ...cat import CategoryWithAxiom_over_base_ring
from ...types import DiscriminantGroup, Lattice, RModule, RModuleMorphism, SubModule
from ..chain import LatticesCategory


class _LatticesOverIntegralDomain(CategoryWithAxiom_over_base_ring):
    r"""Lattices whose base ring is an integral domain.

    Canonical chain: ``Lattices(R).OverIntegralDomain()``.

    This is the first lattice refinement where the fraction field ``K`` of
    ``R`` is available.  Metric duals, rational spans, and primitivity by
    torsion-free quotient therefore belong here rather than to the stronger
    Dedekind-domain refinement.
    """

    _base_category_class_and_axiom = (LatticesCategory, "OverIntegralDomain")
    _defining_predicates = ("is_over_integral_domain",)
    OverDedekindDomain = LazyImport(
        "category_specs.lattices.subcategories.over_dedekind",
        "_LatticesOverDedekindDomain",
    )

    class ParentMethods:
        @final
        def is_over_integral_domain(self) -> bool:
            return True

        @abstractmethod
        def is_primitive(self, S: SubModule) -> bool:
            r"""Return whether ``S`` is primitive in ``L``.

            For a submodule ``S <= L`` over an integral domain, this means
            ``L/S`` is torsion-free, equivalently
            ``S = L cap (S tensor_R K)`` inside ``L tensor_R K`` when the
            scalar extension is realized.
            """
            ...

        @abstractmethod
        def rational_span(self) -> RModule:
            r"""Return ``L tensor_R K`` as a bilinear module over ``K=Frac(R)``."""
            ...

        @abstractmethod
        def dual_lattice(self) -> Lattice:
            r"""Return the metric dual ``L^# = {v in L_K : b(v, L) subset R}``.

            Diagnostics: when the global category diagnostic flag is enabled, emit a
            category diagnostic if this call may be confused with the Hom-dual object
            ``Hom_R(L, R)``.  The diagnostic should name the hypotheses under which
            the form identifies ``L^#`` with the Hom dual, or say that no such
            evaluation-bearing identification is being returned.
            """
            ...

        @abstractmethod
        def inclusion_morphism(self) -> RModuleMorphism:
            r"""Return the canonical inclusion ``L -> L^#``."""
            ...

        @abstractmethod
        def discriminant_group(self) -> DiscriminantGroup:
            r"""Return ``A_L = L^# / L`` with descended quotient-valued form data."""
            ...

        @final
        def is_unimodular(self) -> bool:
            r"""Return whether ``L = L^#``, equivalently ``A_L`` is trivial."""
            return self.discriminant_group().is_trivial()

    class ElementMethods: ...
