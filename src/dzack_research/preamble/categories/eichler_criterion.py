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


class EichlerCoveringOrbitDatum(SageObject):
    r"""One explicit covering vector together with its recursive orbit data.

    A covering discriminant class need not be a distinct full ``O(L)`` orbit.
    This object therefore retains both the vector constructed from that class
    and the actual full-orbit representative selected by the indefinite
    backend, together with a transporter between them and generators of the
    covering vector's stabilizer ``P_v``.
    """

    def __init__(
        self,
        discriminant_class,
        representative,
        stabilizer_generators,
        full_orbit_representative,
        transporter,
    ) -> None:
        match transporter(representative) == full_orbit_representative:
            case True:
                pass
            case False:
                raise ValueError(
                    "the retained transporter moves the covering vector to the wrong orbit representative"
                )
        match any(generator(representative) != representative for generator in stabilizer_generators):
            case False:
                pass
            case True:
                raise ValueError(
                    "a retained covering stabilizer generator does not fix its vector"
                )
        self._discriminant_class = discriminant_class
        self._representative = representative
        self._stabilizer_generators = stabilizer_generators
        self._full_orbit_representative = full_orbit_representative
        self._transporter = transporter

    def discriminant_class(self):
        return self._discriminant_class

    def representative(self):
        return self._representative

    def stabilizer_generators(self):
        return self._stabilizer_generators

    def full_orbit_representative(self):
        return self._full_orbit_representative

    def transporter_to_full_orbit(self):
        return self._transporter

    def __repr__(self) -> str:
        return f"Eichler covering orbit datum for {self.discriminant_class()}"


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
        from dzack_research.preamble.categories.lattices import Lattices
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
        from sage.rings.integer_ring import ZZ as SageZZ

        ZZ = _own_ring(SageZZ)
        if orthogonal_complement.base_ring() is not ZZ:
            raise ValueError("the 2U Eichler model is currently integral over ZZ")
        if not orthogonal_complement.is_even():
            raise ValueError("the Eichler model requires an even orthogonal complement")
        category = Lattices(ZZ)
        plane = category("U")
        self._orthogonal_complement = orthogonal_complement
        self._lattice = category.biproduct((plane, plane, orthogonal_complement))

    def lattice(self):
        return self._lattice

    def orthogonal_complement(self):
        return self._orthogonal_complement

    def first_hyperbolic_plane(self):
        return self.lattice().biproduct_factor(0)

    def second_hyperbolic_plane(self):
        return self.lattice().biproduct_factor(1)

    def _embedded_hyperbolic_basis(self):
        lattice = self.lattice()
        first = self.first_hyperbolic_plane()
        second = self.second_hyperbolic_plane()
        first_inclusion = lattice.injection(0)
        second_inclusion = lattice.injection(1)
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
        lattice = self.lattice()
        complement = self.orthogonal_complement()
        inclusion = lattice.injection(2)
        return tuple(inclusion(generator) for generator in complement.module_generators())

    def _sl2_entries(self, element):
        r"""Return the exact entries of an owned ``SL_2(ZZ)`` element."""
        matrix = element._backend().matrix()
        ring = self.lattice().base_ring()
        return tuple(ring(matrix[row, column]) for row in range(2) for column in range(2))

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
        return lattice.O()(images)

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
        return lattice.O()(images)

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
        lattice = self.lattice()
        inclusion = lattice.injection(2)
        images = self.hyperbolic_basis() + tuple(
            inclusion(isometry(generator)) for generator in complement.module_generators()
        )
        return lattice.O()(images)

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
        complement_inclusion = lattice.injection(2)
        isotropic = self.hyperbolic_basis()[0]
        return finite_indexed_family(
            complement.module_generating_set(),
            lambda label: self.eichler_transvection(
                isotropic,
                complement_inclusion(complement.module_generator(label)),
            ),
            name=f"K-direction Eichler transvections in {lattice}",
        )

    def covering_vector_representatives(self, square):
        r"""Return one explicit primitive vector for every covering class in ``A_K``.

        Since ``2U`` is unimodular, ``A_{2U+K} = A_K``.  For a covering
        class ``x`` of order ``d``, choose its selected lift ``y in K^#`` and
        put ``k=d*y in K``.  The defining discriminant-form equality says

        ``square-k^2 = 2 d^2 m``

        for an integer ``m``.  Then ``v=d e+d m f+k`` has square ``square``,
        divisibility exactly ``d``, is primitive, and has divided class ``x``
        under the canonical discriminant identification.
        """
        from dzack_research.preamble.categories.sets.indexed_families import (
            finite_indexed_family,
        )

        lattice = self.lattice()
        ring = lattice.base_ring()
        square = ring(square)
        complement = self.orthogonal_complement()
        discriminant = complement.discriminant_group()
        covering = covering_discriminant_classes(complement, square)
        correlation = complement.correlation_morphism()
        complement_inclusion = lattice.injection(2)
        e, f, _e_prime, _f_prime = self.hyperbolic_basis()

        def representative(discriminant_class):
            discriminant_class = discriminant(discriminant_class)
            order = ring(int(discriminant_class.additive_order()))
            dual_lift = discriminant.dual_lattice_lift(discriminant_class)
            scaled_dual = dual_lift.parent().scalar_multiple(order, dual_lift)
            complement_vector = correlation.lift(scaled_dual)
            denominator = ring(2) * order * order
            numerator = square - complement.q(complement_vector)
            coefficient = numerator // denominator
            if denominator * coefficient != numerator:
                raise ArithmeticError(
                    "a covering discriminant class did not produce the required integral hyperbolic coefficient"
                )
            vector = (
                lattice.scalar_multiple(order, e)
                + lattice.scalar_multiple(order * coefficient, f)
                + complement_inclusion(complement_vector)
            )
            if vector.q() != square:
                raise ArithmeticError("the constructed covering vector has the wrong square")
            if vector.div() != order:
                raise ArithmeticError("the constructed covering vector has the wrong divisibility")
            if not vector.is_primitive():
                raise ArithmeticError("the constructed covering vector is not primitive")
            if complement.discriminant_class(dual_lift) != discriminant_class:
                raise ArithmeticError("the selected dual lift represents the wrong discriminant class")
            return vector

        return finite_indexed_family(
            covering,
            representative,
            name=f"Eichler covering representatives of square {square} in {lattice}",
        )

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
            if witness is None:
                raise NotImplementedError(
                    "the represented orthogonal-group generators do not surject onto O(A_L)"
                )
            if witness.discriminant_morphism() != generator:
                raise ArithmeticError("a discriminant lift induces the wrong finite-form automorphism")
            return witness

        return finite_indexed_family(
            generators,
            lift,
            name=f"Discriminant-generator lifts in O({lattice})",
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
                    raise ValueError(f"unknown 2U source-generator label {kind!r}")

        return finite_indexed_family(
            labels,
            generator,
            name=f"Source-defined Eichler generating family in O({self.lattice()})",
        )

    def covering_orbit_data(self, square):
        r"""Return exact stabilizer/transporter data for every covering class.

        The finite discriminant list indexes explicitly constructed primitive
        vectors.  For each one, the exact indefinite backend supplies
        generators of its full-orthogonal stabilizer and a transporter to one
        of the backend's full ``O(L)`` orbit representatives.  Several covering
        classes are allowed to land in the same full orbit; this method records
        that fact instead of quotienting the covering list prematurely.
        """
        from dzack_research.preamble.categories.sets.indexed_families import (
            finite_indexed_family,
        )

        lattice = self.lattice()
        orthogonal_group = lattice.O()
        representatives = self.covering_vector_representatives(square)
        full_orbits = tuple(orthogonal_group.vector_orbit_representatives(square))

        def datum(discriminant_class):
            vector = representatives[discriminant_class]
            stabilizer_generators = orthogonal_group.vector_stabilizer_generators(vector)
            for full_representative in full_orbits:
                transporter = orthogonal_group.vector_equivalence_witness(
                    vector,
                    full_representative,
                )
                match transporter:
                    case None:
                        continue
                    case _:
                        return EichlerCoveringOrbitDatum(
                            discriminant_class,
                            vector,
                            stabilizer_generators,
                            full_representative,
                            transporter,
                        )
            raise ArithmeticError(
                "an explicit covering vector did not belong to any full orthogonal-group orbit returned by the backend"
            )

        return finite_indexed_family(
            representatives.index_set(),
            datum,
            name=f"Recursive covering-orbit data of square {square} in {lattice}",
        )

    def isometry_to(self, other):
        r"""Return the represented recursive isometry ``2U+K -> 2U+K'``.

        The selected two hyperbolic planes are carried identically to the
        selected two hyperbolic planes of ``other``.  The only recursive
        problem is therefore the complement isometry ``K -> K'``; when that
        owner returns a witness, the orthogonal direct sum of the three maps
        is an actual lattice isometry.  This decreases rank by four and does
        not assert the separate generation theorem for ``O(2U+K)``.
        """
        if not isinstance(other, TwoUEichlerModel):
            raise TypeError("a represented 2U recursion compares two TwoUEichlerModel objects")
        source = self.lattice()
        target = other.lattice()
        if source.base_ring() is not target.base_ring():
            return None
        complement_isometry = self.orthogonal_complement().isometry_to(
            other.orthogonal_complement()
        )
        if complement_isometry is None:
            return None
        target_first = other.first_hyperbolic_plane()
        target_second = other.second_hyperbolic_plane()
        first_inclusion = target.injection(0)
        second_inclusion = target.injection(1)
        complement_inclusion = target.injection(2)
        first_labels = target_first.module_generating_set()
        second_labels = target_second.module_generating_set()
        images = (
            tuple(first_inclusion(target_first.module_generator(label)) for label in first_labels)
            + tuple(second_inclusion(target_second.module_generator(label)) for label in second_labels)
            + tuple(
                complement_inclusion(
                    complement_isometry(
                        self.orthogonal_complement().module_generator(label)
                    )
                )
                for label in self.orthogonal_complement().module_generating_set()
            )
        )
        if len(images) != int(source.module_rank()):
            raise ArithmeticError("the recursive 2U isometry does not specify one image per source generator")
        result = source.Isom(target)(images)
        if any(
            result(left) != right
            for left, right in zip(
                self.hyperbolic_basis(), other.hyperbolic_basis(), strict=True
            )
        ):
            raise ArithmeticError("the recursive 2U isometry moves a selected hyperbolic basis")
        source_complement_inclusion = source.injection(2)
        if any(
            result(source_complement_inclusion(generator))
            != complement_inclusion(complement_isometry(generator))
            for generator in self.orthogonal_complement().module_generators()
        ):
            raise ArithmeticError("the recursive 2U isometry disagrees with its complement witness")
        return result

    def is_isometric_to(self, other) -> bool:
        r"""Return the exact represented ``2U`` isometry decision when known."""
        if not isinstance(other, TwoUEichlerModel):
            return False
        if self.lattice().base_ring() is not other.lattice().base_ring():
            return False
        return self.orthogonal_complement().is_isometric_to(
            other.orthogonal_complement()
        )


def two_u_eichler_model(orthogonal_complement):
    r"""Return the represented ``U + U + K`` determinant model for ``K``."""
    return TwoUEichlerModel(orthogonal_complement)


def covering_discriminant_classes(lattice, square):
    r"""Return the discriminant classes covering the primitive vectors of ``square``.

    For a primitive ``v`` write ``d = div(v)``, so ``v/d`` lies in ``L^#`` and
    ``x = [v/d]`` lies in ``A_L``.  The order of ``x`` is exactly ``d``: a
    smaller order ``e`` would put ``(e/d) v`` in ``L`` and contradict
    primitivity.  The discriminant quadratic form then reads
    ``q_{A_L}(x) = q(v)/d^2`` in ``K/2R``.  Both statements are unconditional,
    so the classes satisfying

    ``q_{A_L}(x) = square / ord(x)^2``

    cover the primitive vectors of that square: every such vector has its
    divided class among them, with its divisibility the order of that class.
    This is the finite covering list, and it is computed by one pass over the
    finite discriminant group with no search in ``L``.

    Under Eichler's criterion the list is sharper still: the stable orthogonal
    group is then transitive on the primitive vectors sharing a square and a
    divided class, so each class in the list carries at most one stable orbit.
    Which classes are actually attained is a separate question this list does
    not answer, which is why it covers rather than enumerates.
    """
    from dzack_research.preamble.categories.sets.finite_ordered_sets import (
        finite_ordered_set,
    )

    discriminant = lattice.discriminant_group()
    values = discriminant.quadratic_value_module()
    field = lattice.base_ring().fraction_field()
    target = field(square)
    return finite_ordered_set(
        tuple(
            element
            for element in discriminant.elements()
            if discriminant.q(element)
            == values(target / field(element.additive_order()) ** 2)
        )
    )


def hyperbolic_plane_summand_count(lattice):
    r"""Return how many indecomposable summands of ``lattice`` are hyperbolic planes."""
    from dzack_research.preamble.categories.lattices import Lattices

    plane = Lattices(lattice.base_ring())("U")
    return sum(
        1 for summand in lattice.indecomposable_summands() if summand.is_isometric(plane)
    )


def splits_two_hyperbolic_planes(lattice) -> bool:
    r"""Return whether the represented decomposition has two hyperbolic-plane summands.

    This is the hypothesis of Eichler's criterion, read off the decomposition
    the lattice was built with.  A lattice presented only by a Gram matrix has
    no represented decomposition and answers ``False`` even when it is
    abstractly isometric to one that splits ``U + U``.
    """
    if not lattice.is_decomposable():
        return False
    return hyperbolic_plane_summand_count(lattice) >= 2


def eichler_criterion_applies(lattice) -> bool:
    r"""Return whether Eichler's criterion classifies primitive-vector orbits here."""
    return bool(lattice.is_even()) and splits_two_hyperbolic_planes(lattice)


def are_in_one_stable_orbit(left, right) -> bool:
    r"""Decide whether two primitive vectors share a ``ker(rho_L)`` orbit.

    The decision is Eichler's: under the criterion's hypothesis the square,
    the divisibility and the divided discriminant class are a complete
    invariant of the orbit.  Both vectors are required to be primitive,
    because the criterion is a statement about primitive vectors.
    """
    lattice = left.parent()
    assert right.parent() is lattice, (
        "an orbit comparison is between two vectors of one lattice"
    )
    assert eichler_criterion_applies(lattice), (
        "Eichler's criterion classifies primitive-vector orbits for an even "
        "lattice splitting two hyperbolic planes; this lattice does not "
        "present such a decomposition, and the orbit question is then a "
        "computation for the exact indefinite backend rather than a "
        "comparison of invariants"
    )
    for vector in (left, right):
        assert lattice.subobject_on((vector,)).is_primitive(), (
            "Eichler's criterion compares primitive vectors"
        )
    return (
        left.q() == right.q()
        and left.div() == right.div()
        and left.divided_discriminant_class() == right.divided_discriminant_class()
    )


__all__ = [
    "EichlerCoveringOrbitDatum",
    "TwoUEichlerModel",
    "are_in_one_stable_orbit",
    "covering_discriminant_classes",
    "eichler_criterion_applies",
    "hyperbolic_plane_summand_count",
    "splits_two_hyperbolic_planes",
    "two_u_eichler_model",
]
