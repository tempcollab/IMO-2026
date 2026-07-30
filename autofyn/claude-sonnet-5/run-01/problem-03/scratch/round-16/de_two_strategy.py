from fractions import Fraction as F
import solve2 as S
from scipy.optimize import differential_evolution
def c(k): return F(2**k,2**(k+1)-1)
c3=float(c(3))

def strategyA(p1,t1,t2,t3):
    if t1>p1: return None
    r=p1-t1
    leftover=[t2,t3,r]
    S.memo.clear()
    return float(t1 + S.solve2(leftover,2))

def strategyB(p1,t1,t2,t3):
    tail=[t1,t2,t3]
    S.memo.clear()
    return float(p1/2 + S.solve2(tail,2))

def margin(x):
    p1,t1,t2=x
    t3=1-p1-t1-t2
    if not (p1>=t1>=t2>=t3>0 and p1<1/2):
        return 10
    P=F(p1).limit_denominator(20000); T1=F(t1).limit_denominator(20000); T2=F(t2).limit_denominator(20000); T3=F(t3).limit_denominator(20000)
    target = c3*float(P+T1+T2+T3)
    cands=[]
    a=strategyA(P,T1,T2,T3)
    if a is not None: cands.append(a)
    cands.append(strategyB(P,T1,T2,T3))
    val=min(cands)
    return target-val

res = differential_evolution(margin, bounds=[(0.001,0.4999)]*3, seed=7, tol=1e-13, maxiter=400, popsize=40)
print(res.x, res.fun)
