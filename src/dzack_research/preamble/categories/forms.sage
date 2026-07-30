r"""Forms as morphisms.

A bilinear form is a morphism out of the tensor square,
$b: M\otimes_R M\to W$, which needs nothing of $W$ but that it be a module --
so this covers every value module, $\mathbb Q/\mathbb Z$ included.

A quadratic form is an element $q\in S^2(M^{\vee_W})$, $M^{\vee_W}=\operatorname
{Hom}_R(M,W)$ (Auel, *Quadratic forms over local rings*, for $W=R$).  That
description multiplies two functionals, so it needs $W\otimes_R W\to W$ -- a
ring.  It therefore covers the free rows, where $W$ is $\mathbb Z$ or
$\mathbb Q$, and *not* the torsion rows, where $W$ is $\mathbb Q/\mathbb Z$ or
$\mathbb Q/2\mathbb Z$ and no such multiplication exists.  For those the
domain-side description $\operatorname{Hom}(\Gamma^2 M, W)$ is the one that
survives, and it is not built here.
"""

from typing import Any

from sage.categories.rings import Rings
from sage.matrix.matrix0 import Matrix


def tensor_square_relations(relations: Matrix) -> Matrix:
    r"""Return the relations of $A\otimes A$ for $A=\operatorname{coker}$ of ``relations``.

    Right exactness of $\otimes$ applied twice: $A\otimes A$ is the cokernel of
    $f\otimes 1$ and $1\otimes f$ together, so its relations are those two
    families stacked.  The point of expressing it this way is that the result is
    again a cokernel of a morphism of free modules, so the owned quotient layer
    covers it with nothing new.
    """
    relations = matrix(ZZ, relations)
    rows, columns = relations.nrows(), relations.ncols()
    identity = identity_matrix(ZZ, columns)
    return relations.tensor_product(identity).stack(
        identity.tensor_product(relations)
    )


class BilinearForm:
    r"""$b: M\otimes_R M\to W$, held as the morphism it is.

    The Gram matrix is this morphism's values on the generators of $M\otimes M$,
    reshaped; it is a reading of the morphism rather than the data.
    """

    def __init__(self, module: Any, value_module: Any, gram_matrix: Matrix) -> None:
        gram_matrix = matrix(gram_matrix)
        size = len(tuple(module.gens()))
        assert gram_matrix.is_symmetric(), "a bilinear form's Gram matrix is symmetric"
        assert gram_matrix.nrows() == size, (
            f"the Gram matrix is {gram_matrix.nrows()}x{gram_matrix.ncols()} but the "
            f"module has {size} generators"
        )
        assert all(entry in value_module for entry in gram_matrix.list()), (
            f"b takes its values in {value_module}"
        )
        self._module = module
        self._value_module = value_module
        self._gram_matrix = gram_matrix

    def module(self) -> Any:
        return self._module

    def value_module(self) -> Any:
        return self._value_module

    def gram_matrix(self) -> Matrix:
        return self._gram_matrix

    def descends_along(self, relations: Matrix) -> bool:
        r"""Return whether $b$ factors through the cokernel of ``relations``.

        The morphism out of $M\otimes M$ descends when it kills the relations,
        which is the same statement as the pairings of the relations with the
        generators lying in the subgroup $W$ is a quotient by.
        """
        transported = matrix(relations) * self._gram_matrix
        return all(entry in ZZ for entry in transported.list())

    def __repr__(self) -> str:
        return (
            f"Bilinear form on {len(tuple(self._module.gens()))} generators "
            f"with values in {self._value_module}"
        )


class QuadraticForm:
    r"""$q\in S^2(M^{\vee_W})$, held by its coefficients $a_{ij}$, $i\le j$.

    So $q(x)=\sum_{i\le j}a_{ij}x_ix_j$, the classical shape, and the polar form
    $b_q(x,y)=q(x+y)-q(x)-q(y)$ has Gram $2a_{ii}$ on the diagonal and $a_{ij}$
    off it.  That is where evenness comes from: a symmetric Gram matrix is the
    polar form of a $q$ over $W$ exactly when its diagonal is divisible by 2 in
    $W$, so "even" is the condition for $q$ to exist rather than a separate
    axiom.
    """

    def __init__(self, module: Any, value_module: Any, coefficients: dict) -> None:
        assert value_module in Rings(), (
            f"q lives in S^2(M^v) which multiplies functionals, so W must be a "
            f"ring; {value_module} is not.  Use Hom(Gamma^2 M, W) for those."
        )
        self._module = module
        self._value_module = value_module
        self._coefficients = dict(coefficients)

    @classmethod
    def from_polar_form(
        cls, module: Any, value_module: Any, gram_matrix: Matrix
    ) -> "QuadraticForm":
        r"""Return the $q$ whose polar form is ``gram_matrix``, if there is one."""
        gram_matrix = matrix(gram_matrix)
        size = gram_matrix.nrows()
        halves = []
        for i in range(size):
            diagonal = gram_matrix[i, i]
            assert diagonal / 2 in value_module, (
                f"no q over {value_module} has this polar form: the diagonal entry "
                f"{diagonal} at {i} is not divisible by 2, i.e. the form is odd"
            )
            halves.append(diagonal / 2)
        coefficients = {(i, i): halves[i] for i in range(size)}
        coefficients.update(
            {(i, j): gram_matrix[i, j] for i in range(size) for j in range(i + 1, size)}
        )
        return cls(module, value_module, coefficients)

    def coefficients(self) -> dict:
        return dict(self._coefficients)

    def __call__(self, x: Any) -> Any:
        coordinates = vector(x)
        return sum(
            coefficient * coordinates[i] * coordinates[j]
            for (i, j), coefficient in self._coefficients.items()
        )

    def polar_form(self, value_module: Any = None) -> BilinearForm:
        r"""Return $b_q(x,y)=q(x+y)-q(x)-q(y)$."""
        size = len(tuple(self._module.gens()))
        gram = matrix(self._value_module, size, size)
        for (i, j), coefficient in self._coefficients.items():
            if i == j:
                gram[i, i] = 2 * coefficient
            else:
                gram[i, j] = gram[j, i] = coefficient
        return BilinearForm(self._module, value_module or self._value_module, gram)

    def __repr__(self) -> str:
        return (
            f"Quadratic form on {len(tuple(self._module.gens()))} generators "
            f"with values in {self._value_module}"
        )
