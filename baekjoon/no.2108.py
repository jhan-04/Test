#시간초과
import sys

N=int(sys.stdin.readline())
nums=[]
summ=0
for i in range(N):
    nums.append(int(sys.stdin.readline()))
    summ+=nums[i]

ranking=[0]*(N+1)
same=[0]*(N+1)

cnt=[(-1,-1)] #count,value
sol=[False]*4
#1
sol[0]=int(round(summ/N,0))

for i in range(N):
    for j in range(i,N):
        if nums[i]==nums[j]:
            same[i]+=1
            same[j]+=1
        if nums[i]>nums[j]:
            ranking[j]+=1
        else: ranking[i]+=1
for i in range(N):
    #calcultation
    if ranking[i]==N//2+1:
        sol[1]=nums[i]#2
    if ranking[i]==1:
        maxi=nums[i]#4
    if ranking[i]==N:
        mini=nums[i]#4
    #3
    if same[i]>cnt[0][0]:
            cnt=[(same[i],nums[i])]
    elif same[i]==cnt[0][0] and ((same[i],nums[i]) not in cnt):
        cnt.append((same[i],nums[i]))

#3 
if len(cnt)==1: sol[2]=cnt[0][1]
else: 
    cnt.sort(key=lambda x: x[1])
    sol[2]=cnt[1][1]
#4
sol[3]=maxi-mini

for s in sol: print(s)