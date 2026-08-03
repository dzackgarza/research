r"""Finitely generated modules over a base ring.

Defines the ``FinitelyGenerated`` axiom for ``Modules(R)`` via Sage's ``CategoryWithAxiom_over_base_ring``
framework, enabling ``Modules(R).FinitelyGenerated()`` and ``FinitelyGeneratedModules(R)``.
"""

import sage.categories.category_with_axiom as cwa
from sage.categories.category_types import Category_module
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.modules import Modules
from sage.misc.cachefunc import cached_method

from sage_lattice_category_spike.objects.sets import Sets

# Register FinitelyGenerated axiom string if not present in Sage's axiom container
if "FinitelyGenerated" not in cwa.all_axioms:
    cwa.all_axioms.add("FinitelyGenerated")


class FinitelyGeneratedModules(CategoryWithAxiom_over_base_ring):
    r"""Category of finitely generated modules over a base ring."""

    _base_category_class_and_axiom = (Modules, "FinitelyGenerated")

    def extra_super_categories(self) -> list:
        r"""Require the chosen finite generating morphism used by this preamble."""
        return [Modules(self.base_ring()).Framed()]

    class ParentMethods:
        def module_generators(self):
            r"""Return the finite framed generators as a tuple."""
            generating_set = self.generating_set()
            assert generating_set in Sets().Finite(), (
                "module_generators() is defined only for finitely generated modules"
            )
            return tuple(
                self.generator(element_of_S)
                for element_of_S in generating_set
            )

        def is_finitely_generated(self) -> bool:
            r"""Return whether this module is finitely generated.

            Always ``True`` for objects in this category.
            """
            return True

        def is_zero(self) -> bool:
            r"""Return whether every element in the chosen generating set vanishes."""
            return all(
                generator == self.zero()
                for generator in self.module_generators()
            )


@cached_method
def _fg_subcategory(self):
    return self._with_axiom("FinitelyGenerated")


setattr(Modules, "FinitelyGenerated", FinitelyGeneratedModules)
setattr(Category_module, "FinitelyGenerated", _fg_subcategory)
