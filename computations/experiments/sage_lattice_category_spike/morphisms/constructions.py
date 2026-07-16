r"""Typed algebraic constructions at their first valid categories.

``R``-Mod is an abelian category: kernel, image, and cokernel exist for
EVERY morphism by contract. The three operations are computed here, once,
from a morphism's matrix presentation over its base ring — the level of
finitely generated free modules, where the data actually lives. The
form-bearing spellings (``LatticeMorphism.kernel/image/cokernel``) delegate
here and add no computation of their own.

The direct sum is a functor, so it also acts on morphisms; ``direct_sum``
below is that action. No same-named construction categories are invented
(no ``Kernels()``/``Cokernels()``): these are typed operations sited on the
data they consume — a morphism, or a pair of them.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from .. import lexicon

if TYPE_CHECKING:
    from .homsets import Subobject, SyntheticLatticeCokernel


def kernel(morphism: lexicon.LatticeMorphism) -> Subobject:
    r"""The kernel as a subobject of the domain: the span of a basis of the
    matrix's right kernel, carried with its inclusion."""
    domain = morphism.domain()
    basis = morphism.matrix().right_kernel().basis_matrix()
    return cast("Subobject", domain.subobject([domain(list(row)) for row in basis.rows()], "ker"))


def image(morphism: lexicon.LatticeMorphism) -> Subobject:
    r"""The image as a subobject of the codomain: the span of the images of
    the domain generators, carried with its inclusion."""
    codomain = morphism.codomain()
    return cast("Subobject", codomain.subobject([codomain(list(column)) for column in morphism.matrix().columns()], "im"))


def cokernel(morphism: lexicon.LatticeMorphism) -> SyntheticLatticeCokernel:
    r"""The cokernel ``codomain / image`` as a finitely generated R-module
    (free plus torsion) — it exists for every morphism; the finite
    (full-rank image) case is the special one, not the only one."""
    from .homsets import SyntheticLatticeCokernel

    codomain = morphism.codomain()
    codomain_module = codomain.base_ring() ** codomain.rank()
    image_span = codomain_module.span(morphism.matrix().columns())
    return SyntheticLatticeCokernel(codomain_module.quotient(image_span))
