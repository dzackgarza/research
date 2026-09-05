r"""The preamble reference, surveyed from a live session.

Run it::

    just preamble-megadoc

The question this document answers is "what can I build on, and how does it
fit together".  That is a question about the category graph, and the category
graph exists only at runtime: ``super_categories`` is a method, the base ring
is an argument, and which operations an object gets is decided by Sage's
dynamic ``parent_class``.  A source-text scrape can see none of it, so this
module imports ``dzack_research.preamble.all`` and interrogates the objects.

Three surfaces come out of one survey:

- ``docs/preamble-megadoc.md``   the reference a contributor reads
- ``docs/preamble-graph.json``   the category and functor graph, serialized
- ``docs/preamble-graph.dot``    the same graph for GraphViz, rendered to
  ``docs/preamble-graph.html`` (pan and zoom) when ``dot`` is installed

Introspection is defensive: a category the survey cannot instantiate, or a
method whose signature will not resolve, is *recorded with its error*.  A
reference that quietly omits what it could not read is worse than one that
says so.
"""

from __future__ import annotations

import argparse
import html
import inspect
import json
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from types import ModuleType
from typing import Final, Protocol, TypeVar, runtime_checkable

# Imported for real, not only for annotations: `issubclass` against a module
# name narrows a type, while `issubclass` against an attribute stashed on the
# survey does not, and the survey's whole job is to sort a namespace by kind.
from sage.categories.category import Category, JoinCategory
from sage.categories.morphism import Morphism
from sage.misc.abstract_method import AbstractMethod
from sage.misc.cachefunc import CachedMethod
from sage.structure.parent import Parent
from sage.structure.element import Element


@runtime_checkable
class WrapsAFunction(Protocol):
    r"""What Sage's cached-method descriptor yields: a caller keeping its function.

    The caller's own docstring and signature describe the caching wrapper, so the
    function it holds is the only route to what the method actually is.
    """

    f: Callable[..., object]

from dzack_research.preamble.categories.functors.core import Adjunction, Functor

# What a class dictionary holds: a plain function, or one of the descriptors
# Sage wraps one in.  The survey reads these to report a category's operations.
type ClassMember = Callable[..., object] | CachedMethod | AbstractMethod | property

# Anything `inspect` can locate source for, and anything it can sign.
type Inspectable = type | Callable[..., object]

# A mathematical object of the session: a parent, or an element of one.
type Specimen = Parent | Element

# `inspect` raises TypeError for a value carrying no code object and OSError
# once the source file is gone; either way there is no source to point at.
# Named rather than written inline because the formatter unparenthesizes an
# inline tuple into Python 3.14's `except A, B`, which reads as a syntax error.
NO_SOURCE: Final = (TypeError, OSError)

# TypeError for something not callable, ValueError for a callable whose
# signature cannot be recovered -- a Cython builtin, most often.
NO_SIGNATURE: Final = (TypeError, ValueError)

Built = TypeVar("Built")

REPO_ROOT: Final = Path(__file__).resolve().parents[3]
GRAPH_TEMPLATE: Final = REPO_ROOT / "docs" / "lean" / "_category-graph-template.html"

# Directory under ``preamble/`` -> chapter title and its one-line scope.
SUBSYSTEM_ORDER: Final[list[tuple[str, str, str]]] = [
    (
        "abstract_categories",
        "Abstract Category Theory & Universal Constructions",
        "Category of categories (Cat), Arrow and Slice categories, Limits, Colimits, Biproducts, Subobjects, and Diagram categories.",
    ),
    (
        "functors",
        "Functors & Adjunctions",
        "Functorial constructions, Adjunctions, Base change, Free/Forgetful, Cohomology, De Rham, Group actions, and Induction.",
    ),
    (
        "lattices",
        "Lattices, Quadratic Forms & Invariants",
        "Free modules with quadratic forms, Genus, Definite/Root/Rational lattices, Isometries, Embeddings, Orbits, and Diagrams.",
    ),
    (
        "modules",
        "Modules, Complexes & Homological Algebra",
        "Framed free modules, Finitely presented modules, Formed modules, Group modules, Cochain complexes, Connections, and DG modules.",
    ),
    (
        "algebras",
        "Algebras & Differential Graded Algebras",
        "Associative/Commutative algebras, DGAs, Cohomology algebras, De Rham algebras, Derivations, and Graded algebras.",
    ),
    (
        "group",
        "Groups, Profinite Groups & Galois Theory",
        "Groups, Finitely presented groups, G-Sets, Actions, Profinite groups, Absolute Galois groups, Characters, and Inertia.",
    ),
    (
        "rings",
        "Rings, Fields & Commutative Algebra",
        "Owned rings, Fields, Number fields, Prime spectrum, Completions, Localizations, Exact real field, and Predicate subrings.",
    ),
    (
        "schemes",
        "Schemes & Algebraic Geometry",
        "Schemes, Affine/Projective schemes, Subschemes, Varieties, Curves, Surfaces, Polytopes, and Structure sheaves.",
    ),
    (
        "divisors",
        "Divisors & Picard Theory",
        "Divisor groups, Cartier divisors, Weil divisors, Picard groups, Class groups, and Formal divisors.",
    ),
    (
        "forms",
        "Bilinear Forms, Quadratic Forms & Pairings",
        "Bilinear/Quadratic forms, Pairings, Gram matrices, and Form spaces.",
    ),
    (
        "functions",
        "Function Spaces & Analysis",
        "Lebesgue modules, Lp, ell, C(X), Graded Lebesgue algebras, and Convolution algebras.",
    ),
    (
        "sets",
        "Sets, Cardinals & Ordinals",
        "Sets, Cardinalities, Ordinals, Enumerated sets, Fourier characters, Hermite polynomials, and Power sets.",
    ),
    (
        "catalogue",
        "Named Catalogue & Classification Tables",
        "Named integral lattices (U, E8, LK3, Mukai, etc.), 2-elementary tables, Nikulin involutions, and Primitive embeddings.",
    ),
    (
        "tensors",
        "Tensor Calculus",
        "Multilinear tensors, Tensor modules, Tensor shapes, and Tensor products.",
    ),
    (
        "logic",
        "Logic & Predicates",
        "Three-valued logic predicates, queries, and certainty propagation.",
    ),
    (
        "geometry_specialized",
        "Specialized Geometries (Coble & Sterk)",
        "Coble surfaces, Sterk invariant theory, and Automorphic forms.",
    ),
    (
        "preamble_root",
        "Preamble Entrypoints & Utilities",
        "Top-level session loaders, environment initializers, and refinement helpers.",
    ),
]
SUBSYSTEM_TITLES: Final = {key: (title, scope) for key, title, scope in SUBSYSTEM_ORDER}

# Above this many nodes an inline diagram is a hairball; the interactive graph
# is the right surface for that subsystem instead.
MERMAID_NODE_CAP: Final = 44

# Naming a dozen specimens tells a reader what the category is for; naming
# forty tells them nothing more and buries the entry.
SPECIMEN_CAP: Final = 12


def summarize(doc: str | None) -> str:
    r"""The first sentence of a docstring, on one line."""
    if not doc:
        return ""
    text = inspect.cleandoc(doc)
    text = text.split("\n\n", 1)[0].replace("\n", " ").strip()
    return re.sub(r"\s+", " ", text)


def anchor(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def source_of(obj: Inspectable) -> str:
    r"""``path:line`` relative to the repository, or an empty string."""
    try:
        path = Path(inspect.getsourcefile(obj) or "")
        line = inspect.getsourcelines(obj)[1]
    except NO_SOURCE:
        return ""
    try:
        return f"{path.relative_to(REPO_ROOT)}:{line}"
    except ValueError:
        return f"{path}:{line}"


def subsystem_of(module_name: str) -> str:
    r"""The chapter a symbol belongs to, from the module that defines it."""
    prefix = "dzack_research.preamble."
    if not module_name.startswith(prefix):
        return "preamble_root"
    parts = module_name[len(prefix) :].split(".")
    if parts[0] == "categories" and len(parts) > 1:
        return parts[1] if parts[1] in SUBSYSTEM_TITLES else "abstract_categories"
    if parts[0] in SUBSYSTEM_TITLES:
        return parts[0]
    if parts[0] in {"coble", "sterk"}:
        return "geometry_specialized"
    return "preamble_root"


def signature_of(obj: Inspectable, constructor: bool = False) -> str:
    r"""The call signature, with the receiver dropped: a reader supplies the rest.

    A constructor additionally loses its ``-> None``, which says nothing about
    what building the thing gives you.
    """
    try:
        signature = inspect.signature(obj)
    except NO_SIGNATURE:
        return "(...)"
    kept = [p for name, p in signature.parameters.items() if name != "self"]
    signature = signature.replace(
        parameters=kept,
        return_annotation=inspect.Signature.empty if constructor else signature.return_annotation,
    )
    return str(signature)


@dataclass
class MethodDoc:
    name: str
    signature: str
    summary: str
    mark: str = ""

    def render(self) -> str:
        head = f"- `{self.name}{self.signature}`"
        if self.mark:
            head += f" <sub>{self.mark}</sub>"
        return f"{head}\n  - {self.summary}" if self.summary else head


@dataclass
class CategoryDoc:
    name: str
    module: str
    subsystem: str
    source: str
    doc: str
    exported: bool
    arity: str  # "nullary" | "parameterized" | "construction"
    instance_repr: str = ""
    call_signature: str = ""
    init_signature: str = ""
    supers: list[str] = field(default_factory=list)
    ancestry: list[str] = field(default_factory=list)
    subcategories: list[str] = field(default_factory=list)
    own_methods: dict[str, list[MethodDoc]] = field(default_factory=dict)
    inherited: list[tuple[str, int, int, int]] = field(default_factory=list)
    specimens: list[str] = field(default_factory=list)
    specimen_total: int = 0
    problem: str = ""

    @property
    def display(self) -> str:
        return f"{self.name}(R)" if self.arity == "parameterized" else self.name

    @property
    def own_total(self) -> int:
        return sum(len(v) for v in self.own_methods.values())


@dataclass
class FunctorDoc:
    name: str
    kind: str  # "FUNCTOR" | "ADJUNCTION"
    subsystem: str
    source: str
    doc: str
    exported: bool
    domain: str = ""
    codomain: str = ""
    init_signature: str = ""
    methods: list[MethodDoc] = field(default_factory=list)
    problem: str = ""


@dataclass
class SpecimenDoc:
    name: str
    repr_text: str
    invariants: dict[str, str]
    category: str


@dataclass
class CatalogueDoc:
    name: str
    subsystem: str
    source: str
    doc: str
    specimens: list[SpecimenDoc] = field(default_factory=list)


@dataclass
class PlainDoc:
    r"""An exported symbol that is not a category, functor or catalogue."""

    name: str
    kind: str
    subsystem: str
    source: str
    doc: str
    signature: str = ""
    category: str = ""
    methods: list[MethodDoc] = field(default_factory=list)


class Survey:
    r"""Everything the reference reports, read off a live session."""

    def __init__(self) -> None:
        sys.setrecursionlimit(5000)
        import dzack_research.preamble.all as session
        from dzack_research.preamble.rings import session_ring_objects

        self.session: ModuleType = session
        self.names = [n for n in dir(session) if not n.startswith("_")]
        self.exported = set(self.names)

        # The probe ring is the session's own ZZ, which a session receives by
        # rebinding rather than by export, so it is taken from the constructor
        # that makes it instead of read off the module.
        ring = session_ring_objects()["ZZ"]
        assert isinstance(ring, Parent), "the session's ZZ must be an owned parent"
        self.ring: Parent = ring

        self.categories: dict[str, CategoryDoc] = {}
        self.functors: list[FunctorDoc] = []
        self.catalogues: list[CatalogueDoc] = []
        self.plain: list[PlainDoc] = []
        self.sage_supers: set[str] = set()

    # ---- naming -------------------------------------------------------

    @staticmethod
    def family_of(category: Category) -> tuple[str, str]:
        r"""The defining class of a live category, as ``(name, module)``.

        Sage hands out dynamic ``X_with_category`` subclasses; the family a
        contributor writes is the class underneath.
        """
        for klass in type(category).__mro__:
            if not klass.__name__.endswith("_with_category"):
                return klass.__name__, klass.__module__
        return type(category).__name__, type(category).__module__

    @staticmethod
    def expand(category: Category) -> list[Category]:
        r"""A join stands for its components; anything else stands for itself."""

        if isinstance(category, JoinCategory):
            return list(category.super_categories())
        return [category]

    @staticmethod
    def is_owned(module: str) -> bool:
        return module.startswith("dzack_research.")

    @staticmethod
    def build(factory: Callable[..., Built], arguments: tuple[Parent, ...]) -> Built | str:
        r"""Construct one, or report why it would not build.

        Reaching an arbitrary owned constructor reaches GAP, PARI and every
        category in the tree, so the raise is unbounded.  The failure is
        returned rather than swallowed: it is printed in the entry.
        """
        try:
            return factory(*arguments)
        except Exception as error:  # noqa: BLE001 - see the docstring
            return f"{type(error).__name__}: {error}"

    # ---- categories ---------------------------------------------------

    def probe_arguments(self, klass: type) -> tuple[tuple[Parent, ...], str] | None:
        r"""What to build one from, read off the category's declared type.

        The declaration is the base class or the annotation, never the parameter's
        name: a name is a string, and a string is not a type.  A category derived
        from ``OwnedCategoryOverBaseRing`` *is* declared to be over a base ring, so
        the session's ring is supplied.  Anything else -- a bare ``parameter``, or a
        second parameter with no annotation -- declares nothing, and there is
        nothing here to construct from.  The survey does not guess, and it does not
        keep a table of what each category probably meant: what a parameter *is* is
        mathematics, and it belongs in the preamble's own signature (`LEX-01`,
        `LEX-12`).  Until it is written there, the category is reported as
        undeclared rather than placed on a guess that happened to work.
        """
        try:
            signature = inspect.signature(klass)
        except NO_SIGNATURE:
            return None
        params = [p for name, p in signature.parameters.items() if name != "self"]
        if not params:
            return (), "nullary"
        if len(params) == 1 and self.is_over_a_ring(klass):
            return (self.ring,), "parameterized"
        return None

    @staticmethod
    def is_over_a_ring(klass: type) -> bool:
        r"""Whether the category declares, by its base class, that it is over a ring."""
        from dzack_research.preamble.categories.rings.ring_foundation import (
            OwnedCategoryOverBaseRing,
        )

        return issubclass(klass, OwnedCategoryOverBaseRing)

    def collect_categories(self) -> None:
        pending: list[Category] = []
        for name in self.names:
            value = getattr(self.session, name)
            if not (inspect.isclass(value) and issubclass(value, Category)):
                continue
            probe = self.probe_arguments(value)
            arity = probe[1] if probe is not None else "undeclared"
            doc = CategoryDoc(
                name=name,
                module=value.__module__,
                subsystem=subsystem_of(value.__module__),
                source=source_of(value),
                doc=inspect.getdoc(value) or "",
                exported=True,
                arity=arity,
                init_signature=signature_of(value, constructor=True),
            )
            self.categories[name] = doc
            built = self.build(value, probe[0]) if probe is not None else None
            if isinstance(built, Category):
                self.describe(doc, built)
                pending.append(built)
                continue
            if isinstance(built, str):
                doc.problem = built
            self.read_declared_methods(doc, value)

        self.close_ancestry(pending)
        self.invert_edges()

    def describe(self, doc: CategoryDoc, instance: Category) -> None:
        doc.instance_repr = repr(instance)
        doc.call_signature = signature_of(type(instance).__call__)
        for super_category in instance.super_categories():
            for part in self.expand(super_category):
                name, module = self.family_of(part)
                doc.supers.append(name)
                if not self.is_owned(module):
                    self.sage_supers.add(name)
        for ancestor in instance.all_super_categories()[1:]:
            for part in self.expand(ancestor):
                name, _ = self.family_of(part)
                if name not in doc.ancestry:
                    doc.ancestry.append(name)
        self.read_methods(doc, instance)

    def read_methods(self, doc: CategoryDoc, instance: Category) -> None:
        r"""Split every operation an object of this category answers to by owner.

        Sage builds ``parent_class`` and its siblings from the category graph, so
        the defining class in that MRO *is* the category that owns the method.
        """
        counts: dict[str, list[int]] = defaultdict(lambda: [0, 0, 0])
        slots = ("parent_class", "element_class", "morphism_class")
        labels = ("objects", "elements", "morphisms")
        for index, (slot, label) in enumerate(zip(slots, labels, strict=True)):
            dynamic = getattr(instance, slot, None)
            if dynamic is None:
                continue
            for klass in dynamic.__mro__:
                owner = klass.__qualname__.split(".")[0]
                if owner in {"object", "type"}:
                    continue
                members = self.members(klass)
                if owner == doc.name:
                    if members:
                        doc.own_methods.setdefault(label, []).extend(members)
                elif members:
                    counts[owner][index] += len(members)
        doc.inherited = sorted(
            ((owner, tally[0], tally[1], tally[2]) for owner, tally in counts.items()),
            key=lambda row: (-(row[1] + row[2] + row[3]), row[0]),
        )

    # Sage's runtime containers for methods a category installs on its objects,
    # elements and morphisms.  They are read here only to recover operations
    # from a category the survey could not build; the public vocabulary is the
    # mathematical one the report prints.
    CONTAINERS: Final = (
        ("parent_class", "objects"),
        ("element_class", "elements"),
        ("morphism_class", "morphisms"),
        ("ParentMethods", "objects"),
        ("ElementMethods", "elements"),
        ("MorphismMethods", "morphisms"),
    )

    def read_declared_methods(self, doc: CategoryDoc, klass: type) -> None:
        r"""Operations a category declares, for one that will not instantiate.

        No provenance is available without a live object -- there is no MRO to
        walk -- so this reports what the class body itself introduces, which is
        the part that would otherwise vanish from the reference entirely.
        """
        for attribute, label in self.CONTAINERS[3:]:
            container = vars(klass).get(attribute)
            if inspect.isclass(container):
                found = self.members(container)
                if found:
                    doc.own_methods.setdefault(label, []).extend(found)

    @staticmethod
    def unwrap(klass: type, value: ClassMember) -> tuple[Inspectable, str]:
        r"""The plain function behind a descriptor, and what the descriptor is.

        Sage's ``cached_method`` and ``abstract_method`` are Cython descriptors
        that keep the function out of reach until the descriptor protocol runs;
        an unwrapped one reports its own class docstring as the method's, which
        is how a reference ends up documenting ``CachedMethod`` 372 times.
        """

        if isinstance(value, CachedMethod):
            caller = value.__get__(None, klass)
            return caller.f, "cached"
        if isinstance(value, AbstractMethod):
            return value._f, "abstract, a contract on implementations"  # noqa: SLF001
        if isinstance(value, property):
            assert value.fget is not None, "a property the survey reads must be readable"
            return value.fget, "read as an attribute"
        return value, ""

    @classmethod
    def members(cls, klass: type) -> list[MethodDoc]:

        found: list[MethodDoc] = []
        for name, value in sorted(vars(klass).items()):
            if name.startswith("_"):
                continue
            if not (callable(value) or isinstance(value, (CachedMethod, AbstractMethod, property))):
                continue
            target, mark = cls.unwrap(klass, value)
            found.append(
                MethodDoc(
                    name=name,
                    signature=signature_of(target),
                    summary=summarize(inspect.getdoc(target)),
                    mark=mark,
                )
            )
        return found

    def close_ancestry(self, instances: list[Category]) -> None:
        r"""Add the categories reachable only as ancestors, so the poset closes."""
        seen = set(self.categories)
        for instance in instances:
            for ancestor in instance.all_super_categories():
                for part in self.expand(ancestor):
                    name, module = self.family_of(part)
                    if name in seen:
                        continue
                    seen.add(name)
                    klass = type(part).__mro__[0]
                    doc = CategoryDoc(
                        name=name,
                        module=module,
                        subsystem=subsystem_of(module),
                        source=source_of(klass),
                        doc=inspect.getdoc(part) or "",
                        exported=False,
                        arity="nullary",
                    )
                    self.describe(doc, part)
                    self.categories[name] = doc

    def invert_edges(self) -> None:
        for name, doc in self.categories.items():
            for super_name in doc.supers:
                parent = self.categories.get(super_name)
                if parent is not None and name not in parent.subcategories:
                    parent.subcategories.append(name)
        for doc in self.categories.values():
            doc.subcategories.sort()

    # ---- functors -----------------------------------------------------

    @staticmethod
    def name_functor(value: Functor) -> str:
        r"""A functor's own repr, or its class name when it has not got one."""
        text = repr(value)
        return type(value).__name__ if text.startswith("<") else text

    def collect_functors(self) -> None:
        for name in self.names:
            value = getattr(self.session, name)
            if not (inspect.isclass(value) and issubclass(value, (Functor, Adjunction))):
                continue
            kind = "ADJUNCTION" if issubclass(value, Adjunction) else "FUNCTOR"
            doc = FunctorDoc(
                name=name,
                kind=kind,
                subsystem=subsystem_of(value.__module__),
                source=source_of(value),
                doc=inspect.getdoc(value) or "",
                exported=True,
                init_signature=signature_of(value, constructor=True),
                methods=self.members(value),
            )
            self.functors.append(doc)
            probe = self.probe_arguments(value)
            if probe is None:
                doc.problem = "parameterized by data the survey does not choose for you"
                continue
            built: Functor | Adjunction | str = self.build(value, probe[0])
            if isinstance(built, str):
                doc.problem = built
            elif isinstance(built, Adjunction):
                doc.domain = self.name_functor(built.left_adjoint())
                doc.codomain = self.name_functor(built.right_adjoint())
            else:
                doc.domain = repr(built.domain())
                doc.codomain = repr(built.codomain())
        self.functors.sort(key=lambda f: f.name)

    # ---- catalogues and specimens --------------------------------------

    INVARIANTS: Final = ("rank", "signature_pair", "discriminant", "degree", "order")

    @staticmethod
    def ask(value: Specimen, question: str, show: Callable[[object], str] = str) -> str | None:
        r"""Ask a specimen one question and render the answer.

        ``None`` when the specimen does not answer to it at all.  A specimen
        that *has* the operation and raises gets the exception name back: a
        named lattice that cannot state its own rank is a finding, and hiding
        it would leave a blank cell that reads as "not applicable".
        """
        method = getattr(value, question, None)
        if not callable(method):
            return None
        try:
            return show(method())
        except Exception as error:  # noqa: BLE001 - a specimen may raise anything
            return f"!{type(error).__name__}"

    @staticmethod
    def category_of(value: Specimen) -> Category | None:
        r"""Where a specimen says it lives, or nothing when it will not say."""
        try:
            return value.category()
        except Exception:  # noqa: BLE001 - an object that will not place itself is unplaced
            return None

    def invariants_of(self, value: Specimen) -> dict[str, str]:
        asked: list[tuple[str, Callable[[object], str]]] = [
            *((name, str) for name in self.INVARIANTS),
            ("domain", repr),
            ("codomain", repr),
        ]
        answers = ((name, self.ask(value, name, show)) for name, show in asked)
        return {name: answer for name, answer in answers if answer is not None}

    def collect_catalogues(self) -> None:
        for name in self.names:
            value = getattr(self.session, name)
            if not inspect.isclass(value) or issubclass(value, (Category, Functor)):
                continue
            entries = [(key, getattr(value, key)) for key in vars(value) if not key.startswith("_") and isinstance(getattr(value, key), (Parent, Element))]
            if len(entries) < 2:
                continue
            doc = CatalogueDoc(
                name=name,
                subsystem=subsystem_of(value.__module__),
                source=source_of(value),
                doc=inspect.getdoc(value) or "",
            )
            for key, specimen in entries:
                doc.specimens.append(
                    SpecimenDoc(
                        name=key,
                        repr_text=repr(specimen),
                        invariants=self.invariants_of(specimen),
                        category=str(self.category_of(specimen) or ""),
                    )
                )
            self.catalogues.append(doc)
        self.catalogues.sort(key=lambda c: c.name)

    # ---- everything else -----------------------------------------------

    def collect_plain(self) -> None:

        catalogued = {c.name for c in self.catalogues}
        for name in self.names:
            value = getattr(self.session, name)
            if name in catalogued or inspect.ismodule(value):
                continue
            if inspect.isclass(value) and issubclass(value, (Category, Functor, Adjunction)):
                continue
            if inspect.isclass(value):
                if issubclass(value, Morphism):
                    kind = "MORPHISM"
                elif Element in value.__mro__:
                    kind = "ELEMENT"
                elif issubclass(value, Parent):
                    kind = "OBJECT"
                else:
                    kind = "CLASS"
                self.plain.append(
                    PlainDoc(
                        name=name,
                        kind=kind,
                        subsystem=subsystem_of(value.__module__),
                        source=source_of(value),
                        doc=inspect.getdoc(value) or "",
                        signature=signature_of(value, constructor=True),
                        methods=self.members(value),
                    )
                )
            elif isinstance(value, Parent):
                self.plain.append(
                    PlainDoc(
                        name=name,
                        kind="LIVE OBJECT",
                        subsystem=subsystem_of(type(value).__module__),
                        source=source_of(type(value)),
                        doc=summarize(inspect.getdoc(value)),
                        signature=repr(value),
                        category=str(self.category_of(value) or ""),
                    )
                )
            elif callable(value):
                # A `cached_function` keeps the real function on `.f`; a callable
                # instance has no code of its own, so its class carries the source.
                target = getattr(value, "f", value)
                located = target if inspect.isroutine(target) else type(target)
                self.plain.append(
                    PlainDoc(
                        name=name,
                        kind="FUNCTION",
                        subsystem=subsystem_of(located.__module__),
                        source=source_of(located),
                        doc=inspect.getdoc(target) or "",
                        signature=signature_of(target),
                    )
                )
        self.plain.sort(key=lambda p: p.name)

    def attach_specimens(self) -> None:
        r"""Name, on each category, objects a session can actually reach."""
        live: list[tuple[str, Specimen]] = [(p.name, getattr(self.session, p.name)) for p in self.plain if p.kind == "LIVE OBJECT"]
        for catalogue in self.catalogues:
            namespace = getattr(self.session, catalogue.name)
            live.extend((f"{catalogue.name}.{s.name}", getattr(namespace, s.name)) for s in catalogue.specimens)
        for label, specimen in live:
            category = self.category_of(specimen)
            if category is None:
                continue
            for part in self.expand(category):
                name, _ = self.family_of(part)
                doc = self.categories.get(name)
                if doc is None or label in doc.specimens:
                    continue
                doc.specimen_total += 1
                if len(doc.specimens) < SPECIMEN_CAP:
                    doc.specimens.append(label)

    def run(self) -> Survey:
        self.collect_categories()
        self.collect_functors()
        self.collect_catalogues()
        self.collect_plain()
        self.attach_specimens()
        return self


class Report:
    r"""Markdown for the surveyed session."""

    def __init__(self, survey: Survey) -> None:
        self.survey = survey
        self.lines: list[str] = []

    def out(self, *lines: str) -> None:
        self.lines.extend(lines)

    # ---- helpers -------------------------------------------------------

    def link(self, name: str) -> str:
        doc = self.survey.categories.get(name)
        if doc is None:
            return f"`{name}`"
        return f"[`{doc.display}`](#{anchor('cat-' + name)})"

    def depth(self, doc: CategoryDoc) -> int:
        return len(doc.ancestry)

    def chapters(self) -> list[tuple[str, str, str]]:
        present = {d.subsystem for d in self.survey.categories.values()}
        present |= {f.subsystem for f in self.survey.functors}
        present |= {c.subsystem for c in self.survey.catalogues}
        present |= {p.subsystem for p in self.survey.plain}
        return [row for row in SUBSYSTEM_ORDER if row[0] in present]

    # ---- sections ------------------------------------------------------

    def orientation(self) -> None:
        functors = [f for f in self.survey.functors if f.kind == "FUNCTOR"]
        adjunctions = [f for f in self.survey.functors if f.kind == "ADJUNCTION"]
        counts = {
            "categories": len(self.survey.categories),
            "instantiated": sum(1 for d in self.survey.categories.values() if d.instance_repr),
            "functors": len(functors),
            "placed": sum(1 for f in functors if f.domain),
            "adjunctions": len(adjunctions),
            "operations": sum(d.own_total for d in self.survey.categories.values()),
        }
        self.out(
            "# The preamble, surveyed from a live session",
            "",
            "This is the reference for what a session can build on: which categories",
            "exist, what sits above and below each one, which operations an object of",
            "each category answers to and where each operation is defined, which",
            "functors move between categories, and which named specimens are on hand.",
            "",
            "Everything here was read from a running session, not from the source text.",
            "`super_categories` is a method, the base ring is an argument, and the",
            "operations an object carries are assembled by Sage from the category graph",
            "at runtime -- so a category's place and its methods are facts only a live",
            "object can report.",
            "",
            "```python",
            "from dzack_research.preamble.all import *",
            "```",
            "",
            "## How to read an entry",
            "",
            "A category parameterized by a ring is written `C(R)` and was probed at",
            "`R = ZZ`; the relations hold for the parameter generally, and the",
            "**probed as** line shows the object the survey actually held.",
            "",
            "**Above** and **below** are the direct edges of the poset: `super_categories`",
            "and its inverse. **Refines** is the transitive closure upward.",
            "",
            "**Operations introduced here** are the ones this category *defines*.  Every",
            "operation is written out once, at the category that owns it; a descendant",
            "lists it under **inherited** with a link, because that is where placement",
            "lives.  So an object of `C` answers to the union of the operations",
            "introduced by `C` and by everything in its ancestry.",
            "",
            "Operations are split by what they act on: **objects** of the category,",
            "**elements** of those objects, and **morphisms** between them.",
            "",
            "A category the survey could not build, or an operation whose signature",
            "would not resolve, is recorded with the error rather than dropped.",
            "",
            "The same survey is serialized to `docs/preamble-graph.json`, which carries",
            "every operation name, so a question this prose cannot index is a `jq` away:",
            "",
            "```bash",
            "# which category owns discriminant_group?",
            "jq -r '.categories | to_entries[]",
            '      | select(.value.operations.objects[]?.name == "discriminant_group")',
            "      | .key' docs/preamble-graph.json",
            "```",
            "",
            "The poset is drawn in `docs/preamble-graph.html` (pan and zoom), from",
            "`docs/preamble-graph.dot`.",
            "",
            "| | |",
            "| :--- | ---: |",
            f"| categories in the poset | {counts['categories']} |",
            f"| of those, built and interrogated | {counts['instantiated']} |",
            f"| operations, each written once at its owner | {counts['operations']} |",
            f"| functors | {counts['functors']}, {counts['placed']} of them with a domain and codomain resolved here |",
            f"| adjunctions | {counts['adjunctions']} |",
            "",
        )

    def graph_section(self) -> None:
        roots = sorted(d.name for d in self.survey.categories.values() if not d.supers and d.instance_repr)
        self.out(
            "## The category poset",
            "",
            "An edge points from a category to a category it refines.  In the drawing the",
            "arrow runs leftward and the chapters are boxed, so reading left is forgetting",
            "structure and reading right is adding it; a dashed node is a category Sage",
            "provides rather than one the preamble owns.",
            "",
            "The top of the poset, refining nothing further: " + ", ".join(self.link(name) for name in roots) + ".",
            "",
            "The whole graph at once is [`preamble-graph.html`](preamble-graph.html);"
            " the diagrams below are its restriction to one chapter, together with any"
            " immediate supercategory that lies outside it.",
            "",
        )

    def mermaid(self, subsystem: str) -> None:
        inside = [d for d in self.survey.categories.values() if d.subsystem == subsystem and d.instance_repr]
        if not inside:
            return
        names = {d.name for d in inside}
        border = {s for d in inside for s in d.supers if s not in names}
        if len(names) + len(border) > MERMAID_NODE_CAP:
            self.out(
                f"This chapter holds {len(names)} categories, too many to draw legibly here; see [the interactive graph](preamble-graph.html).",
                "",
            )
            return
        # RL for the same reason the whole-graph DOT uses it: bottom-to-top puts
        # a chapter's forty categories in one flat row.
        self.out("```mermaid", "graph RL")
        for doc in sorted(inside, key=lambda d: d.name):
            self.out(f'  {doc.name}["{doc.display}"]')
        for name in sorted(border):
            other = self.survey.categories.get(name)
            label = other.display if other else name
            self.out(f'  {name}("{label}")')
        for doc in sorted(inside, key=lambda d: d.name):
            for super_name in sorted(set(doc.supers)):
                self.out(f"  {doc.name} --> {super_name}")
        if border:
            # No space after the colon: mermaid ends the attribute value there,
            # and the dashes silently do not appear.
            self.out("  classDef outside stroke-dasharray:6 4,fill:#f8fafc;")
            self.out(f"  class {','.join(sorted(border))} outside;")
        self.out("```", "")

    def functor_index(self) -> None:
        resolved = [f for f in self.survey.functors if f.kind == "FUNCTOR" and f.domain]
        adjunctions = [f for f in self.survey.functors if f.kind == "ADJUNCTION" and f.domain]
        self.out(
            "## Getting from one category to another",
            "",
            "Every functor the survey could build, indexed by where it starts.  This is",
            "the table to read when the object you have and the object you want are in",
            "different categories.",
            "",
            "| from | functor | to |",
            "| :--- | :--- | :--- |",
        )
        for functor in sorted(resolved, key=lambda f: (f.domain, f.name)):
            target = f"[`{functor.name}`](#{anchor('fun-' + functor.name)})"
            self.out(f"| {functor.domain} | {target} | {functor.codomain} |")
        self.out("")
        if adjunctions:
            self.out(
                "### Adjunctions",
                "",
                "| adjunction | left adjoint | | right adjoint |",
                "| :--- | :--- | :---: | :--- |",
            )
            for adjunction in sorted(adjunctions, key=lambda f: f.name):
                target = f"[`{adjunction.name}`](#{anchor('fun-' + adjunction.name)})"
                self.out(f"| {target} | {adjunction.domain} | ⊣ | {adjunction.codomain} |")
            self.out("")
        unresolved = [f for f in self.survey.functors if not f.domain]
        if unresolved:
            self.out(
                f"{len(unresolved)} further functors take data the survey does not choose"
                " for you (a ring map, a group, a subgroup pair); they are written out in"
                " their chapters with the arguments they want.",
                "",
            )

    def catalogue_section(self) -> None:
        if not self.survey.catalogues:
            return
        self.out(
            "## Named specimens",
            "",
            "Objects the catalogue has already built, with the invariants the survey could compute from them.",
            "",
        )
        for catalogue in self.survey.catalogues:
            self.out(f"### `{catalogue.name}` {{#{anchor(catalogue.name)}}}", "")
            if catalogue.doc:
                self.out(summarize(catalogue.doc), "")
            self.out(f"`{catalogue.source}`", "")
            keys: list[str] = []
            for specimen in catalogue.specimens:
                for key in specimen.invariants:
                    if key not in keys:
                        keys.append(key)
            header = ["name", "is"] + keys + ["category"]
            self.out(
                "| " + " | ".join(header) + " |",
                "| " + " | ".join([":---"] * len(header)) + " |",
            )
            for specimen in catalogue.specimens:
                cells = [f"`{catalogue.name}.{specimen.name}`", specimen.repr_text]
                cells += [specimen.invariants.get(key, "") for key in keys]
                cells.append(specimen.category)
                self.out("| " + " | ".join(cell.replace("|", "\\|") for cell in cells) + " |")
            self.out("")

    # ---- entries -------------------------------------------------------

    @staticmethod
    def prose(text: str) -> str:
        return text.replace("``", "`")

    def docstring(self, text: str) -> None:
        r"""The summary as prose, and the rest verbatim so examples survive."""
        if not text:
            return
        cleaned = inspect.cleandoc(text)
        head, _, rest = cleaned.partition("\n\n")
        self.out(self.prose(head.replace("\n", " ")), "")
        if rest.strip():
            self.out("```text", rest.rstrip(), "```", "")

    def category_entry(self, doc: CategoryDoc) -> None:
        self.out(f"#### `{doc.display}` {{#{anchor('cat-' + doc.name)}}}", "")
        self.docstring(doc.doc)
        facts = [f"- **defined at** `{doc.source}`" if doc.source else ""]
        if not doc.exported:
            facts.append("- **not exported**: reachable only as a supercategory")
        if doc.instance_repr:
            facts.append(f"- **probed as** `{doc.instance_repr}`")
        if doc.problem:
            facts.append(f"- **could not be built**: {doc.problem}")
        if doc.arity == "undeclared":
            facts.append(
                f"- **not placed**: `{doc.name}{doc.init_signature}` annotates no parameter,"
                " so the survey has nothing to construct it from (`LEX-12`)"
            )
        if doc.supers:
            facts.append("- **above** " + ", ".join(self.link(s) for s in sorted(set(doc.supers))))
        if doc.subcategories:
            facts.append("- **below** " + ", ".join(self.link(s) for s in doc.subcategories))
        if doc.ancestry:
            facts.append("- **refines**, transitively, in Sage's linearization order: " + " · ".join(self.link(a) for a in doc.ancestry))
        if doc.call_signature and doc.call_signature != "(...)":
            facts.append(f"- **build an object** `{doc.display}{doc.call_signature}`")
        if doc.specimens:
            shown = ", ".join(f"`{s}`" for s in doc.specimens)
            more = doc.specimen_total - len(doc.specimens)
            facts.append(f"- **specimens** {shown}" + (f", and {more} more" if more else ""))
        self.out(*[line for line in facts if line], "")

        if doc.own_methods:
            tally = ", ".join(f"{len(v)} on {k}" for k, v in doc.own_methods.items())
            self.out(f"**Operations introduced here** ({tally})", "")
            for label in ("objects", "elements", "morphisms"):
                methods = doc.own_methods.get(label)
                if not methods:
                    continue
                self.out(f"*on {label}*", "")
                self.out(*[m.render() for m in methods], "")
        elif doc.instance_repr:
            self.out(
                "Introduces no operations of its own: membership is the whole statement, and everything an object here answers to is inherited.",
                "",
            )
        if doc.inherited:
            self.out(
                "**Inherited operations**, defined where they are owned:",
                "",
                "| from | objects | elements | morphisms |",
                "| :--- | ---: | ---: | ---: |",
            )
            for owner, on_objects, on_elements, on_morphisms in doc.inherited:
                self.out(f"| {self.link(owner)} | {on_objects or ''} | {on_elements or ''} | {on_morphisms or ''} |")
            self.out("")

    def functor_entry(self, doc: FunctorDoc) -> None:
        self.out(f"#### `{doc.name}` {{#{anchor('fun-' + doc.name)}}}", "")
        self.docstring(doc.doc)
        facts = [f"- **defined at** `{doc.source}`" if doc.source else ""]
        if doc.domain and doc.kind == "FUNCTOR":
            facts.append(f"- **acts** {doc.domain} → {doc.codomain}")
        elif doc.domain:
            facts.append(f"- **adjunction** {doc.domain} ⊣ {doc.codomain}")
        facts.append(f"- **built by** `{doc.name}{doc.init_signature}`")
        if doc.problem:
            facts.append(f"- **not resolved here**: {doc.problem}")
        self.out(*[line for line in facts if line], "")
        if doc.methods:
            self.out("**Operations**", "", *[m.render() for m in doc.methods], "")

    def plain_entry(self, doc: PlainDoc) -> None:
        self.out(f"#### `{doc.name}` <sub>{doc.kind}</sub>", "")
        self.docstring(doc.doc)
        facts = [f"- **defined at** `{doc.source}`" if doc.source else ""]
        if doc.kind == "LIVE OBJECT":
            facts.append(f"- **is** {doc.signature}")
            facts.append(f"- **in** {doc.category}")
        elif doc.signature:
            facts.append(f"- **built by** `{doc.name}{doc.signature}`")
        self.out(*[line for line in facts if line], "")
        if doc.methods:
            self.out("**Operations**", "", *[m.render() for m in doc.methods], "")

    def chapter(self, key: str, title: str, scope: str) -> None:
        self.out(f"## {title}", "", f"> {scope}", "")
        self.mermaid(key)

        categories = [d for d in self.survey.categories.values() if d.subsystem == key]
        # One list, ordered by how much structure a category carries.  A category
        # the survey could not construct has no depth to sort on and sorts last;
        # its entry says why, and says nothing once the cause is gone.
        poset = sorted(categories, key=lambda d: (d.instance_repr == "", self.depth(d), d.name))
        functors = [f for f in self.survey.functors if f.subsystem == key]
        symbols = [p for p in self.survey.plain if p.subsystem == key]

        if poset:
            self.out(
                "### Categories",
                "",
                "Ordered by depth: the least structured first.",
                "",
            )
            for doc in poset:
                self.category_entry(doc)
        if functors:
            self.out("### Functors and adjunctions", "")
            for functor in functors:
                self.functor_entry(functor)
        for kind, heading in (
            ("OBJECT", "Objects"),
            ("ELEMENT", "Elements"),
            ("MORPHISM", "Morphisms and homsets"),
            ("LIVE OBJECT", "Objects the session already holds"),
            ("CLASS", "Supporting classes"),
            ("FUNCTION", "Functions"),
        ):
            group = [p for p in symbols if p.kind == kind]
            if not group:
                continue
            self.out(f"### {heading}", "")
            for symbol in group:
                self.plain_entry(symbol)

    def locator(self) -> None:
        rows: list[tuple[str, str, str]] = []
        for doc in self.survey.categories.values():
            if doc.exported:
                rows.append((doc.name, "category", f"#{anchor('cat-' + doc.name)}"))
        for functor in self.survey.functors:
            rows.append(
                (
                    functor.name,
                    functor.kind.lower(),
                    f"#{anchor('fun-' + functor.name)}",
                )
            )
        for catalogue in self.survey.catalogues:
            rows.append((catalogue.name, "catalogue", f"#{anchor(catalogue.name)}"))
        for symbol in self.survey.plain:
            rows.append((symbol.name, symbol.kind.lower(), ""))
        self.out(
            "## Every exported name",
            "",
            "| name | kind | chapter |",
            "| :--- | :--- | :--- |",
        )
        chapter_of: dict[str, str] = {}
        for doc in self.survey.categories.values():
            chapter_of[doc.name] = doc.subsystem
        for functor in self.survey.functors:
            chapter_of[functor.name] = functor.subsystem
        for catalogue in self.survey.catalogues:
            chapter_of[catalogue.name] = catalogue.subsystem
        for symbol in self.survey.plain:
            chapter_of[symbol.name] = symbol.subsystem
        for name, kind, target in sorted(set(rows)):
            title = SUBSYSTEM_TITLES.get(chapter_of.get(name, ""), ("", ""))[0]
            shown = f"[`{name}`]({target})" if target else f"`{name}`"
            self.out(f"| {shown} | {kind} | {title} |")
        self.out("")

    def render(self) -> str:
        self.orientation()
        self.graph_section()
        self.functor_index()
        self.catalogue_section()
        for key, title, scope in self.chapters():
            self.chapter(key, title, scope)
        self.locator()
        return "\n".join(self.lines).rstrip() + "\n"


PALETTE: Final = [
    "#dbeafe",
    "#dcfce7",
    "#fef3c7",
    "#fae8ff",
    "#ffe4e6",
    "#e0e7ff",
    "#ccfbf1",
    "#fee2e2",
    "#ede9fe",
    "#ecfccb",
    "#cffafe",
    "#fce7f3",
    "#f1f5f9",
    "#fef9c3",
    "#e2e8f0",
    "#d1fae5",
    "#ffedd5",
]


def graph_json(survey: Survey) -> str:
    categories = {
        doc.name: {
            "display": doc.display,
            "subsystem": doc.subsystem,
            "source": doc.source,
            "summary": summarize(doc.doc),
            "owned": survey.is_owned(doc.module),
            "exported": doc.exported,
            "arity": doc.arity,
            "probed_as": doc.instance_repr,
            "supers": sorted(set(doc.supers)),
            "subcategories": doc.subcategories,
            "ancestry": doc.ancestry,
            "operations": {
                label: [
                    {
                        "name": m.name,
                        "signature": m.signature,
                        "summary": m.summary,
                        "mark": m.mark,
                    }
                    for m in methods
                ]
                for label, methods in doc.own_methods.items()
            },
            "inherits": [
                {
                    "from": owner,
                    "objects": on_objects,
                    "elements": on_elements,
                    "morphisms": on_morphisms,
                }
                for owner, on_objects, on_elements, on_morphisms in doc.inherited
            ],
            "specimens": doc.specimens,
            "problem": doc.problem,
        }
        for doc in sorted(survey.categories.values(), key=lambda d: d.name)
    }
    functors = [
        {
            "name": f.name,
            "kind": f.kind,
            "subsystem": f.subsystem,
            "source": f.source,
            "summary": summarize(f.doc),
            "domain": f.domain,
            "codomain": f.codomain,
            "problem": f.problem,
        }
        for f in survey.functors
    ]
    specimens = [
        {
            "catalogue": catalogue.name,
            "name": specimen.name,
            "is": specimen.repr_text,
            "category": specimen.category,
            **specimen.invariants,
        }
        for catalogue in survey.catalogues
        for specimen in catalogue.specimens
    ]
    return json.dumps(
        {"categories": categories, "functors": functors, "specimens": specimens},
        indent=2,
        sort_keys=False,
    )


def graph_dot(survey: Survey) -> str:
    drawn = {name: doc for name, doc in survey.categories.items() if doc.instance_repr}
    order = [key for key, _, _ in SUBSYSTEM_ORDER]
    colour = {key: PALETTE[index % len(PALETTE)] for index, key in enumerate(order)}
    lines = [
        "// Generated by dzack_research.utilities.megadoc from a live session.",
        "// An edge points from a category to a category it refines.",
        "digraph preamble {",
        # Ranking right-to-left keeps a 200-node poset near A-series proportions.
        # Stacking it bottom-to-top instead lays the chapters side by side and
        # the drawing comes out ten times wider than it is tall.
        "  rankdir=RL;",
        '  graph [bgcolor="#ffffff", fontname="Helvetica", fontsize=14, nodesep=0.25, ranksep=0.6, pad=0.2];',
        '  node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, margin="0.10,0.06"];',
        '  edge [color="#94a3b8", arrowsize=0.6];',
    ]
    grouped: dict[str, list[CategoryDoc]] = defaultdict(list)
    for doc in drawn.values():
        grouped[doc.subsystem].append(doc)
    for index, key in enumerate(order):
        members = grouped.get(key)
        if not members:
            continue
        title, _ = SUBSYSTEM_TITLES[key]
        lines.append(f"  subgraph cluster_{index} {{")
        lines.append(f'    label="{html.escape(title)}"; fontsize=13; color="#cbd5e1"; style=rounded;')
        for doc in sorted(members, key=lambda d: d.name):
            shape = "" if survey.is_owned(doc.module) else ', style="rounded,filled,dashed"'
            lines.append(f'    {json.dumps(doc.name)} [label="{doc.display}", fillcolor="{colour[key]}"{shape}];')
        lines.append("  }")
    for doc in sorted(drawn.values(), key=lambda d: d.name):
        for super_name in sorted(set(doc.supers)):
            if super_name in drawn:
                lines.append(f"  {json.dumps(doc.name)} -> {json.dumps(super_name)};")
    lines.append("}")
    return "\n".join(lines) + "\n"


def render_interactive(dot_path: Path, out_path: Path) -> bool:
    r"""Rasterize the DOT into the repository's pan-and-zoom viewer."""
    if shutil.which("dot") is None or not GRAPH_TEMPLATE.exists():
        return False
    svg = subprocess.run(["dot", "-Tsvg", str(dot_path)], capture_output=True, text=True, check=True).stdout
    template = GRAPH_TEMPLATE.read_text()
    assert template.count("%SVG%") == 1
    out_path.write_text(template.replace("%SVG%", svg[svg.find("<svg") :]))
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-o", "--output", default="docs/preamble-megadoc.md")
    arguments = parser.parse_args(argv)

    survey = Survey().run()
    markdown = Path(arguments.output)
    markdown.parent.mkdir(parents=True, exist_ok=True)
    markdown.write_text(Report(survey).render())

    stem = markdown.with_name("preamble-graph")
    json_path = stem.with_suffix(".json")
    dot_path = stem.with_suffix(".dot")
    json_path.write_text(graph_json(survey) + "\n")
    dot_path.write_text(graph_dot(survey))
    drawn = render_interactive(dot_path, stem.with_suffix(".html"))

    print(f"{markdown} ({markdown.stat().st_size // 1024} KiB)")
    print(f"{json_path} ({len(survey.categories)} categories, {len(survey.functors)} functors)")
    print(f"{dot_path}" + (f" -> {stem.with_suffix('.html')}" if drawn else "  (no `dot`; HTML skipped)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
