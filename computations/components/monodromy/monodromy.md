```python
from sage.all import *

R.<t,x,y> = QQ[]
f = y^2 - x^3 + t
D = f.resultant(f.derivative(y), y).factor()   # up to a scalar, x^3 - t

A.<t,x> = AffineSpace(QQ, 2)
C = Curve(x^3 - t, A)

bm = C.braid_monodromy()   # needs sirocco
bm
```

```python
from sage.all import *
from sage.interfaces.singular import singular

singular.eval('LIB "mondromy.lib";')
singular.eval('ring R=0,(x,y),ds;')
singular.eval('poly g = x3 - y2;')          # y^2 = x^3 - t  <=>  g(x,y)=t
print(singular.eval('matrix M = monodromyB(g); M;'))
# assert M == Matrix(QQ, 2, [[7/6, 0], [0, 5/6]])
# Mp = e^(-2pi * I * M) 
# assert Mp.eigenvalues() == [e^(-I*pi/3), e^(I*pi/3)}]
# assert Mp.is_conjugate_to( Matrix(ZZ, 2, [0, -1, 1, 1]))
```
