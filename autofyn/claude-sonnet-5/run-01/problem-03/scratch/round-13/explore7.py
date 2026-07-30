from fractions import Fraction as F
import random

def solve(A, budget):
    A = tuple(sorted(A, reverse=True))
    if len(A) == 1:
        return A[0]
    p1 = A[0]; tail = A[1:]
    v1 = p1/2 + solve(tail, budget)
    S = F(0); jstar=0
    for j in range(1,len(tail)+1):
        Snew = S+tail[j-1]
        if p1>=Snew:
            jstar=j; S=Snew
        else: break
    r = p1-S
    leftover = list(tail[jstar:])
    if r>0: leftover.append(r)
    leftover = tuple(leftover)
    v2 = S if len(leftover)==0 else S+solve(leftover, max(budget-1,0))
    cands=[v1,v2]
    if len(A)%2==1 and len(A)>=3 and budget>0:
        last=A[-1]
        Aprime=tuple(sorted(list(A[:-1])+[last/2,last/2],reverse=True))
        cands.append(solve(Aprime,budget-1))
    return min(cands)

def excess(A,budget):
    return solve(A,budget) - sum(A)/2

random.seed(42)
for trial in range(8):
    m = random.choice([4,5,6,7])
    vals = [random.randint(1,997) for _ in range(m)]
    while len(set(vals))<len(vals):
        vals = [random.randint(1,997) for _ in range(m)]
    vals.sort(reverse=True)
    Af = [F(v) for v in vals]
    s = sum(Af)
    if Af[0]*2 >= s:
        continue
    e = excess(Af,1)
    print(m, [float(a/s) for a in Af], "excess=",e, float(e), "margin(vs Sigma/2)=", float(-e))

print("---- targeted tests ----")
tests = [
    [F(499,1000), F(498,1000), F(3,1000)],
    [F(4999,10000), F(4998,10000), F(3,10000)],
    [F(1,2)-F(1,1000), F(1,2)-F(2,1000), F(3,1000)],
    [F(9,20), F(8,20), F(2,20), F(1,20)],
    [F(1,1000)]+[F(999,3000)]*3,
    [F(100),F(99),F(1)],
]
for A in tests:
    s=sum(A)
    if A[0]*2>=s:
        print("not Case C, skip", A); continue
    e=excess(A,1)
    print(A, "sum=",s,"excess=",e,"solve=",float(sum(A)/2+e)," Sigma/2=",float(s/2))
