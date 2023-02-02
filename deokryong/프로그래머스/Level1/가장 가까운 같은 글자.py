def solution(s):
    answer = []
    for i in range(len(s)):
        temp = 0
        chk = False
        for j in range(len(s[:i])-1,-1,-1):
            temp += 1
            if s[j] == s[i]:
                answer.append(temp)
                chk = True
                break
        if chk == False:
            answer.append(-1)
    return answer

solution("banana")
solution("foobar")
