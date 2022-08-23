import sys
N,K=map(int, sys.stdin.readline().split())
nums=[x for x in range(1,N+1)]
sol=[]

state=0
while nums:
    cnt=K
    state=(state+cnt-1)%len(nums)
    sol.append(nums[state])
    del nums[state]

print('<'+str(sol)[1:-1]+'>')