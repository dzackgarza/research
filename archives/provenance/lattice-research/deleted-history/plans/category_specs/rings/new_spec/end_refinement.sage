import sys

sys.path.insert(0, '/home/dzack/research')

from plans.category_specs.rings import Rings

RRings = Rings()
NR = RRings.NamedRings()

for R in [NR.ZZ(), NR.QQ()]:
    assert R in RRings
    assert R.End() in RRings
    assert RRings.End(R) in RRings
