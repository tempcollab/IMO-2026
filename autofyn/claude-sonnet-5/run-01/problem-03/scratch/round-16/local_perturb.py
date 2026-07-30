from fractions import Fraction as F
import sys
sys.path.insert(0,'/tmp/round-16')
exec(open('/tmp/round-16/verify_v2.py').read().split("# Witness check")[0])

base = [F(6),F(4),F(3),F(2)]
import itertools, random
random.seed(7)
worst = None
for _ in range(50000):
    eps = [F(random.randint(-50,50),1000) for _ in range(4)]
    vals = [base[i]+eps[i] for i in range(4)]
    if any(v<=0 for v in vals): continue
    vals_sorted = sorted(vals, reverse=True)
    p1,t1,t2,t3 = vals_sorted
    if not (p1<t1+t2+t3): continue
    Sigma=p1+t1+t2+t3
    target=c(3)*Sigma
    res=V4_case_C(p1,t1,t2,t3)
    m=min(res.values())
    margin=target-m
    if worst is None or margin<worst[0]:
        worst=(margin,vals_sorted)
print("worst local margin:", worst[0], float(worst[0]))
print(worst[1])
