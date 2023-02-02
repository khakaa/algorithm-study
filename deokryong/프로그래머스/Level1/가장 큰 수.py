def solution(numbers):
    
    str_arr = [str(i) for i in numbers]
    str_arr.sort(key=lambda x: (x*3),reverse=True)
    answer = ''.join(str_arr)
    if answer[0] == '0':
        answer = '0'
    print(answer)
    return answer

solution([6, 10, 2])
solution([3, 30, 34, 5,0, 9])
solution([0, 0, 0, 0,0, 0])

solution([3,0, 301, 343, 52, 91]) # 91523433301

