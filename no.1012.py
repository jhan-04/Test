import sys
from collections import deque

def maps_arrange(x,y):
    if maps[x][y]==0:
        return False

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    location=deque()
    location.append((x,y))
    while location:
        x,y=location.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or ny<0 or nx>=M or ny>=N: continue
            if maps[nx][ny]==1:
                maps[nx][ny]=0
                location.append((nx,ny))
    return True


T=int(sys.stdin.readline())
for t in range(T): #test case t
    M,N,K=map(int, sys.stdin.readline().split())
    maps=[[0]*N for _ in range(M)]
    for k in range(K):
        x,y=map(int, sys.stdin.readline().split())
        maps[x][y]=1
    cnt=0
    for x in range(M):
        for y in range(N):
            if maps_arrange(x,y): cnt+=1
    print(cnt)