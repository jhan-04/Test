import sys
N,M=map(int, sys.stdin.readline().split())
nums=list(map(int, sys.stdin.readline().split()))
for i in range(1,N):
    nums[i]=nums[i]+nums[i-1]
nums.insert(0,0)
for _ in range(M):
    i,j=map(int, sys.stdin.readline().split())
    print(nums[j]-nums[i-1])