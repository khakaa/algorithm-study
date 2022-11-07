def solution(n):
    answer = [int(i) for i in str(n)]
    answer.sort(reverse=True)
    return answer

# 처음 이렇게 풀었으나 정확성검사 15.3/100 나옴

def solution(n):
    answer = list(str(n))
    answer.reverse()
    
    return list(map(int, answer))

# 다시 작성해서 통과