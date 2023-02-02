def solution(citations):
    answer = 0
    citations.sort()
    
    for i in range(10001):
        for j in range(len(citations)):
            if citations[j] >= i:
                if len(citations[j:]) >= i:
                    answer = i
        
    return answer

solution([3, 0, 6, 1, 5])
solution([0,2,4,77,9,11,13,15])
solution([0,0,1,1,2,3,5])

