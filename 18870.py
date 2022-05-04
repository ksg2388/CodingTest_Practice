from operator import index

n = int(input())
num_list = []
re_list = []

num_list = list(map(int, input().split()))

# 시간초과됨
# for i in range(n):
#     count = 0
#     for j in range(n):
#         if i == j:
#             continue
#         if(num_list[i] > num_list[j]):
#             if(num_list[j] in num_list[j+1:]):
#                 continue
#             count += 1
#     re_list.append(count)
# print(re_list)

# 시간초과2
# sort_list = sorted(num_list)

# i = 1
# while(True):
#     if i == len(sort_list):
#         break
#     if sort_list[i] == sort_list[i-1]:
#         sort_list.pop(i)
#     else:
#         i += 1

# for i in num_list:
#     re_list.append(sort_list.index(i))
    
# print(re_list)

sort_list = sorted(list(set(num_list)))
dic = {sort_list[i] : i for i in range(len(sort_list))}
for i in num_list:
    print(dic[i], end = ' ')