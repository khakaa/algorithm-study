def solution(x, n):
    answer = []
    for i in range(n+1):
        if i == 0:
            continue
        if i == 1 :
            answer.append(x)
        else:
            answer.append(x*i)
    return answer