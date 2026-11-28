r"""Category obligation examples for number-field and rational-field splits."""

import ast
from pathlib import Path

ROOT = Path("/home/dzack/research")
RINGS_INIT = ROOT / "category_specs/rings/__init__.py"
RINGS_MAPPING = (
    ROOT
    / "plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/"
    / "SPEC-MAPPING-RINGS.md"
)

module = ast.parse(RINGS_INIT.read_text())


def constructor_method(name):
    for node in module.body:
        if isinstance(node, ast.ClassDef) and node.name == "Rings":
            for child in node.body:
                if isinstance(child, ast.ClassDef) and child.name == "Constructors":
                    for method in child.body:
                        if isinstance(method, ast.FunctionDef) and method.name == name:
                            return method
    raise AssertionError(f"missing Rings().Constructors().{name}")


def assert_closed_signature(name, args, kwonly=()):
    method = constructor_method(name)
    actual_args = tuple(arg.arg for arg in method.args.args)
    actual_kwonly = tuple(arg.arg for arg in method.args.kwonlyargs)
    assert actual_args == ("self", *args), (name, actual_args)
    assert actual_kwonly == tuple(kwonly), (name, actual_kwonly)
    assert method.args.vararg is None, f"{name} exposes *args"
    assert method.args.kwarg is None, f"{name} exposes **kwargs"


assert_closed_signature("QQ", ())
assert_closed_signature(
    "NumberField",
    (
        "polynomial",
        "name",
        "check",
        "names",
        "embedding",
        "latex_name",
        "assume_disc_small",
        "maximize_at_primes",
        "structure",
    ),
    kwonly=("latex_names",),
)
assert_closed_signature(
    "NumberFieldTower",
    (
        "polynomials",
        "names",
        "check",
        "embeddings",
        "latex_names",
        "assume_disc_small",
        "maximize_at_primes",
        "structures",
    ),
)

mapping = RINGS_MAPPING.read_text()
assert "`RationalField()` / `QQ`" in mapping
assert "`Rings().Constructors().QQ()`" in mapping
assert "NumberField(polynomial, name=None" in mapping
assert "NumberFieldTower(polynomials, names" in mapping
