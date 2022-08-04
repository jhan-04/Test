import sys
N,K=map(int, sys.stdin.readline().split())
coin=[]
for _ in range(N):
    coin.append(int(sys.stdin.readline()))
coin.sort(reverse=True)

sol=0
for c in coin:
    sol+=(K//c)
    K%=c
    if K==0: break

print(sol)
