import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])

for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        queue.append(int(a[1]))
    elif a[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(queue))
    elif a[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)