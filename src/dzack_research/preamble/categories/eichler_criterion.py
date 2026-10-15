r"""Eichler's criterion: the orbit invariants of a primitive vector.

Let ``L`` be an even lattice splitting two hyperbolic planes, ``L = U + U +
K``.  Eichler's criterion says that the stable orthogonal group ``ker(rho_L)``
acts transitively on the primitive vectors of a given square and a given
class in the discriminant group, so the orbit of a primitive ``v`` is
determined by

``q(v)``,   ``div(v) = gcd b(v, L)``,   ``[v / div(v)] in A_L``.

The reference is Eichler, *Quadratische Formen und orthogonale Gruppen*,
Springer 1952, section 10.

All three invariants are already owned: ``v.q()``, ``v.div()`` and
``v.divided_discriminant_class()``.  What this module adds is the hypothesis
under which they are a complete invariant, and the decision the theorem then
licenses.  That decision replaces a search: it answers an orbit question about
an infinite group by comparing three finite pieces of data, with no
enumeration and no bound.

The hypothesis is checked on the lattice's *represented* decomposition, not by
searching for an abstract isometry to ``U + U + K``.  A lattice built as a sum
of named summands answers it; a lattice given only by a Gram matrix does not,
and that is a statement about the presentation rather than about the lattice.
"""

from sage.misc.cachefunc import cached_method
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.group.groups import _matrix_group_element_matrix
from dzack_research.preamble.categories.rings.ring_foundation import _engine_element, _engine_ring, _owned_engine_element
from sage.matrix.constructor import matrix


def _column_matrix_from_images(lattice, images):
    labels = tuple(lattice.module_generating_set())
    ring = lattice.base_ring()
    return matrix(
        _engine_ring(ring),
        [[_engine_element(ring, image.to_vector()(label)) for image in images] for label in labels],
    )


class EichlerOrthogonalFactorizationDatum(SageObject):
    r"""The exact extension factorization of one ``g in O(2U+K)``.

    The quotient factor is a live lift of the discriminant action of ``g``;
    the residual factor lies in the stable orthogonal group.  Thus the datum
    realizes the standard exact-sequence decomposition by the stable kernel
    and a lift of the finite discriminant action.  It does not identify the
    separately represented finite approximate subgroup with that kernel.
    """

    def __init__(self, isometry, stable_factor, discriminant_lift) -> None:
        if stable_factor * discriminant_lift != isometry:
            raise ValueError(
                f"{stable_factor} and {discriminant_lift} do not factor {isometry}: their product "
                f"is {stable_factor * discriminant_lift}"
            )
        if stable_factor not in isometry.domain().stable_orthogonal_group():
            raise ValueError(
                f"{stable_factor} is not in the stable orthogonal group of "
                f"{isometry.domain()}: it acts nontrivially on the discriminant group"
            )
        if discriminant_lift.discriminant_morphism() != isometry.discriminant_morphism():
            raise ValueError(
                f"{discriminant_lift} does not lift the discriminant action of {isometry}: it "
                f"induces {discriminant_lift.discriminant_morphism()} on the discriminant group "
                f"instead of {isometry.discriminant_morphism()}"
            )
        self._isometry = isometry
        self._stable_factor = stable_factor
        self._discriminant_lift = discriminant_lift

    def isometry(self):
        return self._isometry

    def stable_factor(self):
        return self._stable_factor

    def discriminant_lift(self):
        return self._discriminant_lift

    def reconstruct(self):
        return self.stable_factor() * self.discriminant_lift()

    def __repr__(self) -> str:
        return f"Stable/discriminant factorization of {self.isometry()}"


class TwoUFullGeneratingDatum(SageObject):
    r"""Finite generators supplied by the ``2U`` approximate-model theorem.

    Let ``A`` be the finite-generator approximate subgroup, let ``v`` be the
    selected primitive base vector, and let ``r_i`` run through the approximate
    orbit representatives lying in the full ``O(L)``-orbit of ``v``.  Choose
    ``t_i`` with ``t_i(v)=r_i`` and generators of ``P_v=Stab(v)``.  Since the
    approximate-model oracle says every vector in that full orbit is
    ``A``-equivalent to some ``r_i``, the elementary orbit argument gives

    ``O(L) = < A, P_v, t_i >``.

    The object retains precisely those finite families.  It does not claim a
    word algorithm in the approximate subgroup beyond the sourced oracle.
    """

    def __init__(
        self,
        model,
        square,
        base_vector,
        approximate_generators,
        stabilizer_generators,
        orbit_representatives,
        orbit_transporters,
        generating_family,
    ) -> None:
        self._model = model
        self._square = square
        self._base_vector = base_vector
        self._approximate_generators = approximate_generators
        self._stabilizer_generators = stabilizer_generators
        self._orbit_representatives = orbit_representatives
        self._orbit_transporters = orbit_transporters
        self._generating_family = generating_family

    def model(self):
        return self._model

    def lattice(self):
        return self.model().lattice()

    def square(self):
        return self._square

    def base_vector(self):
        return self._base_vector

    def approximate_generators(self):
        return self._approximate_generators

    def stabilizer_generators(self):
        return self._stabilizer_generators

    def orbit_representatives(self):
        return self._orbit_representatives

    def orbit_transporters(self):
        return self._orbit_transporters

    def generating_family(self):
        return self._generating_family

    def __repr__(self) -> str:
        return f"Finite 2U orthogonal generating datum for {self.lattice()}"


class TwoUEichlerModel(SageObject):
    r"""The represented determinant model ``U + U + K`` used by Eichler's theorem.

    The first four basis vectors are not selected by coordinate position.  They
    are the images of the chosen bases of two explicit hyperbolic-plane
    summands under the biproduct injections.  Under

    ``a e + d f + b e' + c f' |-> [[a,b],[-c,d]]``

    the two copies of ``SL_2(ZZ)`` act by ``X |-> A X`` and
    ``X |-> X B^-1`` respectively.  Those formulas extend by the identity on
    ``K`` and therefore give actual functors ``B SL_2(ZZ) -> Lattices(ZZ)``.
    """

    def __init__(self, orthogonal_complement) -> None:
        from sage.rings.integer_ring import ZZ as SageZZ

        from dzack_research.preamble.categories.lattices import Lattices
        from dzack_research.preamble.categories.rings.ring_foundation import (
            _own_ring,
            _owned_integers,
        )

        ZZ = _owned_integers()
        if orthogonal_complement.base_ring() is not ZZ:
            raise ValueError(
                f"cannot form 2U + K with K = {orthogonal_complement}: the Eichler model needs K "
                f"to be a lattice over ZZ, but its base ring is {orthogonal_complement.base_ring()}"
            )
        if not orthogonal_complement.is_even():
            raise ValueError(
                f"cannot form 2U + K with K = {orthogonal_complement}: the Eichler model needs K "
                f"to be even, and it is not"
            )
        category = Lattices(ZZ)
        plane = category("U")
        self._orthogonal_complement = orthogonal_complement
        self._lattice = category.biproduct((plane, plane, orthogonal_complement))
        self._hyperbolic_inclusions = (self._lattice.injection(0), self._lattice.injection(1))
        self._selected_complement_inclusion = self._lattice.injection(2)

    @classmethod
    def from_represented_biproduct(cls, lattice):
        r"""Select two represented U factors and retain every other summand."""
        from dzack_research.preamble.categories.lattices import Lattices

        category = Lattices(lattice.base_ring())
        if not lattice.is_even():
            raise ValueError("the Eichler determinant model requires an even lattice")
        plane = category("U")
        inclusions = []

        def descend(factor, inclusion):
            if factor.decomposition() is None:
                inclusions.append(inclusion)
            else:
                for index in factor.biproduct_factors().index_set():
                    child = factor.biproduct_factors().value(index)
                    descend(child, inclusion * factor.injection(index))

        descend(lattice, lattice.identity_morphism())
        positions = tuple(
            index for index, inclusion in enumerate(inclusions)
            if int(inclusion.domain().rank()) == 2
            and inclusion.domain().is_unimodular()
            and tuple(int(value) for value in inclusion.domain().signature_pair()) == (1, 1)
        )
        if len(positions) < 2:
            raise ValueError("a represented 2U model needs two hyperbolic-plane factors")
        selected = positions[:2]
        remaining = tuple(inclusion for index, inclusion in enumerate(inclusions) if index not in selected)
        if not remaining:
            complement = category(lattice.base_ring().free_module(0))
        elif len(remaining) == 1:
            complement = remaining[0].domain()
        else:
            complement = category.biproduct(tuple(inclusion.domain() for inclusion in remaining))
        images = tuple(inclusion(point) for inclusion in remaining for point in inclusion.domain().module_generators())
        result = cls.__new__(cls)
        result._orthogonal_complement = complement
        result._lattice = lattice
        plane_inclusions = []
        for index in selected:
            inclusion = inclusions[index]
            factor = inclusion.domain()
            if factor.gram_tensor() == plane.gram_tensor():
                first, second = tuple(factor.module_generators())
            else:
                first = factor.isotropic_vector().primitive_part()
                second = first.hyperbolic_partner()
            plane_inclusions.append(plane.Emb(lattice)((inclusion(first), inclusion(second))))
        result._hyperbolic_inclusions = tuple(plane_inclusions)
        result._selected_complement_inclusion = complement.Emb(lattice)(images)
        return result

    def lattice(self):
        return self._lattice

    def orthogonal_complement(self):
        return self._orthogonal_complement

    def complement_inclusion(self):
        r"""The selected isometric inclusion K -> L, including K=0."""
        return self._selected_complement_inclusion

    def first_hyperbolic_plane(self):
        return self._hyperbolic_inclusions[0].domain()

    def second_hyperbolic_plane(self):
        return self._hyperbolic_inclusions[1].domain()

    def _embedded_hyperbolic_basis(self):
        first = self.first_hyperbolic_plane()
        second = self.second_hyperbolic_plane()
        first_inclusion, second_inclusion = self._hyperbolic_inclusions
        first_basis = tuple(first.module_generators())
        second_basis = tuple(second.module_generators())
        return (
            first_inclusion(first_basis[0]),
            first_inclusion(first_basis[1]),
            second_inclusion(second_basis[0]),
            second_inclusion(second_basis[1]),
        )

    def hyperbolic_basis(self):
        r"""Return the selected embedded basis ``(e,f,e',f')`` of ``U + U``."""
        return self._embedded_hyperbolic_basis()

    def _embedded_complement_basis(self):
        complement = self.orthogonal_complement()
        if int(complement.module_rank()) == 0:
            return ()
        inclusion = self.complement_inclusion()
        return tuple(inclusion(generator) for generator in complement.module_generators())

    def _sl2_entries(self, element):
        r"""Return the exact entries of an owned ``SL_2(ZZ)`` element."""
        matrix = _matrix_group_element_matrix(element.parent(), element)
        ring = self.lattice().base_ring()
        return tuple(
            _owned_engine_element(ring, matrix[row, column])
            for row in range(2)
            for column in range(2)
        )

    def _isometry_on_model_basis(self, images):
        r"""Extend images of the selected 2U+K basis in the ambient presentation."""
        lattice = self.lattice()
        basis = self.hyperbolic_basis() + self._embedded_complement_basis()
        change = _column_matrix_from_images(lattice, basis)
        transformation = _column_matrix_from_images(lattice, images) * change.inverse()
        return lattice.O()._isometry_from_column_matrix(transformation)

    def _left_isometry(self, element):
        r"""Return the isometry induced by ``X |-> A X`` on the determinant model."""
        p, q, r, s = self._sl2_entries(element)
        lattice = self.lattice()
        e, f, e_prime, f_prime = self._embedded_hyperbolic_basis()
        images = (
            lattice.scalar_multiple(p, e) - lattice.scalar_multiple(r, f_prime),
            lattice.scalar_multiple(s, f) + lattice.scalar_multiple(q, e_prime),
            lattice.scalar_multiple(p, e_prime) + lattice.scalar_multiple(r, f),
            lattice.scalar_multiple(s, f_prime) - lattice.scalar_multiple(q, e),
        ) + self._embedded_complement_basis()
        return self._isometry_on_model_basis(images)

    def _right_isometry(self, element):
        r"""Return the isometry induced by ``X |-> X B^-1`` on the determinant model."""
        p, q, r, s = self._sl2_entries(element)
        lattice = self.lattice()
        e, f, e_prime, f_prime = self._embedded_hyperbolic_basis()
        images = (
            lattice.scalar_multiple(s, e) - lattice.scalar_multiple(q, e_prime),
            lattice.scalar_multiple(p, f) + lattice.scalar_multiple(r, f_prime),
            lattice.scalar_multiple(p, e_prime) - lattice.scalar_multiple(r, e),
            lattice.scalar_multiple(s, f_prime) + lattice.scalar_multiple(q, f),
        ) + self._embedded_complement_basis()
        return self._isometry_on_model_basis(images)

    def left_action(self, element):
        r"""Return the left ``SL_2(ZZ)`` action isometry attached to ``element``."""
        element = self.special_linear_group()(element)
        return self._left_isometry(element)

    def right_action(self, element):
        r"""Return the right ``SL_2(ZZ)`` action isometry attached to ``element``."""
        element = self.special_linear_group()(element)
        return self._right_isometry(element)

    def complement_action(self, isometry):
        r"""Extend ``h in O(K)`` by the identity on the selected ``2U`` summand.

        Since ``2U`` is unimodular, ``A_{2U+K}`` identifies with ``A_K`` and
        these extensions induce exactly the subgroup ``tau O(K)`` of
        discriminant automorphisms coming from actual isometries of ``K``.
        This does not assert that every element of ``O(A_K)`` lifts.
        """
        complement = self.orthogonal_complement()
        isometry = complement.O()(isometry)
        inclusion = self.complement_inclusion()
        images = self.hyperbolic_basis() + tuple(
            inclusion(isometry(generator)) for generator in complement.module_generators()
        )
        return self._isometry_on_model_basis(images)

    @cached_method
    def special_linear_group(self):
        from dzack_research.preamble.categories.group.groups import Groups

        return Groups.SL(2, self.lattice().base_ring())

    @cached_method
    def left_action_functor(self):
        r"""Return ``B SL_2(ZZ) -> Lattices(ZZ)`` for left multiplication."""
        from dzack_research.preamble.categories.functors.group_actions import (
            GroupActionFunctor,
        )
        from dzack_research.preamble.categories.lattices import Lattices

        return GroupActionFunctor(
            self.special_linear_group(),
            Lattices(self.lattice().base_ring()),
            self.lattice(),
            self._left_isometry,
        )

    @cached_method
    def right_action_functor(self):
        r"""Return ``B SL_2(ZZ) -> Lattices(ZZ)`` for right multiplication."""
        from dzack_research.preamble.categories.functors.group_actions import (
            GroupActionFunctor,
        )
        from dzack_research.preamble.categories.lattices import Lattices

        return GroupActionFunctor(
            self.special_linear_group(),
            Lattices(self.lattice().base_ring()),
            self.lattice(),
            self._right_isometry,
        )

    @cached_method
    def complement_action_functor(self):
        r"""Return ``B O(K) -> Lattices(ZZ)`` by identity extension on ``2U``."""
        from dzack_research.preamble.categories.functors.group_actions import (
            GroupActionFunctor,
        )
        from dzack_research.preamble.categories.lattices import Lattices

        complement = self.orthogonal_complement()
        return GroupActionFunctor(
            complement.O(),
            Lattices(self.lattice().base_ring()),
            self.lattice(),
            self.complement_action,
        )

    def eichler_transvection(self, isotropic, orthogonal):
        r"""Return the existing exact Eichler transvection in this ``2U`` lattice."""
        return self.lattice().eichler_transvection(isotropic, orthogonal)

    def complement_eichler_transvections(self):
        r"""Return ``E_{e,x}`` for the selected ``K`` framing and first isotropic ``e``.

        This is the represented ``K``-direction part of the source-defined
        Eichler generating family.  It is not named as the full approximate
        subgroup ``A(L)``: that subgroup also requires the separately specified
        lifts of the relevant automorphisms of the discriminant data of ``K``.
        """
        from dzack_research.preamble.categories.sets.indexed_families import (
            finite_indexed_family,
        )

        lattice = self.lattice()
        complement = self.orthogonal_complement()
        complement_inclusion = self.complement_inclusion()
        isotropic = self.hyperbolic_basis()[0]
        return finite_indexed_family(
            complement.module_generating_set(),
            lambda label: self.eichler_transvection(
                isotropic,
                complement_inclusion(complement.module_generator(label)),
            ),
            name=f"K-direction Eichler transvections in {lattice}",
        )

    def approximate_generating_family(self):
        r"""Dispatch the specialized split-2U generating search to its port owner."""
        from sage_indefinite_port.indefinite.eichler import OrbitCoverModel

        return OrbitCoverModel.split_generating_family(self)

    def approximate_generating_family_after_base_change(self, ring_map):
        r"""Extend the supplied approximate family along the stated scalar map."""
        from dzack_research.preamble.categories.sets.indexed_families import finite_indexed_family

        if ring_map.domain() is not self.lattice().base_ring():
            raise ValueError("the scalar map must start at the model's coefficient ring")
        family = self.approximate_generating_family()
        return finite_indexed_family(
            family.index_set(),
            lambda label: family.value(label).base_change(ring_map),
            name=f"Eichler approximate generators over {ring_map.codomain()}",
        )

    def covering_vector_representatives(self, square):
        r"""Dispatch the prescribed-invariant covering search to its port owner."""
        from sage_indefinite_port.indefinite.eichler import OrbitCoverModel

        return OrbitCoverModel.split_covering_vectors(self, square)

    def discriminant_generator_lifts(self):
        r"""Return live lifts in ``O(2U+K)`` of generators of ``O(A_K)``.

        The discriminant form of ``2U+K`` is canonically the one of ``K``.
        This method asks the actual arithmetic orthogonal-group generators to
        lift each generator of the full finite orthogonal group of that
        discriminant form.  It therefore succeeds exactly when the computed
        discriminant representation is surjective; otherwise it refuses
        rather than replacing the missing lift by a formal discriminant action.
        """
        from dzack_research.preamble.categories.sets.indexed_families import (
            finite_indexed_family,
        )

        lattice = self.lattice()
        discriminant_orthogonal_group = lattice.discriminant_group().O()
        generators = discriminant_orthogonal_group.group_generators()

        def lift(generator):
            witness = lattice.O().discriminant_lift(generator)
            assert witness is not None, (
                f"cannot lift {generator} from O(A_L) to O(L) for L = {lattice}: no isometry of "
                f"L was found that induces it, so O(L) -> O(A_L) is not known to be surjective "
                f"on the generators of O(A_L)"
            )
            if witness.discriminant_morphism() != generator:
                raise ArithmeticError(
                    f"{witness} does not lift {generator}: it induces "
                    f"{witness.discriminant_morphism()} on the discriminant group of {lattice}"
                )
            return witness

        return finite_indexed_family(
            generators,
            lift,
            name=f"Discriminant-generator lifts in O({lattice})",
        )

    def stable_kernel(self):
        r"""Return ``ker(O(L) -> O(A_L))``, the stable orthogonal subgroup."""
        return self.lattice().stable_orthogonal_group()

    def factor_orthogonal_isometry(self, isometry):
        r"""Factor ``g`` as a stable-kernel factor times a discriminant lift.

        This is the exact-sequence factorization for the represented ``2U`` construction.
        The finite discriminant image is enumerated from exact generators of
        ``O(L)`` while retaining a live lift.  Since the selected image is the
        image of ``g`` itself, failure to lift is an arithmetic inconsistency,
        not a supported ``None`` branch.
        """
        orthogonal_group = self.lattice().O()
        isometry = orthogonal_group(isometry)
        quotient_action = isometry.discriminant_morphism()
        quotient_lift = orthogonal_group.discriminant_lift(quotient_action)
        if quotient_lift is None:
            raise ArithmeticError(
                f"cannot factor {isometry}: its action {quotient_action} on the discriminant group "
                f"of {self.lattice()} was not found in the image of O(L) -> O(A_L), although it "
                f"is the image of {isometry}"
            )
        stable_factor = isometry * ~quotient_lift
        if stable_factor not in self.stable_kernel():
            raise ArithmeticError(
                f"cannot factor {isometry}: dividing by the lift {quotient_lift} of its discriminant "
                f"action leaves {stable_factor}, which is not in the stable orthogonal group"
            )
        return EichlerOrthogonalFactorizationDatum(
            isometry,
            stable_factor,
            quotient_lift,
        )

    def source_generating_family(self):
        r"""Return the represented source-defined finite family inside ``O(2U+K)``.

        The family retains five mathematically different sources of
        isometries: the two determinant-model ``SL_2(ZZ)`` actions, the
        chosen generators of ``O(K)`` extended by the identity on ``2U``,
        the selected ``K``-direction Eichler transvections, and explicit
        lifts of generators of ``O(A_L)``.  Labels retain those sources even
        when two labels happen to determine the same lattice isometry.

        This is generating *data*, not a claim that the generated subgroup is
        the full orthogonal group.  That equality belongs to the recursive
        generation theorem and its parabolic-stabilizer hypotheses.
        """
        from dzack_research.preamble.categories.sets.finite_ordered_sets import (
            finite_ordered_set,
        )
        from dzack_research.preamble.categories.sets.indexed_families import (
            finite_indexed_family,
        )

        special_linear_generators = self.special_linear_group().group_generators()
        complement_generators = self.orthogonal_complement().O().group_generators()
        eichler = self.complement_eichler_transvections()
        discriminant_lifts = self.discriminant_generator_lifts()
        labels = finite_ordered_set(
            tuple(("left-SL2", generator) for generator in special_linear_generators)
            + tuple(("right-SL2", generator) for generator in special_linear_generators)
            + tuple(("O(K)", generator) for generator in complement_generators)
            + tuple(("Eichler", label) for label in eichler.index_set())
            + tuple(("discriminant-lift", label) for label in discriminant_lifts.index_set())
        )

        def generator(label):
            kind, datum = label
            match kind:
                case "left-SL2":
                    return self.left_action(datum)
                case "right-SL2":
                    return self.right_action(datum)
                case "O(K)":
                    return self.complement_action(datum)
                case "Eichler":
                    return eichler[datum]
                case "discriminant-lift":
                    return discriminant_lifts[datum]
                case _:
                    raise ValueError(
                        f"{label!r} does not name a generator of O(2U + K) for {self}: its kind "
                        f"{kind!r} is not a known kind of generator"
                    )

        return finite_indexed_family(
            labels,
            generator,
            name=f"Source-defined Eichler generating family in O({self.lattice()})",
        )

    def full_generating_data(self, square):
        r"""Dispatch the specialized approximate-model generation theorem to the port."""
        from sage_indefinite_port.indefinite.eichler import OrbitCoverModel

        return OrbitCoverModel.split_full_generating_data(self, square)


__all__ = [
    "EichlerOrthogonalFactorizationDatum",
    "TwoUEichlerModel",
    "TwoUFullGeneratingDatum",
]
