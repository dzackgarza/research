r"""Free commutative algebras on arbitrary sets.

``FreeAlgebraOn(R, S)`` realizes the free commutative ``R``-algebra on a set ``S``:

\[
    \operatorname{FreeAlg}_R(S) = R[\operatorname{Mon}(S)]
\]

As an ``R``-module this is the free module on ``Mon(S)``, the free commutative
monoid on ``S``.  Multiplication is the monoid operation on ``Mon(S)``
extended ``R``-bilinearly.

Which monoid indexes the monomials is what separates the four free
constructions, and each of them is its own category: the symmetric algebra,
the tensor algebra, the alternating algebra and the divided power algebra.

The exposed *algebra* generating set is ``S``; the module generators are
``Mon(S)``.
"""

from typing import Callable
from typing import TYPE_CHECKING
from dzack_research.preamble.lexicon import Element
if TYPE_CHECKING:
    from sage.categories.modules import Module
    from dzack_research.preamble.categories.sets.cardinals import Cardinal
    from sage.structure.parent import ElementConstructorInput

from dzack_research.preamble.categories.algebras.algebras import FramedAlgebras
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
from dzack_research.preamble.categories.algebras.free_algebras import AlternatingAlgebras
from dzack_research.preamble.categories.algebras.free_algebras import DividedPowerAlgebras
from dzack_research.preamble.categories.algebras.free_algebras import FreeAlgebras
from dzack_research.preamble.categories.algebras.free_algebras import SymmetricAlgebras
from dzack_research.preamble.categories.algebras.free_algebras import TensorAlgebras
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import HomsetsCategory
from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.sets import _as_set
from sage.misc.cachefunc import cached_method
from dzack_research.preamble.categories.rings.rings import engine_ring
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
if TYPE_CHECKING:
    from sage.categories.morphism import Morphism
    from sage.rings.ring import Ring
    from dzack_research.preamble.owned_category import ConstructionData

from collections.abc import Iterable as _Iterable, Mapping
from typing import Protocol, TYPE_CHECKING

from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.monoids.free_abelian_monoid import FreeAbelianMonoid
from sage.monoids.free_monoid import FreeMonoid as _FreeMonoid
from sage.rings.abc import AlgebraicRealField as _AlgebraicRealFieldType
from sage.rings.abc import RealIntervalField as _RealIntervalFieldType
from sage.rings.infinity import Infinity as _Infinity
from sage.rings.integer import Integer as _SageIntegerType
from sage.rings.rational_field import QQ as SageQQ
from sage.arith.misc import factorial
from sage.rings.qqbar import QQbar as _AlgebraicNumbers
from sage.rings.polynomial.polynomial_ring_constructor import (
    PolynomialRing as _SagePolynomialRing,
)
from sage.rings.ideal import Ideal_generic
from sage.structure.element import Element as _SageElement
from sage.structure.element import ModuleElement
from sage.categories.rings import Rings as SageRings
from sage.structure.element import RingElement
from sage.structure.element import Vector
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

assert "_as_set" in globals(), "Framed free algebras requires Set() from the preamble"

from dzack_research.preamble.categories.sets.owned_sets import Sets
from dzack_research.preamble.categories.sets.underlying_sets import UnderlyingSet

if TYPE_CHECKING:
    from sage.categories.sets_cat import Set

    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet

    # The surfaces the category's methods are written against.  Sage binds
    # ``ParentMethods`` onto a parent and ``ElementMethods`` onto its
    # elements by COPYING them into a dynamic class, so neither edge is a
    # Python base; ``typings/sage/categories/rings.pyi`` declares the same
    # true edge statically, for the same reason.  At runtime both names are
    # ``object``, so what Sage receives is the plain class it expects.

    class FreeAlgebraParent(Protocol):
        r"""A parent in ``FramedFreeAlgebras(R)``.

        Two framings, and every operation below reads one of them: \(S\) is
        the algebra framing and \(\operatorname{Mon}(S)\) the module one.  The
        category's ``ParentMethods`` is what answers them; its fields are
        named here because the methods written against this surface read
        them.
        """

        _algebra_generating_set: "OrderedSet"
        _algebra_generating_set_for_morphism: "Set"
        _monomial_system: "MonomialSystem"
        _monomial_parent: "_MonomialParent"
        _algebra_generator_morphism: SetMorphism

        def base_ring(self) -> "Ring": ...
        def one(self) -> "FramedFreeAlgebras.ElementMethods": ...
        def zero(self) -> "FramedFreeAlgebras.ElementMethods": ...
        def number_of_algebra_generators(self) -> "Cardinal": ...
        def monomial_system(self) -> "MonomialSystem": ...
        def algebra_generating_set(self) -> "OrderedSet": ...
        def algebra_generator(self, label: "Element") -> "FramedFreeAlgebras.ElementMethods": ...
        def algebra_generators(self) -> tuple: ...
        def module_generating_set(self) -> "OrderedSet": ...
        def module_generator(
            self, monomial: "Element"
        ) -> "FramedFreeAlgebras.ElementMethods": ...
        def _algebra_generator_label(self, monomial: "Element") -> "Element": ...
        def _require_symmetric_polynomial_structure(self) -> None: ...
        def _polynomial_ring(self) -> "_PolynomialRing": ...
        def _polynomial_variables(self) -> dict: ...
        def _as_polynomial(
            self, element: "FreeAlgebraElement"
        ) -> "_EnginePolynomial": ...
        def _from_polynomial(
            self, polynomial: "_EnginePolynomial"
        ) -> "FramedFreeAlgebras.ElementMethods": ...
        def _engine_base_ring(self) -> "SageRings.ParentMethods": ...
        def _as_engine_coefficient(
            self, coefficient: "_NumberFieldCoefficient"
        ) -> "RingElement": ...
        def _from_engine_coefficient(self, value: "RingElement") -> "RingElement": ...
        def _generator_images(
            self,
            images: "SetMorphism | dict | tuple | list | Callable",
            codomain: "Module",
        ) -> "tuple[Callable, Module]": ...
        def _extend_to_monomials(
            self, image_of_generator: "Callable", codomain: "Module"
        ) -> "Callable": ...
        def _from_algebra_generator_values(
            self, codomain: "Module", values: tuple
        ) -> dict: ...
        def hom(
            self,
            images: "SetMorphism | dict | tuple | list | Callable",
            codomain: "Module" = ...,
        ) -> "FreeAlgebraMorphism": ...

    class DividedPowerAlgebraParent(FreeAlgebraParent, Protocol):
        r"""A parent in ``FramedDividedPowerAlgebras(R)``.

        \(\Gamma\) is the one construction whose divided powers are its own
        operation: \(\gamma_a(x)\) is not \(x^a\), so it has to be asked for
        by name.
        """

        def divided_power(
            self, value: "Element", exponent: "Integer | int"
        ) -> "Element": ...
        def divided_square(self, element: "Element") -> "Element": ...

    class _MonomialParent(Parent):
        r"""Where the monomials live: a monoid, or the finite subsets of
        \(S\) for \(\Lambda\).  Two operations are common to all four, and
        they are the ones :class:`MonomialSystem` reads."""

        def one(self) -> "Element": ...
        def gen(self, label: "Element") -> "Element": ...

    class _PolynomialRing(Parent["_EnginePolynomial"]):
        r"""The engine's \(R[x_s]\): the presentation this algebra crosses
        into for division, factorisation and roots.  Its variables are what
        the bijection \(S\leftrightarrow\{x_s\}\) is chosen against."""

        def gens(self) -> tuple["_EnginePolynomial", ...]: ...
        def ideal(self, generators: list["_EnginePolynomial"]) -> "_EngineIdeal": ...

    class _EngineIdeal:
        r"""An ideal of the polynomial presentation: what a quotient decides
        equality by, through the normal form it can reduce to."""

        def reduce(self, element: "_EnginePolynomial") -> "_EnginePolynomial": ...
        def __contains__(self, element: "_EnginePolynomial") -> bool: ...

    class _EnginePolynomial(RingElement):
        r"""The engine's polynomial, on the far side of
        :meth:`FreeAlgebraParent._as_polynomial`.

        Named by the operations the crossing uses rather than by a class: the
        presentation is univariate at rank one and multivariate above, and
        Sage's two polynomial classes share no base below
        ``CommutativeRingElement``.
        """

        def derivative(self, variable: "Element") -> "_EnginePolynomial": ...
        def divides(self, other: "_EnginePolynomial") -> bool: ...
        def dict(self) -> dict["Element", "Element"]: ...
        def roots(
            self, ring: "Parent | None" = ..., multiplicities: bool = ...
        ) -> list: ...
        def __mod__(self, other: "_EnginePolynomial") -> "_EnginePolynomial": ...

    class _NumberFieldCoefficient(RingElement):
        r"""A base-ring coefficient when the base ring is a number field: it
        is written in the power basis of the primitive element, which is what
        the crossing transports."""

        def _power_basis_coordinates(self) -> "Vector": ...

    class FreeAlgebraElement(Protocol):
        r"""An element of a framed free algebra: a finitely supported
        function on \(\operatorname{Mon}(S)\), so its coefficients are a
        lookup rather than a question for an engine."""

        def parent(self) -> "FreeAlgebraParent": ...
        def base_ring(self) -> "Ring": ...
        def coefficients(self) -> Mapping["Element", "RingElement"]: ...
        def degree(self) -> "Integer": ...
        def coefficient(self, monomial: "Element") -> "RingElement": ...
        def constant_coefficient(self: "FreeAlgebraElement") -> "RingElement": ...
        def leading_coefficient(self) -> "RingElement": ...
        def denominator(self) -> "Element": ...
        def derivative(self, label: "Element" = ...) -> "Element": ...
        def gcd(self, other: "Element") -> "Element": ...
        def subs(self, values: dict) -> "Element": ...
        def roots(
            self, ring: "Ring" = ..., multiplicities: bool = ...
        ) -> list: ...


assert "FramedAlgebras" in globals(), (
    "Framed free algebras requires FramedAlgebras from algebras"
)
assert "FreeAlgebras" in globals(), (
    "Framed free algebras requires FreeAlgebras from free_algebras"
)
assert "FramedFreeModules" in globals(), (
    "Framed free algebras requires FramedFreeModules from framed free modules"
)
assert "ModuleMorphism" in globals(), (
    "Framed free algebra morphisms require ModuleMorphism from module morphisms"
)
assert "module_homset" in globals(), (
    "Framed free algebra hom constructor requires module_homset"
)


class MonomialSystem:
    r"""How one free construction indexes its monomials and multiplies them.

    Every algebra here is \(F_R(\text{monomials})\) with a bilinear product,
    and the four constructions differ only in what a monomial is and what two
    of them multiply to.  Stating that pair once is what lets \(\Lambda\) and
    \(\Gamma\) be the same construction as \(T\) and \(\operatorname{Sym}\)
    rather than three more classes: the symmetric algebra indexes by the free
    abelian monoid, the tensor algebra by the free monoid, the alternating
    algebra by finite subsets, and the divided power algebra by the abelian
    monoid again but with a different product.

    A product returns a *coefficient* as well as a monomial, because two of
    them are not monoid operations: \(x\wedge y=-y\wedge x\) and
    \(\gamma_a\gamma_b=\binom{a+b}{a}\gamma_{a+b}\).  A zero coefficient is
    how \(x\wedge x=0\) is said.

    ``factors`` reports a monomial as \((label, exponent)\) *in order*, which
    is the primitive every degree, substitution and coefficient question is
    written against.  Order matters for words and is harmless elsewhere.
    """

    if TYPE_CHECKING:
        # What one construction supplies and the next one differs in.  The
        # degree, enumeration and word methods below are written against
        # these four, which is what makes the four constructions one class;
        # each subclass answers them, and only there.
        @staticmethod
        def _build_parent(labels: "OrderedSet") -> "_MonomialParent": ...
        def factors(self, monomial: "Element") -> tuple: ...
        def product(
            self, left: "Element", right: "Element"
        ) -> tuple["Integer", "Element"]: ...
        def monomials_of_degree(
            self, degree: "Integer | int"
        ) -> Parent | tuple: ...

    def __init__(self, labels: "OrderedSet") -> None:
        self._labels = labels
        self._parent = self._build_parent(labels)

    def parent(self) -> "_MonomialParent":
        r"""Return the parent the monomials live in."""
        return self._parent

    def degree(self, monomial: "Element") -> int:
        r"""Return the total degree: the sum of the exponents."""
        return sum(exponent for _, exponent in self.factors(monomial))

    def basis_monomial(self, index: "Element") -> "Element":
        r"""Return the algebra monomial represented by a graded-piece index."""
        return index

    def _finite_labels(self) -> tuple:
        assert self._labels in Sets().Finite(), (
            "enumerating a graded piece runs over the generators, so there "
            "must be finitely many of them"
        )
        return tuple(self._labels)

    def _monomials_by_exponent_vector(self, degree: "Integer | int") -> tuple:
        r"""Return the monomials of a degree, as exponent vectors on the labels."""
        from sage.combinat.integer_vector import IntegerVectors

        labels = self._finite_labels()
        monomials = []
        for vector in IntegerVectors(int(degree), len(labels)):
            monomial = self._parent.one()
            for label, exponent in zip(labels, vector):
                monomial *= self._parent.gen(label) ** exponent
            monomials.append(monomial)
        return tuple(monomials)

    def _monomials_from_words(
        self,
        degree: "Integer | int",
        *,
        injective: bool,
    ) -> Parent:
        r"""Return degree monomials as the image of length-``degree`` words."""
        from sage.categories.cartesian_product import cartesian_product
        from dzack_research.preamble.categories.sets.sets import ImageSet
        from dzack_research.preamble.categories.sets.sets import finite_ordered_set
        from dzack_research.preamble.refine import refine

        degree = int(degree)
        assert degree >= 0, "a graded degree is nonnegative"
        if degree == 0:
            one_only: Parent = finite_ordered_set((self._parent.one(),))
            return one_only
        words = cartesian_product([self._labels] * degree)

        def monomial_of_word(word: "Element") -> "Element":
            monomial = self._parent.one()
            for label in word:
                monomial *= self._parent.gen(label)
            return monomial

        def word_of_monomial(monomial: "Element") -> "Element":
            letters = tuple(
                label
                for label, exponent in self.factors(monomial)
                for _ in range(exponent)
            )
            return words(letters)

        monomials: Parent = refine(
            ImageSet(
                monomial_of_word,
                words,
                is_injective=injective,
                inverse=word_of_monomial,
            ),
            Sets().Infinite(),
        )
        return monomials


class CommutativeMonomials(MonomialSystem):
    r"""\(\operatorname{Mon}(S)\): the free commutative monoid, for \(\operatorname{Sym}\)."""

    @staticmethod
    def _build_parent(labels: "OrderedSet") -> "_MonomialParent":
        monoid: "_MonomialParent" = FreeAbelianMonoid(labels)
        return monoid

    def factors(self, monomial: "Element") -> tuple:
        return tuple(monomial.dict().items())

    def product(
        self, left: "Element", right: "Element"
    ) -> tuple["Integer", "Element"]:
        return (1, left * right)

    def monomials_of_degree(self, degree: "Integer | int") -> Parent | tuple:
        if self._labels in Sets().Finite():
            return self._monomials_by_exponent_vector(degree)
        return self._monomials_from_words(degree, injective=False)


class WordMonomials(MonomialSystem):
    r"""Words in \(S\): the free monoid, for \(T\).

    A word is its letters in order and nothing may be reordered, which is the
    whole content of the tensor algebra being noncommutative.
    """

    @staticmethod
    def _build_parent(labels: "OrderedSet") -> "_MonomialParent":
        monoid: "_MonomialParent" = _FreeMonoid(labels)
        return monoid

    def factors(self, monomial: "Element") -> tuple:
        return tuple((letter, 1) for letter in monomial.to_word_list())

    def product(
        self, left: "Element", right: "Element"
    ) -> tuple["Integer", "Element"]:
        return (1, left * right)

    def monomials_of_degree(self, degree: "Integer | int") -> Parent | tuple:
        r"""Return the words of a length: \(\mathrm{rank}^n\) of them."""
        from itertools import product as _tuples

        if self._labels not in Sets().Finite():
            return self._monomials_from_words(degree, injective=True)
        labels = self._finite_labels()
        monomials = []
        for word in _tuples(labels, repeat=int(degree)):
            monomial = self._parent.one()
            for letter in word:
                monomial *= self._parent.gen(letter)
            monomials.append(monomial)
        return tuple(monomials)


class AlternatingMonomials(MonomialSystem):
    r"""Finite subsets of \(S\), for \(\Lambda\).

    Not a monoid: \(x\wedge x=0\) and \(x\wedge y=-y\wedge x\), so the product
    carries a sign and may be zero.  Indexing by subsets rather than by
    squarefree monomials is what makes the module the right one --
    \(\Lambda(F_R(S))\) has rank \(2^{|S|}\), which is what a framing by
    subsets says and a framing by all monomials does not.

    The sign is the parity of the shuffle: the number of pairs taken out of
    order when the two sorted subsets are merged.
    """

    @staticmethod
    def _build_parent(labels: "OrderedSet") -> "_MonomialParent":
        r"""Return the finite subsets of \(S\), which is what \(\Lambda\) is free on.

        Finite subsets, not subsets: a monomial is a wedge of finitely many
        generators whatever \(S\) is, so \(\Lambda(F_R(S))\) is free of
        countable rank over a countable \(S\) and \(\Lambda^k\) is free of
        rank \(\binom{|S|}{k}\) at every \(k\).
        """
        from dzack_research.preamble.categories.sets.sets import FiniteSubsets

        subsets: "_MonomialParent" = FiniteSubsets(labels)
        return subsets

    def _subset(self, members: "_Iterable[Element]") -> "Element":
        r"""Return the monomial that is the subset with these members."""
        from dzack_research.preamble.categories.sets.sets import SubsetsOfSize

        members = tuple(members)
        return SubsetsOfSize(self._labels, len(members))(members)

    def _sorted(self, monomial: "Element") -> tuple:
        r"""Return the members in the generating set's own order.

        Its order, not a position looked up in an enumeration: a monomial is
        finite however large \(S\) is, so sorting its members must not depend
        on running through \(S\).
        """
        return tuple(sorted(monomial))

    def one(self) -> "Element":
        return self._subset(())

    def generator(self, label: "Element") -> "Element":
        return self._subset((label,))

    def factors(self, monomial: "Element") -> tuple:
        return tuple((label, 1) for label in self._sorted(monomial))

    def basis_monomial(self, index: "Element") -> "Element":
        return self._subset(tuple(index))

    def product(
        self, left: "Element", right: "Element"
    ) -> tuple["Integer", "Element"]:
        if set(left) & set(right):
            return (0, self.one())
        inversions = sum(
            1 for first in left for second in right if first > second
        )
        return ((-1) ** inversions, self._subset(set(left) | set(right)))

    def monomials_of_degree(self, degree: "Integer | int") -> Parent | tuple:
        r"""Return the subsets of a size: \(\binom{n}{k}\) of them."""
        from dzack_research.preamble.categories.sets.sets import SubsetsOfSize

        subsets: "OrderedSet" = SubsetsOfSize(self._labels, int(degree))
        if int(degree) == 0 or self._labels in Sets().Finite():
            return tuple(subsets)
        of_that_size: Parent = subsets
        return of_that_size


class DividedMonomials(MonomialSystem):
    r"""Divided powers \(\gamma_a(s)\), for \(\Gamma\).

    Indexed exactly as the symmetric algebra is -- \(\Gamma\) is not a
    quotient of \(T\) but has the same monomials -- and multiplied by
    \(\gamma_a(s)\gamma_b(s)=\binom{a+b}{a}\gamma_{a+b}(s)\).  Over \(\QQ\)
    that binomial is invertible and \(\gamma_a(s)=s^a/a!\) makes
    \(\Gamma\cong\operatorname{Sym}\); over \(\ZZ\) it does not, and the
    difference is why \(\Gamma^2\) rather than \(\operatorname{Sym}^2\)
    classifies quadratic forms.
    """

    @staticmethod
    def _build_parent(labels: "OrderedSet") -> "_MonomialParent":
        monoid: "_MonomialParent" = FreeAbelianMonoid(labels)
        return monoid

    def factors(self, monomial: "Element") -> tuple:
        return tuple(monomial.dict().items())

    def product(
        self, left: "Element", right: "Element"
    ) -> tuple["Integer", "Element"]:
        from sage.arith.misc import binomial

        left_exponents = left.dict()
        coefficient = 1
        for label, exponent in right.dict().items():
            coefficient *= binomial(left_exponents.get(label, 0) + exponent, exponent)
        return (coefficient, left * right)

    def monomials_of_degree(self, degree: "Integer | int") -> Parent | tuple:
        if self._labels in Sets().Finite():
            return self._monomials_by_exponent_vector(degree)
        return self._monomials_from_words(degree, injective=False)


class FreeAlgebraIdeal(Ideal_generic):
    r"""An ideal of a free commutative algebra, carrying its normal form.

    A quotient decides equality by comparing normal forms, so an ideal that
    cannot reduce makes \(A/I\) unable to say what it is a quotient by.  The
    normal form is the polynomial one, read through the presentation.
    """

    if TYPE_CHECKING:
        # The ring is the free algebra this ideal was formed in, and its
        # generators are elements of that algebra -- which is what carries
        # the polynomial presentation read below.
        def ring(self) -> "FreeAlgebraParent": ...
        def gens(self) -> tuple["FramedFreeAlgebras.ElementMethods", ...]: ...

    @cached_method
    def _polynomial_ideal(self) -> "_EngineIdeal":
        algebra = self.ring()
        return algebra._polynomial_ring().ideal(
            [algebra._as_polynomial(generator) for generator in self.gens()]
        )

    def reduce(
        self, element: "FramedFreeAlgebras.ElementMethods"
    ) -> "FramedFreeAlgebras.ElementMethods":
        r"""Return the normal form of ``element`` modulo this ideal."""
        algebra = self.ring()
        return algebra._from_polynomial(
            self._polynomial_ideal().reduce(algebra._as_polynomial(element))
        )

    def _contains_(self, element: "FramedFreeAlgebras.ElementMethods") -> bool:
        algebra = self.ring()
        return algebra._as_polynomial(element) in self._polynomial_ideal()


class FramedFreeAlgebras(OwnedCategoryOverBaseRing):
    r"""Free R-algebras equipped with the canonical map \(S \to U(\operatorname{FreeAlg}_R(S))\)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "framed free algebras"

    def super_categories(self) -> list:
        r"""The module level leads: this algebra *is* the framed free module
        on \(\operatorname{Mon}(S)\), and that is how it is constructed --
        :meth:`ParentMethods.__init__` hands that framing to the level above.

        The order is load-bearing and not cosmetic.  A dynamic class takes
        its instance layout from its **first** base (CPython's ``best_base``
        keeps the first winner when two candidates share a solid base), so
        naming the algebra branch first laid an algebra element out on
        ``Element`` rather than on ``ModuleElement``.  Sage's
        ``RightModuleAction._act_`` then casts such an element to
        ``ModuleElement`` unchecked and calls ``_lmul_`` through the wrong
        Cython vtable, which segfaults -- so \(r\cdot x\) crashed on every
        free algebra.
        """
        return [
            FramedFreeModules(self.base_ring()),
            FreeAlgebras(self.base_ring()),
            FramedAlgebras(self.base_ring()),
        ]

    class ParentMethods(UniqueRepresentation):
        r"""\(\operatorname{FreeAlg}_R(S)\), free on \(S\) as an algebra.

        As a module it is free on \(\operatorname{Mon}(S)\), and that framing
        is what the module category above receives.  Which monoid supplies
        the monomials is the datum each construction's own subcategory
        states, so this level writes every operation once for the four free
        constructions.

        ``UniqueRepresentation`` is named here because there must be one free
        algebra on \((R,S)\): two parents on one pair would print alike and
        refuse each other's elements.  It is a Sage implementation class, so
        naming it states how this chain reaches Sage.
        """


        # Installed by the constructor.
        _algebra_generating_set: "OrderedSet"
        _algebra_generating_set_for_morphism: "Set"
        _monomial_system: MonomialSystem
        _monomial_parent: "_MonomialParent"
        _algebra_generator_morphism: SetMorphism

        def __init__(
            self,
            algebra_generating_set: "OrderedSet",
            monomial_system: type[MonomialSystem],
            **rest: "ConstructionData",
        ) -> None:
            r"""Frame the algebra on \(S\), over the monomials of one flavour.

            ``monomial_system`` says which monoid indexes the monomials and
            how two of them multiply.  The subcategory for the construction
            supplies it; the module framing \(\operatorname{Mon}(S)\) is read
            off it and passed to the level above.
            """
            if isinstance(algebra_generating_set, Parent):
                self._algebra_generating_set = algebra_generating_set
            else:
                self._algebra_generating_set = Set(algebra_generating_set)
            self._algebra_generating_set_for_morphism = _as_set(
                self._algebra_generating_set
            )
            self._monomial_system = monomial_system(
                self._algebra_generating_set_for_morphism
            )
            self._monomial_parent = self._monomial_system.parent()
            super().__init__(
                module_generating_set=UnderlyingSet(self._monomial_parent),
                **rest,
            )
            self._algebra_generator_morphism = SetMorphism(
                Hom(
                    self._algebra_generating_set_for_morphism,
                    UnderlyingSet(self),
                    Sets(),
                ),
                self.algebra_generator,
            )

        def number_of_algebra_generators(self: "FreeAlgebraParent") -> "Cardinal":
            r"""Return \(|S|\), the cardinality of the algebra generating set.

            A cardinal, not an integer: a generating set may be infinite, and
            the count of one is the thing that can say so.
            """
            return cardinal(self.algebra_generating_set().cardinality())

        def number_of_module_generators(self: "FreeAlgebraParent") -> "Cardinal":
            r"""Return \(|\operatorname{Mon}(S)|\).

            Two framings, two counts: the module framing is by monomials, so
            this is not \(|S|\) -- it is infinite as soon as \(S\) is
            non-empty.  Cardinality is total on sets, so neither count is
            restricted to the finitely generated case.
            """
            return cardinal(self.module_generating_set().cardinality())

        def hom(
            self: "FreeAlgebraParent",
            images: "SetMorphism | dict | tuple | list | Callable",
            codomain: "Module" = None,
        ) -> "ModuleMorphism":
            r"""Return the algebra map sending each generator to its image.

            Freeness is the whole content:
            \(\operatorname{Hom}_{R\text{-}\mathbf{Alg}}(\operatorname{FreeAlg}_R(S),A)
            =\operatorname{Hom}_{\mathbf{Set}}(S,U(A))\).  An algebra map out
            of here *is* a set map on \(S\), sending each generator to any
            element of \(A\); no further data exists to supply, and none is
            accepted.  Where a monomial goes is then forced, not chosen.

            Sited on the category and not on the concrete parent: a free
            algebra is also a framed free module, whose ``hom`` reads the
            module framing \(\operatorname{Mon}(S)\), and only the more
            specific category can say that the data here is a map on \(S\).
            """
            image_of_generator, codomain_parent = self._generator_images(
                images,
                codomain,
            )
            return FreeAlgebraMorphism(
                free_algebra_homset(self, codomain_parent),
                SetMorphism(
                    Hom(
                        self.module_generating_set(),
                        UnderlyingSet(codomain_parent),
                        Sets(),
                    ),
                    self._extend_to_monomials(image_of_generator, codomain_parent),
                ),
            )

        def induced_hom(
            self: "FreeAlgebraParent", set_morphism: SetMorphism, codomain: "Module"
        ) -> "Morphism":
            r"""Return \(\operatorname{FreeAlg}_R(g)\) for \(g:S\to T\).

            The free construction is a functor, and this is its action on a
            morphism of generating sets: post-compose \(g\) with the
            codomain's own generator map and hand the result to
            :meth:`hom`, which is where a map on \(S\) becomes an algebra
            map.
            """
            assert set_morphism.parent() == Hom(
                self.algebra_generating_set(),
                codomain.algebra_generating_set(),
                Sets(),
            ), "the map must have the two algebra generating sets as endpoints"
            induced: "Morphism" = self.hom(
                lambda label: codomain.algebra_generator(set_morphism(label)),
                codomain,
            )
            return induced

        def _an_element_(self: "FreeAlgebraParent") -> "Element":
            r"""Return \(1+s\) for a generator \(s\), or \(1\) if there are none.

            Named rather than left to be guessed: Sage's default looks for an
            element by *converting a string*, and this algebra's constructor
            rejects one -- so a parent built over this algebra would fail while
            asking it for an example of itself.
            """
            generators = self.algebra_generating_set()
            if generators.cardinality() == 0:
                return self.one()
            return self.one() + self.algebra_generator(
                next(iter(generators))
            )

        def characteristic(self: "FreeAlgebraParent") -> "Integer":
            r"""Return the characteristic, which is the base ring's.

            Adjoining indeterminates adds no additive relation, so nothing
            here can change it.
            """
            characteristic: "Integer" = self.base_ring().characteristic()
            return characteristic

        def is_field(self: "FreeAlgebraParent") -> bool:
            r"""Return whether this algebra is a field.

            A generator is never invertible -- there is no monomial of
            negative degree -- so this is a field exactly when there are no
            generators and the base ring is one.
            """
            if self.number_of_algebra_generators() > 0:
                return False
            return bool(self.base_ring().is_field())

        def is_integral_domain(self: "FreeAlgebraParent") -> bool:
            r"""Return whether this algebra has no zero divisors.

            The degree is additive on products, so a product of nonzero
            elements has the sum of their degrees and cannot vanish -- for
            exactly as long as the base ring has no zero divisors either.
            """
            return bool(self.base_ring().is_integral_domain())

        def krull_dimension(self: "FreeAlgebraParent") -> "Integer":
            r"""Return \(\dim R+|S|\), for \(R\) Noetherian.

            Adjoining one indeterminate raises the dimension by one, which is
            the statement that makes the polynomial ring over a field of
            dimension \(n\) the coordinate ring of \(n\)-space.
            """
            rank = self.number_of_algebra_generators()
            assert rank.is_finite(), (
                "the dimension of an algebra on infinitely many generators is "
                "infinite, and is not read off a finite sum"
            )
            dimension: "Integer" = (
                self.base_ring().krull_dimension() + rank.finite_value()
            )
            return dimension

        def linear_combination(self, coefficients: dict) -> "Element":
            r"""Refuse: an algebra element is built from the algebra generators.

            \(\operatorname{FreeAlg}_R(S)\) is free on \(S\) as an *algebra*
            and on \(\operatorname{Mon}(S)\) as a module.  A combination of
            the elements of \(S\) is neither, so there is nothing for this
            to mean here.
            """
            assert False, (
                "a free algebra's elements are built from its algebra "
                "generators by ring operations, not by linear combination "
                "of the generating set"
            )

        def _element_constructor_(
            self: "FreeAlgebraParent",
            value: "FramedFreeAlgebras.ElementMethods | RingElement",
        ) -> "FramedFreeAlgebras.ElementMethods":
            r"""Return ``value`` as an element of this algebra.

            An \(R\)-algebra comes with its structure map \(R\to A\), so a
            scalar names the element \(r\cdot 1\).  A module has no such map
            and admits only its own elements; an algebra admits its scalars
            too, which is what makes \(0\) and \(1\) elements here and lets
            Sage's ring machinery build ideals over it.
            """
            if isinstance(value, FramedFreeModules.ElementMethods) and value.parent() is self:
                own_element: "FramedFreeAlgebras.ElementMethods" = value
                return own_element
            assert value in self.base_ring(), (
                f"{value} is neither an element of {self} nor a scalar of "
                f"{self.base_ring()}"
            )
            # The structure map \(R\to A\) written in this algebra's own
            # framing: \(1\) is the empty monomial, so \(r\cdot 1\) is the
            # coefficient function carrying \(r\) there.  Not ``r * self.one()``
            # -- that asks Sage's coercion model for the scalar action, and
            # the coercion model reaches this constructor through
            # ``an_element`` while it is still looking for that action.
            system = self.monomial_system()
            monomial_one = (
                system._subset(())
                if isinstance(system, AlternatingMonomials)
                else system.parent().one()
            )
            scalar_multiple: "FramedFreeAlgebras.ElementMethods" = self.element_class(
                self,
                {monomial_one: self.base_ring()(value)},
            )
            return scalar_multiple

        def _engine_base_ring(
            self: "FreeAlgebraParent",
        ) -> "SageRings.ParentMethods":
            r"""Return the base ring as the engine knows how to compute in it.

            A base ring the preamble presents as a quotient -- a number field
            -- is a ring Sage will build polynomials over and then decline to
            factor in, because the algorithms are written for its own number
            fields.  So the crossing translates the coefficients too, and this
            says where they go.  Every other base ring is its own answer.
            """
            # Local: number_fields imports this module, so a module-level
            # import would close that cycle; it is built by the time this
            # method runs.
            from dzack_research.preamble.categories.algebras.number_fields import OwnedNumberFields

            base_ring = self.base_ring()
            if base_ring.category().is_subcategory(OwnedNumberFields()):
                engine_field: "SageRings.ParentMethods" = base_ring._engine_field()
                return engine_field
            # A ring the session names is reported in the session's word;
            # Singular is not told about that word, so the crossing unwraps it
            # here.
            engine_base_ring: "SageRings.ParentMethods" = engine_ring(base_ring)
            return engine_base_ring

        def _as_engine_coefficient(
            self: "FreeAlgebraParent", coefficient: "_NumberFieldCoefficient"
        ) -> "RingElement":
            r"""Return ``coefficient`` in :meth:`_engine_base_ring`."""
            # Local: number_fields imports this module, so a module-level
            # import would close that cycle; it is built by the time this
            # method runs.
            from dzack_research.preamble.categories.algebras.number_fields import OwnedNumberFields

            base_ring = self.base_ring()
            if not base_ring.category().is_subcategory(OwnedNumberFields()):
                # Only a number field's coefficients are written in a basis
                # the engine spells differently; a wrapped ring's elements are
                # the engine's already.
                return coefficient
            # The power basis of the primitive element is what the quotient
            # reduces to, and the engine's generator satisfies the same
            # polynomial, so the coordinates carry over unchanged.
            engine = self._engine_base_ring()
            generator = engine.gen()
            total = engine.zero()
            power = engine.one()
            for entry in coefficient._power_basis_coordinates():
                total += entry * power
                power *= generator
            return total

        def _from_engine_coefficient(
            self: "FreeAlgebraParent", value: "RingElement"
        ) -> "RingElement":
            r"""Return ``value`` back in the base ring."""
            # Local: number_fields imports this module, so a module-level
            # import would close that cycle; it is built by the time this
            # method runs.
            from dzack_research.preamble.categories.algebras.number_fields import OwnedNumberFields

            base_ring = self.base_ring()
            if not base_ring.category().is_subcategory(OwnedNumberFields()):
                return value
            in_the_base_ring: "RingElement" = base_ring._from_engine_element(value)
            return in_the_base_ring

        @cached_method
        def _polynomial_ring(self: "FreeAlgebraParent") -> "_PolynomialRing":
            r"""Return \(R[x_s:s\in S]\), which this algebra *is* for finite \(S\).

            \(R[\operatorname{Mon}(S)]\) built as a module knows its addition
            and its multiplication but not its division; the polynomial ring
            knows both.  The bijection \(S\leftrightarrow\{x_s\}\) is chosen
            here, once, and stays private: what leaves is :meth:`divides`, a
            word about this algebra.

            At rank one the presentation is a ring in one variable and not a
            ring in a family of size one.  They are isomorphic and their
            *algorithms* are not: division with remainder, gcd, root finding
            and factorisation into linear factors are written for one
            variable, and the engine offers them only there.
            """
            self._require_symmetric_polynomial_structure()
            assert self._algebra_generating_set in Sets().Finite(), (
                "the polynomial presentation names one variable per generator, "
                "so it exists for finitely generated free algebras"
            )
            rank = self.number_of_algebra_generators().finite_value()
            engine_base_ring = self._engine_base_ring()
            if rank == 1:
                # Sage's constructor by its private name: the shared namespace
                # binds ``PolynomialRing`` to the delivery, which returns a
                # free algebra -- and this is the crossing *into* the engine,
                # where a free algebra is what we already have.
                in_one_variable: "_PolynomialRing" = _SagePolynomialRing(
                    engine_base_ring, "x"
                )
                return in_one_variable
            in_several: "_PolynomialRing" = _SagePolynomialRing(
                engine_base_ring, rank, "x"
            )
            return in_several

        def _require_symmetric_polynomial_structure(
            self: "FreeAlgebraParent",
        ) -> None:
            r"""Require the commutative polynomial structure used by these algorithms."""
            assert self in SymmetricAlgebras(self.base_ring()), (
                "polynomial factorization, division, roots, and leading terms "
                "belong to the symmetric algebra"
            )

        @cached_method
        def _polynomial_variables(self: "FreeAlgebraParent") -> dict:
            return dict(
                zip(self._algebra_generating_set, self._polynomial_ring().gens())
            )

        def _as_polynomial(
            self: "FreeAlgebraParent", element: "FreeAlgebraElement"
        ) -> "_EnginePolynomial":
            r"""Transport ``element`` along the polynomial presentation.

            Built by handing the ring its coefficients, not by multiplying its
            variables together.  The two agree as elements, and only the first
            is the ring *constructing* one: a ring whose elements carry more
            than their own class -- a category refinement, say -- gives that to
            what it constructs, and Cython arithmetic does not.
            """
            ring = self._polynomial_ring()
            labels = tuple(self._algebra_generating_set)
            position_of = {label: position for position, label in enumerate(labels)}
            zero = self.base_ring().zero()
            terms: dict = {}
            system = self.monomial_system()
            for monomial, coefficient in element.coefficients().items():
                exponents = [0] * len(labels)
                for label, exponent in system.factors(monomial):
                    exponents[position_of[label]] = exponent
                key = exponents[0] if len(labels) == 1 else tuple(exponents)
                terms[key] = terms.get(key, zero) + coefficient
            presented: "_EnginePolynomial" = ring(
                {
                    key: self._as_engine_coefficient(value)
                    for key, value in terms.items()
                }
            )
            return presented

        def ideal(
            self: "FreeAlgebraParent", generators: "OrderedSet"
        ) -> FreeAlgebraIdeal:
            r"""Return the ideal generated by ``generators``, with its normal form."""
            # Local: the set node reaches this module, so a module-level
            # import would close that cycle; it is built by the time this
            # method runs.
            from dzack_research.preamble.categories.sets.sets import finite_ordered_set

            return FreeAlgebraIdeal(
                self,
                [self(generator) for generator in finite_ordered_set(generators)],
            )

        def _from_polynomial(
            self: "FreeAlgebraParent", polynomial: "_EnginePolynomial"
        ) -> "FramedFreeAlgebras.ElementMethods":
            r"""Transport ``polynomial`` back along the polynomial presentation.

            A polynomial in one variable indexes its coefficients by an
            exponent and one in several by a tuple of them; both are the same
            statement about \(\operatorname{Mon}(S)\), read here in whichever
            form the presentation used.
            """
            system = self.monomial_system()
            labels = tuple(self._algebra_generating_set)
            result: "FramedFreeAlgebras.ElementMethods" = self.zero()
            for exponents, coefficient in polynomial.dict().items():
                # One variable indexes by an exponent, several by a sequence
                # of them -- and the engine's sequence is its own type, not a
                # tuple.
                exponents = (
                    tuple(exponents)
                    if isinstance(exponents, _Iterable)
                    else (exponents,)
                )
                monomial = system.parent().one()
                for label, exponent in zip(labels, exponents):
                    monomial *= system.parent().gen(label) ** exponent
                result += self._from_engine_coefficient(coefficient) * (
                    self.module_generator(monomial)
                )
            return result

        def monomial_system(self: "FreeAlgebraParent") -> MonomialSystem:
            r"""Return how this algebra's monomials are indexed and multiplied.

            The one place any construction-specific fact about monomials
            lives: what the unit is, what a generator is, how one reads off
            exponents, and what two of them multiply to.
            """
            return self._monomial_system

        def monomial_parent(self: "FreeAlgebraParent") -> "_MonomialParent":
            r"""Return the parent the monomials live in.

            The module framing is indexed by it, and the product on it is the
            algebra's: \(\operatorname{FreeAlg}_R(S)=R[\operatorname{Mon}(S)]\)
            for the symmetric flavour, and the same statement with the other
            monomials for the rest.  :meth:`module_generating_set` is its
            underlying set, which no longer multiplies, so monomial questions
            go to :meth:`monomial_system`.
            """
            return self._monomial_parent

        def _algebra_generator_label(
            self: "FreeAlgebraParent", monomial: "_SageElement"
        ) -> "_SageElement":
            monomial_profile = dict(self.monomial_system().factors(monomial))
            assert len(monomial_profile) == 1, (
                f"{monomial!r} is not a degree-1 monomial; the profile is "
                f"{monomial_profile}"
            )
            label, exponent = next(iter(monomial_profile.items()))
            assert exponent == 1, (
                f"{monomial!r} is not a generator monomial; exponent profile is "
                f"{monomial_profile}"
            )
            generator_label: "_SageElement" = label
            return generator_label

        def _algebra_to_monomial(
            self: "FreeAlgebraParent", s: "_SageElement"
        ) -> "_SageElement":
            system = self.monomial_system()
            monomial: "_SageElement" = (
                system._subset((s,))
                if isinstance(system, AlternatingMonomials)
                else system.parent().gen(s)
            )
            return monomial

        def _ring_morphism_defining_algebra_structure(
            self: "FreeAlgebraParent",
        ) -> "Morphism":
            r"""Return $R\to Z(A)$, $r\mapsto r\cdot 1$.

            A free construction has its structure morphism for free: the
            scalars enter as multiples of the unit, and they are central
            because the monomials commute with them by construction.
            """
            # Local: a module-level import here would close a cycle; by call
            # time this module is built.
            from sage.categories.rings import Rings

            return SetMorphism(
                Hom(self.base_ring(), self, Rings()),
                lambda scalar: scalar * self.one(),
            )

        def algebra_generating_set(self: "FreeAlgebraParent") -> "OrderedSet":
            r"""Return the original set ``S`` (not ``Mon(S)``)."""
            return self._algebra_generating_set

        def algebra_generator_morphism(self: "FreeAlgebraParent") -> SetMorphism:
            """Return the framing map from algebra generators to the free algebra."""
            return self._algebra_generator_morphism

        def algebra_generator(
            self: "FreeAlgebraParent", s: "_SageElement"
        ) -> "FramedFreeAlgebras.ElementMethods":
            r"""Return the degree-1 monomial ``[s]`` in ``FreeAlg_R(S)``."""
            assert s in self._algebra_generating_set, (
                f"{s!r} is not in {self._algebra_generating_set}"
            )
            generator: "FramedFreeAlgebras.ElementMethods" = self.module_generator(
                self._algebra_to_monomial(s)
            )
            return generator

        def algebra_generators(self: "FreeAlgebraParent") -> tuple:
            r"""Return algebra generators when the framing set is finite."""
            assert self._algebra_generating_set in Sets().Finite(), (
                "algebra_generators() is defined only for finitely generated "
                "framed free algebras; use algebra_generator(s) for arbitrary "
                "sets"
            )
            return tuple(
                self.algebra_generator(s) for s in self._algebra_generating_set
            )

        def product_on_algebra_generators(
            self: "FreeAlgebraParent", s: "_SageElement", t: "_SageElement"
        ) -> "FramedFreeAlgebras.ElementMethods":
            r"""Return the product of algebra generators s and t."""
            product: "FramedFreeAlgebras.ElementMethods" = (
                self.algebra_generator(s) * self.algebra_generator(t)
            )
            return product

        def _generator_images(
            self: "FreeAlgebraParent",
            images: "SetMorphism | dict | tuple | list | Callable",
            codomain: "Module",
        ) -> "tuple[Callable, Module]":
            r"""Return ``(f, A)``: the map on \(S\) naming an algebra morphism.

            Each spelling below names the same thing -- where every generator
            goes.  A partial assignment names no morphism, and is refused.
            """
            match images:
                case SetMorphism():
                    assert (
                        images.domain()
                        == self._algebra_generating_set_for_morphism
                    ), (
                        "a generator map is defined on this algebra's "
                        "generating set"
                    )
                    return images._call_, images.codomain().structured_parent()
                case dict():
                    values = dict(images)
                    assert set(values) == set(self._algebra_generating_set), (
                        f"{self!r} is generated by {self._algebra_generating_set}; "
                        f"an assignment names the image of every one of them, "
                        f"and this one names {sorted(values)}"
                    )
                    target = next(iter(values.values())).parent()
                    assert all(
                        value.parent() is target for value in values.values()
                    ), "the images of the generators lie in one codomain"
                    return values.__getitem__, target
                case list() | tuple():
                    assert codomain is not None, (
                        "images listed in generator order require their codomain"
                    )
                    return (
                        self._from_algebra_generator_values(
                            codomain, tuple(images)
                        ).__getitem__,
                        codomain,
                    )
                case _ if callable(images):
                    assert codomain is not None, (
                        "a generator function requires its codomain"
                    )
                    return images, codomain
                case _:
                    assert False, (
                        "an algebra map out of a free algebra is named by the "
                        "images of its algebra generators: an assignment, a "
                        "list in generator order, or a map on the generating set"
                    )

        def _extend_to_monomials(
            self: "FreeAlgebraParent",
            image_of_generator: "Callable",
            codomain: "Module",
        ) -> "Callable":
            r"""Return the forced map on \(\operatorname{Mon}(S)\).

            \(\prod s^{e_s}\mapsto\prod f(s)^{e_s}\): multiplicativity leaves
            no choice, which is what makes the map on \(S\) the whole of the
            data.
            """

            def image_of_monomial(monomial: "Element") -> "Element":
                image = codomain.one()
                for label, exponent in self.monomial_system().factors(monomial):
                    image *= image_of_generator(label) ** exponent
                return image

            return image_of_monomial

        def _from_algebra_generator_values(
            self: "FreeAlgebraParent",
            codomain: "Module",
            values: tuple["ModuleElement", ...],
        ) -> dict["Element", "ModuleElement"]:
            assert self._algebra_generating_set in Sets().Finite(), (
                "a finite assignment requires a finite algebra generating set"
            )
            algebra_generating_set_cardinality = (
                self._algebra_generating_set.cardinality()
            )
            assert len(values) == algebra_generating_set_cardinality, (
                f"{self!r} has {algebra_generating_set_cardinality} algebra "
                f"generators, got {len(values)}"
            )
            assert all(value in codomain for value in values), (
                "all values in a finite assignment must belong to the "
                "specified codomain"
            )
            return dict(zip(self._algebra_generating_set, values, strict=True))

        def one(self: "FreeAlgebraParent") -> "FramedFreeAlgebras.ElementMethods":
            r"""Return the multiplicative identity: the empty monomial."""
            system = self.monomial_system()
            monomial_one = (
                system._subset(())
                if isinstance(system, AlternatingMonomials)
                else system.parent().one()
            )
            one: "FramedFreeAlgebras.ElementMethods" = self.module_generator(
                monomial_one
            )
            return one

        def _first_ngens(self: "FreeAlgebraParent", count: int) -> tuple:
            r"""Return the first ``count`` generators, for the ``R.<x, y> =`` sugar.

            The preparser expands that binding into a call and this reader;
            both are Sage's spelling of what this category already answers
            with :meth:`algebra_generators`.
            """
            return tuple(self.algebra_generators())[:count]

    class ElementMethods:
        def _mod_(self, other: "Element") -> "FramedFreeAlgebras.ElementMethods":
            r"""Return this element reduced modulo ``other``.

            Equality in \(A/(g)\) is equality of remainders, so a quotient of
            this algebra can only decide it once division with remainder is
            available here.
            """
            parent = self.parent()
            reduced: "FramedFreeAlgebras.ElementMethods" = parent._from_polynomial(
                parent._as_polynomial(self) % parent._as_polynomial(other)
            )
            return reduced

        def divides(self, other: "Element") -> bool:
            r"""Return whether this element divides ``other`` in the algebra.

            Divisibility is the ring question the module construction cannot
            answer, and it is what membership in a principal ideal *is*.
            """
            assert other.parent() is self.parent(), (
                "divisibility is a question inside one algebra"
            )
            parent = self.parent()
            divides: bool = parent._as_polynomial(self).divides(
                parent._as_polynomial(other)
            )
            return divides

        def _mul_(
            self,
            other: "ElementConstructorInput",
        ) -> "FramedFreeAlgebras.ElementMethods":
            assert (
                isinstance(other, FramedFreeAlgebras.ElementMethods)
                and other.parent() is self.parent()
            ), "free-algebra multiplication requires elements of one parent"
            parent = self.parent()
            zero = parent.base_ring().zero()
            coefficients: dict["Element", "RingElement"] = {}
            for left_monomial, left_coefficient in self.coefficients().items():
                for right_monomial, right_coefficient in other.coefficients().items():
                    sign, monomial = parent.monomial_system().product(
                        left_monomial, right_monomial
                    )
                    if sign == 0:
                        continue
                    coefficients[monomial] = parent.base_ring()(
                        coefficients.get(monomial, zero)
                        + sign * left_coefficient * right_coefficient
                    )
            product: "FramedFreeAlgebras.ElementMethods" = parent.element_class(
                parent, coefficients
            )
            return product

        def underlying_set_element(self) -> "_SageElement":
            r"""Recover the algebra label ``s`` when this element is ``[s]``."""
            assert len(self._coefficients) == 1, (
                "only an element in the image of the canonical algebra generator map "
                "has one underlying element of S"
            )
            monomial, coefficient = next(iter(self._coefficients.items()))
            assert coefficient == self.parent().base_ring().one(), (
                "only an element in the image of the canonical algebra generator map "
                "has coefficient one"
            )
            label: "_SageElement" = self.parent()._algebra_generator_label(monomial)
            return label

        def multidegree(self: "FreeAlgebraElement") -> dict:
            r"""Return \(s\mapsto\deg_s\), the degree in each generator.

            Also canonical at every rank, and for a different reason than a
            leading monomial: no order on \(\operatorname{Mon}(S)\) is chosen
            here.  \(\deg_s\) is the largest exponent of \(s\) over the
            support, so the answer is a function on \(S\) -- given as the part
            that is nonzero, since a generator absent from the support has
            degree zero and there may be infinitely many of those.
            """
            degrees: dict = {}
            system = self.parent().monomial_system()
            for monomial in self.coefficients():
                for label, exponent in system.factors(monomial):
                    if exponent > degrees.get(label, 0):
                        degrees[label] = exponent
            return degrees

        # ---------------------------------------------------------------
        # Coefficients, read off the framing.  An element *is* a finitely
        # supported function on Mon(S), so these are lookups and not
        # questions for an engine.
        # ---------------------------------------------------------------

        def coefficient(
            self: "FreeAlgebraElement", monomial: "Element"
        ) -> "RingElement":
            r"""Return the coefficient of ``monomial``, zero when absent."""
            return self.coefficients().get(
                monomial, self.parent().base_ring().zero()
            )

        def constant_coefficient(self: "FreeAlgebraElement") -> "RingElement":
            r"""Return the coefficient of \(1\): this element's value at zero."""
            system = self.parent().monomial_system()
            monomial_one = (
                system._subset(())
                if isinstance(system, AlternatingMonomials)
                else system.parent().one()
            )
            return self.coefficient(monomial_one)

        def leading_coefficient(self: "FreeAlgebraElement") -> "RingElement":
            r"""Return the coefficient of the top-degree part, at rank one.

            Above rank one 'leading' is a choice of monomial order, which this
            algebra does not make -- see :meth:`multidegree`, which needs none.
            """
            parent = self.parent()
            parent._require_symmetric_polynomial_structure()
            assert parent.number_of_algebra_generators() == 1, (
                "a leading coefficient at higher rank names a monomial order, "
                "and none is chosen here"
            )
            top = self.degree()
            if top == -_Infinity:
                return parent.base_ring().zero()
            system = parent.monomial_system()
            return next(
                coefficient
                for monomial, coefficient in self.coefficients().items()
                if system.degree(monomial) == top
            )

        def is_monic(self: "FreeAlgebraElement") -> bool:
            r"""Return whether the leading coefficient is \(1\)."""
            monic: bool = self.leading_coefficient() == self.parent().base_ring().one()
            return monic

        def monic(self: "FreeAlgebraElement") -> "Element":
            r"""Return this element scaled to leading coefficient \(1\)."""
            leading = self.leading_coefficient()
            assert leading.is_unit(), (
                "scaling to a monic element requires a unit leading "
                "coefficient"
            )
            return self.parent().base_ring()(leading**-1) * self

        # ---------------------------------------------------------------
        # Division, factorisation and roots.  Each is an algorithm rather
        # than a definition, so each crosses to the engine at the algebra's
        # own presentation -- once -- and comes back as algebra elements.
        # ---------------------------------------------------------------

        def derivative(self: "FreeAlgebraElement", label: "Element" = None) -> "Element":
            r"""Return \(\partial/\partial s\) for the generator \(s\).

            A derivation of the algebra, determined by where it sends the
            generators -- so it is asked with a generator's label, and only
            an algebra of rank one may leave that open.
            """
            parent = self.parent()
            if label is None:
                assert parent.number_of_algebra_generators() == 1, (
                    "which generator to differentiate in is only obvious at "
                    "rank one"
                )
                label = tuple(parent.algebra_generating_set())[0]
            variable = parent._polynomial_variables()[label]
            return parent._from_polynomial(
                parent._as_polynomial(self).derivative(variable)
            )

        def quo_rem(self: "FreeAlgebraElement", other: "Element") -> tuple:
            r"""Return \((q,r)\) with ``self`` \(=q\cdot\)``other``\(+r\)."""
            parent = self.parent()
            quotient, remainder = parent._as_polynomial(self).quo_rem(
                parent._as_polynomial(other)
            )
            return (
                parent._from_polynomial(quotient),
                parent._from_polynomial(remainder),
            )

        def gcd(self: "FreeAlgebraElement", other: "Element") -> "Element":
            r"""Return a greatest common divisor of the two."""
            parent = self.parent()
            return parent._from_polynomial(
                parent._as_polynomial(self).gcd(parent._as_polynomial(other))
            )

        def lcm(self: "FreeAlgebraElement", other: "Element") -> "Element":
            r"""Return a least common multiple of the two."""
            parent = self.parent()
            return parent._from_polynomial(
                parent._as_polynomial(self).lcm(parent._as_polynomial(other))
            )

        def xgcd(self: "FreeAlgebraElement", other: "Element") -> tuple:
            r"""Return \((g,a,b)\) with \(g=a\cdot\)``self``\(+b\cdot\)``other``."""
            parent = self.parent()
            return tuple(
                parent._from_polynomial(entry)
                for entry in parent._as_polynomial(self).xgcd(
                    parent._as_polynomial(other)
                )
            )

        def is_irreducible(self: "FreeAlgebraElement") -> bool:
            r"""Return whether this element is irreducible in the algebra."""
            return bool(self.parent()._as_polynomial(self).is_irreducible())

        def irreducible_factors(self: "FreeAlgebraElement") -> tuple:
            r"""Return the irreducible factors with their multiplicities.

            The unit is not among them: over a field it is
            :meth:`leading_coefficient`, and reporting it as a factor would
            make a unit look like an irreducible.
            """
            parent = self.parent()
            return tuple(
                (parent._from_polynomial(factor), multiplicity)
                for factor, multiplicity in parent._as_polynomial(self).factor()
            )

        def resultant(self: "FreeAlgebraElement", other: "Element") -> "Element":
            r"""Return \(\operatorname{Res}\) of the two, at rank one.

            An element of the base ring: it vanishes exactly when the two have
            a common root in an extension, which is what makes it the tool it
            is.
            """
            assert self.parent().number_of_algebra_generators() == 1, (
                "the resultant eliminates one variable, and which one is only "
                "obvious at rank one"
            )
            parent = self.parent()
            return parent._as_polynomial(self).resultant(
                parent._as_polynomial(other)
            )

        def discriminant(self: "FreeAlgebraElement") -> "Element":
            r"""Return \(\operatorname{disc}\), zero exactly on a repeated root."""
            assert self.parent().number_of_algebra_generators() == 1, (
                "the discriminant is the resultant with the derivative, and "
                "that names a variable"
            )
            return self.parent()._as_polynomial(self).discriminant()

        def roots(
            self: "FreeAlgebraElement", ring: "Ring" = None, multiplicities: bool = True
        ) -> list:
            r"""Return the roots of this element, with multiplicities.

            ``ring`` left open means the base ring, as it does everywhere.
            """
            assert self.parent().number_of_algebra_generators() == 1, (
                "roots are the zeros of an element of an algebra of rank one; "
                "of higher rank the zero locus is a variety"
            )
            presented = self.parent()._as_polynomial(self)
            if ring is None:
                return presented.roots(multiplicities=multiplicities)
            if isinstance(ring, (_AlgebraicRealFieldType, _RealIntervalFieldType)):
                # The engine isolates real roots in the Bernstein basis
                # through a mutable ZZ^{n+1} buffer, which a module element is
                # not.  The real roots are the algebraic numbers of zero
                # imaginary part, so the algebraic closure answers the same
                # question and is isolated without one.
                over_the_closure = presented.roots(
                    ring=_AlgebraicNumbers, multiplicities=True
                )
                real_roots = sorted(
                    (
                        (ring(root), multiplicity)
                        for root, multiplicity in over_the_closure
                        if root.imag().is_zero()
                    ),
                    key=lambda pair: pair[0],
                )
                if multiplicities:
                    return real_roots
                return [root for root, _ in real_roots]
            return presented.roots(ring=ring, multiplicities=multiplicities)

        def any_root(self: "FreeAlgebraElement", ring: "Ring" = None) -> "Element":
            r"""Return one root, in ``ring`` when given."""
            roots = self.roots(ring=ring, multiplicities=False)
            assert roots, "this element has no root in that ring"
            return roots[0]

        def monomials(self: "FreeAlgebraElement") -> tuple:
            r"""Return the monomials this element is supported on."""
            return tuple(self.coefficients())

        def is_constant(self: "FreeAlgebraElement") -> bool:
            r"""Return whether this element lies in the base ring."""
            constant: bool = self.degree() <= 0
            return constant

        def is_squarefree(self: "FreeAlgebraElement") -> bool:
            r"""Return whether no irreducible divides this element twice.

            Decided by \(\gcd(f,f')\), which is a unit exactly then -- so it
            needs no factorisation, and the derivative it needs is this
            algebra's own.
            """
            assert self.parent().number_of_algebra_generators() == 1, (
                "the criterion by the derivative names a variable; at higher "
                "rank squarefreeness is decided by factorisation"
            )
            if self == self.parent().zero():
                return False
            squarefree: bool = self.gcd(self.derivative()).degree() == 0
            return squarefree

        def complex_roots(self: "FreeAlgebraElement") -> tuple:
            r"""Return the roots in \(\overline{\QQ}\), where there are \(\deg\) of them.

            The algebraically closed answer, which is the one the degree
            counts: over the base ring there may be fewer.
            """
            return tuple(self.roots(ring=_AlgebraicNumbers, multiplicities=True))

        def content(self: "FreeAlgebraElement") -> "Element":
            r"""Return the gcd of the coefficients.

            A statement about the coefficients, so it is read off the framing:
            the element is primitive exactly when this is a unit, and Gauss's
            lemma is what makes that multiplicative.
            """
            coefficients = tuple(self.coefficients().values())
            if not coefficients:
                return self.base_ring().zero()
            content = coefficients[0]
            for coefficient in coefficients[1:]:
                content = content.gcd(coefficient)
            return content

        def denominator(self: "FreeAlgebraElement") -> "Element":
            r"""Return the least common denominator of the coefficients."""
            denominator = self.base_ring().one()
            for coefficient in self.coefficients().values():
                denominator = denominator.lcm(coefficient.denominator())
            return denominator

        def numerator(self: "FreeAlgebraElement") -> "Element":
            r"""Return this element cleared of denominators.

            The same element scaled by :meth:`denominator`, so its
            coefficients are integral -- which is what lets a factorisation
            over \(\ZZ\) speak about a rational polynomial.
            """
            return self.denominator() * self

        def change_ring(self: "FreeAlgebraElement", ring: "Ring") -> "Element":
            r"""Return this element with its coefficients moved to ``ring``.

            The image under \(\operatorname{FreeAlg}_R(S)\to
            \operatorname{FreeAlg}_{R'}(S)\), the free construction applied to
            a map of base rings: the generating set is untouched, which is
            what makes the two algebras comparable at all.
            """
            target = FreeAlgebraOn(
                ring, self.parent().algebra_generating_set()
            )
            image = target.zero()
            system = self.parent().monomial_system()
            for monomial, coefficient in self.coefficients().items():
                term = ring(coefficient) * target.one()
                for label, exponent in system.factors(monomial):
                    term = term * target.algebra_generator(label) ** exponent
                image = image + term
            return image

        def subs(self: "FreeAlgebraElement", values: dict) -> "Element":
            r"""Return the value of this element at ``values``, keyed by label.

            Evaluation is the universal property, so it is the algebra map out
            of a free algebra determined by where the generators go -- and a
            partial assignment leaves the rest of them alone.
            """
            parent = self.parent()
            zero = parent.base_ring().zero()
            total = zero
            system = parent.monomial_system()
            for monomial, coefficient in self.coefficients().items():
                term = coefficient
                for label, exponent in system.factors(monomial):
                    if label in values:
                        term = term * values[label] ** exponent
                    else:
                        term = term * parent.algebra_generator(label) ** exponent
                total = total + term
            return total

        def __call__(
            self: "FreeAlgebraElement",
            *values: "ElementConstructorInput",
        ) -> "Element":
            r"""Evaluate at the generators in their framing's order."""
            labels = tuple(self.parent().algebra_generating_set())
            assert len(values) == len(labels), (
                f"this algebra has {len(labels)} generators, got {len(values)} "
                "values"
            )
            return self.subs(dict(zip(labels, values)))

    class Homsets(HomsetsCategory):
        r"""Algebra homsets whose domain is free on a specified set."""

        def extra_super_categories(self) -> list:
            return [FramedAlgebras(self.base_category().base_ring()).Homsets()]

        class ElementMethods:
            def then(
                self: "FreeAlgebraMorphism", other: ModuleMorphism
            ) -> "FreeAlgebraMorphism":
                r"""Return ``other`` after this algebra morphism."""
                assert other.domain() is self.codomain(), (
                    "the codomain of the first map must be the domain of the second"
                )
                domain = self.domain()
                codomain = other.codomain()
                return FreeAlgebraMorphism(
                    free_algebra_homset(domain, codomain),
                    SetMorphism(
                        Hom(
                            domain.module_generating_set(),
                            UnderlyingSet(codomain),
                            Sets(),
                        ),
                        lambda module_generator: other(self(module_generator)),
                    ),
                )



class FreeAlgebraMorphism(ModuleMorphism):
    r"""Algebra morphisms are module maps on monomial generators."""

    def _domain_module_generating_set(self) -> Parent:
        generating_set: Parent = self.domain().module_generating_set()
        return generating_set

class DividedPowerAlgebraMorphism(FreeAlgebraMorphism):
    r"""An algebra morphism constructed to preserve all divided powers."""


def free_algebra_homset(
    domain: "FreeAlgebraParent", codomain: "Module"
) -> Parent:
    r"""Return the algebra homset from a specified free algebra."""
    return object_of(
        FramedFreeAlgebras(domain.base_ring()).Homsets(),
        domain=domain,
        codomain=codomain,
    )


def divided_power_algebra_homset(
    domain: "FreeAlgebraParent", codomain: "Module"
) -> Parent:
    r"""Return the divided-power algebra homset with the stated ends."""
    return object_of(
        FramedDividedPowerAlgebras(domain.base_ring()).Homsets(),
        domain=domain,
        codomain=codomain,
    )


class FramedSymmetricAlgebras(OwnedCategoryOverBaseRing):
    r"""\(\operatorname{Sym}(F_R(S))=R[S]\), framed by \(S\).

    Monomials are the free commutative monoid on \(S\), which is the
    polynomial algebra written out.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "framed symmetric algebras"

    def super_categories(self) -> list:
        return [
            FramedFreeAlgebras(self.base_ring()),
            SymmetricAlgebras(self.base_ring()),
        ]

    class ParentMethods:
        def __init__(self, **rest: "ConstructionData") -> None:
            super().__init__(monomial_system=CommutativeMonomials, **rest)

        def _repr_(self: "FreeAlgebraParent") -> str:
            return (
                f"Free {self.base_ring()}-algebra on "
                f"{self.algebra_generating_set()}"
            )


def FreeAlgebraOn(
    base_ring: "Ring", algebra_generating_set: "OrderedSet"
) -> "FreeAlgebraParent":
    r"""Return \(\operatorname{FreeAlg}_R(S)\), the same object on every call.

    \(\operatorname{FreeAlg}_R(-)\) is a functor, so \((R,S)\) names one
    algebra.  The ``ParentMethods`` of these categories name
    ``UniqueRepresentation``, which is what makes that hold however the
    algebra is reached.

    A ring and the owned view of it are one ring, so both name the same
    algebra: the object is built over the engine either way, and two spellings
    must not give two incomparable parents.
    """
    return object_of(
        FramedSymmetricAlgebras(engine_ring(base_ring)),
        algebra_generating_set=algebra_generating_set,
    )


def polynomial_ring(
    base_ring: "Ring",
    *arguments: "ElementConstructorInput",
    **keywords: "ElementConstructorInput",
) -> "FreeAlgebraParent":
    r"""Return \(R[x_s:s\in S]\) as the free \(R\)-algebra on \(S\).

    A polynomial ring is not a separate construction: it *is* the free
    commutative algebra on its variables, and a notebook that asks for one
    receives that object.  Sage's own polynomial rings stay behind the
    boundary as the engine the algorithms run in; nothing here hands one out.

    The variables may be named -- ``"x"``, ``"x, y"``, a family of labels --
    or counted, which names them \(x_0,\dots\).  Both at once is how
    ``R.<x, y> = PolynomialRing(QQ, 2)`` reaches here, and the names win: the
    count is the length they already have.
    """
    # Local: the set node reaches this module, so a module-level import would
    # close that cycle; it is built by the time this function runs.
    from dzack_research.preamble.categories.sets.sets import finite_ordered_set

    names: "OrderedSet | str | tuple[str, ...] | None" = keywords.pop("names", None)
    counted = None
    for argument in arguments:
        if isinstance(argument, (int, _SageIntegerType)):
            counted = argument
        elif names is None:
            names = argument
    if names is None:
        assert counted is not None, (
            "a polynomial ring needs its variables named or counted"
        )
        names = tuple(f"x{index}" for index in range(counted))
    match names:
        case str():
            labels = tuple(
                part.strip() for part in names.split(",") if part.strip()
            )
            if counted is not None and len(labels) == 1 and counted != 1:
                # A count and one name is a *prefix*: n variables called
                # x0, ..., x(n-1), which is how Sage spells it.
                labels = tuple(f"{labels[0]}{index}" for index in range(counted))
        case _:
            labels = tuple(names)
    assert counted is None or len(labels) == counted, (
        f"{counted} variables were asked for and {len(labels)} were named"
    )
    return FreeAlgebraOn(base_ring, finite_ordered_set(labels))


class FramedTensorAlgebras(OwnedCategoryOverBaseRing):
    r"""The tensor algebra \(T(F_R(S))=R\langle S\rangle\), framed by \(S\).

    The same construction as the symmetric algebra beside it, over the free
    monoid instead of the free abelian one: monomials are words in \(S\), so
    the generators no longer commute and the degree-\(n\) piece is
    \(F_R(S)^{\otimes n}\).

    \(T\) is left adjoint to the forgetful functor to modules, so this is
    \(T(M)\) for \(M\) free on \(S\).  For a framed \(M=F_R(S)/K\) the
    tensor algebra is this one modulo the two-sided ideal generated by
    \(K\), which sits in degree one and so leaves the grading intact.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "framed tensor algebras"

    def super_categories(self) -> list:
        return [
            FramedFreeAlgebras(self.base_ring()),
            TensorAlgebras(self.base_ring()),
        ]

    class ParentMethods:
        def __init__(self, **rest: "ConstructionData") -> None:
            super().__init__(monomial_system=WordMonomials, **rest)

        def _repr_(self: "FreeAlgebraParent") -> str:
            return (
                f"Tensor algebra over {self.base_ring()} on "
                f"{self.algebra_generating_set()}"
            )


def TensorAlgebraOn(
    base_ring: "Ring", algebra_generating_set: "OrderedSet"
) -> "FreeAlgebraParent":
    r"""Return \(T(F_R(S))\), the same object on every call."""
    return object_of(
        FramedTensorAlgebras(engine_ring(base_ring)),
        algebra_generating_set=algebra_generating_set,
    )


class FramedAlternatingAlgebras(OwnedCategoryOverBaseRing):
    r"""The alternating algebra \(\Lambda(F_R(S))=T(M)/\langle x\otimes x\rangle\), framed by \(S\).

    Framed by the subsets of \(S\), so \(\Lambda(F_R(S))\) is free of rank
    \(2^{|S|}\) and \(\Lambda^k\) of rank \(\binom{n}{k}\) -- which is
    the statement a framing by squarefree monomials inside all monomials would
    not make.  The product is the shuffle sign, and zero when a generator
    repeats.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "framed alternating algebras"

    def super_categories(self) -> list:
        return [
            FramedFreeAlgebras(self.base_ring()),
            AlternatingAlgebras(self.base_ring()),
        ]

    class ParentMethods:
        def __init__(self, **rest: "ConstructionData") -> None:
            super().__init__(monomial_system=AlternatingMonomials, **rest)

        def _repr_(self: "FreeAlgebraParent") -> str:
            return (
                f"Alternating algebra over {self.base_ring()} on "
                f"{self.algebra_generating_set()}"
            )


def AlternatingAlgebraOn(
    base_ring: "Ring", algebra_generating_set: "OrderedSet"
) -> "FreeAlgebraParent":
    r"""Return \(\Lambda(F_R(S))\), the same object on every call."""
    return object_of(
        FramedAlternatingAlgebras(engine_ring(base_ring)),
        algebra_generating_set=algebra_generating_set,
    )


class FramedDividedPowerAlgebras(OwnedCategoryOverBaseRing):
    r"""The divided power algebra \(\Gamma(F_R(S))\), framed by \(S\).

    Framed by the same monomials as the symmetric algebra -- \(\Gamma\) is
    not a quotient of \(T\) -- and multiplied by
    \(\gamma_a\gamma_b=\binom{a+b}{a}\gamma_{a+b}\).  Over \(\QQ\) the
    map \(\gamma_a(x)\mapsto x^a/a!\) is an isomorphism to
    \(\operatorname{Sym}\); over \(\ZZ\) it is not, and \(\Gamma^2\) is
    what represents quadratic forms.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "framed divided power algebras"

    def super_categories(self) -> list:
        return [
            FramedFreeAlgebras(self.base_ring()),
            DividedPowerAlgebras(self.base_ring()),
        ]

    class ParentMethods:
        def __init__(self, **rest: "ConstructionData") -> None:
            super().__init__(monomial_system=DividedMonomials, **rest)

        def divided_power(
            self: "FreeAlgebraParent",
            value: "Element",
            exponent: "Integer | int",
        ) -> "Element":
            r"""Return \(\gamma_a(x)\), which is *not* \(x^a\).

            \(s^a=a!\,\gamma_a(s)\), so over \(\ZZ\) the powers of a
            generator span a proper submodule of what the divided powers
            span.  Naming the monomial directly is the only way to reach the
            rest.
            """
            exponent = int(exponent)
            system = self.monomial_system()
            match value:
                case FramedFreeAlgebras.ElementMethods() if value.parent() is self:
                    assert value.degree() == 1 or value == self.zero(), (
                        "divided powers are defined here on degree-one elements"
                    )
                    terms = tuple(value.coefficients().items())
                    from sage.combinat.integer_vector import IntegerVectors

                    result = self.zero()
                    for powers in IntegerVectors(exponent, len(terms)):
                        monomial = system.parent().one()
                        coefficient = self.base_ring().one()
                        for (generator_monomial, scalar), power in zip(
                            terms, powers
                        ):
                            label = self._algebra_generator_label(
                                generator_monomial
                            )
                            monomial *= system.parent().gen(label) ** power
                            coefficient *= scalar**power
                        result += coefficient * self.module_generator(monomial)
                    return result
                case _:
                    assert value in self._algebra_generating_set, (
                        f"{value!r} is not in {self._algebra_generating_set}"
                    )
                    return self.module_generator(
                        system.parent().gen(value) ** exponent
                    )

        def divided_square(
            self: "FreeAlgebraParent", element: "Element"
        ) -> "Element":
            r"""Return \(\gamma_2(x)\) for a degree-one element \(x\).

            If \(x=\sum_i a_i e_i\), then
            \(\gamma_2(x)=\sum_i a_i^2\gamma_2(e_i)
            +\sum_{i<j}a_i a_j e_i e_j\).
            """
            assert element.parent() is self and element.degree() == 1, (
                "the divided square is defined here on degree-one elements"
            )
            return self.divided_power(element, 2)

        def _repr_(self: "FreeAlgebraParent") -> str:
            return (
                f"Divided power algebra over {self.base_ring()} on "
                f"{self.algebra_generating_set()}"
            )

    class Homsets(HomsetsCategory):
        r"""Divided-power algebra homsets and their morphisms."""

        def extra_super_categories(self) -> list:
            return [
                FramedFreeAlgebras(self.base_category().base_ring()).Homsets()
            ]

        class ElementMethods:
            def preserves_divided_power(
                self: "FreeAlgebraMorphism",
                element: "Element",
                degree: int,
            ) -> bool:
                r"""Return whether \(f(\gamma_n(x))=\gamma_n(f(x))\)."""
                return self(
                    self.domain().divided_power(element, degree)
                ) == self.codomain().divided_power(self(element), degree)


def DividedPowerAlgebraOn(
    base_ring: "Ring", algebra_generating_set: "OrderedSet"
) -> "DividedPowerAlgebraParent":
    r"""Return \(\Gamma(F_R(S))\), the same object on every call."""
    return object_of(
        FramedDividedPowerAlgebras(engine_ring(base_ring)),
        algebra_generating_set=algebra_generating_set,
    )


def tensor_to_symmetric(source: "FreeAlgebraParent") -> FreeAlgebraMorphism:
    r"""Return \(T(M)\twoheadrightarrow\operatorname{Sym}(M)\)."""
    assert source in FramedTensorAlgebras(source.base_ring()), (
        "the source must be a framed tensor algebra"
    )
    target = FreeAlgebraOn(source.base_ring(), source.algebra_generating_set())
    morphism: "FreeAlgebraMorphism" = source.hom(
        {
            label: target.algebra_generator(label)
            for label in source.algebra_generating_set()
        }
    )
    return morphism


def tensor_to_alternating(source: "FreeAlgebraParent") -> FreeAlgebraMorphism:
    r"""Return \(T(M)\twoheadrightarrow\Lambda(M)\)."""
    assert source in FramedTensorAlgebras(source.base_ring()), (
        "the source must be a framed tensor algebra"
    )
    target = AlternatingAlgebraOn(
        source.base_ring(), source.algebra_generating_set()
    )
    morphism: "FreeAlgebraMorphism" = source.hom(
        {
            label: target.algebra_generator(label)
            for label in source.algebra_generating_set()
        }
    )
    return morphism


def symmetric_to_divided(source: "FreeAlgebraParent") -> FreeAlgebraMorphism:
    r"""Return \(\operatorname{Sym}(M)\to\Gamma(M)\), \(x^n\mapsto n!\gamma_n(x)\)."""
    assert source in SymmetricAlgebras(source.base_ring()), (
        "the source must be a symmetric algebra"
    )
    target = DividedPowerAlgebraOn(
        source.base_ring(), source.algebra_generating_set()
    )
    morphism: "FreeAlgebraMorphism" = source.hom(
        {
            label: target.algebra_generator(label)
            for label in source.algebra_generating_set()
        }
    )
    return morphism


def divided_to_symmetric(source: "FreeAlgebraParent") -> FreeAlgebraMorphism:
    r"""Return \(\Gamma(M)\to\operatorname{Sym}(M)\) over \(\mathbb Q\)."""
    assert source in FramedDividedPowerAlgebras(source.base_ring()), (
        "the source must be a framed divided power algebra"
    )
    assert engine_ring(source.base_ring()) is SageQQ, (
        "the inverse map from divided to symmetric powers requires QQ"
    )
    target = FreeAlgebraOn(source.base_ring(), source.algebra_generating_set())

    def image_of_monomial(monomial: "Element") -> "Element":
        image = target.one()
        denominator = SageQQ.one()
        for label, exponent in source.monomial_system().factors(monomial):
            image *= target.algebra_generator(label) ** exponent
            denominator *= factorial(exponent)
        return image / denominator

    return FreeAlgebraMorphism(
        free_algebra_homset(source, target),
        SetMorphism(
            Hom(
                source.module_generating_set(),
                UnderlyingSet(target),
                Sets(),
            ),
            image_of_monomial,
        ),
    )


def tensor_extension(module_morphism: ModuleMorphism) -> FreeAlgebraMorphism:
    r"""Extend \(f:M\to U(A)\) uniquely to \(T(M)\to A\)."""
    module = module_morphism.domain()
    source = TensorAlgebraOn(
        module.base_ring(), module.module_generating_set()
    )
    morphism: "FreeAlgebraMorphism" = source.hom(
        {
            label: module_morphism(module.module_generator(label))
            for label in module.module_generating_set()
        }
    )
    return morphism


def symmetric_extension(module_morphism: ModuleMorphism) -> FreeAlgebraMorphism:
    r"""Extend \(f:M\to U(A)\) uniquely to \(\operatorname{Sym}(M)\to A\)."""
    from sage.categories.commutative_rings import CommutativeRings

    assert module_morphism.codomain() in CommutativeRings(), (
        "a symmetric-algebra extension requires a commutative target"
    )
    module = module_morphism.domain()
    source = FreeAlgebraOn(
        module.base_ring(), module.module_generating_set()
    )
    morphism: "FreeAlgebraMorphism" = source.hom(
        {
            label: module_morphism(module.module_generator(label))
            for label in module.module_generating_set()
        }
    )
    return morphism


def alternating_extension(module_morphism: ModuleMorphism) -> FreeAlgebraMorphism:
    r"""Extend an alternating linear map uniquely to \(\Lambda(M)\)."""
    module = module_morphism.domain()
    labels = tuple(module.module_generating_set())
    images = tuple(
        module_morphism(module.module_generator(label)) for label in labels
    )
    target = module_morphism.codomain()
    assert all(image * image == target.zero() for image in images), (
        "each generator image must square to zero"
    )
    assert all(
        left * right + right * left == target.zero()
        for index, left in enumerate(images)
        for right in images[index + 1:]
    ), "generator images must anticommute"
    source = AlternatingAlgebraOn(module.base_ring(), module.module_generating_set())
    image_by_label = dict(zip(labels, images))
    return FreeAlgebraMorphism(
        free_algebra_homset(source, target),
        SetMorphism(
            Hom(
                source.module_generating_set(),
                UnderlyingSet(target),
                Sets(),
            ),
            source._extend_to_monomials(image_by_label.__getitem__, target),
        ),
    )


def restrict_free_algebra_morphism(
    module: "Module", algebra_morphism: FreeAlgebraMorphism
) -> ModuleMorphism:
    r"""Restrict a free-algebra morphism to its degree-one module."""
    source = algebra_morphism.domain()
    assert source.algebra_generating_set() == module.module_generating_set(), (
        "the algebra must be free on this module's framing"
    )
    return module_homset(module, algebra_morphism.codomain())(
        {
            label: algebra_morphism(source.algebra_generator(label))
            for label in module.module_generating_set()
        }
    )


def divided_power_induced_morphism(
    module_morphism: ModuleMorphism,
) -> FreeAlgebraMorphism:
    r"""Return \(\Gamma(f):\Gamma(M)\to\Gamma(N)\)."""
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector

    domain = module_morphism.domain()
    codomain = module_morphism.codomain()
    source = DividedPowerAlgebraOn(
        domain.base_ring(), domain.module_generating_set()
    )
    target = DividedPowerAlgebraOn(
        codomain.base_ring(), codomain.module_generating_set()
    )

    def degree_one_image(label: "Element") -> "Element":
        image = module_morphism(domain.module_generator(label))
        return sum(
            (
                coefficient * target.algebra_generator(target_label)
                for coefficient, target_label in zip(
                    _coordinate_vector(image), codomain.module_generating_set()
                )
            ),
            target.zero(),
        )

    def image_of_monomial(monomial: "Element") -> "Element":
        image = target.one()
        for label, exponent in source.monomial_system().factors(monomial):
            image *= target.divided_power(degree_one_image(label), exponent)
        return image

    return FreeAlgebraMorphism(
        divided_power_algebra_homset(source, target),
        SetMorphism(
            Hom(
                source.module_generating_set(),
                UnderlyingSet(target),
                Sets(),
            ),
            image_of_monomial,
        ),
    )


def divided_power_extension(
    module_morphism: ModuleMorphism,
) -> DividedPowerAlgebraMorphism:
    r"""Extend \(f:M\to U(A)\) uniquely to a divided-power morphism \(\Gamma(M)\to A\)."""
    module = module_morphism.domain()
    target = module_morphism.codomain()
    assert target in DividedPowerAlgebras(module.base_ring()), (
        "a divided-power extension requires a divided-power algebra target"
    )
    source = DividedPowerAlgebraOn(
        module.base_ring(), module.module_generating_set()
    )

    def degree_one_image(label: "Element") -> "Element":
        return module_morphism(module.module_generator(label))

    def image_of_monomial(monomial: "Element") -> "Element":
        image = target.one()
        for label, exponent in source.monomial_system().factors(monomial):
            image *= target.divided_power(degree_one_image(label), exponent)
        return image

    return DividedPowerAlgebraMorphism(
        divided_power_algebra_homset(source, target),
        SetMorphism(
            Hom(
                source.module_generating_set(),
                UnderlyingSet(target),
                Sets(),
            ),
            image_of_monomial,
        ),
    )


class PresentedFreeAlgebraElement(ModuleElement):
    r"""A class in a free algebra modulo relations generated in degree one."""

    def __init__(
        self, parent: "Parent", representative: "FramedFreeAlgebras.ElementMethods"
    ) -> None:
        ModuleElement.__init__(self, parent)
        assert representative.parent() is parent.presentation_algebra(), (
            "a representative lies in this presentation algebra"
        )
        self._representative = representative

    def representative(self) -> "FramedFreeAlgebras.ElementMethods":
        return self._representative


class PresentedFreeAlgebras(OwnedCategoryOverBaseRing):
    r"""The graded algebras \(A(F)/\langle K\rangle\) of a presented module."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "presented free algebras"

    def super_categories(self) -> list:
        from dzack_research.preamble.categories.algebras.algebras import Algebras

        return [Algebras(self.base_ring())]

    class ParentMethods:
        r"""\(A(F)/\langle K\rangle\) for a module given by a presentation."""

        def __init__(
            self,
            module: "Module",
            construction: str,
            presentation_algebra: "FreeAlgebraParent",
            **rest: "ConstructionData",
        ) -> None:
            r"""Build \(A(F)/\langle K\rangle\) for one of the four constructions."""
            self._module = module
            self._construction = construction
            self._presentation_algebra = presentation_algebra
            self._algebra_generating_set = module.module_generating_set()
            self._zero_representative = presentation_algebra.zero()
            self._one_representative = presentation_algebra.one()
            super().__init__(base=module.base_ring(), **rest)
            self._algebra_generator_morphism = SetMorphism(
                Hom(
                    self._algebra_generating_set,
                    UnderlyingSet(self),
                    Sets(),
                ),
                lambda label: self(
                    self._presentation_algebra.algebra_generator(label)
                ),
            )

        def module(self) -> "Module":
            return self._module

        def presentation_algebra(self) -> "FreeAlgebraParent":
            return self._presentation_algebra

        def algebra_generating_set(self) -> "OrderedSet":
            return self._algebra_generating_set

        def algebra_generator(
            self, label: "_SageElement"
        ) -> "PresentedFreeAlgebraElement":
            return self._algebra_generator_morphism(label)

        def algebra_generators(self) -> tuple:
            return tuple(
                self.algebra_generator(label)
                for label in self.algebra_generating_set()
            )

        def zero(self) -> "PresentedFreeAlgebraElement":
            return self(self._zero_representative)

        def one(self) -> "PresentedFreeAlgebraElement":
            return self(self._one_representative)

        def _element_constructor_(
            self, representative: "PresentedFreeAlgebraElement | FramedFreeAlgebras.ElementMethods"
        ) -> "PresentedFreeAlgebraElement":
            if isinstance(representative, PresentedFreeAlgebraElement):
                assert representative.parent() is self, "an algebra element has one parent"
                return representative
            if representative.parent() is not self._presentation_algebra:
                representative = representative * self._presentation_algebra.one()
            algebra_class = PresentedFreeAlgebraElement(self, representative)
            return algebra_class

        def _ring_morphism_defining_algebra_structure(self) -> "Morphism":
            from sage.categories.rings import Rings

            return SetMorphism(
                Hom(self.base_ring(), self, Rings()),
                lambda scalar: scalar * self.one(),
            )

        def graded_piece(self, degree: int) -> "Module":
            from dzack_research.preamble.categories.modules.tensors import AlternatingPower
            from dzack_research.preamble.categories.modules.tensors import DividedPower
            from dzack_research.preamble.categories.modules.tensors import SymmetricPower
            from dzack_research.preamble.categories.modules.tensors import TensorPower

            constructions = {
                "tensor": TensorPower,
                "symmetric": SymmetricPower,
                "alternating": AlternatingPower,
                "divided": DividedPower,
            }
            return constructions[self._construction](self._module, int(degree))

        def _class_in_degree(
            self, degree: int, representative: "_SageElement"
        ) -> "_SageElement":
            from dzack_research.preamble.categories.modules.tensors import _element_of_degree_piece

            in_degree: "_SageElement" = _element_of_degree_piece(
                self.graded_piece(degree), representative
            )
            return in_degree

        def divided_power(
            self,
            element: "PresentedFreeAlgebraElement | FramedFreeAlgebras.ElementMethods",
            degree: int,
        ) -> "PresentedFreeAlgebraElement":
            assert self._construction == "divided", (
                "divided powers belong to the divided power construction"
            )
            representative = (
                element.representative()
                if isinstance(element, PresentedFreeAlgebraElement)
                else element
            )
            return self(self._presentation_algebra.divided_power(representative, degree))

        def _repr_(self) -> str:
            names = {
                "tensor": "Tensor",
                "symmetric": "Symmetric",
                "alternating": "Alternating",
                "divided": "Divided power",
            }
            return f"{names[self._construction]} algebra on {self._module}"

    class ElementMethods:
        def _add_(self, other: "PresentedFreeAlgebraElement") -> "PresentedFreeAlgebraElement":
            return self.parent()(self._representative + other._representative)

        def _neg_(self) -> "PresentedFreeAlgebraElement":
            return self.parent()(-self._representative)

        def _mul_(self, other: "PresentedFreeAlgebraElement") -> "PresentedFreeAlgebraElement":
            return self.parent()(self._representative * other._representative)

        def _lmul_(self, scalar: "Element") -> "PresentedFreeAlgebraElement":
            return self.parent()(scalar * self._representative)

        def _rmul_(self, scalar: "Element") -> "PresentedFreeAlgebraElement":
            return self.parent()(self._representative * scalar)

        def __eq__(self, other: "Element") -> bool:
            if not isinstance(other, PresentedFreeAlgebraElement):
                return False
            if other.parent() is not self.parent():
                return False
            difference = self._representative - other._representative
            return all(
                self.parent()._class_in_degree(degree, component).is_zero()
                for degree, component in difference.homogeneous_components().items()
            )

        def _repr_(self) -> str:
            return repr(self._representative)

        def homogeneous_components(self) -> dict:
            return {
                degree: self.parent()(component)
                for degree, component in self._representative.homogeneous_components().items()
            }

        def degree(self) -> "Integer":
            return self._representative.degree()


def _free_algebra_of_module(
    module: "Module",
    construction: str,
    constructor: "Callable[[Ring, OrderedSet], FreeAlgebraParent]",
) -> "Parent":
    source = constructor(module.base_ring(), module.module_generating_set())
    if module.relation_matrix().nrows() == 0:
        return source
    return object_of(
        PresentedFreeAlgebras(module.base_ring()),
        module=module,
        construction=construction,
        presentation_algebra=source,
    )


def TensorAlgebraOf(module: "Module") -> "Parent":
    r"""Return (T(M)), preserving a presentation of (M)."""
    return _free_algebra_of_module(module, "tensor", TensorAlgebraOn)


def SymmetricAlgebraOf(module: "Module") -> "Parent":
    r"""Return (operatorname{Sym}(M)), preserving a presentation of (M)."""
    return _free_algebra_of_module(module, "symmetric", FreeAlgebraOn)


def AlternatingAlgebraOf(module: "Module") -> "Parent":
    r"""Return (Lambda(M)), preserving a presentation of (M)."""
    return _free_algebra_of_module(module, "alternating", AlternatingAlgebraOn)


def DividedPowerAlgebraOf(module: "Module") -> "Parent":
    r"""Return (Gamma(M)), preserving a presentation of (M)."""
    return _free_algebra_of_module(module, "divided", DividedPowerAlgebraOn)
