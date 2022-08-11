import sys
import heapq

N=int(sys.stdin.readline()) 
nums=[]
for _ in range(N):
    heapq.heappush(nums,int(sys.stdin.readline()))


sums=0
while len(nums)!=1:
    # heappop: 가장 작은수를 뽑아냄
    #여기서 주의사항은 인덱스 0에 가장 작은 원소가 있다고 해서, \
    # 인덱스 1에 두번째 작은 원소, 인덱스 2에 세번째 작은 원소가 있다는 보장은 없다는 것입니다. \
    # 왜냐하면 힙은 heappop() 함수를 호출하여 원소를 삭제할 때마다 \
    # 이진 트리의 재배치를 통해 매번 새로운 최소값을 인덱스 0에 위치시키기 때문입니다.
    a=heapq.heappop(nums)+heapq.heappop(nums)
    sums+=a
    heapq.heappush(nums,a)

print(sums)
