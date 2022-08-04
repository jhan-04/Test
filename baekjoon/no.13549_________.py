
import sys
from collections import deque
N,K=map(int, sys.stdin.readline().split())

loca=deque() #(location, time)
loca.append(N)
visited=[-1]*100001
visited[N]=0
while loca:
    s=loca.popleft() #state, time

    #three case: *2,-,+,
    if s*2>=0 and s*2<100001 and (visited[s*2]==-1 or visited[s*2]>visited[s]):
        visited[s*2]=visited[s]
        loca.append(s*2)
    if s+1>=0 and s+1<100001 and (visited[s+1]==-1 or visited[s+1]>visited[s]+1): 
        visited[s+1]=visited[s]+1
        loca.append(s+1)
    if s-1>=0 and s-1<100001 and (visited[s-1]==-1 or visited[s-1]>visited[s]+1):
        visited[s-1]=visited[s]+1
        loca.append(s-1)
#while문 내에서 visited[K]가 -1이 아닐 경우 print를 하면 
#뒤에서 더 짧은 시간에 K로 가는 경우를 놓칠 수 있다.
print(visited[K])
    