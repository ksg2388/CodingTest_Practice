from collections import deque

n, k = map(int, input().split())
q = deque([])
y = deque([])

for i in range(1, n+1):
    q.append(i)
    
for i in range(n):
    q.rotate(-k)
    y.append(q.pop())

print('<', end="")
for i in range(n-1):
    print(y[i], end=', ')
print(y[-1], end="")
print('>')