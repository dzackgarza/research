r"""Profinite groups: the ``Profinite`` axiom on topological groups.

A profinite group is an inverse limit of finite groups, equivalently a
compact Hausdorff topological group that is totally disconnected.  It
carries a topology, and its algebraic generators differ from its
topological generators the way module generators differ from algebra
generators: a finite set may topologically generate while no finite set
algebraically generates.  The two are distinct notions, both
meaningful, and both named.

The absolute Galois group \(G_K=\operatorname{Gal}(\bar K/K)\) is the
shape of all profinite groups in this preamble; its construction lives
in :mod:`absolute_galois_groups`.

Sage's :class:`Groups` already exposes ``Groups().Topological()`` as a
regressive covariant construction category.  ``Profinite`` is an axiom
on that, so ``ProfiniteGroups()`` is the ambient
category for all profinite groups here.

Placed as a plain subcategory of Sage's topological groups rather than as a
new axiom.  An axiom would have to be registered globally and installed onto
``Groups.Topological`` by hand, and it buys nothing here: nothing asks Sage to
*derive* profiniteness from other axioms, and the only thing wanted is that a
profinite group sits somewhere honest in the hierarchy.
"""

from sage.categories.category_singleton import Category_singleton
from sage.categories.groups import Groups as SageGroups


class ProfiniteGroups(Category_singleton):
    r"""Profinite groups: topological groups that are inverse limits of
    finite groups, each carrying the limit topology."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "profinite groups"

    def super_categories(self) -> list:
        # Local: a module-level import would close a cycle; the module is built by the time this runs.
        from dzack_research.preamble.categories.group.groups import OwnedGroups

        return [OwnedGroups(), SageGroups().Topological()]

    class ParentMethods:
        def topological_group_generators(self):
            r"""Yield some topological generators as an infinite stream.

            Distinct from :meth:`group_generators`: a finite set may be
            topologically dense without algebraically generating, the way a
            finite set of algebra generators need not module-generate.
            No exhaustivity is claimed; the supply is infinite.
            """
            yield from self.group_generators()

        def is_profinite(self) -> bool:
            r"""Return ``True``: membership in this category is the claim."""
            return True
