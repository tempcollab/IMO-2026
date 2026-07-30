import random
exec(open('/tmp/round-5/probe_runcase.py').read().split("rng = random.Random(1)")[0])

rng=random.Random(11)
n=6
data=[]
for trial in range(60000):
    a = rng.randint(1, n-1)
    b = rng.randint(0, n-a)
    Y = gen_Y(n, a, rng)
    Z, anchors, cutcounts = gen_Z(n, b, rng)
    maxc, deficit, surplus, Dtilde = compute_run_stats(Y,Z)
    num_uncut = sum(1 for c in cutcounts if c==0)
    data.append((maxc,deficit,surplus,Dtilde,num_uncut,a,b,len(anchors)))

bad=[r for r in data if r[0]>=2]
print("n=",n,"trials",len(data),"maxc>=2:",len(bad))
mind = min(r[3] for r in bad)
print("min Dtilde among maxc>=2:", mind)
# relationship deficit vs surplus and num_uncut
worst5 = sorted(bad, key=lambda r:r[3])[:10]
for r in worst5:
    print("maxc=%d deficit=%.3f surplus=%.3f D=%.4f uncut=%d a=%d b=%d"%(r[0],r[1],r[2],r[3],r[4],r[5],r[6]))

# check: does deficit <= 2 * num_uncut * something?  try deficit <= surplus always (should, since D>=1)
viol = [r for r in bad if r[1] > r[2] + 1e-9 and r[3] < 1-1e-9]
print("true violations of D>=1:", len(viol))
