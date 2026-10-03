"""Geometric objects use their Hodge numbers and the lattice corpus together."""

from pathlib import Path

import frontmatter
import pytest
from latticedb import corpus, site
from latticedb.geometric import ProjectiveComplexVariety
from pydantic import ValidationError

ROOT = Path(__file__).parent.parent


def test_k3_hodge_diamond_and_lattice_link_are_published(tmp_path: Path) -> None:
    target = tmp_path / "site"
    site.build(ROOT, target)
    html = (target / "geometric-objects" / "k3-surface.html").read_text()
    assert 'href="../tag/027E.html"' in html
    assert 'href="../tag/027E.html">U^3 + E8(-1)^2</a>' in html
    assert "H<sup>2</sup>(X; ℤ)/tors" in html
    assert '<div class="hodge-row">' in html
    assert "<span>1</span><span>20</span><span>1</span>" in html
    assert 'href="../geometric-objects/k3-surface.html"' in (target / "tag" / "027E.html").read_text()
    assert "Huybrechts" in html
    assert 'href="./geometric-families/k3-hilbert.html"' in (target / "geometric-objects.html").read_text()
    hilbert = (target / "geometric-objects" / "k3-hilbert-2.html").read_text()
    assert 'href="../tag/027Z.html"' in hilbert
    assert 'href="../geometric-families/k3-hilbert.html"' in hilbert
    assert "<span>1</span><span>21</span><span>232</span><span>21</span><span>1</span>" in hilbert
    kummer = (target / "geometric-objects" / "kummer-2.html").read_text()
    assert 'href="../tag/0283.html"' in kummer
    assert "<span>1</span><span>5</span><span>96</span><span>5</span><span>1</span>" in kummer


def test_symmetric_spaces_and_analytic_variety_are_published(tmp_path: Path) -> None:
    (tmp_path / "lattices").mkdir()
    for tag in ("0001", "0002", "0006", "0011", "0013", "0016", "0151"):
        (tmp_path / "lattices" / f"{tag}.md").symlink_to(ROOT / "lattices" / f"{tag}.md")
    (tmp_path / "families.yaml").symlink_to(ROOT / "families.yaml")
    (tmp_path / "retired-tags.yaml").symlink_to(ROOT / "retired-tags.yaml")
    (tmp_path / "geometric-bibliography.bib").symlink_to(ROOT / "geometric-bibliography.bib")
    (tmp_path / "theory").symlink_to(ROOT / "theory", target_is_directory=True)
    (tmp_path / "geometric-objects").mkdir()
    for slug in (
        "complex-projective-plane",
        "complex-projective-plane-analytic",
        "complex-hyperbolic-2-space",
        "three-sphere",
        "real-hyperbolic-3-space",
    ):
        (tmp_path / "geometric-objects" / f"{slug}.md").symlink_to(ROOT / "geometric-objects" / f"{slug}.md")
    target = tmp_path / "site"
    site.build(tmp_path, target)
    algebraic_plane = (target / "geometric-objects" / "complex-projective-plane.html").read_text()
    analytic_plane = (target / "geometric-objects" / "complex-projective-plane-analytic.html").read_text()
    complex_ball = (target / "geometric-objects" / "complex-hyperbolic-2-space.html").read_text()
    real_hyperbolic = (target / "geometric-objects" / "real-hyperbolic-3-space.html").read_text()
    assert 'href="../geometric-objects/complex-projective-plane-analytic.html"' in algebraic_plane
    assert 'href="../geometric-objects/complex-projective-plane.html"' in analytic_plane
    assert 'href="../geometric-objects/complex-projective-plane-analytic.html"' in complex_ball
    assert 'href="../geometric-objects/three-sphere.html"' in real_hyperbolic
    assert "Hodge diamond" not in complex_ball


def test_cohomology_link_must_match_the_hodge_betti_number(tmp_path: Path) -> None:
    (tmp_path / "lattices").symlink_to(ROOT / "lattices", target_is_directory=True)
    (tmp_path / "families.yaml").symlink_to(ROOT / "families.yaml")
    (tmp_path / "retired-tags.yaml").symlink_to(ROOT / "retired-tags.yaml")
    source = frontmatter.load(str(ROOT / "geometric-objects" / "k3-surface.md"))
    source.metadata["cohomology_lattices"][0]["tag"] = "0016"
    geometric = tmp_path / "geometric-objects"
    geometric.mkdir()
    (geometric / "k3-surface.md").write_text(frontmatter.dumps(source))
    with pytest.raises(corpus.CorpusInvalid, match="Betti number 22, but lattice 0016 has rank 2"):
        corpus.load(tmp_path)


def test_hodge_series_determines_symmetry_and_chern_number() -> None:
    source = frontmatter.load(str(ROOT / "geometric-objects" / "k3-surface.md"))
    record = ProjectiveComplexVariety.model_validate(source.metadata)
    assert record.betti_number(2) == 22
    assert record.euler_characteristic() == 24
    assert record.hodge_number(1, 1) == 20

    source.metadata["symmetry_group"] = "V4"
    with pytest.raises(ValidationError, match="declared symmetry group"):
        ProjectiveComplexVariety.model_validate(source.metadata)

    source.metadata["symmetry_group"] = "D4"
    source.metadata["chern_numbers"][0]["value"] = 25
    with pytest.raises(ValidationError, match="top Chern number"):
        ProjectiveComplexVariety.model_validate(source.metadata)
