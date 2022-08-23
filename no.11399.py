import sys
N=int(sys.stdin.readline())
nums=list(map(int, sys.stdin.readline().split()))
nums.sort()
time=[0]*N
time[0]=nums[0]
for i in range(1,N):
    time[i]=time[i-1]+nums[i]
print(sum(time))