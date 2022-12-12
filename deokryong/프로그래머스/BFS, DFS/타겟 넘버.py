# BFS 풀이
from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-numbers[0],0])
    while queue:
        temp, level = queue.popleft()
        level += 1
        if level < n:
            queue.append([temp+numbers[level],level])
            queue.append([temp-numbers[level],level])
        else:
            if temp == target:
                answer += 1
    print(answer)
    return answer
solution([1,1,1,1,1],3)