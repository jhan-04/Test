import sys
from collections import deque

N=int(sys.stdin.readline())
nums=deque()
sol=deque()
for _ in range(N):
    a=int(sys.stdin.readline())
    if a!=0: 
        if not nums: nums.append(a)
        elif abs(a)>abs(nums[-1]) or (abs(a)==abs(nums[-1]) and a>=nums[-1]):nums.append(a)
        else:
            for i in range(len(nums)):
                if abs(a)<abs(nums[i]):
                    nums.insert(i,a)
                    break
                elif abs(a)==abs(nums[i]) and a<=nums[i]:
                    nums.insert(i,a)
                    break
    else:
        if not nums: sol.append(0)
        else:
            sol.append(nums.popleft())

while sol: print(sol.popleft())