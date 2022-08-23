import sys

N,K=map(int, sys.stdin.readline().split())
lan=[]
for _ in range(N):
    lan.append(int(sys.stdin.readline()))
maxi=max(lan)*N//K
mini=min(lan)*N//K
mid=(maxi+mini)/2
sol=0
if N==0: print(0)
else: 
    while (maxi-mini)>1:
        lenth=(maxi+mini)//2
        num=sum([x//lenth for x in lan])
        if num>=K: 
            sol=max(sol,lenth)
            mini=lenth
        else: maxi=lenth

    if maxi==0: sol=max(sol,maxi)
    elif sum([x//maxi for x in lan])>=K: sol=max(sol,maxi)
    if mini==0: sol=max(sol,mini)
    elif sum([x//mini for x in lan])>=K: sol=max(sol,mini)

    print(int(sol))