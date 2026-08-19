# Sage Axiom Binding Is Descriptor Binding

When editing `category_specs` axiom subcategory selectors, treat `_base_category_class_and_axiom = (B, "A")` as the binding contract between the axiomatic call `B().A()` and the concrete axiom category class.

The class descriptor or `LazyImport` for axiom `A` must live on exactly the declared base category class `B` under the exact attribute name `A`. A transitive ancestor may expose a convenience method that routes through the chain, but it must not also carry the descriptor for `A` unless its own `_base_category_class_and_axiom` declares that ancestor as the base.

The Sage source pattern for a direct axiom selector is:

```python
class SubcategoryMethods:
    def A(self):
        return self._with_axiom("A")
```

Do not write `with_axiom(self, "A")`, and do not wrap axiom selectors in `typing.cast`. If static checking cannot see the dynamic category binding, fix the category graph, plugin, or hook/QC model; do not hide the mismatch in spec code.

Do not introduce local `cached_method` wrappers as mathematical spec content. A direct Sage `@cached_method` may be a runtime witness only when cached category identity is a documented Sage interop requirement; otherwise category selectors should state the mathematical operation plainly. Local aliases such as `_cached_method = cast(...)` or `def _field_cached_method(...): return cached_method(...)` are engineering leakage and should be removed or centralized at an explicit interop boundary.

Mechanical guard: `category_specs/validators/banned_spec_patterns.py` scans the whole tracked `category_specs` tree and reports warning findings for banned patterns. It is warning-only while inherited debt exists, so it preserves visibility without blocking unrelated commits. Once the debt is cleared, the same validator can be run with `--fail-on-staged` or tightened to fail.

A warning-only guard must still be actionable. It must report dynamic repo-wide facts, not static prose: scanned file count, affected file count, total findings, staged findings, counts by rule, top affected files, exact file:line findings, and the repair action for each rule.

Verification: for every axiom class `C` with `_base_category_class_and_axiom = (B, "A")`, `B.__dict__["A"]` is the class or lazy import for `C`, and `B().A()` reaches the corresponding `SubcategoryMethods.A` method returning `self._with_axiom("A")`. Running `just --justfile category_specs/justfile check-banned-spec-patterns` reports any remaining `cast(...)` or `with_axiom(self, ...)` occurrences repo-wide with an actionable dynamic summary.
