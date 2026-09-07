"""Owned categories of groups and their standard constructor catalogue.

An owned group is a parent built through the owned category chain.  The Sage
group it computes with is its engine, held privately; every call into that
engine is one of the crossings in the "engine crossings" section below, and
nothing public returns a Sage group or a GAP object.  Elements are engine
elements, as for the owned ring views.
"""

from functools import wraps
from weakref import WeakValueDictionary

from sage.categories.category import Category
from sage.categories.finite_groups import FiniteGroups as SageFiniteGroups
from sage.categories.groups import Groups as SageGroups
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.objects import Objects
from sage.groups.abelian_gps.abelian_group import (
    AbelianGroup_class,
    AbelianGroup_subgroup,
)
from sage.groups.finitely_presented import FinitelyPresentedGroup
from sage.groups.free_group import FreeGroup_class
from sage.groups.indexed_free_group import IndexedFreeGroup
from sage.groups.libgap_morphism import GroupHomset_libgap, GroupMorphism_libgap
from sage.groups.libgap_wrapper import ParentLibGAP
from sage.groups.matrix_gps.coxeter_group import CoxeterMatrixGroup
from sage.groups.matrix_gps.finitely_generated import (
    FinitelyGeneratedMatrixGroup_generic,
)
from sage.groups.matrix_gps.finitely_generated_gap import (
    FinitelyGeneratedMatrixGroup_gap,
)
from sage.groups.matrix_gps.named_group import NamedMatrixGroup_generic
from sage.groups.matrix_gps.named_group_gap import NamedMatrixGroup_gap
from sage.groups.perm_gps.permgroup import (
    PermutationGroup_generic,
    PermutationGroup_subgroup,
)
from sage.libs.gap.element import GapElement
from sage.libs.gap.libgap import libgap
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.classcall_metaclass import typecall
from sage.misc.latex import latex
from sage.misc.unknown import Unknown
from sage.rings.infinity import infinity
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.rings.number_field.galois_group import GaloisGroup_v2 as SageGaloisGroup
from sage.structure.category_object import CategoryObject
from sage.structure.element import MultiplicativeGroupElement, RingElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    CategoryPacketMethods,
    EndCategoryConstruction,
    HomCategoryConstruction,
    IsoCategoryConstruction,
    _category_homset,
    category_packet,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.group.magmas import (
    AdditiveGroups,
    Monoids,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    MatrixSpaces,
    _engine_matrix,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedRings,
    _engine_element,
    _engine_ring,
    _own_ring,
    _owned_ring,
    ring_morphism,
)
from dzack_research.preamble.categories.sets.cardinals import (
    Cardinalities,
    aleph,
    cardinal,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_filter,
    finite_ordered_image,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom
from dzack_research.preamble.refine import realize_owned_category

# --------------------------------------------------------------------------
# Engine crossings.  These are the only sites that read the Sage group behind
# an owned group; everything above them speaks the owned vocabulary.
# --------------------------------------------------------------------------


def _identity(element):
    return element


def _engine_group(group):
    """Return the Sage group computing for ``group``.

    Protected contract: an owned group that computes through a Sage group
    supplies ``_engine_group()``, ``_to_engine(element)`` and
    ``_from_engine(_engine_element)``; :class:`OwnedGroup` and the lattice
    isometry group are its providers.
    """
    try:
        crossing = group._engine_group
    except AttributeError:
        raise NotImplementedError(f"{group} has no Sage group engine") from None
    return crossing()


def _engine_finiteness(engine):
    """Return True/False when Sage's category already decides finiteness."""
    if engine in SageFiniteGroups():
        return True
    if engine.category().is_subcategory(SageGroups().Infinite()):
        return False
    return Unknown


def _gap_model(group):
    """Return the GAP group modelling ``group``."""
    match group:
        case GroupAutomorphismGroup():
            return group._libgap_()
    engine = _engine_group(group)
    match engine:
        case PermutationGroup_generic():
            return libgap(engine)
        case ParentLibGAP():
            return engine.gap()
        case AbelianGroup_class():
            if _engine_finiteness(engine) is not True:
                raise NotImplementedError("GAP normalization of this abelian group requires finiteness")
            return libgap(engine.permutation_group())
        case CoxeterMatrixGroup():
            free, relations = coxeter_presentation(engine.coxeter_matrix())
            return libgap(free / list(relations))
        case NamedMatrixGroup_generic() | FinitelyGeneratedMatrixGroup_generic():
            if _engine_finiteness(engine) is not True:
                raise NotImplementedError("GAP permutation normalization requires finiteness")
            return libgap(engine.as_permutation_group())
        case _:
            raise NotImplementedError(f"{group} has no GAP model in this engine")


def _automorphism_gap_model(group):
    """Return GAP's automorphism group of ``group`` where the engine computes it."""
    match group:
        case OwnedGroup():
            match group._engine:
                case FreeGroup_class() | FinitelyPresentedGroup():
                    raise NotImplementedError(f"Aut({group}) exists, but this engine does not compute it from a bare presentation")
    if group.is_finite() is not True:
        raise NotImplementedError(f"the available GAP automorphism algorithm requires {group} finite")
    return libgap.AutomorphismGroup(_gap_model(group))


def _elements_have_gap_models(group) -> bool:
    """Whether elements of ``group`` are identified elementwise with GAP elements."""
    try:
        engine = _engine_group(group)
    except NotImplementedError:
        return False
    return isinstance(engine, (PermutationGroup_generic, ParentLibGAP))


def _transported_subgroup(group, engine_subgroup):
    """Return the owned subgroup object with its exact ambient endpoint."""
    return _TransportedGroupSubobject(group, engine_subgroup)


def _subgroup_from_gap(group, gap_subgroup):
    """Return the owned subgroup of ``group`` modelled by the GAP subgroup."""
    engine = _engine_group(group)
    match engine:
        case PermutationGroup_generic() | ParentLibGAP():
            return _transported_subgroup(group, engine._subgroup_constructor(gap_subgroup))
        case _:
            raise NotImplementedError(f"{group} does not construct subgroups from GAP data")


def _finite_order(group):
    r"""Return the finite group order as an owned integer."""
    from sage.rings.integer_ring import ZZ as SageZZ

    integers = _own_ring(SageZZ)
    try:
        backend_order = _engine_group(group).order()
    except NotImplementedError:
        backend_order = _gap_model(group).Size().sage()
    return integers._from_engine_element(SageZZ(backend_order))


def _engine_supergroup(group):
    """Return the group ``group`` was constructed as a subgroup of, else ``group``."""
    match group:
        case OwnedGroup() if group._supergroup is not None:
            return group._supergroup
        case OwnedGroup():
            engine = group._engine
        case _:
            return group
    match engine:
        case PermutationGroup_subgroup() | AbelianGroup_subgroup():
            return _own_group(engine.ambient_group())
        case ParentLibGAP() if engine.ambient() is not engine:
            return _own_group(engine.ambient())
        case _:
            return group


def _engine_subgroup(group, generators):
    engine = _engine_group(group)
    try:
        construct = engine.subgroup
    except AttributeError:
        raise NotImplementedError(f"{group} does not construct subgroups from generators in this engine") from None
    return _transported_subgroup(group, construct([group._to_engine(group(generator)) for generator in generators]))


def _engine_cosets(group, subgroup, side):
    engine = _engine_group(group)
    try:
        cosets = engine.cosets
    except AttributeError:
        raise NotImplementedError(f"{group} does not enumerate cosets in this engine") from None
    if _law_reversed(group):
        # The owned coset gH is {g h} = {h *_engine g}: the engine's coset on the other side.
        side = "right" if side == "left" else "left"
    backend_cosets = cosets(_engine_group(subgroup), side=side)
    coset_positions = Sets.Δ[len(backend_cosets) - 1]

    def own_coset(backend_members):
        member_positions = Sets.Δ[len(backend_members) - 1]
        return finite_ordered_image(
            member_positions,
            lambda member_position: group._from_engine(backend_members[int(member_position)]),
            name="Coset elements",
        )

    # Each coset is one object: build them once, so a coset read back from a
    # representative is the coset the family already holds.
    owned_cosets = tuple(own_coset(backend_members) for backend_members in backend_cosets)
    return finite_ordered_image(
        coset_positions,
        lambda position: owned_cosets[int(position)],
        name=f"{side.capitalize()} cosets",
    )


def _unique_nonidentity_generators(group):
    engine = _engine_group(group)
    identity = engine.one()
    backend_generators = engine.gens()
    engine_generators = finite_ordered_image(
        Sets.Δ[len(backend_generators) - 1],
        lambda position: backend_generators[int(position)],
        name="Backend chosen group generators",
    )
    nonidentity = finite_ordered_filter(
        engine_generators,
        lambda generator: generator != identity,
    )
    return finite_ordered_image(
        nonidentity,
        group._from_engine,
        name="Chosen group generators",
    )


def _free_basis(group):
    selected = getattr(group, "_preamble_free_basis", None)
    if selected is not None:
        return selected
    engine = _engine_group(group)
    match engine:
        case IndexedFreeGroup():
            return engine.indices()
        case _:
            raise NotImplementedError(f"{group} has no chosen free basis")


def _free_generator(group, index):
    basis = _free_basis(group)
    if index not in basis:
        try:
            normalized = basis(index)
        except TypeError, ValueError, AttributeError:
            normalized = None
        if normalized is not None and normalized in basis:
            index = normalized
        else:
            try:
                size = cardinal(basis.cardinality())
            except AttributeError, TypeError, ValueError:
                size = None
            if size is None or not size.is_finite():
                raise ValueError(f"{index!r} is not in the chosen free basis")
            for candidate in basis:
                parent = getattr(candidate, "parent", lambda: None)()
                if parent is None:
                    continue
                try:
                    coerced = parent(index)
                except TypeError, ValueError:
                    continue
                if coerced == candidate:
                    index = candidate
                    break
            else:
                raise ValueError(f"{index!r} is not in the chosen free basis")
    engine_label = getattr(
        group,
        "_preamble_free_basis_engine_label",
        _group_constructor_argument,
    )
    return group._from_engine(_engine_group(group).gen(engine_label(index)))


def _reduced_word(group, element):
    """Return the reduced word with generator labels in the owned free basis.

    Letters are listed in the order they multiply in the owned group, which
    is the engine's word reversed when the engine multiplies left to right.
    """
    owned_label = getattr(
        group,
        "_preamble_free_basis_owned_label",
        lambda label: label,
    )
    letters = tuple((owned_label(backend_index), sign) for backend_index, sign in group._to_engine(group(element)).to_word_list())
    return letters[::-1] if _law_reversed(group) else letters


def _law_reversed(group) -> bool:
    """Whether the owned product is the engine product reversed.

    The owned product is composition of the maps a group's elements act as.
    Matrix engines already multiply as such maps on column vectors.  Sage's
    permutation groups and GAP's word and automorphism groups multiply left
    to right, ``(g h)(x) = h(g(x))``, so their owned product is reversed.
    """
    match group:
        case GroupAutomorphismGroup():
            return True
    try:
        engine = _engine_group(group)
    except NotImplementedError:
        return False
    match engine:
        case CoxeterMatrixGroup() | NamedMatrixGroup_generic() | FinitelyGeneratedMatrixGroup_generic():
            return False
        case PermutationGroup_generic() | FreeGroup_class() | FinitelyPresentedGroup() | IndexedFreeGroup() | AbelianGroup_class() | ParentLibGAP():
            return True
    return False


def _engine_point(engine, point):
    """Cross an owned point into the domain of a Sage permutation group.

    An owned integer becomes the engine's integer when the group permutes
    integers; any other point is already one the engine's domain holds.
    """
    engine_point = _integer_engine_point(point)
    return engine_point if engine_point in engine.domain() else point


def _integer_engine_point(point):
    """An owned integer as the engine's integer; any other point unchanged."""
    integers = _own_ring(ZZ)
    if not isinstance(point, int) and point in integers:
        return _engine_element(integers, point)
    return point


def _owned_point(engine, point):
    """Read a point of a Sage permutation group's domain as an owned point."""
    _ = engine
    match point:
        case Integer():
            return _own_ring(ZZ)._from_engine_element(point)
    return point


def _presentation_of(group):
    engine = _engine_group(group)
    match engine:
        case FreeGroup_class():
            return _own_group(engine), ()
        case FinitelyPresentedGroup():
            return _own_group(engine.free_group()), tuple(engine.relations())
        case PermutationGroup_generic():
            presented = engine.as_finitely_presented_group()
            return _own_group(presented.free_group()), tuple(presented.relations())
        case AbelianGroup_class():
            presented = engine.permutation_group().as_finitely_presented_group()
            return _own_group(presented.free_group()), tuple(presented.relations())
        case CoxeterMatrixGroup():
            free, relations = coxeter_presentation(engine.coxeter_matrix())
            return _own_group(free), relations
        case NamedMatrixGroup_generic() | NamedMatrixGroup_gap():
            presented = engine.as_permutation_group().as_finitely_presented_group()
            return _own_group(presented.free_group()), tuple(presented.relations())
        case _:
            raise NotImplementedError(f"{group} does not supply chosen finite-presentation data")


def _engine_quotient_by_relators(group, relators):
    engine = _engine_group(group)
    match engine:
        case FreeGroup_class():
            return _own_group(engine.quotient([group._to_engine(group(relator)) for relator in relators]))
        case FinitelyPresentedGroup():
            # G = F/R and G/<<S>> = F/<<R, S>>, with S lifted to words in F.
            free = engine.free_group()
            relations = list(engine.relations()) + [free(group._to_engine(group(relator)).Tietze()) for relator in relators]
            return _own_group(free.quotient(relations))
        case _:
            raise NotImplementedError(f"{group} does not form quotients by relators in this engine")


def _is_arithmetic_witness(engine) -> bool:
    return isinstance(engine, NamedMatrixGroup_generic) and engine.base_ring() is ZZ


def _is_abelian_witness(engine):
    if engine.category().is_subcategory(SageGroups().Commutative()):
        return True
    if isinstance(engine, (AbelianGroup_class, AbelianGroup_subgroup)):
        return True
    try:
        return bool(engine.is_abelian())
    except AttributeError, NotImplementedError, TypeError, ValueError:
        return False


def _has_chosen_generators(engine):
    return isinstance(
        engine,
        (
            PermutationGroup_generic,
            AbelianGroup_class,
            FreeGroup_class,
            FinitelyPresentedGroup,
            FinitelyGeneratedMatrixGroup_generic,
            FinitelyGeneratedMatrixGroup_gap,
            CoxeterMatrixGroup,
        ),
    )


def _has_chosen_presentation(engine):
    if isinstance(engine, (FreeGroup_class, FinitelyPresentedGroup, CoxeterMatrixGroup)):
        return True
    return _engine_finiteness(engine) is True and isinstance(
        engine,
        (PermutationGroup_generic, AbelianGroup_class, NamedMatrixGroup_generic, NamedMatrixGroup_gap),
    )


def _is_finitely_generated_witness(engine):
    return _engine_finiteness(engine) is True or _has_chosen_generators(engine) or _is_arithmetic_witness(engine)


def _is_finitely_presented_witness(engine):
    return _engine_finiteness(engine) is True or isinstance(engine, (FreeGroup_class, FinitelyPresentedGroup, CoxeterMatrixGroup, AbelianGroup_class))


def _owned_group_category(engine) -> Category:
    """Return the join of owned group categories witnessed by ``engine``."""
    categories = [OwnedGroups()]
    finiteness = _engine_finiteness(engine)
    finite = finiteness is True
    abelian = _is_abelian_witness(engine)
    if finite and abelian:
        categories.append(OwnedFiniteAbelianGroups())
    elif finite:
        categories.append(OwnedFiniteGroups())
    elif abelian:
        categories.append(OwnedAbelianGroups())
    if finiteness is False:
        categories.append(OwnedInfiniteGroups())
    if not finite and _is_finitely_generated_witness(engine):
        categories.append(OwnedFinitelyGeneratedGroups())
    if not finite and _is_finitely_presented_witness(engine):
        categories.append(OwnedFinitelyPresentedGroups())
    if _has_chosen_generators(engine):
        categories.append(GroupsWithChosenFiniteGeneratingSet())
    if _has_chosen_presentation(engine):
        categories.append(GroupsWithChosenFinitePresentation())
    if isinstance(engine, IndexedFreeGroup):
        categories.append(GroupsWithChosenFreeBasis())
    if isinstance(engine, PermutationGroup_generic):
        categories.append(PermutationGroups())
    return Category.join(tuple(categories))


class _OwnedGroupElement(MultiplicativeGroupElement):
    r"""An element of a preamble group with a private backend representative."""

    def __init__(self, parent, backend_element) -> None:
        MultiplicativeGroupElement.__init__(self, parent)
        self._backend_element = backend_element

    def _backend(self):
        return self._backend_element

    def _mul_(self, other):
        r"""``self * other`` is the composition ``self ∘ other``.

        A group acts on the left: ``rho(g h) = rho(g) rho(h)``, the product of
        the matrices acting on an ordered basis.  Sage's permutation groups and
        GAP's word groups multiply left to right, ``(g h)(x) = h(g(x))``, so
        for those engines the owned product is the engine product reversed.
        """
        parent = self.parent()
        left, right = self._backend(), other._backend()
        if _law_reversed(parent):
            left, right = right, left
        return parent._from_engine(left * right)

    def __call__(self, point):
        r"""Apply this element to a point of the set it acts on.

        A Galois group acts on its field by automorphisms; any other
        permutation group acts on the points it permutes.
        """
        parent = self.parent()
        engine = _engine_group(parent)
        match engine:
            case SageGaloisGroup():
                field = _own_ring(engine.number_field())
                assert point in field, f"{point} is not an element of {field}"
                return field._from_engine_element(self._backend().as_hom()(_engine_element(field, point)))
        assert isinstance(engine, PermutationGroup_generic), f"{parent} is not realized as a permutation group, so its elements do not act on points"
        engine_point = _engine_point(engine, point)
        if engine_point not in engine.domain():
            # A permutation of a set fixes every point outside that set.
            return point
        return _owned_point(engine, self._backend()(engine_point))

    def Tietze(self):
        r"""The word of this element in the chosen generators, as signed generator positions."""
        word = tuple(int(letter) for letter in self._backend().Tietze())
        return word[::-1] if _law_reversed(self.parent()) else word

    def _invert_(self):
        return self.parent()._from_engine(~self._backend())

    def __invert__(self):
        return self._invert_()

    def __pow__(self, exponent, modulus=None):
        if modulus is not None:
            return NotImplemented
        return self.parent()._from_engine(self._backend() ** int(exponent))

    def _richcmp_(self, other, op):
        if not isinstance(other, _OwnedGroupElement) or other.parent() is not self.parent():
            return NotImplemented
        return richcmp(self._backend(), other._backend(), op)

    def __eq__(self, other):
        return isinstance(other, _OwnedGroupElement) and other.parent() is self.parent() and self._backend() == other._backend()

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash((id(self.parent()), self._backend()))

    def is_one(self):
        return bool(self._backend() == self.parent()._engine.one())

    def order(self):
        from sage.rings.integer_ring import ZZ as SageZZ

        return _own_ring(SageZZ)._from_engine_element(SageZZ(self._backend().order()))

    multiplicative_order = order

    def sign(self):
        from sage.rings.integer_ring import ZZ as SageZZ

        return _own_ring(SageZZ)._from_engine_element(SageZZ(self._backend().sign()))

    def _repr_(self):
        return repr(self._backend())

    def _latex_(self):
        return str(latex(self._backend()))


class OwnedGroup(Parent):
    r"""A preamble group with one private Sage/GAP computational model."""

    Element = _OwnedGroupElement

    def __init__(self, engine) -> None:
        self._engine = engine
        Parent.__init__(self, category=_owned_group_category(engine))
        realize_owned_category(self)

    def _engine_group(self):
        return self._engine

    def _to_engine(self, element):
        if getattr(element, "parent", lambda: None)() is not self:
            raise TypeError("the backend crossing requires an element of this preamble group")
        backend = getattr(element, "_backend", None)
        if not callable(backend):
            raise TypeError("the preamble group element has no represented backend value")
        return backend()

    def _from_engine(self, element):
        if getattr(element, "parent", lambda: None)() is not self._engine:
            element = self._engine(element)
        return self.element_class(self, element)

    def __call__(self, value):
        r"""Construct an owned group element without Sage coercion discovery."""
        return self._element_constructor_(value)

    def _element_constructor_(self, value):
        parent = getattr(value, "parent", lambda: None)()
        if parent is self:
            return value
        if parent is not None and parent in OwnedGroups():
            to_engine = getattr(parent, "_to_engine", None)
            if callable(to_engine):
                try:
                    return self._from_engine(self._engine(to_engine(value)))
                except TypeError, ValueError:
                    pass
        if isinstance(value, SageObject):
            raise TypeError("raw backend group elements are not accepted by the public preamble API")
        return self._from_engine(self._engine(value))

    def __contains__(self, value) -> bool:
        return isinstance(value, _OwnedGroupElement) and value.parent() is self

    def __iter__(self):
        return (self._from_engine(element) for element in self._engine)

    def one(self):
        return self._from_engine(self._engine.one())

    def _repr_(self):
        return repr(self._engine)

    def _latex_(self):
        return str(latex(self._engine))


class _TransportedGroupSubobject(Parent):
    r"""A subgroup of a preamble group computed by a private backend subgroup."""

    def __init__(self, supergroup, engine_subgroup) -> None:
        self._supergroup = supergroup
        self._preamble_supergroup = supergroup
        self._engine = engine_subgroup
        Parent.__init__(
            self,
            facade=supergroup,
            category=Category.join((_owned_group_category(engine_subgroup), Subgroups(supergroup))),
        )
        realize_owned_category(self)

    def _engine_group(self):
        return self._engine

    def _to_engine(self, element):
        if element not in self._supergroup:
            raise TypeError("the subgroup crossing requires an ambient preamble element")
        return self._engine(self._supergroup._to_engine(element))

    def _from_engine(self, element):
        return self._supergroup._from_engine(element)

    def __call__(self, value):
        r"""Construct a subgroup element without Sage coercion discovery."""
        return self._element_constructor_(value)

    def _element_constructor_(self, value):
        if value not in self._supergroup:
            raise TypeError("a subgroup element must be an ambient preamble element")
        backend = self._supergroup._to_engine(value)
        if backend not in self._engine:
            raise ValueError(f"{value} is not in this subgroup")
        return value

    def __contains__(self, value) -> bool:
        if value not in self._supergroup:
            return False
        try:
            return self._supergroup._to_engine(value) in self._engine
        except TypeError, ValueError:
            return False

    def __iter__(self):
        return (self._supergroup._from_engine(element) for element in self._engine)

    def one(self):
        return self._supergroup.one()

    def supergroup(self):
        return self._supergroup

    def _repr_(self):
        return f"Subgroup of {self._supergroup}"


_OWNED_GROUPS: WeakValueDictionary = WeakValueDictionary()


def _owned_group(group):
    r"""Return ``group`` after asserting that it is already a preamble group."""
    if group not in OwnedGroups():
        raise TypeError("this API expects a preamble group")
    return group


def _own_group(group):
    """Return the owned group over the Sage group ``group``, one per engine."""
    if group in OwnedGroups():
        return group
    if group not in SageGroups():
        raise TypeError(f"{group} is not a group")
    # Keyed by identity: Sage groups compare structurally, and a subgroup
    # equal to a freestanding group must keep its own containing group.
    owned = _OWNED_GROUPS.get(id(group))
    if owned is None:
        owned = OwnedGroup(group)
        _OWNED_GROUPS[id(group)] = owned
    return owned


# --------------------------------------------------------------------------
# Constructor catalogue.
# --------------------------------------------------------------------------


def _group_constructor_argument(value):
    r"""Cross preamble constructor data into a Sage group-constructor input."""

    try:
        if value in OwnedRings():
            return _engine_ring(value)
    except AttributeError, TypeError, ValueError:
        pass

    parent = getattr(value, "parent", lambda: None)()
    if parent is not None:
        try:
            if parent in OwnedGroups():
                return _element_to_engine(parent, value)
        except AttributeError, NameError, NotImplementedError, TypeError, ValueError:
            pass
        try:
            if parent in OwnedRings():
                return _engine_element(parent, value)
        except AttributeError, TypeError, ValueError:
            pass
        try:
            base_ring = parent.base_ring()
            if parent in MatrixSpaces(base_ring):
                return _engine_matrix(value)
        except AttributeError, TypeError, ValueError:
            pass

    if isinstance(value, tuple):
        return tuple(_group_constructor_argument(entry) for entry in value)
    if isinstance(value, list):
        return [_group_constructor_argument(entry) for entry in value]
    if isinstance(value, dict):
        return {_group_constructor_argument(key): _group_constructor_argument(entry) for key, entry in value.items()}
    return value


def _owned_group_constructor(constructor):
    @wraps(constructor)
    def construct(*args, **kwargs):
        return _own_group(
            constructor(
                *tuple(_group_constructor_argument(argument) for argument in args),
                **{name: _group_constructor_argument(argument) for name, argument in kwargs.items()},
            )
        )

    return staticmethod(construct)


def _free_group_constructor(n=None, names="x", index_set=None, abelian=False, **kwds):
    from sage.groups.misc_gps.misc_groups_catalog import Free as SageFree

    engine_label = _group_constructor_argument
    if index_set is None:
        backend_index_set = None
    else:
        if index_set not in Sets():
            raise TypeError("a free-group index set must be an owned set")
        try:
            size = cardinal(index_set.cardinality())
            finite_index_set = size.is_finite()
        except AttributeError, TypeError, ValueError:
            finite_index_set = getattr(index_set, "is_finite", lambda: False)() is True
        if finite_index_set:
            backend_index_set = tuple(engine_label(label) for label in index_set)

            def owned_label(backend_label):
                for label in index_set:
                    if engine_label(label) == backend_label:
                        return label
                raise ValueError(f"{backend_label!r} is not in the backend free basis")
        else:
            backend_index_set = _group_constructor_argument(index_set)
            if backend_index_set is index_set:

                def engine_label(label):
                    return label

                def owned_label(label):
                    return label
            else:
                if index_set in OwnedRings():
                    owned_label = index_set._from_engine_element
                else:

                    def owned_label(label):
                        return label

    owned = _own_group(
        SageFree(
            _group_constructor_argument(n) if n is not None else None,
            _group_constructor_argument(names),
            index_set=backend_index_set,
            abelian=abelian,
            **{name: _group_constructor_argument(value) for name, value in kwds.items()},
        )
    )
    if index_set is not None:
        owned._preamble_free_basis = index_set
        owned._preamble_free_basis_engine_label = engine_label
        owned._preamble_free_basis_owned_label = owned_label
    return owned


def _group_over_ring(constructor, degree, ring, *args, **kwargs):

    owned_ring = _owned_ring(ring)
    return _own_group(
        constructor(
            _group_constructor_argument(degree),
            _engine_ring(owned_ring),
            *tuple(_group_constructor_argument(argument) for argument in args),
            **{name: _group_constructor_argument(argument) for name, argument in kwargs.items()},
        )
    )


def _GL(degree, ring, var="a"):
    from sage.groups.matrix_gps.catalog import GL

    return _group_over_ring(GL, degree, ring, var=var)


def _SL(degree, ring, var="a"):
    from sage.groups.matrix_gps.catalog import SL

    return _group_over_ring(SL, degree, ring, var=var)


def _Sp(degree, ring, var="a", invariant_form=None):
    from sage.groups.matrix_gps.catalog import Sp

    return _group_over_ring(Sp, degree, ring, var=var, invariant_form=invariant_form)


def _GU(degree, ring, var="a", invariant_form=None):
    from sage.groups.matrix_gps.catalog import GU

    return _group_over_ring(GU, degree, ring, var=var, invariant_form=invariant_form)


def _SU(degree, ring, var="a", invariant_form=None):
    from sage.groups.matrix_gps.catalog import SU

    return _group_over_ring(SU, degree, ring, var=var, invariant_form=invariant_form)


def _GO(degree, ring, e=0, var="a", invariant_form=None):
    from sage.groups.matrix_gps.catalog import GO

    return _group_over_ring(GO, degree, ring, e=e, var=var, invariant_form=invariant_form)


def _SO(degree, ring, e=None, var="a", invariant_form=None):
    from sage.groups.matrix_gps.catalog import SO

    return _group_over_ring(SO, degree, ring, e=e, var=var, invariant_form=invariant_form)


def _Affine(degree, ring):
    from sage.groups.affine_gps.catalog import Affine

    return _group_over_ring(Affine, degree, ring)


def _Euclidean(degree, ring):
    from sage.groups.affine_gps.catalog import Euclidean

    return _group_over_ring(Euclidean, degree, ring)


def _Heisenberg(degree=1, ring=0):
    from sage.groups.matrix_gps.catalog import Heisenberg

    scalar_ring = ring if ring == 0 else _engine_ring(ring)
    return _own_group(Heisenberg(_group_constructor_argument(degree), scalar_ring))


def _SemimonomialTransformation(ring, degree):
    from sage.groups.misc_gps.misc_groups_catalog import SemimonomialTransformation

    return _own_group(SemimonomialTransformation(_engine_ring(ring), _group_constructor_argument(degree)))


def _SmallGroup(order, index):
    from sage.groups.perm_gps.permgroup import PermutationGroup

    model = (
        libgap.SmallGroup(
            _group_constructor_argument(order),
            _group_constructor_argument(index),
        )
        .IsomorphismPermGroup()
        .Image()
    )
    return _own_group(PermutationGroup(gap_group=model))


def _Coxeter(data, implementation="reflection", base_ring=None, index_set=None):
    from sage.groups.misc_gps.misc_groups_catalog import CoxeterGroup

    scalar_ring = None if base_ring is None else _engine_ring(base_ring)
    return _own_group(
        CoxeterGroup(
            data,
            implementation=implementation,
            base_ring=scalar_ring,
            index_set=index_set,
        )
    )


# --------------------------------------------------------------------------
# Subgroup inclusions and the Hom packet.
# --------------------------------------------------------------------------


class SubgroupInclusion(SetMorphism):
    def is_injective(self):
        return True


def _group_inclusion_image(subgroup, containing_group, element):
    match subgroup:
        case OwnedGroup():
            match subgroup._engine:
                case AbelianGroup_subgroup() as engine:
                    image = containing_group.one()
                    for generator, exponent in zip(engine.gens(), element.exponents(), strict=True):
                        image *= containing_group(generator) ** exponent
                    return image
    return containing_group(element)


def _canonical_subgroup_inclusion(subgroup):
    containing_group = subgroup.supergroup()
    return SubgroupInclusion(
        subgroup.Mor(containing_group),
        lambda element: _group_inclusion_image(subgroup, containing_group, element),
    )


def _element_to_engine(group, element):

    match group:
        case GroupAutomorphismGroup():
            return element.gap()
        case _ if _elements_have_gap_models(group):
            return group._to_engine(group(element)).gap()
        case _:
            raise NotImplementedError(f"{group}'s GAP model does not retain an elementwise identification")


def _element_from_engine(group, _engine_element):

    match group:
        case GroupAutomorphismGroup():
            return group(_engine_element, check=False)
        case _ if _elements_have_gap_models(group):
            return group._from_engine(_engine_group(group)(_engine_element))
        case _:
            raise NotImplementedError(f"{group}'s GAP model does not retain an elementwise identification")


class IndexedFreeGroupHomomorphism(Morphism):
    r"""A morphism out of the free group on a chosen set.

    The free group on an arbitrary set has no elementwise GAP model.  Its
    universal morphisms are therefore evaluated directly on reduced words
    instead of forcing this object through the unrelated libGAP path.
    """

    def __init__(self, parent, images) -> None:
        Morphism.__init__(self, parent)
        indices = self.domain().free_basis()
        set_homset = Sets().Mor(indices, self.codomain())
        if isinstance(images, SetMorphism):
            if images.domain() is not indices or images.codomain() is not self.codomain():
                raise ValueError("the generator map has the wrong source or target")
            self._generator_morphism = images
        elif isinstance(images, dict):
            if indices.cardinality() == infinity:
                raise ValueError("an infinite indexed free group requires a set morphism on its index set")
            missing = [index for index in indices if index not in images]
            if missing:
                raise ValueError(f"generator assignment omits {missing}")
            self._generator_morphism = SetMorphism(set_homset, images.__getitem__)
        elif callable(images):
            self._generator_morphism = SetMorphism(set_homset, images)
        else:
            raise TypeError("an indexed-free-group morphism is specified on its index set")

    def generator_morphism(self):
        return self._generator_morphism

    def _call_(self, element):
        value = self.codomain().one()
        for index, sign in self.domain().reduced_word(element):
            image = self.generator_morphism()(index)
            value *= image if sign == 1 else image**-1
        return value

    def postcompose(self, morphism):
        if morphism.domain() is not self.codomain():
            raise ValueError("group-morphism composition requires matching middle groups")
        indices = self.domain().free_basis()
        return group_homset(self.domain(), morphism.codomain())(
            SetMorphism(
                Sets().Mor(indices, morphism.codomain()),
                lambda index: morphism(self.generator_morphism()(index)),
            )
        )

    def __mul__(self, other):

        if other.codomain() is not self.domain():
            return NotImplemented
        if other.domain() not in GroupsWithChosenFreeBasis():
            return NotImplemented
        indices = other.domain().free_basis()
        return group_homset(other.domain(), self.codomain())(
            SetMorphism(
                Sets().Mor(indices, self.codomain()),
                lambda index: self(other(other.domain().free_generator(index))),
            )
        )


class IndexedFreeGroupHomset(CategoricalHomset):
    """The canonical Hom-set out of the free group on a chosen set."""

    Element = IndexedFreeGroupHomomorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        category = Monoids() if domain is codomain else None
        CategoricalHomset.__init__(
            self,
            hom_family,
            domain,
            codomain,
            category=category,
        )
        realize_owned_category(self)

    def _element_constructor_(self, images, **_options):
        return self.element_class(self, images)

    def _repr_(self):
        return f"Hom({self.domain()}, {self.codomain()})"


class GroupHomomorphism(GroupMorphism_libgap):
    """A group homomorphism represented by Sage's maintained GAP morphism."""

    def __eq__(self, other):
        r"""Decide equality on a finite generating family of the source."""
        if getattr(other, "parent", lambda: None)() is not self.parent():
            return False
        if self is other:
            return True

        source = _gap_model(self.domain())
        return all(self(_element_from_engine(self.domain(), generator)) == other(_element_from_engine(self.domain(), generator)) for generator in source.GeneratorsOfGroup())

    def __ne__(self, other):
        return not self == other

    def __mul__(self, other):
        if isinstance(other, IndexedFreeGroupHomomorphism):
            return other.postcompose(self)
        if not isinstance(other, GroupHomomorphism) or other.codomain() is not self.domain():
            return NotImplemented
        source = other.domain()
        backend_generators = _gap_model(source).GeneratorsOfGroup()
        return group_homset(source, self.codomain())(tuple(self(other(_element_from_engine(source, generator))) for generator in backend_generators))

    def _call_(self, element):
        model = _element_to_engine(self.domain(), element)
        if self.parent()._twisted:
            model = model.Inverse()
        return _element_from_engine(self.codomain(), self.gap().Image(model))

    def lift(self, element):
        r"""Return one preimage of ``element``."""
        _engine_element = _element_to_engine(self.codomain(), element)
        if _engine_element not in self.gap().Image():
            raise ValueError(f"{element} is not in the image of {self}")
        preimage = self.gap().PreImagesRepresentative(_engine_element)
        if self.parent()._twisted:
            preimage = preimage.Inverse()
        return _element_from_engine(self.domain(), preimage)

    def kernel(self):

        return _subgroup_from_gap(self.domain(), self.gap().Kernel())

    def image(self):

        return _subgroup_from_gap(self.codomain(), self.gap().Image())

    def is_injective(self):
        return bool(self.gap().IsInjective())

    def is_surjective(self):
        return bool(self.gap().IsSurjective())


class GroupHomset(GroupHomset_libgap, CategoricalHomset):
    """The canonical owned homset Hom(G,H)."""

    Element = GroupHomomorphism

    @staticmethod
    def __classcall__(cls, family, domain, codomain):
        return typecall(cls, family, domain, codomain)

    def __init__(self, hom_family, domain, codomain, *, category=None):
        self._family = hom_family
        self._end_family = None
        self._aut_family = None
        self._domain_object = domain
        self._codomain_object = codomain
        # When exactly one endpoint multiplies as its engine reversed, an owned
        # morphism Phi is an engine anti-morphism; it is represented by the
        # engine morphism phi(x) = Phi(x^-1), and read back through inverses.
        self._twisted = _law_reversed(domain) != _law_reversed(codomain)
        self._super_categories_for_classes = [Objects()]
        Category.__init__(self)
        GroupHomset_libgap.__init__(self, domain, codomain, category=SageGroups(), check=False)
        placement = []
        if domain is codomain:
            placement.append(Monoids())
        if category is not None:
            placement.append(category)
        if placement:
            CategoryObject._refine_category_(self, Category.join(tuple(placement)))
            realize_owned_category(self)

    def _element_constructor_(self, images, check=True, **_options):
        match images:
            case dict():
                return self._from_group_generator_images(images, check=check)
            case GapElement():
                return self._from_gap_homomorphism(images, check=check)
            case Morphism() if images.parent() is self:
                return images
            case tuple() | list():
                return self._from_gap_generator_images(images, check=check)
        raise TypeError(f"unable to convert {images!r} to an element of {self}")

    def _from_gap_homomorphism(self, gap_homomorphism, check=True):

        if check:
            if gap_homomorphism.Source() != _gap_model(self.domain()):
                raise ValueError("the GAP homomorphism has the wrong source")
            if gap_homomorphism.Range() != _gap_model(self.codomain()):
                raise ValueError("the GAP homomorphism has the wrong range")
        return self.element_class(self, gap_homomorphism, check=False)

    def _from_engine_generator_images(self, generator_models, image_models, check=True):

        source = _gap_model(self.domain())
        target = _gap_model(self.codomain())
        if self._twisted:
            image_models = [model.Inverse() for model in image_models]
        if check:
            engine = libgap.GroupHomomorphismByImages(source, target, generator_models, image_models)
            if engine.is_bool():
                raise ValueError("the images do not satisfy the domain relations")
        else:
            engine = libgap.GroupHomomorphismByImagesNC(source, target, generator_models, image_models)
        return self.element_class(self, engine, check=False)

    def _from_group_generator_images(self, images, check=True):
        domain = self.domain()
        codomain = self.codomain()
        generators = tuple(domain.group_generators())
        if set(images) != set(generators):
            raise ValueError("the assignment must name exactly the distinguished group generators")
        return self._from_engine_generator_images(
            [_element_to_engine(domain, g) for g in generators],
            [_element_to_engine(codomain, codomain(images[g])) for g in generators],
            check=check,
        )

    def _from_gap_generator_images(self, images, check=True):
        r"""Images listed in the order of the GAP model's own generators."""

        codomain = self.codomain()
        return self._from_engine_generator_images(
            list(_gap_model(self.domain()).GeneratorsOfGroup()),
            [_element_to_engine(codomain, codomain(image)) for image in images],
            check=check,
        )

    def _repr_(self):
        return f"Hom({self.domain()}, {self.codomain()})"


@cached_function
def group_homset(domain, codomain):
    return domain.Mor(codomain)


class GroupAutomorphism(GroupHomomorphism):
    pass


class GroupAutomorphismGroups(OwnedCategory):
    def super_categories(self):
        return [OwnedGroups()]

    class ParentMethods:
        @cached_method
        def _libgap_(self):

            if self._engine_subgroup is not None:
                return self._engine_subgroup
            return _automorphism_gap_model(self.domain())

        def one(self):
            return self(libgap.IdentityMapping(_gap_model(self.domain())), check=False)

        def supergroup(self):
            return self._supergroup

        @cached_method
        def group_generators(self):
            backend_generators = self._libgap_().GeneratorsOfGroup()
            positions = Sets.Δ[len(backend_generators) - 1]
            return finite_ordered_image(
                positions,
                lambda position: self(
                    backend_generators[int(position)],
                    check=False,
                ),
                name=f"Group generators of {self}",
            )

        def number_of_group_generators(self):
            return ZZ(self.group_generators().cardinality())

        def cardinality(self):
            domain = self.domain()
            if domain in OwnedFiniteGroups():
                return cardinal(_finite_order(self))
            if domain in GroupsWithChosenFreeBasis():
                basis_cardinality = domain.free_basis().cardinality()
                if basis_cardinality.is_finite():
                    rank = int(basis_cardinality.finite_value())
                    if rank == 0:
                        return cardinal(1)
                    if rank == 1:
                        return cardinal(2)
                    return aleph(0)
            return OwnedGroups.ParentMethods.cardinality(self)

        def _repr_(self):
            if self._engine_subgroup is not None:
                return f"Subgroup of Aut({self.domain()})"
            return f"Aut({self.domain()})"

    class ElementMethods:
        def inverse(self):
            return self.parent()(self.gap().InverseGeneralMapping(), check=False)

        def _composition_(self, right, homset):
            if right.parent() is not self.parent():
                raise ValueError("automorphisms must belong to one automorphism group")
            return self.parent()(right.gap() * self.gap(), check=False)


class GroupAutomorphismGroup(GroupHomset):
    Element = GroupAutomorphism

    @staticmethod
    def __classcall__(cls, hom_family, group, engine_subgroup=None):
        return typecall(cls, hom_family, group, engine_subgroup=engine_subgroup)

    def __init__(self, hom_family, group, engine_subgroup=None):
        self._engine_subgroup = engine_subgroup
        self._supergroup = self
        categories = [GroupAutomorphismGroups()]
        if group.is_finite() is True:
            categories.append(OwnedFiniteGroups())
        GroupHomset.__init__(
            self,
            hom_family,
            group,
            group,
            category=Category.join(tuple(categories)),
        )

    def super_categories(self):
        packet = category_packet(self.base_category())
        group = self.domain()
        supers = [
            packet.Homs().Of(group, group),
            packet.Monos().Of(group, group),
            packet.Epis().Of(group, group),
        ]
        supers.extend(superpacket.Isos().Of(group, group) for superpacket in packet.super_packets() if group in superpacket.C())
        if self.aut_family() is not None:
            supers.append(packet.Ends().Of(group))
            supers.extend(superpacket.Auts().Of(group) for superpacket in packet.super_packets() if group in superpacket.C())
        return supers

    def identity(self):

        return self(libgap.IdentityMapping(_gap_model(self.domain())), check=False)

    one = identity
    identity_automorphism = identity

    def set_supergroup(self, supergroup):
        self._supergroup = supergroup

    def _element_constructor_(self, images, check=True, **options):
        if isinstance(images, GapElement):
            automorphism = self.element_class(self, images, check=False)
        else:
            automorphism = super()._element_constructor_(images, check=check, **options)
        if check and not bool(automorphism.gap().IsBijective()):
            raise ValueError("the endomorphism is not invertible")
        return automorphism

    def _subgroup_from_engine(self, engine_subgroup):
        subgroup = GroupAutomorphismGroup(
            self.hom_family(),
            self.domain(),
            engine_subgroup=engine_subgroup,
        )
        subgroup.set_supergroup(self)
        return subgroup


class GroupHomCategoryConstruction(HomCategoryConstruction):
    r"""The represented Hom categories of owned groups."""

    def Of(self, domain, codomain=None):
        if codomain is None:
            codomain = domain
        if domain not in self.base_category() or codomain not in self.base_category():
            raise TypeError("a group Hom requires two owned groups")
        cached = self._cached_between(domain, codomain)
        if cached is not None:
            return cached

        fixed_class = IndexedFreeGroupHomset if domain in GroupsWithChosenFreeBasis() else GroupHomset
        result = fixed_class(self, domain, codomain)
        return self._remember_between(domain, codomain, result)


class GroupEndCategoryConstruction(EndCategoryConstruction):
    r"""Endomorphism monoids of groups, on the same underlying set as ``Hom(G,G)``."""

    def Of(self, obj, codomain=None):
        if codomain is not None and codomain is not obj:
            raise ValueError("a group endomorphism category has equal endpoints")
        if obj not in self.base_category():
            raise TypeError("the endomorphism object must be an owned group")
        cached = self._cached_between(obj, obj)
        if cached is not None:
            return cached
        endomorphisms = self.base_category().Mor(obj, obj)
        endomorphisms.attach_end_family(self)
        return self._remember_between(obj, obj, endomorphisms)


class GroupIsoCategoryConstruction(IsoCategoryConstruction):
    r"""Group isomorphisms, using the maintained automorphism group on the diagonal."""

    def Of(self, domain, codomain=None):
        if codomain is None:
            codomain = domain
        if domain is not codomain:
            return super().Of(domain, codomain)

        # A free group on a set has no GAP elementwise model, so its
        # automorphism group has no stronger computational parent than the
        # generic Iso object.
        if domain in GroupsWithChosenFreeBasis():
            return super().Of(domain, codomain)

        cached = self._cached_between(domain, domain)
        if cached is not None:
            return cached
        result = GroupAutomorphismGroup(self, domain)
        return self._remember_between(domain, domain, result)


# --------------------------------------------------------------------------
# The owned categories.
# --------------------------------------------------------------------------


class OwnedGroups(CategoryPacketMethods, OwnedCategory):
    """Groups whose notebook-facing group interface is owned by the preamble."""

    from sage.groups.abelian_gps.abelian_group import AbelianGroup as _SageAbelianGroup
    from sage.groups.lie_gps.catalog import Nilpotent as _SageNilpotent
    from sage.groups.misc_gps.misc_groups_catalog import (
        Artin as _SageArtin,
    )
    from sage.groups.misc_gps.misc_groups_catalog import (
        Braid as _SageBraid,
    )
    from sage.groups.misc_gps.misc_groups_catalog import (
        Cactus as _SageCactus,
    )
    from sage.groups.misc_gps.misc_groups_catalog import (
        Free as _SageFree,
    )
    from sage.groups.misc_gps.misc_groups_catalog import (
        PureCactus as _SagePureCactus,
    )
    from sage.groups.misc_gps.misc_groups_catalog import (
        ReflectionGroup as _SageReflection,
    )
    from sage.groups.misc_gps.misc_groups_catalog import (
        RightAngledArtin as _SageRightAngledArtin,
    )
    from sage.groups.misc_gps.misc_groups_catalog import (
        WeylGroup as _SageWeyl,
    )
    from sage.groups.perm_gps.permgroup_named import (
        AlternatingGroup as _SageAlternatingGroup,
    )
    from sage.groups.perm_gps.permgroup_named import (
        CyclicPermutationGroup as _SageCyclicGroup,
    )
    from sage.groups.perm_gps.permgroup_named import (
        DiCyclicGroup as _SageDiCyclicGroup,
    )
    from sage.groups.perm_gps.permgroup_named import (
        DihedralGroup as _SageDihedralGroup,
    )
    from sage.groups.perm_gps.permgroup_named import (
        KleinFourGroup as _SageKleinFourGroup,
    )
    from sage.groups.perm_gps.permgroup_named import (
        QuaternionGroup as _SageQuaternionGroup,
    )
    from sage.groups.perm_gps.permgroup_named import (
        SymmetricGroup as _SageSymmetricGroup,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        PGL as _SagePGL,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        PGU as _SagePGU,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        PSL as _SagePSL,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        PSU as _SagePSU,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        ComplexReflection as _SageComplexReflection,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        Janko as _SageJanko,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        Mathieu as _SageMathieu,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        PSp as _SagePSp,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        RubiksCube as _SageRubiksCube,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        Suzuki as _SageSuzuki,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        SuzukiSporadic as _SageSuzukiSporadic,
    )
    from sage.groups.perm_gps.permutation_groups_catalog import (
        Transitive as _SageTransitive,
    )

    def an_object(self):
        r"""The cyclic group of order two.

        The smallest group that is not the trivial one, so a construction over an
        arbitrary group is exercised on a group with a non-identity element.
        """
        return self.C(2)

    C = _owned_group_constructor(_SageCyclicGroup)
    S = _owned_group_constructor(_SageSymmetricGroup)
    A = _owned_group_constructor(_SageAlternatingGroup)
    D = _owned_group_constructor(_SageDihedralGroup)
    Dic = _owned_group_constructor(_SageDiCyclicGroup)
    Q = _owned_group_constructor(_SageQuaternionGroup)
    V4 = _owned_group_constructor(_SageKleinFourGroup)
    Abelian = _owned_group_constructor(_SageAbelianGroup)
    Free = staticmethod(_free_group_constructor)
    Artin = _owned_group_constructor(_SageArtin)
    Braid = _owned_group_constructor(_SageBraid)
    Cactus = _owned_group_constructor(_SageCactus)
    PureCactus = _owned_group_constructor(_SagePureCactus)
    Coxeter = staticmethod(_Coxeter)
    Weyl = _owned_group_constructor(_SageWeyl)
    Reflection = _owned_group_constructor(_SageReflection)
    RightAngledArtin = _owned_group_constructor(_SageRightAngledArtin)
    GL = staticmethod(_GL)
    SL = staticmethod(_SL)
    Sp = staticmethod(_Sp)
    GU = staticmethod(_GU)
    SU = staticmethod(_SU)
    GO = staticmethod(_GO)
    SO = staticmethod(_SO)
    Heisenberg = staticmethod(_Heisenberg)
    SemimonomialTransformation = staticmethod(_SemimonomialTransformation)
    Affine = staticmethod(_Affine)
    Euclidean = staticmethod(_Euclidean)
    Nilpotent = _owned_group_constructor(_SageNilpotent)
    SmallGroup = staticmethod(_SmallGroup)
    ComplexReflection = _owned_group_constructor(_SageComplexReflection)
    Mathieu = _owned_group_constructor(_SageMathieu)
    Janko = _owned_group_constructor(_SageJanko)
    Suzuki = _owned_group_constructor(_SageSuzuki)
    SuzukiSporadic = _owned_group_constructor(_SageSuzukiSporadic)
    PGL = _owned_group_constructor(_SagePGL)
    PSL = _owned_group_constructor(_SagePSL)
    PSp = _owned_group_constructor(_SagePSp)
    PGU = _owned_group_constructor(_SagePGU)
    PSU = _owned_group_constructor(_SagePSU)
    Transitive = _owned_group_constructor(_SageTransitive)
    RubiksCube = _owned_group_constructor(_SageRubiksCube)

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a group Hom requires two owned groups")
        return self.HomCategory().Of(domain, codomain)

    def group_algebra(self, base_ring):
        r"""The functor \(R[-]\colon \mathbf{Grp}\to\mathbf{Alg}_R\)."""
        from dzack_research.preamble.categories.algebras.group_algebras import (
            GroupAlgebraFunctor,
        )

        return GroupAlgebraFunctor(base_ring)

    _HomCategory = GroupHomCategoryConstruction
    _EndCategory = GroupEndCategoryConstruction
    _IsoCategory = GroupIsoCategoryConstruction

    @classmethod
    def _repr_object_names(cls):
        return "groups"

    def super_categories(self):
        return [Monoids()]

    class SubcategoryMethods:
        r"""Constructions this category owns, reachable from any subcategory."""

        # Functors out of ``Grp``, each spelled as a method of this, their
        # domain category, and named by the construction it performs.

        def abelianization(self):
            r"""``(-)^ab : Grp -> Ab``, the abelianization functor.

            A group is sent to its quotient by the derived subgroup, and a
            group morphism to the morphism the universal property of that
            quotient determines.  Left adjoint of the inclusion of abelian
            groups; the adjunction is ``abelianization_adjunction``.
            """
            from dzack_research.preamble.categories.functors.abelianization import (
                abelianization_functor,
            )

            return abelianization_functor()

        def abelianization_adjunction(self):
            r"""``(-)^ab -| i`` between ``Grp`` and ``Ab``.

            An adjunction is a method of its left adjoint's domain category,
            and ``(-)^ab`` is the left adjoint.  Its unit at ``G`` is the
            quotient projection onto ``G/[G,G]``, and its counit identifies an
            abelian group with its own abelianization.
            """
            from dzack_research.preamble.categories.functors.abelianization import (
                abelianization_adjunction,
            )

            return abelianization_adjunction()

        def underlying_set(self):
            r"""``U : Grp -> Set``, the underlying-set functor.

            The right adjoint of the free-group functor spelled on ``Set``.
            On an object it is the identity: a group already is a set object,
            and forgetting the multiplication removes structure, not elements.
            """
            from dzack_research.preamble.categories.functors.free_groups import (
                group_underlying_set_functor,
            )

            return group_underlying_set_functor()

    class ElementMethods:
        def inverse(self):
            r"""Return the group inverse."""
            return ~self

    class ParentMethods:
        @cached_method
        def classifying_category(self):
            r"""Return ``BG``, with one object and this group's elements as arrows."""
            from dzack_research.preamble.categories.group.classifying_categories import (
                ClassifyingCategory,
            )

            return ClassifyingCategory(self)

        def Mor(self, codomain, category=None):
            groups = OwnedGroups()
            if category is None or (isinstance(category, OwnedCategory) and category.is_subcategory(groups)):
                return groups.Mor(self, codomain)
            return _category_homset(category, self, codomain)

        def _Hom_(self, codomain, category=None):
            groups = OwnedGroups()
            if codomain in groups and (category is None or category.is_subcategory(groups)):
                return groups.Mor(self, codomain)
            raise TypeError("the requested Hom category is not a group category")

        def is_finite(self):
            return Unknown

        def is_abelian(self):
            if self in OwnedAbelianGroups():
                return True
            if self in OwnedFiniteGroups():
                try:
                    return bool(_gap_model(self).IsAbelian())
                except NotImplementedError:
                    return Unknown
            return Unknown

        def is_finitely_generated(self):
            if self in OwnedFinitelyGeneratedGroups():
                return True
            return Unknown

        def is_finitely_presented(self):
            return True if self in OwnedFinitelyPresentedGroups() else Unknown

        def is_arithmetic_group(self):
            match self:
                case OwnedGroup() if _is_arithmetic_witness(self._engine):
                    return True
            return Unknown

        def cardinality(self):
            if self in OwnedFiniteGroups():
                return cardinal(_finite_order(self))
            if self in GroupsWithChosenFreeBasis():
                basis_cardinality = self.free_basis().cardinality()
                if basis_cardinality == cardinal(0):
                    return cardinal(1)
                return Cardinalities().supremum(aleph(0), basis_cardinality)
            if self in OwnedInfiniteGroups() and self in OwnedFinitelyGeneratedGroups():
                # A finitely generated group is countable.
                return aleph(0)
            assert False, "cardinality is defined for every group, but the current exact computation requires a finite group or a represented infinite finitely generated group"

        def order(self):
            r"""Return the group order as an integer when finite, else its cardinality."""
            if self in OwnedFiniteGroups():
                return _finite_order(self)
            return self.cardinality()

        def subgroup(self, generators):
            return _engine_subgroup(self, generators)

        def supergroup(self):
            return _engine_supergroup(self)

        def inclusion(self):
            return _canonical_subgroup_inclusion(self)

        def End(self):
            return OwnedGroups().End(self)

        @cached_method
        def Aut(self):
            return OwnedGroups().Aut(self)

        def is_isomorphic_to(self, other):
            if self.is_finite() is not True or other.is_finite() is not True:
                return Unknown
            found = _gap_model(self).IsomorphismGroups(_gap_model(other))
            return str(found) != "fail"

    class Commutative(CategoryWithAxiom):
        def an_object(self):
            r"""The cyclic group of order two."""
            return OwnedGroups().C(2)

        @classmethod
        def _repr_object_names(cls):
            return "abelian groups"

        class ElementMethods:
            def __rmul__(self, exponent):
                r"""Return the canonical integer multiple of an abelian-group element."""
                return self.parent().scalar_multiple(exponent, self)

        class ParentMethods:
            def is_abelian(self):
                return True

            @cached_method
            def endomorphism_ring(self):
                return _AbelianEndomorphismRingParent(self)

            @cached_method
            def scalar_action(self):

                integers = _own_ring(ZZ)
                endomorphisms = self.endomorphism_ring()
                additive = self.category().is_subcategory(AdditiveGroups().AdditiveCommutative())

                def multiple(exponent, element):
                    return exponent * element if additive else element ** int(exponent)

                return ring_morphism(
                    integers,
                    endomorphisms,
                    lambda exponent: endomorphisms(lambda element: multiple(exponent, element)),
                )

            def scalar_multiple(self, exponent, element):

                return self.scalar_action()(_own_ring(ZZ)(exponent))(element)

    class Finite(CategoryWithAxiom):
        def an_object(self):
            r"""The cyclic group of order two."""
            return OwnedGroups().C(2)

        @classmethod
        def _repr_object_names(cls):
            return "finite groups"

        class ParentMethods:
            def is_finite(self):
                return True

            def conjugacy_classes_representatives(self):
                classes = _gap_model(self).ConjugacyClasses()
                return finite_ordered_image(
                    Sets.Δ[len(classes) - 1],
                    lambda position: _element_from_engine(
                        self,
                        classes[int(position)].Representative(),
                    ),
                    name="Conjugacy-class representatives",
                )

            @cached_method
            def irreducible_characters(self):
                r"""The complex irreducible characters, as class functions.

                Values lie in the cyclotomic field of the group's exponent
                and are read on the chosen conjugacy-class representatives,
                in the order GAP's ``Irr`` lists them.
                """
                from dzack_research.preamble.categories.group.class_functions import (
                    finite_group_class_function,
                )
                from dzack_research.preamble.categories.rings.number_fields import (
                    CyclotomicField,
                )

                gap_group = _gap_model(self)
                exponent = int(gap_group.Exponent())
                field = CyclotomicField(exponent)
                engine_field = _engine_ring(field)
                representatives = self.conjugacy_classes_representatives()
                # One class-function object per character: the set is the
                # index of isotypic components and is compared by identity.
                return finite_ordered_set(
                    tuple(
                        finite_group_class_function(
                            self,
                            field,
                            tuple(field._from_engine_element(engine_field(value.sage())) for value in character.List()),
                            representatives=representatives,
                        )
                        for character in gap_group.Irr()
                    )
                )

            @cached_method
            def character_table(self):
                r"""The character table: rows the irreducible characters, columns the classes.

                A square matrix over the cyclotomic field of the group's
                exponent, the row and column orders being those of
                ``irreducible_characters()`` and
                ``conjugacy_classes_representatives()``.
                """
                from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                    MatrixSpace,
                )

                characters = self.irreducible_characters()
                size = int(characters.cardinality())
                field = characters[0].codomain()
                return MatrixSpace(field, size, size).from_rows(tuple(tuple(character.values()) for character in characters))

            def left_cosets(self, subgroup):
                r"""Return the set of left cosets ``gH``, each an ordered set of elements."""
                return _engine_cosets(self, subgroup, "left")

            def right_cosets(self, subgroup):
                r"""Return the set of right cosets ``Hg``, each an ordered set of elements."""
                return _engine_cosets(self, subgroup, "right")

    class Infinite(CategoryWithAxiom):
        @classmethod
        def _repr_object_names(cls):
            return "infinite groups"

        class ParentMethods:
            def is_finite(self):
                return False


class TopologicalGroups(OwnedCategory):
    r"""Owned groups equipped with a represented compatible topology."""

    def super_categories(self):
        return [OwnedGroups()]

    class ParentMethods:
        def is_topological_group(self) -> bool:
            return True


class OwnedFinitelyGeneratedGroups(OwnedCategory):
    """Groups admitting some finite generating set."""

    def an_object(self):
        r"""The cyclic group of order two, generated by one element."""
        return OwnedGroups().C(2)

    @classmethod
    def _repr_object_names(cls):
        return "finitely generated groups"

    def super_categories(self):
        return [OwnedGroups()]

    class ParentMethods:
        def is_finitely_generated(self):
            return True


class GroupsWithChosenFiniteGeneratingSet(OwnedCategory):
    """Finitely generated groups carrying a chosen finite generating set."""

    def an_object(self):
        r"""The cyclic group of order two, with its chosen generator."""
        return OwnedGroups().C(2)

    def super_categories(self):
        return [OwnedFinitelyGeneratedGroups()]

    class ParentMethods:
        @cached_method
        def group_generators(self):
            return _unique_nonidentity_generators(self)

        def number_of_group_generators(self):
            return ZZ(self.group_generators().cardinality())

        def conjugation_morphism(self):
            automorphisms = self.Aut()
            model = _gap_model(self)
            images = {generator: automorphisms(libgap.ConjugatorAutomorphism(model, _element_to_engine(self, generator))) for generator in self.group_generators()}
            return self.Mor(automorphisms)(images)


class GroupsWithChosenFreeBasis(OwnedCategory):
    """Free groups carrying the chosen set they are free on."""

    def super_categories(self):
        return [OwnedGroups()]

    class ParentMethods:
        def free_basis(self):
            r"""Return the set ``S`` this group is the free group on."""
            return _free_basis(self)

        def free_generator(self, index):
            r"""Return the free generator indexed by a point of the free basis."""
            return _free_generator(self, index)

        def reduced_word(self, element):
            r"""Return the reduced word of ``element`` as ``(index, sign)`` pairs."""
            return _reduced_word(self, element)


class PermutationGroups(OwnedCategory):
    """Groups carrying a chosen faithful action on a finite set of points.

    A data subcategory: the natural action on the points is the chosen datum,
    and the methods below consume it.  Elements act on the left, so
    ``(g h)(x) = g(h(x))``.
    """

    def an_object(self):
        r"""The symmetric group on two points."""
        return OwnedGroups().S(2)

    @classmethod
    def _repr_object_names(cls):
        return "permutation groups"

    def super_categories(self):
        return [OwnedGroups()]

    class ParentMethods:
        def natural_points(self):
            r"""The finite set the group permutes."""
            engine = _engine_group(self)
            return finite_ordered_set(tuple(_owned_point(engine, point) for point in engine.domain()))

        def action_on(self, points):
            r"""The ``G``-set on ``points`` with the natural action ``g . x = g(x)``."""
            from dzack_research.preamble.categories.group.g_sets import finite_g_set

            return finite_g_set(points, self, lambda group_element, point: group_element(point))

        def natural_g_set(self):
            r"""The natural ``G``-set on the points the group permutes."""
            return self.action_on(self.natural_points())

        def orbit(self, point):
            r"""The orbit ``G . point`` of the natural action."""
            engine = _engine_group(self)
            return finite_ordered_set(tuple(_owned_point(engine, image) for image in engine.orbit(_engine_point(engine, point))))

        def orbits(self, points=None):
            r"""The orbit set of the natural action on ``points`` (all natural points by default)."""
            g_set = self.natural_g_set() if points is None else self.action_on(points)
            return g_set.orbits()

        def stabilizer(self, point):
            r"""The subgroup ``G_x`` fixing ``point``, computed by the permutation engine."""
            engine = _engine_group(self)
            engine_point = _engine_point(engine, point)
            return _subgroup_from_gap(
                self,
                libgap.Stabilizer(_gap_model(self), libgap(engine_point), libgap.OnPoints),
            )

        def is_transitive(self) -> bool:
            r"""Whether the natural action has one orbit."""
            return bool(_engine_group(self).is_transitive())


class OwnedFinitelyPresentedGroups(OwnedCategory):
    """Finitely presented groups, as a property of the group."""

    def an_object(self):
        r"""The cyclic group of order two."""
        return OwnedGroups().C(2)

    @classmethod
    def _repr_object_names(cls):
        return "finitely presented groups"

    def super_categories(self):
        return [OwnedFinitelyGeneratedGroups()]

    class ParentMethods:
        def is_finitely_presented(self):
            return True


class GroupsWithChosenFinitePresentation(OwnedCategory):
    """Groups carrying a chosen finite presentation."""

    def an_object(self):
        r"""The cyclic group of order two, with its chosen presentation."""
        return OwnedGroups().C(2)

    def super_categories(self):
        return [OwnedFinitelyPresentedGroups(), GroupsWithChosenFiniteGeneratingSet()]

    class ParentMethods:
        def presenting_free_group(self):
            free, _ = _presentation_of(self)
            return free

        @cached_method
        def defining_relations(self):
            r"""The chosen relators, as elements of the presenting free group."""
            free, relations = _presentation_of(self)
            return finite_ordered_set(tuple(free._from_engine(relation) for relation in relations))

        def quotient_by_relators(self, relators):
            r"""Return ``G / <<relators>>``, the quotient by the normal closure of ``relators``."""
            return _engine_quotient_by_relators(self, relators)


class _AbelianEndomorphismElement(RingElement):
    """Storage for one endomorphism; the operations live on its category."""

    def __init__(self, parent, mapping):
        self._mapping = mapping
        RingElement.__init__(self, parent)


class AbelianGroupEndomorphismRings(OwnedCategory):
    """Endomorphism rings of abelian groups."""

    def super_categories(self):

        return [OwnedRings()]

    class ElementMethods:
        def __call__(self, element):
            return self._mapping(element)

        def _add_(self, other):
            return self.parent()(lambda element: self.parent()._sum_values(self(element), other(element)))

        def _neg_(self):
            return self.parent()(lambda element: self.parent()._negative_value(self(element)))

        def _mul_(self, other):
            return self.parent()(lambda element: self(other(element)))

    class ParentMethods:
        def domain(self):
            return self._group

        def codomain(self):
            return self._group

        def _sum_values(self, left, right):
            return left + right if self._additive else left * right

        def _negative_value(self, value):
            return -value if self._additive else value**-1

        def _identity_value(self):
            return self._group.zero() if self._additive else self._group.one()

        def _element_constructor_(self, mapping):
            return self.element_class(self, mapping)

        def one(self):
            return self(lambda element: element)

        def zero(self):
            return self(lambda element: self._identity_value())

        def _repr_(self):
            return f"Endomorphism ring of {self._group}"


class _AbelianEndomorphismRingParent(Parent):
    Element = _AbelianEndomorphismElement

    def __call__(self, mapping):
        r"""Construct an endomorphism without Sage coercion discovery."""
        return self._element_constructor_(mapping)

    def __init__(self, group):
        self._group = group
        self._additive = group.category().is_subcategory(AdditiveGroups().AdditiveCommutative())
        Parent.__init__(self, category=AbelianGroupEndomorphismRings())
        realize_owned_category(self)

    def is_commutative(self):
        r"""``End(A)`` commutes when ``A`` is cyclic; a group on one generator is, and otherwise this is not decided here."""
        generators = self._group.group_generators().cardinality()
        if generators.is_finite() and int(generators.finite_value()) <= 1:
            return True
        return Unknown


class Subgroups(OwnedParameterizedCategory):
    r"""Groups represented as a specified subgroup of one ambient owned group."""

    @staticmethod
    def __classcall__(cls, supergroup):
        return OwnedParameterizedCategory.__classcall__(cls, _owned_group(supergroup))

    def parameter_category(self):
        r"""A subgroup is a subgroup of one group, so the parameter is a group."""
        return OwnedGroups()

    def an_object(self):
        r"""The trivial subgroup, generated by nothing."""
        return self.supergroup().subgroup(())

    def supergroup(self):
        return self.base()

    def super_categories(self):
        return [OwnedGroups()]

    @classmethod
    def _repr_object_names(cls):
        return "subgroups"

    class ParentMethods:
        def __init__(self, supergroup, **rest) -> None:
            self._preamble_supergroup = supergroup
            super().__init__(facade=supergroup, **rest)

        def supergroup(self):
            return self._preamble_supergroup

        def inclusion(self):
            return _canonical_subgroup_inclusion(self)


def coxeter_presentation(coxeter_matrix, names=None):
    from sage.groups.free_group import FreeGroup

    indices = tuple(coxeter_matrix.index_set())
    free = FreeGroup(len(indices) if names is None else names)
    generators = free.gens()
    relations = [generator**2 for generator in generators]
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            bond = coxeter_matrix[indices[i], indices[j]]
            if bond is infinity or bond == -1:
                continue
            relations.append((generators[i] * generators[j]) ** ZZ(bond))
    return free, tuple(relations)


Groups = groups = OwnedGroups
FinitelyGeneratedGroups = OwnedFinitelyGeneratedGroups
FinitelyPresentedGroups = OwnedFinitelyPresentedGroups


def FiniteGroups():
    r"""The category of finite groups."""
    return OwnedGroups().Finite()


def InfiniteGroups():
    r"""The category of infinite groups."""
    return OwnedGroups().Infinite()


def AbelianGroups():
    r"""The category of abelian groups."""
    return OwnedGroups().Commutative()


def FiniteAbelianGroups():
    r"""The category of finite abelian groups.

    One category cut out by two axioms, not a third class beside them.
    """
    return OwnedGroups().Commutative().Finite()


OwnedFiniteGroups = FiniteGroups
OwnedInfiniteGroups = InfiniteGroups
OwnedAbelianGroups = AbelianGroups
OwnedFiniteAbelianGroups = FiniteAbelianGroups
