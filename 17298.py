from collections import deque

n = int(input())
s = list(map(int, input().split()))
stack = []
nge = [-1 for i in range(n)]

for i in range(n):
    while stack and s[stack[-1]] < s[i]:
        nge[stack.pop()] = s[i]
    stack.append(i)

print(*nge)