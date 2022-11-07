# 숫자 문자열과 영단어

def solution(s):
    array = [['zero','0'],['one','1'],['two','2'],['three','3'],['four','4'],['five','5'],['six','6'],['seven','7'],['eight','8'],['nine','9']]
    i = 0
    while True:
        if i == 10:
            break
        for i in range(len(array)):
            if array[i][0] in s:
                num_count = s.count(array[i][0])
                s = s.replace(array[i][0],array[i][1],num_count)
                i+=1
            else:
                i+=1
    return int(s)