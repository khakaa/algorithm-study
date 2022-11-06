# 정수 내림차순으로 배치하기

def solution(n):
    answer = ""
    n_str = str(n)
    array = []
    for i in range(len(n_str)):
        array.append(n_str[i])
    
    array.sort()
    array.reverse()
    
    for i in range(len(array)):
        answer += str(array[i])
    return int(answer)
    
    