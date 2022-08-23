import sys
from collections import deque
N= int(sys.stdin.readline())
nums= list(map(int,sys.stdin.readline().split()))

cnt=[1]*N
state=deque()

for i in range(N): state.append((1,i))#cnt,index
maxi=1
while state:
    c,s=state.popleft()
    if cnt[s]>c: continue
    for i in range(s,N):
        if nums[i]>nums[s] and cnt[i]<c+1:
            cnt[i]=c+1
            state.append((c+1,i))
            maxi=max(maxi,c+1)

print(maxi)