import sys
N,M=map(int, sys.stdin.readline().split())
trees=list(map(int, sys.stdin.readline().split()))
mini=0
maxi=max(trees)
while maxi>=mini:
    mid=(maxi+mini)//2
    bring=0
    for t in trees:
        if t>mid: bring+=t-mid
    if bring<M: maxi=mid-1
    else:
        result=mid
        mini=mid+1

print(result)
