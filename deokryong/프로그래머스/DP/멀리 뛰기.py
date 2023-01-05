def solution(n):
    dp = [0] * 2001
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(3,2001):
        dp[i] = (dp[i-2] + dp[i-1]) % 1234567
    
    print(dp[n])
    answer = dp[n]
    return answer

solution(4)
solution(3)
