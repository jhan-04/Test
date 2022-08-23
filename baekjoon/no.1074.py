import sys
N,r,c=map(int, sys.stdin.readline().split())

cnt=0

def ordering(state1,state2):
    global cnt
    x1,y1=state1
    x2,y2=state2

    if x1+1==x2:
        if x1==r and y1==c: return cnt
        elif x1==r and y2==c: return cnt+1
        elif x2==r and y1==c: return cnt+2
        elif x2==r and y2==c: return cnt+3

    if x1<=r<=(x1+x2)//2 and y1<=c<=(y1+y2)//2:
        return ordering((x1,y1),((x1+x2)//2,(y1+y2)//2))
    else: 
        cnt+= (x2-x1+1)**2//4
    if x1<=r<=(x1+x2)//2 and (y1+y2)//2 +1<=c<=y2:
        return ordering((x1,(y1+y2)//2 +1),((x1+x2)//2,y2))
    else: 
        cnt+= (x2-x1+1)**2//4
    if (x1+x2)//2+1<=r<=x2 and y1<=c<=(y1+y2)//2:
        return ordering(((x1+x2)//2+1,y1),(x2,(y1+y2)//2))
    else: 
        cnt+= (x2-x1+1)**2//4
    if (x1+x2)//2+1<=r<=x2 and (y1+y2)//2 +1<=c<=y2:
        return ordering(((x1+x2)//2 +1,(y1+y2)//2+1),(x2,y2))
    else:
        cnt+= (x2-x1+1)**2//4

print(ordering((0,0),(2**N-1,2**N-1)))


