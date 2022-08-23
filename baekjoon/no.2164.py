import sys
from collections import deque
N= int(sys.stdin.readline())
card=deque([x for x in range(1,N+1)])
while len(card)>1:
    card.popleft()
    a=card.popleft()
    card.append(a)
print(card[0])