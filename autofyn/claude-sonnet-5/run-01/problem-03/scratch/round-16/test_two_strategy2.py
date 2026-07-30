from fractions import Fraction as F
import random
import solve2 as S
def c(k): return F(2**k,2**(k+1)-1)

def strategyA(p1,t1,t2,t3):
    if t1> p1: return None
    r = p1-t1
    leftover=[t2,t3,r]
    S.memo.clear()
    return t1 + S.solve2(leftover,2)

def strategyB(p1,t1,t2,t3):
    tail=[t1,t2,t3]
    S.memo.clear()
    return p1/2 + S.solve2(tail,2)

random.seed(4)
worst=None
viol=0
N=8000
for _ in range(N):
    while True:
        xs=sorted([random.random() for _ in range(4)],reverse=True)
        s=sum(xs); xs=[x/s for x in xs]
        p1=xs[0]
        if p1<0.5: break
    p1,t1,t2,t3=[F(v).limit_denominator(300) for v in xs]
    target=c(3)*(p1+t1+t2+t3)
    cands=[]
    a=strategyA(p1,t1,t2,t3)
    if a is not None: cands.append(a)
    b=strategyB(p1,t1,t2,t3)
    cands.append(b)
    val=min(cands)
    m=target-val
    if worst is None or m<worst[0]:
        worst=(m,p1,t1,t2,t3,val,target)
    if m<0:
        viol+=1

print('violations', viol, 'of', N)
print('worst', worst, float(worst[0]))
