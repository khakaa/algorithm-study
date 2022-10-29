def solution(arr):
    answer = []
    n = -1
    
    for i in range(len(arr)) :
        if n == arr[i] :
            n = arr[i]
        else :
            answer.append(arr[i])
            n = arr[i]
    
    return answer