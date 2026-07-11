r"""Owned objects of the Deligne-Mumford compactification spike.

Layering (each module depends only on those above it):

- ``records``: the immutable half-edge ``StableGraphRecord`` and its validation.
- ``canonical``: canonical labelling, automorphisms, JSON serialization.
- ``curve_types``: the ``StableCurveTypes`` parent and ``StableCurveType`` element.
- ``contractions``: contraction morphisms of curve types.
- ``enumeration``: one-edge degenerations and rank-by-rank enumeration.
- ``strata``: geometric strata and symbolic stack/clutching presentations.
- ``stratification``: the finite stratification and its typed poset facades.
- ``model``: the public ``DMCompactificationModel`` ambient.
"""

from __future__ import annotations
