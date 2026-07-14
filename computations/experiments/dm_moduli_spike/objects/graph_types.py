r"""Deprecated shims — prefer :mod:`dm_moduli_spike.objects.stable_graphs`.

``StableGraphTypes(g, n)`` aliases :class:`~dm_moduli_spike.objects.stable_graphs.StableGraphs`.
``StableGraphType`` aliases :class:`~dm_moduli_spike.objects.stable_graphs.StableGraph`.

TODO(Phase 2): delete this module and all ``StableGraphTypes`` / ``StableGraphType``
imports; callers must use :class:`StableGraphs` / :class:`StableGraph` directly.
Also delete :class:`~dm_moduli_spike.objects.stratification.DMStratification` once
stratification is owned solely by ``StableGraphs`` + :class:`StableGraphCategory`.
"""

from __future__ import annotations

from .stable_graphs import StableGraph as StableGraphType
from .stable_graphs import StableGraphs as StableGraphTypes

__all__ = ["StableGraphType", "StableGraphTypes"]
