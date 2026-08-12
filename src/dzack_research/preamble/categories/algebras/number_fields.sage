r"""Number fields, as what they are: \(\QQ[x]/(f)\) for \(f\) irreducible.

A number field is not a new kind of object.  It is a finitely presented
\(\QQ\)-algebra on one generator, and the single relation is its defining
polynomial -- so the free algebra already built here presents it, the ideal
already reduces, and equality in the quotient is equality of remainders.

What the field *adds* to that quotient is nothing structural; it is the
irreducibility of \(f\), which is what makes every nonzero element invertible.
So irreducibility is asserted at construction and the object is placed in the
owned fields, rather than the field axiom being claimed and hoped for.

Degree is the one word that means two things and must not be conflated: the
degree of \(f\) is the degree \([K:\QQ]\) of the field, and the degree of an
*element* is its degree as a polynomial before reduction, which is bounded by
it.  The field answers the first; its elements answer the second.
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Element
    from dzack_research.preamble.categories.functors.algebra_base_change import AlgebraBaseChangeFunctor
    from dzack_research.preamble.lexicon import Group
    from dzack_research.preamble.lexicon import Vector

from sage.rings.rational_field import QQ as SageQQ
if TYPE_CHECKING:
    # The matrix CLASS, which is what an annotation names; the capitalized
    # name in ``sage.matrix.constructor`` is an alias of the constructor
    # function, and a value of this type is what that function returns.
    from sage.structure.element import Matrix
    from sage.structure.parent import Parent
    from sage.rings.ring import Ring
    from sage.structure.sequence import Sequence
    from dzack_research.preamble.lexicon import OrderedSet

from dzack_research.preamble.categories.rings.rings import SageZZ
from typing import Protocol

from sage.categories.category import Category
from sage.libs.pari import pari as _pari
from sage.matrix.special import column_matrix as _column_matrix
from sage.misc.cachefunc import cached_method
from sage.modules.free_module_element import vector as _vector
from sage.rings.number_field.number_field import (
    NumberField as _SageNumberField,
)
from sage.rings.rational_field import RationalField as _RationalFieldType
from sage.categories.rings import Rings as SageRings

if TYPE_CHECKING:
    # What this node requires of the objects it is about.  Sage binds
    # ``ParentMethods`` onto a parent and ``ElementMethods`` onto its
    # elements by COPYING the methods into a dynamic class, so the object a
    # method runs on is never an instance of the class the method is written
    # in: ``self`` is annotated with what its placement gives it.

    class PresentingAlgebraParent(Protocol):
        r"""The free \(\QQ\)-algebra of rank one that presents \(K\).

        The presentation is where the polynomial spelling of \(f\) lives:
        crossing to a polynomial and back is this algebra's operation, not
        the field's.
        """

        def number_of_algebra_generators(self) -> "Integer": ...
        def _as_polynomial(self, element: "Element") -> "Element": ...
        def _from_polynomial(self, polynomial: "Element") -> "Element": ...

    class EngineNumberField(Protocol):
        r"""Sage's \(\QQ[x]/(f)\), which the arithmetic algorithms run in.

        Reached only through
        :meth:`OwnedNumberFields.ParentMethods._engine_field`, and only for
        the five computations below: each is an algorithm rather than a
        definition, so each crosses once and comes back.
        """

        def discriminant(self) -> "Integer": ...
        def signature(self) -> tuple["Integer", "Integer"]: ...
        def class_number(self) -> "Integer": ...
        def is_galois(self) -> bool: ...
        def galois_group(self) -> "Group": ...

    class NumberFieldParent(Protocol):
        r"""A parent in ``OwnedNumberFields()``.

        Everything here is the finite presentation it inherits from
        ``FinitelyPresentedAlgebras``: one generator, one relation.
        """

        def __call__(self, value: "Element") -> "Element": ...
        def base_ring(self) -> "Ring": ...
        def zero(self) -> "Element": ...
        def one(self) -> "Element": ...
        def relations(self) -> "OrderedSet": ...
        def algebra_generating_set(self) -> "OrderedSet": ...
        def algebra_generator(self, label: "Element") -> "Element": ...
        def presentation_ring(self) -> "PresentingAlgebraParent": ...
        def defining_polynomial(self) -> "Element": ...
        def degree(self) -> "Integer": ...
        def discriminant(self) -> "Integer": ...
        def primitive_element(self) -> "Element": ...
        def embedding_images(self, ring: "Ring") -> tuple: ...
        def underlying_algebra(self, base_ring: "Ring" = ...) -> "Parent": ...
        def _from_power_basis(self, coefficients: "Sequence") -> "Element": ...
        def _engine_field(self) -> "EngineNumberField": ...

    class NumberFieldElement(Protocol):
        r"""An element of \(K\): a class in the quotient, so it lifts."""

        def lift(self) -> "Element": ...
        def parent(self) -> "NumberFieldParent": ...
        def _representative(self) -> "Element": ...
        def _power_basis_coordinates(self) -> "Vector": ...
        def matrix(self) -> "Matrix": ...
        def minimal_polynomial(self) -> "Element": ...
        def roots(self) -> tuple: ...

class OwnedNumberFields(Category):
    r"""Finite extensions \(K/\QQ\), presented on a primitive element."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "number fields"

    def super_categories(self) -> list:
        # Local: both nodes reach this module, so module-level imports would
        # close those cycles; they are built by the time this runs.
        from dzack_research.preamble.categories.algebras.finitely_presented_algebras import FinitelyPresentedAlgebras
        from dzack_research.preamble.categories.rings.rings import OwnedFields

        return [FinitelyPresentedAlgebras(SageQQ), OwnedFields()]

    class ParentMethods:
        def defining_polynomial(self: "NumberFieldParent") -> "Element":
            r"""Return \(f\), the one relation this field is presented by."""
            relations = self.relations()
            assert len(relations) == 1, (
                "a number field is presented by one polynomial in one "
                "generator"
            )
            return relations[0]

        def degree(self: "NumberFieldParent") -> "Integer":
            r"""Return \([K:\QQ]\), which is \(\deg f\).

            The dimension of \(K\) as a \(\QQ\)-module: reduction modulo \(f\)
            leaves the monomials below \(\deg f\), and they are a basis.
            """
            degree: "Integer" = self.defining_polynomial().degree()
            return degree

        def primitive_element(self: "NumberFieldParent") -> "Element":
            r"""Return the image of the generator, a root of \(f\) in \(K\).

            Primitive because \(K\) is generated by it as a \(\QQ\)-algebra --
            which is what presenting on one generator says.  Read from the
            presentation and not from :meth:`algebra_generators`, which is
            written in terms of this.
            """
            label = next(iter(self.algebra_generating_set()))
            return self.algebra_generator(label)

        def algebra_generators(self: "NumberFieldParent") -> tuple:
            r"""Return \((\alpha)\): one generator, because \(K=\QQ(\alpha)\).

            Declared here because the generic field answers this by asking for
            ``gens``, which a quotient forwards to the ring covering it -- and
            the algebra presenting this field does not carry that word.  The
            presentation already says what the generators are.
            """
            return (self.primitive_element(),)

        def is_field(self) -> bool:
            r"""Return ``True``: \(f\) is irreducible, so \((f)\) is maximal."""
            return True

        def _an_element_(self: "NumberFieldParent") -> "Element":
            r"""Return \(\alpha\), the element this field is presented on.

            Named rather than left to be guessed: Sage looks for an example by
            converting a string, the quotient forwards that to the algebra
            presenting it, and the algebra rejects it -- so anything built
            *over* this field would fail while asking it for an example of
            itself.
            """
            return self.primitive_element()

        # ---------------------------------------------------------------
        # The arithmetic of K.  Each of these is a computation rather than a
        # definition -- a maximal order, a class number, a Galois group --
        # so each crosses to the engine at the presentation, once, through
        # ``_engine_field``, and returns owned objects or plain integers.
        # ---------------------------------------------------------------

        @cached_method
        def _engine_field(self: "NumberFieldParent") -> "EngineNumberField":
            r"""Return the engine's \(\QQ[x]/(f)\), for the algorithms only.

            The presentation is the same \(f\); nothing is chosen here that
            was not already chosen in presenting this field, which is why the
            crossing can be private and cached.
            """
            presented = self.presentation_ring()._as_polynomial(
                self.defining_polynomial()
            )
            engine_field: "EngineNumberField" = _SageNumberField(presented, "a")
            return engine_field

        def _from_engine_element(
            self: "NumberFieldParent", element: "Element"
        ) -> "Element":
            r"""Return ``element`` as a combination of powers of \(\alpha\).

            The engine writes an element in the power basis of its own
            generator, and \(\alpha\) is this field's, so the coefficients
            transport unchanged: that basis *is* the reduction the quotient
            performs.
            """
            primitive = self.primitive_element()
            total = self.zero()
            power = self.one()
            for coefficient in element.list():
                total = total + coefficient * power
                power = power * primitive
            return total

        def discriminant(self: "NumberFieldParent") -> "Integer":
            r"""Return \(d_K\), the discriminant of the maximal order.

            Not the discriminant of \(f\): they differ by the square of the
            index of \(\ZZ[\alpha]\) in the ring of integers, and it is the
            field's that the ramification reads.
            """
            return self._engine_field().discriminant()

        def signature(self: "NumberFieldParent") -> tuple:
            r"""Return \((r,s)\): the real and the conjugate-pair places.

            \(r+2s=[K:\QQ]\), which is what makes this a decomposition of the
            degree and not two independent counts.
            """
            return tuple(self._engine_field().signature())

        def _from_power_basis(
            self: "NumberFieldParent", coefficients: "Sequence"
        ) -> "Element":
            r"""Return \(\sum c_i\alpha^i\) for the coefficients given."""
            total = self.zero()
            power = self.one()
            for coefficient in coefficients:
                total = total + SageQQ(coefficient) * power
                power = power * self.primitive_element()
            return total

        def underlying_algebra(
            self: "NumberFieldParent", base_ring: "Ring" = SageZZ
        ) -> "Parent":
            r"""Return the \(R\)-algebra this field is the base change of.

            \(K\) is a \(\operatorname{Frac}(R)\)-algebra, and an \(R\)-algebra
            underlying it is one with the same presentation over \(R\): the
            relation is the same \(f\), which needs integral coefficients and
            a unit leading one for that to be a presentation over \(R\) at all.
            \(A\otimes_R\operatorname{Frac}(R)=K\) is then the base change,
            which :meth:`FinitelyPresentedAlgebras.ParentMethods.base_change`
            computes -- so the relation between the two is an arrow and not a
            resemblance.

            Not *the* underlying algebra: an \(R\)-form is a choice, and this
            is the one the presentation already made.  A maximal one is a
            different choice and a different object.
            """
            # Local: finitely_presented_algebras reaches this module, so a
            # module-level import would close that cycle.
            from dzack_research.preamble.categories.algebras.finitely_presented_algebras import FGAlgebra

            defining_polynomial = self.defining_polynomial()
            assert all(
                coefficient in base_ring
                for coefficient in defining_polynomial.coefficients().values()
            ), (
                f"{defining_polynomial} does not have coefficients in "
                f"{base_ring}, so it presents no algebra over it"
            )
            assert defining_polynomial.leading_coefficient().is_unit(), (
                "a presentation over R needs a unit leading coefficient, or "
                "the quotient is not free of rank deg(f)"
            )
            over_the_base = defining_polynomial.change_ring(base_ring)
            underlying: "Parent" = FGAlgebra(
                base_ring,
                self.algebra_generating_set(),
                (over_the_base,),
            )
            return underlying

        def base_change_functor(
            self: "NumberFieldParent", base_ring: "Ring" = SageZZ
        ) -> "AlgebraBaseChangeFunctor":
            r"""Return \(F=-\otimes_R\operatorname{Frac}(R)\), with \(F(A)=K\).

            The functor itself, because that is what relates this field to the
            \(R\)-algebra underlying it: an arrow between the two categories,
            which can be applied to the maps between algebras as well as to
            the algebras.
            """
            # Local: the base-change functor reaches this module through the
            # algebra node, so a module-level import would close that cycle.
            from dzack_research.preamble.categories.functors.algebra_base_change import algebra_base_change

            return algebra_base_change(self.base_ring().coerce_map_from(base_ring))

        def integral_basis(
            self: "NumberFieldParent", base_ring: "Ring" = SageZZ
        ) -> tuple:
            r"""Return an \(R\)-basis of :meth:`underlying_algebra`, inside \(K\).

            An integral basis is not a number-field notion: it is a basis of
            the \(R\)-algebra underlying this one, transported here along the
            base change.  Reduction modulo \(f\) leaves the powers below
            \(\deg f\), so those *are* that basis.
            """
            self.underlying_algebra(base_ring)
            return tuple(
                self._from_power_basis(
                    [1 if index == power else 0 for index in range(power + 1)]
                )
                for power in range(self.degree())
            )

        def class_number(self: "NumberFieldParent") -> "Integer":
            r"""Return \(|\operatorname{Cl}(\mathcal O_K)|\)."""
            return self._engine_field().class_number()

        def ramified_primes(self: "NumberFieldParent") -> tuple:
            r"""Return the primes that ramify: those dividing \(d_K\)."""
            return tuple(self.discriminant().prime_factors())

        def is_galois(self: "NumberFieldParent") -> bool:
            r"""Return whether \(K/\QQ\) is Galois.

            Equivalently whether \(f\) splits in \(K\): the extension is
            normal exactly when every root of the defining polynomial is
            already here.
            """
            return bool(self._engine_field().is_galois())

        def galois_group(self: "NumberFieldParent") -> "Group":
            r"""Return \(\operatorname{Gal}\), as an owned group.

            The Galois group of the *defining polynomial*, which is the group
            of \(K/\QQ\) exactly when the extension is normal and is the group
            of its normal closure otherwise -- so the two cases are not
            conflated, and the caller is told which it asked for by
            :meth:`is_galois`.

            Refined on the way back, because no construction hook reaches this
            one: Sage builds a Galois group without running
            ``PermutationGroup_generic.__init__`` (its attributes are lazy), so
            the post-init hook the owned groups install never fires for it.
            """
            # Local: the group node reaches the algebra node, so a module-level
            # import here would close that cycle.
            from dzack_research.preamble.categories.group.groups import refine_group

            return refine_group(self._engine_field().galois_group())

        def embedding_images(self: "NumberFieldParent", ring: "Ring") -> tuple:
            r"""Return the images of \(\alpha\) under the embeddings into ``ring``.

            An embedding \(K\hookrightarrow L\) is determined by where
            \(\alpha\) goes, and it may go to any root of \(f\) in \(L\) --
            so the embeddings *are* those roots, and there is nothing further
            to compute.  Over \(\AA\) their number is \(r\) from
            :meth:`signature`.
            """
            return tuple(
                root
                for root, _ in self.defining_polynomial().roots(
                    ring=ring, multiplicities=True
                )
            )


    class ElementMethods:
        def _representative(self: "NumberFieldElement") -> "Element":
            r"""Return the reduced representative in \(\QQ[x]\)."""
            return self.lift()

        def _power_basis_coordinates(self: "NumberFieldElement") -> "Vector":
            r"""Return the coordinates in \(1,\alpha,\dots,\alpha^{n-1}\).

            Reduction modulo \(f\) leaves exactly those monomials, so the
            representative's coefficients *are* the coordinates -- no basis is
            chosen here that the quotient had not already fixed.
            """
            field = self.parent()
            degree = field.degree()
            representative = self._representative()
            by_degree = {
                sum(monomial.dict().values()): coefficient
                for monomial, coefficient in representative.coefficients().items()
            }
            return _vector(
                SageQQ,
                [by_degree.get(exponent, SageQQ.zero()) for exponent in range(degree)],
            )

        def matrix(self: "NumberFieldElement") -> "Matrix":
            r"""Return the matrix of multiplication by this element.

            \(K\) is a \(\QQ\)-vector space and multiplication by an element is
            \(\QQ\)-linear, so the element *is* that endomorphism; its norm,
            trace and minimal polynomial below are the endomorphism's, which
            is what makes them independent of the presentation.
            """
            field = self.parent()
            primitive = field.primitive_element()
            columns = []
            image = self
            for _ in range(field.degree()):
                columns.append(image._power_basis_coordinates())
                image = image * primitive
            return _column_matrix(SageQQ, columns)

        def norm(self: "NumberFieldElement") -> "Element":
            r"""Return \(N(a)=\det\) of multiplication by \(a\)."""
            return self.matrix().determinant()

        def trace(self: "NumberFieldElement") -> "Element":
            r"""Return \(\operatorname{Tr}(a)=\operatorname{tr}\) of multiplication by \(a\)."""
            return self.matrix().trace()

        def characteristic_polynomial(self: "NumberFieldElement") -> "Element":
            r"""Return the characteristic polynomial of multiplication by \(a\).

            Of degree \([K:\QQ]\) whatever \(a\) is, which is what
            distinguishes it from the minimal polynomial: the two agree
            exactly when \(a\) generates \(K\).
            """
            return self.parent().presentation_ring()._from_polynomial(
                self.matrix().characteristic_polynomial()
            )

        def minimal_polynomial(self: "NumberFieldElement") -> "Element":
            r"""Return the minimal polynomial of \(a\) over \(\QQ\)."""
            return self.parent().presentation_ring()._from_polynomial(
                self.matrix().minimal_polynomial()
            )

        def is_integral(self: "NumberFieldElement") -> bool:
            r"""Return whether \(a\) is an algebraic integer.

            Whether its minimal polynomial is monic over \(\ZZ\), which is the
            definition -- not whether it lies in \(\ZZ[\alpha]\), a smaller
            ring in general.
            """
            return all(
                coefficient in SageZZ
                for coefficient in self.minimal_polynomial().coefficients().values()
            )

        def inverse(self: "NumberFieldElement") -> "Element":
            r"""Return \(a^{-1}\), from a Bezout identity with \(f\).

            \(\gcd(g,f)=1\) for any representative \(g\) of a nonzero \(a\),
            since \(f\) is irreducible and does not divide \(g\) -- so the
            cofactor of \(g\) *is* the inverse, and no engine is asked for one.
            """
            field = self.parent()
            assert self != field.zero(), "zero has no inverse"
            common, cofactor, _ = self._representative().xgcd(
                field.defining_polynomial()
            )
            return field(cofactor * common.leading_coefficient()**-1)

        def conjugates(self: "NumberFieldElement", ring: "Ring") -> tuple:
            r"""Return the images of \(a\) under the embeddings into ``ring``.

            An embedding is fixed by where \(\alpha\) goes, so a conjugate of
            \(a\) is its representative evaluated at a root of \(f\) --
            :meth:`OwnedNumberFields.ParentMethods.embedding_images` names
            those roots.
            """
            field = self.parent()
            label = tuple(field.algebra_generating_set())[0]
            representative = self._representative()
            return tuple(
                representative.subs({label: image})
                for image in field.embedding_images(ring)
            )


def own_number_field(defining_polynomial: "Element") -> "Parent":
    r"""Return \(\QQ[x]/(f)\) as a number field, for ``defining_polynomial``.

    The argument is an element of a free \(\QQ\)-algebra of rank one, so the
    presentation is read off it and no variable name has to be invented here.
    Irreducibility is checked rather than assumed: a reducible \(f\) gives a
    quotient that is a ring and not a field, and it would fail later at a
    division instead of here at the claim.
    """
    # Local: these modules reach this one, so module-level imports would close
    # those cycles; all are built by the time this function runs.
    from dzack_research.preamble.categories.algebras.finitely_presented_algebras import FinitelyPresentedAlgebra
    from dzack_research.preamble.categories.rings.rings import OwnedRing
    from dzack_research.preamble.refine import refine

    presentation_ring = defining_polynomial.parent()
    base_ring = presentation_ring.base_ring()
    engine_base_ring = (
        base_ring._engine if isinstance(base_ring, OwnedRing) else base_ring
    )
    assert isinstance(engine_base_ring, _RationalFieldType), (
        "a number field is an extension of QQ; over another base this is a "
        "finitely presented algebra and is built as one"
    )
    assert presentation_ring.number_of_algebra_generators() == 1, (
        "a number field is presented on a primitive element, so on one "
        "generator"
    )
    assert defining_polynomial.degree() >= 1, (
        "a defining polynomial has positive degree"
    )
    assert defining_polynomial.is_irreducible(), (
        f"{defining_polynomial} is reducible, so the quotient by it has zero "
        "divisors and is not a field"
    )
    field = FinitelyPresentedAlgebra(presentation_ring, (defining_polynomial,))
    # Refined into this category alone, not into a join with the one it
    # already has: ``refine`` puts *the named category's* methods before the
    # concrete class, and a join has none of its own to name -- so joining
    # would leave the quotient's own ``is_field``, which declines to decide,
    # in front of the answer irreducibility already gives.
    owned_field: "Parent" = refine(field, OwnedNumberFields())
    return owned_field
