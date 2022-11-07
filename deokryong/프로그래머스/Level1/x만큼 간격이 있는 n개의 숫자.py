# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    answer.append(x)
    for i in range(n-1):
        answer.append(answer[i]+x)
    return answer
