"""Focused experiments: (1) which configs tie the target? (2) parity-pairing test."""
from fractions import Fraction

def odd_index(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

def D_alt(pieces):
    s = sorted(pieces, reverse=True)
    d = Fraction(0)
    for i,a in enumerate(s):
        d += a if i%2==0 else -a
    return d

def xiang_best(pieces, marks, grid=14):
    cur = odd_index(pieces)
    best = cur
    if marks == 0:
        return best
    fracs = sorted(set([Fraction(1,k) for k in range(2, grid+2)] + [Fraction(2,5), Fraction(3,7)]))
    for i, L in enumerate(pieces):
        if L <= 0: continue
        for g in fracs:
            t = g * L
            new = list(pieces)
            new.pop(i)
            new.extend([t, L - t])
            val = xiang_best(new, marks-1, grid)
            if val < best:
                best = val
    return best

# ---- Exp A: n=2, scan 2-piece configs (a, 1-a) on a fine grid ----
print("="*70)
print("EXP A: n=2, scan 2-piece configs (a,1-a); which achieve Xiang-best = 4/7?")
print("="*70)
tgt2 = Fraction(4,7)
print(f"target = 4/7 = {float(tgt2):.6f}")
ties = []
for num in range(500, 1001, 5):  # a = num/1000, from 0.5 to 1.0
    a = Fraction(num, 1000)
    b = 1 - a
    if b <= 0: continue
    v = xiang_best([a, b], 2, grid=12)
    if v >= tgt2:
        ties.append((a, b, v))

if ties:
    print(f"  configs with Xiang-best >= 4/7: {len(ties)}")
    for a,b,v in ties[:10]:
        print(f"    a={float(a):.4f}, v={float(v):.6f} ({v})")
else:
    print("  NO 2-piece config achieves Xiang-best >= 4/7 (all strictly below)")

# ---- Exp B: n=2, 3-piece configs on a coarser grid ----
print()
print("="*70)
print("EXP B: n=2, scan 3-piece configs; which achieve Xiang-best = 4/7?")
print("="*70)
ties3 = []
for i in range(1, 20):
    for j in range(i+1, 21):
        a = Fraction(i, 20)
        b = Fraction(j - i, 20)
        c = Fraction(20 - j, 20)
        if a <= 0 or b <= 0 or c <= 0: continue
        cfg = [a, b, c]
        v = xiang_best(cfg, 2, grid=10)
        if v >= tgt2:
            ties3.append((cfg, v))
print(f"  configs with Xiang-best >= 4/7: {len(ties3)}")
for cfg, v in ties3[:15]:
    print(f"    {sorted(cfg, reverse=True)} -> {float(v):.6f} ({v})")

# ---- Exp C: tower and near-tower for n=2,3 with exact best ----
print()
print("="*70)
print("EXP C: tower Xiang-best (exact grid) for n=1,2,3")
print("="*70)
for n in [1,2,3]:
    Dn = 2**(n+1)-1
    tower = [Fraction(2**k, Dn) for k in range(n, -1, -1)]
    tgt = Fraction(2**n, Dn)
    v = xiang_best(tower, n, grid=14)
    print(f"n={n}: tower={tower} Xiang-best={v} ({float(v):.6f}) target={tgt} ({float(tgt):.6f}) {'TIE' if v==tgt else 'MISMATCH'}")

# ---- Exp D: parity-pairing strategy test ----
# Strategy: Xiang greedily PAIRS pieces by halving the largest into two equal halves,
# creating pairs (x,x) that fill an odd+even slot and cancel in D.
# Test: does "halve the largest piece" (creating pairs) reduce D to <= 1/D_n?
print()
print("="*70)
print("EXP D: 'halve-largest-pairing' strategy: does D <= 1/D_n after n halvings?")
print("="*70)
def halve_largest_strategy(pieces, n):
    """Xiang uses n marks, each halving the current largest piece."""
    p = list(pieces)
    for _ in range(n):
        # find largest piece
        idx = max(range(len(p)), key=lambda i: p[i])
        L = p[idx]
        p.pop(idx)
        p.extend([L/2, L/2])
    return D_alt(p)

for n in [1,2,3,4]:
    Dn = 2**(n+1)-1
    Dtarget = Fraction(1, Dn)
    tower = [Fraction(2**k, Dn) for k in range(n, -1, -1)]
    D_strat = halve_largest_strategy(tower, n)
    print(f"n={n}: tower, halve-largest D = {D_strat} ({float(D_strat):.6f}), target D = {float(Dtarget):.6f}, {'OK' if D_strat <= Dtarget else 'FAIL'}")

# Test on random configs too
import random
random.seed(42)
print()
for n in [2,3]:
    Dn = 2**(n+1)-1
    Dtarget = Fraction(1, Dn)
    fails = 0
    worst = Fraction(0)
    for _ in range(500):
        k = random.randint(0, n)
        pts = sorted(random.sample(range(1,1000), k))
        bounds = [0]+pts+[1000]
        cfg = [Fraction(bounds[i+1]-bounds[i], 1000) for i in range(len(bounds)-1)]
        s = sum(cfg)
        cfg = [p/s for p in cfg]
        D_strat = halve_largest_strategy(cfg, n)
        if D_strat > Dtarget:
            fails += 1
            if D_strat > worst:
                worst = D_strat
    print(f"n={n}: halve-largest on 500 random configs: {fails} exceed 1/D_n, worst D={float(worst):.6f}")

# ---- Exp E: does Xiang-best for tower use balanced-pairs? ----
print()
print("="*70)
print("EXP E: for tower n=2, enumerate Xiang's best refinement type")
print("="*70)
n = 2
Dn = 7
tower = [Fraction(4,7), Fraction(2,7), Fraction(1,7)]
# The balanced-pairs config: split 4->2,2 => {2,2,2,1}/7. D=(2-2)+(2-1)=1. odd=2+2=4/7. Hmm D=1/7? Let me check
bp = [Fraction(2,7), Fraction(2,7), Fraction(2,7), Fraction(1,7)]
print(f"balanced-pairs {{2,2,2,1}}/7: D={D_alt(bp)} ({float(D_alt(bp)):.6f}), odd={odd_index(bp)} ({float(odd_index(bp)):.6f})")
# Actually the equality config from the writeup: {2,2,1,1,1}/7 (5 pieces, 2 marks on 3-piece tower)
bp2 = [Fraction(2,7), Fraction(2,7), Fraction(1,7), Fraction(1,7), Fraction(1,7)]
print(f"equality config {{2,2,1,1,1}}/7: D={D_alt(bp2)} ({float(D_alt(bp2)):.6f}), odd={odd_index(bp2)} ({float(odd_index(bp2)):.6f})")
# Xiang splits top 4->2,2 (1 mark) and then 2->1,1 (1 mark on one of the 2's)
bp3 = [Fraction(2,7), Fraction(2,7), Fraction(1,7), Fraction(1,7), Fraction(1,7)]
# Also: split 4->2,2, and split the other 1->...
# What about: split 4 -> 2,2 and 2 -> 1,1 => {2,2,1,1,1}/7
print(f"  (split 4->2,2 & one 2->1,1 on rest 2,1) => {sorted(bp3,reverse=True)}")
v = xiang_best(tower, 2, grid=14)
print(f"  grid Xiang-best = {v}")
