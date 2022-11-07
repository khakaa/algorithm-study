n = int(input())

my_dp = [0] * (n+1)

for i in range(2, n+1):
    my_dp[i] = my_dp[i-1] + 1

    if i % 2 == 0:
        my_dp[i] = min(my_dp[i], my_dp[i // 2] + 1)
    
    if i % 3 == 0:
        my_dp[i] = min(my_dp[i], my_dp[i // 3] + 1)
    
print(my_dp[n])