from fractions import Fraction as F
# Check majorization-upper regime C1 inequality chain.
# Claim in proof: a_3 <= (1-a_1)/3 < (3/7)/3 = 1/7. But regime C has a_1 < 4/7 => 1-a_1 > 3/7 => (1-a_1)/3 > 1/7. BUG.
# Correct bound: a_3 <= a_2/2 <= a_1/4 (since a_1>=2a_2 and a_2>=2a_3) and a_1<4/7 => a_1/4 < 1/7. So a_3 < 1/7. CONCLUSION HOLDS via a_1/4.
# Stress-test: pick regime-C1 configs and confirm a_3 < 1/7 AND a_3 <= (1-a_1)/3 (true) but (1-a_1)/3 > 1/7 (so that chain fails to give <1/7).
import random
random.seed(0)
bad_chain=0; conclusion_holds=0; tested=0
for _ in range(200000):
    a1=F(random.randint(28,39),70)  # < 4/7 = 40/70, >= 28/70=0.4
    if a1>=F(4,7): continue
    # a1 >= 2 a2 and a2 >= 2 a3, sum=1
    a2max = a1/2
    a2 = F(random.randint(1,70),70)
    if a2>a2max or a2<=0: continue
    a3 = 1-a1-a2
    if a3<=0 or a3>a2: continue
    if not (a1>=2*a2 and a2>=2*a3): continue  # regime C1
    tested+=1
    bound_loose = (1-a1)/3   # the buggy chain's bound
    bound_tight = a1/4        # the correct bound
    if not (a3 <= bound_tight < F(1,7)):
        conclusion_holds-=1
    if bound_loose > F(1,7):  # the buggy chain overshoots
        bad_chain+=1
print(f"tested={tested}, configs where (1-a_1)/3 > 1/7 (buggy chain fails to give <1/7): {bad_chain}, conclusion (a_3<a_1/4<1/7) holds in all: {conclusion_holds==0}")
