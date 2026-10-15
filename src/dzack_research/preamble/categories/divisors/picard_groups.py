r"""The Picard functor ``Pic : C^op -> Mod_ZZ`` on a category of schemes.

For a scheme ``X`` the Picard group ``Pic(X)`` is the abelian group of
isomorphism classes of invertible ``O_X``-modules under tensor product, and a
morphism ``f: X -> Y`` induces the pullback ``f^* : Pic(Y) -> Pic(X)``,
``[L] |-> [f^* L]`` (Hartshorne, *Algebraic Geometry*, II.6).  An abelian group
is a ``ZZ``-module, so the values are objects of ``Modules(ZZ)``.  The value at
one scheme is that scheme's ``picard_group()``; this module holds the functor
and the represented values that the projective-bundle formula and the field
case build.
"""

from sage.categories.map import Map
from sage.misc.cachefunc import cached_function, cached_method
from sage.structure.element import parent as element_parent
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.divisors.divisor_groups import _integers
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.ring_foundation import _owned_integers
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.lexicon.category_theory import ObjectOfCategory
from dzack_research.preamble.logic import AtomicProposition, negation
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.owned_category_bases import Category


class _PicardFunctor(Functor):
    r"""``Pic : C^op -> Mod_ZZ`` on a category ``C`` of schemes over a base ring.

    ``op(X) |-> Pic(X)``, the group of isomorphism classes of invertible
    ``O_X``-modules under tensor product, and ``op(f) |-> f^*`` for
    ``f: X -> Y`` (Hartshorne, *Algebraic Geometry*, II.6).  Pullback
    preserves tensor products, so ``f^*`` is a group homomorphism, and
    ``(g f)^* = f^* g^*``, so ``Pic`` is contravariant.
    """

    def __init__(self, scheme_category: Category) -> None:
        self._scheme_category = scheme_category
        super().__init__(scheme_category.opposite(), Modules(_owned_integers()))

    def _apply_object(self, opposite_scheme: ObjectOfCategory) -> Parent:
        r"""``Pic(X)`` for the object ``op(X)`` of ``C^op``."""
        return opposite_scheme.underlying_object().picard_group()

    def _apply_morphism(self, morphism: Map) -> Map:
        r"""``f^* : Pic(Y) -> Pic(X)``, ``[L] |-> [f^* L]``, for the arrow ``op(f): op(Y) -> op(X)`` of ``f: X -> Y``.

        ``f^*`` is a group homomorphism, so it is fixed by the images of
        module generators of ``Pic(Y)``.  For ``Y = P^n_k`` over a field,
        ``Pic(Y) = Pic(Spec k) + ZZ[O(1)]`` with ``Pic(Spec k) = 0``
        (Hartshorne, II.6.17), and the one module generator ``[O(1)]`` goes to
        ``[f^* O(1)]``.
        """
        from dzack_research.preamble.categories.schemes.schemes import ProjectiveSpaces

        arrow = morphism.underlying_arrow()
        target_scheme = arrow.codomain()
        source = self(morphism.domain())
        target = self(morphism.codomain())
        base = target_scheme.scheme_base_ring()
        assert target_scheme in ProjectiveSpaces(base), (
            f"cannot pull back Pic({target_scheme}) along {arrow}: f^* is computed on the module generators "
            f"of Pic(P^n_k), and {target_scheme} is not a projective space over {base}"
        )
        assert source.biproduct_factor(0).module_generating_set().is_empty() is True, (
            f"cannot pull back Pic({target_scheme}) along {arrow}: the base summand {source.biproduct_factor(0)} "
            "of Pic(P^n_S) = Pic(S) + ZZ[O(1)] has module generators, and their invertible sheaves on S are "
            "not represented"
        )
        pulled_hyperplane = target(target.underlying_set()(arrow.module_pullback(target_scheme.O(1))))
        return self.codomain().Mor(source, target)(
            {label: pulled_hyperplane for label in source.module_generating_set()}
        )

    @cached_method
    def category_of_elements(self):
        r"""``int Pic`` over ``C``: the pairs ``(X, L)`` with ``L`` in ``Pic(X)``.

        ``Pic`` is a presheaf on ``C``, so a morphism ``(X, L) -> (Y, M)`` is
        ``f: X -> Y`` with ``f^* M = L``.
        """
        from dzack_research.preamble.categories.schemes.polarized_varieties import (
            _PicardCategoryOfElements,
        )

        return _PicardCategoryOfElements(self, self._scheme_category)

    def _repr_(self) -> str:
        return "Pic"


def _zero_picard_group() -> Parent:
    r"""``Pic(X) = 0``, the free ``ZZ``-module on no classes.

    The value for ``X = Spec k`` with ``k`` a field, and more generally for
    the schemes whose invertible sheaves are all trivial, such as ``A^n_k``:
    there ``Pic = Cl`` (Hartshorne, II.6.16), and ``Cl = 0`` because
    ``k[x_1, ..., x_n]`` is a unique factorization domain.
    """
    return _integers().free_module(finite_ordered_set(()))


def _projective_bundle_picard_group(base_picard_group: Parent) -> Parent:
    r"""``Pic(P^n_S) = Pic(S) + ZZ[O(1)]``, the biproduct of ``Pic(S)`` and the hyperplane summand.

    The base Picard group is required input, so this never replaces it by
    zero.  The injection of the second factor sends its generator ``O(1)``
    to the hyperplane class ``[O(1)]`` (Hartshorne, II.6.17 and II,
    Exercise 6.1).
    """
    integers = _integers()
    hyperplane = integers.free_module(finite_ordered_set(("O(1)",)))
    return Modules(integers).biproduct((base_picard_group, hyperplane))


class _InvertibleSheafClass:
    r"""The isomorphism class ``[L]`` of one invertible ``O_X``-module ``L``."""

    def __init__(self, parent, representative) -> None:
        self._representative = representative
        super().__init__(parent)

    def representative(self):
        r"""The invertible sheaf ``L`` that represents this class."""
        return self._representative

    def _richcmp_(self, other, op):
        match op in (op_EQ, op_NE):
            case False:
                return NotImplemented
            case True:
                pass
        match element_parent(other) is self.parent():
            case False:
                return op == op_NE
            case True:
                pass
        decision = self.parent().equal(self, other)
        return decision if op == op_EQ else negation(decision)

    __hash__ = None

    def _repr_(self):
        return f"[{self.representative()}]"


class _InvertibleSheafClasses:
    r"""The set of isomorphism classes of invertible ``O_X``-modules.

    The group law is the tensor product, ``[L] + [M] = [L tensor M]``; the
    inverse is the dual sheaf, ``-[L] = [L^vee]``, because
    ``L tensor L^vee = O_X`` for ``L`` invertible; and the unit is ``[O_X]``
    (Hartshorne, *Algebraic Geometry*, II.6.12).  Two represented sheaves
    that are the same object give the same class; any other identification
    is the proposition ``isomorphic(L, M)``.
    """

    def __init__(self, scheme, unit_sheaf, **rest) -> None:
        self._scheme = scheme
        self._unit_sheaf = unit_sheaf
        super().__init__(**rest)

    def scheme(self):
        return self._scheme

    def __contains__(self, value):
        return element_parent(value) is self

    def __call__(self, value):
        r"""The class of ``value``: an element of this set, or an invertible sheaf on ``X``."""
        from dzack_research.preamble.categories.schemes.ringed_spaces import QuasiCoherentSheaves

        match element_parent(value) is self:
            case True:
                return value
            case False:
                invertible = QuasiCoherentSheaves(self.scheme()).Invertible()
                assert value in invertible, (
                    f"{value} has no class in Pic({self.scheme()}): it is not an object of {invertible}"
                )
                return self.element_class(self, value)

    @cached_method
    def zero(self):
        r"""``[O_X]``, the class of the structure sheaf."""
        return self.element_class(self, self._unit_sheaf)

    def add(self, left, right):
        left = self(left)
        right = self(right)
        match (left.representative() is self._unit_sheaf, right.representative() is self._unit_sheaf):
            case (True, _):
                return right
            case (_, True):
                return left
            case _:
                return self(left.representative().tensor_product(right.representative()))

    def negate(self, value):
        value = self(value)
        match value.representative() is self._unit_sheaf:
            case True:
                return value
            case False:
                return self(value.representative().dual_sheaf())

    def scale(self, scalar, value):
        exponent = _integers()(scalar)
        value = self(value)
        match exponent == 0:
            case True:
                return self.zero()
            case False:
                return self(value.representative().tensor_power(exponent))

    def equal(self, left, right):
        r"""Decide ``[L] = [M]`` when ``L`` and ``M`` are one sheaf, else return ``isomorphic(L, M)``."""
        left = self(left)
        right = self(right)
        match left.representative() is right.representative():
            case True:
                return True
            case False:
                return AtomicProposition("isomorphic", left.representative(), right.representative())

    def _repr_(self):
        return f"Isomorphism classes of invertible sheaves on {self.scheme()}"


class _PicardGroupEngine:
    r"""``Pic(X)`` as a ``ZZ``-module on the isomorphism classes of invertible sheaves."""

    def __init__(self, picard_scheme, **rest) -> None:
        self._picard_scheme = picard_scheme
        super().__init__(**rest)

    def picard_scheme(self):
        r"""The scheme ``X`` in ``Pic(X)``."""
        return self._picard_scheme

    def _repr_(self):
        return f"Pic({self.picard_scheme()})"


@cached_function(key=lambda scheme, unit_sheaf: id(scheme))
def _invertible_sheaf_class_group(scheme, unit_sheaf):
    r"""``Pic(X)``, the isomorphism classes of invertible ``O_X``-modules under tensor product.

    ``unit_sheaf`` is the represented invertible sheaf ``O_X``, the unit of
    the tensor product.  An abelian group is a ``ZZ``-module, with ``n [L]``
    the class of ``L^{tensor n}``.
    """
    from dzack_research.preamble.categories.modules.general_modules import GeneralModules
    from dzack_research.preamble.categories.sets.set_categories import Sets

    classes = _object_of(
        Sets(),
        _engine=(Sets(), _InvertibleSheafClasses, _InvertibleSheafClass),
        scheme=scheme,
        unit_sheaf=unit_sheaf,
    )
    integers = _integers()
    return _object_of(
        GeneralModules(integers),
        _engine=(GeneralModules(integers), _PicardGroupEngine, None),
        picard_scheme=scheme,
        base_ring=integers,
        underlying_set=classes,
        addition=classes.add,
        zero=classes.zero(),
        negation=classes.negate,
        scalar_action=classes.scale,
    )


__all__ = []
