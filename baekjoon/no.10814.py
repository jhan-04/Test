import sys
N=int(sys.stdin.readline())
names=[]
for i in range(N):
    a,b=sys.stdin.readline().strip().split()
    names.append((a,b))

names.sort(key=lambda x:int(x[0]))
for age,name in names:
    print(age, name)