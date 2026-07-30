from fractions import Fraction as F
import numpy as np
from explore_paritypairgen import geom_config, c_of, optimize_allocation

n = 4
p = geom_config(n)
p_floats = [float(x) for x in p]
print("p_i:", [str(x) for x in p], [float(x) for x in p])
print("c(n)=", c_of(n), float(c_of(n)))

# tail anchors t_i = p_{i+1}, i=1..n (n=4 tail has p2,p3,p4,p5 -> that's only n=4 tail values, matches t_1..t_n)
tail_anchors = [float(p[i]) for i in range(1, n+1)]
print("tail anchors (t_1..t_n):", tail_anchors)

# k=2: 2 marks on p1 (3 parts), remaining 2 marks distributed as 1 mark each on two DIFFERENT tail pieces
for alloc in [(2,1,1,0,0), (2,1,0,1,0), (2,1,0,0,1), (2,0,1,1,0), (2,0,1,0,1), (2,0,0,1,1)]:
    val, vs = optimize_allocation(p_floats, alloc, restarts=20, seed=1)
    print("\nalloc=", alloc, "oddsum=", val, "c(n)=", float(c_of(n)))
    for v in vs:
        # check closeness to any anchor or to zero
        closest = min(tail_anchors + [0.0], key=lambda a: abs(a-v))
        print(f"   {v:.6f}  (closest anchor {closest:.6f}, diff {v-closest:+.2e})")
