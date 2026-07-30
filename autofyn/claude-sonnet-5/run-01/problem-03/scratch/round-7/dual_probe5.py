from scipy.optimize import minimize
import numpy as np

A1 = [0.4265,0.2536,0.1747,0.1014,0.0438]

def oddrank(vals):
    s = sorted(vals, reverse=True)
    return sum(s[0::2])

def build_B(A, x, y, z1, z2):
    p1,p2,p3,p4,p5 = A
    return [p1*x, p1*(1-x), p2, p3*y, p3*(1-y), p4*z1, p4*(z2-z1), p4*(1-z2), p5]

def obj(v, A):
    x,y,z1,z2 = v
    if not (0<x<1 and 0<y<1 and 0<z1<z2<1):
        return 10
    return oddrank(build_B(A,x,y,z1,z2))

# try hypothesis: y=0 exactly, z1=z2-z1, (1-z2)*p4=p5 exactly => z2 = 1-p5/p4
p1,p2,p3,p4,p5=A1
z2_h = 1-p5/p4
z1_h = z2_h/2
print("z2_h,z1_h", z2_h, z1_h)

# now minimize over x only, with y=0, z1,z2 fixed at hypothesis
def obj_x(x, A):
    return oddrank(build_B(A, x[0], 1e-9, z1_h, z2_h))

from scipy.optimize import minimize_scalar
res = minimize_scalar(lambda x: obj_x([x],A1), bounds=(1e-6,1-1e-6), method='bounded',
                       options={'xatol':1e-14})
print("x*", res.x, res.fun)

# check candidate exact x values
cands = {
 'p3/p1': p3/p1,
 '(p1-p3)/p1': (p1-p3)/p1,
 '1-p2/p1': 1-p2/p1,
 'p2/p1': p2/p1,
}
for k,v in cands.items():
    print(k, v, obj_x([v],A1))
