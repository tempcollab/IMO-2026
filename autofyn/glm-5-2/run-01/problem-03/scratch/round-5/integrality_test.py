"""
Test LP INTEGRALITY (total unimodularity) of the per-type bin-partition LP
across many random combinatorial types of T_n refinements, for n=2,3,4,5.

If every primal optimum p has INTEGER entries, then min D is an integer.
Combined with the parity argument (D=0 requires even total mass, but D_n odd),
this would give min D >= 1 (G1 closed).

Also: explicitly check the parity argument -- D=0 <=> all adjacent pairs equal
(+ trailing 0 if m odd) <=> total mass even.  But D_n = 2^{n+1}-1 is odd.
So D=0 is infeasible.  If min D integer, min D >= 1.
"""
import numpy as np
from scipy.optimize import linprog
from fractions import Fraction
import random

def build_lp(n, b, tower_vals):
    m = len(b)
    c = np.array([(-1.)**k for k in range(m)])
    bins = sorted(set(b))
    A_eq = np.zeros((len(bins), m)); b_eq = np.zeros(len(bins))
    for i, t in enumerate(bins):
        for k in range(m):
            if b[k] == t: A_eq[i, k] = 1.0
        b_eq[i] = float(tower_vals[t])
    A_ub = np.zeros((m-1, m)) if m > 1 else np.zeros((0,m))
    for k in range(m-1):
        A_ub[k, k] = -1.0; A_ub[k, k+1] = 1.0
    return c, A_eq, b_eq, A_ub

def is_integer(x, tol=1e-7):
    return all(abs(v - round(v)) < tol for v in x)

def random_type(n, seed=None):
    """Generate a random combinatorial type: randomly split each tower piece
    into 1..(available marks) fragments, return (b, tower_vals, m)."""
    rng = random.Random(seed) if seed is not None else random
    tower_vals = {t: 2**(n-t) for t in range(n+1)}
    # total marks available = n ; each split of bin t into r pieces uses r-1 marks
    marks_left = n
    # decide how many fragments per bin
    frags = {}
    bins = list(range(n+1))
    rng.shuffle(bins)
    for t in bins:
        max_extra = min(marks_left, 3)
        r = rng.randint(1, 1 + max_extra)  # 1..(1+max_extra) fragments
        r = min(r, 1 + marks_left)
        frags[t] = r
        marks_left -= (r - 1)
        if marks_left <= 0:
            for t2 in bins:
                if t2 not in frags: frags[t2] = 1
            break
    for t in range(n+1):
        if t not in frags: frags[t] = 1
    # build a list of (fragment_value_placeholder, bin) -- we don't need actual
    # values, just the combinatorial type (bin assignment b in sorted order).
    # To get a valid SORTED bin assignment, assign random values then sort.
    # But values must sum to tower_vals[t] per bin. Use random splits.
    pieces = []
    for t in range(n+1):
        r = frags[t]
        if r == 1:
            pieces.append((float(tower_vals[t]), t))
        else:
            # random split of tower_vals[t] into r positive parts
            vals = sorted([rng.random() for _ in range(r)], reverse=True)
            s = sum(vals)
            cuts = [0] + list(np.cumsum(vals))
            parts = [vals[i]/s * tower_vals[t] for i in range(r)]
            for v in parts:
                pieces.append((float(v), t))
    pieces.sort(reverse=True)
    b = tuple(p[1] for p in pieces)
    return b, tower_vals

def test_integrality(n, ntrials=200):
    noninteger_count = 0
    min_d_values = set()
    min_d_below_1 = 0
    examples_nonint = []
    for seed in range(ntrials):
        b, tv = random_type(n, seed=seed*1000+n)
        c, A_eq, b_eq, A_ub = build_lp(n, b, tv)
        m = len(b)
        bounds = [(0, None)]*m
        try:
            res = linprog(c, A_ub=A_ub, b_ub=np.zeros(A_ub.shape[0]) if A_ub.shape[0]>0 else None,
                          A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
        except Exception as e:
            continue
        if not res.success:
            continue
        if not is_integer(res.x):
            noninteger_count += 1
            min_d_below_1 += (res.fun < 1 - 1e-9)
            if len(examples_nonint) < 5:
                examples_nonint.append((b, np.round(res.x,4), round(res.fun,4)))
        min_d_values.add(round(res.fun, 6))
        if res.fun < 1 - 1e-9:
            min_d_below_1 += 1
    return noninteger_count, min_d_below_1, examples_nonint, min_d_values

for n in [2, 3, 4, 5]:
    ni, below, ex, vals = test_integrality(n, ntrials=300)
    print(f"n={n}: noninteger-optimum count = {ni}/300,  min D < 1 count = {below}")
    print(f"  distinct min D values (sample): {sorted(vals)[:20]}")
    if ex:
        print(f"  noninteger examples: {ex[:3]}")

# ---- EXHAUSTIVE small check: n=2, ALL combinatorial types with m=3,4,5 (all fragment counts) ----
print("\n=== Exhaustive-ish: all 'shape' types for n=2 by fragment-count vector ===")
from itertools import product
n = 2; TV = {0:4,1:2,2:1}
# fragment-count vectors (r0,r1,r2) with r0-1+r1-1+r2-1 <= n=2, each r>=1
shapes = []
for r0 in range(1,5):
    for r1 in range(1,5):
        for r2 in range(1,5):
            if (r0-1)+(r1-1)+(r2-1) <= 2:
                shapes.append((r0,r1,r2))
print(f"fragment-count shapes: {len(shapes)}")
# For each shape, sample several random value-splits and check integrality
nonint = 0; total = 0; below1 = 0
for shape in shapes:
    for seed in range(20):
        rng = random.Random(seed*999+hash(shape)%10000)
        pieces=[]
        for t in range(3):
            r = shape[t]; tv = TV[t]
            if r==1: pieces.append((float(tv),t))
            else:
                vals=[rng.random() for _ in range(r)]
                s=sum(vals)
                parts=[v/s*tv for v in vals]
                for v in parts: pieces.append((float(v),t))
        pieces.sort(reverse=True)
        b=tuple(p[1] for p in pieces)
        c,A_eq,b_eq,A_ub=build_lp(n,b,TV); m=len(b)
        res=linprog(c,A_ub=A_ub,b_ub=np.zeros(A_ub.shape[0]) if A_ub.shape[0]>0 else None,
                    A_eq=A_eq,b_eq=b_eq,bounds=[(0,None)]*m,method='highs')
        if not res.success: continue
        total+=1
        if not is_integer(res.x): nonint+=1
        if res.fun < 1-1e-9: below1+=1
print(f"n=2 sampled: {total} LPs, noninteger = {nonint}, min D < 1 = {below1}")
