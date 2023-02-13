def solution(s):
    s_len = len(s)
    answer = 0

    for i in range(s_len):
        if i > 0:
            s = s[1:s_len] + s[0]
        stack = [s[0]]
        # print("s===",s)
        for bracket in s[1:]:
            if len(stack) == 0:
                stack.append(bracket)
                continue

            if bracket == ']' and stack[-1] == '[':
                stack.pop()
            elif bracket == '}' and stack[-1] == '{':
                stack.pop()
            elif bracket == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(bracket)
            # print("bracket===",bracket,"stack===",stack)
        if len(stack) == 0:
            answer += 1

    return answer
                            
print(solution("[()]"))
print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
