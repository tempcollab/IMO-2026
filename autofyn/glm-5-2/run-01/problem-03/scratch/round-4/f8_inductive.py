"""
Trace the optimal Xiang strategy for f8 = M2/2^{n-1} in the crux.
Key question: what 2-mark move reduces the (M, M2) problem by 2 levels?
Hypothesis: pair a_1 (1 mark, cancels a_2), then pair a_3 (1 mark, cancels a_4 or a_1-a_2),
using 2 marks to drop from n to n-2, with the bound M2/2^{n-1} -> M2'/2^{n-3}.
"""
from fractions import Fraction as F

def D_of(ps):
    s = sorted(ps, reverse=True)
    v = F(0)
    for i,x in enumerate(s): v += x*(1 if i%2==0 else -1)
    return v
def bp_splits(piece, allp):
    cs = {piece/2}
    for p in allp:
        if 0 < p < piece: cs.add(p); cs.add(piece-p)
    return [(q,piece-q) for q in cs if 0<q<piece]
def min_D_trace(cfg, k):
    best = D_of(cfg); best_seq=[]
    if k==0: return best, best_seq
    cs = sorted(cfg, reverse=True)
    for i in range(len(cs)):
        piece=cs[i]; rest=cs[:i]+cs[i+1:]
        for (q,r) in bp_splits(piece, cs):
            d, seq = min_D_trace(rest+[q,r], k-1)
            if d < best:
                best=d; best_seq=[(piece,q,r)]+seq
    return best, best_seq

# Test crux configs and trace the optimal strategy
configs = [
    ([F(7,21),F(6,21),F(5,21),F(3,21)], "(7,6,5,3)/21"),
    ([F(22,67),F(19,67),F(16,67),F(10,67)], "(22,19,16,10)/67"),
    ([F(15,45),F(13,45),F(11,45),F(6,45)], "(15,13,11,6)/45"),
]
for cfg, name in configs:
    d, seq = min_D_trace(cfg, 3)
    M, M2, a3, a4 = sorted(cfg, reverse=True)
    print(f"{name}: D*={d}={float(d):.6f} M2/4={M2/4}={float(M2/4):.6f} ratio={float(d/(M2/4)):.4f}")
    final = list(cfg)
    for (p,q,r) in seq:
        idx = final.index(p); final = final[:idx]+final[idx+1:]+[q,r]
        print(f"  split {float(p):.5f} -> {float(q):.5f}+{float(r):.5f}")
    sf = sorted(final, reverse=True)
    print(f"  final = {[float(x) for x in sf]} D={float(D_of(sf)):.6f}")
    # identify pairs
    i=0; pairs=[]; unpaired=[]
    used = [False]*len(sf)
    for i in range(len(sf)):
        if used[i]: continue
        if i+1 < len(sf) and sf[i]==sf[i+1] and not used[i+1]:
            pairs.append(sf[i]); used[i]=True; used[i+1]=True
        else:
            unpaired.append(sf[i]); used[i]=True
    print(f"  canceling pairs: {[float(x) for x in pairs]}")
    print(f"  unpaired residuals: {[float(x) for x in unpaired]}")
    print()

# Now: the key structural question. After 2 marks (pair a_1, pair a_3),
# does the rest satisfy a clean bound?
print("=== 2-mark reduction analysis ===")
for cfg, name in configs:
    M, M2, a3, a4 = sorted(cfg, reverse=True)
    # pair a_1 -> {a_2, a_1-a_2}, pair a_3 -> {a_4, a_3-a_4} (if a_3 >= 2*a_4)
    # OR pair a_3 -> {a_1-a_2, a_3-(a_1-a_2)} etc.
    # The trace shows the actual optimal. Let's see if 2 marks suffice to get
    # the rest into a form where the (n-2)-IH M2'/2^{n-3} closes.
    # After 2 marks, rest'' has second-largest M2''.
    # The bound we need: D(rest'') <= M2''/2^{n-3} = M2''/2 (for n=3, n-2=1).
    # For n=3, after 2 marks we have 1 mark left. The 1-mark bound is M2/2 (n=1: M2/2^0=M2... no).
    # Actually for n=1: f8 = M2/2^0 = M2. The 1-mark bound is D* <= M2 (second largest).
    # With 1 mark on a 2-piece config {x,y}: D=x-y, halve x -> {x/2,x/2,y}, D=x/2-x/2+y... no.
    # D({x/2,x/2,y}) sorted: if x/2 >= y: x/2 - x/2 + y = y. If x/2 < y: y - x/2 + ... depends.
    # Let's just compute.
    print(f"{name}: after optimal 2 marks, what's the rest?")
    # Use the trace's first 2 moves
    d, seq = min_D_trace(cfg, 3)
    if len(seq) >= 2:
        final = list(cfg)
        for (p,q,r) in seq[:2]:
            idx = final.index(p); final = final[:idx]+final[idx+1:]+[q,r]
        sf = sorted(final, reverse=True)
        # the remaining config with 1 mark left
        d1 = D_of(sf)
        # best 1-mark on sf
        best1 = d1; best_cfg1 = sf
        for i in range(len(sf)):
            piece=sf[i]; rest=sf[:i]+sf[i+1:]
            for (q,r) in bp_splits(piece, sf):
                dd = D_of(sorted(rest+[q,r], reverse=True))
                if dd < best1: best1=dd; best_cfg1=sorted(rest+[q,r],reverse=True)
        M2_rest = sorted(sf,reverse=True)[1] if len(sf)>=2 else 0
        print(f"  after 2 marks: {sf} D={float(d1):.6f}, best 1-mark D*={float(best1):.6f}")
        print(f"  M2(rest)={float(M2_rest):.6f}, M2(rest)/2={float(M2_rest/2):.6f}")
        print(f"  f8 check: D*(rest,1mark)={float(best1):.6f} <= M2(rest)/2^0={float(M2_rest):.6f}? {best1<=M2_rest+1e-12}")
        print(f"  f8 check: D*(rest,1mark)={float(best1):.6f} <= M2(rest)/2={float(M2_rest/2):.6f}? {best1<=M2_rest/2+1e-12}")
    print()
