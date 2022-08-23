import sys
N,M= map(int, sys.stdin.readline().split())
maps=[]
for i in range(N):
    a=sys.stdin.readline().strip()
    maps.append(a)

state=set([])
state.add((0,0,maps[0][0])) #count, row,column, 거쳐온 load
dx=[0,0,1,-1]
dy=[1,-1,0,0]

#dist=[[0]*M for _ in range(N)]
solution=1
while state:
    x,y,load=state.pop()
    #if dist[x][y]>cnt: continue
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=N or ny>=M: continue
        if maps[nx][ny] in load: continue
        '''if dist[nx][ny]<=cnt+1:
            dist[nx][ny]=cnt+1
            solution=max(solution,cnt+1)
            state.append((cnt+1,nx,ny,load | set([maps[nx][ny]])))'''
        solution=max(solution,len(load)+1)
        state.add((nx,ny,load+maps[nx][ny]))

print(solution)
            