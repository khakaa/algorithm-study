#[1차] 다트 게임
import re
def solution(dartResult):
    answer = 0
    count = dartResult.count('S') + dartResult.count('D') + dartResult.count('T')
    array = [0] * count
    k = 0
    st = ''
    for i in range(len(dartResult)):
        temp = 0
        if dartResult[i] not in ['S','D','T','*','#']:
            st+=dartResult[i]
        elif dartResult[i] in ['S','D','T']:
            temp = int(st)
            if dartResult[i] == 'S':
                array[k] = pow(temp,1)
            elif dartResult[i] == 'D':
                array[k] = pow(temp,2)
            elif dartResult[i] == 'T':
                array[k] = pow(temp,3)
            k+=1
            st = '' 
        elif dartResult[i] in ['*','#']:
            if dartResult[i] == '*':
                array[k-1] *= 2
                array[k-2] *= 2         
            elif dartResult[i] == '#':
                array[k-1] *= -1
    for i in range(len(array)):
        answer += array[i]
        
    return answer

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))


# 스타상* -> 해당 점수와 바로전에 얻은 점수 2배, 첫번째 기회에서 나올수도 있음
# 아차상# -> 해당 점수 마이너스
# Single -> S 1제곱
# Doulbe -> D 2제곱
# Triple -> T 3제곱
