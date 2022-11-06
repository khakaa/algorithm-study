# 시저 암호
def solution(s, n):
    result = ''
    for i in s:
        if i.isalpha():
            if ord(i) >= 65 and ord(i) <= 90:
                if ord(i) + n > 90:
                    result += chr(64 + ord(i)+n - 90)
                else:
                    result += chr(ord(i) + n)
            elif ord(i) >= 97 and ord(i) <= 122:
                if ord(i) + n > 122:
                    result += chr(96 + ord(i)+n - 122)
                else:
                    result += chr(ord(i) + n)
        else:
            result += i
    return result