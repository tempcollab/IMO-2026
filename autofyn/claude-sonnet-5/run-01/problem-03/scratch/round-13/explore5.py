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

def partial_dom_leftover(A):
    A = tuple(sorted(A, reverse=True))
    p1 = A[0]; tail = A[1:]
    S = F(0); jstar = 0
    for j in range(1, len(tail)+1):
        Snew = S + tail[j-1]
        if p1 >= Snew:
            jstar = j; S = Snew
        else: break
    r = p1 - S
    leftover = list(tail[jstar:])
    if r > 0: leftover.append(r)
    return jstar, S, tuple(sorted(leftover, reverse=True))

random.seed(3)
trials=0
non_casec_leftover_violates_half = 0
non_casec_leftover_ok = 0
worst_margin_noncasec = None
for m in range(3, 11):
    for _ in range(3000):
        vals = [random.random()**2 for _ in range(m)]
        s=sum(vals); vals=[v/s for v in vals]; vals.sort(reverse=True)
        if vals[0] >= 0.5: continue
        Af = [F(v).limit_denominator(400) for v in vals]
        s2=sum(Af); Af=[a/s2 for a in Af]
        if Af[0] >= F(1,2): continue
        trials+=1
        jstar,S,leftover = partial_dom_leftover(Af)
        if len(leftover)<2: continue
        Sigma_left = sum(leftover)
        if Sigma_left==0: continue
        top_left = leftover[0]
        if top_left < Sigma_left/2:
            continue  # is Case C, skip -- IH applies trivially
        # leftover NOT case C -- test if solve(leftover, budget=0 or 1) still <= Sigma_left/2
        v0 = solve(leftover, 0)
        margin0 = Sigma_left/2 - v0
        if margin0 < 0:
            non_casec_leftover_violates_half += 1
        else:
            non_casec_leftover_ok += 1
        if worst_margin_noncasec is None or margin0 < worst_margin_noncasec:
            worst_margin_noncasec = margin0
            worst_ex = (Af, jstar, leftover, v0, Sigma_left)

print("trials:", trials)
print("non-CaseC leftover but solve<=Sigma/2 anyway:", non_casec_leftover_ok)
print("non-CaseC leftover AND solve>Sigma/2 (violates half-bound at recursion!):", non_casec_leftover_violates_half)
print("worst margin among non-CaseC leftovers:", worst_margin_noncasec, float(worst_margin_noncasec) if worst_margin_noncasec is not None else None)
print("example:", worst_ex)
