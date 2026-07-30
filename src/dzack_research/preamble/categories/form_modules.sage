r"""Modules carrying a form.

The node under lattices, rational lattices, and torsion bilinear and quadratic
forms.  All four are the same shape -- a module with a generating set, a Gram
matrix in that generating set, and a value module the form lands in -- and they
differ only in the first and third entries:

===========================  ==================  ==============
object                       module              value module
===========================  ==================  ==============
lattice                      $\mathbb Z^n$       $\mathbb Z$
rational lattice, $L^\vee$   $\mathbb Z^n$       $\mathbb Q$
torsion bilinear form        $\operatorname{coker} c$  $\mathbb Q/\mathbb Z$
torsion quadratic form       $\operatorname{coker} c$  $\mathbb Q/2\mathbb Z$
===========================  ==================  ==============

So integrality is not a property of the Gram entries but a fact about where the
form lands, and $L^\vee$ and $A_L$ -- same generators, same entries $G^{-1}$ --
are distinguished only by their value modules.  Taking a cokernel changes the
module; reducing changes the value module; $A_L$ is both applied to $L^\vee$.

The module is passed rather than inferred: a Gram matrix determines a *free*
module of its size, but a torsion form's module is not free, and covering both
is the point.
"""

from typing import Any

from sage.matrix.matrix0 import Matrix
from sage.structure.parent import Parent


class FormModule(Parent):
    r"""A module with a generating set, a Gram matrix, and a value module.

    Composition, not inheritance: this has an underlying module rather than
    being a submodule of, or an ambient for, anything.  Sage's lattice classes
    are realizations -- ``FreeQuadraticModule_submodule_with_basis_pid`` is a
    submodule of a rational ambient with a chosen basis -- and subclassing one
    inherits an embedding this object does not have.  The module interface below
    is delegated, so the realization stays a detail of the module rather than
    part of what a form module is.
    """

    def __init__(self, module: Any, value_module: Any, gram_matrix: Any) -> None:
        gram_matrix = matrix(gram_matrix)
        assert gram_matrix.is_symmetric(), "a Gram matrix must be symmetric"
        assert gram_matrix.nrows() == len(tuple(module.gens())), (
            f"the Gram matrix is {gram_matrix.nrows()}x{gram_matrix.ncols()} but "
            f"the module has {len(tuple(module.gens()))} generators"
        )
        assert all(entry in value_module for entry in gram_matrix.list()), (
            f"the form takes its values in {value_module}, but the Gram matrix "
            "has entries outside it"
        )
        Parent.__init__(self, base=module.base_ring())
        self._module = module
        self._value_module = value_module
        self._gram_matrix = gram_matrix

    # ---- the form ----

    def module(self) -> Any:
        r"""Return the module underlying this form."""
        return self._module

    def value_module(self) -> Any:
        r"""Return where the form takes its values."""
        return self._value_module

    def gram_matrix(self) -> Matrix:
        r"""Return the form in this object's generating set."""
        return self._gram_matrix

    # ---- delegated to the module ----

    def gens(self) -> tuple:
        r"""Return the generating set the Gram matrix is written in."""
        return tuple(self(generator) for generator in self._module.gens())

    def ngens(self) -> int:
        return len(tuple(self._module.gens()))

    def rank(self) -> Any:
        return self._module.rank()

    def _element_constructor_(self, x: Any) -> Any:
        return self._module(x)

    def _repr_(self) -> str:
        return (
            f"Form module of rank {self.rank()} over {self.base_ring()} "
            f"with values in {self._value_module}"
        )


class FormMorphism:
    r"""A form-preserving map of form modules, held by its matrix.

    Owned rather than a Sage morphism, because the objects are no longer Sage
    modules: a form module has an underlying module and a Gram matrix, and a map
    of them is a matrix in the two generating sets satisfying
    $MG_BM^{\mathsf T}=G_A$.  That identity is the whole content, so it is
    checked here rather than assumed by whoever built the matrix.
    """

    def __init__(self, domain: Any, codomain: Any, matrix_: Any) -> None:
        matrix_ = matrix(matrix_)
        assert matrix_.nrows() == domain.ngens(), (
            f"a map out of {domain.ngens()} generators needs that many rows, "
            f"got {matrix_.nrows()}"
        )
        assert matrix_.ncols() == codomain.ngens(), (
            f"a map into {codomain.ngens()} generators needs that many columns, "
            f"got {matrix_.ncols()}"
        )
        transported = matrix_ * codomain.gram_matrix() * matrix_.transpose()
        assert transported == domain.gram_matrix(), (
            "not a morphism of form modules: M G_B M^T is "
            f"{transported.list()}, not {domain.gram_matrix().list()}"
        )
        self._domain = domain
        self._codomain = codomain
        self._matrix = matrix_

    def domain(self) -> Any:
        return self._domain

    def codomain(self) -> Any:
        return self._codomain

    def matrix(self) -> Matrix:
        return self._matrix

    def __call__(self, x: Any) -> Any:
        return self._codomain(vector(x) * self._matrix)

    def __repr__(self) -> str:
        return (
            f"Form morphism from {self._domain.ngens()} to "
            f"{self._codomain.ngens()} generators"
        )


def free_form_module(gram_matrix: Any, value_module: Any) -> FormModule:
    r"""Return the form module free on as many generators as ``gram_matrix`` has."""
    from sage.modules.free_module import FreeModule

    gram_matrix = matrix(gram_matrix)
    return FormModule(
        FreeModule(ZZ, gram_matrix.nrows()), value_module, gram_matrix
    )


def correlation_of(gram_matrix: Any) -> FormMorphism:
    r"""Return $c: L\to L^\vee$ for a lattice with this Gram matrix.

    $L$ is free with Gram $G$ and $\mathbb Z$-valued form; $L^\vee$ is free on
    the dual generators with Gram $G^{-1}$ and $\mathbb Q$-valued form; and $c$
    has matrix $G$, since $c(e_i)=\sum_j G_{ij}e_j^\vee$.  Form preservation is
    then $G\,G^{-1}G^{\mathsf T}=G$, which is what makes $c$ a morphism here.
    """
    gram_matrix = matrix(ZZ, gram_matrix)
    source = free_form_module(gram_matrix, ZZ)
    dual = free_form_module(gram_matrix.inverse(), QQ)
    return FormMorphism(source, dual, gram_matrix)
