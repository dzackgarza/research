r"""The owned ``Sets()`` root and its five axioms.

The owned root sits over Sage's ``Sets()`` and reuses Sage's standard
``Finite`` and ``Infinite`` axioms; project-owned ``Countable``,
``Uncountable``, and ``TotallyOrdered`` enter Sage's global ``all_axioms``
registry through the exact idempotent adapter below — the only Sage mutation
this module performs.

The axiom lattice is mathematical fact: ``Finite`` refines ``Countable``
(every finite set receives the enumeration contract), ``Uncountable``
refines ``Infinite``, ``Countable`` and ``Uncountable`` are disjoint, and
totally ordered sets are a trusted placement that says nothing about
cardinality. Countably-infinite is the join ``Sets().Countable().Infinite()``,
never a new named root. Membership is opt-in-with-trust: ``Countable`` forces
the executable witness suite (exhaustive duplicate-free iteration, integer
indexing, reverse lookup) through Sage ``abstract_method`` obligations;
``Uncountable`` is trusted placement carrying uniform consequences and no
enumeration obligation. Generic infinite-set consequences (``is_finite``,
``cardinality() == +Infinity``) are inherited from Sage's ``Infinite`` axiom
through the join and are never reimplemented here.
"""

from __future__ import annotations

from collections.abc import Iterator
from typing import cast, Generic, TYPE_CHECKING, TypeVar

from sage.categories.cartesian_product import CartesianProductsCategory
from sage.categories.category import Category
from sage.categories.category_with_axiom import CategoryWithAxiom, all_axioms
from sage.categories.sets_cat import Sets as SageSets
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.rings.semirings.non_negative_integer_semiring import NN

from dzack_research.preamble.lexicon.interop import SageParent, SageUniqueRepresentation



if TYPE_CHECKING:
    # Sage's abstract_method ships untyped; for type-checking use
    # abc.abstractmethod (typed, and permits the empty abstract bodies
    # below). Runtime uses Sage's.
    from abc import abstractmethod as abstract_method
    from sage.categories.morphism import SetMorphism
    from sage.structure.parent import ElementConstructorInput

    from dzack_research.preamble.categories.sets.cardinals import Cardinal

    class _ParentWithIsFinite(SageParent[_E], Generic[_E]):
        def is_finite(self) -> bool: ...
else:
    from sage.misc.abstract_method import abstract_method

_E = TypeVar("_E")

_SET_AXIOMS = ("Countable", "Uncountable", "PartiallyOrdered", "TotallyOrdered")


def register_set_axioms() -> None:
    r"""Register exactly ``Countable``, ``Uncountable``, ``PartiallyOrdered``, and
    ``TotallyOrdered`` in Sage's global
    axiom registry. Idempotent: after the first registration, repeated calls
    leave the registry unchanged."""
    for axiom_name in _SET_AXIOMS:
        if axiom_name not in all_axioms:
            all_axioms.add(axiom_name)
    assert all(axiom_name in all_axioms for axiom_name in _SET_AXIOMS)


register_set_axioms()


class CountabilitySubcategoryMethods:
    r"""The ``Countable``/``Uncountable``/``PartiallyOrdered``/``TotallyOrdered``
    axiom requests with their disjointness guards. Shared by the owned ``Sets()``
    root and by every owned structured root whose objects carry set axioms."""

    # Runtime Sage mixes this class into every subcategory, so ``self``
    # is a Category there; the casts state that fact for the checker.
    def Countable(self) -> Category:
        r"""Objects whose underlying set has a chosen computable,
        exhaustive, duplicate-free enumeration."""
        category = cast(Category, self)
        assert "Uncountable" not in category.axioms(), "Countable and Uncountable are disjoint"
        return category._with_axiom("Countable")

    def Uncountable(self) -> Category:
        r"""Objects whose underlying set is beyond every enumeration, by
        trusted declaration. (The reverse contradiction, ``Uncountable``
        then ``Finite``, is refused by Sage's native finite/infinite
        incompatibility because ``Uncountable`` implies ``Infinite``.)"""
        category = cast(Category, self)
        assert "Countable" not in category.axioms(), "Countable and Uncountable are disjoint"
        return category._with_axiom("Uncountable")

    def PartiallyOrdered(self) -> Category:
        r"""Objects whose underlying set is equipped with a partial order."""
        category = cast(Category, self)
        return category._with_axiom("PartiallyOrdered")

    def TotallyOrdered(self) -> Category:
        r"""Objects whose underlying set is equipped with a total order."""
        category = cast(Category, self)
        return category._with_axiom("TotallyOrdered")


class Sets(Category):
    r"""The owned category of sets: declaration owner of the generic
    meanings of cardinality, finiteness, infinitude, countability,
    uncountability, enumeration, indexing, and reverse lookup."""

    def super_categories(self) -> list[Category]:
        return [SageSets()]

    if TYPE_CHECKING:
        # Typed axiom navigation: at runtime Sage synthesizes these from
        # SubcategoryMethods; the axiom tree is closed under its own axioms.
        # The class-attribute wiring at the bottom of this module is Sage's
        # class-resolution shortcut and is runtime-only.
        def Countable(self) -> Sets: ...
        def Uncountable(self) -> Sets: ...
        def PartiallyOrdered(self) -> Sets: ...
        def TotallyOrdered(self) -> Sets: ...
        def Finite(self) -> Sets: ...
        def Infinite(self) -> Sets: ...
        def Facade(self) -> Sets: ...
    SubcategoryMethods = CountabilitySubcategoryMethods

    class CartesianProducts(CartesianProductsCategory):
        r"""Cartesian products in the owned category of sets."""

        def extra_super_categories(self) -> list[Category]:
            return [Sets()]

        class ParentMethods:
            if TYPE_CHECKING:
                def cartesian_factors(self) -> tuple[Sets.ParentMethods, ...]: ...

            def cardinality(self) -> Cardinal:
                r"""Return ``prod(#X_i)`` for the cartesian factors ``X_i``."""
                from dzack_research.preamble.categories.sets.cardinals import (
                    Cardinalities,
                )

                return Cardinalities().product(
                    *(factor.cardinality() for factor in self.cartesian_factors())
                )

    class ParentMethods:
        if TYPE_CHECKING:
            def cardinality(self) -> Cardinal: ...

        def is_countable(self) -> bool:
            r"""Whether $|X| \le \aleph_0$.

            Read off the cardinal, which is total on sets, rather than
            declared by placement: countability is a fact about the size, so
            any set that can say how big it is answers this, and no chosen
            enumeration is required to do it.  The axiom subcategories
            override with their exact answer.
            """
            return bool(self.cardinality().is_countable())

        def is_uncountable(self) -> bool:
            r"""Whether $|X| > \aleph_0$."""
            return bool(self.cardinality().is_uncountable())


class FiniteSets(CategoryWithAxiom):
    r"""Finite sets: Sage's standard axiom, plus the owned refinement that
    finiteness implies the countable enumeration contract."""

    _base_category_class_and_axiom = (Sets, "Finite")

    def extra_super_categories(self) -> list[Category]:
        return [cast(Sets, self.base_category()).Countable()]

    def __contains__(self, parent: ElementConstructorInput) -> bool:
        r"""Return whether ``parent`` is a finite set.

        Sage's default answers from category placement alone, so an object
        that has *computed* its finiteness — and says so through
        ``is_finite`` — is reported infinite merely because nothing refined
        it afterwards. Finiteness is a property of the object, and this
        category is the place that asks for it, so a caller writing the
        membership question gets the object's own answer rather than a
        record of how it was constructed.
        """
        from sage.structure.parent import Parent

        return isinstance(parent, Parent) and hasattr(parent, "is_finite") and bool(parent.is_finite())

    class ParentMethods:
        if TYPE_CHECKING:
            def __iter__(self) -> Iterator[_E]: ...

        def cardinality(self) -> Cardinal:
            r"""The exact count, by materializing the chosen enumeration —
            finite sets own the termination-dependent implementation,
            constructed from the witness suite.

            A construction that determines its own count states it directly
            (the fundamental finite sets, cartesian products, disjoint
            unions).  This is the one-time evaluation witness for a finite
            set whose construction does not: the enumeration runs once and
            the cardinal it yields is the set's stored count from then on."""
            stored = self.__dict__.get("_owned_cardinality")
            if stored is not None:
                return cast("Cardinal", stored)

            from sage.rings.integer_ring import ZZ

            from dzack_research.preamble.categories.sets.cardinals import cardinal

            stored = cardinal(ZZ(sum(1 for _ in self)))
            self._owned_cardinality = stored
            return stored


class InfiniteSets(CategoryWithAxiom):
    r"""Infinite sets: Sage's standard axiom supplies the uniform
    consequences (``is_finite() == False``, ``cardinality() == +Infinity``)
    through the join; nothing is reimplemented here."""

    _base_category_class_and_axiom = (Sets, "Infinite")


class CountableSets(CategoryWithAxiom):
    r"""Countable sets: the property that an injection into $\mathbb N$
    exists.

    Countability does not name an enumeration.  A set is countable when
    *some* injection into $\mathbb N$ exists, and a chosen one is extra
    data: the pair $(X, f\colon X\hookrightarrow U(\mathbb N))$ is an object
    of the slice over $U(\mathbb N)$, not a set carrying an adjective.  So
    this node declares the property and demands no enumeration; Sage's
    ``EnumeratedSets`` — parents that do come with a chosen one — is
    admitted as adapter machinery, which is what lets Sage's solved
    construction machinery (fair Cartesian-product iteration, disjoint
    unions) consume these natively, and is what supplies ``iter(X)`` where
    an enumeration was in fact chosen.
    """

    _base_category_class_and_axiom = (Sets, "Countable")

    def extra_super_categories(self) -> list[Category]:
        from sage.categories.enumerated_sets import EnumeratedSets

        return [EnumeratedSets()]

    class ParentMethods(Generic[_E]):
        if TYPE_CHECKING:
            def __iter__(self) -> Iterator[_E]: ...

        # Operations of a CHOSEN enumeration, available where one exists;
        # never obligations of countability.  ponytail: they read the
        # enumeration through iteration rather than through the slice object
        # that properly holds it -- see the module note on Slice(f).
        def __getitem__(self, n: int) -> _E:
            r"""The ``n``-th element of the chosen enumeration, ``n >= 0``."""
            assert n >= 0, f"enumeration indices are nonnegative; found {n}"
            for position, element in enumerate(self):
                if position == n:
                    return element
            assert False, f"index {n} exceeds the enumeration of {self}"

        def index(self, element: _E) -> int:
            r"""Reverse lookup in the chosen enumeration: terminates for
            members and satisfies ``X[X.index(x)] == x``. No termination
            promise for a nonmember of an infinite parent."""
            for position, candidate in enumerate(self):
                if candidate == element:
                    return position
            assert False, f"{element} is not in the enumeration of {self}"

        def enumeration_injection(self) -> SetMorphism[_E, Integer]:
            r"""The monomorphism into the SET of nonnegative integers
            realized by the chosen enumeration, ``x -> index(x)``, as an
            element of the actual homset — the constructed effective
            witness of countability. (The codomain is the underlying set of
            the naturals: the injection is a set map, so it forgets the
            semiring structure of its codomain.)"""
            from sage.categories.homset import Hom
            from sage.categories.morphism import SetMorphism

            from dzack_research.preamble.categories.sets.underlying_sets import UnderlyingSet

            domain = cast(SageParent[_E], self)
            naturals = cast(SageParent[Integer], NonNegativeIntegers())
            target: UnderlyingSet[Integer] = UnderlyingSet(naturals)
            homset = Hom(domain, target, SageSets())
            # target[n] IS the natural number n (identity enumeration),
            # already normalized into the host parent.
            return SetMorphism(homset, lambda element: target[self.index(element)])

        def is_countable(self) -> bool:
            return True

        def is_uncountable(self) -> bool:
            return False


class CountablyInfiniteSets(CategoryWithAxiom):
    r"""Countably infinite sets — the join ``Sets().Countable().Infinite()``,
    never a new named root. Owns the exact cardinal: ``aleph_0``."""

    _base_category_class_and_axiom = (CountableSets, "Infinite")

    class ParentMethods:
        def cardinality(self) -> Cardinal:
            r"""``aleph_0``, exactly — not Sage's countable-blind
            ``+Infinity`` (to which it compares equal)."""
            from dzack_research.preamble.categories.sets.cardinals import aleph0

            return aleph0


class UncountableSets(CategoryWithAxiom):
    r"""Uncountable sets: trusted placement, uniform consequences, and in
    particular infinite."""

    _base_category_class_and_axiom = (Sets, "Uncountable")

    def extra_super_categories(self) -> list[Category]:
        return [self.base_category().Infinite()]

    class ParentMethods:
        def is_countable(self) -> bool:
            return False

        def is_uncountable(self) -> bool:
            return True

from sage.structure.element import Element as SageElement
from sage.categories.homset import Homset as SageHomset


class PosetMorphism(SageElement):
    r"""Morphism of partially ordered sets (order-preserving map)."""

    def __init__(self, parent: "PosetHomset", function: Any) -> None:
        SageElement.__init__(self, parent)
        self._function = function

    def __call__(self, x: Any) -> Any:
        return self._function(x)

    def domain(self) -> Any:
        return self.parent().domain()

    def codomain(self) -> Any:
        return self.parent().codomain()

    def is_order_preserving(self) -> bool:
        r"""Return True if x <= y implies f(x) <= f(y)."""
        dom = self.domain()
        codom = self.codomain()
        for x, y in dom.cover_relations():
            if not codom.is_lequal(self(x), self(y)):
                return False
        return True

    def is_order_reflecting(self) -> bool:
        r"""Return True if f(x) <= f(y) implies x <= y."""
        dom = self.domain()
        codom = self.codomain()
        for x in dom:
            for y in dom:
                if codom.is_lequal(self(x), self(y)) and not dom.is_lequal(x, y):
                    return False
        return True

    def is_order_embedding(self) -> bool:
        r"""Return True if x <= y iff f(x) <= f(y)."""
        return self.is_order_preserving() and self.is_order_reflecting()

    def is_injective(self) -> bool:
        r"""Return True if f is one-to-one."""
        images = [self(x) for x in self.domain()]
        return len(images) == len(set(images))

    def is_surjective(self) -> bool:
        r"""Return True if f maps onto the codomain."""
        images = set(self(x) for x in self.domain())
        return images == set(self.codomain())

    def is_bijective(self) -> bool:
        return self.is_injective() and self.is_surjective()

    def is_order_isomorphism(self) -> bool:
        r"""Return True if f is a bijective order embedding."""
        return self.is_order_embedding() and self.is_bijective()

    def inverse(self) -> "PosetMorphism":
        r"""Return the inverse poset isomorphism."""
        if not self.is_order_isomorphism():
            raise ValueError("Inverse only exists for order isomorphisms")
        inv_map = {self(x): x for x in self.domain()}
        return PosetHomset(self.codomain(), self.domain())(lambda y: inv_map[y])

    def __mul__(self, other: "PosetMorphism") -> "PosetMorphism":
        if self.domain() != other.codomain():
            raise ValueError("Domains and codomains do not match for composition")
        return PosetHomset(other.domain(), self.codomain())(lambda x: self(other(x)))

    def _repr_(self) -> str:
        return f"Poset morphism from {self.domain()} to {self.codomain()}"


class PosetHomset(SageHomset):
    r"""Set of morphisms between partially ordered sets."""

    Element = PosetMorphism

    def _element_constructor_(self, f: Any) -> PosetMorphism:
        mor = PosetMorphism(self, f)
        if not mor.is_order_preserving():
            raise ValueError(f"Function {f} does not preserve partial order (not a poset homomorphism)")
        return mor


class PosetTikz:
    r"""TikZ Hasse diagram representation."""

    def __init__(self, poset: Any, label_map: Any = None, scale: float = 1.0, width: int = 550, height: int = 420) -> None:
        self._poset = poset
        self._label_map = label_map
        self._scale = scale
        self._width = width
        self._height = height
        self._coords = self._compute_layout()

    def _compute_layout(self) -> dict[Any, tuple[float, float]]:
        heights: dict[Any, int] = {}
        for v in self._poset.linear_extension():
            low = self._poset.lower_covers(v)
            if not low:
                heights[v] = 0
            else:
                heights[v] = max(heights[u] for u in low) + 1

        max_h = max(heights.values()) if heights else 0
        levels: dict[int, list[Any]] = {h: [] for h in range(max_h + 1)}
        for v, h in heights.items():
            levels[h].append(v)

        coords: dict[Any, tuple[float, float]] = {}
        for h in range(max_h + 1):
            elems = list(levels[h])
            if h > 0:
                def avg_pred_x(v: Any) -> float:
                    preds = self._poset.lower_covers(v)
                    if preds and any(u in coords for u in preds):
                        return sum(coords[u][0] for u in preds if u in coords) / len(preds)
                    return 0.0
                try:
                    elems.sort(key=lambda v: (avg_pred_x(v), str(v)))
                except Exception:
                    pass

            m = len(elems)
            for i, v in enumerate(elems):
                x = (i - (m - 1) / 2.0) * 2.0
                y = float(h * 2.0)
                coords[v] = (x, y)

        return coords

    def tikz_code(self) -> str:
        node_id_map = {v: f"node_{i}" for i, v in enumerate(self._poset)}
        lines = [
            r"\begin{tikzpicture}[",
            f"  scale={self._scale:.2f},",
            r"  every node/.style={circle, draw=black!80, fill=blue!10, inner sep=2pt, minimum size=18pt, font=\small},",
            r"  edge/.style={draw=black!70, thick, -}",
            r"]",
        ]
        for v, (x, y) in self._coords.items():
            lbl = str(self._label_map(v) if self._label_map else v)
            nid = node_id_map[v]
            lines.append(f"  \\node ({nid}) at ({x:.2f}, {y:.2f}) {{{lbl}}};")
        for u, v in self._poset.cover_relations():
            nid_u = node_id_map[u]
            nid_v = node_id_map[v]
            lines.append(f"  \\draw[edge] ({nid_u}) -- ({nid_v});")
        lines.append(r"\end{tikzpicture}")
        return "\n".join(lines)

    def _repr_(self) -> str:
        return self.tikz_code()

    def _latex_(self) -> str:
        return self.tikz_code()

    def _repr_latex_(self) -> str:
        return f"$$\n{self.tikz_code()}\n$$"

    def _repr_html_(self) -> str:
        if not self._coords:
            return "<div>Empty Poset</div>"
        margin = 45
        xs = [pt[0] for pt in self._coords.values()]
        ys = [pt[1] for pt in self._coords.values()]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        span_x = (max_x - min_x) if max_x > min_x else 1.0
        span_y = (max_y - min_y) if max_y > min_y else 1.0

        px_coords = {}
        for v, (x, y) in self._coords.items():
            px_x = margin + (x - min_x) / span_x * (self._width - 2 * margin)
            px_y = (self._height - margin) - (y - min_y) / span_y * (self._height - 2 * margin)
            px_coords[v] = (px_x, px_y)

        node_radius = 16
        svg_lines = [
            '<div style="display: flex; justify-content: center; margin: 12px 0;">',
            f'<svg width="{self._width}" height="{self._height}" viewBox="0 0 {self._width} {self._height}" xmlns="http://www.w3.org/2000/svg">',
            "  <style>",
            "    .hasse-edge { stroke: #5f6368; stroke-width: 2; stroke-linecap: round; }",
            "    .hasse-node { fill: #f8f9fa; stroke: #1a73e8; stroke-width: 2; transition: all 0.2s; }",
            "    .hasse-node:hover { fill: #e8f0fe; stroke: #174ea6; stroke-width: 3; }",
            '    .hasse-text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; font-size: 11px; font-weight: 600; fill: #202124; text-anchor: middle; dominant-baseline: central; pointer-events: none; }',
            "  </style>",
        ]

        for u, v in self._poset.cover_relations():
            x1, y1 = px_coords[u]
            x2, y2 = px_coords[v]
            svg_lines.append(f'  <line class="hasse-edge" x1="{x1:.1f}" y1="{y1:.1f}" x2="{y2:.1f}" y2="{y2:.1f}" />')

        for v, (x, y) in px_coords.items():
            lbl = str(self._label_map(v) if self._label_map else v)
            if len(lbl) > 12:
                lbl = lbl[:10] + ".."
            svg_lines.append(f'  <circle class="hasse-node" cx="{x:.1f}" cy="{y:.1f}" r="{node_radius}" />')
            svg_lines.append(f'  <text class="hasse-text" x="{x:.1f}" y="{y:.1f}">{lbl}</text>')

        svg_lines.append("</svg></div>")
        return "\n".join(svg_lines)


def _poset_repr_html(poset: Any) -> str:
    return PosetTikz(poset)._repr_html_()


def _poset_latex(poset: Any) -> str:
    return PosetTikz(poset).tikz_code()


def _poset_repr_latex(poset: Any) -> str:
    return rf"\(\displaystyle {_poset_latex(poset)}\)"


def _poset_rich_repr(poset: Any, dm: Any) -> Any:
    if hasattr(dm, "types") and hasattr(dm, "supported_output"):
        if dm.types.OutputHtml in dm.supported_output():
            html_content = _poset_repr_html(poset)
            return dm.types.OutputHtml(html_content)
        elif dm.types.OutputLatex in dm.supported_output():
            return dm.types.OutputLatex(_poset_latex(poset))
        elif dm.types.OutputPlainText in dm.supported_output():
            return dm.types.OutputPlainText(repr(poset))
    return None


def _poset_repr_mimebundle(poset: Any, include: Any = None, exclude: Any = None) -> dict[str, str]:
    return {
        "text/html": _poset_repr_html(poset),
        "text/latex": _poset_repr_latex(poset),
        "text/plain": repr(poset),
    }


class PartiallyOrderedSets(CategoryWithAxiom):
    r"""Partially ordered sets."""

    _base_category_class_and_axiom = (Sets, "PartiallyOrdered")

    class ParentMethods:
        def hasse_layout(self) -> dict[Any, tuple[float, float]]:
            r"""Compute ranked (x, y) coordinates for the Hasse diagram without dot2tex."""
            pt = PosetTikz(self)
            return pt._coords

        def hasse_tikz(self, label_map: Any = None, scale: float = 1.0) -> PosetTikz:
            r"""Return a PosetTikz representation of the Hasse diagram."""
            return PosetTikz(self, label_map=label_map, scale=scale)

        def tikz(self, label_map: Any = None, scale: float = 1.0) -> PosetTikz:
            r"""Alias for :meth:`hasse_tikz`."""
            return self.hasse_tikz(label_map=label_map, scale=scale)

        def _repr_html_(self) -> str:
            r"""Render clean inline SVG in Jupyter notebook without dot2tex warnings."""
            return _poset_repr_html(self)

        def _latex_(self) -> str:
            return _poset_latex(self)

        def _repr_latex_(self) -> str:
            return _poset_repr_latex(self)

        def _rich_repr_(self, dm: Any) -> Any:
            return _poset_rich_repr(self, dm)

        def _repr_mimebundle_(self, include: Any = None, exclude: Any = None) -> dict[str, str]:
            return _poset_repr_mimebundle(self, include=include, exclude=exclude)


def install_poset_display() -> None:
    r"""Install clean Hasse diagram TikZ/SVG display methods onto Sage's FinitePoset."""
    try:
        from sage.combinat.posets.posets import FinitePoset
        FinitePoset.hasse_layout = lambda self: PosetTikz(self)._coords
        FinitePoset.hasse_tikz = lambda self, label_map=None, scale=1.0: PosetTikz(self, label_map=label_map, scale=scale)
        FinitePoset.tikz = lambda self, label_map=None, scale=1.0: PosetTikz(self, label_map=label_map, scale=scale)
        FinitePoset._repr_html_ = _poset_repr_html
        FinitePoset._latex_ = _poset_latex
        FinitePoset._repr_latex_ = _poset_repr_latex
        FinitePoset._rich_repr_ = _poset_rich_repr
        FinitePoset._repr_mimebundle_ = _poset_repr_mimebundle
    except Exception:
        pass


install_poset_display()


class TotallyOrderedSets(CategoryWithAxiom):
    r"""Totally ordered sets."""

    _base_category_class_and_axiom = (Sets, "TotallyOrdered")

    def extra_super_categories(self) -> list[Category]:
        return [self.base_category().PartiallyOrdered()]


_SET_AXIOM_NAMES = (
    "Finite",
    "Infinite",
    "Countable",
    "Uncountable",
    "PartiallyOrdered",
    "TotallyOrdered",
)


def placement_of(parent: SageParent[_E]) -> Sets:
    r"""The owned ``Sets()`` placement a parent's declared axioms carry.

    Countability, finiteness and order are answers this parent already
    declares; reading them off is how an object enters the owned sets able
    to answer what ``Sets`` declares abstract.  Contradictory declarations
    are refused by the owned axiom guards at translation time.

    Sage's ``Enumerated`` witnesses countability without being it: it
    asserts a *chosen* enumeration, and exhibiting one injection into
    $\mathbb N$ proves the property.  Only the property is recorded here;
    the chosen enumeration is the structure map of a slice object over
    $U(\mathbb N)$ and does not travel in a ``Sets`` placement.
    """
    declared = frozenset(parent.category().axioms())
    axioms = declared & frozenset(_SET_AXIOM_NAMES)
    placement = Sets()
    if "Finite" in axioms:
        placement = placement.Finite()
    elif "Countable" in axioms or "Enumerated" in declared:
        placement = placement.Countable()
    if "Uncountable" in axioms:
        placement = placement.Uncountable()
    elif "Infinite" in axioms:
        placement = placement.Infinite()
    if "TotallyOrdered" in axioms:
        placement = placement.TotallyOrdered()
    elif "PartiallyOrdered" in axioms:
        placement = placement.PartiallyOrdered()
    else:
        from sage.categories.posets import Posets as SagePosets
        if parent.category().is_subcategory(SagePosets()):
            placement = placement.PartiallyOrdered()
    return placement


class NonNegativeIntegers(SageUniqueRepresentation, SageParent):
    r"""The nonnegative integers as an owned countable set: the identity
    enumeration ``0, 1, 2, ...`` over Sage's ``NN``.

    Placed in the owned sets and nowhere higher.  This exists as the codomain
    of :meth:`enumeration_injection`, which is a map of *sets*: it forgets the
    semiring structure of the naturals, so declaring that structure here would
    claim something the one caller discards.
    """

    def __init__(self) -> None:
        SageParent.__init__(self, facade=NN, category=Sets().Countable().Infinite().Facade())

    def _repr_(self) -> str:
        return "Set of nonnegative integers"

    def __iter__(self) -> Iterator[Integer]:
        return iter(NN)

    def index(self, element: Integer | int) -> Integer:
        member = ZZ(element)
        assert member >= 0, f"{element} is not a nonnegative integer"
        return member


if not TYPE_CHECKING:
    # Sage's class-resolution shortcut: the axiom category class must be
    # reachable as `<BaseCategory>.<Axiom>` for `_base_category_class_and_axiom`
    # to resolve. Runtime-only wiring; the typed surface of these names is the
    # axiom-navigation method declarations on the category class above.
    Sets.Finite = FiniteSets
    Sets.Infinite = InfiniteSets
    Sets.Countable = CountableSets
    Sets.Uncountable = UncountableSets
    Sets.PartiallyOrdered = PartiallyOrderedSets
    Sets.TotallyOrdered = TotallyOrderedSets
    CountableSets.Infinite = CountablyInfiniteSets
