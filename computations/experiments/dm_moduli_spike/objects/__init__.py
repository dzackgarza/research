r"""Owned objects of the Deligne-Mumford compactification spike.

Layering (each module depends only on those above it):

- ``records``: the immutable half-edge ``StableGraph`` record and its validation.
- ``canonical``: canonical labelling and JSON serialization.
- ``graph_types``: the ``StableGraphTypes`` parent and ``StableGraphType`` element.
- ``contractions``: contraction morphisms of curve types.
- ``enumeration``: one-edge degenerations and rank-by-rank enumeration.
- ``gamma`` / ``stable_graphs``: combinatorial ``Γ_{g,n}`` and typed ``StableGraphs(g,I)``.
- ``stratification``: finite combinatorial stratification and typed poset facades.
- ``model``: internal ``StableGraphStratificationEnumerator`` backend.
- Stack-geometric strata live under ``dm_moduli_spike.geometry``.
"""

from __future__ import annotations
