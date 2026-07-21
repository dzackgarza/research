# Lean and Sage

Lean and Sage realize different parts of the same mathematics. Lean states definitions,
functoriality, coherence, and theorems. Sage supplies data representations and executable
algorithms.

## Mathematical boundary {#sec-layering}

Every implemented notion cites its definition in the theory chapters. Lean declarations
formalize that definition or a stated specialization. Sage classes and methods realize
the corresponding computation. An implementation name does not introduce a second
mathematical definition.

## Existing and missing formalizations {#sec-abc-model}

When Mathlib already contains the required construction, the project uses that
declaration and records the comparison with the book's notation. When a standard result
is absent, it is developed in `ForMathlib/` in a form suitable for upstream contribution.
If a proof is not yet available, the statement and its hypotheses remain explicit; its
proof status is reported with the declaration.

The formalization distinguishes:

- definitions already present in Mathlib;
- local statements intended for Mathlib;
- cited theorems whose formal proofs remain open;
- Sage computations whose correctness is checked by a separate theorem or certificate.

## The `ForMathlib` boundary {#sec-formathlib-layer-contract}

Files under `ForMathlib/` import Mathlib and state generally useful missing mathematics.
Each declaration records the Mathlib location to which it is intended to move. Project
modules may import these files; the reverse import is excluded so the formalization can be
contributed upstream independently.

## The comparison manifest {#sec-registry-semantics}

The comparison manifest links a Lean declaration to its Sage realization when such a
realization exists. A row records the Lean name, the Sage owner, the comparison being
claimed, and the proof or test that supports that claim. Missing analogues are reported
only after searches of Mathlib's declarations and documentation.

## Proof and computation {#sec-cop-out-visibility}

Commutativity, naturality, universal properties, and equivalences are theorem statements.
Finite examples may test an implementation, but they do not prove these statements. Sage
results that admit compact certificates may be checked by Lean or by a separately
specified certified procedure; otherwise their status remains computational.
