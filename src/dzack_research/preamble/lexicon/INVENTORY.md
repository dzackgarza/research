# The lexicon: representation policy, naming rules, obligations

Normative for `src/dzack_research/preamble/lexicon/`. It says how a noun
enters the preamble's type surface, how it is named, and what the subtree
must satisfy at all times. It is not a catalogue: the modules
(`foundations.py`, `algebra.py`, `geometry.py`, `interop.py`) are their own
catalogue, and `__init__.py` is the single import surface.

Provenance: distilled from Parts III–V of the archived spike's
`lexicon/INVENTORY.md` (`computations/archives/sage_lattice_category_spike/`,
retired in the W1 absorption round; git history holds the original). Parts
I–II of that document were an audit and a catalogue of a tree that no longer
exists, and did not survive.

Rules that live elsewhere are cited, never restated here: banned terminology
is the always-on index in `AGENTS.md` plus
`.agents/references/terminology-dictionary.md`; category siting is the
categorical organization model in `AGENTS.md`; Sage typing is the external
package `dzackgarza/sage-stubs`.

## What belongs in the lexicon

Only the preamble's own nouns and the re-exports its own code draws on.
Names for Sage's own objects — `Ring`, `Field`, `Set`, `Vector`,
`FreeModule_generic` — are Sage typing and live in the stub tree. Notions the
preamble owns categorically — `Cardinal`, `Character`, `MorphismMatrix` — are
imported from the categories that define them; re-exporting them here would
make `lexicon` and `categories` import each other.

The dependency runs one way: the lexicon draws on nothing but Sage.

## Representation policy

Priority order when a noun enters:

1. **Owned class wired as category `ParentMethods`** — when the preamble owns
   the mathematics. The typed class and the runtime API are one artifact.
2. **Alias to the Sage implementation class** — when the semantic meaning
   coincides with exactly one Sage class (`Matrix`, `Element`, `Polyhedron`).
   Tightest contract, no drift possible.
3. **Union over enumerated Sage implementation classes** — for dev seams that
   must accept whichever implementation Sage hands back (`SageFreeModule`,
   `SageInfinity`). Extending a union is a one-line catalogued change.
4. **Protocol** — only for external objects the preamble neither owns nor can
   enumerate, where structural typing is the honest statement. A protocol
   shadowing a single concrete class is a defect: alias the class.
5. **NewType over a real class** — parse-witnesses (`GramMatrix`): the codec
   proved a property the class does not encode. A witness must itself be a
   mathematical noun.

`Any` and `object` are not representations. A value that cannot be named by
1–5 means the noun is missing: add it.

A noun with no consumer is untestable, so it is not declared until a
signature needs it. Deferring is the default; the first consumer is the
admission ticket.

## Naming rules

1. A type name is a mathematical noun a researcher would say aloud.
2. Implementation-role vocabulary is banned in type names (`Host`, `Delta`,
   `Like`, `Impl`, `Base` as a suffix, `Mixin`, and the terms in the
   `AGENTS.md` banned-language index). If a class plays an implementation
   role, the docstring says so; the name states the mathematics.
3. The `Sage*` prefix is reserved for `interop.py`: Sage's object exactly
   where it is distinct from the owned object of the same mathematical kind.
   A noun whose only realization is Sage's class is never prefixed.
4. No import-site renames of lexicon nouns. A collision inside one module is
   real information: one of the two is an `interop` noun or a missing entry.
   The one sanctioned exception is a Sage *constructor function* spelled like
   the class it builds — bind the function lowercase (`polyhedron`) and keep
   the noun for the type.
5. Untrusted input to a constructor is `RawX`; a codec turns it into the
   witness `X`. Codecs are the only producers of witnesses.

## Consistency obligations

1. `mypy --strict` passes over the lexicon with `sage-stubs` installed: the
   catalogue type-checks as a collection of declarations.
2. Every Sage identifier a lexicon alias names exists on the running Sage.
   Stubs and aliases are claims about an external system, verified against it
   and never trusted from memory. The verifier for the stub tree belongs to
   `dzackgarza/sage-stubs`, beside the claims it checks.
3. One authority per noun: each name is defined in exactly one lexicon
   module, and `__init__.py` re-exports only.
