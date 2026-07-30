"""
Trace optimal Xiang move in the adversarial non-dominant case
(a_3 > a_1/2), where the simple 'halve max -> IH' induction BREAKS.
What move actually achieves D* <= M/2^n? Is it halve a_2? pair a_2 with a_3?
Characterize for the outliner.
"""
from fractions import Fraction as F
from xiang_optimizer import D_of

def trace(cfg, k, depth=0):
    best_d = D_of(cfg); best_seq = []
    if k == 0: return best_d, best_seq
    for i in range(len(cfg)):
        piece = cfg[i]; rest = cfg[:i] + cfg[i+1:]
        cs = {piece/2}
        for p in cfg:
            if 0 < p < piece: cs.add(p); cs.add(piece-p)
        for q in cs:
            if 0 < q < piece:
                d, seq = trace(rest + [q, piece-q], k-1, depth+1)
                if d < best_d - 1e-12:
                    best_d = d; best_seq = [(i, piece, q, piece-q)] + seq
    return best_d, best_seq

n = 2
cases = [
    ([0.40, 0.35, 0.25], "a3=0.25 > a1/2=0.20"),
    ([0.42, 0.30, 0.28], "a3=0.28 > a1/2=0.21"),
    ([0.45, 0.28, 0.27], "a3=0.27 > a1/2=0.225"),
    ([0.49, 0.27, 0.24], "a3=0.24 < a1/2=0.245 (dominant-ish)"),
    ([4/7, 2/7, 1/7], "tower T_2"),
]
for cfg, note in cases:
    cfg = sorted(cfg, reverse=True)
    d, seq = trace(cfg, n)
    M = max(cfg); b = M/2**n
    print(f"cfg={[round(x,4) for x in cfg]} {note}")
    print(f"  D*={d:.5f} M/2^n={b:.5f} ratio={d/b:.4f}")
    for (i,p,q,r) in seq:
        print(f"    split piece[{i}]={p:.4f} -> {q:.4f}+{r:.4f} (halve? {abs(q-r)<1e-9}, tie-to? {[round(x,4) for x in cfg if abs(q-x)<1e-4 or abs(r-x)<1e-4]})")
    # show final
    final = list(cfg)
    for (i,p,q,r) in seq:
        idx = final.index(p); final = final[:idx]+final[idx+1:]+[q,r]
    sf = sorted(final, reverse=True)
    print(f"  final={[round(x,4) for x in sf]} D={D_of(sf):.5f}")
    print()

# n=3 adversarial non-dominant
print("=== n=3 ===")
n=3
cases3 = [
    [0.30, 0.25, 0.24, 0.21],
    [0.28, 0.26, 0.24, 0.22],
    [0.27, 0.26, 0.25, 0.22],
    [8/15, 4/15, 2/15, 1/15],
]
for cfg in cases3:
    cfg = sorted(cfg, reverse=True)
    d, seq = trace(cfg, n)
    M=max(cfg); b=M/2**n
    print(f"cfg={[round(x,4) for x in cfg]} D*={d:.5f} M/2^n={b:.5f} ratio={d/b:.4f}")
    for (i,p,q,r) in seq:
        print(f"    split piece[{i}]={p:.4f} -> {q:.4f}+{r:.4f}")
    print()
