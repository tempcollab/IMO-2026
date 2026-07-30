import itertools, random
import numpy as np
from scipy.optimize import minimize

def oddrank(vals):
    vals = sorted(vals, reverse=True)
    return sum(vals[0::2])

def split_piece(p, k):
    # returns k+1 positive parts summing to p, parameterized by k free fractions in (0,1)
    # we'll parameterize via cumulative sigmoid-like fractions
    pass

def eval_config(A, mark_dist, params):
    # A: list of pieces (sorted desc), mark_dist: list same length, marks per piece
    # params: flat array, for each piece with k marks we need k values (fractions of remaining) to split into k+1 parts
    idx = 0
    all_parts = []
    for p, k in zip(A, mark_dist):
        if k == 0:
            all_parts.append(p)
            continue
        # use k raw values in (0,1) via sigmoid, sorted, as cut points along [0,p]
        raw = params[idx:idx+k]
        idx += k
        fracs = 1/(1+np.exp(-raw))  # in (0,1)
        cuts = sorted(fracs)
        cuts = [0.0] + cuts + [1.0]
        parts = [p*(cuts[i+1]-cuts[i]) for i in range(len(cuts)-1)]
        all_parts.extend(parts)
    return oddrank(all_parts)

def optimize_for_dist(A, mark_dist, n_restarts=8):
    total_marks = sum(mark_dist)
    if total_marks == 0:
        return oddrank(A)
    best_val = None
    best_parts = None
    for _ in range(n_restarts):
        x0 = np.random.randn(total_marks)*2
        res = minimize(lambda x: eval_config(A, mark_dist, x), x0, method='Nelder-Mead',
                        options={'xatol':1e-10,'fatol':1e-12,'maxiter':5000})
        val = res.fun
        if best_val is None or val < best_val:
            best_val = val
    return best_val

def all_mark_dists(m, n):
    # distribute n marks among m pieces (each piece 0..n), sum = n (Xiang Yu can use up to n, but using all weakly helps or is neutral; enumerate <=n too)
    results = []
    for combo in itertools.product(range(n+1), repeat=m):
        if sum(combo) <= n:
            results.append(combo)
    return results

def best_response(A, n, n_restarts=6):
    m = len(A)
    best_val = None
    best_dist = None
    for dist in all_mark_dists(m, n):
        val = optimize_for_dist(A, dist, n_restarts=n_restarts)
        if best_val is None or val < best_val:
            best_val = val
            best_dist = dist
    return best_val, best_dist

def c(n):
    return 2**n/(2**(n+1)-1)

random.seed(1)
np.random.seed(1)

print("c(2) =", c(2), " c(3)=", c(3))

configs = [
    [0.9862,0.0081,0.0057],
    [0.9977,0.00223,0.0000518],
    [0.7,0.2,0.1],
    [0.5,0.3,0.2],
    [0.4,0.35,0.25],
    [0.6,0.25,0.15],
    [0.99,0.005,0.005],
    [0.8,0.15,0.05],
]

for A in configs:
    A = sorted(A, reverse=True)
    A = [a/sum(A) for a in A]
    val, dist = best_response(A, 2, n_restarts=8)
    print(A, "-> best oddrank", val, "dist", dist, " c(2)=",c(2))

print("\n--- Testing candidate recursive strategy ---")

def oddrank_list(vals):
    return oddrank(vals)

def recursive_strategy(A, budget):
    """Candidate: at each step with current sorted piece list and remaining budget r:
       - if budget==0: stop.
       - sort desc, let S = sum(tail).
       - if p1 >= S: apply full Lemma DOM using k=min(budget, len(tail)) marks:
            split p1 into k parts matching top k tail elements + remainder r=p1-matched_sum,
            keep tail as is (do not recurse into tail).
       - elif p1 >= 2*p2: halve p1 (spend 1 mark), recurse into the tail (list without p1)
            with budget-1, merge results.
       - else: (balanced / no big top piece) recurse by treating the SECOND-largest gap:
            just halve p1 anyway (best local guess) and recurse on tail with budget-1.
       Returns final list of pieces.
    """
    A = sorted(A, reverse=True)
    if budget == 0:
        return A
    if len(A) == 1:
        # single piece, still has budget: split in half and recurse on the
        # resulting 2-element list with the remaining budget
        p = A[0]
        half = p/2
        return recursive_strategy([half, half], budget-1)
    p1 = A[0]
    tail = A[1:]
    S = sum(tail)
    if p1 >= S:
        k = min(budget, len(tail))
        tail_sorted = sorted(tail, reverse=True)
        matched = tail_sorted[:k]
        matched_sum = sum(matched)
        r = p1 - matched_sum
        parts = matched + ([r] if r > 1e-15 else [])
        return parts + tail  # tail stays, matched pieces + remainder + original tail
    else:
        # halve p1, recurse on tail with budget-1
        half = p1/2
        rest = recursive_strategy(tail, budget-1)
        return [half, half] + rest

random.seed(2); np.random.seed(2)
worst_ratio = 0
worst_case = None
for trial in range(3000):
    m = random.choice([1,2,3])
    n_marks = 2
    raw = [random.random()**random.choice([1,3,6]) for _ in range(m)]
    A = sorted([x/sum(raw) for x in raw], reverse=True)
    val = oddrank_list(recursive_strategy(A, n_marks))
    ratio = val / c(2)
    if ratio > worst_ratio:
        worst_ratio = ratio
        worst_case = (A[:], val)
print("n=2 worst ratio (recursive candidate)/c(2):", worst_ratio, worst_case)

print("\n--- Testing discrete DOM/HALVE recursive search (branch over both moves) ---")

def dom_partial(A, k):
    """Apply generalized-DOM-style move: p1 = A[0], tail = A[1:].
       Use k marks (k <= len(tail)) to split p1 into: top-k tail values matched + remainder r=p1-sum(matched),
       merge with the (unchanged) tail. Returns new list."""
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

import functools

def best_discrete(A_tuple, budget, memo={}):
    A = list(A_tuple)
    key = (tuple(round(x,9) for x in sorted(A, reverse=True)), budget)
    if key in memo:
        return memo[key]
    if budget == 0:
        val = oddrank_list(A)
        memo[key] = val
        return val
    A_sorted = sorted(A, reverse=True)
    best = oddrank_list(A_sorted)  # option: do nothing further
    # option: halve top, recurse with budget-1
    newA = halve_top(A_sorted)
    best = min(best, best_discrete(tuple(newA), budget-1, memo))
    # option: dom-partial with k=1..budget (if tail nonempty)
    if len(A_sorted) > 1:
        maxk = min(budget, len(A_sorted)-1)
        for k in range(1, maxk+1):
            newA2 = dom_partial(A_sorted, k)
            best = min(best, best_discrete(tuple(newA2), budget-k, memo))
    memo[key] = best
    return best

random.seed(3); np.random.seed(3)
worst_ratio = 0
worst_case = None
for trial in range(2000):
    m = random.choice([1,2,3])
    n_marks = 2
    raw = [random.random()**random.choice([1,3,6]) for _ in range(m)]
    A = sorted([x/sum(raw) for x in raw], reverse=True)
    memo = {}
    val = best_discrete(tuple(A), n_marks, memo)
    ratio = val / c(2)
    if ratio > worst_ratio:
        worst_ratio = ratio
        worst_case = (A[:], val)
print("n=2 worst ratio (discrete DOM/HALVE search)/c(2):", worst_ratio, worst_case)
