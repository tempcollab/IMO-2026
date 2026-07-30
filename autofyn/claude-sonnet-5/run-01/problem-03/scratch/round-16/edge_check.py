from fractions import Fraction as F
exec(open('/tmp/round-16/verify_v2.py').read().split("# Witness check")[0])

random.seed(99)
worst=None
viol=0
tests=0
# edge cases: t3 -> 0, p1 -> Sigma/2 boundary, ties p1=t1, t1=t2, t2=t3
cases = []
for _ in range(20000):
    tests+=1
    t3 = F(random.randint(0,3),1000)  # near 0 allowed since >0 required strictly but test small
    if t3<=0: t3=F(1,10000)
    t2 = t3 + F(random.randint(0,5000),1000)
    t1 = t2 + F(random.randint(0,5000),1000)
    # p1 near Sigma(tail) boundary from below
    tailsum = t1+t2+t3
    p1 = tailsum - F(random.randint(1,1000000),1000000)  # slightly less than tailsum
    if p1 < t1:
        continue  # need p1>=t1 sorted descending assumption; if not, skip (not a valid ordering)
    if p1<=0: continue
    Sigma=p1+t1+t2+t3
    if not (p1 < Sigma/2): continue
    target=c(3)*Sigma
    res=V4_case_C(p1,t1,t2,t3)
    m=min(res.values())
    margin=target-m
    if margin<0:
        viol+=1
        print("VIOLATION",p1,t1,t2,t3,m,target)
    if worst is None or margin<worst[0]:
        worst=(margin,(p1,t1,t2,t3))
print("tests run near boundary:",tests,"violations:",viol)
print("worst margin near boundary:", worst[0], float(worst[0]))
print(worst[1])
