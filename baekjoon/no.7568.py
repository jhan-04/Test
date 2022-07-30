import sys
N=int(sys.stdin.readline())
person=[]
for i in range(N):
    person.append(list(map(int,sys.stdin.readline().split())))
rank_list=[1]*N
for i in range(N):
    rank0=0
    if i==0: 
        rank_list[0]==1
        continue
    for j in range(i):
        if person[i][0]>person[j][0] and person[i][1]>person[j][1]:
            rank_list[j]=rank_list[j]+1
        elif person[i][0]<person[j][0] and person[i][1]<person[j][1]:
            rank_list[i]=rank_list[i]+1

for x in rank_list: print(x, end=' ')

