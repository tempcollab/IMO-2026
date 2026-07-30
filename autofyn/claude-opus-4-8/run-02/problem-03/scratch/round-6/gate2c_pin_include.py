import random, sys
sys.path.insert(0,'/tmp/round-6')
from rt_search import eval_f, u

random.seed(9)
print("Testing: pin ell1,ell2 into |ell1-ell2| (1 op), apply optimal RT(k-1) to result (k pieces total incl merged, budget k-1)")
for k in [2,3,4]:
    uk=u(k)
    m=k+1
    worst_ratio=0; worst=None
    n_fail=0
    trials=300
    for t in range(trials):
        xs = sorted([random.random() for _ in range(m-1)])
        parts=[]; prev=0
        for x in xs:
            parts.append(x-prev); prev=x
        parts.append(1-prev)
        parts.sort(reverse=True)
        if parts[0] >= 0.5-1e-9: continue
        merged = abs(parts[0]-parts[1])
        rest = [merged]+parts[2:]
        g = eval_f(rest, k-1)
        ratio = g/uk
        if ratio > worst_ratio:
            worst_ratio = ratio; worst=(parts, g)
        if g > uk+1e-9: n_fail+=1
    print(f"k={k}: fails(g>u_k)={n_fail}/{trials}  worst g/u_k={worst_ratio:.4f}  worst_parts={[round(p,4) for p in worst[0]] if worst else None}")
