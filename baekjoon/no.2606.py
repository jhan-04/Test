import sys
from collections import deque

K=int(sys.stdin.readline())
N=int(sys.stdin.readline())
connection=[[] for _ in range(K+1)]
for _ in range(N):
    a,b=map(int, sys.stdin.readline().split())
    connection[a].append(b)
    connection[b].append(a)
addict=deque()
addict.append(1)
state=[False]*(K+1)
state[1]=True
while addict:
    a=addict.popleft()
    for i in connection[a]:
        if state[i]==False:
            state[i]=True
            addict.append(i)
print(sum(state)-1)
    


