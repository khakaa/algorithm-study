def solution(s):
    answer = list(s)
    answer.sort(reverse=True)
    result = ''
    for i in answer:
        result += i
    return result