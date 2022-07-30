import sys
from collections import deque
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))

sol=[-1]*(N)

stack=deque()
stack.append(0)
s=0

while stack:
    if N==1: break
    s=stack[-1]
    for i in range(s+1,N):
        if len(stack)==0: 
            stack.append(i-1)
            break
        if A[stack[-1]]>=A[i]: 
            stack.append(i)
        else:
            while stack:
                if A[stack[-1]]<A[i]: 
                    sol[stack.pop()]=A[i]
                else:
                    stack.append(i)
                    break          
    if i>=N-1: break

for s in sol: print(s,end=' ')


'''for i in range(N):
    stack=deque()
    if sol[i]!=-1: 
        print(sol[i],end=' ')
        continue

    stack.append(i)
    for j in range(i+1,N):
        if len(stack)==0 : break
        if A[stack[-1]]<A[j]:
            while stack:
                if A[stack[-1]]<A[j]: sol[stack.pop()]=A[j]
                elif sol[j]!=-1:
                    stack.append(j)
                    break
      
    print(sol[i],end=' ')'''