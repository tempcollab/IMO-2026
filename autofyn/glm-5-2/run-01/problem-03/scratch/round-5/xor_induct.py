"""
Critical test for the XOR/overlap induction:
  G1(n): "every <= n-mark refinement of T_n has D >= 1"
  XOR: D = D_F + D_R - 2C,  R = refinement of T_{n-1} (<= n-1 marks).
  By G1(n-1): D_R >= 1.  Need D_F >= 2C  (then D >= 2C + 1 - 2C = 1).

  KEY LEMMA to prove: for every refinement R of T_{n-1} (any, incl G1 hard case)
  and every split F of the top 2^n, D_F(F) >= 2*C(F,R).

  Test exhaustively over breakpoint refinements R of T_{n-1} and breakpoint splits F.
  Also: is D_F >= 2C independent of G1(R) status? (does it hold even for R with D_R < 1, if any?)
"""
from fractions import Fraction as F
import random

def D_of(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**k)*v for k,v in enumerate(s))

def D_integral(pieces):
    s = sorted(set([F(0)] + [p for p in pieces]), reverse=False)
    total = F(0)
    for i in range(len(s)-1):
        lo, hi = s[i], s[i+1]; mid = (lo+hi)/2
        N = sum(1 for p in pieces if p >= mid)
        if N % 2 == 1: total += (hi - lo)
    return total

def overlap_C(Fp, Rp):
    allvals = sorted(set([F(0)] + list(Fp) + list(Rp)), reverse=False)
    total = F(0)
    for i in range(len(allvals)-1):
        lo, hi = allvals[i], allvals[i+1]; mid = (lo+hi)/2
        NF = sum(1 for p in Fp if p >= mid); NR = sum(1 for p in Rp if p >= mid)
        if NF % 2 == 1 and NR % 2 == 1: total += (hi - lo)
    return total

def tower(n): return [F(2**k) for k in range(n,-1,-1)]

def breakpoint_refine(T, max_marks):
    """Enumerate breakpoint (tie) refinements. Returns set of sorted tuples."""
    start = tuple(sorted(T, reverse=True))
    results = {start}; frontier=[(start,0)]; seen={start:0}
    while frontier:
        config, marks = frontier.pop()
        if marks >= max_marks: continue
        pieces = list(config); vals = sorted(set(pieces), reverse=True)
        for i, V in enumerate(pieces):
            cutset = set()
            for v in vals:
                if F(0) < v < V: cutset.add(v); cutset.add(V-v)
            k=0
            while (1<<k) < V:
                f=F(1<<k)
                if F(0)<f<V: cutset.add(f)
                k+=1
            for f in cutset:
                if F(0) < f < V:
                    new = [p for j,p in enumerate(pieces) if j != i]
                    new.append(f); new.append(V-f)
                    nc = tuple(sorted(new, reverse=True))
                    if nc not in seen or seen[nc]>marks+1:
                        seen[nc]=marks+1; results.add(nc); frontier.append((nc,marks+1))
    return list(results)

def top_splits(top_val, max_marks):
    """Enumerate breakpoint splits of a single piece top_val into fragments."""
    return breakpoint_refine([top_val], max_marks)

# Exhaustive test: for n, enumerate breakpoint refinements R of T_{n-1} and
# breakpoint splits F of 2^n, check D_F >= 2C.
print("Exhaustive: D_F >= 2C over breakpoint F (split of 2^n) x breakpoint R (ref of T_{n-1}):")
for n in [2,3,4]:
    top = F(2**n)
    # R: breakpoint refinements of T_{n-1} with up to n-1 marks
    R_cfgs = breakpoint_refine(tower(n-1), n-1)
    # F: breakpoint splits of top with up to n marks
    F_cfgs = top_splits(top, n)
    print(f"  T_{n}: {len(F_cfgs)} F-splits x {len(R_cfgs)} R-refinements = {len(F_cfgs)*len(R_cfgs)} pairs")
    fails = 0; worst=F(0); worstinfo=None
    minD = None; tight_count=0
    for fc in F_cfgs:
        Fp = list(fc)
        DF = D_integral(Fp)
        for rc in R_cfgs:
            Rp = list(rc)
            C = overlap_C(Fp, Rp)
            if DF < 2*C:
                fails += 1
                if 2*C - DF > worst:
                    worst = 2*C - DF; worstinfo = (fc, rc, DF, C)
            # also check global D >= 1
            Dg = D_of(Fp + Rp)
            if minD is None or Dg < minD: minD = Dg
            if Dg == 1 and DF == 2*C: tight_count += 1
    print(f"    D_F < 2C failures: {fails}/{len(F_cfgs)*len(R_cfgs)}")
    if worstinfo: print(f"    worst deficit: {worst} at F={worstinfo[0]}, R={worstinfo[1]}, D_F={worstinfo[2]}, C={worstinfo[3]}")
    print(f"    min global D = {minD}, #tight(D=1 & D_F=2C) = {tight_count}")

print()
print("Does D_F >= 2C hold for R = T_{n-1} itself (unsplit, the easy base)?")
for n in [2,3,4,5]:
    top=F(2**n); Rp=tower(n-1)
    F_cfgs = top_splits(top, n)
    fails=0
    for fc in F_cfgs:
        Fp=list(fc); DF=D_integral(Fp); C=overlap_C(Fp,Rp)
        if DF < 2*C: fails+=1
    print(f"  T_{n}, R=T_{n-1} unsplit: {fails}/{len(F_cfgs)} F-splits violate D_F>=2C")
