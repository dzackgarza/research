"""Finite free resolutions of finitely presented modules over a PID."""

from dataclasses import dataclass


@dataclass(frozen=True)
class FreeResolution:
    r"""The exact resolution ``0 -> F_1 -> F_0 -> M -> 0`` over a PID."""

    _module: object
    _degree_zero: object
    _degree_one: object
    _differential_one: object
    _augmentation: object

    @classmethod
    def of(cls, module):
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
            BasedFreeModule,
            FinitelyGeneratedFreeModules,
        )
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
            ModulesWithChosenFinitePresentation,
        )
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            module_embedding,
            module_homset,
        )
        from dzack_research.preamble.categories.sets import finite_ordered_set

        ring = module.base_ring()
        if module in FinitelyGeneratedFreeModules(ring):
            degree_one = BasedFreeModule(ring, 0)
            return cls(
                module,
                module,
                degree_one,
                module_embedding(degree_one, module, {}),
                module_homset(module, module).identity(),
            )

        if module not in ModulesWithChosenFinitePresentation(ring):
            raise NotImplementedError(
                "a free resolution currently requires a finite free module or "
                "a module with a chosen finite presentation over a PID"
            )

        degree_zero = module.presentation().codomain()
        relation_rows = tuple(module.W().basis_matrix().rows())
        relation_labels = finite_ordered_set(range(len(relation_rows)))
        degree_one = BasedFreeModule(ring, relation_labels)
        target_labels = tuple(degree_zero.module_generating_set())
        images = {
            label: degree_zero.linear_combination(
                {
                    target_label: coefficient
                    for target_label, coefficient in zip(target_labels, row, strict=True)
                    if coefficient
                }
            )
            for label, row in zip(relation_labels, relation_rows, strict=True)
        }
        return cls(
            module,
            degree_zero,
            degree_one,
            module_embedding(degree_one, degree_zero, images),
            module.presentation_projection(),
        )

    def module(self):
        return self._module

    def term(self, degree):
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule

        degree = int(degree)
        if degree < 0:
            raise ValueError("a homological degree is nonnegative")
        if degree == 0:
            return self._degree_zero
        if degree == 1:
            return self._degree_one
        return BasedFreeModule(self._degree_zero.base_ring(), 0)

    def differential(self, degree):
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

        degree = int(degree)
        if degree <= 0:
            raise ValueError("resolution differentials are indexed in positive degree")
        if degree == 1:
            return self._differential_one
        return module_homset(self.term(degree), self.term(degree - 1)).zero()

    def augmentation(self):
        return self._augmentation

    def length(self):
        return 0 if self._degree_one.rank() == 0 else 1

    def is_exact(self):
        d1 = self.differential(1)
        if not d1.is_injective() or not self.augmentation().is_surjective():
            return False
        if any(
            self.augmentation()(d1(generator)) != self._module.zero()
            for generator in self._degree_one.module_generators()
        ):
            return False

        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
            ModulesWithChosenFinitePresentation,
        )

        ring = self._module.base_ring()
        if self._module in ModulesWithChosenFinitePresentation(ring):
            image_relation_module = d1.tensor().dual_tensor().row_module()
            return image_relation_module == self._module.W()

        if self._degree_one.rank() != 0:
            return False
        return all(
            self.augmentation()(generator) == generator
            for generator in self._degree_zero.module_generators()
        )


def free_resolution(module):
    return FreeResolution.of(module)


__all__ = ["FreeResolution", "free_resolution"]
