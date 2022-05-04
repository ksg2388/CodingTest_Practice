k = int(input())
num_iist = []

for i in range(k):
    a = int(input())
    if a != 0:
        num_iist.append(a)
    else:
        num_iist.pop()

print(sum(num_iist))