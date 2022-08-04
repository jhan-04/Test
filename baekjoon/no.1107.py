import sys
N=sys.stdin.readline().strip()

K=int(sys.stdin.readline())
if K==0: 
    print(min(abs(100-int(N)),len(N)))
else:
    broken=list(sys.stdin.readline().split())
    
    #0. num is not in bromken number
    if sum([1 for x in N if x in broken])==0:
        print(min(abs(100-int(N)),len(N)))
    else:
        #1.start 100
        mov100=abs(int(N)-100)
        #2.move to other number>N
        num_min=int(N)
        num_plus=int(N)
        while 1:
            num_min-=1
            num_plus+=1
            if not set(str(num_min))&set(broken):
                mov_other=len(str(num_min))+abs(int(N)-num_min)
                break
            if not set(str(num_plus))&set(broken):
                mov_other=len(str(num_plus))+abs(int(N)-num_plus)
                break
        print(min(mov100,mov_other))


