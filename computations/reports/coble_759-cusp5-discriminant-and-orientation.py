"""Exact certificate for the marked cusp-five root orbits, in the basis of
coble_759-lift-1314.py (Sterk (4.3.9), p. 24, Fig. 12)."""
from sage.all import ZZ, QQ, matrix, vector, block_diagonal_matrix, CartanMatrix, identity_matrix, gcd

C = CartanMatrix(['E', 8]); U = matrix(ZZ, [[0, 1], [1, 0]])
G = block_diagonal_matrix(U, 2*U, -2*C)
e, f, ep, fp, *a = identity_matrix(ZZ, 12).columns()
A = matrix(ZZ, a).transpose(); abar = (-A*C.inverse()).columns()
delta = e-f; eta = 2*e+2*f+abar[0]
et, ft = e+ep+fp-a[0], f+ep+fp-a[0]
at = [ep-fp, a[1], fp+a[2]] + a[3:]
B = matrix(ZZ, at).transpose(); abart = (2*B*(B.transpose()*G*B).inverse()).columns()
roots = [at[1],at[3],at[4],at[5],at[6],at[7],at[0],abart[7],2*et-at[0],2*et+abart[1]-abart[2],ft-et,et+ft+abart[5]-abart[2],et+ft+abart[0]+abart[7]-abart[2],et+ft+at[2]]
ip = lambda x,y: x*G*y
assert all(v in ZZ**12 for v in [eta]+roots)
assert eta == vector(ZZ,[2,2,0,0,-4,-5,-7,-10,-8,-6,-4,-2])
assert ip(eta,eta)==ip(eta,delta)==0 and gcd(list(eta))==1
assert roots[10] == -delta
assert roots[11] == vector(ZZ,[1,1,3,3,-2,1,2,2,1,0,0,0])
assert roots[12] == vector(ZZ,[1,1,3,4,-2,2,3,4,3,2,1,0])
assert roots[13] == vector(ZZ,[1,1,2,3,-2,0,1,0,0,0,0,0])
for v in roots[11:]:
    assert ip(v,v)==-2 and ip(v,delta)==ip(v,eta)==0
    assert gcd(list(v))==1
projection=lambda v: tuple(ZZ(v[i])%2 for i in [2,3])
assert projection(eta)==(0,0)
assert [projection(v) for v in roots[11:]]==[(1,1),(1,0),(0,1)]
M=matrix(ZZ,[[1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0],[0,0,4,3,6,-2,-2,0,0,0,0,0],[0,0,3,4,6,-2,-2,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0],[0,0,6,6,12,-3,-4,0,0,0,0,0],[0,0,6,6,12,-4,-3,0,0,0,0,0],[0,0,10,10,20,-6,-6,0,0,0,0,1],[0,0,8,8,16,-5,-5,0,0,0,1,0],[0,0,6,6,12,-4,-4,0,0,1,0,0],[0,0,4,4,8,-3,-3,0,1,0,0,0],[0,0,2,2,4,-2,-2,1,0,0,0,0]])
assert M.transpose()*G*M==G and M*M==identity_matrix(ZZ,12)
assert M*delta==delta and M*eta==eta
perm=[8,6,5,4,3,2,7,1,9,10,11,12,14,13]
assert all(M*v==roots[j-1] for v,j in zip(roots,perm))
assert all(M[i,j]%2==0 and M[j,i]%2==0 for i in [2,3] for j in range(4,12))
p=e+f; q=vector(ZZ,[0,0,5,3,0,6,6,10,8,6,4,2])
assert M*p==p and M*q==q
assert ip(delta,p)==ip(delta,q)==ip(p,q)==0 and ip(p,p)==2 and ip(q,q)==12
print('eta =',eta)
for j,v in enumerate(roots[11:],12):
    x,y=projection(v); print(j,v,'projection',(x,y),'q_W',x*y)
print('M preserves Gram, delta, eta, both discriminant blocks and all root labels as specified.')
print('M fixes positive plane in delta-perp, Gram diag(2,12).')
print('Exact certificate passed.')
