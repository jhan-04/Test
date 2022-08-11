import sys

N=int(sys.stdin.readline()) 
students=[]
for _ in range(N):
    name,k,e,m=sys.stdin.readline().strip().split()
    students.append((name,int(k),int(e),int(m)))

students.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in students: print(i[0])