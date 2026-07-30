from fractions import Fraction as F
import random

def solve(A, budget, trace=False, depth=0):
    if len(A) <= 1:
        return sum(A)
    p1 = A[0]
    tail = A[1:]
    val1 = p1/2 + solve(tail, budget)
    best = val1
    bestmove = "move1"
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
        if val2 < best:
            best = val2; bestmove="move2(jstar=%d)"%jstar
    if len(A) % 2 == 1 and len(A) >= 3 and budget > 0:
        smallest = A[-1]
        newA = list(A[:-1]) + [smallest/2, smallest/2]
        newA = tuple(sorted(newA, reverse=True))
        val3 = solve(newA, budget-1)
        if val3 < best:
            best = val3; bestmove="move3"
    if trace:
        print("  "*depth, "A=",[float(x) for x in A],"budget=",budget,"->",float(best), bestmove)
    return best

A = tuple(F(x) for x in [45,40,6,5,4])
print("trace of witness:")
solve(A,1,trace=True)
