---
edges:
- id: order3
  relation: bond
  source: wall1
  target: wall2
  weight:
    gram: -1/2
    order: 3
- id: cusp
  relation: bond
  source: wall2
  target: wall3
  weight:
    gram: '-1'
    order: infinity
name: Hyperbolic triangle (2,3,infinity)
properties:
- Coxeter
- rational Coxeter–Vinberg
slug: hyperbolic-triangle-2-3-infinity
vertices:
- id: wall1
  weight:
    norm_squared: 1
- id: wall2
  weight:
    norm_squared: 1
- id: wall3
  weight:
    norm_squared: 1
---

The Gram matrix has diagonal entries 1 and off-diagonal entries -1/2, -1 and 0. It has signature (2,1), so these reflecting walls give a hyperbolic Coxeter triangle with angles pi/2, pi/3 and 0.