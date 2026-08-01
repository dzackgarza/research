r"""Subtree for ambient spaces AA^n(R) and PP^n(R) shadowing native Sage types.

AA(dimension, base_ring) -> Affine n-space AA^n_R placed in Schemes(R).
PP(dimension, base_ring) -> Projective n-space PP^n_R placed in Schemes(R) and Varieties(R).Toric(), with .fan(), .picard_group(), and .class_group().
"""

from typing import Any

import sage.schemes.affine.affine_space as _sage_affine
import sage.schemes.projective.projective_space as _sage_projective
from sage.matrix.constructor import matrix
from sage.schemes.toric.all import toric_varieties
from sage.rings.integer_ring import ZZ

_NativeAffineSpace = _sage_affine.AffineSpace
_NativeProjectiveSpace = _sage_projective.ProjectiveSpace


def AffineSpace(*args: Any, **kwargs: Any) -> Any:
    r"""Construct AA^n_R shadowing native Sage AffineSpace, placing it in Schemes(R)."""
    obj = _NativeAffineSpace(*args, **kwargs)
    base_r = obj.base_ring() if hasattr(obj, "base_ring") else ZZ
    return refine(obj, Schemes(base_r))


def ProjectiveSpace(*args: Any, **kwargs: Any) -> Any:
    r"""Construct PP^n_R shadowing native Sage ProjectiveSpace, placing it in Schemes(R)."""
    obj = _NativeProjectiveSpace(*args, **kwargs)
    base_r = obj.base_ring() if hasattr(obj, "base_ring") else ZZ
    return refine(obj, Schemes(base_r))


def AA(dimension: Any = 1, base_ring: Any = ZZ) -> Any:
    r"""Construct AA^n_R (Affine n-space over base_ring)."""
    obj = AffineSpace(dimension, base_ring)
    
    # Pic(AA^n) = Cl(AA^n) = 0 (rank 0 formed module)
    zero_lattice = IntegralLattice(matrix(ZZ, 0, 0, []))
    obj.picard_group = lambda: zero_lattice
    obj.class_group = lambda: zero_lattice
    return obj


def PP(dimension: Any = 1, base_ring: Any = ZZ) -> Any:
    r"""Construct PP^n_R (Projective n-space over base_ring) as a toric variety.
    
    Pic(PP^n) = Cl(PP^n) = I_{1, 0}, the rank-1 unimodular formed module with Gram matrix (1).
    """
    obj = ProjectiveSpace(dimension, base_ring)
    base_r = obj.base_ring() if hasattr(obj, "base_ring") else base_ring
    refine(obj, Varieties(base_r))
    
    # Attach fan() method for toric projective space
    dim = int(dimension)
    obj.fan = lambda: toric_varieties.P(dim).fan()

    # Pic(PP^n) = Cl(PP^n) = I_{1, 0} (Gram matrix (1))
    i_1_0 = IntegralLattice(matrix(ZZ, 1, 1, [1]))
    obj.picard_group = lambda: i_1_0
    obj.class_group = lambda: i_1_0
    return obj


def install_ambient_spaces() -> None:
    r"""Register post-init hooks and installation for ambient spaces."""
    pass
