from fractions import Fraction as F
import itertools

def claim_value(pieces):
    s=sorted(pieces, reverse=True)
    return sum(s[i] for i in range(0,len(s),2))
def Dval(pieces):
    s=sorted(pieces,reverse=True)
    return sum(s[i]-s[i+1] for i in range(0,len(s)-1,2)) + (s[-1] if len(s)%2==1 else 0)

# verify gaps+leftover = D identity
import random
random.seed(0)
for _ in range(5):
    pp=[random.randint(1,9) for _ in range(random.randint(3,7))]
    s=sorted(pp,reverse=True)
    gaps=sum(s[i]-s[i+1] for i in range(0,len(s)-1,2))
    left = s[-1] if len(s)%2==1 else 0
    assert gaps+left == 2*claim_value(pp)-sum(pp)
print("identity D = sum_{k}(p_{2k-1}-p_{2k}) + p_m (m odd) verified.")

# n=2 full minimax with grid multiple of 7 (so tower on-grid)
def liu_configs(T,n,gridpts):
    cfgs=set()
    for k in range(0,n+1):
        for cuts in itertools.combinations(gridpts,k):
            pts=sorted(cuts); parts=[]; prev=0
            for c in pts: parts.append(F(c)-F(prev)); prev=c
            parts.append(F(1)-F(prev))
            parts=[p*T for p in parts]
            if all(p>0 for p in parts): cfgs.add(tuple(sorted(parts)))
    return cfgs

def xiang_best(liu_pieces,n,gridpts):
    best=[None]
    def opts(size,mm):
        o=[([size],0)]
        for k in range(1,mm+1):
            for cuts in itertools.combinations(gridpts,k):
                pts=sorted(cuts); parts=[]; prev=0
                for c in pts: parts.append(size*(F(c)-F(prev))); prev=c
                parts.append(size*(F(1)-F(prev)))
                if all(p>0 for p in parts): o.append((parts,k))
        return o
    np=len(liu_pieces)
    def dfs(idx,ml,acc):
        if idx==np:
            v=claim_value(acc)
            if best[0] is None or v<best[0]: best[0]=v
            return
        for parts,m in opts(liu_pieces[idx],min(ml,n)):
            if m<=ml: dfs(idx+1,ml-m,acc+parts)
    dfs(0,n,[])
    return best[0]

T=F(7); n=2
# grid = multiples of 1/7 (so 1/7,2/7,...,6/7 on grid) plus finer for xiang halving (need 1/14 etc)
# Use grid pts at i/56 for i=1..55 (so 1/7=8/56, 2/7=16/56, 1/14=4/56 on grid)
gp=[F(i,56) for i in range(1,56)]
cfgs=liu_configs(T,n,gp)
print("num Liu configs (grid56):",len(cfgs))
bestv=None; bestcfg=None; cnt=0
vals=[]
for cfg in cfgs:
    v=xiang_best(list(cfg),n,gp)
    vals.append((v,cfg))
    if bestv is None or v>bestv: bestv=v; bestcfg=cfg
print("max-min:", bestv, "frac:", bestv/T, "target 4/7=",F(4,7))
print("best cfg:", bestcfg)
vals.sort(key=lambda x:-x[0])
print("top configs by max-min:")
for v,c in vals[:5]: print("  ",c,"->",v,"frac",v/T)
print("tower (1,2,4) present?", (F(1),F(2),F(4)) in cfgs)
# tower's xiang-best:
if (F(1),F(2),F(4)) in cfgs:
    print("tower xiang-best:", xiang_best([F(1),F(2),F(4)],n,gp), "frac", xiang_best([F(1),F(2),F(4)],n,gp)/T)
