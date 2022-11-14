def solution(k, m, score):
    answer = 0
    score.sort()
    for i in range(len(score) // m):
        answer += score[-(i+1)*m]*m
    return answer