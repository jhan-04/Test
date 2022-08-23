
import sys
from itertools import combinations
L,C= map(int, sys.stdin.readline().split())
alpha=sys.stdin.readline().strip().split()

aa=['a','e','i','o','u']
mo=[x for x in alpha if x in aa]
ja=[x for x in alpha if x not in aa]
sol=[]
for i in range(1, min(len(aa)+1,L-1)):
    for x1 in combinations(mo,i):
        for x2 in combinations(ja,L-i):
            sol.append(''.join(x for x in sorted(x1+x2)))
sol.sort()
for s in sol: print(s)
