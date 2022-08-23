import sys
from itertools import permutations
N,M=map(int, sys.stdin.readline().split())

nums=list(range(1,N+1))
for x in permutations(nums,M):
    print(* x)
