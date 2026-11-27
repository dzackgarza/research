# Regression for set-partition constructor category declarations.

import sys

from sage.rings.integer import Integer

sys.path.insert(0, "/home/dzack/research")

from category_specs.sets import Sets
from category_specs.sets.subcategories.partitioned import PartitionsCategory


constructors = Sets().Constructors()

all_partitions = constructors.SetPartitions()
if all_partitions not in Sets().Countable():
    raise AssertionError("SetPartitions() did not declare Countable membership")
if not issubclass(
    all_partitions.category().parent_class,
    Sets().Countable().parent_class,
):
    raise AssertionError("SetPartitions() parent class does not extend Countable")

fixed_base_partitions = (
    ("iterable base", constructors.SetPartitions(base_set=[1, 2, 3])),
    ("integer base", constructors.SetPartitions(base_set=Integer(3))),
    (
        "finite enumerated base",
        constructors.SetPartitions(
            base_set=constructors.FiniteEnumeratedSet([1, 2, 3])
        ),
    ),
)

for label, partitions in fixed_base_partitions:
    if partitions not in Sets().Partitioned():
        raise AssertionError(f"{label} partitions did not declare Partitioned")
    if partitions not in PartitionsCategory():
        raise AssertionError(f"{label} partitions did not declare PartitionsCategory")
    if not issubclass(
        partitions.category().parent_class,
        Sets().Partitioned().parent_class,
    ):
        raise AssertionError(f"{label} parent class does not extend Partitioned")
    if not issubclass(
        partitions.category().parent_class,
        PartitionsCategory().parent_class,
    ):
        raise AssertionError(
            f"{label} parent class does not extend PartitionsCategory"
        )
