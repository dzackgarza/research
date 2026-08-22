r"""The owned scalar hierarchy, and what \(R^n\) means.

``^`` is exponentiation.  The preparser lowers it to ``**``, and CPython
re-parses, so the notation carries no meaning of its own: what ``R**n``
*builds* is decided at runtime by the ring.  Sage says as much in
``Parent.__pow__``, which redirects to the category precisely because a Cython
parent does not inherit its category's ``ParentMethods`` -- and then ships no
node that answers with anything but a native free module.

The hierarchy is the answer, not a single node.  A category parented only at
Sage's ``Rings()`` loses ``ZZ``'s linearization to ``EuclideanDomains``, which
inherits Sage's own ``__pow__`` and wins; the owned intermediate nodes are
what put this chain ahead of it.  So the shape is the mathematics: a semiring
is a multiplicative monoid over an additively commutative monoid, a rng is a
multiplicative semigroup over an additively commutative group, a ring is their
unital join, and division rings and fields refine it.  ``__pow__`` is declared
once, on ``Rings``, and everything below inherits it.

Sage's own node of each name is a super category of the owned one, so a ring
in this hierarchy is a ring in Sage's terms and every Sage algorithm still
recognizes it.  The multiplicative and additive roots are the owned ones in
``group/magmas.sage``, which is the spine that carries a ring to the owned
``Sets()``.  A ring is built as a set before it is built as a ring, so this
edge is what makes the construction chain reach the root: without it
``OwnedRings().parent_class`` inherits no ``Parent`` and nothing can be
constructed in the category at all.
"""

from dzack_research.preamble.refine import refine
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.categories.sets.owned_sets import Sets as OwnedSets
from collections.abc import Callable, Iterator
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Protocol
    from sage.structure.parent import ElementConstructorInput, MembershipInput

    class BaseRingParent(Protocol):
        r"""What this mixin's parents have from ``CategoryObject``: ``base()``
        returns what ``Parent.__init__`` was handed."""

        def base(self) -> "Ring": ...

    from dzack_research.preamble.categories.sets.cardinals import Cardinal
    from dzack_research.preamble.lexicon import Element
    from sage.rings.integer import Integer
    from sage.categories.groups import Group
    from sage.categories.modules import Module
    from dzack_research.preamble.lexicon import OrderedSet

if TYPE_CHECKING:
    from sage.rings.ring import Ring

from sage.misc.cachefunc import cached_method
from dzack_research.preamble.owned_category_bases import Category
from dzack_research.preamble.owned_category_bases import Category_over_base_ring
from dzack_research.preamble.categories.group.magmas import (
    AdditiveGroups as OwnedAdditiveGroups,
    AdditiveMonoids as OwnedAdditiveMonoids,
    Monoids as OwnedMonoids,
    Semigroups as OwnedSemigroups,
)
from sage.categories.division_rings import DivisionRings as SageDivisionRings
from sage.categories.fields import Fields as SageFields
from sage.categories.rings import Rings as SageRings
from sage.categories.rngs import Rngs as SageRngs
from sage.categories.semirings import Semirings as SageSemirings
from sage.rings.integer import Integer as SageInteger
from sage.structure.element import RingElement as SageRingElement
from sage.rings.finite_rings.finite_field_constructor import GF as SageGF
# The engine's own names for the two rings the preamble computes in, bound
# here for every script that loads after this one.  A session binds ``ZZ`` and
# ``QQ`` to the owned view of them, and the preamble shares that namespace, so
# the bare names say what the *session* means.  Where the engine is meant -- a
# matrix to run Smith form on, a ring identity to test -- these say so, and no
# later binding can take them away.
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.unique_representation import UniqueRepresentation
from sage.rings.rational_field import QQ as SageQQ
from dzack_research.preamble.categories.sets.cardinals import Cardinal
from sage.structure.parent import Parent


class OwnedSemirings(Category):
    r"""A multiplicative monoid over an additively commutative monoid."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "semirings"

    def super_categories(self) -> list:
        return [SageSemirings(), OwnedMonoids(), OwnedAdditiveMonoids()]


class OwnedRngs(Category):
    r"""A multiplicative semigroup over an additively commutative group."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "rngs"

    def super_categories(self) -> list:
        return [SageRngs(), OwnedSemigroups(), OwnedAdditiveGroups()]


class OwnedRings(Category):
    r"""Unital rings: the join of the semiring and rng routes."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "rings"

    def super_categories(self) -> list:
        return [SageRings(), OwnedSemirings(), OwnedRngs()]

    class ElementMethods(SageRingElement):
        r"""An element of a ring: where Sage's ring element enters the chain.

        The ring level is where addition acquires a multiplication, so this is
        where ``RingElement`` enters, as ``ModuleElement`` enters at the module
        level and ``Element`` at the set level.  It carries that base and
        nothing else.

        The base is not decoration.  A dynamic class takes its instance layout
        from its first base, and the layout decides which Cython method table
        an instance carries.  Without this the elements of an algebra were laid
        out on ``Element``, and Sage's ``RightModuleAction._act_`` -- which
        casts to ``ModuleElement`` unchecked and calls ``_lmul_`` through that
        table -- jumped through a table that has no such slot.  So \(r\cdot x\)
        segfaulted on every free algebra.
        """

    class ParentMethods(UniqueRepresentation):
        def __init__(
            self,
            engine: "Ring | None" = None,
            **rest: "ConstructionData",
        ) -> None:
            """Build a ring parent around Sage's computation parent."""
            if engine is None:
                super().__init__(**rest)
                return
            self._engine = engine
            super().__init__(facade=engine, **rest)

        def engine(self: "Ring") -> "Ring":
            return self._engine

        def _repr_(self: "Ring") -> str:
            return repr(self._engine)

        def cardinality(self: "Ring") -> "Cardinal":
            return self._cardinality

        def __iter__(self: "Ring") -> "Iterator[Element]":
            return iter(self._engine)

        def gen(self: "Ring", index: "Integer" = 0) -> "Element":
            return self._engine.gen(index)

        def gens(self: "Ring") -> "tuple[Element, ...]":
            return tuple(self._engine.gens())

        def _element_constructor_(self: "Ring", value: "Element") -> "Element":
            return self._engine(value)

        def _coerce_map_from_(
            self: "Ring",
            source: "Parent",
        ) -> "Morphism | None":
            r"""Identify the engine parent with this owned view of the ring."""
            engine: "Ring | None" = self.__dict__.get("_engine")
            if engine is None:
                from sage.categories.unital_algebras import UnitalAlgebras

                return UnitalAlgebras.ParentMethods._coerce_map_from_(self, source)
            if source is not engine:
                return None

            from sage.categories.homset import Hom
            from sage.categories.morphism import SetMorphism

            return SetMorphism(
                Hom(source, self, SageRings()),
                lambda element: element,
            )

        def __getitem__(self: "Ring", names: "OrderedSet | str | int") -> "Parent":
            r"""Return \(R[x_s:s\in S]\), the free \(R\)-algebra on the names.

            On the category, not on the concrete ring class.  Subscript has a
            second meaning here -- the countable-sets node reads it as the
            position in a chosen enumeration -- and a countable ring answers to
            both; the category methods precede the concrete class, so a
            statement written on the class loses, and $\Q[x]$ became the
            zeroth rational.  Ring vocabulary belongs to the ring node, which
            is what makes the subscript of a ring its algebra.
            """
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.algebras.framed_free_algebras import polynomial_ring

            algebra: "Parent" = polynomial_ring(self, names)
            return algebra

        def _ring_morphism_defining_algebra_structure(self: "Ring") -> "Morphism":
            r"""Return $R\to Z(R)$, the identity.

            A ring is an algebra over itself, and this is the whole content of
            saying so.  It is also the base case the other constructions
            reduce to.
            """
            from sage.categories.commutative_rings import CommutativeRings
            from sage.categories.homset import Hom
            from sage.categories.morphism import SetMorphism
            from sage.categories.rings import Rings

            # The identity is a map into the centre only when the centre is
            # the whole ring.  A noncommutative $R$ is not an algebra over
            # itself in this sense, and saying so here is what keeps the
            # base case honest now that $Z(R)$ answers for more rings.
            assert self in CommutativeRings(), (
                f"{self} is not commutative, so the identity does not land in "
                f"its centre and {self} is not an algebra over itself"
            )
            centre = self.ring_center()
            return SetMorphism(Hom(self, centre, Rings()), lambda scalar: scalar)

        def is_central(self: "Ring", element: "Element") -> bool:
            r"""Return whether ``element`` commutes with every element of \(R\).

            Deciding this needs nothing but a generating set.  The
            centralizer of an element is a subring, so an element that
            commutes with a set commutes with everything that set generates:
            checking the generators decides all of \(R\).

            A commutative ring has nothing to check.  For an \(R\)-algebra
            the generators to check are the algebra generators, and the
            scalars need no checking -- an \(R\)-algebra *is* a ring map
            \(R\to Z(A)\), so its image is central by the obligation that
            makes it an algebra, and the algebra generators together with the
            scalars generate the ring.

            A ring that can name no finite generating set is refused rather
            than answered on trust.
            """
            from sage.categories.commutative_rings import CommutativeRings

            # Local: the algebra node reaches this one, so a module-level
            # import would close that cycle; it is built by call time.
            from dzack_research.preamble.categories.algebras.algebras import finite_algebra_generators

            if self in CommutativeRings():
                return True
            return all(
                element * generator == generator * element
                for generator in finite_algebra_generators(self)
            )

        @cached_method
        def ring_center(self: "Ring") -> "Ring":
            r"""Return $Z(R)$, the elements commuting with everything.

            A commutative ring is its own centre, and that is the case this
            preamble is built on: an $R$-algebra is a ring $A$ with a morphism
            $R\to Z(A)$, and the morphism is what an algebra *is*.

            Otherwise the centre is the carve-out by :meth:`is_central` and
            not a presentation of it.  Constructing $Z(\Lambda(M))$ means
            proving $\Lambda^{\text{even}}\oplus\Lambda^{\text{top}}$, while
            *deciding* $z\in Z(\Lambda(M))$ is a finite check against the
            generators -- and deciding is what every use of the centre needs.

            Cached, because $Z$ is a functor and a functor must be well
            defined on objects: two carve-outs of one ring would be two
            objects with no map between them.
            """
            from sage.categories.commutative_rings import CommutativeRings

            # Local: the carve-out imports this node, so a module-level
            # import would close that cycle; it is built by call time.
            from dzack_research.preamble.categories.rings.predicate_subrings import predicate_subring

            if self in CommutativeRings():
                return self
            return predicate_subring(
                self,
                self.is_central,
                "z commutes with every element",
                # Always commutative: two central elements commute with
                # everything, so in particular with each other.
                CommutativeRings(),
            )

        def __pow__(self: "Ring", exponent: "Integer | Cardinal") -> "Module":
            r"""Return \(R^n\), the free \(R\)-module on the canonical framing.

            EXAMPLES::

                sage: (ZZ^3).number_of_module_generators()
                3
            """
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule

            if isinstance(exponent, Cardinal):
                # The rank of a free module *is* a cardinal, and the modules
                # here answer their rank with one -- so a rank read off one
                # module and used to build another arrives in that form.
                assert exponent.is_finite(), (
                    "a free module on infinitely many generators is built from "
                    "its generating set, not from a cardinal"
                )
                exponent = exponent.finite_value()
            assert isinstance(exponent, (int, SageInteger)), (
                f"a free module has a cardinality as rank, got {exponent!r}"
            )
            assert exponent >= 0, "a rank is a nonnegative cardinality"
            return BasedFreeModule(self, exponent)




class OwnedDivisionRings(Category):
    r"""Rings in which every nonzero element is a unit."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "division rings"

    def super_categories(self) -> list:
        return [SageDivisionRings(), OwnedRings()]


class OwnedFields(Category):
    r"""Commutative division rings."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "fields"

    def super_categories(self) -> list:
        return [SageFields(), OwnedDivisionRings()]

    class ParentMethods:
        @cached_method
        def absolute_galois_group(self) -> "Group":
            r"""Return \(G_K=\operatorname{Gal}(\bar K/K)\).

            Sited here because this is the node the preamble owns.  It stood
            on Sage's own ``Fields().ParentMethods`` as an assignment made
            when the preamble installed itself -- which is after Sage has
            built and cached every ``parent_class`` that would have inherited
            it, so no field ever answered.  A category the preamble declares
            has its methods hoisted by ``refine`` at the moment an object
            joins it, and the owned rings join at construction.
            """
            # Local: a module-level import would close a cycle; the module is built by the time this runs.
            from dzack_research.preamble.categories.group.profinite.absolute_galois_groups import absolute_galois_group_factory

            return absolute_galois_group_factory(self)

# Most specific first: a ring joins the hierarchy at the node it actually
# belongs to, so ``QQ`` arrives as a field rather than as a ring that happens
# to have inverses.
_PLACEMENTS = (
    (SageFields(), OwnedFields),
    (SageDivisionRings(), OwnedDivisionRings),
    (SageRings(), OwnedRings),
)


def _owning[**P](
    constructor: "Callable[P, Ring]",
) -> "Callable[P, Parent]":
    r"""Return ``constructor``, placing the ring it builds in the owned graph."""

    def build(*arguments: "P.args", **keywords: "P.kwargs") -> Parent:
        return own_ring(constructor(*arguments, **keywords))

    build.__name__ = getattr(constructor, "__name__", "constructor")
    build.__doc__ = constructor.__doc__
    return build


class OwnedCategoryOverBaseRing(Category_over_base_ring):
    r"""A category over a base ring, named as the objects in it name theirs.

    A ring and the owned view of it are one ring, so they name one category.
    Which of the two names it is cannot be chosen freely: Sage decides
    membership in a category over a base ring by
    ``x.base_ring() is self.base_ring()`` -- identity, in
    ``Category_over_base_ring.__contains__`` -- so a category whose base is
    spelled differently from the way its objects spell theirs has no members
    at all.  The objects answer with the owned view, so this does too.
    """

    @staticmethod
    def __classcall__(
        cls: type["OwnedCategoryOverBaseRing"],
        base_ring: "Ring",
        *arguments: "ElementConstructorInput",
        **keywords: "ElementConstructorInput",
    ) -> Category:
        over_the_owned_base: Category = Category_over_base_ring.__classcall__(
            cls, owned_ring_view(base_ring), *arguments, **keywords
        )
        return over_the_owned_base


SESSION_RING_NAMES = ("ZZ", "QQ", "RR", "CC", "QQbar", "RDF", "CDF")

# Constructors that both cross to the engine and hand back an owned ring.
# \(M_n(R)\) is a ring the session names, so it answers the session's
# questions -- and it is built over the ring the engine computes in, or its
# matrices would be generic.  Both, in that order.
SESSION_OWNED_ENGINE_CONSTRUCTORS = ("MatrixSpace",)


class PrimeFields(Category):
    r"""\(\mathbb{F}_p\), placed in its mathematical category.

    Being a
    ring here means being a set with ring structure, so this level declares
    where it sits among the owned sets -- \(\mathbb{F}_p\) has \(p\) elements
    for every prime \(p\), which is a fact about the mathematics and not a
    stamp on an object -- and the enumeration below is the witness that level
    asks for.  Nothing here counts anything: the size is *stated*, because
    \(p\) is the datum this object is built from, and running the enumeration
    to rediscover it would be deriving a defining datum from its own witness.
    Sage supplies the arithmetic on the same parent.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "prime fields"

    def super_categories(self) -> list:
        return [OwnedFields(), OwnedSets().Finite()]

def PrimeField(characteristic: SageInteger) -> Parent:
    r"""Return \(\mathbb{F}_p\) in the owned category graph."""
    return object_of(
        PrimeFields(),
        engine=SageGF(characteristic),
        cardinality=characteristic,
    )


def install_rings(namespace: dict) -> dict:
    r"""Put every ring a session can name into the owned hierarchy.

    Three routes, because a ring reaches the preamble three ways and no one
    of them covers the others.  The named rings get their owned view built
    here, ready for the session to be handed it.  A ring the preamble builds
    a module over is owned on intake.  A ring the session constructs --
    ``GF(11)``, ``QQ['t']`` -- is owned by its constructor, because
    ``GF(11)^3`` is the *first* thing that happens to it and there is nothing
    earlier to intercept: Sage's ring classes are immutable extension types,
    so a construction hook on the class does not exist.

    ``ZZ['x','y']`` reaches ``PolynomialRing`` through ``__getitem__``, which
    Python looks up on the type -- Sage's own categories never see it, and
    ``Parent.__pow__`` works only because Sage wrote that redirect by hand.
    Override-refine is what makes it reachable anyway: it builds the parent's
    type out of the owned ``ParentMethods``, so ``OwnedRings`` states the
    subscript and a session that names an owned ring gets it.  Stating it on
    The ring node must precede the countable-sets node, which otherwise reads
    a subscript as an enumeration position.
    """
    # Local: a module-level import would close a cycle; the module is built by the time this runs.
    from dzack_research.preamble.categories.algebras.framed_free_algebras import polynomial_ring

    # The owned rings are *not* bound here.  This namespace is the preamble's
    # own, and it is still loading: a script that has not run yet will write
    # ``matrix(ZZ, ...)`` at load time and must get the engine's matrix.  The
    # session's names are bound once everything is built, by
    # :func:`install_session_rings`; the views themselves were made when this
    # file loaded, before anything could be built over one.
    #
    # A polynomial ring is delivered as what it is: the free commutative
    # algebra on its variables.  Sage's own polynomial rings stay behind the
    # boundary, where the algorithms run; a notebook never receives one.
    installed = {"PolynomialRing": polynomial_ring}
    namespace["PolynomialRing"] = polynomial_ring
    # ``RR`` and ``CC`` are session names already, bound to the owned view by
    # :func:`install_session_rings`.  A constructor that spells the same ring
    # has to answer with the same object, or the session holds two names for
    # one ring and ``CC is ComplexField()`` stops being true.
    #
    # Every name, and not one per constructor: ``GF``, ``Zmod`` and
    # ``Integers`` are aliases -- the same factory object under three
    # spellings -- and a session names the ring with whichever it writes.  A
    # spelling left out here hands back the engine's ring, so \(R[G]\) built
    # over ``Integers(6)`` and \(R[G]\) built over ``Zmod(6)`` sit over two
    # different objects and neither is the other's base ring.
    for name in (
        "GF",
        "FiniteField",
        "Zmod",
        "IntegerModRing",
        "Integers",
        "Zp",
        "Qp",
        "RealField",
        "ComplexField",
        "QuadraticField",
    ):
        constructor = namespace.get(name)
        if constructor is not None:
            namespace[name] = _owning(constructor)
            installed[name] = namespace[name]
    # What a session must receive to keep naming these rings.  A constructor
    # wrapped here lives in the scope it was installed into and in no module,
    # so a caller that copies the preamble's module contents would miss it and
    # silently hold Sage's ``GF`` again.
    return installed


def _owned_ring_category(engine: "Ring") -> "Category":
    r"""Return the engine's own category, joined with the owned node.

    Everything the engine *is* -- commutative, euclidean, a unique
    factorisation domain -- is true of this ring too, since it is the same
    ring. Dropping the engine's category would make \(\ZZ\) stop
    being a commutative ring, which every Sage construction over it checks.

    The size of the underlying set is settled here as well, because it is a
    fact about the engine and the object is built in the category this
    returns.
    """
    category = engine.category()
    placement = OwnedRings()
    for sage_category, owned_category in _PLACEMENTS:
        if category.is_subcategory(sage_category):
            placement = owned_category()
            break
    return Category.join(
        (OwnedRings(), OwnedSets(), category, placement, _owned_ring_size(engine))
    )


def _owned_ring_size(engine: "Ring") -> "Category":
    r"""Return where \(R\) sits among the owned sets by its size.

    \(|R|\), which the engine cannot state: Sage's axioms record finiteness
    alone, so \(\mathbb R\) and \(\mathbb Z\) both arrive *infinite* and both
    answer \(+\infty\) -- the one distinction the owned cardinals exist to
    keep.

    An inexact ring is Sage's own word for a ring whose elements are
    approximations to those of a completion (\(\mathbb R\), \(\mathbb C\),
    \(\mathbb Q_p\), a power series ring), and every such completion is of the
    continuum: a point is an infinite sequence of digits and every sequence is
    a point.  Uncountability of the reals is Mathlib's
    ``Cardinal.not_countable_real``.  Inexactness is used here only as that
    statement about completions, never as a cardinality criterion in itself.

    Countability is per-engine, never ``exact => countable``: SR is exact with
    continuum cardinality.  The engines the session catalogue names whose
    countability is a theorem: \(\mathbb Z\), \(\mathbb Q\), every number
    field (finite over \(\mathbb Q\)), and \(\overline{\mathbb Q}\).
    """
    from sage.categories.number_fields import NumberFields
    from sage.rings.qqbar import QQbar as SageQQbar

    if not engine.is_exact():
        return OwnedSets().Uncountable()
    countable_engine = (
        engine is SageZZ
        or engine is SageQQ
        or engine in NumberFields()
        or engine is SageQQbar
    )
    if countable_engine:
        return OwnedSets().Countable().Infinite()
    return OwnedSets()


def engine_ring(ring: "Ring") -> "Ring":
    r"""Return the ring Sage's algorithms compute in.

    The owned parent stores Sage's computation parent as construction data.
    Algorithms cross back to that parent at this boundary.
    """
    if ring in OwnedRings():
        return ring.engine()
    return ring


def install_session_rings(scope: dict) -> None:
    r"""Bind the session's ``ZZ``, ``QQ``, ... to the rings it names.

    A session says \(\ZZ\) and means the ring, so ``ZZ^3`` is the free module
    the preamble builds and ``ZZ['x']`` the free algebra.  The engine's
    \(\ZZ\) answers both in Sage's own terms, and it must keep doing so:
    Sage's algorithms hold that object.  So the name moves and the object
    does not.

    Last, and only last.  ``load()`` of any further script re-imports Sage's
    namespace into this same scope and rebinds these names to the engine
    behind the session's back, so a notebook would find ``ZZ^3`` meaning one
    thing before that line and another after it.  So every scope that loads
    more preamble scripts calls this again once it has finished loading, and
    calling it twice is calling it once.
    """
    for name in SESSION_RING_NAMES:
        engine = scope.get(name)
        if isinstance(engine, Parent) and engine in SageRings():
            scope[name] = own_ring(engine)
    for name in SESSION_OWNED_ENGINE_CONSTRUCTORS:
        constructor = scope.get(name)
        if constructor is not None:
            scope[name] = _owning(constructor)


# The owned rings, under names that cannot be mistaken for the engine's.
#
# ``ZZ`` in a preamble file is Sage's ring: the modules import it as
# ``SageZZ`` and build over it, while a session's ``ZZ`` is the owned view
# that ``install_session_rings`` binds.  The two print alike, so a file that
# reached for the wrong one read correctly and produced a second object --
# two free modules on one $(R,S)$, whose elements then refuse to coerce.
#
# Spelling the owned ones as the mathematics writes them makes the choice
# visible: $\ZZ$ is the ring, ``SageZZ`` is the engine's object, and no line
# can mean both.


def owned_ring_named(name: str) -> Parent:
    r"""Return the owned view of the engine ring bound to ``name``."""
    from sage.all import __dict__ as _sage_all
    engine = _sage_all[name]
    return own_ring(engine)


def own_ring(ring: "Ring") -> Parent:
    r"""Place ``ring`` in the owned category graph and return it."""
    if ring in OwnedRings():
        return ring
    from dzack_research.preamble.categories.sets.cardinals import cardinal, continuum
    from sage.rings.infinity import Infinity

    count = continuum if not ring.is_exact() else ring.cardinality()
    assert count != Infinity or _owned_ring_size(ring).is_subcategory(
        OwnedSets().Countable()
    ), f"{ring} has no determined cardinality"
    return object_of(
        _owned_ring_category(ring),
        engine=ring,
        cardinality=cardinal(count),
    )


def owned_ring_view(ring: "Ring") -> "Ring":
    r"""Return the owned parent used as the session-facing ring."""
    if ring in OwnedRings():
        return ring
    return own_ring(ring)

class OwnedBaseRing:
    r"""Answers ``base_ring`` with the ring the object was built with.

    Built with, in the word the session used.  Sage's ``base_ring`` reports
    what ``Parent.__init__`` was handed, which is the engine's ring, because
    that is what the coercion system and every algorithm must see.  A session
    that wrote \(\ZZ^3\) asked about *its* \(\ZZ\), and the two are one ring,
    so this reports the name it used and leaves the computation alone.

    Read off ``base()`` and not off ``super().base_ring()``: Sage supplies
    ``base_ring`` from the *category*, so the inherited call goes through
    ``getattr_from_category`` and raises ``AttributeError`` while the parent
    is still being constructed.  ``Category.__contains__`` catches that and
    answers ``False``, which turns a mid-construction membership check into a
    silent denial.  ``base()`` is a real method on ``CategoryObject`` and
    returns exactly what ``Parent.__init__`` was handed.
    """

    def base_ring(self: "BaseRingParent") -> "Ring":
        return owned_ring_view(self.base())


# The owned view of each named ring is made now, as this file loads, and not
# when a session asks for one.  Everything after this point -- every category
# over a base ring, every module built over one -- names its base through
# :func:`owned_ring_view`, and that answer has to be the same at the first
# construction and the last.  A view made later would put the objects built
# before it in one category and the objects built after it in another.
#
# The rings are read off ``sage.all`` and not off this module's globals: this
# file is imported, so its globals hold what it imports and not the session
# names.  ``sage.all`` is where a session's ``ZZ`` comes from, so the object
# owned here is the object :func:`install_session_rings` will later rebind.
import sage.all as _sage_all

for _session_ring_name in SESSION_RING_NAMES:
    _session_ring = getattr(_sage_all, _session_ring_name, None)
    if isinstance(_session_ring, Parent) and _session_ring in SageRings():
        own_ring(_session_ring)


# The owned rings, in code, under names nothing else in scope can supply.
#
# The point is a hard failure.  If these were spelled ``ZZ``, a file that
# forgot the import would still find a ``ZZ`` -- Sage's, through the preparser
# prelude or a stray import -- and build over the engine's ring silently,
# which is the defect that put two free modules on one $(R,S)$.  Under these
# names a missing import is a ``NameError`` at the first use.
#
# Code only.  Nobody types these at a prompt, and nobody has to: ``init.sage``
# binds the session's ``ZZ`` to this object as its last act.
ℤ = owned_ring_named("ZZ")
ℚ = owned_ring_named("QQ")
ℝ = owned_ring_named("RR")
ℂ = owned_ring_named("CC")
