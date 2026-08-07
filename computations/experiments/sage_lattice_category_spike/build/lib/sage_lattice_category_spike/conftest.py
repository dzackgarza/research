r"""Every test run imports the full Sage-defect patch subtree: monkey-patches
(when any exist) apply at import, and a broken re-export fails collection
loudly instead of surfacing mid-test."""

import sage_lattice_category_spike.sage_patches  # noqa: F401
