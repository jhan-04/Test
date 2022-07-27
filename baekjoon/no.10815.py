import sys
N=int(sys.stdin.readline())
card=set(map(int,sys.stdin.readline().split()))

M=int(sys.stdin.readline())
check=list(map(int,sys.stdin.readline().split()))

for i in check:
    if i in card: print(1,end=' ')
    else: print(0,end=' ')