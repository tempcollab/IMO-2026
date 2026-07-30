"""
IMO 2026 P3 explorer: upper-bound majorization/parity route.
Tests:
  (a) Is max_Liu min_Xiang(odd-index) attained at the tower T_n?
  (b) Does a "halve-and-pair" parity strategy achieve D <= 1/D_n on random configs?
Uses exact Fraction arithmetic for odd-index evaluation; grid search for Xiang-best.
"""
import numpy as np
from fractions import Fraction
import itertools, random

random.seed(1)
np.random.seed(1)

def odd_index(pieces):
    """pieces: list of Fraction or float. Returns odd-index sum of sorted-desc."""
    s = sorted(pieces, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def D_alt(pieces):
    """alternating sum a1-a2+a3-..."""
    s = sorted(pieces, reverse=True)
    d = Fraction(0)
    for i,a in enumerate(s):
        d += a if i%2==0 else -a
    return d

def xiang_best(pieces, marks, grid=15):
    """Min over Xiang refinements using <=marks splits. pieces: list of Fraction.
    Uses a grid of split fractions. Includes the 'stop' (use fewer marks) option.
    Returns (min_odd_index_value, best_refinement_pieces)."""
    # current value if Xiang stops
    cur = odd_index(pieces)
    best = cur
    best_ref = list(pieces)
    if marks == 0:
        return best, best_ref
    # try splitting each piece at grid points
    # grid fractions: include 1/2 and spread
    fracs = [Fraction(1,k) for k in range(2, grid+2)]  # 1/2,1/3,...,1/(grid+1)
    # also include 1/2 twice is fine; add some others
    fracs = sorted(set(fracs + [Fraction(1,2), Fraction(2,5), Fraction(3,7)]))
    for i, L in enumerate(pieces):
        if L <= 0:
            continue
        for g in fracs:
            t = g * L
            new = list(pieces)
            new.pop(i)
            new.extend([t, L - t])
            val, ref = xiang_best(new, marks-1, grid)
            if val < best:
                best = val
                best_ref = ref
    return best, best_ref

def xiang_best_pruned(pieces, marks, target, grid=12):
    """Pruned: stop searching a branch once odd-index <= target (Xiang satisfied)."""
    cur = odd_index(pieces)
    best = cur
    if best <= target or marks == 0:
        return best
    fracs = [Fraction(1,k) for k in range(2, grid+2)]
    fracs = sorted(set(fracs + [Fraction(2,5)]))
    for i, L in enumerate(pieces):
        if L <= 0:
            continue
        for g in fracs:
            t = g * L
            new = list(pieces)
            new.pop(i)
            new.extend([t, L - t])
            val = xiang_best_pruned(new, marks-1, target, grid)
            if val < best:
                best = val
                if best <= target:
                    return best
    return best

def make_tower(n):
    Dn = 2**(n+1) - 1
    # (2^n, 2^{n-1}, ..., 2, 1)/D_n  -- n+1 pieces, summing to 1
    return [Fraction(2**k, Dn) for k in range(n, -1, -1)]

def random_liu_config(n):
    """Random Liu config with <=n marks => <=n+1 pieces summing to 1 (Fraction)."""
    k = random.randint(0, n)  # number of marks
    # k marks => k+1 pieces; cut positions
    pts = sorted(random.sample(range(1, 1000), k))  # coarse grid for reproducibility
    bounds = [0] + [p for p in pts] + [1000]
    pieces = [Fraction(bounds[i+1]-bounds[i], 1000) for i in range(len(bounds)-1)]
    return pieces

def random_liu_config_float(n):
    """Float-based random config, then convert to Fraction via grid."""
    k = random.randint(0, n)
    pts = sorted(np.random.uniform(0,1, k))
    bounds = [0.0]+list(pts)+[1.0]
    pieces = []
    for i in range(len(bounds)-1):
        # quantize to /10000
        v = int(round((bounds[i+1]-bounds[i])*10000))
        if v>0:
            pieces.append(Fraction(v,10000))
    # normalize
    s = sum(pieces)
    pieces = [p/s for p in pieces]
    return pieces

# ---- Experiment 1: tower value and Xiang-best for tower ----
print("="*70)
print("EXPERIMENT 1: tower T_n and its Xiang-best (min odd-index)")
print("="*70)
for n in [1,2,3]:
    Dn = 2**(n+1)-1
    tower = make_tower(n)
    tgt = Fraction(2**n, Dn)
    Dtarget = Fraction(1, Dn)
    val, ref = xiang_best(tower, n, grid=16)
    print(f"n={n}: tower pieces={[str(p) for p in tower]}")
    print(f"  target odd-index = 2^n/D_n = {tgt} = {float(tgt):.6f}")
    print(f"  Xiang-best (grid) odd-index = {val} = {float(val):.6f}")
    print(f"  D (alt sum) of best ref = {D_alt(ref)} = {float(D_alt(ref)):.6f}, target D={float(Dtarget):.6f}")
    print(f"  best refinement sorted = {sorted(ref, reverse=True)}")
    print()

# ---- Experiment 2: max over random Liu configs of Xiang-best ----
print("="*70)
print("EXPERIMENT 2: max_Liu min_Xiang odd-index over random configs")
print("  Does any random Liu config EXCEED the tower value?")
print("="*70)
for n in [2,3]:
    Dn = 2**(n+1)-1
    tgt = Fraction(2**n, Dn)
    N = 400 if n==2 else 150
    worst_val = Fraction(-1)
    worst_config = None
    worst_ref = None
    exceed_count = 0
    for trial in range(N):
        cfg = random_liu_config_float(n)
        v = xiang_best_pruned(cfg, n, tgt, grid=10 if n==2 else 7)
        if v > tgt:
            exceed_count += 1
            if v > worst_val:
                worst_val = v
                worst_config = cfg
        if v > worst_val:
            worst_val = v
            worst_config = cfg
            worst_ref = None
    print(f"n={n}: {N} random configs. target={tgt}={float(tgt):.6f}")
    print(f"  configs exceeding target: {exceed_count}")
    print(f"  worst Xiang-best odd-index found = {worst_val} = {float(worst_val):.6f}")
    print(f"  worst config = {sorted(worst_config, reverse=True)}")
    print()

# ---- Experiment 3: near-tower perturbations ----
print("="*70)
print("EXPERIMENT 3: perturb tower slightly; does Xiang-best drop below tower value?")
print("="*70)
for n in [2,3]:
    Dn = 2**(n+1)-1
    tgt = Fraction(2**n, Dn)
    tower = make_tower(n)
    print(f"n={n}: target={float(tgt):.6f}")
    # perturb: shift mass between top two pieces
    eps = Fraction(1, 1000)
    for d in range(-5, 6, 2):
        cfg = list(tower)
        cfg[0] += d*eps
        cfg[1] -= d*eps
        if any(c<0 for c in cfg):
            continue
        v = xiang_best_pruned(cfg, n, tgt, grid=12 if n==2 else 8)
        print(f"  perturb d={d}eps: config={sorted(cfg,reverse=True)} -> Xiang-best={float(v):.6f} ({'>' if v>tgt else '<='} target)")
    # perturb: merge two smallest
    cfg2 = list(tower)
    cfg2[-1] = cfg2[-1] + cfg2[-2]
    cfg2 = cfg2[:-1]
    v2 = xiang_best_pruned(cfg2, n, tgt, grid=12 if n==2 else 8)
    print(f"  merge two smallest: {sorted(cfg2,reverse=True)} -> {float(v2):.6f}")
    # perturb: equalize all pieces
    m = len(tower)
    eq = [Fraction(1,m)]*m
    veq = xiang_best_pruned(eq, n, tgt, grid=12 if n==2 else 8)
    print(f"  equal pieces {[str(p) for p in eq]} -> {float(veq):.6f}")
    print()
