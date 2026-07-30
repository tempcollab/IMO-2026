import sys
sys.path.insert(0,'/tmp/round-2')
from brute import xiang_min_D
liu=[0.4192355488287052, 0.3879859592368884, 0.19277849193440652]
val,info=xiang_min_D(liu,2,restarts=20,seed=3)
print(val, info[0], sorted(info[1],reverse=True) if info[1] else None)
