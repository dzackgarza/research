r"""Finitely generated modules over a base ring.

Defines the ``FinitelyGenerated`` axiom for ``Modules(R)`` via Sage's ``CategoryWithAxiom_over_base_ring``
framework, enabling ``Modules(R).FinitelyGenerated()`` and ``FinitelyGeneratedModules(R)``.
"""

from typing import Protocol, TYPE_CHECKING
from dzack_research.preamble.utilities import zipsum
if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Module

if TYPE_CHECKING:
    from sage.structure.element import Matrix
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism

import sage.categories.category_with_axiom as cwa
from sage.categories.category_types import Category_module
from sage.categories.category_with_axiom import CategoryWithAxiom_over_base_ring
from sage.categories.modules import Modules
from sage.categories.principal_ideal_domains import PrincipalIdealDomains
from sage.matrix.constructor import matrix
from sage.misc.cachefunc import cached_method
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.sets.owned_sets import Sets

# Register FinitelyGenerated axiom string if not present in Sage's axiom container
if "FinitelyGenerated" not in cwa.all_axioms:
    cwa.all_axioms.add("FinitelyGenerated")


class FreeResolution(SageObject):
    r"""The complex $0\leftarrow M\leftarrow F_0\leftarrow F_1\leftarrow 0$.

    The differentials are numbered along the complex as it is written, so
    $d_1$ is the framing epimorphism $F_0\twoheadrightarrow M$ and $d_2$,
    when there is one, is the inclusion of the relation module into $F_0$.
    Numbering the augmentation is what makes a free module the specialization
    it is rather than a separate answer: a free module has no relations, the
    complex stops after $d_1$, and that one differential is an isomorphism.
    """

    def __init__(self, module: "Module") -> None:
        # Local: at module level this closes an import cycle; the ring module
        # is built by the time a resolution is asked for.
        from dzack_research.preamble.categories.rings.rings import engine_ring

        base_ring = engine_ring(module.base_ring())
        assert base_ring in PrincipalIdealDomains(), (
            "a submodule of a free module is free over a principal ideal "
            "domain, which is what stops this resolution at one relation step"
        )
        augmentation = module.framing_morphism()
        free_on_generators = augmentation.domain()
        relations = module.relation_matrix()._sage_matrix()
        # Sage resolves $F/N$ for a submodule $N\subseteq F$, so handing it
        # the relation module is handing it this module.  What comes back is
        # a basis of the relations as the columns of the first differential:
        # the reduction over the PID, done by the engine and not restated
        # here.  A free module hands over the zero submodule and the basis
        # has no columns, which is how that case is the same construction.
        relation_basis = (
            (base_ring ** relations.ncols())
            .submodule(relations.rows())
            .free_resolution()
            .matrix(1)
        )
        self._module = module
        self._differentials = (augmentation,) + _relation_inclusion(
            free_on_generators, relation_basis.columns()
        )

    def module(self) -> "Module":
        r"""Return the module this is a resolution of."""
        return self._module

    def length(self) -> int:
        r"""Return the number of differentials."""
        return len(self._differentials)

    def differential(self, index: int) -> "ModuleMorphism":
        r"""Return the ``index``-th differential, counted from $M$."""
        assert 1 <= index <= self.length(), (
            f"this resolution has differentials 1 to {self.length()}"
        )
        return self._differentials[index - 1]

    def matrix(self, index: int) -> "Matrix":
        r"""Return the matrix of the ``index``-th differential.

        A morphism's matrix here is read in the two framings with its
        domain's generators indexing the rows, so the relations of $d_2$ are
        its rows.
        """
        return matrix(self.differential(index).matrix())

    def _repr_(self) -> str:
        stages = " <-- ".join(
            f"R^{differential.domain().number_of_module_generators()}"
            for differential in self._differentials
        )
        return f"0 <-- {self._module} <-- {stages} <-- 0"


def _relation_inclusion(free_on_generators: "Module", columns: list) -> tuple:
    r"""Return the inclusion $F_1\hookrightarrow F_0$ of the relation module.

    Each column is a relation written in the generators of $F_0$.  With no
    columns there is no such morphism to return, and the resolution is one
    differential long.
    """
    if not columns:
        return ()
    # Imported here and not at the top: the framed free module is a
    # specialization of this one, so naming it at import time would close a
    # cycle.  By the time a resolution is asked for, it is built.
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
    # Local for the same reason: the homset module names this one.
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

    relation_module = BasedFreeModule(
        free_on_generators.base_ring(), Sets.Δ[len(columns) - 1]
    )
    module_generators = free_on_generators.module_generators()
    return (
        module_homset(relation_module, free_on_generators)(
            dict(
                zip(
                    relation_module.module_generating_set(),
                    (
                        zipsum(
                            column,
                            module_generators,
                            free_on_generators.zero(),
                        )
                        for column in columns
                    ),
                )
            )
        ),
    )


if TYPE_CHECKING:
    class FinitelyGeneratedModuleParent(Protocol):
        r"""What a parent placed in ``Modules(R).FinitelyGenerated()``
        supplies: the framing set, the generator naming a label, and the
        module's zero."""

        def module_generating_set(self) -> "OrderedSet": ...
        def module_generator(self, element_of_S: "Element") -> "ModuleElement": ...
        def module_generators(self) -> "OrderedSet": ...
        def zero(self) -> "ModuleElement": ...


class FinitelyGeneratedModules(CategoryWithAxiom_over_base_ring):
    r"""Category of finitely generated modules over a base ring."""

    _base_category_class_and_axiom = (Modules, "FinitelyGenerated")

    def extra_super_categories(self) -> list:
        r"""Require the chosen finite generating morphism used by this preamble."""
        # Imported for its registration of the Framed axiom on Modules, which
        # is what makes ``.Framed()`` below an attribute at all.
        from dzack_research.preamble.categories.modules.framed.framed_modules import FramedModules  # noqa: F401

        return [Modules(self.base_ring()).Framed()]

    class ParentMethods:
        def module_generators(self: "FinitelyGeneratedModuleParent") -> "OrderedSet":
            r"""Return the finite framed generators, as an ordered set.

            An ordered set, not a tuple: the generators are a set, and the
            framing is what orders them.  Owned by this module rather than
            canonical by value -- ``Free_R(S) = Free_R(S')`` when ``S = S'``,
            which makes the *index* set canonical, but two modules'
            generators can compare equal while being different generators.
            """
            cached: "OrderedSet | None" = self.__dict__.get("_preamble_module_generators")
            if cached is None:
                module_generating_set = self.module_generating_set()
                assert module_generating_set in Sets().Finite(), (
                    "module_generators() is defined only for finitely generated modules"
                )
                # Local: a module-level import here would close a cycle; by call time this module is built.
                from dzack_research.preamble.categories.sets.sets import ordered_set_owned_by
                cached = ordered_set_owned_by(
                    tuple(
                        self.module_generator(element_of_S)
                        for element_of_S in module_generating_set
                    )
                )
                self._preamble_module_generators = cached
            return cached

        def free_resolution(self: "FinitelyGeneratedModuleParent") -> FreeResolution:
            r"""Return the free resolution of this module.

            A resolution writes $M$ in free modules: $F_0$ on this module's
            generating set, $F_1$ on a basis of the relations among them, and
            $0\leftarrow M\leftarrow F_0\leftarrow F_1\leftarrow 0$ exact.
            Over a principal ideal domain the relation module is free, so
            there is nothing left to resolve after $F_1$ and the complex is
            finite -- which is the hypothesis the construction asserts.

            A free module has no relations, so $F_1$ is absent and the
            resolution is its framing isomorphism alone: a free module
            resolves in one step by the identity.  Nothing is special-cased
            to say so; the relation module is zero and the same construction
            returns one differential instead of two.
            """
            return FreeResolution(self)

        def is_finitely_generated(self: "FinitelyGeneratedModuleParent") -> bool:
            r"""Return whether the chosen generating set is finite.

            Computed from the framing rather than declared from membership:
            the ``FinitelyGenerated`` axiom gate consults this answer, so an
            object claiming the axiom with an infinite framing is refused
            rather than believed.
            """
            return self.module_generating_set() in Sets().Finite()

        def is_zero(self: "FinitelyGeneratedModuleParent") -> bool:
            r"""Return whether every element in the chosen generating set vanishes."""
            return all(
                generator == self.zero()
                for generator in self.module_generators()
            )


@cached_method
def _fg_subcategory(self: "Category") -> "Category":
    subcategory: "Category" = self._with_axiom("FinitelyGenerated")
    return subcategory


setattr(Modules, "FinitelyGenerated", FinitelyGeneratedModules)
setattr(Category_module, "FinitelyGenerated", _fg_subcategory)
