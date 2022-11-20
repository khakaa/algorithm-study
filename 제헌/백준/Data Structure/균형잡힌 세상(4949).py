while True:
    s = input()
    stack = []
    flag = True

    if s == '.':
        break

    for a in s:
        if a == '(' or a == '[':
            stack.append(a)

        elif a == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break

        elif a == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break

    print('yes') if flag == True and len(stack) == 0 else print('no')