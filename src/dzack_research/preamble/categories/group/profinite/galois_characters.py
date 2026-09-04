r"""Continuous cyclotomic and quadratic characters of absolute Galois groups."""

from math import gcd
from typing import Any, cast

from sage.categories.morphism import Morphism
from sage.groups.perm_gps.permgroup_named import CyclicPermutationGroup
from sage.rings.finite_rings.integer_mod_ring import Integers
from sage.rings.integer_ring import ZZ
from sage.misc.functional import cyclotomic_polynomial
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories.group.groups import _own_group
from dzack_research.preamble.categories.group.profinite.field_morphisms import (
    _exact_field_morphism_from_engine,
)
from dzack_research.preamble.categories.group.profinite.galois_quotient import (
    FiniteGaloisExtension,
    continuous_group_homset,
)
from dzack_research.preamble.categories.rings.ring_foundation import _engine_element, _engine_ring, _own_ring


def _unit_group_element(unit_group, residue):
    residue = unit_group.values_group()(residue)
    for element in unit_group:
        if element.value() == residue:
            return element
    raise ValueError(f"{residue} is not represented in {unit_group}")


class RestrictedProfiniteCharacter(Morphism):
    def __init__(self, character, subgroup) -> None:
        if subgroup.ambient() is not character.domain():
            raise ValueError("the subgroup does not lie in this character's domain")
        self._character = character
        Morphism.__init__(
            self,
            continuous_group_homset(subgroup, character.codomain()),
        )

    def _call_(self, element):
        return self._character(self.domain().inclusion()(element))

    def is_continuous(self) -> bool:
        return True


class ProfiniteCharacter(Morphism):
    r"""A character factoring through one represented finite Galois quotient."""

    def __init__(self, domain, codomain, extension: FiniteGaloisExtension) -> None:
        self._factor_extension = extension
        Morphism.__init__(self, continuous_group_homset(domain, codomain))

    def factor_extension(self) -> FiniteGaloisExtension:
        return self._factor_extension

    def factorization(self):
        return self.domain().restriction_map(self._factor_extension)

    def kernel(self):
        return self.domain().open_subgroup(self._factor_extension)

    def restrict(self, subgroup):
        return RestrictedProfiniteCharacter(self, subgroup)

    def is_continuous(self) -> bool:
        return True


def _finite_root_at_stage(root, stage):
    total_degree = ZZ(_engine_ring(stage.field()).degree())
    lifted = root.change_level(total_degree)
    field, value, embedding = lifted.as_finite_field_element()
    if field is not _engine_ring(stage.field()):
        raise ValueError(
            "the canonical finite stage does not contain the required root"
        )
    if embedding(value) != root:
        raise ValueError(
            "the finite-stage root does not realize the chosen closure root"
        )
    return value


class CyclotomicCharacter(ProfiniteCharacter):
    r"""The continuous character (\chi_n:G_K\to(\mathbb Z/n)^{\times})."""

    def __init__(self, domain, n) -> None:
        n = ZZ(n)
        if n < 2:
            raise ValueError("the finite cyclotomic character requires n >= 2")
        characteristic = ZZ(int(domain.characteristic()))
        if characteristic and gcd(int(n), int(characteristic)) != 1:
            raise ValueError("n must be invertible in the base field")
        self._modulus = n
        target = Integers(n).unit_group()
        closure = _engine_ring(domain.algebraic_closure())
        root = closure.zeta(n)
        self._root = root

        if domain._is_finite_field():
            q_mod_n = Integers(n)(int(domain.base_field_order()))
            degree = ZZ(q_mod_n.multiplicative_order())
            stage = domain.finite_extension(degree)
            self._root_at_stage = _finite_root_at_stage(root, stage)
        elif _engine_ring(domain.base_field()) is SageQQ:
            if n == 2:
                stage = domain.extension_data(domain.base_field())
                self._root_at_stage = _engine_ring(domain.base_field())(-1)
            else:
                base = cast(Any, _engine_ring(domain.base_field()))
                polynomial = cast(Any, cyclotomic_polynomial(n)).change_ring(base)
                field = base.extension(polynomial, f"zeta_{n}")
                owned_field = _own_ring(field)
                backend = field.mor([root], closure)
                embedding = _exact_field_morphism_from_engine(
                    owned_field,
                    domain.algebraic_closure(),
                    backend,
                )
                stage = domain.extension_data(owned_field, embedding=embedding)
                self._root_at_stage = field.gen()
        else:
            raise NotImplementedError(
                "the exact cyclotomic compositum is currently constructed for finite fields and QQ"
            )
        super().__init__(domain, target, stage)

    def modulus(self):
        return self._modulus

    def primitive_root(self):
        return self._root

    def _exponent_image(self, exponent):
        modulus = int(self._modulus)
        residue = pow(int(self.domain().base_field_order()), int(exponent), modulus)
        return _unit_group_element(self.codomain(), residue)

    def _call_(self, element):
        exponent = getattr(element, "frobenius_exponent", lambda: None)()
        if exponent is not None and self.domain()._is_finite_field():
            return self._exponent_image(exponent)

        coordinate = getattr(element, "restriction_coordinate", lambda _stage: None)(
            self.factor_extension()
        )
        if coordinate is not None:
            image = self.factor_extension().embedding()(coordinate(self._root_at_stage))
        else:
            image = element(self._root)
        for residue in range(int(self._modulus)):
            if gcd(residue, int(self._modulus)) == 1 and image == self._root**residue:
                return _unit_group_element(self.codomain(), residue)
        raise ValueError(
            "the represented automorphism does not act through a unit exponent on mu_n"
        )

    def _repr_(self) -> str:
        return f"Cyclotomic character chi_{self._modulus}: {self.domain()} -> {self.codomain()}"


class QuadraticCharacter(ProfiniteCharacter):
    r"""The character attached to (K(\sqrt a)/K) in characteristic not two."""

    def __init__(self, domain, a) -> None:
        characteristic = ZZ(int(domain.characteristic()))
        if characteristic == 2:
            raise ValueError(
                "quadratic Kummer characters require characteristic different from two"
            )
        base_field = domain.base_field()
        base = _engine_ring(base_field)
        owned_a = base_field(a)
        backend_a = base(_engine_element(base_field, owned_a))
        if not backend_a:
            raise ValueError("a quadratic character requires a nonzero square class")
        self._square_class = owned_a
        closure = _engine_ring(domain.algebraic_closure())
        embedded_a = domain.base_embedding()(owned_a)
        root = _engine_element(domain.algebraic_closure(), embedded_a).sqrt()
        self._root = domain.algebraic_closure()._from_engine_element(closure(root))

        if backend_a.is_square():
            stage = domain.extension_data(domain.base_field())
            self._root_at_stage = backend_a.sqrt()
        elif domain._is_finite_field():
            stage = domain.finite_extension(2)
            self._root_at_stage = _finite_root_at_stage(root, stage)
        else:
            polynomial_ring = base["t"]
            t = polynomial_ring.gen()
            field = base.extension(t**2 - backend_a, "sqrt_a")
            owned_field = _own_ring(field)
            backend = field.mor([root], closure)
            embedding = _exact_field_morphism_from_engine(
                owned_field,
                domain.algebraic_closure(),
                backend,
            )
            stage = domain.extension_data(owned_field, embedding=embedding)
            self._root_at_stage = field.gen()

        target = _own_group(CyclicPermutationGroup(2))
        super().__init__(domain, target, stage)

    def square_class(self):
        return self._square_class

    def square_root(self):
        return self._root

    def _call_(self, element):
        coordinate = getattr(element, "restriction_coordinate", lambda _stage: None)(
            self.factor_extension()
        )
        if coordinate is not None:
            image = self.factor_extension().embedding()(coordinate(self._root_at_stage))
        else:
            image = element(self._root)
        if image == self._root:
            return self.codomain().one()
        if image == -self._root:
            return self.codomain().group_generators()[0]
        raise ValueError(
            "the represented automorphism does not preserve the quadratic extension"
        )

    def _repr_(self) -> str:
        return f"Quadratic character for {self._square_class}: {self.domain()} -> {self.codomain()}"


__all__ = [
    "CyclotomicCharacter",
    "ProfiniteCharacter",
    "QuadraticCharacter",
    "RestrictedProfiniteCharacter",
]
