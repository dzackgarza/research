"""The genus invariants of integral lattices, computed by SageMath: run by `latticedb certify` under `sage -python`.

Reads from standard input a JSON object `{"seconds": s, "lattices": [{"tag", "gram", "sign", "fields"}, ...]}`,
where `sign` is 1 for a positive definite lattice, -1 for a negative definite one and 0 otherwise, and
`fields` names the values to compute among `genus_symbol`, `genus_class_count` and
`automorphism_group_order`. Writes one JSON line per lattice to standard output, as soon as it is
computed: the tag, the version of SageMath as `by`, and each value of `fields`. A value that is not
computed within `s` seconds is null.

The module imports SageMath and nothing of `latticedb`, whose environment does not have SageMath.
"""

import json
import sys
from collections.abc import Callable
from functools import partial
from typing import TypedDict

from cysignals.signals import AlarmInterrupt
from sage.all import ZZ, alarm, cancel_alarm, matrix, pari
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.quadratic_forms.binary_qf import BinaryQF
from sage.quadratic_forms.genera.genus import Genus
from sage.version import version


class Request(TypedDict):
    tag: str
    gram: list[list[int]]
    sign: int
    fields: list[str]


def symbol(gram: Matrix_integer_dense) -> str:
    """`I` or `II` with the signature pair, then, when the determinant is not 1 or -1, the local symbol at each prime of twice the determinant as SageMath prints it."""
    genus = Genus(gram)
    positive, negative = genus.signature_pair()
    head = f"{'II' if genus.is_even() else 'I'}_{{{positive},{negative}}}"
    if abs(gram.det()) == 1:
        return head
    local = [f"{local_symbol.prime()}: {repr(local_symbol).split(':', 1)[1].strip()}" for local_symbol in genus.local_symbols()]
    return f"{head} ({'; '.join(local)})"


def class_count(gram: Matrix_integer_dense) -> int:
    """The number of isometry classes in the genus of `gram`.

    `representatives(backend="sage")` avoids Magma, which SageMath calls by default for a definite form of rank more than 6.
    For an indefinite binary form it lists every reduced form of each cycle, so the forms are counted up to improper equivalence.
    """
    representatives = Genus(gram).representatives(backend="sage")
    if gram.nrows() != 2 or gram.det() > 0:
        return len(representatives)
    classes: list[BinaryQF] = []
    for form in (BinaryQF(r[0, 0], 2 * r[0, 1], r[1, 1]) for r in representatives):
        if not any(form.is_equivalent(other, proper=False) for other in classes):
            classes.append(form)
    return len(classes)


def within(seconds: int, compute: Callable[[], int | str]) -> int | str | None:
    """The value of `compute`, or None when it takes more than `seconds` seconds."""
    alarm(seconds)
    # SageMath interrupts a computation only by raising AlarmInterrupt in it.
    try:
        value = compute()
    except AlarmInterrupt:
        return None
    cancel_alarm()
    return value


def automorphism_group_order(gram: Matrix_integer_dense) -> int:
    """The order of O(L) of a positive definite Gram matrix, by `qfauto` of PARI/GP."""
    return int(pari(gram).qfauto()[0])


def main() -> None:
    task = json.load(sys.stdin)
    seconds: int = task["seconds"]
    lattices: list[Request] = task["lattices"]
    for lattice in lattices:
        gram = matrix(ZZ, lattice["gram"])
        positive = gram if lattice["sign"] >= 0 else -gram
        computations: dict[str, Callable[[], int | str]] = {
            "genus_symbol": partial(symbol, gram),
            "genus_class_count": partial(class_count, gram),
            "automorphism_group_order": partial(automorphism_group_order, positive),
        }
        line: dict[str, int | str | None] = {"tag": lattice["tag"], "by": f"SageMath {version}"}
        for field in lattice["fields"]:
            line[field] = within(seconds, computations[field])
        print(json.dumps(line), flush=True)


if __name__ == "__main__":
    main()
