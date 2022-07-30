import queue
import sys
from collections import deque
N,M,V=list(map(int, sys.stdin.readline().split()))
graph=[[]]*(N+1)
visited=[False]*(N+1)
for i in range(M):
    A,B=list(map(int, sys.stdin.readline().split()))
    graph[A]=graph[A]+[B]
    graph[B]=graph[B]+[A]

graph=[sorted(x) for x in graph]

def DFS(graph,V,visit):
    visit[V]=True
    print(V,end=' ')
    for i in graph[V]:
        if visit[i]==False:
            DFS(graph,i,visit)


def BFS(graph,V,visit):
    que=deque([V])
    while que:
        i= que.popleft()
        visit[i]=True
        print(i,end=' ')
        for j in graph[i]:
            if visit[j]==False:
                que.append(j)
                visit[j]=True
DFS(graph,V,visited)
print('')
visited=[False]*(N+1)
BFS(graph,V,visited)