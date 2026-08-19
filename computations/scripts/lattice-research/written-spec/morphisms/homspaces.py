from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from sage.all import QQ, ZZ
from sage.categories.homset import Homset
from src.lattices.morphisms.lattice import BilinearModuleMorphism, LatticeMorphism, RationalLatticeMorphism
from src.lattices.validation.presentations import GeneratorImagePresentation, MorphismPresentation

if TYPE_CHECKING:
    from src.lattices.core.abstract import BilinearModule
    from src.lattices.core.elements import FreeBilinearModuleElement


class BilinearModuleHomSpace(Homset):
    Element: type[BilinearModuleMorphism]

    def __init__(self, domain: BilinearModule, codomain: BilinearModule, category=None):
        self._domain = domain
        self._codomain = codomain
        self._fgp_homset = domain._module_like().Hom(codomain._module_like())
        if category is None:
            category = domain.category()
        Homset.__init__(self, domain, codomain, category=category, check=False)

    def _module_ring(self):
        if self._domain.base_ring() is QQ or self._codomain.base_ring() is QQ:
            return QQ
        return ZZ

    def _value_ring(self):
        if self._domain.value_ring() is QQ or self._codomain.value_ring() is QQ:
            return QQ
        return self._codomain.value_ring()

    def _validate_matrix(self, matrix_data):
        presentation = MorphismPresentation(
            module_ring=self._module_ring(),
            value_ring=self._value_ring(),
            domain_ngens=self._domain.ngens(),
            codomain_ngens=self._codomain.ngens(),
            domain_gram=self._domain.gram_matrix(),
            codomain_gram=self._codomain.gram_matrix(),
            matrix_data=matrix_data,
        )
        return presentation.matrix_data

    def _validate_images(self, images: Sequence[FreeBilinearModuleElement]):
        presentation = GeneratorImagePresentation(domain=self._domain, codomain=self._codomain, images=images)
        return tuple(self._codomain(image) for image in presentation.images)

    def _backend_images(self, images: Sequence[FreeBilinearModuleElement]):
        codomain_module = self._codomain._module_like()
        return tuple(codomain_module(image._sage_like()) for image in images)

    def element_from_images(self, images: Sequence[FreeBilinearModuleElement]):
        image_tuple = self._validate_images(images)
        sage_morphism = self._domain._module_like().hom(
            self._backend_images(image_tuple),
            self._codomain._module_like(),
        )
        return self.element_class(self, sage_morphism)

    def element_from_matrix(self, matrix_data):
        morphism_matrix = self._validate_matrix(matrix_data)
        return self.element_from_images(
            tuple(self._codomain.element_from(morphism_matrix.column(index)) for index in range(morphism_matrix.ncols()))
        )

    def element_from_dict(self, mapping: Mapping[FreeBilinearModuleElement, FreeBilinearModuleElement]):
        return self.element_from_images(tuple(mapping[generator] for generator in self._domain.gens()))

    def __call__(self, value):
        from src.lattices.morphisms.lattice import BilinearModuleMorphism

        if isinstance(value, BilinearModuleMorphism):
            assert value.parent() is self, "Morphisms belong to a fixed hom-space parent"
            return value
        if value in self._fgp_homset:
            return self.element_class(self, value)
        return self.element_from_matrix(value)

    def __contains__(self, morphism):
        from src.lattices.morphisms.lattice import BilinearModuleMorphism

        return (
            isinstance(morphism, BilinearModuleMorphism)
            and morphism.parent() is self
            and morphism._fgp_morphism in self._fgp_homset
            and (
                morphism.to_matrix().transpose() * self._codomain.gram_matrix() * morphism.to_matrix()
                == self._domain.gram_matrix()
            )
        )


class RationalLatticeHomSpace(BilinearModuleHomSpace):
    pass


class LatticeHomSpace(RationalLatticeHomSpace):
    pass


BilinearModuleHomSpace.Element = BilinearModuleMorphism
RationalLatticeHomSpace.Element = RationalLatticeMorphism
LatticeHomSpace.Element = LatticeMorphism
