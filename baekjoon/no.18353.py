import sys
N=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))
nums.reverse()
cnt=[1]*N

for i in range(N):
    n=nums[i]
    for j in range(i):
        if nums[j]<n: cnt[i]=max(cnt[i],cnt[j]+1)
print(N-max(cnt))
