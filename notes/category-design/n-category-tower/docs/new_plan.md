<!--
Origin: gitclones/integral_lattice/cat/docs/new_plan.md
Copied 2026-08-20 by the integral_lattice enrichment migration
(PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.

This is a DESIGN RECORD: it states an intended interface, not the built
preamble. Divergences and recorded errors are listed in the INDEX.md of
this corpus.
-->

# Scaffolding categories

New plan:

First, one needs to define a raw category, raw elements, and raw objects (no morphisms):

```python
class Arrow(ABC): ...
class mn1_Arrow(Arrow): ... # Elements
class m0_Arrow(Arrow): ... # Objects
class mn_Arrow(Arrow): ... # Morphisms

# -------------------
# Distinctly separate objects from morphisms.
# -------------------
class wCategory:
    objects: type[m0_Arrow] # Class representing X in C
    morphisms: type[Hom_wCategory] # Class representing f in Hom_C(X,Y)

class Hom_wCategory(wCategory):
    objects: type[mn_Arrow]
    morphisms: type[Hom_wCategory] # Can be empty or terminal

class EmptyObject(m0_Arrow):
    data = {}

class TrivialObject(m0_Arrow):
    data = {0}

E_0 = EmptyObject()
T_0 = TrivialObject()

E = Empty_wCategory()
T = Terminal_wCategory()

class Empty_wCategory(Hom_wCategory):
    objects = E_0
    morphisms = E

class Terminal_wCategory(Hom_wCategory):
    objects = T_0
    morphisms = T

```



```python

class Connective_wCategory(wCategory):
    objects: type[_Object]
    morphisms: type[Hom_wCategory]

    """
    A category that is not explicitly a hom category.
    Derived notions:
    C.morphisms() = Hom_wCategory.objects()
    C.two_morphisms() = Hom_wCategory.morphisms()
    ...
    C.n_morphisms(n) = Hom_wCategory.n_morphisms(n-1)
    """


```

