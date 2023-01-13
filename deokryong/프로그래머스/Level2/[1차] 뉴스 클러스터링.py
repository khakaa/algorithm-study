import copy
def solution(str1, str2):
    answer = 0
    str1_arr = [] # str1을 두 글자씩 끊어서 저장할 리스트 
    str2_arr = [] # str2을 두 글자씩 끊어서 저장할 리스트

    # 두 글자씩 끊은 단어가 영문자로만 이루어져 있을 경우 소문자로 변환하여 리스트에 저장
    for i in range(1,len(str1)):
        temp = str1[i-1]+str1[i]
        if temp.isalpha():
            str1_arr.append(temp.lower())

    for i in range(1,len(str2)):
        temp = str2[i-1]+str2[i]
        if temp.isalpha():
            str2_arr.append(temp.lower())

    # 합집합 구하는 과정
    union = []
    str1_arr_copy = copy.deepcopy(str1_arr)
    str2_arr_copy = copy.deepcopy(str2_arr)
    
    for i in range(len(str1_arr_copy)-1,-1,-1):
        if str1_arr_copy[i] in str2_arr_copy:
            temp = str1_arr_copy[i]
            union.append(temp)
            str1_arr_copy.remove(temp)
            str2_arr_copy.remove(temp)
        else:
            temp = str1_arr_copy[i]
            union.append(str1_arr_copy[i])
            str1_arr_copy.remove(temp)
    if len(str2_arr_copy) != 0:
        union.extend(str2_arr_copy)

    # 교집합 구하는 과정
    intersection = []
    str1_arr_copy = copy.deepcopy(str1_arr)
    str2_arr_copy = copy.deepcopy(str2_arr)
    
    for i in range(len(str1_arr_copy)-1,-1,-1):
        if str1_arr_copy[i] in str2_arr_copy:
            temp = str1_arr_copy[i]
            intersection.append(temp)
            str2_arr_copy.remove(temp)
   
    if len(intersection) == 0 and len(union) == 0:      # 교집합과 합집합이 공집합일 경우
        answer = 65536
    else:                                               # 교집합과 합집합이 공집합이 아닐 경우
        answer = int((len(intersection) / len(union) * 65536))
    return answer
solution("FRANCE","french")
solution("handshake","shake hands")
solution("aa1+aa2","AAAA12")
solution("E=M*C^2","e=m*c^2")
