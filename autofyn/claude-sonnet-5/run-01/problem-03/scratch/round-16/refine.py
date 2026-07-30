from fractions import Fraction as F
import solve2 as S
from scipy.optimize import minimize, differential_evolution
import numpy as np

def c(k):
    return F(2**k, 2**(k+1)-1)
c3 = float(c(3))

def margin_float(x):
    # x = (t1,t2,t3) fractions of sum after p1 fixed via simplex param
    # use params a>=b>=c>=d>0 sum=1 with a<0.5 via reparam
    p1,t1,t2,t3 = x
    if not (p1>=t1>=t2>=t3>0 and p1<0.5):
        return 10
    A=[F(p1).limit_denominator(100000),F(t1).limit_denominator(100000),F(t2).limit_denominator(100000),F(t3).limit_denominator(100000)]
    S.memo.clear()
    v=float(S.solve2(A,3))
    target = c3*(p1+t1+t2+t3)
    return target-v

def obj(v):
    p1,t1,t2 = v
    t3 = 1-p1-t1-t2
    return margin_float([p1,t1,t2,t3])

res = differential_evolution(obj, bounds=[(0.001,0.4999),(0.001,0.4999),(0.001,0.4999)], seed=1, tol=1e-12, maxiter=500, popsize=40)
print(res.x, res.fun)
p1,t1,t2=res.x
t3=1-p1-t1-t2
print(p1,t1,t2,t3)
