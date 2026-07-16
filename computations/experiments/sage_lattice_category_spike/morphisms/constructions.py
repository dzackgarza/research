r"""Typed algebraic constructions at their first valid categories.

``R``-Mod is an abelian category: kernel, image, and cokernel exist for
EVERY morphism by contract. The three operations are computed here, once,
from a morphism's matrix presentation over its base ring — the level of
finitely generated free modules, where the data actually lives. The
form-bearing spellings (``LatticeMorphism.kernel/image/cokernel``) delegate
here and add no computation of their own.

The direct sum is a functor, so it also acts on morphisms; ``direct_sum``
below is that action. No same-named construction categories are invented
(no ``Kernels()`` / ``Cokernels()``): these are typed operations sited on
the data they consume — a morphism, or a pair of them.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from sage.matrix.special import block_diagonal_matrix

from .. import lexicon

if TYPE_CHECKING:
    from ..objects.parents import SyntheticLattice
    from .homsets import Subobject, SyntheticLatticeCokernel


def kernel(morphism: lexicon.LatticeMorphism) -> Subobject:
    r"""The kernel as a subobject of the domain: the span of a basis of the
    matrix's right kernel, carried with its inclusion."""
    domain = cast("SyntheticLattice", morphism.domain())
    basis = morphism.matrix().right_kernel().basis_matrix()
    return domain.subobject([domain(list(row)) for row in basis.rows()], "ker")


def image(morphism: lexicon.LatticeMorphism) -> Subobject:
    r"""The image as a subobject of the codomain: the span of the images of
    the domain generators, carried with its inclusion."""
    codomain = cast("SyntheticLattice", morphism.codomain())
    return codomain.subobject([codomain(list(column)) for column in morphism.matrix().columns()], "im")


def direct_sum(first: lexicon.LatticeMorphism, *others: lexicon.LatticeMorphism) -> lexicon.LatticeMorphism:
    r"""The direct sum acting on morphisms — the functor's full data, not an
    object-only construction: ``f (+) g`` is the block-diagonal morphism
    between the summand direct sums, preserving identities and composition.
    Associative and variadic like the object spelling."""
    assert others, "direct_sum needs at least one other summand morphism; fix the caller"
    result = first
    for other in others:
        domain = cast("SyntheticLattice", result.domain()).direct_sum(cast("SyntheticLattice", other.domain()))
        codomain = cast("SyntheticLattice", result.codomain()).direct_sum(cast("SyntheticLattice", other.codomain()))
        result = domain.hom(block_diagonal_matrix(result.matrix(), other.matrix()), codomain=codomain)
    return result


def cokernel(morphism: lexicon.LatticeMorphism) -> SyntheticLatticeCokernel:
    r"""The cokernel ``codomain / image`` as a finitely generated R-module
    (free plus torsion) — it exists for every morphism; the finite
    (full-rank image) case is the special one, not the only one."""
    from .homsets import SyntheticLatticeCokernel

    codomain = cast("SyntheticLattice", morphism.codomain())
    codomain_module = codomain.base_ring() ** codomain.rank()
    image_span = codomain_module.span(morphism.matrix().columns())
    return SyntheticLatticeCokernel(codomain_module.quotient(image_span))
