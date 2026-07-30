from fractions import Fraction as F
import random, sys
sys.setrecursionlimit(10000)
memo={}
def solve(A,budget):
    A=tuple(A); key=(A,budget)
    if key in memo: return memo[key]
    if len(A)<=1:
        memo[key]=sum(A); return memo[key]
    p1=A[0]; tail=A[1:]
    v1=solve(tail,budget)
    val1=p1/F(2)+v1
    Sj=F(0);jstar=0
    for j in range(1,len(tail)+1):
        s=sum(tail[:j])
        if s<=p1: jstar=j;Sj=s
        else: break
    val2=None
    if jstar>=1:
        r=p1-Sj
        leftover=list(tail[jstar:])
        if r>0: leftover=leftover+[r]
        leftover=tuple(sorted(leftover,reverse=True))
        newbudget=max(budget-1,0)
        if len(leftover)==0:
            v2=F(0)
        else:
            v2=solve(leftover,newbudget)
        val2=Sj+v2
    val3=None
    if len(A)%2==1 and len(A)>=3 and budget>0:
        smallest=A[-1]
        Aprime=tuple(sorted(list(A[:-1])+[smallest/F(2),smallest/F(2)],reverse=True))
        val3=solve(Aprime,budget-1)
    vals=[val1]+([val2] if val2 is not None else [])+([val3] if val3 is not None else [])
    best=min(vals)
    memo[key]=best
    return best

random.seed(0)
minexcess=None
for trial in range(3000):
    m = random.randint(1,7)
    vals = sorted([F(random.randint(1,50)) for _ in range(m)], reverse=True)
    budget = random.choice([0,1])
    memo.clear()
    v = solve(vals, budget)
    e = v - sum(vals)/F(2)
    if minexcess is None or e<minexcess:
        minexcess=e
print("min excess found over 3000 random trials:", minexcess, float(minexcess))
