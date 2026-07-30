from fractions import Fraction as F
import random

def solve(A, budget):
    if len(A) <= 1:
        return sum(A)
    p1 = A[0]
    tail = A[1:]
    best = p1/2 + solve(tail, budget)
    prefsum = []
    s = F(0)
    for x in tail:
        s += x
        prefsum.append(s)
    jstar = 0
    for j in range(1, len(tail)+1):
        if prefsum[j-1] <= p1:
            jstar = j
        else:
            break
    if jstar >= 1:
        Sj = prefsum[jstar-1]
        leftover = list(tail[jstar:])
        r = p1 - Sj
        if r > 0:
            leftover.append(r)
        leftover = tuple(sorted(leftover, reverse=True))
        val2 = Sj + solve(leftover, max(budget-1,0))
        best = min(best, val2)
    if len(A) % 2 == 1 and len(A) >= 3 and budget > 0:
        smallest = A[-1]
        newA = list(A[:-1]) + [smallest/2, smallest/2]
        newA = tuple(sorted(newA, reverse=True))
        val3 = solve(newA, budget-1)
        best = min(best, val3)
    return best

# construct explicit cascading-dominance families: p_i = (1/2 - eps)*R_i for each i (each element just under half its own remaining sum)
def cascade(m, eps):
    eps = F(eps)
    vals = []
    remaining = F(1)
    for i in range(m-1):
        p = (F(1,2)-eps)*remaining
        vals.append(p)
        remaining -= p
    vals.append(remaining)
    return tuple(sorted(vals, reverse=True))

for m in range(4,16):
    for epsnum in [1,5,20]:
        A = cascade(m, F(1,10**epsnum if epsnum<10 else 1000))
        # simpler: eps = 1/(10*epsnum)
        eps = F(1,50*epsnum)
        A = cascade(m, eps)
        Sig = sum(A)
        if A[0] >= Sig/2: 
            continue
        v = solve(A,1)
        margin = Sig/2 - v
        print(f"m={m} eps={eps} margin={float(margin):.6g}", "VIOLATION" if margin<0 else "")

print("=== random hunt m up to 18 ===")
random.seed(7)
worst=None
cnt=0
for trial in range(1500):
    m = random.randint(10,18)
    remaining=F(1)
    vals=[]
    for i in range(m-1):
        num=random.randint(1,999)
        p=F(num,1000)*remaining
        vals.append(p); remaining-=p
    vals.append(remaining)
    A=tuple(sorted(vals,reverse=True))
    Sig=sum(A)
    if A[0]>=Sig/2: continue
    cnt+=1
    v=solve(A,1)
    margin=Sig/2-v
    if worst is None or margin<worst[0]:
        worst=(margin,A,v,m)
print("tested",cnt,"trials, worst margin:",float(worst[0]) if worst else None)
if worst and worst[0]<0:
    print("VIOLATION FOUND", worst)
