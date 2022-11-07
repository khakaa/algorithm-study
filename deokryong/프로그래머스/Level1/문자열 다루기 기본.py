# 문자열 다루기 기본

def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i.isdecimal()==False:
                answer = False
            else:
                continue
    else:
        answer = False

    return answer