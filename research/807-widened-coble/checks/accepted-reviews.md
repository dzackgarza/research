# Accepted independent model reviews

Swarm smwrt1msy ended solved with three accepted scoped solutions. This is not the independent Kimi review required by issue acceptance item 2.

## Review-A (m2): accepted

Checks the Z8/Z64 substitutions, projective irreducibility and rationality, A_15 resolutions, E_8 classes and determinant, mod-two roots, lifting to the K3 cover, effectivity and final pushforward contradiction. Report: `.ultramath/smwrt1msy/m2/review-A-verdict.md`. The only wording concern was repaired: affine irreducibility and restriction x^6 on z=0 separately prove that the affine curve is irreducible and that the line at infinity is not a component.

Independent corroboration: checks/e8-root-classes.py enumerates 240 roots in the standard simple-root basis and gives 120 classes modulo 2E8, each one antipodal pair.

## Review-B (m1): accepted after second-round recheck

Checks ordered-node PGL_3 freeness, Grivaux Proposition 3.1, fixed-involution deformations and periods, relative quotients, Picard-general density, Harris–Morrison smoothness and full node monodromy, and the connected/irreducible component conclusion. Report with repair recheck: `.ultramath/smwrt1msy/m1/verdict-review-B.md`.

The first submission was rejected for two write-up requirements and the local-finiteness inequality. The recheck verifies: the tangent calculation proves that the fixed-involution period map is a local biholomorphism onto an open subset of the 9-dimensional domain; HM98 Theorem (1.49)(1) supplies smoothness and irreducibility follows from smoothness plus connectedness; beta(delta) <= c beta_pi(delta) = c|delta|^2 now proves local finiteness. No substantive gap remains in this scope.

## Review-C (m3): accepted after second-round recheck

Checks every Dolgachev–Zhang hypothesis used, the plane-model reduction and ten-double-point count, the reduced/singular/non-reduced distinctions, and the invariant-transport versus universal anti-invariant monodromy scope. Original report: `.ultramath/smwrt1msy/m3/review-C-verdict.md`; accepted repair recheck: `.ultramath/smwrt1msy/m3/review-C-repair-recheck.md`; arithmetic certificate: `.ultramath/smwrt1msy/m3/repair-recheck-certificate.txt`.

The original submission was rejected for a false canonical identity and three weak citations. The recheck verifies all four repairs: -2K_S=pi^*(-2K_Y)-2E; DZ99 §5.1 for the Halphen plane model; the local node/cusp calculation replacing Remark 3.3; and the n>1 rank calculation separated from the n=1 (11,11,1) input at DK13 §3. No substantive gap remains in this scope.

## Coverage boundary

Review-B treats period-surjectivity steps 1–6 and abstract lattice identifications as imported page inputs. Review-C does not re-derive O^+(K^perp)=W(E_10). Those inputs are not silently promoted to a universal-stack monodromy theorem: the published decision is the surface classification and no-new-component statement, while the stack-local-system clause stays conditional as printed in the corollary. The reviews do not constitute the required independent Kimi MET review.
