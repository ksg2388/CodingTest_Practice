from unittest import TestLoader

t = int(input())

for i in range(t):
    vps_list = []
    vps_list = list(map(str, input()))
    test_list = []
    
    for j in range(len(vps_list)):
        if vps_list[j] == '(':
            test_list.append(vps_list[j])
        else:
            if (len(test_list) > 0) and test_list[-1] == '(':
                test_list.pop()
            else:
                test_list.append(vps_list[j])
    
    if len(test_list) == 0:
        print("YES")
    else:
        print("NO")