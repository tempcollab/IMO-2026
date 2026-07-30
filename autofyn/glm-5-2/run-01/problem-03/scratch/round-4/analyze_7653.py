"""
Deep analysis of the (7,6,5,3)/21 counterexample to the Max-bound.
D* = 1/21, M/8 = 1/24, ratio 8/7. But D* < 1/15 (actual target).
Trace the optimal Xiang strategy, understand the structure.
"""
from fractions import Fraction as F

def D_of_e(ps):
    s = sorted(ps, reverse=True)
    v = F(0)
    for i,x in enumerate(s): v += x*(1 if i%2==0 else -1)
    return v

def bp_splits_e(piece, allp):
    cs = {piece/2}
    for p in allp:
        if 0 < p < piece: cs.add(p); cs.add(piece-p)
    return [(q,piece-q) for q in cs if 0<q<piece]

def min_D_e_trace(cfg, k):
    best = D_of_e(cfg); best_seq=[]
    if k==0: return best, best_seq
    cs = sorted(cfg, reverse=True)
    for i in range(len(cs)):
        piece=cs[i]; rest=cs[:i]+cs[i+1:]
        for (q,r) in bp_splits_e(piece, cs):
            d, seq = min_D_e_trace(rest+[q,r], k-1)
            if d < best:
                best=d; best_seq=[(piece,q,r)]+seq
    return best, best_seq

cfg = [F(7,21), F(6,21), F(5,21), F(3,21)]
print("Config (7,6,5,3)/21:")
print(f"  pieces = {[float(x) for x in cfg]}")
print(f"  M = 7/21 = {float(F(7,21)):.6f}")
print(f"  M_2 = 6/21 = {float(F(6,21)):.6f}")
print(f"  a3 = 5/21 = {float(F(5,21)):.6f}")
print(f"  a4 = 3/21 = {float(F(3,21)):.6f}")
print(f"  a1 < 2*a2? {F(7,21) < 2*F(6,21)} (7 < 12)")
print(f"  a3 > a1/2? {F(5,21) > F(7,21)/2} (5 > 3.5)")
print(f"  D(cfg) = {D_of_e(cfg)} = {float(D_of_e(cfg)):.6f}")
print(f"  M/8 = {F(7,21)/8} = {float(F(7,21)/8):.6f}")
print(f"  target 1/15 = {float(F(1,15)):.6f}")

d, seq = min_D_e_trace(cfg, 3)
print(f"\n  D* = {d} = {float(d):.6f}")
print(f"  moves:")
final = list(cfg)
for (p,q,r) in seq:
    print(f"    split {p}={float(p):.6f} -> {q}={float(q):.6f} + {r}={float(r):.6f}")
    idx = final.index(p); final = final[:idx]+final[idx+1:]+[q,r]
sf = sorted(final, reverse=True)
print(f"  final sorted = {[float(x) for x in sf]}")
print(f"  final D = {D_of_e(sf)} = {float(D_of_e(sf)):.6f}")
# show the pair structure
print(f"  final pairs: ", end="")
i=0
while i < len(sf):
    if i+1 < len(sf) and sf[i]==sf[i+1]:
        print(f"({float(sf[i]):.5f},{float(sf[i+1]):.5f})cancel", end=" ")
        i+=2
    else:
        print(f"[{float(sf[i]):.5f}]", end=" ")
        i+=1
print()

# What is the residual? The unpaired piece.
# Let's understand: what bound DOES hold?
# The actual target is 1/D_n = 1/15. D* = 1/21 < 1/15. OK.
# The Max-bound M/8 = 1/24 < D* = 1/21. So Max-bound FAILS.
# What about M_2/8? = (6/21)/8 = 6/168 = 1/28. Even smaller, worse.
# What about (M+M_2)/8? = (13/21)/8 = 13/168. D*=1/21=8/168. 8<13 OK.
# What about a3/4? = (5/21)/4 = 5/84. D*=1/21=4/84. 4<5 OK.
# What about (a1+a2+a3)/8? = 18/21/8 = 18/168 = 3/28. D*=8/168. 8<18 OK (loose).
# Let's test candidate bounds:
M, M2, a3, a4 = F(7,21), F(6,21), F(5,21), F(3,21)
print(f"\n  Candidate bounds (must be >= D*={d}={float(d):.6f}):")
print(f"    M/8 = {M/8} = {float(M/8):.6f}  {'OK' if d<=M/8 else 'FAIL'}")
print(f"    M2/8 = {M2/8} = {float(M2/8):.6f}  {'OK' if d<=M2/8 else 'FAIL'}")
print(f"    (M+M2)/8 = {(M+M2)/8} = {float((M+M2)/8):.6f}  {'OK' if d<=(M+M2)/8 else 'FAIL'}")
print(f"    (M+M2+a3)/8 = {(M+M2+a3)/8} = {float((M+M2+a3)/8):.6f}  {'OK' if d<=(M+M2+a3)/8 else 'FAIL'}")
print(f"    a3/4 = {a3/4} = {float(a3/4):.6f}  {'OK' if d<=a3/4 else 'FAIL'}")
print(f"    (M-a2)/1 = a1-a2 = {M-M2} = {float(M-M2):.6f}  (residual) {'OK' if d<=M-M2 else 'FAIL'}")
# The residual after pairing a1 with a2 is a1-a2 = 1/21 = D*!
print(f"    a1-a2 = {M-M2} = {float(M-M2):.6f}  <-- equals D*!")
# Interesting: D* = a1 - a2 = 1/21.
# Check: after pairing a1->{a2, a1-a2}, two a2's cancel, rest' = {a3, a4, a1-a2}.
# Then halve a3 -> two a3/2, halve a4 -> two a4/2. rest' has {a3/2,a3/2,a4/2,a4/2,a1-a2}.
# sorted: a3/2=5/42, a4/2=3/42=1/14, a1-a2=1/21=2/42.
# sorted desc: 5/42, 2/42, 1/14=3/42? wait 1/14 = 3/42. So sorted: 5/42, 3/42, 2/42.
# Hmm that's 3 pieces after the 2 pairs cancel. Let me recompute.
print()
print("  After pairing a1->{a2, a1-a2} and halving a3, a4:")
rest_prime = sorted([a3, a4, M-M2], reverse=True)
print(f"    rest' (before halving) = {[float(x) for x in rest_prime]}")
# with 2 more marks: halve a3 and halve a4
rest2 = sorted([a3/2, a3/2, a4/2, a4/2, M-M2], reverse=True)
print(f"    after halve a3, a4: {[float(x) for x in rest2]}")
print(f"    D(rest2) = {D_of_e(rest2)} = {float(D_of_e(rest2)):.6f}")
# the two a3/2 cancel, two a4/2 cancel, leaving a1-a2 at... position?
# sorted desc: a3/2=5/42≈0.119, a4/2=3/42≈0.071, a1-a2=2/42≈0.048
# Wait a3/2 = 5/42, a4/2 = 1/14 = 3/42, a1-a2 = 1/21 = 2/42
# sorted desc: 5/42, 3/42, 2/42 (but two copies of each except a1-a2)
# [5/42, 5/42, 3/42, 3/42, 2/42]
# D = 5/42 - 5/42 + 3/42 - 3/42 + 2/42 = 2/42 = 1/21. YES = a1-a2.
print(f"    a1-a2 = {M-M2} = {float(M-M2):.6f} = D* ✓ (residual = D*)")
