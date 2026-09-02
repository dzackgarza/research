"""Modules equipped with a chosen generating morphism."""

from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from dzack_research.preamble.categories.sets import Sets

from dzack_research.preamble.categories.rings import OwnedCategoryOverBaseRing


class FramedModules(OwnedCategoryOverBaseRing):
    r"""Modules carrying a specified generating map from a set."""

    @classmethod
    def _repr_object_names(cls):
        return "framed modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        return [Modules(self.base_ring())]

    class ParentMethods:
        def number_of_module_generators(self):
            return self.module_generating_set().cardinality()

        def module_generator_morphism(self):
            source = self.module_generating_set()
            return SetMorphism(
                Sets().hom(source, self),
                self.module_generator,
            )

        def linear_combination(self, coefficients, factor_on_left=True):
            if not isinstance(coefficients, dict):
                return super().linear_combination(
                    coefficients,
                    factor_on_left=factor_on_left,
                )
            return sum(
                (
                    self.scalar_multiple(
                        coefficient,
                        self.module_generator(label),
                    )
                    for label, coefficient in coefficients.items()
                ),
                self.zero(),
            )

        def inject_variables(self, scope=None, verbose=True):
            if not isinstance(scope, dict):
                raise TypeError("scope is required when injecting module generators")
            names = tuple(self.variable_names())
            generators = tuple(self.module_generators())
            if len(names) != len(generators):
                raise ValueError("the variable names do not describe the module framing")
            if verbose:
                print("Defining %s" % ", ".join(names))
            scope.update(zip(names, generators, strict=True))

        def is_framed(self) -> bool:
            return True

        def subobject_on(self, module_generating_set):
            r"""Return the submodule spanned by the specified elements."""
            from dzack_research.preamble.categories.modules.subobjects import (
                module_subobject_on,
            )

            return module_subobject_on(self, module_generating_set)

        def hom(self, images, codomain=None):
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_homset,
            )

            if codomain is None:
                if isinstance(images, dict) and images:
                    codomain = next(iter(images.values())).parent()
                elif isinstance(images, (tuple, list)) and images:
                    codomain = images[0].parent()
                else:
                    raise TypeError("the codomain is required when it cannot be read from generator images")
            return module_homset(self, codomain)(images)
