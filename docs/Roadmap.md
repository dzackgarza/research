# Project roadmap

The project has two development tracks.
Their current tasks and dependencies are recorded in the [GitHub issue tree](https://github.com/dzackgarza/research/issues/46).

## Sage parity

The base implementation reproduces Sage's mathematical behavior category by category.
Each parity pass compares public operations, normalizations, morphisms, and return values with the corresponding Sage implementation.
The lattice pass supplies the base required by the extension track.

The generated [Sage category framework reference](sage/Sage-Category-Framework-Inventory.md) and [class catalogue](sage/Sage-Category-Classes.md) record the reference surface used by these comparisons.

## Mathematical extensions

The extension implementation imports the parity base and adds mathematics not supplied by Sage.
Its principal subjects are forms over more general base rings, base change and local categories, primitive embeddings and orthogonal complements, arithmetic invariants, and lattices arising from algebraic varieties.

An extension begins only after its prerequisites have stable mathematical definitions and tested public operations in the parity base.
The mathematical definition belongs in the theory chapters; Sage- or Lean-specific representation belongs in the realization chapters.

## Relation between the tracks

Parity establishes a reliable computational reference.
Extensions then generalize from that reference and state every new hypothesis, codomain, and normalization explicitly.
Results that specialize to Sage's setting are compared with the parity implementation.

## Notebook verification

High-level notebooks exercise the public interface by reproducing published lattice arguments.
The intended examples include results of Nikulin, Sterk, Dolgachev--Kondō, and the Enriques-moduli literature.
A notebook records its mathematical source, hypotheses, input construction, and the observable conclusion it reproduces.

The downstream research objective is exact computational support for the Coble and Enriques moduli program.
