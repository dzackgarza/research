r"""Modules equipped with a chosen finite or infinite generating set.

``Framed`` records the extra data used by the coordinate-facing module
categories in this preamble.  It is deliberately separate from
``FinitelyGenerated``: the latter is an existence assertion, whereas this
axiom says that a particular generating set is part of each object.
"""

from typing import Any

import sage.categories.category_with_axiom as cwa
from sage.categories.category_types import Category_module
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.modules import Modules
from sage.misc.cachefunc import cached_method


if "Framed" not in cwa.all_axioms:
    cwa.all_axioms.add("Framed")


class FramedModules(CategoryWithAxiom_over_base_ring):
    r"""Category of modules with a chosen generating-set witness.

    A framed module is understood as a module ``M`` together with a map
    ``Free_R(S) -> M``.  ``generating_set()`` returns ``S``; ``gens()`` is the
    image of that set in ``M``.
    """

    _base_category_class_and_axiom = (Modules, "Framed")

    class ParentMethods:
        def generating_set(self):
            r"""Extract the actual set ``S`` in ``Free_R(S) -> M``.

            Construction stores this witness on the parent.  A missing
            witness is an invalid framed object and fails at extraction.
            """
            return self._generating_set

        def is_framed(self: Any) -> bool:
            r"""Return whether this module includes a chosen generating set."""
            return True

        def is_zero(self: Any) -> bool:
            r"""Return whether every chosen generator is zero."""
            return all(generator == self.zero() for generator in self.gens())


@cached_method
def _framed_subcategory(self):
    return self._with_axiom("Framed")


setattr(Modules, "Framed", FramedModules)
setattr(Category_module, "Framed", _framed_subcategory)
