from fractions import Fraction as F
import sys
sys.setrecursionlimit(10000)
memo={}
def solve(A,budget):
    A=tuple(A)
    key=(A,budget)
    if key in memo: return memo[key]
    if len(A)<=1:
        r=(sum(A), ("base",))
        memo[key]=r; return r
    p1=A[0]; tail=A[1:]
    v1,t1=solve(tail,budget)
    val1=p1/F(2)+v1
    trace1=("move1(halve %s)"%p1,)+t1
    Sj=F(0);jstar=0
    for j in range(1,len(tail)+1):
        s=sum(tail[:j])
        if s<=p1: jstar=j;Sj=s
        else: break
    val2=None; trace2=None
    if jstar>=1:
        r=p1-Sj
        leftover=list(tail[jstar:])
        if r>0: leftover=leftover+[r]
        leftover=tuple(sorted(leftover,reverse=True))
        newbudget=max(budget-1,0)
        if len(leftover)==0:
            v2=F(0); t2=()
        else:
            v2,t2=solve(leftover,newbudget)
        val2=Sj+v2
        trace2=("move2(match top %s vs prefix sum %s, jstar=%d, r=%s)"%(p1,Sj,jstar,r),)+t2
    val3=None; trace3=None
    if len(A)%2==1 and len(A)>=3 and budget>0:
        smallest=A[-1]
        Aprime=tuple(sorted(list(A[:-1])+[smallest/F(2),smallest/F(2)],reverse=True))
        v3,t3=solve(Aprime,budget-1)
        val3=v3
        trace3=("move3(snip %s)"%smallest,)+t3
    options=[(val1,trace1)]
    if val2 is not None: options.append((val2,trace2))
    if val3 is not None: options.append((val3,trace3))
    best=min(options,key=lambda x:x[0])
    memo[key]=best
    return best

A=tuple(sorted([F(26),F(21),F(10)],reverse=True))
val,trace=solve(A,1)
print("value:",val,float(val))
for t in trace:
    print(" ", t)

# count marks: each move1/move3 = 1 mark; move2 costs j*-1 if r==0 else j* (per solve2 model)
marks=0
for t in trace:
    if isinstance(t,str):
        if t.startswith("move1"): marks+=1
        elif t.startswith("move3"): marks+=1
        elif t.startswith("move2"):
            # parse jstar, r
            import re
            m=re.search(r"jstar=(\d+), r=(\S+)\)",t)
            jstar=int(m.group(1)); rstr=m.group(2)
            r=F(rstr)
            cost = jstar if r>0 else jstar-1
            marks+=cost
print("total marks used along winning path:", marks, " vs budget m-1=2")
