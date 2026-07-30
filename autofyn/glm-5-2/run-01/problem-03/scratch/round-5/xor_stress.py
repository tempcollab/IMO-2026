"""
Stress-test the D_F >= 2C bound:
  (1) Is it tight at global minimizers (D=1)?
  (2) Does it hold for ARBITRARY R (mass 2^n-1, not tower refinement)?
  (3) Does it hold for arbitrary F (split of 2^n) with arbitrary R?
  (4) What is the structure of C -- can we prove C <= D_F/2 structurally?
"""
from fractions import Fraction as F
import random
random.seed(7)

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

def random_refine(T, nmarks):
    pieces = list(T)
    for _ in range(nmarks):
        if len(pieces) <= 1: break
        idx = random.randrange(len(pieces)); V = pieces[idx]
        f = V * F(random.randint(1, 8), 16)
        if f <= 0 or f >= V: continue
        pieces = pieces[:idx] + [f, V-f] + pieces[idx+1:]
    return sorted(pieces, reverse=True)

# (1) At minimizers D=1, is D_F = 2C tight?  Search for D=1 configs.
print("(1) Searching for D=1 minimizers and checking D_F vs 2C:")
for n in [3,4,5]:
    T = tower(n); top=T[0]; below=T[1:]
    found = []
    for trial in range(20000):
        ntop = random.randint(1, n); nbelow = random.randint(0, n-ntop)
        top_frags = random_refine([top], ntop)
        below_pieces = random_refine(below, nbelow)
        Dg = D_of(top_frags + below_pieces)
        if Dg == 1:
            DF = D_integral(top_frags); DR = D_integral(below_pieces)
            C = overlap_C(top_frags, below_pieces)
            found.append((DF, DR, C, top_frags, below_pieces))
    print(f"  T_{n}: {len(found)} minimizers found.")
    if found:
        # check tightness D_F = 2C?
        tight = sum(1 for DF,DR,C,_,_ in found if DF == 2*C)
        print(f"    D_F == 2C in {tight}/{len(found)} minimizers.")
        print(f"    D_F - 2C range: [{min(DF-2*C for DF,DR,C,_,_ in found)}, {max(DF-2*C for DF,DR,C,_,_ in found)}]")
        print(f"    D_R range: [{min(DR for DF,DR,C,_,_ in found)}, {max(DR for DF,DR,C,_,_ in found)}]")
        print(f"    C range: [{min(C for DF,DR,C,_,_ in found)}, {max(C for DF,DR,C,_,_ in found)}]")
        ex = found[0]
        print(f"    example: D_F={ex[0]}, D_R={ex[1]}, C={ex[2]}, top_frags={ex[3]}, below={ex[4][:5]}")

# (2) Does D_F >= 2C hold for ARBITRARY R (mass 2^n-1, random pieces, NOT tower refinement)?
print("\n(2) D_F >= 2C with ARBITRARY R (random mass-2^n-1 multiset, not tower ref):")
for n in [3,4]:
    T = tower(n); top=T[0]; target_below = F(2**n - 1)
    fails = 0; worst=None; trials=8000
    for trial in range(trials):
        ntop = random.randint(1, n)
        top_frags = random_refine([top], ntop)
        # arbitrary R: random pieces summing to 2^n-1
        npieces = random.randint(1, 6)
        raw = [F(random.randint(1,9)) for _ in range(npieces)]
        sraw = sum(raw)
        Rp = [r * target_below / sraw for r in raw]  # scale to mass 2^n-1
        DF = D_integral(top_frags); C = overlap_C(top_frags, Rp)
        if DF < 2*C:
            fails += 1
            if worst is None or (2*C-DF) > worst[0]: worst = (2*C-DF, DF, C, top_frags, Rp)
    print(f"  T_{n}: D_F < 2C in {fails}/{trials} arbitrary-R cases.", end="")
    if worst: print(f" worst deficit {worst[0]} (D_F={worst[1]},C={worst[2]})")
    else: print(" (never violated)")

# (3) Does D_F >= 2C hold for arbitrary F (mass 2^n) AND arbitrary R (mass 2^n-1)?
print("\n(3) D_F >= 2C with ARBITRARY F (mass 2^n) AND arbitrary R (mass 2^n-1):")
for n in [3,4]:
    target_top = F(2**n); target_below = F(2**n - 1)
    fails=0; worst=None; trials=8000
    for trial in range(trials):
        nf = random.randint(1,5); nr = random.randint(1,5)
        rawf = [F(random.randint(1,9)) for _ in range(nf)]; sf=sum(rawf)
        Fp = [r*target_top/sf for r in rawf]
        rawr = [F(random.randint(1,9)) for _ in range(nr)]; sr=sum(rawr)
        Rp = [r*target_below/sr for r in rawr]
        DF = D_integral(Fp); C = overlap_C(Fp, Rp)
        if DF < 2*C:
            fails += 1
            if worst is None or (2*C-DF)>worst[0]: worst=(2*C-DF,DF,C,Fp,Rp)
    print(f"  T_{n}: D_F < 2C in {fails}/{trials} fully-arbitrary cases.", end="")
    if worst: print(f" worst deficit {worst[0]} (D_F={worst[1]},C={worst[2]}, Fp={worst[4]}, Rp={worst[5]})")
    else: print(" (never violated)")

# (4) Probe: what is the max ratio C / D_F over tower-refinement configs?
print("\n(4) max C/D_F ratio (tower refinements) -- how tight is the factor 2?:")
for n in [3,4,5]:
    T=tower(n); top=T[0]; below=T[1:]
    best_ratio = F(0); best=None
    for trial in range(10000):
        ntop=random.randint(1,n); nbelow=random.randint(0,n-ntop)
        Fp=random_refine([top],ntop); Rp=random_refine(below,nbelow)
        DF=D_integral(Fp); C=overlap_C(Fp,Rp)
        if DF > 0:
            r = C/DF
            if r > best_ratio: best_ratio=r; best=(DF,C,Fp,Rp)
    print(f"  T_{n}: max C/D_F = {best_ratio} (= {float(best_ratio):.4f}), factor-2 slack = {2-best_ratio}", end="")
    print(f"\n    at D_F={best[0]}, C={best[1]}")
