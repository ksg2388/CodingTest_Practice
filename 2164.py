from collections import deque
import sys

n = int(sys.stdin.readline())
q = deque([])

for i in range(1, n+1):
    q.append(i)

while len(q) > 1:
    q.popleft()
    q.rotate(-1)

print(*q)