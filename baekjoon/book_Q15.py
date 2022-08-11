#same problem with no.18352

import sys
from collections import deque
N,M,K,X=map(int, sys.stdin.readline().split()) #N:도시개수,M:도로의 개수,K:거리정보,X:출발도시번호
dist=[-1]*(N+1)
dist[X]=0
load={x:[] for x in range(1,N+1)}
for _ in range(M):
    a,b=map(int, sys.stdin.readline().split())
    load[a].append(b)

states=deque()
states.append(X)

while states:
    s=states.popleft()
    for i in load[s]:
        if dist[i]==-1: 
            dist[i]=dist[s]+1
            states.append(i)

check=False
for i in range(1,N+1):
    if dist[i]==K: 
        print(i)
        check=True

if check==False: print(-1)