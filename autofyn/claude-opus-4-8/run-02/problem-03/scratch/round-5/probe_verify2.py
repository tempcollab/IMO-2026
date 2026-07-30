import random

def altsum(vals):
    s=sorted(vals, reverse=True)
    tot=0; sign=1
    for v in s:
        tot+=sign*v; sign=-sign
    return tot

def maxc_of(Y,Z):
    merged = sorted([(w,1) for w in Y]+[(w,-1) for w in Z], key=lambda x:-x[0])
    c=0; mx=0
    for w,s in merged:
        c+=s; mx=max(mx,c)
    return mx

rng=random.Random(3)
Y=[4.0,4.0]
cnt_tight=0
cnt_maxc2=0
examples=[]
for trial in range(20000):
    # random split of 4 into 3 positive parts
    c1=rng.uniform(0,4); c2=rng.uniform(0,4)
    lo,hi=sorted([c1,c2])
    z=[lo, hi-lo, 4-hi]
    Z=[1.0,2.0]+z
    D=altsum(Y+Z)
    mc=maxc_of(Y,Z)
    if abs(D-1.0)<1e-9:
        cnt_tight+=1
        if mc>=2: cnt_maxc2+=1
        if len(examples)<5: examples.append((z,D,mc))
print("tight count", cnt_tight, "of which maxc>=2:", cnt_maxc2)
for e in examples: print(e)

# Now test general random z (not summing to exactly 4, i.e. general random D across many trials), check: is D ALWAYS exactly 1 for this family (Y=(4,4),Z=(1,2,z1,z2,z3) with sum z=4)? 
diffs=[]
for trial in range(2000):
    c1=rng.uniform(0,4); c2=rng.uniform(0,4)
    lo,hi=sorted([c1,c2])
    z=[lo, hi-lo, 4-hi]
    Z=[1.0,2.0]+z
    D=altsum(Y+Z)
    diffs.append(D-1.0)
print("max abs diff from 1:", max(abs(d) for d in diffs))
