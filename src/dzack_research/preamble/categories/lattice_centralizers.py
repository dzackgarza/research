r"""The primitive extension cut out by a lattice isometry, and its centralizer.

For an isometry ``f`` of a nondegenerate lattice ``L`` the invariant lattice
``L^f`` and its orthogonal complement are primitive sublattices whose
orthogonal sum sits in ``L`` with finite index.  Nikulin's correspondence
presents that primitive extension by the anti-isometry

``gamma : H_+ -> H_-(-1)``,   ``H_+ <= A_{L^f}``,  ``H_- <= A_{(L^f)^perp}``,

whose graph is ``L/(L^f + (L^f)^perp)``.  The centralizer ``O(L,f)`` is then
the group of pairs ``(g_+, g_-)`` in ``O(L^f) x O((L^f)^perp)`` whose induced
discriminant automorphisms commute with ``gamma``, equivalently which carry
the graph onto itself.

This object is the isometry-cut sibling of ``VectorPrimitiveExtension``, which
records the same primitive-extension data for the decomposition cut out by one
anisotropic vector.  The two share the owned pieces they stand on: the
invariant lattice and formed coinvariants of the isometry, ``glue_map`` for
the anti-isometry, and ``centralizer`` for the subgroup.

What this file adds is the decomposition as one object, both halves of that
isomorphism -- the restriction morphisms ``O(L,f) -> O(L^f)`` and
``O(L,f) -> O((L^f)^perp)`` forwards, and ``centralizer_element`` back -- and
the cyclotomic summands ``ker Phi_d(f)`` of a finite-order isometry.
"""

from sage.arith.misc import divisors
from sage.misc.cachefunc import cached_method
from sage.misc.unknown import Unknown
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.orthogonal_quotients import (
    _finite_supergroup_elements,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import finite_indexed_family


class EquivariantVectorOrbit(SageObject):
    r"""One orbit of a vector under the centralizer of an equipped isometry."""

    def __init__(self, decorated_lattice, representative, centralizer_elements) -> None:
        self._decorated_lattice = decorated_lattice
        self._representative = representative
        self._centralizer_elements = tuple(centralizer_elements)

    def decorated_lattice(self):
        return self._decorated_lattice

    def group(self):
        return self.decorated_lattice().centralizer_group()

    def representative(self):
        return self._representative

    def stabilizer(self):
        r"""Return the exact point stabilizer inside ``O(L,f)``."""
        from dzack_research.preamble.categories.group.predicate_subgroups import (
            StabilizerSubgroups,
        )

        representative = self.representative()
        return StabilizerSubgroups(self.group())(
            representative,
            "pointwise",
            lambda automorphism: automorphism(representative) == representative,
            description=f"g fixes {representative}",
        )

    def transporter_from(self, vector):
        r"""Return ``g in O(L,f)`` carrying ``vector`` to the representative."""
        lattice = self.decorated_lattice().lattice()
        if vector.parent() is not lattice:
            vector = lattice(vector)
        for automorphism in self._centralizer_elements:
            if automorphism(vector) == self.representative():
                return automorphism
        return None

    def __contains__(self, vector) -> bool:
        return self.transporter_from(vector) is not None

    def _repr_(self) -> str:
        return f"Orbit of {self.representative()} under {self.group()}"



class EquivariantVectorOrbitDecomposition(SageObject):
    r"""The exact vector-orbit decomposition under ``O(L,f)`` when finite.

    The centralizer of ``f`` is listed only when the full orthogonal group is
    finite, equivalently in the definite regime supported by the existing
    subgroup engine.  No finite approximation is used for an indefinite
    arithmetic centralizer.
    """

    def __init__(self, decorated_lattice, square) -> None:
        self._decorated_lattice = decorated_lattice
        self._square = decorated_lattice.lattice().base_ring()(square)
        centralizer = decorated_lattice.centralizer_group()
        elements = _finite_supergroup_elements(centralizer)
        self._centralizer_elements = tuple(elements)
        remaining = {tuple(vector.to_tuple()): vector for vector in decorated_lattice.lattice().vectors_of_square(self._square)}
        orbits = []
        while remaining:
            _coordinates, representative = next(iter(remaining.items()))
            orbit = EquivariantVectorOrbit(
                decorated_lattice,
                representative,
                elements,
            )
            orbits.append(orbit)
            for automorphism in elements:
                remaining.pop(tuple(automorphism(representative).to_tuple()), None)
        self._orbits = finite_ordered_set(tuple(orbits))

    def decorated_lattice(self):
        return self._decorated_lattice

    def square(self):
        return self._square

    def group(self):
        return self.decorated_lattice().centralizer_group()

    def orbits(self):
        return self._orbits

    def representatives(self):
        return finite_ordered_set(tuple(orbit.representative() for orbit in self.orbits()))

    def orbit_of(self, vector):
        lattice = self.decorated_lattice().lattice()
        if vector.parent() is not lattice:
            vector = lattice(vector)
        if vector.q() != self.square():
            raise ValueError("orbit_of requires a vector of the selected square")
        for orbit in self.orbits():
            if vector in orbit:
                return orbit
        raise ArithmeticError("the exact centralizer orbit list did not cover the square shell")

    def stabilizer(self, representative):
        return self.orbit_of(representative).stabilizer()

    def transporter(self, source, target):
        source_orbit = self.orbit_of(source)
        target_orbit = self.orbit_of(target)
        if source_orbit is not target_orbit:
            return None
        lattice = self.decorated_lattice().lattice()
        if source.parent() is not lattice:
            source = lattice(source)
        if target.parent() is not lattice:
            target = lattice(target)
        for automorphism in self._centralizer_elements:
            if automorphism(source) == target:
                return automorphism
        raise ArithmeticError("one centralizer orbit has no transporter between two of its members")

    def _repr_(self) -> str:
        return f"Vector orbits of square {self.square()} under {self.group()}: {self.representatives()}"



def _same_embedded_sublattice(left, right) -> bool:
    if left.ambient_lattice() is not right.ambient_lattice():
        return False
    try:
        left.inclusion().factor_through(right.inclusion())
        right.inclusion().factor_through(left.inclusion())
    except (AttributeError, TypeError, ValueError):
        return False
    return True


def _transport_sublattice(automorphism, sublattice):
    return (automorphism * sublattice.inclusion()).image()


class EquivariantSublatticeFlag(SageObject):
    r"""A nested finite flag of represented sublattices stable under ``f``."""

    def __init__(self, decorated_lattice, terms) -> None:
        terms = tuple(terms)
        if not terms:
            raise ValueError("an equivariant sublattice flag has at least one term")
        previous = None
        for term in terms:
            decorated_lattice.equivariant_sublattice(term)
            if previous is not None:
                previous.inclusion().factor_through(term.inclusion())
                if int(previous.module_rank()) >= int(term.module_rank()):
                    raise ValueError("an equivariant flag has strictly increasing ranks")
            previous = term
        self._decorated_lattice = decorated_lattice
        self._terms = terms

    def decorated_lattice(self):
        return self._decorated_lattice

    def lattice(self):
        return self.decorated_lattice().lattice()

    def terms(self):
        return finite_ordered_set(self._terms)

    def ranks(self):
        return finite_ordered_set(tuple(term.module_rank() for term in self._terms))

    def __repr__(self) -> str:
        return f"Equivariant sublattice flag of ranks {tuple(self.ranks())} in {self.lattice()}"


def _same_equivariant_flag(left, right) -> bool:
    left_terms = tuple(left.terms())
    right_terms = tuple(right.terms())
    if len(left_terms) != len(right_terms):
        return False
    return all(_same_embedded_sublattice(source, target) for source, target in zip(left_terms, right_terms, strict=True))


def _transport_equivariant_flag(automorphism, flag):
    decorated = flag.decorated_lattice()
    return EquivariantSublatticeFlag(
        decorated,
        tuple(_transport_sublattice(automorphism, term) for term in flag.terms()),
    )


class _EquivariantFiniteOrbit(SageObject):
    def __init__(self, decomposition, representative, members) -> None:
        self._decomposition = decomposition
        self._representative = representative
        self._members = finite_ordered_set(tuple(members))

    def decomposition(self):
        return self._decomposition

    def group(self):
        return self.decomposition().group()

    def representative(self):
        return self._representative

    def members(self):
        return self._members

    def stabilizer(self):
        from dzack_research.preamble.categories.group.predicate_subgroups import (
            StabilizerSubgroups,
        )

        representative = self.representative()
        decomposition = self.decomposition()
        return StabilizerSubgroups(self.group())(
            representative,
            "on the represented finite family",
            lambda automorphism: decomposition.same(decomposition.act(automorphism, representative), representative),
            description=f"g fixes {representative}",
        )

    def transporter_from(self, source):
        return self.decomposition().transporter(source, self.representative())


class EquivariantFiniteOrbitDecomposition(SageObject):
    r"""Exact centralizer orbits on a supplied finite centralizer-stable family."""

    def __init__(self, decorated_lattice, candidates, action, equality) -> None:
        candidates = tuple(candidates)
        if not candidates:
            raise ValueError("an equivariant finite orbit decomposition needs candidates")
        self._decorated_lattice = decorated_lattice
        self._action = action
        self._equality = equality
        self._centralizer_elements = tuple(_finite_supergroup_elements(decorated_lattice.centralizer_group()))

        for candidate in candidates:
            for automorphism in self._centralizer_elements:
                image = self.act(automorphism, candidate)
                if not any(self.same(image, target) for target in candidates):
                    raise ValueError("the supplied finite family is not stable under the full centralizer")

        remaining = list(candidates)
        orbits = []
        while remaining:
            representative = remaining.pop(0)
            members = []
            for candidate in candidates:
                if any(self.same(self.act(automorphism, representative), candidate) for automorphism in self._centralizer_elements):
                    members.append(candidate)
            remaining = [candidate for candidate in remaining if not any(self.same(candidate, member) for member in members)]
            orbits.append(_EquivariantFiniteOrbit(self, representative, members))
        self._orbits = finite_ordered_set(tuple(orbits))

    def decorated_lattice(self):
        return self._decorated_lattice

    def group(self):
        return self.decorated_lattice().centralizer_group()

    def act(self, automorphism, candidate):
        return self._action(automorphism, candidate)

    def same(self, left, right) -> bool:
        return bool(self._equality(left, right))

    def orbits(self):
        return self._orbits

    def representatives(self):
        return finite_ordered_set(tuple(orbit.representative() for orbit in self.orbits()))

    def orbit_of(self, candidate):
        for orbit in self.orbits():
            if any(self.same(candidate, member) for member in orbit.members()):
                return orbit
        raise ValueError("the selected object is not in the represented finite family")

    def stabilizer(self, candidate):
        return self.orbit_of(candidate).stabilizer()

    def transporter(self, source, target):
        if self.orbit_of(source) is not self.orbit_of(target):
            return None
        for automorphism in self._centralizer_elements:
            if self.same(self.act(automorphism, source), target):
                return automorphism
        raise ArithmeticError("one exact centralizer orbit has no transporter")


def _isometry_power(isometry, exponent):
    r"""Return an exact nonnegative power of one lattice automorphism."""
    exponent = int(exponent)
    if exponent < 0:
        raise ValueError("an isometry power exponent is nonnegative here")
    result = isometry.domain().O().one()
    for _step in range(exponent):
        result = isometry * result
    return result


class CyclotomicDecomposition(SageObject):
    r"""The integral cyclotomic decomposition of a finite-order isometry.

    For an automorphism ``f`` of exact order ``n`` this owns the primitive
    sublattices ``L_d = ker(Phi_d(f))`` for ``d | n`` and the finite-index
    inclusion ``direct_sum_d L_d -> L``.  The finite quotient of that
    inclusion is the integral gluing datum.  Component isometries are allowed
    to act on the summands independently only when they extend across that
    quotient to an actual isometry of ``L`` commuting with ``f``.
    """

    def __init__(self, decorated_lattice, order) -> None:
        self._decorated_lattice = decorated_lattice
        self._order = int(order)
        if self._order <= 0:
            raise ValueError("the order of a finite-order isometry is positive")
        isometry = decorated_lattice.isometry()
        identity = decorated_lattice.lattice().O().one()
        if _isometry_power(isometry, self._order) != identity:
            raise ValueError("the supplied integer does not annihilate the equipped isometry")
        for proper_divisor in divisors(self._order):
            if proper_divisor == self._order:
                continue
            if _isometry_power(isometry, proper_divisor) == identity:
                raise ValueError("the supplied integer is not the exact order of the equipped isometry")

        self._divisors = finite_ordered_set(tuple(divisors(self._order)))
        self._summands = finite_indexed_family(
            self._divisors,
            lambda divisor: isometry.cyclotomic_summand(int(divisor)),
            name=f"Cyclotomic summands of {isometry}",
        )
        nonzero = tuple(divisor for divisor in self._divisors if int(self._summands[divisor].module_rank()) != 0)
        if not nonzero:
            raise ArithmeticError("a finite-order isometry has no nonzero cyclotomic summand")
        self._nonzero_divisors = finite_ordered_set(nonzero)

        lattice = self.lattice()
        total_rank = sum(int(self._summands[divisor].module_rank()) for divisor in self._nonzero_divisors)
        if total_rank != int(lattice.module_rank()):
            raise ArithmeticError("the cyclotomic summands do not span the ambient rational lattice")
        ring = lattice.base_ring()
        zero = ring.zero()
        for left_position, left_divisor in enumerate(self._nonzero_divisors):
            left = self._summands[left_divisor]
            for right_divisor in tuple(self._nonzero_divisors)[left_position + 1 :]:
                right = self._summands[right_divisor]
                if any(
                    lattice.b(left_vector, right_vector) != zero for left_vector in left.embedded_module_generators() for right_vector in right.embedded_module_generators()
                ):
                    raise ArithmeticError("distinct cyclotomic summands are not orthogonal")

    def decorated_lattice(self):
        return self._decorated_lattice

    def lattice(self):
        return self.decorated_lattice().lattice()

    def isometry(self):
        return self.decorated_lattice().isometry()

    def order(self):
        return self._order

    def divisor_set(self):
        return self._divisors

    def summands(self):
        return self._summands

    def summand(self, divisor):
        divisor = self.divisor_set()(divisor)
        return self.summands()[divisor]

    def nonzero_divisors(self):
        return self._nonzero_divisors

    @cached_method
    def orthogonal_sum(self):
        summands = tuple(self.summand(divisor) for divisor in self.nonzero_divisors())
        result = summands[0]
        for summand in summands[1:]:
            result = result + summand
        return result

    @cached_method
    def orthogonal_sum_inclusion(self):
        r"""Return ``direct_sum_d L_d -> L`` with finite-index image."""
        images = []
        for divisor in self.nonzero_divisors():
            summand = self.summand(divisor)
            inclusion = summand.inclusion()
            images.extend(inclusion(generator) for generator in summand.module_generators())
        return self.orthogonal_sum().Emb(self.lattice())(tuple(images))

    def index(self):
        return self.orthogonal_sum_inclusion().index()

    @cached_method
    def gluing_quotient(self):
        r"""Return ``L / direct_sum_d L_d``, the finite integral glue quotient."""
        return self.orthogonal_sum_inclusion().cokernel()

    @cached_method
    def component_isometries(self):
        r"""Return the restrictions ``f_d`` on every nonzero cyclotomic summand."""
        equipped = self.decorated_lattice()
        return finite_indexed_family(
            self.nonzero_divisors(),
            lambda divisor: equipped.equivariant_sublattice(self.summand(divisor)).isometry(),
            name=f"Cyclotomic restrictions of {self.isometry()}",
        )

    @cached_method
    def component_centralizers(self):
        r"""Return ``Z_{O(L_d)}(f_d)`` for every nonzero cyclotomic component."""
        restrictions = self.component_isometries()
        return finite_indexed_family(
            self.nonzero_divisors(),
            lambda divisor: self.summand(divisor).O().centralizer(restrictions[divisor]),
            name=f"Cyclotomic component centralizers of {self.isometry()}",
        )

    def centralizer_group(self):
        r"""Return the actual ambient arithmetic centralizer ``Z_{O(L)}(f)``."""
        return self.decorated_lattice().centralizer_group()

    def restrict_centralizer_element(self, automorphism):
        r"""Restrict one ambient centralizer element to every cyclotomic summand.

        Commutation with ``f`` makes each polynomial kernel
        ``ker(Phi_d(f))`` stable, so every restriction is defined and belongs
        to ``Z_{O(L_d)}(f_d)``.  The result is indexed by the nonzero
        cyclotomic divisors and retains the actual component isometries.
        """
        if automorphism not in self.centralizer_group():
            raise ValueError("a cyclotomic restriction requires an element of the ambient centralizer")
        restrictions = self.component_isometries()
        centralizers = self.component_centralizers()

        def restrict(divisor):
            summand = self.summand(divisor)
            inclusion = summand.inclusion()
            component = summand.O()({label: inclusion.lift(automorphism(inclusion(summand.module_generator(label)))) for label in summand.module_generating_set()})
            if component * restrictions[divisor] != restrictions[divisor] * component:
                raise ArithmeticError("an ambient centralizer restriction does not commute with f_d")
            if component not in centralizers[divisor]:
                raise ArithmeticError("an ambient centralizer restriction left its component centralizer")
            return component

        return finite_indexed_family(
            self.nonzero_divisors(),
            restrict,
            name=f"Cyclotomic restrictions of an element of {self.centralizer_group()}",
        )

    def lift_component_isometries(self, component_isometries):
        r"""Lift a compatible tuple of component isometries to ``O(L,f)``.

        Compatibility is tested by extension, not by comparing only finite
        discriminant images.  If ``m`` is the index of the cyclotomic sum,
        every ``m*x`` lies in that sum.  Apply the component tuple there and
        divide by ``m`` again.  The division succeeds in ``L`` exactly when
        the tuple preserves the integral glue; the ambient ``O(L)`` constructor
        then verifies the form and bijectivity, and commutation with ``f`` is
        checked separately.
        """
        components = {}
        restrictions = self.component_isometries()
        for divisor in self.nonzero_divisors():
            summand = self.summand(divisor)
            try:
                component = component_isometries[divisor]
            except (KeyError, TypeError):
                component = component_isometries[int(divisor)]
            component = summand.O()(component)
            if component * restrictions[divisor] != restrictions[divisor] * component:
                raise ValueError("a component isometry does not commute with the cyclotomic action")
            components[divisor] = component

        lattice = self.lattice()
        moved_images = []
        for divisor in self.nonzero_divisors():
            summand = self.summand(divisor)
            inclusion = summand.inclusion()
            component = components[divisor]
            moved_images.extend(inclusion(component(generator)) for generator in summand.module_generators())
        orthogonal_sum = self.orthogonal_sum()
        moved = orthogonal_sum.module_category().Mor(orthogonal_sum, lattice)(tuple(moved_images))

        scalar = lattice.base_ring()(int(self.index().finite_value()))
        scaling = lattice.module_category().Mor(lattice, lattice)(tuple(lattice.scalar_multiple(scalar, generator) for generator in lattice.module_generators()))
        inclusion = self.orthogonal_sum_inclusion()

        def image(label):
            scaled = lattice.scalar_multiple(scalar, lattice.module_generator(label))
            return scaling.lift(moved(inclusion.lift(scaled)))

        lifted = lattice.O()(image)
        if lifted * self.isometry() != self.isometry() * lifted:
            raise ArithmeticError("the lifted component tuple does not centralize the equipped isometry")
        return lifted

    def component_isometries_extend(self, component_isometries) -> bool:
        try:
            self.lift_component_isometries(component_isometries)
        except (ArithmeticError, AssertionError, ValueError):
            return False
        return True


class EquivariantLattice(SageObject):
    r"""A lattice equipped with a specified lattice automorphism.

    This is the semantic object ``(L,f)``.  The underlying lattice and the
    isometry remain live owned objects; equivariant constructions are defined
    by literal commutation with the selected automorphisms.
    """

    def __init__(self, lattice, isometry) -> None:
        if isometry.domain() is not lattice or isometry.codomain() is not lattice:
            raise ValueError("an equivariant lattice is equipped by an automorphism of that lattice")
        self._lattice = lattice
        self._isometry = lattice.O()(isometry)

    def lattice(self):
        return self._lattice

    def isometry(self):
        return self._isometry

    @cached_method
    def centralizer_group(self):
        r"""Return ``O(L,f)=Z_{O(L)}(f)``."""
        return self.lattice().O().centralizer(self.isometry())

    def primitive_extension(self):
        r"""Return the invariant/coinvariant primitive extension cut out by ``f``."""
        return self.isometry().primitive_extension()

    @cached_method
    def cyclotomic_decomposition(self, order):
        r"""Return the integral cyclotomic decomposition for the exact stated order."""
        return CyclotomicDecomposition(self, order)

    @cached_method
    def polarized(self, polarization):
        r"""Return this equivariant lattice together with an invariant polarization.

        The polarization is an actual vector of ``L`` fixed by the equipped
        isometry.  The resulting object owns the structured arithmetic group
        ``Z_{O(L)}(f) cap Stab(h)`` rather than requiring callers to reconstruct
        that intersection ad hoc.
        """
        return PolarizedEquivariantLattice(self, polarization)

    def equivariant_sublattice(self, sublattice):
        r"""Equip an ``f``-stable represented sublattice with the restricted isometry."""
        if not callable(getattr(sublattice, "inclusion", None)):
            raise TypeError("an equivariant sublattice is a represented lattice subobject")
        if sublattice.ambient_lattice() is not self.lattice():
            raise ValueError("the selected sublattice has the wrong ambient lattice")

        inclusion = sublattice.inclusion()
        images = {}
        for label in sublattice.module_generating_set():
            embedded = inclusion(sublattice.module_generator(label))
            moved = self.isometry()(embedded)
            if not inclusion.is_in_image(moved):
                raise ValueError("the selected sublattice is not stable under the equipped isometry")
            images[label] = inclusion.lift(moved)
        restricted = sublattice.O()(images)
        return EquivariantLattice(sublattice, restricted)

    def equivariant_isometry_to(self, other):
        r"""Return ``h:(L,f)->(M,g)`` with ``h f = g h`` when exactly decidable.

        Definite target lattices have a finite enumerable isometry torsor, so
        the search is exhaustive there.  In an indefinite regime one exact
        underlying witness may be available without an exact conjugacy
        classifier; a non-equivariant witness is therefore not evidence that
        no equivariant isometry exists, and this method refuses in that case.
        """
        if not isinstance(other, EquivariantLattice):
            raise TypeError("equivariant_isometry_to expects another equipped lattice")
        source = self.lattice()
        target = other.lattice()
        if source is target and self.isometry() == other.isometry():
            return source.O().one()

        homset = source.Isom(target)
        empty = homset.is_empty()
        if empty is True:
            return None
        if target.module_rank().is_finite() and target.is_definite():
            for candidate in homset:
                if candidate * self.isometry() == other.isometry() * candidate:
                    return candidate
            return None
        assert empty is not Unknown, (
            "equivariant-isometry search in the indefinite regime requires the underlying isometry Hom to be decided exactly"
        )

        witness = homset.an_element()
        assert witness * self.isometry() == other.isometry() * witness, (
            "the represented indefinite equivariant-isometry path requires the selected underlying isometry witness to intertwine the equipped actions; "
            "no exhaustive indefinite conjugacy classifier is selected"
        )
        return witness

    def equivariant_vector_orbit_representatives(self, square):
        r"""Return vector-orbit representatives under ``O(L,f)`` in the supported regime."""
        return self.equivariant_vector_orbit_decomposition(square).representatives()

    def equivariant_vector_orbit_decomposition(self, square):
        r"""Return exact ``O(L,f)``-orbits on vectors of the selected square."""
        return EquivariantVectorOrbitDecomposition(self, square)

    def equivariant_sublattice_orbit_decomposition(self, sublattices):
        r"""Return exact centralizer orbits on a finite stable family of sublattices.

        Every selected sublattice must be stable under ``f`` and the supplied
        finite family must be stable under the full centralizer.  In the
        definite regime the centralizer is finite and is listed exactly, so
        the returned representatives, stabilizers and transporters form the
        complete quotient of the stated family rather than a search prefix.
        """
        sublattices = tuple(sublattices)
        for sublattice in sublattices:
            self.equivariant_sublattice(sublattice)
        return EquivariantFiniteOrbitDecomposition(
            self,
            sublattices,
            _transport_sublattice,
            _same_embedded_sublattice,
        )

    def equivariant_flag(self, terms):
        r"""Return the represented nested flag of ``f``-stable sublattices."""
        return EquivariantSublatticeFlag(self, terms)

    def equivariant_flag_orbit_decomposition(self, flags):
        r"""Return exact centralizer orbits on a finite stable family of flags."""
        flags = tuple(flags)
        if any(flag.decorated_lattice() is not self for flag in flags):
            raise ValueError("an equivariant flag family belongs to one equipped lattice")
        return EquivariantFiniteOrbitDecomposition(
            self,
            flags,
            _transport_equivariant_flag,
            _same_equivariant_flag,
        )

    def __repr__(self) -> str:
        return f"{self.lattice()} equipped with {self.isometry()}"


class PolarizedEquivariantLattice(SageObject):
    r"""An equivariant lattice ``(L,f)`` with an invariant polarization ``h``.

    This owns the three live objects that define the polarized arithmetic
    group: the centralizer ``Z_{O(L)}(f)``, the point stabilizer of ``h``, and
    their structured intersection.  The polarization is retained both in the
    ambient lattice and through its lift to the invariant lattice ``L^f``.
    """

    def __init__(self, decorated_lattice, polarization) -> None:
        if not isinstance(decorated_lattice, EquivariantLattice):
            raise TypeError("a polarized equivariant lattice starts from an EquivariantLattice")
        lattice = decorated_lattice.lattice()
        polarization = lattice(polarization)
        if decorated_lattice.isometry()(polarization) != polarization:
            raise ValueError("a polarization of (L,f) must lie in the invariant lattice")
        if polarization == lattice.zero():
            raise ValueError("a polarization is nonzero")
        self._decorated_lattice = decorated_lattice
        self._polarization = polarization

    def decorated_lattice(self):
        return self._decorated_lattice

    def lattice(self):
        return self.decorated_lattice().lattice()

    def isometry(self):
        return self.decorated_lattice().isometry()

    def polarization(self):
        return self._polarization

    def primitive_extension(self):
        return self.decorated_lattice().primitive_extension()

    @cached_method
    def invariant_polarization(self):
        invariant = self.primitive_extension().invariant
        inclusion = invariant.inclusion()
        if not inclusion.is_in_image(self.polarization()):
            raise ArithmeticError("an f-invariant polarization did not lie in L^f")
        return inclusion.lift(self.polarization())

    def centralizer_group(self):
        return self.decorated_lattice().centralizer_group()

    @cached_method
    def polarization_stabilizer(self):
        return self.lattice().O().stabilizer(self.polarization())

    @cached_method
    def polarized_group(self):
        r"""Return ``Z_{O(L)}(f) cap Stab(h)`` as a structured subgroup."""
        return self.centralizer_group().intersection(self.polarization_stabilizer())

    def __repr__(self) -> str:
        return f"{self.decorated_lattice()} polarized by {self.polarization()}"


class IsometryPrimitiveExtension:
    r"""The primitive extension ``L^f + (L^f)^perp -> L`` cut out by ``f``.

    Every field below is an owned object: the two primitive sublattices with
    their inclusions, the finite index of their orthogonal sum, and the glue
    anti-isometry presenting the extension.
    """

    def __init__(self, isometry) -> None:
        lattice = isometry.domain()
        assert isometry.codomain() is lattice, "a primitive extension is cut out by an automorphism of one lattice"
        assert lattice.module_rank().is_finite() and lattice.is_nondegenerate(), "the invariant and coinvariant lattices span L only when L is a finite nondegenerate lattice"
        invariant = isometry.invariant_lattice()
        coinvariant = isometry.formed_coinvariants()
        assert invariant.module_rank() + coinvariant.module_rank() == lattice.module_rank(), (
            "the invariant lattice and its orthogonal complement do not have complementary rank; f is not of finite order on this lattice"
        )

        self.isometry = isometry
        self.lattice = lattice
        self.invariant = invariant
        self.coinvariant = coinvariant

    @cached_method
    def glue(self):
        r"""Return the Nikulin anti-isometry ``H_+ -> H_-(-1)`` of this extension."""
        return self.lattice.glue_map(self.invariant, self.coinvariant)

    def gluing_subgroup(self):
        r"""Return ``H_+ = L/(L^f + (L^f)^perp)`` seen inside ``A_{L^f}``."""
        return self.glue().domain()

    @cached_method
    def index(self):
        r"""Return ``[L : L^f + (L^f)^perp]``, the order of the glue subgroup."""
        return self.invariant.sum(self.coinvariant).index()

    def centralizer_group(self):
        r"""Return ``O(L,f) = Z_{O(L)}(f)`` as a predicate subgroup of ``O(L)``."""

        return self.lattice.Aut().centralizer(self.isometry)

    def centralizer_discriminant_image(self):
        r"""Return ``rho_L(O(L,f)) <= O(A_L)``, the finite image of the centralizer."""
        return self.isometry.centralizer_discriminant_image()

    def _full_discriminant_glue_data(self):
        r"""Return the primitive glue data when both discriminant forms are glued in full."""
        glue = self.glue()
        invariant_form = self.invariant.discriminant_group()
        coinvariant_form = self.coinvariant.discriminant_group()
        glue_source = glue.domain()
        glue_target = glue.codomain()
        assert glue_source.cardinality() == invariant_form.cardinality(), (
            "the represented discriminant conjugation requires the primitive extension to glue the full invariant discriminant form"
        )
        assert glue_target.cardinality() == coinvariant_form.cardinality(), (
            "the represented discriminant conjugation requires the primitive extension to glue the full coinvariant discriminant form"
        )
        return glue, invariant_form, coinvariant_form, glue_source, glue_target

    @cached_method
    def coinvariant_extension_subgroup(self):
        r"""Return the coinvariant restriction image in the full-glue involution case.

        Suppose ``f`` is an involution and the primitive extension glues the
        *entire* discriminant forms of ``L^f`` and ``(L^f)^perp``.  Then every
        isometry of the coinvariant lattice commutes with ``f|_{L^-}=-1``, and
        it extends across the primitive gluing exactly when its discriminant
        action belongs to

        ``gamma rho(O(L^f)) gamma^-1``.

        The returned group is therefore the actual finite-character preimage
        in ``O(L^-)``; it is not a separately represented copy of the ambient
        centralizer.
        """
        assert self.acts_as_negation_on_coinvariants(), (
            "the represented coinvariant extension subgroup is the involution case where the coinvariant action is -1"
        )

        _glue, invariant_form, coinvariant_form, _glue_source, _glue_target = (
            self._full_discriminant_glue_data()
        )

        invariant_image = self.invariant.discriminant_image()
        coinvariant_orthogonal_group = coinvariant_form.O()

        allowed_discriminant_image = coinvariant_orthogonal_group.subgroup_on(
            tuple(self._coinvariant_discriminant_from_invariant(generator) for generator in invariant_image.group_generators())
        )
        return self.coinvariant.O().discriminant_preimage(allowed_discriminant_image)

    def _coinvariant_discriminant_from_invariant(self, invariant_automorphism):
        r"""Conjugate an invariant discriminant action across the primitive glue.

        If ``gamma:H_+ -> H_-(-1)`` is the glue anti-isometry, this returns
        the automorphism of ``A_{L^-}`` induced by
        ``gamma invariant_automorphism gamma^-1``.  The full-discriminant
        hypothesis is exactly the one required by
        :meth:`coinvariant_extension_subgroup`.
        """
        glue, invariant_form, coinvariant_form, glue_source, glue_target = (
            self._full_discriminant_glue_data()
        )
        source_inclusion = glue_source.inclusion()
        target_inclusion = glue_target.inclusion()
        twisted_coinvariant_form = target_inclusion.codomain()

        invariant_automorphism = invariant_form.O()(invariant_automorphism)
        images = {}
        for label in coinvariant_form.module_generating_set():
            element = coinvariant_form.module_generator(label)
            unformed = coinvariant_form.forget_form_morphism()(element)
            twisted = twisted_coinvariant_form.equip_form_morphism()(unformed)
            target_element = target_inclusion.lift(twisted)
            source_element = glue.inverse_morphism()(target_element)
            invariant_class = source_inclusion(source_element)
            moved_invariant_class = invariant_automorphism(invariant_class)
            moved_source = source_inclusion.lift(moved_invariant_class)
            moved_target = glue.forward()(moved_source)
            moved_twisted = target_inclusion(moved_target)
            moved_unformed = twisted_coinvariant_form.forget_form_morphism()(moved_twisted)
            images[label] = coinvariant_form.equip_form_morphism()(moved_unformed)
        morphism = coinvariant_form.module_category().Mor(coinvariant_form, coinvariant_form)(images)
        return coinvariant_form.O()(morphism)

    def lift_coinvariant_extension_element(self, coinvariant_part):
        r"""Lift ``g_-`` from the anti-invariant extension group to ``O(L,f)``.

        The selected ``g_-`` already has discriminant action in the conjugate
        of the invariant discriminant image.  Enumerate that finite image,
        choose the matching invariant discriminant action, lift it to an
        actual isometry of ``L^f``, and assemble the pair through the retained
        primitive glue.  The result is an ambient centralizer element whose
        coinvariant restriction is literally ``g_-``.
        """
        subgroup = self.coinvariant_extension_subgroup()
        if coinvariant_part not in subgroup:
            raise ValueError("the selected coinvariant isometry does not preserve the primitive gluing")
        coinvariant_part = self.coinvariant.O()(coinvariant_part)
        target_action = coinvariant_part.discriminant_morphism()
        invariant_group = self.invariant.O()
        invariant_image = self.invariant.discriminant_image()

        invariant_part = None
        for invariant_action in invariant_image:
            if self._coinvariant_discriminant_from_invariant(invariant_action) != target_action:
                continue
            invariant_part = invariant_group.discriminant_lift(invariant_action)
            if invariant_part is not None:
                break
        if invariant_part is None:
            raise ArithmeticError("a glue-compatible coinvariant action had no retained invariant discriminant lift")

        lifted = self.centralizer_element(invariant_part, coinvariant_part)
        if self.coinvariant_restriction(lifted) != coinvariant_part:
            raise ArithmeticError("the ambient centralizer lift restricts to the wrong coinvariant isometry")
        return lifted

    def coinvariant_isotropic_orbit_representatives(self, rank, *, flag=False):
        r"""Return anti-invariant isotropic orbits under the ambient centralizer image."""
        return self.coinvariant_extension_subgroup().isotropic_orbit_representatives(
            rank,
            flag=flag,
        )

    def coinvariant_isotropic_equivalence_witness(self, left, right, *, flag=False):
        r"""Return an ambient centralizer element carrying ``left`` to ``right``.

        The finite-character subgroup first constructs the exact transporter
        on the anti-invariant lattice.  This method then lifts that transporter
        through the primitive gluing, so the witness acts on the original
        lattice rather than only on ``L^-``.
        """
        coinvariant_witness = self.coinvariant_extension_subgroup().isotropic_equivalence_witness(
            left,
            right,
            flag=flag,
        )
        if coinvariant_witness is None:
            return None
        return self.lift_coinvariant_extension_element(coinvariant_witness)

    def _restriction(self, automorphism, subobject):
        assert automorphism.domain() is self.lattice, "a restriction of the centralizer is taken of an automorphism of L"
        assert automorphism * self.isometry == self.isometry * automorphism, (
            "restriction along this decomposition is defined on O(L,f); the stated automorphism does not commute with f"
        )
        inclusion = subobject.inclusion()
        summand = inclusion.domain()
        return summand.Aut()({label: inclusion.lift(automorphism(inclusion(summand.module_generator(label)))) for label in summand.module_generating_set()})

    def invariant_restriction(self, automorphism):
        r"""Return ``g|_{L^f}`` in ``O(L^f)`` for ``g`` in the centralizer.

        An element of ``O(L,f)`` commutes with ``f``, so it preserves the
        fixed lattice and, being an isometry of ``L``, its orthogonal
        complement.  Restriction is therefore defined and lands in the
        orthogonal group of the summand.
        """
        return self._restriction(automorphism, self.invariant)

    def coinvariant_restriction(self, automorphism):
        r"""Return ``g|_{(L^f)^perp}`` in ``O((L^f)^perp)`` for ``g`` in the centralizer."""
        return self._restriction(automorphism, self.coinvariant)

    def acts_as_negation_on_coinvariants(self) -> bool:
        r"""Return whether ``f`` restricts to ``-1`` on ``(L^f)^perp``.

        This holds exactly when ``f`` is an involution: then ``(L^f)^perp`` is
        ``ker(f + 1)``, which is the statement the eigenspace decomposition
        ``V_pm = ker(f -+ 1)`` makes.
        """
        inclusion = self.coinvariant.inclusion()
        return all(self.isometry(inclusion(generator)) == -inclusion(generator) for generator in inclusion.domain().module_generators())

    @cached_method
    def orthogonal_sum_inclusion(self):
        r"""Return the finite-index inclusion ``L^f + (L^f)^perp -> L``.

        The two summands are orthogonal of complementary rank, so their
        orthogonal sum is a lattice in its own right and this arrow is the
        primitive extension the class is named for.  Its cokernel has order
        :meth:`index`, so that scalar carries every vector of ``L`` into the
        image: an isometry of the two summands is read on ``L`` by clearing
        that one denominator.
        """
        invariant_inclusion = self.invariant.inclusion()
        coinvariant_inclusion = self.coinvariant.inclusion()
        invariant_summand = invariant_inclusion.domain()
        coinvariant_summand = coinvariant_inclusion.domain()
        summands = invariant_summand + coinvariant_summand
        return summands.Emb(self.lattice)(
            tuple(invariant_inclusion(generator) for generator in invariant_summand.module_generators())
            + tuple(coinvariant_inclusion(generator) for generator in coinvariant_summand.module_generators())
        )

    def glue_graph(self):
        r"""Return the graph of ``gamma`` inside ``A_{L^f} x A_{(L^f)^perp}(-1)``.

        Nikulin presents ``L`` by the subgroup ``L/(L^f + (L^f)^perp)``, which
        sits in the sum of the two discriminant forms as the graph of the
        anti-isometry ``gamma``.  The graph is a finite group of order
        :meth:`index`, and it is what an isometry of the two summands has to
        preserve in order to be an isometry of ``L``.
        """
        glue = self.glue()
        gluing = glue.domain()
        into_invariant = gluing.inclusion()
        into_coinvariant = glue.codomain().inclusion()
        return finite_ordered_set(tuple((into_invariant(element), into_coinvariant(glue(element))) for element in gluing.elements()))

    def _discriminant_action(self, automorphism, ambient, element):
        r"""Return the image of a class of ``ambient`` under ``Disc(automorphism)``.

        An automorphism of a summand induces an automorphism of that summand's
        discriminant module, and that module is what underlies whichever
        finite form the glue map put the graph in: the discriminant module
        itself, its bilinear reading when an even summand sits inside an odd
        ``L``, or the twist ``A_R(-1)``.  Polarizing and rescaling both leave
        the underlying map alone -- an isometry of ``q`` is an isometry of its
        polar form and of any rescaling of either -- so the action is read by
        forgetting the ambient form, applying the induced automorphism, and
        equipping the ambient form again.
        """
        return ambient.equip_form_morphism()(automorphism.discriminant_morphism()(ambient.forget_form_morphism()(element)))

    def pair_preserves_glue_graph(self, invariant_part, coinvariant_part) -> bool:
        r"""Return whether ``(g_+, g_-)`` carries the graph of ``gamma`` onto itself.

        The pair acts on the sum of the two discriminant forms by its induced
        discriminant automorphisms ``Disc(g_+)`` and ``Disc(g_-)``, the second
        read on the twist ``A_{(L^f)^perp}(-1)`` in which ``gamma`` lands.  It
        extends to an isometry of ``L`` exactly when that action preserves the
        graph, which is Nikulin's criterion for a primitive extension.  Both
        maps are automorphisms of finite forms, so preserving the graph
        setwise is the same as permuting it.

        The criterion reads the same in either parity of ``L``; only the
        finite forms the graph lives in change, and which ones those are is
        settled once, by ``glue_map``, from the parity of ``L``.  An even
        ``L`` glues its quadratic discriminant forms and an odd one its
        bilinear forms, so the two ambients are taken from the endpoints of
        the glue arrow rather than chosen a second time here.
        """
        invariant_ambient = self.glue().domain().inclusion().codomain()
        coinvariant_ambient = self.glue().codomain().inclusion().codomain()
        graph = self.glue_graph()
        return all(
            (
                self._discriminant_action(invariant_part, invariant_ambient, invariant_class),
                self._discriminant_action(coinvariant_part, coinvariant_ambient, coinvariant_class),
            )
            in graph
            for invariant_class, coinvariant_class in graph
        )

    def centralizer_element(self, invariant_part, coinvariant_part):
        r"""Assemble ``g`` in ``O(L,f)`` from a compatible pair of restrictions.

        This is the inverse of :meth:`invariant_restriction` and
        :meth:`coinvariant_restriction`.  A pair ``(g_+, g_-)`` in
        ``O(L^f) x O((L^f)^perp)`` is an element of ``O(L,f)`` under two
        conditions.  It has to extend to ``L``, which is
        :meth:`pair_preserves_glue_graph`.  It then has to commute with ``f``,
        and since ``f`` is the identity on ``L^f`` that is the single
        condition that ``g_-`` commutes with ``f`` restricted to
        ``(L^f)^perp``.

        The extension itself is one denominator.  The orthogonal sum has index
        ``m`` in ``L``, so ``m x`` lies in the sum for every ``x`` in ``L``;
        applying the pair there and dividing by ``m`` again gives ``g x``, and
        the division is exact because the pair preserves the graph.  The
        returned arrow is built in ``O(L)``, whose constructor is what proves
        the assembled map preserves the form and is bijective.
        """
        lattice = self.lattice
        invariant_inclusion = self.invariant.inclusion()
        coinvariant_inclusion = self.coinvariant.inclusion()
        invariant_summand = invariant_inclusion.domain()
        coinvariant_summand = coinvariant_inclusion.domain()
        assert invariant_part.parent() is invariant_summand.Aut(), "the invariant half of the pair is an element of O(L^f)"
        assert coinvariant_part.parent() is coinvariant_summand.Aut(), "the coinvariant half of the pair is an element of O((L^f)^perp)"
        coinvariant_isometry = self.coinvariant_restriction(self.isometry)
        assert coinvariant_part * coinvariant_isometry == coinvariant_isometry * coinvariant_part, (
            "an element of O(L,f) restricts on (L^f)^perp to the centralizer of f there; the stated g_- does not commute with f"
        )
        assert self.pair_preserves_glue_graph(invariant_part, coinvariant_part), (
            "the stated pair does not preserve the graph of the glue anti-isometry, so it is an isometry of L^f + (L^f)^perp that does not extend to L"
        )

        ring = lattice.base_ring()
        scalar = ring(int(self.index().finite_value()))
        inclusion = self.orthogonal_sum_inclusion()
        summands = inclusion.domain()
        moved = summands.module_category().Mor(summands, lattice)(
            tuple(invariant_inclusion(invariant_part(generator)) for generator in invariant_summand.module_generators())
            + tuple(coinvariant_inclusion(coinvariant_part(generator)) for generator in coinvariant_summand.module_generators())
        )
        scaling = lattice.module_category().Mor(lattice, lattice)(tuple(lattice.scalar_multiple(scalar, generator) for generator in lattice.module_generators()))

        def image(label):
            scaled = lattice.scalar_multiple(scalar, lattice.module_generator(label))
            return scaling.lift(moved(inclusion.lift(scaled)))

        return lattice.O()(image)

    def equivariant_vector_orbit_representatives(self, square):
        r"""Return ``O(L,f)``-orbit representatives of the vectors of ``square``.

        The centralizer is a subgroup of ``O(L)`` cut out by a predicate and
        not by a character, so the finite-character quotient that splits an
        ``O(L)`` orbit does not describe it.  What describes it is the group
        itself, and acting with it is a finite computation exactly when
        ``O(L)`` is finite, which for a lattice is definiteness; the
        assertion in the owning subgroup operation states that hypothesis.
        For the orbits under the full ``O(L)`` use
        ``L.O().vector_orbit_representatives(square)``.
        """
        return EquivariantLattice(
            self.lattice,
            self.isometry,
        ).equivariant_vector_orbit_representatives(square)

    def equivariant_vector_orbit_decomposition(self, square):
        r"""Return the exact decorated-vector orbit package for this isometry."""
        return EquivariantLattice(
            self.lattice,
            self.isometry,
        ).equivariant_vector_orbit_decomposition(square)

    def __repr__(self) -> str:
        return f"Primitive extension of {self.lattice} cut out by {self.isometry}"


__all__ = [
    "CyclotomicDecomposition",
    "EquivariantLattice",
    "EquivariantVectorOrbit",
    "EquivariantVectorOrbitDecomposition",
    "IsometryPrimitiveExtension",
    "PolarizedEquivariantLattice",
]
