r"""Free modules over a base ring with a chosen basis.

The category of free modules equipped with a chosen basis.  No finite-generation
hypothesis is assumed at this node.  Finitely generated free modules are refined
in ``finitely_generated_free_modules.sage``.
"""

from typing import Any

from sage.categories.category_types import Category_over_base_ring
from sage.categories.modules import Modules


class FramedFreeModules(Category_over_base_ring):
    r"""Category of free modules over a base ring with a chosen basis."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "based free modules"

    def super_categories(self) -> list:
        return [FreeModules(self.base_ring()), Modules(self.base_ring()).Framed()]

    class ParentMethods:
        r"""What a chosen basis of a free module makes askable."""

        def basis(self):
            r"""Return the chosen basis, namely the image of ``S`` in ``M``.

            No finite, countable, or orderability hypothesis is attached to
            this category.  Those are refinements of the framing witness and
            its image.
            """
            return self.gens()

        def linear_combination(self: Any, coefficients: Any) -> Any:
            r"""Return $\sum_i a_ie_i$.

            Shadows Sage's ``Modules.ParentMethods.linear_combination``, which
            reads its argument as ``(element, coefficient)`` pairs.  Every
            object in this universe reads a coefficient vector the way this one
            does, and one name with two meanings is worse than either.
            """
            coefficients = tuple(coefficients)
            generators = self.gens()
            assert len(coefficients) == len(generators), (
                f"this module has {len(generators)} basis elements, got "
                f"{len(coefficients)} coefficients"
            )
            total = self.zero()
            for coefficient, generator in zip(coefficients, generators):
                total += self.base_ring()(coefficient) * generator
            return total

        def subobject_on(self: Any, generators: Any) -> Any:
            r"""Return the submodule these generate, as its inclusion."""
            generators = _independent_generators(self, generators)
            sub = BasedFreeModule(
                self.base_ring(), standard_framing_set(len(generators))
            )
            return Subobject(
                ModuleMorphism.zero(sub, self)
                if not generators
                else _module_morphism(dict(zip(sub.gens(), generators)))
            )

        def is_torsionfree(self: Any) -> bool:
            r"""Return whether this module is torsion-free."""
            return True

        def is_torsion(self: Any) -> bool:
            r"""Return whether this module is torsion."""
            return self.is_zero()

        def hom(self: Any, images: Any, codomain: Any = None) -> Any:
            r"""Return the morphism sending this module's basis to ``images``."""
            images = tuple(images)
            generators = self.gens()
            assert len(images) == len(generators), (
                f"this module has {len(generators)} basis elements, got "
                f"{len(images)} images"
            )
            if not images:
                assert codomain is not None, (
                    "a morphism out of the zero module needs its codomain named"
                )
                return ModuleMorphism.zero(self, codomain)
            return _module_morphism(dict(zip(generators, images)))

        def Aut(self: Any) -> Any:
            r"""Return the homset of automorphisms of this module."""
            cached = self.__dict__.get("_preamble_Aut")
            if cached is None:
                cached = ModuleAutomorphismGroup(self)
                self._preamble_Aut = cached
            return cached
