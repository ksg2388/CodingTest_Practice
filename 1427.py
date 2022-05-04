n = int(input())
sort_num = list(map(int, str(n)))
sort_num.sort(reverse=True)

for i in sort_num:
    print(i, end="")