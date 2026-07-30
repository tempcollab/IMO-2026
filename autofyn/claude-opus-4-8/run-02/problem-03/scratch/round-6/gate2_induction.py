import random
import sys
sys.path.insert(0,'/tmp/round-6')
from rt_search import eval_f, u

random.seed(3)
print("Testing: bisect ell1 (1 op), apply optimal RT(k-1) to remainder (k-1 ops) -- does this beat u_k*Sigma for region B (ell1<Sigma/2)?")
for k in [2,3,4]:
    uk=u(k)
    m=k+1
    worst_ratio=0; worst=None
    n_fail=0
    trials=400
    for t in range(trials):
        xs = sorted([random.random() for _ in range(m-1)])
        parts=[]; prev=0
        for x in xs:
            parts.append(x-prev); prev=x
        parts.append(1-prev)
        parts.sort(reverse=True)
        if parts[0] >= 0.5-1e-9: continue
        remainder = parts[1:]  # bisect the largest away
        g = eval_f(remainder, k-1)  # optimal RT(k-1) on remainder
        ratio = g/uk
        if ratio > worst_ratio:
            worst_ratio = ratio; worst=(parts, g)
        if g > uk + 1e-9:
            n_fail += 1
    print(f"k={k}: trials(region B)={trials-sum(1 for _ in [0])} fails(g>u_k)={n_fail} worst g/u_k={worst_ratio:.4f}  worst_parts={[round(p,4) for p in worst[0]] if worst else None}")
