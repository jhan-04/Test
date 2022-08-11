import sys
N=int(sys.stdin.readline())

sol=[0]
for _ in range(N):
    nums=list(map(int,sys.stdin.readline().split()))
    for i in range(len(nums)):
        if i-1<0: 
            nums[i]=nums[i]+sol[i]
        elif i>=len(sol): 
            nums[i]=nums[i]+sol[i-1]
        else:nums[i]=nums[i]+max(sol[i-1],sol[i])
    sol=[]+nums
print(max(nums))
