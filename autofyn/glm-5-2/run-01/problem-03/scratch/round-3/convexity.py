import numpy as np
from itertools import product

def claim_value(pieces):
    s=sorted(pieces, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))
def Dval(pieces):
    return 2*claim_value(pieces)-sum(pieces)

# Tower T_n unnormalized: [1,2,...,2^n]
def tower(n): return [2**k for k in range(0,n+1)]

# === n=2 convexity: tower [1,2,4], Xiang 2 marks. Parametrize cuts on the size-axis-per-piece.
# A refinement: for each piece, a list of cut fractions in (0,1). total marks<=2.
# Let Xiang place 2 marks anywhere. We scan over a fine grid of (piece_index, fraction) and compute D.
# Simpler: enumerate all ways to put 2 marks among the 3 pieces (multi-mark per piece allowed), grid of fractions.

def xiang_D_surface(liu_pieces, n, grid=200):
    pts=np.linspace(0,1,grid+2)[1:-1]  # interior grid points
    # generate cut options: list of (piece_idx, fraction). choose up to n cuts, each on a piece.
    # For n=2 small, enumerate pairs (incl. both on same piece).
    # cut = (piece_idx, frac). marks = number of cuts. We fix exactly n cuts (can also use fewer, but min D with more cuts <= fewer, so use exactly n).
    bestD=None; bestcfg=None; minima=[]
    npieces=len(liu_pieces)
    # all single cuts
    singlecuts=[]
    for pi in range(npieces):
        for f in pts:
            singlecuts.append((pi,f))
    # exactly 2 cuts (with replacement, could be same piece different frac)
    # too many (npieces*grid)^2; use coarser grid for the 2-cut scan
    cg=np.linspace(0,1,81)[1:-1]
    cutset=[]
    for pi in range(npieces):
        for f in cg: cutset.append((pi,f))
    Darr=[]
    for i in range(len(cutset)):
        for j in range(i,len(cutset)):
            cuts=[cutset[i],cutset[j]]
            # must be on distinct pieces OR distinct fractions on same piece; if same piece same frac skip
            # build refined pieces
            perpiece=[[] for _ in range(npieces)]
            for (pi,f) in cuts:
                perpiece[pi].append(f)
            ok=True
            parts_all=[]
            for pi in range(npieces):
                fs=sorted(perpiece[pi])
                size=liu_pieces[pi]
                prev=0; segs=[]
                for f in fs:
                    segs.append(size*(f-prev)); prev=f
                segs.append(size*(1-prev))
                if any(s<=0 for s in segs): ok=False; break
                parts_all.extend(segs)
            if not ok: continue
            D=Dval(parts_all)
            Darr.append((D, cuts))
    Darr.sort()
    print("  n=2 tower: min D (grid80, 2 cuts):", Darr[0][0], "at cuts", Darr[0][1])
    print("  target D=1 (unnormalized).")
    # how many near-min (D<1.05)?
    near=[d for d,_ in Darr if d<1.05]
    print("  #configs with D<1.05:", len(near), "out of", len(Darr))
    print("  top-8 minimizers:")
    for D,cuts in Darr[:8]:
        print("    D=%.4f cuts=%s"%(D,cuts))
    print("  max D:", Darr[-1][0])

xiang_D_surface(tower(2),2)
print()
# n=3 tower [1,2,4,8], 3 marks - coarser
def xiang_D_surface_n3(liu_pieces, n, grid=40):
    cg=np.linspace(0,1,grid+2)[1:-1]
    npieces=len(liu_pieces)
    cutset=[]
    for pi in range(npieces):
        for f in cg: cutset.append((pi,f))
    best=None; bestcuts=None
    # 3 cuts with replacement - too many combos (npieces*grid choose 3 ~ big). subsample.
    import random
    random.seed(1)
    # enumerate all triples i<=j<=k
    N=len(cutset)
    print(f"  cutset size {N}, triples ~ {N**3//6}")
    cnt=0; best=None; bestcuts=None; near=0; total=0
    for i in range(N):
        ci=cutset[i]
        for j in range(i,N):
            cj=cutset[j]
            for k in range(j,N):
                ck=cutset[k]
                cuts=[ci,cj,ck]
                perpiece=[[] for _ in range(npieces)]
                for (pi,f) in cuts: perpiece[pi].append(f)
                ok=True; parts=[]
                for pi in range(npieces):
                    fs=sorted(perpiece[pi]); size=liu_pieces[pi]; prev=0; segs=[]
                    for f in fs: segs.append(size*(f-prev)); prev=f
                    segs.append(size*(1-prev))
                    if any(s<=0 for s in segs): ok=False;break
                    parts.extend(segs)
                if not ok: continue
                D=Dval(parts); total+=1
                if best is None or D<best: best=D; bestcuts=cuts
                if D<1.02: near+=1
    print(f"  n=3 tower: min D (grid{grid},3cuts): {best:.5f} target 1; near(<1.02)={near}/{total}")
    print("  minimizer cuts:", bestcuts)

xiang_D_surface_n3(tower(3),3,grid=30)
