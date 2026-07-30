from fractions import Fraction as F
import random, itertools

def solve(A, budget, memo=None):
    # A: tuple sorted descending, exact Fractions
    A = tuple(sorted(A, reverse=True))
    if len(A) == 1:
        return A[0]
    cands = []
    # Move 1: halve top
    p1 = A[0]
    tail = A[1:]
    cands.append(p1/2 + solve(tail, budget))
    # Move 2: partial-dom maximal prefix match
    # S_j = sum of first j elements of tail
    S = F(0)
    jstar = 0
    for j in range(1, len(tail)+1):
        Snew = S + tail[j-1]
        if p1 >= Snew:
            jstar = j
            S = Snew
        else:
            break
    r = p1 - S
    leftover = list(tail[jstar:])
    if r > 0:
        leftover.append(r)
    leftover = tuple(leftover)
    if len(leftover) == 0:
        val2 = S
    else:
        val2 = S + solve(leftover, max(budget-1,0))
    cands.append(val2)
    # Move 3: tail-snip, only when |A| odd and budget>0
    if len(A) % 2 == 1 and len(A) >= 3 and budget > 0:
        last = A[-1]
        Aprime = list(A[:-1]) + [last/2, last/2]
        cands.append(solve(tuple(Aprime), budget-1))
    return min(cands)

def solve_full(A):
    return solve(tuple(A), 1)

# Test HALF-BOUND on random Case C configs, focusing on "tail locally dominant" regime
random.seed(1)
worst_margin = None
worst_A = None
trials = 0
violations = 0
for m in range(4, 10):
    for _ in range(300):
        # generate random positive reals, normalize
        vals = [random.random()**2 for _ in range(m)]
        s = sum(vals)
        vals = [v/s for v in vals]
        vals.sort(reverse=True)
        p1 = vals[0]
        if p1 >= 0.5:
            continue
        # check tail locally dominant: p2 >= R2/2
        R2 = sum(vals[1:])
        if vals[1] < R2/2:
            continue  # only interested in tail-dominant regime
        # convert to Fraction via rounding
        Af = [F(v).limit_denominator(2000) for v in vals]
        s2 = sum(Af)
        Af = [x/s2 for x in Af]
        trials += 1
        val = solve_full(Af)
        Sigma = sum(Af)
        margin = Sigma/2 - val
        if margin < 0:
            violations += 1
            print("VIOLATION", m, Af, val, Sigma/2)
        if worst_margin is None or margin < worst_margin:
            worst_margin = margin
            worst_A = Af

print("trials in tail-dominant regime:", trials, "violations:", violations)
print("worst margin:", worst_margin, float(worst_margin) if worst_margin is not None else None)
print("worst A:", worst_A)
