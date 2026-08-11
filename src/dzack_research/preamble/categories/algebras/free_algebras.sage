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
        return [FreeAlgebras(self.base_ring())]

    class ParentMethods:
        def monomial_degree(self, monomial: "Element") -> "Integer":
            r"""Return the \(n\) with this monomial in \(T(M)[n]\).

            The number of letters, however the monoid spells them: a word
            reports its letters in order, an abelian monomial its exponents.
            Both count to the same degree, which is what makes the symmetric
            algebra a graded quotient of the tensor algebra.
            """
            if hasattr(monomial, "to_word_list"):
                return len(monomial.to_word_list())
            return sum(monomial.dict().values())

        def graded_piece_monomials(self, degree: "Integer") -> tuple:
            r"""Return the monomials spanning \(T(M)[n]\).

            For a free \(M\) on \(S\) these are the words of length \(n\),
            so the piece is \(M^{\otimes n}\) and there is no separate
            \(M^{\otimes 2}\) to build: it is this.
            """
            from itertools import product as _tuples

            labels = tuple(self.algebra_generating_set())
            assert labels, "a graded piece of the tensor algebra on no generators"
            return tuple(
                self.algebra_generator(word[0]) if degree == 1 else
                _product_of(self, word)
                for word in _tuples(labels, repeat=int(degree))
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


def _product_of(algebra: "Parent", word: tuple) -> "Element":
    r"""Return the monomial spelled by ``word``, in order."""
    monomial = algebra.one()
    for label in word:
        monomial = monomial * algebra.algebra_generator(label)
    return monomial
