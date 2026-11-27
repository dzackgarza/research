import sys

sys.path.insert(0, '/home/dzack/research')

from plans.category_specs.rings import Rings

RRings = Rings()
NR = RRings.Constructors()

for R in [NR.ZZ(), NR.QQ()]:
    assert R in RRings
    assert RRings.EndCategory().Of(R) in RRings.EndCategory()
    assert R.Hom(R) == RRings.EndCategory().Of(R)
