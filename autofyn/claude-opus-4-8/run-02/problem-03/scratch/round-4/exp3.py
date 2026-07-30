from fractions import Fraction as Fr
import random
exec(open('exp1.py').read().split('# random')[0])  # get eval_f, optf, u, c

# empirical worst residual as function of beta=l1/Sigma for k=3, and also as function of (l1,l2)
random.seed(5)
k=3; uk=u(k); ck=c(k)
import collections
buckets=collections.defaultdict(lambda:Fr(0))
records=[]
for _ in range(6000):
    cuts=sorted(Fr(random.randint(1,999),1000) for _ in range(k))
    pts=[Fr(0)]+cuts+[Fr(1)]
    pieces=sorted([pts[i+1]-pts[i] for i in range(k+1)],reverse=True)
    if any(p==0 for p in pieces):continue
    l1,l2=pieces[0],pieces[1]
    if not(l1<ck and 2*l2<ck):continue
    r=optf(pieces,k)
    b=int(float(l1)*20)/20.0
    buckets[b]=max(buckets[b],r/uk)
    records.append((float(l1),float(l2),float(r/uk),pieces))
print("k=3 worst residual/u_k by beta bucket (l1):")
for b in sorted(buckets):
    print(f"  l1 in [{b:.2f},{b+0.05:.2f}): maxratio={float(buckets[b]):.3f}")
# find the worst records overall
records.sort(key=lambda t:-t[2])
print("worst 6 (l1,l2,ratio):")
for l1,l2,ra,pc in records[:6]:
    print(f"  l1={l1:.3f} l2={l2:.3f} ratio={ra:.3f}  pieces={[float(x) for x in pc]}")
