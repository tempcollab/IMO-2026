"""
Xiang optimizer: compute min D over Xiang's <=k marks for a Liu config.
D = alternating sum of sorted multiset (a_1 - a_2 + a_3 - ...).
Xiang's move: pick one piece, split into two positive parts (one mark).
By Lemma B1 (pl-breakpoint-minimum), the global optimum is at a breakpoint
(tie) refinement. We search breakpoint split candidates recursively:
  - half split (q = piece/2)
  - tie-to-each-existing-piece (fragment = each other piece value, if < piece)
  - grid points for safety (to catch non-breakpoint local mins that B1 says don't win)
Uses floating point for search speed; key results re-verified with Fractions.
"""
import numpy as np
from itertools import product

def D_of(pieces):
    s = sorted(pieces, reverse=True)
    return sum(s[i] * (1 if i % 2 == 0 else -1) for i in range(len(s)))

def candidate_splits(piece, all_pieces, n_grid=8):
    """Candidate split positions q in (0, piece): fragment = q, piece-q.
    Breakpoints: q = piece/2 (equal halves); q = each other piece value (tie);
    plus a fine grid to be safe."""
    cands = set()
    cands.add(piece / 2.0)
    for p in all_pieces:
        if 0 < p < piece:
            cands.add(p)            # fragment ties p
            cands.add(piece - p)    # other fragment ties p
    for i in range(1, n_grid):
        cands.add(piece * i / n_grid)
    return [(q, piece - q) for q in cands if 0 < q < piece]

def min_D(config, k, n_grid=8):
    """Min D over <=k Xiang marks. config = list of piece sizes (floats)."""
    best = D_of(config)
    if k == 0:
        return best
    # try splitting each piece
    for i in range(len(config)):
        piece = config[i]
        rest = config[:i] + config[i+1:]
        for (q, r) in candidate_splits(piece, config, n_grid):
            new = rest + [q, r]
            d = min_D(new, k - 1, n_grid)
            if d < best:
                best = d
    return best

def min_D_exact_check(config, k):
    """Exact Fraction check of a claimed min via the same breakpoint recursion."""
    from fractions import Fraction as F
    def D_of_e(ps):
        s = sorted(ps, reverse=True)
        v = F(0)
        for i, x in enumerate(s):
            v += x * (1 if i % 2 == 0 else -1)
        return v
    def cands(piece, allp):
        cs = set()
        cs.add(piece / 2)
        for p in allp:
            if 0 < p < piece:
                cs.add(p); cs.add(piece - p)
        return [(q, piece - q) for q in cs if 0 < q < piece]
    def rec(cfg, kk):
        b = D_of_e(cfg)
        if kk == 0:
            return b
        for i in range(len(cfg)):
            piece = cfg[i]
            rest = cfg[:i] + cfg[i+1:]
            for (q, r) in cands(piece, cfg):
                d = rec(rest + [q, r], kk - 1)
                if d < b:
                    b = d
        return b
    return rec([F(x).limit_denominator(10**6) for x in config], k)

if __name__ == "__main__":
    # sanity: tower T_2 = (4,2,1)/7, n=2 -> D* should be 1/7
    T2 = [4/7, 2/7, 1/7]
    print("T_2 n=2:", min_D(T2, 2), "target", 1/7)
    # non-tower /7 configs -> should give 0
    for cfg in [(5,1,1), (3,3,1), (3,2,2), (5,2), (4,3), (6,1)]:
        c = [x/7 for x in cfg]
        print(cfg, "n=2:", min_D(c, 2))
    # tower T_3 = (8,4,2,1)/15, n=3 -> target 1/15
    T3 = [8/15, 4/15, 2/15, 1/15]
    print("T_3 n=3:", min_D(T3, 3), "target", 1/15)
