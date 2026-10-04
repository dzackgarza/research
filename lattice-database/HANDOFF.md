# Handoff: migrate latticedb's lattice arithmetic onto the preamble

## Governing rules — every migration follows CONTRIBUTING.md

**All work in this task obeys [CONTRIBUTING.md](../CONTRIBUTING.md), without
exception.** In particular, no hand-rolled function is replaced and no gap is
migrated until its mathematics is traced first:

- Every migrated or replaced operation begins with the
  [mathematical dependency trace](../CONTRIBUTING.md#mathematical-dependency-tracing):
  locate the notion in `lean-categories`' formalization, unfold its defining
  data, maps, hypotheses and constructions, and only then choose the
  implementation. A function is not moved because a method of a similar name
  exists.
- The replacement obeys the
  [architecture specification](../CONTRIBUTING.md#preamble-architecture-specification):
  `OWN-01` (locate the formalized operation before selecting an implementation),
  `OWN-08` (reuse the highest suitable maintained operation),
  `OWN-11` (a missing shared operation is repaired at its owner) and
  `OWN-18` (generic operations live on the weakest sufficient structure).
- A gap that no preamble method supplies is **new mathematics for the preamble,
  not a leaf algorithm**: per
  [New mathematics goes upstream](../CONTRIBUTING.md#new-mathematics-goes-upstream-a-new-algorithm-is-an-engineering-decision),
  it is requested and implemented at its preamble owner, with the
  [integration-code boundary](../CONTRIBUTING.md#integration-code-has-a-specific-job)
  observed — `latticedb` wires existing owned constructions and computes nothing
  of its own.
- The existing record of these prerequisites is
  [COMPLAINTS.md](../COMPLAINTS.md); its `DEV-59` capture/lifecycle rule governs
  new findings, and the preamble's [TODO.md](../TODO.md) schedules repairs.

A migration that replaces a function without its dependency trace, or that ports
hand-rolled code into the leaf instead of the preamble, is not delivered.

## Objective

`latticedb` re-implements the preamble's lattice mathematics instead of consuming it:
`src/latticedb/arithmetic.py` defines 31 invariants over bare
`GramTensor = tuple[tuple[Fraction, ...], ...]`, and `latticedb` imports
`dzack_research` **zero times**. Replace each hand-rolled implementation with the
preamble's owned construction, and migrate the genuine gaps *into* the preamble.

This is a series of small, systematic replacements, not a rewrite. Replace the
computation; keep the card schema, the four workflows and the site.

## Blocker: do not start until these two preamble nodes are delivered

Both are recorded in [COMPLAINTS.md](COMPLAINTS.md) ("The discriminant-quotient
construction fails for every lattice…") with TODO nodes in the preamble's
`TODO.md`. Until they close, the replacement cannot land, because the preamble
methods it targets currently raise on every lattice, including unimodular `U`:

| method | current result |
| --- | --- |
| `L.discriminant_group()`, `L.delta()`, `L.level()`, `L.genus()` | `TypeError: Rational Field / (2)Integer Ring is not a ring` |
| `L.is_isometric(other)` | `KeyError: (0, 1766847064778384329583300423746193477726582719585514895531500160449343182)` |

Preamble nodes: `discriminant-quotient-constructs`,
`lattice-isometry-comparison-joins-categories`.

## Runtime wiring (verified)

- The preamble is installed into Sage as `dzack-research 0.1.1`; `latticedb` is not
  installed into Sage. Both import together when Sage's interpreter is used with
  both `src` roots on the path:

  ```
  PYTHONPATH=/home/dzack/research/src:/home/dzack/research/lattice-database/src \
  /home/dzack/gitclones/sage-dev-allopts/sage -c \
    "from dzack_research.preamble.all import *; import latticedb"
  ```

- Sage's Python is 3.14.7, the same as `lattice-database/.venv`, and already has
  `pydantic`, `frontmatter`, `cypari2`, `flint`.
- `just new|seed|enrich|verify|build` run under `uv run` in the venv, which has no
  `sage`. **Decide the one entry point** before starting: either latticedb runs
  under Sage, or the venv gains the preamble's dependencies. The replacement of
  `arithmetic.py` is impossible under the current plain-CPython entry point.

## Mapping: hand-rolled → preamble

Build the owned lattice from a card's Gram tensor with
`Lattices(ZZ)(<rows>)` (verified: `Lattices(ZZ)([[2,-1],[-1,2]])` gives A2 and
answers `determinant`, `signature_pair`, `is_definite`, `is_even`, `roots`).

| `latticedb/arithmetic.py` | preamble owner | state |
| --- | --- | --- |
| `determinant` | `L.determinant()` | works |
| `inertia` | `L.signature_pair()` | works |
| `is_definite` | `L.is_definite()` | works |
| parity in `is_integer_valued` | `L.is_even()` | works |
| `definite_roots`, `is_root` | `L.roots()`, `L.roots_of_square(n)` | works |
| `discriminant_invariants` | `L.discriminant_group()` | blocked |
| `delta` | `L.delta()` | blocked |
| `level` | `L.level()` | blocked |
| genus methods | `L.genus()` | blocked |
| `is_isometric` | `L.is_isometric(other)` | blocked |
| `overlattice_count` | `L.overlattice(...)` / `L.maximal_overlattice()` / `L.even_overlattice_inclusions()` | blocked |
| `pairing`, `restriction`, `orthogonal_sum`, `scaled`, `scale` | orthogonal sum / subobject / `_lattice.py` routes | map each at its owner |
| `invariant_factors`, `generate`, `span_basis` | free-module / span routes | map each at its owner |
| `minimum_and_kissing_number`, `theta_coefficients` | no method found | **migrate into the preamble** (`DefiniteLattices`) |
| `is_isotropic` | formed/discriminant modules | check the owner |
| `bad_reduction_primes`, `quadratic_character`, `is_perfect`, `overlattice_count`, `generating_norms` | no method found | **migrate into the preamble** |

The "no method found" rows are a source-search boundary, not a proof of absence:
widen to upstream Mathlib/Loogle and the preamble's own `_lattice.py` before
concluding, then migrate the mathematics (not the code) into the preamble at its
category owner, and let latticedb call it.

## Steps

1. **Choose the runtime** (one entry point; see above). Nothing else can start.
2. **Migrate `arithmetic.py` function by function.** After each, delete the
   hand-rolled body and call the preamble through a thin adapter that still takes
   and returns a card's `GramTensor`. One function per commit, with a card-level
   specimen that pins its result.
3. **Migrate the gaps** (`minimum_and_kissing_number`, `theta_coefficients`,
   `bad_reduction_primes`, `quadratic_character`, `is_perfect`, `overlattice_count`,
   `generating_norms`) into the preamble at their owner; latticedb then calls them.
4. **Route `sage_genus.py` through the preamble.** It currently runs as a Sage
   subprocess over raw Gram matrices; its genus symbol, class number, spinor
   genera, hyperbolic index and orbit series are preamble computations. The two
   series are `integral.primitive_orbits` (`F_{L,Γ}`) and
   `integral.discriminant_orbits` (`F_{A_L,Γ}`); keep them distinct.
5. **Replace the cardinal coinage.** `GroupData.cardinality` in
   `src/latticedb/model.py` is `int | Literal["aleph0"] | None` — a leaf-local
   serialization invented because the preamble was unreachable. When the preamble
   is reachable, type it as the preamble's `Cardinal` and parse `aleph0` to
   `aleph0()`; do not keep the literal.
6. **Record the cross-repo finding.** `lattice-database/AGENTS.md` currently
   states the four workflows without mentioning the preamble. Add the contract
   that latticedb consumes the preamble's lattice mathematics and computes none
   of its own; link the complaint.

## Specimens (acceptance)

Each replacement carries a specimen with an independently known value:

- `U = Lattices(ZZ)("U")`: `determinant()` is `-1`, `signature_pair()` is `(1, 1)`,
  `is_definite()` is `False`, `is_even()` is `True`.
- `A2`: `determinant()` is `3`, `roots()` has 6 elements, discriminant group `Z/3`,
  `delta()` is `1`.
- `E8`: `roots()` has 240 elements; `E8.is_isometric(A2)` is `False`.
- A card round-trip: build `Lattices(ZZ)` from one stored card's `gram_tensor`,
  recompute each migrated invariant, and assert it equals the stored value (for
  `3I23 = E8(-2)`: rank 8, determinant 256, `overlattice_count` 19381, and
  `cardinality: aleph0` on its groups).

## Verification

- Run under the chosen runtime, not the plain venv.
- Per the repository rules, the full suite and the 160,781-card site build run
  through `~/ai-review-ci`, never locally; a card-level specimen is the local
  check.
- After migration, `latticedb/arithmetic.py` holds only adapters and card I/O;
  `rg -n "^def " src/latticedb/arithmetic.py` should list no invariant of a lattice.

## Prior state (intake, unchanged by this task)

160,781 permanent cards; 0 source rows in `lattices/source/`; 63 Nebe–Sloane
archive cards without a parsed Gram tensor. Card seeder reads only its source row.
Site reads root cards; verification is scheduled CI. These are unaffected by the
migration and are not re-listed as actions here.
