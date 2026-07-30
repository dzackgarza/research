r"""Load and install the preamble's category layer into the calling namespace.

``load()`` shares the caller's globals, so everything defined here -- the
categories, the ``install_*`` hooks they register, and the names the scripts
export -- lands in the namespace that loaded this file.

This sequence is order-sensitive (``install_integral_lattices`` needs
``HyperbolicLattices``, which ``hyperbolic_lattices.sage`` defines), which is
why it lives in one file: ``init.sage`` and every ``.sage`` test load it rather
than each maintaining its own copy.

Loading twice re-exports the *same* objects rather than re-running the scripts.
Categories are compared by identity, and the post-init hooks patch the Sage
classes once, process-wide: a second set of category classes would leave
lattices refined into one ``DirectSumObjects`` and tested against another.

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

    def _vendor_import_roots(vendor_dir):
        r"""Return the vendor subtrees that expose importable modules or packages."""
        assert vendor_dir.is_dir(), f"vendor directory is missing: {vendor_dir}"
        roots = {vendor_dir}
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
    load(str(_PREAMBLE / "categories/gram_matrices.sage"))
    load(str(_PREAMBLE / "categories/group/groups.sage"))
    load(str(_PREAMBLE / "categories/group/finitely_presented_groups.sage"))
    load(str(_PREAMBLE / "categories/integrallattice/integral_lattices.sage"))
    load(str(_PREAMBLE / "categories/integrallattice/subobjects.sage"))
    load(str(_PREAMBLE / "categories/integrallattice/direct_sum_objects.sage"))
    load(str(_PREAMBLE / "categories/lattice_homomorphisms.sage"))
    load(str(_PREAMBLE / "categories/lattice_isometries.sage"))
    load(str(_PREAMBLE / "categories/coxeter_diagrams.sage"))
    load(str(_PREAMBLE / "categories/integrallattice/hyperbolic_lattices.sage"))
    load(str(_PREAMBLE / "categories/torsionform/torsion_modules_with_form.sage"))
    load(str(_PREAMBLE / "categories/torsionform/discriminant_bilinear_modules.sage"))
    load(str(_PREAMBLE / "categories/torsionform/discriminant_quadratic_modules.sage"))

    install_integral_lattices()
    install_finitely_presented_groups()

    # Only what the scripts added: re-exporting the caller's own names would
    # overwrite a later module's helpers with this one's.
    _dzack_research._preamble_namespace = {
        _name: _value
        for _name, _value in globals().items()
        if _name not in _exported_before and not _name.startswith("__")
    }
