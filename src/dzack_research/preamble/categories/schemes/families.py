r"""Relative affine families and their fibres over a local base.

An affine family ``X -> Spec T`` presented by equations over ``T`` is the
affine ``T``-scheme ``Spec T[x_1,...,x_n]/(f_1,...,f_r)``: an object of
``Sch/T`` is a scheme together with its structure morphism to ``Spec T``, and
that structure morphism is the family.  Fibres are fibre products along
morphisms into ``Spec T``, flatness and the relative nonsmooth locus are the
affine scheme's own operations, and the slice object is
``Schemes(T).as_slice_object(X)``.  Nothing here is a second object beside
the scheme.
"""

from dzack_research.preamble.categories.schemes.schemes import Schemes


def _relative_affine_family(parameter_algebra, relative_variables, equations):
    r"""``Spec T[x_1,...,x_n]/(f_1,...,f_r)`` as an object of ``Schemes(T).Affine()``.

    ``equations`` is either a family of elements of the presentation ring
    ``T[x_1,...,x_n]`` or a function of that ring returning one, since the
    presentation ring does not exist before this construction names it.
    """
    presentation_ring = parameter_algebra.polynomial_ring(relative_variables)
    stated = equations(presentation_ring) if callable(equations) else equations
    total_algebra = presentation_ring.quotient_by_relations(
        tuple(presentation_ring(equation) for equation in stated)
    )
    return total_algebra.affine_spectrum(base_ring=parameter_algebra)


def _special_fiber_comparison(family):
    r"""The isomorphism ``(X_{R^})_k -> X_k`` of the two special fibres over a local base.

    ``R`` is the base ring of ``X``, ``m`` its maximal ideal, ``R^`` the
    ``m``-adic completion and ``k = R/m = R^/m^``.  Both special fibres are
    fibre products over ``Spec k``; the comparison is built from their
    pullback cones, and its inverse from the cone of ``X_k`` into
    ``X_{R^}``, so the two maps are the universal factorizations and are
    mutually inverse by uniqueness.
    """
    base = family.scheme_base_ring()
    completion = base.adic_completion(base.maximal_ideal())
    category = family.scheme_category()
    direct = category.base_change_functor(base.residue_map())(family)
    completed_total = category.base_change_functor(completion.completion_map())(family)
    completed_residue = completed_total.scheme_category().base_change_functor(
        completion.residue_map()
    )
    completed_special = completed_residue(completed_total)

    forward = direct.from_pullback_cone(
        completed_total.left_projection() * completed_special.left_projection(),
        completed_special.right_projection(),
    )
    direct_to_completed_total = completed_total.from_pullback_cone(
        direct.left_projection(),
        completed_residue.base_morphism() * direct.right_projection(),
    )
    inverse = completed_special.from_pullback_cone(
        direct_to_completed_total,
        direct.right_projection(),
    )
    return Schemes(direct.scheme_base_ring()).Core().Mor(completed_special, direct)(
        forward, inverse
    )


__all__ = []
