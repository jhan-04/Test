import sys
M=int(sys.stdin.readline())
N=int(sys.stdin.readline())

num=list(range(2,N+1))
prime=[]
while num:
    p=num[0]
    prime.append(p)
    num=[x for x in num if x%p!=0]
    #print(num)
    #print('prime=',prime)

prime=[x for x in prime if x>=M]
if len(prime)!=0:
    print(sum(prime))
    print(prime[0])
else: print(-1)