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

    def __init__(self, base_ring: "Ring"):
        self._base_ring = base_ring
        super().__init__(Sets(), Modules(base_ring))

    @cached_method
    def _apply_functor(self, set_object: "Set") -> "Module":
        r"""Return \(F_R(S)\), the same object on every call.

        ``FreeModuleOnSet`` is not a ``UniqueRepresentation``, so
        constructing it twice yields two parents.  A functor must be
        well-defined on objects -- \(F(\operatorname{dom} f)\) has to *be*
        the domain of \(F(f)\), not merely be isomorphic to it -- so the
        result is cached here.
        """
        return FreeModuleOnSet(self._base_ring, set_object)

    def _apply_functor_to_morphism(self, set_morphism: SetMorphism) -> "Morphism":
        r"""Apply F_R to a set morphism f: S -> T, producing F_R(f): F_R(S) -> F_R(T)."""
        domain_free = self._apply_functor(set_morphism.domain())
        codomain_free = self._apply_functor(set_morphism.codomain())
        mapping = {
            s: codomain_free.module_generator(set_morphism(s))
            for s in set_morphism.domain()
        }
        return domain_free.Hom(codomain_free)(mapping)


class UnderlyingSetOfGroupFunctor(Functor):
    r"""The forgetful functor \(U:\mathrm{Grp}\to\mathrm{Set}\)."""

    def __init__(self) -> None:
        from sage.categories.groups import Groups

        super().__init__(Groups(), Sets())

    def _apply_functor(self, group: "Group") -> "Set":
        return UnderlyingSet(group)

    def _apply_functor_to_morphism(self, group_morphism: "Morphism") -> SetMorphism:
        return SetMorphism(
            Hom(
                UnderlyingSet(group_morphism.domain()),
                UnderlyingSet(group_morphism.codomain()),
                Sets(),
            ),
            group_morphism,
        )


class GroupRingFunctor(Functor):
    r"""The group ring functor \(R[-]:\mathrm{Grp}\to\mathrm{Rings}\).

    \(R[G]\) is the free \(R\)-module on \(G\) with the multiplication got by
    extending the group law bilinearly.  It is the construction a group
    supports that a bare set does not, and an \(R[G]\)-module is then a module
    over this ring and nothing further.

    A functor and not ``G.algebra(R)``: an object that is a semigroup under
    two operations -- as a subgroup of \(O(L)\) is, being an endset whose
    morphisms also add -- leaves that method ambiguous, and Sage says so.
    Naming \(\mathrm{Grp}\) as the source is what resolves it, so the
    disambiguation lives in the functor's declaration rather than at each
    call site.
    """

    def __init__(self, base_ring: "Ring") -> None:
        from sage.categories.groups import Groups
        from sage.categories.rings import Rings

        self._base_ring = base_ring
        super().__init__(Groups(), Rings())

    def base_ring(self) -> "Ring":
        return self._base_ring

    @cached_method
    def _apply_functor(self, group: "Group") -> "Ring":
        from sage.algebras.group_algebra import GroupAlgebra

        return GroupAlgebra(group, self._base_ring)


class FreeModuleOnGroupFunctor(Functor):
    r"""The underlying \(R\)-module of the group ring, \(\mathrm{Grp}\to R\text{-Mod}\).

    Not the free module functor on groups: a group structure on \(S\) endows
    \(F_R(S)\) with a multiplication, extending the group law bilinearly, so
    the construction \(\mathrm{Grp}\) actually supports is the group ring
    \(R[G]\) -- an \(R\)-algebra, not merely a module.  This functor is that
    one followed by forgetting the multiplication, and it is named for what
    it is rather than for the composite that computes it.
    """

    def __init__(self, base_ring: "Ring") -> None:
        from sage.categories.groups import Groups

        self._base_ring = base_ring
        self._free_on_sets = FreeModuleFunctorClass(base_ring)
        self._underlying_set = UnderlyingSetOfGroupFunctor()
        super().__init__(Groups(), Modules(base_ring))

    def base_ring(self) -> "Ring":
        return self._base_ring

    def _apply_functor(self, group: "Group") -> "Module":
        return self._free_on_sets(self._underlying_set(group))

    def _apply_functor_to_morphism(self, group_morphism: "Morphism") -> "Morphism":
        return self._free_on_sets._apply_functor_to_morphism(
            self._underlying_set._apply_functor_to_morphism(group_morphism)
        )


class ForgetfulFunctorClass(Functor):
    r"""The forgetful functor U: Mod_R -> Set."""

    def __init__(self, base_ring: "Ring"):
        self._base_ring = base_ring
        super().__init__(Modules(base_ring), Sets())

    def _apply_functor(self, module_object: "Module") -> "Module":
        return UnderlyingSet(module_object)

    def _apply_functor_to_morphism(self, module_morphism: "ModuleMorphism") -> SetMorphism:
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
    def unit(self, object_C: "Set") -> "Morphism":
        r"""Return the unit component $\eta_A: A \to U(F(A))$ in Hom_C(A, U(F(A)))."""

    @abstract_method
    def counit(self, object_D: "Module") -> "Morphism":
        r"""Return the counit component $\varepsilon_B: F(U(B)) \to B$ in Hom_D(F(U(B)), B)."""

    @abstract_method
    def hom_set_isomorphism_forward(self, module_morphism: "ModuleMorphism") -> "Morphism":
        r"""Forward bijection \Phi(\phi) = U(\phi) \circ \eta_S."""

    @abstract_method
    def hom_set_isomorphism_inverse(
        self, set_morphism: "SetMorphism", codomain_D: "Module"
    ) -> "ModuleMorphism":
        r"""Inverse bijection \Psi(f) = \varepsilon_M \circ F(f)."""


class FreeForgetfulAdjunction(Adjunction):
    r"""The free/forgetful adjunction F_R \dashv U between Set and R-Mod."""

    def __init__(self, base_ring: "Ring"):
        self._base_ring = base_ring
        super().__init__(
            FreeModuleFunctorClass(base_ring),
            ForgetfulFunctorClass(base_ring),
        )

    def unit(self, set_object: "Set") -> SetMorphism:
        r"""Return the unit set map \eta_S: S \to U(F_R(S)), s \mapsto e_s."""
        free_mod = self._left_adjoint(set_object)
        target_set = self._right_adjoint(free_mod)
        mapping = {s: free_mod.module_generator(s) for s in set_object}
        return SetMorphism(Hom(set_object, target_set, Sets()), mapping)

    def counit(self, module_object: "Module") -> "Morphism":
        r"""Return the counit module epimorphism \varepsilon_M: F_R(U(M)) \twoheadrightarrow M."""
        underlying = self._right_adjoint(module_object)
        free_mod = self._left_adjoint(underlying)
        mapping = {s: s.value for s in underlying}
        return free_mod.Hom(module_object)(mapping)

    def hom_set_isomorphism_forward(self, module_morphism: "ModuleMorphism") -> SetMorphism:
        r"""Forward bijection \Phi(\phi) = U(\phi) \circ \eta_S: S \to U(M)."""
        domain_free = module_morphism.domain()
        set_object = domain_free.module_generating_set()
        eta_S = self.unit(set_object)
        U_phi = self._right_adjoint._apply_functor_to_morphism(module_morphism)
        return U_phi * eta_S

    def hom_set_isomorphism_inverse(
        self, set_morphism: SetMorphism, codomain_module: "Module"
    ) -> "ModuleMorphism":
        r"""Inverse bijection \Psi(f) = \varepsilon_M \circ F_R(f): F_R(S) \to M."""
        F_f = self._left_adjoint._apply_functor_to_morphism(set_morphism)
        epsilon_M = self.counit(codomain_module)
        return epsilon_M * F_f
