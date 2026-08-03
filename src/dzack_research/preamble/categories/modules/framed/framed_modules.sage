r"""Modules equipped with a chosen generating morphism.

A framing of an \(R\)-module \(M\) is a surjection

\[
    \phi:F_R(S)\longrightarrow M
\]

for a set \(S\).  The morphism, not a cached list of its values, is the extra
datum.  No finiteness, countability, or orderability hypothesis is imposed on
\(S\).
"""

from typing import Any

import sage.categories.category_with_axiom as cwa
from sage.categories.category_types import Category_module
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.modules import Modules
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.sets.image_set import ImageSubobject


if "Framed" not in cwa.all_axioms:
    cwa.all_axioms.add("Framed")


def _finite_generator_assignment(
    module: Any,
    images: list | tuple,
    codomain: Any,
) -> tuple[Any, dict]:
    r"""Return the codomain and finite generator assignment."""
    images = tuple(images)
    assert len(images) == module.ngens(), (
        f"{module} has {module.ngens()} generators, got {len(images)} images"
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
            module.generating_set(),
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
        def generator_morphism(self):
            r"""Return the set morphism \(S\to U(M)\) supplied by the framing."""
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
            return framing.generator_morphism()

        def generating_set(self):
            r"""Return the domain \(S\) of the distinguished-generator morphism."""
            return self.generator_morphism().domain()

        def module_generator(self, element_of_S: Any):
            r"""Return the distinguished module generator associated to \(s\in S\)."""
            return self.generator_morphism()._call_(element_of_S)

        generator = module_generator

        def module_generators(self) -> tuple:
            r"""Return the framed generators as an iterable set.

            For general framed modules this may be infinite, so the result is not
            coerced to a tuple.
            """
            return ImageSubobject(
                self.generator_morphism(),
                self.generating_set(),
            )

        def Hom(self, codomain: Any, *args: Any, **kwargs: Any):
            r"""Return the canonical homset from this module to ``codomain``."""
            if hasattr(codomain, "base_ring") and getattr(codomain, "base_ring")() == self.base_ring():
                return module_homset(self, codomain)
            return Parent.Hom(self, codomain, *args, **kwargs)

        def is_framed(self: Any) -> bool:
            return True


@cached_method
def _framed_subcategory(self):
    return self._with_axiom("Framed")


setattr(Modules, "Framed", FramedModules)
setattr(Category_module, "Framed", _framed_subcategory)
