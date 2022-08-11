#ㅇ
L,N,T= map(int, input().split())
location=[0]*N
dir=[0]*N
for i in range(N):
    location[i],dir[i]=input().split()

location=list(map(int, location)) #location=[int(i) for i in location]
dir=[-1 if i=='L' else 1 for i in dir]
cnt=0
for t in range(T):
    #change direction when ball in next the wall
    dir=[-1*dir[i] if (location[i]==0 and dir[i]==-1)or(location[i]==L and dir[i]==1) else dir[i] for i in range(N)]
    location=[loca+mov for loca,mov in zip(location,dir)]
    if len(location)!=len(list(set(location))):
        cnt+=1
print(cnt)