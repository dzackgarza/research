r"""Subtree for scheme points in Sch/S.

An R-point of a scheme X over S is a morphism of schemes:
    p: Spec(R) -> X in Sch/S

A point IS such a morphism, so a point carries the two schemes it runs
between and answers with them.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.morphism import Morphism

if TYPE_CHECKING:
    from sage.schemes.generic.scheme import Scheme


class SchemePoint(Morphism):
    r"""A point of a scheme X in Sch/S: the morphism p: Spec(R) -> X."""

    def __init__(self, domain_spec_R: Scheme, codomain_X: Scheme) -> None:
        r"""Build the point p: Spec(R) -> X over the shared base S."""
        assert domain_spec_R.base_ring() == codomain_X.base_ring(), (
            f"Base ring mismatch: domain base {domain_spec_R.base_ring()} "
            f"!= codomain base {codomain_X.base_ring()}"
        )
        self._domain: Scheme = domain_spec_R
        self._codomain: Scheme = codomain_X

    def domain(self) -> Scheme:
        r"""Return the domain scheme Spec(R)."""
        return self._domain

    def codomain(self) -> Scheme:
        r"""Return the codomain scheme X."""
        return self._codomain


def install_scheme_points() -> None:
    r"""Register post-init hooks and installation for scheme points."""
    pass


install_scheme_points()
