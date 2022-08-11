#same problem with no.14502
import sys
from collections import deque
N,K=map(int, sys.stdin.readline().split()) 

vir_map=[]
cases=[]

for i in range(N):
    a=list(map(int, sys.stdin.readline().split()))
    vir_map.append(a)
    for j in range(N):
        if a[j]!=0: cases.append((a[j],0,i,j))

S,X,Y=map(int, sys.stdin.readline().split())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
qq=deque(sorted(cases))
qq2=deque()

while qq:
    v,time,x,y=qq.popleft()
    if time==S: break
    for i in range(4):
        xn=x+dx[i]
        yn=y+dy[i]
        if xn<0 or xn>=N or yn<0 or yn>=N: continue
        if vir_map[xn][yn]==0:
            vir_map[xn][yn]=v
            qq.append((v,time+1,xn,yn))

        

print(vir_map[X-1][Y-1])