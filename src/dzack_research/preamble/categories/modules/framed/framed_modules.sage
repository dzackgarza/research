r"""Modules equipped with a chosen generating morphism.

A framing of an \(R\)-module \(M\) is a surjection

\[
    \phi:F_R(S)\longrightarrow M
\]

for a set \(S\).  The morphism, not a cached list of its values, is the extra
datum.  No finiteness, countability, or orderability hypothesis is imposed on
\(S\).
"""

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
            if codomain in Modules(self.base_ring()).Framed():
                return module_homset(self, codomain)
            return Parent.Hom(self, codomain, category)

        def is_framed(self: Self) -> bool:
            return True


@cached_method
def _framed_subcategory(self: Self) -> "Category":
    return self._with_axiom("Framed")


setattr(Modules, "Framed", FramedModules)
setattr(Category_module, "Framed", _framed_subcategory)
