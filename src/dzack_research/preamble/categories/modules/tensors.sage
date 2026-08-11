r"""Type-$(p,q)$ tensors on a module, and a constructor for them.

A tensor of type $(p,q)$ on $M$ is an element of $M^{\otimes p}\otimes
(M^*)^{\otimes q}$ -- a graded piece of $T(M)\otimes_R T(M^*)$, which is an
$R$-algebra for any commutative $R$ and is bigraded by $(p,q)$ without further
hypothesis.  Identifying that piece with multilinear maps $ (M^*)^p\times M^q
\to R$ is the part that wants $M$ finitely generated projective, and the
components below are read in a framing, so that is where these live.

Evaluation is contraction and is partial: a type-$(p,q)$ tensor fed $k\le q$
elements is a type-$(p,q-k)$ tensor, and only one with no slots left is a
scalar.  A vector is type $(1,0)$ and a functional type $(0,1)$, so nothing
has to be handed in that is not already a tensor.

A Gram matrix is the components of a type-$(0,2)$ tensor in a framing: twice
covariant, because it eats two vectors.  A multiplication table $m:A\otimes_R
A\to A$ is type $(1,2)$ -- once up, twice down.

The constructor mirrors ``matrix``: ``tensor(R, [[...], [...]])`` reads its
shape off the nesting, so a Gram matrix is written exactly as a matrix is.
Mixed valence is stated rather than guessed, since nesting cannot say which
slots are up.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage_lattice_category_spike.lexicon import Element, Module

from itertools import product as _index_product
from typing import Self

from sage.structure.parent import Parent
from sage.structure.element import ModuleElement
from sage.structure.unique_representation import UniqueRepresentation


def _nesting_shape(components) -> tuple:
    r"""Return the shape of a nested list, checking it is rectangular."""
    if not isinstance(components, (list, tuple)):
        return ()
    assert components, "a tensor's components cannot be an empty list"
    inner = {_nesting_shape(entry) for entry in components}
    assert len(inner) == 1, (
        f"the components are ragged: {sorted(inner)} at one level"
    )
    return (len(components),) + inner.pop()


def _entries_by_index(components, shape: tuple) -> dict:
    r"""Return ``{multi-index: entry}`` for a rectangular nesting."""
    if not shape:
        return {(): components}
    entries = {}
    for position, block in enumerate(components):
        for index, entry in _entries_by_index(block, shape[1:]).items():
            entries[(position,) + index] = entry
    return entries


class Tensor(UniqueRepresentation, Parent):
    r"""The module of type-$(p,q)$ tensors on $M$."""

    def __init__(self, module: "Module", valence: tuple) -> None:
        contravariant, covariant = valence
        assert contravariant >= 0 and covariant >= 0, (
            f"a tensor type is a pair of counts, got {valence}"
        )
        self._module = module
        self._valence = (contravariant, covariant)
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        Parent.__init__(self, base=module.base_ring(), category=Modules(module.base_ring()))

    def module(self) -> "Module":
        r"""Return $M$, the module the tensors are on."""
        return self._module

    def valence(self) -> tuple:
        r"""Return $(p,q)$: how many slots are up, and how many down."""
        return self._valence

    def degree(self) -> int:
        r"""Return $p+q$, the number of slots."""
        return sum(self._valence)

    def base_ring(self) -> "Ring":
        return self.base()

    def _ring_morphism_defining_module_action(self: Self) -> "Morphism":
        r"""Return $\rho$, scaling every component."""
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
        from sage.categories.homset import Hom
        from sage.categories.morphism import SetMorphism
        from sage.categories.rings import Rings

        endomorphisms = module_homset(self, self)
        return SetMorphism(
            Hom(self.base_ring(), endomorphisms, Rings()),
            lambda scalar: SetMorphism(endomorphisms, lambda t: scalar * t),
        )

    def _repr_(self) -> str:
        contravariant, covariant = self._valence
        return f"Type-({contravariant},{covariant}) tensors on {self._module}"

    def _element_constructor_(self, entries: dict) -> "TensorElement":
        return self.element_class(self, entries)

    def zero(self) -> "TensorElement":
        return self({})


class TensorElement(ModuleElement):
    r"""A tensor, held by its components in the module's framing."""

    def __init__(self, parent: Tensor, entries: dict) -> None:
        ModuleElement.__init__(self, parent)
        self._entries = dict(entries)

    def valence(self) -> tuple:
        return self.parent().valence()

    def __getitem__(self, index):
        r"""Return the component at a multi-index, zero where unrecorded."""
        index = index if isinstance(index, tuple) else (index,)
        assert len(index) == self.parent().degree(), (
            f"a type-{self.parent().valence()} tensor takes "
            f"{self.parent().degree()} indices, got {len(index)}"
        )
        return self._entries.get(index, self.parent().base_ring().zero())

    def components(self) -> dict:
        r"""Return the components, keyed by multi-index."""
        return dict(self._entries)

    def __eq__(self, other: "Element") -> bool:
        return (
            isinstance(other, TensorElement)
            and other.parent() is self.parent()
            and other._entries == self._entries
        )

    def __hash__(self) -> int:
        return hash((self.parent(), tuple(sorted(self._entries.items()))))

    def _scaled(self, scalar) -> "TensorElement":
        return self.parent()(
            {index: scalar * entry for index, entry in self._entries.items()},
        )

    def _lmul_(self, scalar) -> "TensorElement":
        return self._scaled(scalar)

    def _rmul_(self, scalar) -> "TensorElement":
        return self._scaled(scalar)

    def _add_(self, other: "TensorElement") -> "TensorElement":
        assert other.parent() is self.parent(), (
            "tensors add within one type on one module"
        )
        entries = dict(self._entries)
        for index, entry in other._entries.items():
            entries[index] = entries.get(index, self.parent().base_ring().zero()) + entry
        return self.parent()(entries)

    def _scalar_or_tensor(self, valence: tuple, entries: dict):
        r"""Return the scalar when no slots are left, else the tensor."""
        if sum(valence) == 0:
            return entries.get((), self.parent().base_ring().zero())
        return Tensor(self.parent().module(), valence)(
            {index: entry for index, entry in entries.items() if entry != 0},
        )

    def __call__(self, *arguments):
        r"""Feed elements into the covariant slots, left to right.

        Partial: a type-$(p,q)$ tensor given $k\le q$ elements is a
        type-$(p,q-k)$ tensor, and only a tensor with no slots left is a
        scalar.  So a multiplication table eats two elements and returns the
        product -- a vector, which is a type-$(1,0)$ tensor -- rather than
        refusing because it has an upper slot.

        Covectors are not a separate kind of thing to be handed in: a
        functional is a type-$(0,1)$ tensor, so pairing against one is
        :meth:`contract`.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector

        contravariant, covariant = self.valence()
        assert len(arguments) <= covariant, (
            f"a type-{self.valence()} tensor has {covariant} covariant slots, "
            f"got {len(arguments)} arguments"
        )
        coordinates = [_coordinate_vector(argument) for argument in arguments]
        filled = len(coordinates)
        entries: dict = {}
        for index, entry in self._entries.items():
            eaten = index[contravariant : contravariant + filled]
            weight = self.parent().base_ring().one()
            for slot, position in enumerate(eaten):
                weight = weight * coordinates[slot][position]
            if weight == 0:
                continue
            remaining = index[:contravariant] + index[contravariant + filled :]
            entries[remaining] = entries.get(
                remaining, self.parent().base_ring().zero()
            ) + entry * weight
        return self._scalar_or_tensor((contravariant, covariant - filled), entries)

    def contract(self, other: "TensorElement", slot: int = 0, other_slot: int = 0):
        r"""Contract an upper slot of this tensor with a lower slot of ``other``.

        The basic operation of the calculus: sum over the shared index.  The
        result is type $(p-1+p',\,q+q'-1)$, and a full contraction leaves a
        scalar.  Evaluating on a vector is the case where ``other`` is that
        vector as a type-$(1,0)$ tensor; pairing with a functional is the case
        where it is a type-$(0,1)$ one.
        """
        contravariant, covariant = self.valence()
        other_contravariant, other_covariant = other.valence()
        assert contravariant > slot >= 0, (
            f"slot {slot} is not an upper index of a type-{self.valence()} tensor"
        )
        assert other_covariant > other_slot >= 0, (
            f"slot {other_slot} is not a lower index of a "
            f"type-{other.valence()} tensor"
        )
        assert other.parent().module() is self.parent().module(), (
            "contraction pairs tensors on one module"
        )
        entries: dict = {}
        for index, entry in self._entries.items():
            for other_index, other_entry in other.components().items():
                if index[slot] != other_index[other_contravariant + other_slot]:
                    continue
                left = index[:slot] + index[slot + 1 :]
                right = (
                    other_index[: other_contravariant + other_slot]
                    + other_index[other_contravariant + other_slot + 1 :]
                )
                # Upper indices first, then lower, so the pieces interleave by
                # valence rather than by which tensor they came from.
                merged = (
                    left[: contravariant - 1]
                    + right[:other_contravariant]
                    + left[contravariant - 1 :]
                    + right[other_contravariant:]
                )
                entries[merged] = entries.get(
                    merged, self.parent().base_ring().zero()
                ) + entry * other_entry
        return self._scalar_or_tensor(
            (contravariant - 1 + other_contravariant, covariant + other_covariant - 1),
            entries,
        )

    def trace(self, slot: int = 0, other_slot: int = 0):
        r"""Contract one of this tensor's own upper slots against a lower one."""
        contravariant, covariant = self.valence()
        assert contravariant > slot >= 0 and covariant > other_slot >= 0, (
            f"a type-{self.valence()} tensor has no such pair of slots"
        )
        entries: dict = {}
        for index, entry in self._entries.items():
            if index[slot] != index[contravariant + other_slot]:
                continue
            remaining = tuple(
                position
                for place, position in enumerate(index)
                if place not in (slot, contravariant + other_slot)
            )
            entries[remaining] = entries.get(
                remaining, self.parent().base_ring().zero()
            ) + entry
        return self._scalar_or_tensor((contravariant - 1, covariant - 1), entries)

    def raise_index(self, formed_module: "Module", slot: int = 0) -> "TensorElement":
        r"""Raise one lower index with the inverse Gram matrix."""
        from sage.matrix.constructor import matrix

        contravariant, covariant = self.valence()
        assert covariant > slot >= 0, (
            f"slot {slot} is not a lower index of a type-{self.valence()} tensor"
        )
        assert formed_module.forget_form() is self.parent().module(), (
            "the form and tensor must use the same module"
        )
        inverse = matrix(formed_module.gram_matrix()).inverse()
        ring = self.parent().base_ring()
        assert all(entry in ring for entry in inverse.list()), (
            "raising an index over this ring requires a unimodular form"
        )
        rank = inverse.nrows()
        entries = {}
        for index, entry in self._entries.items():
            contracted = index[contravariant + slot]
            remaining_lower = (
                index[contravariant:contravariant + slot]
                + index[contravariant + slot + 1:]
            )
            for raised in range(rank):
                output = index[:contravariant] + (raised,) + remaining_lower
                entries[output] = entries.get(output, ring.zero()) + (
                    ring(inverse[raised, contracted]) * entry
                )
        return Tensor(self.parent().module(), (contravariant + 1, covariant - 1))(
            {index: entry for index, entry in entries.items() if entry != 0}
        )

    def lower_index(self, formed_module: "Module", slot: int = 0) -> "TensorElement":
        r"""Lower one upper index with the Gram matrix."""
        from sage.matrix.constructor import matrix

        contravariant, covariant = self.valence()
        assert contravariant > slot >= 0, (
            f"slot {slot} is not an upper index of a type-{self.valence()} tensor"
        )
        assert formed_module.forget_form() is self.parent().module(), (
            "the form and tensor must use the same module"
        )
        gram = matrix(formed_module.gram_matrix())
        ring = self.parent().base_ring()
        rank = gram.nrows()
        entries = {}
        for index, entry in self._entries.items():
            contracted = index[slot]
            remaining_upper = index[:slot] + index[slot + 1:contravariant]
            lower = index[contravariant:]
            for lowered in range(rank):
                output = remaining_upper + lower + (lowered,)
                entries[output] = entries.get(output, ring.zero()) + (
                    ring(gram[lowered, contracted]) * entry
                )
        return Tensor(self.parent().module(), (contravariant - 1, covariant + 1))(
            {index: entry for index, entry in entries.items() if entry != 0}
        )

    def __repr__(self) -> str:
        contravariant, covariant = self.valence()
        return (
            f"type-({contravariant},{covariant}) tensor on "
            f"{self.parent().module()}"
        )


Tensor.Element = TensorElement


def tensor(base_ring: "Ring", components, valence: tuple = None, module: "Module" = None):
    r"""Return the tensor with these components, as ``matrix`` returns a matrix.

    ``tensor(R, [[-2, 1], [1, -2]])`` is a type-$(0,2)$ tensor: the nesting
    says how many slots there are, and they are covariant unless told
    otherwise, because that is what a form is.  Mixed valence is stated --
    ``valence=(1, 2)`` for a multiplication table -- since a nested list
    cannot say which slots are up.
    """
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreeModuleOn
    from sage_lattice_category_spike.objects.sets import Sets as _OwnedSets

    shape = _nesting_shape(components)
    assert shape, "a tensor is built from a nested list of components"
    assert len(set(shape)) == 1, (
        f"the slots of a tensor on one module have one size, got shape {shape}"
    )
    if valence is None:
        valence = (0, len(shape))
    assert sum(valence) == len(shape), (
        f"a type-{valence} tensor has {sum(valence)} slots but the components "
        f"are nested {len(shape)} deep"
    )
    if module is None:
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.sets.sets import Sets

        module = FreeModuleOn(base_ring, Sets.Δ[shape[0] - 1])
    entries = {
        index: base_ring(entry)
        for index, entry in _entries_by_index(components, shape).items()
        if entry != 0
    }
    return Tensor(module, tuple(valence))(entries)
