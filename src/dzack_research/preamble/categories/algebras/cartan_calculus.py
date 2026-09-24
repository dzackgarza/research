r"""Cartan calculus on represented affine algebraic de Rham algebras.

No new object is introduced here.  Vector fields are exactly derivations
``Der_R(A,A)`` (with ``A`` read as its rank-one ``A``-module), while
contractions and Lie derivatives are actual graded derivations of the existing
de Rham DGA.
"""

from dzack_research.preamble.categories.algebras.derivations import (
    Derivation,
    GradedDerivation,
)
def _vector_field_scalar(vector_field, element):
    r"""Read the value of a vector field as the underlying scalar of ``A``."""
    target = vector_field.codomain()
    labels = target.module_generating_set()
    if int(labels.cardinality()) != 1:
        raise TypeError(
            f"the vector field {vector_field} must take values in the algebra A itself, a module generated "
            f"by one element, but {target} has {labels.cardinality()} generators"
        )
    label = labels[0]
    coefficients = target.framing_coefficients(vector_field(element))
    return vector_field.domain()(coefficients.get(label, target.base_ring().zero()))


def _lie_bracket(left, right):
    r"""Return the commutator ``[left,right]`` of two vector fields."""
    if not isinstance(left, Derivation) or not isinstance(right, Derivation):
        raise TypeError(
            f"the Lie bracket [X, Y] is defined on vector fields, but got {left!r} and {right!r}"
        )
    if left.parent() is not right.parent():
        raise ValueError(
            f"the Lie bracket [X, Y] needs vector fields on one algebra, but {left} lies in {left.parent()} "
            f"and {right} lies in {right.parent()}"
        )
    algebra = left.domain()
    vector_fields = algebra.vector_fields()
    if left.parent() is not vector_fields:
        raise TypeError(
            f"the Lie bracket [X, Y] needs derivations A -> A, but {left} is not a vector field on {algebra}"
        )
    return vector_fields(
        {
            label: left(_vector_field_scalar(right, algebra.algebra_generator(label)))
            - right(_vector_field_scalar(left, algebra.algebra_generator(label)))
            for label in vector_fields.generator_labels()
        }
    )


def _graded_commutator(left, right):
    r"""Return the graded commutator of endo-derivations.

    For homogeneous derivations of shifts ``p`` and ``q`` this is
    ``D E - (-1)^(pq) E D`` and has shift ``p+q``.
    """
    if not isinstance(left, GradedDerivation) or not isinstance(right, GradedDerivation):
        raise TypeError(
            f"the graded commutator needs two graded derivations, but got {left!r} and {right!r}"
        )
    if left.algebra() is not right.algebra():
        raise ValueError(
            f"the graded commutator needs derivations of one graded algebra, but {left} is on "
            f"{left.algebra()} and {right} is on {right.algebra()}"
        )
    algebra = left.algebra()
    if left.target() is not algebra or right.target() is not algebra:
        raise TypeError(
            f"the graded commutator needs derivations A -> A of {algebra}, but {left} or {right} takes "
            "values elsewhere"
        )
    parity = (left.degree_shift() * right.degree_shift()) % 2

    def commutator(element):
        result = left(right(element))
        second = right(left(element))
        return result + second if parity else result - second

    return algebra.graded_derivations(
        algebra,
        shift=left.degree_shift() + right.degree_shift(),
    )._from_derived_elementwise(commutator, left, right)


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


def _interior_product(vector_field):
    r"""Return contraction ``i_X`` as a degree ``-1`` derivation of ``DR(A)``."""
    if not isinstance(vector_field, Derivation):
        raise TypeError(
            f"the contraction i_X needs a vector field X, but {vector_field!r} is not one"
        )
    algebra = vector_field.domain()
    if vector_field.parent() is not algebra.vector_fields():
        raise TypeError(
            f"the contraction i_X needs a derivation X: A -> A with A = {algebra}, but {vector_field} "
            "takes values elsewhere"
        )


    de_rham = algebra.de_rham_algebra()
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
            for label, coefficient in source_piece.framing_coefficients(component).items():
                word = _exterior_word(label, degree)
                for position, differential_label in enumerate(word):
                    if (
                        not isinstance(differential_label, tuple)
                        or len(differential_label) != 2
                        or differential_label[0] != "d"
                    ):
                        raise ValueError(
                            f"the basis element {label} of the de Rham algebra is not a product of Kahler differentials "
                            f"da: its factor {differential_label} is not of the form da"
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
                result += exterior.from_component(degree - 1, target_component)
        return result

    def contraction(element):
        return de_rham.from_realization(contract_extension(de_rham.realize(element)))

    return de_rham.graded_derivations(
        de_rham, shift=-1
    )._from_constructed_elementwise(contraction)


def _lie_derivative(vector_field):
    r"""Return ``L_X = [d,i_X]`` as a degree-zero derivation of ``DR(A)``."""
    contraction = vector_field.interior_product()
    return contraction.algebra().differential().graded_commutator(contraction)
