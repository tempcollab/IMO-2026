import random, itertools
from functools import lru_cache

def u(k): return 1.0/(2**(k+1)-1)
def c(k): return 2**k/(2.0**(k+1)-1)

def reachable_set(pieces, budget):
    # returns SET of all totals reachable via legal op-sequences using AT MOST `budget` ops
    # (Xiang may stop early at any point -- "not using all ops" is legal)
    pieces = tuple(sorted(pieces, reverse=True))
    seen = set()
    def rec(p, b):
        p = tuple(sorted(p, reverse=True))
        key=(p,b)
        tot = round(sum(p),9)
        seen.add(tot)
        if b<=0 or len(p)==0:
            return
        m=len(p)
        # free-delete equal pair
        for i in range(m):
            for j in range(i+1,m):
                if abs(p[i]-p[j])<1e-9:
                    newp = p[:i]+p[i+1:j]+p[j+1:]
                    rec(newp, b)  # 0 cost
        # bisect
        for i in range(m):
            newp = p[:i]+p[i+1:]
            rec(newp, b-1)
        # pin j into i
        for i in range(m):
            for j in range(m):
                if i==j: continue
                if p[i] > p[j]+1e-9:
                    rem = p[i]-p[j]
                    newp = [p[x] for x in range(m) if x!=i and x!=j]+[rem]
                    rec(tuple(newp), b-1)
    rec(pieces, budget)
    return sorted(seen)

def mesh_near_zero(vals, frac=0.3, Sigma=1.0):
    # look at values in [0, frac*Sigma], compute max consecutive gap
    lo = [v for v in vals if v <= frac*Sigma]
    lo = sorted(set(lo))
    if len(lo)<2: return None, lo
    gaps = [lo[i+1]-lo[i] for i in range(len(lo)-1)]
    return max(gaps), lo

random.seed(1)
for k in [3,4]:
    uk = u(k); ck=c(k)
    print(f"=== k={k}  u_k={uk:.5f}  c(k)={ck:.5f} (Sigma=1 target: min <= {uk:.5f}) ===")
    worst_ratio = 0
    worst_info=None
    trials=0
    for trial in range(25):
        # region B instance: ell1 < 1/2, m=k+1 pieces summing to 1
        m=k+1
        while True:
            xs = sorted([random.random() for _ in range(m-1)])
            parts=[]
            prev=0
            for x in xs:
                parts.append(x-prev); prev=x
            parts.append(1-prev)
            parts.sort(reverse=True)
            if parts[0] < 0.5 - 1e-6 and parts[0]>1e-6:
                break
        vals = reachable_set(parts, k)
        gap, lo = mesh_near_zero(vals, frac=uk*2.5)
        trials+=1
        themin = min(vals)
        ratio = themin/uk
        if gap is not None:
            gap_ratio = gap/uk
            if gap_ratio > worst_ratio:
                worst_ratio = gap_ratio
                worst_info = (parts, gap, themin, ratio, lo[:8])
    print(f"  trials={trials}  worst mesh-gap/u_k = {worst_ratio:.3f}")
    if worst_info:
        parts,gap,themin,ratio,lo = worst_info
        print(f"    worst instance parts={[round(p,4) for p in parts]}")
        print(f"    mesh-gap={gap:.5f} (u_k={uk:.5f}), min-found={themin:.5f} (ratio to u_k={ratio:.3f})")
        print(f"    lowest reachable vals: {[round(v,5) for v in lo]}")
