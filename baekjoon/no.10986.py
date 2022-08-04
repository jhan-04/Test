import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())

nums=deque(map(int,sys.stdin.readline().split()))
sum=deque()

cnt=0#the number of group sum of which is M
while nums:
    n=nums.popleft()
    a=deque()
    while sum: #수정필요
        s=sum.popleft()
        if (s+n)%M==0: 
            print('n=',n,'s=',s)
            cnt+=1
        a.append(s+n)
    
    sum=deque()+a
    sum.append(n)
    if n%M==0: cnt+=1
    print(sum)
print(cnt)