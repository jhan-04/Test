
import sys

N=int(sys.stdin.readline()) 
home=list(map(int,sys.stdin.readline().split()))
home.sort()
# 중간값에서 값이 최소이다. 
print(home[(N-1)//2])