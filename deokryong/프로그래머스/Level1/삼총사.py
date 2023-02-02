def solution(number):
    answer = 0
    for i in range(len(number)-2):
        for j in range(i+1,len(number)-1):
            for k in range(j+1,len(number)):
                if i != j and j != k:
                    temp = number[i] + number[j] + number[k]
                    if temp == 0:
                        # print(f'{number[i]}, {number[j]}, {number[k]}')
                        answer += 1
    print(answer)
    return answer

solution([-2, 3, 0, 2, -5])
solution([-3, -2, -1, 0, 1, 2, 3])
solution([-1, 1, -1, 1])
