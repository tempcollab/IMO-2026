from fractions import Fraction as F

def L2(u,v):
    M,m=(u,v) if u>=v else (v,u)
    return M if M<=2*m else M/2+m

def V3(x,y,z):
    trip=sorted([x,y,z],reverse=True)
    x,y,z=trip
    sigma=x+y+z
    if x>=F(4,7)*sigma:
        return x/2+L2(y,z)
    elif sigma/2<=x:
        return x
    else:
        return min(x+z/2, y+L2(x-y,z))

def strategies(p1,t1,t2,t3):
    A = t1+V3(*sorted([t2,t3,p1-t1],reverse=True))
    B = p1/2+V3(t1,t2,t3)
    C12 = t2+V3(*sorted([p1,t3,t1-t2],reverse=True))
    C13 = t3+V3(*sorted([p1,t2,t1-t3],reverse=True))
    C23 = t3+V3(*sorted([p1,t1,t2-t3],reverse=True))
    return dict(A=A,B=B,C12=C12,C13=C13,C23=C23)

# fixed tail (4,3,2), vary p1 over Case-C-valid range: p1>=t1=4, p1<Sigma/2=(p1+9)/2 => p1<9
for num in range(40,90,2):
    p1 = F(num,10)
    t1,t2,t3=F(4),F(3),F(2)
    if not (p1>=t1): continue
    Sigma=p1+t1+t2+t3
    if not (p1<Sigma/2): continue
    vals=strategies(p1,t1,t2,t3)
    tgt=F(8,15)*Sigma
    best=min(vals.values())
    winner=min(vals,key=lambda k:vals[k])
    print(f"p1={float(p1):.2f} Sigma={float(Sigma):.2f} t1/Sigma={float(t1/Sigma):.4f} best={float(best):.4f} tgt={float(tgt):.4f} margin={float(tgt-best):.5f} winner={winner}")
