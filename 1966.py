import sys

num = int(sys.stdin.readline())

for i in range(num):
    count = 0
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    checklist = [0 for _ in range(n)]
    checklist[m] = 1
    
    while True:
        if max(a) == a[0]:
            count += 1
            
            if checklist[0] == 1:
                print(count)
                break
            else:
                del a[0]
                del checklist[0]
        
        else:
            a.append(a[0])
            del a[0]
            checklist.append(checklist[0])
            del checklist[0]