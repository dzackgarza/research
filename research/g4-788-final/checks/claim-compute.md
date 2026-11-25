# Independent recomputation

Command:

    python3 research/g4-788-final/checks/independent-finite-check.py

Exit status: 0. Full output: independent-finite-check-output.txt in this directory.

The new program constructs an E_8 Cartan form (determinant checked to be 1), enumerates the 1024 elements of the ten-dimensional discriminant block, and checks all pairings. It does not import or reuse the existing index script.

- q=0 on 528 elements and q=1 on 496.
- It enumerates 134912 ordered hyperbolic pairs and 67456 distinct hyperbolic planes; every complement has 256 elements and 136 singular classes, confirming nondegenerate plus type in dimension eight.
- It checks b(w,x)=q(x) mod 1 on all 2048 classes of <w> + A_E10(2), with zero failures.
- Hyperbolic-basis recurrence gives |O_2^+|=2, |O_8^+|=348364800, |O_10^+|=46998591897600, |P|=696729600, and index 67456.
- It computes |H^perp|=2048 and |H^perp/H|=1024.

A first diagram input failed the determinant-one assertion and was corrected before any conclusion was drawn; a second test-harness error reduced q modulo the wrong integer and was also corrected. The final successful output is the evidence used here.
