from collections import deque

def solution(people, limit):
    people.sort(reverse=True)
    queue = deque(people)
    count = 0
    while queue:
        if len(queue) == 1:
            count += 1
            break
        heavy_p = queue[0]
        light_p = queue[-1]
        if heavy_p + light_p <= limit:
            queue.popleft()
            queue.pop()
            count += 1
        else:
            queue.popleft()
            count+=1
    print(count)
    return count

solution([70, 50, 80, 50],100)
solution([70, 80, 50],100)