r"""Base change and restriction of scalars along a ring morphism.

For \(f:R\to S\) there are two functors between module categories:

- **base change** \(F=-\otimes_RS:\mathbf{Mod}(R)\to\mathbf{Mod}(S)\);
- **restriction of scalars** \(G:\mathbf{Mod}(S)\to\mathbf{Mod}(R)\), reading
  an \(S\)-module over \(R\) through \(f\).

\(F\dashv G\).  Neither is an endofunctor, and neither is invertible.

Getting the adjunction's direction right is what makes the unit statable.
\(F(M)=M\otimes_RS\) is an \(S\)-module, so \(M\to F(M)\) is not a morphism in
either category: its source lives in \(\mathbf{Mod}(R)\) and its target in
\(\mathbf{Mod}(S)\).  The unit is
\(\eta_M:M\to G(F(M))\), whose codomain is \(M\otimes_RS\) *restricted back to
\(R\)* -- that restriction is exactly what makes source and target comparable.
The counit is \(\varepsilon_N:F(G(N))\to N\) in \(\mathbf{Mod}(S)\).

Restriction is not an inverse: \(G(F(L))\) for a lattice \(L\) is
\(L\otimes\mathbb Q\) read additively over \(\mathbb Z\), not \(L\).  Getting
a lattice back requires choosing one inside its rational span, which is what
saturation does.
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.modules import Module
    from sage.structure.parent import MembershipInput

from dzack_research.preamble.lexicon import Element

from sage.categories.modules import Modules
if TYPE_CHECKING:
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
    from dzack_research.preamble.owned_category import ConstructionData
    from sage.categories.morphism import Morphism
    from sage.rings.ring import Ring

from dzack_research.preamble.categories.functors.free_forgetful_adjunction import Adjunction
from dzack_research.preamble.categories.abstract_categories.functors import Functor
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import Category_over_base_ring


class BaseChangeFunctor(Functor):
    r"""\(-\otimes_RS:\mathbf{Mod}(R)\to\mathbf{Mod}(S)\) along \(f:R\to S\)."""

    def __init__(self, ring_map: "Morphism") -> None:
        self._ring_map = ring_map
        Functor.__init__(
            self, Modules(ring_map.domain()), Modules(ring_map.codomain())
        )

    def ring_map(self) -> "Morphism":
        return self._ring_map

    def _apply_functor(self, module: "Module") -> "Module":
        r"""Return \(M\otimes_RS\).

        A free module base-changes to the free module on the same framing
        set: the generators do not move, only the ring they are combined
        over does.  A form module base-changes with its form: the pairing of
        two generators is the entry \(f\) carries into \(S\), so the Gram
        matrix is the same matrix read there.
        """
        # Local: the module nodes import this module, so module-level imports
        # here would close those cycles; they are built by call time.
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModule
        from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModules
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules

        base_ring = module.base_ring()
        formed = module in FormModules(base_ring)
        underlying = module.forget_form() if formed else module
        assert underlying in FramedFreeModules(base_ring), (
            f"{module} is not free on its framing, and base change is "
            "computed here by carrying that framing over to S. A module "
            "with relations base-changes to the cokernel of its relations "
            "read over S, which this does not compute."
        )
        changed = BasedFreeModule(
            self._ring_map.codomain(), module.module_generating_set()
        )
        if not formed:
            return changed
        return FormModule(module.form().base_changed(changed))

    def _apply_functor_to_morphism(self, morphism: "ModuleMorphism") -> "ModuleMorphism":
        r"""Return \(f\otimes S\), the same matrix read over \(S\)."""
        # Local: the morphism node imports this module, so a module-level
        # import would close that cycle; it is built by call time.
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
        from dzack_research.preamble.utilities import zipsum

        source, target = self(morphism.domain()), self(morphism.codomain())
        return module_homset(source, target)(
            {
                label: zipsum(
                    row, target.module_generators(), target.zero()
                )
                for label, row in zip(
                    source.module_generating_set(),
                    morphism.matrix().change_ring(self._ring_map.codomain()).rows(),
                )
            }
        )

    def _repr_(self) -> str:
        return f"Base change along {self._ring_map}"


def fraction_field_base_change(base_ring: "Ring") -> BaseChangeFunctor:
    r"""Return \(-\otimes_R\operatorname{Frac}(R)\), the rationalization functor.

    Rationalizing an \(R\)-module is base change and nothing else, so it is
    built as base change: the ring map is the inclusion
    \(R\hookrightarrow\operatorname{Frac}(R)\), an actual morphism of the two
    rings a session names, and the functor is the one this file already
    defines along it.

    The hypothesis is the one that makes the inclusion an inclusion.  An
    integral domain embeds in its field of fractions by \(r\mapsto r/1\);
    without the hypothesis there is no field of fractions to embed in, and
    "the vector space of \(M\)" names nothing.
    """
    # Local: importing the ring node here would close a cycle, and the module
    # is built by the time this function runs.
    from dzack_research.preamble.categories.rings.rings import engine_ring
    from dzack_research.preamble.categories.rings.rings import own_ring

    ring = own_ring(engine_ring(base_ring))
    assert ring.is_integral_domain(), (
        f"{ring} is not an integral domain, so it has no field of fractions "
        "and no module over it has a rationalization"
    )
    fraction_field = ring.fraction_field()
    return BaseChangeFunctor(fraction_field.coerce_map_from(ring))


class RestrictedScalarsModules(Category_over_base_ring):
    r"""The \(S\)-modules read as \(R\)-modules through \(f:R\to S\).

    The restriction of scalars of \(N\) is \(N\) itself as an additive group,
    with the action \(\rho_N\circ f\): the datum that *is* an \(R\)-module is
    the ring morphism \(R\to\operatorname{End}(N)\), and composing \(\rho_N\)
    with \(f\) is the whole construction.  The elements do not move, so the
    object is a facade over \(N\), the way ``UnderlyingSet`` realizes the
    other forgetful functors' object actions.

    Not free and not framed: \(N\)'s framing over \(S\) is not one over
    \(R\) unless \(S\) itself is framed free over \(R\), which
    \(\mathbb Z\hookrightarrow\mathbb Q\) already fails.  \(G(F(L))\) for a
    lattice \(L\) is \(L\otimes\mathbb Q\) read additively over
    \(\mathbb Z\) -- not finitely generated, and explicitly not \(L\).
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "restricted scalars modules"

    def super_categories(self) -> list:
        # Local: the module node imports this module, so a module-level import
        # would close that cycle; it is built by call time.
        from dzack_research.preamble.categories.modules.pure.modules import Modules as OwnedModules

        return [OwnedModules(self.base_ring())]

    class ParentMethods:
        r"""\(N\) read over \(R\), with the elements left where they are."""

        def __init__(
            self,
            module: "Module",
            ring_map: "Morphism",
            **rest: "ConstructionData",
        ) -> None:
            r"""Build \(N\) read over \(R\) through ``ring_map``."""
            self._module = module
            self._ring_map = ring_map
            super().__init__(
                base=ring_map.domain(), facade=module, **rest
            )

        def ring_map(self) -> "Morphism":
            return self._ring_map

        def module_over_extension(self) -> "Module":
            r"""The \(S\)-module this object reads over \(R\)."""
            return self._module

        def _ring_morphism_defining_module_action(self) -> "Morphism":
            r"""Return \(\rho_N\circ f:R\to\operatorname{End}(N)\), which is the module.

            \(\rho(r)\) is scaling by \(f(r)\) in \(N\): the \(S\)-action already
            present, read along the ring map.  Nothing is computed -- restriction
            of scalars *is* this composition.
            """
            from sage.categories.homset import Hom
            from sage.categories.morphism import SetMorphism
            from sage.categories.rings import Rings

            # Local: the module node imports this module, so a module-level import
            # would close that cycle; it is built by call time.
            from dzack_research.preamble.categories.modules.pure.modules import Modules as OwnedModules

            endomorphisms = Hom(self, self, OwnedModules(self._ring_map.domain()))
            return SetMorphism(
                Hom(self._ring_map.domain(), endomorphisms, Rings()),
                lambda scalar: SetMorphism(
                    endomorphisms,
                    lambda element, scalar=scalar: self._ring_map(scalar) * element,
                ),
            )

        def scalar_multiple(self, scalar: "Element", element: "Element") -> "Element":
            return self._ring_map(scalar) * element

        def _coordinate_module(self) -> "Module":
            r"""\(N\)'s coordinate module: restriction does not move coordinates."""
            return self._module._coordinate_module()

        def zero(self) -> "Element":
            return self(self._module.zero())

        def _element_constructor_(self, element: "Element") -> "Element":
            r"""Same elements as \(N\), answering to this parent.

            Restriction of scalars does not move elements, so conversion first
            runs \(N\)'s and then re-homes the result: the element's class and
            coordinates are unchanged, and only the parent it answers to is this
            restricted reading.  That identification is what makes an image
            \(g\otimes1\in F(M)\) an element *of* \(G(F(M))\), which is the
            codomain-parent equality a module morphism into this facade checks.
            """
            # Local: the module node imports this module through the functor
            # tower; it is built by call time.
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModuleElement

            member = self._module(element)
            if member.parent() is self:
                return member
            assert isinstance(member, BasedFreeModuleElement), (
                f"restriction of scalars re-homes coordinate elements; "
                f"{member!r} is not one"
            )
            reparented: "Element" = type(member)(self, member._coordinates_)
            return reparented

        def __contains__(self, element: "MembershipInput") -> bool:
            # An element already re-homed here belongs here; otherwise the
            # facade's members are exactly \(N\)'s.
            if isinstance(element, Element) and element.parent() is self:
                return True
            return element in self._module

        def _repr_(self) -> str:
            return f"{self._module} read over {self._ring_map.domain()} through {self._ring_map}"


class RestrictionOfScalarsFunctor(Functor):
    r"""\(\mathbf{Mod}(S)\to\mathbf{Mod}(R)\) along \(f:R\to S\).

    The object action lands in :class:`RestrictedScalarsModules`: the same
    module with the action read through \(f\).  A morphism restricts to itself --
    an \(S\)-linear map is \(R\)-linear for the composed action, on the same
    elements -- so the morphism action re-homes the map between the
    restricted parents without touching its values.
    """

    def __init__(self, ring_map: "Morphism") -> None:
        self._ring_map = ring_map
        Functor.__init__(
            self, Modules(ring_map.codomain()), Modules(ring_map.domain())
        )

    def ring_map(self) -> "Morphism":
        return self._ring_map

    def _apply_functor(self, module: "Module") -> "Module":
        return object_of(
            RestrictedScalarsModules(self._ring_map.domain()),
            module=module,
            ring_map=self._ring_map,
        )

    def _apply_functor_to_morphism(self, morphism: "Morphism") -> "Morphism":
        from sage.categories.homset import Hom
        from sage.categories.morphism import SetMorphism

        # Local: the module node imports this module, so a module-level import
        # would close that cycle; it is built by call time.
        from dzack_research.preamble.categories.modules.pure.modules import Modules as OwnedModules

        return SetMorphism(
            Hom(
                self(morphism.domain()),
                self(morphism.codomain()),
                OwnedModules(self._ring_map.domain()),
            ),
            morphism,
        )

    def _repr_(self) -> str:
        return f"Restriction of scalars along {self._ring_map}"


class BaseChangeAdjunction(Adjunction):
    r"""\(-\otimes_RS\dashv\) restriction of scalars."""

    def __init__(self, ring_map: "Morphism") -> None:
        self._ring_map = ring_map
        Adjunction.__init__(
            self,
            BaseChangeFunctor(ring_map),
            RestrictionOfScalarsFunctor(ring_map),
        )

    def unit(self, module: "Module") -> "ModuleMorphism":
        r"""Return \(\eta_M:M\to G(F(M))\), \(m\mapsto m\otimes 1\).

        The codomain is \(M\otimes_RS\) *restricted to \(R\)*.  Without that
        restriction there is no morphism to speak of: \(M\) is an \(R\)-module
        and \(M\otimes_RS\) is an \(S\)-module, and a map between them belongs
        to no single category.
        """
        # Local: the morphism node imports this module, so a module-level
        # import would close that cycle; it is built by call time.
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

        extended = self._left_adjoint(module)
        restricted = self._right_adjoint(extended)
        # The images are the tensor generators \(g\otimes1\), elements of
        # \(F(M)\); the restricted parent is a facade over \(F(M)\), so
        # they are its elements too, and the codomain of the arrow is the
        # restriction -- which is what makes the unit statable at all.
        return module_homset(module, restricted)(
            {
                label: extended.module_generator(label)
                for label in module.module_generating_set()
            }
        )

    # ``counit`` stays the inherited abstract declaration: a stated gap.
    # \(\varepsilon_N:F(G(N))\to N\) exists, but computing it here needs
    # \(F\) applied to \(G(N)\), and this file's \(F\) carries a framing
    # over \(R\) across the ring map -- a framing \(G(N)\) does not have,
    # since \(N\)'s framing over \(S\) is not one over \(R\).  Implementing
    # \(F\) on unframed modules is the missing capability, not a smaller
    # counit.

    def _repr_(self) -> str:
        return f"Base change adjunction along {self._ring_map}"
