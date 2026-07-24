"""Build Sage ``Category`` / ``CategoryWithAxiom`` stubs from the DOT graph."""

from __future__ import annotations

from typing import Any, cast

from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.categories.category_with_axiom import (
    CategoryWithAxiom,
    CategoryWithAxiom_over_base_ring,
)
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ

from .axioms import register_graph_axioms
from .dot_parse import DotGraph, parse_dot
from .slugs import axiom_method_name, class_slug, is_parameterized, short_name

register_graph_axioms()

_HOST_ALIASES: dict[str, str] = {
    "∫Bil_R(R)": "∫Bil_R(W)",
    "∫Bil": "∫Bil_R(W)",
    "∫Quad": "∫Quad_R(W)",
    "∫Herm": "∫Herm_R(W)",
    "∫Hom": "∫Hom_R(−,W)",
    "CatObject.Limits": "CatObject.Limits",
    "CatObject.Colimits": "CatObject.Colimits",
    "∫Bil.SkewSymmetric": "∫Bil.SkewSymmetric",
    "VectorSpaces": "VectorSpaces(K) = Modules.OverField",
    "Modules": "Modules(R)",
    "LeftModules": "LeftModules(R)",
    "RightModules": "RightModules(R)",
    "Bimodules": "Bimodules(R,S)",
    "Rings": "Rings",
    "Fields": "Fields",
    "Algebras": "Algebras(R)",
    "Groups": "Groups = Magmas.Associative.Unital.Inverse",
    "AdditiveGroups": "AdditiveGroups = Magmas.Additive.Associative.Unital.Inverse",
    "UnitalAlgebras": "UnitalAlgebras = Algebras.Associative.Unital",
    "AssociativeAlgebras": "AssociativeAlgebras = Algebras.Associative",
    "LieAlgebras": "LieAlgebras(R)",
    "Coalgebras": "Coalgebras(R)",
    "Bialgebras": "Bialgebras(R)",
    "HopfAlgebras": "HopfAlgebras(R)",
    "CliffordAlgebras": "CliffordAlgebras(R)",
    "SymmetricAlgebras": "SymmetricAlgebras(R)",
    "ExteriorAlgebras": "ExteriorAlgebras(R)",
    "TensorAlgebras": "TensorAlgebras(R)",
    "C∞Algebras": "C∞Algebras(R)",
    "G-Objects": "G-Objects(G)",
    "Sets": "Sets",
    "Magmas": "Magmas",
    "Domains": "Domains = Rings.Domain",
    "Cat": "Cat_1",
    "Cat_1": "Cat_1",
    "Cat_2": "Cat_2",
    "(2,1)-Categories": "Cat_2",
    "Graphs": "Graphs",
    "Schemes": "Schemes(S)",
    "Manifolds": "Manifolds",
    # Lat.* axiom nodes in the DOT sit on Lat_R
    "Lat": "Lat_R = ∫Bil_R(R).Symmetric.GenericallyNondegenerate",
    "Lat_R": "Lat_R = ∫Bil_R(R).Symmetric.GenericallyNondegenerate",
}

# Sage forked AdditiveMagmas + AdditiveAssociative names. Stub Magmas uses a
# flat axiom set (Additive / Multiplicative / Associative / …); no remapping.
_ADDITIVE_AXIOM_MAP: dict[str, str] = {}

# Vertices that look like Host.Axiom but are independent category families.
# Magmas.Additive is Magmas+Additive (one-tower), not a sibling root under Sets.
_PLAIN_SIBLING_ROOTS: frozenset[str] = frozenset()

# Domain ladder: Domains need not be commutative (parent = Rings).
_DOMAIN_LADDER: tuple[tuple[str, str, str], ...] = (
    ("Domains = Rings.Domain", "Rings", "Domain"),
    ("IntegralDomains = Domains.Commutative", "Domains = Rings.Domain", "Commutative"),
    (
        "GCDDomains = Rings.Commutative.GCDDomain",
        "IntegralDomains = Domains.Commutative",
        "GCDDomain",
    ),
    (
        "UFDs = Rings.Commutative.UFD",
        "GCDDomains = Rings.Commutative.GCDDomain",
        "UFD",
    ),
    ("PIDs = Rings.Commutative.PID", "UFDs = Rings.Commutative.UFD", "PID"),
    (
        "EuclideanDomains = Rings.Commutative.Euclidean",
        "PIDs = Rings.Commutative.PID",
        "Euclidean",
    ),
)


class CategoryTreeFactory:
    """Materialize the DOT graph as Sage category classes and instances."""

    def __init__(self, graph: DotGraph | None = None) -> None:
        self.graph = graph or parse_dot()
        self.classes: dict[str, type] = {}
        self._axiom_classes: dict[tuple[str, str], type] = {}
        self._built = False
        self._solid_parents_map = self._compute_solid_parents()

    def _compute_solid_parents(self) -> dict[str, tuple[str, ...]]:
        parents: dict[str, list[str]] = {}
        for edge in self.graph.solid_edges:
            parents.setdefault(edge.src, []).append(edge.tgt)
        return {node: tuple(dict.fromkeys(ps)) for node, ps in parents.items()}

    def _axiom_category_nodes(self) -> set[str]:
        """Solid node ids that are Host.Axiom refinements, not independent roots."""
        nodes: set[str] = set()
        axiom_names = {axiom_method_name(lab) for lab in self.graph.axiom_labels.values()}
        for edge in self.graph.axiom_edges:
            label = self.graph.axiom_labels.get(edge.src, edge.src.rsplit(".", 1)[-1])
            ax = axiom_method_name(label)
            host = short_name(edge.tgt)
            for cand in (f"{host}.{ax}", f"{edge.tgt}.{ax}", edge.src):
                if cand in _PLAIN_SIBLING_ROOTS:
                    continue
                nodes.add(cand)
        # Sets.Finite, Lat.Definite, Cat.Thin, … Magmas.Additive is Magmas+Additive
        candidates = set(self.graph.solid_nodes) | set(self.graph.axiom_labels)
        for node in candidates:
            if node in _PLAIN_SIBLING_ROOTS:
                continue
            if " = " in node or node.count(".") != 1:
                continue
            _host, ax = node.split(".", 1)
            if axiom_method_name(ax) in axiom_names or ax in axiom_names:
                nodes.add(node)
            elif _host in _HOST_ALIASES or _host in self.graph.solid_nodes:
                nodes.add(node)
        return nodes

    def build(self) -> None:
        if self._built:
            return
        axiom_nodes = self._axiom_category_nodes()
        # 1. plain categories (non-named-join, non-axiom-refinement solid nodes)
        plain = sorted(
            (n for n in self.graph.solid_nodes if n not in self.graph.named_joins and n not in axiom_nodes),
            key=str,
        )
        pending = set(plain)
        while pending:
            progress = False
            for node in sorted(pending, key=str):
                deps = [d for d in self._solid_parents_map.get(node, ()) if d not in self.graph.named_joins and d not in axiom_nodes]
                if any(d in pending for d in deps):
                    continue
                self._make_plain_category(node, self._solid_parents_map.get(node, ()))
                pending.remove(node)
                progress = True
            if not progress:
                for node in sorted(pending, key=str):
                    self._make_plain_category(node, self._solid_parents_map.get(node, ()))
                break

        # Sibling roots need their own axiom suite (Associative/Unital/…) before joins.
        for sibling in sorted(_PLAIN_SIBLING_ROOTS):
            if sibling not in self.classes:
                continue
            for axiom_name in ("Associative", "Unital", "Inverse", "Commutative"):
                self._ensure_axiom_class(sibling, axiom_name)

        # 2. axioms on hosts
        self._install_host_axioms()

        # 3. named joins: wire host axioms, then materialize as DOT stubs
        # (dependency order: host named-joins before joins that refine them)
        ladder_names = {row[0] for row in _DOMAIN_LADDER}
        for join_name in self._named_join_build_order():
            if join_name in ladder_names:
                continue  # wired in step 4 as a true refinement chain
            self._materialize_named_join(join_name)

        # 4. domain ladder: each rung axioms the previous rung (not CommRings)
        self._wire_domain_ladder()

        # Host.Axiom solid nodes → axiom classes (Lat.Definite → Lat_R.Definite, …)
        for node in sorted(axiom_nodes, key=str):
            if "." not in node or " = " in node:
                continue
            host, ax = node.split(".", 1)
            try:
                cls = self._ensure_axiom_class(host, axiom_method_name(ax))
            except Exception:
                continue
            self.classes[node] = cls
            # also index under Lat_R.Definite etc.
            resolved = self._resolve_host(host)
            self.classes.setdefault(f"{short_name(resolved)}.{axiom_method_name(ax)}", cls)

        # 5. remaining host axioms (Sets/Magmas/Schemes/…); skip clobbering
        self._install_host_axioms()
        self._built = True

    def _wire_domain_ladder(self) -> None:
        if "CommRings = Rings.Commutative" not in self.classes:
            self._ensure_axiom_chain("Rings", ("Commutative",))
            self._make_dot_category_stub(
                "CommRings = Rings.Commutative",
                self._axioms_for_join("Rings", ("Commutative",)),
                (),
            )
        for join_name, parent_join, axiom_name in _DOMAIN_LADDER:
            parent_key = parent_join if parent_join in self.classes else self._resolve_host(parent_join)
            self._ensure_axiom_class(parent_key, axiom_name)
            parent_cls = self.classes[parent_key]
            parent_axioms = set(getattr(parent_cls, "_axiom_set", ()))
            parent_axioms.add(axiom_method_name(axiom_name))
            self._make_dot_category_stub(
                join_name,
                frozenset(parent_axioms),
                self._solid_parents_map.get(join_name, ()),
            )

    def _named_join_build_order(self) -> list[str]:
        """Topological order: materialize host named-joins before dependents."""
        joins = dict(self.graph.named_joins)
        short_to_join = {short_name(j): j for j in joins}
        order: list[str] = []
        seen: set[str] = set()
        visiting: set[str] = set()

        def visit(join_name: str) -> None:
            if join_name in seen:
                return
            if join_name in visiting:
                return  # cycle; break
            visiting.add(join_name)
            host, _path = joins[join_name]
            host_short = short_name(host)
            dep = short_to_join.get(host_short)
            if dep is not None and dep != join_name:
                visit(dep)
            # Also: path prefix UnitalAlgebras.Commutative depends on UnitalAlgebras join
            # (already via host). Multi-segment hosts like Algebras.Associative are not joins.
            visiting.discard(join_name)
            seen.add(join_name)
            order.append(join_name)

        for name in sorted(joins):
            visit(name)
        return order

    def _materialize_named_join(self, join_name: str) -> None:
        if join_name in self.classes:
            return
        host, path = self.graph.named_joins[join_name]
        host_res = self._resolve_host(host)
        if host_res in self.graph.named_joins and host_res not in self.classes:
            self._materialize_named_join(host_res)
        self._ensure_axiom_chain(host, path)
        axioms = self._axioms_for_join(host, path)
        self._make_dot_category_stub(
            join_name,
            axioms,
            self._solid_parents_map.get(join_name, ()),
        )

    def _collect_axioms_from_path(
        self,
        host: str,
        path: tuple[str, ...],
    ) -> set[str]:
        """Flat Magmas axioms: path labels are used as-is (no Additive* rename)."""
        axioms: set[str] = set()
        for axiom_name in path:
            axioms.add(axiom_method_name(axiom_name))
        return axioms

    def _axioms_for_join(self, host: str, path: tuple[str, ...]) -> frozenset[str]:
        axioms = self._collect_axioms_from_path(host, path)
        resolved = self._resolve_host(host)
        if resolved in self.classes:
            host_cls = self.classes[resolved]
            parent_axioms = getattr(host_cls, "_axiom_set", None)
            if parent_axioms is not None:
                axioms |= set(parent_axioms)
        if resolved == "Magmas.Additive" or resolved.startswith("Magmas.Additive."):
            axioms.add("Additive")
        if resolved == "Magmas.Multiplicative" or resolved.startswith("Magmas.Multiplicative."):
            axioms.add("Multiplicative")
        if path and path[0] == "Additive":
            axioms.add("Additive")
        if path and path[0] == "Multiplicative":
            axioms.add("Multiplicative")
        return frozenset(axioms)

    def _make_dot_category_stub(
        self,
        node: str,
        axioms: frozenset[str],
        parent_nodes: tuple[str, ...],
    ) -> type:
        if node in self.classes:
            return self.classes[node]

        factory = self
        parents = parent_nodes
        axiom_set = axioms

        def super_categories(self: Any) -> list[Category]:
            out: list[Category] = []
            seen: set[int] = set()
            for parent in parents:
                if (
                    parent not in _PLAIN_SIBLING_ROOTS
                    and parent.count(".") == 1
                    and " = " not in parent
                    and parent.split(".", 1)[0]
                    in {
                        "Sets",
                        "Schemes",
                        "Schemes(S)",
                        "Magmas",
                        "Cat",
                        "Cat_1",
                        "CatObject",
                        "Lat",
                    }
                ):
                    host, ax = parent.split(".", 1)
                    cat = factory.axiom_instance(host, ax)
                else:
                    # A parameterized parent is taken over this category's own base:
                    # ``VectorSpaces(QQ)`` sits over ``Modules(QQ)``, not over the
                    # parent vertex's default ``Modules(ZZ)``.
                    own_base = getattr(self, "base_ring", None)
                    cat = factory.instance(
                        parent,
                        base=own_base() if callable(own_base) and is_parameterized(parent) else None,
                    )
                key = id(cat)
                if key not in seen:
                    seen.add(key)
                    out.append(cat)
            return out

        def axioms_method(self: Any) -> frozenset[str]:
            return axiom_set

        slug = class_slug(node)
        base_cls: type = Category_over_base_ring if is_parameterized(short_name(node)) or is_parameterized(node) else Category
        ns: dict[str, Any] = {
            "super_categories": super_categories,
            "axioms": axioms_method,
            "ParentMethods": type("ParentMethods", (), {}),
            "ElementMethods": type("ElementMethods", (), {}),
            "MorphismMethods": type("MorphismMethods", (), {}),
        }
        cls = type(slug, (base_cls,), ns)
        setattr(cls, "_axiom_set", axiom_set)
        self.classes[node] = cls
        self.classes[short_name(node)] = cls
        return cls

    def _finalize_category(self, cat: Category, vertex: str) -> Category:
        """Tag the vertex id and strip axiom-only ``super_categories`` edges."""
        import types

        if vertex in self._axiom_category_nodes() and not self._solid_parents_map.get(vertex):
            object.__setattr__(cat, "super_categories", types.MethodType(lambda self: [], cat))
        setattr(cat, "_dot_vertex", vertex)
        return cat

    def _resolve_host(self, host: str) -> str:
        if host in self.classes:
            return host
        if host in _HOST_ALIASES:
            return _HOST_ALIASES[host]
        if short_name(host) in self.classes:
            return short_name(host)
        # Named-join short names (Groups, UnitalAlgebras, …) are hosts of further joins
        for join in self.graph.named_joins:
            if short_name(join) == host or short_name(join) == short_name(host):
                return join
        return host

    def _make_plain_category(self, node: str, parent_nodes: tuple[str, ...]) -> type:
        if node in self.classes:
            return self.classes[node]

        slug = class_slug(node)
        factory = self
        parents = parent_nodes

        if is_parameterized(node) and node not in {
            "ChainComplexes(C)",
            "CochainComplexes(C)",
            "G-Objects(G)",
        }:

            def parameterized_super_categories(self: Any) -> list[Category]:
                return [factory.instance(p) for p in parents]

            ns: dict[str, Any] = {
                "super_categories": parameterized_super_categories,
                "ParentMethods": type("ParentMethods", (), {}),
                "ElementMethods": type("ElementMethods", (), {}),
                "MorphismMethods": type("MorphismMethods", (), {}),
            }
            cls = type(slug, (Category_over_base_ring,), ns)
            self.classes[node] = cls
            self.classes[short_name(node)] = cls
            return cls

        def plain_super_categories(self: Any) -> list[Category]:
            return [factory.instance(p) for p in parents]

        ns = {
            "super_categories": plain_super_categories,
            "ParentMethods": type("ParentMethods", (), {}),
            "ElementMethods": type("ElementMethods", (), {}),
            "MorphismMethods": type("MorphismMethods", (), {}),
        }
        if node in _PLAIN_SIBLING_ROOTS:
            axiom_set = frozenset({"Additive"})

            def plain_axioms(self: Any) -> frozenset[str]:
                return axiom_set

            ns["axioms"] = plain_axioms
        cls = type(slug, (Category,), ns)
        self.classes[node] = cls
        self.classes[short_name(node)] = cls
        if node in _PLAIN_SIBLING_ROOTS:
            setattr(cls, "_axiom_set", frozenset({"Additive"}))
        return cls

    def _install_host_axioms(self) -> None:
        by_host: dict[str, list[str]] = {}
        for edge in self.graph.axiom_edges:
            label = self.graph.axiom_labels.get(edge.src, edge.src.rsplit(".", 1)[-1])
            by_host.setdefault(edge.tgt, []).append(axiom_method_name(label))
        for host, names in by_host.items():
            resolved = self._resolve_host(host)
            if resolved not in self.classes:
                continue
            for axiom_name in sorted(set(names)):
                self._ensure_axiom_class(resolved, axiom_name)

    def _host_class(self, host: str) -> type:
        resolved = self._resolve_host(host)
        if resolved not in self.classes:
            self._make_plain_category(resolved, self._solid_parents_map.get(resolved, ()))
        return self.classes[resolved]

    def _ensure_axiom_class(self, host: str, axiom_name: str) -> type:
        resolved = self._resolve_host(host)
        key = (resolved, axiom_name)
        if key in self._axiom_classes:
            return self._axiom_classes[key]

        host_cls = self._host_class(resolved)
        over_ring = issubclass(host_cls, Category_over_base_ring)
        base_ax = CategoryWithAxiom_over_base_ring if over_ring else CategoryWithAxiom
        slug = f"{class_slug(resolved)}_{axiom_name}"

        ax_cls = type(
            slug,
            (base_ax,),
            {
                "_base_category_class_and_axiom": (host_cls, axiom_name),
                "ParentMethods": type("ParentMethods", (), {}),
                "ElementMethods": type("ElementMethods", (), {}),
                "MorphismMethods": type("MorphismMethods", (), {}),
                "SubcategoryMethods": type("SubcategoryMethods", (), {}),
            },
        )
        # Do not clobber an axiom class already installed on this host
        existing_attr = getattr(host_cls, axiom_name, None)
        if existing_attr is None or existing_attr is ax_cls:
            setattr(host_cls, axiom_name, ax_cls)
        self._axiom_classes[key] = ax_cls
        path_key = f"{short_name(resolved)}.{axiom_name}"
        self.classes.setdefault(path_key, ax_cls)

        # Bind a host-local SubcategoryMethods entry that returns *this* axiom
        # class. Plain ``_with_axiom`` silently prefers an ancestor host's class
        # for the same axiom name (Magmas.Commutative vs Rings.Commutative).
        def _method(self: Any, _ax_cls: type = ax_cls, _over_ring: bool = over_ring) -> Category:
            refined: Category
            if _over_ring:
                refined = cast(Category, _ax_cls(self.base_ring()))
            else:
                refined = cast(Category, _ax_cls())
            if self is refined or self == refined:
                return refined
            return Category.join([self, refined])

        _method.__name__ = axiom_name
        aliases = {axiom_name: _method}
        # DOT walks Magmas.Additive.Associative; Sage class is AdditiveAssociative
        for dot_name, additive_name in _ADDITIVE_AXIOM_MAP.items():
            if axiom_name == additive_name:
                aliases[dot_name] = _method
        existing = getattr(host_cls, "SubcategoryMethods", None)
        if existing is None:
            setattr(host_cls, "SubcategoryMethods", type("SubcategoryMethods", (), aliases))
        else:
            for name, method in aliases.items():
                if not hasattr(existing, name):
                    setattr(existing, name, method)

        return ax_cls

    def _in_additive_spine(self, host: str) -> bool:
        h = self._resolve_host(host)
        return h == "Magmas.Additive" or h.startswith("Magmas.Additive.")

    def _spine_axiom(self, host: str, axiom_name: str) -> str:
        return axiom_method_name(axiom_name)

    def _ensure_axiom_chain(self, host: str, path: tuple[str, ...]) -> type:
        """Walk Magmas axioms under a shared flat registry (no Additive* rename)."""
        current = self._resolve_host(host)
        cls = self._host_class(current)
        for axiom_name in path:
            raw = axiom_method_name(axiom_name)
            cls = self._ensure_axiom_class(current, raw)
            current = f"{short_name(current)}.{raw}"
            self.classes.setdefault(current, cls)
        return cls

    def _default_base(self, node: str) -> object:
        # ``OverField`` is the refinement that fixes the base, so it decides the
        # ring wherever it appears — including joins whose short name is not in the
        # table below.
        if "OverField" in node:
            return QQ
        # Named joins carry their parameter (``VectorSpaces(K) = Modules.OverField``
        # → ``VectorSpaces(K)``); the table is keyed by the unparameterized name.
        name = short_name(node).split("(", 1)[0].strip()
        if name in {
            "VectorSpaces",
            "Varieties",
            "Curves",
            "Surfaces",
            "Hypersurfaces",
            "CompleteIntersections",
            "ToricVarieties",
        }:
            return QQ
        return ZZ

    def instance(self, node: str, base: object | None = None) -> Category:
        """Materialize ``node``; ``base`` overrides the vertex's default base ring.

        Comparing a parameterized edge such as ``VectorSpaces(K) → Modules(R)``
        requires both endpoints at the same parameter — instantiating each at its
        own default compares vector spaces over one ring with modules over another.
        """
        self.build()
        canonical = node
        if node in _HOST_ALIASES:
            node = _HOST_ALIASES[node]
        if node in self.graph.named_joins or short_name(node) in {short_name(j) for j in self.graph.named_joins}:
            key = node if node in self.classes else next(j for j in self.graph.named_joins if short_name(j) == short_name(node))
            cls = self.classes[key]
            cat: Category
            if issubclass(cls, Category_over_base_ring):
                # The base comes from the join vertex, not its host: the host of
                # ``VectorSpaces(K) = Modules.OverField`` is ``Modules(R)``, whose
                # default base is ZZ, which would build the vector-space stub over
                # the integers.
                cat = cast(Category, cls(self._default_base(key) if base is None else base))
            else:
                cat = cast(Category, cls())
            return self._finalize_category(cat, key)

        key = node if node in self.classes else short_name(node)
        if key not in self.classes and key in _HOST_ALIASES:
            key = _HOST_ALIASES[key]
        if key not in self.classes:
            raise KeyError(f"unknown category node {node!r}")
        cls = self.classes[key]
        cat_out: Category
        if issubclass(cls, Category_over_base_ring) or issubclass(cls, CategoryWithAxiom_over_base_ring):
            cat_out = cast(
                Category,
                cls(self._default_base(node if is_parameterized(node) else ("∫Bil_R(W)" if key.startswith("Lat") or "Bil" in key else key)) if base is None else base),
            )
        else:
            cat_out = cast(Category, cls())
        vertex = canonical if canonical in self.classes else key
        return self._finalize_category(cat_out, vertex)

    def axiom_instance(self, host: str, axiom_label: str) -> Category:
        self.build()
        ax = axiom_method_name(axiom_label)
        host_cat = self.instance(host)
        method = getattr(host_cat, ax, None)
        if method is None:
            resolved = self._resolve_host(host)
            key = (resolved, ax)
            if key in self._axiom_classes:
                ax_cls = self._axiom_classes[key]
                if is_parameterized(resolved):
                    base = cast(Category_over_base_ring, host_cat).base_ring()
                    return cast(Category, ax_cls(base))
                return cast(Category, ax_cls())
            raise AttributeError(f"{host_cat} has no axiom {ax}")
        return cast(Category, method())


_FACTORY: CategoryTreeFactory | None = None


def reset_factory() -> None:
    """Drop cached factory (call after regenerating the presentation DOT)."""
    global _FACTORY
    _FACTORY = None


def factory() -> CategoryTreeFactory:
    global _FACTORY
    if _FACTORY is None:
        _FACTORY = CategoryTreeFactory()
        _FACTORY.build()
    return _FACTORY
