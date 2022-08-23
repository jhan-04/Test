import sys
N=int(sys.stdin.readline())
x=[]
y=[]
z=[]
load=[]#(거리,행성1,행성2)
for i in range(N):
    a,b,c=map(int, sys.stdin.readline().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))
x.sort()
y.sort()
z.sort()

for i in range(N-1):
    load.append((abs(x[i][0]-x[i+1][0]),x[i][1],x[i+1][1]))
    load.append((abs(y[i][0]-y[i+1][0]),y[i][1],y[i+1][1]))
    load.append((abs(z[i][0]-z[i+1][0]),z[i][1],z[i+1][1]))
load.sort()

parent=[i for i in range(N)]
total_cost=0
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
for cost,p1,p2 in load:
    if find_parent(parent,p1)!=find_parent(parent,p2): 
        #최종 parent값의 parent값을 변경하기 위해
        p1=find_parent(parent,p1)
        p2=find_parent(parent,p2)
        if p1<p2:
            parent[p2]=p1
        else: 
            parent[p1]=p2
        total_cost+=cost
print(total_cost)