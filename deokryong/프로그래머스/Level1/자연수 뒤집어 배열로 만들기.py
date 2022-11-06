# 자연수 뒤집어 배열로 만들기

def solution(n):
    n_str = str(n)
    array = []
    for i in range(len(n_str)):
        array.append(int(n_str[i]))
    array.reverse()
    
    return array