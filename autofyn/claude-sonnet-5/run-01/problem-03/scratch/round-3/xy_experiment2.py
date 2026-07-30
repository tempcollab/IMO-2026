import random
import numpy as np

def oddrank(vals):
    vals = sorted(vals, reverse=True)
    return sum(vals[0::2])

def c(n):
    return 2**n/(2**(n+1)-1)

def dom_full(A, k):
    A = sorted(A, reverse=True)
    p1 = A[0]
    tail = sorted(A[1:], reverse=True)
    k = min(k, len(tail))
    matched = tail[:k]
    r = p1 - sum(matched)
    parts = matched + ([r] if r > 1e-15 else [])
    return parts + tail

def halve_top(A):
    A = sorted(A, reverse=True)
    p1 = A[0]
    return [p1/2, p1/2] + A[1:]

def best_discrete2(A, budget, memo=None):
    if memo is None: memo = {}
    A = sorted(A, reverse=True)
    if len(A) == 0:
        return 0.0
    key = (tuple(round(x,9) for x in A), budget)
    if key in memo: return memo[key]
    best = oddrank(A)  # do-nothing baseline
    if budget > 0:
        # halve top
        best = min(best, oddrank_via(halve_top(A), budget-1, memo))
        # dom-full with k=1..budget
        if len(A) > 1:
            maxk = min(budget, len(A)-1)
            for k in range(1, maxk+1):
                best = min(best, oddrank_via(dom_full(A,k), budget-k, memo))
    # peel (free, no marks) if applicable
    if len(A) >= 2:
        p1, p2 = A[0], A[1]
        tail = A[2:]
        if (not tail or p2 >= max(tail)) :
            peeled_val = p1 + best_discrete2(tail, budget, memo)
            best = min(best, peeled_val)
    memo[key] = best
    return best

def oddrank_via(A, budget, memo):
    return best_discrete2(A, budget, memo)

random.seed(5); np.random.seed(5)
for n_marks in [2,3]:
    worst_ratio = 0; worst_case=None
    for trial in range(3000):
        m = random.choice([1,2,3,4]) if n_marks==3 else random.choice([1,2,3])
        raw = [random.random()**random.choice([1,3,6,10]) for _ in range(m)]
        A = sorted([x/sum(raw) for x in raw], reverse=True)
        memo={}
        val = best_discrete2(A, n_marks, memo)
        ratio = val/c(n_marks)
        if ratio > worst_ratio:
            worst_ratio = ratio; worst_case=(A[:], val)
    print(f"n={n_marks} worst ratio:", worst_ratio, worst_case)
