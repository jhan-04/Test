import sys
N,M= map(int,sys.stdin.readline().split())
parent=[i for i in range(N+1)]

def find_parent(x,parent):
    if parent[x]==x:
        return x
    else:
        return find_parent(parent[x],parent)

def union_parent(a,b,parent):
    a=find_parent(a,parent)
    b=find_parent(b,parent)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
load=[]
for _ in range(M):
    A,B,C= map(int,sys.stdin.readline().split())
    load.append((C,A,B))
load.sort()
cost=0
for C,A,B in load:
    if find_parent(A,parent)!=find_parent(B,parent):
        cost+=C
        last=C
        union_parent(A,B,parent)

print(cost-last)