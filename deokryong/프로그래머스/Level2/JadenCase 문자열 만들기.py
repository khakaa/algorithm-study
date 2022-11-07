def solution(s):
    answer = []
    trans_count = 0
    zero_count = 0

    while s != '1':
        zero_count += s.count('0')
        s = s.replace("0","")
        num = len(s)
        s = bin(num)[2:]
        trans_count += 1
    answer = [trans_count,zero_count]
    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
