r"""Load and install the preamble's category layer into the calling namespace.

``load()`` shares the caller's globals, so everything defined here -- the
categories, the ``install_*`` hooks they register, and the names the scripts
export -- lands in the namespace that loaded this file.

This sequence is order-sensitive, which is why it lives in one file:
``init.sage`` and every ``.sage`` test load it rather than each maintaining
its own copy.

Loading twice re-exports the *same* objects rather than re-running the scripts.
Categories are compared by identity, and the post-init hooks patch the Sage
classes once, process-wide: a second set of category classes would leave
objects refined into one ``DirectSumObjects`` and tested against another.

Callers that also want the named specimens continue with ``utilities.py``,
``catalogue.sage``, ``sterk.sage``, and ``Lattices.install(globals())``.
"""

import dzack_research as _dzack_research

_preamble_cache = getattr(_dzack_research, "_preamble_namespace", None)

if _preamble_cache is not None:
    globals().update(_preamble_cache)
else:
    _exported_before = set(globals())

    import sys as _sys
    from pathlib import Path as _Path

    _PREAMBLE = _Path(_dzack_research.__file__).resolve().parent / "preamble"
    _VENDOR_DIR = _PREAMBLE.parents[2] / "computations" / "vendor"
    from dzack_research.preamble.preparser import install_preparser

    install_preparser()

    def _vendor_import_roots(vendor_dir):
        r"""Return the vendor subtrees that expose importable modules or packages."""
        assert vendor_dir.is_dir(), f"vendor directory is missing: {vendor_dir}"
        roots = set((vendor_dir,))
        for path in vendor_dir.rglob("*"):
            if not path.is_dir():
                continue
            relative_parts = path.relative_to(vendor_dir).parts
            if any(
                part.startswith(".") or part == "__pycache__"
                for part in relative_parts
            ):
                continue
            children = tuple(path.iterdir())
            exposes_loose_module = any(
                child.is_file() and child.suffix == ".py" for child in children
            )
            exposes_package = any(
                child.is_dir() and (child / "__init__.py").is_file()
                for child in children
            )
            if exposes_loose_module or exposes_package:
                roots.add(path)
        return tuple(sorted(roots))

    for _vendor_root in _vendor_import_roots(_VENDOR_DIR):
        _vendor_entry = str(_vendor_root)
        if _vendor_entry not in _sys.path:
            _sys.path.append(_vendor_entry)

    load(str(_PREAMBLE / "refine.sage"))
    # Load the Sage-only implementation of ``refine``, but expose it as a
    # standard importable module path so category scripts that use normal
    # Python imports keep working during bootstrap.
    import types as _types

    if "dzack_research.preamble.refine" not in _sys.modules:
        _pre_refine_module = _types.ModuleType("dzack_research.preamble.refine")
        _pre_refine_module.__file__ = str(_PREAMBLE / "refine.sage")
        _pre_refine_module.__package__ = "dzack_research.preamble"
        _sys.modules["dzack_research.preamble.refine"] = _pre_refine_module
    else:
        _pre_refine_module = _sys.modules["dzack_research.preamble.refine"]

    for _export in ("hook_post_init", "hooked_classes", "refine"):
        _pre_refine_module.__dict__.setdefault(_export, globals()[_export])

    load(str(_PREAMBLE / "utilities.py"))
    load(str(_PREAMBLE / "categories/forms/gram_matrices.sage"))
    load(str(_PREAMBLE / "categories/sets/sets.sage"))
    load(str(_PREAMBLE / "categories/abstract_categories/slice_categories.sage"))
    load(str(_PREAMBLE / "categories/modules/pure/finitely_generated/finitely_generated_modules.sage"))
    load(str(_PREAMBLE / "categories/modules/pure/free_modules.sage"))
    load(str(_PREAMBLE / "categories/modules/framed/framed_modules.sage"))
    load(str(_PREAMBLE / "categories/modules/framed/finitely_generated/finitely_presented_modules.sage"))
    load(str(_PREAMBLE / "categories/modules/framed/framed_free_modules.sage"))
    load(str(_PREAMBLE / "categories/modules/framed/finitely_generated/finitely_generated_free_modules.sage"))

    load(str(_PREAMBLE / "categories/modules/direct_sum_objects.sage"))
    load(str(_PREAMBLE / "categories/modules/module_morphisms/module_morphisms.sage"))
    load(str(_PREAMBLE / "categories/modules/framed/formed/form_modules.sage"))
    load(str(_PREAMBLE / "categories/modules/pure/torsion_modules.sage"))
    load(str(_PREAMBLE / "categories/modules/framed/finitely_generated/finitely_presented_torsion_modules.sage"))
    load(str(_PREAMBLE / "categories/modules/group_modules/group_modules.sage"))
    load(str(_PREAMBLE / "categories/forms/forms.sage"))
    load(str(_PREAMBLE / "categories/group/groups.sage"))
    load(str(_PREAMBLE / "categories/group/finitely_presented_groups.sage"))
    load(str(_PREAMBLE / "categories/modules/framed/formed/integrallattice/integral_lattices.sage"))
    load(str(_PREAMBLE / "categories/modules/framed/formed/integrallattice/subobjects.sage"))
    load(str(_PREAMBLE / "categories/modules/group_modules/group_lattices.sage"))
    load(str(_PREAMBLE / "categories/modules/framed/formed/integrallattice/lattice_homomorphisms.sage"))
    load(str(_PREAMBLE / "categories/modules/framed/formed/integrallattice/lattice_isometries.sage"))
    load(str(_PREAMBLE / "categories/modules/framed/formed/integrallattice/coxeter_diagrams.sage"))
    load(str(_PREAMBLE / "categories/modules/framed/formed/integrallattice/hyperbolic_lattices.sage"))
    load(str(_PREAMBLE / "categories/modules/framed/formed/torsionform/torsion_modules_with_form.sage"))
    load(str(_PREAMBLE / "categories/modules/framed/formed/torsionform/discriminant_bilinear_modules.sage"))
    load(str(_PREAMBLE / "categories/modules/framed/formed/torsionform/discriminant_quadratic_modules.sage"))
    load(str(_PREAMBLE / "categories/divisors/divisor_groups.sage"))
    load(str(_PREAMBLE / "categories/divisors/weil_divisor_groups.sage"))
    load(str(_PREAMBLE / "categories/divisors/cartier_divisor_groups.sage"))
    load(str(_PREAMBLE / "categories/divisors/class_groups.sage"))
    load(str(_PREAMBLE / "categories/divisors/picard_groups.sage"))
    load(str(_PREAMBLE / "categories/algebras/free_algebras.sage"))
    load(str(_PREAMBLE / "categories/algebras/algebras.sage"))
    # Make ``from dzack_research.preamble.categories.algebras.algebras``
    # importable during bootstrap even though the implementation is a ``.sage``
    # file loaded via ``load()``.
    if "dzack_research.preamble.categories" not in _sys.modules:
        _pre_categories_module = _types.ModuleType(
            "dzack_research.preamble.categories",
        )
        _pre_categories_module.__file__ = str(_PREAMBLE / "categories")
        _pre_categories_module.__path__ = [str(_PREAMBLE / "categories")]
        _pre_categories_module.__package__ = "dzack_research.preamble"
        _sys.modules["dzack_research.preamble.categories"] = _pre_categories_module
    else:
        _pre_categories_module = _sys.modules["dzack_research.preamble.categories"]

    if "dzack_research.preamble.categories.algebras" not in _sys.modules:
        _pre_algebras_pkg = _types.ModuleType(
            "dzack_research.preamble.categories.algebras",
        )
        _pre_algebras_pkg.__file__ = str(_PREAMBLE / "categories" / "algebras")
        _pre_algebras_pkg.__path__ = [str(_PREAMBLE / "categories" / "algebras")]
        _pre_algebras_pkg.__package__ = "dzack_research.preamble.categories"
        _pre_algebras_pkg.__parent__ = _pre_categories_module
        _sys.modules["dzack_research.preamble.categories.algebras"] = _pre_algebras_pkg
    else:
        _pre_algebras_pkg = _sys.modules["dzack_research.preamble.categories.algebras"]

    _pre_algebras_module = _types.ModuleType(
        "dzack_research.preamble.categories.algebras.algebras",
    )
    _pre_algebras_module.__file__ = str(_PREAMBLE / "categories" / "algebras" / "algebras.sage")
    _pre_algebras_module.__package__ = "dzack_research.preamble.categories.algebras"
    for _export in ("FramedAlgebras", "Algebras"):
        _pre_algebras_module.__dict__.setdefault(_export, globals()[_export])
    _sys.modules["dzack_research.preamble.categories.algebras.algebras"] = (
        _pre_algebras_module
    )
    _pre_algebras_pkg.__dict__.setdefault(
        "algebras",
        _pre_algebras_module,
    )
    _pre_categories_module.__dict__.setdefault(
        "algebras",
        _pre_algebras_pkg,
    )

    load(str(_PREAMBLE / "categories/algebras/framed_free_algebras.sage"))
    load(str(_PREAMBLE / "categories/algebras/finitely_presented_algebras.sage"))
    load(str(_PREAMBLE / "categories/schemes/ringed_spaces.sage"))
    load(str(_PREAMBLE / "categories/schemes/schemes.sage"))
    load(str(_PREAMBLE / "categories/schemes/scheme_morphisms.sage"))
    load(str(_PREAMBLE / "categories/schemes/scheme_points.sage"))
    load(str(_PREAMBLE / "categories/schemes/ambient_spaces.sage"))
    load(str(_PREAMBLE / "categories/schemes/subschemes.sage"))
    load(str(_PREAMBLE / "categories/schemes/varieties.sage"))
    load(str(_PREAMBLE / "catalogue.sage"))
    install_finitely_presented_groups()
    install_finitely_presented_algebras()
    install_algebras()
    install_ringed_spaces()
    install_schemes()
    install_scheme_morphisms()
    install_scheme_points()
    install_ambient_spaces()
    install_subschemes()
    install_varieties()

    # Sage's ``R^n`` syntax is implemented by the parent class of ``Rings``.
    # Install this after the preamble's own catalogue has loaded, since Sage's
    # internal construction work still needs its native free modules while the
    # layer is being initialized.
    from sage.categories.rings import Rings as _SageRings

    _preamble_ring_pow = _SageRings.ParentMethods.__pow__
    if not getattr(_preamble_ring_pow, "_preamble_routed", False):
        import types as _types

        _preamble_original_ring_pow = _types.FunctionType(
            _preamble_ring_pow.__code__,
            _preamble_ring_pow.__globals__,
            name="_preamble_original_ring_pow",
        )
        _preamble_ring_pow.__globals__["_preamble_original_ring_pow"] = (
            _preamble_original_ring_pow
        )
        _preamble_ring_pow.__globals__["_PreambleSageInteger"] = SageInteger
        _preamble_ring_pow.__globals__["_PreambleBasedFreeModule"] = BasedFreeModule

        def _route_ring_pow(self, exponent):
            match exponent:
                case int() | _PreambleSageInteger() if exponent >= int():
                    return _PreambleBasedFreeModule(self, exponent)
                case _:
                    return _preamble_original_ring_pow(self, exponent)

        _preamble_ring_pow.__code__ = _route_ring_pow.__code__
        _preamble_ring_pow._preamble_routed = True

    # Only what the scripts added: re-exporting the caller's own names would
    # overwrite a later module's helpers with this one's.
    _preamble_namespace = {
        _name: _value
        for _name, _value in globals().items()
        if _name not in _exported_before and not _name.startswith("__")
    }
    _preamble_namespace.update(
        {
            "ConditionSet": ConditionSet,
            "ImageSet": ImageSet,
            "Set": Set,
            "Sets": Sets,
        }
    )
    _dzack_research._preamble_namespace = _preamble_namespace
