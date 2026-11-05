# Verifying the provider's `FractionFieldQuotients` repair at `ad436ca5`

Separate measured source binding: the commit's tarball extracted to
`.scratch/se-provider-ad436ca5` and put first on `PYTHONPATH` for the run only. The
consumer pin (`.scratch/se-provider-6ad7a5ea`) and the live rootfs are unchanged.

## What the repair delivers

`src/sage_extensions/all.py:243` now exports `FractionFieldQuotients`, so it reaches
`dzack_research.preamble.all`. Under that binding
`tests/constructions/test_fraction_field_quotient_arithmetic_regression.sage`
**collects for the first time** — the original third blocker (the missing export) is
verified repaired at source.

## What the test reports under the harness

`1 failed in 0.34 s` with

```
TypeError: cannot convert 2 into Integer Ring: it is a raw Sage element of Integer Ring;
construct it from a ring of this session        ring_foundation.py:6384
```

## What makes that failure not yet a defect adjudication

The identical expressions, in the same runtime and against the same repaired binding but
run **outside** the pytest harness, both succeed:

```
python int 2    -> OK; sum: True ; neg: True
session ZZ(2)   -> OK; sum: True ; neg: True
```

So the coercion the harness rejects is accepted by the provider when the session is
driven directly. The difference is the `qc_sage_session` harness-plugin layer, and
deciding which behaviour is the contract — the plugin's strictness or the provider's
acceptance — is not something to settle by editing the expectation. **The test was left
unchanged.**

## State

- provider export: verified repaired (`ad436ca5`);
- pin change: not made here — the consumer still binds `6ad7a5ea`, and adopting the repair
  is a pin decision for the consumer owner, not a side effect of this measurement;
- the `FractionFieldQuotients` handoff is therefore closed at source but open for the pin;
- coverage is unchanged: the same two of 754 files run under the harness, now with a
  third file collecting.
