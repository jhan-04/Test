#same problem with no.14502
import sys
N,M=map(int, sys.stdin.readline().split()) 

vir_map=[0]*N
for i in range(N):
    vir_map[i].append(list(map(int, sys.stdin.readline().split()) ))
