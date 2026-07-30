"""Test parallel-halving (one mark per piece) and scan for tower ties."""
from fractions import Fraction
import random

def odd_index(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def D_alt(pieces):
    s = sorted(pieces, reverse=True)
    d = Fraction(0)
    for i,a in enumerate(s):
        d += a if i%2==0 else -a
    return d

# ---- Parallel halving: split the n LARGEST pieces, each once, in half ----
def parallel_halve(pieces, n):
    """Split each of the n largest pieces in half (one mark each)."""
    p = sorted(pieces, reverse=True)
    out = []
    for i, x in enumerate(p):
        if i < n:
            out.extend([x/2, x/2])
        else:
            out.append(x)
    return D_alt(out)

print("="*70)
print("PARALLEL HALVING (split n largest pieces in half): D on tower & random")
print("="*70)
for n in [1,2,3,4,5]:
    Dn = 2**(n+1)-1
    Dtarget = Fraction(1, Dn)
    tower = [Fraction(2**k, Dn) for k in range(n, -1, -1)]
    D = parallel_halve(tower, n)
    print(f"n={n}: tower parallel-halve D = {D} ({float(D):.6f}), target = {float(Dtarget):.6f}, {'OK' if D <= Dtarget else 'FAIL'}")

print()
random.seed(7)
for n in [2,3,4]:
    Dn = 2**(n+1)-1
    Dtarget = Fraction(1, Dn)
    fails = 0; worst = Fraction(0); N=500
    for _ in range(N):
        k = random.randint(0, n)
        pts = sorted(random.sample(range(1,1000), k))
        bounds = [0]+pts+[1000]
        cfg = [Fraction(bounds[i+1]-bounds[i], 1000) for i in range(len(bounds)-1)]
        s = sum(cfg); cfg = [p/s for p in cfg]
        D = parallel_halve(cfg, n)
        if D > Dtarget:
            fails += 1
            if D > worst: worst = D
    print(f"n={n}: parallel-halve on {N} random: {fails} exceed 1/D_n, worst D={float(worst):.6f}")

# ---- Scan for tower ties at n=2 on /21 and /7 grids ----
print()
print("="*70)
print("SCAN: n=2, which configs tie at Xiang-best = 4/7? (/21 grid)")
print("="*70)
def xiang_best(pieces, marks, grid=12):
    cur = odd_index(pieces)
    best = cur
    if marks == 0: return best
    fracs = sorted(set([Fraction(1,k) for k in range(2, grid+2)] + [Fraction(2,5)]))
    for i, L in enumerate(pieces):
        if L <= 0: continue
        for g in fracs:
            t = g * L
            new = list(pieces); new.pop(i); new.extend([t, L - t])
            val = xiang_best(new, marks-1, grid)
            if val < best: best = val
    return best

tgt2 = Fraction(4,7)
ties = []
# /21 grid 3-piece configs
for i in range(1, 21):
    for j in range(i+1, 21):
        for k in range(j+1, 22):
            a = Fraction(i,21); b = Fraction(j-i,21); c = Fraction(21-k+1,21) if k<=21 else Fraction(0)
            # actually: pieces are i/21, (j-i)/21, (22-k)/21... let me just do simpler
            pass
# Simpler: 3 pieces summing to 1, on /21 grid
for x in range(1, 20):
    for y in range(x, 21-x):
        z = 21 - x - y
        if z <= 0: continue
        cfg = [Fraction(x,21), Fraction(y,21), Fraction(z,21)]
        v = xiang_best(cfg, 2, grid=10)
        if v >= tgt2:
            ties.append((cfg, v))
print(f"  /21 grid 3-piece ties (>= 4/7): {len(ties)}")
for cfg, v in ties[:10]:
    print(f"    {sorted(cfg,reverse=True)} -> {float(v):.6f} ({v})")

# Specifically check the tower
tower2 = [Fraction(4,7), Fraction(2,7), Fraction(1,7)]
vt = xiang_best(tower2, 2, grid=12)
print(f"  tower (4/7,2/7,1/7) -> {vt} ({float(vt):.6f})")

# Check scaled tower and other configs that might tie
# e.g. (3/7, 2/7, 2/7)? (3/7,3/7,1/7)?
for cfg_desc in [
    [Fraction(4,7), Fraction(2,7), Fraction(1,7)],
    [Fraction(3,7), Fraction(3,7), Fraction(1,7)],
    [Fraction(3,7), Fraction(2,7), Fraction(2,7)],
    [Fraction(5,7), Fraction(1,7), Fraction(1,7)],
    [Fraction(4,7), Fraction(3,7)],
    [Fraction(5,7), Fraction(2,7)],
    [Fraction(6,7), Fraction(1,7)],
    [Fraction(3,7), Fraction(4,7)],
]:
    if sum(cfg_desc) != 1: continue
    v = xiang_best(cfg_desc, 2, grid=12)
    print(f"  {sorted(cfg_desc,reverse=True)} -> {float(v):.6f} ({v}) {'TIE' if v==tgt2 else ''}")

# ---- n=3: does tower tie? check a few alternative configs ----
print()
print("="*70)
print("n=3: tower and near configs, Xiang-best vs 8/15")
print("="*70)
tgt3 = Fraction(8,15)
for cfg in [
    [Fraction(8,15),Fraction(4,15),Fraction(2,15),Fraction(1,15)],
    [Fraction(7,15),Fraction(5,15),Fraction(2,15),Fraction(1,15)],
    [Fraction(6,15),Fraction(5,15),Fraction(3,15),Fraction(1,15)],
    [Fraction(5,15),Fraction(4,15),Fraction(3,15),Fraction(2,15),Fraction(1,15)],
]:
    if sum(cfg) != 1: continue
    v = xiang_best(cfg, 3, grid=10)
    print(f"  {sorted(cfg,reverse=True)} -> {float(v):.6f} ({v}) {'TIE' if v==tgt3 else ''}")
