r"""Cartan calculus on represented affine algebraic de Rham algebras.

No new object is introduced here.  Vector fields are exactly derivations
``Der_R(A,A)`` (with ``A`` read as its rank-one ``A``-module), while
contractions and Lie derivatives are actual graded derivations of the existing
de Rham DGA.
"""

from dzack_research.preamble.categories.algebras.derivations import (
    Derivation,
    Derivations,
    GradedDerivation,
    GradedDerivations,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.algebras.de_rham_algebras import DeRhamAlgebra
from dzack_research.preamble.categories.modules.framed.framed_free_modules import ring_as_module


def VectorFields(algebra):
    r"""Return ``Der_R(A,A)`` as the existing derivation module."""

    return Derivations(algebra, ring_as_module(algebra))


def _vector_field_scalar(vector_field, element):
    r"""Read the value of a vector field as the underlying scalar of ``A``."""
    target = vector_field.codomain()
    labels = target.module_generating_set()
    if int(labels.cardinality()) != 1:
        raise TypeError("a vector field here takes values in the rank-one A-module A")
    label = labels[0]
    coefficients = module_coefficients(vector_field(element), target)
    return vector_field.domain()(coefficients.get(label, target.base_ring().zero()))


def LieBracket(left, right):
    r"""Return the commutator ``[left,right]`` of two vector fields."""
    if not isinstance(left, Derivation) or not isinstance(right, Derivation):
        raise TypeError("the Lie bracket here is defined on represented vector fields")
    if left.parent() is not right.parent():
        raise ValueError("the Lie bracket requires vector fields on one algebra")
    algebra = left.domain()
    vector_fields = VectorFields(algebra)
    if left.parent() is not vector_fields:
        raise TypeError("the derivations must take values in A itself")
    return vector_fields(
        {
            label: left(_vector_field_scalar(right, algebra.algebra_generator(label)))
            - right(_vector_field_scalar(left, algebra.algebra_generator(label)))
            for label in vector_fields.generator_labels()
        }
    )


def GradedCommutator(left, right):
    r"""Return the graded commutator of endo-derivations.

    For homogeneous derivations of shifts ``p`` and ``q`` this is
    ``D E - (-1)^(pq) E D`` and has shift ``p+q``.
    """
    if not isinstance(left, GradedDerivation) or not isinstance(right, GradedDerivation):
        raise TypeError("a graded commutator requires two graded derivations")
    if left.algebra() is not right.algebra():
        raise ValueError("graded commutators require one graded algebra")
    algebra = left.algebra()
    if left.target() is not algebra or right.target() is not algebra:
        raise TypeError("graded commutator composition requires endo-derivations")
    parity = (left.degree_shift() * right.degree_shift()) % 2

    def commutator(element):
        result = left(right(element))
        second = right(left(element))
        return result + second if parity else result - second

    return GradedDerivations(
        algebra,
        algebra,
        left.degree_shift() + right.degree_shift(),
    )(commutator)


def _exterior_word(label, degree):
    if degree == 0:
        return ()
    if degree == 1:
        return (label,)
    return tuple(label)


def _exterior_label(word):
    if len(word) == 0:
        return 0
    if len(word) == 1:
        return word[0]
    return tuple(word)


def InteriorProduct(vector_field):
    r"""Return contraction ``i_X`` as a degree ``-1`` derivation of ``DR(A)``."""
    if not isinstance(vector_field, Derivation):
        raise TypeError("contraction requires a represented vector field")
    algebra = vector_field.domain()
    if vector_field.parent() is not VectorFields(algebra):
        raise TypeError("contraction requires a derivation with values in A")


    de_rham = DeRhamAlgebra(algebra)
    exterior = de_rham.extension_algebra()

    def contract_extension(element):
        element = exterior(element)
        result = exterior.zero()
        for degree, component in element.homogeneous_components().items():
            if degree == 0:
                continue
            source_piece = exterior.graded_piece(degree)
            target_piece = exterior.graded_piece(degree - 1)
            target_component = target_piece.zero()
            for label, coefficient in module_coefficients(component, source_piece).items():
                word = _exterior_word(label, degree)
                for position, differential_label in enumerate(word):
                    if (
                        not isinstance(differential_label, tuple)
                        or len(differential_label) != 2
                        or differential_label[0] != "d"
                    ):
                        raise ValueError(
                            "the de Rham exterior basis is not generated by Kähler differentials"
                        )
                    scalar = _vector_field_scalar(
                        vector_field,
                        algebra.algebra_generator(differential_label[1]),
                    )
                    if not scalar:
                        continue
                    remaining = word[:position] + word[position + 1 :]
                    basis = target_piece.module_generator(_exterior_label(remaining))
                    signed = -scalar if position % 2 else scalar
                    target_component += target_piece.scalar_multiple(
                        coefficient * signed,
                        basis,
                    )
            if target_component != target_piece.zero():
                result += exterior._from_component(degree - 1, target_component)
        return result

    def contraction(element):
        return de_rham.from_realization(contract_extension(de_rham.realize(element)))

    return GradedDerivations(de_rham, de_rham, -1)(contraction)


def LieDerivative(vector_field):
    r"""Return ``L_X = [d,i_X]`` as a degree-zero derivation of ``DR(A)``."""
    contraction = InteriorProduct(vector_field)
    return GradedCommutator(contraction.algebra().differential(), contraction)


__all__ = [
    "GradedCommutator",
    "InteriorProduct",
    "LieBracket",
    "LieDerivative",
    "VectorFields",
]
