def solution(n):
    answer = 0
    arr = [0]*100001
    arr[1] = 1
    arr[2] = 1
    i = 3
    while i != len(arr):
        arr[i] = (arr[i-1]+arr[i-2])%1234567
        i+=1
    answer=arr[n]
    return answer

print(solution(3))

print(solution(5))
