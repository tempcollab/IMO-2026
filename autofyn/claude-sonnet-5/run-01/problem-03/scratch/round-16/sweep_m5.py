from fractions import Fraction as F
import solve2 as S
from scipy.optimize import differential_evolution
def c(k): return F(2**k,2**(k+1)-1)
c4=float(c(4))

def margin_float(x):
    p1,t1,t2,t3,t4=x
    if not (p1>=t1>=t2>=t3>=t4>0 and p1<sum(x)/2):
        return 10
    A=[F(v).limit_denominator(20000) for v in x]
    S.memo.clear()
    v=float(S.solve2(A,4))
    target=c4*sum(A)
    return target-v

def obj(v):
    p1,t1,t2,t3=v
    t4=1-p1-t1-t2-t3
    return margin_float([p1,t1,t2,t3,t4])

res = differential_evolution(obj, bounds=[(0.001,0.4999)]*4, seed=2, tol=1e-10, maxiter=300, popsize=40)
print(res.x, res.fun)
