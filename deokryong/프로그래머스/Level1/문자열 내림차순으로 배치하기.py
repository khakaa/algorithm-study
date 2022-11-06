# 문자열 내림차순으로 배치하기


def solution(s):
    array = [ord(i) for i in s]
    array.sort()
    array.reverse()
    array = list(map(chr,array))
    
    return "".join(array)