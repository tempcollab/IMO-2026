from fractions import Fraction as F
from itertools import combinations, product
import math

def alt_sum(m):
    s=F(0)
    for i,x in enumerate(sorted(m,reverse=True)):
        s += (x if i%2==0 else -x)
    return s

TARGET = F(1,7)

def xiang_min_D(liu_cfg, nmarks):
    """Brute force: Xiang places <= nmarks marks refining pieces. 
    Each mark splits one piece into two positive parts. Enumerate all 1-mark, 2-mark refinements on a fine grid."""
    # We enumerate over split positions on a grid, with multiplicity for which piece is split.
    # For thoroughness, use grid step g.
    g = 24  # 1/g grid in real units; since values are fractions, use Fraction grid over each piece
    best = None
    pieces = list(liu_cfg)
    # 2 marks: enumerate (piece1, q1, piece2, q2) where q is in (0, len(piece)/2]  (the smaller fragment)
    # But Xiang can split either the same piece twice or two different pieces.
    # To keep exhaustive-ish, grid each piece's split position.
    def splits_of(piece_len):
        # all possible single splits p+q=piece_len, p>=q, on grid step = piece_len/g
        out=[]
        for i in range(1,g):
            q = piece_len * F(i,g)
            if q > piece_len/2: break
            p = piece_len - q
            out.append((p,q))
        return out
    # 0 marks
    D0 = alt_sum(pieces)
    if best is None or D0<best: best=D0
    if nmarks>=1:
        for idx in range(len(pieces)):
            for (p,q) in splits_of(pieces[idx]):
                new_pieces = pieces[:idx] + [p,q] + pieces[idx+1:]
                D1 = alt_sum(new_pieces)
                if best is None or D1<best: best=D1
                if nmarks>=2:
                    # second mark: split any piece (including the new ones) 
                    for idx2 in range(len(new_pieces)):
                        for (p2,q2) in splits_of(new_pieces[idx2]):
                            new2 = new_pieces[:idx2] + [p2,q2] + new2[idx2+1:] if False else (new_pieces[:idx2] + [p2,q2] + new_pieces[idx2+1:])
                            D2 = alt_sum(new2)
                            if best is None or D2<best: best=D2
    return best

# Enumerate Liu configs for n=2: m in {1,2,3}, pieces sum to 1, sorted desc, on a grid.
# Use grid step 1/28 (finer than 1/7 to catch breakpoints). 
print("== n=2 exhaustive upper bound check ==")
violations=0
worst=None
worst_cfg=None
tested=0
G=28
# m=1: single piece a1=1
for m in [1,2,3]:
    if m==1:
        cfgs=[[F(1)]]
    elif m==2:
        cfgs=[]
        for i in range(G//2, G+1):
            a = F(i,G)
            b = F(1)-a
            if b>=0 and b<=a:
                cfgs.append([a,b])
    else: # m==3
        cfgs=[]
        for i in range(0,G+1):
            for j in range(0,i+1):
                a1=F(i,G); a2=F(j,G)
                a3=F(1)-a1-a2
                if a3<0: continue
                if a3>a2: continue
                if a2>a1: continue
                cfgs.append([a1,a2,a3])
    for cfg in cfgs:
        tested+=1
        D = xiang_min_D(cfg, 2)
        if D > TARGET:
            violations+=1
            if worst is None or D>worst:
                worst=D; worst_cfg=cfg
print(f"tested={tested}, violations(D>1/7)={violations}, worst={worst} at {worst_cfg}")
# also check equality cases (tower T_2 = 4/7,2/7,1/7)
T2=[F(4,7),F(2,7),F(1,7)]
print(f"T2 Xiang min D = {xiang_min_D(T2,2)} (should be 1/7)")
