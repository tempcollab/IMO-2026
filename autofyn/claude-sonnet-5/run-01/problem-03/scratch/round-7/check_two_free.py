from fractions import Fraction as F
import numpy as np
from explore_paritypairgen import geom_config, c_of, optimize_allocation

for n in [3,4,5]:
    p = geom_config(n)
    p_floats = [float(x) for x in p]
    tail_anchors = [float(p[i]) for i in range(1, n+1)]
    print(f"\n=== n={n}  c(n)={float(c_of(n)):.6f}  tail anchors={['%.5f'%a for a in tail_anchors]} ===")
    # k=1 (p1 split into 2 parts) + 1 mark on p2 (split into 2 parts), rest unsplit -- uses 2 of n marks
    alloc = [0]*(n+1); alloc[0]=1; alloc[1]=1
    val, vs = optimize_allocation(p_floats, tuple(alloc), restarts=25, seed=2)
    print("alloc(k=1,tailmark on p2)=",alloc," oddsum=",val," c(n)=",float(c_of(n)))
    for v in vs:
        closest = min(tail_anchors + [0.0, p_floats[0]], key=lambda a: abs(a-v))
        print(f"   {v:.6f}  (closest {closest:.6f}, diff {v-closest:+.2e})")
