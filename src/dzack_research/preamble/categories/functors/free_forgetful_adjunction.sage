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

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.groups import Group
    from sage.categories.modules import Module

if TYPE_CHECKING:
    from dzack_research.preamble.categories.sets.sets import Set
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
    from sage.categories.morphism import Morphism
    from sage.rings.ring import Ring

from sage.misc.cachefunc import cached_function, cached_method
from sage.categories.functor import Functor
from sage.categories.homset import Hom
from sage.categories.modules import Modules
from sage.categories.sets_cat import Sets
from sage.misc.abstract_method import abstract_method
from sage.structure.sage_object import SageObject
from sage.categories.morphism import SetMorphism
from dzack_research.preamble.categories.sets.underlying_sets import UnderlyingSet


class ModuleAlgebraFunctor(Functor):
    r"""A functor \(\mathbf{Mod}(R)\to\mathbf{Alg}(R)\) built degreewise on a framing.

    The shared machinery of \(T\), \(\operatorname{Sym}\), \(\Lambda\) and
    \(\Gamma\): an algebra on the module's generating labels, and a morphism
    action by extending a linear lift multiplicatively in the flavor's own
    sense.  What is *not* shared is an adjunction -- only the three free
    flavors are left adjoint to the forgetful functor, so the unit lives on
    :class:`FreeAlgebraFunctor` below and nowhere here.
    """

    def __init__(self, base_ring: "Ring", construction: str) -> None:
        from dzack_research.preamble.categories.algebras.algebras import Algebras
        from dzack_research.preamble.categories.rings.rings import owned_ring_view

        self._base_ring = owned_ring_view(base_ring)
        self._construction = construction
        super().__init__(Modules(self._base_ring), Algebras(self._base_ring))

    @cached_method
    def _apply_functor(self, module: "Module") -> "Module":
        from dzack_research.preamble.categories.algebras.framed_free_algebras import AlternatingAlgebraOf
        from dzack_research.preamble.categories.algebras.framed_free_algebras import DividedPowerAlgebraOf
        from dzack_research.preamble.categories.algebras.framed_free_algebras import SymmetricAlgebraOf
        from dzack_research.preamble.categories.algebras.framed_free_algebras import TensorAlgebraOf

        constructors = {
            "tensor": TensorAlgebraOf,
            "symmetric": SymmetricAlgebraOf,
            "alternating": AlternatingAlgebraOf,
            "divided": DividedPowerAlgebraOf,
        }
        return constructors[self._construction](module)

    def _apply_functor_to_morphism(
        self,
        module_morphism: "ModuleMorphism",
    ) -> "Morphism":
        from dzack_research.preamble.categories.algebras.framed_free_algebras import PresentedFreeAlgebra
        from dzack_research.preamble.categories.algebras.framed_free_algebras import PresentedFreeAlgebraElement
        from dzack_research.preamble.categories.algebras.framed_free_algebras import alternating_extension
        from dzack_research.preamble.categories.algebras.framed_free_algebras import divided_power_extension
        from dzack_research.preamble.categories.algebras.framed_free_algebras import symmetric_extension
        from dzack_research.preamble.categories.algebras.framed_free_algebras import tensor_extension
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

        domain_module = module_morphism.domain()
        codomain_module = module_morphism.codomain()
        domain = self._apply_functor(domain_module)
        codomain = self._apply_functor(codomain_module)
        target_presentation = (
            codomain.presentation_algebra()
            if isinstance(codomain, PresentedFreeAlgebra)
            else codomain
        )
        source_frame = BasedFreeModule(
            domain_module.base_ring(),
            domain_module.module_generating_set(),
        )

        def image_in_target_presentation(label: "Element") -> "Element":
            image = module_morphism(domain_module.module_generator(label))
            return sum(
                (
                    coefficient * target_presentation.algebra_generator(target_label)
                    for coefficient, target_label in zip(
                        _coordinate_vector(image),
                        codomain_module.module_generating_set(),
                    )
                ),
                target_presentation.zero(),
            )

        linear_lift = module_homset(source_frame, target_presentation)(
            {
                label: image_in_target_presentation(label)
                for label in domain_module.module_generating_set()
            }
        )
        extensions = {
            "tensor": tensor_extension,
            "symmetric": symmetric_extension,
            "alternating": alternating_extension,
            "divided": divided_power_extension,
        }
        lifted = extensions[self._construction](linear_lift)

        def apply_to_class(element: "Element") -> "Element":
            representative = (
                element.representative()
                if isinstance(element, PresentedFreeAlgebraElement)
                else element
            )
            return codomain(lifted(representative))

        from dzack_research.preamble.categories.algebras.algebras import Algebras

        return SetMorphism(
            Hom(domain, codomain, Algebras(self._base_ring)),
            apply_to_class,
        )


class FreeAlgebraFunctor(ModuleAlgebraFunctor):
    r"""One of the three free-algebra functors on \(R\)-modules.

    \(T\), \(\operatorname{Sym}\), \(\Lambda\): each is left adjoint to the
    forgetful functor from its algebra category to \(\mathbf{Mod}(R)\), and
    the unit below is that adjunction's.  \(\Gamma\) is deliberately not
    admitted here: it is the graded dual of \(\operatorname{Sym}\), not a
    free construction, and carries no such unit -- see
    :func:`DividedPowerAlgebraFunctor`.
    """

    def __init__(self, base_ring: "Ring", construction: str) -> None:
        assert construction in ("tensor", "symmetric", "alternating"), (
            f"{construction!r} is not one of the free-algebra flavors: the "
            "divided-power algebra is not left adjoint to a forgetful "
            "functor, so it is a ModuleAlgebraFunctor without a unit"
        )
        super().__init__(base_ring, construction)

    @cached_method
    def unit(self, module: "Module") -> "ModuleMorphism":
        r"""Return the canonical map \(M\to U(A(M))\).

        This is the unit component of the free-algebra adjunction.  For a
        presented module, the defining relations vanish in ``A(M)``, so the
        same formula on generators descends from the chosen presentation.
        """
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

        algebra = self._apply_functor(module)
        return module_homset(module, algebra)(
            {
                label: algebra.algebra_generator(label)
                for label in module.module_generating_set()
            }
        )


@cached_function
def _free_algebra_functor(base_ring: "Ring", construction: str) -> FreeAlgebraFunctor:
    return FreeAlgebraFunctor(base_ring, construction)


def TensorAlgebraFunctor(base_ring: "Ring") -> FreeAlgebraFunctor:
    return _free_algebra_functor(base_ring, "tensor")


def SymmetricAlgebraFunctor(base_ring: "Ring") -> FreeAlgebraFunctor:
    return _free_algebra_functor(base_ring, "symmetric")


def AlternatingAlgebraFunctor(base_ring: "Ring") -> FreeAlgebraFunctor:
    return _free_algebra_functor(base_ring, "alternating")


@cached_function
def DividedPowerAlgebraFunctor(base_ring: "Ring") -> ModuleAlgebraFunctor:
    r"""Return \(\Gamma:\mathbf{Mod}(R)\to\mathbf{Alg}(R)\), the divided-power algebra functor.

    A functor, not a free construction: \(\Gamma\) is the graded dual of
    \(\operatorname{Sym}\), coinciding with it only in characteristic
    \(0\), and is not left adjoint to any forgetful functor to modules --
    so it shares the object and morphism actions of the algebra functors
    and carries no adjunction unit.
    """
    return ModuleAlgebraFunctor(base_ring, "divided")


class FreeModuleFunctorClass(Functor):
    r"""The free module functor F_R: Set -> Mod_R."""

    def __init__(self, base_ring: "Ring") -> None:
        # Local: importing the ring node here would close a cycle, and the
        # module is built by the time this constructor runs.
        from dzack_research.preamble.categories.rings.rings import owned_ring_view

        # Intake, as for any construction over a ring: the codomain named
        # below is a category over this ring, and Sage checks membership in
        # it on every application -- by base-ring identity, so the name here
        # has to be the one the modules themselves report.
        base_ring = owned_ring_view(base_ring)
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
        # Local: the free-module node imports this module, so a module-level
        # import would close that cycle; it is built by call time.
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreeModuleOnSet

        return FreeModuleOnSet(self._base_ring, set_object)

    def _apply_functor_to_morphism(self, set_morphism: Morphism) -> "Morphism":
        r"""Apply F_R to a set morphism f: S -> T, producing F_R(f): F_R(S) -> F_R(T)."""
        domain_free = self._apply_functor(set_morphism.domain())
        codomain_free = self._apply_functor(set_morphism.codomain())
        # ``_call_`` and not ``__call__``: the labels come out of the domain
        # already, and a facade set has no conversion to put them back
        # through.  This is the spelling the rest of the preamble uses when
        # applying a set morphism to its own elements.
        mapping = {
            s: codomain_free.module_generator(set_morphism._call_(s))
            for s in set_morphism.domain()
        }
        free_morphism: "Morphism" = domain_free.Hom(codomain_free)(mapping)
        return free_morphism


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

        # Local: importing the ring node here would close a cycle, and the
        # module is built by the time this constructor runs.
        from dzack_research.preamble.categories.rings.rings import owned_ring_view

        base_ring = owned_ring_view(base_ring)
        self._base_ring = base_ring
        super().__init__(Groups(), Rings())

    def base_ring(self) -> "Ring":
        return self._base_ring

    @cached_method
    def _apply_functor(self, group: "Group") -> "Ring":
        from sage.algebras.group_algebra import GroupAlgebra

        # Local: the algebra and ring nodes import this module, so
        # module-level imports would close those cycles.
        from dzack_research.preamble.categories.algebras.algebras import own_algebra
        from dzack_research.preamble.categories.rings.rings import engine_ring

        # Sage's group algebra is the engine's construction: it is built over
        # the ring the engine computes in, not over the session's name.  What
        # leaves the functor is the owned algebra it presents, because an
        # \(R\)-algebra *is* the ring map \(R\to R[G]\), and because the
        # session asked for \(R[G]\) over the \(R\) it named -- an object of
        # this functor's codomain answers with the base ring it was built on.
        #
        # Owned and not refined.  Sage computes in ``GroupAlgebra`` through
        # its category, which is over the engine's ring; joining a second
        # algebra-over-a-base-ring node onto it leaves the scalar action with
        # two bases to choose between, and the products stop resolving.
        base_ring = engine_ring(self._base_ring)
        # The functor names its source: a refined group is a semigroup under
        # more than one operation, and the group ring is the one over the
        # group law -- exactly the disambiguation the docstring promises.
        from sage.categories.groups import Groups as SageGroupsCategory

        # ``S.algebra(R, category=...)`` is the disambiguated spelling Sage
        # itself names; the functor is still the public surface.
        algebra = group.algebra(base_ring, category=SageGroupsCategory())
        return own_algebra(algebra.coerce_map_from(base_ring))


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

        # Local: importing the ring node here would close a cycle, and the
        # module is built by the time this constructor runs.
        from dzack_research.preamble.categories.rings.rings import owned_ring_view

        base_ring = owned_ring_view(base_ring)
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

    def __init__(self, base_ring: "Ring") -> None:
        # Local: importing the ring node here would close a cycle, and the
        # module is built by the time this constructor runs.
        from dzack_research.preamble.categories.rings.rings import owned_ring_view

        base_ring = owned_ring_view(base_ring)
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

    def __init__(self, left_adjoint: Functor, right_adjoint: Functor) -> None:
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

    def __init__(self, base_ring: "Ring") -> None:
        # Local: importing the ring node here would close a cycle, and the
        # module is built by the time this constructor runs.
        from dzack_research.preamble.categories.rings.rings import owned_ring_view

        base_ring = owned_ring_view(base_ring)
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
        counit_morphism: "Morphism" = free_mod.Hom(module_object)(mapping)
        return counit_morphism

    def hom_set_isomorphism_forward(self, module_morphism: "ModuleMorphism") -> SetMorphism:
        r"""Forward bijection \Phi(\phi) = U(\phi) \circ \eta_S: S \to U(M)."""
        domain_free = module_morphism.domain()
        set_object = domain_free.module_generating_set()
        eta_S = self.unit(set_object)
        U_phi = self._right_adjoint._apply_functor_to_morphism(module_morphism)
        transposed = U_phi * eta_S
        assert isinstance(transposed, SetMorphism), (
            "the transpose of a module morphism is a map of sets"
        )
        return transposed

    def hom_set_isomorphism_inverse(
        self, set_morphism: SetMorphism, codomain_module: "Module"
    ) -> "ModuleMorphism":
        r"""Inverse bijection \Psi(f) = \varepsilon_M \circ F_R(f): F_R(S) \to M."""
        F_f = self._left_adjoint._apply_functor_to_morphism(set_morphism)
        epsilon_M = self.counit(codomain_module)
        return epsilon_M * F_f
