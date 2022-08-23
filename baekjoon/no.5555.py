import sys
check= sys.stdin.readline().strip()
N=int(sys.stdin.readline())
cnt=0
for _ in range(N):
    ring=sys.stdin.readline().strip()
    if check in ring*2: cnt+=1
    #elif check[::-1] in  ring*2: cnt+=1
print(cnt)

