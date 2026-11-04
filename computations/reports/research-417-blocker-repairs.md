# #417 collection blockers: audited, repaired in this repo, and measured

Owned repairs only; no file excluded, no skip masked, `POLICY.NO_SKIP_MASK` left on, no
assertion weakened, provider pin and shared runtime untouched.

## Blocker 1 — `POLICY.NO_SKIP_MASK` on `test_functors_construct.sage`

**Audit.** `NULLARY_FUNCTORS = {}` and the test was `@pytest.mark.parametrize("name",
sorted(NULLARY_FUNCTORS))`. An empty parametrization is reported by pytest as a skip
(`[NOTSET]`), which the project's plugin treats as a usage error and aborts the session.
History shows the dict has been empty since the file was introduced (`fca075e6d5`,
`64e66e8804`), so no assertion ever ran — the skip was masking a vacuous population. The
file's own `test_known_values_of_the_nullary_functors` names the real population
(abelianization, cardinality, power set, free group, underlying set, ring of integers,
fraction field), and a probe of the deployed runtime confirms those objects are callable
with `.domain()` and `.codomain()`.

**Repair.** The parametrization is replaced by one test that (a) asserts the population is
non-empty with a message naming those seven functors, and (b) runs the *identical*
assertion body over every entry. No assertion was dropped; the vacuous case now fails
instead of skipping.

**Measured.** The file collects and runs: **147 failed, 3 errors in 41.53 s**. Those are
real expectation failures against the deployed `6ad7a5ea` provider, now visible instead of
hidden behind a session abort.

## Blocker 2 — `ImportError: COMMUTATIVE_RINGS from conftest`

**Audit.** `test_properties_construct.sage` imports `COMMUTATIVE_RINGS, FIELDS,
PRINCIPAL_IDEAL_DOMAINS, specimen` from `conftest`. Inside `tests/constructions` that name
resolves to the directory's own `conftest.py`, which only installs category
abbreviations; the definitions live in the test-root `tests/conftest.py`.

**Repair.** `tests/constructions/conftest.py` now re-exports those four names from the
test-root conftest, loaded by path. No duplication, no change to any expectation.

**Measured.** The import now resolves. The next blocker is environmental and new:
`ModuleNotFoundError: No module named 'hypothesis'` in the deployed venv.

## Blocker 3 — `ImportError: FractionFieldQuotients`

**Audit.** The class exists in the provider
(`sage_extensions/categories/modules/framed/fraction_field_quotients.py:40`) but is **not
exported by `sage_extensions/all.py`**, so it is absent from
`dzack_research.preamble.all`. Nothing in this repository can legitimately re-export it
without reaching into provider internals, which the ownership rule forbids.

**State.** Not repaired here. It is a third owner handoff, distinct from the subset-read
contract and `object_set`: *export `FractionFieldQuotients` (or its supported public
spelling) through `sage_extensions.all`*.

## Net effect

| blocker | owner | state |
| --- | --- | --- |
| vacuous parametrization / skip | research | **repaired**; file now runs (147 failed, 3 errors) |
| `COMMUTATIVE_RINGS` conftest resolution | research | **repaired**; now blocked on `hypothesis` |
| `hypothesis` absence | runtime/harness | new, environmental |
| `FractionFieldQuotients` export | sage-extensions | handoff |

`#417` remains unaccepted; these repairs unblock collection, they do not make the suite
pass.
