r"""The general construction of a module over a ring.

An \(S\)-module is an object \(M\) together with a ring morphism
\(\rho:S\to\operatorname{End}(M)\); the scalar action *is* \(\rho\), by
\(s\cdot m:=\rho(s)(m)\).  Every module already has such a \(\rho\), usually
implicitly.  Making it explicit is what removes the need for a separate
parent class per ring of scalars: an \(R[G]\)-module is this construction
with \(S=R[G]\), and requires nothing new.

The codomain of \(\rho\) is a ring, so it is
\(\operatorname{End}\) taken where the additive structure lives -- in
\(R\text{-Mod}\).  Specializing which endomorphisms \(\rho\) may hit is how
extra structure is imposed: a \(G\)-action by isometries is a \(\rho\) whose
image lies in \(\operatorname{Aut}\) of the form-bearing category.  That is a
condition on \(\rho\), not a different endomorphism ring.
"""


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.structure.parent import MembershipInput, Parent
    from dzack_research.preamble.lexicon import Element
    from dzack_research.preamble.owned_category import ConstructionData
    from sage.categories.modules import Module

    # \(\rho\) is a morphism in ``Rings()``: whichever morphism class its
    # homset built, so the noun is the categorical one.
    from sage.categories.morphism import Morphism as RingMorphism

from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import Category_over_base_ring
from sage.categories.rings import Rings


class ModulesWithChosenAction(Category_over_base_ring):
    r"""Modules that carry a chosen scalar action as their datum.

    Every \(S\)-module has a ring morphism
    \(\rho:S\to\operatorname{End}(M)\); that is what makes it a module, and
    ``Modules(S)`` declares it.  An object here is built **from** \(\rho\),
    and \(M\) is read back off it.  So this states a chosen datum, not a
    property, and it is a different category from ``Modules(S)``.
    """

    def super_categories(self) -> list:
        return [Modules(self.base_ring())]

    class ParentMethods:
        # Installed by the constructor: the chosen action and the object it
        # acts on.
        _action: "RingMorphism"
        _underlying: "Module"

        def __init__(
            self,
            action: "RingMorphism",
            **rest: "ConstructionData",
        ) -> None:
            endomorphisms = action.codomain()
            assert endomorphisms in Rings(), (
                "the action of a ring lands in an endomorphism *ring*; "
                f"{endomorphisms} is not one"
            )
            assert action.domain() in Rings(), (
                f"the scalars {action.domain()} do not form a ring"
            )
            # \(\operatorname{End}(M)\) is the endset of \(M\), so it names
            # \(M\) as its own domain: the pair \((M,\rho)\) is recovered from
            # \(\rho\) alone, and passing \(M\) separately could only disagree
            # with it.
            self._underlying = endomorphisms.domain()
            self._action = action
            super().__init__(**rest)

        def _ring_morphism_defining_module_action(self) -> "RingMorphism":
            r"""Return \(\rho\), which this level carries as its datum."""
            return self._action

        def underlying_module(self) -> "Module":
            r"""Return \(M\), the object the scalars act on."""
            return self._underlying

        def action(self) -> "RingMorphism":
            r"""Return \(\rho:S\to\operatorname{End}(M)\), the scalar action."""
            return self._action

        def act(self, scalar: "Element", element: "Element") -> "Element":
            r"""Return \(s\cdot m=\rho(s)(m)\)."""
            assert scalar in self.base_ring(), (
                f"{scalar} is not a scalar of {self.base_ring()}"
            )
            return self._action(scalar)(element)

        def _element_constructor_(self, value: "Element") -> "Element":
            r"""Return ``value`` as an element.

            The underlying set is \(U(M)\) unchanged: remembering that more
            scalars act does not replace the elements, so nothing is wrapped.
            """
            return self._underlying(value)

        def __contains__(self, value: "MembershipInput") -> bool:
            return value in self._underlying

        def zero(self) -> "Element":
            r"""Return \(0\), the zero of this module.

            \(0\cdot m=0\) for every \(m\), so \(\rho(0)\) is the constant map
            at it and any element serves as the argument.  Asking \(M\) for a
            ``zero`` instead would demand additive notation of an underlying
            object that need not use it: a multiplicative abelian group writes
            the same element ``1``.
            """
            return self._action(self.base_ring().zero())(
                self._underlying.an_element()
            )

        def __hash__(self) -> int:
            # Equality compares \(\rho\), but a morphism need not be hashable
            # -- two actions agreeing on all of \(S\) is not a question a hash
            # can ask.  So the hash uses the coarser invariant \(M\), which
            # equal modules must share, and equality does the exact
            # comparison.  Two different actions on one \(M\) collide, which
            # is legal.
            return hash((type(self), self._underlying))

        def __eq__(self, other: "MembershipInput") -> bool:
            return (
                type(other) is type(self)
                and self._underlying == other._underlying
                and self._action == other._action
            )

        def _repr_(self) -> str:
            return f"{self._underlying} as a module over {self.base_ring()}"


def module_over_ring(action: "RingMorphism") -> "Parent":
    r"""Return the \(S\)-module carried by \(\rho:S\to\operatorname{End}(M)\)."""
    # Local: at module level this closes an import cycle; the ring module is
    # built by the time an action is constructed.
    from dzack_research.preamble.categories.rings.rings import engine_ring

    # Intake: the module is built over the ring the engine computes in,
    # whichever of the two names for it \(\rho\) was written with.
    # ``base_ring`` reports the name back.
    scalars = engine_ring(action.domain())
    return object_of(ModulesWithChosenAction(scalars), action=action)
