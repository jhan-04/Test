
import sys

T=int(sys.stdin.readline())
for i in range(T):
    orders=sys.stdin.readline().strip()
    n=int(sys.stdin.readline())
    a=sys.stdin.readline().strip()
    dell=orders.count('D')
    if dell>n: 
        print('error')
        continue
    if dell==n: 
        print('[]')
        continue

    test=list(a[1:-1].split(','))
    reversing=False
    for order in orders:
        if order=='R': reversing=not(reversing)
        else: del test[0-1*reversing]
    if reversing: 
        print('['+','.join(test[::-1])+']')
    else: print('['+','.join(test)+']')

    