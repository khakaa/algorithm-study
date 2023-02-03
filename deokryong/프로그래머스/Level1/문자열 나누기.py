def solution(s):
    answer = 0
    while s:
        x_equal = 0
        x_diff = 0
        chk = False
        x = s[0]
        for i in range(len(s)):
            if x == s[i]:
                x_equal += 1
            else:
                x_diff += 1
            if x_equal == x_diff:
                s = s[x_equal*2:]
                answer += 1
                chk = True
                break
        if chk == False:
            answer += 1
            break
    return answer

solution("banana")
solution("abracadabra")
solution("aaabbaccccabba")
