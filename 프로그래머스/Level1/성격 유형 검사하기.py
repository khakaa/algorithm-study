#성격 유형 검사하기

def solution(survey, choices):
    array1 = [['R',0],['C',0],['J',0],['A',0]]
    array2 = [['T',0],['F',0],['M',0],['N',0]]
    answer = ''
    for i in range(len(survey)):
        temp = 0
        for j in range(4):
            if survey[i][0] in array1[j][0] or survey[i][0] in array2[j][0]:
                temp = j
                break
        if survey[i][0] in ['R','C','J','A']:
            if choices[i] == 1 :
                array1[temp][1] += 3
            if choices[i] == 2:
                array1[temp][1] += 2
            if choices[i] == 3:
                array1[temp][1] += 1
            if choices[i] == 4:
                pass
            if choices[i] == 5:
                array2[temp][1] += 1
            if choices[i] == 6:
                array2[temp][1] += 2
            if choices[i] == 7:
                array2[temp][1] += 3
        else:
            if choices[i] == 1 :
                array2[temp][1] += 3
            if choices[i] == 2:
                array2[temp][1] += 2
            if choices[i] == 3:
                array2[temp][1] += 1
            if choices[i] == 4:
                pass
            if choices[i] == 5:
                array1[temp][1] += 1
            if choices[i] == 6:
                array1[temp][1] += 2
            if choices[i] == 7:
                array1[temp][1] += 3

    for i in range(4):
        if array1[i][1] > array2[i][1]:
            answer += array1[i][0]
        elif array1[i][1] == array2[i][1]:
            answer += array1[i][0]
        else:
            answer += array2[i][0]
    return answer