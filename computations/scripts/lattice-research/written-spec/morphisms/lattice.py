from __future__ import annotations

from sage.all import QQ, block_diagonal_matrix, matrix
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method


class BilinearModuleMorphism(Morphism):
    def __init__(self, parent, fgp_morphism):
        import sage.modules.fg_pid.fgp_morphism as fgp_morphism_module

        Morphism.__init__(self, parent)
        if isinstance(fgp_morphism, BilinearModuleMorphism):
            assert fgp_morphism.parent() is parent, "A bilinear-module morphism belongs to a fixed hom-space parent"
            self._fgp_morphism = fgp_morphism._fgp_morphism
            return
        if isinstance(fgp_morphism, fgp_morphism_module.FGP_Morphism):
            if fgp_morphism.parent() == parent._fgp_homset:
                self._fgp_morphism = fgp_morphism
            else:
                self._fgp_morphism = parent._fgp_homset(fgp_morphism)
            return
        self._fgp_morphism = parent._fgp_homset(fgp_morphism)

    @cached_method
    def images(self):
        return tuple(self(generator) for generator in self.domain().gens())

    im_gens = images

    def _sage_like(self):
        return self._fgp_morphism

    def _repr_(self):
        return repr(self._fgp_morphism)

    def to_matrix(self):
        return matrix(self.domain().base_ring(), [image.to_vector() for image in self.images()]).transpose()

    def _call_(self, value):
        element = value if value in self.domain() else self.domain().element_from(value)
        return self.codomain()._wrap_element(self._fgp_morphism(element._sage_like()))

    def __neg__(self):
        return self.parent()(-self._fgp_morphism)

    def __add__(self, other):
        right = self.parent()(other)
        return self.parent()(self._fgp_morphism + right._fgp_morphism)

    def __sub__(self, other):
        right = self.parent()(other)
        return self.parent()(self._fgp_morphism - right._fgp_morphism)

    def image(self):
        return self.codomain()._wrap_sage_submodule(self._fgp_morphism.image())

    def kernel(self):
        return self.domain()._wrap_sage_submodule(self._fgp_morphism.kernel())

    def cokernel(self):
        quotient = self.codomain()._module_like() / self._fgp_morphism.image()
        return self._promote_cokernel(self.codomain()._wrap_sage_quotient(quotient))

    def _promote_cokernel(self, quotient):
        from src.lattices.core.discriminant import DiscriminantGroup
        from src.lattices.core.rational import DualLattice

        codomain = self.codomain()
        if isinstance(codomain, DualLattice) and codomain.source_lattice() is self.domain():
            return DiscriminantGroup.from_invariants_and_gram(
                quotient.invariants(),
                quotient.gram_matrix(),
                lattice=self.domain(),
            )
        return quotient

    def lift(self, value):
        lifted = self._fgp_morphism.lift(self.codomain()(value)._sage_like())
        return self.domain()._wrap_element(lifted)

    def is_primitive(self):
        return self.cokernel().is_torsionfree()

    def is_injective(self):
        return self.kernel().ngens() == 0

    def is_surjective(self):
        return self.cokernel().ngens() == 0

    def is_bijective(self):
        return self.is_injective() and self.is_surjective()

    def is_isomorphism(self):
        return self.is_bijective()

    def is_isometry(self):
        return self in self.parent()

    def inverse(self):
        inverse_matrix = matrix(QQ, self.to_matrix()).inverse()
        return self.codomain().hom(self.domain()).element_from_matrix(inverse_matrix)

    def direct_sum(self, other):
        right = other if isinstance(other, BilinearModuleMorphism) else self.parent()(other)
        domain = self.domain() + right.domain()
        codomain = self.codomain() + right.codomain()
        direct_sum_matrix = block_diagonal_matrix(
            [
                matrix(QQ, self.to_matrix()),
                matrix(QQ, right.to_matrix()),
            ],
            subdivide=False,
        )
        return domain.hom(codomain).element_from_matrix(direct_sum_matrix)


class RationalLatticeMorphism(BilinearModuleMorphism):
    pass


class LatticeMorphism(RationalLatticeMorphism):
    pass
