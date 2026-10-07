"""Geometric objects use their Hodge numbers and the lattice corpus together."""

from pathlib import Path

import frontmatter
import pytest
from pydantic import ValidationError

from latticedb import checks, site
from latticedb.geometric import ProjectiveComplexVariety
from latticedb.graphs import WeightedGraph

ROOT = Path(__file__).parent.parent


def test_k3_hodge_diamond_and_lattice_link_are_published(tmp_path: Path) -> None:
    lattice_directory = tmp_path / "lattices"
    lattice_directory.mkdir()
    for tag in (
            "0001",
            "0002",
            "0013",
        "0016",
        "0151",
        "027E",
        "027Z",
        "0283",
    ):
        (lattice_directory / f"{tag}.md").symlink_to(
            ROOT / "lattices" / f"{tag}.md"
        )
    for name in ("families.yaml", "retired-tags.yaml", "geometric-bibliography.bib"):
        (tmp_path / name).symlink_to(ROOT / name)
    (tmp_path / "theory").symlink_to(ROOT / "theory", target_is_directory=True)
    geometric = tmp_path / "geometric-objects"
    geometric.mkdir()
    for slug in ("k3-surface", "k3-hilbert-2", "kummer-2"):
        (geometric / f"{slug}.md").symlink_to(
            ROOT / "geometric-objects" / f"{slug}.md"
        )
    families = tmp_path / "geometric-families"
    families.mkdir()
    for slug in ("k3-hilbert", "generalized-kummer"):
        (families / f"{slug}.md").symlink_to(
            ROOT / "geometric-families" / f"{slug}.md"
        )
    target = tmp_path / "site"
    site.build(tmp_path, target)
    html = (target / "geometric-objects" / "k3-surface.html").read_text()
    assert 'href="../tag/027E.html"' in html
    assert 'href="../tag/027E.html">U^3 + E8(-1)^2</a>' in html
    assert "H<sup>2</sup>(X; ℤ)/tors" in html
    assert '<div class="hodge-row">' in html
    assert "<span>1</span><span>20</span><span>1</span>" in html
    assert (
        'href="../geometric-objects/k3-surface.html"'
        in (target / "tag" / "027E.html").read_text()
    )
    assert "Huybrechts" in html
    assert (
        'href="./geometric-families/k3-hilbert.html"'
        in (target / "geometric-objects.html").read_text()
    )
    hilbert = (target / "geometric-objects" / "k3-hilbert-2.html").read_text()
    assert 'href="../tag/027Z.html"' in hilbert
    assert 'href="../geometric-families/k3-hilbert.html"' in hilbert
    assert (
        "<span>1</span><span>21</span><span>232</span><span>21</span><span>1</span>"
        in hilbert
    )
    kummer = (target / "geometric-objects" / "kummer-2.html").read_text()
    assert 'href="../tag/0283.html"' in kummer
    assert (
        "<span>1</span><span>5</span><span>96</span><span>5</span><span>1</span>"
        in kummer
    )


def test_symmetric_spaces_and_analytic_variety_are_published(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    for tag in ("0001", "0002", "0011", "0013", "0016", "0151"):
        (tmp_path / "lattices" / f"{tag}.md").symlink_to(
            ROOT / "lattices" / f"{tag}.md"
        )
    (tmp_path / "families.yaml").symlink_to(ROOT / "families.yaml")
    (tmp_path / "retired-tags.yaml").symlink_to(ROOT / "retired-tags.yaml")
    (tmp_path / "geometric-bibliography.bib").symlink_to(
        ROOT / "geometric-bibliography.bib"
    )
    (tmp_path / "theory").symlink_to(ROOT / "theory", target_is_directory=True)
    (tmp_path / "geometric-objects").mkdir()
    (tmp_path / "graphs").symlink_to(ROOT / "graphs", target_is_directory=True)
    for slug in (
        "complex-projective-plane",
        "complex-projective-plane-analytic",
        "complex-hyperbolic-2-space",
        "three-sphere",
        "real-hyperbolic-3-space",
        "complex-quadric-q-5",
        "bdi-25-compact",
        "bdi-25-noncompact",
        "complex-cayley-plane",
        "eiii-compact",
        "eiii-noncompact",
    ):
        (tmp_path / "geometric-objects" / f"{slug}.md").symlink_to(
            ROOT / "geometric-objects" / f"{slug}.md"
        )
    target = tmp_path / "site"
    site.build(tmp_path, target)
    algebraic_plane = (
        target / "geometric-objects" / "complex-projective-plane.html"
    ).read_text()
    analytic_plane = (
        target / "geometric-objects" / "complex-projective-plane-analytic.html"
    ).read_text()
    complex_ball = (
        target / "geometric-objects" / "complex-hyperbolic-2-space.html"
    ).read_text()
    real_hyperbolic = (
        target / "geometric-objects" / "real-hyperbolic-3-space.html"
    ).read_text()
    assert (
        'href="../geometric-objects/complex-projective-plane-analytic.html"'
        in algebraic_plane
    )
    assert 'href="../geometric-objects/complex-projective-plane.html"' in analytic_plane
    assert (
        'href="../geometric-objects/complex-projective-plane-analytic.html"'
        in complex_ball
    )
    assert 'href="../geometric-objects/three-sphere.html"' in real_hyperbolic
    assert 'href="../graphs/restricted-a1.html"' in real_hyperbolic
    assert 'href="../graphs/a2-su21-satake.html"' in complex_ball
    graph = (target / "graphs" / "a2-su21-satake.html").read_text()
    assert "Coxeter, Dynkin, simply laced, Satake" in graph
    assert 'href="../geometric-objects/complex-hyperbolic-2-space.html"' in graph
    vinberg = (target / "graphs" / "hyperbolic-triangle-2-3-infinity.html").read_text()
    assert "rational Coxeter–Vinberg" in vinberg
    assert '<h2 id="hodge-diamond">' not in complex_ball
    quadric = (target / "geometric-objects" / "complex-quadric-q-5.html").read_text()
    bdi = (target / "geometric-objects" / "bdi-25-compact.html").read_text()
    exceptional = (target / "geometric-objects" / "eiii-noncompact.html").read_text()
    assert 'href="../geometric-objects/bdi-25-compact.html"' in quadric
    assert 'href="../geometric-objects/complex-quadric-q-5.html"' in bdi
    assert 'href="../geometric-objects/eiii-compact.html"' in exceptional


def test_graph_cards_derive_distinct_datum_from_shared_coxeter_order() -> None:
    def card(slug: str) -> WeightedGraph:
        return WeightedGraph.model_validate(
            frontmatter.load(ROOT / "graphs" / f"{slug}.md").metadata
        )

    b2 = card("b2-root-diagram")
    c2 = card("c2-root-diagram")
    assert b2.properties() == c2.properties() == ("Coxeter", "Dynkin")
    assert b2.cartan_matrix() != c2.cartan_matrix()
    assert card("a2-su21-satake").properties() == (
        "Coxeter",
        "Dynkin",
        "simply laced",
        "Satake",
    )
    assert card("hyperbolic-triangle-2-3-infinity").properties() == (
        "Coxeter",
        "rational Coxeter–Vinberg",
    )
    invalid_satake = card("a2-su21-satake").model_dump()
    invalid_satake["vertices"][0]["weight"]["satake"] = "black"
    invalid_satake["edges"] = invalid_satake["edges"][:1]
    assert not WeightedGraph.model_validate(invalid_satake).is_satake()
    arbitrary = WeightedGraph.model_validate(
        {
            "slug": "arbitrary",
            "name": "Weighted directed multigraph",
            "vertices": [
                {"id": "a", "weight": {"colour": ["red", 2]}},
                {"id": "b", "weight": "blue"},
            ],
            "edges": [
                {
                    "id": "loop",
                    "source": "a",
                    "target": "a",
                    "relation": "map",
                    "directed": True,
                    "weight": [1, "x"],
                },
                {
                    "id": "first",
                    "source": "a",
                    "target": "b",
                    "relation": "map",
                    "directed": True,
                },
                {
                    "id": "second",
                    "source": "a",
                    "target": "b",
                    "relation": "map",
                    "directed": True,
                },
            ],
        }
    )
    assert len(arbitrary.edges) == 3
    assert arbitrary.properties() == ()


def test_cohomology_link_must_match_the_stored_betti_number(tmp_path: Path) -> None:
    lattices = tmp_path / "lattices"
    lattices.mkdir()
    (lattices / "0016.md").symlink_to(ROOT / "lattices" / "0016.md")
    (tmp_path / "families.yaml").symlink_to(ROOT / "families.yaml")
    (tmp_path / "retired-tags.yaml").symlink_to(ROOT / "retired-tags.yaml")
    source = frontmatter.load(str(ROOT / "geometric-objects" / "k3-surface.md"))
    source.metadata["cohomology_lattices"][0]["tag"] = "0016"
    geometric = tmp_path / "geometric-objects"
    geometric.mkdir()
    (geometric / "k3-surface.md").write_text(frontmatter.dumps(source))
    assert any(
        "Betti number 22, but lattice 0016 has rank 2" in problem
        for problem in checks.report(tmp_path)
    )


def test_k3_card_reads_its_transcribed_topology_and_hodge_numbers() -> None:
    source = frontmatter.load(str(ROOT / "geometric-objects" / "k3-surface.md"))
    record = ProjectiveComplexVariety.model_validate(source.metadata)
    assert record.betti_numbers == (1, 0, 22, 0, 1)
    assert record.euler_characteristic == 24
    assert record.hodge_number(1, 1) == 20
    assert record.hodge_number(1, 0) == 0

    source.metadata["betti_numbers"] = [1, 0, 22, 0]
    with pytest.raises(ValidationError, match="b_0 through b_"):
        ProjectiveComplexVariety.model_validate(source.metadata)
