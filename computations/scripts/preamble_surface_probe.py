r"""What a researcher can actually do with the preamble, measured.

Run it::

    sage -python computations/scripts/preamble_surface_probe.py
    # or, directly:
    /home/dzack/gitclones/sage-dev-allopts/.venv/bin/python3 computations/scripts/preamble_surface_probe.py

Not a test suite and not a gate: it always exits 0 and reports. The output is
grouped **by operation**, because a broken operation is one finding however
many objects it breaks on -- `an_element` failing on forty lattices is one
defect, and a list of forty failures hides that.

Three populations, because a defect in one is invisible from the others:

- **adopted** -- the parents a session *names* (``ZZ``, ``GF(7)``, ``RR``,
  ``QQ['x']``) and the Sage groups it constructs. These reach the preamble
  through ``install_session_rings`` and the post-init hooks, never through an
  owned constructor, so nothing an owned constructor does covers them.
- **constructed** -- every way the preamble builds an object, read from
  ``tests/test_constructors_meet_their_obligations.sage``'s own
  ``_constructions()`` table rather than re-listed here, so a constructor
  added there is probed here without an edit.
- **lattices** -- the catalogue, which additionally gets the operations the
  mathematics is for.

The session is seeded from ``sage.all`` before the preamble loads, because
that is a researcher's situation and it is load-bearing:
``install_session_rings`` rebinds names *already in scope*, so an empty
namespace silently yields a session with no ``RR``, no ``GF`` and no
``MatrixSpace`` -- and every operation on them then reads as absent when it
is really untested.
"""

from __future__ import annotations

import sys
import traceback
from collections import OrderedDict

sys.setrecursionlimit(3000)

REPO = "/home/dzack/research"
OBLIGATIONS = f"{REPO}/tests/test_constructors_meet_their_obligations.sage"


class Inapplicable(Exception):
    r"""The operation is not defined for this object, and that is not a defect."""


def session():
    r"""A namespace as a researcher holds it: Sage's names, then the preamble."""
    import sage.all as sage_all

    scope = {k: v for k, v in vars(sage_all).items() if not k.startswith("_")}
    from dzack_research.preamble.install import install_preamble

    install_preamble(scope)
    return scope


def constructed_specimens(scope):
    r"""The obligations table: one specimen per way the preamble builds."""
    from sage.repl.preparse import preparse

    module = type(sys)("obligations")
    module.__dict__.update(scope)
    source = open(OBLIGATIONS).read()
    exec(compile(preparse(source), OBLIGATIONS, "exec"), module.__dict__)
    return module._constructions()


def adopted_specimens(scope):
    r"""Parents a session names or builds from Sage's own constructors."""
    found = OrderedDict()
    for expression in (
        "ZZ", "QQ", "RR", "CC", "QQbar",
        "GF(7)", "GF(9)", "Zmod(6)", "Integers(6)", "Zp(5)",
        "QQ['x']", "ZZ['x','y']", "MatrixSpace(ZZ, 2)",
        "SymmetricGroup(3)", "CyclicPermutationGroup(4)",
        "CoxeterGroup(['A', 2])", "DihedralGroup(4)",
    ):
        try:
            found[expression] = eval(expression, dict(scope))
        except Exception as error:
            found[expression] = error
    return found


def lattice_specimens(scope):
    r"""The catalogue: named lattices, Coxeter and Sterk specimens."""
    found = OrderedDict()
    for holder in ("Lattices", "Coble", "Sterk"):
        namespace = scope.get(holder)
        if namespace is None:
            continue
        for name in sorted(n for n in dir(namespace) if not n.startswith("_")):
            try:
                specimen = getattr(namespace, name)
            except Exception:
                continue
            if hasattr(specimen, "gram_matrix") and not callable(
                getattr(specimen, "__call__", None)
            ):
                found[f"{holder}.{name}"] = specimen
            elif hasattr(specimen, "form") and hasattr(specimen, "rank"):
                found[f"{holder}.{name}"] = specimen
    return found


# ---------------------------------------------------------------- operations


def _additive(parent):
    r"""Whether ``0`` names anything here. A group is not an additive parent."""
    from sage.categories.additive_magmas import AdditiveMagmas

    if parent not in AdditiveMagmas():
        raise Inapplicable("multiplicative")


def _enumerable(parent):
    r"""Whether being iterable is a *contract* this object took on.

    Membership of ``FiniteEnumeratedSets`` is the promise of a chosen
    enumeration, so failing to iterate there is a defect. ``RR`` refusing to
    enumerate is not: it never claimed to, and countability names no
    enumeration either -- ``QQbar`` is countable and has chosen none.
    """
    from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets

    if parent not in FiniteEnumeratedSets():
        raise Inapplicable("no enumeration claimed")


def _first(parent):
    _enumerable(parent)
    for element in parent:
        return element
    raise Inapplicable("empty")


def _contains_own(parent):
    return parent.an_element() in parent


def _zero(parent):
    _additive(parent)
    return parent.zero()


def _coerce_literal(parent):
    from sage.rings.integer_ring import ZZ as SageZZ

    _additive(parent)
    return parent(SageZZ.zero())


def _hom(parent):
    from sage.categories.homset import Hom

    return Hom(parent, parent)


def _placement(parent):
    from dzack_research.preamble.categories.sets.owned_sets import placement_of

    return placement_of(parent)


def _cardinal_kind(parent):
    r"""The count, and whether it is an owned cardinal rather than a raw count."""
    from dzack_research.preamble.categories.sets.cardinals import Cardinal

    count = parent.cardinality()
    if not isinstance(count, Cardinal):
        raise AssertionError(
            f"answers {type(count).__name__}, not a Cardinal: {count}"
        )
    return count


PROTOCOL = OrderedDict(
    [
        ("an_element", lambda p: p.an_element()),
        ("zero", _zero),
        ("random_element", lambda p: p.random_element()),
        ("iter (first)", _first),
        ("contains own element", _contains_own),
        ("cardinality", lambda p: p.cardinality()),
        ("cardinality is a Cardinal", _cardinal_kind),
        ("is_finite", lambda p: p.is_finite()),
        ("is_countable", lambda p: p.is_countable()),
        ("coerce 0", _coerce_literal),
        ("equality with self", lambda p: p == p),
        ("hash", lambda p: hash(p)),
        ("Hom(P, P)", _hom),
        ("placement_of", _placement),
    ]
)


def _pairing(lattice):
    generators = list(lattice.module_generating_set())
    if not generators:
        raise Inapplicable("rank zero")
    first = lattice.module_generator(generators[0])
    return first.b(first)


def _aut_order(lattice):
    return lattice.Aut().cardinality()


def _subobject_index(lattice):
    generators = list(lattice.module_generating_set())
    if not generators:
        raise Inapplicable("rank zero")
    return lattice.subobject_on([lattice.module_generator(generators[0])])


# Invariant and coinvariant lattices are not probed. Both consume a
# G-action, which is a morphism the caller constructs and a datum the object
# does not carry -- synthesizing one here would be inventing the very thing
# the operation is about. They need a specimen with a named action (the swap
# involution on U, a catalogue involution), which is a probe of the
# catalogue's involutions rather than of every lattice.
MATHEMATICS = OrderedDict(
    [
        ("module_rank", lambda L: L.module_rank()),
        ("gram_matrix", lambda L: L.gram_matrix()),
        ("pairing b(e, e)", _pairing),
        ("signature_pair", lambda L: L.signature_pair()),
        ("direct sum L + L", lambda L: L + L),
        ("twist L(-1)", lambda L: L.twist(-1)),
        ("tensor L @ L", lambda L: L @ L),
        ("discriminant_group", lambda L: L.discriminant_group()),
        ("Aut", lambda L: L.Aut()),
        ("|Aut|", _aut_order),
        ("subobject_on", _subobject_index),
    ]
)


# ------------------------------------------------------------------- running


def run(specimens, operations, label, results):
    for name, specimen in specimens.items():
        if isinstance(specimen, Exception):
            results.setdefault(("construction", label), []).append(
                (name, f"{type(specimen).__name__}: {specimen}")
            )
            continue
        for operation, action in operations.items():
            try:
                action(specimen)
            except Inapplicable:
                continue
            except Exception as error:
                message = str(error).strip().splitlines()
                first_line = message[0] if message else ""
                results.setdefault((operation, label), []).append(
                    (name, f"{type(error).__name__}: {first_line}")
                )


def report(results, totals):
    print()
    print("=" * 78)
    print("BROKEN, grouped by operation")
    print("=" * 78)
    if not results:
        print("  nothing")
        return
    for (operation, label), failures in sorted(results.items()):
        total = totals.get(label, 0)
        print()
        print(f"  {operation}  [{label}]  {len(failures)}/{total} specimens")
        seen = OrderedDict()
        for name, message in failures:
            # One defect renders once per object it names, so the ranks and
            # signatures in the text are noise: collapse digits to see how
            # many *distinct* failures there really are.
            key = "".join("#" if character.isdigit() else character for character in message)
            seen.setdefault(key, (message, []))[1].append(name)
        for index, (message, names) in enumerate(seen.values()):
            if index == 6:
                print(f"      ... and {len(seen) - 6} further distinct messages")
                break
            shown = ", ".join(names[:5])
            more = f", +{len(names) - 5} more" if len(names) > 5 else ""
            print(f"      {message[:150]}")
            print(f"        on: {shown}{more}")


# A small specimen proves the operation as well as a large one and costs
# seconds instead of minutes: |Aut(E8)| = 696729600 and E10 @ E10 has rank
# 100, and neither tells you anything the rank-2 case does not.
SMALL_RANK = 4


def small(lattices):
    kept = OrderedDict()
    for name, lattice in lattices.items():
        try:
            if lattice.module_rank() <= SMALL_RANK:
                kept[name] = lattice
        except Exception:
            continue
    return kept


def main():
    from time import time

    started = time()

    def note(message):
        print(f"[{time() - started:5.1f}s] {message}", flush=True)

    note("building the session")
    scope = session()

    results = {}
    totals = {}

    note("adopted specimens")
    adopted = adopted_specimens(scope)
    totals["adopted"] = len(adopted)
    note(f"  {len(adopted)}; probing")
    run(adopted, PROTOCOL, "adopted", results)

    note("constructed specimens (the obligations table)")
    try:
        constructed = constructed_specimens(scope)
    except Exception:
        print("could not load the obligations table:")
        traceback.print_exc()
        constructed = OrderedDict()
    totals["constructed"] = len(constructed)
    note(f"  {len(constructed)}; probing")
    run(constructed, PROTOCOL, "constructed", results)

    note("catalogue lattices")
    lattices = lattice_specimens(scope)
    totals["lattices"] = len(lattices)
    note(f"  {len(lattices)}; probing the Sage protocol")
    run(lattices, PROTOCOL, "lattices", results)

    modest = small(lattices)
    totals[f"lattices rank<={SMALL_RANK}"] = len(modest)
    note(f"  {len(modest)} of rank <= {SMALL_RANK}; probing the mathematics")
    run(modest, MATHEMATICS, f"lattices rank<={SMALL_RANK}", results)

    report(results, totals)
    print()
    print(f"{len(results)} broken (operation, population) pairs")
    note("done")


if __name__ == "__main__":
    main()
