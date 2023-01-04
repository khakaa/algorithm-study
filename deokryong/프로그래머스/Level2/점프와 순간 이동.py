def solution(n):
    ans = 0
    while True:
        if n == 0:
            break
        if n % 2 == 0:
            n = n//2
        else:
            n = n - 1
            ans += 1
    print(ans)

    return ans

solution(5)
solution(6)
solution(5000)
