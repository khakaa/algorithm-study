from itertools import permutations

def solution(k, dungeons):
    answer = -1
    p = permutations(dungeons,len(dungeons))
    p = list(map(list,p))
    
    for i in range(len(p)):
        temp = 0
        temp_k = k
        for j in range(len(dungeons)):
            # print(p[i][j][0])
            if p[i][j][0] <= temp_k:
                temp_k -= p[i][j][1]
                temp += 1
        if temp > answer:
            answer = temp

    print(answer)
    return answer
solution(80,[[80,20],[50,40],[30,10]])
solution(90,[[80,80],[90,10]])
solution(90,[[80,40],[60,10],[10,10]])
solution(90,[[20,20],[20,20],[20,20],[10,10]])


