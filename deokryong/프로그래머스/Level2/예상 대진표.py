from collections import deque
def solution(n,a,b):
    answer = 0
    queue = deque()
    for i in range(n):
        queue.append([i+1,i//2+1])

    chk_list = [a,b]
    def win():
        chk = False
        if queue[0][0] in chk_list and queue[1][0] in chk_list:
            chk = True
        elif queue[0][0] in chk_list:
            queue[0][1] = (queue[0][1]-1) // 2 + 1
            queue.append([queue[0][0],queue[0][1]])
            queue.popleft()
            queue.popleft()
        elif queue[1][0] in chk_list:
            queue[1][1] = (queue[1][1]-1) // 2 + 1
            queue.append([queue[1][0],queue[1][1]])
            queue.popleft()
            queue.popleft()
        else:
            queue[0][1] = (queue[0][1]-1) // 2 + 1
            queue.append([queue[0][0],queue[0][1]])
            queue.popleft()
            queue.popleft()
        return chk

    count = 0
    while True:
        chk2 = False
        count += 1
        for j in range(n//2):
            chk3 = win()
            if chk3 == True:
                answer = count
                chk2 = True
                break
        sorted(queue,key=lambda x : x[1])
        n = n//2
        if chk2 == True:
            break
    print(count)
    return answer

solution(8,4,7)