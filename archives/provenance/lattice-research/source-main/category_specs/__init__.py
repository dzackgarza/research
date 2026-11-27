"""Category specs for the module redesign.

Importing this package loads the static category specifications.  Phase 1
records the mathematical hierarchy and abstract method surfaces; later phases
install concrete category interceptors and constructor redefinitions.
"""

from importlib import import_module

from .axioms import register_all

register_all()

algebras = import_module("category_specs.algebras")
cat = import_module("category_specs.cat")
forms = import_module("category_specs.forms")
homsets = import_module("category_specs.homsets")
lattices = import_module("category_specs.lattices")
modules = import_module("category_specs.modules")
posets = import_module("category_specs.posets")
rings = import_module("category_specs.rings")
sets = import_module("category_specs.sets")
topological_spaces = import_module("category_specs.topological_spaces")
