"""Free/torsion decomposition and generator operations for enriched FGP modules.

Adds free_part() and torsion_part() methods to FGP_Module_class using
Sage's existing Smith normal form invariants.
"""

from __future__ import annotations

from typing import Any

from sage.groups.abelian_gps.abelian_group_gap import AbelianGroupGap
from sage.groups.additive_abelian.additive_abelian_wrapper import AdditiveAbelianGroupWrapper
from sage.modules.fg_pid.fgp_module import FGP_Module_class
from sage.modules.free_module import FreeModule
from sage.modules.torsion_quadratic_module import TorsionQuadraticModule
from sage.rings.integer_ring import ZZ

_installed = False
_native_tqm_normal_form = TorsionQuadraticModule.normal_form
_native_tqm_orthogonal_group = TorsionQuadraticModule.orthogonal_group


def _elementary_divisors_from_invariants(invariants: Any) -> tuple[Any, ...]:
    """Return prime-power elementary divisors determined by invariant factors."""
    divisors = []
    for invariant in invariants:
        if invariant == 0:
            divisors.append(invariant)
            continue
        if invariant == 1:
            continue
        for prime, exponent in ZZ(invariant).factor():
            divisors.append(prime**exponent)
    divisors.sort()
    return tuple(divisors)


class _TransportedTorsionQuadraticForm:
    """Finite torsion form transported through a supplied morphism."""

    def __init__(self, source: Any, phi: Any, *, direction: str) -> None:
        assert direction in {"pullback", "pushforward"}
        self._source = source
        self._phi = phi
        self._direction = direction

    def _pull(self, x: Any) -> Any:
        if self._direction == "pullback":
            return self._phi(x)
        return self._phi.lift(x)

    def b(self, x: Any, y: Any) -> Any:
        return self._source.b(self._pull(x), self._pull(y))

    def q(self, x: Any) -> Any:
        return self._source.q(self._pull(x))


def _fgp_free_part(self: Any) -> Any:
    """Return the free part of this FGP module as a free module over the base ring.

    Uses Smith normal form invariants: zero invariants correspond to free generators.
    """
    invs = self.invariants()
    free_rank = sum(1 for x in invs if x == 0)
    R = self.base_ring()
    return FreeModule(R, free_rank)


def _fgp_torsion_part(self: Any) -> Any:
    """Return the torsion part of this FGP module as an FGP module."""
    invs = self.invariants()
    torsion_invs = tuple(x for x in invs if x != 0)
    if not torsion_invs:
        # Trivial torsion part: zero module
        V = FreeModule(self.base_ring(), 1)
        return V.quotient(V)
    R = self.base_ring()
    V = FreeModule(R, len(torsion_invs))
    sub = V.submodule([V.gen(i) * torsion_invs[i] for i in range(len(torsion_invs))])
    return V.quotient(sub)


def _fgp_order(self: Any) -> Any:
    """Return the finite cardinality when available."""
    return self.cardinality()


def _fgp_invariant_factors(self: Any) -> tuple[Any, ...]:
    """Group-facing alias for Sage's invariant tuple."""
    return tuple(self.invariants())


def _fgp_elementary_divisors(self: Any) -> tuple[Any, ...]:
    """Return prime-power elementary divisors."""
    return _elementary_divisors_from_invariants(self.invariants())


def _fgp_smith_generators(self: Any) -> tuple[Any, ...]:
    """Group-facing alias for Smith-form generators."""
    return tuple(self.smith_form_gens())


def _fgp_coordinates_in_generators(
    self: Any,
    x: Any,
    *,
    reduce: bool = True,
) -> Any:
    """Return coordinates in Sage's distinguished generators."""
    return self.gens_vector(x, reduce=reduce)


def _fgp_coordinates_in_smith_basis(self: Any, x: Any) -> Any:
    """Return coordinates in Smith generators when Sage exposes the conversion."""
    if hasattr(self, "coordinate_vector"):
        return self.coordinate_vector(x)
    return self.gens_vector(x)


def _fgp_generator_relations(self: Any) -> Any:
    """Return the relation module W in the presentation V/W."""
    return self.W()


def _fgp_cover(self: Any) -> Any:
    """Return the cover module V in the presentation V/W."""
    return self.V()


def _fgp_relations(self: Any) -> Any:
    """Return the relation module W in the presentation V/W."""
    return self.W()


def _tqm_as_additive_abelian_group(self: Any) -> Any:
    """Return the finite additive group view; Sage's FGP parent is the backend."""
    return AdditiveAbelianGroupWrapper.from_generators(self.gens(), universe=self)


def _tqm_order(self: Any) -> Any:
    """Return the finite cardinality."""
    return self.cardinality()


def _tqm_exponent(self: Any) -> Any:
    """Return the exponent of the underlying finite abelian group."""
    exponent = ZZ.one()
    for invariant in self.invariants():
        if invariant:
            exponent = exponent.lcm(invariant)
    return exponent


def _tqm_is_cyclic(self: Any) -> bool:
    """Return whether the underlying finite abelian group is cyclic."""
    return sum(1 for invariant in self.invariants() if invariant not in (0, 1)) <= 1


def _tqm_short_name(self: Any) -> str:
    """Return a compact invariant-factor name for the finite abelian group."""
    invariants = tuple(invariant for invariant in self.invariants() if invariant not in (0, 1))
    if not invariants:
        return "0"
    return " x ".join(f"C{invariant}" for invariant in invariants)


def _tqm_generator_orders(self: Any) -> tuple[Any, ...]:
    """Return additive orders of distinguished generators."""
    return tuple(generator.additive_order() for generator in self.gens())


def _tqm_zero(self: Any) -> Any:
    """Return the additive identity."""
    return self(0)


def _tqm_discrete_exp(
    self: Any,
    v: Any,
    gens: Any | None = None,
) -> Any:
    """Build an element from coordinates in the requested generators."""
    if gens is None:
        return self.linear_combination_of_smith_form_gens(v)
    return AdditiveAbelianGroupWrapper.from_generators(
        gens, universe=self
    ).discrete_exp(v)


def _tqm_coordinates(
    self: Any,
    x: Any,
    gens: Any | None = None,
    *,
    reduce: bool = True,
) -> Any:
    """Return additive coordinates of an element."""
    if gens is None:
        return self.gens_vector(x, reduce=reduce)
    return AdditiveAbelianGroupWrapper.from_generators(
        gens, universe=self
    ).discrete_log(x)


def _tqm_relations_among(self: Any, gens: Any) -> Any:
    """Return relations among the supplied generators through Sage's additive wrapper."""
    return AdditiveAbelianGroupWrapper.from_generators(gens, universe=self).W()


def _tqm_basis_from_generators(self: Any, gens: Any) -> Any:
    """Return independent additive generators generated by the supplied elements."""
    return AdditiveAbelianGroupWrapper.from_generators(gens, universe=self).gens()


def _tqm_from_generators(self: Any, gens: Any) -> Any:
    """Return the form-preserving torsion quadratic submodule generated by gens."""
    return self.submodule_with_gens(gens)


def _tqm_subgroup(self: Any, gens: Any) -> Any:
    """Group-facing alias for Sage torsion-quadratic submodules."""
    return self.submodule_with_gens(gens)


def _tqm_subgroups(self: Any) -> Any:
    """Group-facing alias for all finite submodules."""
    return self.all_submodules()


def _tqm_p_torsion(self: Any, p: Any, *, k: int = 1) -> Any:
    """Return the subgroup killed by p^k."""
    zero = _tqm_zero(self)
    return self.submodule_with_gens([x for x in self if (p**k) * x == zero])


def _tqm_primary_decomposition(self: Any) -> tuple[Any, ...]:
    """Return primary parts indexed by primes dividing the exponent."""
    return tuple(self.primary_part(p) for p, _ in _tqm_exponent(self).factor())


def _tqm_p_primary_part(self: Any, p: Any) -> Any:
    """Group-facing alias for Sage's primary_part."""
    return self.primary_part(p)


def _tqm_rank_p(self: Any, p: Any) -> int:
    """Return the p-rank of the underlying finite abelian group."""
    return sum(1 for invariant in self.invariants() if invariant % p == 0)


def _tqm_length_p(self: Any, p: Any) -> int:
    """Return the p-length of the underlying finite abelian group."""
    return len(self.primary_part(p).invariants())


def _tqm_contains_subgroup(self: Any, H: Any) -> bool:
    """Return whether H is a submodule of this finite module."""
    return bool(H.is_submodule(self))


def _tqm_quotient_group(self: Any, H: Any) -> Any:
    """Return the ordinary quotient by H."""
    return self.quotient(H)


def _tqm_quotient_map(self: Any, H: Any) -> Any:
    """Return the quotient map to the quotient by H."""
    return self.quotient(H).quotient_map()


def _tqm_cosets(self: Any, H: Any) -> Any:
    """Return cosets represented through the quotient object."""
    return self.quotient(H).list()


def _tqm_torsion_subgroup(self: Any) -> Any:
    """Return the torsion subgroup; torsion quadratic modules are torsion."""
    return self


def _tqm_automorphism_group(self: Any) -> Any:
    """Return the GAP-backed automorphism group of the underlying finite abelian group."""
    return AbelianGroupGap([invariant for invariant in self.invariants() if invariant != 1]).automorphism_group()


def _tqm_character_group(self: Any) -> Any:
    """Return the abstract Pontryagin dual, isomorphic to the underlying finite abelian group."""
    return AbelianGroupGap([invariant for invariant in self.invariants() if invariant != 1])


def _tqm_b(self: Any, x: Any, y: Any) -> Any:
    """Evaluate the finite bilinear pairing."""
    return x * y


def _tqm_q(self: Any, x: Any) -> Any:
    """Evaluate the finite quadratic refinement."""
    return x.q()


def _tqm_orthogonal_group(
    self: Any, gens: Any | None = None, *, kind: str = "quadratic", check: bool = False
) -> Any:
    """Return the requested finite form-preserving group."""
    if kind == "quadratic":
        return _native_tqm_orthogonal_group(self, gens=gens, check=check)
    if kind == "bilinear":
        raise NotImplementedError("Sage exposes quadratic orthogonal_group here, not the larger bilinear group")
    raise ValueError("orthogonal_group kind must be 'quadratic' or 'bilinear'")


def _tqm_bilinear_orthogonal_group(self: Any) -> Any:
    """Return the bilinear orthogonal group when Sage exposes it."""
    raise NotImplementedError("Sage exposes quadratic orthogonal_group here, not the larger bilinear group")


def _tqm_normal_form(
    self: Any, *, partial: bool = False, return_isometry: bool = False
) -> Any:
    """Return Sage's torsion quadratic normal form with plan-compatible keyword spelling."""
    if return_isometry:
        raise NotImplementedError("Sage normal_form does not return an isometry")
    return _native_tqm_normal_form(self, partial=partial)


def _tqm_is_isotropic_element(self: Any, x: Any) -> bool:
    """Return whether the quadratic value of x is zero."""
    return bool(x.q() == 0)


def _tqm_isotropic_elements(self: Any) -> tuple[Any, ...]:
    """Return isotropic elements."""
    return tuple(x for x in self if _tqm_is_isotropic_element(self, x))


def _tqm_is_isotropic_subgroup(self: Any, H: Any) -> bool:
    """Return whether every element of H is isotropic."""
    return all(_tqm_is_isotropic_element(self, x) for x in H)


def _tqm_isotropic_subgroups(self: Any) -> tuple[Any, ...]:
    """Return isotropic subgroups."""
    return tuple(H for H in self.all_submodules() if _tqm_is_isotropic_subgroup(self, H))


def _tqm_orthogonal(self: Any, H: Any) -> Any:
    """Return the orthogonal subgroup."""
    return self.orthogonal_submodule_to(H)


def _tqm_orthogonal_quotient(self: Any, H: Any) -> Any:
    """Return H^perp/H."""
    return self.orthogonal_submodule_to(H).quotient(H)


def _tqm_restricted_form(self: Any, H: Any) -> Any:
    """Return H with Sage's restricted torsion quadratic form."""
    return H


def _tqm_pushforward_form(self: Any, phi: Any) -> Any:
    """Return the form transported forward along a morphism with a lift."""
    assert hasattr(phi, "lift")
    return _TransportedTorsionQuadraticForm(self, phi, direction="pushforward")


def _tqm_pullback_form(self: Any, phi: Any) -> Any:
    """Return the pullback finite form along a callable morphism."""
    assert callable(phi)
    return _TransportedTorsionQuadraticForm(self, phi, direction="pullback")


def _tqm_subquotient_form(self: Any, H: Any, K: Any) -> Any:
    """Return the induced Sage quotient K/H."""
    return K.quotient(H)


def _tqm_is_lagrangian(self: Any, H: Any) -> bool:
    """Return whether H equals its orthogonal complement."""
    return bool(self.orthogonal_submodule_to(H) == H)


def _tqm_lagrangian_subgroups(self: Any) -> tuple[Any, ...]:
    """Return lagrangian subgroups."""
    return tuple(H for H in _tqm_isotropic_subgroups(self) if _tqm_is_lagrangian(self, H))


def _tqm_is_metabolic(self: Any) -> bool:
    """Return whether a lagrangian subgroup exists."""
    return bool(_tqm_lagrangian_subgroups(self))


def _tqm_is_anisotropic(self: Any) -> bool:
    """Return whether zero is the only isotropic element."""
    zero = _tqm_zero(self)
    return all(x == zero for x in _tqm_isotropic_elements(self))


def _tqm_is_maximal_isotropic(self: Any, H: Any) -> bool:
    """Return whether H is maximal among isotropic subgroups."""
    return _tqm_is_isotropic_subgroup(self, H) and not any(
        H != K and H.is_submodule(K) for K in _tqm_isotropic_subgroups(self)
    )


def _tqm_maximal_isotropic_subgroups(self: Any) -> tuple[Any, ...]:
    """Return maximal isotropic subgroups."""
    return tuple(H for H in _tqm_isotropic_subgroups(self) if _tqm_is_maximal_isotropic(self, H))


def _tqm_isometry_to(self: Any, other: Any, *, kind: str = "quadratic") -> Any:
    """Direct form isometry construction is not exposed by Sage."""
    raise NotImplementedError("Sage does not expose a direct torsion-quadratic isometry_to constructor")


def _tqm_is_isomorphic_to(self: Any, other: Any, *, kind: str = "quadratic") -> bool:
    """Return finite-group or finite-form isomorphism status."""
    if kind == "group":
        return tuple(self.invariants()) == tuple(other.invariants())
    if kind == "bilinear":
        raise NotImplementedError("Sage does not expose bilinear finite-form isomorphism here")
    if kind != "quadratic":
        raise ValueError("is_isomorphic_to kind must be 'group', 'bilinear', or 'quadratic'")
    return bool(_native_tqm_normal_form(self) == _native_tqm_normal_form(other))


def _tqm_pairing_character(self: Any, x: Any) -> Any:
    """Return the character y |-> b(x, y)."""
    return lambda y: x * y


def _tqm_left_kernel(self: Any) -> Any:
    """Return the left kernel of the finite pairing."""
    return self.submodule_with_gens([x for x in self if all(x * y == 0 for y in self)])


def _tqm_right_kernel(self: Any) -> Any:
    """Return the right kernel of the finite pairing."""
    return self.submodule_with_gens([y for y in self if all(x * y == 0 for x in self)])


def _tqm_radical(self: Any) -> Any:
    """Return the finite pairing radical."""
    return _tqm_left_kernel(self)


def _tqm_is_nondegenerate(self: Any) -> bool:
    """Return whether the finite bilinear pairing is nondegenerate."""
    return bool(
        _tqm_left_kernel(self).cardinality() == 1
        and _tqm_right_kernel(self).cardinality() == 1
    )


def _tqm_pairing_isomorphism_to_dual(self: Any) -> Any:
    """Return the pairing map when the pairing is nondegenerate."""
    if not _tqm_is_nondegenerate(self):
        raise ValueError("the pairing map is an isomorphism only for nondegenerate pairings")
    return lambda x: _tqm_pairing_character(self, x)


def _tqm_annihilator_subgroup(self: Any, H: Any) -> Any:
    """Return the annihilator of H under the finite pairing."""
    return self.orthogonal_submodule_to(H)


def install() -> None:
    """Install free_part/torsion_part on FGP module class.

    Idempotent: safe to call multiple times.
    """
    global _installed
    if _installed:
        return

    FGP_Module_class.free_part = _fgp_free_part
    FGP_Module_class.torsion_part = _fgp_torsion_part

    fgp_aliases = {
        "order": _fgp_order,
        "invariant_factors": _fgp_invariant_factors,
        "elementary_divisors": _fgp_elementary_divisors,
        "smith_generators": _fgp_smith_generators,
        "coordinates_in_generators": _fgp_coordinates_in_generators,
        "coordinates_in_smith_basis": _fgp_coordinates_in_smith_basis,
        "generator_relations": _fgp_generator_relations,
        "cover": _fgp_cover,
        "relations": _fgp_relations,
    }
    for name, method in fgp_aliases.items():
        if not hasattr(FGP_Module_class, name):
            setattr(FGP_Module_class, name, method)

    tqm_aliases = {
        "as_additive_abelian_group": _tqm_as_additive_abelian_group,
        "underlying_abelian_group": _tqm_as_additive_abelian_group,
        "order": _tqm_order,
        "invariant_factors": _fgp_invariant_factors,
        "elementary_divisors": _fgp_elementary_divisors,
        "exponent": _tqm_exponent,
        "is_cyclic": _tqm_is_cyclic,
        "short_name": _tqm_short_name,
        "zero": _tqm_zero,
        "identity": _tqm_zero,
        "generator_orders": _tqm_generator_orders,
        "smith_generators": _fgp_smith_generators,
        "coordinates_in_generators": _fgp_coordinates_in_generators,
        "coordinates_in_smith_basis": _fgp_coordinates_in_smith_basis,
        "generator_relations": _fgp_generator_relations,
        "discrete_exp": _tqm_discrete_exp,
        "coordinates": _tqm_coordinates,
        "discrete_log": _tqm_coordinates,
        "relations_among": _tqm_relations_among,
        "basis_from_generators": _tqm_basis_from_generators,
        "from_generators": _tqm_from_generators,
        "subgroup": _tqm_subgroup,
        "subgroup_generated_by": _tqm_subgroup,
        "subgroups": _tqm_subgroups,
        "all_subgroups": _tqm_subgroups,
        "contains_subgroup": _tqm_contains_subgroup,
        "quotient_group": _tqm_quotient_group,
        "quotient_map": _tqm_quotient_map,
        "cosets": _tqm_cosets,
        "p_torsion": _tqm_p_torsion,
        "p_primary_part": _tqm_p_primary_part,
        "primary_decomposition": _tqm_primary_decomposition,
        "primary_parts": _tqm_primary_decomposition,
        "rank_p": _tqm_rank_p,
        "length_p": _tqm_length_p,
        "torsion_subgroup": _tqm_torsion_subgroup,
        "automorphism_group": _tqm_automorphism_group,
        "character_group": _tqm_character_group,
        "pontryagin_dual": _tqm_character_group,
        "b": _tqm_b,
        "q": _tqm_q,
        "is_isotropic_element": _tqm_is_isotropic_element,
        "isotropic_elements": _tqm_isotropic_elements,
        "is_isotropic_subgroup": _tqm_is_isotropic_subgroup,
        "is_totally_isotropic": _tqm_is_isotropic_subgroup,
        "isotropic_subgroups": _tqm_isotropic_subgroups,
        "orthogonal": _tqm_orthogonal,
        "orthogonal_complement": _tqm_orthogonal,
        "orthogonal_quotient": _tqm_orthogonal_quotient,
        "restricted_form": _tqm_restricted_form,
        "pushforward_form": _tqm_pushforward_form,
        "pullback_form": _tqm_pullback_form,
        "subquotient_form": _tqm_subquotient_form,
        "is_lagrangian": _tqm_is_lagrangian,
        "is_metabolic": _tqm_is_metabolic,
        "is_anisotropic": _tqm_is_anisotropic,
        "is_maximal_isotropic": _tqm_is_maximal_isotropic,
        "maximal_isotropic_subgroups": _tqm_maximal_isotropic_subgroups,
        "lagrangian_subgroups": _tqm_lagrangian_subgroups,
        "metabolizers": _tqm_lagrangian_subgroups,
        "quadratic_orthogonal_group": _tqm_orthogonal_group,
        "bilinear_orthogonal_group": _tqm_bilinear_orthogonal_group,
        "isometry_group": _tqm_orthogonal_group,
        "isometry_to": _tqm_isometry_to,
        "is_isomorphic_to": _tqm_is_isomorphic_to,
        "pairing_character": _tqm_pairing_character,
        "pairing_isomorphism_to_dual": _tqm_pairing_isomorphism_to_dual,
        "annihilator_subgroup": _tqm_annihilator_subgroup,
        "left_kernel": _tqm_left_kernel,
        "right_kernel": _tqm_right_kernel,
        "radical": _tqm_radical,
        "is_nondegenerate": _tqm_is_nondegenerate,
        "normal_form": _tqm_normal_form,
    }
    for name, method in tqm_aliases.items():
        if not hasattr(TorsionQuadraticModule, name):
            setattr(TorsionQuadraticModule, name, method)
    TorsionQuadraticModule.normal_form = _tqm_normal_form
    TorsionQuadraticModule.orthogonal_group = _tqm_orthogonal_group

    _installed = True
