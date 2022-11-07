# 문자열을 정수로 바꾸기

def solution(s):
    answer = 0
    if s[0] == '+':
        return int(s[1:])
    elif s[0] == '-':
        return int(s[:])
    else:
        return int(s[:])