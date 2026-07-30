from fractions import Fraction as F
import solve2 as S
import random

def c(k):
    return F(2**k, 2**(k+1)-1)

def margin_float(p1,t1,t2,t3):
    A = [F(p1).limit_denominator(2000), F(t1).limit_denominator(2000), F(t2).limit_denominator(2000), F(t3).limit_denominator(2000)]
    S.memo.clear()
    v = S.solve2(A,3)
    target = c(3)*sum(A)
    return float(target - v)

# random search over Case C m=4 configs (float, coarse)
best = None
random.seed(1)
N=3000
worst=[]
for _ in range(N):
    # generate descending p1>t1>=t2>=t3>0, sum=1, p1<0.5
    while True:
        xs = sorted([random.random() for _ in range(4)], reverse=True)
        s=sum(xs)
        xs=[x/s for x in xs]
        p1,t1,t2,t3=xs
        if p1<0.5:
            break
    A=[F(p1).limit_denominator(500),F(t1).limit_denominator(500),F(t2).limit_denominator(500),F(t3).limit_denominator(500)]
    S.memo.clear()
    v=S.solve2(A,3)
    target=c(3)*sum(A)
    m=float(target-v)
    worst.append((m,p1,t1,t2,t3))

worst.sort()
for w in worst[:15]:
    print(w)
