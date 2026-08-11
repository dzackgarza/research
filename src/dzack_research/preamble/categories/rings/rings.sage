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
recognizes it.  The multiplicative and additive roots are Sage's too: routing
them through a parallel set-forgetting layer makes ``QQ.cardinality()``
recurse, and the elements of a ring do not change when its operations are
forgotten.  Naming the multiplicative and additive roots again would add
nothing -- Sage's own semiring and rng nodes already carry them -- and in the
preamble's shared load namespace it sends Sage's axiom deduction hunting for a
base category class by name, where it finds the preamble's groups node.
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage_lattice_category_spike.lexicon import Element
    from sage_lattice_category_spike.lexicon import Group
    from sage_lattice_category_spike.lexicon import Module
    from sage_lattice_category_spike.lexicon import OrderedSet

if TYPE_CHECKING:
    from sage.rings.ring import Ring

from sage.misc.cachefunc import cached_method
from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.categories.homset import Hom
from sage.categories.morphism import Morphism
from sage.categories.division_rings import DivisionRings as SageDivisionRings
from sage.categories.fields import Fields as SageFields
from sage.categories.rings import Rings as SageRings
from sage.categories.rngs import Rngs as SageRngs
from sage.categories.semirings import Semirings as SageSemirings
from sage.rings.integer import Integer as SageInteger
# The engine's own names for the two rings the preamble computes in, bound
# here for every script that loads after this one.  A session binds ``ZZ`` and
# ``QQ`` to the owned view of them, and the preamble shares that namespace, so
# the bare names say what the *session* means.  Where the engine is meant -- a
# matrix to run Smith form on, a ring identity to test -- these say so, and no
# later binding can take them away.
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage_lattice_category_spike.objects.cardinals import Cardinal
from sage.structure.parent import Parent


class OwnedSemirings(Category):
    r"""A multiplicative monoid over an additively commutative monoid."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "semirings"

    def super_categories(self) -> list:
        return [SageSemirings()]


class OwnedRngs(Category):
    r"""A multiplicative semigroup over an additively commutative group."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "rngs"

    def super_categories(self) -> list:
        return [SageRngs()]


class OwnedRings(Category):
    r"""Unital rings: the join of the semiring and rng routes."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "rings"

    def super_categories(self) -> list:
        return [SageRings(), OwnedSemirings(), OwnedRngs()]

    class ParentMethods:
        def _ring_morphism_defining_algebra_structure(self: "Ring") -> "Morphism":
            r"""Return $R\to Z(R)$, the identity.

            A ring is an algebra over itself, and this is the whole content of
            saying so.  It is also the base case the other constructions
            reduce to.
            """
            from sage.categories.homset import Hom
            from sage.categories.morphism import SetMorphism
            from sage.categories.rings import Rings

            centre = self.ring_center()
            return SetMorphism(Hom(self, centre, Rings()), lambda scalar: scalar)

        def ring_center(self: "Ring") -> "Ring":
            r"""Return $Z(R)$, the elements commuting with everything.

            A commutative ring is its own centre, and that is the case this
            preamble is built on: an $R$-algebra is a ring $A$ with a morphism
            $R\to Z(A)$, and the morphism is what an algebra *is*.  For a
            noncommutative $R$ the centre is a real computation and this
            declines rather than guessing.
            """
            from sage.categories.commutative_rings import CommutativeRings

            assert self in CommutativeRings(), (
                f"{self} is not commutative, so its centre is not itself and "
                "this preamble has no construction for it yet"
            )
            return self

        def __pow__(self, exponent):
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

        def algebra_generators(self) -> tuple:
            r"""Return generators of \(K\) as an algebra over its base.

            Sage's bare ``gens`` on a number field leaves open which
            structure is meant -- \(K\) as a \(\QQ\)-module has a basis of
            degree many elements, \(K\) as a \(\QQ\)-algebra is generated
            by a primitive element.  An automorphism fixes \(K\) pointwise
            exactly when it fixes the algebra generators, since fixing them
            fixes everything they generate, so that is the word for it.
            """
            return tuple(self.gens())


# Most specific first: a ring joins the hierarchy at the node it actually
# belongs to, so ``QQ`` arrives as a field rather than as a ring that happens
# to have inverses.
_PLACEMENTS = (
    (SageFields(), OwnedFields),
    (SageDivisionRings(), OwnedDivisionRings),
    (SageRings(), OwnedRings),
)


def _owning(constructor):
    r"""Return ``constructor``, handing out the owned view of the ring it builds.

    Owned and not refined.  Sage's ring constructors are cached by
    ``UniqueRepresentation``, so refining what one returns rewrites the single
    object Sage's own algorithms hold: a session that names ``GF(5)`` would
    give the preamble's ``R^n`` and ``submodule`` to every finite-field
    computation in the engine, and the p-adic symbols of a genus stop
    computing.  The wrapper leaves the engine's ring alone.
    """

    def build(*arguments, **keywords):
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
    def __classcall__(cls, base_ring, *arguments, **keywords):
        return Category_over_base_ring.__classcall__(
            cls, owned_ring_view(base_ring), *arguments, **keywords
        )


def _over_the_engine(constructor):
    r"""Return ``constructor`` reading an owned ring as the ring it is.

    A session says ``matrix(ZZ, ...)`` and means a matrix of integers.  Sage
    builds one from its own \(\ZZ\) and has fast implementations keyed to it;
    over the owned view it would build a generic matrix instead and lose the
    Smith and Hermite forms that make it worth having.  So the ring argument
    crosses to the engine here, which is where the computation starts.
    """

    if getattr(constructor, "_crosses_to_the_engine", False):
        return constructor

    def build(*arguments, **keywords):
        return constructor(
            *(engine_ring(argument) for argument in arguments), **keywords
        )

    build.__name__ = getattr(constructor, "__name__", "constructor")
    build.__doc__ = constructor.__doc__
    build._crosses_to_the_engine = True
    return build


SESSION_RING_NAMES = ("ZZ", "QQ", "RR", "CC", "QQbar", "RDF", "CDF")

# What a session builds over a ring by naming the ring first.
SESSION_ENGINE_CONSTRUCTORS = (
    "matrix",
    "vector",
    "column_matrix",
    "diagonal_matrix",
    "identity_matrix",
    "zero_matrix",
    "block_diagonal_matrix",
    "FreeModule",
)

# Constructors that both cross to the engine and hand back an owned ring.
# \(M_n(R)\) is a ring the session names, so it answers the session's
# questions -- and it is built over the ring the engine computes in, or its
# matrices would be generic.  Both, in that order.
SESSION_OWNED_ENGINE_CONSTRUCTORS = ("MatrixSpace",)


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
    Python looks up on the type and never on the category -- ``Parent.__pow__``
    works only because Sage wrote that redirect by hand, and no such redirect
    exists for subscripting.  ``OwnedRing`` is the preamble's own type, so the
    subscript of an owned ring is answered here; a session names owned rings,
    so that is the route it takes.
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


class OwnedRing(Parent):
    r"""The ring a Sage ring presents, as an owned object.

    Constructed around the Sage ring rather than refining it, for the reason
    the owned groups give: refinement rewrites an object this preamble did not
    build, and here it rewrites one Sage's *own algorithms* hold.  A refined
    \(\ZZ\) answers \(\ZZ^n\) with a preamble module inside Sage's real-root
    isolator, which wants a mutable coordinate buffer; wrapping leaves the
    engine's \(\ZZ\) alone and gives the notebook its own.

    The elements are the engine's.  A ring's underlying set does not change by
    being placed, and the arithmetic that makes it a ring is the one the
    engine already computes.

    The engine crosses the boundary once, here, and is private afterwards.
    """

    def __init__(self, engine: "Ring") -> None:
        assert engine in SageRings(), f"{engine} is not a ring"
        self._engine = engine
        # A facade: the elements are the engine's own.  A ring's underlying
        # set does not change by being placed, and an element parented here
        # instead would lose every coercion Sage knows for the engine's --
        # a rational matrix divided by one would have no common parent.
        Parent.__init__(
            self,
            facade=engine,
            category=_owned_ring_category(engine),
        )

    def _coerce_map_from_(self, other: "Parent") -> bool:
        r"""Return whether ``other`` coerces here, which is the engine's answer.

        ``other`` crosses to the engine to be asked.  A session names owned
        rings on both sides -- \(\ZZ\to\QQ\) is asked of two of them -- and the
        engine knows the map between the rings they are, while it has never
        heard of the wrappers.
        """
        if other is self or other is self._engine:
            return True
        return bool(self._engine.has_coerce_map_from(engine_ring(other)))

    def coerce_map_from(self, other: "Parent") -> "Morphism":
        r"""Return the coercion \(S\to R\), named between the rings it joins.

        Answered here rather than by Sage, and this is the whole of the
        crossing.  Sage decides a coercion by asking the codomain and then
        *composing* whatever it finds, and the composite is built through
        ``Hom`` with an explicit category -- whose membership, for
        ``NumberFields`` among others, is an ``isinstance`` test that no
        facade passes however sound the mathematics.  So both ends cross to
        the engine before Sage is asked anything, and the engine's answer is
        renamed on the way out.
        """
        crossed = engine_ring(other)
        engine_map = self._engine.coerce_map_from(crossed)
        if engine_map is None:
            return None
        if not isinstance(crossed, Parent):
            # Sage asks this of Python types too -- ``int`` coerces into every
            # ring.  A type is not a ring a session named, so it has no owned
            # view and there are no two ends to rename.
            return engine_map
        return OwnedRingMap(engine_map, owned_ring_view(crossed), self)

    def has_coerce_map_from(self, other: "Parent") -> bool:
        return bool(self._engine.has_coerce_map_from(engine_ring(other)))

    def _element_constructor_(self, value: "Element") -> "Element":
        return self._engine(value)

    def __contains__(self, value: object) -> bool:
        return value in self._engine

    def __pow__(self, exponent: "Integer") -> "Module":
        r"""Return \(R^n\), the free \(R\)-module on the canonical framing."""
        return OwnedRings.ParentMethods.__pow__(self, exponent)

    def __getitem__(self, names: "OrderedSet | str | int") -> "Parent":
        r"""Return \(R[x_s:s\in S]\), the free \(R\)-algebra on the names.

        Sage's rings cannot answer this in the preamble's terms: a dunder is
        looked up on the type, their types are extension types, and the
        category never sees the call.  This class is the preamble's own, so
        the subscript means here what the preamble says it means.
        """
        # Local: a module-level import would close a cycle; the module is built by the time this runs.
        from dzack_research.preamble.categories.algebras.framed_free_algebras import polynomial_ring

        return polynomial_ring(self, names)

    def __iter__(self):
        r"""Iterate the engine's elements: they are this ring's own.

        Promised by the category, which is the engine's -- \(\ZZ\) is an
        infinite enumerated set, and claiming that while declining to
        enumerate is what a facade must not do.
        """
        return iter(self._engine)

    def some_elements(self) -> tuple:
        r"""Return a few elements, which are the engine's."""
        return tuple(self._engine.some_elements())

    def an_element(self) -> "Element":
        return self._engine.an_element()

    def zero(self) -> "Element":
        return self._engine.zero()

    def one(self) -> "Element":
        return self._engine.one()

    def characteristic(self) -> "Integer":
        return self._engine.characteristic()

    def is_field(self) -> bool:
        return self._engine.is_field()

    def is_integral_domain(self) -> bool:
        return self._engine.is_integral_domain()

    def is_finite(self) -> bool:
        return self._engine.is_finite()

    def cardinality(self) -> "Cardinal":
        return self._engine.cardinality()

    def fraction_field(self) -> "Parent":
        r"""Return \(\operatorname{Frac}(R)\), owned as this ring is."""
        return own_ring(self._engine.fraction_field())

    def _first_ngens(self, count: "Integer") -> tuple:
        r"""Return the first ``count`` generators, for ``K.<a> = ...`` syntax.

        Sage's preparser lowers a generator-naming assignment to this call, so
        a ring a session names that way has to answer it.  The generators are
        the engine's elements, which are this ring's own.
        """
        return self._engine._first_ngens(count)

    def gens(self) -> tuple:
        r"""Return the generators, which are the engine's elements."""
        return tuple(self._engine.gens())

    def gen(self, index: "Integer" = 0) -> "Element":
        return self._engine.gen(index)

    def ring_of_integers(self) -> "Parent":
        r"""Return \(\mathcal O_K\), owned as this ring is."""
        return own_ring(self._engine.ring_of_integers())

    def ideal(self, *generators: object, **keywords: object) -> "Parent":
        r"""Return the ideal generated by ``generators``.

        The engine's object: an ideal is not a ring, so it has no owned view
        of its own, and ``own_ideal`` is the preamble's word for one.
        """
        return self._engine.ideal(*generators, **keywords)

    def embeddings(self, codomain: "Ring") -> list:
        r"""Return the field maps \(R\to\Omega\), which the engine computes.

        Both ends cross: an embedding is a computation, and the engine has
        never heard of either wrapper.
        """
        return self._engine.embeddings(engine_ring(codomain))

    def algebraic_closure(self) -> "Parent":
        r"""Return \(\bar R\), owned as this ring is.

        The engine's answer, because which field \(\bar\QQ\) *is* was never
        the wrapper's to decide.  Delegated rather than inherited: Sage
        supplies a generic ``algebraic_closure`` from the ``Fields`` category
        that declines, and the one that answers lives on the concrete ring
        class this facade does not inherit from.
        """
        return own_ring(self._engine.algebraic_closure())

    def __hash__(self) -> int:
        return hash((type(self), self._engine))

    def __eq__(self, other: object) -> bool:
        r"""Return whether ``other`` is this owned ring.

        Not equal to the engine it views, however tempting: Sage sorts its
        category poset with these as keys, and two base rings that compare
        equal while being distinct objects make that sort inconsistent --
        it says so, and then its caches miss.  Consistency comes from using
        the owned ring everywhere instead, with ``engine_ring`` at the
        crossings.
        """
        return type(other) is type(self) and other._engine == self._engine

    def _repr_(self) -> str:
        return repr(self._engine)


class OwnedRingMap(Morphism):
    r"""The engine's ring map, named between the rings a session names.

    The arithmetic is the engine's -- a coercion is a computation, and this
    changes none of it.  What the wrapper adds is the two ends: a session that
    asked \(\ZZ\to\QQ\) of its own rings is told the answer in those words,
    and ``domain()`` is the ring it named.

    The homset is built without naming a category, which is what keeps this
    safe: ``Hom`` derives one from the two parents and then re-enters itself
    with ``check=False``, so the containment tests that reject a facade are
    never reached.  Naming a category here would walk straight into them.
    """

    def __init__(self, engine_map: "Map", domain: "Ring", codomain: "Ring") -> None:
        self._engine_map = engine_map
        Morphism.__init__(self, Hom(domain, codomain))

    def _call_(self, element: "Element") -> "Element":
        return self._engine_map(element)

    def _repr_type(self) -> str:
        return "Coercion"


def _owned_ring_category(engine: "Ring") -> "Category":
    r"""Return the engine's own category, joined with the owned node.

    Everything the engine *is* -- commutative, euclidean, a unique
    factorisation domain -- is true of this ring too, since it is the same
    ring: the wrapper adds a place in the preamble's hierarchy and takes
    nothing away.  Dropping the engine's category would make \(\ZZ\) stop
    being a commutative ring, which every Sage construction over it checks.
    """
    category = engine.category()
    for sage_category, owned_category in _PLACEMENTS:
        if category.is_subcategory(sage_category):
            return Category.join((category, owned_category()))
    return Category.join((category, OwnedRings()))


def engine_ring(ring: "Ring") -> "Ring":
    r"""Return the ring Sage's algorithms compute in.

    The inverse of :func:`own_ring` at the boundary: a matrix, a vector or a
    Groebner basis is the engine's work, and the engine has fast
    implementations keyed to *its* rings -- a matrix over the wrapper is a
    generic one and loses them.

    So this is what every constructor calls on intake.  The owned ring is the
    session's name for the ring, and it is a name: the objects the preamble
    builds are over the ring the engine holds, and so are the categories they
    belong to.  A module whose base were the wrapper would sit in a category
    over the engine's ring with no member, and its matrices would be generic.
    """
    return ring._engine if isinstance(ring, OwnedRing) else ring


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
    for name in SESSION_ENGINE_CONSTRUCTORS:
        constructor = scope.get(name)
        if constructor is not None:
            scope[name] = _over_the_engine(constructor)
    for name in SESSION_OWNED_ENGINE_CONSTRUCTORS:
        constructor = scope.get(name)
        if constructor is not None:
            scope[name] = _owning(_over_the_engine(constructor))


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


def owned_ring_named(name: str) -> "OwnedRing":
    r"""Return the owned view of the engine ring bound to ``name``."""
    from sage.all import __dict__ as _sage_all
    engine = _sage_all[name]
    return own_ring(engine)


_OWNED_RINGS: dict = {}


def own_ring(ring: "Ring") -> OwnedRing:
    r"""Return the owned ring ``ring`` presents, the same object every time.

    One object per engine: a ring is compared and cached by identity all over
    Sage, and two wrappers of one ring would be two rings with no map between
    them.
    """
    if isinstance(ring, OwnedRing):
        return ring
    owned = _OWNED_RINGS.get(ring)
    if owned is None:
        owned = OwnedRing(ring)
        _OWNED_RINGS[ring] = owned
    return owned


def owned_ring_view(ring: "Ring") -> "Ring":
    r"""Return the session's name for ``ring``, which is ``ring`` unless it has one.

    A lookup and never a construction: only a ring a session has actually
    been handed has an owned view, so this reports the word the session
    used without inventing one for rings it never named.  A ring the
    preamble builds -- a free algebra, say -- is its own name and comes back
    unchanged.

    Promoting every engine ring here instead -- "owned rings, period" -- is
    the stated intent and does not hold yet: it breaks the construction of a
    free algebra over a preamble number field, in Sage's
    ``UnitalAlgebras.__init_extra__`` -> ``_coerce_map_from_base_ring``,
    which runs inside ``Parent.__init__`` before the parent can answer for
    itself.  See the report accompanying this change.
    """
    return _OWNED_RINGS.get(ring, ring)


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

    def base_ring(self) -> "Ring":
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
