r"""Free commutative algebras on arbitrary sets.

``FreeAlgebraOnSet(R, S)`` realizes the free commutative ``R``-algebra on a set ``S``:

\[
    \operatorname{FreeAlg}_R(S) = R[\operatorname{Mon}(S)]
\]

As an ``R``-module this is ``FreeModuleOnSet(R, Mon(S))`` where ``Mon(S)`` is the
free commutative monoid on ``S``.  Multiplication is the monoid operation on
``Mon(S)`` extended ``R``-bilinearly.

The exposed *algebra* generating set is ``S``; the module generators are
``Mon(S)``.
"""

from typing import Any, TYPE_CHECKING

from sage.categories.category_types import Category_over_base_ring
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.monoids.free_abelian_monoid import FreeAbelianMonoid
from sage.rings.ideal import Ideal_generic
from sage.sets.image_set import ImageSubobject
from sage.structure.parent import Parent

assert "_as_set" in globals(), "Framed free algebras requires Set() from the preamble"

from sage_lattice_category_spike.objects.sets import Sets
from sage_lattice_category_spike.objects.underlying_sets import UnderlyingSet

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from sage_lattice_category_spike.lexicon import OrderedSet


assert "FramedAlgebras" in globals(), (
    "Framed free algebras requires FramedAlgebras from algebras"
)
assert "FreeAlgebras" in globals(), (
    "Framed free algebras requires FreeAlgebras from free_algebras"
)
assert "FramedFreeModules" in globals(), (
    "Framed free algebras requires FramedFreeModules from framed free modules"
)
assert "FreeModuleOnSet" in globals(), (
    "Framed free algebras requires FreeModuleOnSet from framed free modules"
)
assert "FreeModuleOnSetElement" in globals(), (
    "Framed free algebras requires FreeModuleOnSetElement from framed free modules"
)
assert "ModuleMorphism" in globals(), (
    "Framed free algebra morphisms require ModuleMorphism from module morphisms"
)
assert "module_homset" in globals(), (
    "Framed free algebra hom constructor requires module_homset"
)


class FramedFreeAlgebras(Category_over_base_ring):
    r"""Free R-algebras equipped with the canonical map \(S \to U(\operatorname{FreeAlg}_R(S))\)."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "framed free algebras"

    def super_categories(self) -> list:
        return [
            FreeAlgebras(self.base_ring()),
            FramedAlgebras(self.base_ring()),
            FramedFreeModules(self.base_ring()),
        ]

    class ParentMethods:
        def number_of_algebra_generators(self) -> "Cardinal":
            r"""Return \(|S|\), the cardinality of the algebra generating set."""
            return self.algebra_generating_set().cardinality()

        def number_of_module_generators(self) -> "Cardinal":
            r"""Return \(|\operatorname{Mon}(S)|\).

            Two framings, two counts: the module framing is by monomials, so
            this is not \(|S|\) -- it is infinite as soon as \(S\) is
            non-empty.  Cardinality is total on sets, so neither count is
            restricted to the finitely generated case.
            """
            return self.module_generating_set().cardinality()

        def hom(
            self,
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
                module_homset(self, codomain_parent),
                SetMorphism(
                    Hom(
                        self.module_generating_set(),
                        UnderlyingSet(codomain_parent),
                        Sets(),
                    ),
                    self._extend_to_monomials(image_of_generator, codomain_parent),
                ),
            )

        def induced_hom(self, set_morphism: SetMorphism, codomain: "Module") -> "Morphism":
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
            return self.hom(
                lambda label: codomain.algebra_generator(set_morphism._call_(label)),
                codomain,
            )

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


class FreeAlgebraMorphism(ModuleMorphism):
    r"""Algebra morphisms are module maps on monomial generators."""

    def _domain_module_generating_set(self) -> Parent:
        return self.domain().module_generating_set()

    def then(self, other: object) -> "FreeAlgebraMorphism":
        r"""Compose this morphism with a second morphism.

        This returns ``other ∘ self`` by extending the composition on
        monomial generators.
        """
        assert other.domain() is self.codomain(), (
            "the codomain of the first map must be the domain of the second"
        )
        module_generator_morphism = self.module_generator_morphism()
        return FreeAlgebraMorphism(
            module_homset(self.domain(), other.codomain()),
            SetMorphism(
                Hom(
                    module_generator_morphism.domain(),
                    UnderlyingSet(other.codomain()),
                    Sets(),
                ),
                lambda element_of_M: other(self._module_generator_image(element_of_M)),
            ),
        )


class FreeAlgebraIdeal(Ideal_generic):
    r"""An ideal of a free commutative algebra, carrying its normal form.

    A quotient decides equality by comparing normal forms, so an ideal that
    cannot reduce makes \(A/I\) unable to say what it is a quotient by.  The
    normal form is the polynomial one, read through the presentation.
    """

    @cached_method
    def _polynomial_ideal(self) -> "Ideal_generic":
        algebra = self.ring()
        return algebra._polynomial_ring().ideal(
            [algebra._as_polynomial(generator) for generator in self.gens()]
        )

    def reduce(self, element: "Element") -> "Element":
        r"""Return the normal form of ``element`` modulo this ideal."""
        algebra = self.ring()
        return algebra._from_polynomial(
            self._polynomial_ideal().reduce(algebra._as_polynomial(element))
        )

    def _contains_(self, element: "Element") -> bool:
        algebra = self.ring()
        return algebra._as_polynomial(element) in self._polynomial_ideal()


class FreeAlgebraOnSetElement(FreeModuleOnSetElement):
    r"""An element of ``FreeAlgebraOnSet`` with bilinear multiplication."""

    def _mod_(self, other: "Element") -> "FreeAlgebraOnSetElement":
        r"""Return this element reduced modulo ``other``.

        Equality in \(A/(g)\) is equality of remainders, so a quotient of
        this algebra can only decide it once division with remainder is
        available here.
        """
        parent = self.parent()
        return parent._from_polynomial(
            parent._as_polynomial(self) % parent._as_polynomial(other)
        )

    def divides(self, other: "Element") -> bool:
        r"""Return whether this element divides ``other`` in the algebra.

        Divisibility is the ring question the module construction cannot
        answer, and it is what membership in a principal ideal *is*.
        """
        assert other.parent() is self.parent(), (
            "divisibility is a question inside one algebra"
        )
        parent = self.parent()
        return parent._as_polynomial(self).divides(parent._as_polynomial(other))

    def _mul_(self, other: object) -> "FreeAlgebraOnSetElement":
        assert (
            isinstance(other, FreeAlgebraOnSetElement)
            and other.parent() is self.parent()
        ), "free-algebra multiplication requires elements of one parent"
        parent = self.parent()
        zero = parent.base_ring().zero()
        coefficients = {}
        for left_monomial, left_coefficient in self.coefficients().items():
            for right_monomial, right_coefficient in other.coefficients().items():
                monomial = left_monomial * right_monomial
                coefficients[monomial] = coefficients.get(monomial, zero) + (
                    left_coefficient * right_coefficient
                )
        return parent.element_class(parent, coefficients)

    def underlying_set_element(self) -> "Element":
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
        return self.parent()._algebra_generator_label(monomial)


class FreeAlgebraOnSet(FreeModuleOnSet):
    r"""The free commutative ``R``-algebra on ``S``.

    As an ``R``-module this is ``F_R(\operatorname{Mon}(S))``: the free module
    on the free commutative monoid on ``S``.  Multiplication is the monoid
    operation extended ``R``-bilinearly.

    Inherits the generating set and generator morphism from ``FreeModuleOnSet``.
    Algebra elements are built from algebra generators by explicit algebra
    operations, not via any ``linear_combination`` front-door constructor.
    """

    Element = FreeAlgebraOnSetElement

    def __init__(self, base_ring: "Ring", algebra_generating_set: "OrderedSet") -> None:
        if isinstance(algebra_generating_set, Parent):
            self._algebra_generating_set = algebra_generating_set
        else:
            self._algebra_generating_set = Set(algebra_generating_set)
        self._algebra_generating_set_for_morphism = _as_set(
            self._algebra_generating_set
        )
        self._monomial_parent = FreeAbelianMonoid(self._algebra_generating_set_for_morphism)
        self._monomial_generating_set = _as_set(self._monomial_parent)
        FreeModuleOnSet.__init__(
            self,
            base_ring,
            self._monomial_generating_set,
            category=FramedFreeAlgebras(base_ring),
        )
        self._algebra_generator_morphism = SetMorphism(
            Hom(
                self._algebra_generating_set_for_morphism,
                UnderlyingSet(self),
                Sets(),
            ),
            self.algebra_generator,
        )

    def _element_constructor_(self, value: "Element") -> "Element":
        r"""Return ``value`` as an element of this algebra.

        An \(R\)-algebra comes with its structure map \(R\to A\), so a scalar
        names the element \(r\cdot 1\).  A module has no such map and admits
        only its own elements; an algebra admits its scalars too, which is
        what makes \(0\) and \(1\) elements here and lets Sage's ring
        machinery build ideals over it.

        On the class and not on the category: ``Parent.__init__`` binds the
        element constructor, and it runs before this parent is refined.
        """
        if isinstance(value, FreeModuleOnSetElement) and value.parent() is self:
            return value
        assert value in self.base_ring(), (
            f"{value} is neither an element of {self} nor a scalar of "
            f"{self.base_ring()}"
        )
        return self.base_ring()(value) * self.one()

    @cached_method
    def _polynomial_ring(self) -> Parent:
        r"""Return \(R[x_s:s\in S]\), which this algebra *is* for finite \(S\).

        \(R[\operatorname{Mon}(S)]\) built as a module knows its addition and
        its multiplication but not its division; the polynomial ring knows
        both.  The bijection \(S\leftrightarrow\{x_s\}\) is chosen here, once,
        and stays private: what leaves is :meth:`divides`, a word about this
        algebra.
        """
        assert self._algebra_generating_set in Sets().Finite(), (
            "the polynomial presentation names one variable per generator, "
            "so it exists for finitely generated free algebras"
        )
        return PolynomialRing(
            self.base_ring(),
            self.number_of_algebra_generators().finite_value(),
            "x",
        )

    @cached_method
    def _polynomial_variables(self) -> dict:
        return dict(
            zip(self._algebra_generating_set, self._polynomial_ring().gens())
        )

    def _as_polynomial(self, element: "Element") -> "Element":
        r"""Transport ``element`` along the polynomial presentation."""
        ring = self._polynomial_ring()
        variables = self._polynomial_variables()
        total = ring.zero()
        for monomial, coefficient in element.coefficients().items():
            term = ring.one()
            for label, exponent in monomial.dict().items():
                term *= variables[label] ** exponent
            total += coefficient * term
        return total

    def ideal(self, generators: "OrderedSet") -> FreeAlgebraIdeal:
        r"""Return the ideal generated by ``generators``, with its normal form."""
        return FreeAlgebraIdeal(
            self,
            [self(generator) for generator in finite_ordered_set(generators)],
        )

    def _from_polynomial(self, polynomial: "Element") -> "Element":
        r"""Transport ``polynomial`` back along the polynomial presentation."""
        monoid = self.monomial_monoid()
        labels = tuple(self._algebra_generating_set)
        result = self.zero()
        for exponents, coefficient in polynomial.dict().items():
            monomial = monoid.one()
            for label, exponent in zip(labels, exponents):
                monomial *= monoid.gen(label) ** exponent
            result += coefficient * self.module_generator(monomial)
        return result

    def monomial_monoid(self) -> Parent:
        r"""Return \(\operatorname{Mon}(S)\), the free commutative monoid on \(S\).

        The module framing is indexed by it, and its multiplication is the
        algebra's: \(\operatorname{FreeAlg}_R(S)=R[\operatorname{Mon}(S)]\).
        :meth:`module_generating_set` is its underlying set, which no longer
        multiplies, so the monoid is asked for monoid questions.
        """
        return self._monomial_parent

    def module_generating_set(self) -> Parent:
        """Return the monomial framing set in which relations live."""
        return self._monomial_generating_set

    def module_generators(self) -> "OrderedSet":
        """Return the monomial framing image inside the algebra."""
        return ImageSubobject(
            self.module_generator_morphism(),
            self.module_generating_set(),
        )

    def _algebra_generator_label(self, monomial: "Element") -> "Element":
        monomial_profile = monomial.dict()
        assert len(monomial_profile) == 1, (
            f"{monomial!r} is not a degree-1 monomial; the profile is {monomial_profile}"
        )
        label, exponent = next(iter(monomial_profile.items()))
        assert exponent == 1, (
            f"{monomial!r} is not a generator monomial; exponent profile is "
            f"{monomial_profile}"
        )
        return label

    def _algebra_to_monomial(self, s: "Element") -> "Element":
        return self.monomial_monoid().gen(s)

    def algebra_generating_set(self) -> Parent:
        r"""Return the original set ``S`` (not ``Mon(S)``)."""
        return self._algebra_generating_set

    def algebra_generator_morphism(self) -> SetMorphism:
        """Return the framing map from algebra generators to the free algebra."""
        return self._algebra_generator_morphism

    def algebra_framing_morphism(self) -> SetMorphism:
        """Alias for the free-algebra framing morphism from algebra generators."""
        return self.algebra_generator_morphism()

    def module_generator_morphism(self) -> SetMorphism:
        """Return the framing map from module generators (monomials) to the algebra."""
        return FramedFreeModules.ParentMethods.module_generator_morphism(self)

    def algebra_generator(self, s: "Element") -> "Element":
        r"""Return the degree-1 monomial ``[s]`` in ``FreeAlg_R(S)``."""
        assert s in self._algebra_generating_set, (
            f"{s!r} is not in {self._algebra_generating_set}"
        )
        return self.module_generator(self._algebra_to_monomial(s))

    def algebra_generators(self) -> tuple:
        r"""Return algebra generators when the framing set is finite."""
        assert self._algebra_generating_set in Sets().Finite(), (
            "algebra_generators() is defined only for finitely generated framed "
            "free algebras; use algebra_generator(s) for arbitrary sets"
        )
        return tuple(self.algebra_generator(s) for s in self._algebra_generating_set)

    def product_on_algebra_generators(self, s: "Element", t: "Element") -> "Element":
        r"""Return the product of algebra generators s and t."""
        return self.algebra_generator(s) * self.algebra_generator(t)

    def _generator_images(
        self,
        images: "SetMorphism | dict | tuple | list | Callable",
        codomain: "Module",
    ) -> "tuple[Callable, Module]":
        r"""Return ``(f, A)``: the map on \(S\) naming an algebra morphism.

        Each spelling below names the same thing -- where every generator
        goes.  A partial assignment names no morphism, and is refused.
        """
        match images:
            case SetMorphism():
                assert images.domain() == self._algebra_generating_set_for_morphism, (
                    "a generator map is defined on this algebra's generating set"
                )
                return images._call_, images.codomain().structured_parent()
            case dict():
                values = dict(images)
                assert set(values) == set(self._algebra_generating_set), (
                    f"{self!r} is generated by {self._algebra_generating_set}; an "
                    f"assignment names the image of every one of them, and this "
                    f"one names {sorted(values)}"
                )
                target = next(iter(values.values())).parent()
                assert all(value.parent() is target for value in values.values()), (
                    "the images of the generators lie in one codomain"
                )
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
                    "an algebra map out of a free algebra is named by the images "
                    "of its algebra generators: an assignment, a list in "
                    "generator order, or a map on the generating set"
                )

    def _extend_to_monomials(
        self,
        image_of_generator: "Callable",
        codomain: "Module",
    ) -> "Callable":
        r"""Return the forced map on \(\operatorname{Mon}(S)\).

        \(\prod s^{e_s}\mapsto\prod f(s)^{e_s}\): multiplicativity leaves no
        choice, which is what makes the map on \(S\) the whole of the data.
        """

        def image_of_monomial(monomial: "Element") -> "Element":
            image = codomain.one()
            for label, exponent in monomial.dict().items():
                image *= image_of_generator(label) ** exponent
            return image

        return image_of_monomial

    def _from_algebra_generator_values(self, codomain: "Module", values: tuple[Any, ...]) -> dict:
        assert self._algebra_generating_set in Sets().Finite(), (
            "a finite assignment requires a finite algebra generating set"
        )
        algebra_generating_set_cardinality = self._algebra_generating_set.cardinality()
        assert len(values) == algebra_generating_set_cardinality, (
            f"{self!r} has {algebra_generating_set_cardinality} algebra generators, "
            f"got {len(values)}"
        )
        assert all(value.parent() is codomain for value in values), (
            "all values in a finite assignment must belong to the specified codomain"
        )
        return dict(zip(self._algebra_generating_set, values, strict=True))

    def one(self) -> "Element":
        r"""Return the multiplicative identity: the empty monomial."""
        return self.module_generator(self.monomial_monoid().one())

    def _repr_(self) -> str:
        return f"Free {self.base_ring()}-algebra on {self._algebra_generating_set}"


@cached_function
def FreeAlgebraOn(base_ring: "Ring", algebra_generating_set: "OrderedSet") -> FreeAlgebraOnSet:
    r"""Return ``\operatorname{FreeAlg}_R(S)``, the same object on every call.

    ``FreeAlgebraOnSet`` is not a ``UniqueRepresentation``, so constructing
    it twice would yield two parents with no map between them and no
    comparable elements.  \(\operatorname{FreeAlg}_R(-)\) is a functor, and a
    functor must be well defined on objects, so \((R,S)\) names one algebra.
    """
    return FreeAlgebraOnSet(base_ring, algebra_generating_set)
