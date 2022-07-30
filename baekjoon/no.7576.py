
import sys
from collections import deque

M,N=map(int,sys.stdin.readline().split())
box=[]
for i in range(N):
    box.append(list(map(int,sys.stdin.readline().split())))


di=[1,-1,0,0]
dj=[0,0,1,-1]



ones=[(i,j) for i in range(N) for j in range(M) if box[i][j]==1]
lst=deque()
for i,j in ones:
    lst.append((i,j))

while lst:
    i,j=lst.popleft()
    for d in range(4):
        ni=i+di[d]
        nj=j+dj[d]
        if ni<0 or nj<0 or ni>=N or nj>=M or box[ni][nj]==-1: continue
        if box[ni][nj]==0 or box[ni][nj]>box[i][j]+1: 
            box[ni][nj]=box[i][j]+1
            lst.append((ni,nj))

if True in [0 in x for x in box]: print(-1)
else: print(max([max(x) for x in box])-1)
            