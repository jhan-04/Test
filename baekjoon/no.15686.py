import sys
from itertools import combinations
from collections import deque

N,M=map(int, sys.stdin.readline().split())
chickens=[]
house=[]
for i in range(N):
    a=list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if a[j]==2: chickens.append((i,j))
        elif a[j]==1: house.append((i,j)) 

def cal_destance(chicken):
    dist=[[False]*N for _ in range(N)]
    state=deque()
    #치킨집의 거리 지도
    for i,j in chicken:
        dist[i][j]=0
        state.append((0,i,j))
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    while state:
        d,x,y=state.popleft()
        if d>dist[x][y]: continue
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N: continue
            if dist[nx][ny]==False or dist[nx][ny]>d+1:
                dist[nx][ny]=d+1
                state.append((d+1,nx,ny))

    #모든 집의 치킨 거리
    chicken_distance=0
    for x,y in house:
        chicken_distance+=dist[x][y]
    
    return chicken_distance


sol=[]
for c in combinations(chickens,M):
    sol.append(cal_destance(c))
print(min(sol))