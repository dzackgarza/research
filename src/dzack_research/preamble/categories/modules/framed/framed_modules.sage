r"""Modules equipped with a chosen generating morphism.

A framing of an \(R\)-module \(M\) is a surjection

\[
    \phi:F_R(S)\longrightarrow M
\]

for a set \(S\).  The morphism, not a cached list of its values, is the extra
datum.  No finiteness, countability, or orderability hypothesis is imposed on
\(S\).
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage_lattice_category_spike.lexicon import Element
    from sage_lattice_category_spike.lexicon import Module
    from sage_lattice_category_spike.lexicon import ModuleElement

from sage.categories.morphism import SetMorphism
from sage.structure.parent import Parent
if TYPE_CHECKING:
    from sage.categories.category import Category
    from sage.categories.homset import Homset
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import FramingMorphism

from typing import Any, Self, TYPE_CHECKING

import sage.categories.category_with_axiom as cwa
from sage.categories.category_types import Category_module
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.modules import Modules
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.sets.image_set import ImageSubobject

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from sage_lattice_category_spike.lexicon import OrderedSet


if TYPE_CHECKING:
    # The mathematical ``Set`` noun must not bind at runtime: these files
    # load into one shared namespace where Sage's ``Set()`` constructor
    # lives under the same name.
    from sage_lattice_category_spike.lexicon import Set


if "Framed" not in cwa.all_axioms:
    cwa.all_axioms.add("Framed")


def _finite_coefficient_function(module: "Module", coefficients: dict) -> dict:
    r"""Pair a coordinate vector with the module's ordered generating set."""
    coefficients = tuple(coefficients)
    assert len(coefficients) == module.number_of_module_generators(), (
        f"{module} has {module.number_of_module_generators()} generators, got "
        f"{len(coefficients)} coefficients"
    )
    return dict(
        zip(
            module.module_generating_set(),
            coefficients,
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


class FramedModules(CategoryWithAxiom_over_base_ring):
    r"""Modules carrying a specified surjection \(F_R(S)\to M\)."""

    _base_category_class_and_axiom = (Modules, "Framed")

    def extra_super_categories(self) -> list:
        r"""A framed module is a module, in the sense this preamble owns.

        Which is where the obligation lives: a module is a ring morphism
        $\rho:R\to\operatorname{End}(M)$, and saying the framed ones are
        modules is what puts that requirement on everything built here.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.pure.modules import Modules as OwnedModules

        return [OwnedModules(self.base_ring())]

    class ParentMethods:

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
            return framing.module_generator_morphism()

        def _ring_morphism_defining_module_action(self: Self) -> "Morphism":
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

        def inject_variables(self: Self, scope: dict, verbose: bool = True) -> None:
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
            names = tuple(self.variable_names())
            generators = tuple(self.module_generators())
            assert len(names) == len(generators), (
                f"{self} has {len(names)} names for {len(generators)} "
                "generators, so the naming does not describe this module"
            )
            if verbose:
                print("Defining %s" % (", ".join(names)))
            scope.update(zip(names, generators, strict=True))

        def linear_combination(self: Self, coefficients: dict) -> "ModuleElement":
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

        def Hom(self, codomain: "Module", category: "Category" = None) -> "Homset":
            r"""Return the canonical homset from this module to ``codomain``."""
            # Local: at module level this closes an import cycle; the homset
            # module is built by the time a homset is asked for.
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

            if codomain in Modules(self.base_ring()).Framed():
                return module_homset(self, codomain)
            return Parent.Hom(self, codomain, category)

        def is_framed(self: Self) -> bool:
            return True

        def vector_space(self: Self) -> "Module":
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


@cached_method
def _framed_subcategory(self: Self) -> "Category":
    return self._with_axiom("Framed")


setattr(Modules, "Framed", FramedModules)
setattr(Category_module, "Framed", _framed_subcategory)
