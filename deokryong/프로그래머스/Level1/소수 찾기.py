# 소수 찾기
import math
def solution(n):
    count = 0
    def prime_number(n):
        detect = True
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                detect = False
                break
        return detect
    for i in range(2,n+1):
        if prime_number(i):
            count += 1

    return count