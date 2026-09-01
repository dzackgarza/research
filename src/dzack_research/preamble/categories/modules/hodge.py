r"""Determinant, Poincaré-duality, and Hodge constructions on finite free modules."""

from dzack_research.preamble.categories.abstract_categories import Isomorphism
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)


def _require_finite_free(module) -> int:
    from sage.rings.infinity import Infinity
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
        FinitelyGeneratedFreeModules,
    )

    ring = module.base_ring()
    if module not in FinitelyGeneratedFreeModules(ring):
        raise TypeError("this construction requires a finite free module")
    rank = module.rank()
    if rank == Infinity:
        raise TypeError("this construction requires finite rank")
    return int(rank)


def _power_word(label, degree: int) -> tuple:
    if degree == 0:
        return ()
    if degree == 1:
        return (label,)
    return tuple(label)


def _power_label(word: tuple, degree: int):
    if degree == 0:
        return 0
    if degree == 1:
        return word[0]
    return tuple(word)


def _unique_generator(module):
    labels = tuple(module.module_generating_set())
    if len(labels) != 1:
        raise ValueError(f"{module} is not represented as a rank-one free module")
    return module.module_generator(labels[0])


def DeterminantLine(module):
    r"""Return ``det(module) = Lambda^rank(module) module``."""
    from dzack_research.preamble.categories.modules.powers import AlternatingPower

    rank = _require_finite_free(module)
    return AlternatingPower(module, rank)


def ExteriorForms(module, degree):
    r"""Return ``Lambda^degree(module^vee)``."""
    from dzack_research.preamble.categories.modules.powers import AlternatingPower

    rank = _require_finite_free(module)
    degree = int(degree)
    if degree < 0 or degree > rank:
        raise ValueError(f"an exterior degree must lie in [0,{rank}]")
    return AlternatingPower(module.dual_module(), degree)


def VolumeTrivialization(module, forward, inverse):
    r"""Return the stated isomorphism ``det(module) ~= R``.

    No orientation or volume is inferred from a framing.  This constructor
    merely verifies two already represented mutually inverse module maps.
    """
    from dzack_research.preamble.categories.modules.framed.finitely_generated.ring_as_module import (
        ring_as_module,
    )
    from dzack_research.preamble.categories.modules.pure.modules import Modules

    determinant = DeterminantLine(module)
    scalars = ring_as_module(module.base_ring())
    if forward.domain() is not determinant or forward.codomain() is not scalars:
        raise ValueError("the volume map must have type det(M) -> R")
    if inverse.domain() is not scalars or inverse.codomain() is not determinant:
        raise ValueError("the inverse volume map must have type R -> det(M)")
    result = Isomorphism(forward, inverse)
    if result not in Modules(module.base_ring()).Iso(determinant, scalars):
        raise ValueError("the stated maps do not define a module volume trivialization")
    return result


def FramingVolumeTrivialization(module, unit=None):
    r"""Explicitly trivialize ``det(M)`` using the selected framing.

    This is deliberately opt-in: a chosen module framing is not silently
    treated as orientation data.  ``unit`` rescales the selected top wedge and
    must be a unit of the coefficient ring.
    """
    from dzack_research.preamble.categories.modules.framed.finitely_generated.ring_as_module import (
        ring_as_module,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )
    from dzack_research.preamble.categories.rings import engine_ring

    determinant = DeterminantLine(module)
    scalars = ring_as_module(module.base_ring())
    top = _unique_generator(determinant)
    one = _unique_generator(scalars)
    engine = engine_ring(module.base_ring())
    unit = engine.one() if unit is None else engine(unit)
    if not unit.is_unit():
        raise ValueError("a volume trivialization must send a determinant basis to a unit")
    inverse_unit = unit.inverse_of_unit()
    forward = module_homset(determinant, scalars)(
        {next(iter(determinant.module_generating_set())): scalars.scalar_multiple(unit, one)}
    )
    inverse = module_homset(scalars, determinant)(
        {next(iter(scalars.module_generating_set())): determinant.scalar_multiple(inverse_unit, top)}
    )
    return VolumeTrivialization(module, forward, inverse)


def _volume_scalars(module, volume):
    from dzack_research.preamble.categories.modules.framed.finitely_generated.ring_as_module import (
        ring_as_module,
    )
    from dzack_research.preamble.categories.modules.pure.modules import Modules

    determinant = DeterminantLine(module)
    scalars = ring_as_module(module.base_ring())
    if volume not in Modules(module.base_ring()).Iso(determinant, scalars):
        raise TypeError("the Hodge datum requires an isomorphism det(M) ~= R")
    top = _unique_generator(determinant)
    one = _unique_generator(scalars)
    forward_coefficients = module_coefficients(volume(top), scalars)
    inverse_coefficients = module_coefficients(volume.inverse()(one), determinant)
    scalar_label = next(iter(scalars.module_generating_set()))
    determinant_label = next(iter(determinant.module_generating_set()))
    return (
        forward_coefficients.get(scalar_label, module.base_ring().zero()),
        inverse_coefficients.get(determinant_label, module.base_ring().zero()),
    )


def PoincareDuality(module, volume, degree):
    r"""Return ``Lambda^k M ~= Lambda^(n-k) M^vee`` from ``volume``."""
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )
    from dzack_research.preamble.categories.modules.powers import AlternatingPower
    from dzack_research.preamble.categories.modules.pure.modules import Modules

    rank = _require_finite_free(module)
    degree = int(degree)
    if degree < 0 or degree > rank:
        raise ValueError(f"an exterior degree must lie in [0,{rank}]")
    volume_scalar, inverse_volume_scalar = _volume_scalars(module, volume)
    dual = module.dual_module()
    source = AlternatingPower(module, degree)
    target = AlternatingPower(dual, rank - degree)
    module_labels = tuple(module.module_generating_set())
    positions = {label: index for index, label in enumerate(module_labels)}

    forward_images = {}
    for source_label in source.module_generating_set():
        word = _power_word(source_label, degree)
        occupied = {positions[label] for label in word}
        complement = tuple(
            label
            for index, label in enumerate(module_labels)
            if index not in occupied
        )
        complement_positions = tuple(positions[label] for label in complement)
        inversions = sum(
            left > right
            for left in tuple(positions[label] for label in word)
            for right in complement_positions
        )
        coefficient = -volume_scalar if inversions % 2 else volume_scalar
        target_label = _power_label(complement, rank - degree)
        forward_images[source_label] = target.scalar_multiple(
            coefficient,
            target.module_generator(target_label),
        )

    inverse_images = {}
    for target_label in target.module_generating_set():
        complement = _power_word(target_label, rank - degree)
        complement_positions = {positions[label] for label in complement}
        word = tuple(
            label
            for index, label in enumerate(module_labels)
            if index not in complement_positions
        )
        inversions = sum(
            left > right
            for left in tuple(positions[label] for label in word)
            for right in tuple(positions[label] for label in complement)
        )
        coefficient = (
            -inverse_volume_scalar if inversions % 2 else inverse_volume_scalar
        )
        source_label = _power_label(word, degree)
        inverse_images[target_label] = source.scalar_multiple(
            coefficient,
            source.module_generator(source_label),
        )

    forward = module_homset(source, target)(forward_images)
    inverse = module_homset(target, source)(inverse_images)
    result = Isomorphism(forward, inverse)
    if result not in Modules(module.base_ring()).Iso(source, target):
        raise ArithmeticError("the represented Poincaré maps failed to define an isomorphism")
    return result


def AlgebraicCorrelationMorphism(metric):
    r"""Return ``g^flat : M -> M^vee`` for a scalar-valued bilinear metric."""
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )

    _require_finite_free(metric)
    if metric.value_module() is not metric.base_ring():
        raise TypeError("the algebraic correlation requires a scalar-valued form")
    dual = metric.dual_module()
    source_labels = tuple(metric.module_generating_set())
    dual_labels = tuple(dual.module_generating_set())
    images = {}
    for source_label in source_labels:
        source_generator = metric.module_generator(source_label)
        images[source_label] = dual.linear_combination(
            {
                dual_label: metric.b(
                    source_generator,
                    metric.module_generator(dual_label),
                )
                for dual_label in dual_labels
                if metric.b(
                    source_generator,
                    metric.module_generator(dual_label),
                )
                != metric.base_ring().zero()
            }
        )
    return module_homset(metric, dual)(images)


def CorrelationIsomorphism(metric):
    r"""Return the perfect correlation ``M ~= M^vee`` for a unimodular form."""
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )
    from dzack_research.preamble.categories.modules.pure.modules import Modules

    if not metric.is_unimodular():
        raise ValueError(
            "an integral Hodge star on covariant forms requires a perfect/unimodular metric"
        )
    forward = AlgebraicCorrelationMorphism(metric)
    dual = forward.codomain()
    inverse = module_homset(dual, metric)(
        {
            label: forward.lift(dual.module_generator(label))
            for label in dual.module_generating_set()
        }
    )
    result = Isomorphism(forward, inverse)
    if result not in Modules(metric.base_ring()).Iso(metric, dual):
        raise ArithmeticError("the represented correlation failed to define an isomorphism")
    return result


def HodgeDiscriminant(metric, volume):
    r"""Return ``Delta_(g,eps) = det(g) / eps(e_1 wedge ... wedge e_n)^2``."""
    _require_finite_free(metric)
    _volume_scalar, inverse_volume_scalar = _volume_scalars(metric, volume)
    return metric.gram_tensor().det() * inverse_volume_scalar**2


def HodgeStar(metric, volume, degree):
    r"""Return the Hodge isomorphism on covariant ``degree``-forms.

    For a perfect metric this is the categorical composite

    ``Lambda^k M^vee --Lambda^k(g^sharp)--> Lambda^k M --PD--> Lambda^(n-k) M^vee``.
    """
    from dzack_research.preamble.categories.modules.powers import alternating_power_morphism
    from dzack_research.preamble.categories.modules.pure.modules import Modules

    rank = _require_finite_free(metric)
    degree = int(degree)
    if degree < 0 or degree > rank:
        raise ValueError(f"an exterior degree must lie in [0,{rank}]")
    correlation = CorrelationIsomorphism(metric)
    poincare = PoincareDuality(metric, volume, degree)
    raise_metric = alternating_power_morphism(correlation.inverse(), degree)
    lower_metric = alternating_power_morphism(correlation.forward(), degree)
    forward = poincare.forward() * raise_metric
    inverse = lower_metric * poincare.inverse()
    result = Isomorphism(forward, inverse)
    source = ExteriorForms(metric, degree)
    target = ExteriorForms(metric, rank - degree)
    if result not in Modules(metric.base_ring()).Iso(source, target):
        raise ArithmeticError("the represented form Hodge maps failed to define an isomorphism")
    return result


def MultivectorHodgeStar(metric, volume, degree):
    r"""Return the integral multivector Hodge map ``Lambda^k M -> Lambda^(n-k) M``.

    Unlike the covariant-form Hodge star, this direction uses ``g^flat`` and
    therefore does not require the metric to be perfect over the coefficient
    ring.  It need not be an isomorphism for a non-unimodular metric.
    """
    from dzack_research.preamble.categories.modules.powers import (
        AlternatingPower,
        alternating_power_morphism,
    )

    rank = _require_finite_free(metric)
    degree = int(degree)
    if degree < 0 or degree > rank:
        raise ValueError(f"an exterior degree must lie in [0,{rank}]")
    correlation = AlgebraicCorrelationMorphism(metric)
    poincare_complement = PoincareDuality(metric, volume, rank - degree)
    lower_metric = alternating_power_morphism(correlation, degree)
    forward = poincare_complement.inverse() * lower_metric
    source = AlternatingPower(metric, degree)
    target = AlternatingPower(metric, rank - degree)
    if forward.domain() is not source or forward.codomain() is not target:
        raise ArithmeticError("the represented multivector Hodge map has the wrong endpoints")
    return forward


def HodgeStarOverFractionField(metric, volume, degree):
    r"""Return the covariant-form Hodge isomorphism after ``R -> Frac(R)``.

    This is the explicit scalar-extension path for a nondegenerate but
    non-unimodular metric.  The returned isomorphism lives over the fraction
    field; it is never reported as an integral Hodge star on ``metric``.
    """
    from dzack_research.preamble.categories.rings import engine_ring

    _require_finite_free(metric)
    if not metric.is_nondegenerate():
        raise ValueError("fraction-field Hodge star requires a nondegenerate metric")
    ring = metric.base_ring()
    try:
        fraction_field = ring.fraction_field()
    except (AttributeError, NotImplementedError) as error:
        raise TypeError("the coefficient ring has no represented fraction field") from error
    if fraction_field is ring:
        return HodgeStar(metric, volume, degree)
    ring_map = engine_ring(fraction_field).coerce_map_from(engine_ring(ring))
    if ring_map is None:
        raise ValueError("the fraction field does not expose the canonical scalar extension")
    changed_metric = metric.base_change(ring_map)
    volume_scalar, _inverse_volume_scalar = _volume_scalars(metric, volume)
    changed_volume = FramingVolumeTrivialization(
        changed_metric,
        unit=engine_ring(fraction_field)(volume_scalar),
    )
    return HodgeStar(changed_metric, changed_volume, degree)


determinant_line = DeterminantLine
exterior_forms = ExteriorForms
volume_trivialization = VolumeTrivialization
framing_volume_trivialization = FramingVolumeTrivialization
poincare_duality = PoincareDuality
algebraic_correlation_morphism = AlgebraicCorrelationMorphism
correlation_isomorphism = CorrelationIsomorphism
hodge_discriminant = HodgeDiscriminant
hodge_star = HodgeStar
hodge_star_over_fraction_field = HodgeStarOverFractionField
multivector_hodge_star = MultivectorHodgeStar


__all__ = [
    "AlgebraicCorrelationMorphism",
    "CorrelationIsomorphism",
    "DeterminantLine",
    "ExteriorForms",
    "FramingVolumeTrivialization",
    "HodgeDiscriminant",
    "HodgeStar",
    "HodgeStarOverFractionField",
    "MultivectorHodgeStar",
    "PoincareDuality",
    "VolumeTrivialization",
    "algebraic_correlation_morphism",
    "correlation_isomorphism",
    "determinant_line",
    "exterior_forms",
    "framing_volume_trivialization",
    "hodge_discriminant",
    "hodge_star",
    "hodge_star_over_fraction_field",
    "multivector_hodge_star",
    "poincare_duality",
    "volume_trivialization",
]
