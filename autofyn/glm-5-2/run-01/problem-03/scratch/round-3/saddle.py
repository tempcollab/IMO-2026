from fractions import Fraction as F
import itertools

def claim_value(pieces):
    s=sorted(pieces, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))

def total(p): return sum(p)

# ---- Xiang best response (min claim value) over grid refinements, with marks<=n ----
def xiang_best(liu_pieces, n, grid):
    gridpts=[F(i,grid) for i in range(1,grid)]
    best=[None]
    def piece_options(size, maxmarks):
        opts=[([size],0)]
        for k in range(1,maxmarks+1):
            for cuts in itertools.combinations(gridpts,k):
                pts=sorted(cuts); parts=[]; prev=0; ok=True
                for c in pts:
                    parts.append(size*(c-prev)); prev=c
                parts.append(size*(1-prev))
                if all(p>0 for p in parts): opts.append((parts,k))
        return opts
    npieces=len(liu_pieces)
    def dfs(idx, marks_left, acc):
        if idx==npieces:
            val=claim_value(acc)
            if best[0] is None or val<best[0]: best[0]=val
            return
        for parts,m in piece_options(liu_pieces[idx], min(marks_left,n)):
            if m<=marks_left: dfs(idx+1,marks_left-m,acc+parts)
    dfs(0,n,[])
    return best[0]

# ---- Liu configs: <=n marks on stick of length T => <=n+1 pieces. Enumerate partitions of T into <=n+1 positive parts on a grid ----
def liu_configs(T, n, grid):
    # piece sizes are positive, sum T, count <= n+1. Generate compositions via cut points.
    # Use grid cuts: choose k<=n cut points from {1..grid-1}/grid * T
    gridpts=[F(i,grid) for i in range(1,grid)]
    configs=set()
    for k in range(0,n+1):
        for cuts in itertools.combinations(gridpts,k):
            pts=sorted(cuts); parts=[]; prev=0
            for c in pts:
                parts.append(F(c)-F(prev)); prev=c
            parts.append(F(1)-F(prev))
            parts=[p*T for p in parts]
            if all(p>0 for p in parts):
                configs.add(tuple(sorted(parts)))
    return configs

# ====== Saddle test for n=2 ======
T=F(7)  # unnormalized tower total
n=2
grid=30
liu = liu_configs(T, n, grid)
print("num Liu configs (grid30):", len(liu))
# for each Liu config, compute Xiang best (min claim value). Then c(n)*T = max over Liu of that min.
best_l=None; best_val=None
results=[]
for cfg in liu:
    v=xiang_best(list(cfg), n, grid)
    results.append((v,cfg))
    if best_val is None or v>best_val:
        best_val=v; best_l=cfg
print("max-min Liu config:", best_l, "value:", best_val, "frac:", best_val/T, "target 4/7=", F(4,7))
# how many configs achieve the max?
maxcnt=sum(1 for v,_ in results if v==best_val)
print("configs achieving max-min:", maxcnt)
# print a few top configs
results.sort(key=lambda x:-x[0])
for v,cfg in results[:6]:
    print("  ", cfg, "->", v, "frac", v/T)
