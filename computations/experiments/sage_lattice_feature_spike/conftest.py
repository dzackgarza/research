r"""Every feature-spike test run brings the base parity spike (and its Sage-defect
patch subtree) live before any lattice object is built: importing the package
imports the base, whose ``__init__`` loads ``sage_patches``. Mirrors the base
spike's own conftest so a broken re-export fails collection loudly."""

import sage_lattice_feature_spike  # noqa: F401  (import side effect: load base + sage_patches)
