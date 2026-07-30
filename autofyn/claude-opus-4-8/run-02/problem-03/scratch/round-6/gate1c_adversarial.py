import random
import sys
sys.path.insert(0,'/tmp/round-6')
from gate1_mesh import reachable_set, u

random.seed(7)
for k in [3,4,5]:
    uk=u(k)
    worst_ratio=0; worst_parts=None
    m=k+1
    trials=3000
    for trial in range(trials):
        # bias sampling toward boundary ell1 -> 1/2, and toward skewed/near-degenerate configs
        style = trial % 4
        if style==0:
            xs = sorted([random.random() for _ in range(m-1)])
        elif style==1:
            # near boundary: ell1 close to 0.5
            eps = random.uniform(0,0.05)
            ell1 = 0.5-eps
            rest = sorted([random.random()*(1-ell1) for _ in range(m-2)])
            xs=None
        elif style==2:
            # skewed dirichlet-like via exponential weights
            w = sorted([random.expovariate(1.0)**random.uniform(0.3,3) for _ in range(m)], reverse=True)
            s=sum(w); parts=[x/s for x in w]
            if parts[0]>=0.5: continue
            themin = min(reachable_set(parts,k))
            ratio = themin/uk
            if ratio>worst_ratio: worst_ratio=ratio; worst_parts=parts
            continue
        else:
            xs = sorted([random.random() for _ in range(m-1)])
        if style==1:
            parts = [ell1]+rest
            prev=0; pr=[]
            rest2=sorted(rest)
            cum=[]
            tot=sum(rest)
            # normalize rest to sum to 1-ell1
            rest_n=[r*(1-ell1)/tot if tot>0 else (1-ell1)/len(rest) for r in rest]
            parts=[ell1]+rest_n
        else:
            parts=[]; prev=0
            for x in xs:
                parts.append(x-prev); prev=x
            parts.append(1-prev)
        parts.sort(reverse=True)
        if parts[0]>=0.5-1e-9 or parts[0]<=1e-9: continue
        themin=min(reachable_set(parts,k))
        ratio=themin/uk
        if ratio>worst_ratio:
            worst_ratio=ratio; worst_parts=parts
    print(f"k={k}: worst min/u_k ratio over {trials} adversarial trials = {worst_ratio:.4f}  parts={[round(p,4) for p in worst_parts]}")
