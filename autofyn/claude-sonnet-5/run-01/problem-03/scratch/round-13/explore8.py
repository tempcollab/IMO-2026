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

random.seed(7)
neq0 = 0
total=0
worst=None
for m in range(4, 13):
    for _ in range(400):
        vals=[random.randint(1,10**6) for _ in range(m)]
        if len(set(vals))<m: continue
        vals.sort(reverse=True)
        Af=[F(v) for v in vals]
        s=sum(Af)
        if Af[0]*2>=s: continue
        total+=1
        e = solve(Af,1) - s/2
        if e!=0:
            neq0+=1
            if worst is None or abs(e)>abs(worst[0]):
                worst=(e,m,Af)
print("total tested:",total,"nonzero excess count:",neq0)
if worst:
    print("worst nonzero example:", worst[1], [float(x) for x in worst[2]], float(worst[0]))
else:
    print("ALL EXACT ZERO -- solve_full(A) == Sigma(A)/2 identically on every Case-C test")
