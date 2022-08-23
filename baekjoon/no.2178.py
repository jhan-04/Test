import sys
from collections import deque

N,M= map(int,sys.stdin.readline().split()) #row,col
maps=[]
for _ in range(N):
    a=list(sys.stdin.readline().strip())
    maps.append(list(map(int,a)))


state=deque()
state.append((1,0,0))#cnt,row,col

dx=[0,0,1,-1]
dy=[1,-1,0,0]
while state:
    d,x,y=state.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=M: continue
        if maps[nx][ny]==0: continue
        if maps[nx][ny]==1 or maps[nx][ny]>d+1:
            maps[nx][ny]=d+1
            state.append((d+1,nx,ny))
print(maps[N-1][M-1])














# 다시 공부하고 해볼 것
'''def moving(x,y,table_map,load,fail):
    #동남서북
    x_move=[1,0,-1,0]
    y_move=[0,-1,0,1]
    for x_m,y_m in zip(x_move,y_move):
        if table_map[x+x_m][y+y_m]=='1' and ((x+x_m,y+y_m) not in fail):
            if (x,y) in load:
                load.remove((x,y))
                fail.append((x,y))
            else:
                load.append((x+x_m,y+y_m))    
            x=x+x_m
            y=y+y_m
    return x,y,load,fail'''


'''N,M= map(int, sys.stdin.readline().split())
table_map=[]

for _ in range(N):
    table_map.append(list(sys.stdin.readline().split()))
x_move=[1,0,-1,0]
y_move=[0,1,0,-1]
x,y=0,0
load=[(0,0)]
fail=[]
while x!=N-1 or y!=M-1:
    cnt=0
    for x_m,y_m in zip(x_move,y_move):
        if x+x_m>=0 and y+y_m>=0 and x+x_m<N and y+y_m<M:
            if table_map[x+x_m][y+y_m]=='1' and ((x+x_m,y+y_m) not in load) and ((x+x_m,y+y_m) not in fail):
                load.append((x+x_m,y+y_m))    
                x=x+x_m
                y=y+y_m
                break
            else: cnt+=1 
        else: cnt+=1
    if cnt==4: 
        load.remove((x,y))
        fail.append((x,y))
        x=load[-1][0]
        y=load[-1][1]
print(load)
print(len(load))'''
