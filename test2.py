from collections import deque
a=deque()
a.append(1)
a.append(2)
b=deque()+a
print(a)
print(b)
a.pop()
print(a)
print(b)