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

random.seed(2)
# Test hypothesis: budget=0 alone suffices for even m in Case C
fail_even=0
tot_even=0
worst_even=None
for trial in range(4000):
    m = random.choice([4,6,8,10])
    remaining = F(1)
    vals=[]
    for i in range(m-1):
        num = random.randint(1,999)
        p = F(num,1000)*remaining
        vals.append(p); remaining-=p
    vals.append(remaining)
    A = tuple(sorted(vals, reverse=True))
    Sig=sum(A)
    if A[0] >= Sig/2: continue
    tot_even+=1
    v0 = solve(A,0)
    if v0 > Sig/2:
        fail_even+=1
        m2 = Sig/2-v0
        if worst_even is None or m2<worst_even[0]:
            worst_even=(m2,A,v0)
print("even m: tested",tot_even,"budget0 fails",fail_even, "worst margin", worst_even[0] if worst_even else None)

# odd m
fail_odd=0
tot_odd=0
worst_odd=None
for trial in range(4000):
    m = random.choice([5,7,9,11])
    remaining = F(1)
    vals=[]
    for i in range(m-1):
        num = random.randint(1,999)
        p = F(num,1000)*remaining
        vals.append(p); remaining-=p
    vals.append(remaining)
    A = tuple(sorted(vals, reverse=True))
    Sig=sum(A)
    if A[0] >= Sig/2: continue
    tot_odd+=1
    v0 = solve(A,0)
    if v0 > Sig/2:
        fail_odd+=1
        m2 = Sig/2-v0
        if worst_odd is None or m2<worst_odd[0]:
            worst_odd=(m2,A,v0)
print("odd m: tested",tot_odd,"budget0 fails",fail_odd, "worst margin", worst_odd[0] if worst_odd else None)
if worst_odd: print("example odd fail:", worst_odd)
if worst_even: print("example even fail:", worst_even)
