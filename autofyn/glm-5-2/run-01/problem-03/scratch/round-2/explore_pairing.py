"""Final check: pairing structure. For tower, D = unpaired residual = 1/D_n.
For non-tower, can Xiang pair to get D < 1/D_n? Test the 'median piece' idea."""
from fractions import Fraction

def D_alt(pieces):
    s = sorted(pieces, reverse=True)
    d = Fraction(0)
    for i,a in enumerate(s):
        d += a if i%2==0 else -a
    return d

def odd_index(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] for i in range(0, len(s), 2))

# After n parallel halvings on tower: {2^{n-1},2^{n-1},...,1,1,1}/D_n
# D = last unpaired 1/D_n. Let's verify the pairing cascades.
for n in [1,2,3,4,5]:
    Dn = 2**(n+1)-1
    # parallel halve: split 2^k -> (2^{k-1}, 2^{k-1}) for k=n..1, leave 1 unsplit
    pieces = []
    for k in range(n, 0, -1):
        pieces.extend([Fraction(2**(k-1), Dn), Fraction(2**(k-1), Dn)])
    pieces.append(Fraction(1, Dn))  # the unpaired smallest
    D = D_alt(pieces)
    print(f"n={n}: parallel-halve pieces={sorted(pieces,reverse=True)}")
    print(f"  D={D} ({float(D):.6f}), 1/D_n={float(Fraction(1,Dn)):.6f}, match={D==Fraction(1,Dn)}")
    print(f"  odd-index={odd_index(pieces)} = {float(odd_index(pieces)):.6f}, target={float(Fraction(2**n,Dn)):.6f}")

print()
print("="*70)
print("KEY: residual = smallest unpaired piece = 1/D_n for tower.")
print("For non-tower: parallel-halve leaves a DIFFERENT residual. Check:")
print("="*70)
# n=2: configs and their parallel-halve D (residual)
import random
random.seed(11)
for n in [2]:
    Dn = 7; Dtarget = Fraction(1,7)
    print(f"n=2, target D=1/7={float(Dtarget):.6f}")
    for desc, cfg in [
        ("tower", [Fraction(4,7),Fraction(2,7),Fraction(1,7)]),
        ("(5,1,1)/7", [Fraction(5,7),Fraction(1,7),Fraction(1,7)]),
        ("(3,3,1)/7", [Fraction(3,7),Fraction(3,7),Fraction(1,7)]),
        ("(3,2,2)/7", [Fraction(3,7),Fraction(2,7),Fraction(2,7)]),
        ("(6,1)/7... no", [Fraction(6,7),Fraction(1,7)]),
    ]:
        if sum(cfg)!=1: continue
        # parallel halve: split 2 largest in half
        s = sorted(cfg, reverse=True)
        out = []
        for i,x in enumerate(s):
            if i < n: out.extend([x/2, x/2])
            else: out.append(x)
        D = D_alt(out)
        print(f"  {desc}: {sorted(cfg,reverse=True)} -> halved={sorted(out,reverse=True)}, D={float(D):.6f} ({'<=1/7' if D<=Dtarget else '>1/7 FAIL'})")

# The real Xiang-best for these (grid search)
def xiang_best(pieces, marks, grid=14):
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

print()
print("Xiang-best (D = 2*odd - 1) for these n=2 configs:")
for desc, cfg in [
    ("tower", [Fraction(4,7),Fraction(2,7),Fraction(1,7)]),
    ("(5,1,1)/7", [Fraction(5,7),Fraction(1,7),Fraction(1,7)]),
    ("(3,3,1)/7", [Fraction(3,7),Fraction(3,7),Fraction(1,7)]),
    ("(3,2,2)/7", [Fraction(3,7),Fraction(2,7),Fraction(2,7)]),
    ("(6,1)/7", [Fraction(6,7),Fraction(1,7)]),
    ("(5,2)/7", [Fraction(5,7),Fraction(2,7)]),
    ("(4,3)/7", [Fraction(4,7),Fraction(3,7)]),
]:
    if sum(cfg)!=1: continue
    v = xiang_best(cfg, 2, grid=14)
    D = 2*v - 1
    print(f"  {desc}: odd={float(v):.6f}, D={float(D):.6f} ({D}), {'<=1/7' if D<=Fraction(1,7) else '>1/7'}")
