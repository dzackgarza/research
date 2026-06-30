# Sage Reference Coverage

The structured source is `reference_manifest.py`.

| Sage locus | Classification | Contract |
| --- | --- | --- |
| `free_quadratic_module_integer_symmetric.py` | `adapted` | Constructors, overlattices, local modification, and explicit isometry-generator action are local contracts. |
| `free_quadratic_module.py` | `synthetic-superseded` | Synthetic rationalization replaces Sage ambient-module APIs. |
| `torsion_quadratic_module.py` | `adapted` | Even genus, finite form isomorphism, and orthogonal group behavior are adapted; odd genus is explicitly unsupported. |
| `fgp_module.py` | `adapted` | Finite Smith quotient methods are adapted on discriminant groups and lattice finite quotients. |
| `free_module.py` | `irrelevant-generic` | Generic free-module APIs are not independently owned beyond the promoted lattice surface. |
| `free_module_integer.py` | `rejected-parity` | Ordinary quotient-module and broad integer free-module parity remain outside the accepted contract. |

No row is `pending-gap`; tests enforce that accepted symbols and adapted test names stay covered by this manifest.
