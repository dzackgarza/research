r"""Subtree for ambient spaces AA^n(R) and PP^n(R) shadowing native Sage constructors.

AffineSpace / AA -> constructs native AffineSpace, refines into AffineSpaces(R)
ProjectiveSpace / PP -> constructs native ProjectiveSpace, refines into ProjectiveSpaces(R)
"""

from typing import TYPE_CHECKING
from dzack_research.preamble.categories.schemes.schemes import AffineSpaces
from dzack_research.preamble.categories.schemes.schemes import ProjectiveSpaces
from dzack_research.preamble.refine import refine
if TYPE_CHECKING:
    from sage.structure.parent import Parent
    from sage.rings.ring import Ring

import sage.schemes.affine.affine_space as _sage_affine
import sage.schemes.projective.projective_space as _sage_projective


if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet


_NativeAffineSpace = _sage_affine.AffineSpace
_NativeProjectiveSpace = _sage_projective.ProjectiveSpace


def AffineSpace(
    n: "Integer",
    R: "Ring | None" = None,
    names: "OrderedSet | None" = None,
    ambient_projective_space: "Parent | None" = None,
    default_embedding_index: "Integer | None" = None,
) -> "Parent":
    r"""Construct $\mathbb A^n_R$, refining it into ``AffineSpaces(R)``."""
    obj = _NativeAffineSpace(
        n, R, names, ambient_projective_space, default_embedding_index
    )
    affine_space: "Parent" = refine(obj, AffineSpaces(obj.base_ring()))
    return affine_space


def ProjectiveSpace(
    n: "Integer",
    R: "Ring | None" = None,
    names: "OrderedSet | None" = None,
) -> "Parent":
    r"""Construct $\mathbb P^n_R$, refining it into ``ProjectiveSpaces(R)``."""
    obj = _NativeProjectiveSpace(n, R, names)
    projective_space: "Parent" = refine(obj, ProjectiveSpaces(obj.base_ring()))
    return projective_space


# Aliases exported to preamble scope
AA = AffineSpace
PP = ProjectiveSpace


def install_ambient_spaces() -> None:
    r"""Register post-init hooks and installation for ambient spaces."""
    pass


install_ambient_spaces()
