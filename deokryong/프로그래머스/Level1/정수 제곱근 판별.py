# 정수 제곱근 판별
import math
def solution(n):
    answer = 0
    if math.sqrt(n) == math.sqrt(n)//1:
        answer = int(math.pow((math.sqrt(n)+1),2))
    else:
        answer = -1
    return answer