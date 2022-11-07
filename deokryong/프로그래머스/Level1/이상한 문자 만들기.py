# 이상한 문자 만들기

def solution(s):
    array = s.split(" ")
    answer = ""
    for i in range(len(array)):
        for j in range(len(array[i])):
            if j % 2 == 0:
                answer += array[i][j].upper()
            else:
                answer += array[i][j].lower()
        if i != len(array)-1:
            answer += " "
    return answer