def solution(arr1, arr2):
    answer = []
    
    # 1 4    3 3
    # 3 2    3 3
    # 4 1

    # 3,3    3,3
    # 2 3 2  5 4 3
    # 4 2 4  2 4 1
    # 3 1 4  3 1 1

    # 2*5 + 3*2 + 2*3   2*4 + 3*4 + 2*1  2*3 + 3*1 + 2*1

    # 4*4 + 2*4 + 4*1

    # 22 22 11
    # 36 28 18
    # 29 29 14

    for i in range(len(arr1)):
        temp_arr = []
        for j in range(len(arr1[0])):
            temp = 0
            for k in range(len(arr2)):
                temp += arr1[i][j] * arr2[k][j]
            temp_arr.append(temp)
        
        answer.append(temp_arr)
    print(answer)
    return answer
solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]])
solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]])
