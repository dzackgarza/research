r"""Free algebras over a base ring, without a chosen generating set."""

from typing import Protocol, TYPE_CHECKING

from sage.categories.category import Category
from sage.structure.parent import Parent

from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.sets.owned_sets import Sets

if TYPE_CHECKING:
    from dzack_research.preamble.categories.algebras.framed_free_algebras import (
        MonomialSystem,
    )
    from dzack_research.preamble.lexicon import Element
    from dzack_research.preamble.lexicon import OrderedSet

    # What these categories require of the objects they are about.  Sage
    # binds ``ParentMethods`` onto a parent and ``SubcategoryMethods`` onto a
    # category by COPYING the methods into a dynamic class, so the object a
    # method runs on is never an instance of the class the method is written
    # in: ``self`` is annotated with what its placement gives it.

    class GradedFreeAlgebraParent(Protocol):
        r"""A parent in these categories, read through its monomials.

        Everything below is off the framing -- what a monomial is, and which
        element of the algebra it names -- so these are the operations the
        graded surface is written against.
        """

        def base_ring(self) -> "Ring": ...
        def algebra_generating_set(self) -> "OrderedSet": ...
        def monomial_system(self) -> "MonomialSystem": ...
        def module_generator(self, monomial: "Element") -> "Element": ...
        def degree_on_module_generator(
            self, module_generator: "Element"
        ) -> "Integer": ...
        def graded_piece_monomials(
            self, degree: "Integer | int"
        ) -> "Set | tuple": ...

    class DividedPowerAlgebraParent(GradedFreeAlgebraParent, Protocol):
        r"""A parent in \(\Gamma\): the divided powers are its own operation."""

        def divided_power(
            self, value: "Element", exponent: "Integer | int"
        ) -> "Element": ...

    class FreeAlgebraCategory(Protocol):
        r"""The category itself, which ``SubcategoryMethods`` are bound onto."""

        def base_ring(self) -> "Ring": ...


class FreeAlgebras(OwnedCategoryOverBaseRing):
    r"""Algebras whose underlying modules are free."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "free algebras"

    def super_categories(self) -> list:
        # Local: both nodes import this module, so module-level imports here
        # would close those cycles; the modules are built by call time.
        from dzack_research.preamble.categories.algebras.algebras import Algebras
        from dzack_research.preamble.categories.modules.pure.free_modules import FreeModules

        return [
            Algebras(self.base_ring()),
            FreeModules(self.base_ring()),
        ]

    class SubcategoryMethods:
        def on(
            self: "FreeAlgebraCategory", algebra_generating_set: "OrderedSet"
        ) -> "Parent":
            r"""Return the free algebra on ``algebra_generating_set``."""
            # Local: framed_free_algebras imports this module, so a
            # module-level import here would close that cycle.
            from dzack_research.preamble.categories.algebras.framed_free_algebras import FreeAlgebraOn

            free_algebra: "Parent" = FreeAlgebraOn(
                self.base_ring(), algebra_generating_set
            )
            return free_algebra

    class ParentMethods:
        def is_free(self) -> bool:
            r"""Return whether this algebra is free."""
            return True


class GradedFreeAlgebras(OwnedCategoryOverBaseRing):
    r"""The common graded structure of the four free constructions."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "graded free algebras"

    def super_categories(self) -> list:
        # Local: the graded node reaches the algebra node, so a module-level
        # import here would close that cycle.
        from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras

        return [FreeAlgebras(self.base_ring()), GradedAlgebras(self.base_ring())]

    class ParentMethods:
        def _ring_morphism_defining_algebra_structure(self) -> "Morphism":
            r"""Return \(R\to A\), \(r\mapsto r1_A\)."""
            from sage.categories.homset import Hom
            from sage.categories.morphism import SetMorphism
            from sage.categories.rings import Rings

            return SetMorphism(
                Hom(self.base_ring(), self, Rings()),
                lambda scalar: scalar * self.one(),
            )

        def graded_piece(
            self: "GradedFreeAlgebraParent", degree: "Integer"
        ) -> "Module":
            r"""Return the free submodule on the monomials of one degree."""
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreeModuleOn
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set

            monomials = self.monomial_system().monomials_of_degree(degree)
            if isinstance(monomials, tuple):
                monomials = finite_ordered_set(monomials)
            source = FreeModuleOn(
                self.base_ring(),
                monomials,
            )
            inclusion = module_homset(source, self)(
                lambda index: self.module_generator(
                    self.monomial_system().basis_monomial(index)
                )
            )
            inclusion._known_injective = True
            return Subobject(inclusion)

        def degree_on_module_generator(
            self: "GradedFreeAlgebraParent", module_generator: "Element"
        ) -> "Integer":
            r"""Return the degree of a monomial: the grading of these algebras.

            The number of letters, however this construction spells them: a
            word reports its letters in order, an abelian monomial its
            exponents, a subset its members.  All count to the same degree,
            which is what makes the other three graded companions of the
            tensor algebra.
            """
            degree: "Integer" = self.monomial_system().degree(module_generator)
            return degree

        def monomial_degree(
            self: "GradedFreeAlgebraParent", monomial: "Element"
        ) -> "Integer":
            r"""Return the \(n\) with this monomial in \(T(M)[n]\).

            The grading, asked of a monomial by the word this construction
            uses for one.
            """
            return self.degree_on_module_generator(monomial)

        def graded_piece_monomials(
            self: "GradedFreeAlgebraParent", degree: "Integer | int"
        ) -> "Set | tuple":
            r"""Return the monomials spanning \(T(M)[n]\).

            For a free \(M\) on \(S\) these are the words of length \(n\),
            so the piece is \(M^{\otimes n}\) and there is no separate
            \(M^{\otimes 2}\) to build: it is this.

            Asked of the monomials rather than assembled from products of
            generators, because in \(\Gamma\) a product of generators is not
            a monomial: \(x\cdot x=2\gamma_2(x)\).  Each construction knows
            its own basis in each degree, and that is what a graded piece is.
            """
            from dzack_research.preamble.categories.sets.sets import ImageSet

            monomials = self.monomial_system().monomials_of_degree(degree)
            if isinstance(monomials, tuple):
                return tuple(
                    self.module_generator(
                        self.monomial_system().basis_monomial(index)
                    )
                    for index in monomials
                )
            return ImageSet(
                lambda index: self.module_generator(
                    self.monomial_system().basis_monomial(index)
                ),
                monomials,
                is_injective=True,
            )

        def module_generators_of_degree(
            self: "GradedFreeAlgebraParent", degree: "Integer | int"
        ) -> "Set | tuple":
            r"""Return the monomials of a degree, which the grading asks for.

            Asked of the monomials rather than filtered out of all of them:
            there are infinitely many monomials and finitely many in each
            degree, so the general reading -- run over the generators and keep
            the ones that fit -- does not terminate here.
            """
            return self.graded_piece_monomials(degree)

        def ideal_generators_in_degree(
            self: "GradedFreeAlgebraParent",
            relations: tuple,
            degree: "Integer | int",
        ) -> tuple:
            r"""Return generators of \(\langle K\rangle_n\) for \(K\) in degree one.

            \(A\) is a left adjoint, so it takes a presentation
            \(M=\operatorname{coker}(K\to F)\) to \(A(M)=A(F)/\langle
            K\rangle\).  The degree-\(n\) part of a two-sided ideal generated
            in degree one is \(\sum_{i+j=n-1}A_i\,K\,A_j\), which is what this
            spans.

            One statement for three of the four: in a commutative flavour the
            two sides coincide, so the extra generators are redundant rather
            than wrong.  \(\Gamma\) adds its divided powers.
            """
            monomials = self.monomial_system().monomials_of_degree
            generators = []
            for relation in relations:
                for left_degree in range(int(degree)):
                    right_degree = int(degree) - 1 - left_degree
                    for left in monomials(left_degree):
                        for right in monomials(right_degree):
                            generators.append(
                                self.module_generator(left)
                                * relation
                                * self.module_generator(right)
                            )
            return tuple(generators)


class TensorAlgebras(OwnedCategoryOverBaseRing):
    r"""Tensor algebras \(T(M)\)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "tensor algebras"

    def super_categories(self) -> list:
        return [GradedFreeAlgebras(self.base_ring())]

    class ParentMethods:
        def ring_center(self) -> "Ring":
            r"""Return \(Z(T(M))\).

            For zero or one generator the tensor algebra is commutative.  For
            at least two generators, its center consists of the scalars.
            """
            labels = self.algebra_generating_set()
            match labels in Sets().Finite():
                case True if labels.cardinality() <= 1:
                    return self
                case _:
                    return self.base_ring()

        def center_embedding(self) -> "Morphism":
            r"""Return the inclusion \(Z(T(M))\hookrightarrow T(M)\)."""
            from sage.categories.homset import Hom
            from sage.categories.morphism import SetMorphism
            from sage.categories.rings import Rings

            center = self.ring_center()
            match center is self:
                case True:
                    return SetMorphism(Hom(self, self, Rings()), lambda element: element)
                case False:
                    return SetMorphism(
                        Hom(center, self, Rings()),
                        lambda scalar: scalar * self.one(),
                    )


class SymmetricAlgebras(OwnedCategoryOverBaseRing):
    r"""\(\operatorname{Sym}(M)=T(M)/\langle x\otimes y-y\otimes x\rangle\).

    The polynomial algebra, when \(M\) is free: monomials are the free
    *abelian* monoid on the generators, which is that quotient written out.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "symmetric algebras"

    def super_categories(self) -> list:
        from dzack_research.preamble.categories.algebras.algebras import Algebras

        return [
            GradedFreeAlgebras(self.base_ring()),
            Algebras(self.base_ring()).Commutative(),
        ]


class AlternatingAlgebras(OwnedCategoryOverBaseRing):
    r"""\(\Lambda(M)=T(M)/\langle x\otimes x\rangle\)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "alternating algebras"

    def super_categories(self) -> list:
        return [GradedFreeAlgebras(self.base_ring())]


class DividedPowerAlgebras(OwnedCategoryOverBaseRing):
    r"""\(\Gamma(M)\), whose degree-two piece classifies quadratic forms.

    Not a quotient by a relation but the object with the universal property
    \(\operatorname{Hom}(\Gamma^2M,W)\cong\{\text{quadratic maps }M\to W\}\),
    which is what makes a quadratic form a morphism rather than a set map.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "divided power algebras"

    def super_categories(self) -> list:
        from dzack_research.preamble.categories.algebras.algebras import Algebras

        return [
            GradedFreeAlgebras(self.base_ring()),
            Algebras(self.base_ring()).Commutative(),
        ]

    class ParentMethods:
        def ideal_generators_in_degree(
            self: "DividedPowerAlgebraParent",
            relations: tuple,
            degree: "Integer | int",
        ) -> tuple:
            generators = GradedFreeAlgebras.ParentMethods.ideal_generators_in_degree(
                self, relations, degree
            )
            degree = int(degree)
            added = []
            for relation in relations:
                for divided_degree in range(2, degree + 1):
                    divided = self.divided_power(relation, divided_degree)
                    for monomial in self.monomial_system().monomials_of_degree(
                        degree - divided_degree
                    ):
                        added.append(divided * self.module_generator(monomial))
            return generators + tuple(added)
