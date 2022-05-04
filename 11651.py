n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
    
arr.sort(key=lambda x : (x[1], x[0]))   # x[1]을 우선 그 다음 x[0]을 기준으로 정렬

for i in range(n):
    print(arr[i][0], end=" ")
    print(arr[i][1])