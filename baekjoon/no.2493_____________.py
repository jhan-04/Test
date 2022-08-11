
import sys
from collections import deque

N=int(sys.stdin.readline())
tops=tuple(map(int,sys.stdin.readline().split()))

sol=[0]*N
maxi=deque() # 큰값만 순서대로 add 내림차순, [2 3 1 2 4 2]->[4 2]

for i in range(N):
    while maxi:
        if maxi[-1][1]>=tops[i]: 
            sol[i]=maxi[-1][0]+1
            break
        else: maxi.pop()
    maxi.append((i,tops[i]))
    
for s in sol: print(s,end=' ')
