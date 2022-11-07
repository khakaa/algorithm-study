def solution(s):
    answer = True
    stack = []

    # s 만큼 반복문
    for b in s:
        if len(stack) == 0:
            stack.append(b)

        else:
            if b == ')' and stack[len(stack) - 1] == '(':
                stack.pop() 
            else:
                stack.append(b)

    if len(stack) > 0:
        answer = False

    print(stack)
    return answer
    # stack에 아무것도 없으면 스택에 괄호 하나 넣고
    # stack에 들어있으면 올바른 괄호인지 check

print(solution('()()'))
print(solution('(())()'))
print(solution(')()('))
print(solution('(()('))
