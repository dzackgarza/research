r"""Modules equipped with a chosen generating morphism.

A framing of an \(R\)-module \(M\) is a surjection

\[
    \phi:F_R(S)\longrightarrow M
\]

for a set \(S\).  The morphism, not a cached list of its values, is the extra
datum.  No finiteness, countability, or orderability hypothesis is imposed on
\(S\).
"""

from typing import Any

import sage.categories.category_with_axiom as cwa
from sage.categories.category_types import Category_module
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.modules import Modules
from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.sets.image_set import ImageSubobject


if "Framed" not in cwa.all_axioms:
    cwa.all_axioms.add("Framed")


class FramedModules(CategoryWithAxiom_over_base_ring):
    r"""Modules carrying a specified surjection \(F_R(S)\to M\)."""

    _base_category_class_and_axiom = (Modules, "Framed")

    class ParentMethods:
        @abstract_method
        def framing_morphism(self) -> "FramingMorphism":
            r"""Return the framing morphism \(F_R(S)\to M\)."""

        def generating_set(self):
            r"""Return the set \(S\) on which the framing source is free."""
            framing = self.framing_morphism()
            assert isinstance(framing, FramingMorphism), (
                "the Framed axiom is witnessed by a declared epimorphism"
            )
            assert framing.codomain() is self, (
                "the stored framing morphism does not land in this module"
            )
            source = framing.domain()
            assert source in FramedFreeModules(self.base_ring()), (
                "the source of a framing morphism is a free module on a set"
            )
            assert framing.parent() is module_homset(source, self), (
                "the framing morphism belongs to a noncanonical homset"
            )
            return source.basis_index_set()

        def generator(self, label: Any):
            r"""Return the image of the basis element indexed by ``label``."""
            source = self.framing_morphism().domain()
            return self.framing_morphism()(source.monomial(label))

        @cached_method
        def gens(self):
            r"""Return the actual image of \(S\) under the framing.

            A finite image receives the transported order fixed by \(S\).
            Otherwise Sage's lazy image-subobject is returned; it does not
            presume that the image can be enumerated.
            """
            labels = self.generating_set()
            if labels in SageSets().Finite():
                return finite_ordered_set(
                    tuple(
                        dict.fromkeys(
                            self.generator(label) for label in labels
                        )
                    )
                )
            return ImageSubobject(
                self.framing_morphism().basis_map(),
                labels,
            )

        def Hom(self, codomain: Any):
            r"""Return the canonical homset from this module to ``codomain``."""
            return module_homset(self, codomain)

        def is_framed(self: Any) -> bool:
            return True


@cached_method
def _framed_subcategory(self):
    return self._with_axiom("Framed")


setattr(Modules, "Framed", FramedModules)
setattr(Category_module, "Framed", _framed_subcategory)
