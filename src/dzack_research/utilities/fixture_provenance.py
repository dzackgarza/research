r"""Check that every cited fact resolves, and report what is still unverified.

`DEV-41` puts mathematical expectations in ``tests/fixtures`` as data carrying a
citation.  A citation nobody checks is decoration, so this reports three things:

- **unresolved citations** -- a key that is not in the bibliography.  The fact
  claims a source that does not exist, which is worse than no citation, because
  it reads as verified.
- **unverified rows** -- a citation that resolves, but which nobody has checked
  the value against.  A row moved out of an implementation starts here.  It is
  reported rather than failed: the state is legitimate, and silence about it is
  not.
- **fixtures that import the code under test** -- a fixture is data.  One that
  imports ``dzack_research`` can derive its expectation from the implementation,
  which is the failure `DEV-41` exists to prevent.

Only the first and the third fail.  The second is a standing count, so that
"nothing wrong" stays distinguishable from "nothing looked at" (`DEV-42`).
"""

import ast
import pathlib
import re
import sys


BIBLIOGRAPHY = pathlib.Path.home() / ".pandoc" / "bib" / "references.bib"
_ENTRY = re.compile(r"^@\w+\{([^,]+),", re.M)


def _known_citation_keys(bibliography: pathlib.Path) -> set[str]:
    if not bibliography.is_file():
        return set()
    return set(_ENTRY.findall(bibliography.read_text(errors="replace")))


def _facts(module: ast.Module):
    r"""Yield ``(name, citation, verified)`` for each ``Fact`` in a fixture."""
    for node in ast.walk(module):
        match node:
            case ast.Assign(targets=[ast.Name(id=name)], value=ast.Call(func=func, keywords=keywords)):
                called = func.id if isinstance(func, ast.Name) else getattr(func, "attr", None)
                if called != "Fact":
                    continue
                fields = {}
                for keyword in keywords:
                    if keyword.arg is None:
                        continue
                    try:
                        fields[keyword.arg] = ast.literal_eval(keyword.value)
                    except ValueError:
                        fields[keyword.arg] = None
                yield name, fields.get("citation"), bool(fields.get("verified"))


def _imports_the_code_under_test(module: ast.Module) -> bool:
    for node in ast.walk(module):
        match node:
            case ast.Import(names=names):
                if any(alias.name.startswith("dzack_research") for alias in names):
                    return True
            case ast.ImportFrom(module=name) if name and name.startswith("dzack_research"):
                return True
    return False


def main(argv: list[str]) -> int:
    root = pathlib.Path(argv[1]) if len(argv) > 1 else pathlib.Path("tests/fixtures")
    if not root.is_dir():
        print(f"No fixtures subtree at {root}.")
        return 0
    known = _known_citation_keys(BIBLIOGRAPHY)
    if not known:
        print(f"The bibliography {BIBLIOGRAPHY} is missing; citations cannot resolve.")
        return 1

    paths = sorted(p for p in root.rglob("*.py") if p.name != "__init__.py")
    unresolved: list[str] = []
    unverified: list[str] = []
    importing: list[str] = []
    facts = 0

    for path in paths:
        module = ast.parse(path.read_text(), filename=str(path))
        if _imports_the_code_under_test(module):
            importing.append(str(path))
        for name, citation, verified in _facts(module):
            facts += 1
            if citation not in known:
                unresolved.append(f"{path}: {name} cites {citation!r}, which is not in the bibliography")
            elif not verified:
                unverified.append(f"{path}: {name} (cites {citation})")

    print(f"Examined {facts} facts in {len(paths)} fixture modules.")
    print(f"Bibliography: {len(known)} entries in {BIBLIOGRAPHY}.")

    if importing:
        print("\nFixtures importing the code under test:")
        for line in importing:
            print(f"  {line}")
    if unresolved:
        print("\nCitations that do not resolve:")
        for line in unresolved:
            print(f"  {line}")
    if unverified:
        print(f"\n{len(unverified)} facts cite a real source but are unverified against it:")
        for line in unverified:
            print(f"  {line}")

    if importing or unresolved:
        print("\nA fixture is data, and a citation names a source that exists.")
        return 1
    print("\nEvery citation resolves, and no fixture reads the code under test.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
