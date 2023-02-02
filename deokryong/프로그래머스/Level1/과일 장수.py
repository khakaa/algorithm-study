def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score)//m):
        answer += (min(score[(i*m):(i*m+m)]) * m)
    return answer

solution(3,4,[1, 2, 3, 1, 2, 3, 1])
solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])
