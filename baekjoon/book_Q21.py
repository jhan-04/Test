#same problem with no.16234
import sys
from collections import deque
N,L,R=map(int, sys.stdin.readline().split()) 
people=[]
for _ in range(N):
    people.append(list(map(int, sys.stdin.readline().split())))

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def sol(i,j,ind):
    check[i][j]=ind
    q=[]
    q.append((i,j))
    cities=deque()
    cities.append((i,j))
    summ=people[i][j]
    num=1

    while cities:
        a,b= cities.popleft()
        for k in range(4):
            xn=a+dx[k]
            yn=b+dy[k]
            if xn<0 or xn>=N or yn<0 or yn>=N or check[xn][yn]!=-1: continue
            if L<=abs(people[a][b]-people[xn][yn])<=R: 
                check[xn][yn]=ind
                cities.append((xn,yn))
                q.append((xn,yn))
                summ+=people[xn][yn]
                num+=1

    for a,b in q:
        people[a][b]=summ//num
    return num
            

                
cnt=0
while 1:
    ind=0
    check=[[-1]*N for _ in range(N)]
    
    for x in range(N):
        for y in range(N):
            if check[x][y]==-1:
                sol(x,y,ind)
                ind+=1
    if ind==N*N: break
    cnt+=1

print(cnt)
        

