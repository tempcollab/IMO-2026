import sys
sys.path.insert(0,'/tmp/round-6')
from rt_search import eval_f, u

cases = [
 (2, [0.4059,0.395,0.1991]),
 (3, [0.4298,0.3261,0.1614,0.0827]),
 (4, [0.3569,0.3504,0.18,0.0798,0.0329]),
]
for k,parts in cases:
    uk=u(k)
    g_exclude = eval_f(parts[1:], k-1)
    g_true = eval_f(parts, k)
    print(f"k={k} parts={parts}")
    print(f"  u_k={uk:.5f}  exclude-ell1-then-recurse={g_exclude:.5f} (ratio {g_exclude/uk:.3f})  TRUE optimal={g_true:.5f} (ratio {g_true/uk:.3f})")
