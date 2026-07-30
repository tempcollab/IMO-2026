from fractions import Fraction as F
import random

def L2(u,v):
    M,m = (u,v) if u>=v else (v,u)
    if M <= 2*m:
        return M
    else:
        return M/2+m

def V3(x,y,z):
    # sorted descending x>=y>=z required
    assert x>=y>=z
    s = x+y+z
    if x >= F(4,7)*s:
        return x/2 + L2(y,z)
    elif x >= s/2:
        return x
    else:
        return min(x+z/2, y+L2(x-y,z))

def c(k):
    return F(2**k, 2**(k+1)-1)

def V4(A):
    p1,t1,t2,t3 = A
    vals=[]
    if p1>=t1:
        r = p1-t1
        trip = sorted([t2,t3,r], reverse=True)
        vals.append(t1 + V3(*trip))
    # StratB
    trip = sorted([t1,t2,t3], reverse=True)
    vals.append(p1/2 + V3(*trip))
    # StratC_12: tie t1,t2 (r=t1-t2), recurse on (p1,t3,r)
    r12=t1-t2
    if r12>=0:
        trip=sorted([p1,t3,r12],reverse=True)
        vals.append(t2 + V3(*trip))
    r13=t1-t3
    if r13>=0:
        trip=sorted([p1,t2,r13],reverse=True)
        vals.append(t3 + V3(*trip))
    r23=t2-t3
    if r23>=0:
        trip=sorted([p1,t1,r23],reverse=True)
        vals.append(t3 + V3(*trip))
    return min(vals)

if __name__=="__main__":
    A=[F(6),F(4),F(3),F(2)]
    S=sum(A); print('witness1', V4(A), c(3)*S)
    A=[F(1859),F(931),F(619),F(611)]
    S=sum(A); print('witness2', V4(A), c(3)*S)
    A=[F(992),F(670),F(325),F(158)]
    S=sum(A); print('prev-bug-witness', V4(A), c(3)*S)

    random.seed(1)
    worst=None
    for _ in range(200000):
        vals = sorted([random.randint(1,2000) for _ in range(4)], reverse=True)
        A=[F(v) for v in vals]
        S=sum(A)
        if A[0]>=S/2: continue
        val=V4(A)
        target=c(3)*S
        margin=target-val
        ratio=margin/S
        if worst is None or ratio<worst[0]:
            worst=(ratio,A,val,target)
    print('worst', worst)
