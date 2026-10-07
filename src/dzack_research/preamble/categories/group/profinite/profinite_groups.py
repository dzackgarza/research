"""Profinite groups."""

from sage.misc.abstract_method import abstract_method
from sage.misc.unknown import Unknown

from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.group.groups import TopologicalGroups
from dzack_research.preamble.logic import Predicate, ask


class ProfiniteGroupIsAbelian(Predicate):
    r"""The proposition that the profinite group ``G`` is abelian.

    A quotient of an abelian group is abelian: if ``q: G -> Q`` is surjective,
    then ``q(s) q(t) = q(st) = q(ts) = q(t) q(s)`` for all ``s, t`` in ``G``.
    So one continuous surjection of ``G`` onto a finite group that is not
    abelian decides the proposition ``False``.  The surjections searched are
    those the group selects through ``_finite_quotient_witnesses``.  A search
    that finds no such quotient decides nothing, because no finite search
    exhausts the finite quotients of ``G``.
    """

    def __init__(self, group):
        self._group = group
        super().__init__()

    def group(self):
        return self._group

    def _ask_(self, *, max_prec=4096):
        if any(
            restriction.codomain().is_abelian() is False
            for restriction in self.group()._finite_quotient_witnesses()
        ):
            return False
        return Unknown

    def _repr_(self):
        return f"{self.group()} is abelian"


class ProfiniteGroups(OwnedCategory):
    def an_object(self):
        r"""The procyclic absolute Galois group of ``GF(2)``."""
        from sage.rings.finite_rings.finite_field_constructor import GF as SageGF

        from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
            AbsoluteGaloisGroup,
        )
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        return AbsoluteGaloisGroup(_own_ring(SageGF(2)))

    @classmethod
    def _repr_object_names(cls):
        return "profinite groups"

    def super_categories(self):
        return [TopologicalGroups()]

    class ParentMethods:
        def continuous_morphisms_to(self, codomain):
            r"""Return the owned group Mor used by represented continuous morphisms.

            Continuity is structure on the selected arrows, not a second Mor.
            """
            return self.Mor(codomain)

        def _abelianity_decision(self):
            r"""Decide commutativity from finite continuous quotients, or return the proposition.

            The answer is ``False`` when a selected continuous surjection onto
            a finite group lands in a group that is not abelian.  Otherwise it
            is the :class:`ProfiniteGroupIsAbelian` proposition, which
            :func:`ask` evaluates.
            """
            proposition = ProfiniteGroupIsAbelian(self)
            answer = ask(proposition)
            return proposition if answer is Unknown else answer

        def _finite_quotient_witnesses(self):
            r"""Yield selected continuous surjections of ``self`` onto finite groups.

            Protected contract (`OWN-05`).  Owner: :class:`ProfiniteGroups`.
            A subcategory whose objects name finite quotients from their own
            data overrides it; each value is a continuous surjective group
            morphism onto a finite group.  Called only by
            ``ProfiniteGroupIsAbelian._ask_``.  The default selects none.
            """
            yield from ()

        @abstract_method(optional=True)
        def topological_group_generators(self):
            r"""Return a family of elements generating a dense subgroup."""
            ...
