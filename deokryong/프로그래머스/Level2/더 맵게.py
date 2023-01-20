import heapq
def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    chk = True
    print(scoville)
    while True:
        if len(scoville) == 1 and scoville[0] < K:
            chk = False
            break
        n1 = heapq.heappop(scoville)
        if n1 >= K:
            break
        n2 = heapq.heappop(scoville)
        temp = n1 + (n2 * 2)
        heapq.heappush(scoville,temp)
        answer += 1
        print(scoville)
    if chk == False:
        answer = -1
    print(answer)
    return answer

# solution([1, 2, 3, 9, 10, 12],7)
solution([1, 2, 3, 9, 10, 12],200000)
