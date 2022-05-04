import imp
import sys
from collections import Counter

n = int(sys.stdin.readline())
list1 = []

for i in range(n):
    list1.append(int(sys.stdin.readline()))

list1.sort()

print(round(sum(list1)/n))          #산술평균
print(list1[n//2])                  #중앙값

cnt_li = Counter(list1).most_common()
if len(cnt_li) > 1 and cnt_li[0][1] == cnt_li[1][1]:
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])             #최빈값
print(max(list1) - min(list1))      #범위