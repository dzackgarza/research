r"""Free/Forgetful Adjunction between Set and R-Mod with Triangle Identities.

Formalizes the adjunction F_R \dashv U:
- Left adjoint functor F_R: Set -> Mod_R
- Right adjoint functor U: Mod_R -> Set
- Unit natural transformation \eta: 1_Set \implies U \circ F_R
- Counit natural transformation \varepsilon: F_R \circ U \implies 1_{Mod_R}

Satisfies the natural hom-set bijection:
    \Phi_{S, M}: Hom_{Mod_R}(F_R(S), M) \xrightarrow{\sim} Hom_{Set}(S, U(M))
    \Phi(\phi) = U(\phi) \circ \eta_S
    \Psi(f)   = \varepsilon_M \circ F_R(f)

And the triangle identities (zigzag equations):
    1) U(\varepsilon_M) \circ \eta_{U(M)} = id_{U(M)}  \in End_{Set}(U(M))
    2) \varepsilon_{F_R(S)} \circ F_R(\eta_S) = id_{F_R(S)}  \in End_{Mod_R}(F_R(S))
"""

from typing import Any
from sage.categories.functor import Functor
from sage.categories.homset import Hom
from sage.categories.modules import Modules
from sage.categories.sets_cat import Sets
from sage.misc.abstract_method import abstract_method
from sage.structure.sage_object import SageObject
from sage.categories.morphism import SetMorphism
from sage_lattice_category_spike.objects.underlying_sets import UnderlyingSet


class FreeModuleFunctorClass(Functor):
    r"""The free module functor F_R: Set -> Mod_R."""

    def __init__(self, base_ring: Any):
        self._base_ring = base_ring
        super().__init__(Sets(), Modules(base_ring))

    def _apply_object(self, set_object: Any) -> Any:
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
            FreeModuleOnSet,
        )

        return FreeModuleOnSet(self._base_ring, set_object)

    def _apply_morphism(self, set_morphism: SetMorphism) -> Any:
        r"""Apply F_R to a set morphism f: S -> T, producing F_R(f): F_R(S) -> F_R(T)."""
        domain_free = self._apply_object(set_morphism.domain())
        codomain_free = self._apply_object(set_morphism.row() if hasattr(set_morphism, 'row') else set_morphism.codomain())
        mapping = {
            s: codomain_free.module_generator_element(set_morphism(s))
            for s in set_morphism.domain()
        }
        return domain_free.Hom(codomain_free)(mapping)


class ForgetfulFunctorClass(Functor):
    r"""The forgetful functor U: Mod_R -> Set."""

    def __init__(self, base_ring: Any):
        self._base_ring = base_ring
        super().__init__(Modules(base_ring), Sets())

    def _apply_object(self, module_object: Any) -> Any:
        return UnderlyingSet(module_object)

    def _apply_morphism(self, module_morphism: Any) -> SetMorphism:
        r"""Apply U to a module morphism \phi: M -> N, producing U(\phi): U(M) -> U(N)."""
        domain_set = UnderlyingSet(module_morphism.domain())
        codomain_set = UnderlyingSet(module_morphism.codomain())
        mapping = {
            s: codomain_set.element_class(codomain_set, module_morphism(s.value))
            for s in domain_set
        }
        return SetMorphism(Hom(domain_set, codomain_set, Sets()), mapping)


class Adjunction(SageObject):
    r"""An adjunction (F, U, \eta, \varepsilon) between categories C and D."""

    def __init__(self, left_adjoint: Functor, right_adjoint: Functor):
        self._left_adjoint = left_adjoint
        self._right_adjoint = right_adjoint

    def left_adjoint(self) -> Functor:
        r"""Return the left adjoint functor $F: \mathcal{C} \to \mathcal{D}$."""
        return self._left_adjoint

    def right_adjoint(self) -> Functor:
        r"""Return the right adjoint functor $U: \mathcal{D} \to \mathcal{C}$."""
        return self._right_adjoint

    @abstract_method
    def unit(self, object_C: Any) -> Any:
        r"""Return the unit component $\eta_A: A \to U(F(A))$ in Hom_C(A, U(F(A)))."""

    @abstract_method
    def counit(self, object_D: Any) -> Any:
        r"""Return the counit component $\varepsilon_B: F(U(B)) \to B$ in Hom_D(F(U(B)), B)."""

    @abstract_method
    def hom_set_isomorphism_forward(self, module_morphism: Any) -> Any:
        r"""Forward bijection \Phi(\phi) = U(\phi) \circ \eta_S."""

    @abstract_method
    def hom_set_isomorphism_inverse(
        self, set_morphism: Any, codomain_D: Any
    ) -> Any:
        r"""Inverse bijection \Psi(f) = \varepsilon_M \circ F(f)."""


class FreeForgetfulAdjunction(Adjunction):
    r"""The free/forgetful adjunction F_R \dashv U between Set and R-Mod."""

    def __init__(self, base_ring: Any):
        self._base_ring = base_ring
        super().__init__(
            FreeModuleFunctorClass(base_ring),
            ForgetfulFunctorClass(base_ring),
        )

    def unit(self, set_object: Any) -> SetMorphism:
        r"""Return the unit set map \eta_S: S \to U(F_R(S)), s \mapsto e_s."""
        free_mod = self._left_adjoint(set_object)
        target_set = self._right_adjoint(free_mod)
        mapping = {s: free_mod.module_generator_element(s) for s in set_object}
        return SetMorphism(Hom(set_object, target_set, Sets()), mapping)

    def counit(self, module_object: Any) -> Any:
        r"""Return the counit module epimorphism \varepsilon_M: F_R(U(M)) \twoheadrightarrow M."""
        underlying = self._right_adjoint(module_object)
        free_mod = self._left_adjoint(underlying)
        mapping = {s: s.value for s in underlying}
        return free_mod.Hom(module_object)(mapping)

    def hom_set_isomorphism_forward(self, module_morphism: Any) -> SetMorphism:
        r"""Forward bijection \Phi(\phi) = U(\phi) \circ \eta_S: S \to U(M)."""
        domain_free = module_morphism.domain()
        set_object = domain_free.generating_set()
        eta_S = self.unit(set_object)
        U_phi = self._right_adjoint._apply_morphism(module_morphism)
        return U_phi * eta_S

    def hom_set_isomorphism_inverse(
        self, set_morphism: SetMorphism, codomain_module: Any
    ) -> Any:
        r"""Inverse bijection \Psi(f) = \varepsilon_M \circ F_R(f): F_R(S) \to M."""
        F_f = self._left_adjoint._apply_morphism(set_morphism)
        epsilon_M = self.counit(codomain_module)
        return epsilon_M * F_f
