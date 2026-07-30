import sys
sys.path.insert(0,'/tmp/round-2')
from brute import xiang_min_D
liu=[0.6025810891311573, 0.3013084326946351, 0.09611047817420774]
val,info = xiang_min_D(liu,2,restarts=60,seed=42)
print(val, info[0])
print(sorted(info[1],reverse=True) if info[1] else info[1])
