r"""
Bilinear Forms

Thin facade for the bilinear stratum subordinate to
``ModulesWithForms(R)``. This file exists to make the category package
layout explicit during the migration; it is not a second top-level
foundation.
"""
# ****************************************************************************
#  Copyright (C) 2026  The research project authors
#
#  Distributed under the terms of the GNU General Public License (GPL)
# ****************************************************************************

from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from src.lattices.categories.modules_with_forms import ModulesWithForms


class BilinearForms(CategoryWithAxiom_over_base_ring):
    r"""Thin facade name for the bilinear refinement of ``ModulesWithForms``."""

    def super_categories(self):
        r"""Return the immediate super categories."""
        return [ModulesWithForms(self.base_ring()).Bilinear()]
