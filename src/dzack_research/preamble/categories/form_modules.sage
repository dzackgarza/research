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

from sage.groups.additive_abelian.qmodnz import QmodnZ
from sage.matrix.matrix0 import Matrix
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp


class FormModuleElement(Element):
    r"""An element of a form module, held by its coordinates in the generating set.

    The underlying module decides what the coordinates mean -- for a cokernel it
    reduces them to a canonical representative -- and the form module adds the
    pairing, which is why the element's parent is the form module and not the
    module underneath it.
    """

    def __init__(self, parent: Any, x: Any) -> None:
        Element.__init__(self, parent)
        self._underlying = parent.module()(x)

    def underlying(self) -> Any:
        r"""Return this element of the module the form is carried on."""
        return self._underlying

    def coordinates(self) -> Any:
        r"""Return the coordinates in the generating set the Gram matrix uses."""
        lift = getattr(self._underlying, "lift", None)
        return vector(lift() if lift is not None else self._underlying)

    def lift(self) -> Any:
        r"""Return the canonical representative in the generating set.

        The same vector :meth:`coordinates` returns, under the name Sage's
        quotient elements use for it.
        """
        return self.coordinates()

    def b(self, other: "FormModuleElement") -> Any:
        r"""Return the pairing, read in the value module."""
        parent = self.parent()
        # FormModule's stored Gram, not whatever a category reads off it: a
        # quadratic module's ``gram_matrix`` is assembled *from* q and b, so
        # going through it here would be circular.
        pairing = (
            self.coordinates() * FormModule.gram_matrix(parent) * other.coordinates()
        )
        return parent.value_module()(pairing)

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, FormModuleElement):
            return self.b(other)
        return self.parent()(other * self._underlying)

    def _add_(self, other: Any) -> "FormModuleElement":
        return self.parent()(self._underlying + other._underlying)

    def _sub_(self, other: Any) -> "FormModuleElement":
        return self.parent()(self._underlying - other._underlying)

    def _neg_(self) -> "FormModuleElement":
        return self.parent()(-self._underlying)

    def _lmul_(self, factor: Any) -> "FormModuleElement":
        return self.parent()(factor * self._underlying)

    _rmul_ = _lmul_

    def __truediv__(self, divisor: Any) -> "FormModuleElement":
        r"""Return $x/n$, which exists when the coordinates stay integral."""
        quotient = self.coordinates() / divisor
        assert all(entry in ZZ for entry in quotient), (
            f"{divisor} does not divide {self.coordinates()} in this module"
        )
        return self.parent()(quotient)

    def _richcmp_(self, other: Any, op: int) -> bool:
        return richcmp(self._underlying, other._underlying, op)

    def __hash__(self) -> int:
        return hash(self._underlying)

    def order(self) -> Any:
        r"""Return the order of this element in the underlying module."""
        return self._underlying.order()

    def _repr_(self) -> str:
        return repr(self._underlying)


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
        if not hasattr(gram_matrix, "subdivisions"):
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
        r"""Return the rank of the underlying module, when it has one.

        A cokernel is torsion and has none; its size is :meth:`cardinality`.
        """
        return self._module.rank()

    Element = FormModuleElement

    def _element_constructor_(self, x: Any) -> FormModuleElement:
        if isinstance(x, FormModuleElement):
            x = x.underlying()
        return self.element_class(self, x)

    def __iter__(self):
        for element in self._module:
            yield self(element)

    def annihilator(self) -> Any:
        return self._module.annihilator()

    def smith_form_gens(self) -> tuple:
        return tuple(self(g) for g in self._module.smith_form_gens())

    def projection(self) -> "FormProjection":
        r"""Return $\pi: B\to A$, sending each generator to its class."""
        return FormProjection(self)

    def quotient_map(self) -> "FormProjection":
        return self.projection()

    def relation_matrix(self) -> Matrix:
        return self._module.relation_matrix()

    def invariants(self) -> tuple:
        r"""Return the invariant factors of the underlying module."""
        return tuple(self._module.invariants())

    def cardinality(self) -> Any:
        return self._module.cardinality()

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
        expected = domain.gram_matrix()
        target = domain.value_module()
        # Where the entries are compared is not uniform.  For a form valued in a
        # quotient the Gram matrix is only a representative, so the identity
        # M G_B M^T = G_A holds in the value module rather than on the nose --
        # and for a quadratic form the diagonal is q, valued in Q/2Z, while the
        # off-diagonal is the polarization, valued in Q/Z.  Comparing the whole
        # matrix in one of them would reject honest morphisms.
        polar = QmodnZ(1) if hasattr(target, "n") else target
        for i in range(expected.nrows()):
            for j in range(expected.ncols()):
                where = target if i == j else polar
                assert where(transported[i, j]) == where(expected[i, j]), (
                    "not a morphism of form modules: at "
                    f"({i}, {j}) M G_B M^T is {transported[i, j]}, not "
                    f"{expected[i, j]} in {where}"
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


class FormProjection:
    r"""$\pi: B\to\operatorname{coker} f$, the map that comes with the quotient."""

    def __init__(self, target: FormModule) -> None:
        self._target = target

    def domain(self) -> Any:
        return self._target.module().morphism().codomain()

    def codomain(self) -> FormModule:
        return self._target

    def __call__(self, x: Any) -> FormModuleElement:
        return self._target(x)

    def __repr__(self) -> str:
        return f"Projection onto {self._target}"
