import sys, numpy as np
sys.path.insert(0,'/tmp/round-2')
from brute import xiang_min_D
rng=np.random.default_rng(7)
best=-1;bestliu=None
for i in range(40):
    w = rng.dirichlet([1,1,1])
    liu = sorted(w.tolist(), reverse=True)
    val,info = xiang_min_D(liu,2,restarts=12,seed=i)
    if val>best:
        best=val; bestliu=liu; bestinfo=info
    if i%10==0: print(i, liu, val)
print("MAX found:", best, "at", bestliu, "u2=1/7=",1/7)
