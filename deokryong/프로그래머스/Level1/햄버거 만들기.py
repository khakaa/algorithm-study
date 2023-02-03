def solution(ingredient):
    answer = 0
    
    make_list = []
    for i in ingredient:
        make_list.append(i)
        if make_list[-4:] == [1,2,3,1]:
            answer += 1
            for j in range(4):
                make_list.pop()
    return answer

solution([2, 1, 1, 2, 3, 1, 2, 3, 1])
solution([1, 3, 2, 1, 2, 1, 3, 1, 2])
