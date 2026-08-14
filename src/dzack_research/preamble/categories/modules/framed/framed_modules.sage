r"""Modules equipped with a chosen generating morphism.

A framing of an \(R\)-module \(M\) is a surjection

\[
    \phi:F_R(S)\longrightarrow M
\]

for a set \(S\).  The morphism, not a cached list of its values, is the extra
datum.  No finiteness, countability, or orderability hypothesis is imposed on
\(S\).
"""

from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Element
    from dzack_research.preamble.lexicon import Module
    from dzack_research.preamble.lexicon import ModuleElement

from sage.categories.morphism import SetMorphism
from sage.structure.element import Element
from sage.structure.parent import Parent
if TYPE_CHECKING:
    from sage.categories.category import Category
    from sage.categories.homset import Homset
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import FramingMorphism
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleHomset

from collections.abc import Iterable
from typing import Any, Self, TYPE_CHECKING, TypeVar

from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.sets.image_set import ImageSubobject

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet


if TYPE_CHECKING:
    # The mathematical ``Set`` noun must not bind at runtime: these files
    # load into one shared namespace where Sage's ``Set()`` constructor
    # lives under the same name.
    from dzack_research.preamble.lexicon import Set


def _finite_coefficient_function(module: "Module", coefficients: Iterable) -> dict:
    r"""Pair a coordinate vector with the module's ordered generating set."""
    ordered_coefficients = tuple(coefficients)
    assert len(ordered_coefficients) == module.number_of_module_generators(), (
        f"{module} has {module.number_of_module_generators()} generators, got "
        f"{len(ordered_coefficients)} coefficients"
    )
    return dict(
        zip(
            module.module_generating_set(),
            ordered_coefficients,
            strict=True,
        )
    )


def _finite_module_generator_assignment(
    module: "Module",
    images: list | tuple,
    codomain: "Module",
) -> tuple[Any, dict]:
    r"""Return the codomain and finite generator assignment."""
    images = tuple(images)
    assert len(images) == module.number_of_module_generators(), (
        f"{module} has {module.number_of_module_generators()} generators, got {len(images)} images"
    )
    match images:
        case (first, *_):
            target = first.parent()
        case ():
            assert codomain is not None, (
                "an empty generator assignment requires its codomain"
            )
            target = codomain
    return target, dict(
        zip(
            module.module_generating_set(),
            images,
            strict=True,
        )
    )


if TYPE_CHECKING:
    class FramedModuleParent(Protocol):
        r"""What a parent placed in ``FramedModules(R)`` supplies: the ring
        underneath, its zero, the framing, and the generator naming behind the
        preparser's ``M.<e,f> = ...`` protocol."""

        def base_ring(self) -> "Ring": ...
        def zero(self) -> "ModuleElement": ...
        def variable_names(self) -> tuple[str, ...]: ...
        def framing_morphism(self) -> "FramingMorphism": ...
        def module_generator_morphism(self) -> SetMorphism: ...
        def module_generators(self) -> "OrderedSet": ...
        def module_generator(self, label: "Element") -> "ModuleElement": ...
        def module_generating_set(self) -> "OrderedSet": ...
        def subobject_on(self, module_generators: "OrderedSet") -> "Subobject": ...

    class FramedModule(Parent, FramedModuleParent):
        r"""A nominal parent carrying the framed module interface."""

    _D = TypeVar("_D", bound=Parent)
    _C = TypeVar("_C", bound=Parent)



# ``ParentMethods`` methods run on parents, but a bare methods class has no
# base to say so, and ``Parent.Hom``'s fallback branch needs nominal
# parenthood.  Runtime-identical: a bare class already derives from object.
if TYPE_CHECKING:
    _ParentBase = Parent
else:
    _ParentBase = object

class FramedModules(OwnedCategoryOverBaseRing):
    r"""Modules carrying a specified surjection \(F_R(S)\to M\)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "framed modules"

    def super_categories(self) -> list:
        r"""A framed module is a module, in the sense this preamble owns.

        Which is where the obligation lives: a module is a ring morphism
        $\rho:R\to\operatorname{End}(M)$, and saying the framed ones are
        modules is what puts that requirement on everything built here.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.pure.modules import Modules as OwnedModules

        return [OwnedModules(self.base_ring())]

    class ParentMethods(_ParentBase):
        @abstract_method
        def framing_morphism(self) -> "FramingMorphism":
            r"""Return the framing morphism \(F_R(S)\to M\)."""

        @cached_method
        def module_generator_morphism(self) -> "SetMorphism":
            r"""Return the set morphism \(S\to U(M)\) that frames \(M\) as a module.

            For a module the framing is the module framing, so this reads the
            framing morphism itself.  An object framed twice -- a free algebra,
            framed as an algebra by \(S\) and as a module by
            \(\operatorname{Mon}(S)\) -- says which one is the module framing
            by overriding this.
            """
            # Local: at module level these close an import cycle; both modules
            # are built by the time a framed module is asked for its framing.
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import FramingMorphism
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

            framing = self.framing_morphism()
            assert isinstance(framing, FramingMorphism), (
                "the Framed axiom is witnessed by a declared epimorphism"
            )
            assert framing.codomain() is self, (
                "the stored framing morphism does not land in this module"
            )
            source = framing.domain()
            assert source in FramedFreeModules(self.base_ring()), (
                "the source of a framing morphism is a free module on a set"
            )
            assert framing.parent() is module_homset(source, self), (
                "the framing morphism belongs to a noncanonical homset"
            )
            generator_morphism: "SetMorphism" = framing.module_generator_morphism()
            return generator_morphism

        def _ring_morphism_defining_module_action(self: "FramedModuleParent") -> "Morphism":
            r"""Return $\\rho:R\\to\\operatorname{End}(M)$, read off the framing.

            A framed module has generators, and scaling them is the action:
            $\\rho(r)$ sends each generator $g$ to $r\\cdot g$.  It descends
            through a presentation because the relations are $R$-linear, so
            nothing below this level has to be handed an action -- being
            framed is already enough to have one.
            """
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
            from sage.categories.homset import Hom
            from sage.categories.morphism import SetMorphism
            from sage.categories.rings import Rings

            endomorphisms = module_homset(self, self)
            return SetMorphism(
                Hom(self.base_ring(), endomorphisms, Rings()),
                lambda scalar: endomorphisms(
                    {
                        label: scalar * self.module_generator(label)
                        for label in self.module_generating_set()
                    }
                ),
            )

        def module_generating_set(self) -> "OrderedSet":
            r"""Return the domain \(S\) of the distinguished module-generator morphism."""
            return self.module_generator_morphism().domain()


        def module_generator(self, element_of_S: "Element") -> "ModuleElement":
            r"""Return the distinguished module generator associated to \(s\in S\)."""
            return self.module_generator_morphism()._call_(element_of_S)

        def module_generators(self) -> "Set":
            r"""Return the framed generators as a mathematical set.

            For general framed modules this may be infinite, so the result is
            Sage's ``ImageSubobject`` set, not a coerced tuple.
            """
            return ImageSubobject(
                    self.module_generator_morphism(),
                    self.module_generating_set(),
                )

        def inject_variables(self: "FramedModuleParent", scope: object = None, verbose: bool = True) -> None:
            r"""Bind this module's named generators into ``scope``.

            Sage's version of this method zips ``variable_names()`` against
            ``gens()``, and ``gens`` is a name a framed module does not answer
            to -- its generators are ``module_generators``.  So the inherited
            method fails on every object in this category, and the call sites
            that wanted it were writing the zip out by hand.  Said in the
            module's own nouns it is the same act, and one the object
            supports.

            ``scope`` is required.  Sage's optional form falls back to the
            ``globals()`` of the module the method is defined in, which is
            never the namespace the caller meant.
            """
            assert isinstance(scope, dict), (
                "``scope`` is required: Sage's optional form falls back to the "
                "globals() of the module this method is defined in, which is "
                "never the namespace the caller meant"
            )
            names = tuple(self.variable_names())
            generators = tuple(self.module_generators())
            assert len(names) == len(generators), (
                f"{self} has {len(names)} names for {len(generators)} "
                "generators, so the naming does not describe this module"
            )
            if verbose:
                print("Defining %s" % (", ".join(names)))
            scope.update(zip(names, generators, strict=True))

        def linear_combination(self: "FramedModuleParent", coefficients: dict) -> "ModuleElement":
            r"""Return the specified finite \(R\)-linear combination."""
            assert isinstance(coefficients, dict), (
                "a finite linear combination is specified by its coefficient "
                "function on the generating set"
            )
            return sum(
                (
                    self.base_ring()(coefficient)
                    * self.module_generator(element_of_S)
                    for element_of_S, coefficient in coefficients.items()
                ),
                self.zero(),
            )

        def subobject_on(self: "FramedModuleParent", module_generators: "OrderedSet") -> "Subobject":
            r"""Return the subobject generated by finitely many elements.

            Finite input has finite combined support in the framing.  The
            containing module need not have a finite generating set.
            """
            if "_form" in self.__dict__:
                # A formed parent's subobjects carry the restricted form,
                # and the formed category owns that construction.  Said
                # explicitly: which mixin wins the name must not decide
                # whether a sublattice is a lattice.
                # Local: a module-level import here would close a cycle; by call time this module is built.
                from dzack_research.preamble.categories.modules.framed.formed.form_modules import FreeFormModules

                return FreeFormModules.ParentMethods.subobject_on(self, module_generators)
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _independent_module_generators
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set

            module_generators = tuple(module_generators)
            assert all(
                isinstance(generator, Element) and generator.parent() is self
                for generator in module_generators
            ), "a subobject is generated by elements of this module"
            independent = _independent_module_generators(self, module_generators)
            labels = finite_ordered_set(independent)
            source = BasedFreeModule(self.base_ring(), labels)
            inclusion = module_homset(source, self)(
                {generator: generator for generator in independent}
            )
            return Subobject(inclusion)

        def submodule(self: "FramedModuleParent", module_generators: "OrderedSet") -> "Subobject":
            r"""Return the submodule generated by finitely many elements."""
            return self.subobject_on(module_generators)

        def Hom(self: _D, codomain: _C, category: "Category | None" = None) -> "Homset":
            r"""Return the canonical homset from this module to ``codomain``."""
            # Local: at module level this closes an import cycle; the homset
            # module is built by the time a homset is asked for.
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

            if codomain in FramedModules(self.base_ring()):
                homset: "ModuleHomset[_D, _C]" = module_homset(
                    self, codomain
                )
                return homset
            return Parent.Hom(self, codomain, category)

        def is_framed(self: "FramedModuleParent") -> bool:
            return True

        def vector_space(self: "FramedModuleParent") -> "Module":
            r"""Return \(M\otimes_R\operatorname{Frac}(R)\).

            The vector space of a module is its rationalization, and the
            rationalization is base change along
            \(R\hookrightarrow\operatorname{Frac}(R)\).  A module carrying a
            form arrives carrying it: the form is transported by the same
            ring map, so a lattice becomes the quadratic space over
            \(\operatorname{Frac}(R)\) spanned by it.
            """
            # Local: at module level this closes an import cycle; the base
            # change functor is built by the time a module is rationalized.
            from dzack_research.preamble.categories.functors.base_change_adjunction import fraction_field_base_change

            return fraction_field_base_change(self.base_ring())(self)
