import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())

nums=list(map(int,sys.stdin.readline().split()))
cnt=0 #the number of group sum of which is M
front={x:[] for x in range(N)}
back={x:[] for x in range(N)}

for i in range(N):
    front[sum(nums[:i+1])%M].append(i)
    back[sum(nums[i:])%M].append(i)
print(front)
print(back)
sets=[0]*M
for i in range(M):
    sets[i]=sum([1 for x in front[i] for y in back[i] if x>=y])

print(sum(sets)+1*(sum(nums)%M==0))

'''import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())

inputs=list(map(int,sys.stdin.readline().split()))
cnt=0 #the number of group sum of which is M

for i in range(N):
    for j in range(i,N):
        if sum(inputs[i:j+1])%M==0: cnt+=1
print(cnt)'''

'''#시간초과
import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())

nums=deque(map(int,sys.stdin.readline().split()))
sum=deque()
cnt=0 #the number of group sum of which is M

while nums:
    n=nums.popleft()
    a=deque()
    while sum: 
        s=sum.popleft()
        if (s+n)%M==0: 
            cnt+=1
        a.append(s+n)
    sum=deque()+a
    sum.append(n)
    if n%M==0: cnt+=1

print(cnt)'''