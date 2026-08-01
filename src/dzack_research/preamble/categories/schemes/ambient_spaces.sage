r"""Subtree for ambient spaces AA^n(R) and PP^n(R) shadowing native Sage constructors.

AffineSpace / AA -> constructs native AffineSpace, refines into AffineSpaces(R)
ProjectiveSpace / PP -> constructs native ProjectiveSpace, refines into ProjectiveSpaces(R)
"""

import sage.schemes.affine.affine_space as _sage_affine
import sage.schemes.projective.projective_space as _sage_projective

_NativeAffineSpace = _sage_affine.AffineSpace
_NativeProjectiveSpace = _sage_projective.ProjectiveSpace


def AffineSpace(*args, **kwargs):
    r"""Construct AA^n_R shadowing native Sage AffineSpace, refining into AffineSpaces(R)."""
    obj = _NativeAffineSpace(*args, **kwargs)
    return refine(obj, AffineSpaces(obj.base_ring()))


def ProjectiveSpace(*args, **kwargs):
    r"""Construct PP^n_R shadowing native Sage ProjectiveSpace, refining into ProjectiveSpaces(R)."""
    obj = _NativeProjectiveSpace(*args, **kwargs)
    return refine(obj, ProjectiveSpaces(obj.base_ring()))


# Aliases exported to preamble scope
AA = AffineSpace
PP = ProjectiveSpace


def install_ambient_spaces() -> None:
    r"""Register post-init hooks and installation for ambient spaces."""
    pass
