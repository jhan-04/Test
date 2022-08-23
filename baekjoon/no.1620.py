import sys
N,M= map(int, sys.stdin.readline().split())
poketmon1={}
poketmon2={}
for i in range(N):
    a=sys.stdin.readline().strip()
    poketmon1[str(i+1)]=a
    poketmon2[a]=i+1

for _ in range(M):
    a=sys.stdin.readline().strip()
    if a == a.upper(): print(poketmon1[a])
    else: print(poketmon2[a])