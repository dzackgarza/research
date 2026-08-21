r"""Restriction along the augmentation \(\varepsilon:\mathbb Z[G]\to\mathbb Z\).

\(\varepsilon^*:\mathrm{Lat}\to\mathrm{Lat}_G\) equips a lattice with the
trivial action.  It is a functor, unlike ``with_action``: a chosen
\(\rho:G\to O(L)\) belongs to one \(L\) and says nothing about any other,
whereas the trivial action is defined on every lattice at once and carries
every lattice map to an equivariant one.

Its adjoints are what make the invariant and coinvariant lattices mean
something:

\[
    (-)_G \dashv \varepsilon^* \dashv (-)^G
\]

so \(L^G\) is not merely a sublattice that happens to be fixed -- it is the
value of the right adjoint, and
\(\operatorname{Hom}_{\mathrm{Lat}_G}(\varepsilon^*N,(L,\rho))
=\operatorname{Hom}_{\mathrm{Lat}}(N,L^G)\) is why every equivariant map out
of a trivial \(G\)-lattice lands in it.
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.groups import Group
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
    from sage.categories.modules import Module
    from sage.categories.morphism import Morphism
    from sage.rings.ring import Ring

from dzack_research.preamble.categories.modules.group_modules.group_lattices import GroupLattices
from dzack_research.preamble.categories.modules.group_modules.group_modules import GroupModules
from dzack_research.preamble.categories.modules.framed.formed.integrallattice.integral_lattices import IntegralLattices
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import group_action_homset
from dzack_research.preamble.categories.modules.group_modules.group_lattices import group_lattice
from sage.misc.cachefunc import cached_function
from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from dzack_research.preamble.categories.abstract_categories.functors import Functor


class GroupModuleForgetfulFunctor(Functor):
    r"""The faithful functor \(U:R[G]\text{-Mod}\to R\text{-Mod}\).

    A group module is constructed through the module category.  Removing the
    chosen \(G\)-action therefore changes neither the object nor its module
    morphisms.  It changes only the category in which they are read.
    """

    _faithful = True

    def __init__(self, base_ring: "Ring", group: "Group") -> None:
        from dzack_research.preamble.categories.rings.rings import owned_ring_view

        base_ring = owned_ring_view(base_ring)
        Functor.__init__(self, GroupModules(base_ring, group), Modules(base_ring))

    def _apply_functor(self, group_module: "Module") -> "Module":
        return group_module

    def _apply_functor_to_morphism(self, morphism: "Morphism") -> "Morphism":
        return morphism


@cached_function
def group_module_forgetful_functor(
    base_ring: "Ring", group: "Group"
) -> GroupModuleForgetfulFunctor:
    r"""Return the canonical \(R[G]\text{-Mod}\to R\text{-Mod}\) functor."""
    return GroupModuleForgetfulFunctor(base_ring, group)


class TrivialActionFunctor(Functor):
    r"""\(\varepsilon^*:\mathrm{Lat}\to\mathrm{Lat}_G\) for one group \(G\)."""

    def __init__(self, group: "Group") -> None:
        self._group = group
        Functor.__init__(self, IntegralLattices(SageZZ), GroupLattices(group))

    def group(self) -> "Group":
        return self._group

    @cached_method
    def _apply_functor(self, lattice: "FormModule") -> "FormModule":
        r"""Return \((L,\mathbf 1)\), the same object on every call.

        Cached because a functor is well defined on objects:
        \(\varepsilon^*(\operatorname{dom}f)\) has to *be* the domain of
        \(\varepsilon^*(f)\).
        """
        identity = lattice.Aut().one()
        group_elements = (
            tuple(self._group)
            if self._group.is_finite()
            else tuple(self._group.group_generators())
        )
        return group_lattice(
            lattice,
            group_action_homset(self._group, lattice)(
                {element: identity for element in group_elements}
            ),
        )

    def _apply_functor_to_morphism(self, morphism: "Morphism") -> "Morphism":
        r"""Return \(\varepsilon^*(f)\): the same map, now equivariant.

        Equivariance is free on both sides -- \(f(1\cdot x)=1\cdot f(x)\) --
        which is the content of \(\varepsilon^*\) being defined at all.
        """
        domain = morphism.domain()
        codomain = self(morphism.codomain())
        return self(domain).Hom(codomain)(
            {
                label: codomain._from_coordinates(
                    morphism(domain.module_generator(label))._coordinates()
                )
                for label in domain.module_generating_set()
            }
        )

    def _repr_(self) -> str:
        return f"The functor equipping a lattice with the trivial {self._group}-action"


@cached_function
def trivial_action(group: "Group") -> TrivialActionFunctor:
    r"""Return \(\varepsilon^*\), the same functor on every call for one \(G\)."""
    return TrivialActionFunctor(group)
