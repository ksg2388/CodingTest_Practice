n = int(input())
s = []  #입력 받은 수열이 들어가는 리스트
op = [] #출력값이 들어가는 리스트
count = 1
temp = True

for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        op.append('+')
        count += 1
    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)