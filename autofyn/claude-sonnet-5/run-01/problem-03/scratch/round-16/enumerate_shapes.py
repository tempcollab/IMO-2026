from fractions import Fraction as F
import solve2 as S
import random
from collections import Counter

def c(k): return F(2**k,2**(k+1)-1)

def solve2_trace(A, marks):
    A = tuple(sorted(A, reverse=True))
    if len(A)==0 or marks==0:
        return S.oddrank(A), ('stop',)
    best = (S.oddrank(A), ('stop',))
    run = S.find_tied_run(A)
    if run is not None:
        i,j=run
        runlen=j-i; val=A[i]; contrib=(runlen//2)*val
        rest = A[:i]+A[j:]
        v,path = solve2_trace(rest, marks)
        v2=contrib+v
        if v2<best[0]: best=(v2, ('M0',)+path)
    if marks>=1 and len(A)>=1:
        p1=A[0]
        rest=list(A[1:])+[p1/2,p1/2]
        v,path = solve2_trace(rest, marks-1)
        if v<best[0]: best=(v, ('M1',)+path)
    if len(A)>=1:
        p1=A[0]; tail=list(A[1:])
        cum=F(0)
        for jj in range(1,len(tail)+1):
            cum+=tail[jj-1]; s_sum=cum
            if s_sum>p1: break
            r=p1-s_sum
            if r>0:
                cost=jj
                if cost<=marks:
                    leftover=tail[jj:]+[r]
                    v,path=solve2_trace(leftover, marks-cost)
                    v2=cum+v
                    if v2<best[0]: best=(v2, (f'M2j{jj}',)+path)
            else:
                cost=jj-1
                if cost<=marks and cost>=0:
                    leftover=tail[jj:]
                    v,path=solve2_trace(leftover, marks-cost)
                    v2=cum+v
                    if v2<best[0]: best=(v2,(f'M2tie{jj}',)+path)
    if marks>=1 and len(A)>=1:
        pm=A[-1]
        rest=list(A[:-1])+[pm/2,pm/2]
        v,path=solve2_trace(rest, marks-1)
        if v<best[0]: best=(v,('M3',)+path)
    return best

random.seed(3)
cnt=Counter()
worst_by_shape={}
for _ in range(6000):
    while True:
        xs=sorted([random.random() for _ in range(4)],reverse=True)
        s=sum(xs); xs=[x/s for x in xs]
        p1=xs[0]
        if p1<0.5: break
    A=[F(v).limit_denominator(300) for v in xs]
    S_ = S
    v,path = solve2_trace(A,3)
    cnt[path]+=1
    target=c(3)*sum(A)
    m=target-v
    if path not in worst_by_shape or m<worst_by_shape[path][0]:
        worst_by_shape[path]=(m,A)

for shape,n in cnt.most_common(30):
    m,A = worst_by_shape[shape]
    print(n, shape, 'min_margin=',float(m), A)
