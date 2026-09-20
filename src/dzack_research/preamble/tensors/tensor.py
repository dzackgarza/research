r"""Owned tensor modules and finite coordinate tensor constructors.

The general constructor is ``tensor(R, ps, qs, data)``.  ``ps`` is the tuple
of dimensions of the contravariant indices and ``qs`` the tuple of dimensions
of the covariant indices.  Thus the component array has shape ``ps + qs``.

Every variance pattern is an element of its own tensor module over the owned
ring, so variance is carried by the object rather than inferred from storage.
A vector ``tensor(R, (n,), (), data)`` and a covector ``tensor(R, (), (n,),
data)`` are different objects with different parents, and a linear map
``tensor(R, (p,), (q,), data)`` from ``R^q`` to ``R^p`` is distinct from an
all-upper or all-lower two-index tensor.

``tensor.vector(...)``, ``tensor.covector(...)`` and ``tensor.matrix(...)``
accept owned rings and explicit component data.  They do not reproduce Sage's
matrix namespace: matrices as linear maps belong to the owned Hom objects.

Every route ends in one construction: ``TensorModule(R, ps, qs)`` is the
object of ``Modules(R)`` built by that owner's entry from
the rank vector, and a tensor is an element of it built by the module's
element constructor from its row-major components.
"""

from functools import singledispatch
from math import prod

from sage.matrix.constructor import matrix as _sage_matrix
from sage.misc.cachefunc import cached_function
from sage.misc.latex import latex
from sage.modules.free_module_element import vector as _sage_vector
from sage.rings.infinity import Infinity
from sage.structure.element import ModuleElement
from sage.structure.element import parent as element_parent
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.modules.graded_direct_sums import (
    GradedDirectSumElement,
    _FramedDirectSumOfModules,
    _direct_sum_of_modules,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FramedModules,
    MatrixSpaces,
    Modules,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    _engine_matrix as _engine_module_matrix,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _engine_element,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.sets.cardinals import Cardinalities, cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.categories.sets.set_categories import NN, Sets
from dzack_research.preamble.owned_category import _object_of
from dzack_research.static_types import ProductOfNaturalNumbers

_Rings = OwnedRings()


def index_rank_family(ranks):
    r"""Return the family \(i\mapsto\) rank of slot \(i\), for \(i\in\Delta[k-1]\)."""

    entries = tuple(cardinal(rank) for rank in ranks)
    return indexed_family(
        Sets.Δ[len(entries) - 1],
        lambda index: entries[int(index)],
        name=f"Index ranks ({', '.join(str(entry) for entry in entries)})",
    )


def _owned_object_pair(first, second):
    r"""Return two mathematical objects as an object of ``Objects x Objects``."""
    from dzack_research.preamble.categories.abstract_categories.cat import Cat
    from dzack_research.preamble.categories.abstract_categories.objects import Objects

    return Cat().product((Objects(), Objects()))(first, second)


def _tensor_richcmp(left, right, op):
    r"""Implement only the mathematical equality relation on tensors.

    Tensor spaces carry no selected order.  The former componentwise Python
    tuple ordering was therefore a storage shadow, not a tensor operation.
    Arbitrary-operand recognition lives in :meth:`Tensor.__eq__`, the declared
    equality boundary.
    """
    match op:
        case _ if op == op_EQ:
            return Tensor.__eq__(left, right)
        case _ if op == op_NE:
            return not Tensor.__eq__(left, right)
        case _:
            return NotImplemented

_BLACKBOARD_RING_NAMES = {
    "Z": "ZZ",
    "Q": "QQ",
    "R": "RR",
    "C": "CC",
    "N": "NN",
}


def _ring_session_and_latex(ring) -> tuple[str, str]:
    r"""Session name and blackboard latex for a ring."""
    raw = str(latex(ring))
    prefix = r"\Bold{"
    if raw.startswith(prefix) and raw.endswith("}") and raw.count("{") == 1:
        letter = raw[len(prefix) : -1]
        name = _BLACKBOARD_RING_NAMES.get(letter)
        if name is not None:
            return name, rf"\mathbb{{{letter}}}"
    return str(ring), raw


def _free_module_session_and_latex(ring, rank) -> tuple[str, str]:
    r"""Session name and latex for the free module \(R^n\) or \(R^{\mathbb N}\)."""
    name, tex = _ring_session_and_latex(ring)
    if rank == Infinity:
        return f"{name}^NN", rf"{tex}^{{\mathbb{{N}}}}"
    return f"{name}^{rank}", rf"{tex}^{{{rank}}}"


def _otimes_session(factors: tuple[str, ...], unit: str) -> str:
    if not factors:
        return unit
    if len(factors) == 1:
        return factors[0]
    return " ⊗ ".join(factors)


def _otimes_latex(factors: tuple[str, ...], unit: str) -> str:
    if not factors:
        return unit
    if len(factors) == 1:
        return factors[0]
    return r" \otimes ".join(factors)


def _collapse_equal_power(factors: tuple[str, ...], *, latex_mode: bool) -> str | None:
    r"""Return a tensor power when every factor is the same; otherwise ``None``."""
    if not factors:
        return None
    first = factors[0]
    if any(factor != first for factor in factors[1:]):
        return None
    count = len(factors)
    if count == 1:
        return first
    if latex_mode:
        return rf"({first})^{{\otimes {count}}}"
    return f"({first})^{{⊗{count}}}"


def _tensor_space_session_and_latex(
    ring, upper_ranks: tuple, lower_ranks: tuple
) -> tuple[str, str]:
    r"""Name the module of type-\((p,q)\) tensors with these index ranks.

    On \(M=R^n\) this is \(M^{\otimes p}\otimes(M^*)^{\otimes q}\).  At
    infinite rank a type-\((0,q)\) tensor lives in
    \((M^{\otimes q})^*\), which is not \((M^*)^{\otimes q}\).
    """
    ring_name, ring_tex = _ring_session_and_latex(ring)
    upper_session = tuple(
        _free_module_session_and_latex(ring, rank)[0] for rank in upper_ranks
    )
    lower_session = tuple(
        _free_module_session_and_latex(ring, rank)[0] for rank in lower_ranks
    )
    upper_tex = tuple(
        _free_module_session_and_latex(ring, rank)[1] for rank in upper_ranks
    )
    lower_tex = tuple(
        _free_module_session_and_latex(ring, rank)[1] for rank in lower_ranks
    )
    dual_session = tuple(f"({name})*" for name in lower_session)
    dual_tex = tuple(rf"({name})^{{*}}" for name in lower_tex)
    infinite = Infinity in upper_ranks + lower_ranks
    if infinite:
        domain_session = _otimes_session(lower_session, ring_name)
        domain_tex = _otimes_latex(lower_tex, ring_tex)
        if not upper_ranks:
            return (
                f"({domain_session})*",
                rf"({domain_tex})^{{*}}",
            )
        if not lower_ranks:
            return (
                _otimes_session(upper_session, ring_name),
                _otimes_latex(upper_tex, ring_tex),
            )
        codomain_session = _otimes_session(upper_session, ring_name)
        codomain_tex = _otimes_latex(upper_tex, ring_tex)
        return (
            f"Hom({domain_session}, {codomain_session})",
            rf"\operatorname{{Hom}}({domain_tex}, {codomain_tex})",
        )

    def finite_factor(factors, latex_mode):
        if not factors:
            return None
        collapsed = _collapse_equal_power(factors, latex_mode=latex_mode)
        if collapsed is not None:
            return collapsed
        if latex_mode:
            return _otimes_latex(factors, ring_tex)
        return _otimes_session(factors, ring_name)

    session_factors = tuple(
        factor
        for factor in (
            finite_factor(upper_session, False),
            finite_factor(dual_session, False),
        )
        if factor is not None
    )
    tex_factors = tuple(
        factor
        for factor in (
            finite_factor(upper_tex, True),
            finite_factor(dual_tex, True),
        )
        if factor is not None
    )
    if not session_factors:
        return ring_name, ring_tex
    return (
        _otimes_session(session_factors, ring_name),
        _otimes_latex(tex_factors, ring_tex),
    )


class Tensor:
    r"""A tensor of type $(p,q)$.

    A type-$(p,q)$ tensor on a module \(M\) is an element of
    \(M^{\otimes p}\otimes(M^*)^{\otimes q}\).  When the index modules
    differ, it is an element of the corresponding mixed tensor product.
    At infinite rank a type-$(0,2)$ pairing lives in
    \((M\otimes M)^*\), not in \((M^*)^{\otimes 2}\).

    This class carries no storage.  Every tensor, of every valence, is an
    element of a :func:`TensorModule` over the owned base ring, and its
    type and index ranks are those of that module: the parent is the tensor
    space, so the element states neither again.
    """

    __slots__ = ()

    def _index_ranks(self) -> tuple:
        r"""Return the index ranks of this tensor's module, contravariant slots first.

        Private plumbing for the slot families; the public view is
        :meth:`tensor_shape`.
        """
        return self.parent()._index_ranks()

    def tensor_shape(self):
        r"""Return the family assigning each index slot the rank of its module.

        The slots are indexed by \(\Delta[k-1]\) for order \(k\), and a rank
        is a cardinal, so this is a family and not a Python tuple: two slots
        of equal rank are two slots, which a set would collapse.
        """
        return index_rank_family(self._index_ranks())

    def _upper_index_ranks(self) -> tuple:
        r"""Return the dimensions of the contravariant indices."""
        p, _q = self.tensor_type()
        return self._index_ranks()[:p]

    def _lower_index_ranks(self) -> tuple:
        r"""Return the dimensions of the covariant indices."""
        p, _q = self.tensor_type()
        return self._index_ranks()[p:]

    def tensor_type(self) -> ProductOfNaturalNumbers:
        r"""Return $(p,q)$: $p$ contravariant indices and $q$ covariant indices.

        A vector is type $(1,0)$.  A matrix, as a linear map, is type
        $(1,1)$.  A Gram tensor is type $(0,2)$.
        """
        return self.tensor_valence()

    def tensor_valence(self) -> ProductOfNaturalNumbers:
        r"""Return the type $(p,q)$ of this tensor's module; synonym of :meth:`tensor_type`."""
        return self.parent().tensor_valence()

    def tensor_order(self):
        r"""Return the cardinal number of tensor indices."""
        return cardinal(len(self._index_ranks()))

    def gram_graph(self):
        r"""Return the weighted graph presented by this type-``(0,2)`` Gram tensor."""
        from dzack_research.preamble.categories.forms.gram_matrices import (
            _gram_tensor_graph,
        )

        return _gram_tensor_graph(self)

    def gram_connected_component_cuts(self):
        r"""Return cuts between consecutive connected Gram blocks."""
        from dzack_research.preamble.categories.forms.gram_matrices import (
            _tensor_connected_component_cuts,
        )

        return _tensor_connected_component_cuts(self)

    def tensor_space(self):
        r"""Return the module of which this tensor is an element.

        For type $(p,q)$ on \(R^n\) this is
        \((R^n)^{\otimes p}\otimes((R^n)^*)^{\otimes q}\), which is the parent.
        """
        return self.parent()

    def contravariant_index_modules(self):
        r"""Return the family of contravariant index modules."""
        return self.tensor_space().contravariant_index_modules()

    def covariant_index_modules(self):
        r"""Return the family of covariant index modules."""
        return self.tensor_space().covariant_index_modules()

    def index_modules(self):
        r"""Return the contravariant/covariant module families as an object of ``Objects x Objects``."""
        return self.tensor_space().index_modules()

    def contravariant_index_generating_sets(self):
        r"""Return the selected generating sets of the contravariant index modules."""
        return self.tensor_space().contravariant_index_generating_sets()

    def covariant_index_generating_sets(self):
        r"""Return the selected generating sets of the covariant index modules."""
        return self.tensor_space().covariant_index_generating_sets()

    def tensor_indices(self):
        r"""Return the two variance-indexed generating-set families as an object of ``Objects x Objects``."""
        return self.tensor_space().tensor_indices()

    def components(self):
        r"""Return the finite rectangular component array of this tensor."""
        shape = self._index_ranks()
        if Infinity in shape:
            raise ValueError("an infinite tensor has no finite component array")
        from itertools import product as cartesian_product

        entries = tuple(
            self[position]
            for position in cartesian_product(*(range(rank) for rank in shape))
        )
        return _nested(entries, shape)

    def list(self):
        r"""Return flattened finite components in tensor-index order."""
        shape = self._index_ranks()
        if Infinity in shape:
            raise ValueError("an infinite tensor has no finite component list")
        from itertools import product as cartesian_product

        return [
            self[position]
            for position in cartesian_product(*(range(rank) for rank in shape))
        ]

    def _tensor_hash(self) -> int:
        r"""Hash the data equality compares: variance, ranks, components.

        Equal tensors hash equally, so a tensor may key a cache and may be
        a constructor argument of a unique representation.  At infinite
        rank there is no component list and equality is identity, so the
        identity hash is the honest one.
        """
        if Infinity in self._index_ranks():
            return object.__hash__(self)
        return hash(
            (self.tensor_valence(), self._index_ranks(), tuple(self.list()))
        )

    def __eq__(self, other) -> bool:
        r"""Whether ``other`` is the same mathematical tensor.

        This is the arbitrary-operand equality boundary.  Tensor
        implementations may use different storage parents, so equality
        compares variance, slot ranks, coefficient ring, and components rather
        than concrete parent identity.
        """
        if not isinstance(other, Tensor):
            return False
        if self.tensor_valence() != other.tensor_valence():
            return False
        if self.tensor_shape() != other.tensor_shape():
            return False
        if _engine_ring(self.base_ring()) != _engine_ring(other.base_ring()):
            return False
        if Infinity in self._index_ranks():
            return self is other
        return all(
            left == right
            for left, right in zip(self.list(), other.list(), strict=True)
        )

    def __ne__(self, other) -> bool:
        return not Tensor.__eq__(self, other)

    def is_equal_tensor(self, other: "Tensor") -> bool:
        r"""Return whether the tensor ``other`` is the same tensor mathematically.

        This deliberately ignores the concrete storage parent.  Tensor spaces
        built from equal owned/engine ring facades can have distinct Sage
        parents while representing the same variance, ranks, and components.
        """
        return Tensor.__eq__(self, other)

    def change_ring(self, ring):
        r"""Change coefficients without changing tensor variance."""
        return tensor(
            ring,
            self._upper_index_ranks(),
            self._lower_index_ranks(),
            self.components(),
        )

    def is_symmetric(self) -> bool:
        r"""Return whether a square two-index tensor is symmetric in its slots."""
        if self.tensor_order() != 2:
            raise TypeError("symmetry here is defined for a two-index tensor")
        first_rank, second_rank = self._index_ranks()
        if first_rank != second_rank:
            return False
        return all(
            self[i, j] == self[j, i]
            for i in range(first_rank)
            for j in range(second_rank)
        )

    def _partial_contract(self, other, slot=0, other_slot=0):
        r"""Contract upper ``slot`` of ``self`` with lower ``other_slot`` of ``other``."""
        if not _is_coordinate_tensor(other, self.base_ring()):
            raise TypeError("tensor contraction pairs two tensors over one base ring")
        upper = self._upper_index_ranks()
        lower = self._lower_index_ranks()
        other_upper = other._upper_index_ranks()
        other_lower = other._lower_index_ranks()
        slot = int(slot)
        other_slot = int(other_slot)
        if slot < 0 or slot >= len(upper):
            raise IndexError("the selected slot is not an upper index of the left tensor")
        if other_slot < 0 or other_slot >= len(other_lower):
            raise IndexError("the selected slot is not a lower index of the right tensor")
        if upper[slot] != other_lower[other_slot]:
            raise ValueError("contracted tensor slots must have the same rank")
        assert Infinity not in self._index_ranks() + other._index_ranks(), (
            "coordinate contraction requires finite represented index ranks"
        )

        from itertools import product as cartesian_product

        result_upper = upper[:slot] + upper[slot + 1 :] + other_upper
        result_lower = lower + other_lower[:other_slot] + other_lower[other_slot + 1 :]
        entries = {}
        self_positions = cartesian_product(*(range(rank) for rank in self._index_ranks()))
        other_positions = tuple(
            cartesian_product(*(range(rank) for rank in other._index_ranks()))
        )
        for left_index in self_positions:
            left_value = self[left_index]
            if not left_value:
                continue
            left_upper = left_index[: len(upper)]
            left_lower = left_index[len(upper) :]
            contracted = left_upper[slot]
            for right_index in other_positions:
                right_upper = right_index[: len(other_upper)]
                right_lower = right_index[len(other_upper) :]
                if contracted != right_lower[other_slot]:
                    continue
                right_value = other[right_index]
                if not right_value:
                    continue
                result_index = (
                    left_upper[:slot]
                    + left_upper[slot + 1 :]
                    + right_upper
                    + left_lower
                    + right_lower[:other_slot]
                    + right_lower[other_slot + 1 :]
                )
                entries[result_index] = entries.get(
                    result_index, self.base_ring().zero()
                ) + left_value * right_value

        if not result_upper and not result_lower:
            return entries.get((), self.base_ring().zero())
        shape = result_upper + result_lower
        values = tuple(
            entries.get(index, self.base_ring().zero())
            for index in cartesian_product(*(range(rank) for rank in shape))
        )
        return tensor(
            self.base_ring(),
            result_upper,
            result_lower,
            _nested(values, shape),
        )

    def contract(self, *vectors, slot=0, other_slot=0):
        r"""Contract represented tensor slots or fully evaluate a covariant tensor.

        When this tensor has an upper slot, ``contract(other, slot=i,
        other_slot=j)`` pairs that upper slot with lower slot ``j`` of
        ``other``.  The result has type ``(p-1+p', q+q'-1)``.  When this tensor
        is purely covariant, the historical evaluation spelling is retained:
        ``contract(v_1,...,v_q)`` fully evaluates it on contravariant vectors.
        """
        if self._upper_index_ranks():
            if len(vectors) != 1:
                raise TypeError("partial tensor contraction takes exactly one other tensor")
            return self._partial_contract(vectors[0], slot=slot, other_slot=other_slot)
        if int(slot) != 0 or int(other_slot) != 0:
            raise TypeError("slot selectors apply only to upper/lower tensor contraction")
        if len(vectors) != len(self._lower_index_ranks()):
            raise TypeError(
                f"a type-{self.tensor_valence()} tensor takes "
                f"{len(self._lower_index_ranks())} vector arguments, got {len(vectors)}"
            )
        for rank, vector in zip(self._lower_index_ranks(), vectors, strict=True):
            slot_module = TensorModule(self.base_ring(), (rank,), ())
            if vector not in slot_module:
                raise TypeError(
                    f"covariant tensor contraction takes, in a slot of rank {rank}, "
                    f"a vector of {slot_module}"
                )
        from itertools import product as cartesian_product

        return sum(
            (
                self[position]
                * prod(
                    (
                        vector[index]
                        for vector, index in zip(vectors, position, strict=True)
                    ),
                    start=self.base_ring().one(),
                )
                for position in cartesian_product(*(range(rank) for rank in self._lower_index_ranks()))
            ),
            self.base_ring().zero(),
        )

    def trace(self, slot=0, other_slot=0):
        r"""Contract one upper and one lower slot of this tensor."""
        upper = self._upper_index_ranks()
        lower = self._lower_index_ranks()
        slot = int(slot)
        other_slot = int(other_slot)
        if slot < 0 or slot >= len(upper) or other_slot < 0 or other_slot >= len(lower):
            raise IndexError("the tensor has no such upper/lower pair of slots")
        if upper[slot] != lower[other_slot]:
            raise ValueError("traced tensor slots must have the same rank")
        assert Infinity not in self._index_ranks(), (
            "coordinate trace requires finite represented index ranks"
        )

        from itertools import product as cartesian_product

        result_upper = upper[:slot] + upper[slot + 1 :]
        result_lower = lower[:other_slot] + lower[other_slot + 1 :]
        entries = {}
        for index in cartesian_product(*(range(rank) for rank in self._index_ranks())):
            upper_index = index[: len(upper)]
            lower_index = index[len(upper) :]
            if upper_index[slot] != lower_index[other_slot]:
                continue
            result_index = (
                upper_index[:slot]
                + upper_index[slot + 1 :]
                + lower_index[:other_slot]
                + lower_index[other_slot + 1 :]
            )
            entries[result_index] = entries.get(
                result_index, self.base_ring().zero()
            ) + self[index]

        if not result_upper and not result_lower:
            return entries.get((), self.base_ring().zero())
        shape = result_upper + result_lower
        values = tuple(
            entries.get(index, self.base_ring().zero())
            for index in cartesian_product(*(range(rank) for rank in shape))
        )
        return tensor(
            self.base_ring(),
            result_upper,
            result_lower,
            _nested(values, shape),
        )

    def tensor_product(self, other):
        r"""Return the outer tensor product, preserving upper/lower slot order."""
        if not _is_coordinate_tensor(other, self.base_ring()):
            raise TypeError("a tensor product is taken with another tensor over one base ring")
        assert Infinity not in self._index_ranks() + other._index_ranks(), (
            "coordinate tensor products require finite represented index ranks"
        )

        from itertools import product as cartesian_product

        upper = self._upper_index_ranks()
        lower = self._lower_index_ranks()
        other_upper = other._upper_index_ranks()
        other_lower = other._lower_index_ranks()
        result_upper = upper + other_upper
        result_lower = lower + other_lower
        entries = {}
        left_positions = cartesian_product(*(range(rank) for rank in self._index_ranks()))
        right_positions = tuple(
            cartesian_product(*(range(rank) for rank in other._index_ranks()))
        )
        for left_index in left_positions:
            left_upper = left_index[: len(upper)]
            left_lower = left_index[len(upper) :]
            left_value = self[left_index]
            if not left_value:
                continue
            for right_index in right_positions:
                right_value = other[right_index]
                if not right_value:
                    continue
                right_upper = right_index[: len(other_upper)]
                right_lower = right_index[len(other_upper) :]
                result_index = left_upper + right_upper + left_lower + right_lower
                entries[result_index] = entries.get(
                    result_index, self.base_ring().zero()
                ) + left_value * right_value

        shape = result_upper + result_lower
        if not shape:
            return entries.get((), self.base_ring().zero())
        values = tuple(
            entries.get(index, self.base_ring().zero())
            for index in cartesian_product(*(range(rank) for rank in shape))
        )
        return tensor(
            self.base_ring(),
            result_upper,
            result_lower,
            _nested(values, shape),
        )

    def raise_index(self, formed_module, slot=0):
        r"""Raise one lower index with the inverse Gram tensor of ``formed_module``.

        The selected lower slot must have the rank of the supplied formed
        module.  Over an integral base this requires the inverse Gram entries
        to remain integral; no automatic scalar extension is performed.
        """
        lower = self._lower_index_ranks()
        upper = self._upper_index_ranks()
        slot = int(slot)
        if slot < 0 or slot >= len(lower):
            raise IndexError("the selected slot is not a lower tensor index")
        if _engine_ring(formed_module.base_ring()) != _engine_ring(self.base_ring()):
            raise TypeError("raising an index requires the tensor and form over one base ring")
        rank = int(formed_module.module_rank())
        if lower[slot] != rank:
            raise ValueError("the selected lower slot has the wrong rank for this form")
        assert Infinity not in self._index_ranks(), (
            "coordinate index raising requires finite represented index ranks"
        )

        inverse = _engine_component_matrix(formed_module.gram_tensor()).inverse()
        ring = self.base_ring()
        # The inverse is computed over the engine's fraction field; the index
        # is raised over ``ring`` exactly when every entry lies in ``ring``.
        engine = _engine_ring(ring)
        if not all(entry in engine for entry in inverse.list()):
            raise ValueError(
                "raising an index over this ring requires the inverse Gram entries in the base ring"
            )
        coefficients = {
            (raised, contracted): ring._from_engine_element(inverse[raised, contracted])
            for raised in range(rank)
            for contracted in range(rank)
        }

        from itertools import product as cartesian_product

        result_upper = upper + (rank,)
        result_lower = lower[:slot] + lower[slot + 1 :]
        entries = {}
        for index in cartesian_product(*(range(index_rank) for index_rank in self._index_ranks())):
            value = self[index]
            if not value:
                continue
            upper_index = index[: len(upper)]
            lower_index = index[len(upper) :]
            contracted = lower_index[slot]
            remaining_lower = lower_index[:slot] + lower_index[slot + 1 :]
            for raised in range(rank):
                coefficient = coefficients[raised, contracted]
                if not coefficient:
                    continue
                result_index = upper_index + (raised,) + remaining_lower
                entries[result_index] = entries.get(
                    result_index, ring.zero()
                ) + coefficient * value

        shape = result_upper + result_lower
        values = tuple(
            entries.get(index, ring.zero())
            for index in cartesian_product(*(range(index_rank) for index_rank in shape))
        )
        return tensor(ring, result_upper, result_lower, _nested(values, shape))

    def lower_index(self, formed_module, slot=0):
        r"""Lower one upper index with the Gram tensor of ``formed_module``."""
        upper = self._upper_index_ranks()
        lower = self._lower_index_ranks()
        slot = int(slot)
        if slot < 0 or slot >= len(upper):
            raise IndexError("the selected slot is not an upper tensor index")
        if _engine_ring(formed_module.base_ring()) != _engine_ring(self.base_ring()):
            raise TypeError("lowering an index requires the tensor and form over one base ring")
        rank = int(formed_module.module_rank())
        if upper[slot] != rank:
            raise ValueError("the selected upper slot has the wrong rank for this form")
        assert Infinity not in self._index_ranks(), (
            "coordinate index lowering requires finite represented index ranks"
        )

        gram = formed_module.gram_tensor()
        ring = self.base_ring()
        from itertools import product as cartesian_product

        result_upper = upper[:slot] + upper[slot + 1 :]
        result_lower = lower + (rank,)
        entries = {}
        for index in cartesian_product(*(range(index_rank) for index_rank in self._index_ranks())):
            value = self[index]
            if not value:
                continue
            upper_index = index[: len(upper)]
            lower_index = index[len(upper) :]
            contracted = upper_index[slot]
            remaining_upper = upper_index[:slot] + upper_index[slot + 1 :]
            for lowered in range(rank):
                coefficient = gram[lowered, contracted]
                if not coefficient:
                    continue
                result_index = remaining_upper + lower_index + (lowered,)
                entries[result_index] = entries.get(
                    result_index, ring.zero()
                ) + coefficient * value

        shape = result_upper + result_lower
        values = tuple(
            entries.get(index, ring.zero())
            for index in cartesian_product(*(range(index_rank) for index_rank in shape))
        )
        return tensor(ring, result_upper, result_lower, _nested(values, shape))

    def dual_tensor(self):
        r"""Dualize a nondegenerate pairing or copairing.

        For a nondegenerate pairing ``g`` of type ``(0,2)``, duality through
        its correlation isomorphism produces the contravariant tensor
        ``g^vee`` of type ``(2,0)`` on the dual module.  Conversely a
        nondegenerate type-``(2,0)`` tensor dualizes to type ``(0,2)``.
        """
        valence = self.tensor_valence()
        first_rank, second_rank = self._index_ranks()
        if valence in {(NN**2)((0, 2)), (NN**2)((2, 0))}:
            if first_rank != second_rank:
                raise ValueError("dualizing a pairing requires equal index ranks")
            inverse = _engine_component_matrix(self).inverse()
            ring = self.base_ring()
            components = [
                tuple(ring._from_engine_element(entry) for entry in row)
                for row in inverse.rows()
            ]
            if valence == (NN**2)((0, 2)):
                return tensor(ring, (first_rank, second_rank), (), components)
            return tensor(ring, (), (first_rank, second_rank), components)
        raise TypeError("dual_tensor is defined for nondegenerate pairings/copairings")

    def pullback(self, morphism):
        r"""Pull this covariant tensor back along an owned linear morphism.

        For ``f: V -> W`` and ``T`` of type ``(0,q)`` on ``W``, return
        ``f^*T`` on ``V``.  The public datum is the morphism.  Finite coordinate
        matrices are only an implementation of this transport: the morphism's
        own ``matrix()`` states and asserts that its endpoints are finitely
        generated framed free modules.
        """
        if self._upper_index_ranks():
            raise TypeError("pullback is defined here for a covariant tensor")
        if _is_coordinate_tensor(morphism, self.base_ring()):
            raise TypeError(
                "tensor pullback requires an owned linear morphism with finite framed-free "
                "endpoints; a tensor is component data, not a map"
            )
        matrix = morphism.matrix()

        if matrix.parent() not in MatrixSpaces(self.base_ring()):
            raise TypeError("tensor pullback requires one coefficient ring")
        target_rank, source_rank = matrix.parent().matrix_shape()
        if any(rank != target_rank for rank in self._lower_index_ranks()):
            raise ValueError(
                "the linear-map codomain rank must match every covariant tensor index"
            )
        q = len(self._lower_index_ranks())
        if q == 0:
            return self

        # The ubiquitous bilinear case is exactly A^t G A.  Use the selected
        # exact matrix backend only inside this boundary and cross every entry
        # back before constructing the owned tensor.
        if q == 2:

            backend_map = _engine_module_matrix(matrix)
            backend_form = _engine_component_matrix(self)
            backend_pullback = backend_map.transpose() * backend_form * backend_map
            ring = self.base_ring()
            entries = tuple(
                ring._from_engine_element(entry) for entry in backend_pullback.list()
            )
            return tensor(
                ring,
                (),
                (source_rank, source_rank),
                _nested(entries, (source_rank, source_rank)),
            )

        from itertools import product as cartesian_product

        source_positions = tuple(cartesian_product(range(source_rank), repeat=q))
        target_positions = tuple(cartesian_product(range(target_rank), repeat=q))
        entries = []
        for source_indices in source_positions:
            value = self.base_ring().zero()
            for target_indices in target_positions:
                coefficient = self[target_indices]
                for target_index, source_index in zip(
                    target_indices, source_indices, strict=True
                ):
                    coefficient *= matrix[target_index, source_index]
                value += coefficient
            entries.append(value)
        return tensor(
            self.base_ring(),
            (),
            (source_rank,) * q,
            _nested(tuple(entries), (source_rank,) * q),
        )



def _engine_component_matrix(value):
    r"""Private engine adapter (`OWN-06`): the Sage matrix of a two-index tensor.

    The owned operation -- a signature, an inverse Gram tensor, a pullback, a
    display -- is selected by the caller, and this is the one crossing of a
    two-index tensor into Sage's matrix backend: it lowers the owned base ring
    with ``_engine_ring`` and each component with ``_engine_element``.  The
    matrix it returns is engine data; callers cross results back into owned
    tensors before exposing them.
    """
    if value.tensor_order() != 2:
        raise TypeError("engine matrix materialization requires a two-index tensor")
    rows, columns = value._index_ranks()
    if rows == Infinity or columns == Infinity:
        raise ValueError("an infinite tensor has no finite engine matrix")
    rows, columns = int(rows), int(columns)
    ring = value.base_ring()
    return _sage_matrix(
        _engine_ring(ring),
        rows,
        columns,
        [_engine_element(ring, value[i, j]) for i in range(rows) for j in range(columns)],
    )


def _engine_component_vector(value):
    r"""Private engine adapter (`OWN-06`): the Sage vector of a one-index tensor.

    The one crossing of a one-index tensor, of either variance, into Sage's
    vector backend; its only caller is the plain-text component display.
    """
    if value.tensor_order() != 1:
        raise TypeError("engine vector materialization requires a one-index tensor")
    if value._index_ranks()[0] == Infinity:
        raise ValueError("an infinite vector tensor has no finite engine vector")
    ring = value.base_ring()
    return _sage_vector(
        _engine_ring(ring),
        [_engine_element(ring, entry) for entry in value.list()],
    )


class _TensorVectorConstructor:
    r"""Construct a type-``(1,0)`` tensor from an owned ring and components."""

    def __call__(self, base_ring, components=None, *args, **kwds):
        if args or kwds:
            raise TypeError(
                "tensor.vector accepts a preamble ring and one component family"
            )
        if base_ring not in _Rings:
            raise TypeError("tensor.vector expects a preamble ring")
        if components is None:
            raise TypeError("tensor.vector requires its component family")
        # Literal component data: a natural number is the rank of the zero
        # vector; a Python mapping gives the nonzero components by position;
        # anything else is the sequence of components in order.
        match components:
            case _ if components in NN:
                entries = tuple(base_ring.zero() for _ in range(int(components)))
            case dict():
                size = 0 if not components else max(int(index) for index in components) + 1
                entries = tuple(
                    components.get(index, base_ring.zero()) for index in range(size)
                )
            case _:
                entries = tuple(components)
        return tensor(base_ring, (len(entries),), (), entries)


class _TensorCovectorConstructor:
    r"""Construct a type-``(0,1)`` tensor from an owned ring and components.

    A covector is an element of the dual tensor module, so it never shares a
    parent with a type-``(1,0)`` vector even when the component families agree.

    EXAMPLES::

        sage: from dzack_research.preamble.tensors import tensor
        sage: c = tensor.covector(ZZ, [2, -1, 4])
        sage: c.tensor_valence()
        (0, 1)
        sage: c.parent()
        (ZZ^3)*
        sage: c * tensor.vector(ZZ, [5, 6, 7])
        32
    """

    def __call__(self, base_ring, components=None, *args, **kwds):
        contravariant = _TensorVectorConstructor()(
            base_ring, components, *args, **kwds
        )
        return tensor(
            contravariant.base_ring(),
            (),
            contravariant._upper_index_ranks(),
            contravariant.list(),
        )


class _TensorMatrixConstructor:
    r"""Construct finite type-``(1,1)`` coordinate tensors.

    This is component data, not a module morphism.  Actual linear maps are
    elements of ``R.matrix_space(m,n) = Hom_R(R^n,R^m)``.  Sage matrix storage
    options and named constructor namespaces are deliberately not reproduced.
    """

    def __call__(self, *args, **kwds):
        if kwds:
            raise TypeError(
                "tensor.matrix accepts preamble tensor data, not Sage matrix storage options"
            )
        if not args or args[0] not in _Rings:
            raise TypeError("tensor.matrix expects a preamble base ring")
        base = args[0]
        if len(args) == 2:
            components = args[1]
            if _is_coordinate_tensor(components, base):
                if components.tensor_order() != 2:
                    raise TypeError("a matrix tensor has two indices")
                # Reinterpretation: the two index ranks are read off, and the
                # result is the type-(1,1) tensor this constructor makes.  The
                # input's own variance does not survive, which is the whole
                # content of reading its components as a matrix.  The tensor
                # is over this constructor's ring: moving components to
                # another ring is scalar change, done by ``change_ring``.
                contravariant_rank, covariant_rank = components._index_ranks()
                return tensor(
                    base,
                    (contravariant_rank,),
                    (covariant_rank,),
                    components.components(),
                )
            shape = _component_shape(components)
            if len(shape) != 2:
                raise TypeError(
                    "tensor.matrix(R, components) requires a rectangular two-index array"
                )
            rows, columns = shape
            return _coordinate_tensor(base, (rows,), (columns,), components)
        if len(args) in (3, 4):
            rows = int(args[1])
            columns = int(args[2])
            components = (
                tuple(base.zero() for _ in range(rows * columns))
                if len(args) == 3
                else args[3]
            )
            return _coordinate_tensor(base, (rows,), (columns,), components)
        raise TypeError(
            "tensor.matrix expects (R, components) or (R, rows, columns[, components])"
        )


@singledispatch
def _component_shape(component) -> tuple[int, ...]:
    r"""A non-list/tuple is one scalar component and has no remaining indices."""
    return ()


def _sequence_shape(components: list | tuple) -> tuple[int, ...]:
    r"""Return the shape of one rectangular nested component array."""
    if not components:
        return (0,)
    shapes = tuple(_component_shape(component) for component in components)
    first = shapes[0]
    if any(shape != first for shape in shapes[1:]):
        raise ValueError(f"tensor components are ragged: {shapes}")
    return (len(components),) + first


@_component_shape.register
def _(components: list) -> tuple[int, ...]:
    return _sequence_shape(components)


@_component_shape.register
def _(components: tuple) -> tuple[int, ...]:
    return _sequence_shape(components)


def _flatten(components, shape: tuple[int, ...]) -> tuple:
    r"""Flatten a component array whose rectangular shape is already known."""
    if not shape:
        return (components,)
    return tuple(
        entry
        for block in components
        for entry in _flatten(block, shape[1:])
    )


def _nested(entries: tuple, shape: tuple[int, ...]):
    r"""Rebuild the rectangular list presentation of flat row-major entries."""
    if len(shape) == 1:
        return list(entries)
    block_size = prod(shape[1:])
    return [
        _nested(entries[i * block_size : (i + 1) * block_size], shape[1:])
        for i in range(shape[0])
    ]


class _CoordinateTensor(ModuleElement, Tensor):
    r"""A tensor stored as its row-major component array.

    The element engine of the tensor module: its datum is the flat
    sequence of components, and its type, ranks and base ring are those of
    the tensor module it is an element of.
    """

    def __init__(self, parent: Parent, entries: tuple) -> None:
        self._entries = entries
        ModuleElement.__init__(self, parent)

    def __call__(self, *args):
        r"""Feed vectors into the covariant slots, from left to right.

        For a type-$(p,q)$ tensor, supplying $k\leq q$ vectors returns a
        type-$(p,q-k)$ tensor.  Only when every slot is consumed and $p=0$
        does evaluation return a scalar.
        """
        from itertools import product as _index_tuples

        _contravariant, covariant = self.tensor_valence()
        if NN(len(args)) > covariant:
            raise TypeError(
                f"a type-{self.tensor_valence()} tensor has only "
                f"{covariant} covariant slots, got {len(args)} arguments"
            )
        if not args:
            return self
        ring = self.base_ring()
        upper = self._upper_index_ranks()
        lower = self._lower_index_ranks()
        consumed = lower[: len(args)]
        remaining = lower[len(args) :]
        for position, vector in enumerate(args):
            slot = TensorModule(ring, (consumed[position],), ())
            if vector not in slot:
                raise TypeError(
                    f"argument {position} must be an owned vector in {slot}, "
                    f"the contravariant module paired with covariant slot {position}"
                )

        def contracted(output_index):
            upper_index = output_index[: len(upper)]
            remaining_index = output_index[len(upper) :]
            total = ring.zero()
            for eaten in _index_tuples(*(range(int(rank)) for rank in consumed)):
                term = self[upper_index + eaten + remaining_index]
                for position, index in enumerate(eaten):
                    term = term * args[position][index]
                total = total + term
            return total

        result_ranks = upper + remaining
        if not result_ranks:
            return contracted(())
        values = tuple(
            contracted(index)
            for index in _index_tuples(*(range(int(rank)) for rank in result_ranks))
        )
        return tensor(ring, upper, remaining, _nested(values, result_ranks))

    def _latex_(self) -> str:
        if len(self._index_ranks()) == 2:
            return str(latex(_engine_component_matrix(self)))
        return str(latex(self.components()))

    def _repr_(self) -> str:
        p, q = self.tensor_type()
        space = repr(self.parent())
        body = _coordinate_component_repr(self)
        return f"Type ({p}, {q}) tensor in {space}\n{body}"

    def components(self):
        r"""Return the rectangular nested component array."""
        return _nested(self._entries, self._index_ranks())

    def list(self):
        r"""Return flattened components in index order."""
        return list(self._entries)

    def __getitem__(self, index):
        r"""Return the component at a position, one integer per slot.

        A position is a tuple of integers, one per slot; a single integer is
        the position of a one-index tensor, ``v[i]``.  A negative integer
        counts back from the rank of its slot.

        Python's item-access protocol delivers ``t[i, j]`` as the tuple
        ``(i, j)`` and ``v[i]`` as ``i`` itself, so the key's syntax -- a
        tuple or not -- says which was written.  Membership in the integers
        cannot say it: Sage's ``Integer`` reads a tuple as a list of digits.
        """
        match index:
            case tuple():
                positions = index
            case _:
                positions = (index,)
        if len(positions) != len(self._index_ranks()):
            raise IndexError(
                f"a tensor of shape {self._index_ranks()} takes "
                f"{self.tensor_order()} indices, got {len(positions)}"
            )
        offset = 0
        for position, dimension in zip(positions, self._index_ranks()):
            position = int(position)
            if position < 0:
                position += dimension
            if position < 0 or position >= dimension:
                raise IndexError(index)
            offset = offset * dimension + position
        return self._entries[offset]

    def _add_(self, other):
        if other.parent() is not self.parent():
            raise TypeError("tensors add only in the same tensor space")
        return self.parent()._element_constructor_(
            tuple(left + right for left, right in zip(self._entries, other._entries))
        )

    def _sub_(self, other):
        if other.parent() is not self.parent():
            raise TypeError("tensors subtract only in the same tensor space")
        return self.parent()._element_constructor_(
            tuple(left - right for left, right in zip(self._entries, other._entries))
        )

    def _neg_(self):
        return self.parent()._element_constructor_(tuple(-entry for entry in self._entries))

    def _lmul_(self, scalar):
        return self.parent()._element_constructor_(
            tuple(entry * scalar for entry in self._entries)
        )

    def _rmul_(self, scalar):
        return self.parent()._element_constructor_(
            tuple(scalar * entry for entry in self._entries)
        )

    def __mul__(self, other):
        r"""Scale by a scalar, or contract with a tensor over the same ring.

        Multiplication contracts the left tensor's rightmost covariant index
        with the right tensor's first contravariant index; a left tensor with
        no covariant index and at least two contravariant ones instead pairs
        its last contravariant index with a covector.  Which of these applies
        is read from the two tensor modules, after placement has established
        that ``other`` is a scalar of the base ring or an element of a tensor
        module over it.
        """
        ring = self.base_ring()
        if other in ring:
            return self._lmul_(ring(other))
        if not _is_coordinate_tensor(other, ring):
            raise TypeError(
                "there is no generic tensor multiplication; use a stated contraction, "
                "or tensor product"
            )
        upper = self._upper_index_ranks()
        lower = self._lower_index_ranks()
        valence = self.tensor_valence()
        other_valence = other.tensor_valence()
        from itertools import product as cartesian_product

        if len(upper) >= 2 and not lower and other_valence == (NN**2)((0, 1)):
            if upper[-1] != other._lower_index_ranks()[0]:
                raise ValueError(
                    f"cannot contract ranks {upper[-1]} and "
                    f"{other._lower_index_ranks()[0]}"
                )
            output_upper = upper[:-1]
            contracted_rank = upper[-1]
            positions = tuple(cartesian_product(*(range(rank) for rank in output_upper)))
            entries = tuple(
                sum(
                    (self[position + (index,)] * other[index] for index in range(contracted_rank)),
                    ring.zero(),
                )
                for position in positions
            )
            return tensor(ring, output_upper, (), _nested(entries, output_upper))
        if other_valence == (NN**2)((1, 0)):
            if not lower:
                raise TypeError("a tensor with no covariant index cannot act on a vector")
            if lower[-1] != other._upper_index_ranks()[0]:
                raise ValueError(
                    f"cannot contract ranks {lower[-1]} and "
                    f"{other._upper_index_ranks()[0]}"
                )

            # Multiplication contracts the rightmost covariant index.  Thus a
            # bilinear form G in M* tensor M* acts on v in M as G*v in M*,
            # with components (G*v)_i = sum_j G_{ij} v_j.  No row-vector or
            # transpose convention enters the public tensor calculus.
            output_upper = upper
            output_lower = lower[:-1]
            output_shape = output_upper + output_lower
            contracted_rank = lower[-1]
            positions = tuple(
                cartesian_product(*(range(rank) for rank in output_shape))
            ) if output_shape else ((),)
            entries = tuple(
                sum(
                    (self[position + (index,)] * other[index] for index in range(contracted_rank)),
                    ring.zero(),
                )
                for position in positions
            )
            if not output_shape:
                return entries[0]
            return tensor(ring, output_upper, output_lower, _nested(entries, output_shape))
        if valence == (NN**2)((1, 1)) and other_valence == (NN**2)((1, 1)):
            if lower != other._upper_index_ranks():
                raise ValueError(
                    f"cannot contract ranks {lower} and {other._upper_index_ranks()}"
                )
            # In U tensor V* tensor V tensor W*, contract the adjacent V*, V
            # factors.  Under Hom(V,U) = U tensor V* this agrees with map
            # composition, but its owner here is tensor evaluation.
            rows = upper[0]
            inner = other._upper_index_ranks()[0]
            columns = other._lower_index_ranks()[0]
            entries = tuple(
                sum((self[i, k] * other[k, j] for k in range(inner)), ring.zero())
                for i in range(rows)
                for j in range(columns)
            )
            return tensor(ring, (rows,), (columns,), _nested(entries, (rows, columns)))
        if valence == (NN**2)((0, 1)) and other_valence == (NN**2)((1, 1)):
            # In V* tensor V tensor W*, evaluate the adjacent V*, V pair.
            if lower != other._upper_index_ranks():
                raise ValueError(
                    f"cannot contract ranks {lower} and {other._upper_index_ranks()}"
                )
            rows = lower[0]
            columns = other._lower_index_ranks()[0]
            entries = tuple(
                sum((self[i] * other[i, j] for i in range(rows)), ring.zero())
                for j in range(columns)
            )
            return tensor(ring, (), (columns,), entries)
        raise TypeError(
            f"multiplication contracts the left tensor's rightmost covariant "
            f"index with the right tensor's first contravariant index; "
            f"type-{valence} and type-{other_valence} do not meet that way"
        )

    def __rmul__(self, other):
        r"""Scale by a scalar of the base ring on the left.

        A left operand that is not a scalar of the base ring is left to
        Python's operator protocol, which reports the product as unsupported.
        """
        ring = self.base_ring()
        if other not in ring:
            return NotImplemented
        return self._rmul_(ring(other))

    def _richcmp_(self, other, op):
        return _tensor_richcmp(self, other, op)

    __hash__ = Tensor._tensor_hash

    def __reduce__(self):
        return (
            _restore_tensor,
            (
                self.base_ring(),
                self._upper_index_ranks(),
                self._lower_index_ranks(),
                self.components(),
            ),
        )


def _coordinate_component_repr(tensor_value) -> str:
    r"""Plain-text components: a vector, a matrix, or a nested array."""
    match len(tensor_value._index_ranks()):
        case 1:
            return repr(_engine_component_vector(tensor_value))
        case 2:
            return repr(_engine_component_matrix(tensor_value))
        case _:
            return repr(tensor_value.components())


def _normalized_rank(rank):
    r"""The rank of one tensor slot: an ``int``, or ``Infinity`` for an infinite slot."""
    return Infinity if rank == Infinity else int(cardinal(rank).finite_value())


class _CoordinateTensorModule:
    r"""Private component-array realization of an R-module of tensors.

    It retains the split rank vector for the contraction engine.  The module
    is constructed through Modules(R); its Python representation is not an
    additional category in the mathematical graph.
    """

    def __init__(self, upper_ranks, lower_ranks, **rest) -> None:
        self._upper_ranks = upper_ranks
        self._lower_ranks = lower_ranks
        super().__init__(**rest)

    def construction(self):
        r"""Return no functorial construction.

        Sage's coercion walks this when it looks for an action of a ring on
        this module; a tensor module is built from its rank vector, not from
        a construction functor applied to another parent.
        """
        return None

    def __reduce__(self):
        return (
            TensorModule,
            (self.base_ring(), self._upper_ranks, self._lower_ranks),
        )

    def _index_ranks(self) -> tuple:
        return self._upper_ranks + self._lower_ranks

    def tensor_shape(self):
        r"""Return the family assigning each index slot the rank of its module."""
        return index_rank_family(self._index_ranks())

    def tensor_type(self) -> ProductOfNaturalNumbers:
        r"""Return the type $(p, q)$ as a point of $\mathbb N^2$ (`CON-15`)."""

        return (NN**2)((len(self._upper_ranks), len(self._lower_ranks)))

    def tensor_valence(self) -> ProductOfNaturalNumbers:
        return self.tensor_type()

    def _upper_index_ranks(self) -> tuple:
        return self._upper_ranks

    def _lower_index_ranks(self) -> tuple:
        return self._lower_ranks

    def _index_modules_for(self, ranks):
        def free_of_rank(rank):
            if rank == Infinity:
                return self.base_ring().free_module(NN)
            return self.base_ring().free_module(int(rank))

        slots = Sets.Δ[len(ranks) - 1]
        return indexed_family(
            slots,
            lambda slot: free_of_rank(ranks[int(slot)]),
            name="Tensor-index modules",
        )

    def contravariant_index_modules(self):
        r"""Return the family \(M_1,\ldots,M_p\) of contravariant index modules."""
        return self._index_modules_for(self._upper_ranks)

    def covariant_index_modules(self):
        r"""Return the family \(N_1,\ldots,N_q\) of covariant index modules."""
        return self._index_modules_for(self._lower_ranks)

    def index_modules(self):
        r"""Return the two variance module families as an object of ``Objects x Objects``."""
        return _owned_object_pair(
            self.contravariant_index_modules(),
            self.covariant_index_modules(),
        )

    @staticmethod
    def _index_generating_sets(modules):
        return indexed_family(
            modules.index_set(),
            lambda slot: modules[slot].module_generating_set(),
            name="Tensor-index generating sets",
        )

    def contravariant_index_generating_sets(self):
        r"""Return the generating-set family of the contravariant index modules."""
        return self._index_generating_sets(self.contravariant_index_modules())

    def covariant_index_generating_sets(self):
        r"""Return the generating-set family of the covariant index modules."""
        return self._index_generating_sets(self.covariant_index_modules())

    def tensor_indices(self):
        r"""Return the two variance generating-set families as an object of ``Objects x Objects``."""
        return _owned_object_pair(
            self.contravariant_index_generating_sets(),
            self.covariant_index_generating_sets(),
        )

    def _element_constructor_(self, entries):
        r"""Admit a tensor of this module, or its row-major component sequence."""
        if element_parent(entries) is self:
            return entries
        shape = self._index_ranks()
        assert Infinity not in shape, (
            "an infinite-rank tensor space has no component array"
        )
        entries = tuple(entries)
        if len(entries) != prod(shape):
            raise ValueError(
                f"shape {shape} requires {prod(shape)} "
                f"components, got {len(entries)}"
            )
        ring = self.base_ring()
        return self.element_class(self, tuple(ring(entry) for entry in entries))

    def zero(self):
        assert Infinity not in self._index_ranks(), (
            "an infinite-rank tensor space has no component array"
        )
        zero = self.base_ring().zero()
        return self.element_class(
            self,
            tuple(zero for _ in range(prod(self._index_ranks()))),
        )

    def _repr_(self) -> str:
        session, _tex = _tensor_space_session_and_latex(
            self.base_ring(), self._upper_ranks, self._lower_ranks
        )
        return session

    def _latex_(self) -> str:
        _session, tex = _tensor_space_session_and_latex(
            self.base_ring(), self._upper_ranks, self._lower_ranks
        )
        return tex


def _is_coordinate_tensor(value, ring):
    r"""Recognize this private tensor engine at the component-conversion boundary.

    Declared engine adapter (``OWN-06``): this is representation dispatch for
    the private coordinate-tensor realization, not mathematical membership.
    Gram pairing rules and component tensors use the same module engine.
    This is representation dispatch, not a new mathematical category.
    """
    parent = element_parent(value)
    return isinstance(parent, _CoordinateTensorModule) and parent.base_ring() is ring


def TensorModule(base_ring, upper_ranks, lower_ranks):
    r"""Return the module of type-$(p,q)$ tensors with the given index ranks.

    If every contravariant index is a copy of \(M=R^n\) and every covariant
    index is a copy of \(M\), this is
    \(M^{\otimes p}\otimes(M^*)^{\otimes q}\).  A type-$(0,q)$ tensor
    at infinite rank is an element of \((M^{\otimes q})^*\), not of
    \((M^*)^{\otimes q}\).

    The module on this rank vector, built by Modules(base_ring) through its
    private component engine: equal rank vectors over one ring give the same
    module.

    EXAMPLES::

        sage: from dzack_research.preamble.tensors import tensor
        sage: G = tensor(ZZ, (), (2, 2), [[0, 1], [1, 0]])
        sage: G.parent()
        ((ZZ^2)*)^{⊗2}
        sage: G.tensor_type()
        (0, 2)
        sage: latex(G.parent())
        ((\mathbb{Z}^{2})^{*})^{\otimes 2}
    """
    if base_ring not in _Rings:
        raise TypeError(f"the tensor base must be a preamble ring, got {base_ring}")
    return _tensor_module_on(
        base_ring,
        tuple(_normalized_rank(rank) for rank in upper_ranks),
        tuple(_normalized_rank(rank) for rank in lower_ranks),
    )


@cached_function
def _tensor_module_on(base_ring, upper_ranks, lower_ranks):
    r"""Build the tensor module on a normalized rank vector through its category's entry."""
    return _object_of(
        Modules(base_ring),
        _engine=(Modules(base_ring), _CoordinateTensorModule, _CoordinateTensor),
        base_ring=base_ring,
        upper_ranks=upper_ranks,
        lower_ranks=lower_ranks,
    )


def _mixed_tensor_valence(valence) -> ProductOfNaturalNumbers:
    r"""Normalize one bidegree ``(p,q)`` of the mixed tensor algebra."""
    return (NN**2)(valence)


class MixedTensorAlgebraElement(GradedDirectSumElement):
    r"""A finite-support sum of homogeneous mixed tensors."""

    def valences(self):
        r"""Return the finite set of bidegrees with nonzero component."""
        return finite_ordered_set(tuple(self._components))

    def _repr_(self):
        if not self._components:
            return "0"
        return " + ".join(
            f"[{valence[0]},{valence[1]}]({component})"
            for valence, component in self._components.items()
        )


class _MixedTensorDirectSum(_FramedDirectSumOfModules):
    r"""The canonical direct sum underlying one mixed tensor algebra."""

    def __init__(self, mixed_tensor_module, **rest) -> None:
        self._mixed_tensor_module = mixed_tensor_module
        super().__init__(**rest)

    def module(self):
        return self._mixed_tensor_module

    def dual_module(self):
        r"""Return the linear dual ``M^*`` used by the covariant factor."""
        return self.module().dual_module()

    def vector_tensor_algebra(self):
        r"""Return ``T(M)``, the contravariant tensor-algebra factor."""
        return self.module().tensor_algebra()

    def covector_tensor_algebra(self):
        r"""Return ``T(M^*)``, the covariant tensor-algebra factor."""
        return self.dual_module().tensor_algebra()

    def homogeneous_piece(self, valence):
        r"""Return the tensor module of bidegree ``valence``."""
        return self.graded_piece(valence)

    def include(self, tensor_element):
        r"""Include one live homogeneous tensor in its bidegree."""
        if not _is_coordinate_tensor(tensor_element, self.base_ring()):
            raise TypeError(
                f"mixed tensor inclusion requires a tensor over {self.base_ring()}"
            )
        valence = _mixed_tensor_valence(tensor_element.tensor_valence())
        expected = self.homogeneous_piece(valence)
        if tensor_element.parent() is not expected:
            raise ValueError("the tensor does not use the selected frame rank of this mixed algebra")
        return self.from_component(valence, tensor_element)

    def _element_constructor_(self, value):
        r"""Admit an element: one of this algebra, a homogeneous tensor, a scalar, or components by bidegree.

        Components by bidegree are literal data, a Python mapping from
        bidegree to homogeneous tensor.
        """
        ring = self.base_ring()
        match value:
            case _ if element_parent(value) is self:
                return value
            case _ if _is_coordinate_tensor(value, ring):
                return self.include(value)
            case _ if value in ring:
                scalar_tensor = self.homogeneous_piece((0, 0))((ring(value),))
                return self.from_component((0, 0), scalar_tensor)
            case dict():
                return self.from_components(value)
            case _ if element_parent(value) in Modules(ring):
                return super()._element_constructor_(value)
            case _:
                raise TypeError(f"{value!r} does not define an element of {self}")

    def _module_with_structure(self, categories, construction_data):
        return super()._module_with_structure(
            categories,
            {"mixed_tensor_module": self.module(), **construction_data},
        )

    def _direct_sum_realization(self):
        return _MixedTensorDirectSum, MixedTensorAlgebraElement

    def _repr_(self) -> str:
        return f"Mixed tensor algebra T({self.module()}) tensor T({self.module()}^*)"


def _mixed_tensor_algebra(module):
    r"""Return ``T(M) tensor T(M^*)`` through the graded-module and algebra owners."""
    from dzack_research.preamble.categories.algebras.algebras import _algebra_on_module
    from dzack_research.preamble.categories.algebras.graded_algebras import (
        GradedAlgebras,
        _graded_multiplication_from_components,
    )

    rank = module.module_rank()
    assert rank.is_finite(), (
        "the coordinate mixed tensor algebra is represented for a module of finite rank"
    )
    ring = _own_ring(module.base_ring())
    size = int(rank)
    bigrades = NN**2
    pieces = indexed_family(
        bigrades,
        lambda valence: TensorModule(
            ring,
            (size,) * int(valence[0]),
            (size,) * int(valence[1]),
        ),
        name="Mixed tensor homogeneous pieces",
    )
    graded = _direct_sum_of_modules(
        ring,
        bigrades,
        pieces,
        extra_categories=(FramedModules(ring),),
        construction_data={"mixed_tensor_module": module},
        _realization=(_MixedTensorDirectSum, MixedTensorAlgebraElement),
    )

    def component_product(left_degree, left, right_degree, right):
        target = graded.graded_piece(
            graded.combine_degrees(left_degree, right_degree)
        )
        product = left.tensor_product(right)
        match product.parent() is target:
            case True:
                pass
            case False:
                raise ValueError(
                    "mixed tensor multiplication changed the selected homogeneous tensor parent"
                )
        return product

    multiplication = _graded_multiplication_from_components(
        graded,
        component_product,
    )
    degree_zero = graded.graded_piece((0, 0))
    unit = graded.from_component((0, 0), degree_zero((ring.one(),)))
    return _algebra_on_module(
        graded,
        multiplication,
        placement=(GradedAlgebras(ring, bigrades),),
        unit=unit,
        law_decisions={"associativity": True, "unit": True, "grading": True},
    )


def _is_rank(value) -> bool:
    r"""Whether ``value`` names the rank of a finite tensor slot.

    A rank is a natural number, or a finite cardinal -- the rank a module
    reports is a cardinal.  Decided by placement in ``NN`` and in
    ``Cardinalities()``.
    """
    if value in NN:
        return True
    return value in Cardinalities() and value.is_finite()


def _rank_tuple(ranks) -> tuple[int, ...]:
    r"""Normalize one side of the tensor rank vector.

    A single rank is the one-index shorthand used by ``matrix(R, p, q, data)``;
    a family of ranks is the general tensor syntax.
    """
    if _is_rank(ranks):
        return (int(ranks),)
    dimensions = tuple(ranks)
    if not all(_is_rank(rank) for rank in dimensions):
        raise ValueError(f"tensor index ranks must be nonnegative: {dimensions}")
    return tuple(int(rank) for rank in dimensions)


def _coordinate_tensor(
    base_ring: Parent,
    upper_ranks: tuple[int, ...],
    lower_ranks: tuple[int, ...],
    components,
) -> Tensor:
    r"""Construct a coordinate tensor that is not a Sage vector or matrix."""
    shape = upper_ranks + lower_ranks
    nested_shape = _component_shape(components)
    if nested_shape:
        if nested_shape == shape:
            entries = _flatten(components, shape)
        elif nested_shape == (prod(shape),):
            entries = tuple(components)
        else:
            raise ValueError(
                f"tensor components have shape {nested_shape}, expected {shape}"
            )
    else:
        entries = tuple(components)
    return TensorModule(base_ring, upper_ranks, lower_ranks)(entries)


class _TensorConstructor:
    r"""General tensor constructor with variance encoded in the rank vectors.

    ``tensor.vector(R, data)``, ``tensor.covector(R, data)``, and
    ``tensor.matrix(R, data)`` are small typed conveniences over the main
    ``tensor(R, ps, qs, data)`` call.  They accept owned rings and mathematical
    component data only; Sage constructor/storage compatibility is not public
    API.

    The main call is ``tensor(R, ps, qs, data)``.  ``ps`` lists upper-index
    dimensions and ``qs`` lower-index dimensions.  Hence vectors and covectors
    are different constructor calls even though both have one index.
    """

    vector = _TensorVectorConstructor()
    covector = _TensorCovectorConstructor()
    matrix = _TensorMatrixConstructor()

    def from_matrix(self, matrix):
        r"""Interpret a finite matrix Hom element as a type-``(1,1)`` tensor."""

        parent = matrix.parent()
        ring = parent.base_ring()
        if parent not in MatrixSpaces(ring):
            raise TypeError("tensor.from_matrix expects a finite matrix Hom element")
        return self(
            ring,
            (parent.nrows(),),
            (parent.ncols(),),
            matrix.list(),
        )

    def from_morphism(self, morphism):
        r"""Interpret a finite framed-free module morphism as a type-``(1,1)`` tensor.

        The morphism's own ``matrix()`` states and asserts that its endpoints
        are finitely generated framed free modules.
        """
        return self.from_matrix(morphism.matrix())

    def __call__(
        self,
        base_ring: Parent,
        upper_ranks,
        lower_ranks,
        components=None,
        **kwds,
    ) -> Tensor:
        r"""Construct a tensor of type \((\lvert\mathrm{ps}\rvert,\lvert\mathrm{qs}\rvert)\).

        EXAMPLES::

            sage: from dzack_research.preamble.tensors import tensor
            sage: G = tensor(ZZ, (), (2, 2), [[0, 1], [1, 0]])
            sage: G.tensor_type()
            (0, 2)
            sage: G.parent()
            ((ZZ^2)*)^{⊗2}
            sage: tensor(ZZ, (), (3,), [1, 2, 3]).parent()
            (ZZ^3)*
            sage: tensor(ZZ, (2, 3), (), range(6)).parent()
            ZZ^2 ⊗ ZZ^3
        """
        if base_ring not in _Rings:
            raise TypeError(f"the tensor base must be a preamble ring, got {base_ring}")
        ps = _rank_tuple(upper_ranks)
        qs = _rank_tuple(lower_ranks)

        if kwds:
            names = ", ".join(sorted(kwds))
            raise TypeError(f"a tensor has one storage; {names} is a Sage storage option")
        if components is None:
            zero = base_ring.zero()
            components = tuple(zero for _ in range(prod(ps + qs)))
        return _coordinate_tensor(base_ring, ps, qs, components)


tensor = _TensorConstructor()


def _restore_tensor(
    base_ring: Parent,
    upper_ranks: tuple[int, ...],
    lower_ranks: tuple[int, ...],
    components,
) -> Tensor:
    return tensor(base_ring, upper_ranks, lower_ranks, components)
