import sys
from collections import deque
N=int(sys.stdin.readline()) #the number of cities
M=int(sys.stdin.readline()) #the number of bus
maps=[[] for _ in range(N+1)]

for _ in range(M):
    a,b,c=map(int, sys.stdin.readline().split())
    maps[a].append((c,b)) #(cost,departure)

for arr in range(1,N+1): #arrival
    cost=[1e9]*(N+1)
    cost[arr]=0
    state=deque()
    state.append((0,arr)) #cost,arrival city
    while  state:
        c,a=state.popleft()
        if (c,a) in state: continue
        for c1,d in maps[a]: #(departure,cost)
            if cost[d]>c+c1: 
                cost[d]=c+c1
                state.append((c+c1,d))
    del cost[0]
    cost=[x if x!=1e9 else 0 for x in cost] 
    print(* cost)
