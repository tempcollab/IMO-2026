from fractions import Fraction as F

A1 = [F(4265,10000),F(2536,10000),F(1747,10000),F(1014,10000),F(438,10000)]
A2 = [F(3415,10000),F(3023,10000),F(1664,10000),F(1404,10000),F(494,10000)]

def oddrank(vals):
    s = sorted(vals, reverse=True)
    return sum(s[0::2])

c4 = F(16,31)

# Witness 1 construction: p1 split arbitrarily into (x,p1-x) [any x in valid flat range, e.g. x=p1/2]
# p3 untouched (mark "wasted")
# p4 -> (p5, (p4-p5)/2, (p4-p5)/2)
p1,p2,p3,p4,p5 = A1
x = p1/2  # pick midpoint, should be in the flat zone; verify by checking sort order unaffected
frag_p4 = (p4-p5)/2
B1 = [x, p1-x, p2, p3, frag_p4, frag_p4, p5, p5]
B1s = sorted(B1, reverse=True)
print("W1 sorted:", [str(v) for v in B1s])
val1 = oddrank(B1)
print("W1 oddrank exact:", val1, float(val1), "c4=",float(c4), "beats c4:", val1 < c4)
print("W1 formula p2+p3+(p4+p5)/2 =", p2+p3+(p4+p5)/2, "match:", p2+p3+(p4+p5)/2==val1)

# Witness 2 construction: p1 -> (p5,(p1-p5)/2,(p1-p5)/2); p2 -> (p3, p2-p3); p3 untouched original; p4 untouched; p5 untouched
p1,p2,p3,p4,p5 = A2
frag_p1 = (p1-p5)/2
B2 = [p5, frag_p1, frag_p1, p3, p2-p3, p3, p4, p5]
B2s = sorted(B2, reverse=True)
print("W2 sorted:", [str(v) for v in B2s])
val2 = oddrank(B2)
print("W2 oddrank exact:", val2, float(val2), "beats c4:", val2 < c4)
print("W2 formula p1/2+p3+p4+p5/2 =", p1/2+p3+p4+p5/2, "match:", p1/2+p3+p4+p5/2==val2)

# check mark budgets: W1: 1 mark p1(split 2way)=1, p3 split (0 way, mark wasted, still counts as spent w/ 0-length piece, or just don't spend it -> 0 marks), p4 3way=2 marks. total spent (not counting wasted) = 1+2=3 <=4. 
# W2: p1 3way=2 marks, p2 2way=1 mark, total=3<=4.
print("Budgets: W1 uses 3 of 4 marks (1 wasted), W2 uses 3 of 4 marks (1 wasted, on p4)")

print("---retry W1 with x in valid flat window---")
p1,p2,p3,p4,p5 = A1
x = F(4075,10000)  # in (p3/p1, 1-p3/p1)... check window (0.40539,0.40961)
frag_p4 = (p4-p5)/2
B1b = [x*p1, (1-x)*p1, p2, p3, frag_p4, frag_p4, p5, p5]
B1bs = sorted(B1b, reverse=True)
print("W1(b) sorted:", [f"{float(v):.6f}" for v in B1bs])
val1b = oddrank(B1b)
print("W1(b) oddrank exact:", val1b, float(val1b), "beats c4:", val1b < c4)
print("formula check p2+p3+(p4+p5)/2 =", p2+p3+(p4+p5)/2)
