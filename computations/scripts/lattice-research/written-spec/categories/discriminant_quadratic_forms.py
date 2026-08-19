r"""
Discriminant Quadratic Forms

Thin facade for the descended torsion quadratic meet inside
``ModulesWithForms(R)``. The intended codomain is quotient-valued,
typically `K/R` or `K/2R`, and objects in this category are expected to
arise from explicit descent on actual cokernel objects rather than from
arbitrary top-level constructors.
"""
# ****************************************************************************
#  Copyright (C) 2026  The research project authors
#
#  Distributed under the terms of the GNU General Public License (GPL)
# ****************************************************************************

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from src.lattices.categories.modules_with_forms import ModulesWithForms


class DiscriminantQuadraticForms(CategoryWithAxiom_over_base_ring):
    r"""Facade for the descended torsion quadratic discriminant stratum."""

    def super_categories(self):
        r"""Return the immediate super categories."""
        return [ModulesWithForms(self.base_ring()).Quadratic().Torsion().NonDegenerate()]
