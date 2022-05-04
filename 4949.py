while True:
    sol_list = []
    testline = input()
    if testline == '.':
        break
    for i in list(testline):
        if i == '(':
            sol_list.append(i)
        elif i == '[':
            sol_list.append(i)
        elif i == ')':
            if len(sol_list) > 0 and sol_list[-1] == '(':
                sol_list.pop()
            else:
                sol_list.append(i)
        elif i == ']':
            if len(sol_list) > 0 and sol_list[-1] == '[':
                sol_list.pop()
            else:
                sol_list.append(i)
    
    if len(sol_list) == 0:
        print('yes')
    else:
        print('no')