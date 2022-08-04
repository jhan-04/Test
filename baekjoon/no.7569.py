
import sys
from collections import deque

M,N,H=map(int, sys.stdin.readline().split())
box=[]
loca=deque()

for i in range(N*H):
    if i%N==0: box.append([])
    lis=list(map(int, sys.stdin.readline().split()))
    box[i//N].append(lis)
    
    if 1 in lis: 
        for j in [i for i in range(M) if lis[i]==1]:
            loca.append((i//N,i%N,j))

#box[H][N][M]
#위 아래 상 하 좌 우
moving=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
maxi=0
while loca:
    z,x,y=loca.popleft()

    #if (z,x,y) in loca: continue
    for dh,dn,dm in moving:
        h,n,m=dh+z,dn+x,dm+y
        if h>=0 and h<H and n>=0 and n<N and m>=0 and m<M and box[h][n][m]==0: 
            box[h][n][m]=box[z][x][y]+1
            loca.append((h,n,m))
        
boxx=sum(sum(box,[]),[])
maxi=max(boxx)
if 0 in boxx: print(-1)
else: print(max(0,maxi-1))

#백준에서는 numpy 사용 불가능
'''import sys
import numpy as np
from collections import deque

M,N,H=map(int, sys.stdin.readline().split())
box=[]
for _ in range(N*H):
    box.append(list(map(int, sys.stdin.readline().split())))

box=np.array(box).reshape(H,N,M)

a,b,c=np.where(box==1)
loca=deque()
for i in zip(a,b,c):
    loca.append(tuple(i))
#위 아래 상 하 좌 우
moving=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
while loca:
    z,x,y=loca.popleft()
    if (z,x,y) in loca: continue
    for dh,dn,dm in moving:
        h,n,m=dh+z,dn+x,dm+y
        if h<0 or h>=H or n<0 or n>=N or m<0 or m>=M\
             or box[h,n,m]==1 or box[h,n,m]==-1 or box[h,n,m]<=box[z,x,y]+1: continue
        box[h,n,m]=box[z,x,y]+1
        loca.append((h,n,m))

if -1 in box: print(-1)
else: print(np.max(box)-1)'''


