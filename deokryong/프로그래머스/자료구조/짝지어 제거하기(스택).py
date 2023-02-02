def solution(s):
    answer = 0
    stack = []
    
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop(-1)
            else:
                stack.append(s[i])
    if stack:
        answer = 0
    else:
        answer = 1
    print(answer)
    return answer

solution('baabaa')
solution('cdcd')
