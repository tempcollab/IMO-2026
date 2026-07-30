from fractions import Fraction as F
from functools import lru_cache
import itertools, sys

sys.setrecursionlimit(10000)

# Re-implement Round-12 "solve(A,budget)" EXACTLY per the certified WF-C5 spec,
# from scratch (my own understanding of the spec text), tracking move traces.

def oddrank(vals):
    # alternating claim value for player who goes first (Liu Bang), sorted desc
    s = sorted(vals, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

memo = {}
def solve(A, budget):
    A = tuple(A)
    key = (A, budget)
    if key in memo:
        return memo[key]
    if len(A) <= 1:
        v = sum(A)
        memo[key] = (v, ("base",))
        return memo[key]
    best_val = None
    best_trace = None
    p1 = A[0]
    tail = A[1:]
    # Move 1: halve p1
    v1, t1 = solve(tail, budget)
    val1 = p1/F(2) + v1
    if best_val is None or val1 < best_val:
        best_val, best_trace = val1, ("move1",)+t1

    # Move 2: partial-dom match maximal prefix S_j <= p1
    # prefix sums of tail
    Sj = F(0)
    jstar = 0
    for j in range(1, len(tail)+1):
        s = sum(tail[:j])
        if s <= p1:
            jstar = j
            Sj = s
        else:
            break
    if jstar >= 1:
        r = p1 - Sj
        leftover = list(tail[jstar:])
        if r > 0:
            leftover = leftover + [r]
        leftover = tuple(sorted(leftover, reverse=True))
        newbudget = max(budget-1, 0)
        if len(leftover) == 0:
            v2 = Sj
            t2 = ()
        else:
            v2, t2 = solve(leftover, newbudget)
        val2 = Sj + v2
        if val2 < best_val:
            best_val, best_trace = val2, ("move2", jstar, r)+t2

    # Move 3: tail-snip, |A| odd, |A|>=3, budget>0
    if len(A) % 2 == 1 and len(A) >= 3 and budget > 0:
        smallest = A[-1]
        Aprime = tuple(sorted(list(A[:-1]) + [smallest/F(2), smallest/F(2)], reverse=True))
        v3, t3 = solve(Aprime, budget-1)
        val3 = v3
        if val3 < best_val:
            best_val, best_trace = val3, ("move3",)+t3

    memo[key] = (best_val, best_trace)
    return memo[key]

def solve_full(A):
    memo.clear()
    A = tuple(sorted(A, reverse=True))
    return solve(A, 1)

# Witness A=(26,21,10)
A = [F(26), F(21), F(10)]
val, trace = solve_full(A)
print("solve_full(26,21,10) =", val, float(val))
print("Sigma/2 =", F(57,2), float(F(57,2)))
print("trace:", trace)

# debug: print top-level branch values
def debug_solve(A, budget, depth=0):
    A = tuple(A)
    print("  "*depth, "solve", A, budget)
    if len(A)<=1:
        print("  "*depth,"-> base", sum(A))
        return sum(A)
    p1=A[0]; tail=A[1:]
    v1=debug_solve(tail,budget,depth+1)
    val1=p1/F(2)+v1
    print("  "*depth,"move1 val=",val1)
    Sj=F(0);jstar=0
    for j in range(1,len(tail)+1):
        s=sum(tail[:j])
        if s<=p1:
            jstar=j;Sj=s
        else:
            break
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
            v2=debug_solve(leftover,newbudget,depth+1)
        val2=Sj+v2
        print("  "*depth,"move2 jstar=",jstar,"r=",r,"val=",val2)
    val3=None
    if len(A)%2==1 and len(A)>=3 and budget>0:
        smallest=A[-1]
        Aprime=tuple(sorted(list(A[:-1])+[smallest/F(2),smallest/F(2)],reverse=True))
        v3=debug_solve(Aprime,budget-1,depth+1)
        val3=v3
        print("  "*depth,"move3 val=",val3)
    vals=[val1]+([val2] if val2 is not None else [])+([val3] if val3 is not None else [])
    best=min(vals)
    print("  "*depth,"-> best",best)
    return best

print("=== debug trace ===")
debug_solve([F(26),F(21),F(10)],1)
