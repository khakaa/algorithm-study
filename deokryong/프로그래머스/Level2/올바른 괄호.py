def solution(s):
    answer = True
    count_1 = 0
    count_2 = 0
    for i in range(len(s)):
        if s[i] == "(":
            count_1 += 1
        else:
            count_2 += 1
            if count_1 < count_2:
                answer = False
                break
    if count_1 != count_2:
        answer = False
    return answer

# 참고 해볼만한 코드 - 스택 + 에러처리를 활용한 방법
# def is_pair(s):
#     st = list()
#     for c in s:
#         if c == '(':
#             st.append(c)

#         if c == ')':
#             try:
#                 st.pop()
#             except IndexError:
#                 return False

#     return len(st) == 0 
