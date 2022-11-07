def solution(n):
    for i in range(n):
        if i ** 2 == n:
            return ((i+1)**2)
    return -1

# 위 코드는 테스트 18에서 하나 실패함

def solution(n):
    for i in range(n+1):
        if i ** 2 == n:
            return ((i+1)**2)
    return -1
# n도 포함시켜줘야지 통과