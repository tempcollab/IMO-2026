import sys, numpy as np
sys.path.insert(0,'/tmp/round-2')
from brute import xiang_min_D
u3=1/15
liu=[8/15,4/15,2/15,1/15]
val,info = xiang_min_D(liu,3,restarts=6)
print("dyadic n=3:", val, "target", u3, info[0])
val,info = xiang_min_D(liu,3,restarts=20,seed=5)
print(val, info[0])
print(sorted(info[1],reverse=True))
print([x*15 for x in sorted(info[1],reverse=True)])
