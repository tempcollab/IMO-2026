import random, sys
sys.path.insert(0,'/tmp/round-6')
from rt_search import eval_f, u

random.seed(21)

def sample_regionB(k):
    m=k+1
    while True:
        xs = sorted([random.random() for _ in range(m-1)])
        parts=[]; prev=0
        for x in xs:
            parts.append(x-prev); prev=x
        parts.append(1-prev)
        parts.sort(reverse=True)
        if parts[0] < 0.5-1e-6:
            return parts

for k in [3,4]:
    n=400
    pts=[sample_regionB(k) for _ in range(n)]
    vals=[eval_f(p,k) for p in pts]
    viol=0; tot_pairs=0
    for i in range(0,n,2):
        if i+1>=n: continue
        p1,p2 = pts[i],pts[i+1]
        mid = [(a+b)/2 for a,b in zip(sorted(p1,reverse=True), sorted(p2,reverse=True))]
        # renormalize just in case (should already sum to 1)
        s=sum(mid); mid=[x/s for x in mid]
        if mid[0]>=0.5-1e-9: continue  # midpoint left region B, skip (not a valid concavity test point within region)
        fmid = eval_f(mid,k)
        favg = (vals[i]+vals[i+1])/2
        tot_pairs+=1
        if fmid < favg - 1e-9:  # concave would need fmid >= favg; violation = fmid<favg
            viol+=1
    print(f"k={k}: pairs tested (both in region B, midpoint in region B) = {tot_pairs}, concavity violations (f(mid)<avg) = {viol} ({100*viol/max(tot_pairs,1):.1f}%)")
