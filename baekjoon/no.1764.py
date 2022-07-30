
import sys

N,M=list(map(int, sys.stdin.readline().split()))
not_see=set()
not_hear=set()
for _ in range(N):
    not_see.add(sys.stdin.readline().strip())

for _ in range(M):
    not_hear.add(sys.stdin.readline().strip())

not_seehear= sorted(list(not_see &not_hear))
print(len(not_seehear))
for x in not_seehear: print(x)