import sys
from collections import deque

mini,maxi=map(int, sys.stdin.readline().split())

sqr_set=deque(i**2 for i in range(2,int(maxi**0.5)+1))
sqr=deque()
while sqr_set:
    a=sqr_set.popleft()
    sqr_set=deque(x for x in sqr_set if x%a!=0)
    sqr.append(a)
nums=list(range(mini,maxi+1))


while sqr:
    s=sqr.popleft()
    nums=[x for x in nums if x%s!=0]

print(len(nums))


#틀림
'''while sqr:
    num=sqr.popleft()
    #num의 배수들
    if mini%num==0:
        cnt+=maxi//num-mini//num +1
    else: cnt+=maxi//num-mini//num
    #기존에 고려했던 num과 겹치는 배수들을 빼기
    for x in list(mul):
        s=x*num
        if s>maxi: continue
        if mini%s==0:
            cnt-=((maxi//s)-(mini//s) +1)
        else: cnt-=((maxi//s)-(mini//s) )
    mul.append(num)
    print(mul)
print(maxi-mini+1-cnt)'''

'''import sys
mini,maxi=map(int, sys.stdin.readline().split())

sqr=(i**2 for i in range(2,int(maxi**0.5)+1))
nums=set(range(mini,maxi+1))
sol=set()
for s in sqr:
    sol|=set(s*i for i in range(1,maxi//s+1) if s*i>=mini)

print(maxi-mini+1-len(sol))'''