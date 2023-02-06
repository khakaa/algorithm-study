def solution(s, skip, index):
    answer = ''
    for i in range(len(s)):
        idx = 0
        temp = ord(s[i])
        while True:
            if idx == index:
                break
            temp += 1
            if temp == 123:
                temp = 97
            idx += 1
            if chr(temp) in skip:
                idx -= 1
                continue
        answer += chr(temp)
    return answer

solution("aukks","wbqd",5)