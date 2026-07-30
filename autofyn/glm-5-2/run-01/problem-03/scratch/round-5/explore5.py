"""
Explore 5th-framing angles for the LOWER bound of imo-2026-03.
Tower T_n = (2^n, 2^{n-1}, ..., 2, 1), total D_n = 2^{n+1}-1.
Target: D = a_1 - a_2 + a_3 - ... >= 1 (tower units) for every <= n-mark refinement.

Angles to test:
 (a) Exact absorption invariant Q(config) with Q(T_n)=1, predictable per-split change.
 (d) Polynomial encoding: D = P(-1) where P(x) = sum p_k x^k. Root-of-unity / coefficient structure.
 (mod) Modular/residue structure of N(t) = #{pieces >= t}, D = int(N mod 2)dt.
 (e) Min-level set {D=1} connectivity / sign-change structure.
"""
from fractions import Fraction as F
from itertools import product
import random

def D_of(pieces):
    """Alternating sum of sorted-descending pieces. pieces: list of numbers."""
    s = sorted(pieces, reverse=True)
    return sum(((-1)**k)*v for k,v in enumerate(s))  # 0-based: +,-,+,...

def tower(n):
    return [F(2**k) for k in range(n,-1,-1)]  # [2^n, ..., 2, 1]

def Dn(n):
    return F(2**(n+1)-1)

# ---------- Enumerate refinements ----------
# A refinement: start from T_n, apply <= n splits. Each split picks a piece and cuts it.
# Full enumeration of ALL refinements is huge. We enumerate a representative family:
#  (1) cascade splits on the top piece (split top, then split a fragment, etc.)
#  (2) splits on arbitrary tower pieces.
# Use rational cut positions for breakpoints (the min is at breakpoints per PL lemma).
# We enumerate breakpoint configs: each cut ties a fragment to an adjacent piece.

def refine_breakpoint_configs(n, max_marks=None):
    """Enumerate breakpoint (tie) refinements of T_n by recursive splitting.
    A breakpoint config: each cut produces a fragment that ties an existing piece.
    We approximate by enumerating cuts at rational positions that produce ties.
    For tractability, enumerate cascade refinements of the top piece + a few interior splits.
    Returns list of sorted piece multisets (as tuples of Fractions)."""
    if max_marks is None:
        max_marks = n
    results = set()
    T = tower(n)
    # BFS over refinement states: state = multiset of pieces (sorted tuple), marks used.
    start = tuple(sorted(T, reverse=True))
    results.add(start)
    frontier = [(start, 0)]
    seen = {start: 0}
    # To keep tractable, we enumerate splits where the cut position is a breakpoint:
    # splitting piece V into f + (V-f) where f ties some existing piece value OR a dyadic fraction.
    while frontier:
        config, marks = frontier.pop()
        if marks >= max_marks:
            continue
        pieces = list(config)
        vals = sorted(set(pieces), reverse=True)
        for i, V in enumerate(pieces):
            # cut V into f + (V-f), f >= V-f so f >= V/2.
            # breakpoint cut positions: f in {values present} union {V - values present} union {dyadic fractions}
            cutset = set()
            for v in vals:
                if F(0) < v < V:
                    cutset.add(v)  # f ties value v
                    cutset.add(V - v)  # V-f ties value v -> f = V-v
            # also dyadic breakpoints: f = 2^k for k where 2^k in (0, V)
            k = 0
            while (1<<k) < V:
                f = F(1<<k)
                if F(0) < f < V:
                    cutset.add(f)
                k += 1
            for f in cutset:
                if F(0) < f < V:
                    new = [p for j,p in enumerate(pieces) if j != i]
                    new.append(f)
                    new.append(V - f)
                    nc = tuple(sorted(new, reverse=True))
                    if nc not in seen or seen[nc] > marks+1:
                        seen[nc] = marks+1
                        results.add(nc)
                        frontier.append((nc, marks+1))
    return list(results)

# ---------- Test D >= 1 for all enumerated breakpoint configs ----------
for n in [2,3,4]:
    cfgs = refine_breakpoint_configs(n)
    Ds = [D_of(c) for c in cfgs]
    mn = min(Ds) if Ds else None
    nmin = sum(1 for d in Ds if d == mn)
    viol = sum(1 for d in Ds if d < 1)
    print(f"T_{n}: {len(cfgs)} breakpoint configs, min D = {mn}, #minimizers={nmin}, #violations(D<1)={viol}")

print("="*60)
# ---------- Angle (a): exact invariant Q ----------
# Candidate Q1: dominance margin of largest = max(piece) - (total - max)
def Q_dominance(pieces):
    s = sorted(pieces, reverse=True)
    return s[0] - (sum(s) - s[0])

# Candidate Q2: D itself (circular, check)
# Candidate Q3: "alternating mass by 2-adic level" - sum of pieces with even index value mod something
# Candidate Q4: top-mass - below-top-mass = (sum of fragments of 2^n) - (sum of pieces from below tower)
#   For the tower: 2^n - (2^n-1) = 1. This is the "dominance margin" = Q1 essentially when top unsplit.

# Let's test: does any simple Q stay = 1 under ALL single splits of T_n?
# Split T_n's top 2^n into f + (2^n - f). Check Q on {f, 2^n-f} ∪ T_{n-1}.
n = 3
T = tower(n)
top = T[0]
rest = T[1:]
print(f"\nAngle (a): T_{n} top split 2^{n} = {top} into f + ({top}-f). Tests:")
print(f"{'f':>10} {'D':>8} {'Q_dom':>10} {'Q_topfrag':>12}")
for f_num in range(1, int(top)):
    for f_den in [1,2,3,4,8]:
        f = F(f_num, f_den)
        if F(0) < f < top:
            pieces = [f, top-f] + rest
            print(f"{str(f):>10} {str(D_of(pieces)):>8} {str(Q_dominance(pieces)):>10}", end="")
            # Q_topfrag = (sum of top fragments) - (sum of below tower, possibly split)
            # here below tower unsplit
            print(f" {'':>12}")
