r"""Type-$(p,q)$ tensors on a module, and a constructor for them.

A tensor of type $(p,q)$ on $M$ is an element of $M^{\otimes p}\otimes
(M^*)^{\otimes q}$ -- a graded piece of $T(M)\otimes_R T(M^*)$, which is an
$R$-algebra for any commutative $R$ and is bigraded by $(p,q)$ without further
hypothesis.  Identifying that piece with multilinear maps $ (M^*)^p\times M^q
\to R$ is the part that wants $M$ finitely generated projective, and the
evaluation below is only offered there.

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


class TensorElement:
    r"""A tensor, held by its components in the module's framing."""

    def __init__(self, parent: Tensor, entries: dict) -> None:
        self._parent = parent
        self._entries = dict(entries)

    def parent(self) -> Tensor:
        return self._parent

    def valence(self) -> tuple:
        return self._parent.valence()

    def __getitem__(self, index):
        r"""Return the component at a multi-index, zero where unrecorded."""
        index = index if isinstance(index, tuple) else (index,)
        assert len(index) == self._parent.degree(), (
            f"a type-{self._parent.valence()} tensor takes "
            f"{self._parent.degree()} indices, got {len(index)}"
        )
        return self._entries.get(index, self._parent.base_ring().zero())

    def components(self) -> dict:
        r"""Return the components, keyed by multi-index."""
        return dict(self._entries)

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, TensorElement)
            and other._parent is self._parent
            and other._entries == self._entries
        )

    def __hash__(self) -> int:
        return hash((self._parent, tuple(sorted(self._entries.items()))))

    def _scaled(self, scalar) -> "TensorElement":
        return TensorElement(
            self._parent,
            {index: scalar * entry for index, entry in self._entries.items()},
        )

    def __mul__(self, scalar) -> "TensorElement":
        return self._scaled(scalar)

    __rmul__ = __mul__

    def __add__(self, other: "TensorElement") -> "TensorElement":
        assert other.parent() is self._parent, (
            "tensors add within one type on one module"
        )
        entries = dict(self._entries)
        for index, entry in other._entries.items():
            entries[index] = entries.get(index, self._parent.base_ring().zero()) + entry
        return TensorElement(self._parent, entries)

    def __call__(self, *arguments) -> "Element":
        r"""Evaluate on module elements, one per covariant slot.

        Offered for the purely covariant case, which is what a form is: the
        contraction reads coordinates in the framing, so it is available
        exactly where the module has them.
        """
        # Local: a module-level import here would close a cycle; by call time this module is built.
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import _coordinate_vector

        contravariant, covariant = self.valence()
        assert contravariant == 0, (
            "evaluation is defined here for a purely covariant tensor; a "
            f"type-{self.valence()} tensor also eats functionals"
        )
        assert len(arguments) == covariant, (
            f"a type-(0,{covariant}) tensor eats {covariant} elements, "
            f"got {len(arguments)}"
        )
        coordinates = [_coordinate_vector(argument) for argument in arguments]
        total = self._parent.base_ring().zero()
        for index, entry in self._entries.items():
            weight = self._parent.base_ring().one()
            for slot, position in enumerate(index):
                weight = weight * coordinates[slot][position]
            total = total + entry * weight
        return total

    def __repr__(self) -> str:
        contravariant, covariant = self.valence()
        return (
            f"type-({contravariant},{covariant}) tensor on "
            f"{self._parent.module()}"
        )


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
    return TensorElement(Tensor(module, tuple(valence)), entries)
