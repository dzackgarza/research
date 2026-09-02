r"""A tensor constructor extending Sage's ``vector`` and ``matrix`` constructors.

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
read Sage's complete constructor argument families, including the named
matrix-constructor namespace (``identity``, ``diagonal``, ``block``,
``random``, and the rest).  Sage's ``vector`` and ``matrix`` are the engine
that parses those arguments and infers the ring; what they return crosses
back to an owned tensor before any session sees it.
"""

from dzack_research.preamble.categories.rings import engine_ring as _engine_ring
from functools import singledispatch
from math import prod

from sage.matrix.constructor import matrix as _sage_matrix
from sage.misc.cachefunc import cached_function
from sage.misc.latex import latex
from sage.modules.free_module_element import vector as _sage_vector
from sage.rings.infinity import Infinity
from sage.rings.integer_ring import ZZ
from sage.structure.dynamic_class import dynamic_class
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE, richcmp
from sage.structure.unique_representation import UniqueRepresentation

from dzack_research.preamble.categories.rings.rings import (
    OwnedRings,
    engine_ring,
    own_ring,
)


_Rings = OwnedRings()


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
    left_key = (left.tensor_valence(), left.tensor_shape())
    right_key = (right.tensor_valence(), right.tensor_shape())
    if left_key != right_key:
        if op == op_EQ:
            return False
        if op == op_NE:
            return True
        return richcmp(left_key, right_key, op)
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
        return engine_ring(own_ring(value))
    except TypeError:
        return value


def _engine_argument(value):
    r"""Cross a ring or an already-owned tensor to Sage's computation object.

    A tensor is legitimate component data for another tensor constructor, so
    the constructors accept one and cross it here rather than at each site.
    """
    if isinstance(value, Tensor):
        if value.tensor_order() == 1:
            return _engine_vector(value.base_ring(), value.list())
        if value.tensor_order() == 2:
            return _engine_component_matrix(value)
        raise TypeError(
            f"a tensor of shape {value.tensor_shape()} is not component data for "
            "a vector or a matrix"
        )
    return _engine_if_ring(value)


def _engine_vector(*args, **kwds):
    return _sage_vector(*tuple(_engine_argument(arg) for arg in args), **kwds)


def _engine_matrix(*args, **kwds):
    args = tuple(_engine_argument(arg) for arg in args)
    if "base_ring" in kwds:
        kwds = dict(kwds)
        kwds["base_ring"] = _engine_if_ring(kwds["base_ring"])
    return _sage_matrix(*args, **kwds)


def _named_engine_matrix(constructor, *args, **kwds):
    args = tuple(_engine_argument(arg) for arg in args)
    if "base_ring" in kwds:
        kwds = dict(kwds)
        kwds["base_ring"] = _engine_if_ring(kwds["base_ring"])
    return constructor(*args, **kwds)


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

    def tensor_shape(self) -> tuple[int, ...]:
        r"""Return the rank of each tensor index."""
        assert False, "a tensor supplies the ranks of its indices"

    def upper_ranks(self) -> tuple[int, ...]:
        r"""Return the dimensions of the contravariant indices."""
        p, _q = self.tensor_type()
        return self.tensor_shape()[:p]

    def lower_ranks(self) -> tuple[int, ...]:
        r"""Return the dimensions of the covariant indices."""
        p, _q = self.tensor_type()
        return self.tensor_shape()[p:]

    def tensor_type(self) -> tuple[int, int]:
        r"""Return $(p,q)$: $p$ contravariant indices and $q$ covariant indices.

        A vector is type $(1,0)$.  A matrix, as a linear map, is type
        $(1,1)$.  A Gram tensor is type $(0,2)$.
        """
        return self.tensor_valence()

    def tensor_valence(self) -> tuple[int, int]:
        r"""Return the type $(p,q)$; synonym of :meth:`tensor_type`."""
        assert False, "a tensor supplies its type (p, q)"

    def tensor_order(self) -> int:
        r"""Return the number of indices."""
        return len(self.tensor_shape())

    def tensor_space(self):
        r"""Return the module of which this tensor is an element.

        For type $(p,q)$ on \(R^n\) this is
        \((R^n)^{\otimes p}\otimes((R^n)^*)^{\otimes q}\).
        """
        return TensorModule(self.base_ring(), self.upper_ranks(), self.lower_ranks())

    def index_modules(self):
        r"""Return the contravariant and covariant index modules.

        The first tuple is \(M_1,\ldots,M_p\); the second is
        \(N_1,\ldots,N_q\), so the tensor space is
        \(M_1\otimes\cdots\otimes M_p\otimes N_1^*\otimes\cdots\otimes N_q^*\).
        """
        return TensorModule(
            self.base_ring(), self.upper_ranks(), self.lower_ranks()
        ).index_modules()

    def tensor_indices(self):
        r"""Return the generating set of each index module.

        Integer coordinates \(0,\ldots,n-1\) when the index is \(R^n\).
        A pairing on a named free module uses that module's generating
        set, including \(\{e_i:i\in\mathbb N\}\) at infinite rank.
        """
        return TensorModule(
            self.base_ring(), self.upper_ranks(), self.lower_ranks()
        ).tensor_indices()

    def components(self):
        r"""Return the finite rectangular component array of this tensor."""
        shape = self.tensor_shape()
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
        shape = self.tensor_shape()
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
        if Infinity in self.tensor_shape():
            return object.__hash__(self)
        return hash(
            (self.tensor_valence(), self.tensor_shape(), tuple(self.list()))
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
        if engine_ring(self.base_ring()) != engine_ring(other.base_ring()):
            return False
        if Infinity in self.tensor_shape():
            return self is other
        return all(left == right for left, right in zip(self.list(), other.list(), strict=True))

    def rows(self):
        r"""Return component rows for a finite two-index tensor."""
        if self.tensor_order() != 2:
            raise TypeError("rows are defined only for a two-index tensor")
        return tuple(tuple(row) for row in self.components())

    def change_ring(self, ring):
        r"""Change coefficients without changing tensor variance."""
        return tensor(
            ring,
            self.upper_ranks(),
            self.lower_ranks(),
            self.components(),
        )

    def determinant(self):
        r"""Return the determinant of a square finite two-index tensor."""
        if self.tensor_order() != 2 or self.tensor_shape()[0] != self.tensor_shape()[1]:
            raise TypeError("determinant requires a square two-index tensor")
        return _engine_component_matrix(self).det()

    det = determinant

    def is_symmetric(self) -> bool:
        r"""Return whether a square two-index tensor is symmetric in its slots."""
        if self.tensor_order() != 2:
            raise TypeError("symmetry here is defined for a two-index tensor")
        rows, columns = self.tensor_shape()
        if rows != columns:
            return False
        return all(self[i, j] == self[j, i] for i in range(rows) for j in range(columns))

    def contract(self, *vectors):
        r"""Fully contract a purely covariant tensor with contravariant vectors."""
        if self.upper_ranks():
            raise TypeError("full contraction here requires a purely covariant tensor")
        if len(vectors) != len(self.lower_ranks()):
            raise TypeError(
                f"a type-{self.tensor_valence()} tensor takes "
                f"{len(self.lower_ranks())} vector arguments, got {len(vectors)}"
            )
        for rank, vector in zip(self.lower_ranks(), vectors, strict=True):
            if not isinstance(vector, Tensor) or vector.tensor_valence() != (1, 0):
                raise TypeError("covariant tensor contraction takes contravariant vectors")
            if vector.upper_ranks() != (rank,):
                raise ValueError(
                    f"cannot contract covariant rank {rank} with vector ranks {vector.upper_ranks()}"
                )
            if engine_ring(vector.base_ring()) != engine_ring(self.base_ring()):
                raise TypeError("tensor contraction requires one base ring")
        from itertools import product as cartesian_product

        return sum(
            (
                self[position]
                * prod(vector[index] for vector, index in zip(vectors, position, strict=True))
                for position in cartesian_product(*(range(rank) for rank in self.lower_ranks()))
            ),
            self.base_ring().zero(),
        )

    def dual_tensor(self):
        r"""Return the tensor naturally induced on the dual object.

        For a linear map ``T:V->W`` of type ``(1,1)``, this is the dual map
        ``T^vee:W^vee->V^vee`` and therefore has transposed components in the
        selected dual framings.

        For a nondegenerate pairing ``g`` of type ``(0,2)``, duality through
        its correlation isomorphism produces the contravariant tensor
        ``g^vee`` of type ``(2,0)`` on the dual module.  Conversely a
        nondegenerate type-``(2,0)`` tensor dualizes to type ``(0,2)``.
        """
        p, q = self.tensor_valence()
        rows, columns = self.tensor_shape()
        if (p, q) == (1, 1):
            return tensor(
                self.base_ring(),
                (columns,),
                (rows,),
                [[self[i, j] for i in range(rows)] for j in range(columns)],
            )
        if (p, q) in {(0, 2), (2, 0)}:
            if rows != columns:
                raise ValueError("dualizing a pairing requires equal index ranks")
            inverse = _engine_component_matrix(self).inverse()
            components = [tuple(row) for row in inverse.rows()]
            if (p, q) == (0, 2):
                return tensor(self.base_ring(), (rows, columns), (), components)
            return tensor(self.base_ring(), (), (rows, columns), components)
        raise TypeError(
            "dual_tensor is implemented for linear maps and nondegenerate pairings/copairings"
        )

    def rank(self):
        r"""Return the rank of a two-index tensor.

        For a type-``(1,1)`` tensor this is the rank of the linear map; for a
        pairing it is the rank of the form.
        """
        if self.tensor_order() != 2:
            raise TypeError("rank here is defined for a two-index tensor")
        return ZZ(_engine_component_matrix(self).rank())

    def solve_right(self, target):
        r"""Return the ``x`` with ``self * x == target``.

        ``self`` is a type-``(1,1)`` tensor and ``target`` a type-``(1,0)``
        tensor on its codomain index; the solution is a type-``(1,0)`` tensor
        on its domain index.
        """
        if self.tensor_valence() != (1, 1):
            raise TypeError("solving a linear system requires a type-(1,1) tensor")
        if target.tensor_valence() != (1, 0):
            raise TypeError("the right-hand side of a linear system is a vector")
        if self.upper_ranks() != target.upper_ranks():
            raise ValueError(
                f"cannot solve ranks {self.upper_ranks()} against {target.upper_ranks()}"
            )
        solution = _engine_component_matrix(self).solve_right(
            _engine_component_vector(target)
        )
        return tensor(self.base_ring(), self.lower_ranks(), (), solution.list())

    def stack(self, other):
        r"""Return the induced map into the direct sum of the two codomains.

        For ``f: R^n -> R^p`` and ``g: R^n -> R^q`` this is
        ``(f, g): R^n -> R^p (+) R^q``, whose component array is the two
        component arrays one above the other.
        """
        if self.tensor_valence() != (1, 1) or other.tensor_valence() != (1, 1):
            raise TypeError("this universal map is induced by two type-(1,1) tensors")
        if self.lower_ranks() != other.lower_ranks():
            raise ValueError(
                f"the two maps need one domain; got {self.lower_ranks()} "
                f"and {other.lower_ranks()}"
            )
        if engine_ring(other.base_ring()) != engine_ring(self.base_ring()):
            raise TypeError("a universal map requires one base ring")
        rows = self.upper_ranks()[0] + other.upper_ranks()[0]
        return tensor(
            self.base_ring(),
            (rows,),
            self.lower_ranks(),
            list(self.components()) + list(other.components()),
        )

    def trace(self):
        r"""Return the trace of a type-``(1,1)`` tensor.

        This is the contraction of the contravariant slot against the
        covariant one, so it needs equal index ranks.
        """
        if self.tensor_valence() != (1, 1):
            raise TypeError("the trace contracts a type-(1,1) tensor")
        rows, columns = self.tensor_shape()
        if rows != columns:
            raise ValueError("a trace requires equal source and target ranks")
        return sum((self[i, i] for i in range(rows)), self.base_ring().zero())

    def kernel_tensor(self):
        r"""Return the tensor whose rows are a basis of ``ker(self)``.

        For ``f: R^q -> R^p`` the kernel lies in the domain, so the basis
        vectors index the contravariant slot and the domain index the
        covariant one.
        """
        if self.tensor_order() != 2:
            raise TypeError("a kernel here is defined for a two-index tensor")
        basis = _engine_component_matrix(self).right_kernel().basis_matrix()
        return tensor(
            self.base_ring(),
            (int(basis.nrows()),),
            (int(basis.ncols()),),
            basis.list(),
        )

    def row(self, index):
        r"""Return one contravariant slice of a two-index tensor as a vector."""
        if self.tensor_order() != 2:
            raise TypeError("a row here is defined for a two-index tensor")
        columns = self.tensor_shape()[1]
        return tensor(
            self.base_ring(),
            (columns,),
            (),
            [self[int(index), j] for j in range(columns)],
        )

    def left_kernel_tensor(self):
        r"""Return the tensor whose rows are a basis of the left kernel.

        The left kernel of ``f`` is ``ker(f^vee)``; its basis vectors index
        the contravariant slot of the returned type-``(1,1)`` tensor.
        """
        if self.tensor_order() != 2:
            raise TypeError("a left kernel here is defined for a two-index tensor")
        basis = _engine_component_matrix(self).left_kernel().basis_matrix()
        return tensor(
            self.base_ring(),
            (int(basis.nrows()),),
            (int(basis.ncols()),),
            basis.list(),
        )

    def restricted_to_lower_indices(self, positions):
        r"""Return the composite with the inclusion of the named domain indices."""
        if self.tensor_valence() != (1, 1):
            raise TypeError("restricting a domain index requires a type-(1,1) tensor")
        chosen = tuple(int(position) for position in positions)
        rows = self.upper_ranks()[0]
        return tensor(
            self.base_ring(),
            (rows,),
            (len(chosen),),
            [[self[i, j] for j in chosen] for i in range(rows)],
        )

    def transpose(self):
        r"""Return the transposed type-``(1,1)`` tensor.

        Source and target index ranks exchange, so the transpose is the dual
        map and remains a tensor rather than a bare matrix.
        """
        return self.dual_tensor()

    def inverse(self):
        r"""Return the inverse linear-map tensor."""
        return self.inverse_tensor()

    __invert__ = inverse

    def inverse_tensor(self):
        r"""Return the inverse of an invertible type-``(1,1)`` tensor."""
        p, q = self.tensor_valence()
        if (p, q) != (1, 1):
            raise TypeError("inverse_tensor is defined for an invertible linear-map tensor")
        rows, columns = self.tensor_shape()
        if rows != columns:
            raise ValueError("an inverse tensor requires equal source and target ranks")
        inverse = _engine_component_matrix(self).inverse()
        components = [tuple(row) for row in inverse.rows()]
        return tensor(self.base_ring(), (rows,), (columns,), components)

    def pullback(self, linear_map):
        r"""Pull a covariant tensor back along a linear-map tensor.

        If ``T`` has type ``(0,q)`` on ``W`` and ``f:V->W`` has type
        ``(1,1)``, return ``f^*T`` on ``V``.  This is the tensor operation
        underlying form preservation; no row/column-vector convention is
        involved.
        """
        if self.upper_ranks():
            raise TypeError("pullback is defined here for a covariant tensor")
        if linear_map.tensor_valence() != (1, 1):
            raise TypeError("a tensor pullback requires a type-(1,1) linear map")
        if engine_ring(linear_map.base_ring()) != engine_ring(self.base_ring()):
            raise TypeError("tensor pullback requires one base ring")
        target_rank, source_rank = linear_map.tensor_shape()
        if any(rank != target_rank for rank in self.lower_ranks()):
            raise ValueError(
                "the linear-map codomain rank must match every covariant tensor index"
            )
        q = len(self.lower_ranks())
        if q == 0:
            return self

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
                    coefficient *= linear_map[target_index, source_index]
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
    rows, columns = value.tensor_shape()
    if rows == Infinity or columns == Infinity:
        raise ValueError("an infinite tensor has no finite engine matrix")
    return _engine_matrix(
        value.base_ring(),
        rows,
        columns,
        [value[i, j] for i in range(rows) for j in range(columns)],
    )


def _engine_component_vector(value):
    r"""Materialize a type-``(1,0)`` tensor as a private Sage vector."""
    if not isinstance(value, Tensor) or value.tensor_valence() != (1, 0):
        raise TypeError("engine vector materialization requires a type-(1,0) tensor")
    if value.tensor_shape()[0] == Infinity:
        raise ValueError("an infinite vector tensor has no finite engine vector")
    return _engine_vector(value.base_ring(), value.list())


def _tensor_vector_from_native(native) -> Tensor:
    r"""Own one Sage vector as a type-``(1,0)`` tensor.

    Sage's constructor is the engine that reads the argument family and
    infers the ring; the tensor returned is an element of the owned tensor
    module over the owned ring.
    """
    return tensor(native.base_ring(), (int(native.degree()),), (), native.list())


def _tensor_matrix_from_native(native) -> Tensor:
    r"""Own one result of Sage's matrix-constructor family as a type-``(1,1)`` tensor.

    ``matrix(row_keys=..., column_keys=...)`` returns a module morphism rather
    than a matrix; its ``matrix()`` is Sage's documented way to read the
    coordinate array, and this crossing is the only place the tensor layer
    uses it.
    """
    from sage.structure.element import Matrix as SageMatrix

    # Engine boundary: Sage's own class test, not a mathematical predicate.
    coordinates = native if isinstance(native, SageMatrix) else native.matrix()
    return tensor(
        coordinates.base_ring(),
        (int(coordinates.nrows()),),
        (int(coordinates.ncols()),),
        coordinates.list(),
    )


class _TensorVectorConstructor:
    r"""Sage's complete ``vector(...)`` argument family, read as a vector.

    A vector is a type-``(1,0)`` tensor, an element of the owned tensor
    module.  ``sparse`` selects Sage's parsing of the components; a tensor
    has one storage.
    """

    def __call__(self, arg0, arg1=None, arg2=None, sparse=None):
        return _tensor_vector_from_native(
            _engine_vector(arg0, arg1, arg2, sparse=sparse)
        )


class _TensorCovectorConstructor:
    r"""The Sage ``vector(...)`` argument family, read as a covector.

    A covector is a type-``(0,1)`` tensor, an element of the dual tensor
    module, so it never shares a parent with a type-``(1,0)`` vector.  The
    arguments are the ones Sage's ``vector`` already parses; ``sparse``
    selects that parsing, and a tensor has one storage.

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

    def __call__(self, arg0, arg1=None, arg2=None, sparse=None):
        contravariant = _TensorVectorConstructor()(arg0, arg1, arg2, sparse=sparse)
        return tensor(
            contravariant.base_ring(),
            (),
            contravariant.upper_ranks(),
            contravariant.list(),
        )


class _TensorMorphismConstructor:
    r"""A type-``(1,1)`` tensor read as representing a morphism.

    A tensor represents a morphism through the evaluation map

    .. math:: N\otimes_R M^* \longrightarrow \operatorname{Hom}_R(M,N),
              \qquad n\otimes\varphi \mapsto (m\mapsto \varphi(m)\,n),

    and the morphism a tensor represents is its image there.  Only this map
    is needed.  It is neither injective nor surjective in general: distinct
    tensors can represent one morphism, and not every morphism is
    represented.  It is an isomorphism when \(M\) is finitely generated
    projective, which is the regime the coordinate constructors work in.

    So this constructor says that the component array is *meant to*
    represent a morphism.  The contravariant index is the codomain and the
    covariant index the domain, which is what removes the row-versus-column
    reading a bare matrix leaves open.

    **The type-``(1,1)`` reading is a specialization, not the general
    case.**  A morphism always pairs with \(M\otimes N^*\) by
    \(\langle f,\,m\otimes\psi\rangle = \psi(f(m))\), so what one has in
    general is an element of \((M\otimes N^*)^*\), which is of a different
    valence.  It refines to a type-``(1,1)`` tensor only when the modules
    are known to lie in a subcategory where the two agree, and the
    dividing line is finite generation: at infinite rank
    \((M\otimes N^*)^*\) is not \(N\otimes M^*\).
    :class:`TensorModule` already records that boundary, naming an
    infinite-rank mixed space ``Hom(...)`` and an infinite-rank type-
    ``(0,q)`` space \((M^{\otimes q})^*\) rather than \((M^*)^{\otimes q}\).
    Taking integer ranks and a finite component array is exactly what
    places this constructor on the finitely generated side of it.

    EXAMPLES::

        sage: from dzack_research.preamble.tensors import tensor
        sage: f = tensor.morphism(ZZ, 2, 3, [[1, 0, 2], [0, 1, 3]])
        sage: f.tensor_valence()
        (1, 1)
        sage: f.parent()
        ZZ^2 ⊗ (ZZ^3)*
        sage: f * tensor.vector(ZZ, [1, 1, 1])
        Type (1, 0) tensor in ZZ^2
        (3, 4)
    """

    def __call__(self, base_ring, codomain_rank, domain_rank, components=None):
        for rank in (codomain_rank, domain_rank):
            if rank == Infinity:
                raise ValueError(
                    "the type-(1,1) reading of a morphism needs finitely "
                    "generated modules; at infinite rank a morphism is an "
                    "element of (M ⊗ N*)*, whose space TensorModule names "
                    "Hom(...)"
                )
        return tensor(base_ring, (codomain_rank,), (domain_rank,), components)


class _TensorEndomorphismConstructor:
    r"""The square case of :class:`_TensorMorphismConstructor`, where ``M`` is ``N``.

    One rank suffices, and the represented morphism is an endomorphism.
    The same specialization applies: in general an endomorphism gives an
    element of \((M\otimes_R M^*)^*\) through the trace pairing, and only
    finite generation refines that to a type-``(1,1)`` tensor.

    EXAMPLES::

        sage: from dzack_research.preamble.tensors import tensor
        sage: t = tensor.endomorphism(ZZ, 2, [[0, 1], [1, 0]])
        sage: t.tensor_valence()
        (1, 1)
        sage: t.trace()
        0
        sage: t * t == tensor.endomorphism(ZZ, 2, [[1, 0], [0, 1]])
        True
    """

    def __call__(self, base_ring, rank, components=None):
        return _TensorMorphismConstructor()(base_ring, rank, rank, components)


class _TensorMatrixConstructor:
    r"""The complete Sage ``matrix`` constructor namespace, tensor-refined."""

    options = _sage_matrix.options

    def __call__(self, *args, **kwds):
        try:
            return _tensor_matrix_from_native(_engine_matrix(*args, **kwds))
        except TypeError as engine_error:
            if kwds or len(args) not in (3, 4):
                raise engine_error
            try:
                base = own_ring(args[0])
                rows = int(args[1])
                columns = int(args[2])
            except (TypeError, ValueError):
                raise engine_error
            components = (
                tuple(base.zero() for _ in range(rows * columns))
                if len(args) == 3
                else args[3]
            )
            return _coordinate_tensor(
                base,
                (rows,),
                (columns,),
                components,
            )

    def block(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.block, *args, **kwds)
        )

    def block_diagonal(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.block_diagonal, *args, **kwds)
        )

    def circulant(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.circulant, *args, **kwds)
        )

    def column(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.column, *args, **kwds)
        )

    def companion(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.companion, *args, **kwds)
        )

    def diagonal(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.diagonal, *args, **kwds)
        )

    def elementary(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.elementary, *args, **kwds)
        )

    def hankel(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.hankel, *args, **kwds)
        )

    def hilbert(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.hilbert, *args, **kwds)
        )

    def identity(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.identity, *args, **kwds)
        )

    def ith_to_zero_rotation(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.ith_to_zero_rotation, *args, **kwds)
        )

    def jordan_block(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.jordan_block, *args, **kwds)
        )

    def lehmer(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.lehmer, *args, **kwds)
        )

    def ones(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.ones, *args, **kwds)
        )

    def random(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.random, *args, **kwds)
        )

    def random_bistochastic(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.random_bistochastic, *args, **kwds)
        )

    def random_diagonalizable(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.random_diagonalizable, *args, **kwds)
        )

    def random_echelonizable(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.random_echelonizable, *args, **kwds)
        )

    def random_rref(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.random_rref, *args, **kwds)
        )

    def random_subspaces(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.random_subspaces, *args, **kwds)
        )

    def random_unimodular(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.random_unimodular, *args, **kwds)
        )

    def random_unitary(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.random_unitary, *args, **kwds)
        )

    def toeplitz(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.toeplitz, *args, **kwds)
        )

    def vandermonde(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.vandermonde, *args, **kwds)
        )

    def vector_on_axis_rotation(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.vector_on_axis_rotation, *args, **kwds)
        )

    def zero(self, *args, **kwds):
        return _tensor_matrix_from_native(
            _named_engine_matrix(_sage_matrix.zero, *args, **kwds)
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

    def tensor_shape(self) -> tuple[int, ...]:
        return self.parent().tensor_shape()

    def tensor_valence(self) -> tuple[int, int]:
        return self.parent().tensor_valence()

    def __call__(self, *args):
        r"""Contract covariant slots with the given vectors."""
        _contravariant, covariant = self.tensor_valence()
        if len(args) != covariant:
            raise TypeError(
                f"a type-{self.tensor_valence()} tensor takes "
                f"{covariant} vector arguments, got {len(args)}"
            )
        shape = self.tensor_shape()
        if self.tensor_valence() == (0, 1):
            vector = args[0]
            if vector.tensor_valence() != (1, 0):
                raise TypeError("a covector evaluates on a contravariant vector")
            if vector.upper_ranks() != self.lower_ranks():
                raise ValueError(
                    f"cannot pair ranks {self.lower_ranks()} and {vector.upper_ranks()}"
                )
            return sum(
                (self[i] * vector[i] for i in range(shape[0])),
                self.base_ring().zero(),
            )
        if covariant == 2 and len(shape) == 2:
            left, right = args
            return sum(
                (
                    self[i, j] * left[i] * right[j]
                    for i in range(shape[0])
                    for j in range(shape[1])
                ),
                self.base_ring().zero(),
            )
        raise TypeError(
            f"contraction is not implemented for valence {self.tensor_valence()}"
        )

    def _latex_(self) -> str:
        from sage.matrix.constructor import matrix as sage_matrix
        from sage.misc.latex import latex as sage_latex

        shape = self.tensor_shape()
        if len(shape) == 2:
            rows, columns = shape
            return str(
                sage_latex(
                    sage_matrix(
                        _engine_if_ring(self.base_ring()),
                        rows,
                        columns,
                        [
                            self[i, j]
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
        return _nested(self._entries, self.tensor_shape())

    def list(self):
        r"""Return flattened components in index order."""
        return list(self._entries)

    def rows(self):
        r"""Return component rows for a two-index tensor.

        These are component tuples, not row vectors in a module or dual.
        """
        if self.tensor_order() != 2:
            raise TypeError("rows are defined only for a two-index tensor")
        return tuple(tuple(row) for row in self.components())

    def nrows(self):
        if self.tensor_order() != 2:
            raise TypeError("nrows is defined only for a two-index tensor")
        return self.tensor_shape()[0]

    def ncols(self):
        if self.tensor_order() != 2:
            raise TypeError("ncols is defined only for a two-index tensor")
        return self.tensor_shape()[1]

    def is_symmetric(self) -> bool:
        r"""Return whether a square two-index tensor is symmetric in its slots."""
        if self.tensor_order() != 2:
            raise TypeError("symmetry here is defined for a two-index tensor")
        rows, columns = self.tensor_shape()
        if rows != columns:
            return False
        return all(self[i, j] == self[j, i] for i in range(rows) for j in range(columns))

    def change_ring(self, ring):
        r"""Change scalar coefficients without changing tensor variance."""
        target = ring
        return tensor(
            target,
            self.upper_ranks(),
            self.lower_ranks(),
            _nested(
                tuple(target(entry) for entry in self._entries),
                self.tensor_shape(),
            ),
        )

    def determinant(self):
        r"""Return the determinant of a square two-index coordinate tensor."""
        if self.tensor_order() != 2 or self.tensor_shape()[0] != self.tensor_shape()[1]:
            raise TypeError("determinant requires a square two-index tensor")
        return _engine_component_matrix(self).det()

    det = determinant

    def __getitem__(self, index: tuple[int, ...]):
        try:
            len(index)
        except TypeError:
            index = (index,)
        if len(index) != self.tensor_order():
            raise IndexError(
                f"a tensor of shape {self.tensor_shape()} takes "
                f"{self.tensor_order()} indices, got {len(index)}"
            )
        offset = 0
        for position, dimension in zip(index, self.tensor_shape()):
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
            len(self.upper_ranks()) >= 2
            and not self.lower_ranks()
            and isinstance(other, Tensor)
            and other.tensor_valence() == (0, 1)
        ):
            if engine_ring(other.base_ring()) != engine_ring(self.base_ring()):
                raise TypeError("tensor contraction requires one base ring")
            if self.upper_ranks()[-1] != other.lower_ranks()[0]:
                raise ValueError(
                    f"cannot contract ranks {self.upper_ranks()[-1]} and "
                    f"{other.lower_ranks()[0]}"
                )
            output_upper = self.upper_ranks()[:-1]
            output_shape = output_upper
            contracted_rank = self.upper_ranks()[-1]

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
        if isinstance(other, Tensor) and other.tensor_valence() == (1, 0):
            if engine_ring(other.base_ring()) != engine_ring(self.base_ring()):
                raise TypeError("tensor contraction requires one base ring")
            if not self.lower_ranks():
                raise TypeError("a tensor with no covariant index cannot act on a vector")
            if self.lower_ranks()[-1] != other.upper_ranks()[0]:
                raise ValueError(
                    f"cannot contract ranks {self.lower_ranks()[-1]} and "
                    f"{other.upper_ranks()[0]}"
                )

            # Multiplication contracts the rightmost covariant index.  Thus a
            # bilinear form G in M* tensor M* acts on v in M as G*v in M*,
            # with components (G*v)_i = sum_j G_{ij} v_j.  No row-vector or
            # transpose convention enters the public tensor calculus.
            output_upper = self.upper_ranks()
            output_lower = self.lower_ranks()[:-1]
            output_shape = output_upper + output_lower
            contracted_rank = self.lower_ranks()[-1]

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
            self.tensor_valence() == (1, 1)
            and isinstance(other, Tensor)
            and other.tensor_valence() == (1, 1)
        ):
            if engine_ring(other.base_ring()) != engine_ring(self.base_ring()):
                raise TypeError("tensor composition requires one base ring")
            if self.lower_ranks() != other.upper_ranks():
                raise ValueError(
                    f"cannot compose ranks {self.lower_ranks()} and "
                    f"{other.upper_ranks()}"
                )
            rows = self.upper_ranks()[0]
            inner = other.upper_ranks()[0]
            columns = other.lower_ranks()[0]
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

        if self.tensor_valence() == (0, 1):
            if engine_ring(other.base_ring()) != engine_ring(self.base_ring()):
                raise TypeError("tensor contraction requires one base ring")
            if other.tensor_valence() == (1, 0):
                return self(other)
            if other.tensor_valence() == (1, 1):
                if self.lower_ranks() != other.upper_ranks():
                    raise ValueError(
                        f"cannot contract ranks {self.lower_ranks()} and "
                        f"{other.upper_ranks()}"
                    )
                rows = self.lower_ranks()[0]
                columns = other.lower_ranks()[0]
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
            "composition, or tensor product"
        )

    def __rmul__(self, other):
        if other in self.base_ring():
            return self._rmul_(self.base_ring()(other))
        raise TypeError("a tensor can only be multiplied by a scalar on the left")

    def _richcmp_(self, other, op):
        return _tensor_richcmp(self, other, op)

    __hash__ = Tensor._tensor_hash

    def __reduce__(self):
        return (
            _restore_tensor,
            (
                self.base_ring(),
                self.upper_ranks(),
                self.lower_ranks(),
                self.components(),
            ),
        )


def _coordinate_component_repr(tensor_value) -> str:
    r"""Plain-text components: a vector, a matrix, or a nested array."""
    shape = tensor_value.tensor_shape()
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

        return UniqueRepresentation.__classcall__(
            cls,
            own_ring(base_ring),
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
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        Parent.__init__(self, base=_engine_ring(base_ring), category=Modules(base_ring))

    def construction(self):
        r"""Return no functorial construction.

        Sage's coercion walks this when it looks for an action of a ring on
        this module; a tensor module is built from its rank vector, not from
        a construction functor applied to another parent.
        """
        return None

    def tensor_shape(self) -> tuple:
        return self._upper_ranks + self._lower_ranks

    def tensor_type(self) -> tuple[int, int]:
        return (len(self._upper_ranks), len(self._lower_ranks))

    def tensor_valence(self) -> tuple[int, int]:
        return self.tensor_type()

    def upper_ranks(self) -> tuple:
        return self._upper_ranks

    def lower_ranks(self) -> tuple:
        return self._lower_ranks

    def index_modules(self):
        r"""Return the contravariant and covariant index modules \(R^{n_i}\)."""
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
            FreeModule,
        )
        from sage.rings.semirings.non_negative_integer_semiring import NN

        def free_of_rank(rank):
            if rank == Infinity:
                return FreeModule(self.base_ring(), NN)
            return FreeModule(self.base_ring(), int(rank))

        return (
            tuple(free_of_rank(rank) for rank in self._upper_ranks),
            tuple(free_of_rank(rank) for rank in self._lower_ranks),
        )

    def tensor_indices(self):
        r"""Return the standard generating set of each finite index module."""
        from dzack_research.preamble.categories.sets import finite_ordered_set

        def keys(rank):
            assert rank != Infinity, (
                "an infinite index set is the generating set of its index module"
            )
            return finite_ordered_set(range(int(rank)))

        return (
            tuple(keys(rank) for rank in self._upper_ranks),
            tuple(keys(rank) for rank in self._lower_ranks),
        )

    def _element_constructor_(self, entries: tuple) -> _CoordinateTensor:
        shape = self.tensor_shape()
        assert Infinity not in shape, (
            "an infinite-rank tensor space has no component array"
        )
        if len(entries) != prod(shape):
            raise ValueError(
                f"shape {shape} requires {prod(shape)} "
                f"components, got {len(entries)}"
            )
        engine = engine_ring(self.base_ring())
        return self.element_class(self, tuple(engine(entry) for entry in entries))

    def zero(self) -> _CoordinateTensor:
        assert Infinity not in self.tensor_shape(), (
            "an infinite-rank tensor space has no component array"
        )
        zero = self.base_ring().zero()
        return self.element_class(
            self,
            tuple(zero for _ in range(prod(self.tensor_shape()))),
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


def _tensor_module(
    base_ring: Parent,
    upper_ranks: tuple[int, ...],
    lower_ranks: tuple[int, ...],
) -> TensorModule:
    return TensorModule(base_ring, tuple(upper_ranks), tuple(lower_ranks))


def _is_dimension(value) -> bool:
    return value in ZZ and ZZ(value) >= 0


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

    ``tensor.vector`` accepts every call accepted by Sage's ``vector``, and
    ``tensor.covector`` reads that same argument family as a covector.
    ``tensor.matrix`` accepts every call accepted by Sage's ``matrix`` and
    exposes the same named matrix constructors.

    The main call is ``tensor(R, ps, qs, data)``.  ``ps`` lists upper-index
    dimensions and ``qs`` lower-index dimensions.  Hence vectors and covectors
    are different constructor calls even though both have one index.
    """

    vector = _TensorVectorConstructor()
    covector = _TensorCovectorConstructor()
    matrix = _TensorMatrixConstructor()
    morphism = _TensorMorphismConstructor()
    endomorphism = _TensorEndomorphismConstructor()

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
        try:
            base_ring = own_ring(base_ring)
        except TypeError as error:
            raise TypeError(f"the tensor base must be a ring, got {base_ring}") from error
        if base_ring not in _Rings:
            raise TypeError(f"the tensor base must be a ring, got {base_ring}")
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
