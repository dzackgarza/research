r"""Install the preamble's category layer into a caller's namespace.

``install_preamble(namespace)`` binds the categories, the ``install_*`` hooks
they register, and the names the modules export into ``namespace``.

This sequence is order-sensitive, which is why it lives in one place:
``init.sage`` and every ``.sage`` test call it rather than each maintaining
its own copy.

Calling twice re-exports the *same* objects rather than re-running the
sequence. Categories are compared by identity, and the post-init hooks patch
the Sage classes once, process-wide: a second set of category classes would
leave objects refined into one ``DirectSumObjects`` and tested against
another.

Callers that also want the named specimens continue with ``sterk.sage``,
``coble.sage`` and ``Lattices.install(namespace)``; ``utilities`` and
``catalogue`` are in the module list below, so their names arrive with
everything else.
"""

# The preamble's files import each other by module path.  ``.sage`` is an
# importable source format only once this finder is installed, so it goes in
# before anything below loads a file that imports a sibling.
import sageparse.preparser.importer  # noqa: F401
from sage.categories.sets_cat import Sets
from dzack_research.preamble.categories.rings.rings import install_rings
from dzack_research.preamble.categories.rings.rings import install_session_rings
import dzack_research as _dzack_research


def install_preamble(namespace: dict) -> None:
    r"""Install the preamble's category layer into ``namespace``.

    Takes the namespace rather than reading ``globals()``: this is a module,
    so its own globals are not the caller's, and the caller is a session or a
    test module that wants the names bound in *its* scope.
    """
    _preamble_cache = getattr(_dzack_research, "_preamble_namespace", None)

    if _preamble_cache is not None:
        namespace.update(_preamble_cache)
        # The cached names never include ``ZZ`` and its fellows -- they were the
        # engine's before this file ran, so they are not the preamble's exports --
        # and the scope loading this one has just had Sage's namespace imported
        # into it.  So the session's names are bound here as well.
        install_session_rings(namespace)
    else:
        import sys as _sys
        from pathlib import Path as _Path

        _PREAMBLE = _Path(_dzack_research.__file__).resolve().parent / "preamble"
        _VENDOR_DIR = _PREAMBLE.parents[2r] / "computations" / "vendor"
        import sageparse.preparser.research  # noqa: F401

        def _vendor_import_roots(vendor_dir: "_Path") -> "tuple[_Path, ...]":
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

        # The files, in dependency order.  Python derives the order from the
        # import graph, so this sequence no longer carries it -- what it carries
        # is *export* order: a name defined in two files resolves to the later
        # one, which is what sharing a namespace used to mean.
        #
        # Imported rather than loaded, and that is the whole point: ``load`` runs
        # a file's text into this namespace, so loading a file that another file
        # imports builds its classes twice.  Two ``FormModules`` are two
        # categories, an object refined into one fails an identity check against
        # the other, and the failure surfaces far away as a coercion that cannot
        # find a common parent.
        import importlib as _importlib

        _MODULES = (
            "refine",
            "utilities",
            "categories.forms.gram_matrices",
            "categories.sets.ordinals",
            "categories.sets.cardinals",
            "categories.sets.sets",
            "categories.rings.rings",
            "categories.rings.predicate_subrings",
            "categories.abstract_categories.slice_categories",
            "categories.abstract_categories.arrow_categories",
            "categories.abstract_categories.products",
            # After the three above: ``Cat`` imports the constructions they
            # define, and is where they are attached to Sage's ``Category``.
            "categories.abstract_categories.cat",
            # The morphisms of Cat: the owned functor base and Fun(C, D).
            "categories.abstract_categories.functors",
            "categories.modules.pure.modules",
            "categories.modules.graded_modules",
            "categories.modules.pure.finitely_generated.finitely_generated_modules",
            "categories.modules.pure.free_modules",
            "categories.modules.framed.framed_modules",
            "categories.modules.framed.finitely_generated.finitely_presented_modules",
            "categories.modules.framed.framed_free_modules",
            "categories.modules.framed.finitely_generated.finitely_generated_free_modules",
            "categories.abstract_categories.direct_sum_objects",
            "categories.modules.module_morphisms.module_morphisms",
            "categories.modules.pure.scalar_actions",
            "categories.modules.pure.function_modules",
            "categories.modules.tensors",
            "categories.modules.framed.formed.integrallattice.vinberg_invariants",
            "categories.modules.framed.formed.form_modules",
            "categories.modules.framed.formed.free_lattices",
            "categories.modules.pure.projective_modules",
            "categories.modules.framed.formed.lattices",
            "categories.modules.framed.formed.lattice_axioms",
            "categories.modules.pure.torsion_modules",
            "categories.modules.framed.fraction_field_quotients",
            "categories.modules.framed.finitely_generated.finitely_presented_torsion_modules",
            "categories.modules.group_modules.group_modules",
            "categories.forms.forms",
            "categories.group.magmas",
            "categories.group.groups",
            "categories.group.group_morphisms",
            "categories.group.g_sets",
            "categories.group.profinite.profinite_groups",
            "categories.group.profinite.galois_choice_policy",
            "categories.group.profinite.absolute_galois_groups",
            "categories.group.profinite.absolute_galois_group_element",
            "categories.group.profinite.absolute_galois_group",
            "categories.group.profinite.absolute_galois_group_subgroup",
            "categories.group.profinite.galois_quotient",
            "categories.group.profinite.galois_characters",
            "categories.group.profinite.galois_decomposition",
            "categories.group.finitely_presented_groups",
            "categories.group.predicate_subgroups",
            "categories.modules.framed.formed.integrallattice.integral_lattices",
            # Reached only by local imports until now, so the one lattice axiom
            # category a session could not name.  It depends on the owned bases
            # alone; the position is beside its siblings.
            "categories.modules.framed.formed.integrallattice.definite_lattices",
            "categories.modules.framed.formed.integrallattice.subobjects",
            "categories.modules.group_modules.group_lattices",
            "categories.modules.framed.finitely_generated.ring_as_module",
            "categories.modules.fractional_ideals",
            "categories.functors.trivial_action",
            "categories.functors.free_forgetful_adjunction",
            # After the free-forgetful adjunction it is built beside, and
            # after ``form_modules`` above, whose categories are its ends.
            "categories.functors.form_forgetful_adjunction",
            # After ``abstract_categories.functors``, which is where ``Functor``
            # comes from; nothing else constrains it.
            "categories.functors.twist",
            "categories.functors.ring_centers",
            "categories.functors.cardinality",
            "categories.functors.base_change_adjunction",
            "categories.modules.framed.formed.integrallattice.engines",
            "categories.modules.framed.formed.integrallattice.lattice_homomorphisms",
            "categories.modules.framed.formed.integrallattice.lattice_isometries",
            "categories.modules.framed.formed.integrallattice.isotropic_orbits",
            "categories.modules.framed.formed.integrallattice.vector_orbits",
            "categories.modules.framed.formed.integrallattice.root_lattices",
            "categories.modules.framed.formed.integrallattice.coxeter_diagrams",
            "categories.modules.framed.formed.integrallattice.hyperbolic_lattices",
            "categories.modules.framed.formed.torsionform.torsion_modules_with_form",
            "categories.modules.framed.formed.torsionform.discriminant_bilinear_modules",
            "categories.modules.framed.formed.torsionform.discriminant_quadratic_modules",
            "categories.divisors.divisor_groups",
            "categories.divisors.weil_divisor_groups",
            "categories.divisors.cartier_divisor_groups",
            "categories.divisors.class_groups",
            "categories.divisors.picard_groups",
            "categories.algebras.graded_algebras",
            "categories.algebras.free_algebras",
            "categories.algebras.algebras",
            "categories.algebras.framed_free_algebras",
            "categories.algebras.finitely_presented_algebras",
            "categories.functors.algebra_base_change",
            "categories.algebras.number_fields",
            "categories.schemes.ringed_spaces",
            "categories.schemes.schemes",
            "categories.schemes.scheme_points",
            "categories.schemes.ambient_spaces",
            "categories.schemes.subschemes",
            "categories.schemes.varieties",
            # After ``schemes`` and ``varieties``, the two categories it seats
            # on, and before ``ade_surfaces``, which builds toric objects.
            "categories.schemes.toric.toric_schemes",
            "categories.schemes.polytopes",
            "categories.schemes.ade_surfaces",
            "catalogue",
            "sterk",
            "coble",
        )

        _exports = {}
        for _module_name in _MODULES:
            _module = _importlib.import_module("dzack_research.preamble." + _module_name)
            _compiler_names: frozenset[str] = getattr(
                _module,
                "__sageparse_runtime_names__",
                frozenset(),
            )
            _exports.update(
                {
                    _key: _value
                    for _key, _value in vars(_module).items()
                    if not _key.startswith("_") and _key not in _compiler_names
                }
            )
        namespace.update(_exports)

        # Post-init hooks that construct an owned category cannot run at their
        # module's import: constructing one needs ``Cat()``, so doing it while
        # ``cat`` is still importing re-enters that import.  They run here.
        from dzack_research.preamble.categories.sets.owned_sets import (
            install_poset_display,
        )

        install_poset_display()

        # ``R^n`` is the preamble's free module.  These are the rings a notebook
        # names before it has built anything; every other ring is refined on
        # intake, or by the constructor that builds it.
        _installed_rings = install_rings(namespace)

        # Loading twice re-exports the *same* objects rather than re-running the scripts.
        #
        # What the preamble exports is what its modules define, read off the
        # modules.  Diffing this file's namespace against the names it started
        # with cannot say that: a scope that already held Sage's
        # ``IntegralLattice`` -- any scope that has imported ``sage.all`` --
        # makes the preamble's own constructor look pre-existing, and the
        # session silently keeps Sage's, whose lattices have no ``Aut``.
        _preamble_namespace = dict(_exports)
        _preamble_namespace.update(_installed_rings)
        # ``ZZ`` and its fellows are deliberately absent from the cache: while this
        # file runs they are the engine's, which is what the scripts still loading
        # must build over, so they are not among the names this file exports.
        _dzack_research._preamble_namespace = _preamble_namespace

        # Loading the preamble is what makes a scope a session, so this is where
        # its ``ZZ`` starts meaning the ring rather than the engine's object.  Last
        # in the file, because every ``load()`` above re-imports Sage's namespace
        # into this scope and would rebind the names behind the session's back.
        install_session_rings(namespace)
