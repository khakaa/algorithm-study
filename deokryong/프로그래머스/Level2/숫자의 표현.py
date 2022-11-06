def solution(n):
    answer = 0
    arr = [i for i in range(1,n+1)]

    start = 0
    end = 0
    sum = 0
    while True:
        if start == len(arr):
            break
        sum += arr[end]
        if sum == n:
            answer+=1
            start+=1
            end=start
            sum=0
        elif sum < n:
            end+=1
            if end==len(arr):
                start+=1
                end=start
                sum=0
        else:
            start+=1
            end = start
            sum=0

    return answer

print(solution(15))
