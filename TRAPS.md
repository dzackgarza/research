# Engine traps

Measured facts about the engines this repository delegates to, kept because
each one is the product of the work and costs an afternoon to rediscover
(`CONTRIBUTING.md`: *The artifacts are instruments; the product is a map of
Sage*; `DEV-63` owns this file). A row is a finding, never a hypothesis: it
records the operation, the spelling measured, the specimen and its size
parameter, the wall times, the version, the command that reproduces it, and the
route chosen. A cost is a curve in the size parameter, or it is a single data
point and says so. `COMPLAINTS.md` holds the unresolved need; this file holds
the fact, which delivery uses and never resolves.

Read this file before choosing any engine route. Write to it in the turn the
measurement is made.

## Sage

### Importing `sage.all` costs about a second; one module costs a tenth of that

Per-invocation tooling that needs one Sage module pays for the whole library
when it imports `sage.all`, and almost nothing when it imports the module.
Single data points, not a curve: there is no size parameter.

| import | wall time, three runs |
| --- | --- |
| bare interpreter (`python -c pass`) | 0.74 s, 0.44 s, 0.46 s |
| `import sage.all` | 1.59 s, 1.11 s, 1.02 s |
| `from sage.graphs.graph import Graph` | 0.58 s, 0.53 s, 0.72 s |
| `from sage.topology.simplicial_complex import SimplicialComplex` | 0.48 s, 0.53 s, 0.50 s |
| `import sage.all`, then `Graph` | 1.34 s, 1.21 s, 1.22 s |
| `sage -c pass` (the launcher) | 1.02 s, 1.04 s, 0.93 s |

Sage 10.10.beta8, Python 3.14.7, the `.envrc` interpreter
`/home/dzack/gitclones/sage-dev-allopts/.venv/bin/python`, 2026-09-16. The
first run of a set is slower; the steady value is the last two. Reproduce with:

```bash
PY=/home/dzack/gitclones/sage-dev-allopts/.venv/bin/python
for i in 1 2 3; do /usr/bin/time -f '%e s' $PY -c 'from sage.graphs.graph import Graph'; done
```

Route chosen: a tool that runs once per invocation imports the module it
computes with, never `sage.all`. Spawning one Sage process per item is a design
defect at either import. Depends on this: the `category-graph` recipes
(TODO node `category-graph-engine`).

The `sage` on `PATH` is a symlink to `sage-dev-allopts/.venv/bin/sage`, a
Python script that accepts `-c` and rejects `-python`; time module imports with
the venv's `python` directly.
