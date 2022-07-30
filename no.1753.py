import sys
import heapq
V,E=map(int, sys.stdin.readline().split())
K=int(sys.stdin.readline())

load=[1e9]*(V+1)
load[K]=0

mapping={x:[] for x in range(1,V+1)}
state=[]
heapq.heappush(state,(0,K)) #(거리, node)으로 push해야 시간이 줄어듬, (node,거리)는 안됨

for i in range(E):
    u,v,w= map(int,sys.stdin.readline().split())
    mapping[u].append((v,w))

while state:
    s_v,s=heapq.heappop(state)
    #s를 push하고 뒤에서 다시 최소값을 찾아 push했을 수도 있음
    #따라서 뒤에 s가 state에 또 존재할 경우 앞에 s무시
    if load[s]<s_v:
        continue
    for v,w in mapping[s]:
        dist=s_v+w
        if load[v]>dist:
            load[v]=dist
            heapq.heappush(state,(dist,v))

load=[load[i] if not load[i]==1e9 else 'INF' for i in range(1,V+1)]
for x in load: print(x)