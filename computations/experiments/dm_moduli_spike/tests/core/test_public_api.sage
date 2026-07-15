r"""Tier-4: public API surface for geometric ontology + Γ."""

from __future__ import annotations

import importlib

import dm_moduli_spike as spike
from dm_moduli_spike import M_gn, StableGraphCategory, spec
from sage.rings.rational_field import QQ

_BANNED_PUBLIC_NAMES = (
    "DMCompactificationModel",
    "ModuliFactor",
    "DMStratum",
    "StableGraphTypes",
    "StableGraphType",
    "StableGraphStratification",
    "StableGraphStratificationEnumerator",
    "AutomorphismAction",
    "StableGraphRecord",
    "DMStratification",
    "DeligneMumfordModuliStack",
    "DeligneMumfordModuliStackOver",
    "DualGraphType",
    "BoundaryStack",
    "StratifiedStack",
    "StratifiedVariety",
    "ModuliMorphism",
    "CoarseModuliMap",
    "SchemeStackAdapter",
    "Curve",
    "NormalizationMorphism",
    "StratifiedSpace",
)

_BANNED_MODULES = (
    "dm_moduli_spike.objects.graph_types",
    "dm_moduli_spike.objects.curve_types",
    "dm_moduli_spike.objects.model",
    "dm_moduli_spike.objects.stratification",
    "dm_moduli_spike.moduli.stack",
    "dm_moduli_spike.stratification",
    "dm_moduli_spike.stratification.indexing",
    "dm_moduli_spike.stratification.stratified",
    "dm_moduli_spike.geometry.morphisms",
    "dm_moduli_spike.moduli.coarse",
    "dm_moduli_spike.moduli.problems",
)


def test_moduli_problems_are_distinct_classes_not_stable_flag():
    from dm_moduli_spike.moduli.instances import (
        SmoothPointedCurveModuliProblem,
        StablePointedCurveModuliProblem,
    )

    XS = M_gn(0, 4, base=spec(QQ))
    XSbar = spike.Mbar_gn(0, 4, base=spec(QQ))
    assert isinstance(XS.moduli_problem(), SmoothPointedCurveModuliProblem)
    assert isinstance(XSbar.moduli_problem(), StablePointedCurveModuliProblem)
    assert not XS.moduli_problem().is_stable()
    assert XSbar.moduli_problem().is_stable()


def test_curve_families_are_distinct_classes_not_stable_flag():
    from dm_moduli_spike.curves.families import PointedCurveFamily, StablePointedCurveFamily

    XS = M_gn(1, 1, base=spec(QQ))
    XSbar = spike.Mbar_gn(1, 1, base=spec(QQ))
    smooth_fam = XS(spec(QQ)).an_element()
    stable_fam = XSbar(spec(QQ)).an_element()
    assert isinstance(smooth_fam, PointedCurveFamily)
    assert not isinstance(smooth_fam, StablePointedCurveFamily)
    assert isinstance(stable_fam, StablePointedCurveFamily)
    assert not smooth_fam.is_stable()
    assert stable_fam.is_stable()


def test_public_all_includes_moduli_and_gamma():
    for name in ["M_gn", "Mbar_gn", "StableGraphCategory", "ModuliStacks", "Stacks", "spec"]:
        assert name in spike.__all__
    for name in _BANNED_PUBLIC_NAMES:
        assert name not in spike.__all__
    for name in [
        "LocallyClosedSubstacks",
        "OpenSubstack",
        "ClosedSubstack",
        "LocallyClosedSubstack",
        "StableDualGraph",
        "ClutchingMorphism",
        "CurveFamilies",
        "PointedCurveFamilies",
        "StablePointedCurveFamilies",
        "StratifiedSpaces",
        "StratifiedStacks",
        "StableGraphs",
        "StableGraph",
    ]:
        assert name in spike.__all__


_SUBMODULES_TO_PROBE = (
    "dm_moduli_spike",
    "dm_moduli_spike.objects",
    "dm_moduli_spike.objects.stable_graphs",
    "dm_moduli_spike.moduli",
    "dm_moduli_spike.moduli.instances",
    "dm_moduli_spike.geometry",
)


def test_banned_names_unimportable_from_package_surface():
    r"""Banned dual-ontology names must fail importlib/getattr, not only ``__all__``."""
    for name in _BANNED_PUBLIC_NAMES:
        assert not hasattr(spike, name), f"banned name {name!r} still exposed on package"
        try:
            getattr(spike, name)
        except AttributeError:
            pass
        else:
            raise AssertionError(f"getattr(spike, {name!r}) should fail")
        for modname in _SUBMODULES_TO_PROBE:
            mod = importlib.import_module(modname)
            assert not hasattr(mod, name), f"banned name {name!r} still on {modname}"
            try:
                getattr(mod, name)
            except AttributeError:
                pass
            else:
                raise AssertionError(f"getattr({modname}, {name!r}) should fail")


def test_banned_shim_modules_unimportable():
    for modname in _BANNED_MODULES:
        try:
            importlib.import_module(modname)
        except ModuleNotFoundError:
            continue
        raise AssertionError(f"banned module {modname!r} is still importable")


def test_stable_graph_has_no_public_record_method():
    from dm_moduli_spike.objects.stable_graphs import StableGraphs

    G = StableGraphs(1, (1,)).smooth()
    assert not hasattr(G, "record") or not callable(getattr(G, "record", None))
    assert not hasattr(type(G), "record")
    assert "canonical_representative" not in dir(G)
    assert not hasattr(type(G), "canonical_representative")


def test_gamma_still_public():
    Gamma = StableGraphCategory(1, 1)
    assert Gamma.specialization_poset().cardinality() == 2


def test_m_gn_public():
    XS = M_gn(0, 4, base=spec(QQ))
    assert XS.dimension() == 1
