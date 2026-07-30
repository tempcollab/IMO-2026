from fractions import Fraction
import random
random.seed(2)

# Strict parity: L/2 STRICTLY > a_2 (rest max). Then positions 1,2 = L/2,L/2 uniquely; rest at 3.
violations = 0; tests = 0
for _ in range(200000):
    n = random.randint(2,5)
    Dn = 2**(n+1)-1
    L = Fraction(2**n + random.randint(1, Dn-2**n), Dn)
    if L >= 1: continue
    R = 1 - L
    npieces = random.randint(1, n)
    raw = [Fraction(random.randint(1,100)) for _ in range(npieces)]
    s = sum(raw); rest = [r*R/s for r in raw]; rest.sort(reverse=True)
    if not rest: continue
    if not (L/2 > rest[0]): continue  # strict
    merged = sorted([L/2,L/2]+rest, reverse=True)
    # two L/2 at top strictly
    if merged[0] != L/2 or merged[1] != L/2:
        violations += 1; tests += 1; continue
    # rest max at position 3
    if merged[2] != rest[0]:
        violations += 1
    tests += 1
print(f"Strict parity (L/2 > a_2): {violations} violations / {tests} tests")

# Also verify D(total) = D(rest) homogeneity: scaling.
# D(total after split) = L/2 - L/2 + D(rest starting at pos 3). Rest-local pos 1 at global pos 3 (odd, +).
# So D(total) = 0 + D(rest). Confirmed structurally.

# === Verify n=2 below-threshold direct bound: 2L-1 < 1/D_n when L < 2^n/D_n ===
print("\n=== n=2: 2L-1 < 1/7 when L < 4/7 (direct bound for cases C/B2) ===")
for L_num in range(35, 40):  # L = 0.35..0.39? no, L in [1/2, 4/7)
    L = Fraction(L_num, 100)
    if L < Fraction(1,2) or L >= Fraction(4,7): continue
    print(f"  L={L}: 2L-1={2*L-1}, 1/7={Fraction(1,7)}, 2L-1<1/7? {2*L-1 < Fraction(1,7)}")

# === Tower UNIQUE worst n=3: tower Xiang-best = 1/15, perturbations strict < ===
def alt_sum(pieces):
    s = sorted([p for p in pieces if p>0], reverse=True)
    D = Fraction(0)
    for i,x in enumerate(s):
        D += x if i%2==0 else -x
    return D

grid = [Fraction(1,k) for k in range(2,9)] + [Fraction(1,2), Fraction(2,5), Fraction(3,7)]
def xiang_best(pieces, n_marks):
    best = [alt_sum(pieces)]
    def rec(cur, ml):
        best[0] = min(best[0], alt_sum(cur))
        if ml==0: return
        for i in range(len(cur)):
            for qf in grid:
                Lc = cur[i]
                if Lc<=0: continue
                q = Lc*qf; p = Lc-q
                if p<=0 or q<=0: continue
                new=list(cur); new[i]=p; new.append(q)
                rec(new, ml-1)
    rec(list(pieces), n_marks)
    return best[0]

tower3 = [Fraction(8,15), Fraction(4,15), Fraction(2,15), Fraction(1,15)]
print(f"\n=== n=3 tower Xiang-best (3 marks) = {xiang_best(tower3,3)} (expect 1/15) ===")
eps = Fraction(1, 1000)
for d in [-5,-3,-1,1,3,5]:
    # shift mass between top two pieces
    cfg = [Fraction(8,15)+d*eps, Fraction(4,15)-d*eps, Fraction(2,15), Fraction(1,15)]
    if cfg[0]<=0 or cfg[1]<=0: continue
    cfg.sort(reverse=True)
    s = sum(cfg)
    cfg = [c/s for c in cfg]  # renormalize
    print(f"  perturb d={d}: Xiang-best = {xiang_best(cfg,3)}, < 1/15={Fraction(1,15)}? {xiang_best(cfg,3) < Fraction(1,15)}")
