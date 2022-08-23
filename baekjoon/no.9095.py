import sys
from collections import deque
N= int(sys.stdin.readline())
nums=[]
for _ in range(N):
    K= int(sys.stdin.readline())
    nums.append(K)
maxi=max(nums)
cnt=[0]*(maxi+1)
state=deque()
state.append(0)
while state:
    s=state.popleft()
    for i in range(1,4):
        if s+i<=maxi:
            cnt[s+i]+=1
            state.append(s+i)

for n in nums: print(cnt[n])