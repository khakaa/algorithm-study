def solution(n, m):
    MIN = 0
    MAX = 0
    for i in range(max(n, m), 0, -1):
        if (n % i == 0) & (m % i == 0):
            MAX = i
            break
    for i in range(max(n, m), (n * m) + 1):
        if (i % n == 0) & (i % m == 0):
            MIN = i
            break

    return [MAX, MIN]