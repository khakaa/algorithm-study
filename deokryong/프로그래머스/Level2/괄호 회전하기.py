# 첫번째 방법
from collections import deque
import copy

def solution(s):
    answer = 0
    stack = deque(s)
    rotate = 0                                                                              # 회전 수

    if len(s) % 2 != 0:                                                                     # 문자열 개수가 홀수 일때
        answer = 0
    else:                                                                                   # 문자열 개수가 짝수 일때
        for _ in range(len(s)):                                                             # 문자열 개수만큼 회전
            stack_copy = copy.deepcopy(stack)
            for _ in range(rotate):
                stack_copy.append(stack_copy[0])
                stack_copy.popleft()
            
            rotate += 1
            chk = False                                                                     # 여는 괄호와 닫힌 괄호가 짝을 이루면 chk = True, 짝을 이루지 않으면 chk = False
        
            while stack_copy:   
                chk = False
                for k in range(1,len(stack_copy)):
                    if stack_copy[k] == ')' and stack_copy[k-1] == '(':
                        del stack_copy[k]       
                        del stack_copy[k-1]
                        chk = True
                        break
                    if stack_copy[k] == '}' and stack_copy[k-1] == '{':
                        del stack_copy[k]
                        del stack_copy[k-1]
                        chk = True
                        break
                    if stack_copy[k] == ']' and stack_copy[k-1] == '[':
                        del stack_copy[k]
                        del stack_copy[k-1]
                        chk = True
                        break
                if chk == False:                                                            # 괄호가 짝을 이루지 않아서 for문을 이탈하게 되면 while문 종료 
                    break
            if len(stack_copy) == 0:                                                        # stack_copy 개수가 0이면 올바른 괄호 문자열 이므로
                answer += 1
    return answer

# 두번째 방법

# from collections import deque
# import copy

# def solution(s):
#     answer = 0
#     stack = deque(s)
#     rotate = 0                                                                              # 회전 수

#     for _ in range(len(s)):                                                                 # 문자열 개수만큼 회전
#         stack_copy = copy.deepcopy(stack)
#         for _ in range(rotate):
#             stack_copy.append(stack_copy[0])
#             stack_copy.popleft()
        
#         rotate += 1                                                                         # 회전 수 1 증가
        
#         stack_temp = deque()                                                                # 열린 괄호 '(', '{', '[' 를 담을 stack 생성        
#         chk = True                  
#         for i in range(len(s)):         
#             if stack_copy[i] == '(' or stack_copy[i] == '{' or stack_copy[i] == '[':        # 열린 괄호일 경우 stack_temp에 추가
#                 stack_temp.append(stack_copy[i])
#             elif stack_copy[i] == ')':                                                      # 닫힌 괄호 ')' 일경우
#                 if len(stack_temp) != 0 and stack_temp[-1] == '(':                          # stack_temp에 열린 괄호가 들어있고 stack_temp의 마지막 원소가 '('일 경우 올바른 괄호이므로 stack_temp 마지막 원소 pop
#                     stack_temp.pop()
#                 else:                                                                       # stack_temp에 열린 괄호가 없거나 stack_temp의 크기가 0이 아니지만 열린 괄호가 '('가 아닐 경우 올바른 괄호가 아니므로 반복문 탈출
#                     chk = False
#                     break
#             elif stack_copy[i] == '}':
#                 if len(stack_temp) != 0 and stack_temp[-1] == '{':
#                     stack_temp.pop()
#                 else:
#                     chk = False
#                     break
#             elif stack_copy[i] == ']':
#                 if len(stack_temp) != 0 and stack_temp[-1] == '[':
#                     stack_temp.pop()
#                 else:
#                     chk = False
#                     break
            
#         if chk == True and len(stack_temp) == 0:                                            # chk == True이고 stack_temp의 크기가 0일 경우 전부 올바른 문자열이므로 answer += 1
#             answer += 1
#     return answer

