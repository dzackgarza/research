# The rank-2 Shephard groups

**Source**: https://en.wikipedia.org/wiki/Coxeter%E2%80%93Dynkin_diagram, section "Complex reflections"
**Retrieved**: 2025-07-26 (transcribed 2026-08-20 from the full-article capture made by
`literature/tools/webpage_to_markdown.py`)
**Citation Key**: `wikipedia_coxeter_dynkin_2025`
**Revision**: oldid 1290398091 (last edited 14 May 2025), permanent link
https://en.wikipedia.org/w/index.php?title=Coxeter%E2%80%93Dynkin_diagram&oldid=1290398091

**Status in this repository**: outside its scope. Nothing in the preamble
models a unitary reflection or a complex reflection group. The table is kept
because it is the boundary of the Coxeter theory the repository does own: the
same diagrams, with node labels above 2, stop being Coxeter groups.

## The extension

Coxeter–Dynkin diagrams extend to $\mathbb{C}^n$, where a node is a unitary
reflection of period greater than 2. A node's index is the period, and an
index of 2 (an ordinary real reflection) is suppressed. Coxeter writes the
complex group as $p[q]r$.

The symmetry group of a regular complex polygon $p\{q\}r$ in $\mathbb{C}^2$ is
**not** a Coxeter group: it is a *Shephard group*, a kind of complex
reflection group. Its order is

$$\frac{8}{q}\left(\frac{1}{p} + \frac{2}{q} + \frac{1}{r} - 1\right)^{-2}.$$

The group $p_1[q]p_2$ has two generators $R_1, R_2$ with
$R_1^{p_1} = R_2^{p_2} = I$, and

- $q$ even: $(R_2R_1)^{q/2} = (R_1R_2)^{q/2}$;
- $q$ odd: $(R_2R_1)^{(q-1)/2}R_2 = (R_1R_2)^{(q-1)/2}R_1$, and then
  $p_1 = p_2$.

## The fourteen rank-2 groups

| group | order |
|---|---|
| $2[q]2$ | $2q$ |
| $p[4]2$ | $2p^2$ |
| $3[3]3$ | 24 |
| $3[6]2$ | 48 |
| $3[4]3$ | 72 |
| $4[3]4$ | 96 |
| $3[8]2$ | 144 |
| $4[6]2$ | 192 |
| $4[4]3$ | 288 |
| $3[5]3$ | 360 |
| $5[3]5$ | 600 |
| $3[10]2$ | 720 |
| $5[6]2$ | 1200 |
| $5[4]3$ | 1800 |

**Two defects in the source, recorded.** The article lists fourteen groups but
only thirteen orders ("of order $2q$, $2p^2$, 24, 48, 72, 96, 144, 192, 288,
360, 600, 1200, and 1800 respectively"), so the correspondence is off by one
from $3[10]2$ onwards. The missing value is recovered from the article's own
order formula: for $p = 3, q = 10, r = 2$ the bracket is
$\tfrac13 + \tfrac15 + \tfrac12 - 1 = \tfrac1{30}$, so the order is
$\tfrac{8}{10}\cdot 900 = 720$, and the table above is corrected accordingly.
Every other row was checked against the formula and agrees. Separately, a
figure caption in the same section says "12 irreducible Shephard groups",
against the fourteen the text lists; the two counts are not reconciled in the
source. Two of the fourteen rows, $2[q]2$ and $p[4]2$, are families rather
than single groups, which is the likeliest explanation, but the article does
not say so and the count is not used here.
