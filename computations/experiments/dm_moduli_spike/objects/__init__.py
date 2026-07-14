r"""Owned objects of the Deligne-Mumford compactification spike.

Layering (each module depends only on those above it):

- ``records``: the private immutable half-edge ``_GraphRecord`` and its validation.
- ``canonical``: canonical labelling and JSON serialization.
- ``stable_graphs``: the ``StableGraphs(g,I)`` parent and ``StableGraph`` element
  (typed Vertices / HalfEdges / Edges / Legs); owns enumeration caches.
- ``contractions``: contraction morphisms of stable graphs.
- ``enumeration``: one-edge degenerations and rank-by-rank enumeration.
- ``gamma``: combinatorial ``Γ_{g,n}`` with ``StableGraphHomset`` in ``Homsets()``.
- Stack-geometric strata live under ``dm_moduli_spike.geometry``.
"""

from __future__ import annotations
