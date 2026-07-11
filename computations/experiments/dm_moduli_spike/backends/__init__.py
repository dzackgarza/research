r"""Backend adapters.

External libraries are reached only through adapters so no third-party class
leaks into the public API.  The public graph type is always
:class:`~dm_moduli_spike.objects.curve_types.StableCurveType`.
"""

from __future__ import annotations
