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

from typing import Any

from sage.categories.category_types import Category_over_base_ring
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.monoids.free_abelian_monoid import FreeAbelianMonoid
from sage.sets.image_set import ImageSubobject
from sage.structure.parent import Parent

assert "_as_set" in globals(), "Framed free algebras requires Set() from the preamble"

from sage_lattice_category_spike.objects.sets import Sets
from sage_lattice_category_spike.objects.underlying_sets import UnderlyingSet

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


_MISSING = object()


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


class FreeAlgebraMorphism(ModuleMorphism):
    r"""Algebra morphisms are module maps on monomial generators."""

    def _domain_generating_set(self) -> Parent:
        return self.domain()._module_generating_set()

    def then(self, other: Any) -> "FreeAlgebraMorphism":
        r"""Compose this morphism with a second morphism.

        This returns ``other ∘ self`` by extending the composition on
        monomial generators.
        """
        assert other.domain() is self.codomain(), (
            "the codomain of the first map must be the domain of the second"
        )
        generator_morphism = self.generator_morphism()
        return FreeAlgebraMorphism(
            module_homset(self.domain(), other.codomain()),
            SetMorphism(
                Hom(
                    generator_morphism.domain(),
                    UnderlyingSet(other.codomain()),
                    Sets(),
                ),
                lambda element_of_M: other(self.generator_image(element_of_M)),
            ),
        )


class FreeAlgebraOnSetElement(FreeModuleOnSetElement):
    r"""An element of ``FreeAlgebraOnSet`` with bilinear multiplication."""

    def _mul_(self, other: Any) -> "FreeAlgebraOnSetElement":
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

    def underlying_set_element(self) -> Any:
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

    def __init__(self, base_ring: Any, generating_set: Any) -> None:
        if isinstance(generating_set, Parent):
            self._algebra_generating_set = generating_set
        else:
            self._algebra_generating_set = Set(generating_set)
        self._algebra_generating_set_for_morphism = _as_set(
            self._algebra_generating_set
        )
        self._monomial_parent = FreeAbelianMonoid(self._algebra_generating_set_for_morphism)
        self._monomial_generating_set = _as_set(self._monomial_parent)
        FreeModuleOnSet.__init__(self, base_ring, self._monomial_generating_set)
        self._algebra_generator_morphism = SetMorphism(
            Hom(
                self._algebra_generating_set_for_morphism,
                UnderlyingSet(self),
                Sets(),
            ),
            self.algebra_generator,
        )
        refine(self, FramedFreeAlgebras(base_ring))

    def _module_generating_set(self) -> Parent:
        return self._monomial_generating_set

    def module_generating_set(self) -> Parent:
        """Return the monomial framing set in which relations live."""
        return self._module_generating_set()

    def module_generators(self) -> Any:
        """Return the monomial framing image inside the algebra."""
        return ImageSubobject(
            self.module_generator_morphism(),
            self.module_generating_set(),
        )

    def _module_generator_morphism(self) -> SetMorphism:
        return FramedFreeModules.ParentMethods.generator_morphism(self)

    def _algebra_generator_label(self, monomial: Any) -> Any:
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

    def _algebra_to_monomial(self, s: Any) -> Any:
        return self._monomial_parent.gen(s)

    def algebra_generating_set(self) -> Parent:
        r"""Return the original set ``S`` (not ``Mon(S)``)."""
        return self._algebra_generating_set

    def generating_set(self) -> Parent:
        r"""Return the algebra generating set ``S``."""
        return self._algebra_generating_set

    def generator_morphism(self) -> SetMorphism:
        return self._algebra_generator_morphism

    def algebra_generator_morphism(self) -> SetMorphism:
        """Return the framing map from algebra generators to the free algebra."""
        return self._algebra_generator_morphism

    def algebra_framing_morphism(self) -> SetMorphism:
        """Alias for the free-algebra framing morphism from algebra generators."""
        return self.algebra_generator_morphism()

    def module_generator_morphism(self) -> SetMorphism:
        """Return the framing map from module generators (monomials) to the algebra."""
        return self._module_generator_morphism()

    def generator(self, element_of_S_or_monomial: Any) -> Any:
        r"""Return a distinguished element associated to ``s``."""
        if element_of_S_or_monomial in self._algebra_generating_set:
            return self.algebra_generator(element_of_S_or_monomial)
        return self._module_generator_morphism()._call_(element_of_S_or_monomial)

    def algebra_generator(self, s: Any) -> Any:
        r"""Return the degree-1 monomial ``[s]`` in ``FreeAlg_R(S)``."""
        assert s in self._algebra_generating_set, (
            f"{s!r} is not in {self._algebra_generating_set}"
        )
        monomial = self._algebra_to_monomial(s)
        return self._module_generator_morphism()._call_(monomial)

    def algebra_generators(self) -> tuple:
        r"""Return algebra generators when the framing set is finite."""
        assert self._algebra_generating_set in Sets().Finite(), (
            "algebra_generators() is defined only for finitely generated framed "
            "free algebras; use algebra_generator(s) for arbitrary sets"
        )
        return tuple(self.algebra_generator(s) for s in self._algebra_generating_set)

    def product_on_generators(self, s: Any, t: Any) -> Any:
        r"""Return the product of algebra generators s and t."""
        return self.algebra_generator(s) * self.algebra_generator(t)

    def _normalize_hom_dict(self, images: dict) -> tuple[Any, dict]:
        values = dict(images)
        assert values, (
            "an empty assignment does not determine a codomain; "
            "construct it through the codomain argument"
        )
        target = next(iter(values.values())).parent()
        assert all(value.parent() is target for value in values.values()), (
            "all values in a finite assignment must belong to one codomain"
        )
        monomial_keys = all(key in self._module_generating_set() for key in values)
        algebra_keys = all(key in self._algebra_generating_set for key in values)
        assert monomial_keys or algebra_keys, (
            "a homomorphism assignment must use algebra generators or monomial "
            "generators"
        )
        assert not (monomial_keys and algebra_keys), (
            "an assignment mixed algebra and monomial generators"
        )
        if algebra_keys:
            return target, {
                self._algebra_to_monomial(key): value
                for key, value in values.items()
            }
        return target, values

    def _normalize_hom_images(self, images: Any) -> tuple[Any, Any]:
        assert isinstance(images, SetMorphism), (
            "expected a SetMorphism when normalizing images"
        )
        target = images.codomain().structured_parent()
        match images.domain():
            case domain if domain == self._module_generating_set():
                return target, images
            case _:
                assert False, (
                    "the generator-map domain must be the module monomial generators"
                )

    def _from_generator_values(self, codomain: Any, values: tuple[Any, ...]) -> dict:
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
        return {
            self._algebra_to_monomial(s): image
            for s, image in zip(self._algebra_generating_set, values, strict=True)
        }

    def hom(self, images: Any, codomain: Any = _MISSING) -> Any:
        r"""Extend a map on generators by ``R``-linearity."""
        match images:
            case SetMorphism():
                codomain_parent, monomial_map = self._normalize_hom_images(images)
            case dict():
                if images:
                    codomain_parent, monomial_map = self._normalize_hom_dict(images)
                else:
                    if codomain is _MISSING:
                        raise ValueError("an empty assignment requires a codomain")
                    codomain_parent = codomain
                    monomial_map = lambda monomial: codomain_parent.zero()
            case list() | tuple():
                images = tuple(images)
                match images:
                    case ():
                        if codomain is _MISSING:
                            raise ValueError("an empty assignment requires its codomain")
                        codomain_parent = codomain
                        monomial_map = lambda monomial: codomain_parent.zero()
                    case _:
                        if codomain is _MISSING:
                            raise ValueError(
                                "a finite assignment requires an explicit codomain"
                            )
                        codomain_parent = codomain
                        monomial_map = self._from_generator_values(
                            codomain_parent,
                            images,
                        )
            case _ if callable(images):
                if codomain is _MISSING:
                    raise ValueError("a generator function requires a codomain")
                codomain_parent = codomain
                monomial_map: Any = images
            case _:
                assert False, (
                    "a homomorphism is specified by a generator map from the "
                    "algebra or monomial generators, a finite assignment, or a "
                    "callable on monomials"
                    )

        if isinstance(monomial_map, dict):
            monomial_map = monomial_map.__getitem__

        homset = Hom(self._module_generating_set(), UnderlyingSet(codomain_parent), Sets())
        return FreeAlgebraMorphism(
            module_homset(self, codomain_parent),
            SetMorphism(homset, monomial_map),
        )

    def induced_hom(self, set_morphism: SetMorphism, codomain: Any) -> Any:
        r"""Induce the free-algebra map determined by ``set_morphism``."""
        assert isinstance(codomain, FreeAlgebraOnSet), (
            "the target of a free algebra map is a free algebra on a set"
        )
        assert set_morphism.parent() == Hom(
            self.algebra_generating_set(),
            codomain.algebra_generating_set(),
            Sets(),
        ), "the map must have the two algebra generating sets as endpoints"
        target_monoid = codomain._monomial_parent

        def image_of_monomial(monomial: Any) -> Any:
            target_monomial = target_monoid.one()
            for generator, exponent in monomial.dict().items():
                target_generator = set_morphism._call_(generator)
                target_monomial *= target_monoid.gen(target_generator) ** exponent
            return codomain._module_generator_morphism()._call_(target_monomial)

        return self.hom(image_of_monomial, codomain)

    def one(self) -> Any:
        r"""Return the multiplicative identity (the empty monomial)."""
        return self.generator(self._module_generator_morphism().domain().one())

    def _repr_(self) -> str:
        return f"Free {self.base_ring()}-algebra on {self._algebra_generating_set}"


def FreeAlgebraOn(base_ring: Any, generating_set: Any) -> FreeAlgebraOnSet:
    r"""Construct ``\operatorname{FreeAlg}_R(S)`` on the supplied set ``S``."""
    return FreeAlgebraOnSet(base_ring, generating_set)
