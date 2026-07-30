import random
from gate1_mesh import reachable_set, u, c
import sys
sys.path.insert(0,'/tmp/round-6')

random.seed(42)
for k in [3,4]:
    uk=u(k)
    worst_min_ratio = 0
    worst_gap_below_uk = 0
    n_violate=0
    trials=200
    for trial in range(trials):
        m=k+1
        while True:
            xs = sorted([random.random() for _ in range(m-1)])
            parts=[]; prev=0
            for x in xs:
                parts.append(x-prev); prev=x
            parts.append(1-prev)
            parts.sort(reverse=True)
            if parts[0] < 0.5-1e-6 and parts[0]>1e-6:
                break
        vals = reachable_set(parts, k)
        themin = min(vals)
        if themin > uk + 1e-9:
            n_violate+=1
            print("VIOLATION", parts, themin, uk)
        ratio = themin/uk
        if ratio > worst_min_ratio:
            worst_min_ratio = ratio
        # gap structure strictly within [0,uk]
        below = sorted(v for v in vals if v <= uk+1e-9)
        if len(below)>=2:
            gaps = [below[i+1]-below[i] for i in range(len(below)-1)]
            mg = max(gaps)
            if mg > worst_gap_below_uk:
                worst_gap_below_uk = mg
    print(f"k={k}: trials={trials} violations(min>u_k)={n_violate} worst min/u_k ratio={worst_min_ratio:.4f} worst mesh-gap WITHIN [0,u_k]={worst_gap_below_uk:.5f} (u_k={uk:.5f})")
