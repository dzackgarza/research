# Runtime-maintenance checkpoint (research side)

Issued on the runtime-maintenance notice: stop only this session's rootfs processes, launch
none, preserve logs and job IDs, record interrupted runs truthfully, and wait for a verified
resume before rerunning acceptance.

## Processes

| job | state | what it was | result |
| --- | --- | --- | --- |
| `jmw2hyo1i` | **stopped by this agent** during maintenance | chunk run of 247 `tests/constructions/test_[a-f]*.sage` over the rootfs | **interrupted, no results produced**; its log is `.nucleus/jobs/jmw2hyo1i.log` (17 bytes: the file-count line only) |
| `jmw2fot47` | exited 4, 2 m 56 s | first whole-directory attempt | collection abort, recorded in `research-417-suite-attribution.md` |
| `jmw2ftfaq` | exited 4, 2 m 54 s | corrected whole-directory attempt | same, recorded |
| `jmw2fv66n` | exited 0 | polling waiter for `jmw2ftfaq` | printed the stale pre-repair tail |
| `jmw2cgf0j` | exited 0 | upstream-state fetch at rate reset | states recorded |

Quiescence check after the stop: no process references this project's rootfs usage or
`.scratch/udocker_dir/bin/proot`, and an owner-attributed scan for processes holding
`sage-image/rootfs` returned **none** at that instant. No other project's process was
touched.

## Consequence for the measured numbers

Every count recorded so far was measured against the **pre-maintenance live rootfs** with
the `6ad7a5ea` provider snapshot:

- 56-file set-layer batch: 50 passed / 27 failed (`c5b07e2a49`);
- `test_functors_construct` + `test_properties_construct`: 161 failed / 6 passed / 3 errors;
- `test_fraction_field_quotient_arithmetic_regression`: collects only against `ad436ca5`.

If Sage adopts a different immutable image, these become **measurements of a superseded
runtime** and must be re-run against the verified image before any of them is treated as
acceptance for `#417`. They are retained as history, not as current evidence.

## State

- no rootfs job started by this session after the notice;
- no consumer pin change, no shared-runtime write, no upstream edit, no issue write;
- assertions, blocked cases (`ring_of_integers`, `fraction_field`, the three stale names)
  and failed obligations remain as recorded;
- coverage accounting stands at 56 of 754 files measured, 0 measured on a verified image;
- `#417` unaccepted.
