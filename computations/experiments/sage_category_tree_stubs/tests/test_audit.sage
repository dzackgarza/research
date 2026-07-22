"""Audits over the DOT graph: axiom catalog, inheritance, bedrock paths."""

from sage_category_tree_stubs.audit import (
    all_axioms,
    axiom_siting,
    axioms_attached,
    axioms_inherited,
    bedrock_vertices,
    category_axiom_view,
    declared_axiom_hosts,
    first_defined_hosts,
    hasse_nonminimal_edges,
    multi_hosted_axioms,
    paths_to_bedrock,
    solid_ancestors,
)
from sage_category_tree_stubs.dot_parse import parse_dot


def test_finite_declared_on_sets_and_not_on_countable_via_style_dotted() -> None:
    """``Sets.Finite → Sets.Countable`` is solid taxonomy, not a Finite declaration."""
    hosts = declared_axiom_hosts()["Finite"]
    assert "Sets" in hosts
    assert "Sets.Countable" not in hosts
    assert "CatObject" in hosts
    assert "Schemes(S)" in hosts
    assert "Sets" in hosts


def test_associative_siting_lists_lower_hosts_including_sets() -> None:
    siting = axiom_siting("Associative")
    assert siting.declared_hosts == ("Magmas",)
    assert siting.first_defined_on == ("Magmas",)
    assert "Sets" in siting.possible_lower_hosts
    assert "Magmas" not in siting.possible_lower_hosts
    assert any("Semigroups" in j for j in siting.named_joins)


def test_axioms_on_magmas_includes_flat_operation_axioms() -> None:
    view = category_axiom_view("Magmas")
    for ax in ("Associative", "Unital", "Commutative", "Additive", "Multiplicative"):
        assert ax in view.attached, view.attached


def test_rings_ancestry_reaches_sets() -> None:
    assert "Sets" in solid_ancestors("Rings")


def test_multi_hosted_finite_is_flagged() -> None:
    multi = multi_hosted_axioms()
    assert "Finite" in multi
    assert len(multi["Finite"]) >= 2


def test_finite_first_defined_is_catobject_structurally() -> None:
    """Sets/Schemes sit above CatObject, so CatObject is the first Finite host.

    Set-finite / scheme-finite (morphisms) remain distinct *meanings* of the
    shared name — flagged as redeclarations above CatObject.
    """
    first = first_defined_hosts("Finite")
    assert first == ("CatObject",)
    siting = axiom_siting("Finite")
    redecl = {h: below for h, below in siting.redeclared_on}
    assert "Sets" in redecl and "CatObject" in redecl["Sets"]
    assert "Schemes(S)" in redecl


def test_cat_spine_and_monoidal_tensor_dual() -> None:
    from sage_category_tree_stubs.factory import factory

    fac = factory()
    assert fac.instance("Cat_1").is_subcategory(fac.instance("Cat_2"))
    assert fac.instance("Cat_2").is_subcategory(fac.instance("Bicategories"))
    assert fac.instance("HomCategories").is_subcategory(fac.instance("CatObject"))
    tensor = fac.instance("TensorProducts = CatObject.Monoidal")
    assert "Monoidal" in tensor.axioms()
    assert fac.instance("DualObjects").is_subcategory(tensor)
    products = fac.axiom_instance("CatObject.Limits", "Products")
    assert "Products" in products.axioms()
    limits = fac.axiom_instance("CatObject", "Limits")
    assert "Limits" in limits.axioms()
    assert products.is_subcategory(limits)
    assert fac.instance("Subobjects").is_subcategory(fac.instance("Slices"))
    assert fac.instance("Quotients").is_subcategory(fac.instance("Coslices"))
    assert fac.instance("Subquotients").is_subcategory(fac.instance("Subobjects"))
    assert fac.instance("CatObject.Thin").is_subcategory(fac.instance("CatObject"))
    assert fac.instance("Homsets").is_subcategory(fac.instance("HomCategories"))
    assert fac.instance("FunctorCategories").is_subcategory(fac.instance("HomCategories"))
    assert fac.instance("FibredCategories").is_subcategory(fac.instance("Cat_1"))
    assert not fac.instance("FibredCategories").is_subcategory(fac.instance("Groupoids"))
    mods = fac.instance("Modules(R)")
    assert fac.instance("LeftModules(R)").is_subcategory(mods)
    assert fac.instance("Bimodules(R)").is_subcategory(fac.instance("LeftModules(R)"))
    assert "OverField" in fac.axiom_instance("Modules(R)", "OverField").axioms()
    # Vector spaces are modules over the *same* field, not over the default ZZ base.
    vs = fac.instance("VectorSpaces(K) = Modules.OverField")
    assert vs.base_ring().is_field()
    assert vs.is_subcategory(fac.instance("Modules(R)", base=vs.base_ring()))
    assert not vs.is_subcategory(mods)
    assert fac.instance("Algebras(R)").is_subcategory(fac.instance("Modules(R)"))
    assert fac.instance("UnitalAlgebras = Algebras.Associative.Unital").is_subcategory(fac.instance("Algebras(R)"))
    assert fac.instance("DivisionRings = Rings.Division").is_subcategory(fac.instance("Rings"))
    assert fac.instance("Manifolds.Smooth").is_subcategory(fac.instance("Manifolds"))
    alt = fac.axiom_instance("∫Bil.SkewSymmetric", "Alternating")
    skew = fac.axiom_instance("∫Bil_R(W)", "SkewSymmetric")
    assert alt.is_subcategory(skew)


def test_all_axioms_nonempty_and_sorted() -> None:
    axioms = all_axioms()
    assert len(axioms) >= 20
    assert axioms == tuple(sorted(axioms))


def test_rings_attached_domain_and_inherits_magma_axioms() -> None:
    attached = axioms_attached("Rings")
    inherited = axioms_inherited("Rings")
    assert "Domain" in attached
    assert "Associative" in inherited
    assert "Finite" in inherited  # from Sets
    view = category_axiom_view("Rings")
    assert "Domain" in view.available
    assert "Associative" in view.available
    assert any(s.origin == "inherited" and s.via == "Magmas" for s in view.sources)


def test_named_join_semigroups_packages_associative() -> None:
    view = category_axiom_view("Semigroups = Magmas.Associative")
    assert "Associative" in view.named_join_axioms
    assert "Associative" in view.available


def test_bedrock_includes_catobject_and_paths_from_fields() -> None:
    beds = bedrock_vertices()
    assert "CatObject" in beds
    paths = paths_to_bedrock("Fields")
    assert paths
    assert all(p[-1] in beds for p in paths)
    assert all(p[0] == "Fields" or p[0].startswith("Fields") for p in paths)
    # at least one path reaches CatObject
    assert any(p[-1] == "CatObject" for p in paths)


def test_declared_axiom_edges_are_style_dotted_only() -> None:
    graph = parse_dot()
    assert graph.declared_axiom_edges
    for edge in graph.declared_axiom_edges:
        assert edge.style_dotted
    # Semantic DOT marks classifier legs with style=dotted; every declared
    # axiom attachment is therefore both dotted and style_dotted.
    assert all(e.dotted and e.style_dotted for e in graph.declared_axiom_edges)


def test_hasse_audit_returns_edges_or_empty() -> None:
    edges = hasse_nonminimal_edges()
    assert isinstance(edges, tuple)
    for edge in edges:
        assert not edge.dotted
