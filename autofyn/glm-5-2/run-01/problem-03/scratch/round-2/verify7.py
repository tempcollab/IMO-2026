from fractions import Fraction as F

def alt_sum(m):
    s=F(0)
    for i,x in enumerate(sorted(m,reverse=True)):
        s += (x if i%2==0 else -x)
    return s
TARGET=F(1,7)
def xiang_min_D(liu_cfg, nmarks, g=20):
    best=None
    pieces=list(liu_cfg)
    def splits_of(pl):
        out=[]
        for i in range(1,g):
            q=pl*F(i,g)
            if q>pl/2: break
            out.append((pl-q,q))
        return out
    D0=alt_sum(pieces)
    best=D0
    if nmarks>=1:
        for idx in range(len(pieces)):
            for (p,q) in splits_of(pieces[idx]):
                np_=pieces[:idx]+[p,q]+pieces[idx+1:]
                D1=alt_sum(np_)
                if D1<best: best=D1
                if nmarks>=2:
                    for idx2 in range(len(np_)):
                        for (p2,q2) in splits_of(np_[idx2]):
                            np2=np_[:idx2]+[p2,q2]+np_[idx2+1:]
                            D2=alt_sum(np2)
                            if D2<best: best=D2
    return best

# find max over Liu configs of min_Xiang D
G=28
maxD=None; maxcfg=None
near_target=[]
for m in [1,2,3]:
    if m==1:
        cfgs=[[F(1)]]
    elif m==2:
        cfgs=[[F(i,G),F(1)-F(i,G)] for i in range(G//2,G+1) if F(1)-F(i,G)<=F(i,G)]
    else:
        cfgs=[]
        for i in range(0,G+1):
            for j in range(0,i+1):
                a1=F(i,G);a2=F(j,G);a3=F(1)-a1-a2
                if a3<0 or a3>a2 or a2>a1: continue
                cfgs.append([a1,a2,a3])
    for cfg in cfgs:
        D=xiang_min_D(cfg,2)
        if maxD is None or D>maxD:
            maxD=D; maxcfg=cfg
        if D>=TARGET:
            near_target.append((cfg,D))
print(f"max over Liu configs of min_Xiang D = {maxD} at {maxcfg}")
print(f"configs achieving D>=1/7: {len(near_target)}")
for c,d in near_target[:20]:
    print(f"  {c} -> D={d}")
