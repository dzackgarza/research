r"""Relative cyclic covers of an affine scheme, with their deck action.

Let ``X = Spec(A)``, let ``L`` be an invertible ``O_X``-module, let ``n >= 1``
and let ``s`` be a section of ``L^n``.  The cyclic cover of degree ``n``
branched along ``s`` is the relative spectrum of the ``O_X``-algebra
``⊕_{i=0}^{n-1} L^{-i}``, whose multiplication
``L^{-i} ⊗ L^{-j} -> L^{-(i+j)}`` is the identity when ``i + j < n`` and is
multiplication by ``s`` when ``i + j >= n`` (Barth, Hulek, Peters and Van de
Ven, *Compact Complex Surfaces*, I.17).

The construction here is the trivialized one, ``L = O_X``: the section is an
element ``f`` of ``A`` and the cover algebra is ``A[z]/(z^n - f)``.  One
presented algebra supplies everything the cover needs.  Its multiplication is
the algebra structure of the quotient; its underlying finite module is the
free ``A``-module on the powers ``1, z, ..., z^{n-1}`` that a one-variable
monic quotient already carries; its local equation is the relation
``z^n - f``; and a scalar change of ``A`` carries that presentation along.
The graded summand ``A z^i`` is the trivialization of ``L^{-i}``.

The deck group is ``mu_n``.  Over scalars containing a primitive ``n``-th root
of unity ``zeta`` it is the constant group ``C_n``, acting by ``z -> zeta z``
over the base; that is the case constructed here.  Without such a root, or in
a characteristic dividing ``n``, the deck group is the group scheme ``mu_n``,
which the preamble does not own, and the construction says so rather than
letting a constant group stand in for a scheme.

The quotient by the deck action is ``X`` again: the generator multiplies the
summand ``A z^i`` by ``zeta^i``, so an invariant element has ``a_i = 0`` for
``0 < i < n`` and the invariant subalgebra is the degree-zero part ``A``.
That is a theorem about the grading, not an invariant-ring computation, and
it is what this category supplies in place of the general linear-action
backend, which does not apply to a quotient presentation.

Not constructed here: the canonical-bundle formula and the smoothness
criteria of a cover, both of which need the differentials and the invertible
sheaves that the divisor layer will own, and the nontrivial ``L``, which
needs the gluing of rank-one locally free modules with their transition
units.
"""

from sage.categories.category import Category
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.algebras.free_algebras import (
    FinitelyPresentedAlgebra,
    PolynomialRing,
)
from dzack_research.preamble.categories.group.g_objects import GObjects
from dzack_research.preamble.categories.group.groups import OwnedGroups
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.schemes.affine_spec import SpecFunctor
from dzack_research.preamble.categories.schemes.schemes import (
    Schemes,
    Spec,
    _AffineGSchemes,
)
from dzack_research.preamble.refine import refine

_COVER_VARIABLE_LABEL = "z"


def _primitive_root_of_unity(scalars, degree):
    r"""Return a primitive ``degree``-th root of unity in ``scalars``.

    The roots of ``t^n - 1`` are computed in the scalars' own polynomial ring
    and one of exact multiplicative order ``n`` is selected.  A primitive root
    exists exactly when the constant group ``C_n`` can act on the cover by
    scaling ``z``; where it does not, the deck group is the group scheme
    ``mu_n`` and this states that rather than substituting a weaker action.
    """
    engine = _engine_ring(scalars)
    assert engine.is_field(), (
        f"{scalars} is not a field, so the roots of unity acting on a cyclic "
        "cover are not selected by this construction"
    )
    characteristic = int(engine.characteristic())
    assert characteristic == 0 or degree % characteristic != 0, (
        f"the characteristic {characteristic} divides the degree {degree}, so "
        "the cover is inseparable and its deck group scheme mu_n is not the "
        "constant group C_n"
    )
    polynomials = engine[_COVER_VARIABLE_LABEL]
    variable = polynomials.gen()
    primitive = [
        root
        for root, _multiplicity in (variable**degree - polynomials.one()).roots()
        if int(root.multiplicative_order()) == degree
    ]
    assert primitive, (
        f"{scalars} holds no primitive {degree}-th root of unity, so the deck "
        f"group of a degree-{degree} cyclic cover over it is the group scheme "
        "mu_n, which the preamble does not own"
    )
    return scalars._from_engine_element(primitive[0])


class CyclicCovers(OwnedCategory):
    r"""Degree-``n`` cyclic covers of ``Spec(A)``, with their deck action.

    An object is the affine ``A``-scheme ``Spec(A[z]/(z^n - f))`` equipped with
    the deck action of ``C_n``; its structure morphism to the terminal affine
    ``A``-scheme is the finite cover morphism, so a cover is an object of
    ``Sch/Spec(A)`` with no further construction.  The category is a
    subcategory of the affine ``C_n``-schemes over ``A``, which is where the
    common fixed locus and the quotient of an action are already owned; the
    deck fixed locus is the ramification subscheme ``V(z)``, because the
    generator's fixed ideal is generated by ``(zeta - 1) z`` and ``zeta - 1``
    is a unit.
    """

    @staticmethod
    def __classcall__(cls, base_algebra, degree):
        return Category.__classcall__(cls, _own_ring(base_algebra), int(degree))

    def __init__(self, base_algebra, degree) -> None:
        assert degree >= 1, "a cyclic cover has degree at least one"
        self._base_algebra = base_algebra
        self._degree = degree
        OwnedCategory.__init__(self)

    def base_algebra(self):
        r"""Return ``A``, the coordinate algebra of the base."""
        return self._base_algebra

    def base_scheme(self):
        r"""Return ``X = Spec(A)`` as the terminal affine ``A``-scheme."""
        algebra = self.base_algebra()
        return Spec(algebra, base_ring=algebra)

    def cover_degree(self):
        r"""Return ``n``, the degree of the covers in this category."""
        return self._degree

    @cached_method
    def deck_group(self):
        r"""Return ``C_n``, the constant deck group of a degree-``n`` cover."""
        return OwnedGroups().C(self.cover_degree())

    @cached_method
    def deck_root_of_unity(self):
        r"""Return the primitive ``n``-th root of unity the deck generator scales by."""
        return _primitive_root_of_unity(
            self.base_algebra().base_ring(),
            self.cover_degree(),
        )

    def super_categories(self):
        return [_AffineGSchemes(self.deck_group(), self.base_algebra())]

    def _repr_object_names(self):
        return (
            f"degree-{self.cover_degree()} cyclic covers of {self.base_scheme()}"
        )

    def an_object(self):
        r"""The trivial cover ``z^n = 1``, the ``mu_n``-torsor over ``X``."""
        return self(self.base_algebra().one())

    def _call_(self, branch_section):
        r"""Return the cyclic cover branched along ``branch_section``."""
        algebra = self.base_algebra()
        section = algebra(branch_section)
        degree = self.cover_degree()
        root_of_unity = self.deck_root_of_unity()

        presentation = PolynomialRing(algebra, _COVER_VARIABLE_LABEL)
        variable = presentation.algebra_generator(_COVER_VARIABLE_LABEL)
        cover_algebra = FinitelyPresentedAlgebra(
            presentation,
            (variable**degree - presentation(section),),
        )
        cover = Spec(cover_algebra)
        image = cover_algebra.algebra_generator(_COVER_VARIABLE_LABEL)

        group = self.deck_group()
        generator = group.group_generators().unrank(0)
        exponents = {}
        element = group.one()
        for exponent in range(degree):
            exponents[element] = exponent
            element = element * generator

        def deck_action(group_element):
            scaling = cover_algebra(root_of_unity ** exponents[group_element])
            return SpecFunctor(algebra)(
                cover_algebra.Mor(cover_algebra)(
                    {_COVER_VARIABLE_LABEL: scaling * image}
                )
            )

        acted = GObjects(group, Schemes(algebra))(cover, deck_action)
        acted._preamble_cyclic_branch_section = section
        acted._preamble_cyclic_cover_degree = degree
        acted._preamble_cyclic_deck_root_of_unity = root_of_unity
        return refine(acted, self)

    class ParentMethods:
        def cover_degree(self):
            r"""Return ``n``: the cover is finite locally free of this rank."""
            return self._preamble_cyclic_cover_degree

        def branch_section(self):
            r"""Return ``f``, the section of ``L^n = O_X`` the cover is branched along."""
            return self._preamble_cyclic_branch_section

        def deck_root_of_unity(self):
            r"""Return the primitive ``n``-th root of unity the deck generator scales by."""
            return self._preamble_cyclic_deck_root_of_unity

        def cover_variable(self):
            r"""Return ``z``, whose ``n``-th power is the branch section."""
            return self.coordinate_algebra().algebra_generator(_COVER_VARIABLE_LABEL)

        @cached_method
        def branch_subscheme(self):
            r"""Return the branch subscheme ``V(f)`` of the base.

            The cover is étale over the complement of ``V(f)`` and the deck
            action is free there; the ramification subscheme upstairs is the
            deck fixed locus ``V(z)``, which maps isomorphically onto ``V(f)``
            when ``n`` is invertible.
            """
            return self.base_scheme().closed_subscheme(self.branch_section())

        def invariant_algebra(self):
            r"""Return ``A``: the deck invariants are the degree-zero summand.

            The generator multiplies ``A z^i`` by ``zeta^i`` and ``zeta`` is a
            primitive ``n``-th root of unity, so an invariant element has
            ``zeta^i a_i = a_i`` and hence ``a_i = 0`` for ``0 < i < n``.  No
            invariant-ring computation is involved, and the general linear
            backend does not apply to this quotient presentation.
            """
            return self.scheme_base_ring()

        def invariant_algebra_inclusion(self):
            r"""Return ``A -> A[z]/(z^n - f)``, the algebra structure morphism."""
            return self.coordinate_algebra().algebra_structure_morphism()

        def affine_quotient(self):
            r"""Return ``X``: a cyclic cover is the quotient map onto its base."""
            return self.base_scheme()

        def quotient_morphism(self):
            r"""Return the cover morphism, which is the deck quotient map."""
            return self.structure_morphism()


__all__ = ["CyclicCovers"]
