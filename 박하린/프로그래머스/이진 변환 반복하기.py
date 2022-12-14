def solution(s):
    answer = []
    cnt_bin = 0
    cnt_zero = 0

    while s != '1':
        cnt_zero += s.count('0')
        rep_s = s.replace('0','')
        s = bin(len(rep_s))[2:]
        cnt_bin += 1
    
    answer.append(cnt_bin)
    answer.append(cnt_zero)
    
    return answer

print(solution('01110'))
print(solution("1111111"))
print(solution("110010101001"))
print(type(bin(4)))