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

from sage.misc.cachefunc import cached_function
from sage.misc.cachefunc import cached_method
from sage.categories.functor import Functor


class TrivialActionFunctor(Functor):
    r"""\(\varepsilon^*:\mathrm{Lat}\to\mathrm{Lat}_G\) for one group \(G\)."""

    def __init__(self, group: "Group") -> None:
        self._group = group
        Functor.__init__(self, IntegralLattices(), GroupLattices(group))

    def group(self) -> "Group":
        return self._group

    @cached_method
    def _apply_functor(self, lattice: "Lattice") -> "Lattice":
        r"""Return \((L,\mathbf 1)\), the same object on every call.

        Cached because a functor is well defined on objects:
        \(\varepsilon^*(\operatorname{dom}f)\) has to *be* the domain of
        \(\varepsilon^*(f)\).
        """
        identity = lattice.Aut().one()
        return group_lattice(
            lattice,
            group_action_homset(self._group, lattice)(
                {element: identity for element in self._group}
            ),
        )

    def _apply_functor_to_morphism(self, morphism: "FormMorphism") -> "FormMorphism":
        r"""Return \(\varepsilon^*(f)\): the same map, now equivariant.

        Equivariance is free on both sides -- \(f(1\cdot x)=1\cdot f(x)\) --
        which is the content of \(\varepsilon^*\) being defined at all.
        """
        domain = morphism.domain()
        return self(domain).Hom(self(morphism.codomain()))(
            {
                label: self._over_lattice(
                    morphism(domain.module_generator(label))
                )
                for label in domain.module_generating_set()
            }
        )

    def _over_lattice(self, element: "Element") -> "Element":
        r"""Return ``element`` read in \(\varepsilon^*\) of its own lattice."""
        return self(element.parent())._over_forgotten(element)

    def _repr_(self) -> str:
        return f"The functor equipping a lattice with the trivial {self._group}-action"


@cached_function
def trivial_action(group: "Group") -> TrivialActionFunctor:
    r"""Return \(\varepsilon^*\), the same functor on every call for one \(G\)."""
    return TrivialActionFunctor(group)
