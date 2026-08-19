from __future__ import annotations

from collections.abc import Sequence

from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from src.lattices.validation.presentations import GeneratorImagePresentation


class DiscriminantGroupHomSpace(Homset):
    Element: type[DiscriminantGroupMorphism]

    def __init__(self, domain, codomain, category=None):
        self._domain = domain
        self._codomain = codomain
        self._fgp_homset = domain._sage_like().Hom(codomain._sage_like())
        if category is None:
            category = domain.category()
        Homset.__init__(self, domain, codomain, category=category, check=False)

    def element_from_images(self, images: Sequence):
        presentation = GeneratorImagePresentation(domain=self._domain, codomain=self._codomain, images=images)
        return self._domain._hom_from_smith(tuple(presentation.images))

    def __contains__(self, morphism):
        return (
            isinstance(morphism, DiscriminantGroupMorphism)
            and morphism.parent() is self
            and morphism._fgp_morphism in self._fgp_homset
        )


class DiscriminantGroupMorphism(Morphism):
    def __init__(self, parent, fgp_morphism):
        Morphism.__init__(self, parent)
        if isinstance(fgp_morphism, DiscriminantGroupMorphism):
            assert fgp_morphism.parent() is parent, "Discriminant-group morphisms belong to a fixed hom-space parent"
            self._fgp_morphism = fgp_morphism._fgp_morphism
            return
        if fgp_morphism.parent() == parent._fgp_homset:
            self._fgp_morphism = fgp_morphism
            return
        self._fgp_morphism = parent._fgp_homset(fgp_morphism)

    def _sage_like(self):
        return self._fgp_morphism

    def _call_(self, value):
        return self.codomain()(self._fgp_morphism(self.domain()(value)._sage_like()))

    def image(self):
        codomain_lattice = self.codomain().lattice() if self.codomain()._lattice is not None else None
        return self.codomain()._from_sage_like(self._fgp_morphism.image(), lattice=codomain_lattice)

    def kernel(self):
        domain_lattice = self.domain().lattice() if self.domain()._lattice is not None else None
        return self.domain()._from_sage_like(self._fgp_morphism.kernel(), lattice=domain_lattice)

    def cokernel(self):
        codomain_lattice = self.codomain().lattice() if self.codomain()._lattice is not None else None
        return self.codomain()._from_sage_like(
            self.codomain()._sage_like() / self._fgp_morphism.image(),
            lattice=codomain_lattice,
        )

    def lift(self, value):
        return self.domain()(self._fgp_morphism.lift(self.codomain()(value)._sage_like()))

    def is_injective(self):
        return self.kernel().cardinality() == 1

    def is_surjective(self):
        return self.cokernel().cardinality() == 1

    def is_bijective(self):
        return self.is_injective() and self.is_surjective()

    def is_isomorphism(self):
        return self.is_bijective()

    def is_identity(self):
        return self.domain() is self.codomain() and all(self(generator) == generator for generator in self.domain().gens())


DiscriminantGroupHomSpace.Element = DiscriminantGroupMorphism
