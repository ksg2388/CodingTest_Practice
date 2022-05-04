n = int(input())
list1 = []

for i in range(n):
    a = int(input())
    list1.append(a)

for i in sorted(list1):
    print(i)