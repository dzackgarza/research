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
"""

from functools import singledispatch
from math import prod

from sage.matrix.constructor import matrix as _sage_matrix
from sage.misc.latex import latex
from sage.modules.free_module_element import vector as _sage_vector
from sage.rings.infinity import Infinity
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE, richcmp
from sage.structure.unique_representation import UniqueRepresentation

from dzack_research.preamble.categories.modules.graded_direct_sums import (
    GradedDirectSumElement,
    GradedDirectSumModule,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    MatrixSpaces,
    Modules,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    _engine_matrix as _engine_module_matrix,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedRings,
    _engine_element,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily
from dzack_research.preamble.categories.sets.set_categories import NN, Sets
from dzack_research.static_types import ProductOfNaturalNumbers

_Rings = OwnedRings()


def index_rank_family(ranks):
    r"""Return the family \(i\mapsto\) rank of slot \(i\), for \(i\in\Delta[k-1]\)."""

    entries = tuple(cardinal(rank) for rank in ranks)
    return IndexedFamily(
        Sets.Δ[len(entries) - 1],
        lambda index: entries[int(index)],
        name=f"Index ranks ({', '.join(str(entry) for entry in entries)})",
    )


def _owned_set_pair(first, second):
    r"""Return ``(first, second)`` as an object of the categorical product ``Set x Set``."""
    from dzack_research.preamble.categories.abstract_categories.cat import Cat

    return Cat().product((Sets(), Sets()))(first, second)


def _tensor_richcmp(left, right, op):
    r"""Compare finite tensors by variance, shape, and components.

    Tensor implementations may use different storage classes.  Equality is a
    mathematical comparison in one tensor space, not a storage-class test.
    """
    if not isinstance(right, Tensor):
        if op == op_EQ:
            return False
        if op == op_NE:
            return True
        return NotImplemented
    if (
        left.tensor_valence() != right.tensor_valence()
        or left.tensor_shape() != right.tensor_shape()
    ):
        if op == op_EQ:
            return False
        if op == op_NE:
            return True
        # Tensors of different variance or shape lie in different spaces, and
        # there is no order between those spaces to report.
        return NotImplemented
    return richcmp(tuple(left.list()), tuple(right.list()), op)

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


def _engine_if_ring(value):
    r"""Cross an owned ring to Sage's computation parent; leave other values."""
    try:
        return _engine_ring(_own_ring(value))
    except TypeError:
        return value


def _engine_argument(value):
    r"""Cross a ring or an already-owned tensor to Sage's computation object.

    A tensor is legitimate component data for another tensor constructor, so
    the constructors accept one and cross it here rather than at each site.
    """
    if isinstance(value, Tensor):
        if value.tensor_order() == 1:
            return _engine_vector(
                value.base_ring(),
                [_engine_element(value.base_ring(), entry) for entry in value.list()],
            )
        if value.tensor_order() == 2:
            return _engine_component_matrix(value)
        raise TypeError(
            f"a tensor of shape {value._index_ranks()} is not component data for "
            "a vector or a matrix"
        )
    parent = getattr(value, "parent", lambda: None)()
    if parent is not None:
        try:
            if parent in OwnedRings():
                return _engine_element(parent, value)
        except (TypeError, ValueError, AttributeError):
            pass
    return _engine_if_ring(value)


def _engine_components(value):
    """Cross a component array of any depth to the engine.

    A component sequence carries owned ring elements, and Sage's constructors
    convert each entry against their own base ring.  Without crossing the
    entries the owned elements arrive intact and Sage reports that it cannot
    coerce them, so the crossing recurses through rows as well as vectors.
    """
    if isinstance(value, (list, tuple)):
        return [_engine_components(entry) for entry in value]
    return _engine_argument(value)


def _engine_vector(*args, **kwds):
    return _sage_vector(*tuple(_engine_components(arg) for arg in args), **kwds)


def _engine_matrix(*args, **kwds):
    args = tuple(_engine_components(arg) for arg in args)
    if "base_ring" in kwds:
        kwds = dict(kwds)
        kwds["base_ring"] = _engine_if_ring(kwds["base_ring"])
    return _sage_matrix(*args, **kwds)


class Tensor:
    r"""A tensor of type $(p,q)$.

    A type-$(p,q)$ tensor on a module \(M\) is an element of
    \(M^{\otimes p}\otimes(M^*)^{\otimes q}\).  When the index modules
    differ, it is an element of the corresponding mixed tensor product.
    At infinite rank a type-$(0,2)$ pairing lives in
    \((M\otimes M)^*\), not in \((M^*)^{\otimes 2}\).

    This class carries no storage.  Every tensor, of every valence, is an
    element of a :class:`TensorModule` over the owned base ring.
    """

    __slots__ = ()

    def _index_ranks(self) -> tuple:
        r"""Return the index ranks as private plumbing for the slot families."""
        assert False, "a tensor supplies the ranks of its indices"

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
        r"""Return the type $(p,q)$; synonym of :meth:`tensor_type`."""
        assert False, "a tensor supplies its type (p, q)"

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
        \((R^n)^{\otimes p}\otimes((R^n)^*)^{\otimes q}\).
        """
        return TensorModule(self.base_ring(), self._upper_index_ranks(), self._lower_index_ranks())

    def contravariant_index_modules(self):
        r"""Return the family of contravariant index modules."""
        return self.tensor_space().contravariant_index_modules()

    def covariant_index_modules(self):
        r"""Return the family of covariant index modules."""
        return self.tensor_space().covariant_index_modules()

    def index_modules(self):
        r"""Return the contravariant/covariant module families as an object of ``Set x Set``."""
        return self.tensor_space().index_modules()

    def contravariant_index_generating_sets(self):
        r"""Return the selected generating sets of the contravariant index modules."""
        return self.tensor_space().contravariant_index_generating_sets()

    def covariant_index_generating_sets(self):
        r"""Return the selected generating sets of the covariant index modules."""
        return self.tensor_space().covariant_index_generating_sets()

    def tensor_indices(self):
        r"""Return the two variance-indexed generating-set families as an object of ``Set x Set``."""
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

    def is_equal_tensor(self, other) -> bool:
        r"""Return whether ``other`` is the same tensor mathematically.

        This deliberately ignores the concrete storage parent.  Tensor spaces
        built from equal owned/engine ring facades can have distinct Sage
        parents while representing the same variance, ranks, and components.
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
        return all(left == right for left, right in zip(self.list(), other.list(), strict=True))

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
        if not isinstance(other, Tensor):
            raise TypeError("tensor contraction pairs two represented tensors")
        if _engine_ring(other.base_ring()) != _engine_ring(self.base_ring()):
            raise TypeError("tensor contraction requires one base ring")
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
            if not isinstance(vector, Tensor) or vector.tensor_valence() != (NN**2)((1, 0)):
                raise TypeError("covariant tensor contraction takes contravariant vectors")
            if vector._upper_index_ranks() != (rank,):
                raise ValueError(
                    f"cannot contract covariant rank {rank} with vector ranks {vector._upper_index_ranks()}"
                )
            if _engine_ring(vector.base_ring()) != _engine_ring(self.base_ring()):
                raise TypeError("tensor contraction requires one base ring")
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
        if not isinstance(other, Tensor):
            raise TypeError("tensor_product requires another represented tensor")
        if _engine_ring(other.base_ring()) != _engine_ring(self.base_ring()):
            raise TypeError("a tensor product requires one base ring")
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
        coefficients = {}
        for raised in range(rank):
            for contracted in range(rank):
                try:
                    coefficients[raised, contracted] = ring._from_engine_element(
                        inverse[raised, contracted]
                    )
                except (TypeError, ValueError) as error:
                    raise ValueError(
                        "raising an index over this ring requires the inverse Gram entries in the base ring"
                    ) from error

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
        matrices are only an implementation of this transport.
        """
        if self._upper_index_ranks():
            raise TypeError("pullback is defined here for a covariant tensor")
        try:
            matrix = morphism.matrix()
        except (AttributeError, NotImplementedError) as error:
            raise TypeError(
                "tensor pullback requires an owned linear morphism with finite framed-free endpoints"
            ) from error

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
    r"""Materialize a two-index tensor as a private Sage matrix.

    This is an engine crossing, not a public mathematical representation.
    Public code keeps the tensor's variance; algorithms that genuinely require
    Sage's matrix backend cross here and should return to tensors before
    exposing coordinate data again.
    """
    if not isinstance(value, Tensor) or value.tensor_order() != 2:
        raise TypeError("engine matrix materialization requires a two-index tensor")
    rows, columns = value._index_ranks()
    if rows == Infinity or columns == Infinity:
        raise ValueError("an infinite tensor has no finite engine matrix")
    return _engine_matrix(
        value.base_ring(),
        rows,
        columns,
        [
            _engine_element(value.base_ring(), value[i, j])
            for i in range(rows)
            for j in range(columns)
        ],
    )


def _engine_component_vector(value):
    r"""Materialize a type-``(1,0)`` tensor as a private Sage vector."""
    if not isinstance(value, Tensor) or value.tensor_valence() != (NN**2)((1, 0)):
        raise TypeError("engine vector materialization requires a type-(1,0) tensor")
    if value._index_ranks()[0] == Infinity:
        raise ValueError("an infinite vector tensor has no finite engine vector")
    return _engine_vector(
        value.base_ring(),
        [_engine_element(value.base_ring(), entry) for entry in value.list()],
    )


def _tensor_vector_from_native(native) -> Tensor:
    r"""Cross one private Sage vector back into the owned tensor universe."""
    base = _own_ring(native.base_ring())
    entries = tuple(base._from_engine_element(entry) for entry in native.list())
    return tensor(base, (int(native.degree()),), (), entries)


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
        if isinstance(components, int):
            entries = tuple(base_ring.zero() for _ in range(components))
        elif isinstance(components, dict):
            size = 0 if not components else max(int(index) for index in components) + 1
            entries = tuple(
                components.get(index, base_ring.zero()) for index in range(size)
            )
        else:
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
            if isinstance(components, Tensor):
                if components.tensor_order() != 2:
                    raise TypeError("a matrix tensor has two indices")
                # Reinterpretation: the two index ranks are read off, and the
                # result is the type-(1,1) tensor this constructor makes.  The
                # input's own variance does not survive, which is the whole
                # content of reading its components as a matrix.
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
    r"""A coordinate tensor that is not Sage's vector or matrix specialization."""

    def __init__(self, parent: Parent, entries: tuple) -> None:
        self._entries = entries
        ModuleElement.__init__(self, parent)

    def _index_ranks(self) -> tuple:
        return self.parent()._index_ranks()

    def tensor_valence(self) -> ProductOfNaturalNumbers:
        return self.parent().tensor_valence()

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
        from sage.matrix.constructor import matrix as sage_matrix
        from sage.misc.latex import latex as sage_latex

        shape = self._index_ranks()
        if len(shape) == 2:
            rows, columns = shape
            return str(
                sage_latex(
                    sage_matrix(
                        _engine_if_ring(self.base_ring()),
                        rows,
                        columns,
                        [
                            _engine_element(self.base_ring(), self[i, j])
                            for i in range(rows)
                            for j in range(columns)
                        ],
                    )
                )
            )
        return str(sage_latex(self.components()))

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

    def change_ring(self, ring):
        r"""Change scalar coefficients without changing tensor variance."""
        target = ring
        return tensor(
            target,
            self._upper_index_ranks(),
            self._lower_index_ranks(),
            _nested(
                tuple(target(entry) for entry in self._entries),
                self._index_ranks(),
            ),
        )

    def __getitem__(self, index: tuple[int, ...]):
        try:
            len(index)
        except TypeError:
            index = (index,)
        if len(index) != self.tensor_order():
            raise IndexError(
                f"a tensor of shape {self._index_ranks()} takes "
                f"{self.tensor_order()} indices, got {len(index)}"
            )
        offset = 0
        for position, dimension in zip(index, self._index_ranks()):
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
        if other in self.base_ring():
            return self._lmul_(self.base_ring()(other))
        if (
            len(self._upper_index_ranks()) >= 2
            and not self._lower_index_ranks()
            and isinstance(other, Tensor)
            and other.tensor_valence() == (NN**2)((0, 1))
        ):
            if _engine_ring(other.base_ring()) != _engine_ring(self.base_ring()):
                raise TypeError("tensor contraction requires one base ring")
            if self._upper_index_ranks()[-1] != other._lower_index_ranks()[0]:
                raise ValueError(
                    f"cannot contract ranks {self._upper_index_ranks()[-1]} and "
                    f"{other._lower_index_ranks()[0]}"
                )
            output_upper = self._upper_index_ranks()[:-1]
            output_shape = output_upper
            contracted_rank = self._upper_index_ranks()[-1]

            from itertools import product as cartesian_product

            positions = (
                tuple(cartesian_product(*(range(rank) for rank in output_shape)))
                if output_shape
                else ((),)
            )
            entries = tuple(
                sum(
                    (
                        self[position + (index,)] * other[index]
                        for index in range(contracted_rank)
                    ),
                    self.base_ring().zero(),
                )
                for position in positions
            )
            if not output_shape:
                return entries[0]
            return tensor(
                self.base_ring(),
                output_upper,
                (),
                _nested(entries, output_shape),
            )
        if isinstance(other, Tensor) and other.tensor_valence() == (NN**2)((1, 0)):
            if _engine_ring(other.base_ring()) != _engine_ring(self.base_ring()):
                raise TypeError("tensor contraction requires one base ring")
            if not self._lower_index_ranks():
                raise TypeError("a tensor with no covariant index cannot act on a vector")
            if self._lower_index_ranks()[-1] != other._upper_index_ranks()[0]:
                raise ValueError(
                    f"cannot contract ranks {self._lower_index_ranks()[-1]} and "
                    f"{other._upper_index_ranks()[0]}"
                )

            # Multiplication contracts the rightmost covariant index.  Thus a
            # bilinear form G in M* tensor M* acts on v in M as G*v in M*,
            # with components (G*v)_i = sum_j G_{ij} v_j.  No row-vector or
            # transpose convention enters the public tensor calculus.
            output_upper = self._upper_index_ranks()
            output_lower = self._lower_index_ranks()[:-1]
            output_shape = output_upper + output_lower
            contracted_rank = self._lower_index_ranks()[-1]

            from itertools import product as cartesian_product

            positions = tuple(
                cartesian_product(*(range(rank) for rank in output_shape))
            ) if output_shape else ((),)
            entries = tuple(
                sum(
                    (
                        self[position + (index,)] * other[index]
                        for index in range(contracted_rank)
                    ),
                    self.base_ring().zero(),
                )
                for position in positions
            )
            if not output_shape:
                return entries[0]
            return tensor(
                self.base_ring(),
                output_upper,
                output_lower,
                _nested(entries, output_shape),
            )
        if (
            self.tensor_valence() == (NN**2)((1, 1))
            and isinstance(other, Tensor)
            and other.tensor_valence() == (NN**2)((1, 1))
        ):
            if _engine_ring(other.base_ring()) != _engine_ring(self.base_ring()):
                raise TypeError("tensor contraction requires one base ring")
            if self._lower_index_ranks() != other._upper_index_ranks():
                raise ValueError(
                    f"cannot contract ranks {self._lower_index_ranks()} and "
                    f"{other._upper_index_ranks()}"
                )
            # In U tensor V* tensor V tensor W*, contract the adjacent V*, V
            # factors.  Under Hom(V,U) = U tensor V* this agrees with map
            # composition, but its owner here is tensor evaluation.
            rows = self._upper_index_ranks()[0]
            inner = other._upper_index_ranks()[0]
            columns = other._lower_index_ranks()[0]
            entries = tuple(
                sum(
                    (self[i, k] * other[k, j] for k in range(inner)),
                    self.base_ring().zero(),
                )
                for i in range(rows)
                for j in range(columns)
            )
            return tensor(
                self.base_ring(),
                (rows,),
                (columns,),
                _nested(entries, (rows, columns)),
            )

        if self.tensor_valence() == (NN**2)((0, 1)):
            if _engine_ring(other.base_ring()) != _engine_ring(self.base_ring()):
                raise TypeError("tensor contraction requires one base ring")
            if other.tensor_valence() == (NN**2)((1, 0)):
                return self(other)
            if other.tensor_valence() == (NN**2)((1, 1)):
                # In V* tensor V tensor W*, evaluate the adjacent V*, V pair.
                if self._lower_index_ranks() != other._upper_index_ranks():
                    raise ValueError(
                        f"cannot contract ranks {self._lower_index_ranks()} and "
                        f"{other._upper_index_ranks()}"
                    )
                rows = self._lower_index_ranks()[0]
                columns = other._lower_index_ranks()[0]
                entries = tuple(
                    sum(
                        (self[i] * other[i, j] for i in range(rows)),
                        self.base_ring().zero(),
                    )
                    for j in range(columns)
                )
                return tensor(self.base_ring(), (), (columns,), entries)
        if isinstance(other, Tensor):
            raise TypeError(
                f"multiplication contracts the left tensor's rightmost covariant "
                f"index with the right tensor's first contravariant index; "
                f"type-{self.tensor_valence()} and type-{other.tensor_valence()} "
                f"do not meet that way"
            )
        raise TypeError(
            "there is no generic tensor multiplication; use a stated contraction, "
            "or tensor product"
        )

    def __rmul__(self, other):
        try:
            scalar = self.base_ring()(other)
        except (TypeError, ValueError):
            raise TypeError(
                "a tensor can only be multiplied by a scalar on the left"
            ) from None
        return self._rmul_(scalar)

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
    shape = tensor_value._index_ranks()
    ring = _engine_if_ring(tensor_value.base_ring())
    if len(shape) == 1:
        return repr(_engine_vector(ring, list(tensor_value.components())))
    if len(shape) == 2:
        rows, columns = shape
        return repr(
            _engine_matrix(
                ring,
                rows,
                columns,
                [tensor_value[i, j] for i in range(rows) for j in range(columns)],
            )
        )
    return repr(tensor_value.components())


class TensorModule(UniqueRepresentation, Parent):
    r"""The module of type-$(p,q)$ tensors with the given index ranks.

    If every contravariant index is a copy of \(M=R^n\) and every covariant
    index is a copy of \(M\), this is
    \(M^{\otimes p}\otimes(M^*)^{\otimes q}\).  A type-$(0,q)$ tensor
    at infinite rank is an element of \((M^{\otimes q})^*\), not of
    \((M^*)^{\otimes q}\).

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

    Element = _CoordinateTensor

    @staticmethod
    def __classcall__(cls, base_ring, upper_ranks, lower_ranks):
        def normalize(rank):
            return Infinity if rank == Infinity else int(rank)

        if base_ring not in _Rings:
            raise TypeError(f"the tensor base must be a preamble ring, got {base_ring}")
        return UniqueRepresentation.__classcall__(
            cls,
            base_ring,
            tuple(normalize(rank) for rank in upper_ranks),
            tuple(normalize(rank) for rank in lower_ranks),
        )

    def __init__(
        self,
        base_ring: Parent,
        upper_ranks: tuple[int, ...],
        lower_ranks: tuple[int, ...],
    ) -> None:
        self._upper_ranks = tuple(upper_ranks)
        self._lower_ranks = tuple(lower_ranks)

        Parent.__init__(self, base=base_ring, category=Modules(base_ring))

    def construction(self):
        r"""Return no functorial construction.

        Sage's coercion walks this when it looks for an action of a ring on
        this module; a tensor module is built from its rank vector, not from
        a construction functor applied to another parent.
        """
        return None

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
        from sage.rings.semirings.non_negative_integer_semiring import NN

        def free_of_rank(rank):
            if rank == Infinity:
                return self.base_ring().free_module(NN)
            return self.base_ring().free_module(int(rank))

        slots = Sets.Δ[len(ranks) - 1]
        return FiniteOrderedSets().from_indexed(
            slots,
            lambda slot: free_of_rank(ranks[int(slot)]),
        )

    def contravariant_index_modules(self):
        r"""Return the family \(M_1,\ldots,M_p\) of contravariant index modules."""
        return self._index_modules_for(self._upper_ranks)

    def covariant_index_modules(self):
        r"""Return the family \(N_1,\ldots,N_q\) of covariant index modules."""
        return self._index_modules_for(self._lower_ranks)

    def index_modules(self):
        r"""Return the two variance module families as an object of ``Set x Set``."""
        return _owned_set_pair(
            self.contravariant_index_modules(),
            self.covariant_index_modules(),
        )

    @staticmethod
    def _index_generating_sets(modules):
        return FiniteOrderedSets().from_indexed(
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
        r"""Return the two variance generating-set families as an object of ``Set x Set``."""
        return _owned_set_pair(
            self.contravariant_index_generating_sets(),
            self.covariant_index_generating_sets(),
        )

    def _element_constructor_(self, entries: tuple) -> _CoordinateTensor:
        shape = self._index_ranks()
        assert Infinity not in shape, (
            "an infinite-rank tensor space has no component array"
        )
        if len(entries) != prod(shape):
            raise ValueError(
                f"shape {shape} requires {prod(shape)} "
                f"components, got {len(entries)}"
            )
        ring = self.base_ring()
        return self.element_class(self, tuple(ring(entry) for entry in entries))

    def zero(self) -> _CoordinateTensor:
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


def _mixed_tensor_valence(valence) -> ProductOfNaturalNumbers:
    r"""Normalize one bidegree ``(p,q)`` of the mixed tensor algebra."""
    return (NN**2)(valence)


class MixedTensorAlgebraElement(GradedDirectSumElement):
    r"""A finite-support sum of homogeneous mixed tensors."""

    def valences(self):
        r"""Return the finite set of bidegrees with nonzero component."""
        return finite_ordered_set(tuple(self._components))

    def _mul_(self, other):
        if other.parent() is not self.parent():
            return NotImplemented
        return self.parent().multiply(self, other)

    def _repr_(self):
        if not self._components:
            return "0"
        return " + ".join(
            f"[{valence[0]},{valence[1]}]({component})"
            for valence, component in self._components.items()
        )


class MixedTensorAlgebraParent(GradedDirectSumModule):
    r"""The bigraded algebra ``T(M) tensor T(M^*)`` of a finite framed module.

    The current tensor owner realizes each homogeneous piece in the selected
    frame of ``M``.  This parent adds only the finite-support direct sum across
    bidegrees; homogeneous tensor arithmetic remains owned by
    :class:`TensorModule` and :meth:`Tensor.tensor_product`.
    """

    Element = MixedTensorAlgebraElement

    def __init__(self, module) -> None:
        from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras

        rank = module.module_rank()
        if not rank.is_finite():
            raise TypeError("the coordinate mixed tensor algebra currently requires finite rank")
        self._module = module
        self._base_ring = _own_ring(module.base_ring())
        self._rank = int(rank)
        self._preamble_algebra_base_ring = self._base_ring
        self._preamble_algebra_is_commutative = self._rank <= 1
        bigrades = NN**2
        GradedDirectSumModule.__init__(
            self,
            self._base_ring,
            lambda valence: TensorModule(
                self._base_ring,
                (self._rank,) * int(valence[0]),
                (self._rank,) * int(valence[1]),
            ),
            name=f"Mixed tensor algebra T({module}) tensor T({module}^*)",
            degree_index_set=bigrades,
            grading_monoid=bigrades,
            extra_categories=(GradedAlgebras(self._base_ring, bigrades),),
        )

    def module(self):
        return self._module

    def dual_module(self):
        r"""Return the linear dual ``M^*`` used by the covariant factor."""
        return self.module().dual_module()

    def vector_tensor_algebra(self):
        r"""Return ``T(M)``, the contravariant tensor-algebra factor."""
        return self.module().tensor_algebra()

    def covector_tensor_algebra(self):
        r"""Return ``T(M^*)``, the covariant tensor-algebra factor."""
        return self.dual_module().tensor_algebra()

    def algebra_base_ring(self):
        return self._base_ring

    def homogeneous_piece(self, valence):
        r"""Return the tensor module of bidegree ``valence``."""
        return self.graded_piece(valence)

    def include(self, tensor_element):
        r"""Include one live homogeneous tensor in its bidegree."""
        if not isinstance(tensor_element, Tensor):
            raise TypeError("mixed tensor inclusion requires a represented tensor")
        if _own_ring(tensor_element.base_ring()) is not self.base_ring():
            raise ValueError("the tensor and mixed algebra require one base ring")
        valence = _mixed_tensor_valence(tensor_element.tensor_valence())
        expected = self.homogeneous_piece(valence)
        if tensor_element.parent() is not expected:
            raise ValueError("the tensor does not use the selected frame rank of this mixed algebra")
        return self.from_component(valence, tensor_element)

    def _element_constructor_(self, value):
        if isinstance(value, MixedTensorAlgebraElement):
            if value.parent() is self:
                return value
            raise TypeError("the element belongs to a different mixed tensor algebra")
        if isinstance(value, Tensor):
            return self.include(value)
        if isinstance(value, dict):
            return self.from_components(value)
        try:
            scalar = self.base_ring()(value)
        except (TypeError, ValueError) as error:
            raise TypeError(f"{value!r} does not define an element of {self}") from error
        scalar_tensor = self.homogeneous_piece((0, 0))((scalar,))
        return self.from_component((0, 0), scalar_tensor)

    def zero(self):
        return GradedDirectSumModule.zero(self)

    def one(self):
        return self(self.base_ring().one())

    def multiply(self, left, right):
        left = self(left)
        right = self(right)
        result = self.zero()
        for left_component in left.homogeneous_components().values():
            for right_component in right.homogeneous_components().values():
                product = left_component.tensor_product(right_component)
                result += self.include(product)
        return result

    def _repr_(self) -> str:
        return f"Mixed tensor algebra T({self.module()}) tensor T({self.module()}^*)"


def _tensor_module(
    base_ring: Parent,
    upper_ranks: tuple[int, ...],
    lower_ranks: tuple[int, ...],
) -> TensorModule:
    return TensorModule(base_ring, tuple(upper_ranks), tuple(lower_ranks))


def _is_dimension(value) -> bool:
    try:
        dimension = int(value)
    except (TypeError, ValueError, OverflowError):
        return False
    if dimension < 0:
        return False
    try:
        return value == dimension
    except (TypeError, ValueError):
        return False


def _rank_tuple(ranks) -> tuple[int, ...]:
    r"""Normalize one side of the tensor rank vector.

    An integer is the one-index shorthand used by ``matrix(R, p, q, data)``;
    tuples are the general tensor syntax.
    """
    if _is_dimension(ranks):
        return (int(ranks),)
    try:
        dimensions = tuple(ranks)
    except TypeError as error:
        raise TypeError(
            "tensor index ranks are tuples of nonnegative integers"
        ) from error
    if not all(_is_dimension(rank) for rank in dimensions):
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
    module = _tensor_module(base_ring, upper_ranks, lower_ranks)
    return module._element_constructor_(entries)


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
        r"""Interpret a finite framed-free module morphism as a type-``(1,1)`` tensor."""
        try:
            matrix = morphism.matrix()
        except (AttributeError, NotImplementedError) as error:
            raise TypeError(
                "tensor.from_morphism requires finite framed-free endpoints"
            ) from error
        return self.from_matrix(matrix)

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
