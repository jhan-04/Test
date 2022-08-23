import sys
from collections import deque
N,K= map(int, sys.stdin.readline().split())
if K<=N: print(N-K)
else:
    dist=[False]*(100001)
    state=deque()
    state.append((0,N))
    while not dist[K]:
        t,s=state.popleft()
        if t>dist[s]:continue
        for i in range(3):
            if i==0: ns=s-1
            elif i==1: ns=s+1
            elif i==2: ns=s*2
            if not 0<=ns<=1e5:continue
            if  dist[ns]==False:
                dist[ns]=t+1
                state.append((t+1,ns))
                
    print(dist[K])
