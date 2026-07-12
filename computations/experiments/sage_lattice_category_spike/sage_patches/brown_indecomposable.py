r"""Ruled-in re-export of Sage's private per-block Brown-invariant engine.

``_brown_indecomposable`` is Sage-private, but the per-block Brown invariant
it computes has no public Sage surface, and its use was ruled in explicitly
(see ``brown_invariant_blocks``: "engine, ruled in despite
``_brown_indecomposable`` being private"). Reaching a foreign private is a
siting finding everywhere else in the package (``pyrightconfig.json``,
``reportPrivateUsage``); this subtree is the one sanctioned crossing point
for Sage-boundary reaches and is excluded from that check by name.
"""

from sage.modules.torsion_quadratic_module import _brown_indecomposable

brown_indecomposable = _brown_indecomposable
