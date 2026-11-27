r"""Compatibility imports for the named lattice axiom chain.

The lattice root category is defined in :mod:`category_specs.lattices` so that
the package initializer remains the readable index into the subtree.  This
module remains as a compatibility surface for existing imports such as
``category_specs.lattices.chain.LatticesCategory``.
"""

from __future__ import annotations

from . import (
    Lattices,
    LatticesAut,
    LatticesAutCategory,
    LatticesAutomorphism,
    LatticesCategory,
    LatticesElement,
    LatticesEnd,
    LatticesEndCategory,
    LatticesEndomorphism,
    LatticesHom,
    LatticesHomCategory,
    LatticesMorphism,
    LatticesObject,
    _lattice_chain,
    lattice_category,
)
