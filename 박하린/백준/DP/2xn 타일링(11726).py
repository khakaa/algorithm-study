n = int(input())
dp = [0] * (n)

dp[0] = 1

if n > 1:
    dp[1] = 2

    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n-1])

# n = 1 이면 (2,1) 
# n = 2 이면 (2,1)(2,1) (1,2)(1,2)
# n = 3 이면 (1,2)(1,2)(1,2) (2,1)(2,1)(1,2) (1,2)(2,1)(2,1)
# n = 4 (1,2)(1,2)(1,2)(1,2) (1,2)(2,1)(2,1)(1,2) (1,2)(1,2)(2,1)(2,1) (2,1)(2,1)(1,2)(1,2) (2,1)(2,1)(2,1)(2,1)
# ㅣ =