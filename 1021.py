from collections import deque

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
dq = deque([])
count = 0

for i in range(1, n+1):
    dq.append(i)
    
for i in num_list:
    if (i == dq[0]):
        dq.popleft()
    else:
        if dq.index(i) > len(dq)//2:
            while True:
                dq.rotate(1)
                count += 1
                if (i == dq[0]):
                    dq.popleft()
                    break
        else:   
            while True:
                dq.rotate(-1)
                count += 1
                if (i == dq[0]):
                    dq.popleft()
                    break

print(count)