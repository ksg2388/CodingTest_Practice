n = int(input())
member_list = []

for i in range(n):
    a, b = input().split()
    member_list.append((int(a), b))
    
member_list.sort(key=lambda x : x[0])

for i in range(n):
    print(member_list[i][0], end=" ")
    print(member_list[i][1])