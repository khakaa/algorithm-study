def solution(food):
    answer = ''
    for i in range(1,len(food)):
        if food[i] % 2 != 0:
            answer += str(i) * ((food[i]-1)//2)
        else:
            answer += str(i) * (food[i]//2)
    answer += '0'
    answer += answer[len(answer)-2::-1]
    return answer

solution([1, 3, 4, 6])
solution([1, 7, 1, 2])
