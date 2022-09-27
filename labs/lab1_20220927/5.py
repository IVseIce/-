import random
import math

S1=1
S2=1
N=100000000
C1=0
C2=0
for i in range(N):
    x=random.uniform(0.0,1.0)
    y=random.uniform(0.0,1.0)
    if y <=x*x:
        C1 += 1
for j in range(N):
    x=random.uniform(0.0,1.0)
    y=random.uniform(0.0,1.0)
    if y <=x*x*x:
        C2 += 1
I = C1 / N *S1 + C2 / N *S2
print(I)