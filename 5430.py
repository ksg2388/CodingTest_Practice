from collections import deque
import re


t = int(input())

for _ in range(t):
    cmd = list(input())
    n = int(input())
    num_list = deque(re.findall(r'\d+', input()))
    
    for i in cmd:
        if i == 'R':
            num_list.reverse()
        if i == 'D':
            if num_list:
                num_list.popleft()
            else:
                print('error')
                break
    if num_list:
        print('[', end='')
        while len(num_list) > 1:
            print(num_list.popleft(), end=',')
        print(num_list.popleft(), end=']')
        print()