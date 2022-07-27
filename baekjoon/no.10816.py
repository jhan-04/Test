#시간초과
import sys
from collections import Counter
N=int(sys.stdin.readline())
card=sorted(Counter(list( map(int,sys.stdin.readline().strip().split()))).items(),key=lambda x:x[0])
M=int(sys.stdin.readline())
check=list(map(int,sys.stdin.readline().split()))


for i in check:
    s, e=0, len(card)-1
    while s<=e:
        m=int((s+e)/2)
        if i == card[m][0]:
            print(card[m][1],end=' ')
            break
        elif i > card[m][0]: 
            s=m+1
        else: e=m-1 
    if s>e: print(0,end=' ')