# foliation.lib: Reusable Specialized Procedures

**Criterion:** A procedure warrants extraction/reuse iff it is (1) central to actual
algebraic geometry practice, and (2) not trivially recoverable from standard Sage/Julia
primitives.

Under this criterion, the genuinely valuable parts of foliation.lib are the
Hodge-theoretic and Gauss-Manin computations — not the small combinatorial helpers
(e.g., Monomials, RandomPoly, GoodMinor, InsertNew) which are trivial or easily
replaced.

## Summary

The real value of foliation.lib is **not** generic algebra utilities.
Its value is **explicit computational Hodge theory for hypersurfaces**: periods,
Gauss-Manin, Picard-Fuchs, Hodge numbers, Hodge cycles, and Hodge loci.

If extracting a reusable core, start from: HodgeNumber, MixedHodgeFermat, PeriodMatrix,
BasisHodgeCycles, HodgeLocusIdeal, SmoothReduced, InterTang, DeformSpace,
gaussmaninmatrix, PFequ, and sysdif.

* * *

## Mixed Hodge Structure

- **MixedHodgeFermat** — foliation.lib:2321 Mixed Hodge structure data for affine Fermat
  varieties. Highly nontrivial; not standard-library composition.

- **HodgeNumber** — foliation.lib:2369 Hodge numbers for hypersurfaces, especially in
  the explicit Fermat/hypersurface setting.
  Central AG functionality.

## Periods and Intersection Forms

- **PeriodMatrix** — foliation.lib:2400 Explicit period data, not available from
  standard CAS workflows.

- **IntersectionMatrix** — foliation.lib:2643 Explicit intersection data for the same
  setting.

- **Matrixpij** — foliation.lib:2685 Auxiliary matrix for period computation; paired
  with PeriodMatrix.

## Hodge Cycles and Cohomology Decomposition

- **DimHodgeCycles** — foliation.lib:2480
- **BasisHodgeCycles** — foliation.lib:2577
- **TranCoho** — foliation.lib:2724
- **LinearCoho** — foliation.lib:2809

Genuinely specialized tools for decomposing cohomology and studying Hodge classes.

## Explicit Cycle-Period Calculations

- **PeriodLinearCycle** — foliation.lib:2892
- **ListPeriodLinearCycle** — foliation.lib:4220
- **SumTwoLinearCycle** — foliation.lib:3067
- **SumThreeLinearCycle** — foliation.lib:4425
- **mTwoLinearCycle** — foliation.lib:4313
- **mLinearCycle** — foliation.lib:4620

Package explicit cycle-period calculations that are very specific and not
standard-toolbox material.

## Noether-Lefschetz Loci and Explicit Algebraic Cycles

- **CodComInt** — foliation.lib:2946
- **CodComIntZar** — foliation.lib:3020
- **CodRuledCubic** — foliation.lib:4777
- **CodQuarticScroll** — foliation.lib:4831
- **CodVeronese** — foliation.lib:4903
- **TwoCI** — foliation.lib:5051

Specialized and potentially reusable for Noether-Lefschetz-type loci and explicit
algebraic cycles in hypersurfaces.

## IVHS / Hodge Locus (most distinctive from AG perspective)

- **HodgeLocusIdeal** — foliation.lib:3655
- **SmoothReduced** — foliation.lib:3739
- **EquHodge** — foliation.lib:3997
- **InterTang** — foliation.lib:4689
- **DeformSpace** — foliation.lib:4972
- **ConstantRank** — foliation.lib:3132
- **DistinctHodgeLocus** — foliation.lib:4499

Serious IVHS/Hodge-locus tools, not generic utility code.
This is probably the most distinctive part of the library from an AG point of view.

## Gauss-Manin / Picard-Fuchs (differential equation side)

- **gaussmanin** — foliation.lib:1503
- **gaussmaninvf** — foliation.lib:1606
- **gaussmaninmatrix** — foliation.lib:1875
- **PFequ** — foliation.lib:1717
- **PFeq** — foliation.lib:1984
- **sysdif** — foliation.lib:2143
- **dbeta** — foliation.lib:2047

Explicit Gauss-Manin / Picard-Fuchs computation is specialized infrastructure that
standard Sage/Julia workflows do not trivially provide.

* * *

## Explicitly Excluded (not worth extracting)

Monomials, RandomPoly, GoodMinor, InsertNew, and similar small combinatorial helpers are
trivial or easily replaced by standard primitives.
They do not meet the dual criterion of being both central to AG practice and
non-trivially recoverable.
