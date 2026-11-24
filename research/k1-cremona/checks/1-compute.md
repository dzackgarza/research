Command: `python computations/reports/coble_799-cremona-general-point.py`
inside the Sage image (exit 0 on a fresh run).
Output: seed 2 GOOD SINGULAR SCHEME, factor degree 10, CHOSEN NODES (0,1,2),
three nonzero residual discriminants in the splitting field, and VERIFIED.
Taken with the mathematical theorem in the proof (length 10 at ten distinct
points, plus rational parametrization and delta=10), this certifies the good
special fibre.

For the divisor frame, `coble_797-plane-models.py` also exits 0 and checks
A^2=1, A.G_k=0, A.D=6, 3A-sum G_k=-K_S, G_k.D=2. It proves only integral
arithmetic, not the curve geometry. Exploratory numerical trials and aborted
alternative proofs were not used as evidence.
