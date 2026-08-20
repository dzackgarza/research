r"""The enrichment mechanism: derived bases, and generated forwarding.

Two claims, one per kind of enrichment
(:mod:`dzack_research.preamble.enrichment`).

*Determined* enrichment -- a throwaway three-level chain, set to magma to
group, whose classes name only their own category.  Construction threads by
cooperative ``super().__init__``; the class MRO is the category graph's
linearization, computed independently from the registry; ``refine`` still
finds the concrete base and still puts owned category methods in front of
it; and each level's category method reads the datum its own level's
``__init__`` introduced, with the leaf naming none of them.

*Chosen* enrichment -- a declared forgetful map, and forwarding generated
from the enriched category's own surface, on all three of Sage's method
surfaces.  Proved on the throwaway pair and then on the real ones: the four
module answers a form module relays by hand today, the coefficient reading a
form module *element* relays, and the eleven names a form *morphism* relays
to the module morphism it holds.  Nothing in the tree is edited to prove it
-- the generated relays are composed in front of the levels with their
hand-written bodies removed, and asked the same questions.
"""

from sage.categories.category import Category
from sage.categories.sets_cat import Sets as SageSets
from sage.structure.parent import Parent

from dzack_research.preamble.enrichment import (
    BoundTo,
    declared_surface,
    forgets_to,
    forwarding_mixin,
    realization_of,
    realizes,
)


def _ensure_preamble() -> None:
    if "Lattices" in globals():
        return
    from dzack_research.preamble.install import install_preamble
    install_preamble(globals())
    Lattices.install(globals())


# ---------------------------------------------------------------------------
# The throwaway chain: a set, a set with an operation, a group.
# ---------------------------------------------------------------------------


class ProbeSets(Category):
    r"""A set and nothing more: the root of the chain."""

    def super_categories(self) -> list:
        return [SageSets()]

    class ParentMethods:
        def probe_elements(self: Parent) -> "OrderedSet":
            r"""Return the set, which is the datum the root level introduces."""
            return self._probe_elements

        def probe_smallest(self: Parent) -> "Element":
            r"""Return the first element under the set's own order."""
            return self.probe_elements()[0]

    class ElementMethods:
        def probe_element_label(self: "Element") -> "Element":
            return self._probe_label

    class MorphismMethods:
        def probe_morphism_source(self: "Morphism") -> Parent:
            return self.domain()


class ProbeMagmas(Category):
    r"""A set with a binary operation."""

    def super_categories(self) -> list:
        return [ProbeSets()]

    class ParentMethods:
        def probe_product(self: Parent, left: "Element", right: "Element") -> "Element":
            return self._probe_operation(left, right)


class ProbeGroups(Category):
    r"""A magma with a distinguished neutral element."""

    def super_categories(self) -> list:
        return [ProbeMagmas()]

    class ParentMethods:
        def probe_identity(self: Parent) -> "Element":
            return self._probe_identity


@realizes(ProbeSets)
class ProbeSetParent(BoundTo(ProbeSets), Parent):
    r"""The root class, and the only one naming ``Parent.__init__``.

    Its derived bases are empty -- no super-category of ``ProbeSets`` is
    bound -- so ``super()`` here is Sage's non-cooperative constructor and
    the cooperative chain ends.
    """

    def __init__(
        self,
        probe_elements: "OrderedSet",
        **rest: "ElementConstructorInput",
    ) -> None:
        self._probe_elements = probe_elements
        super().__init__(**rest)

    def cardinality(self) -> "Cardinal":
        r"""Return $|X|$, which is the underlying set's count and no other."""
        return self._probe_elements.cardinality()

    def is_countable(self) -> bool:
        r"""The discriminating wrong answer.

        Owned ``Sets().ParentMethods`` reads countability off the cardinal.
        Override-refine has to put that in front of this, so after a refine
        the true answer is what a caller gets.
        """
        return False


@realizes(ProbeMagmas)
class ProbeMagmaParent(BoundTo(ProbeMagmas)):
    r"""The middle level: it introduces the operation and passes the rest up."""

    def __init__(
        self,
        probe_operation: "Callable",
        **rest: "ElementConstructorInput",
    ) -> None:
        self._probe_operation = probe_operation
        super().__init__(**rest)


@realizes(ProbeGroups)
class ProbeGroupParent(BoundTo(ProbeGroups)):
    r"""The leaf: it introduces the neutral element and knows nothing below."""

    def __init__(
        self,
        probe_identity: "Element",
        **rest: "ElementConstructorInput",
    ) -> None:
        self._probe_identity = probe_identity
        super().__init__(**rest)


def _probe_group() -> ProbeGroupParent:
    r"""Return $\mathbb{Z}/3$ built through the derived chain."""
    _ensure_preamble()
    from dzack_research.preamble.categories.sets.sets import finite_ordered_set
    from sage.rings.finite_rings.integer_mod_ring import Zmod

    residues = Zmod(3)
    return ProbeGroupParent(
        probe_identity=residues(0),
        probe_operation=lambda left, right: left + right,
        probe_elements=finite_ordered_set(tuple(residues)),
        category=ProbeGroups(),
    )


def test_construction_threads_through_the_derived_bases() -> None:
    r"""Every level's datum reaches one object through ``super().__init__``."""
    from sage.rings.finite_rings.integer_mod_ring import Zmod

    residues = Zmod(3)
    group = _probe_group()

    assert group.probe_elements().cardinality() == 3
    assert group.probe_identity() == residues(0)
    # 1 + 2 = 0 in Z/3: the operation the middle level introduced, acting on
    # the elements the root level introduced, around the leaf's identity.
    assert group.probe_product(residues(1), residues(2)) == residues(0)
    assert group.probe_product(group.probe_identity(), residues(2)) == residues(2)


def test_the_class_mro_is_the_category_linearization() -> None:
    r"""The class graph is a function of the category graph, so they cannot drift."""
    chain = (ProbeGroupParent, ProbeMagmaParent, ProbeSetParent)

    in_the_mro = tuple(cls for cls in ProbeGroupParent.__mro__ if cls in chain)
    linearization = tuple(
        realization_of(category)
        for category in ProbeGroups().all_super_categories(proper=False)
        if isinstance(category, (ProbeGroups, ProbeMagmas, ProbeSets))
    )

    assert in_the_mro == chain
    assert linearization == chain


def test_a_leaf_names_no_level_below_its_own() -> None:
    r"""Each level's category method answers at the leaf, unmentioned there."""
    group = _probe_group()

    assert type(group).probe_elements is ProbeSets.ParentMethods.probe_elements
    assert type(group).probe_product is ProbeMagmas.ParentMethods.probe_product
    assert type(group).probe_identity is ProbeGroups.ParentMethods.probe_identity
    assert ProbeGroupParent.__mro__[1] is ProbeMagmaParent


def test_refine_still_owns_a_class_with_derived_bases() -> None:
    r"""Override-refine keeps working over a chain it did not write."""
    from dzack_research.preamble.categories.sets.owned_sets import Sets as OwnedSets
    from dzack_research.preamble.refine import refine

    group = _probe_group()
    assert group.is_countable() is False

    refine(group, OwnedSets())

    assert type(group)._preamble_concrete is ProbeGroupParent
    mro = type(group).__mro__
    concrete_at = mro.index(ProbeGroupParent)
    assert concrete_at > 1
    assert all(
        cls.__module__.startswith("dzack_research.preamble.")
        for cls in mro[1:concrete_at]
    )
    # The derived chain survives the rebuild, so the levels below the leaf
    # are still the ones holding the construction.
    assert mro[concrete_at:concrete_at + 3] == (
        ProbeGroupParent,
        ProbeMagmaParent,
        ProbeSetParent,
    )
    # Owned Sets computes it from the cardinal, and Z/3 is countable.
    assert group.is_countable() is True


# ---------------------------------------------------------------------------
# The throwaway chosen enrichment: a set with a chosen basepoint.
# ---------------------------------------------------------------------------


@forgets_to(ProbeSets, through="forget_probe_marking")
class ProbeMarkedSets(Category):
    r"""Sets with a chosen basepoint.

    Many basepoints sit on one set, so a marked set is a distinct parent
    holding the pair -- and it says so once, above, instead of writing a
    body per name the set level declares.
    """

    def super_categories(self) -> list:
        return [SageSets()]

    class ParentMethods:
        def forget_probe_marking(self: Parent) -> Parent:
            return self._probe_underlying

        def probe_basepoint(self: Parent) -> "Element":
            return self._probe_basepoint

        def probe_smallest(self: Parent) -> "Element":
            r"""Answered here: on a marked set the distinguished element is
            the basepoint, whichever one the underlying order puts first."""
            return self.probe_basepoint()


class ProbeMarkedParent(Parent):
    r"""The pair $(X, x_0)$: a distinct parent over a set it does not own."""

    def __init__(self, underlying: Parent, basepoint: "Element") -> None:
        self._probe_underlying = underlying
        self._probe_basepoint = basepoint
        Parent.__init__(self, category=ProbeMarkedSets())


def test_a_declared_forgetful_map_generates_the_whole_lower_surface() -> None:
    r"""One declaration answers every name the enriched category declares."""
    from sage.rings.finite_rings.integer_mod_ring import Zmod

    residues = Zmod(3)
    group = _probe_group()
    marked = ProbeMarkedParent(group, residues(2))

    surface = declared_surface(ProbeSets(), "parent")
    assert surface == frozenset({"probe_elements", "probe_smallest"})

    declared_by_the_marked_level = vars(ProbeMarkedSets.ParentMethods)
    relayed = declared_by_the_marked_level["probe_elements"]
    assert relayed.__wrapped__ is ProbeSets.ParentMethods.probe_elements

    # The relay answers with the underlying set's own answer ...
    assert marked.probe_elements() is group.probe_elements()
    # ... while the name the marked level answers itself is untouched, and
    # says something different from what the relay would have said.
    assert marked.probe_smallest() == residues(2)
    assert group.probe_smallest() == residues(0)


def test_generation_covers_all_three_surfaces() -> None:
    r"""Elements and morphisms get the same treatment as parents."""
    for surface, attribute in (
        ("parent", "ParentMethods"),
        ("element", "ElementMethods"),
        ("morphism", "MorphismMethods"),
    ):
        declared = declared_surface(ProbeSets(), surface)
        assert declared, f"the probe set level declares nothing on {surface}"
        methods = getattr(ProbeMarkedSets, attribute)
        for name in declared - frozenset({"probe_smallest"}):
            relay = vars(methods)[name]
            assert relay.__wrapped__ is vars(getattr(ProbeSets, attribute))[name]


# ---------------------------------------------------------------------------
# The real pairs.  Nothing here is deleted from the tree; the generated
# relays are put in front of a copy of each level with its hand-written
# bodies removed, and asked the same questions.
# ---------------------------------------------------------------------------


def _without(declarer: type, names: frozenset[str], *bases: type) -> type:
    r"""Return ``declarer``'s body with ``names`` removed, over ``bases``."""
    body = {
        name: value
        for name, value in vars(declarer).items()
        if name not in names and name not in ("__dict__", "__weakref__")
    }
    return type(f"{declarer.__name__}WithoutHandWrittenForwarding", bases, body)


FORM_MODULE_HAND_FORWARDED = frozenset(
    {"cardinality", "rank", "is_torsion", "is_torsion_free"}
)


def test_a_form_module_relays_the_module_answers_without_writing_them() -> None:
    r"""$E_8$ answers the four module questions through generated relays."""
    _ensure_preamble()
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
        FinitelyGeneratedFreeModules,
    )
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
        FormModule,
        FormModules,
    )
    from sage.rings.integer_ring import ZZ

    lattice = Lattices.E8
    enriched = FinitelyGeneratedFreeModules(ZZ)
    assert lattice.forget_form() in enriched

    surface = declared_surface(enriched, "parent")
    assert FORM_MODULE_HAND_FORWARDED <= surface

    relays = forwarding_mixin(enriched, "parent", "forget_form")
    stripped = _without(FormModules.ParentMethods, FORM_MODULE_HAND_FORWARDED)
    without_relays = type("E8WithoutAnyForwarding", (stripped, FormModule), {})
    assert not any(
        hasattr(without_relays, name) for name in FORM_MODULE_HAND_FORWARDED
    )

    resolved = type("E8WithGeneratedForwarding", (relays, stripped, FormModule), {})

    assert resolved.rank is relays.rank
    assert resolved.rank(lattice) == 8
    assert resolved.is_torsion_free(lattice) is True
    assert resolved.is_torsion(lattice) is False
    # $E_8 \cong \mathbb{Z}^8$ as a set: countably infinite.
    assert resolved.cardinality(lattice).is_finite() is False
    assert resolved.cardinality(lattice).is_countable() is True


def test_a_form_module_element_relays_its_coefficients() -> None:
    r"""The one element body that only relays is generated instead."""
    _ensure_preamble()
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
        BasedFreeModuleElement,
    )
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
        FormModuleElement,
    )

    lattice = Lattices.E8
    generator = lattice.module_generators()[0]

    surface = declared_surface(BasedFreeModuleElement, "element")
    assert "coefficients" in surface

    # Arithmetic stays where it is: ``_add_`` on a form module element has to
    # land in the form module, and will only be relayable once the two levels
    # share their elements by facade.  ``coefficients`` is the one body here
    # that does the underlying element's job and adds nothing.
    relays = forwarding_mixin(
        BasedFreeModuleElement,
        "element",
        "forget_form",
        answered_here=frozenset(vars(FormModuleElement)) - frozenset({"coefficients"}),
    )
    assert "coefficients" in vars(relays)

    coefficients = relays.coefficients(generator)
    # The first canonical generator is a single framing label with coefficient 1.
    assert list(coefficients.values()) == [1]
    assert coefficients == generator.forget_form().coefficients()


FORM_MORPHISM_HAND_FORWARDED = frozenset(
    {
        "module_generator_morphism",
        "matrix",
        "_call_",
        "lift",
        "kernel",
        "cokernel",
        "image",
        "is_injective",
        "index",
        "orthogonal_complement",
        "_repr_defn",
    }
)


def test_a_form_morphism_relays_the_module_morphism_it_holds() -> None:
    r"""The swap involution of $U$ answers through generated relays."""
    _ensure_preamble()
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
        FormMorphism,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        ModuleMorphism,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.morphism_matrices import (
        MorphismMatrix,
    )
    from sage.categories.morphism import Morphism
    from sage.matrix.constructor import matrix as sage_matrix
    from sage.rings.integer_ring import ZZ

    hyperbolic = Lattices.U
    first, second = tuple(hyperbolic.module_generators())
    swap = hyperbolic.Hom(hyperbolic)({first: second, second: first})

    surface = declared_surface(ModuleMorphism, "morphism")
    assert FORM_MORPHISM_HAND_FORWARDED <= surface

    relays = forwarding_mixin(
        ModuleMorphism,
        "morphism",
        "module_morphism",
        answered_here=frozenset(vars(FormMorphism)) - FORM_MORPHISM_HAND_FORWARDED,
    )
    assert FORM_MORPHISM_HAND_FORWARDED <= frozenset(vars(relays))

    stripped = _without(FormMorphism, FORM_MORPHISM_HAND_FORWARDED, Morphism)
    # Nine of the eleven vanish outright; ``_call_`` and ``_repr_defn`` fall
    # back to Sage's generic morphism versions, which are not the module
    # morphism's answers either.  None of them is the removed body.
    assert all(
        getattr(stripped, name, None) is not vars(FormMorphism)[name]
        for name in FORM_MORPHISM_HAND_FORWARDED
    )

    resolved = type("FormMorphismWithGeneratedForwarding", (relays, stripped), {})

    assert resolved.matrix is relays.matrix
    assert resolved.matrix(swap) == MorphismMatrix(sage_matrix(ZZ, [[0, 1], [1, 0]]))
    assert resolved._call_(swap, first) == second
    assert resolved._call_(swap, second) == first
    assert resolved.is_injective(swap) is True
    assert resolved.index(swap) == 1

    # Equality is about the pair -- two form morphisms with the same
    # underlying module map but different homsets are different morphisms --
    # so it stays where it is written and no relay displaces it.
    assert resolved.__eq__ is FormMorphism.__eq__
    assert "__eq__" not in surface
