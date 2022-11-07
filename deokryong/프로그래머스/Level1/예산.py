# 예산

def solution(d, budget):
    answer = 0
    total = 0
    d.sort()
    for i in d:
        if total + i > budget:
            break
        total += i
        answer += 1
        
    return answer