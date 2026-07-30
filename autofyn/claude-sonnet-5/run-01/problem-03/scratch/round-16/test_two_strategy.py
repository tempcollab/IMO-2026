from fractions import Fraction as F
import random
def c(k): return F(2**k,2**(k+1)-1)

def strategyA(p1,t1,t2,t3):
    # peel t1 against p1 (match, j=1), cost1, leftover = [t2,t3,r], bound by c(2)*Sigma(leftover)
    if t1> p1: return None  # can't match full t1 if t1>p1 (r would be negative) -- actually need r=p1-t1>=0
    r = p1-t1
    if r<0: return None
    leftover_sum = t2+t3+r
    return t1 + c(2)*leftover_sum

def strategyB(p1,t1,t2,t3):
    # halve p1, bound tail (t1,t2,t3) by c(2)*Sigma(tail)
    tail_sum = t1+t2+t3
    return p1/2 + c(2)*tail_sum

def strategyC(p1,t1,t2,t3):
    # TAIL-SNIP on smallest overall (works when m odd..A has m=4 even, doesn't directly apply as closed form to whole A)
    return None

random.seed(4)
worst=None
viol=0
N=20000
for _ in range(N):
    while True:
        xs=sorted([random.random() for _ in range(4)],reverse=True)
        s=sum(xs); xs=[x/s for x in xs]
        p1=xs[0]
        if p1<0.5: break
    p1,t1,t2,t3=[F(v).limit_denominator(400) for v in xs]
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
