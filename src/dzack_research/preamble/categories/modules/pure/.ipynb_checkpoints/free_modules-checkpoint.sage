r"""Finitely generated free modules of finite rank with a chosen basis.

The node under everything else here.  A lattice is a form on one of these, a
discriminant form is a form on a quotient of one, and a $G$-lattice is one with
an action -- so this is where the module structure is owned rather than
borrowed from Sage's ``FreeModule``, whose elements are vectors of an ambient
space and whose submodules carry embeddings this universe does not want.

This category explicitly represents finitely generated free modules (free
modules of finite rank $n \ge 0$) over a base ring $R$, equipped with a chosen
ordered basis.

A coordinate vector *is* an element here, and that is not a hole: the basis is
part of the datum, so the coordinates mean something without anyone having to
say what.  The gating lives one level up, where a form module refuses a bare
vector because reading it as $\sum a_ig_i$ is a claim about *which* generating
set is meant.

The category is over a base ring and says nothing else.  Which rings can
actually be computed with is a question for the constructions -- an isotypic
decomposition wants $|G|$ invertible, and that is a gate on the construction,
not a smaller category.
"""

from typing import Any

from sage.categories.category_types import Category_over_base_ring
from sage.categories.modules import Modules
from sage.matrix.matrix0 import Matrix
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp


class FreeModules(Category_over_base_ring):
    r"""Category of finitely generated free modules of finite rank with a chosen basis."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "finitely generated based free modules"

    def super_categories(self) -> list:
        return [Modules(self.base_ring())]

    class ParentMethods:
        r"""What a chosen basis of a free module makes askable."""

        def is_finitely_generated(self: Any) -> bool:
            r"""Return whether this module is finitely generated.

            Always ``True``: every object in this category is a based free module
            of finite rank.
            """
            return True

        def is_free(self: Any) -> bool:
            r"""Return whether this module is free.

            Always ``True``: joining this category declares that the parent is a
            free module with a chosen basis.
            """
            return True

        def is_torsionfree(self: Any) -> bool:
            r"""Return whether this module is torsion-free."""
            return True

        def is_torsion(self: Any) -> bool:
            r"""Return whether this module is torsion."""
            return self.is_zero()

        def rank(self: Any) -> Any:
            r"""Return the number of basis elements, which is the finite rank.

            Asked of the count rather than of the basis: building the basis
            builds elements, and an element checks its length against the rank.
            """
            return ZZ(self.num_module_generators())

        def basis(self: Any) -> tuple:
            r"""Return the basis, under the name that says it is independent."""
            return self.gens()

        def linear_combination(self: Any, coefficients: Any) -> Any:
            r"""Return $\sum_i a_ie_i$.

            Shadows Sage's ``Modules.ParentMethods.linear_combination``, which
            reads its argument as ``(element, coefficient)`` pairs.  Every
            object in this universe reads a coefficient vector the way this one
            does, and one name with two meanings is worse than either.
            """
            coefficients = tuple(coefficients)
            generators = self.gens()
            assert len(coefficients) == len(generators), (
                f"this module has {len(generators)} basis elements, got "
                f"{len(coefficients)} coefficients"
            )
            total = self.zero()
            for coefficient, generator in zip(coefficients, generators):
                total += self.base_ring()(coefficient) * generator
            return total

        def is_zero(self: Any) -> bool:
            r"""Return whether this is the zero module."""
            return self.num_module_generators() == 0

        def hom(self: Any, images: Any, codomain: Any = None) -> Any:
            r"""Return the morphism sending this module's basis to ``images``."""
            images = tuple(images)
            generators = self.gens()
            assert len(images) == len(generators), (
                f"this module has {len(generators)} basis elements, got "
                f"{len(images)} images"
            )
            if not images:
                assert codomain is not None, (
                    "a morphism out of the zero module needs its codomain named"
                )
                return ModuleMorphism.zero(self, codomain)
            return ModuleMorphism(dict(zip(generators, images)))

        def Aut(self: Any) -> Any:
            r"""Return the homset of automorphisms of this module.

            An automorphism is made by naming the image of every chosen
            generator.  Its matrix is a derived coordinate reading, never an
            alternative constructor.
            """
            return ModuleAutomorphismGroup(self)

        def subobject_on(self: Any, generators: Any) -> Any:
            r"""Return the submodule these generate, as its inclusion.

            The span, on an independent generating set of it -- so what comes
            back is a free module of the right rank together with the mono
            that places it here.
            """
            generators = _independent_generators(self, generators)
            sub = BasedFreeModule(self.base_ring(), len(generators))
            return Subobject(
                ModuleMorphism.zero(sub, self)
                if not generators
                else ModuleMorphism(dict(zip(sub.gens(), generators)))
            )


class BasedFreeModuleElement(ModuleElement):
    r"""An element of a based free module: its coordinates, and nothing else."""

    def __init__(self, parent: Any, coordinates: Any) -> None:
        ModuleElement.__init__(self, parent)
        self._coordinates_ = vector(parent.base_ring(), list(coordinates))
        assert len(self._coordinates_) == parent.num_module_generators(), (
            f"{parent} has rank {parent.num_module_generators()}, got "
            f"{len(self._coordinates_)} coordinates"
        )

    def _coordinates(self) -> Any:
        r"""Return the coordinates in the parent's basis."""
        return self._coordinates_

    def _add_(self, other: Any) -> "BasedFreeModuleElement":
        return self.parent()._from_coordinates(self._coordinates_ + other._coordinates_)

    def _sub_(self, other: Any) -> "BasedFreeModuleElement":
        return self.parent()._from_coordinates(self._coordinates_ - other._coordinates_)

    def _neg_(self) -> "BasedFreeModuleElement":
        return self.parent()._from_coordinates(-self._coordinates_)

    def _lmul_(self, factor: Any) -> "BasedFreeModuleElement":
        return self.parent()._from_coordinates(
            self.parent().base_ring()(factor) * self._coordinates_
        )

    _rmul_ = _lmul_

    def _richcmp_(self, other: Any, op: int) -> bool:
        return richcmp(self._coordinates_, other._coordinates_, op)

    def __hash__(self) -> int:
        return hash(tuple(self._coordinates_))

    def __iter__(self):
        return iter(self._coordinates_)

    def _repr_(self) -> str:
        return repr(self._coordinates_)


class BasedFreeModule(Parent):
    r"""Finitely generated based free module $R^n$ of finite rank $n$ with its standard basis.

    Named for what it is rather than ``FreeModule``, which is Sage's factory
    and stays reachable: this universe's free module and Sage's are different
    objects, and shadowing the name would make which one a caller got depend on
    import order.
    """

    Element = BasedFreeModuleElement

    def __init__(self, base_ring: Any, rank: Any) -> None:
        self._rank = ZZ(rank)
        assert self._rank >= 0, f"a rank is not negative, got {rank}"
        # The category goes in at construction, not only by the refinement
        # below: Sage discovers the base ring's action on this parent while
        # initializing it, and a category arriving afterwards is too late for
        # scalar multiplication by anything but the integers.
        Parent.__init__(self, base=base_ring, category=FreeModules(base_ring))
        refine(self, FreeModules(base_ring))

    def gens(self) -> tuple:
        return tuple(
            self._from_coordinates(
                [self.base_ring()(i == j) for j in range(self._rank)]
            )
            for i in range(self._rank)
        )

    def ngens(self) -> int:
        return int(self._rank)

    def zero(self) -> BasedFreeModuleElement:
        return self._from_coordinates([self.base_ring().zero()] * self._rank)

    def _from_coordinates(self, coordinates: Any) -> BasedFreeModuleElement:
        return self.element_class(self, coordinates)

    def _element_constructor_(self, x: Any) -> BasedFreeModuleElement:
        r"""Return the element ``x`` names.

        A coordinate vector is accepted, because here it is an element: the
        basis is part of this object, so its entries already mean something.
        What is refused is an element of a *different* module, which is a map's
        business and not a constructor's.
        """
        if isinstance(x, BasedFreeModuleElement):
            assert x.parent() is self, (
                f"{x} belongs to {x.parent()}; carrying it here is a morphism's "
                "job, not a constructor's"
            )
            return x
        return self._from_coordinates(x)

    def __contains__(self, x: Any) -> bool:
        return isinstance(x, BasedFreeModuleElement) and x.parent() is self

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, BasedFreeModule)
            and other.base_ring() is self.base_ring()
            and other._rank == self._rank
        )

    def __hash__(self) -> int:
        return hash((type(self).__name__, self.base_ring(), self._rank))

    def _repr_(self) -> str:
        return f"Free module of rank {self._rank} over {self.base_ring()}"
