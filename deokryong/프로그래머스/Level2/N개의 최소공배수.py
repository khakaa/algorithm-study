def solution(arr):
    answer = 0
    max_num = max(arr)
    lcm = max_num
    j = 1
    while True:
        chk = True
        for i in range(len(arr)-1):
            if lcm % arr[i] != 0:
                chk = False
                j+=1
                lcm = max_num * j 
                break
        if chk == True:
            break
    answer = lcm
    print(answer)
    return answer

solution([2,6,8,14])
solution([1,2,3])
