def solution(d, budget):
    answer = []
    count = 0
    n = len(d)
    for i in range(n):
        answer += [min(d)]
        if sum(answer) > budget:
            break
        d.remove(min(d))
        count += 1
    return count