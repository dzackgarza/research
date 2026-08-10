r"""Subtree for scheme points in Sch/S.

An R-point of a scheme X over S is a morphism of schemes:
    p: Spec(R) -> X in Sch/S

Since a point IS a morphism in Sch/S, SchemePoint is a subclass of SchemeMorphism.
"""

from __future__ import annotations

from dzack_research.preamble.categories.schemes.scheme_morphisms import SchemeMorphism

from typing import TYPE_CHECKING
from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.misc.abstract_method import abstract_method
from sage.rings.integer_ring import ZZ as SageZZ

if TYPE_CHECKING:
    from sage.schemes.generic.scheme import Scheme


class SchemePoint(SchemeMorphism):
    r"""A point of a scheme X in Sch/S.

    Modeled directly as a scheme morphism p: Spec(R) -> X in Sch/S.
    """

    def __init__(self, domain_spec_R: Scheme, codomain_X: Scheme) -> None:
        r"""Initialize a scheme point p: Spec(R) -> X in Sch/S."""
        assert domain_spec_R.base_ring() == codomain_X.base_ring(), (
            f"Base ring mismatch: domain base {domain_spec_R.base_ring()} "
            f"!= codomain base {codomain_X.base_ring()}"
        )
        self._domain: Scheme = domain_spec_R
        self._codomain: Scheme = codomain_X

    def domain(self) -> Scheme:
        r"""Return domain scheme Spec(R)."""
        return self._domain

    def codomain(self) -> Scheme:
        r"""Return codomain scheme X."""
        return self._codomain


def install_scheme_points() -> None:
    r"""Register post-init hooks and installation for scheme points."""
    pass
