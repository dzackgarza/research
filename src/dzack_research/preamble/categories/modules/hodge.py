r"""Determinant, Poincaré-duality, and Hodge constructions on finite free modules."""

from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedFreeModules,
    Modules,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FramedFreeModules,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleEmbedding,
)
from dzack_research.preamble.categories.rings.ring_foundation import _engine_ring


def _require_finite_free(module) -> int:
    from sage.rings.infinity import Infinity

    ring = module.base_ring()
    if module not in FinitelyGeneratedFreeModules(ring):
        raise TypeError("this construction requires a finite free module")
    rank = module.module_rank()
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


def _determinant_line(module):
    r"""Return ``det(module) = Lambda^rank(module) module``."""

    rank = _require_finite_free(module)
    return module.exterior_power(rank)


def _exterior_forms(module, degree):
    r"""Return ``Lambda^degree(module^vee)``."""

    rank = _require_finite_free(module)
    degree = int(degree)
    if degree < 0 or degree > rank:
        raise ValueError(f"an exterior degree must lie in [0,{rank}]")
    return module.dual_module().exterior_power(degree)


def _volume_trivialization(module, forward, inverse):
    r"""Return the stated isomorphism ``det(module) ~= R``.

    No orientation or volume is inferred from a framing.  This constructor
    merely verifies two already represented mutually inverse module maps.
    """

    determinant = module.determinant_line()
    scalars = module.base_ring().regular_module()
    if forward.domain() is not determinant or forward.codomain() is not scalars:
        raise ValueError("the volume map must have type det(M) -> R")
    if inverse.domain() is not scalars or inverse.codomain() is not determinant:
        raise ValueError("the inverse volume map must have type R -> det(M)")
    modules = Modules(module.base_ring())
    result = modules.Core().Mor(determinant, scalars)(forward, inverse)
    if result not in modules.Iso(determinant, scalars):
        raise ValueError("the stated maps do not define a module volume trivialization")
    return result


def _framing_volume_trivialization(module, unit=None):
    r"""Explicitly trivialize ``det(M)`` using the selected framing.

    This is deliberately opt-in: a chosen module framing is not silently
    treated as orientation data.  ``unit`` rescales the selected top wedge and
    must be a unit of the coefficient ring.
    """
    determinant = module.determinant_line()
    ring = module.base_ring()
    scalars = ring.regular_module()
    top = _unique_generator(determinant)
    one = _unique_generator(scalars)
    unit = ring.one() if unit is None else ring(unit)
    if not unit.is_unit():
        raise ValueError("a volume trivialization must send a determinant basis to a unit")
    inverse_unit = unit.inverse_of_unit()
    forward = determinant.module_category().Mor(determinant, scalars)(
        {next(iter(determinant.module_generating_set())): scalars.scalar_multiple(unit, one)}
    )
    inverse = scalars.module_category().Mor(scalars, determinant)(
        {next(iter(scalars.module_generating_set())): determinant.scalar_multiple(inverse_unit, top)}
    )
    return module.volume_trivialization(forward, inverse)


def _volume_scalars(module, volume):

    determinant = module.determinant_line()
    scalars = module.base_ring().regular_module()
    if volume not in Modules(module.base_ring()).Iso(determinant, scalars):
        raise TypeError("the Hodge datum requires an isomorphism det(M) ~= R")
    top = _unique_generator(determinant)
    one = _unique_generator(scalars)
    forward_coefficients = scalars.framing_coefficients(volume(top))
    inverse_coefficients = determinant.framing_coefficients(volume.inverse()(one))
    scalar_label = next(iter(scalars.module_generating_set()))
    determinant_label = next(iter(determinant.module_generating_set()))
    return (
        forward_coefficients.get(scalar_label, module.base_ring().zero()),
        inverse_coefficients.get(determinant_label, module.base_ring().zero()),
    )


def _poincare_duality(module, volume, degree):
    r"""Return ``Lambda^k M ~= Lambda^(n-k) M^vee`` from ``volume``."""

    rank = _require_finite_free(module)
    degree = int(degree)
    if degree < 0 or degree > rank:
        raise ValueError(f"an exterior degree must lie in [0,{rank}]")
    volume_scalar, inverse_volume_scalar = _volume_scalars(module, volume)
    dual = module.dual_module()
    source = module.exterior_power(degree)
    target = dual.exterior_power(rank - degree)
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

    forward = source.module_category().Mor(source, target)(forward_images)
    inverse = target.module_category().Mor(target, source)(inverse_images)
    modules = Modules(module.base_ring())
    result = modules.Core().Mor(source, target)(forward, inverse)
    if result not in modules.Iso(source, target):
        raise ArithmeticError("the represented Poincaré maps failed to define an isomorphism")
    return result


class _ConstructedCorrelationEmbedding(ModuleEmbedding):
    r"""A correlation whose injectivity is already part of the formed object's construction."""

    def _injectivity_derivation(self):
        return True


def _algebraic_correlation_morphism(metric, *, injective=False):
    r"""Return ``g^flat : M -> M^vee`` for a scalar-valued bilinear metric."""

    if metric.value_module() is not metric.base_ring():
        raise TypeError("the algebraic correlation requires a scalar-valued form")
    ring = metric.base_ring()
    if metric not in FramedFreeModules(ring):
        raise TypeError(
            "the represented algebraic correlation currently requires a framed free module"
        )
    dual = metric.dual_module()
    source_labels = metric.module_generating_set()

    def correlation_from_generator_images(images):
        if injective:
            return _ConstructedCorrelationEmbedding(
                Modules(ring).Mono(metric, dual),
                images,
            )
        return metric.module_category().Mor(metric, dual)(images)

    match source_labels.cardinality().is_finite():
        case True:
            dual_labels = tuple(dual.module_generating_set())

            def finite_generator_image(source_label):
                source_generator = metric.module_generator(source_label)
                coefficients = {}
                for dual_label in dual_labels:
                    coefficient = metric.b(
                        source_generator,
                        metric.module_generator(dual_label),
                    )
                    if coefficient != ring.zero():
                        coefficients[dual_label] = coefficient
                return dual.linear_combination(coefficients)

            return correlation_from_generator_images(finite_generator_image)
        case False:
            regular = ring.regular_module()

            def infinite_generator_image(source_label):
                source_generator = metric.module_generator(source_label)
                return dual(
                    lambda target_label: regular(
                        metric.b(
                            source_generator,
                            metric.module_generator(source_labels(target_label)),
                        )
                    )
                )

            return correlation_from_generator_images(infinite_generator_image)


def _correlation_isomorphism(metric):
    r"""Return the perfect correlation ``M ~= M^vee`` for a unimodular form."""

    if not metric.is_unimodular():
        raise ValueError(
            "an integral Hodge star on covariant forms requires a perfect/unimodular metric"
        )
    forward = metric.algebraic_correlation_morphism()
    dual = forward.codomain()
    inverse = dual.module_category().Mor(dual, metric)(
        {
            label: forward.lift(dual.module_generator(label))
            for label in dual.module_generating_set()
        }
    )
    modules = Modules(metric.base_ring())
    result = modules.Core().Mor(metric, dual)(forward, inverse)
    if result not in modules.Iso(metric, dual):
        raise ArithmeticError("the represented correlation failed to define an isomorphism")
    return result


def _hodge_discriminant(metric, volume):
    r"""Return ``Delta_(g,eps) = det(g) / eps(e_1 wedge ... wedge e_n)^2``."""
    _require_finite_free(metric)
    _volume_scalar, inverse_volume_scalar = _volume_scalars(metric, volume)
    return metric.determinant() * inverse_volume_scalar**2


def _hodge_star(metric, volume, degree):
    r"""Return the Hodge isomorphism on covariant ``degree``-forms.

    For a perfect metric this is the categorical composite

    ``Lambda^k M^vee --Lambda^k(g^sharp)--> Lambda^k M --PD--> Lambda^(n-k) M^vee``.
    """

    rank = _require_finite_free(metric)
    degree = int(degree)
    if degree < 0 or degree > rank:
        raise ValueError(f"an exterior degree must lie in [0,{rank}]")
    correlation = metric.correlation_isomorphism()
    poincare = metric.poincare_duality(volume, degree)
    raise_metric = correlation.inverse().exterior_power(degree)
    lower_metric = correlation.forward().exterior_power(degree)
    forward = poincare.forward() * raise_metric
    inverse = lower_metric * poincare.inverse()
    source = metric.exterior_forms(degree)
    target = metric.exterior_forms(rank - degree)
    modules = Modules(metric.base_ring())
    result = modules.Core().Mor(source, target)(forward, inverse)
    if result not in modules.Iso(source, target):
        raise ArithmeticError("the represented form Hodge maps failed to define an isomorphism")
    return result


def _multivector_hodge_star(metric, volume, degree):
    r"""Return the integral multivector Hodge map ``Lambda^k M -> Lambda^(n-k) M``.

    Unlike the covariant-form Hodge star, this direction uses ``g^flat`` and
    therefore does not require the metric to be perfect over the coefficient
    ring.  It need not be an isomorphism for a non-unimodular metric.
    """

    rank = _require_finite_free(metric)
    degree = int(degree)
    if degree < 0 or degree > rank:
        raise ValueError(f"an exterior degree must lie in [0,{rank}]")
    correlation = metric.algebraic_correlation_morphism()
    poincare_complement = metric.poincare_duality(volume, rank - degree)
    lower_metric = correlation.exterior_power(degree)
    forward = poincare_complement.inverse() * lower_metric
    source = metric.exterior_power(degree)
    target = metric.exterior_power(rank - degree)
    if forward.domain() is not source or forward.codomain() is not target:
        raise ArithmeticError("the represented multivector Hodge map has the wrong endpoints")
    return forward


def _hodge_star_over_fraction_field(metric, volume, degree):
    r"""Return the covariant-form Hodge isomorphism after ``R -> Frac(R)``.

    This is the explicit scalar-extension path for a nondegenerate but
    non-unimodular metric.  The returned isomorphism lives over the fraction
    field; it is never reported as an integral Hodge star on ``metric``.
    """

    _require_finite_free(metric)
    if not metric.is_nondegenerate():
        raise ValueError("fraction-field Hodge star requires a nondegenerate metric")
    ring = metric.base_ring()
    ring_map = ring.fraction_field_map()
    fraction_field = ring_map.codomain()
    if fraction_field is ring:
        return metric.hodge_star(volume, degree)
    changed_metric = metric.base_change(ring_map)
    volume_scalar, _inverse_volume_scalar = _volume_scalars(metric, volume)
    changed_volume = changed_metric.framing_volume_trivialization(
        unit=_engine_ring(fraction_field)(volume_scalar),
    )
    return changed_metric.hodge_star(changed_volume, degree)
