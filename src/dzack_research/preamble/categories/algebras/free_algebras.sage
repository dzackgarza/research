r"""Free algebras over a base ring, without a chosen generating set."""

from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing



class FreeAlgebras(OwnedCategoryOverBaseRing):
    r"""Category of free commutative algebras over a base ring, without a chosen algebra_generators."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "free algebras"

    def super_categories(self) -> list:
        # Local: both nodes import this module, so module-level imports here
        # would close those cycles; the modules are built by call time.
        from dzack_research.preamble.categories.algebras.algebras import Algebras
        from dzack_research.preamble.categories.modules.pure.free_modules import FreeModules

        # Free *commutative* algebra: the monomials come from the free
        # abelian monoid, so xy = yx holds by construction and the axiom is
        # a declaration, not a claim to be checked.
        return [
            Algebras(self.base_ring()).Commutative(),
            FreeModules(self.base_ring()),
        ]

    class SubcategoryMethods:
        def on(self, algebra_generating_set):
            r"""Return the free algebra on ``algebra_generating_set``."""
            # Local: framed_free_algebras imports this module, so a
            # module-level import here would close that cycle.
            from dzack_research.preamble.categories.algebras.framed_free_algebras import FreeAlgebraOn

            return FreeAlgebraOn(self.base_ring(), algebra_generating_set)

    class ParentMethods:
        def is_free(self) -> bool:
            r"""Return whether this algebra is free."""
            return True


class TensorAlgebras(OwnedCategoryOverBaseRing):
    r"""Tensor algebras \(T(M)\), and what is carved out of them.

    \(T\) is left adjoint to the forgetful functor \(R\text{-Alg}\to
    R\text{-Mod}\), so \(T(M)\) exists for every module and is graded with
    \(T(M)[n]=M^{\otimes n}\).  Everything else here is a quotient of it: the
    symmetric algebra by \(x\otimes y-y\otimes x\), the alternating algebra
    by \(x\otimes x\), and the divided power algebra by its own universal
    property.  Locating them as subcategories is what says they are one
    construction seen through different relations rather than four unrelated
    ones.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "tensor algebras"

    def super_categories(self) -> list:
        # Local: the graded node reaches the algebra node, so a module-level
        # import here would close that cycle.
        from dzack_research.preamble.categories.modules.graded_modules import GradedAlgebras

        return [FreeAlgebras(self.base_ring()), GradedAlgebras(self.base_ring())]

    class ParentMethods:
        def degree_on_module_generator(self, module_generator: "Element") -> "Integer":
            r"""Return the degree of a monomial: the grading of these algebras.

            The number of letters, however this construction spells them: a
            word reports its letters in order, an abelian monomial its
            exponents, a subset its members.  All count to the same degree,
            which is what makes the other three graded companions of the
            tensor algebra.
            """
            return self.monomial_system().degree(module_generator)

        def monomial_degree(self, monomial: "Element") -> "Integer":
            r"""Return the \(n\) with this monomial in \(T(M)[n]\).

            The grading, asked of a monomial by the word this construction
            uses for one.
            """
            return self.degree_on_module_generator(monomial)

        def graded_piece_monomials(self, degree: "Integer") -> tuple:
            r"""Return the monomials spanning \(T(M)[n]\).

            For a free \(M\) on \(S\) these are the words of length \(n\),
            so the piece is \(M^{\otimes n}\) and there is no separate
            \(M^{\otimes 2}\) to build: it is this.

            Asked of the monomials rather than assembled from products of
            generators, because in \(\Gamma\) a product of generators is not
            a monomial: \(x\cdot x=2\gamma_2(x)\).  Each construction knows
            its own basis in each degree, and that is what a graded piece is.
            """
            return tuple(
                self.module_generator(monomial)
                for monomial in self.monomial_system().monomials_of_degree(degree)
            )

        def module_generators_of_degree(self, degree: "Integer") -> "OrderedSet":
            r"""Return the monomials of a degree, which the grading asks for.

            Asked of the monomials rather than filtered out of all of them:
            there are infinitely many monomials and finitely many in each
            degree, so the general reading -- run over the generators and keep
            the ones that fit -- does not terminate here.
            """
            # Local: the set node reaches this module, so a module-level
            # import would close that cycle.
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set

            return finite_ordered_set(
                self.module_generator(monomial)
                for monomial in self.monomial_system().monomials_of_degree(degree)
            )

        def ideal_generators_in_degree(
            self, relations: tuple, degree: "Integer"
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


class SymmetricAlgebras(OwnedCategoryOverBaseRing):
    r"""\(\operatorname{Sym}(M)=T(M)/\langle x\otimes y-y\otimes x\rangle\).

    The polynomial algebra, when \(M\) is free: monomials are the free
    *abelian* monoid on the generators, which is that quotient written out.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "symmetric algebras"

    def super_categories(self) -> list:
        return [TensorAlgebras(self.base_ring())]


class AlternatingAlgebras(OwnedCategoryOverBaseRing):
    r"""\(\Lambda(M)=T(M)/\langle x\otimes x\rangle\)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "alternating algebras"

    def super_categories(self) -> list:
        return [TensorAlgebras(self.base_ring())]


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
        return [TensorAlgebras(self.base_ring())]
