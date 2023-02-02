def solution(a, b, n):
    answer = 0
    while True:
        if n < a:
            break
        answer += (n // a)*b
        n = n - (n - n % a) + (n // a)*b

    return answer

# solution(2,1,20)
# solution(3,1,20)
solution(5,2,20)

