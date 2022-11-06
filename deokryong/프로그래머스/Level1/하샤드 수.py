# 하샤드 수

def solution(x):
    total = 0
    x_str = str(x)
    for i in range(len(x_str)):
        total += int(x_str[i])
    if x % total == 0:
        answer = True
    else:
        answer = False
    return answer