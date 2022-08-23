#A
'''import sys
import math
N,M,a,K=map(int, sys.stdin.readline().split())
print(min(N-1,a-K)+1, math.ceil((a-K)/M)+1)'''


#B
'''import sys
N=int(sys.stdin.readline())
a=[]
answer=0
for _ in range(N):
    aa,bb=map(int, sys.stdin.readline().split())
    a.append(aa)
    answer+=bb
a.sort()
for i in range(1,N+1):
    answer+=a[i-1]*i

print(answer)'''

import sys
N=int(sys.stdin.readline())
alpha=list(sys.stdin.readline().strip())
D={}
K={}
S={}
H={}
for i in range(N):
    if alpha[i]=='D':D[i]=0
    elif alpha[i]=='K':K[i]=0
    elif alpha[i]=='S':S[i]=0
    elif alpha[i]=='H':H[i]=1
for ind in S.keys():
    for ind2 in H.keys():
        if ind<ind2: S[ind]=S[ind]+H[ind2]
for ind in K.keys():
    for ind2 in S.keys():
        if ind<ind2: K[ind]=K[ind]+S[ind2]
for ind in D.keys():
    for ind2 in K.keys():
        if ind<ind2: D[ind]=D[ind]+K[ind2]
print(sum(D.values()))
