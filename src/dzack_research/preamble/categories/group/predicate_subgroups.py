"""Subgroups specified by a membership predicate rather than generators."""

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.group.groups import (
    OwnedGroups,
    Subgroups,
    _finite_group_morphism_kernel_cardinality,
    _finite_group_morphism_kernel_is_abelian,
    _finite_if_bounded_by,
    _owned_group,
)
from dzack_research.preamble.categories.orthogonal_quotients import (
    OrthogonalCharacterQuotient,
    _subgroup_isotropic_orbit_representatives,
    _subgroup_vector_orbit_representatives,
)
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.set_categories import Set, _ConditionSetEngine
from dzack_research.preamble.logic import AtomicProposition, conjunction
from dzack_research.preamble.owned_category import _object_of


def _predicate_subgroup_category(category):
    r"""The category a predicate subgroup of ``category.base()`` is constructed in.

    A subgroup of a finite group is finite (Lagrange), and every subgroup
    of an abelian group is abelian. Both refinements follow from the
    ambient group, independently of whether the predicate is decidable.
    For example, the equalizer of two maps of abelian groups must remain
    in Ab, whereas the equalizer of arbitrary group maps need not.
    """
    group = category.base()
    return Cat().meet((
        category,
        *_finite_if_bounded_by(group),
        *((OwnedGroups().Commutative(),) if group in OwnedGroups().Commutative() else ()),
    ))


class PredicateSubgroups(OwnedParameterizedCategory):

    @staticmethod
    def __classcall__(cls, supergroup):
        return OwnedParameterizedCategory.__classcall__(cls, _owned_group(supergroup))

    def parameter_category(self):
        return OwnedGroups()

    def an_object(self):
        r"""The whole parameter group cut out by the tautological predicate.

        Every element commutes with the identity, so this is the whole group --
        cut out by a predicate, which is what membership here states.
        """
        group = self.base()
        return group.centralizer(group.one())

    def _repr_object_names(self):
        return "predicate subgroups"

    def super_categories(self):
        return [Subgroups(self.base())]

    def _call_(
        self,
        predicate,
        description,
        *,
        character_data=None,
        character_data_complete=None,
    ):
        r"""Construct the predicate subgroup of this category's ambient group."""
        return _object_of(
            _predicate_subgroup_category(self),
            supergroup=self.base(),
            predicate=predicate,
            description=description,
            character_data=character_data,
            character_data_complete=character_data_complete,
        )

    class ParentMethods:
        def __init__(
            self,
            supergroup,
            predicate,
            description,
            character_data=None,
            character_data_complete=None,
            **rest,
        ) -> None:
            self._predicate = predicate
            self._admitted_members = []
            self._description = description
            self._character_data = dict(character_data or {})
            self._character_data_complete = (
                bool(character_data)
                if character_data_complete is None
                else bool(character_data_complete)
            )
            super().__init__(supergroup=supergroup, **rest)

        def defining_predicate(self):
            return self._predicate

        def universe(self):
            r"""The literal ambient set for the inherited predicate-subset operations."""
            return self.supergroup()

        predicate = defining_predicate

        # The subgroup is the same predicate subset of its ambient group.
        # Reuse the set owner's membership, admission and enumeration rules;
        # group closure is a premise of this subgroup construction.
        __contains__ = _ConditionSetEngine.__contains__
        is_parent_of = __contains__
        __iter__ = _ConditionSetEngine.__iter__
        _retain_admitted_member = _ConditionSetEngine._retain_admitted_member

        def _element_constructor_(self, datum):
            r"""Read ambient group literals, then use the set owner's predicate admission."""
            return _ConditionSetEngine._element_constructor_(self, self.supergroup()(datum))

        def finite_index_schreier_generators(self, *, index_bound, generators=None):
            r"""Generate a finite-index predicate subgroup by coset traversal.

            The index bound is required: a predicate alone does not certify
            finite index. Representatives of cosets ``r H`` are recognized
            by membership of ``r^(-1) x`` in ``H``. The resulting Schreier
            words ``t_(s r H)^(-1) s r`` generate the subgroup.

            EXAMPLES::

                sage: G = Groups.S(3)
                sage: H = G.subgroup((G((1, 2)),))
                sage: P = G.predicate_subgroup(lambda g: g in H, "transposition subgroup")
                sage: generators = P.finite_index_schreier_generators(index_bound=3)
                sage: all(g in P for g in generators)
                True
                sage: G.subgroup(generators).cardinality() == 2
                True
                sage: P.finite_index_schreier_generators(index_bound=2)
                Traceback (most recent call last):
                ...
                ValueError: the subgroup index exceeds the supplied bound
                sage: P.finite_index_schreier_generators(index_bound=2.5)
                Traceback (most recent call last):
                ...
                ValueError: the subgroup index bound must be an integer
                sage: F, C = Groups.Free(1), Groups.C(2)
                sage: s, t = F.group_generators()[0], C.group_generators()[0]
                sage: phi = F.Mor(C)({next(iter(F.free_basis())): t})
                sage: P = F.predicate_subgroup(lambda g: phi(g) == C.one(), "even exponent")
                sage: generators = P.finite_index_schreier_generators(index_bound=2)
                sage: any(g == s*s or g == ~(s*s) for g in generators)
                True
            """
            ambient = self.supergroup()
            if generators is None:
                assert ambient.has_selected_group_resolution() and ambient.has_selected_finite_group_generating_set(), (
                    f"cannot compute finite Schreier generators of {self}: {ambient} has no "
                    "selected finite generating set; pass a finite generating family"
                )
                generators = tuple(ambient.group_generators())
            else:
                generators = tuple(generators)
            bound = int(index_bound)
            if bound != index_bound:
                raise ValueError("the subgroup index bound must be an integer")
            if bound < 1:
                raise ValueError("the subgroup index bound must be positive")
            representatives = [ambient.one()]

            def representative_of(candidate):
                for representative in representatives:
                    if (~representative) * candidate in self:
                        return representative
                return None

            for representative in representatives:
                for generator in generators:
                    for step in (generator, ~generator):
                        candidate = step * representative
                        if representative_of(candidate) is None:
                            representatives.append(candidate)
                            if len(representatives) > bound:
                                raise ValueError("the subgroup index exceeds the supplied bound")
            from dzack_research.preamble.categories.sets.finite_families import finite_family

            return finite_family(
                (
                    self((~representative_of(generator * representative)) * generator * representative)
                    for representative in representatives
                    for generator in generators
                ),
                name="Schreier generators of a finite-index subgroup",
            )

        def _selected_schreier_augmentation(self, words):
            r"""Map the free group on a selected Schreier family onto this subgroup.

            This is the common represented boundary for a *known* generating
            family of a predicate subgroup. Its input has an owned finite
            index set and actual elements of this subgroup; its output is
            the free-group Mor landing in this literal subgroup, rather than
            another subgroup generated by the same ambient elements.
            """
            from dzack_research.preamble.categories.sets.indexed_families import IndexedFamily
            from dzack_research.preamble.categories.sets.set_categories import FiniteSets, Sets

            if not isinstance(words, IndexedFamily) or words.index_set() not in FiniteSets():
                raise TypeError("Schreier augmentation requires an owned finite generator family")
            if not all(self.is_parent_of(words.value(label)) is True for label in words.index_set()):
                raise ValueError("Schreier augmentation generators must be admitted in the actual subgroup")
            free = OwnedGroups.Free(index_set=words.index_set())
            ambient_map = free.Mor(self.supergroup())(
                Sets().Mor(words.index_set(), self.supergroup())(
                    lambda label: words.value(label)
                )
            )
            return free.Mor(self)._from_elementwise_rule(ambient_map)

        def finite_index_schreier_generating_morphism(self, *, index_bound, generators=None):
            r"""The free generating epimorphism onto a bounded finite-index subgroup."""
            words = self.finite_index_schreier_generators(
                index_bound=index_bound, generators=generators
            )
            return self._selected_schreier_augmentation(words)

        def _character_data_snapshot(self):
            r"""Return private finite-character representation metadata."""
            return dict(self._character_data)

        def character_data_is_complete(self) -> bool:
            r"""Whether the retained finite characters define this whole subgroup."""
            return self._character_data_complete

        def contains_character_kernel(self) -> bool:
            data = self._character_data_snapshot()
            return self.character_data_is_complete() and bool(
                data.get("determinant_kernel", False)
                or data.get("spinor_kernel", False)
                or data.get("discriminant_preimages", ())
            )

        def _finiteness_decision(self):
            r"""A subgroup of a finite group is finite; finite-index character preimages inherit infinitude."""
            ambient = self.supergroup().is_finite()
            if ambient is True:
                return True
            if ambient is False and self.contains_character_kernel():
                return False
            return AtomicProposition("is_finite", self)

        def _cardinality_decision(self):
            r"""``|H|``: from the retained character data, else by counting a finite supergroup.

            With complete finite-character data ``H`` is the preimage of a
            subgroup of a finite quotient, so ``|H| = |G| |image of H| /
            |image of G|``.  Otherwise, in a finite ``G``, ``H`` is the set of
            elements satisfying the predicate, counted exactly in one pass over
            ``G``, at a cost linear in ``|G|``: the predicate is a Python
            function, which GAP's subgroup search by a property cannot evaluate.
            """
            supergroup_cardinality = self.supergroup().cardinality()
            if self.contains_character_kernel():
                quotient = self.finite_character_quotient()
                image_size = int(quotient.image_keys().cardinality())
                subgroup_image_size = int(quotient.subgroup_image_keys().cardinality())
                if supergroup_cardinality.is_finite():
                    order = int(supergroup_cardinality.finite_value())
                    return cardinal(order * subgroup_image_size // image_size)
                if supergroup_cardinality.is_countably_infinite():
                    return supergroup_cardinality
            assert supergroup_cardinality.is_finite(), (
                f"cannot compute the order of the subgroup {self}: its group "
                f"{self.supergroup()} has order {supergroup_cardinality}, which is not finite, "
                f"and the subgroup is not known as the preimage of a subgroup of a finite quotient"
            )
            return cardinal(sum(1 for _element in self))

        @cached_method
        def _engine_group(self):
            r"""The engine subgroup on the elements of this subgroup of a finite group.

            Engine contract (``OWN-05``), declared in ``groups.py``.  The
            engine cannot evaluate the predicate, so the subgroup it cuts out
            is realized as the engine subgroup generated by its elements,
            listed in one pass over the finite supergroup.
            """
            return self.supergroup()._engine_subgroup_from_generators(self)

        def _to_engine(self, element):
            assert element in self, f"{element} is not an element of the subgroup {self}"
            return self.supergroup()._to_subgroup_engine(element, self._engine_group())

        def _from_engine(self, engine_element):
            return self.supergroup()._from_subgroup_engine(engine_element)

        def one(self):
            r"""The ambient identity, which lies in the declared subgroup."""
            return self.supergroup().one()

        def intersection(self, other):
            if other.supergroup() is not self.supergroup():
                raise ValueError(
                    f"cannot intersect {self} and {other}: they are subgroups of different "
                    f"groups, {self.supergroup()} and {other.supergroup()}"
                )
            left = self._character_data_snapshot()
            right = other._character_data_snapshot()
            data = {
                "determinant_kernel": bool(left.get("determinant_kernel", False))
                or bool(right.get("determinant_kernel", False)),
                "spinor_kernel": bool(left.get("spinor_kernel", False))
                or bool(right.get("spinor_kernel", False)),
                "discriminant_preimages": tuple(left.get("discriminant_preimages", ()))
                + tuple(right.get("discriminant_preimages", ())),
            }
            return IntersectionSubgroups(self.supergroup())(
                (self, other),
                character_data=data,
                character_data_complete=(
                    self.character_data_is_complete()
                    and other.character_data_is_complete()
                ),
            )

        def finite_character_quotient(self):
            if not self.character_data_is_complete():
                raise ValueError(
                    f"{self} has no finite character quotient: it is not known to be the full "
                    f"preimage of a subgroup of a finite quotient of {self.supergroup()} by "
                    f"determinant, spinor norm and discriminant characters"
                )
            return OrthogonalCharacterQuotient(self)

        def vector_orbit_representatives(self, square):

            return _subgroup_vector_orbit_representatives(self, square)

        def vectors_are_equivalent(self, left, right) -> bool:

            return self.vector_equivalence_witness(left, right) is not None

        def vector_equivalence_witness(self, left, right):
            from dzack_research.preamble.categories.orthogonal_quotients import (
                _subgroup_vector_equivalence_witness,
            )

            return _subgroup_vector_equivalence_witness(self, left, right)

        def isotropic_orbit_representatives(self, rank, *, flag=False):

            return _subgroup_isotropic_orbit_representatives(
                self, rank, flag=flag
            )

        def isotropic_are_equivalent(self, left, right, *, flag=False) -> bool:

            return self.isotropic_equivalence_witness(left, right, flag=flag) is not None

        def isotropic_equivalence_witness(self, left, right, *, flag=False):
            from dzack_research.preamble.categories.orthogonal_quotients import (
                _subgroup_isotropic_equivalence_witness,
            )

            return _subgroup_isotropic_equivalence_witness(
                self, left, right, flag=flag
            )

        def cusps(self, rank=1):
            r"""Return this arithmetic subgroup's primitive-isotropic cusp orbits."""
            from dzack_research.preamble.categories.isotropic_orbits import _arithmetic_cusp
            from dzack_research.preamble.categories.sets.finite_ordered_sets import (
                finite_ordered_set,
            )

            return finite_ordered_set(
                tuple(
                    _arithmetic_cusp(self, representative)
                    for representative in self.isotropic_orbit_representatives(rank)
                )
            )

        def tits_building_incidence(self):
            r"""Return this subgroup's line/plane quotient-building incidence.

            Rank-two flags are split under the same finite-character quotient
            as the line and plane orbits, so each edge retains actual subgroup
            transporters to its two cusp vertices rather than transporters
            inherited from the full orthogonal group.
            """
            from dzack_research.preamble.categories.isotropic_orbits import (
                ArithmeticCuspIncidence,
            )
            from dzack_research.preamble.categories.sets.finite_ordered_sets import (
                finite_ordered_set,
            )

            lattice = self.supergroup().domain()
            line_cusps = self.cusps(1)
            plane_cusps = self.cusps(2)
            incidences = []
            for flag in self.isotropic_orbit_representatives(2, flag=True):
                line, plane = flag.terms()
                line_vertices = tuple(cusp for cusp in line_cusps if line in cusp)
                plane_vertices = tuple(cusp for cusp in plane_cusps if plane in cusp)
                if len(line_vertices) != 1 or len(plane_vertices) != 1:
                    raise ArithmeticError(
                        f"the isotropic flag {flag} of {lattice} lies in {len(line_vertices)} "
                        f"line cusps and {len(plane_vertices)} plane cusps of {self}; each "
                        f"term of a flag must lie in exactly one cusp"
                    )
                line_cusp = line_vertices[0]
                plane_cusp = plane_vertices[0]
                line_transporter = line_cusp.transporter_witness(line)
                plane_transporter = plane_cusp.transporter_witness(plane)
                if line_transporter is None or plane_transporter is None:
                    raise ArithmeticError(
                        f"the isotropic flag {flag} of {lattice} lies in the cusps "
                        f"{line_cusp} and {plane_cusp} of {self}, but no element of {self} "
                        f"carries the cusp representatives to its terms"
                    )
                incidences.append(
                    ArithmeticCuspIncidence(
                        self,
                        flag,
                        line_cusp,
                        plane_cusp,
                        line_transporter,
                        plane_transporter,
                    )
                )
            if any(incidence.lattice() is not lattice for incidence in incidences):
                raise ArithmeticError(
                    f"the Tits building incidence of {self} has a cusp incidence in a lattice "
                    f"other than {lattice}, the lattice {self.supergroup()} acts on"
                )
            return finite_ordered_set(tuple(incidences))

        def _repr_(self):
            return f"{{g in {self.supergroup()} : {self._description}}}"


class _PredicateSubgroupConstruction(OwnedParameterizedCategory):
    @staticmethod
    def __classcall__(cls, supergroup):
        return OwnedParameterizedCategory.__classcall__(cls, _owned_group(supergroup))

    def parameter_category(self):
        return OwnedGroups()

    def super_categories(self):
        return [PredicateSubgroups(self.base())]

class KernelSubgroups(_PredicateSubgroupConstruction):
    def an_object(self):

        group = self.base()
        return self(group.Mor(group).identity())

    def _call_(self, morphism):
        r"""Construct the kernel subgroup retaining its defining morphism."""
        group = self.base()
        if morphism.domain() is not group:
            raise ValueError(
                f"{morphism} has no kernel in {group}: its domain is "
                f"{morphism.domain()}, not {group}"
            )
        identity = morphism.codomain().one()
        return _object_of(
            _predicate_subgroup_category(self),
            supergroup=group,
            predicate=lambda element: morphism(element) == identity,
            description=f"{morphism}(g)=1",
            kernel_morphism=morphism,
        )

    @classmethod
    def _repr_object_names(cls):
        return "kernel subgroups"

    class ParentMethods:
        def __init__(self, kernel_morphism, **rest) -> None:
            self._kernel_morphism = kernel_morphism
            super().__init__(**rest)

        def kernel_morphism(self):
            return self._kernel_morphism

        def index(self, *, generators=None):
            r"""The index of a kernel with a represented finite image.

            First isomorphism: ``G/ker(f)`` is the image of ``f``. The
            finite-image transversal retains a representative of every
            image element, including when ``G`` is infinite. Explicit
            generators may be supplied when the ambient group has not
            selected a generating resolution.
            """
            morphism = self.kernel_morphism()
            return cardinal(len(self.supergroup().finite_image_lifts(morphism, generators=generators)))

        def schreier_generators(self, *, generators=None):
            r"""Generators of the kernel of a homomorphism with finite image.

            For left image representatives ``t_q`` and each selected source
            generator ``s``, Schreier's rewriting gives
            ``t_(f(s)q)^(-1) s t_q``. The finite image and its chosen lifts
            come from the group owner's ``finite_image_lifts`` construction;
            no ambient finite-group hypothesis is imposed. Explicit source
            generators may be provided when the ambient resolution has not
            been selected.

            EXAMPLES::

                sage: four, two = Groups.C(4), Groups.C(2)
                sage: s, t = four.group_generators()[0], two.group_generators()[0]
                sage: kernel = four.Mor(two)({s: t}).kernel()
                sage: generators = kernel.schreier_generators()
                sage: all(g in kernel for g in generators)
                True
                sage: four.subgroup(generators).cardinality() == kernel.cardinality()
                True
                sage: F = Groups.Free(1)
                sage: label = next(iter(F.free_basis()))
                sage: s = F.group_generators()[0]
                sage: reduction = F.Mor(two)({label: t})
                sage: free_kernel = reduction.kernel()
                sage: generators = free_kernel.schreier_generators()
                sage: all(reduction(g) == two.one() for g in generators)
                True
                sage: any(g == s*s or g == ~(s*s) for g in generators)
                True
                sage: G = Groups.S(3)
                sage: H = G.subgroup((G((1, 2)),))
                sage: identity_on_generators = G.Mor(G)({g: g for g in G.group_generators()})
                sage: P = identity_on_generators.preimage_subgroup(H)
                sage: generators = P.schreier_generators()
                sage: all(g in P for g in generators)
                True
                sage: G.subgroup(generators).cardinality() == H.cardinality() == 2
                True
            """
            morphism = self.kernel_morphism()
            ambient = self.supergroup()
            if generators is None:
                assert ambient.has_selected_group_resolution() and ambient.has_selected_finite_group_generating_set(), (
                    f"cannot compute finite Schreier generators of {self}: {ambient} has no "
                    "selected finite generating set; pass a finite generating family"
                )
                generators = tuple(ambient.group_generators())
            else:
                generators = tuple(generators)
            from dzack_research.preamble.categories.sets.finite_families import finite_family

            lifts = ambient.finite_image_lifts(morphism, generators=generators)
            return finite_family(
                (
                    self((~lifts[morphism(s) * image]) * s * representative)
                    for image, representative in lifts.items()
                    for s in generators
                ),
                name="Schreier generators of a kernel",
            )

        def schreier_generating_morphism(self, *, generators=None):
            r"""The selected epimorphism from a free group on Schreier generators.

            The images come from the existing Schreier family. The free basis
            and its image map are retained by the free-group Mor constructor,
            rather than exposing an unparented list of group elements.
            """
            words = self.schreier_generators(generators=generators)
            return self._selected_schreier_augmentation(words)

        def _cardinality_decision(self):
            r"""Return the exact kernel order when the ambient group is finite."""
            if self.supergroup().is_finite() is True:
                return _finite_group_morphism_kernel_cardinality(
                    self.kernel_morphism()
                )
            return super()._cardinality_decision()

        def _abelianity_decision(self):
            r"""Decide abelianity from the represented exact kernel when finite."""
            if self.supergroup().is_finite() is True:
                return _finite_group_morphism_kernel_is_abelian(
                    self.kernel_morphism()
                )
            assert False, (
                f"cannot decide whether the kernel {self} of {self.kernel_morphism()} is "
                f"abelian: this is decided only when the domain {self.supergroup()} is known "
                f"to be finite"
            )


class PreimageSubgroups(_PredicateSubgroupConstruction):
    def an_object(self):

        group = self.base()
        whole = PredicateSubgroups(group)(lambda _element: True, "the whole group")
        return self(group.Mor(group).identity(), whole)

    def _call_(
        self,
        morphism,
        subgroup,
        *,
        predicate=None,
        description=None,
        character_data=None,
        character_data_complete=None,
    ):
        r"""Construct the inverse image of ``subgroup`` along ``morphism``."""
        group = self.base()
        if morphism.domain() is not group:
            raise ValueError(
                f"cannot take the preimage of {subgroup} along {morphism} as a subgroup of "
                f"{group}: the domain of {morphism} is {morphism.domain()}, not {group}"
            )
        if subgroup not in Subgroups(morphism.codomain()):
            raise ValueError(
                f"cannot take the preimage of {subgroup} under {morphism}: "
                f"the specified target is not a subgroup of {morphism.codomain()}"
            )
        if predicate is None:
            def predicate(element):
                return subgroup.is_parent_of(morphism(element))
        if description is None:
            description = f"{morphism}(g) lies in {subgroup}"
        return _object_of(
            _predicate_subgroup_category(self),
            supergroup=group,
            predicate=predicate,
            description=description,
            character_data=character_data,
            character_data_complete=character_data_complete,
            preimage_morphism=morphism,
            target_subgroup=subgroup,
        )

    @classmethod
    def _repr_object_names(cls):
        return "preimage subgroups"

    class ParentMethods:
        def __init__(self, preimage_morphism, target_subgroup, **rest) -> None:
            self._preimage_morphism = preimage_morphism
            self._target_subgroup = target_subgroup
            super().__init__(**rest)

        def preimage_morphism(self):
            return self._preimage_morphism

        def target_subgroup(self):
            return self._target_subgroup

        def schreier_generating_morphism(self, *, generators=None):
            r"""A finite free-group augmentation onto this finite-index preimage.

            Write ``P = rho^-1(H)`` inside ``G``. The selected augmentation
            ``pi: F -> G`` supplies formal source words without deciding
            membership of their values in a generated subgroup of a larger
            group. Schreier's formula is computed for ``rho*pi`` in ``F``.
            The resulting word map ``w: E -> F`` satisfies
            ``rho*pi(w(E)) <= H``, so ``pi*w`` defines the returned map
            ``E -> P`` with this literal preimage as codomain.

            Its finite basis indexes the complete Schreier family, retaining
            repeated and identity words. The actual word map and ambient
            augmentation are retained by the defining group-map composite.
            No value is readmitted by the predicate-subgroup constructor.
            Explicit generators may replace the selected augmentation; these
            must be admitted elements generating the ambient group.
            """
            from dzack_research.preamble.categories.sets.set_categories import (
                Sets,
                finite_ordinal_set,
            )

            morphism = self.preimage_morphism()
            ambient = self.supergroup()
            if generators is None:
                assert ambient.has_selected_group_resolution() and ambient.has_selected_finite_group_generating_set(), (
                    f"cannot compute finite Schreier generators of {self}: {ambient} has no "
                    "selected finite generating set; pass a finite generating family"
                )
                resolution = ambient.selected_group_resolution()
                free = resolution.level(0)
                augmentation = resolution.augmentation()
            else:
                source_generators = tuple(generators)
                for generator in source_generators:
                    admitted = ambient.is_parent_of(generator)
                    if admitted is False:
                        raise ValueError(
                            f"cannot compute Schreier generators of {self}: {generator} is not an element of {ambient}"
                        )
                    assert admitted is True, (
                        f"cannot compute Schreier generators of {self}: membership of the supplied "
                        f"generator {generator} in {ambient} is undecided"
                    )
                source_labels = finite_ordinal_set(len(source_generators))
                free = OwnedGroups.Free(index_set=source_labels)
                augmentation = free.Mor(ambient)(
                    Sets().Mor(source_labels, ambient)(
                        lambda label: source_generators[int(label)]
                    )
                )

            target = self.target_subgroup()
            free_generators = tuple(free.group_generators())
            finite_map = morphism * augmentation
            lifts = free.finite_image_lifts(finite_map, generators=free_generators)
            representatives = []
            for image in lifts:
                if not any((~representative) * image in target for representative in representatives):
                    representatives.append(image)

            def representative_of(image):
                return next(rep for rep in representatives if (~rep) * image in target)

            words = tuple(
                (~lifts[representative_of(finite_map(generator) * image)]) * generator * lifts[image]
                for image in representatives
                for generator in free_generators
            )
            labels = finite_ordinal_set(len(words))
            source = OwnedGroups.Free(index_set=labels)
            word_map = source.Mor(free)(
                Sets().Mor(labels, free)(lambda label: words[int(label)])
            )
            return source.Mor(self)._from_elementwise_rule(augmentation * word_map)

        def schreier_generators(self, *, generators=None):
            r"""Generate a finite-index preimage using cosets ``t J`` of its image.

            Let ``Q=f(G)`` and ``J=Q intersect H``. Choose a representative
            ``t`` for each left coset ``q J`` and lift it to ``G``. For
            each source generator ``s`` and representative ``t``, the
            element ``t_(f(s)tJ)^-1 s t`` belongs to the preimage and the
            resulting Schreier family generates it. The supplied generator
            family, when present, must generate the whole ambient group.

            EXAMPLES::

                sage: C = Groups.C(4)
                sage: c = C.group_generators()[0]
                sage: H = C.subgroup((c*c,))
                sage: F = Groups.Free(1)
                sage: s = F.group_generators()[0]
                sage: phi = F.Mor(C)({next(iter(F.free_basis())): c})
                sage: P = phi.preimage_subgroup(H)
                sage: generators = P.schreier_generators()
                sage: all(g in P for g in generators)
                True
                sage: any(g == s*s or g == ~(s*s) for g in generators)
                True
            """
            augmentation = self.schreier_generating_morphism(generators=generators)
            source = augmentation.domain()
            return source.group_generators().map(
                augmentation,
                name="Schreier generators of a subgroup preimage",
            )


class StabilizerSubgroups(_PredicateSubgroupConstruction):
    def an_object(self):
        group = self.base()
        identity = group.one()
        return self(
            identity,
            group.conjugation_g_set().action_functor(),
            lambda element: element * identity * element.inverse() == identity,
        )

    def _call_(
        self,
        stabilized_object,
        action,
        predicate,
        *,
        description=None,
    ):
        r"""Construct the stabilizer retaining the stabilized object and action."""
        from dzack_research.preamble.categories.functors.core import Functor

        group = self.base()
        if not isinstance(action, Functor) or action.domain() is not group.classifying_category():
            raise TypeError(
                f"the stabilizer of {stabilized_object} in {group} requires the actual "
                f"action functor B({group}) -> C, but received {action!r}"
            )
        if description is None:
            description = f"g stabilizes {stabilized_object} {action}"
        return _object_of(
            _predicate_subgroup_category(self),
            supergroup=group,
            predicate=predicate,
            description=description,
            stabilized_object=stabilized_object,
            stabilizer_action=action,
        )

    @classmethod
    def _repr_object_names(cls):
        return "stabilizer subgroups"

    class ParentMethods:
        def __init__(self, stabilized_object, stabilizer_action, **rest) -> None:
            self._stabilized_object = stabilized_object
            self._stabilizer_action = stabilizer_action
            super().__init__(**rest)

        def stabilized_object(self):
            return self._stabilized_object

        def stabilizer_action(self):
            return self._stabilizer_action

        def restricted_stabilizer_action(self):
            r"""The action of this stabilizer, restricted along its inclusion.

            For ``i: H -> G`` and the retained action ``rho: BG -> C``,
            this is the actual composite ``B(i) ; rho: BH -> C``.
            It retains the original stabilized object and does not replace
            the action by the predicate defining membership in ``H``.

            Unexecuted distinguishing specimen: take ``G = S3`` acting on
            itself by conjugation, and ``H = Stab_G((1,2))``. The restricted
            action has domain ``BH``, not ``BG``; on the unique object it
            agrees with the original action, while the morphism associated
            to ``h in H`` acts as conjugation by its image under ``i``.
            In particular, merely returning ``rho`` would have the wrong
            domain, even though every ``h`` fixes the selected point.
            """
            from dzack_research.preamble.categories.group.classifying_categories import (
                ClassifyingFunctor,
            )

            return ClassifyingFunctor(self.inclusion()).then(self.stabilizer_action())


class CentralizerSubgroups(_PredicateSubgroupConstruction):
    def an_object(self):
        group = self.base()
        return self(group.one())

    def _call_(self, element):
        r"""Construct the centralizer of ``element`` in the ambient group."""
        group = self.base()
        if element not in group:
            raise ValueError(
                f"cannot form the centralizer of {element} in {group}: {element} is not an "
                f"element of {group}"
            )
        return _object_of(
            _predicate_subgroup_category(self),
            supergroup=group,
            predicate=lambda candidate: element * candidate == candidate * element,
            description=f"g commutes with {element}",
            centralizing_element=element,
        )

    @classmethod
    def _repr_object_names(cls):
        return "centralizer subgroups"

    class ParentMethods:
        def __init__(self, centralizing_element, **rest) -> None:
            self._centralizing_element = centralizing_element
            super().__init__(**rest)

        def centralizing_element(self):
            return self._centralizing_element


class IntersectionSubgroups(_PredicateSubgroupConstruction):
    def an_object(self):
        group = self.base()
        whole = PredicateSubgroups(group)(lambda _element: True, "the whole group")
        return self((whole, whole))

    def _call_(
        self,
        subgroups,
        *,
        character_data=None,
        character_data_complete=None,
    ):
        r"""Construct the intersection of subgroups of this ambient group."""
        group = self.base()
        subgroups = tuple(subgroups)
        if any(subgroup.supergroup() is not group for subgroup in subgroups):
            raise ValueError(
                f"cannot form the intersection in {group}: the subgroups "
                f"{[subgroup for subgroup in subgroups if subgroup.supergroup() is not group]} "
                f"are not subgroups of {group}"
            )
        return _object_of(
            _predicate_subgroup_category(self),
            supergroup=group,
            predicate=lambda element: conjunction(subgroup.is_parent_of(element) for subgroup in subgroups),
            description="g lies in every selected subgroup",
            character_data=character_data,
            character_data_complete=character_data_complete,
            intersected_subgroups=Set(subgroups),
        )

    @classmethod
    def _repr_object_names(cls):
        return "intersection subgroups"

    class ParentMethods:
        def __init__(self, intersected_subgroups, **rest) -> None:
            self._intersected_subgroups = intersected_subgroups
            super().__init__(**rest)

        def intersected_subgroups(self):
            return self._intersected_subgroups

__all__ = [
    "CentralizerSubgroups",
    "IntersectionSubgroups",
    "KernelSubgroups",
    "PredicateSubgroups",
    "PreimageSubgroups",
    "StabilizerSubgroups",
]
