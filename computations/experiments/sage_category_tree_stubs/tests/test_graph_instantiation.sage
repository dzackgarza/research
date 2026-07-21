r"""Every solid DOT node instantiates; solid and axiom edges are recoverable."""

from sage_category_tree_stubs.dot_parse import parse_dot
from sage_category_tree_stubs.factory import _DOMAIN_LADDER, factory
from sage_category_tree_stubs.registry import instantiate_all
from sage_category_tree_stubs.slugs import axiom_method_name, short_name


def test_every_solid_node_and_named_join_instantiates() -> None:
    instances = instantiate_all()
    assert len(instances) > 0
    for node, category in instances.items():
        assert category is not None, node
        assert hasattr(category, "super_categories"), node
        cls = category.__class__
        # Method containers live on the generating class (may be a with_category wrapper)
        base = cls.__bases__[0] if cls.__name__.endswith("_with_category") else cls
        assert hasattr(base, "ParentMethods") or hasattr(cls, "ParentMethods"), node
        assert hasattr(base, "ElementMethods") or hasattr(cls, "ElementMethods"), node
        assert hasattr(base, "MorphismMethods") or hasattr(cls, "MorphismMethods"), node


def test_every_cluster_subtree_instantiates() -> None:
    from sage_category_tree_stubs.clusters import CLUSTERS

    for cluster in CLUSTERS:
        cats = cluster.categories()
        assert set(cats) == set(cluster.NODES)
        for node, category in cats.items():
            assert category is not None, f"{cluster.CLUSTER}:{node}"
        for (host, name), category in cluster.axiom_categories().items():
            assert category is not None, f"{cluster.CLUSTER}:{host}.{name}"
            ax = axiom_method_name(name)
            assert ax in category.axioms(), (host, name, category.axioms())


def test_solid_parent_edges_are_recoverable() -> None:
    fac = factory()
    failures = []
    for edge in fac.graph.solid_edges:
        child = fac.instance(edge.src)
        parent = fac.instance(edge.tgt)
        if not child.is_subcategory(parent):
            failures.append((edge.src, edge.tgt, child, parent))
    assert not failures, "\n".join(f"{a} -> {b}: {c} not subcategory of {p}" for a, b, c, p in failures[:25])


def test_axiom_edges_are_recoverable() -> None:
    fac = factory()
    for edge in fac.graph.axiom_edges:
        label = fac.graph.axiom_labels.get(edge.src, edge.src.rsplit(".", 1)[-1])
        refined = fac.axiom_instance(edge.tgt, label)
        ax = axiom_method_name(label)
        assert ax in refined.axioms(), (edge.src, edge.tgt, refined, refined.axioms())
        host = fac.instance(edge.tgt)
        assert refined.is_subcategory(host), (refined, host)


def test_named_joins_match_axiom_paths() -> None:
    fac = factory()
    ladder = {row[0]: row for row in _DOMAIN_LADDER}
    for join_name, (host, path) in fac.graph.named_joins.items():
        joined = fac.instance(join_name)
        if join_name in ladder:
            _join, parent_join, axiom_name = ladder[join_name]
            parent = fac.instance(parent_join)
            assert joined.is_subcategory(parent), (join_name, joined, parent)
            assert axiom_name in joined.axioms(), (join_name, joined.axioms())
            continue
        for ax in path:
            name = axiom_method_name(ax)
            assert name in joined.axioms(), (join_name, name, joined.axioms())
        # Magmas.Additive.* paths carry Additive as well as path axioms
        if (path and path[0] == "Additive") or short_name(host) == "Magmas.Additive":
            assert "Additive" in joined.axioms(), (join_name, joined.axioms())
        if (path and path[0] == "Multiplicative") or short_name(host) == "Magmas.Multiplicative":
            assert "Multiplicative" in joined.axioms(), (join_name, joined.axioms())


def test_cluster_nodes_cover_every_solid_dot_node() -> None:
    from sage_category_tree_stubs.clusters import CLUSTERS

    fac = factory()
    cluster_nodes = set()
    for cluster in CLUSTERS:
        cluster_nodes.update(cluster.NODES)
    missing = sorted(n for n in fac.graph.solid_nodes if n not in cluster_nodes)
    assert not missing, f"solid DOT nodes absent from cluster NODES: {missing}"


def test_host_axiom_solid_nodes_carry_their_axiom() -> None:
    """Sets.Finite, Lat.Definite, Cat.Thin, … must be real axiom categories."""
    fac = factory()
    for node in sorted(fac.graph.solid_nodes):
        if " = " in node or node.count(".") != 1:
            continue
        _host, ax = node.split(".", 1)
        category = fac.instance(node)
        assert axiom_method_name(ax) in category.axioms(), (node, category.axioms())


def test_dot_parser_sees_clusters() -> None:
    graph = parse_dot()
    assert "CatObject" in graph.solid_nodes
    assert "Magmas" in graph.solid_nodes
    assert "∫Hom_R(−,W)" in graph.solid_nodes
    assert any("DGAs =" in j for j in graph.named_joins)


def test_solid_multidigraph_matches_dot() -> None:
    from sage_category_tree_stubs.graph_compare import compare_solid_graphs

    result = compare_solid_graphs()
    assert result["vertices_equal"], "vertex sets differ"
    assert result["only_in_dot"] == set(), f"DOT-only solid edges: {result['only_in_dot']}"
    assert result["only_in_sage"] == set(), f"Sage-only solid edges: {result['only_in_sage']}"
    assert result["isomorphic"]


def test_axiom_multidigraph_matches_dot() -> None:
    from sage_category_tree_stubs.graph_compare import compare_axiom_graphs

    result = compare_axiom_graphs()
    assert result["only_in_dot"] == set(), f"DOT-only axiom edges: {result['only_in_dot']}"
    assert result["only_in_sage"] == set(), f"Sage-only axiom edges: {result['only_in_sage']}"
