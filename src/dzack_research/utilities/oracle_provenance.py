r"""Find assertions that ask a composition for its operands and get them back.

`DEV-47` says the expected value in an assertion must come from somewhere the
code under test did not.  This finds the decidable case: a test builds an object
from operands and then asks it, through the accessor whose whole job is to
return those operands, whether they are those operands.

    product = line * plane
    ...
    assert product.factors()[0] is line

The accessor returns what the construction stored, so the assertion is
guaranteed by the construction.  A mutation score still reports such a test as
effective -- a mutant that reverses the factor order dies against it -- which is
why this shape survives review.

The accessor is the signal, not the operator.  Both ``+`` and ``*`` are
overloaded here: on objects they are direct sum and product, on elements they
are addition and multiplication, and on morphisms ``*`` is composition.  Keying
on the operator therefore flags real claims --

    value = AA(sqrt(2)) + RR(1)
    assert value.parent() is RR            # the coercion model picks RR

    composite = identity * identity
    assert composite == identity           # the unit law

-- neither of which recovers a stored operand.  Keying on a factor accessor
separates them: ``parent`` and ``==`` are not asking a composition what it was
built from, and ``factors`` is.

Also not flagged, and correctly: ``value.base_ring() is field`` where ``value``
came from ``tensor.vector(field, ...)``.  That constructor crosses into a
computation engine, so what comes back is a real question about the `ARC-00`
boundary rather than a stored operand.
"""

import ast
import pathlib
import sys


# Accessors whose contract is to return the operands the construction was given.
# Asking one of these for an operand that was passed in cannot fail.
FACTOR_ACCESSORS = frozenset(
    {
        "biproduct_factors",
        "coproduct_factors",
        "coproduct_injections",
        "factors",
        "indecomposable_summands",
        "product_projections",
        "summands",
        "tensor_factors",
    }
)


def _dotted(node: ast.expr) -> str | None:
    r"""Return the dotted path when ``node`` is a pure reference, else ``None``.

    A pure reference reads a name.  Anything with a call or a subscript in it is
    computing something, and is a subject rather than an oracle.
    """
    match node:
        case ast.Name(id=name):
            return name
        case ast.Attribute(value=value, attr=attr):
            prefix = _dotted(value)
            return None if prefix is None else f"{prefix}.{attr}"
        case _:
            return None


def _references(node: ast.expr) -> set[str]:
    r"""Return every dotted reference occurring anywhere inside ``node``."""
    found: set[str] = set()
    for child in ast.walk(node):
        if isinstance(child, (ast.Name, ast.Attribute)):
            path = _dotted(child)
            if path is not None:
                found.add(path)
    return found


def _root(node: ast.expr) -> str | None:
    r"""Return the name a computed expression ultimately reads from."""
    while True:
        match node:
            case ast.Call(func=func):
                node = func
            case ast.Attribute(value=value):
                node = value
            case ast.Subscript(value=value):
                node = value
            case ast.Name(id=name):
                return name
            case _:
                return None


def _factor_accessor_receiver(node: ast.expr) -> ast.expr | None:
    r"""Return the object a factor accessor was called on, if this is one.

    Subscripts and further attribute reads are transparent: ``x.factors()[0]``
    and ``x.factors().first()`` both ask ``x`` for its operands.
    """
    while True:
        match node:
            case ast.Subscript(value=value):
                node = value
            case ast.Call(func=ast.Attribute(value=receiver, attr=attr)):
                if attr in FACTOR_ACCESSORS:
                    return receiver
                node = receiver
            case ast.Call(func=func):
                node = func
            case ast.Attribute(value=value, attr=attr):
                if attr in FACTOR_ACCESSORS:
                    return value
                node = value
            case _:
                return None


class Finding:
    def __init__(self, path: pathlib.Path, line: int, test: str, oracle: str) -> None:
        self.path = path
        self.line = line
        self.test = test
        self.oracle = oracle

    def __str__(self) -> str:
        return (
            f"{self.path}:{self.line}: in {self.test}, {self.oracle} was given to the "
            f"construction and is read back out of it"
        )


def _scan_test(path: pathlib.Path, function: ast.FunctionDef) -> list[Finding]:
    r"""Return the recovered-operand assertions in one test function."""
    built_from: dict[str, set[str]] = {}
    # A name bound to the result of a factor accessor is a view onto what the
    # construction stored, and carries that construction's ingredients with it.
    factor_view: dict[str, set[str]] = {}
    findings: list[Finding] = []

    def ingredients_of(node: ast.expr) -> set[str]:
        found: set[str] = set()
        for reference in _references(node):
            found.add(reference)
            found |= built_from.get(reference, set())
        return found

    for statement in ast.walk(function):
        match statement:
            case ast.Assign(targets=[ast.Name(id=target)], value=value):
                built_from[target] = ingredients_of(value)
                receiver = _factor_accessor_receiver(value)
                if receiver is not None:
                    factor_view[target] = ingredients_of(receiver)
            case ast.Assert(test=ast.Compare(left=left, comparators=[right])):
                for subject, oracle in ((left, right), (right, left)):
                    name = _dotted(oracle)
                    if name is None:
                        continue
                    root = _root(subject)
                    if root is not None and root in factor_view:
                        ingredients = factor_view[root]
                    else:
                        receiver = _factor_accessor_receiver(subject)
                        if receiver is None:
                            continue
                        ingredients = ingredients_of(receiver)
                    if name in ingredients:
                        findings.append(
                            Finding(path, statement.lineno, function.name, name)
                        )
                        break
    return findings


def scan(paths) -> tuple[int, list[Finding]]:
    r"""Return the number of test functions examined and the findings."""
    examined = 0
    findings: list[Finding] = []
    for path in paths:
        tree = ast.parse(path.read_text(), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith("test"):
                examined += 1
                findings.extend(_scan_test(path, node))
    return examined, findings


def main(argv: list[str]) -> int:
    paths = [pathlib.Path(argument) for argument in argv[1:]]
    if not paths:
        print("No test files to check.")
        return 0
    examined, findings = scan(paths)
    print(f"Examined {examined} test functions in {len(paths)} files.")
    if not findings:
        print("No assertion reads an operand back out of the construction.")
        return 0
    print()
    for finding in findings:
        print(finding)
    print()
    print(
        f"{len(findings)} findings.  `DEV-47`: a factor accessor returns what the\n"
        "construction stored, so recovering an operand is guaranteed.  Assert what the\n"
        "composition computed instead -- its form, its rank, its universal property."
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
