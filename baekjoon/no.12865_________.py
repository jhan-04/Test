import sys
N,K=map(int,sys.stdin.readline().split())
sum=[0]*(K+1)
for _ in range(N):
    M,V=map(int,sys.stdin.readline().split())
    
    for i in range(K,M-1,-1):
        sum[i]=max(sum[i],sum[i-M]+V)
print(max(sum))


#메모리
'''import sys
N,K=map(int,sys.stdin.readline().split())
stuff=set()
for i in range(N):
    stuff.add(tuple(map(int,sys.stdin.readline().split())))
cases=[(0,0)]
for s in stuff:
    for case in cases:
        if case[0]+s[0]<=K: 
            cases.append((case[0]+s[0],case[1]+s[1]))
print(max(cases,key=lambda x:x[1])[1])'''


#시간 초과
'''import sys
from itertools import combinations
N,K=map(int,sys.stdin.readline().split())
stuff=[]
for i in range(N):
    stuff.append(tuple(map(int,sys.stdin.readline().split())))

starting=0
endind=0
val=0
for i in range(1,N+1):
    for set in combinations(stuff,i):
        if sum([x[0] for x in set])<=K: val=max(val, sum([x[1] for x in set]))
print(val)'''